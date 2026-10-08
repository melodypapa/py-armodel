"""
Writer/reader round-trip tests for MacSecGlobalKayProps (Table 3.120, p.174).

MacSecGlobalKayProps is an ARElement consumed by ARPackage.element (serialized as
MAC-SEC-GLOBAL-KAY-PROPS). It carries the attributes bypassEtherType (0..255,
PositiveInteger list, container BYPASS-ETHER-TYPES/BYPASS-ETHER-TYPE) and bypassVlan
(0..255, PositiveInteger list, container BYPASS-VLANS/BYPASS-VLAN).

Reader counterpart: tests/test_armodel/parser/test_mac_sec_global_kay_props.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication import MacSecGlobalKayProps
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    AUTOSAR.getInstance().new()
    document = AUTOSAR.getInstance()
    document.setARRelease("R23-11")
    return ARXMLWriter()


@pytest.fixture
def parser():
    AUTOSAR.getInstance().new()
    document = AUTOSAR.getInstance()
    document.setARRelease("R23-11")
    return ARXMLParser()


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


class MockPackage(MockParent):
    def getShortName(self):
        return "Pkg"


def _wrap(element: ET.Element) -> ET.Element:
    inner = ET.tostring(element).decode("utf-8")
    return ET.fromstring(f"<AUTOSAR xmlns='{NS}'>{inner}</AUTOSAR>")


def _pos_int(value):
    p = PositiveInteger()
    p.setValue(str(value))
    return p


def _new_props(short_name="GKP1", ether_types=(88, 90), vlans=(100, 200)):
    props = MacSecGlobalKayProps(MockPackage(), short_name)
    for et in ether_types:
        props.addBypassEtherType(_pos_int(et))
    for v in vlans:
        props.addBypassVlan(_pos_int(v))
    return props


class TestWriteMacSecGlobalKayProps:
    def test_write_all_fields(self, writer):
        props = _new_props()
        parent = ET.Element("ELEMENTS")
        writer.writeMacSecGlobalKayProps(parent, props)

        node = parent.find("MAC-SEC-GLOBAL-KAY-PROPS")
        assert node is not None
        assert node.find("SHORT-NAME").text == "GKP1"
        assert [child.tag for child in node] == ["SHORT-NAME", "BYPASS-ETHER-TYPES", "BYPASS-VLANS"]
        ether_wrapper = node.find("BYPASS-ETHER-TYPES")
        assert ether_wrapper is not None
        assert [int(e.text) for e in ether_wrapper.findall("BYPASS-ETHER-TYPE")] == [88, 90]
        vlan_wrapper = node.find("BYPASS-VLANS")
        assert vlan_wrapper is not None
        assert [int(v.text) for v in vlan_wrapper.findall("BYPASS-VLAN")] == [100, 200]

    def test_write_empty_omits_wrappers(self, writer):
        props = _new_props(ether_types=(), vlans=())
        parent = ET.Element("ELEMENTS")
        writer.writeMacSecGlobalKayProps(parent, props)

        node = parent.find("MAC-SEC-GLOBAL-KAY-PROPS")
        assert node is not None
        assert [child.tag for child in node] == ["SHORT-NAME"]
        assert node.find("BYPASS-ETHER-TYPES") is None
        assert node.find("BYPASS-VLANS") is None


class TestMacSecGlobalKayPropsThroughArPackage:
    def test_ar_package_save_load_round_trip(self):
        """The full ARPackage ELEMENTS path: writeARPackageElement emits the props and the parser dispatch reads it back."""
        document = AUTOSAR.getInstance()
        document.new()
        document.setARRelease("R23-11")
        pkg = document.createARPackage("Sec")
        props = pkg.createMacSecGlobalKayProps("GlobalKayProps")
        props.addBypassEtherType(_pos_int(2048))
        props.addBypassEtherType(_pos_int(34825))
        props.addBypassVlan(_pos_int(1))
        props.addBypassVlan(_pos_int(0))

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            reloaded = AUTOSAR.getInstance()
            reloaded.clear()
            ARXMLParser(options={"warning": True}).load(file_path, reloaded)

            loaded_pkg = reloaded.getARPackages()[0]
            props_list = [e for e in loaded_pkg.getReferrableElements() if isinstance(e, MacSecGlobalKayProps)]
            assert len(props_list) == 1
            recovered = props_list[0]
            assert recovered.getShortName() == "GlobalKayProps"
            assert [v.getValue() for v in recovered.getBypassEtherTypes()] == [2048, 34825]
            assert [v.getValue() for v in recovered.getBypassVlans()] == [1, 0]
        finally:
            os.remove(file_path)

    def test_ar_package_save_load_empty_props(self):
        """An ARElement with empty aggr lists serializes no wrappers and re-parses to empty lists."""
        document = AUTOSAR.getInstance()
        document.new()
        document.setARRelease("R23-11")
        pkg = document.createARPackage("Sec")
        pkg.createMacSecGlobalKayProps("EmptyKayProps")

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            reloaded = AUTOSAR.getInstance()
            reloaded.clear()
            ARXMLParser(options={"warning": True}).load(file_path, reloaded)

            loaded_pkg = reloaded.getARPackages()[0]
            props_list = [e for e in loaded_pkg.getReferrableElements() if isinstance(e, MacSecGlobalKayProps)]
            assert len(props_list) == 1
            recovered = props_list[0]
            assert recovered.getShortName() == "EmptyKayProps"
            assert recovered.getBypassEtherTypes() == []
            assert recovered.getBypassVlans() == []
        finally:
            os.remove(file_path)


class TestMacSecGlobalKayPropsRoundTrip:
    def test_round_trip_preserves_all_values(self, writer, parser, tmp_path):
        props = _new_props()

        parent = ET.Element("ELEMENTS")
        writer.writeMacSecGlobalKayProps(parent, props)

        out_file = str(tmp_path / "mac_sec_global_kay_props.arxml")
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(ET.tostring(_wrap(parent), encoding="unicode"))

        tree = ET.parse(out_file)
        recovered = MacSecGlobalKayProps(MockParent(), "GKP1")
        parser.readMacSecGlobalKayProps(tree.getroot()[0][0], recovered)

        assert recovered.getShortName() == "GKP1"
        assert [e.getValue() for e in recovered.getBypassEtherTypes()] == [88, 90]
        assert [v.getValue() for v in recovered.getBypassVlans()] == [100, 200]

    def test_reader_empty_fields(self, parser):
        element = ET.fromstring("<MAC-SEC-GLOBAL-KAY-PROPS xmlns='%s'><SHORT-NAME>Empty</SHORT-NAME></MAC-SEC-GLOBAL-KAY-PROPS>" % NS)
        recovered = MacSecGlobalKayProps(MockParent(), "Empty")
        parser.readMacSecGlobalKayProps(element, recovered)

        assert recovered.getBypassEtherTypes() == []
        assert recovered.getBypassVlans() == []

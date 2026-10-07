"""
Writer tests for SwitchStreamFilterActionDestPortModification (CP_TPS_SystemTemplate Table 3.93, p.140, R23-11).

Checks the IDENTIFIABLE base level (SHORT-NAME emission), the child element shape and
the XSD sequence order (EGRESS-PORT-REFS, MODIFICATION per group
SWITCH-STREAM-FILTER-ACTION-DEST-PORT-MODIFICATION — the element is emitted in live
documents as the FILTER-ACTION-DEST-PORT-MODIFICATION child of the
SWITCH-STREAM-IDENTIFICATION), the MODIFICATION enum value, the partial-emission case
and the write→parse round-trip.

Round-trip counterpart: tests/test_armodel/parser/test_switch_stream_filter_action_dest_port_modification.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    SwitchStreamFilterActionDestPortModification,
    SwitchStreamFilterActionPortModificationEnum,
    SwitchStreamIdentification,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _ref(value: str) -> RefType:
    ref = RefType()
    ref.setDest("COUPLING-PORT")
    ref.setValue(value)
    return ref


def _enum(member: str) -> SwitchStreamFilterActionPortModificationEnum:
    return SwitchStreamFilterActionPortModificationEnum().setValue(member)


def _full_modification() -> SwitchStreamFilterActionDestPortModification:
    modification = SwitchStreamFilterActionDestPortModification(MockParent(), "DestMod")
    modification.addEgressPortRef(_ref("/AUTOSAR/Switch/Cport2"))
    modification.addEgressPortRef(_ref("/AUTOSAR/Switch/Cport3"))
    modification.setModification(_enum(SwitchStreamFilterActionPortModificationEnum.OVERWRITE))
    return modification


def _write(modification):
    element = ET.Element("SWITCH-STREAM-FILTER-ACTION-DEST-PORT-MODIFICATION")
    ARXMLWriter().writeSwitchStreamFilterActionDestPortModification(element, modification)
    return element


class TestWriteSwitchStreamFilterActionDestPortModification:
    def test_write_identifiable_base_level(self):
        element = _write(SwitchStreamFilterActionDestPortModification(MockParent(), "DestMod"))

        assert element.find("SHORT-NAME").text == "DestMod"

    def test_write_all_children_in_xsd_order(self):
        element = _write(_full_modification())

        assert [child.tag for child in element] == ["SHORT-NAME", "EGRESS-PORT-REFS", "MODIFICATION"]

        egress_port_refs = element.find("EGRESS-PORT-REFS")
        refs = egress_port_refs.findall("EGRESS-PORT-REF")
        assert len(refs) == 2
        assert refs[0].attrib["DEST"] == "COUPLING-PORT"
        assert refs[0].text == "/AUTOSAR/Switch/Cport2"
        assert refs[1].attrib["DEST"] == "COUPLING-PORT"
        assert refs[1].text == "/AUTOSAR/Switch/Cport3"

        assert element.find("MODIFICATION").text == "OVERWRITE"

    def test_write_partial_emission(self):
        modification = SwitchStreamFilterActionDestPortModification(MockParent(), "DestMod")
        modification.setModification(_enum(SwitchStreamFilterActionPortModificationEnum.EXTEND))

        element = _write(modification)

        assert [child.tag for child in element] == ["SHORT-NAME", "MODIFICATION"]
        assert element.find("MODIFICATION").text == "EXTEND"

    def test_write_empty_emits_no_rule_children(self):
        element = _write(SwitchStreamFilterActionDestPortModification(MockParent(), "DestMod"))

        assert [child.tag for child in element] == ["SHORT-NAME"]

    def test_write_dispatch_from_switch_stream_identification(self):
        stream_identification = SwitchStreamIdentification(MockParent(), "Stream1")
        stream_identification.createFilterActionDestPortModification("DestMod")
        modification = stream_identification.getFilterActionDestPortModification()
        modification.addEgressPortRef(_ref("/AUTOSAR/Switch/Cport1"))
        modification.setModification(_enum(SwitchStreamFilterActionPortModificationEnum.EXTEND))

        element = ET.Element("COUPLING-ELEMENT-SWITCH-DETAILS")
        ARXMLWriter().writeSwitchStreamIdentification(element, stream_identification)

        child = element.find("SWITCH-STREAM-IDENTIFICATION/FILTER-ACTION-DEST-PORT-MODIFICATION")
        assert child is not None
        assert [c.tag for c in child] == ["SHORT-NAME", "EGRESS-PORT-REFS", "MODIFICATION"]
        assert child.find("EGRESS-PORT-REFS/EGRESS-PORT-REF").text == "/AUTOSAR/Switch/Cport1"
        assert child.find("MODIFICATION").text == "EXTEND"

    def test_write_and_reparse_round_trip(self):
        element = _write(_full_modification())

        inner = ET.tostring(element).decode("utf-8")
        namespaced = ET.fromstring(inner.replace(element.tag, "%s xmlns='%s'" % (element.tag, NS), 1))

        recovered = SwitchStreamFilterActionDestPortModification(MockParent(), "Initial")
        ARXMLParser(options={"warning": True}).readSwitchStreamFilterActionDestPortModification(namespaced, recovered)

        assert element.find("SHORT-NAME").text == "DestMod"
        egress_port_refs = recovered.getEgressPortRefs()
        assert len(egress_port_refs) == 2
        assert egress_port_refs[0].getValue() == "/AUTOSAR/Switch/Cport2"
        assert egress_port_refs[0].getDest() == "COUPLING-PORT"
        assert egress_port_refs[1].getValue() == "/AUTOSAR/Switch/Cport3"
        assert egress_port_refs[1].getDest() == "COUPLING-PORT"
        assert recovered.getModification() is not None
        assert recovered.getModification().getValue() == SwitchStreamFilterActionPortModificationEnum.OVERWRITE

"""Writer/reader round-trip tests for GlobalTimeCouplingPortProps (Table 9.18, p.875)."""

import xml.etree.cElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    CouplingPortDetails,
    GlobalTimeCouplingPortProps,
)
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
    return ARXMLWriter()


@pytest.fixture
def parser():
    AUTOSAR.getInstance().new()
    return ARXMLParser()


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


def _time_value(text):
    val = TimeValue()
    val.setValue(text)
    return val


def _new_details():
    details = CouplingPortDetails()
    props = GlobalTimeCouplingPortProps()
    props.setPropagationDelay(_time_value("0.005"))
    details.setGlobalTimeProps(props)
    return details


class TestWriteGlobalTimeCouplingPortProps:
    def test_write_all_fields(self, writer):
        parent = ET.Element("PARENT")
        writer.setCouplingPortDetails(parent, "COUPLING-PORT-DETAILS", _new_details())

        node = parent.find("COUPLING-PORT-DETAILS")
        assert node is not None
        props = node.find("GLOBAL-TIME-PROPS")
        assert props is not None
        assert props.find("PROPAGATION-DELAY").text == "0.005"


class TestGlobalTimeCouplingPortPropsRoundTrip:
    def test_round_trip_preserves_all_values(self, writer, parser, tmp_path):
        parent = ET.Element("PARENT")
        writer.setCouplingPortDetails(parent, "COUPLING-PORT-DETAILS", _new_details())

        out_file = str(tmp_path / "global_time_props.arxml")
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(ET.tostring(_wrap(parent), encoding="unicode"))

        tree = ET.parse(out_file)
        parsed = parser.getCouplingPortDetails(tree.getroot()[0], "COUPLING-PORT-DETAILS")
        assert isinstance(parsed, CouplingPortDetails)
        gtp = parsed.getGlobalTimeProps()
        assert isinstance(gtp, GlobalTimeCouplingPortProps)
        assert gtp.getPropagationDelay().getValue() == 0.005

    def test_reader_empty_fields(self, parser):
        element = ET.fromstring("<X xmlns='%s'><COUPLING-PORT-DETAILS></COUPLING-PORT-DETAILS></X>" % NS)
        parsed = parser.getCouplingPortDetails(element, "COUPLING-PORT-DETAILS")
        assert parsed.getGlobalTimeProps() is None


def _wrap(element: ET.Element) -> ET.Element:
    inner = ET.tostring(element).decode("utf-8")
    return ET.fromstring(f"<AUTOSAR xmlns='{NS}'>{inner}</AUTOSAR>")

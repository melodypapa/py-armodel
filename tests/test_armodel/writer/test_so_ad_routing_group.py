"""Writer/reader round-trip tests for SoAdRoutingGroup (R23-11 AUTOSAR_CP_TPS_SystemTemplate, Table F.115, p.2057).

SoAdRoutingGroup is an obsolete Fibex4Ethernet element (atp.Status=obsolete) aggregated by
ARPackage.element; it carries a single 0..1 eventGroupControlType attribute.
"""

import xml.etree.cElementTree as ET

import pytest

from armodel.models import AUTOSAR, SoAdRoutingGroup
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import EventGroupControlTypeEnum
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
    AUTOSAR.getInstance().setARRelease("R23-11")
    return ARXMLWriter()


@pytest.fixture
def parser():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    return ARXMLParser()


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


def _new_group(short_name="RG1"):
    group = SoAdRoutingGroup(MockParent(), short_name)
    control_type = EventGroupControlTypeEnum().setValue(EventGroupControlTypeEnum.ACTIVATION_MULTICAST)
    group.setEventGroupControlType(control_type)
    return group


class TestWriteSoAdRoutingGroup:
    def test_write_all_fields(self, writer):
        parent = ET.Element("PARENT")
        writer.writeSoAdRoutingGroup(parent, _new_group())
        node = parent.find("SO-AD-ROUTING-GROUP")
        assert node is not None
        assert node.find("SHORT-NAME").text == "RG1"
        assert node.find("EVENT-GROUP-CONTROL-TYPE").text == "activationMulticast"

    def test_write_empty_fields_omits_optional_tags(self, writer):
        parent = ET.Element("PARENT")
        writer.writeSoAdRoutingGroup(parent, SoAdRoutingGroup(MockParent(), "Empty"))
        node = parent.find("SO-AD-ROUTING-GROUP")
        assert node is not None
        assert node.find("SHORT-NAME").text == "Empty"
        assert node.find("EVENT-GROUP-CONTROL-TYPE") is None


class TestSoAdRoutingGroupRoundTrip:
    def test_round_trip_preserves_all_values(self, writer, parser):
        parent = ET.Element("PARENT")
        writer.writeSoAdRoutingGroup(parent, _new_group())
        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring("<AUTOSAR xmlns='%s'>%s</AUTOSAR>" % (NS, inner))
        parsed = SoAdRoutingGroup(parent=root, short_name="RG1")
        parser.readSoAdRoutingGroup(root[0][0], parsed)
        assert parsed.getShortName() == "RG1"
        control_type = parsed.getEventGroupControlType()
        assert isinstance(control_type, EventGroupControlTypeEnum)
        assert control_type.getValue() == "activationMulticast"

    def test_reader_empty_fields(self, parser):
        element = ET.fromstring("<SO-AD-ROUTING-GROUP xmlns='%s'><SHORT-NAME>Empty</SHORT-NAME></SO-AD-ROUTING-GROUP>" % NS)
        parsed = SoAdRoutingGroup(parent=MockParent(), short_name="Empty")
        parser.readSoAdRoutingGroup(element, parsed)
        assert parsed.getShortName() == "Empty"
        assert parsed.getEventGroupControlType() is None

    def test_full_document_round_trip_via_ar_package(self, writer, parser, tmp_path):
        document = AUTOSAR.getInstance()
        pkg = document.createARPackage("Ether")
        pkg.createSoAdRoutingGroup("RG1").setEventGroupControlType(EventGroupControlTypeEnum().setValue(EventGroupControlTypeEnum.ACTIVATION_AND_TRIGGER_UNICAST))
        pkg.createSoAdRoutingGroup("RG2")

        path = tmp_path / "soad_routing_group.arxml"
        writer.save(str(path), document)

        AUTOSAR.getInstance().new()
        loaded = AUTOSAR.getInstance()
        parser.load(str(path), loaded)
        loaded_pkg = loaded.getARPackages()[0]

        parsed = loaded_pkg.getElement("RG1", SoAdRoutingGroup)
        assert parsed is not None
        control_type = parsed.getEventGroupControlType()
        assert isinstance(control_type, EventGroupControlTypeEnum)
        assert control_type.getValue() == "activationAndTriggerUnicast"

        empty = loaded_pkg.getElement("RG2", SoAdRoutingGroup)
        assert empty is not None
        assert empty.getEventGroupControlType() is None

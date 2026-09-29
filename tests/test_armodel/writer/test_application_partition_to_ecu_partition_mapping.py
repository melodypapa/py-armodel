"""Writer round-trip tests for ApplicationPartitionToEcuPartitionMapping (Table 5.6, p.201).

Serialized through the APPLICATION-PARTITION-TO-ECU-PARTITION-MAPPINGS wrapper
when aggregated by a SystemMapping (XSD group
APPLICATION-PARTITION-TO-ECU-PARTITION-MAPPING, AUTOSAR_00052.xsd l.3786:
APPLICATION-PARTITION-REFS wrapper, ECU-PARTITION-REF, VARIATION-POINT —
emitted LAST, sequenceOffset=10000).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate import System
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping import ApplicationPartitionToEcuPartitionMapping
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


def _ref(value: str, dest: str) -> RefType:
    ref = RefType()
    ref.setValue(value)
    ref.setDest(dest)
    return ref


def _with_ns(parent: ET.Element) -> ET.Element:
    return ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))


class TestWriteApplicationPartitionToEcuPartitionMapping:
    def test_empty(self):
        mapping = ApplicationPartitionToEcuPartitionMapping(MockParent(), "ApToEpMapping")
        parent = ET.Element("PARENT")
        ARXMLWriter().writeApplicationPartitionToEcuPartitionMapping(parent, mapping)

        node = parent.find("APPLICATION-PARTITION-TO-ECU-PARTITION-MAPPING")
        assert node is not None
        assert node.find("SHORT-NAME").text == "ApToEpMapping"
        assert node.find("APPLICATION-PARTITION-REFS") is None
        assert node.find("ECU-PARTITION-REF") is None
        assert node.find("VARIATION-POINT") is None

    def test_full_element_order(self):
        mapping = ApplicationPartitionToEcuPartitionMapping(MockParent(), "ApToEpMapping")
        mapping.addApplicationPartitionRef(_ref("/ApplicationPartitions/AP1", "APPLICATION-PARTITION"))
        mapping.addApplicationPartitionRef(_ref("/ApplicationPartitions/AP2", "APPLICATION-PARTITION"))
        mapping.setEcuPartitionRef(_ref("/EcuInstances/Ecu1/PARTITIONS/P1", "ECU-PARTITION"))
        parent = ET.Element("PARENT")
        ARXMLWriter().writeApplicationPartitionToEcuPartitionMapping(parent, mapping)

        node = parent.find("APPLICATION-PARTITION-TO-ECU-PARTITION-MAPPING")
        tags = [child.tag for child in node]
        assert tags.index("APPLICATION-PARTITION-REFS") < tags.index("ECU-PARTITION-REF")

        wrapper = node.find("APPLICATION-PARTITION-REFS")
        refs = wrapper.findall("APPLICATION-PARTITION-REF")
        assert len(refs) == 2
        assert refs[0].text == "/ApplicationPartitions/AP1"
        assert refs[0].attrib["DEST"] == "APPLICATION-PARTITION"
        assert refs[1].text == "/ApplicationPartitions/AP2"
        ecu_ref = node.find("ECU-PARTITION-REF")
        assert ecu_ref.text == "/EcuInstances/Ecu1/PARTITIONS/P1"
        assert ecu_ref.attrib["DEST"] == "ECU-PARTITION"

    def test_variation_point_written_last(self):
        system = System(parent=None, short_name="sys")
        system_mapping = system.createSystemMapping("sm")
        mapping = system_mapping.createApplicationPartitionToEcuPartitionMapping("ApToEpMapping")
        mapping.setEcuPartitionRef(_ref("/EcuInstances/Ecu1/PARTITIONS/P1", "ECU-PARTITION"))

        root = ET.fromstring(
            "<ROOT xmlns='%s'>"
            "<APPLICATION-PARTITION-TO-ECU-PARTITION-MAPPING>"
            "<SHORT-NAME>ApToEpMapping</SHORT-NAME>"
            "<VARIATION-POINT><SHORT-LABEL>vp</SHORT-LABEL></VARIATION-POINT>"
            "</APPLICATION-PARTITION-TO-ECU-PARTITION-MAPPING>"
            "</ROOT>" % NS
        )
        ARXMLParser().readApplicationPartitionToEcuPartitionMapping(root[0], mapping)
        assert mapping.getVariationPoint() is not None

        parent = ET.Element("PARENT")
        ARXMLWriter().writeApplicationPartitionToEcuPartitionMapping(parent, mapping)
        node = parent.find("APPLICATION-PARTITION-TO-ECU-PARTITION-MAPPING")
        tags = [child.tag for child in node]
        assert "VARIATION-POINT" in tags
        assert tags.index("VARIATION-POINT") == len(tags) - 1
        assert tags.index("ECU-PARTITION-REF") < tags.index("VARIATION-POINT")

    def test_round_trip_full(self):
        mapping = ApplicationPartitionToEcuPartitionMapping(MockParent(), "ApToEpMapping")
        mapping.addApplicationPartitionRef(_ref("/ApplicationPartitions/AP1", "APPLICATION-PARTITION"))
        mapping.addApplicationPartitionRef(_ref("/ApplicationPartitions/AP2", "APPLICATION-PARTITION"))
        mapping.setEcuPartitionRef(_ref("/EcuInstances/Ecu1/PARTITIONS/P1", "ECU-PARTITION"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeApplicationPartitionToEcuPartitionMapping(parent, mapping)

        reloaded = ApplicationPartitionToEcuPartitionMapping(MockParent(), "ApToEpMapping")
        ARXMLParser().readApplicationPartitionToEcuPartitionMapping(_with_ns(parent)[0], reloaded)

        assert reloaded.getShortName() == "ApToEpMapping"
        refs = reloaded.getApplicationPartitionRefs()
        assert len(refs) == 2
        assert refs[0].getValue() == "/ApplicationPartitions/AP1"
        assert refs[0].getDest() == "APPLICATION-PARTITION"
        assert refs[1].getValue() == "/ApplicationPartitions/AP2"
        assert reloaded.getEcuPartitionRef().getValue() == "/EcuInstances/Ecu1/PARTITIONS/P1"
        assert reloaded.getEcuPartitionRef().getDest() == "ECU-PARTITION"

    def test_round_trip_via_system_mapping(self):
        system = System(parent=None, short_name="sys")
        system_mapping = system.createSystemMapping("sm")
        mapping = system_mapping.createApplicationPartitionToEcuPartitionMapping("ApToEp1")
        mapping.addApplicationPartitionRef(_ref("/ApplicationPartitions/AP1", "APPLICATION-PARTITION"))
        mapping.setEcuPartitionRef(_ref("/EcuInstances/Ecu1/PARTITIONS/P1", "ECU-PARTITION"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeSystemMapping(parent, system_mapping)

        root = _with_ns(parent)
        node = root.find("{%s}SYSTEM-MAPPING" % NS)
        assert node is not None
        wrapper = node.find("{%s}APPLICATION-PARTITION-TO-ECU-PARTITION-MAPPINGS" % NS)
        assert wrapper is not None
        assert len(wrapper.findall("{%s}APPLICATION-PARTITION-TO-ECU-PARTITION-MAPPING" % NS)) == 1

        reloaded_system = System(parent=None, short_name="sys")
        reloaded_mapping = reloaded_system.createSystemMapping("sm")
        ARXMLParser().readSystemMapping(node, reloaded_mapping)
        mappings = reloaded_mapping.getApplicationPartitionToEcuPartitionMappings()
        assert len(mappings) == 1
        assert mappings[0].getShortName() == "ApToEp1"
        assert mappings[0].getApplicationPartitionRefs()[0].getValue() == "/ApplicationPartitions/AP1"
        assert mappings[0].getEcuPartitionRef().getValue() == "/EcuInstances/Ecu1/PARTITIONS/P1"

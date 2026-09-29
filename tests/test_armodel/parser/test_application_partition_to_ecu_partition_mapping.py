"""Parser tests for ApplicationPartitionToEcuPartitionMapping (Table 5.6, p.201).

Identifiable aggregated by SystemMapping.applicationPartitionToEcuPartitionMapping
through the APPLICATION-PARTITION-TO-ECU-PARTITION-MAPPINGS wrapper (XSD group
APPLICATION-PARTITION-TO-ECU-PARTITION-MAPPING, AUTOSAR_00052.xsd l.3786:
APPLICATION-PARTITION-REFS wrapper, ECU-PARTITION-REF, VARIATION-POINT).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping import ApplicationPartitionToEcuPartitionMapping
from armodel.parser.arxml_parser import ARXMLParser

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


def _snip(inner: str) -> ET.Element:
    xml = "<ROOT xmlns='%s'>%s</ROOT>" % (NS, inner)
    return ET.fromstring(xml)


class TestReadApplicationPartitionToEcuPartitionMapping:
    def test_read_full(self):
        mapping = ApplicationPartitionToEcuPartitionMapping(MockParent(), "ApToEpMapping")
        root = _snip(
            "<APPLICATION-PARTITION-TO-ECU-PARTITION-MAPPING>"
            "<SHORT-NAME>ApToEpMapping</SHORT-NAME>"
            "<APPLICATION-PARTITION-REFS>"
            "<APPLICATION-PARTITION-REF DEST='APPLICATION-PARTITION'>/ApplicationPartitions/AP1</APPLICATION-PARTITION-REF>"
            "<APPLICATION-PARTITION-REF DEST='APPLICATION-PARTITION'>/ApplicationPartitions/AP2</APPLICATION-PARTITION-REF>"
            "</APPLICATION-PARTITION-REFS>"
            "<ECU-PARTITION-REF DEST='ECU-PARTITION'>/EcuInstances/Ecu1/PARTITIONS/P1</ECU-PARTITION-REF>"
            "<VARIATION-POINT />"
            "</APPLICATION-PARTITION-TO-ECU-PARTITION-MAPPING>"
        )
        ARXMLParser().readApplicationPartitionToEcuPartitionMapping(root[0], mapping)

        assert mapping.getShortName() == "ApToEpMapping"
        refs = mapping.getApplicationPartitionRefs()
        assert len(refs) == 2
        assert refs[0].getValue() == "/ApplicationPartitions/AP1"
        assert refs[0].getDest() == "APPLICATION-PARTITION"
        assert refs[1].getValue() == "/ApplicationPartitions/AP2"
        assert mapping.getEcuPartitionRef() is not None
        assert mapping.getEcuPartitionRef().getValue() == "/EcuInstances/Ecu1/PARTITIONS/P1"
        assert mapping.getEcuPartitionRef().getDest() == "ECU-PARTITION"
        assert mapping.getVariationPoint() is not None

    def test_read_empty(self):
        mapping = ApplicationPartitionToEcuPartitionMapping(MockParent(), "ApToEpMapping")
        root = _snip("<APPLICATION-PARTITION-TO-ECU-PARTITION-MAPPING>" "<SHORT-NAME>ApToEpMapping</SHORT-NAME>" "</APPLICATION-PARTITION-TO-ECU-PARTITION-MAPPING>")
        ARXMLParser().readApplicationPartitionToEcuPartitionMapping(root[0], mapping)

        assert mapping.getApplicationPartitionRefs() == []
        assert mapping.getEcuPartitionRef() is None
        assert mapping.getVariationPoint() is None

    def test_read_via_system_mapping(self):
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate import System

        system = System(parent=None, short_name="sys")
        system_mapping = system.createSystemMapping("sm")
        root = _snip(
            "<SYSTEM-MAPPING>"
            "<SHORT-NAME>sm</SHORT-NAME>"
            "<APPLICATION-PARTITION-TO-ECU-PARTITION-MAPPINGS>"
            "<APPLICATION-PARTITION-TO-ECU-PARTITION-MAPPING>"
            "<SHORT-NAME>ApToEp1</SHORT-NAME>"
            "<ECU-PARTITION-REF DEST='ECU-PARTITION'>/EcuInstances/Ecu1/PARTITIONS/P1</ECU-PARTITION-REF>"
            "</APPLICATION-PARTITION-TO-ECU-PARTITION-MAPPING>"
            "</APPLICATION-PARTITION-TO-ECU-PARTITION-MAPPINGS>"
            "</SYSTEM-MAPPING>"
        )
        ARXMLParser().readSystemMapping(root[0], system_mapping)

        mappings = system_mapping.getApplicationPartitionToEcuPartitionMappings()
        assert len(mappings) == 1
        assert mappings[0].getShortName() == "ApToEp1"
        assert mappings[0].getEcuPartitionRef().getValue() == "/EcuInstances/Ecu1/PARTITIONS/P1"

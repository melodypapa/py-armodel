"""Writer round-trip tests for SwcToApplicationPartitionMapping (Table 5.4, p.200).

Serialized through the SWC-TO-APPLICATION-PARTITION-MAPPINGS wrapper; child element
order = XSD group SWC-TO-APPLICATION-PARTITION-MAPPING sequence (AUTOSAR_00052.xsd
l.117837): APPLICATION-PARTITION-REF, SW-COMPONENT-PROTOTYPE-IREF, VARIATION-POINT.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate import SystemMapping
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import ComponentInSystemInstanceRef
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteSwcToApplicationPartitionMapping:
    def test_round_trip_via_system_mapping(self):
        """Test write -> re-parse round trip with field values and XSD element order"""
        mapping = SystemMapping(AUTOSAR.getInstance(), "SystemMapping")
        swc_mapping = mapping.createSwcToApplicationPartitionMapping("SwcPartitionMapping")
        partition_ref = RefType()
        partition_ref.setValue("/System/ApplicationPartitions/AP1")
        partition_ref.setDest("APPLICATION-PARTITION")
        swc_mapping.setApplicationPartitionRef(partition_ref)
        iref = ComponentInSystemInstanceRef()
        composition_ref = RefType()
        composition_ref.setValue("/System/Composition")
        composition_ref.setDest("COMPOSITION-SW-COMPONENT-TYPE")
        iref.setContextCompositionRef(composition_ref)
        target_ref = RefType()
        target_ref.setValue("/System/Composition/Swc1")
        target_ref.setDest("SW-COMPONENT-PROTOTYPE")
        iref.setTargetComponentRef(target_ref)
        swc_mapping.setSwComponentPrototypeIRef(iref)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeSystemMapping(parent, mapping)

        node = parent.find("SYSTEM-MAPPING")
        assert node is not None
        wrappers = node.find("SWC-TO-APPLICATION-PARTITION-MAPPINGS")
        assert wrappers is not None
        children = list(wrappers)
        assert len(children) == 1
        swc_node = children[0]
        assert swc_node.tag == "SWC-TO-APPLICATION-PARTITION-MAPPING"
        assert [child.tag for child in swc_node] == ["SHORT-NAME", "APPLICATION-PARTITION-REF", "SW-COMPONENT-PROTOTYPE-IREF"]

        partition_node = swc_node.find("APPLICATION-PARTITION-REF")
        assert partition_node.text == "/System/ApplicationPartitions/AP1"
        assert partition_node.attrib["DEST"] == "APPLICATION-PARTITION"

        xml = ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1)
        root = ET.fromstring(xml)
        reloaded = SystemMapping(AUTOSAR.getInstance(), "SystemMapping")
        ARXMLParser().readSystemMapping(root[0], reloaded)

        reloaded_mappings = reloaded.getSwcToApplicationPartitionMappings()
        assert len(reloaded_mappings) == 1
        round_tripped = reloaded_mappings[0]
        assert round_tripped.getShortName() == "SwcPartitionMapping"
        assert round_tripped.getApplicationPartitionRef().getValue() == "/System/ApplicationPartitions/AP1"
        assert round_tripped.getApplicationPartitionRef().getDest() == "APPLICATION-PARTITION"
        round_tripped_iref = round_tripped.getSwComponentPrototypeIRef()
        assert round_tripped_iref is not None
        assert round_tripped_iref.getContextCompositionRef().getValue() == "/System/Composition"
        assert round_tripped_iref.getTargetComponentRef().getValue() == "/System/Composition/Swc1"
        assert round_tripped_iref.getTargetComponentRef().getDest() == "SW-COMPONENT-PROTOTYPE"

    def test_empty_wrapper_not_emitted(self):
        """Test that a childless SystemMapping emits no SWC-TO-APPLICATION-PARTITION-MAPPINGS wrapper"""
        mapping = SystemMapping(AUTOSAR.getInstance(), "SystemMapping")
        parent = ET.Element("PARENT")
        ARXMLWriter().writeSystemMapping(parent, mapping)

        node = parent.find("SYSTEM-MAPPING")
        assert node is not None
        assert node.find("SWC-TO-APPLICATION-PARTITION-MAPPINGS") is None

    def test_fields_absent_not_emitted(self):
        """Test that unset optional fields emit no elements on a populated mapping"""
        mapping = SystemMapping(AUTOSAR.getInstance(), "SystemMapping")
        mapping.createSwcToApplicationPartitionMapping("BareMapping")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeSystemMapping(parent, mapping)

        swc_node = parent.find("SYSTEM-MAPPING/SWC-TO-APPLICATION-PARTITION-MAPPINGS/SWC-TO-APPLICATION-PARTITION-MAPPING")
        assert swc_node is not None
        assert [child.tag for child in swc_node] == ["SHORT-NAME"]

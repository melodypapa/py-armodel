"""Writer round-trip tests for CpSoftwareClusterToEcuInstanceMapping (Table 5.47, p.283).

Serialized through the CP-SOFTWARE-CLUSTER-TO-ECU-INSTANCE-MAPPING element
(AUTOSAR_00052.xsd l.24765) and the SW-CLUSTER-MAPPINGS wrapper of
SystemMapping (l.119671).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate import System
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster import CpSoftwareClusterToEcuInstanceMapping
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _with_ns(parent: ET.Element) -> ET.Element:
    return ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))


def _ref(value: str, dest: str) -> RefType:
    ref = RefType()
    ref.setValue(value)
    ref.setDest(dest)
    return ref


class TestWriteCpSoftwareClusterToEcuInstanceMapping:
    def test_empty(self):
        mapping = CpSoftwareClusterToEcuInstanceMapping(None, "mapping")
        parent = ET.Element("PARENT")
        ARXMLWriter().writeCpSoftwareClusterToEcuInstanceMapping(parent, mapping)

        node = parent.find("CP-SOFTWARE-CLUSTER-TO-ECU-INSTANCE-MAPPING")
        assert node is not None
        assert node.find("ECU-INSTANCE-REF") is None
        assert node.find("MACHINE-ID") is None
        assert node.find("SW-CLUSTERS") is None

    def test_full(self):
        mapping = CpSoftwareClusterToEcuInstanceMapping(None, "mapping")
        mapping.setEcuInstanceRef(_ref("/EcuInstances/MyEcu", "ECU-INSTANCE"))
        machine_id = PositiveInteger()
        machine_id.setValue(1)
        mapping.setMachineId(machine_id)
        mapping.addSwClusterRef(_ref("/Clusters/MyCluster", "CP-SOFTWARE-CLUSTER"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeCpSoftwareClusterToEcuInstanceMapping(parent, mapping)

        node = parent.find("CP-SOFTWARE-CLUSTER-TO-ECU-INSTANCE-MAPPING")
        assert node.find("ECU-INSTANCE-REF").text == "/EcuInstances/MyEcu"
        assert node.find("ECU-INSTANCE-REF").get("DEST") == "ECU-INSTANCE"
        assert node.find("MACHINE-ID").text == "1"
        sw_clusters = node.find("SW-CLUSTERS")
        conditional = sw_clusters.find("CP-SOFTWARE-CLUSTER-REF-CONDITIONAL")
        assert conditional is not None
        ref = conditional.find("CP-SOFTWARE-CLUSTER-REF")
        assert ref.text == "/Clusters/MyCluster"
        assert ref.get("DEST") == "CP-SOFTWARE-CLUSTER"

    def test_element_order(self):
        mapping = CpSoftwareClusterToEcuInstanceMapping(None, "mapping")
        mapping.setEcuInstanceRef(_ref("/EcuInstances/MyEcu", "ECU-INSTANCE"))
        machine_id = PositiveInteger()
        machine_id.setValue(1)
        mapping.setMachineId(machine_id)
        mapping.addSwClusterRef(_ref("/Clusters/MyCluster", "CP-SOFTWARE-CLUSTER"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeCpSoftwareClusterToEcuInstanceMapping(parent, mapping)

        node = parent.find("CP-SOFTWARE-CLUSTER-TO-ECU-INSTANCE-MAPPING")
        children = [child.tag for child in node]
        assert children[-3:] == ["ECU-INSTANCE-REF", "MACHINE-ID", "SW-CLUSTERS"]

    def test_round_trip_full(self):
        mapping = CpSoftwareClusterToEcuInstanceMapping(None, "mapping")
        mapping.setEcuInstanceRef(_ref("/EcuInstances/MyEcu", "ECU-INSTANCE"))
        machine_id = PositiveInteger()
        machine_id.setValue(1)
        mapping.setMachineId(machine_id)
        mapping.addSwClusterRef(_ref("/Clusters/MyCluster", "CP-SOFTWARE-CLUSTER"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeCpSoftwareClusterToEcuInstanceMapping(parent, mapping)

        reloaded = CpSoftwareClusterToEcuInstanceMapping(None, "mapping")
        ARXMLParser().readCpSoftwareClusterToEcuInstanceMapping(_with_ns(parent)[0], reloaded)

        assert reloaded.getEcuInstanceRef().getValue() == "/EcuInstances/MyEcu"
        assert reloaded.getMachineId().getValue() == 1
        assert len(reloaded.getSwClusterRefs()) == 1
        assert reloaded.getSwClusterRefs()[0].getValue() == "/Clusters/MyCluster"

    def test_round_trip_via_system_mapping(self):
        system = System(parent=None, short_name="sys")
        system_mapping = system.createSystemMapping("sm")
        mapping = CpSoftwareClusterToEcuInstanceMapping(system_mapping, "mapping")
        mapping.setEcuInstanceRef(_ref("/EcuInstances/MyEcu", "ECU-INSTANCE"))
        system_mapping.addSwClusterMapping(mapping)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeSystemMappingSwClusterMappings(parent, system_mapping)

        wrapper = parent.find("SW-CLUSTER-MAPPINGS")
        assert wrapper is not None
        assert wrapper.find("CP-SOFTWARE-CLUSTER-TO-ECU-INSTANCE-MAPPING") is not None

        reloaded_system = System(parent=None, short_name="sys")
        reloaded_mapping = reloaded_system.createSystemMapping("sm")
        ARXMLParser().readSystemMappingSwClusterMappings(_with_ns(parent), reloaded_mapping)
        mappings = reloaded_mapping.getSwClusterMappings()
        assert len(mappings) == 1
        assert isinstance(mappings[0], CpSoftwareClusterToEcuInstanceMapping)
        assert mappings[0].getEcuInstanceRef().getValue() == "/EcuInstances/MyEcu"

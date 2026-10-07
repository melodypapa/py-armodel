"""Writer round-trip tests for EcuResourceEstimation (Table 5.43, p.260).

Serialized through the ECU-RESOURCE-ESTIMATION element (INTRODUCTION,
BSW-RESOURCE-ESTIMATION, ECU-INSTANCE-REF, RTE-RESOURCE-ESTIMATION,
SW-COMP-TO-ECU-MAPPING-REFS) and the RESOURCE-ESTIMATIONS wrapper of
SystemMapping (AUTOSAR_00052.xsd l.119584).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate import System
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping import EcuResourceEstimation
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _ref(value: str, dest: str) -> RefType:
    ref = RefType()
    ref.setValue(value)
    ref.setDest(dest)
    return ref


def _with_ns(parent: ET.Element) -> ET.Element:
    return ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))


class TestWriteEcuResourceEstimation:
    def test_empty(self):
        estimation = EcuResourceEstimation()
        parent = ET.Element("PARENT")
        ARXMLWriter().writeEcuResourceEstimation(parent, estimation)

        node = parent.find("ECU-RESOURCE-ESTIMATION")
        assert node is not None
        assert node.find("INTRODUCTION") is None
        assert node.find("BSW-RESOURCE-ESTIMATION") is None
        assert node.find("ECU-INSTANCE-REF") is None
        assert node.find("RTE-RESOURCE-ESTIMATION") is None
        assert node.find("SW-COMP-TO-ECU-MAPPING-REFS") is None

    def test_full_element_order(self):
        estimation = EcuResourceEstimation()
        estimation.createBswResourceEstimation("BswConsumption")
        estimation.setEcuInstanceRef(_ref("/Ecu/Ecu1", "ECU-INSTANCE"))
        estimation.createRteResourceEstimation("RteConsumption")
        estimation.addSwCompToEcuMappingRef(_ref("/System/Mappings/SwcToEcu1", "SWC-TO-ECU-MAPPING"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeEcuResourceEstimation(parent, estimation)

        node = parent.find("ECU-RESOURCE-ESTIMATION")
        children = [child.tag for child in node]
        assert children == ["BSW-RESOURCE-ESTIMATION", "ECU-INSTANCE-REF", "RTE-RESOURCE-ESTIMATION", "SW-COMP-TO-ECU-MAPPING-REFS"]
        assert node.find("BSW-RESOURCE-ESTIMATION/SHORT-NAME").text == "BswConsumption"
        assert node.find("ECU-INSTANCE-REF").text == "/Ecu/Ecu1"
        assert node.find("ECU-INSTANCE-REF").get("DEST") == "ECU-INSTANCE"
        assert node.find("SW-COMP-TO-ECU-MAPPING-REFS/SW-COMP-TO-ECU-MAPPING-REF").text == "/System/Mappings/SwcToEcu1"

    def test_round_trip_full(self):
        estimation = EcuResourceEstimation()
        estimation.createBswResourceEstimation("BswConsumption")
        estimation.setEcuInstanceRef(_ref("/Ecu/Ecu1", "ECU-INSTANCE"))
        estimation.createRteResourceEstimation("RteConsumption")
        estimation.addSwCompToEcuMappingRef(_ref("/System/Mappings/SwcToEcu1", "SWC-TO-ECU-MAPPING"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeEcuResourceEstimation(parent, estimation)

        reloaded = EcuResourceEstimation()
        ARXMLParser().readEcuResourceEstimation(_with_ns(parent)[0], reloaded)

        assert reloaded.getBswResourceEstimation().getShortName() == "BswConsumption"
        assert reloaded.getEcuInstanceRef().getValue() == "/Ecu/Ecu1"
        assert reloaded.getEcuInstanceRef().getDest() == "ECU-INSTANCE"
        assert reloaded.getRteResourceEstimation().getShortName() == "RteConsumption"
        refs = reloaded.getSwCompToEcuMappingRefs()
        assert len(refs) == 1
        assert refs[0].getValue() == "/System/Mappings/SwcToEcu1"

    def test_round_trip_via_system_mapping(self):
        system = System(parent=None, short_name="sys")
        system_mapping = system.createSystemMapping("sm")
        estimation = EcuResourceEstimation()
        estimation.setEcuInstanceRef(_ref("/Ecu/Ecu1", "ECU-INSTANCE"))
        system_mapping.addResourceEstimation(estimation)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeSystemMappingResourceEstimations(parent, system_mapping)

        wrapper = parent.find("RESOURCE-ESTIMATIONS")
        assert wrapper is not None
        assert wrapper.find("ECU-RESOURCE-ESTIMATION") is not None

        reloaded_system = System(parent=None, short_name="sys")
        reloaded_mapping = reloaded_system.createSystemMapping("sm")
        ARXMLParser().readSystemMappingResourceEstimations(_with_ns(parent), reloaded_mapping)
        estimations = reloaded_mapping.getResourceEstimations()
        assert len(estimations) == 1
        assert estimations[0].getEcuInstanceRef().getValue() == "/Ecu/Ecu1"

    def test_empty_aggregation_no_wrapper(self):
        system = System(parent=None, short_name="sys")
        system_mapping = system.createSystemMapping("sm")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeSystemMappingResourceEstimations(parent, system_mapping)

        assert parent.find("RESOURCE-ESTIMATIONS") is None

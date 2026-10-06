"""Reader tests for EcuResourceEstimation (Table 5.43, p.260).

XML group ECU-RESOURCE-ESTIMATION (AUTOSAR_00052.xsd l.50820):
INTRODUCTION, BSW-RESOURCE-ESTIMATION, ECU-INSTANCE-REF, RTE-RESOURCE-ESTIMATION
and SW-COMP-TO-ECU-MAPPING-REFS wrapper (SW-COMP-TO-ECU-MAPPING-REF items).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate import System
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping import EcuResourceEstimation
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _parse(xml: str) -> ET.Element:
    return ET.fromstring(xml)


class TestReadEcuResourceEstimation:
    def test_read_full(self):
        xml = (
            """
        <ECU-RESOURCE-ESTIMATION xmlns="%s">
            <INTRODUCTION>
                <P>Intro text</P>
            </INTRODUCTION>
            <BSW-RESOURCE-ESTIMATION>
                <SHORT-NAME>BswConsumption</SHORT-NAME>
            </BSW-RESOURCE-ESTIMATION>
            <ECU-INSTANCE-REF DEST="ECU-INSTANCE">/Ecu/Ecu1</ECU-INSTANCE-REF>
            <RTE-RESOURCE-ESTIMATION>
                <SHORT-NAME>RteConsumption</SHORT-NAME>
            </RTE-RESOURCE-ESTIMATION>
            <SW-COMP-TO-ECU-MAPPING-REFS>
                <SW-COMP-TO-ECU-MAPPING-REF DEST="SWC-TO-ECU-MAPPING">/System/Mappings/SwcToEcu1</SW-COMP-TO-ECU-MAPPING-REF>
            </SW-COMP-TO-ECU-MAPPING-REFS>
        </ECU-RESOURCE-ESTIMATION>
        """
            % NS
        )
        element = _parse(xml)
        estimation = EcuResourceEstimation()
        ARXMLParser().readEcuResourceEstimation(element, estimation)

        assert estimation.getIntroduction() is not None
        bsw = estimation.getBswResourceEstimation()
        assert bsw is not None
        assert bsw.getShortName() == "BswConsumption"
        assert estimation.getEcuInstanceRef().getValue() == "/Ecu/Ecu1"
        assert estimation.getEcuInstanceRef().getDest() == "ECU-INSTANCE"
        rte = estimation.getRteResourceEstimation()
        assert rte is not None
        assert rte.getShortName() == "RteConsumption"
        refs = estimation.getSwCompToEcuMappingRefs()
        assert len(refs) == 1
        assert refs[0].getValue() == "/System/Mappings/SwcToEcu1"
        assert refs[0].getDest() == "SWC-TO-ECU-MAPPING"

    def test_read_empty(self):
        xml = '<ECU-RESOURCE-ESTIMATION xmlns="%s"/>' % NS
        element = _parse(xml)
        estimation = EcuResourceEstimation()
        ARXMLParser().readEcuResourceEstimation(element, estimation)

        assert estimation.getBswResourceEstimation() is None
        assert estimation.getEcuInstanceRef() is None
        assert estimation.getIntroduction() is None
        assert estimation.getRteResourceEstimation() is None
        assert estimation.getSwCompToEcuMappingRefs() == []

    def test_read_via_system_mapping(self):
        xml = (
            """
        <PARENT xmlns="%s">
            <RESOURCE-ESTIMATIONS>
                <ECU-RESOURCE-ESTIMATION>
                    <ECU-INSTANCE-REF DEST="ECU-INSTANCE">/Ecu/Ecu1</ECU-INSTANCE-REF>
                </ECU-RESOURCE-ESTIMATION>
            </RESOURCE-ESTIMATIONS>
        </PARENT>
        """
            % NS
        )
        element = _parse(xml)
        system = System(parent=None, short_name="sys")
        mapping = system.createSystemMapping("sm")
        ARXMLParser().readSystemMappingResourceEstimations(element, mapping)

        estimations = mapping.getResourceEstimations()
        assert len(estimations) == 1
        assert isinstance(estimations[0], EcuResourceEstimation)
        assert estimations[0].getEcuInstanceRef().getValue() == "/Ecu/Ecu1"

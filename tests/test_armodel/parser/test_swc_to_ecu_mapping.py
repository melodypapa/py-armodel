"""Parser tests for SwcToEcuMapping (Table 5.2, p.197).

Identifiable aggregated by SystemMapping.swMapping through the SW-MAPPINGS
wrapper (XSD group SWC-TO-ECU-MAPPING, AUTOSAR_00052.xsd l.117895:
COMPONENT-IREFS, CONTROLLED-HW-ELEMENT-REF, ECU-INSTANCE-REF,
[PARTITION-REF removed], PROCESSING-UNIT-REF, VARIATION-POINT).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate import SwcToEcuMapping
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


class TestReadSwcToEcuMapping:
    def test_read_full(self):
        mapping = SwcToEcuMapping(MockParent(), "EcuTestNodeMapping")
        root = _snip(
            "<SWC-TO-ECU-MAPPING>"
            "<SHORT-NAME>EcuTestNodeMapping</SHORT-NAME>"
            "<COMPONENT-IREFS>"
            "<COMPONENT-IREF>"
            "<CONTEXT-COMPOSITION-REF DEST='ROOT-SW-COMPOSITION-PROTOTYPE'>/CanSystem/TopLevelComposition</CONTEXT-COMPOSITION-REF>"
            "<TARGET-COMPONENT-REF DEST='SW-COMPONENT-PROTOTYPE'>/DemoApplication/SWC_ModifyEcho</TARGET-COMPONENT-REF>"
            "</COMPONENT-IREF>"
            "<COMPONENT-IREF>"
            "<TARGET-COMPONENT-REF DEST='SW-COMPONENT-PROTOTYPE'>/DemoApplication/SWC_CyclicCounter</TARGET-COMPONENT-REF>"
            "</COMPONENT-IREF>"
            "</COMPONENT-IREFS>"
            "<CONTROLLED-HW-ELEMENT-REF DEST='HW-ELEMENT'>/HwElements/SensorActuator</CONTROLLED-HW-ELEMENT-REF>"
            "<ECU-INSTANCE-REF DEST='ECU-INSTANCE'>/CanSystem/ECUINSTANCES/EcuTestNode</ECU-INSTANCE-REF>"
            "<PROCESSING-UNIT-REF DEST='HW-ELEMENT'>/HwElements/Core0</PROCESSING-UNIT-REF>"
            "<VARIATION-POINT />"
            "</SWC-TO-ECU-MAPPING>"
        )
        ARXMLParser().readSwcToEcuMapping(root[0], mapping)

        assert mapping.getShortName() == "EcuTestNodeMapping"
        irefs = mapping.getComponentIRefs()
        assert len(irefs) == 2
        assert irefs[0].getContextCompositionRef().getValue() == "/CanSystem/TopLevelComposition"
        assert irefs[0].getContextCompositionRef().getDest() == "ROOT-SW-COMPOSITION-PROTOTYPE"
        assert irefs[0].getTargetComponentRef().getValue() == "/DemoApplication/SWC_ModifyEcho"
        assert irefs[1].getTargetComponentRef().getValue() == "/DemoApplication/SWC_CyclicCounter"
        assert irefs[1].getContextCompositionRef() is None
        assert mapping.getControlledHwElementRef() is not None
        assert mapping.getControlledHwElementRef().getValue() == "/HwElements/SensorActuator"
        assert mapping.getControlledHwElementRef().getDest() == "HW-ELEMENT"
        assert mapping.getEcuInstanceRef().getValue() == "/CanSystem/ECUINSTANCES/EcuTestNode"
        assert mapping.getEcuInstanceRef().getDest() == "ECU-INSTANCE"
        assert mapping.getProcessingUnitRef() is not None
        assert mapping.getProcessingUnitRef().getValue() == "/HwElements/Core0"
        assert mapping.getProcessingUnitRef().getDest() == "HW-ELEMENT"
        assert mapping.getVariationPoint() is not None

    def test_read_empty(self):
        mapping = SwcToEcuMapping(MockParent(), "EcuTestNodeMapping")
        root = _snip("<SWC-TO-ECU-MAPPING>" "<SHORT-NAME>EcuTestNodeMapping</SHORT-NAME>" "</SWC-TO-ECU-MAPPING>")
        ARXMLParser().readSwcToEcuMapping(root[0], mapping)

        assert mapping.getComponentIRefs() == []
        assert mapping.getControlledHwElementRef() is None
        assert mapping.getEcuInstanceRef() is None
        assert mapping.getProcessingUnitRef() is None
        assert mapping.getVariationPoint() is None

    def test_read_removed_partition_ref_not_modeled(self):
        mapping = SwcToEcuMapping(MockParent(), "EcuTestNodeMapping")
        root = _snip(
            "<SWC-TO-ECU-MAPPING>"
            "<SHORT-NAME>EcuTestNodeMapping</SHORT-NAME>"
            "<PARTITION-REF DEST='ECU-PARTITION'>/CanSystem/PARTITIONS/P1</PARTITION-REF>"
            "<ECU-INSTANCE-REF DEST='ECU-INSTANCE'>/CanSystem/ECUINSTANCES/EcuTestNode</ECU-INSTANCE-REF>"
            "</SWC-TO-ECU-MAPPING>"
        )
        ARXMLParser().readSwcToEcuMapping(root[0], mapping)

        assert not hasattr(mapping, "partitionRef")
        assert mapping.getEcuInstanceRef().getValue() == "/CanSystem/ECUINSTANCES/EcuTestNode"

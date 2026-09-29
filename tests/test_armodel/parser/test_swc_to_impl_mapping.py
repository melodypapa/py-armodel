"""Parser tests for SwcToImplMapping (Table 5.3, p.199).

Identifiable aggregated by SystemMapping.swImplMapping through the
SW-IMPL-MAPPINGS wrapper (XSD group SWC-TO-IMPL-MAPPING, AUTOSAR_00052.xsd
l.118071: COMPONENT-IMPLEMENTATION-REF, COMPONENT-IREFS, VARIATION-POINT).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping import SwcToImplMapping
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


class TestReadSwcToImplMapping:
    def test_read_full(self):
        mapping = SwcToImplMapping(MockParent(), "ImplMapping")
        root = _snip(
            "<SWC-TO-IMPL-MAPPING>"
            "<SHORT-NAME>ImplMapping</SHORT-NAME>"
            "<COMPONENT-IMPLEMENTATION-REF DEST='SWC-IMPLEMENTATION'>/SwcTypes/Engine/Impl</COMPONENT-IMPLEMENTATION-REF>"
            "<COMPONENT-IREFS>"
            "<COMPONENT-IREF>"
            "<CONTEXT-COMPOSITION-REF DEST='ROOT-SW-COMPOSITION-PROTOTYPE'>/CanSystem/TopLevelComposition</CONTEXT-COMPOSITION-REF>"
            "<TARGET-COMPONENT-REF DEST='SW-COMPONENT-PROTOTYPE'>/DemoApplication/SWC_ModifyEcho</TARGET-COMPONENT-REF>"
            "</COMPONENT-IREF>"
            "<COMPONENT-IREF>"
            "<TARGET-COMPONENT-REF DEST='SW-COMPONENT-PROTOTYPE'>/DemoApplication/SWC_CyclicCounter</TARGET-COMPONENT-REF>"
            "</COMPONENT-IREF>"
            "</COMPONENT-IREFS>"
            "<VARIATION-POINT />"
            "</SWC-TO-IMPL-MAPPING>"
        )
        ARXMLParser().readSwcToImplMapping(root[0], mapping)

        assert mapping.getShortName() == "ImplMapping"
        assert mapping.getComponentImplementationRef() is not None
        assert mapping.getComponentImplementationRef().getValue() == "/SwcTypes/Engine/Impl"
        assert mapping.getComponentImplementationRef().getDest() == "SWC-IMPLEMENTATION"
        irefs = mapping.getComponentIRefs()
        assert len(irefs) == 2
        assert irefs[0].getContextCompositionRef().getValue() == "/CanSystem/TopLevelComposition"
        assert irefs[0].getContextCompositionRef().getDest() == "ROOT-SW-COMPOSITION-PROTOTYPE"
        assert irefs[0].getTargetComponentRef().getValue() == "/DemoApplication/SWC_ModifyEcho"
        assert irefs[0].getTargetComponentRef().getDest() == "SW-COMPONENT-PROTOTYPE"
        assert irefs[1].getTargetComponentRef().getValue() == "/DemoApplication/SWC_CyclicCounter"
        assert irefs[1].getContextCompositionRef() is None
        assert mapping.getVariationPoint() is not None

    def test_read_empty(self):
        mapping = SwcToImplMapping(MockParent(), "ImplMapping")
        root = _snip("<SWC-TO-IMPL-MAPPING>" "<SHORT-NAME>ImplMapping</SHORT-NAME>" "</SWC-TO-IMPL-MAPPING>")
        ARXMLParser().readSwcToImplMapping(root[0], mapping)

        assert mapping.getComponentImplementationRef() is None
        assert mapping.getComponentIRefs() == []
        assert mapping.getVariationPoint() is None

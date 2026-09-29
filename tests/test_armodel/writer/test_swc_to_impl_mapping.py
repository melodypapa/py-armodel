"""Writer round-trip tests for SwcToImplMapping (Table 5.3, p.199).

Serialized through the SW-IMPL-MAPPINGS wrapper when aggregated by a
SystemMapping (XSD group SWC-TO-IMPL-MAPPING, AUTOSAR_00052.xsd l.118071:
COMPONENT-IMPLEMENTATION-REF, COMPONENT-IREFS, VARIATION-POINT — emitted
LAST, sequenceOffset=10000).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate import System
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import ComponentInSystemInstanceRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping import SwcToImplMapping
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


def _iref(target: str) -> ComponentInSystemInstanceRef:
    iref = ComponentInSystemInstanceRef()
    iref.setTargetComponentRef(_ref(target, "SW-COMPONENT-PROTOTYPE"))
    return iref


def _with_ns(parent: ET.Element) -> ET.Element:
    return ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))


class TestWriteSwcToImplMapping:
    def test_empty(self):
        mapping = SwcToImplMapping(MockParent(), "Map")
        parent = ET.Element("PARENT")
        ARXMLWriter().writeSwcToImplMapping(parent, mapping)

        node = parent.find("SWC-TO-IMPL-MAPPING")
        assert node is not None
        assert node.find("SHORT-NAME").text == "Map"
        assert node.find("COMPONENT-IMPLEMENTATION-REF") is None
        assert node.find("COMPONENT-IREFS") is None
        assert node.find("VARIATION-POINT") is None

    def test_full_element_order(self):
        mapping = SwcToImplMapping(MockParent(), "Map")
        mapping.addComponentIRef(_iref("/DemoApplication/SWC_ModifyEcho"))
        mapping.setComponentImplementationRef(_ref("/SwcTypes/Engine/Impl", "SWC-IMPLEMENTATION"))
        parent = ET.Element("PARENT")
        ARXMLWriter().writeSwcToImplMapping(parent, mapping)

        node = parent.find("SWC-TO-IMPL-MAPPING")
        tags = [child.tag for child in node]
        assert tags.index("COMPONENT-IMPLEMENTATION-REF") < tags.index("COMPONENT-IREFS")

        impl_ref = node.find("COMPONENT-IMPLEMENTATION-REF")
        assert impl_ref.text == "/SwcTypes/Engine/Impl"
        assert impl_ref.attrib["DEST"] == "SWC-IMPLEMENTATION"
        irefs_wrapper = node.find("COMPONENT-IREFS")
        assert len(irefs_wrapper.findall("COMPONENT-IREF")) == 1
        assert irefs_wrapper.find("COMPONENT-IREF/TARGET-COMPONENT-REF").text == "/DemoApplication/SWC_ModifyEcho"

    def test_variation_point_written_last(self):
        system = System(parent=None, short_name="sys")
        system_mapping = system.createSystemMapping("sm")
        mapping = system_mapping.createSwcToImplMapping("Map")
        mapping.setComponentImplementationRef(_ref("/SwcTypes/Engine/Impl", "SWC-IMPLEMENTATION"))

        xml = (
            "<ROOT xmlns='%s'>"
            "<SWC-TO-IMPL-MAPPING>"
            "<SHORT-NAME>Map</SHORT-NAME>"
            "<COMPONENT-IMPLEMENTATION-REF DEST='SWC-IMPLEMENTATION'>/SwcTypes/Engine/Impl</COMPONENT-IMPLEMENTATION-REF>"
            "<VARIATION-POINT><SHORT-LABEL>vp</SHORT-LABEL></VARIATION-POINT>"
            "</SWC-TO-IMPL-MAPPING>"
            "</ROOT>" % NS
        )
        root = ET.fromstring(xml)
        ARXMLParser().readSwcToImplMapping(root[0], mapping)
        assert mapping.getVariationPoint() is not None

        parent = ET.Element("PARENT")
        ARXMLWriter().writeSwcToImplMapping(parent, mapping)
        node = parent.find("SWC-TO-IMPL-MAPPING")
        tags = [child.tag for child in node]
        assert "VARIATION-POINT" in tags
        assert tags.index("VARIATION-POINT") == len(tags) - 1
        assert tags.index("COMPONENT-IMPLEMENTATION-REF") < tags.index("VARIATION-POINT")
        assert node.find("COMPONENT-IREFS") is None

    def test_round_trip_full(self):
        mapping = SwcToImplMapping(MockParent(), "Map")
        iref = _iref("/DemoApplication/SWC_ModifyEcho")
        iref.setContextCompositionRef(_ref("/CanSystem/TopLevelComposition", "ROOT-SW-COMPOSITION-PROTOTYPE"))
        mapping.addComponentIRef(iref)
        mapping.addComponentIRef(_iref("/DemoApplication/SWC_CyclicCounter"))
        mapping.setComponentImplementationRef(_ref("/SwcTypes/Engine/Impl", "SWC-IMPLEMENTATION"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeSwcToImplMapping(parent, mapping)

        reloaded = SwcToImplMapping(MockParent(), "Map")
        ARXMLParser().readSwcToImplMapping(_with_ns(parent)[0], reloaded)

        assert reloaded.getShortName() == "Map"
        assert reloaded.getComponentImplementationRef().getValue() == "/SwcTypes/Engine/Impl"
        assert reloaded.getComponentImplementationRef().getDest() == "SWC-IMPLEMENTATION"
        irefs = reloaded.getComponentIRefs()
        assert len(irefs) == 2
        assert irefs[0].getTargetComponentRef().getValue() == "/DemoApplication/SWC_ModifyEcho"
        assert irefs[0].getContextCompositionRef().getValue() == "/CanSystem/TopLevelComposition"
        assert irefs[1].getTargetComponentRef().getValue() == "/DemoApplication/SWC_CyclicCounter"

    def test_round_trip_via_system_mapping(self):
        system = System(parent=None, short_name="sys")
        system_mapping = system.createSystemMapping("sm")
        mapping = system_mapping.createSwcToImplMapping("ImplMapping")
        mapping.addComponentIRef(_iref("/DemoApplication/SWC_ModifyEcho"))
        mapping.setComponentImplementationRef(_ref("/SwcTypes/Engine/Impl", "SWC-IMPLEMENTATION"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeSystemMappingSwImplMappings(parent, system_mapping)

        wrapper = parent.find("SW-IMPL-MAPPINGS")
        assert wrapper is not None
        assert len(wrapper.findall("SWC-TO-IMPL-MAPPING")) == 1

        reloaded_system = System(parent=None, short_name="sys")
        reloaded_mapping = reloaded_system.createSystemMapping("sm")
        ARXMLParser().readSystemMappingSwImplMappings(_with_ns(parent), reloaded_mapping)
        sw_impl_mappings = reloaded_mapping.getSwImplMappings()
        assert len(sw_impl_mappings) == 1
        assert sw_impl_mappings[0].getShortName() == "ImplMapping"
        assert sw_impl_mappings[0].getComponentImplementationRef().getValue() == "/SwcTypes/Engine/Impl"
        assert sw_impl_mappings[0].getComponentIRefs()[0].getTargetComponentRef().getValue() == "/DemoApplication/SWC_ModifyEcho"

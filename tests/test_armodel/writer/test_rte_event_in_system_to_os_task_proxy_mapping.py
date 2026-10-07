"""Writer round-trip tests for RteEventInSystemToOsTaskProxyMapping (Table 5.20, p.214).

Serialized through the RTE-EVENT-IN-SYSTEM-TO-OS-TASK-PROXY-MAPPING element and the
RTE-EVENT-TO-OS-TASK-PROXY-MAPPINGS wrapper of SystemMapping
(XSD group RTE-EVENT-IN-SYSTEM-TO-OS-TASK-PROXY-MAPPING, AUTOSAR_00052.xsd l.100713:
OFFSET, OS-TASK-PROXY-REF, RTE-EVENT-IREF).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Integer, RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate import System
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import RteEventInSystemInstanceRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.RteEventToOsTaskMapping import RteEventInSystemToOsTaskProxyMapping
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


class TestWriteRteEventInSystemToOsTaskProxyMapping:
    def test_empty(self):
        mapping = RteEventInSystemToOsTaskProxyMapping(MockParent(), "Map")
        parent = ET.Element("PARENT")
        ARXMLWriter().writeRteEventInSystemToOsTaskProxyMapping(parent, mapping)

        node = parent.find("RTE-EVENT-IN-SYSTEM-TO-OS-TASK-PROXY-MAPPING")
        assert node is not None
        assert node.find("SHORT-NAME").text == "Map"
        assert node.find("OFFSET") is None
        assert node.find("OS-TASK-PROXY-REF") is None
        assert node.find("RTE-EVENT-IREF") is None

    def test_full_element_order(self):
        mapping = RteEventInSystemToOsTaskProxyMapping(MockParent(), "Map")
        offset = Integer()
        offset.setValue("2")
        mapping.setOffset(offset)
        mapping.setOsTaskProxyRef(_ref("/OsTaskProxies/TaskProxy2", "OS-TASK-PROXY"))
        iref = RteEventInSystemInstanceRef()
        iref.setContextRootCompositionRef(_ref("/Root", "ROOT-SW-COMPOSITION-PROTOTYPE"))
        iref.addContextSwComponentRef(_ref("/Root/SwcA", "SW-COMPONENT-PROTOTYPE"))
        iref.setTargetRteEventRef(_ref("/Root/SwcA/Ev1", "RTE-EVENT"))
        mapping.setRteEventIRef(iref)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeRteEventInSystemToOsTaskProxyMapping(parent, mapping)

        node = parent.find("RTE-EVENT-IN-SYSTEM-TO-OS-TASK-PROXY-MAPPING")
        tags = [child.tag for child in node]
        assert tags.index("SHORT-NAME") < tags.index("OFFSET") < tags.index("OS-TASK-PROXY-REF") < tags.index("RTE-EVENT-IREF")
        assert node.find("OFFSET").text == "2"
        iref_node = node.find("RTE-EVENT-IREF")
        iref_tags = [child.tag for child in iref_node]
        assert iref_tags.index("CONTEXT-ROOT-COMPOSITION-REF") < iref_tags.index("CONTEXT-SW-COMPONENT-REF") < iref_tags.index("TARGET-RTE-EVENT-REF")

    def test_round_trip_full(self):
        mapping = RteEventInSystemToOsTaskProxyMapping(MockParent(), "Map")
        offset = Integer()
        offset.setValue("2")
        mapping.setOffset(offset)
        mapping.setOsTaskProxyRef(_ref("/OsTaskProxies/TaskProxy2", "OS-TASK-PROXY"))
        iref = RteEventInSystemInstanceRef()
        iref.setContextRootCompositionRef(_ref("/Root", "ROOT-SW-COMPOSITION-PROTOTYPE"))
        iref.addContextSwComponentRef(_ref("/Root/SwcA", "SW-COMPONENT-PROTOTYPE"))
        iref.setTargetRteEventRef(_ref("/Root/SwcA/Ev1", "RTE-EVENT"))
        mapping.setRteEventIRef(iref)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeRteEventInSystemToOsTaskProxyMapping(parent, mapping)

        reloaded = RteEventInSystemToOsTaskProxyMapping(MockParent(), "Map")
        ARXMLParser().readRteEventInSystemToOsTaskProxyMapping(_with_ns(parent)[0], reloaded)

        assert reloaded.getShortName() == "Map"
        assert reloaded.getOffset().getValue() == 2
        assert reloaded.getOsTaskProxyRef().getValue() == "/OsTaskProxies/TaskProxy2"
        reloaded_iref = reloaded.getRteEventIRef()
        assert reloaded_iref is not None
        assert reloaded_iref.getContextRootCompositionRef().getValue() == "/Root"
        assert reloaded_iref.getContextSwComponentRefs()[0].getValue() == "/Root/SwcA"
        assert reloaded_iref.getTargetRteEventRef().getValue() == "/Root/SwcA/Ev1"

    def test_round_trip_via_system_mapping(self):
        system = System(parent=None, short_name="sys")
        system_mapping = system.createSystemMapping("sm")
        mapping = RteEventInSystemToOsTaskProxyMapping(system_mapping, "Map1")
        offset = Integer()
        offset.setValue("5")
        mapping.setOffset(offset)
        mapping.setOsTaskProxyRef(_ref("/OsTaskProxies/TaskProxy2", "OS-TASK-PROXY"))
        system_mapping.addRteEventToOsTaskProxyMapping(mapping)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeSystemMappingRteEventToOsTaskProxyMappings(parent, system_mapping)

        wrapper = parent.find("RTE-EVENT-TO-OS-TASK-PROXY-MAPPINGS")
        assert wrapper is not None
        assert len(wrapper.findall("RTE-EVENT-IN-SYSTEM-TO-OS-TASK-PROXY-MAPPING")) == 1

        reloaded_system = System(parent=None, short_name="sys")
        reloaded_mapping = reloaded_system.createSystemMapping("sm")
        ARXMLParser().readSystemMappingRteEventToOsTaskProxyMappings(_with_ns(parent), reloaded_mapping)
        mappings = reloaded_mapping.getRteEventToOsTaskProxyMappings()
        assert len(mappings) == 1
        assert mappings[0].getShortName() == "Map1"
        assert mappings[0].getOffset().getValue() == 5
        assert mappings[0].getOsTaskProxyRef().getValue() == "/OsTaskProxies/TaskProxy2"

    def test_empty_aggregation_no_wrapper(self):
        system = System(parent=None, short_name="sys")
        system_mapping = system.createSystemMapping("sm")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeSystemMappingRteEventToOsTaskProxyMappings(parent, system_mapping)

        assert parent.find("RTE-EVENT-TO-OS-TASK-PROXY-MAPPINGS") is None

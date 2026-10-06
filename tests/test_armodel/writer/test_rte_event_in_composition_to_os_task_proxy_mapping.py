"""Writer round-trip tests for RteEventInCompositionToOsTaskProxyMapping (Table 5.18, p.212).

Serialized through the RTE-EVENT-IN-COMPOSITION-TO-OS-TASK-PROXY-MAPPING element
(XSD group RTE-EVENT-IN-COMPOSITION-TO-OS-TASK-PROXY-MAPPING, AUTOSAR_00052.xsd l.100501:
OFFSET, OS-TASK-PROXY-REF, RTE-EVENT-IREF). The aggregator SwComponentMappingConstraints
is not yet implemented, so the element-level writer is exercised directly.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import RteEventInCompositionInstanceRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.RteEventToOsTaskMapping import RteEventInCompositionToOsTaskProxyMapping
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


class TestWriteRteEventInCompositionToOsTaskProxyMapping:
    def test_empty(self):
        mapping = RteEventInCompositionToOsTaskProxyMapping(MockParent(), "Map")
        parent = ET.Element("PARENT")
        ARXMLWriter().writeRteEventInCompositionToOsTaskProxyMapping(parent, mapping)

        node = parent.find("RTE-EVENT-IN-COMPOSITION-TO-OS-TASK-PROXY-MAPPING")
        assert node is not None
        assert node.find("SHORT-NAME").text == "Map"
        assert node.find("OFFSET") is None
        assert node.find("OS-TASK-PROXY-REF") is None
        assert node.find("RTE-EVENT-IREF") is None

    def test_full_element_order(self):
        mapping = RteEventInCompositionToOsTaskProxyMapping(MockParent(), "Map")
        offset = PositiveInteger()
        offset.setValue("4")
        mapping.setOffset(offset)
        mapping.setOsTaskProxyRef(_ref("/OsTaskProxies/TaskProxy1", "OS-TASK-PROXY"))
        iref = RteEventInCompositionInstanceRef()
        iref.addContextSwComponentRef(_ref("/Comps/SwcA", "SW-COMPONENT-PROTOTYPE"))
        iref.setTargetRteEventRef(_ref("/Comps/SwcA/Ev1", "RTE-EVENT"))
        mapping.setRteEventIRef(iref)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeRteEventInCompositionToOsTaskProxyMapping(parent, mapping)

        node = parent.find("RTE-EVENT-IN-COMPOSITION-TO-OS-TASK-PROXY-MAPPING")
        tags = [child.tag for child in node]
        assert tags.index("SHORT-NAME") < tags.index("OFFSET") < tags.index("OS-TASK-PROXY-REF") < tags.index("RTE-EVENT-IREF")
        assert node.find("OFFSET").text == "4"
        os_ref = node.find("OS-TASK-PROXY-REF")
        assert os_ref.text == "/OsTaskProxies/TaskProxy1"
        assert os_ref.attrib["DEST"] == "OS-TASK-PROXY"
        iref_node = node.find("RTE-EVENT-IREF")
        assert iref_node.find("TARGET-RTE-EVENT-REF").text == "/Comps/SwcA/Ev1"

    def test_round_trip_full(self):
        mapping = RteEventInCompositionToOsTaskProxyMapping(MockParent(), "Map")
        offset = PositiveInteger()
        offset.setValue("4")
        mapping.setOffset(offset)
        mapping.setOsTaskProxyRef(_ref("/OsTaskProxies/TaskProxy1", "OS-TASK-PROXY"))
        iref = RteEventInCompositionInstanceRef()
        iref.addContextSwComponentRef(_ref("/Comps/SwcA", "SW-COMPONENT-PROTOTYPE"))
        iref.setTargetRteEventRef(_ref("/Comps/SwcA/Ev1", "RTE-EVENT"))
        mapping.setRteEventIRef(iref)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeRteEventInCompositionToOsTaskProxyMapping(parent, mapping)

        reloaded = RteEventInCompositionToOsTaskProxyMapping(MockParent(), "Map")
        ARXMLParser().readRteEventInCompositionToOsTaskProxyMapping(_with_ns(parent)[0], reloaded)

        assert reloaded.getShortName() == "Map"
        assert reloaded.getOffset().getValue() == 4
        assert reloaded.getOsTaskProxyRef().getValue() == "/OsTaskProxies/TaskProxy1"
        assert reloaded.getOsTaskProxyRef().getDest() == "OS-TASK-PROXY"
        reloaded_iref = reloaded.getRteEventIRef()
        assert reloaded_iref is not None
        assert len(reloaded_iref.getContextSwComponentRefs()) == 1
        assert reloaded_iref.getContextSwComponentRefs()[0].getValue() == "/Comps/SwcA"
        assert reloaded_iref.getTargetRteEventRef().getValue() == "/Comps/SwcA/Ev1"
        assert reloaded_iref.getTargetRteEventRef().getDest() == "RTE-EVENT"

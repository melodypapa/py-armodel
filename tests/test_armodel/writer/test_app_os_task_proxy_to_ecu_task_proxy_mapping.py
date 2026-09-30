"""Writer round-trip tests for AppOsTaskProxyToEcuTaskProxyMapping (Table 5.17, p.209).

Serialized through the APP-OS-TASK-PROXY-TO-ECU-TASK-PROXY-MAPPINGS wrapper when
aggregated by a SystemMapping (XSD group APP-OS-TASK-PROXY-TO-ECU-TASK-PROXY-MAPPING,
AUTOSAR_00052.xsd l.2599: APP-TASK-PROXY-REF, ECU-TASK-PROXY-REF, OFFSET —
no VARIATION-POINT, the class is not VariationPointCapable).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Integer, RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate import System
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.RteEventToOsTaskMapping import AppOsTaskProxyToEcuTaskProxyMapping
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


class TestWriteAppOsTaskProxyToEcuTaskProxyMapping:
    def test_empty(self):
        mapping = AppOsTaskProxyToEcuTaskProxyMapping(MockParent(), "Map")
        parent = ET.Element("PARENT")
        ARXMLWriter().writeAppOsTaskProxyToEcuTaskProxyMapping(parent, mapping)

        node = parent.find("APP-OS-TASK-PROXY-TO-ECU-TASK-PROXY-MAPPING")
        assert node is not None
        assert node.find("SHORT-NAME").text == "Map"
        assert node.find("APP-TASK-PROXY-REF") is None
        assert node.find("ECU-TASK-PROXY-REF") is None
        assert node.find("OFFSET") is None
        assert node.find("VARIATION-POINT") is None

    def test_full_element_order(self):
        mapping = AppOsTaskProxyToEcuTaskProxyMapping(MockParent(), "Map")
        mapping.setAppTaskProxyRef(_ref("/SwProxies/AppTaskProxy", "OS-TASK-PROXY"))
        mapping.setEcuTaskProxyRef(_ref("/EcuProxies/EcuTaskProxy", "OS-TASK-PROXY"))
        offset = Integer()
        offset.setValue("3")
        mapping.setOffset(offset)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeAppOsTaskProxyToEcuTaskProxyMapping(parent, mapping)

        node = parent.find("APP-OS-TASK-PROXY-TO-ECU-TASK-PROXY-MAPPING")
        tags = [child.tag for child in node]
        assert tags.index("APP-TASK-PROXY-REF") < tags.index("ECU-TASK-PROXY-REF") < tags.index("OFFSET")

        app_ref = node.find("APP-TASK-PROXY-REF")
        assert app_ref.text == "/SwProxies/AppTaskProxy"
        assert app_ref.attrib["DEST"] == "OS-TASK-PROXY"
        ecu_ref = node.find("ECU-TASK-PROXY-REF")
        assert ecu_ref.text == "/EcuProxies/EcuTaskProxy"
        assert ecu_ref.attrib["DEST"] == "OS-TASK-PROXY"
        assert node.find("OFFSET").text == "3"

    def test_round_trip_full(self):
        mapping = AppOsTaskProxyToEcuTaskProxyMapping(MockParent(), "Map")
        mapping.setAppTaskProxyRef(_ref("/SwProxies/AppTaskProxy", "OS-TASK-PROXY"))
        mapping.setEcuTaskProxyRef(_ref("/EcuProxies/EcuTaskProxy", "OS-TASK-PROXY"))
        offset = Integer()
        offset.setValue("3")
        mapping.setOffset(offset)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeAppOsTaskProxyToEcuTaskProxyMapping(parent, mapping)

        reloaded = AppOsTaskProxyToEcuTaskProxyMapping(MockParent(), "Map")
        ARXMLParser().readAppOsTaskProxyToEcuTaskProxyMapping(_with_ns(parent)[0], reloaded)

        assert reloaded.getShortName() == "Map"
        assert reloaded.getAppTaskProxyRef().getValue() == "/SwProxies/AppTaskProxy"
        assert reloaded.getAppTaskProxyRef().getDest() == "OS-TASK-PROXY"
        assert reloaded.getEcuTaskProxyRef().getValue() == "/EcuProxies/EcuTaskProxy"
        assert reloaded.getEcuTaskProxyRef().getDest() == "OS-TASK-PROXY"
        assert reloaded.getOffset().getValue() == 3

    def test_round_trip_via_system_mapping(self):
        system = System(parent=None, short_name="sys")
        system_mapping = system.createSystemMapping("sm")
        mapping = system_mapping.createAppOsTaskProxyToEcuTaskProxyMapping("Map1")
        mapping.setAppTaskProxyRef(_ref("/SwProxies/AppTaskProxy", "OS-TASK-PROXY"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeSystemMappingAppOsTaskProxyToEcuTaskProxyMappings(parent, system_mapping)

        wrapper = parent.find("APP-OS-TASK-PROXY-TO-ECU-TASK-PROXY-MAPPINGS")
        assert wrapper is not None
        assert len(wrapper.findall("APP-OS-TASK-PROXY-TO-ECU-TASK-PROXY-MAPPING")) == 1

        reloaded_system = System(parent=None, short_name="sys")
        reloaded_mapping = reloaded_system.createSystemMapping("sm")
        ARXMLParser().readSystemMappingAppOsTaskProxyToEcuTaskProxyMappings(_with_ns(parent), reloaded_mapping)
        mappings = reloaded_mapping.getAppOsTaskProxyToEcuTaskProxyMappings()
        assert len(mappings) == 1
        assert mappings[0].getShortName() == "Map1"
        assert mappings[0].getAppTaskProxyRef().getValue() == "/SwProxies/AppTaskProxy"

    def test_empty_aggregation_no_wrapper(self):
        system = System(parent=None, short_name="sys")
        system_mapping = system.createSystemMapping("sm")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeSystemMappingAppOsTaskProxyToEcuTaskProxyMappings(parent, system_mapping)

        assert parent.find("APP-OS-TASK-PROXY-TO-ECU-TASK-PROXY-MAPPINGS") is None

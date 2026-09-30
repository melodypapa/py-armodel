"""Parser tests for AppOsTaskProxyToEcuTaskProxyMapping (Table 5.17, p.209).

Identifiable aggregated by SystemMapping.appOsTaskProxyToEcuTaskProxyMapping through the
APP-OS-TASK-PROXY-TO-ECU-TASK-PROXY-MAPPINGS wrapper (XSD group
APP-OS-TASK-PROXY-TO-ECU-TASK-PROXY-MAPPING, AUTOSAR_00052.xsd l.2599:
APP-TASK-PROXY-REF, ECU-TASK-PROXY-REF, OFFSET — no VARIATION-POINT).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.RteEventToOsTaskMapping import AppOsTaskProxyToEcuTaskProxyMapping
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


class TestReadAppOsTaskProxyToEcuTaskProxyMapping:
    def test_read_full(self):
        mapping = AppOsTaskProxyToEcuTaskProxyMapping(MockParent(), "AppEcuMapping")
        root = _snip(
            "<APP-OS-TASK-PROXY-TO-ECU-TASK-PROXY-MAPPING>"
            "<SHORT-NAME>AppEcuMapping</SHORT-NAME>"
            "<APP-TASK-PROXY-REF DEST='OS-TASK-PROXY'>/SwProxies/AppTaskProxy</APP-TASK-PROXY-REF>"
            "<ECU-TASK-PROXY-REF DEST='OS-TASK-PROXY'>/EcuProxies/EcuTaskProxy</ECU-TASK-PROXY-REF>"
            "<OFFSET>3</OFFSET>"
            "</APP-OS-TASK-PROXY-TO-ECU-TASK-PROXY-MAPPING>"
        )
        ARXMLParser().readAppOsTaskProxyToEcuTaskProxyMapping(root[0], mapping)

        assert mapping.getShortName() == "AppEcuMapping"
        assert mapping.getAppTaskProxyRef() is not None
        assert mapping.getAppTaskProxyRef().getValue() == "/SwProxies/AppTaskProxy"
        assert mapping.getAppTaskProxyRef().getDest() == "OS-TASK-PROXY"
        assert mapping.getEcuTaskProxyRef() is not None
        assert mapping.getEcuTaskProxyRef().getValue() == "/EcuProxies/EcuTaskProxy"
        assert mapping.getEcuTaskProxyRef().getDest() == "OS-TASK-PROXY"
        assert mapping.getOffset() is not None
        assert mapping.getOffset().getValue() == 3

    def test_read_empty(self):
        mapping = AppOsTaskProxyToEcuTaskProxyMapping(MockParent(), "AppEcuMapping")
        root = _snip("<APP-OS-TASK-PROXY-TO-ECU-TASK-PROXY-MAPPING>" "<SHORT-NAME>AppEcuMapping</SHORT-NAME>" "</APP-OS-TASK-PROXY-TO-ECU-TASK-PROXY-MAPPING>")
        ARXMLParser().readAppOsTaskProxyToEcuTaskProxyMapping(root[0], mapping)

        assert mapping.getAppTaskProxyRef() is None
        assert mapping.getEcuTaskProxyRef() is None
        assert mapping.getOffset() is None

    def test_read_via_system_mapping_wrapper(self):
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate import System

        system = System(parent=None, short_name="sys")
        system_mapping = system.createSystemMapping("sm")
        root = _snip(
            "<APP-OS-TASK-PROXY-TO-ECU-TASK-PROXY-MAPPINGS>"
            "<APP-OS-TASK-PROXY-TO-ECU-TASK-PROXY-MAPPING>"
            "<SHORT-NAME>Map1</SHORT-NAME>"
            "<APP-TASK-PROXY-REF DEST='OS-TASK-PROXY'>/SwProxies/AppTaskProxy</APP-TASK-PROXY-REF>"
            "</APP-OS-TASK-PROXY-TO-ECU-TASK-PROXY-MAPPING>"
            "</APP-OS-TASK-PROXY-TO-ECU-TASK-PROXY-MAPPINGS>"
        )
        ARXMLParser().readSystemMappingAppOsTaskProxyToEcuTaskProxyMappings(root, system_mapping)

        mappings = system_mapping.getAppOsTaskProxyToEcuTaskProxyMappings()
        assert len(mappings) == 1
        assert mappings[0].getShortName() == "Map1"
        assert mappings[0].getAppTaskProxyRef().getValue() == "/SwProxies/AppTaskProxy"

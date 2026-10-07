"""Writer round-trip tests for TriggerToSignalMapping (Table 5.35, p.250) and
TriggerInSystemInstanceRef (Table B.4, p.1005).

Serialized through the TRIGGER-TO-SIGNAL-MAPPING element
(AUTOSAR_00052.xsd l.126726) and the DATA-MAPPINGS wrapper of SystemMapping.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate import System
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping import TriggerToSignalMapping
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import TriggerInSystemInstanceRef
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


class TestWriteTriggerToSignalMapping:
    def test_empty(self):
        mapping = TriggerToSignalMapping()
        parent = ET.Element("PARENT")
        ARXMLWriter().writeTriggerToSignalMapping(parent, mapping)

        node = parent.find("TRIGGER-TO-SIGNAL-MAPPING")
        assert node is not None
        assert node.find("TRIGGER-IREF") is None
        assert node.find("SYSTEM-SIGNAL-REF") is None

    def test_full(self):
        mapping = TriggerToSignalMapping()
        iref = TriggerInSystemInstanceRef()
        iref.setContextCompositionRef(_ref("/Root", "ROOT-SW-COMPOSITION-PROTOTYPE"))
        iref.setContextPortRef(_ref("/Root/SwcA/TriggerPort", "PORT-PROTOTYPE"))
        iref.setTargetTriggerRef(_ref("/Root/SwcA/T1", "TRIGGER"))
        mapping.setTriggerIRef(iref)
        mapping.setSystemSignalRef(_ref("/System/TrigSignal", "SYSTEM-SIGNAL"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeTriggerToSignalMapping(parent, mapping)

        node = parent.find("TRIGGER-TO-SIGNAL-MAPPING")
        assert node.find("TRIGGER-IREF/TARGET-TRIGGER-REF").text == "/Root/SwcA/T1"
        assert node.find("TRIGGER-IREF/TARGET-TRIGGER-REF").get("DEST") == "TRIGGER"
        assert node.find("SYSTEM-SIGNAL-REF").text == "/System/TrigSignal"

    def test_round_trip_full(self):
        mapping = TriggerToSignalMapping()
        iref = TriggerInSystemInstanceRef()
        iref.setBaseRef(_ref("/Root", "ROOT-SW-COMPOSITION-PROTOTYPE"))
        iref.addContextComponentRef(_ref("/Root/SwcA", "SW-COMPONENT-PROTOTYPE"))
        iref.setContextCompositionRef(_ref("/Root", "ROOT-SW-COMPOSITION-PROTOTYPE"))
        iref.setContextPortRef(_ref("/Root/SwcA/TriggerPort", "PORT-PROTOTYPE"))
        iref.setTargetTriggerRef(_ref("/Root/SwcA/T1", "TRIGGER"))
        mapping.setTriggerIRef(iref)
        mapping.setSystemSignalRef(_ref("/System/TrigSignal", "SYSTEM-SIGNAL"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeTriggerToSignalMapping(parent, mapping)

        reloaded = TriggerToSignalMapping()
        ARXMLParser().readTriggerToSignalMapping(_with_ns(parent)[0], reloaded)

        r_iref = reloaded.getTriggerIRef()
        assert r_iref is not None
        assert r_iref.getBaseRef().getValue() == "/Root"
        assert [ref.getValue() for ref in r_iref.getContextComponentRefs()] == ["/Root/SwcA"]
        assert r_iref.getContextCompositionRef().getValue() == "/Root"
        assert r_iref.getContextPortRef().getValue() == "/Root/SwcA/TriggerPort"
        assert r_iref.getTargetTriggerRef().getValue() == "/Root/SwcA/T1"
        assert r_iref.getTargetTriggerRef().getDest() == "TRIGGER"
        assert reloaded.getSystemSignalRef().getValue() == "/System/TrigSignal"

    def test_round_trip_via_system_mapping(self):
        system = System(parent=None, short_name="sys")
        system_mapping = system.createSystemMapping("sm")
        mapping = TriggerToSignalMapping()
        mapping.setSystemSignalRef(_ref("/System/TrigSignal", "SYSTEM-SIGNAL"))
        system_mapping.addDataMapping(mapping)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeSystemMappingDataMappings(parent, system_mapping)

        wrapper = parent.find("DATA-MAPPINGS")
        assert wrapper is not None
        assert wrapper.find("TRIGGER-TO-SIGNAL-MAPPING") is not None

        reloaded_system = System(parent=None, short_name="sys")
        reloaded_mapping = reloaded_system.createSystemMapping("sm")
        ARXMLParser().readSystemMappingDataMappings(_with_ns(parent), reloaded_mapping)
        data_mappings = reloaded_mapping.getDataMappings()
        assert len(data_mappings) == 1
        assert isinstance(data_mappings[0], TriggerToSignalMapping)
        assert data_mappings[0].getSystemSignalRef().getValue() == "/System/TrigSignal"

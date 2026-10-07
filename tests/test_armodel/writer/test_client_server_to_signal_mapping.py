"""Writer round-trip tests for ClientServerToSignalMapping (Table 5.33, p.242).

Element order per XSD group CLIENT-SERVER-TO-SIGNAL-MAPPING: CALL-SIGNAL-REF,
CLIENT-SERVER-OPERATION-IREF, RETURN-SIGNAL-REF (LENGTH-CLIENT-ID,
LENGTH-SEQUENCE-COUNTER and SERIALIZER-REF are atp.Status="removed" and not
modeled). Dispatched from SystemMapping DATA-MAPPINGS.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate import System
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping import ClientServerToSignalMapping
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import OperationInSystemInstanceRef
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _ref(value, dest):
    ref = RefType()
    ref.setValue(value)
    ref.setDest(dest)
    return ref


def _new_mapping():
    mapping = ClientServerToSignalMapping()
    mapping.setCallSignalRef(_ref("/System/CallSignal", "SYSTEM-SIGNAL"))
    iref = OperationInSystemInstanceRef()
    iref.setContextCompositionRef(_ref("/Root", "ROOT-SW-COMPOSITION-PROTOTYPE"))
    iref.addContextComponentRef(_ref("/Root/SwcA", "SW-COMPOSITION-PROTOTYPE"))
    iref.setContextPortRef(_ref("/Root/SwcA/CSPort", "P-PORT-PROTOTYPE"))
    iref.setTargetOperationRef(_ref("/Root/SwcA/CSPort/Op", "CLIENT-SERVER-OPERATION"))
    mapping.setClientServerOperationIRef(iref)
    mapping.setReturnSignalRef(_ref("/System/ReturnSignal", "SYSTEM-SIGNAL"))
    return mapping


def _write_direct(mapping):
    parent = ET.Element("PARENT")
    ARXMLWriter().writeClientServerToSignalMapping(parent, mapping)
    return parent.find("CLIENT-SERVER-TO-SIGNAL-MAPPING")


def _write_via_system_mapping(mapping):
    system = System(parent=None, short_name="sys")
    system_mapping = system.createSystemMapping("sm")
    system_mapping.addDataMapping(mapping)
    parent = ET.Element("PARENT")
    ARXMLWriter().writeSystemMappingDataMappings(parent, system_mapping)
    return parent.find("DATA-MAPPINGS/CLIENT-SERVER-TO-SIGNAL-MAPPING")


class TestWriteClientServerToSignalMapping:
    def test_write_content_in_xsd_order(self):
        element = _write_direct(_new_mapping())
        assert element is not None

        children = [child.tag for child in element]
        assert children == ["CALL-SIGNAL-REF", "CLIENT-SERVER-OPERATION-IREF", "RETURN-SIGNAL-REF"]
        assert element.find("CALL-SIGNAL-REF").text == "/System/CallSignal"
        assert element.find("CALL-SIGNAL-REF").get("DEST") == "SYSTEM-SIGNAL"
        assert element.find("CLIENT-SERVER-OPERATION-IREF/CONTEXT-COMPOSITION-REF").text == "/Root"
        assert element.find("CLIENT-SERVER-OPERATION-IREF/CONTEXT-COMPONENT-REF").text == "/Root/SwcA"
        assert element.find("CLIENT-SERVER-OPERATION-IREF/CONTEXT-PORT-REF").text == "/Root/SwcA/CSPort"
        assert element.find("CLIENT-SERVER-OPERATION-IREF/TARGET-OPERATION-REF").text == "/Root/SwcA/CSPort/Op"
        assert element.find("RETURN-SIGNAL-REF").text == "/System/ReturnSignal"
        assert element.find("RETURN-SIGNAL-REF").get("DEST") == "SYSTEM-SIGNAL"

    def test_write_via_system_mapping(self):
        element = _write_via_system_mapping(_new_mapping())
        assert element is not None
        assert element.find("CALL-SIGNAL-REF").text == "/System/CallSignal"

    def test_round_trip_full(self):
        element = _write_direct(_new_mapping())
        reparsed = ET.fromstring(ET.tostring(element).decode("utf-8").replace("<CLIENT-SERVER-TO-SIGNAL-MAPPING>", "<CLIENT-SERVER-TO-SIGNAL-MAPPING xmlns='%s'>" % NS, 1))
        reloaded = ClientServerToSignalMapping()
        ARXMLParser().readClientServerToSignalMapping(reparsed, reloaded)

        assert reloaded.getCallSignalRef().getValue() == "/System/CallSignal"
        iref = reloaded.getClientServerOperationIRef()
        assert iref is not None
        assert iref.getContextCompositionRef().getValue() == "/Root"
        assert iref.getContextComponentRefs()[0].getValue() == "/Root/SwcA"
        assert iref.getContextPortRef().getValue() == "/Root/SwcA/CSPort"
        assert iref.getTargetOperationRef().getValue() == "/Root/SwcA/CSPort/Op"
        assert reloaded.getReturnSignalRef().getValue() == "/System/ReturnSignal"

    def test_round_trip_empty(self):
        element = _write_direct(ClientServerToSignalMapping())
        assert len(list(element)) == 0

        reparsed = ET.fromstring(ET.tostring(element).decode("utf-8").replace("<CLIENT-SERVER-TO-SIGNAL-MAPPING>", "<CLIENT-SERVER-TO-SIGNAL-MAPPING xmlns='%s'>" % NS, 1))
        reloaded = ClientServerToSignalMapping()
        ARXMLParser().readClientServerToSignalMapping(reparsed, reloaded)
        assert reloaded.getCallSignalRef() is None
        assert reloaded.getClientServerOperationIRef() is None
        assert reloaded.getReturnSignalRef() is None

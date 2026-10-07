"""Writer round-trip tests for SenderReceiverCompositeElementToSignalMapping
(Table 5.34, p.247).

Element order per XSD group SENDER-RECEIVER-COMPOSITE-ELEMENT-TO-SIGNAL-MAPPING:
DATA-ELEMENT-IREF, SYSTEM-SIGNAL-REF, TYPE-MAPPING. Dispatched from SystemMapping
DATA-MAPPINGS.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping import (
    SenderReceiverCompositeElementToSignalMapping,
    SenderRecRecordTypeMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import VariableDataPrototypeInSystemInstanceRef
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
    mapping = SenderReceiverCompositeElementToSignalMapping()
    iref = VariableDataPrototypeInSystemInstanceRef()
    iref.setContextCompositionRef(_ref("/Root", "ROOT-SW-COMPOSITION-PROTOTYPE"))
    iref.setContextPortRef(_ref("/Root/SwcA/DataPort", "R-PORT-PROTOTYPE"))
    iref.setTargetDataPrototypeRef(_ref("/Root/SwcA/DataPort/Elem", "VARIABLE-DATA-PROTOTYPE"))
    mapping.setDataElementIRef(iref)
    mapping.setSystemSignalRef(_ref("/System/Signal", "SYSTEM-SIGNAL"))
    mapping.setTypeMapping(SenderRecRecordTypeMapping())
    return mapping


def _write_direct(mapping):
    parent = ET.Element("PARENT")
    ARXMLWriter().writeSenderReceiverCompositeElementToSignalMapping(parent, mapping)
    return parent.find("SENDER-RECEIVER-COMPOSITE-ELEMENT-TO-SIGNAL-MAPPING")


class TestWriteSenderReceiverCompositeElementToSignalMapping:
    def test_write_content_in_xsd_order(self):
        element = _write_direct(_new_mapping())
        assert element is not None

        children = [child.tag for child in element]
        assert children == ["DATA-ELEMENT-IREF", "SYSTEM-SIGNAL-REF", "TYPE-MAPPING"]
        assert element.find("DATA-ELEMENT-IREF/CONTEXT-COMPOSITION-REF").text == "/Root"
        assert element.find("DATA-ELEMENT-IREF/CONTEXT-PORT-REF").text == "/Root/SwcA/DataPort"
        assert element.find("DATA-ELEMENT-IREF/TARGET-DATA-PROTOTYPE-REF").text == "/Root/SwcA/DataPort/Elem"
        assert element.find("SYSTEM-SIGNAL-REF").text == "/System/Signal"
        assert element.find("SYSTEM-SIGNAL-REF").get("DEST") == "SYSTEM-SIGNAL"
        assert element.find("TYPE-MAPPING/SENDER-REC-RECORD-TYPE-MAPPING") is not None

    def test_round_trip_full(self):
        element = _write_direct(_new_mapping())
        reparsed = ET.fromstring(
            ET.tostring(element).decode("utf-8").replace("<SENDER-RECEIVER-COMPOSITE-ELEMENT-TO-SIGNAL-MAPPING>", "<SENDER-RECEIVER-COMPOSITE-ELEMENT-TO-SIGNAL-MAPPING xmlns='%s'>" % NS, 1)
        )
        reloaded = SenderReceiverCompositeElementToSignalMapping()
        ARXMLParser().readSenderReceiverCompositeElementToSignalMapping(reparsed, reloaded)

        iref = reloaded.getDataElementIRef()
        assert iref is not None
        assert iref.getContextCompositionRef().getValue() == "/Root"
        assert iref.getContextPortRef().getValue() == "/Root/SwcA/DataPort"
        assert iref.getTargetDataPrototypeRef().getValue() == "/Root/SwcA/DataPort/Elem"
        assert reloaded.getSystemSignalRef().getValue() == "/System/Signal"
        assert isinstance(reloaded.getTypeMapping(), SenderRecRecordTypeMapping)

    def test_round_trip_empty(self):
        element = _write_direct(SenderReceiverCompositeElementToSignalMapping())
        assert len(list(element)) == 0

        reparsed = ET.fromstring(
            ET.tostring(element).decode("utf-8").replace("<SENDER-RECEIVER-COMPOSITE-ELEMENT-TO-SIGNAL-MAPPING>", "<SENDER-RECEIVER-COMPOSITE-ELEMENT-TO-SIGNAL-MAPPING xmlns='%s'>" % NS, 1)
        )
        reloaded = SenderReceiverCompositeElementToSignalMapping()
        ARXMLParser().readSenderReceiverCompositeElementToSignalMapping(reparsed, reloaded)
        assert reloaded.getDataElementIRef() is None
        assert reloaded.getSystemSignalRef() is None
        assert reloaded.getTypeMapping() is None

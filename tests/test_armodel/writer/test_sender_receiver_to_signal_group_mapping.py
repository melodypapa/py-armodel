"""Writer round-trip tests for SenderReceiverToSignalGroupMapping (Table 5.26, p.234).

Element order per XSD complexType SENDER-RECEIVER-TO-SIGNAL-GROUP-MAPPING: group
DATA-MAPPING (INTRODUCTION, VARIATION-POINT) then group
SENDER-RECEIVER-TO-SIGNAL-GROUP-MAPPING (DATA-ELEMENT-IREF, SIGNAL-GROUP-REF,
TYPE-MAPPING).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping import SenderReceiverToSignalGroupMapping, SenderRecRecordElementMapping, SenderRecRecordTypeMapping
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import VariableDataPrototypeInSystemInstanceRef
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import LParagraph
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultiLanguageParagraph
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
    result = RefType()
    result.setValue(value)
    result.setDest(dest)
    return result


def _new_mapping() -> SenderReceiverToSignalGroupMapping:
    mapping = SenderReceiverToSignalGroupMapping()

    paragraph = MultiLanguageParagraph()
    l1 = LParagraph()
    l1.setL("EN")
    l1.setValue("Group mapping intro")
    paragraph.addL1(l1)
    block = DocumentationBlock()
    block.addP(paragraph)
    mapping.setIntroduction(block)

    iref = VariableDataPrototypeInSystemInstanceRef()
    iref.setContextCompositionRef(_ref("/CanSystem/CanSystem/TopLevelComposition", "ROOT-SW-COMPOSITION-PROTOTYPE"))
    iref.setContextPortRef(_ref("/DemoApplication/SwComponentTypes/TopLevelComposition/P_CounterOut", "P-PORT-PROTOTYPE"))
    iref.setTargetDataPrototypeRef(_ref("/DemoApplication/PortInterfaces/If_Counter/CounterValue", "VARIABLE-DATA-PROTOTYPE"))
    mapping.setDataElementIRef(iref)

    mapping.setSignalGroupRef(_ref("/CanSystem/SIGNALGROUPS/CounterGroup", "SYSTEM-SIGNAL-GROUP"))

    record_element_mapping = SenderRecRecordElementMapping()
    record_element_mapping.setApplicationRecordElementRef(_ref("/DemoApplication/DataTypes/RecordType/Element1", "APPLICATION-RECORD-ELEMENT"))
    record_element_mapping.setSystemSignalRef(_ref("/CanSystem/SYSSIGNALS/CounterOut", "SYSTEM-SIGNAL"))
    record_type_mapping = SenderRecRecordTypeMapping()
    record_type_mapping.addRecordElementMapping(record_element_mapping)
    mapping.setTypeMapping(record_type_mapping)

    return mapping


def _write(mapping: SenderReceiverToSignalGroupMapping) -> ET.Element:
    element = ET.Element("MAPPINGS")
    ARXMLWriter().writeSenderReceiverToSignalGroupMapping(element, mapping)
    return element.find("SENDER-RECEIVER-TO-SIGNAL-GROUP-MAPPING")


class TestWriteSenderReceiverToSignalGroupMapping:
    def test_write_field_values(self):
        element = _write(_new_mapping())

        introduction = element.find("INTRODUCTION")
        assert introduction is not None
        assert introduction.find("P/L-1").text == "Group mapping intro"

        iref = element.find("DATA-ELEMENT-IREF")
        assert iref is not None
        composition_ref = iref.find("CONTEXT-COMPOSITION-REF")
        assert composition_ref.text == "/CanSystem/CanSystem/TopLevelComposition"
        assert composition_ref.get("DEST") == "ROOT-SW-COMPOSITION-PROTOTYPE"
        port_ref = iref.find("CONTEXT-PORT-REF")
        assert port_ref.text == "/DemoApplication/SwComponentTypes/TopLevelComposition/P_CounterOut"
        assert port_ref.get("DEST") == "P-PORT-PROTOTYPE"
        target_ref = iref.find("TARGET-DATA-PROTOTYPE-REF")
        assert target_ref.text == "/DemoApplication/PortInterfaces/If_Counter/CounterValue"
        assert target_ref.get("DEST") == "VARIABLE-DATA-PROTOTYPE"

        signal_group_ref = element.find("SIGNAL-GROUP-REF")
        assert signal_group_ref.text == "/CanSystem/SIGNALGROUPS/CounterGroup"
        assert signal_group_ref.get("DEST") == "SYSTEM-SIGNAL-GROUP"

        type_mapping = element.find("TYPE-MAPPING")
        assert type_mapping is not None
        record_mapping = type_mapping.find("SENDER-REC-RECORD-TYPE-MAPPING/RECORD-ELEMENT-MAPPINGS/SENDER-REC-RECORD-ELEMENT-MAPPING")
        assert record_mapping is not None
        assert record_mapping.find("APPLICATION-RECORD-ELEMENT-REF").text == "/DemoApplication/DataTypes/RecordType/Element1"
        assert record_mapping.find("APPLICATION-RECORD-ELEMENT-REF").get("DEST") == "APPLICATION-RECORD-ELEMENT"
        assert record_mapping.find("SYSTEM-SIGNAL-REF").text == "/CanSystem/SYSSIGNALS/CounterOut"
        assert record_mapping.find("SYSTEM-SIGNAL-REF").get("DEST") == "SYSTEM-SIGNAL"

    def test_write_empty_omits_all_elements(self):
        element = _write(SenderReceiverToSignalGroupMapping())

        assert len(element) == 0
        assert element.find("INTRODUCTION") is None
        assert element.find("DATA-ELEMENT-IREF") is None
        assert element.find("SIGNAL-GROUP-REF") is None
        assert element.find("TYPE-MAPPING") is None

    def test_write_xsd_order(self):
        element = _write(_new_mapping())

        assert [child.tag for child in element] == [
            "INTRODUCTION",
            "DATA-ELEMENT-IREF",
            "SIGNAL-GROUP-REF",
            "TYPE-MAPPING",
        ]

    def test_round_trip_field_values(self):
        source = _write(_new_mapping())

        wrapped = ET.fromstring("<AUTOSAR xmlns='%s'>%s</AUTOSAR>" % (NS, ET.tostring(source, encoding="unicode")))
        mapping = SenderReceiverToSignalGroupMapping()
        ARXMLParser().readSenderReceiverToSignalGroupMapping(wrapped[0], mapping)

        target = _write(mapping)

        assert target.find("INTRODUCTION/P/L-1").text == "Group mapping intro"
        assert target.find("DATA-ELEMENT-IREF/TARGET-DATA-PROTOTYPE-REF").text == "/DemoApplication/PortInterfaces/If_Counter/CounterValue"
        assert target.find("DATA-ELEMENT-IREF/CONTEXT-PORT-REF").get("DEST") == "P-PORT-PROTOTYPE"
        assert target.find("SIGNAL-GROUP-REF").text == "/CanSystem/SIGNALGROUPS/CounterGroup"
        assert target.find("SIGNAL-GROUP-REF").get("DEST") == "SYSTEM-SIGNAL-GROUP"
        record_mapping = target.find("TYPE-MAPPING/SENDER-REC-RECORD-TYPE-MAPPING/RECORD-ELEMENT-MAPPINGS/SENDER-REC-RECORD-ELEMENT-MAPPING")
        assert record_mapping.find("SYSTEM-SIGNAL-REF").text == "/CanSystem/SYSSIGNALS/CounterOut"
        assert record_mapping.find("SYSTEM-SIGNAL-REF").get("DEST") == "SYSTEM-SIGNAL"

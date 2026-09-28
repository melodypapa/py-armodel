"""Writer round-trip tests for SenderReceiverToSignalMapping (Table 5.24, p.229).

Element order per XSD complexType SENDER-RECEIVER-TO-SIGNAL-MAPPING: group DATA-MAPPING
(INTRODUCTION, VARIATION-POINT) then group SENDER-RECEIVER-TO-SIGNAL-MAPPING
(DATA-ELEMENT-IREF, SENDER-TO-SIGNAL-TEXT-TABLE-MAPPING,
SIGNAL-TO-RECEIVER-TEXT-TABLE-MAPPING, SYSTEM-SIGNAL-REF).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import TextTableMapping
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping import SenderReceiverToSignalMapping
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import VariableDataPrototypeInSystemInstanceRef
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import LParagraph
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultiLanguageParagraph
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


def _boolean(value):
    result = Boolean()
    result.setValue(value)
    return result


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _new_mapping() -> SenderReceiverToSignalMapping:
    mapping = SenderReceiverToSignalMapping()

    paragraph = MultiLanguageParagraph()
    l1 = LParagraph()
    l1.setL("EN")
    l1.setValue("Mapping intro")
    paragraph.addL1(l1)
    block = DocumentationBlock()
    block.addP(paragraph)
    mapping.setIntroduction(block)

    iref = VariableDataPrototypeInSystemInstanceRef()
    composition_ref = RefType()
    composition_ref.setValue("/CanSystem/CanSystem/TopLevelComposition")
    composition_ref.setDest("ROOT-SW-COMPOSITION-PROTOTYPE")
    iref.setContextCompositionRef(composition_ref)
    port_ref = RefType()
    port_ref.setValue("/DemoApplication/SwComponentTypes/TopLevelComposition/P_CounterOut")
    port_ref.setDest("P-PORT-PROTOTYPE")
    iref.setContextPortRef(port_ref)
    target_ref = RefType()
    target_ref.setValue("/DemoApplication/PortInterfaces/If_Counter/CounterValue")
    target_ref.setDest("VARIABLE-DATA-PROTOTYPE")
    iref.setTargetDataPrototypeRef(target_ref)
    mapping.setDataElementIRef(iref)

    sender_to_signal = TextTableMapping()
    sender_to_signal.setIdenticalMapping(_boolean(True))
    mapping.setSenderToSignalTextTableMapping(sender_to_signal)

    signal_to_receiver = TextTableMapping()
    signal_to_receiver.setIdenticalMapping(_boolean(False))
    mapping.setSignalToReceiverTextTableMapping(signal_to_receiver)

    signal_ref = RefType()
    signal_ref.setValue("/CanSystem/SYSSIGNALS/CounterOut")
    signal_ref.setDest("SYSTEM-SIGNAL")
    mapping.setSystemSignalRef(signal_ref)

    return mapping


def _write(mapping: SenderReceiverToSignalMapping) -> ET.Element:
    element = ET.Element("MAPPINGS")
    ARXMLWriter().writeSenderReceiverToSignalMapping(element, mapping)
    return element.find("SENDER-RECEIVER-TO-SIGNAL-MAPPING")


class TestWriteSenderReceiverToSignalMapping:
    def test_write_field_values(self):
        element = _write(_new_mapping())

        introduction = element.find("INTRODUCTION")
        assert introduction is not None
        assert introduction.find("P/L-1").text == "Mapping intro"

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

        sender_to_signal = element.find("SENDER-TO-SIGNAL-TEXT-TABLE-MAPPING")
        assert sender_to_signal is not None
        assert sender_to_signal.find("IDENTICAL-MAPPING").text == "true"
        signal_to_receiver = element.find("SIGNAL-TO-RECEIVER-TEXT-TABLE-MAPPING")
        assert signal_to_receiver is not None
        assert signal_to_receiver.find("IDENTICAL-MAPPING").text == "false"

        signal_ref = element.find("SYSTEM-SIGNAL-REF")
        assert signal_ref.text == "/CanSystem/SYSSIGNALS/CounterOut"
        assert signal_ref.get("DEST") == "SYSTEM-SIGNAL"

    def test_write_empty_omits_all_elements(self):
        element = _write(SenderReceiverToSignalMapping())

        assert len(element) == 0
        assert element.find("INTRODUCTION") is None
        assert element.find("DATA-ELEMENT-IREF") is None
        assert element.find("SENDER-TO-SIGNAL-TEXT-TABLE-MAPPING") is None
        assert element.find("SIGNAL-TO-RECEIVER-TEXT-TABLE-MAPPING") is None
        assert element.find("SYSTEM-SIGNAL-REF") is None

    def test_write_xsd_order(self):
        element = _write(_new_mapping())

        assert [child.tag for child in element] == [
            "INTRODUCTION",
            "DATA-ELEMENT-IREF",
            "SENDER-TO-SIGNAL-TEXT-TABLE-MAPPING",
            "SIGNAL-TO-RECEIVER-TEXT-TABLE-MAPPING",
            "SYSTEM-SIGNAL-REF",
        ]

    def test_round_trip_field_values(self):
        source = _write(_new_mapping())

        wrapped = ET.fromstring("<AUTOSAR xmlns='%s'>%s</AUTOSAR>" % (NS, ET.tostring(source, encoding="unicode")))
        mapping = SenderReceiverToSignalMapping()
        ARXMLParser().readSenderReceiverToSignalMapping(wrapped[0], mapping)

        target = _write(mapping)

        assert target.find("INTRODUCTION/P/L-1").text == "Mapping intro"
        assert target.find("DATA-ELEMENT-IREF/TARGET-DATA-PROTOTYPE-REF").text == "/DemoApplication/PortInterfaces/If_Counter/CounterValue"
        assert target.find("DATA-ELEMENT-IREF/CONTEXT-PORT-REF").get("DEST") == "P-PORT-PROTOTYPE"
        assert target.find("SENDER-TO-SIGNAL-TEXT-TABLE-MAPPING/IDENTICAL-MAPPING").text == "true"
        assert target.find("SIGNAL-TO-RECEIVER-TEXT-TABLE-MAPPING/IDENTICAL-MAPPING").text == "false"
        assert target.find("SYSTEM-SIGNAL-REF").text == "/CanSystem/SYSSIGNALS/CounterOut"
        assert target.find("SYSTEM-SIGNAL-REF").get("DEST") == "SYSTEM-SIGNAL"

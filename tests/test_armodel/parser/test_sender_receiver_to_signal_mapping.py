"""Parser tests for SenderReceiverToSignalMapping (Table 5.24, p.229).

Element order per XSD: the complexType inlines group DATA-MAPPING (INTRODUCTION +
VARIATION-POINT) before group SENDER-RECEIVER-TO-SIGNAL-MAPPING (DATA-ELEMENT-IREF,
SENDER-TO-SIGNAL-TEXT-TABLE-MAPPING, SIGNAL-TO-RECEIVER-TEXT-TABLE-MAPPING,
SYSTEM-SIGNAL-REF).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate import SystemMapping
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping import SenderReceiverToSignalMapping
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import VariableDataPrototypeInSystemInstanceRef
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str) -> ET.Element:
    return ET.fromstring("<ROOT xmlns='%s'>%s</ROOT>" % (NS, inner))


SIGNAL_MAPPING_XML = (
    "<SENDER-RECEIVER-TO-SIGNAL-MAPPING>"
    "<INTRODUCTION><P><L-1 L='en'>Mapping intro</L-1></P></INTRODUCTION>"
    "<DATA-ELEMENT-IREF>"
    '<CONTEXT-COMPOSITION-REF DEST="ROOT-SW-COMPOSITION-PROTOTYPE">/CanSystem/CanSystem/TopLevelComposition</CONTEXT-COMPOSITION-REF>'
    '<CONTEXT-PORT-REF DEST="P-PORT-PROTOTYPE">/DemoApplication/SwComponentTypes/TopLevelComposition/P_CounterOut</CONTEXT-PORT-REF>'
    '<TARGET-DATA-PROTOTYPE-REF DEST="VARIABLE-DATA-PROTOTYPE">/DemoApplication/PortInterfaces/If_Counter/CounterValue</TARGET-DATA-PROTOTYPE-REF>'
    "</DATA-ELEMENT-IREF>"
    "<SENDER-TO-SIGNAL-TEXT-TABLE-MAPPING>"
    "<IDENTICAL-MAPPING>true</IDENTICAL-MAPPING>"
    "</SENDER-TO-SIGNAL-TEXT-TABLE-MAPPING>"
    "<SIGNAL-TO-RECEIVER-TEXT-TABLE-MAPPING>"
    "<IDENTICAL-MAPPING>false</IDENTICAL-MAPPING>"
    "</SIGNAL-TO-RECEIVER-TEXT-TABLE-MAPPING>"
    '<SYSTEM-SIGNAL-REF DEST="SYSTEM-SIGNAL">/CanSystem/SYSSIGNALS/CounterOut</SYSTEM-SIGNAL-REF>'
    "</SENDER-RECEIVER-TO-SIGNAL-MAPPING>"
)


class TestReadSenderReceiverToSignalMapping:
    def test_read_field_values(self):
        root = _snip(SIGNAL_MAPPING_XML)
        mapping = SenderReceiverToSignalMapping()
        ARXMLParser().readSenderReceiverToSignalMapping(root[0], mapping)

        block = mapping.getIntroduction()
        assert block is not None
        assert block.getPs()[0].getL1s()[0].getValue() == "Mapping intro"

        iref = mapping.getDataElementIRef()
        assert isinstance(iref, VariableDataPrototypeInSystemInstanceRef)
        assert iref.getContextCompositionRef().getValue() == "/CanSystem/CanSystem/TopLevelComposition"
        assert iref.getContextCompositionRef().getDest() == "ROOT-SW-COMPOSITION-PROTOTYPE"
        assert iref.getContextPortRef().getValue() == "/DemoApplication/SwComponentTypes/TopLevelComposition/P_CounterOut"
        assert iref.getContextPortRef().getDest() == "P-PORT-PROTOTYPE"
        assert iref.getTargetDataPrototypeRef().getValue() == "/DemoApplication/PortInterfaces/If_Counter/CounterValue"
        assert iref.getTargetDataPrototypeRef().getDest() == "VARIABLE-DATA-PROTOTYPE"

        sender_to_signal = mapping.getSenderToSignalTextTableMapping()
        assert sender_to_signal is not None
        assert sender_to_signal.getIdenticalMapping().getValue() is True
        signal_to_receiver = mapping.getSignalToReceiverTextTableMapping()
        assert signal_to_receiver is not None
        assert signal_to_receiver.getIdenticalMapping().getValue() is False

        assert mapping.getSystemSignalRef().getValue() == "/CanSystem/SYSSIGNALS/CounterOut"
        assert mapping.getSystemSignalRef().getDest() == "SYSTEM-SIGNAL"

    def test_read_empty(self):
        root = _snip("<SENDER-RECEIVER-TO-SIGNAL-MAPPING />")
        mapping = SenderReceiverToSignalMapping()
        ARXMLParser().readSenderReceiverToSignalMapping(root[0], mapping)

        assert mapping.getIntroduction() is None
        assert mapping.getVariationPoint() is None
        assert mapping.getDataElementIRef() is None
        assert mapping.getSenderToSignalTextTableMapping() is None
        assert mapping.getSignalToReceiverTextTableMapping() is None
        assert mapping.getSystemSignalRef() is None

    def test_read_variation_point(self):
        root = _snip("<SENDER-RECEIVER-TO-SIGNAL-MAPPING>" "<VARIATION-POINT><SHORT-LABEL>varLbl</SHORT-LABEL></VARIATION-POINT>" "</SENDER-RECEIVER-TO-SIGNAL-MAPPING>")
        mapping = SenderReceiverToSignalMapping()
        ARXMLParser().readSenderReceiverToSignalMapping(root[0], mapping)

        variation_point = mapping.getVariationPoint()
        assert variation_point is not None
        assert variation_point.getShortLabel().getValue() == "varLbl"

    def test_read_dispatch_via_system_mapping(self):
        root = _snip("<SYSTEM-MAPPING><DATA-MAPPINGS>%s</DATA-MAPPINGS></SYSTEM-MAPPING>" % SIGNAL_MAPPING_XML)
        system_mapping = SystemMapping(MockParent(), "SystemMapping")
        ARXMLParser().readSystemMappingDataMappings(root[0], system_mapping)

        data_mappings = system_mapping.getDataMappings()
        assert len(data_mappings) == 1
        signal_mapping = data_mappings[0]
        assert isinstance(signal_mapping, SenderReceiverToSignalMapping)
        assert signal_mapping.getSystemSignalRef().getValue() == "/CanSystem/SYSSIGNALS/CounterOut"
        assert signal_mapping.getDataElementIRef().getTargetDataPrototypeRef().getValue() == "/DemoApplication/PortInterfaces/If_Counter/CounterValue"

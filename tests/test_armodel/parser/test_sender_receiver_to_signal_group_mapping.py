"""Parser tests for SenderReceiverToSignalGroupMapping (Table 5.26, p.234).

Element order per XSD: the complexType inlines group DATA-MAPPING (INTRODUCTION +
VARIATION-POINT) before group SENDER-RECEIVER-TO-SIGNAL-GROUP-MAPPING
(DATA-ELEMENT-IREF, SIGNAL-GROUP-REF, TYPE-MAPPING).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate import SystemMapping
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping import SenderReceiverToSignalGroupMapping, SenderRecRecordElementMapping, SenderRecRecordTypeMapping
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


GROUP_MAPPING_XML = (
    "<SENDER-RECEIVER-TO-SIGNAL-GROUP-MAPPING>"
    "<INTRODUCTION><P><L-1 L='en'>Group mapping intro</L-1></P></INTRODUCTION>"
    "<DATA-ELEMENT-IREF>"
    '<CONTEXT-COMPOSITION-REF DEST="ROOT-SW-COMPOSITION-PROTOTYPE">/CanSystem/CanSystem/TopLevelComposition</CONTEXT-COMPOSITION-REF>'
    '<CONTEXT-PORT-REF DEST="P-PORT-PROTOTYPE">/DemoApplication/SwComponentTypes/TopLevelComposition/P_CounterOut</CONTEXT-PORT-REF>'
    '<TARGET-DATA-PROTOTYPE-REF DEST="VARIABLE-DATA-PROTOTYPE">/DemoApplication/PortInterfaces/If_Counter/CounterValue</TARGET-DATA-PROTOTYPE-REF>'
    "</DATA-ELEMENT-IREF>"
    '<SIGNAL-GROUP-REF DEST="SYSTEM-SIGNAL-GROUP">/CanSystem/SIGNALGROUPS/CounterGroup</SIGNAL-GROUP-REF>'
    "<TYPE-MAPPING>"
    "<SENDER-REC-RECORD-TYPE-MAPPING>"
    "<RECORD-ELEMENT-MAPPINGS>"
    "<SENDER-REC-RECORD-ELEMENT-MAPPING>"
    '<APPLICATION-RECORD-ELEMENT-REF DEST="APPLICATION-RECORD-ELEMENT">/DemoApplication/DataTypes/RecordType/Element1</APPLICATION-RECORD-ELEMENT-REF>'
    '<SYSTEM-SIGNAL-REF DEST="SYSTEM-SIGNAL">/CanSystem/SYSSIGNALS/CounterOut</SYSTEM-SIGNAL-REF>'
    "</SENDER-REC-RECORD-ELEMENT-MAPPING>"
    "</RECORD-ELEMENT-MAPPINGS>"
    "</SENDER-REC-RECORD-TYPE-MAPPING>"
    "</TYPE-MAPPING>"
    "</SENDER-RECEIVER-TO-SIGNAL-GROUP-MAPPING>"
)


class TestReadSenderReceiverToSignalGroupMapping:
    def test_read_field_values(self):
        root = _snip(GROUP_MAPPING_XML)
        mapping = SenderReceiverToSignalGroupMapping()
        ARXMLParser().readSenderReceiverToSignalGroupMapping(root[0], mapping)

        block = mapping.getIntroduction()
        assert block is not None
        assert block.getPs()[0].getL1s()[0].getValue() == "Group mapping intro"

        iref = mapping.getDataElementIRef()
        assert isinstance(iref, VariableDataPrototypeInSystemInstanceRef)
        assert iref.getContextCompositionRef().getValue() == "/CanSystem/CanSystem/TopLevelComposition"
        assert iref.getContextCompositionRef().getDest() == "ROOT-SW-COMPOSITION-PROTOTYPE"
        assert iref.getContextPortRef().getValue() == "/DemoApplication/SwComponentTypes/TopLevelComposition/P_CounterOut"
        assert iref.getContextPortRef().getDest() == "P-PORT-PROTOTYPE"
        assert iref.getTargetDataPrototypeRef().getValue() == "/DemoApplication/PortInterfaces/If_Counter/CounterValue"
        assert iref.getTargetDataPrototypeRef().getDest() == "VARIABLE-DATA-PROTOTYPE"

        assert mapping.getSignalGroupRef().getValue() == "/CanSystem/SIGNALGROUPS/CounterGroup"
        assert mapping.getSignalGroupRef().getDest() == "SYSTEM-SIGNAL-GROUP"

        type_mapping = mapping.getTypeMapping()
        assert isinstance(type_mapping, SenderRecRecordTypeMapping)
        record_mappings = type_mapping.getRecordElementMappings()
        assert len(record_mappings) == 1
        record_mapping = record_mappings[0]
        assert isinstance(record_mapping, SenderRecRecordElementMapping)
        assert record_mapping.getApplicationRecordElementRef().getValue() == "/DemoApplication/DataTypes/RecordType/Element1"
        assert record_mapping.getApplicationRecordElementRef().getDest() == "APPLICATION-RECORD-ELEMENT"
        assert record_mapping.getSystemSignalRef().getValue() == "/CanSystem/SYSSIGNALS/CounterOut"
        assert record_mapping.getSystemSignalRef().getDest() == "SYSTEM-SIGNAL"

    def test_read_empty(self):
        root = _snip("<SENDER-RECEIVER-TO-SIGNAL-GROUP-MAPPING />")
        mapping = SenderReceiverToSignalGroupMapping()
        ARXMLParser().readSenderReceiverToSignalGroupMapping(root[0], mapping)

        assert mapping.getIntroduction() is None
        assert mapping.getVariationPoint() is None
        assert mapping.getDataElementIRef() is None
        assert mapping.getSignalGroupRef() is None
        assert mapping.getTypeMapping() is None

    def test_read_variation_point(self):
        root = _snip("<SENDER-RECEIVER-TO-SIGNAL-GROUP-MAPPING>" "<VARIATION-POINT><SHORT-LABEL>grpVarLbl</SHORT-LABEL></VARIATION-POINT>" "</SENDER-RECEIVER-TO-SIGNAL-GROUP-MAPPING>")
        mapping = SenderReceiverToSignalGroupMapping()
        ARXMLParser().readSenderReceiverToSignalGroupMapping(root[0], mapping)

        variation_point = mapping.getVariationPoint()
        assert variation_point is not None
        assert variation_point.getShortLabel().getValue() == "grpVarLbl"

    def test_read_dispatch_via_system_mapping(self):
        root = _snip("<SYSTEM-MAPPING><DATA-MAPPINGS>%s</DATA-MAPPINGS></SYSTEM-MAPPING>" % GROUP_MAPPING_XML)
        system_mapping = SystemMapping(MockParent(), "SystemMapping")
        ARXMLParser().readSystemMappingDataMappings(root[0], system_mapping)

        data_mappings = system_mapping.getDataMappings()
        assert len(data_mappings) == 1
        group_mapping = data_mappings[0]
        assert isinstance(group_mapping, SenderReceiverToSignalGroupMapping)
        assert group_mapping.getSignalGroupRef().getValue() == "/CanSystem/SIGNALGROUPS/CounterGroup"
        assert group_mapping.getDataElementIRef().getTargetDataPrototypeRef().getValue() == "/DemoApplication/PortInterfaces/If_Counter/CounterValue"

"""Tests for System Mapping and Type Mapping handler gaps."""
import logging
from unittest.mock import MagicMock

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate import SystemMapping
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping import (
    SenderRecRecordElementMapping,
    SenderRecRecordTypeMapping,
    SenderReceiverToSignalGroupMapping,
)
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease('R23-11')
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease('R23-11')
    return ARXMLParser()


@pytest.fixture
def warning_parser():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease('R23-11')
    return ARXMLParser(options={"warning": True})


def _snip(inner: str, root_tag: str = "ROOT") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


def _autosar_root():
    return AUTOSAR.getInstance()


def _make_system_mapping():
    return SystemMapping(parent=MagicMock(), short_name="TestSystemMapping")


# ==================== readSenderRecRecordElementMapping (L5373-5377) ====================


class TestReadSenderRecRecordElementMapping:
    """Cover readSenderRecRecordElementMapping optional ref handling."""

    def test_sets_all_optional_refs_when_present(self, parser):
        mapping = SenderRecRecordElementMapping()
        element = _snip("""
            <APPLICATION-RECORD-ELEMENT-REF DEST="RECORD-ELEMENT">/App/Rec1</APPLICATION-RECORD-ELEMENT-REF>
            <IMPLEMENTATION-RECORD-ELEMENT-REF DEST="RECORD-ELEMENT">/Impl/Rec1</IMPLEMENTATION-RECORD-ELEMENT-REF>
            <SYSTEM-SIGNAL-REF DEST="SYSTEM-SIGNAL">/Sig/S1</SYSTEM-SIGNAL-REF>
        """)
        parser.readSenderRecRecordElementMapping(element, mapping)
        assert mapping.getApplicationRecordElementRef() is not None
        assert mapping.getApplicationRecordElementRef().getValue() == "/App/Rec1"
        assert mapping.getImplementationRecordElementRef() is not None
        assert mapping.getImplementationRecordElementRef().getValue() == "/Impl/Rec1"
        assert mapping.getSystemSignalRef() is not None
        assert mapping.getSystemSignalRef().getValue() == "/Sig/S1"

    def test_keeps_refs_none_when_absent(self, parser):
        mapping = SenderRecRecordElementMapping()
        element = _snip("")
        parser.readSenderRecRecordElementMapping(element, mapping)
        assert mapping.getApplicationRecordElementRef() is None
        assert mapping.getImplementationRecordElementRef() is None
        assert mapping.getSystemSignalRef() is None


# ==================== readSenderRecArrayTypeMappingRecordElementMapping (L5379-5387) ====================


class TestReadSenderRecArrayTypeMappingRecordElementMapping:
    """Cover SENDER-REC-RECORD-ELEMENT-MAPPING branch and warning branch."""

    def test_reads_sender_rec_record_element_mapping(self, parser):
        mapping = SenderRecRecordTypeMapping()
        element = _snip("""
            <RECORD-ELEMENT-MAPPINGS>
                <SENDER-REC-RECORD-ELEMENT-MAPPING>
                    <APPLICATION-RECORD-ELEMENT-REF DEST="RECORD-ELEMENT">/App/Rec1</APPLICATION-RECORD-ELEMENT-REF>
                    <IMPLEMENTATION-RECORD-ELEMENT-REF DEST="RECORD-ELEMENT">/Impl/Rec1</IMPLEMENTATION-RECORD-ELEMENT-REF>
                    <SYSTEM-SIGNAL-REF DEST="SYSTEM-SIGNAL">/Sig/S1</SYSTEM-SIGNAL-REF>
                </SENDER-REC-RECORD-ELEMENT-MAPPING>
            </RECORD-ELEMENT-MAPPINGS>
        """)
        parser.readSenderRecArrayTypeMappingRecordElementMapping(element, mapping)
        mappings = mapping.getRecordElementMappings()
        assert len(mappings) == 1
        assert isinstance(mappings[0], SenderRecRecordElementMapping)
        assert mappings[0].getSystemSignalRef().getValue() == "/Sig/S1"

    def test_unsupported_record_element_mapping_raises(self, parser):
        mapping = SenderRecRecordTypeMapping()
        element = _snip("""
            <RECORD-ELEMENT-MAPPINGS>
                <UNKNOWN-MAPPING>
                    <SHORT-NAME>X</SHORT-NAME>
                </UNKNOWN-MAPPING>
            </RECORD-ELEMENT-MAPPINGS>
        """)
        with pytest.raises(NotImplementedError):
            parser.readSenderRecArrayTypeMappingRecordElementMapping(element, mapping)

    def test_unsupported_record_element_mapping_logs_warning(self, warning_parser, caplog):
        mapping = SenderRecRecordTypeMapping()
        element = _snip("""
            <RECORD-ELEMENT-MAPPINGS>
                <UNKNOWN-MAPPING>
                    <SHORT-NAME>X</SHORT-NAME>
                </UNKNOWN-MAPPING>
            </RECORD-ELEMENT-MAPPINGS>
        """)
        with caplog.at_level(logging.ERROR):
            warning_parser.readSenderRecArrayTypeMappingRecordElementMapping(element, mapping)
        assert any("Unsupported RecordElementMapping" in rec.getMessage() for rec in caplog.records)
        assert mapping.getRecordElementMappings() == []

    def test_empty_record_element_mappings(self, parser):
        mapping = SenderRecRecordTypeMapping()
        element = _snip("<RECORD-ELEMENT-MAPPINGS></RECORD-ELEMENT-MAPPINGS>")
        parser.readSenderRecArrayTypeMappingRecordElementMapping(element, mapping)
        assert mapping.getRecordElementMappings() == []


# ==================== readSenderRecRecordTypeMapping (L5389-5391) ====================


class TestReadSenderRecRecordTypeMapping:
    """Cover readSenderRecRecordTypeMapping delegation."""

    def test_delegates_to_composite_and_array_type_mapping(self, parser):
        mapping = SenderRecRecordTypeMapping()
        element = _snip("""
            <RECORD-ELEMENT-MAPPINGS>
                <SENDER-REC-RECORD-ELEMENT-MAPPING>
                    <APPLICATION-RECORD-ELEMENT-REF DEST="RECORD-ELEMENT">/App/Rec1</APPLICATION-RECORD-ELEMENT-REF>
                    <IMPLEMENTATION-RECORD-ELEMENT-REF DEST="RECORD-ELEMENT">/Impl/Rec1</IMPLEMENTATION-RECORD-ELEMENT-REF>
                    <SYSTEM-SIGNAL-REF DEST="SYSTEM-SIGNAL">/Sig/S1</SYSTEM-SIGNAL-REF>
                </SENDER-REC-RECORD-ELEMENT-MAPPING>
                <SENDER-REC-RECORD-ELEMENT-MAPPING>
                    <APPLICATION-RECORD-ELEMENT-REF DEST="RECORD-ELEMENT">/App/Rec2</APPLICATION-RECORD-ELEMENT-REF>
                    <IMPLEMENTATION-RECORD-ELEMENT-REF DEST="RECORD-ELEMENT">/Impl/Rec2</IMPLEMENTATION-RECORD-ELEMENT-REF>
                    <SYSTEM-SIGNAL-REF DEST="SYSTEM-SIGNAL">/Sig/S2</SYSTEM-SIGNAL-REF>
                </SENDER-REC-RECORD-ELEMENT-MAPPING>
            </RECORD-ELEMENT-MAPPINGS>
        """)
        parser.readSenderRecRecordTypeMapping(element, mapping)
        mappings = mapping.getRecordElementMappings()
        assert len(mappings) == 2
        assert mappings[0].getSystemSignalRef().getValue() == "/Sig/S1"
        assert mappings[1].getSystemSignalRef().getValue() == "/Sig/S2"


# ==================== readSenderReceiverToSignalGroupMappingTypeMapping (L5393-5402) ====================


class TestReadSenderReceiverToSignalGroupMappingTypeMapping:
    """Cover SENDER-REC-RECORD-TYPE-MAPPING branch and warning branch."""

    def test_reads_sender_rec_record_type_mapping(self, parser):
        mapping = SenderReceiverToSignalGroupMapping()
        element = _snip("""
            <TYPE-MAPPING>
                <SENDER-REC-RECORD-TYPE-MAPPING>
                    <RECORD-ELEMENT-MAPPINGS>
                        <SENDER-REC-RECORD-ELEMENT-MAPPING>
                            <APPLICATION-RECORD-ELEMENT-REF DEST="RECORD-ELEMENT">/App/Rec1</APPLICATION-RECORD-ELEMENT-REF>
                            <IMPLEMENTATION-RECORD-ELEMENT-REF DEST="RECORD-ELEMENT">/Impl/Rec1</IMPLEMENTATION-RECORD-ELEMENT-REF>
                            <SYSTEM-SIGNAL-REF DEST="SYSTEM-SIGNAL">/Sig/S1</SYSTEM-SIGNAL-REF>
                        </SENDER-REC-RECORD-ELEMENT-MAPPING>
                    </RECORD-ELEMENT-MAPPINGS>
                </SENDER-REC-RECORD-TYPE-MAPPING>
            </TYPE-MAPPING>
        """)
        parser.readSenderReceiverToSignalGroupMappingTypeMapping(element, mapping)
        type_mapping = mapping.getTypeMapping()
        assert type_mapping is not None
        assert isinstance(type_mapping, SenderRecRecordTypeMapping)
        assert len(type_mapping.getRecordElementMappings()) == 1
        assert type_mapping.getRecordElementMappings()[0].getSystemSignalRef().getValue() == "/Sig/S1"

    def test_unsupported_type_mapping_raises(self, parser):
        mapping = SenderReceiverToSignalGroupMapping()
        element = _snip("""
            <TYPE-MAPPING>
                <UNKNOWN-TYPE-MAPPING>
                    <SHORT-NAME>X</SHORT-NAME>
                </UNKNOWN-TYPE-MAPPING>
            </TYPE-MAPPING>
        """)
        with pytest.raises(NotImplementedError):
            parser.readSenderReceiverToSignalGroupMappingTypeMapping(element, mapping)

    def test_unsupported_type_mapping_logs_warning(self, warning_parser, caplog):
        mapping = SenderReceiverToSignalGroupMapping()
        element = _snip("""
            <TYPE-MAPPING>
                <UNKNOWN-TYPE-MAPPING>
                    <SHORT-NAME>X</SHORT-NAME>
                </UNKNOWN-TYPE-MAPPING>
            </TYPE-MAPPING>
        """)
        with caplog.at_level(logging.ERROR):
            warning_parser.readSenderReceiverToSignalGroupMappingTypeMapping(element, mapping)
        assert any("Unsupported Type Mapping" in rec.getMessage() for rec in caplog.records)
        assert mapping.getTypeMapping() is None

    def test_no_type_mapping_child_keeps_none(self, parser):
        mapping = SenderReceiverToSignalGroupMapping()
        element = _snip("")
        parser.readSenderReceiverToSignalGroupMappingTypeMapping(element, mapping)
        assert mapping.getTypeMapping() is None


# ==================== readSystemMappingDataMappings (L5409-5421) ====================


class TestReadSystemMappingDataMappings:
    """Cover SENDER-RECEIVER-TO-SIGNAL-MAPPING and SENDER-RECEIVER-TO-SIGNAL-GROUP-MAPPING branches + warning."""

    def test_reads_sender_receiver_to_signal_mapping(self, parser):
        mapping = _make_system_mapping()
        element = _snip("""
            <DATA-MAPPINGS>
                <SENDER-RECEIVER-TO-SIGNAL-MAPPING>
                    <COMMUNICATION-DIRECTION>IN</COMMUNICATION-DIRECTION>
                    <DATA-ELEMENT-IREF>
                        <CONTEXT-COMPOSITION-REF DEST="COMPOSITION-SW-COMPONENT-TYPE">/Cmp/Comp</CONTEXT-COMPOSITION-REF>
                        <CONTEXT-COMPONENT-REF DEST="SW-COMPONENT-PROTOTYPE">/Cmp/Comp/sw1</CONTEXT-COMPONENT-REF>
                        <CONTEXT-PORT-REF DEST="P-PORT-PROTOTYPE">/Cmp/Comp/port1</CONTEXT-PORT-REF>
                        <TARGET-DATA-PROTOTYPE-REF DEST="VARIABLE-DATA-PROTOTYPE">/Iface/If/de1</TARGET-DATA-PROTOTYPE-REF>
                    </DATA-ELEMENT-IREF>
                    <SYSTEM-SIGNAL-REF DEST="SYSTEM-SIGNAL">/Sig/S1</SYSTEM-SIGNAL-REF>
                </SENDER-RECEIVER-TO-SIGNAL-MAPPING>
            </DATA-MAPPINGS>
        """)
        parser.readSystemMappingDataMappings(element, mapping)
        data_mappings = mapping.getDataMappings()
        assert len(data_mappings) == 1
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping import (
            SenderReceiverToSignalMapping,
        )
        assert isinstance(data_mappings[0], SenderReceiverToSignalMapping)
        assert data_mappings[0].getSystemSignalRef().getValue() == "/Sig/S1"
        assert data_mappings[0].getCommunicationDirection().getValue() == "IN"
        assert data_mappings[0].getDataElementIRef() is not None

    def test_reads_sender_receiver_to_signal_group_mapping(self, parser):
        mapping = _make_system_mapping()
        element = _snip("""
            <DATA-MAPPINGS>
                <SENDER-RECEIVER-TO-SIGNAL-GROUP-MAPPING>
                    <DATA-ELEMENT-IREF>
                        <CONTEXT-COMPOSITION-REF DEST="COMPOSITION-SW-COMPONENT-TYPE">/Cmp/Comp</CONTEXT-COMPOSITION-REF>
                        <CONTEXT-COMPONENT-REF DEST="SW-COMPONENT-PROTOTYPE">/Cmp/Comp/sw1</CONTEXT-COMPONENT-REF>
                        <CONTEXT-PORT-REF DEST="P-PORT-PROTOTYPE">/Cmp/Comp/port1</CONTEXT-PORT-REF>
                        <TARGET-DATA-PROTOTYPE-REF DEST="VARIABLE-DATA-PROTOTYPE">/Iface/If/de1</TARGET-DATA-PROTOTYPE-REF>
                    </DATA-ELEMENT-IREF>
                    <SIGNAL-GROUP-REF DEST="SIGNAL-GROUP">/Sig/Group1</SIGNAL-GROUP-REF>
                    <TYPE-MAPPING>
                        <SENDER-REC-RECORD-TYPE-MAPPING>
                            <RECORD-ELEMENT-MAPPINGS>
                                <SENDER-REC-RECORD-ELEMENT-MAPPING>
                                    <APPLICATION-RECORD-ELEMENT-REF DEST="RECORD-ELEMENT">/App/Rec1</APPLICATION-RECORD-ELEMENT-REF>
                                    <IMPLEMENTATION-RECORD-ELEMENT-REF DEST="RECORD-ELEMENT">/Impl/Rec1</IMPLEMENTATION-RECORD-ELEMENT-REF>
                                    <SYSTEM-SIGNAL-REF DEST="SYSTEM-SIGNAL">/Sig/S1</SYSTEM-SIGNAL-REF>
                                </SENDER-REC-RECORD-ELEMENT-MAPPING>
                            </RECORD-ELEMENT-MAPPINGS>
                        </SENDER-REC-RECORD-TYPE-MAPPING>
                    </TYPE-MAPPING>
                </SENDER-RECEIVER-TO-SIGNAL-GROUP-MAPPING>
            </DATA-MAPPINGS>
        """)
        parser.readSystemMappingDataMappings(element, mapping)
        data_mappings = mapping.getDataMappings()
        assert len(data_mappings) == 1
        assert isinstance(data_mappings[0], SenderReceiverToSignalGroupMapping)
        assert data_mappings[0].getSignalGroupRef().getValue() == "/Sig/Group1"
        assert data_mappings[0].getDataElementIRef() is not None
        type_mapping = data_mappings[0].getTypeMapping()
        assert type_mapping is not None
        assert isinstance(type_mapping, SenderRecRecordTypeMapping)
        assert len(type_mapping.getRecordElementMappings()) == 1

    def test_reads_both_signal_and_signal_group_mappings(self, parser):
        mapping = _make_system_mapping()
        element = _snip("""
            <DATA-MAPPINGS>
                <SENDER-RECEIVER-TO-SIGNAL-MAPPING>
                    <DATA-ELEMENT-IREF>
                        <CONTEXT-COMPOSITION-REF DEST="COMPOSITION-SW-COMPONENT-TYPE">/Cmp/Comp</CONTEXT-COMPOSITION-REF>
                    </DATA-ELEMENT-IREF>
                    <SYSTEM-SIGNAL-REF DEST="SYSTEM-SIGNAL">/Sig/S1</SYSTEM-SIGNAL-REF>
                </SENDER-RECEIVER-TO-SIGNAL-MAPPING>
                <SENDER-RECEIVER-TO-SIGNAL-GROUP-MAPPING>
                    <DATA-ELEMENT-IREF>
                        <CONTEXT-COMPOSITION-REF DEST="COMPOSITION-SW-COMPONENT-TYPE">/Cmp/Comp</CONTEXT-COMPOSITION-REF>
                    </DATA-ELEMENT-IREF>
                    <SIGNAL-GROUP-REF DEST="SIGNAL-GROUP">/Sig/Group1</SIGNAL-GROUP-REF>
                </SENDER-RECEIVER-TO-SIGNAL-GROUP-MAPPING>
            </DATA-MAPPINGS>
        """)
        parser.readSystemMappingDataMappings(element, mapping)
        data_mappings = mapping.getDataMappings()
        assert len(data_mappings) == 2

    def test_unsupported_data_mapping_raises(self, parser):
        mapping = _make_system_mapping()
        element = _snip("""
            <DATA-MAPPINGS>
                <UNKNOWN-MAPPING>
                    <SHORT-NAME>X</SHORT-NAME>
                </UNKNOWN-MAPPING>
            </DATA-MAPPINGS>
        """)
        with pytest.raises(NotImplementedError):
            parser.readSystemMappingDataMappings(element, mapping)

    def test_unsupported_data_mapping_logs_warning(self, warning_parser, caplog):
        mapping = _make_system_mapping()
        element = _snip("""
            <DATA-MAPPINGS>
                <UNKNOWN-MAPPING>
                    <SHORT-NAME>X</SHORT-NAME>
                </UNKNOWN-MAPPING>
            </DATA-MAPPINGS>
        """)
        with caplog.at_level(logging.ERROR):
            warning_parser.readSystemMappingDataMappings(element, mapping)
        assert any("Unsupported Data Mapping" in rec.getMessage() for rec in caplog.records)
        assert mapping.getDataMappings() == []

    def test_empty_data_mappings(self, parser):
        mapping = _make_system_mapping()
        element = _snip("<DATA-MAPPINGS></DATA-MAPPINGS>")
        parser.readSystemMappingDataMappings(element, mapping)
        assert mapping.getDataMappings() == []

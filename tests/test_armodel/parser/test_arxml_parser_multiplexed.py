"""Tests for Multiplexed I-PDU, User-Defined PDU, and Secure Communication handlers.

Covers:
- MultiplexedPart / DynamicPart / StaticPart handlers
- MultiplexedIPdu dynamic/static part orchestrators
- UserDefinedIPdu, UserDefinedPdu, GeneralPurposePdu, GeneralPurposeIPdu handlers
- SecureCommunicationAuthenticationProps / FreshnessProps handlers
- SecureCommunicationPropsSet orchestrators
- SoAdRoutingGroup handler

Shared fixtures (``parser``, ``warning_parser``, ``reset_autosar``) are provided
by ``conftest.py``; helper functions (``_snip``, ``_autosar_root``) live in
``_helpers.py``.
"""
from unittest.mock import MagicMock
import logging

from tests.test_armodel.parser._helpers import _autosar_root, _snip


class TestMultiplexedPartHandlers:
    """Tests for MultiplexedPart, DynamicPart, StaticPart handlers."""

    def test_readMultiplexedPartSegmentPositions_with_segment(self, parser):
        from armodel.models import DynamicPart
        part = DynamicPart()
        element = _snip(
            "<SEGMENT-POSITIONS>"
            "<SEGMENT-POSITION>"
            "<SEGMENT-BYTE-ORDER>MOST-SIGNIFICANT-BYTE-LAST</SEGMENT-BYTE-ORDER>"
            "<SEGMENT-LENGTH>8</SEGMENT-LENGTH>"
            "<SEGMENT-POSITION>0</SEGMENT-POSITION>"
            "</SEGMENT-POSITION>"
            "</SEGMENT-POSITIONS>",
        )
        parser.readMultiplexedPartSegmentPositions(element, part)
        positions = part.getSegmentPositions()
        assert len(positions) == 1
        assert positions[0].getSegmentByteOrder().getValue() == "MOST-SIGNIFICANT-BYTE-LAST"
        assert positions[0].getSegmentLength().getValue() == 8
        assert positions[0].getSegmentPosition().getValue() == 0

    def test_readMultiplexedPartSegmentPositions_empty(self, parser):
        from armodel.models import DynamicPart
        part = DynamicPart()
        element = _snip("")
        parser.readMultiplexedPartSegmentPositions(element, part)
        assert len(part.getSegmentPositions()) == 0

    def test_readMultiplexedPartSegmentPositions_unknown_warning(self, warning_parser):
        from armodel.models import DynamicPart
        part = DynamicPart()
        element = _snip(
            "<SEGMENT-POSITIONS>"
            "<UNKNOWN-SEGMENT>"
            "<SHORT-NAME>Unknown</SHORT-NAME>"
            "</UNKNOWN-SEGMENT>"
            "</SEGMENT-POSITIONS>",
        )
        warning_parser.readMultiplexedPartSegmentPositions(element, part)
        assert len(part.getSegmentPositions()) == 0

    def test_readMultiplexedPart_delegates(self, parser):
        from armodel.models import DynamicPart
        part = DynamicPart()
        element = _snip(
            "<SEGMENT-POSITIONS>"
            "<SEGMENT-POSITION>"
            "<SEGMENT-LENGTH>4</SEGMENT-LENGTH>"
            "</SEGMENT-POSITION>"
            "</SEGMENT-POSITIONS>",
        )
        parser.readMultiplexedPart(element, part)
        assert len(part.getSegmentPositions()) == 1

    def test_readDynamicPartAlternative_sets_fields(self, parser):
        from armodel.models import DynamicPartAlternative
        alternative = DynamicPartAlternative()
        element = _snip(
            '<I-PDU-REF DEST="I-PDU">/pdus/DynAlt</I-PDU-REF>'
            '<INITIAL-DYNAMIC-PART>true</INITIAL-DYNAMIC-PART>'
            '<SELECTOR-FIELD-CODE>1</SELECTOR-FIELD-CODE>',
        )
        parser.readDynamicPartAlternative(element, alternative)
        assert alternative.getIPduRef() is not None
        assert alternative.getIPduRef().getValue() == "/pdus/DynAlt"
        assert alternative.getIPduRef().getDest() == "I-PDU"
        assert alternative.getInitialDynamicPart() is not None
        assert alternative.getSelectorFieldCode() is not None
        assert alternative.getSelectorFieldCode().getValue() == 1

    def test_readDynamicPartAlternative_empty(self, parser):
        from armodel.models import DynamicPartAlternative
        alternative = DynamicPartAlternative()
        element = _snip("")
        parser.readDynamicPartAlternative(element, alternative)
        assert alternative.getIPduRef() is None
        assert alternative.getInitialDynamicPart() is None
        assert alternative.getSelectorFieldCode() is None

    def test_readDynamicPartDynamicPartAlternatives_with_alternative(self, parser):
        from armodel.models import DynamicPart
        part = DynamicPart()
        element = _snip(
            "<DYNAMIC-PART-ALTERNATIVES>"
            "<DYNAMIC-PART-ALTERNATIVE>"
            '<I-PDU-REF DEST="I-PDU">/pdus/A1</I-PDU-REF>'
            '<SELECTOR-FIELD-CODE>2</SELECTOR-FIELD-CODE>'
            "</DYNAMIC-PART-ALTERNATIVE>"
            "</DYNAMIC-PART-ALTERNATIVES>",
        )
        parser.readDynamicPartDynamicPartAlternatives(element, part)
        alternatives = part.getDynamicPartAlternatives()
        assert len(alternatives) == 1
        assert alternatives[0].getIPduRef().getValue() == "/pdus/A1"

    def test_readDynamicPartDynamicPartAlternatives_unknown_warning(self, warning_parser):
        from armodel.models import DynamicPart
        part = DynamicPart()
        element = _snip(
            "<DYNAMIC-PART-ALTERNATIVES>"
            "<UNKNOWN-ALT>"
            "<SHORT-NAME>Unknown</SHORT-NAME>"
            "</UNKNOWN-ALT>"
            "</DYNAMIC-PART-ALTERNATIVES>",
        )
        warning_parser.readDynamicPartDynamicPartAlternatives(element, part)
        assert len(part.getDynamicPartAlternatives()) == 0

    def test_readDynamicPart_delegates(self, parser):
        from armodel.models import DynamicPart
        part = DynamicPart()
        element = _snip(
            "<SEGMENT-POSITIONS>"
            "<SEGMENT-POSITION>"
            "<SEGMENT-LENGTH>4</SEGMENT-LENGTH>"
            "</SEGMENT-POSITION>"
            "</SEGMENT-POSITIONS>"
            "<DYNAMIC-PART-ALTERNATIVES>"
            "<DYNAMIC-PART-ALTERNATIVE>"
            '<SELECTOR-FIELD-CODE>1</SELECTOR-FIELD-CODE>'
            "</DYNAMIC-PART-ALTERNATIVE>"
            "</DYNAMIC-PART-ALTERNATIVES>",
        )
        parser.readDynamicPart(element, part)
        assert len(part.getSegmentPositions()) == 1
        assert len(part.getDynamicPartAlternatives()) == 1

    def test_readStaticPart_sets_fields(self, parser):
        from armodel.models import StaticPart
        part = StaticPart()
        element = _snip(
            "<SEGMENT-POSITIONS>"
            "<SEGMENT-POSITION>"
            "<SEGMENT-LENGTH>8</SEGMENT-LENGTH>"
            "</SEGMENT-POSITION>"
            "</SEGMENT-POSITIONS>"
            '<I-PDU-REF DEST="I-PDU">/pdus/Static</I-PDU-REF>',
        )
        parser.readStaticPart(element, part)
        assert len(part.getSegmentPositions()) == 1
        assert part.getIPduRef() is not None
        assert part.getIPduRef().getValue() == "/pdus/Static"


class TestMultiplexedIPduHandlers:
    """Tests for MultiplexedIPdu dynamic/static part handlers."""

    def test_readMultiplexedIPduDynamicParts_with_part(self, parser):
        from armodel.models import MultiplexedIPdu
        ipdu = MultiplexedIPdu(parent=_autosar_root(), short_name="muxIPdu")
        element = _snip(
            "<DYNAMIC-PARTS>"
            "<DYNAMIC-PART>"
            "<DYNAMIC-PART-ALTERNATIVES>"
            "<DYNAMIC-PART-ALTERNATIVE>"
            '<SELECTOR-FIELD-CODE>1</SELECTOR-FIELD-CODE>'
            "</DYNAMIC-PART-ALTERNATIVE>"
            "</DYNAMIC-PART-ALTERNATIVES>"
            "</DYNAMIC-PART>"
            "</DYNAMIC-PARTS>",
        )
        parser.readMultiplexedIPduDynamicParts(element, ipdu)
        assert ipdu.getDynamicPart() is not None
        assert len(ipdu.getDynamicPart().getDynamicPartAlternatives()) == 1

    def test_readMultiplexedIPduDynamicParts_unknown_warning(self, warning_parser):
        from armodel.models import MultiplexedIPdu
        ipdu = MultiplexedIPdu(parent=_autosar_root(), short_name="muxIPdu")
        element = _snip(
            "<DYNAMIC-PARTS>"
            "<UNKNOWN-PART>"
            "<SHORT-NAME>Unknown</SHORT-NAME>"
            "</UNKNOWN-PART>"
            "</DYNAMIC-PARTS>",
        )
        warning_parser.readMultiplexedIPduDynamicParts(element, ipdu)
        assert ipdu.getDynamicPart() is None

    def test_readMultiplexedIPduStaticParts_with_part(self, parser):
        from armodel.models import MultiplexedIPdu
        ipdu = MultiplexedIPdu(parent=_autosar_root(), short_name="muxIPdu")
        element = _snip(
            "<STATIC-PARTS>"
            "<STATIC-PART>"
            '<I-PDU-REF DEST="I-PDU">/pdus/Static</I-PDU-REF>'
            "</STATIC-PART>"
            "</STATIC-PARTS>",
        )
        parser.readMultiplexedIPduStaticParts(element, ipdu)
        assert ipdu.getStaticPart() is not None
        assert ipdu.getStaticPart().getIPduRef().getValue() == "/pdus/Static"

    def test_readMultiplexedIPduStaticParts_unknown_warning(self, warning_parser):
        from armodel.models import MultiplexedIPdu
        ipdu = MultiplexedIPdu(parent=_autosar_root(), short_name="muxIPdu")
        element = _snip(
            "<STATIC-PARTS>"
            "<UNKNOWN-PART>"
            "<SHORT-NAME>Unknown</SHORT-NAME>"
            "</UNKNOWN-PART>"
            "</STATIC-PARTS>",
        )
        warning_parser.readMultiplexedIPduStaticParts(element, ipdu)
        assert ipdu.getStaticPart() is None

    def test_readMultiplexedIPdu_full(self, parser):
        from armodel.models import MultiplexedIPdu
        ipdu = MultiplexedIPdu(parent=_autosar_root(), short_name="muxIPdu")
        element = _snip(
            "<SHORT-NAME>muxIPdu</SHORT-NAME>"
            "<DYNAMIC-PARTS>"
            "<DYNAMIC-PART>"
            "<DYNAMIC-PART-ALTERNATIVES>"
            "<DYNAMIC-PART-ALTERNATIVE>"
            '<SELECTOR-FIELD-CODE>1</SELECTOR-FIELD-CODE>'
            "</DYNAMIC-PART-ALTERNATIVE>"
            "</DYNAMIC-PART-ALTERNATIVES>"
            "</DYNAMIC-PART>"
            "</DYNAMIC-PARTS>"
            "<SELECTOR-FIELD-BYTE-ORDER>MOST-SIGNIFICANT-BYTE-LAST</SELECTOR-FIELD-BYTE-ORDER>"
            "<SELECTOR-FIELD-LENGTH>4</SELECTOR-FIELD-LENGTH>"
            "<SELECTOR-FIELD-START-POSITION>0</SELECTOR-FIELD-START-POSITION>"
            "<STATIC-PARTS>"
            "<STATIC-PART>"
            '<I-PDU-REF DEST="I-PDU">/pdus/Static</I-PDU-REF>'
            "</STATIC-PART>"
            "</STATIC-PARTS>"
            "<TRIGGER-MODE>ONE-SHOT</TRIGGER-MODE>"
            "<UNUSED-BIT-PATTERN>255</UNUSED-BIT-PATTERN>",
            root_tag="MULTIPLEXED-I-PDU",
        )
        parser.readMultiplexedIPdu(element, ipdu)
        assert ipdu.getShortName() == "muxIPdu"
        assert ipdu.getDynamicPart() is not None
        assert ipdu.getStaticPart() is not None
        assert ipdu.getSelectorFieldByteOrder().getValue() == "MOST-SIGNIFICANT-BYTE-LAST"
        assert ipdu.getSelectorFieldLength().getValue() == 4
        assert ipdu.getSelectorFieldStartPosition().getValue() == 0
        assert ipdu.getTriggerMode().getValue() == "ONE-SHOT"
        assert ipdu.getUnusedBitPattern().getValue() == 255


class TestUserDefinedAndGeneralPurposePduHandlers:
    """Tests for UserDefinedIPdu, UserDefinedPdu, GeneralPurposePdu, GeneralPurposeIPdu."""

    def test_readUserDefinedIPdu_sets_cddType(self, parser):
        from armodel.models import UserDefinedIPdu
        ipdu = UserDefinedIPdu(parent=_autosar_root(), short_name="udIPdu")
        element = _snip(
            "<SHORT-NAME>udIPdu</SHORT-NAME>"
            "<CDD-TYPE>MyCdd</CDD-TYPE>",
            root_tag="USER-DEFINED-I-PDU",
        )
        parser.readUserDefinedIPdu(element, ipdu)
        assert ipdu.getShortName() == "udIPdu"
        assert ipdu.getCddType() is not None
        assert ipdu.getCddType().getValue() == "MyCdd"

    def test_readUserDefinedIPdu_empty(self, parser):
        from armodel.models import UserDefinedIPdu
        ipdu = UserDefinedIPdu(parent=_autosar_root(), short_name="udIPdu")
        element = _snip(
            "<SHORT-NAME>udIPdu</SHORT-NAME>",
            root_tag="USER-DEFINED-I-PDU",
        )
        parser.readUserDefinedIPdu(element, ipdu)
        assert ipdu.getCddType() is None

    def test_readUserDefinedPdu_sets_cddType(self, parser):
        from armodel.models import UserDefinedPdu
        pdu = UserDefinedPdu(parent=_autosar_root(), short_name="udPdu")
        element = _snip(
            "<SHORT-NAME>udPdu</SHORT-NAME>"
            "<CDD-TYPE>MyCdd</CDD-TYPE>",
            root_tag="USER-DEFINED-PDU",
        )
        parser.readUserDefinedPdu(element, pdu)
        assert pdu.getShortName() == "udPdu"
        assert pdu.getCddType() is not None
        assert pdu.getCddType().getValue() == "MyCdd"

    def test_readUserDefinedPdu_empty(self, parser):
        from armodel.models import UserDefinedPdu
        pdu = UserDefinedPdu(parent=_autosar_root(), short_name="udPdu")
        element = _snip(
            "<SHORT-NAME>udPdu</SHORT-NAME>",
            root_tag="USER-DEFINED-PDU",
        )
        parser.readUserDefinedPdu(element, pdu)
        assert pdu.getCddType() is None

    def test_readGeneralPurposePdu_minimal(self, parser):
        from armodel.models import GeneralPurposePdu
        pdu = GeneralPurposePdu(parent=_autosar_root(), short_name="gpPdu")
        element = _snip(
            "<SHORT-NAME>gpPdu</SHORT-NAME>",
            root_tag="GENERAL-PURPOSE-PDU",
        )
        parser.readGeneralPurposePdu(element, pdu)
        assert pdu.getShortName() == "gpPdu"

    def test_readGeneralPurposeIPdu_minimal(self, parser):
        from armodel.models import GeneralPurposeIPdu
        ipdu = GeneralPurposeIPdu(parent=_autosar_root(), short_name="gpIPdu")
        element = _snip(
            "<SHORT-NAME>gpIPdu</SHORT-NAME>",
            root_tag="GENERAL-PURPOSE-I-PDU",
        )
        parser.readGeneralPurposeIPdu(element, ipdu)
        assert ipdu.getShortName() == "gpIPdu"


class TestSecureCommunicationHandlers:
    """Tests for SecureCommunication props handlers."""

    def test_readSecureCommunicationAuthenticationProps_with_mock(self, parser):
        props = MagicMock()
        element = _snip(
            "<SHORT-NAME>authProps</SHORT-NAME>"
            "<AUTH-ALGORITHM>AES-128</AUTH-ALGORITHM>"
            "<AUTH-INFO-TX-LENGTH>16</AUTH-INFO-TX-LENGTH>",
            root_tag="SECURE-COMMUNICATION-AUTHENTICATION-PROPS",
        )
        parser.readSecureCommunicationAuthenticationProps(element, props)
        assert props.setAuthAlgorithm.called
        assert props.setAuthAlgorithm.return_value.setAuthInfoTxLength.called

    def test_readSecureCommunicationAuthenticationProps_empty_with_mock(self, parser):
        props = MagicMock()
        element = _snip(
            "<SHORT-NAME>authProps</SHORT-NAME>",
            root_tag="SECURE-COMMUNICATION-AUTHENTICATION-PROPS",
        )
        parser.readSecureCommunicationAuthenticationProps(element, props)
        assert props.setAuthAlgorithm.called
        assert props.setAuthAlgorithm.return_value.setAuthInfoTxLength.called

    def test_readSecureCommunicationPropsSetAuthenticationProps_with_props(self, parser):
        props_set = MagicMock()
        props_set.createSecureCommunicationAuthenticationProps.return_value = MagicMock()
        element = _snip(
            "<AUTHENTICATION-PROPSS>"
            "<SECURE-COMMUNICATION-AUTHENTICATION-PROPS>"
            "<SHORT-NAME>authProps</SHORT-NAME>"
            "<AUTH-ALGORITHM>AES-128</AUTH-ALGORITHM>"
            "</SECURE-COMMUNICATION-AUTHENTICATION-PROPS>"
            "</AUTHENTICATION-PROPSS>",
        )
        parser.readSecureCommunicationPropsSetAuthenticationProps(element, props_set)
        props_set.createSecureCommunicationAuthenticationProps.assert_called_once_with("authProps")

    def test_readSecureCommunicationPropsSetAuthenticationProps_unknown_warning(self, warning_parser):
        from armodel.models import SecureCommunicationPropsSet
        props_set = SecureCommunicationPropsSet(parent=_autosar_root(), short_name="propsSet")
        element = _snip(
            "<AUTHENTICATION-PROPSS>"
            "<UNKNOWN-AUTH-PROPS>"
            "<SHORT-NAME>Unknown</SHORT-NAME>"
            "</UNKNOWN-AUTH-PROPS>"
            "</AUTHENTICATION-PROPSS>",
        )
        warning_parser.readSecureCommunicationPropsSetAuthenticationProps(element, props_set)

    def test_readSecureCommunicationFreshnessProps_sets_fields(self, parser):
        from armodel.models import SecureCommunicationFreshnessProps
        props = SecureCommunicationFreshnessProps(parent=_autosar_root(), short_name="freshProps")
        element = _snip(
            "<SHORT-NAME>freshProps</SHORT-NAME>"
            "<FRESHNESS-VALUE-LENGTH>16</FRESHNESS-VALUE-LENGTH>"
            "<FRESHNESS-VALUE-TX-LENGTH>8</FRESHNESS-VALUE-TX-LENGTH>",
            root_tag="SECURE-COMMUNICATION-FRESHNESS-PROPS",
        )
        parser.readSecureCommunicationFreshnessProps(element, props)
        assert props.getShortName() == "freshProps"
        assert props.getFreshnessValueLength() is not None
        assert props.getFreshnessValueLength().getValue() == "16"
        assert props.getFreshnessValueTxLength() is not None
        assert props.getFreshnessValueTxLength().getValue() == 8

    def test_readSecureCommunicationFreshnessProps_empty(self, parser):
        from armodel.models import SecureCommunicationFreshnessProps
        props = SecureCommunicationFreshnessProps(parent=_autosar_root(), short_name="freshProps")
        element = _snip(
            "<SHORT-NAME>freshProps</SHORT-NAME>",
            root_tag="SECURE-COMMUNICATION-FRESHNESS-PROPS",
        )
        parser.readSecureCommunicationFreshnessProps(element, props)
        assert props.getFreshnessValueLength() is None
        assert props.getFreshnessValueTxLength() is None

    def test_readSecureCommunicationPropsSetFreshnessProps_with_props(self, parser):
        props_set = MagicMock()
        props_set.createSecureCommunicationFreshnessProps.return_value = MagicMock()
        element = _snip(
            "<FRESHNESS-PROPSS>"
            "<SECURE-COMMUNICATION-FRESHNESS-PROPS>"
            "<SHORT-NAME>freshProps</SHORT-NAME>"
            "<FRESHNESS-VALUE-LENGTH>16</FRESHNESS-VALUE-LENGTH>"
            "</SECURE-COMMUNICATION-FRESHNESS-PROPS>"
            "</FRESHNESS-PROPSS>",
        )
        parser.readSecureCommunicationPropsSetFreshnessProps(element, props_set)
        props_set.createSecureCommunicationFreshnessProps.assert_called_once_with("freshProps")

    def test_readSecureCommunicationPropsSetFreshnessProps_unknown_warning(self, warning_parser):
        from armodel.models import SecureCommunicationPropsSet
        props_set = SecureCommunicationPropsSet(parent=_autosar_root(), short_name="propsSet")
        element = _snip(
            "<FRESHNESS-PROPSS>"
            "<UNKNOWN-FRESH-PROPS>"
            "<SHORT-NAME>Unknown</SHORT-NAME>"
            "</UNKNOWN-FRESH-PROPS>"
            "</FRESHNESS-PROPSS>",
        )
        warning_parser.readSecureCommunicationPropsSetFreshnessProps(element, props_set)

    def test_readSecureCommunicationPropsSet_minimal(self, parser):
        from armodel.models import SecureCommunicationPropsSet
        props_set = SecureCommunicationPropsSet(parent=_autosar_root(), short_name="propsSet")
        element = _snip(
            "<SHORT-NAME>propsSet</SHORT-NAME>",
            root_tag="SECURE-COMMUNICATION-PROPS-SET",
        )
        parser.readSecureCommunicationPropsSet(element, props_set)
        assert props_set.getShortName() == "propsSet"


class TestSoAdRoutingGroupHandler:
    """Tests for readSoAdRoutingGroup."""

    def test_readSoAdRoutingGroup_sets_eventGroupControlType(self, parser):
        from armodel.models import SoAdRoutingGroup
        group = SoAdRoutingGroup(parent=_autosar_root(), short_name="routeGroup")
        element = _snip(
            "<SHORT-NAME>routeGroup</SHORT-NAME>"
            "<EVENT-GROUP-CONTROL-TYPE>POSITIVE</EVENT-GROUP-CONTROL-TYPE>",
            root_tag="SO-AD-ROUTING-GROUP",
        )
        parser.readSoAdRoutingGroup(element, group)
        assert group.getShortName() == "routeGroup"
        assert group.getEventGroupControlType() is not None
        assert group.getEventGroupControlType().getValue() == "POSITIVE"

    def test_readSoAdRoutingGroup_empty(self, parser):
        from armodel.models import SoAdRoutingGroup
        group = SoAdRoutingGroup(parent=_autosar_root(), short_name="routeGroup")
        element = _snip(
            "<SHORT-NAME>routeGroup</SHORT-NAME>",
            root_tag="SO-AD-ROUTING-GROUP",
        )
        parser.readSoAdRoutingGroup(element, group)
        assert group.getEventGroupControlType() is None


# === Migrated from test_arxml_parser_remaining_gaps.py ===

class TestPduAndSecureCommunication:
    def test_readISignalToIPduMapping_sets_refs(self, parser):
        from armodel.models import ISignalToIPduMapping
        mapping = ISignalToIPduMapping(
            parent=MagicMock(), short_name="M"
        )
        element = _snip(
            '<I-SIGNAL-REF DEST="I-SIGNAL">/is</I-SIGNAL-REF>'
            "<PACKING-BYTE-ORDER>MOST-SIGNIFICANT-BYTE-LAST</PACKING-BYTE-ORDER>"
            "<START-POSITION>0</START-POSITION>"
            "<TRANSFER-PROPERTY>TRIGGERED</TRANSFER-PROPERTY>"
        )
        parser.readISignalToIPduMapping(element, mapping)
        assert mapping.getISignalRef() is not None
        assert mapping.getPackingByteOrder() is not None

    def test_readNmPduISignalToIPduMappings_creates_mapping(
        self, parser
    ):
        from armodel.models import NmPdu
        pdu = NmPdu(parent=MagicMock(), short_name="Np")
        element = _snip(
            "<I-SIGNAL-TO-I-PDU-MAPPINGS>"
            "<I-SIGNAL-TO-I-PDU-MAPPING>"
            "<SHORT-NAME>m</SHORT-NAME>"
            "</I-SIGNAL-TO-I-PDU-MAPPING>"
            "</I-SIGNAL-TO-I-PDU-MAPPINGS>"
        )
        parser.readNmPduISignalToIPduMappings(element, pdu)
        assert len(pdu.getISignalToIPduMappings()) == 1

    def test_readNmPduISignalToIPduMappings_unsupported_warns(
        self, warning_parser, caplog
    ):
        from armodel.models import NmPdu
        pdu = NmPdu(parent=MagicMock(), short_name="Np")
        element = _snip(
            "<I-SIGNAL-TO-I-PDU-MAPPINGS><BAD/></I-SIGNAL-TO-I-PDU-MAPPINGS>"
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readNmPduISignalToIPduMappings(element, pdu)
        assert any("Unsupported ISignalToIPduMapping" in r.getMessage()
                   for r in caplog.records)

    def test_getSecureCommunicationProps_sets_props(self, parser):
        element = _snip(
            "<SECURE-COMMUNICATION-PROPS>"
            "<AUTH-DATA-FRESHNESS-LENGTH>16</AUTH-DATA-FRESHNESS-LENGTH>"
            "<AUTH-DATA-FRESHNESS-START-POSITION>0</AUTH-DATA-FRESHNESS-START-POSITION>"
            "<AUTH-INFO-TX-LENGTH>8</AUTH-INFO-TX-LENGTH>"
            "</SECURE-COMMUNICATION-PROPS>"
        )
        result = parser.getSecureCommunicationProps(
            element, "SECURE-COMMUNICATION-PROPS"
        )
        assert result is not None
        assert result.getAuthDataFreshnessLength().getValue() == 16


# ==================== NmConfig (L3981, L4072) ====================



# === Migrated from test_arxml_parser_remaining_gaps.py ===

class TestBufferProperties:
    def test_readBufferPropertiesBufferComputation_sets_scale(
        self, parser
    ):
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import BufferProperties
        props = BufferProperties()
        element = _snip(
            "<BUFFER-COMPUTATION>"
            "<SHORT-LABEL>bc</SHORT-LABEL>"
            "<LOWER-LIMIT>0</LOWER-LIMIT>"
            "<UPPER-LIMIT>100</UPPER-LIMIT>"
            "</BUFFER-COMPUTATION>"
        )
        parser.readBufferPropertiesBufferComputation(element, props)
        assert props.getBufferComputation() is not None


# ==================== ECUC ModuleDef / ContainerDef (L4461, L4480, L4484-4489, L4503, L4560, L4627-4667) ====================



# === Migrated from test_arxml_parser_remaining_gaps.py ===

class TestTargetIPduRef:
    def test_getTargetIPduRef_with_child(self, parser):
        element = _snip(
            "<TARGET-I-PDU-REF>"
            '<TARGET-I-PDU-REF DEST="I-PDU">/ipdu</TARGET-I-PDU-REF>'
            "</TARGET-I-PDU-REF>"
        )
        result = parser.getTargetIPduRef(
            element, "TARGET-I-PDU-REF"
        )
        assert result is not None
        assert result.getTargetIPdu().getValue() == "/ipdu"


# ==================== EcucParameterValue (L5081, L5103) ====================


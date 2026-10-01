"""
Tests for reading the COMMON-PROPERTIES element — DiagnosticCommonProps, Table 4.19 (p.65, R23-11).

DiagnosticCommonProps (Base = ARObject, <<atpVariation>> class) serializes its
attributes inside the DIAGNOSTIC-COMMON-PROPS-VARIANTS/DIAGNOSTIC-COMMON-PROPS-
CONDITIONAL wrapper (XSD group DIAGNOSTIC-COMMON-PROPS, AUTOSAR_00052.xsd
l.33083; the conditional is read transparently into the owning object per the
atpVariation convention). The class-level diagnosticCommonPropsVariant split
wrapper carries no PDF attribute row and is not modeled (Rule 0015); the XSD-only
removed attributes (agingRequiresTestedCycle, clearDtcLimitation, ...) are not
modeled either.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_common_props.py
"""

from tests.test_armodel.parser._helpers import _snip

_CONDITIONAL_INNER = (
    "<AUTHENTICATION-TIMEOUT>0.5</AUTHENTICATION-TIMEOUT>"
    "<DEBOUNCE-ALGORITHM-PROPSS>"
    "<DIAGNOSTIC-DEBOUNCE-ALGORITHM-PROPS><SHORT-NAME>Deb1</SHORT-NAME></DIAGNOSTIC-DEBOUNCE-ALGORITHM-PROPS>"
    "<DIAGNOSTIC-DEBOUNCE-ALGORITHM-PROPS><SHORT-NAME>Deb2</SHORT-NAME></DIAGNOSTIC-DEBOUNCE-ALGORITHM-PROPS>"
    "</DEBOUNCE-ALGORITHM-PROPSS>"
    "<DEFAULT-ENDIANNESS>OPAQUE</DEFAULT-ENDIANNESS>"
    "<MAX-NUMBER-OF-REQUEST-CORRECTLY-RECEIVED-RESPONSE-PENDING>10</MAX-NUMBER-OF-REQUEST-CORRECTLY-RECEIVED-RESPONSE-PENDING>"
    "<OCCURRENCE-COUNTER-PROCESSING>CONFIRMED-DTC-BIT</OCCURRENCE-COUNTER-PROCESSING>"
    "<RESET-CONFIRMED-BIT-ON-OVERFLOW>true</RESET-CONFIRMED-BIT-ON-OVERFLOW>"
    "<RESET-PENDING-BIT-ON-OVERFLOW>false</RESET-PENDING-BIT-ON-OVERFLOW>"
    "<RESPONSE-ON-ALL-REQUEST-SIDS>false</RESPONSE-ON-ALL-REQUEST-SIDS>"
    "<RESPONSE-ON-SECOND-DECLINED-REQUEST>true</RESPONSE-ON-SECOND-DECLINED-REQUEST>"
)

_CONDITIONAL_WRAPPED = "<DIAGNOSTIC-COMMON-PROPS-VARIANTS><DIAGNOSTIC-COMMON-PROPS-CONDITIONAL>%s</DIAGNOSTIC-COMMON-PROPS-CONDITIONAL></DIAGNOSTIC-COMMON-PROPS-VARIANTS>" % _CONDITIONAL_INNER


class TestReadDiagnosticCommonProps:
    """Tests for readDiagnosticCommonProps — own element field values (Table 4.19)."""

    def _read(self, parser, inner):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import DiagnosticCommonProps

        common_props = DiagnosticCommonProps()
        element = _snip(inner, root_tag="COMMON-PROPERTIES")
        parser.readDiagnosticCommonProps(element, common_props)
        return common_props

    def test_with_field_values(self, parser):
        """Test that the CONDITIONAL wrapper attributes are read transparently with field values."""
        common_props = self._read(parser, _CONDITIONAL_WRAPPED)
        assert common_props.getAuthenticationTimeout() is not None
        assert common_props.getAuthenticationTimeout().getValue() == 0.5
        debounce_props = common_props.getDebounceAlgorithmProps()
        assert [item.getShortName() for item in debounce_props] == ["Deb1", "Deb2"]
        assert common_props.getDefaultEndianness() is not None
        assert common_props.getDefaultEndianness().getValue() == "opaque"
        assert common_props.getMaxNumberOfRequestCorrectlyReceivedResponsePending() is not None
        assert common_props.getMaxNumberOfRequestCorrectlyReceivedResponsePending().getValue() == 10
        assert common_props.getOccurrenceCounterProcessing() is not None
        assert common_props.getOccurrenceCounterProcessing().getValue() == "confirmedDtcBit"
        assert common_props.getResetConfirmedBitOnOverflow() is not None
        assert common_props.getResetConfirmedBitOnOverflow().getValue() is True
        assert common_props.getResetPendingBitOnOverflow() is not None
        assert common_props.getResetPendingBitOnOverflow().getValue() is False
        assert common_props.getResponseOnAllRequestSids() is not None
        assert common_props.getResponseOnAllRequestSids().getValue() is False
        assert common_props.getResponseOnSecondDeclinedRequest() is not None
        assert common_props.getResponseOnSecondDeclinedRequest().getValue() is True

    def test_without_conditional_wrapper(self, parser):
        """Test that a COMMON-PROPERTIES element without the CONDITIONAL wrapper leaves all fields empty."""
        common_props = self._read(parser, "")
        assert common_props.getAuthenticationTimeout() is None
        assert common_props.getDebounceAlgorithmProps() == []
        assert common_props.getDefaultEndianness() is None
        assert common_props.getMaxNumberOfRequestCorrectlyReceivedResponsePending() is None
        assert common_props.getOccurrenceCounterProcessing() is None
        assert common_props.getResetConfirmedBitOnOverflow() is None
        assert common_props.getResetPendingBitOnOverflow() is None
        assert common_props.getResponseOnAllRequestSids() is None
        assert common_props.getResponseOnSecondDeclinedRequest() is None
        assert common_props.getTypeOfEventCombinationSupported() is None

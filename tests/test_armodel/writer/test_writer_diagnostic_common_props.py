"""
Tests for writing the COMMON-PROPERTIES element — DiagnosticCommonProps, Table 4.19 (p.65, R23-11).

DiagnosticCommonProps (Base = ARObject, <<atpVariation>> class) serializes its
attributes inside the DIAGNOSTIC-COMMON-PROPS-VARIANTS/DIAGNOSTIC-COMMON-PROPS-
CONDITIONAL wrapper (XSD group DIAGNOSTIC-COMMON-PROPS, AUTOSAR_00052.xsd
l.33083). The writer reads the model via the get* getters; the dispatch entry is
DiagnosticContributionSet → writeDiagnosticCommonProps (Aggregated by
DiagnosticContributionSet.commonProperties).

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_common_props.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import DiagnosticCommonProps
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticContributionSet
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    ByteOrderEnum,
    DiagnosticEventCombinationBehaviorEnum,
    DiagnosticOccurrenceCounterProcessingEnum,
    PositiveInteger,
    TimeValue,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteDiagnosticCommonProps:
    """Tests for writeDiagnosticCommonProps — own element field values (Table 4.19)."""

    def test_write_field_values_in_xsd_order(self):
        """Test that the CONDITIONAL wrapper attributes are emitted with field values in XSD order."""
        common_props = DiagnosticCommonProps()
        timeout = TimeValue()
        timeout.setValue(0.5)
        common_props.setAuthenticationTimeout(timeout)
        common_props.createDebounceAlgorithmProps("Deb1")
        common_props.setDefaultEndianness(ByteOrderEnum().setValue(ByteOrderEnum.OPAQUE))
        max_number = PositiveInteger()
        max_number.setValue("10")
        common_props.setMaxNumberOfRequestCorrectlyReceivedResponsePending(max_number)
        common_props.setOccurrenceCounterProcessing(DiagnosticOccurrenceCounterProcessingEnum().setValue(DiagnosticOccurrenceCounterProcessingEnum.CONFIRMED_DTC_BIT))
        confirmed = Boolean()
        confirmed.setValue(True)
        common_props.setResetConfirmedBitOnOverflow(confirmed)
        pending = Boolean()
        pending.setValue(False)
        common_props.setResetPendingBitOnOverflow(pending)
        all_sids = Boolean()
        all_sids.setValue(False)
        common_props.setResponseOnAllRequestSids(all_sids)
        second_declined = Boolean()
        second_declined.setValue(True)
        common_props.setResponseOnSecondDeclinedRequest(second_declined)
        common_props.setTypeOfEventCombinationSupported(DiagnosticEventCombinationBehaviorEnum().setValue(DiagnosticEventCombinationBehaviorEnum.EVENT_COMBINATION_ON_STORAGE))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticCommonProps(parent, common_props)

        child = parent.find("COMMON-PROPERTIES")
        assert child is not None
        conditional = child.find("DIAGNOSTIC-COMMON-PROPS-VARIANTS/DIAGNOSTIC-COMMON-PROPS-CONDITIONAL")
        assert conditional is not None
        assert conditional.find("AUTHENTICATION-TIMEOUT").text == "0.5"
        debounce_items = conditional.findall("DEBOUNCE-ALGORITHM-PROPSS/DIAGNOSTIC-DEBOUNCE-ALGORITHM-PROPS")
        assert [item.find("SHORT-NAME").text for item in debounce_items] == ["Deb1"]
        assert conditional.find("DEFAULT-ENDIANNESS").text == "OPAQUE"
        assert conditional.find("MAX-NUMBER-OF-REQUEST-CORRECTLY-RECEIVED-RESPONSE-PENDING").text == "10"
        assert conditional.find("OCCURRENCE-COUNTER-PROCESSING").text == "CONFIRMED-DTC-BIT"
        assert conditional.find("RESET-CONFIRMED-BIT-ON-OVERFLOW").text == "true"
        assert conditional.find("RESET-PENDING-BIT-ON-OVERFLOW").text == "false"
        assert conditional.find("RESPONSE-ON-ALL-REQUEST-SIDS").text == "false"
        assert conditional.find("RESPONSE-ON-SECOND-DECLINED-REQUEST").text == "true"
        assert conditional.find("TYPE-OF-EVENT-COMBINATION-SUPPORTED").text == "EVENT-COMBINATION-ON-STORAGE"
        tags = [c.tag for c in conditional]
        assert tags == [
            "AUTHENTICATION-TIMEOUT",
            "DEBOUNCE-ALGORITHM-PROPSS",
            "DEFAULT-ENDIANNESS",
            "MAX-NUMBER-OF-REQUEST-CORRECTLY-RECEIVED-RESPONSE-PENDING",
            "OCCURRENCE-COUNTER-PROCESSING",
            "RESET-CONFIRMED-BIT-ON-OVERFLOW",
            "RESET-PENDING-BIT-ON-OVERFLOW",
            "RESPONSE-ON-ALL-REQUEST-SIDS",
            "RESPONSE-ON-SECOND-DECLINED-REQUEST",
            "TYPE-OF-EVENT-COMBINATION-SUPPORTED",
        ]

    def test_write_unset_fields_emits_empty_conditional(self):
        """Test that a DiagnosticCommonProps without field values emits the empty VARIANTS/CONDITIONAL chain."""
        common_props = DiagnosticCommonProps()

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticCommonProps(parent, common_props)

        child = parent.find("COMMON-PROPERTIES")
        assert child is not None
        conditional = child.find("DIAGNOSTIC-COMMON-PROPS-VARIANTS/DIAGNOSTIC-COMMON-PROPS-CONDITIONAL")
        assert conditional is not None
        assert len(list(conditional)) == 0

    def test_round_trip_via_contribution_set(self):
        """Test the full set → save → reload → assert cycle over a DiagnosticContributionSet with commonProperties."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("ContributionSets")
        contribution_set = package.createDiagnosticContributionSet("Dcs")
        common_props = DiagnosticCommonProps()
        timeout = TimeValue()
        timeout.setValue(0.5)
        common_props.setAuthenticationTimeout(timeout)
        common_props.setDefaultEndianness(ByteOrderEnum().setValue(ByteOrderEnum.MOST_SIGNIFICANT_BYTE_FIRST))
        max_number = PositiveInteger()
        max_number.setValue("10")
        common_props.setMaxNumberOfRequestCorrectlyReceivedResponsePending(max_number)
        common_props.setOccurrenceCounterProcessing(DiagnosticOccurrenceCounterProcessingEnum().setValue(DiagnosticOccurrenceCounterProcessingEnum.TEST_FAILED_BIT))
        common_props.setTypeOfEventCombinationSupported(DiagnosticEventCombinationBehaviorEnum().setValue(DiagnosticEventCombinationBehaviorEnum.EVENT_COMBINATION_ON_RETRIEVAL))
        confirmed = Boolean()
        confirmed.setValue(True)
        common_props.setResetConfirmedBitOnOverflow(confirmed)
        contribution_set.setCommonProperties(common_props)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            contribution_set_2 = package_2.getElement("Dcs", DiagnosticContributionSet)
            assert contribution_set_2 is not None
            common_props_2 = contribution_set_2.getCommonProperties()
            assert common_props_2 is not None
            assert common_props_2.getAuthenticationTimeout() is not None
            assert common_props_2.getAuthenticationTimeout().getValue() == 0.5
            assert common_props_2.getDefaultEndianness() is not None
            assert common_props_2.getDefaultEndianness().getValue() == "mostSignificantByteFirst"
            assert common_props_2.getMaxNumberOfRequestCorrectlyReceivedResponsePending() is not None
            assert common_props_2.getMaxNumberOfRequestCorrectlyReceivedResponsePending().getValue() == 10
            assert common_props_2.getOccurrenceCounterProcessing() is not None
            assert common_props_2.getOccurrenceCounterProcessing().getValue() == "testFailedBit"
            assert common_props_2.getTypeOfEventCombinationSupported() is not None
            assert common_props_2.getTypeOfEventCombinationSupported().getValue() == "eventCombinationOnRetrieval"
            assert common_props_2.getResetConfirmedBitOnOverflow() is not None
            assert common_props_2.getResetConfirmedBitOnOverflow().getValue() is True
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_round_trip_empty(self):
        """Test that an empty DiagnosticCommonProps round-trips with all fields empty."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("ContributionSets")
        contribution_set = package.createDiagnosticContributionSet("Dcs")
        contribution_set.setCommonProperties(DiagnosticCommonProps())

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            contribution_set_2 = package_2.getElement("Dcs", DiagnosticContributionSet)
            assert contribution_set_2 is not None
            common_props_2 = contribution_set_2.getCommonProperties()
            assert common_props_2 is not None
            assert common_props_2.getAuthenticationTimeout() is None
            assert common_props_2.getDebounceAlgorithmProps() == []
            assert common_props_2.getDefaultEndianness() is None
            assert common_props_2.getOccurrenceCounterProcessing() is None
            assert common_props_2.getResetConfirmedBitOnOverflow() is None
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

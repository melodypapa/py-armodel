"""
Tests for writing DIAGNOSTIC-DEBOUNCE-ALGORITHM-PROPS elements —
DiagnosticDebounceAlgorithmProps, Table 4.187 (p.196, R23-11).

DiagnosticDebounceAlgorithmProps (Base most-derived Identifiable) aggregates one
polymorphic 0..1 debounceAlgorithm (XSD wrapper DEBOUNCE-ALGORITHM holding a choice of
DIAG-EVENT-DEBOUNCE-COUNTER-BASED / DIAG-EVENT-DEBOUNCE-MONITOR-INTERNAL /
DIAG-EVENT-DEBOUNCE-TIME-BASED — XSD group DIAGNOSTIC-DEBOUNCE-ALGORITHM-PROPS,
AUTOSAR_00052.xsd l.34682) plus the 0..1 debounceBehavior enum token and the 0..1
debounceCounterStorage boolean. The writer reads the model via the get* getters; the
dispatch entry is DiagnosticCommonProps → writeDiagnosticDebounceAlgorithmProps
(Aggregated by DiagnosticCommonProps.debounceAlgorithmProps). XML element order
follows the XSD sequenceOffset: DEBOUNCE-ALGORITHM, DEBOUNCE-BEHAVIOR,
DEBOUNCE-COUNTER-STORAGE.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_debounce_algorithm_props.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import DiagEventDebounceTimeBased
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import DiagnosticCommonProps
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticContributionSet
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import DiagnosticDebounceAlgorithmProps
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, DiagnosticDebounceBehaviorEnum, Integer, TimeValue
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _behavior() -> DiagnosticDebounceBehaviorEnum:
    behavior = DiagnosticDebounceBehaviorEnum()
    behavior.setValue(DiagnosticDebounceBehaviorEnum.FREEZE)
    return behavior


class TestWriteDiagnosticDebounceAlgorithmProps:
    """Tests for writeDiagnosticDebounceAlgorithmProps — own element field values (Table 4.187)."""

    def test_write_counter_based_algorithm_in_xsd_order(self):
        """Test that the DEBOUNCE-ALGORITHM choice and DEBOUNCE-COUNTER-STORAGE are emitted in XSD order."""
        debounce_props = DiagnosticDebounceAlgorithmProps(AUTOSAR.getInstance(), "DebounceProps1")
        algorithm = debounce_props.createDiagEventDebounceCounterBased("CounterBased")
        failed_threshold = Integer()
        failed_threshold.setValue(3)
        algorithm.setCounterFailedThreshold(failed_threshold)
        storage = Boolean()
        storage.setValue(True)
        debounce_props.setDebounceCounterStorage(storage)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticDebounceAlgorithmProps(parent, debounce_props)

        child = parent.find("DIAGNOSTIC-DEBOUNCE-ALGORITHM-PROPS")
        assert child is not None
        assert child.find("SHORT-NAME").text == "DebounceProps1"
        algorithm_element = child.find("DEBOUNCE-ALGORITHM/DIAG-EVENT-DEBOUNCE-COUNTER-BASED")
        assert algorithm_element is not None
        assert algorithm_element.find("COUNTER-FAILED-THRESHOLD").text == "3"
        assert child.find("DEBOUNCE-COUNTER-STORAGE").text == "true"
        tags = [c.tag for c in child]
        assert tags == ["SHORT-NAME", "DEBOUNCE-ALGORITHM", "DEBOUNCE-COUNTER-STORAGE"]

    def test_write_monitor_internal_algorithm(self):
        """Test that the DEBOUNCE-ALGORITHM wrapper emits a DIAG-EVENT-DEBOUNCE-MONITOR-INTERNAL."""
        debounce_props = DiagnosticDebounceAlgorithmProps(AUTOSAR.getInstance(), "DebounceProps1")
        debounce_props.createDiagEventDebounceMonitorInternal("MonitorInternal")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticDebounceAlgorithmProps(parent, debounce_props)

        child = parent.find("DIAGNOSTIC-DEBOUNCE-ALGORITHM-PROPS")
        algorithm_element = child.find("DEBOUNCE-ALGORITHM/DIAG-EVENT-DEBOUNCE-MONITOR-INTERNAL")
        assert algorithm_element is not None
        assert algorithm_element.find("SHORT-NAME").text == "MonitorInternal"

    def test_write_time_based_algorithm(self):
        """Test that the DEBOUNCE-ALGORITHM wrapper emits a DIAG-EVENT-DEBOUNCE-TIME-BASED with field values."""
        debounce_props = DiagnosticDebounceAlgorithmProps(AUTOSAR.getInstance(), "DebounceProps1")
        algorithm = debounce_props.createDiagEventDebounceTimeBased("TimeBased")
        failed_threshold = TimeValue()
        failed_threshold.setValue(0.5)
        algorithm.setTimeFailedThreshold(failed_threshold)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticDebounceAlgorithmProps(parent, debounce_props)

        child = parent.find("DIAGNOSTIC-DEBOUNCE-ALGORITHM-PROPS")
        algorithm_element = child.find("DEBOUNCE-ALGORITHM/DIAG-EVENT-DEBOUNCE-TIME-BASED")
        assert algorithm_element is not None
        assert algorithm_element.find("SHORT-NAME").text == "TimeBased"
        assert algorithm_element.find("TIME-FAILED-THRESHOLD").text == "0.5"

    def test_write_debounce_behavior_token(self):
        """Test that the debounceBehavior enum is emitted as the DEBOUNCE-BEHAVIOR XML token."""
        debounce_props = DiagnosticDebounceAlgorithmProps(AUTOSAR.getInstance(), "DebounceProps1")
        debounce_props.setDebounceBehavior(_behavior())

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticDebounceAlgorithmProps(parent, debounce_props)

        child = parent.find("DIAGNOSTIC-DEBOUNCE-ALGORITHM-PROPS")
        assert child.find("DEBOUNCE-BEHAVIOR").text == "FREEZE"

    def test_write_unset_fields_emits_short_name_only(self):
        """Test that props without own values emit the identity only."""
        debounce_props = DiagnosticDebounceAlgorithmProps(AUTOSAR.getInstance(), "DebounceProps1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticDebounceAlgorithmProps(parent, debounce_props)

        child = parent.find("DIAGNOSTIC-DEBOUNCE-ALGORITHM-PROPS")
        assert child is not None
        assert child.find("DEBOUNCE-ALGORITHM") is None
        assert child.find("DEBOUNCE-BEHAVIOR") is None
        assert child.find("DEBOUNCE-COUNTER-STORAGE") is None

    def test_write_via_common_props(self):
        """Test that writeDiagnosticCommonProps emits the props items through the helper."""
        common_props = DiagnosticCommonProps()
        debounce_props = common_props.createDebounceAlgorithmProps("DebounceProps1")
        debounce_props.createDiagEventDebounceTimeBased("TimeBased")
        storage = Boolean()
        storage.setValue(False)
        debounce_props.setDebounceCounterStorage(storage)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticCommonProps(parent, common_props)

        conditional = parent.find("COMMON-PROPERTIES/DIAGNOSTIC-COMMON-PROPS-VARIANTS/DIAGNOSTIC-COMMON-PROPS-CONDITIONAL")
        assert conditional is not None
        item = conditional.find("DEBOUNCE-ALGORITHM-PROPSS/DIAGNOSTIC-DEBOUNCE-ALGORITHM-PROPS")
        assert item is not None
        assert item.find("SHORT-NAME").text == "DebounceProps1"
        assert item.find("DEBOUNCE-ALGORITHM/DIAG-EVENT-DEBOUNCE-TIME-BASED") is not None
        assert item.find("DEBOUNCE-COUNTER-STORAGE").text == "false"

    def test_round_trip_via_contribution_set(self):
        """Test the full set → save → reload → assert cycle with field values one level down."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("ContributionSets")
        contribution_set = package.createDiagnosticContributionSet("Dcs")
        common_props = DiagnosticCommonProps()
        debounce_props = common_props.createDebounceAlgorithmProps("DebounceProps1")
        algorithm = debounce_props.createDiagEventDebounceTimeBased("TimeBased")
        failed_threshold = TimeValue()
        failed_threshold.setValue(0.5)
        algorithm.setTimeFailedThreshold(failed_threshold)
        storage = Boolean()
        storage.setValue(True)
        debounce_props.setDebounceCounterStorage(storage)
        debounce_props.setDebounceBehavior(_behavior())
        contribution_set.setCommonProperties(common_props)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            contribution_set_2 = package_2.getReferrableElement("Dcs", DiagnosticContributionSet)
            assert contribution_set_2 is not None
            common_props_2 = contribution_set_2.getCommonProperties()
            assert common_props_2 is not None
            debounce_props_2 = common_props_2.getDebounceAlgorithmProps()
            assert len(debounce_props_2) == 1
            assert debounce_props_2[0].getShortName() == "DebounceProps1"
            algorithm_2 = debounce_props_2[0].getDebounceAlgorithm()
            assert isinstance(algorithm_2, DiagEventDebounceTimeBased)
            assert algorithm_2.getShortName() == "TimeBased"
            assert algorithm_2.getTimeFailedThreshold().getValue() == 0.5
            assert debounce_props_2[0].getDebounceCounterStorage().getValue() is True
            assert debounce_props_2[0].getDebounceBehavior().getValue() == DiagnosticDebounceBehaviorEnum.FREEZE
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_round_trip_empty(self):
        """Test that props without own values round-trip with all fields unset."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("ContributionSets")
        contribution_set = package.createDiagnosticContributionSet("Dcs")
        common_props = DiagnosticCommonProps()
        common_props.createDebounceAlgorithmProps("DebounceProps1")
        contribution_set.setCommonProperties(common_props)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            contribution_set_2 = package_2.getReferrableElement("Dcs", DiagnosticContributionSet)
            common_props_2 = contribution_set_2.getCommonProperties()
            debounce_props_2 = common_props_2.getDebounceAlgorithmProps()
            assert len(debounce_props_2) == 1
            assert debounce_props_2[0].getDebounceAlgorithm() is None
            assert debounce_props_2[0].getDebounceBehavior() is None
            assert debounce_props_2[0].getDebounceCounterStorage() is None
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

"""
Tests for writing DIAG-EVENT-DEBOUNCE-TIME-BASED elements — DiagEventDebounceTimeBased, Table 12.34 (p.260, R23-11).

DiagEventDebounceTimeBased (Base = DiagEventDebounceAlgorithm) carries the optional
time attributes TIME-BASED-FDC-THRESHOLD-STORAGE-VALUE, TIME-FAILED-THRESHOLD and
TIME-PASSED-THRESHOLD (all TIME-VALUE, 0..1, XSD group order after the IDENTIFIABLE
group). The writer reads the model via the getTime* getters; the dispatch entry is
writeDiagEventDebounceAlgorithm → setDiagEventDebounceTimeBased.

Round-trip counterpart: tests/test_armodel/parser/test_diag_event_debounce_time_based.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET
from unittest.mock import MagicMock

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import DiagEventDebounceTimeBased
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import TimeValue
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _time_value(val) -> TimeValue:
    t = TimeValue()
    t.setValue(val)
    return t


class TestWriteDiagEventDebounceTimeBased:
    """Tests for setDiagEventDebounceTimeBased — own element field values (Table 12.34)."""

    def test_write_field_values(self):
        """Test that all three TIME-* elements are emitted with the field values in XSD order."""
        algorithm = DiagEventDebounceTimeBased(parent=MagicMock(), short_name="Di")
        algorithm.setTimeBasedFdcThresholdStorageValue(_time_value("0.005"))
        algorithm.setTimeFailedThreshold(_time_value("1.5"))
        algorithm.setTimePassedThreshold(_time_value("2.0"))

        parent = ET.Element("PARENT")
        ARXMLWriter().setDiagEventDebounceTimeBased(parent, algorithm)

        child = parent.find("DIAG-EVENT-DEBOUNCE-TIME-BASED")
        assert child is not None
        assert child.find("TIME-BASED-FDC-THRESHOLD-STORAGE-VALUE") is not None
        assert child.find("TIME-BASED-FDC-THRESHOLD-STORAGE-VALUE").text == "0.005"
        assert child.find("TIME-FAILED-THRESHOLD") is not None
        assert child.find("TIME-FAILED-THRESHOLD").text == "1.5"
        assert child.find("TIME-PASSED-THRESHOLD") is not None
        assert child.find("TIME-PASSED-THRESHOLD").text == "2.0"
        tags = [c.tag for c in child if c.tag != "SHORT-NAME"]
        assert tags == ["TIME-BASED-FDC-THRESHOLD-STORAGE-VALUE", "TIME-FAILED-THRESHOLD", "TIME-PASSED-THRESHOLD"]

    def test_write_empty_element(self):
        """Test that unset fields emit no TIME-* elements."""
        algorithm = DiagEventDebounceTimeBased(parent=MagicMock(), short_name="Di")

        parent = ET.Element("PARENT")
        ARXMLWriter().setDiagEventDebounceTimeBased(parent, algorithm)

        child = parent.find("DIAG-EVENT-DEBOUNCE-TIME-BASED")
        assert child is not None
        assert child.find("TIME-BASED-FDC-THRESHOLD-STORAGE-VALUE") is None
        assert child.find("TIME-FAILED-THRESHOLD") is None
        assert child.find("TIME-PASSED-THRESHOLD") is None

    def test_round_trip(self):
        """Test the full set → save → reload → assert cycle over the ServiceNeeds aggregation."""
        from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior import BswServiceDependency
        from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import DiagnosticEventNeeds

        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        desc = ar_root.createBswModuleDescription("BswMd")
        behavior = desc.createBswInternalBehavior("Beh")
        dependency = BswServiceDependency()
        needs = DiagnosticEventNeeds(dependency, "Den")
        algorithm = needs.createDiagEventDebounceTimeBased("Deb")
        algorithm.setTimeBasedFdcThresholdStorageValue(_time_value("0.005"))
        algorithm.setTimeFailedThreshold(_time_value("1.5"))
        algorithm.setTimePassedThreshold(_time_value("2.0"))
        dependency.setServiceNeeds(needs)
        behavior.addServiceDependency(dependency)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            behavior_2 = document_2.getARPackages()[0].getBswModuleDescriptions()[0].getInternalBehaviors()[0]
            needs_2 = behavior_2.getServiceDependencies()[0].getServiceNeeds()
            assert needs_2.getShortName() == "Den"
            algorithm_2 = needs_2.getDiagEventDebounceAlgorithm()
            assert algorithm_2 is not None
            assert algorithm_2.getShortName() == "Deb"
            assert algorithm_2.getTimeBasedFdcThresholdStorageValue() is not None
            assert algorithm_2.getTimeBasedFdcThresholdStorageValue().getValue() == 0.005
            assert algorithm_2.getTimeFailedThreshold() is not None
            assert algorithm_2.getTimeFailedThreshold().getValue() == 1.5
            assert algorithm_2.getTimePassedThreshold() is not None
            assert algorithm_2.getTimePassedThreshold().getValue() == 2.0
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_round_trip_empty(self):
        """Test that a debounce algorithm without field values round-trips with all fields None."""
        from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior import BswServiceDependency
        from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import DiagnosticEventNeeds

        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        desc = ar_root.createBswModuleDescription("BswMd")
        behavior = desc.createBswInternalBehavior("Beh")
        dependency = BswServiceDependency()
        needs = DiagnosticEventNeeds(dependency, "Den")
        needs.createDiagEventDebounceTimeBased("Deb")
        dependency.setServiceNeeds(needs)
        behavior.addServiceDependency(dependency)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            behavior_2 = document_2.getARPackages()[0].getBswModuleDescriptions()[0].getInternalBehaviors()[0]
            needs_2 = behavior_2.getServiceDependencies()[0].getServiceNeeds()
            algorithm_2 = needs_2.getDiagEventDebounceAlgorithm()
            assert algorithm_2 is not None
            assert algorithm_2.getShortName() == "Deb"
            assert algorithm_2.getTimeBasedFdcThresholdStorageValue() is None
            assert algorithm_2.getTimeFailedThreshold() is None
            assert algorithm_2.getTimePassedThreshold() is None
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

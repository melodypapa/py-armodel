"""
This module contains tests for the DiagEventDebounceTimeBased class
in the AUTOSAR CommonStructure ServiceNeeds module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    DiagEventDebounceAlgorithm,
    DiagEventDebounceTimeBased,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import TimeValue

SPEC_NOTE = (
    "This meta-class represents the ability to indicate that the time-based pre-debounce "
    "algorithm shall be used by the Dem for this diagnostic monitor. This is related to set "
    "the EcuC choice container DemDebounceAlgorithmClass to DemDebounceTimeBase."
)


def _time_value(val) -> TimeValue:
    t = TimeValue()
    t.setValue(val)
    return t


class TestDiagEventDebounceTimeBased:
    def test_initialization(self):
        """Test that the concrete DiagEventDebounceTimeBased is a DiagEventDebounceAlgorithm whose fields default to None"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        debounce = DiagEventDebounceTimeBased(ar_root, "TestDiagEventDebounceTimeBased")

        assert isinstance(debounce, DiagEventDebounceAlgorithm)
        assert debounce.getShortName() == "TestDiagEventDebounceTimeBased"
        assert debounce.timeBasedFdcThresholdStorageValue is None
        assert debounce.timeFailedThreshold is None
        assert debounce.timePassedThreshold is None

    def test_class_docstring_is_spec_note(self):
        """Test that the class docstring carries the spec Note verbatim (Table 12.34)"""
        assert DiagEventDebounceTimeBased.__doc__.strip() == SPEC_NOTE

    def test_init_has_no_docstring(self):
        """Test that __init__ carries no docstring"""
        assert DiagEventDebounceTimeBased.__init__.__doc__ is None

    def test_get_set_time_based_fdc_threshold_storage_value(self):
        """Test getTimeBasedFdcThresholdStorageValue and setTimeBasedFdcThresholdStorageValue methods"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        debounce = DiagEventDebounceTimeBased(ar_root, "TestDiagEventDebounceTimeBased")

        assert debounce.getTimeBasedFdcThresholdStorageValue() is None

        result = debounce.setTimeBasedFdcThresholdStorageValue(_time_value("0.005"))
        assert result is debounce
        assert debounce.getTimeBasedFdcThresholdStorageValue().getValue() == 0.005

        debounce.setTimeBasedFdcThresholdStorageValue(None)
        assert debounce.getTimeBasedFdcThresholdStorageValue().getValue() == 0.005

    def test_get_set_time_failed_threshold(self):
        """Test getTimeFailedThreshold and setTimeFailedThreshold methods"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        debounce = DiagEventDebounceTimeBased(ar_root, "TestDiagEventDebounceTimeBased")

        assert debounce.getTimeFailedThreshold() is None

        result = debounce.setTimeFailedThreshold(_time_value("1.5"))
        assert result is debounce
        assert debounce.getTimeFailedThreshold().getValue() == 1.5

        debounce.setTimeFailedThreshold(None)
        assert debounce.getTimeFailedThreshold().getValue() == 1.5

    def test_get_set_time_passed_threshold(self):
        """Test getTimePassedThreshold and setTimePassedThreshold methods"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        debounce = DiagEventDebounceTimeBased(ar_root, "TestDiagEventDebounceTimeBased")

        assert debounce.getTimePassedThreshold() is None

        result = debounce.setTimePassedThreshold(_time_value("2.0"))
        assert result is debounce
        assert debounce.getTimePassedThreshold().getValue() == 2.0

        debounce.setTimePassedThreshold(None)
        assert debounce.getTimePassedThreshold().getValue() == 2.0

import pytest

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.Timing import (
    ModeDrivenTransmissionModeCondition,
    TransmissionModeCondition,
    TimeRangeType,
    CyclicTiming,
    EventControlledTiming,
    TransmissionModeTiming,
    TransmissionModeDeclaration
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Describable


class Test_FibexCoreTiming:
    """Test cases for FibexCore Timing classes."""
    
    def test_ModeDrivenTransmissionModeCondition(self):
        """Test ModeDrivenTransmissionModeCondition class functionality."""
        condition = ModeDrivenTransmissionModeCondition()

        assert isinstance(condition, ARObject)
        
        # Test default values
        assert condition.getModeDeclarationRef() is None
        
        # Test setter/getter methods
        condition.setModeDeclarationRef("mode_ref")
        assert condition.getModeDeclarationRef() == "mode_ref"

    def test_TransmissionModeCondition(self):
        """Test TransmissionModeCondition class functionality."""
        condition = TransmissionModeCondition()

        assert isinstance(condition, ARObject)
        
        # Test default values
        assert condition.getDataFilter() is None
        assert condition.getISignalInIPduRef() is None

    def test_TimeRangeType(self):
        """Test TimeRangeType class functionality."""
        time_range = TimeRangeType()

        assert isinstance(time_range, ARObject)
        
        # Test default values
        assert time_range.getTolerance() is None
        assert time_range.getValue() is None

    def test_CyclicTiming(self):
        """Test CyclicTiming class functionality."""
        timing = CyclicTiming()

        assert isinstance(timing, Describable)
        
        # Test default values
        assert timing.getTimeOffset() is None
        assert timing.getTimePeriod() is None

    def test_EventControlledTiming(self):
        """Test EventControlledTiming class functionality."""
        timing = EventControlledTiming()

        assert isinstance(timing, Describable)
        
        # Test default values
        assert timing.getNumberOfRepetitions() is None
        assert timing.getRepetitionPeriod() is None

    def test_TransmissionModeTiming(self):
        """Test TransmissionModeTiming class functionality."""
        timing = TransmissionModeTiming()

        assert isinstance(timing, ARObject)
        
        # Test default values
        assert timing.getCyclicTiming() is None
        assert timing.getEventControlledTiming() is None

    def test_TransmissionModeDeclaration(self):
        """Test TransmissionModeDeclaration class functionality."""
        declaration = TransmissionModeDeclaration()

        assert isinstance(declaration, ARObject)
        
        # Test default values
        assert declaration.getModeDrivenFalseConditions() == []
        assert declaration.getModeDrivenTrueConditions() == []
        assert declaration.getTransmissionModeConditions() == []
        assert declaration.getTransmissionModeFalseTiming() is None
        assert declaration.getTransmissionModeTrueTiming() is None
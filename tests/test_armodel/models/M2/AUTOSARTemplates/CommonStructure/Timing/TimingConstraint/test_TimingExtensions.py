import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.TimingExtensions import TimingExtension, SwcTiming
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.ExecutionOrderConstraint import ExecutionOrderConstraint


class TestTimingExtension:
    def test_abstract_class_cannot_be_instantiated(self):
        """Test that TimingExtension abstract class cannot be instantiated directly"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        with pytest.raises(NotImplementedError, match="TimingExtension is an abstract class."):
            TimingExtension(ar_root, "TestTimingExtension")

    def test_create_execution_order_constraint(self):
        """Test createExecutionOrderConstraint method for concrete subclass"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        # Create a concrete subclass for testing
        class ConcreteTimingExtension(TimingExtension):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)
        
        extension = ConcreteTimingExtension(ar_root, "TestTimingExtension")
        constraint = extension.createExecutionOrderConstraint("TestConstraint")
        
        assert isinstance(constraint, ExecutionOrderConstraint)
        assert constraint.getShortName() == "TestConstraint"
        assert constraint in extension.getTimingRequirements()
        assert len(extension.getTimingRequirements()) == 1


class TestSwcTiming:
    def test_initialization(self):
        """Test SwcTiming initialization"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        swc_timing = SwcTiming(ar_root, "TestSwcTiming")
        
        assert swc_timing is not None
        assert swc_timing.getShortName() == "TestSwcTiming"
        assert swc_timing.timing_requirements == []

    def test_create_execution_order_constraint(self):
        """Test createExecutionOrderConstraint method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        swc_timing = SwcTiming(ar_root, "TestSwcTiming")
        
        constraint = swc_timing.createExecutionOrderConstraint("TestConstraint")
        assert isinstance(constraint, ExecutionOrderConstraint)
        assert constraint.getShortName() == "TestConstraint"
        assert constraint in swc_timing.getTimingRequirements()
        assert len(swc_timing.getTimingRequirements()) == 1

    def test_get_timing_requirements(self):
        """Test getTimingRequirements method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        swc_timing = SwcTiming(ar_root, "TestSwcTiming")
        
        requirements = swc_timing.getTimingRequirements()
        assert requirements == []
        assert isinstance(requirements, list)
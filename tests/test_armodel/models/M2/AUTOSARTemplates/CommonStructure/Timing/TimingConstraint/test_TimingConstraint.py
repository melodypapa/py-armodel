import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.TimingConstraint import TimingConstraint
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType


class TestTimingConstraint:
    def test_abstract_class_cannot_be_instantiated(self):
        """Test that TimingConstraint abstract class cannot be instantiated directly"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        with pytest.raises(NotImplementedError, match="TimingConstraint is an abstract class."):
            TimingConstraint(ar_root, "TestTimingConstraint")

    def test_timing_condition_ref_property(self):
        """Test timingConditionRef property"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        # Create a concrete subclass for testing
        class ConcreteTimingConstraint(TimingConstraint):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)
        
        constraint = ConcreteTimingConstraint(ar_root, "TestTimingConstraint")
        
        # Test property setter and getter
        test_ref = RefType().setValue("TestRef")
        constraint.timingConditionRef = test_ref
        assert constraint.timingConditionRef == test_ref
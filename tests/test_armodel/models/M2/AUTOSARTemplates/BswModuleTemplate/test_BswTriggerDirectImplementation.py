"""
Test suite for BswTriggerDirectImplementation class.
Tests verify initialization, getter/setter methods, and proper attribute handling.
"""


from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior import BswTriggerDirectImplementation
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Identifier, RefType


class TestBswTriggerDirectImplementation:
    """Test cases for BswTriggerDirectImplementation class."""

    def test_initialization(self):
        """Test initialization of BswTriggerDirectImplementation with proper default values."""
        obj = BswTriggerDirectImplementation()

        assert obj.getCat2Isr() is None
        assert obj.getMasteredTriggerRef() is None
        assert obj.getTask() is None

    def test_get_set_cat2_isr(self):
        """
        Test getter/setter for cat2Isr attribute.
        Verifies: setter returns self, value round-trips, and None is a no-op.
        """
        obj = BswTriggerDirectImplementation()
        isr_name = Identifier()
        isr_name.setValue("ISR_CAT2")

        # Test setter returns self for method chaining
        result = obj.setCat2Isr(isr_name)
        assert result is obj

        # Test value round-trips
        assert obj.getCat2Isr() is isr_name

        # Test setting None is a no-op (preserves existing value)
        result = obj.setCat2Isr(None)
        assert result is obj
        assert obj.getCat2Isr() is isr_name

    def test_get_set_mastered_trigger_ref(self):
        """
        Test getter/setter for masteredTriggerRef attribute.
        Verifies: setter returns self, value round-trips, and None is a no-op.
        """
        obj = BswTriggerDirectImplementation()
        ref = RefType()

        # Test setter returns self for method chaining
        result = obj.setMasteredTriggerRef(ref)
        assert result is obj

        # Test value round-trips
        assert obj.getMasteredTriggerRef() is ref

        # Test setting None is a no-op (preserves existing value)
        result = obj.setMasteredTriggerRef(None)
        assert result is obj
        assert obj.getMasteredTriggerRef() is ref

    def test_get_set_task(self):
        """
        Test getter/setter for task attribute.
        Verifies: setter returns self, value round-trips, and None is a no-op.
        """
        obj = BswTriggerDirectImplementation()
        task_name = Identifier()
        task_name.setValue("OS_TASK_1")

        # Test setter returns self for method chaining
        result = obj.setTask(task_name)
        assert result is obj

        # Test value round-trips
        assert obj.getTask() is task_name

        # Test setting None is a no-op (preserves existing value)
        result = obj.setTask(None)
        assert result is obj
        assert obj.getTask() is task_name

    def test_method_chaining(self):
        """Test that multiple setter calls can be chained together."""
        obj = BswTriggerDirectImplementation()
        ref = RefType()
        isr_name = Identifier()
        isr_name.setValue("ISR_CAT2")
        task_name = Identifier()
        task_name.setValue("OS_TASK_1")

        result = obj.setCat2Isr(isr_name).setMasteredTriggerRef(ref).setTask(task_name)

        assert result is obj
        assert obj.getCat2Isr() is isr_name
        assert obj.getMasteredTriggerRef() is ref
        assert obj.getTask() is task_name

    def test_setter_none_on_empty_attributes(self):
        """Test that setting None on empty attributes is safe."""
        obj = BswTriggerDirectImplementation()

        # These should all be no-ops and return self
        assert obj.setCat2Isr(None) is obj
        assert obj.setMasteredTriggerRef(None) is obj
        assert obj.setTask(None) is obj

        # All attributes should still be None
        assert obj.getCat2Isr() is None
        assert obj.getMasteredTriggerRef() is None
        assert obj.getTask() is None

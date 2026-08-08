"""
Unit tests for BswModeReceiverPolicy class.
"""

from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior import BswModeReceiverPolicy
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType


class TestBswModeReceiverPolicyInitialization:
    """Tests for __init__ method and default values."""

    def test_initialization(self):
        """Tests that initialization sets all attributes to correct default values."""
        policy = BswModeReceiverPolicy()

        assert policy.enhancedModeApi is None
        assert policy.requiredModeGroupRef is None
        assert policy.supportsAsynchronousModeSwitch is None

    def test_init_has_docstring(self):
        """Tests that __init__ method has a docstring."""
        assert BswModeReceiverPolicy.__init__.__doc__ is not None


class TestEnhancedModeApiGetSet:
    """Tests for getEnhancedModeApi and setEnhancedModeApi methods."""

    def test_get_enhanced_mode_api_default(self):
        """Tests getter returns None by default."""
        policy = BswModeReceiverPolicy()
        assert policy.getEnhancedModeApi() is None

    def test_set_enhanced_mode_api_true(self):
        """Tests setting enhancedModeApi to True."""
        policy = BswModeReceiverPolicy()
        result = policy.setEnhancedModeApi(True)

        assert policy.getEnhancedModeApi() is True
        assert result is policy

    def test_set_enhanced_mode_api_false(self):
        """Tests setting enhancedModeApi to False."""
        policy = BswModeReceiverPolicy()
        result = policy.setEnhancedModeApi(False)

        assert policy.getEnhancedModeApi() is False
        assert result is policy

    def test_set_enhanced_mode_api_none_is_noop(self):
        """Tests that setting None is a no-op and preserves existing value."""
        policy = BswModeReceiverPolicy()
        policy.setEnhancedModeApi(True)
        policy.setEnhancedModeApi(None)

        assert policy.getEnhancedModeApi() is True

    def test_set_enhanced_mode_api_returns_self(self):
        """Tests that setter returns self for method chaining."""
        policy = BswModeReceiverPolicy()
        result = policy.setEnhancedModeApi(True)

        assert result is policy

    def test_get_enhanced_mode_api_has_docstring(self):
        """Tests that getter has a docstring."""
        assert BswModeReceiverPolicy.getEnhancedModeApi.__doc__ is not None

    def test_set_enhanced_mode_api_has_docstring(self):
        """Tests that setter has a docstring."""
        assert BswModeReceiverPolicy.setEnhancedModeApi.__doc__ is not None


class TestRequiredModeGroupRefGetSet:
    """Tests for getRequiredModeGroupRef and setRequiredModeGroupRef methods."""

    def test_get_required_mode_group_ref_default(self):
        """Tests getter returns None by default."""
        policy = BswModeReceiverPolicy()
        assert policy.getRequiredModeGroupRef() is None

    def test_set_required_mode_group_ref(self):
        """Tests setting requiredModeGroupRef."""
        policy = BswModeReceiverPolicy()
        ref = RefType()
        result = policy.setRequiredModeGroupRef(ref)

        assert policy.getRequiredModeGroupRef() is ref
        assert result is policy

    def test_set_required_mode_group_ref_none_is_noop(self):
        """Tests that setting None is a no-op and preserves existing value."""
        policy = BswModeReceiverPolicy()
        ref = RefType()
        policy.setRequiredModeGroupRef(ref)
        policy.setRequiredModeGroupRef(None)

        assert policy.getRequiredModeGroupRef() is ref

    def test_set_required_mode_group_ref_returns_self(self):
        """Tests that setter returns self for method chaining."""
        policy = BswModeReceiverPolicy()
        ref = RefType()
        result = policy.setRequiredModeGroupRef(ref)

        assert result is policy

    def test_get_required_mode_group_ref_has_docstring(self):
        """Tests that getter has a docstring."""
        assert BswModeReceiverPolicy.getRequiredModeGroupRef.__doc__ is not None

    def test_set_required_mode_group_ref_has_docstring(self):
        """Tests that setter has a docstring."""
        assert BswModeReceiverPolicy.setRequiredModeGroupRef.__doc__ is not None


class TestSupportsAsynchronousModeSwitchGetSet:
    """Tests for getSupportsAsynchronousModeSwitch and setSupportsAsynchronousModeSwitch methods."""

    def test_get_supports_asynchronous_mode_switch_default(self):
        """Tests getter returns None by default."""
        policy = BswModeReceiverPolicy()
        assert policy.getSupportsAsynchronousModeSwitch() is None

    def test_set_supports_asynchronous_mode_switch_true(self):
        """Tests setting supportsAsynchronousModeSwitch to True."""
        policy = BswModeReceiverPolicy()
        result = policy.setSupportsAsynchronousModeSwitch(True)

        assert policy.getSupportsAsynchronousModeSwitch() is True
        assert result is policy

    def test_set_supports_asynchronous_mode_switch_false(self):
        """Tests setting supportsAsynchronousModeSwitch to False."""
        policy = BswModeReceiverPolicy()
        result = policy.setSupportsAsynchronousModeSwitch(False)

        assert policy.getSupportsAsynchronousModeSwitch() is False
        assert result is policy

    def test_set_supports_asynchronous_mode_switch_none_is_noop(self):
        """Tests that setting None is a no-op and preserves existing value."""
        policy = BswModeReceiverPolicy()
        policy.setSupportsAsynchronousModeSwitch(True)
        policy.setSupportsAsynchronousModeSwitch(None)

        assert policy.getSupportsAsynchronousModeSwitch() is True

    def test_set_supports_asynchronous_mode_switch_returns_self(self):
        """Tests that setter returns self for method chaining."""
        policy = BswModeReceiverPolicy()
        result = policy.setSupportsAsynchronousModeSwitch(True)

        assert result is policy

    def test_get_supports_asynchronous_mode_switch_has_docstring(self):
        """Tests that getter has a docstring."""
        assert BswModeReceiverPolicy.getSupportsAsynchronousModeSwitch.__doc__ is not None

    def test_set_supports_asynchronous_mode_switch_has_docstring(self):
        """Tests that setter has a docstring."""
        assert BswModeReceiverPolicy.setSupportsAsynchronousModeSwitch.__doc__ is not None


class TestMethodChaining:
    """Tests for method chaining capability."""

    def test_method_chaining_with_all_setters(self):
        """Tests that all setters can be chained together."""
        policy = BswModeReceiverPolicy()
        ref = RefType()

        result = policy.setEnhancedModeApi(True).setRequiredModeGroupRef(ref).setSupportsAsynchronousModeSwitch(False)

        assert result is policy
        assert policy.getEnhancedModeApi() is True
        assert policy.getRequiredModeGroupRef() is ref
        assert policy.getSupportsAsynchronousModeSwitch() is False

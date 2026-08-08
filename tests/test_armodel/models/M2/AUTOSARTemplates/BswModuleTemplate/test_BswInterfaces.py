"""
Test suite for BSW (Basic Software) interface classes in armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces.

This module tests BSW interface classes including BswModuleDependency, BswModuleEntry,
and BswModuleClientServerEntry. These classes represent BSW-specific interface elements
that define dependencies, module entries, and client-server relationships in the AUTOSAR architecture.
"""

import pytest

from armodel import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces import (
    BswCallType,
    BswEntryKindEnum,
    BswExecutionContext,
    BswModuleClientServerEntry,
    BswModuleDependency,
    BswModuleEntry,
    SwServiceImplPolicyEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARNumerical, Identifier, NameToken, PositiveInteger, RefType


class TestBswEntryKindEnum:
    """Test cases for BswEntryKindEnum enumeration."""

    def test_bsw_entry_kind_enum_values(self):
        """Test BswEntryKindEnum values."""
        assert BswEntryKindEnum.FUNCTION == "FUNCTION"


class TestBswCallType:
    """Test cases for BswCallType enumeration."""

    def test_bsw_call_type_enum_values(self):
        """Test BswCallType enum values."""
        assert BswCallType.SYNCHRONOUS == "SYNCHRONOUS"
        assert BswCallType.ASYNCHRONOUS == "ASYNCHRONOUS"


class TestBswExecutionContext:
    """Test cases for BswExecutionContext enumeration."""

    def test_bsw_execution_context_enum_values(self):
        """Test BswExecutionContext enum values."""
        assert BswExecutionContext.HOOK == "HOOK"
        assert BswExecutionContext.INTERRUPT_CAT_1 == "INTERRUPT-CAT-1"
        assert BswExecutionContext.INTERRUPT_CAT_2 == "INTERRUPT-CAT-2"
        assert BswExecutionContext.TASK == "TASK"
        assert BswExecutionContext.UNSPECIFIED == "UNSPECIFIED"


class TestSwServiceImplPolicyEnum:
    """Test cases for SwServiceImplPolicyEnum enumeration."""

    def test_sw_service_impl_policy_enum_values(self):
        """Test SwServiceImplPolicyEnum enum values."""
        assert SwServiceImplPolicyEnum.INLINE == "INLINE"
        assert SwServiceImplPolicyEnum.INLINE_CONDITIONAL == "INLINE-CONDITIONAL"
        assert SwServiceImplPolicyEnum.MACRO == "MACRO"
        assert SwServiceImplPolicyEnum.STANDARD == "STANDARD"


class TestBswModuleDependency:
    """Test cases for BswModuleDependency class - represents BSW module dependencies."""

    def test_initialization(self):
        """Test BswModuleDependency initialization with default values."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        dep = BswModuleDependency(ar_root, "test_dependency")

        assert dep.short_name == "test_dependency"
        assert dep.getTargetModuleId() is None
        assert dep.getTargetModuleRef() is None

    def test_get_set_target_module_id(self):
        """Test getter and setter for target module ID."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        dep = BswModuleDependency(ar_root, "test_dependency")

        target_id = PositiveInteger()
        target_id.setValue(42)
        result = dep.setTargetModuleId(target_id)

        assert result == dep
        assert dep.getTargetModuleId() == target_id

        # Test setting None (should not change value)
        result = dep.setTargetModuleId(None)
        assert result == dep
        assert dep.getTargetModuleId() == target_id  # Should remain unchanged

    def test_get_set_target_module_ref(self):
        """Test getter and setter for target module reference."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        dep = BswModuleDependency(ar_root, "test_dependency")

        ref = RefType()
        ref.setValue("/path/to/target/module")
        result = dep.setTargetModuleRef(ref)

        assert result == dep
        assert dep.getTargetModuleRef() == ref

        # Test setting None (should not change value)
        result = dep.setTargetModuleRef(None)
        assert result == dep
        assert dep.getTargetModuleRef() == ref  # Should remain unchanged


class TestBswModuleEntry:
    """Test cases for BswModuleEntry class - represents BSW module entry points."""

    def test_initialization(self):
        """Test BswModuleEntry initialization with default values."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        entry = BswModuleEntry(ar_root, "test_entry")

        assert entry.short_name == "test_entry"
        assert entry.getArguments() == []
        assert entry.getBswEntryKind() is None
        assert entry.getCallType() is None
        assert entry.getExecutionContext() is None
        assert entry.getFunctionPrototypeEmitter() is None
        assert entry.getIsReentrant() is None
        assert entry.getIsSynchronous() is None
        assert entry.getReturnType() is None
        assert entry.getRole() is None
        assert entry.getServiceId() is None
        assert entry.getSwServiceImplPolicy() is None

    def test_get_arguments(self):
        """Test getter for arguments."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        entry = BswModuleEntry(ar_root, "test_entry")

        assert entry.getArguments() == []

    def test_create_argument(self):
        """Test creating an argument."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        entry = BswModuleEntry(ar_root, "test_entry")

        arg = entry.createArgument("test_arg")

        assert arg.short_name == "test_arg"
        assert len(entry.getArguments()) == 1
        assert entry.getArguments()[0] == arg

    def test_get_set_bsw_entry_kind(self):
        """Test getter and setter for BSW entry kind."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        entry = BswModuleEntry(ar_root, "test_entry")

        result = entry.setBswEntryKind(BswEntryKindEnum.FUNCTION)

        assert result == entry
        assert entry.getBswEntryKind() == BswEntryKindEnum.FUNCTION

        # Test setting None (should not change value)
        result = entry.setBswEntryKind(None)
        assert result == entry
        assert entry.getBswEntryKind() == BswEntryKindEnum.FUNCTION  # Should remain unchanged

    def test_get_set_call_type(self):
        """Test getter and setter for call type."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        entry = BswModuleEntry(ar_root, "test_entry")

        result = entry.setCallType(BswCallType.SYNCHRONOUS)

        assert result == entry
        assert entry.getCallType() == BswCallType.SYNCHRONOUS

        # Test setting None (should not change value)
        result = entry.setCallType(None)
        assert result == entry
        assert entry.getCallType() == BswCallType.SYNCHRONOUS  # Should remain unchanged

    def test_get_set_execution_context(self):
        """Test getter and setter for execution context."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        entry = BswModuleEntry(ar_root, "test_entry")

        result = entry.setExecutionContext("TASK")

        assert result == entry
        assert entry.getExecutionContext() == "TASK"

        # Test setting None (should not change value)
        result = entry.setExecutionContext(None)
        assert result == entry
        assert entry.getExecutionContext() == "TASK"  # Should remain unchanged

    def test_set_execution_context_invalid(self):
        """Test setting invalid execution context raises ValueError."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        entry = BswModuleEntry(ar_root, "test_entry")

        with pytest.raises(ValueError) as exc_info:
            entry.setExecutionContext("INVALID_CONTEXT")
        assert "Invalid execution context" in str(exc_info.value)

    def test_get_set_function_prototype_emitter(self):
        """Test getter and setter for function prototype emitter."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        entry = BswModuleEntry(ar_root, "test_entry")

        emitter = NameToken()
        emitter.setValue("emitter_name")
        result = entry.setFunctionPrototypeEmitter(emitter)

        assert result == entry
        assert entry.getFunctionPrototypeEmitter() == emitter

        # Test setting None (should not change value)
        result = entry.setFunctionPrototypeEmitter(None)
        assert result == entry
        assert entry.getFunctionPrototypeEmitter() == emitter  # Should remain unchanged

    def test_get_set_is_reentrant(self):
        """Test getter and setter for is reentrant flag."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        entry = BswModuleEntry(ar_root, "test_entry")

        result = entry.setIsReentrant(True)

        assert result == entry
        assert entry.getIsReentrant() is True

        # Test setting None (should not change value)
        result = entry.setIsReentrant(None)
        assert result == entry
        assert entry.getIsReentrant() is True  # Should remain unchanged

    def test_get_set_is_synchronous(self):
        """Test getter and setter for is synchronous flag."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        entry = BswModuleEntry(ar_root, "test_entry")

        result = entry.setIsSynchronous(True)

        assert result == entry
        assert entry.getIsSynchronous() is True

        # Test setting None (should not change value)
        result = entry.setIsSynchronous(None)
        assert result == entry
        assert entry.getIsSynchronous() is True  # Should remain unchanged

    def test_get_return_type(self):
        """Test getter for return type."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        entry = BswModuleEntry(ar_root, "test_entry")

        assert entry.getReturnType() is None

    def test_create_return_type(self):
        """Test creating return type."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        entry = BswModuleEntry(ar_root, "test_entry")

        return_type = entry.createReturnType("return_type")

        assert return_type.short_name == "return_type"
        assert entry.getReturnType() == return_type

    def test_get_set_role(self):
        """Test getter and setter for role."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        entry = BswModuleEntry(ar_root, "test_entry")

        role = Identifier()
        role.setValue("test_role")
        result = entry.setRole(role)

        assert result == entry
        assert entry.getRole() == role

        # Test setting None (should not change value)
        result = entry.setRole(None)
        assert result == entry
        assert entry.getRole() == role  # Should remain unchanged

    def test_get_set_service_id(self):
        """Test getter and setter for service ID."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        entry = BswModuleEntry(ar_root, "test_entry")

        service_id = ARNumerical()
        service_id.setValue(123)
        result = entry.setServiceId(service_id)

        assert result == entry
        assert entry.getServiceId() == service_id

        # Test setting None (should not change value)
        result = entry.setServiceId(None)
        assert result == entry
        assert entry.getServiceId() == service_id  # Should remain unchanged

    def test_get_set_sw_service_impl_policy(self):
        """Test getter and setter for SW service implementation policy."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        entry = BswModuleEntry(ar_root, "test_entry")

        result = entry.setSwServiceImplPolicy(SwServiceImplPolicyEnum.STANDARD)

        assert result == entry
        assert entry.getSwServiceImplPolicy() == SwServiceImplPolicyEnum.STANDARD

        # Test setting None (should not change value)
        result = entry.setSwServiceImplPolicy(None)
        assert result == entry
        assert entry.getSwServiceImplPolicy() == SwServiceImplPolicyEnum.STANDARD  # Should remain unchanged

    def test_set_sw_service_impl_policy_invalid(self):
        """Test setting invalid SW service implementation policy raises ValueError."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        entry = BswModuleEntry(ar_root, "test_entry")

        with pytest.raises(ValueError) as exc_info:
            entry.setSwServiceImplPolicy("INVALID_POLICY")
        assert "Invalid SwServiceImplPolicy" in str(exc_info.value)

    def test_str_method(self):
        """Test string representation of BswModuleEntry."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        entry = BswModuleEntry(ar_root, "test_entry")

        # Set some properties to test string representation including serviceId
        service_id = ARNumerical()
        service_id.setValue(123)
        entry.setServiceId(service_id)
        entry.setIsReentrant(True)
        entry.setIsSynchronous(False)
        entry.setCallType(BswCallType.SYNCHRONOUS)
        entry.setExecutionContext("TASK")
        entry.setSwServiceImplPolicy(SwServiceImplPolicyEnum.STANDARD)

        # Call the __str__ method which should work with serviceId set
        str_repr = str(entry)

        assert "short_name" in str_repr
        assert "test_entry" in str_repr
        assert "service_id" in str_repr
        assert "123" in str_repr
        assert "is_reentrant" in str_repr
        assert "True" in str_repr
        assert "is_synchronous" in str_repr
        assert "False" in str_repr
        assert "call_type" in str_repr
        assert "SYNCHRONOUS" in str_repr
        assert "execution_context" in str_repr
        assert "TASK" in str_repr
        assert "sw_service_impl_policy" in str_repr
        assert "STANDARD" in str_repr


class TestBswModuleClientServerEntry:
    """Test cases for BswModuleClientServerEntry class - represents BSW client-server entry relationships."""

    def test_initialization(self):
        """Test BswModuleClientServerEntry initialization with default values."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        entry = BswModuleClientServerEntry(ar_root, "test_client_server_entry")

        assert entry.short_name == "test_client_server_entry"
        assert entry.getEncapsulatedEntryRef() is None
        assert entry.getIsReentrant() is None
        assert entry.getIsSynchronous() is None

    def test_get_set_encapsulated_entry_ref(self):
        """Test getter and setter for encapsulated entry reference."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        entry = BswModuleClientServerEntry(ar_root, "test_client_server_entry")

        ref = RefType()
        ref.setValue("/path/to/encapsulated/entry")
        result = entry.setEncapsulatedEntryRef(ref)

        assert result == entry
        assert entry.getEncapsulatedEntryRef() == ref

        # Test setting None (should not change value)
        result = entry.setEncapsulatedEntryRef(None)
        assert result == entry
        assert entry.getEncapsulatedEntryRef() == ref  # Should remain unchanged

    def test_get_set_is_reentrant(self):
        """Test getter and setter for is reentrant flag."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        entry = BswModuleClientServerEntry(ar_root, "test_client_server_entry")

        result = entry.setIsReentrant(True)

        assert result == entry
        assert entry.getIsReentrant() is True

        # Test setting None (should not change value)
        result = entry.setIsReentrant(None)
        assert result == entry
        assert entry.getIsReentrant() is True  # Should remain unchanged

    def test_get_set_is_synchronous(self):
        """Test getter and setter for is synchronous flag."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        entry = BswModuleClientServerEntry(ar_root, "test_client_server_entry")

        result = entry.setIsSynchronous(True)

        assert result == entry
        assert entry.getIsSynchronous() is True

        # Test setting None (should not change value)
        result = entry.setIsSynchronous(None)
        assert result == entry
        assert entry.getIsSynchronous() is True  # Should remain unchanged

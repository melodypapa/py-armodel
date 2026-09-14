"""
Test suite for BSW (Basic Software) interface classes in armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces.

This module tests BSW interface classes including BswModuleDependency, BswModuleEntry,
and BswModuleClientServerEntry. These classes represent BSW-specific interface elements
that define dependencies, module entries, and client-server relationships in the AUTOSAR architecture.
"""

from armodel import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces import (
    BswCallType,
    BswEntryKindEnum,
    BswEntryRelationship,
    BswEntryRelationshipEnum,
    BswExecutionContext,
    BswModuleClientServerEntry,
    BswModuleDependency,
    BswModuleEntry,
    SwServiceImplPolicyEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Identifier, NameToken, PositiveInteger, RefType


class TestBswEntryKindEnum:
    """Test cases for BswEntryKindEnum enumeration."""

    def test_bsw_entry_kind_enum_values(self):
        """Test BswEntryKindEnum values and instantiability (AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate Table 4.2)."""
        BswEntryKindEnum()
        assert hasattr(BswEntryKindEnum, "ABSTRACT")
        assert hasattr(BswEntryKindEnum, "CONCRETE")
        assert BswEntryKindEnum.ABSTRACT == "abstract"
        assert BswEntryKindEnum.CONCRETE == "concrete"

    def test_bsw_entry_kind_enum_set_value(self):
        """Test setting an enum value via the AREnum pattern."""
        enum = BswEntryKindEnum()
        enum.setValue(BswEntryKindEnum.ABSTRACT)
        assert enum.getValue() == "abstract"


class TestBswCallType:
    """Test cases for BswCallType enumeration."""

    def test_bsw_call_type_enum_values(self):
        """Test BswCallType enum values and instantiability (AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate Table 4.4)."""
        BswCallType()
        assert hasattr(BswCallType, "CALLBACK")
        assert hasattr(BswCallType, "CALLOUT")
        assert hasattr(BswCallType, "INTERRUPT")
        assert hasattr(BswCallType, "REGULAR")
        assert hasattr(BswCallType, "SCHEDULED")
        assert BswCallType.CALLBACK == "callback"
        assert BswCallType.CALLOUT == "callout"
        assert BswCallType.INTERRUPT == "interrupt"
        assert BswCallType.REGULAR == "regular"
        assert BswCallType.SCHEDULED == "scheduled"

    def test_bsw_call_type_enum_set_value(self):
        """Test setting an enum value via the AREnum pattern."""
        enum = BswCallType()
        enum.setValue(BswCallType.REGULAR)
        assert enum.getValue() == "regular"


class TestBswExecutionContext:
    """Test cases for BswExecutionContext enumeration."""

    def test_bsw_execution_context_enum_values(self):
        """Test BswExecutionContext enum values and instantiability (AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate Table 4.3)."""
        BswExecutionContext()
        assert hasattr(BswExecutionContext, "HOOK")
        assert hasattr(BswExecutionContext, "INTERRUPT_CAT_1")
        assert hasattr(BswExecutionContext, "INTERRUPT_CAT_2")
        assert hasattr(BswExecutionContext, "TASK")
        assert hasattr(BswExecutionContext, "UNSPECIFIED")
        assert BswExecutionContext.HOOK == "hook"
        assert BswExecutionContext.INTERRUPT_CAT_1 == "interruptCat1"
        assert BswExecutionContext.INTERRUPT_CAT_2 == "interruptCat2"
        assert BswExecutionContext.TASK == "task"
        assert BswExecutionContext.UNSPECIFIED == "unspecified"

    def test_bsw_execution_context_enum_set_value(self):
        """Test setting an enum value via the AREnum pattern."""
        enum = BswExecutionContext()
        enum.setValue(BswExecutionContext.TASK)
        assert enum.getValue() == "task"


class TestSwServiceImplPolicyEnum:
    """Test cases for SwServiceImplPolicyEnum enumeration."""

    def test_sw_service_impl_policy_enum_values(self):
        """Test SwServiceImplPolicyEnum enum values and instantiability (AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate Table 4.5)."""
        SwServiceImplPolicyEnum()
        assert hasattr(SwServiceImplPolicyEnum, "INLINE")
        assert hasattr(SwServiceImplPolicyEnum, "INLINE_CONDITIONAL")
        assert hasattr(SwServiceImplPolicyEnum, "MACRO")
        assert hasattr(SwServiceImplPolicyEnum, "STANDARD")
        assert SwServiceImplPolicyEnum.INLINE == "inline"
        assert SwServiceImplPolicyEnum.INLINE_CONDITIONAL == "inlineConditional"
        assert SwServiceImplPolicyEnum.MACRO == "macro"
        assert SwServiceImplPolicyEnum.STANDARD == "standard"

    def test_sw_service_impl_policy_enum_set_value(self):
        """Test setting an enum value via the AREnum pattern."""
        enum = SwServiceImplPolicyEnum()
        enum.setValue(SwServiceImplPolicyEnum.STANDARD)
        assert enum.getValue() == "standard"


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

        result = entry.setBswEntryKind(BswEntryKindEnum.CONCRETE)

        assert result == entry
        assert entry.getBswEntryKind() == BswEntryKindEnum.CONCRETE

        # Test setting None (should not change value)
        result = entry.setBswEntryKind(None)
        assert result == entry
        assert entry.getBswEntryKind() == BswEntryKindEnum.CONCRETE  # Should remain unchanged

    def test_get_set_call_type(self):
        """Test getter and setter for call type."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        entry = BswModuleEntry(ar_root, "test_entry")

        result = entry.setCallType(BswCallType.REGULAR)

        assert result == entry
        assert entry.getCallType() == BswCallType.REGULAR

        # Test setting None (should not change value)
        result = entry.setCallType(None)
        assert result == entry
        assert entry.getCallType() == BswCallType.REGULAR  # Should remain unchanged

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

        service_id = PositiveInteger()
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
        """Setting a non-None SW service implementation policy stores it (no ValueError validation)."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        entry = BswModuleEntry(ar_root, "test_entry")

        entry.setSwServiceImplPolicy("INLINE")
        assert entry.getSwServiceImplPolicy() == "INLINE"


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


class TestBswEntryRelationshipInitialization:
    """Test BswEntryRelationship initialization and default values."""

    def test_initialization(self):
        """Test BswEntryRelationship initialization with default values."""
        relationship = BswEntryRelationship()

        assert relationship.getBswEntryRelationshipType() is None
        assert relationship.getFromRef() is None
        assert relationship.getToRef() is None


class TestBswEntryRelationshipType:
    """Test getter and setter for bswEntryRelationshipType attribute."""

    def test_get_set_bsw_entry_relationship_type(self):
        """
        Test getter and setter for BSW entry relationship type.
        Verifies method chaining and value retrieval.
        """
        relationship = BswEntryRelationship()

        # Use enum value
        enum_value = BswEntryRelationshipEnum.DERIVED_FROM

        # Test setter with value
        result = relationship.setBswEntryRelationshipType(enum_value)

        assert result == relationship  # Test method chaining
        assert relationship.getBswEntryRelationshipType() == enum_value

    def test_get_set_bsw_entry_relationship_type_none(self):
        """
        Test that setting None is a no-op (does not overwrite existing value).
        """
        relationship = BswEntryRelationship()

        # Set initial value
        enum_value = BswEntryRelationshipEnum.DERIVED_FROM
        relationship.setBswEntryRelationshipType(enum_value)
        assert relationship.getBswEntryRelationshipType() == enum_value

        # Try to set None (should be no-op)
        result = relationship.setBswEntryRelationshipType(None)

        assert result == relationship  # Still returns self
        assert relationship.getBswEntryRelationshipType() == enum_value  # Value unchanged

    def test_get_bsw_entry_relationship_type_default(self):
        """Test that getter returns None by default."""
        relationship = BswEntryRelationship()
        assert relationship.getBswEntryRelationshipType() is None


class TestBswEntryRelationshipFromRef:
    """Test getter and setter for fromRef attribute."""

    def test_get_set_from_ref(self):
        """
        Test getter and setter for from reference.
        Verifies method chaining and value retrieval.
        """
        relationship = BswEntryRelationship()

        # Create reference
        ref = RefType()
        ref.setValue("/Abstract/BswModuleEntry")

        # Test setter with value
        result = relationship.setFromRef(ref)

        assert result == relationship  # Test method chaining
        assert relationship.getFromRef() == ref
        assert relationship.getFromRef().getValue() == "/Abstract/BswModuleEntry"

    def test_get_set_from_ref_none(self):
        """
        Test that setting None is a no-op (does not overwrite existing value).
        """
        relationship = BswEntryRelationship()

        # Set initial value
        ref = RefType()
        ref.setValue("/Abstract/BswModuleEntry")
        relationship.setFromRef(ref)
        assert relationship.getFromRef() == ref

        # Try to set None (should be no-op)
        result = relationship.setFromRef(None)

        assert result == relationship  # Still returns self
        assert relationship.getFromRef() == ref  # Value unchanged

    def test_get_from_ref_default(self):
        """Test that getter returns None by default."""
        relationship = BswEntryRelationship()
        assert relationship.getFromRef() is None


class TestBswEntryRelationshipToRef:
    """Test getter and setter for toRef attribute."""

    def test_get_set_to_ref(self):
        """
        Test getter and setter for to reference.
        Verifies method chaining and value retrieval.
        """
        relationship = BswEntryRelationship()

        # Create reference
        ref = RefType()
        ref.setValue("/Concrete/BswModuleEntry")

        # Test setter with value
        result = relationship.setToRef(ref)

        assert result == relationship  # Test method chaining
        assert relationship.getToRef() == ref
        assert relationship.getToRef().getValue() == "/Concrete/BswModuleEntry"

    def test_get_set_to_ref_none(self):
        """
        Test that setting None is a no-op (does not overwrite existing value).
        """
        relationship = BswEntryRelationship()

        # Set initial value
        ref = RefType()
        ref.setValue("/Concrete/BswModuleEntry")
        relationship.setToRef(ref)
        assert relationship.getToRef() == ref

        # Try to set None (should be no-op)
        result = relationship.setToRef(None)

        assert result == relationship  # Still returns self
        assert relationship.getToRef() == ref  # Value unchanged

    def test_get_to_ref_default(self):
        """Test that getter returns None by default."""
        relationship = BswEntryRelationship()
        assert relationship.getToRef() is None


class TestBswEntryRelationshipMethodChaining:
    """Test method chaining functionality across multiple setters."""

    def test_method_chaining(self):
        """Test that setters return self, enabling method chaining."""
        relationship = BswEntryRelationship()

        enum_value = BswEntryRelationshipEnum.DERIVED_FROM
        from_ref = RefType()
        from_ref.setValue("/From/Entry")
        to_ref = RefType()
        to_ref.setValue("/To/Entry")

        # Test method chaining
        result = relationship.setBswEntryRelationshipType(enum_value).setFromRef(from_ref).setToRef(to_ref)

        assert result == relationship
        assert relationship.getBswEntryRelationshipType() == enum_value
        assert relationship.getFromRef() == from_ref
        assert relationship.getToRef() == to_ref


class TestBswEntryRelationshipComplex:
    """Test complex scenarios with multiple relationships."""

    def test_multiple_relationships(self):
        """Test creating and managing multiple relationships."""
        relationships = []

        for i in range(3):
            rel = BswEntryRelationship()

            enum_val = BswEntryRelationshipEnum.DERIVED_FROM
            from_ref = RefType()
            from_ref.setValue(f"/From/Entry{i}")
            to_ref = RefType()
            to_ref.setValue(f"/To/Entry{i}")

            rel.setBswEntryRelationshipType(enum_val)
            rel.setFromRef(from_ref)
            rel.setToRef(to_ref)

            relationships.append(rel)

        assert len(relationships) == 3
        for i, rel in enumerate(relationships):
            assert rel.getFromRef().getValue() == f"/From/Entry{i}"
            assert rel.getToRef().getValue() == f"/To/Entry{i}"

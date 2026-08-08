"""
Test suite for BswEntryRelationship class in armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces.

This module tests the BswEntryRelationship class which describes a relationship
between two BswModuleEntrys and the type of relationship.
"""

from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces import (
    BswEntryRelationship,
    BswEntryRelationshipEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType  # noqa: E501


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

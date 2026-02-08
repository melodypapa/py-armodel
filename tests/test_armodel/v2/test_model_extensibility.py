"""
Test V2 model extensibility features.

Tests for CODING_RULE_V2_00014: V2 Model Extensibility
Tests for CODING_RULE_V2_00015: V2 Module Integration Contract
"""
from armodel.v2.models import AUTOSAR, ARPackage, Identifiable


class TestV2ModelExtensibility:
    """Test V2 model extensibility features (CODING_RULE_V2_00014)."""

    def test_arobject_has_extended_attributes(self):
        """Test ARObject has extended attributes dict for custom properties."""
        obj = Identifiable()
        assert hasattr(obj, "_extended_attributes")
        assert isinstance(obj._extended_attributes, dict)
        # Identifiable pre-populates with adminData and category
        assert "adminData" in obj._extended_attributes
        assert "category" in obj._extended_attributes

    def test_arobject_extended_attributes_api(self):
        """Test ARObject extended attributes get/set methods."""
        obj = ARPackage()

        # Set extended attribute
        obj.setExtendedAttribute("custom_property", "custom_value")
        assert obj.getExtendedAttribute("custom_property") == "custom_value"

        # Get non-existent attribute returns None
        assert obj.getExtendedAttribute("non_existent") is None

    def test_arobject_multiple_extended_attributes(self):
        """Test multiple extended attributes can be stored."""
        obj = ARPackage()
        obj.setExtendedAttribute("vendor", "MyCompany")
        obj.setExtendedAttribute("version", "1.0")
        obj.setExtendedAttribute("description", "Test package")

        assert obj.getExtendedAttribute("vendor") == "MyCompany"
        assert obj.getExtendedAttribute("version") == "1.0"
        assert obj.getExtendedAttribute("description") == "Test package"

    def test_autosar_singleton_pattern(self):
        """Test AUTOSAR singleton pattern works correctly."""
        # Reset singleton for testing
        AUTOSAR.resetInstance()

        # Get first instance
        instance1 = AUTOSAR.getInstance()
        assert instance1 is not None

        # Get second instance - should be same object
        instance2 = AUTOSAR.getInstance()
        assert instance1 is instance2

        # Reset and get new instance
        AUTOSAR.resetInstance()
        instance3 = AUTOSAR.getInstance()
        assert instance3 is not None

    def test_identifiable_getter_setter(self):
        """Test Identifiable getShortName/setShortName methods."""
        obj = Identifiable()

        # Initial state
        assert obj.getShortName() is None

        # Set and get
        result = obj.setShortName("TestName")
        assert obj.getShortName() == "TestName"

        # Method chaining (returns self)
        assert result is obj

    def test_arpackage_parent_child_relationship(self):
        """Test ARPackage maintains parent-child relationships."""
        parent = ARPackage()
        parent.setShortName("Parent")

        child = ARPackage()
        child.setShortName("Child")

        # Add child package
        parent.addARPackage(child)

        # Verify parent is set
        assert child.parent is parent
        assert len(parent.getARPackages()) == 1
        assert parent.getARPackages()[0] is child

    def test_arpackage_element_management(self):
        """Test ARPackage element management methods."""
        pkg = ARPackage()
        pkg.setShortName("TestPackage")

        elem1 = Identifiable()
        elem1.setShortName("Element1")

        elem2 = Identifiable()
        elem2.setShortName("Element2")

        # Add elements
        pkg.addElement(elem1)
        pkg.addElement(elem2)

        # Verify elements
        assert len(pkg.getElements()) == 2
        assert pkg.getElements()[0] is elem1
        assert pkg.getElements()[1] is elem2

        # Verify parent is set
        assert elem1.parent is pkg
        assert elem2.parent is pkg

    def test_extensibility_without_base_modification(self):
        """
        Test that V2 modules can extend functionality without modifying base classes.

        This is the core requirement of CODING_RULE_V2_00014.
        """
        # Create a V2 model instance
        pkg = ARPackage()
        pkg.setShortName("TestPackage")

        # Use extended attributes to add custom properties
        # This simulates what a V2 module would do
        pkg.setExtendedAttribute("custom_metadata", {"key": "value"})
        pkg.setExtendedAttribute("module_specific_flag", True)
        pkg.setExtendedAttribute("custom_list", [1, 2, 3])

        # Verify we can retrieve all custom properties
        assert pkg.getExtendedAttribute("custom_metadata") == {"key": "value"}
        assert pkg.getExtendedAttribute("module_specific_flag") is True
        assert pkg.getExtendedAttribute("custom_list") == [1, 2, 3]

        # Verify base class functionality still works
        assert pkg.getShortName() == "TestPackage"
        assert pkg.getTagName() == "ARPackage"

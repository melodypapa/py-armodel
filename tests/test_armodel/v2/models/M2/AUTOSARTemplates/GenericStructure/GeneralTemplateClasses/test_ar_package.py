"""
Test module for ARPackage.py.

This file tests all classes defined in ARPackage.py:
- ARPackage_ManuallyMaintained (marker class)
- ARPackage
- PackageableElement
- ReferenceBase
- ARElement

Tests cover:
- Abstract class instantiation
- Property getter/setter methods
- AUTOSAR-compatible method delegation
- Fluent method chaining
- Type validation
- Collection management
- Parent-child relationships
- Extended attributes (CODING_RULE_V2_00014)
"""
import pytest

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARPackage_ManuallyMaintained,
    ARPackage,
    PackageableElement,
    ReferenceBase,
    ARElement,
)


class TestARPackageManuallyMaintained:
    """Test class for ARPackage_ManuallyMaintained marker class."""

    def test_ar_package_manually_maintained_exists(self):
        """Test that ARPackage_ManuallyMaintained marker class exists."""
        assert ARPackage_ManuallyMaintained is not None

    def test_ar_package_manually_maintained_can_be_instantiated(self):
        """Test that ARPackage_ManuallyMaintained can be instantiated."""
        obj = ARPackage_ManuallyMaintained()
        assert obj is not None
        assert isinstance(obj, ARPackage_ManuallyMaintained)


class TestARPackage:
    """Test class for ARPackage functionality."""

    def test_ar_package_can_be_instantiated(self):
        """Test that ARPackage can be instantiated."""
        pkg = ARPackage()
        assert pkg is not None

    def test_ar_package_short_name_initialization(self):
        """Test that short_name property is initialized to None."""
        pkg = ARPackage()
        assert pkg.shortName is None

    def test_ar_package_short_name_setter_getter(self):
        """Test short_name property setter and getter."""
        pkg = ARPackage()
        pkg.shortName = "TestPackage"
        assert pkg.shortName == "TestPackage"

    def test_ar_package_get_short_name(self):
        """Test getShortName method."""
        pkg = ARPackage()
        pkg.shortName = "TestPackage"
        assert pkg.getShortName() == "TestPackage"

    def test_ar_package_set_short_name(self):
        """Test setShortName method with method chaining."""
        pkg = ARPackage()
        result = pkg.setShortName("TestPackage")
        assert result is pkg  # Method chaining
        assert pkg.getShortName() == "TestPackage"

    def test_ar_package_parent_initialization(self):
        """Test that parent attribute is initialized to None."""
        pkg = ARPackage()
        assert pkg.parent is None

    def test_ar_package_ar_package_initialization(self):
        """Test that ar_package property is initialized to empty list."""
        pkg = ARPackage()
        assert pkg.ar_package == []

    def test_ar_package_element_initialization(self):
        """Test that element property is initialized to empty list."""
        pkg = ARPackage()
        assert pkg.element == []

    def test_ar_package_reference_base_initialization(self):
        """Test that reference_base property is initialized to empty list."""
        pkg = ARPackage()
        assert pkg.reference_base == []

    def test_ar_package_add_ar_package(self):
        """Test addARPackage method."""
        parent = ARPackage()
        child = ARPackage()
        child.shortName = "ChildPackage"

        parent.addARPackage(child)

        assert len(parent.getARPackages()) == 1
        assert parent.getARPackages()[0] is child
        assert child.parent is parent

    def test_ar_package_add_element(self):
        """Test addElement method."""
        pkg = ARPackage()
        elem = ARPackage()  # Use ARPackage as a PackageableElement for testing
        elem.shortName = "TestElement"

        pkg.addElement(elem)

        assert len(pkg.getElements()) == 1
        assert pkg.getElements()[0] is elem
        assert elem.parent is pkg

    def test_ar_package_get_ar_packages(self):
        """Test getARPackages method."""
        pkg = ARPackage()
        child1 = ARPackage()
        child1.shortName = "Child1"
        child2 = ARPackage()
        child2.shortName = "Child2"

        pkg.addARPackage(child1)
        pkg.addARPackage(child2)

        ar_packages = pkg.getARPackages()
        assert len(ar_packages) == 2
        assert ar_packages[0] is child1
        assert ar_packages[1] is child2

    def test_ar_package_get_elements(self):
        """Test getElements method."""
        pkg = ARPackage()
        elem1 = ARPackage()
        elem1.shortName = "Element1"
        elem2 = ARPackage()
        elem2.shortName = "Element2"

        pkg.addElement(elem1)
        pkg.addElement(elem2)

        elements = pkg.getElements()
        assert len(elements) == 2
        assert elements[0] is elem1
        assert elements[1] is elem2

    def test_ar_package_ar_packages_alias(self):
        """Test ar_packages alias for ar_package property (V1 compatibility)."""
        pkg = ARPackage()
        child = ARPackage()
        child.shortName = "Child"

        pkg.ar_package.append(child)

        assert pkg.ar_packages == pkg.ar_package

    def test_ar_package_get_tag_name(self):
        """Test getTagName method."""
        pkg = ARPackage()
        assert pkg.getTagName() == "ARPackage"

    def test_ar_package_extended_attributes(self):
        """Test extended attributes (CODING_RULE_V2_00014)."""
        pkg = ARPackage()
        pkg.setExtendedAttribute("custom_key", "custom_value")
        assert pkg.getExtendedAttribute("custom_key") == "custom_value"

    def test_ar_package_parent_child_relationships(self):
        """Test parent-child relationships with multiple levels."""
        root = ARPackage()
        root.shortName = "Root"

        parent = ARPackage()
        parent.shortName = "Parent"

        child = ARPackage()
        child.shortName = "Child"

        root.addARPackage(parent)
        parent.addARPackage(child)

        assert child.parent is parent
        assert parent.parent is root
        assert root.parent is None

    def test_ar_package_collection_methods_delegation(self):
        """Test that collection methods delegate to properties."""
        pkg = ARPackage()
        child = ARPackage()
        child.shortName = "Child"

        pkg.ar_package.append(child)

        # getArPackage should delegate to ar_package property
        assert pkg.getArPackage() == pkg.ar_package

        # getElement should delegate to element property
        assert pkg.getElement() == pkg.element

        # getReferenceBase should delegate to reference_base property
        assert pkg.getReferenceBase() == pkg.reference_base


class TestPackageableElement:
    """Test class for PackageableElement base class functionality."""

    def test_packageable_element_abstract_class_cannot_be_instantiated(self):
        """Test that PackageableElement abstract class cannot be instantiated directly."""
        with pytest.raises(TypeError, match="PackageableElement is an abstract class"):
            PackageableElement()

    def test_concrete_packageable_element_can_be_instantiated(self):
        """Test that a concrete subclass of PackageableElement can be instantiated."""
        class ConcretePackageableElement(PackageableElement):
            """Concrete implementation for testing."""

            def __init__(self):
                super().__init__()

        obj = ConcretePackageableElement()
        assert obj is not None


class TestReferenceBase:
    """Test class for ReferenceBase functionality."""

    def test_reference_base_can_be_instantiated(self):
        """Test that ReferenceBase can be instantiated."""
        obj = ReferenceBase()
        assert obj is not None

    def test_reference_base_global_element_initialization(self):
        """Test that global_element property is initialized to empty list."""
        obj = ReferenceBase()
        assert obj.global_element == []

    def test_reference_base_global_in_initialization(self):
        """Test that global_in property is initialized to empty list."""
        obj = ReferenceBase()
        assert obj.global_in == []

    def test_reference_base_is_default_initialization(self):
        """Test that is_default property is initialized to None."""
        obj = ReferenceBase()
        assert obj.is_default is None

    def test_reference_base_package_initialization(self):
        """Test that package property is initialized to None."""
        obj = ReferenceBase()
        assert obj.package is None

    def test_reference_base_short_label_initialization(self):
        """Test that short_label property is initialized to None."""
        obj = ReferenceBase()
        assert obj.short_label is None

    def test_reference_base_is_default_setter_none(self):
        """Test is_default property setter with None."""
        obj = ReferenceBase()
        obj.is_default = None
        assert obj.is_default is None

    def test_reference_base_package_setter_none(self):
        """Test package property setter with None."""
        obj = ReferenceBase()
        obj.package = None
        assert obj.package is None

    def test_reference_base_short_label_setter_identifier(self):
        """Test short_label property setter with Identifier value."""
        from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
            Identifier,
        )

        obj = ReferenceBase()
        identifier = Identifier().setValue("TestLabel")
        obj.short_label = identifier
        assert obj.short_label is identifier
        assert obj.short_label.getValue() == "TestLabel"

    def test_reference_base_short_label_setter_string(self):
        """Test short_label property setter with string value."""
        from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
            Identifier,
        )

        obj = ReferenceBase()
        obj.short_label = "TestLabel"
        assert isinstance(obj.short_label, Identifier)
        assert obj.short_label.getValue() == "TestLabel"

    def test_reference_base_short_label_type_validation(self):
        """Test short_label property setter type validation."""
        obj = ReferenceBase()
        with pytest.raises(TypeError, match="shortLabel must be Identifier"):
            obj.short_label = 123  # Wrong type

    def test_reference_base_package_type_validation(self):
        """Test package property setter type validation."""
        obj = ReferenceBase()
        with pytest.raises(TypeError, match="package must be ARPackage or None"):
            obj.package = "invalid"  # Wrong type

    def test_reference_base_get_global_element_delegates_to_property(self):
        """Test that getGlobalElement delegates to global_element property."""
        obj = ReferenceBase()
        assert obj.getGlobalElement() == []

    def test_reference_base_get_global_in_delegates_to_property(self):
        """Test that getGlobalIn delegates to global_in property."""
        obj = ReferenceBase()
        assert obj.getGlobalIn() == []

    def test_reference_base_get_is_default_delegates_to_property(self):
        """Test that getIsDefault delegates to is_default property."""
        obj = ReferenceBase()
        assert obj.getIsDefault() is None

    def test_reference_base_set_is_default_delegates_to_property(self):
        """Test that setIsDefault delegates to is_default property."""
        from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
            Boolean,
        )

        obj = ReferenceBase()
        result = obj.setIsDefault(Boolean().setValue(True))
        assert result is obj  # Method chaining

    def test_reference_base_get_package_delegates_to_property(self):
        """Test that getPackage delegates to package property."""
        obj = ReferenceBase()
        assert obj.getPackage() is None

    def test_reference_base_set_package_delegates_to_property(self):
        """Test that setPackage delegates to package property."""
        obj = ReferenceBase()
        pkg = ARPackage()
        result = obj.setPackage(pkg)
        assert result is obj  # Method chaining
        assert obj.getPackage() is pkg

    def test_reference_base_get_short_label_delegates_to_property(self):
        """Test that getShortLabel delegates to short_label property."""
        from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
            Identifier,
        )

        obj = ReferenceBase()
        obj.short_label = "TestLabel"
        assert isinstance(obj.getShortLabel(), Identifier)
        assert obj.getShortLabel().getValue() == "TestLabel"

    def test_reference_base_set_short_label_delegates_to_property(self):
        """Test that setShortLabel delegates to short_label property."""
        from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
            Identifier,
        )

        obj = ReferenceBase()
        result = obj.setShortLabel("TestLabel")
        assert result is obj  # Method chaining
        assert isinstance(obj.getShortLabel(), Identifier)
        assert obj.getShortLabel().getValue() == "TestLabel"

    def test_reference_base_with_is_default_fluent_method(self):
        """Test with_is_default fluent method (CODING_RULE_V2_00019)."""
        from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
            Boolean,
        )

        obj = ReferenceBase()
        result = obj.with_is_default(Boolean().setValue(True))
        assert result is obj  # Method chaining

    def test_reference_base_with_package_fluent_method(self):
        """Test with_package fluent method (CODING_RULE_V2_00019)."""
        obj = ReferenceBase()
        pkg = ARPackage()
        result = obj.with_package(pkg)
        assert result is obj  # Method chaining
        assert obj.package is pkg

    def test_reference_base_with_short_label_fluent_method(self):
        """Test with_short_label fluent method (CODING_RULE_V2_00019)."""
        from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
            Identifier,
        )

        obj = ReferenceBase()
        result = obj.with_short_label("TestLabel")
        assert result is obj  # Method chaining
        assert isinstance(obj.short_label, Identifier)
        assert obj.short_label.getValue() == "TestLabel"

    def test_reference_base_extended_attributes(self):
        """Test extended attributes (CODING_RULE_V2_00014)."""
        obj = ReferenceBase()
        obj.setExtendedAttribute("custom_key", "custom_value")
        assert obj.getExtendedAttribute("custom_key") == "custom_value"


class TestARElement:
    """Test class for ARElement base class functionality."""

    def test_ar_element_abstract_class_cannot_be_instantiated(self):
        """Test that ARElement abstract class cannot be instantiated directly."""
        with pytest.raises(TypeError, match="ARElement is an abstract class"):
            ARElement()

    def test_concrete_ar_element_can_be_instantiated(self):
        """Test that a concrete subclass of ARElement can be instantiated."""
        class ConcreteARElement(ARElement):
            """Concrete implementation for testing."""

            def __init__(self):
                super().__init__()

        obj = ConcreteARElement()
        assert obj is not None

    def test_ar_element_inherits_from_packageable_element(self):
        """Test that ARElement inherits from PackageableElement."""
        class ConcreteARElement(ARElement):
            """Concrete implementation for testing."""

            def __init__(self):
                super().__init__()

        obj = ConcreteARElement()
        # Should be an instance of ARElement and PackageableElement
        assert isinstance(obj, ARElement)
        assert isinstance(obj, PackageableElement)

    def test_ar_element_extended_attributes(self):
        """Test extended attributes (CODING_RULE_V2_00014)."""
        class ConcreteARElement(ARElement):
            """Concrete implementation for testing."""

            def __init__(self):
                super().__init__()

        obj = ConcreteARElement()
        obj.setExtendedAttribute("custom_key", "custom_value")
        assert obj.getExtendedAttribute("custom_key") == "custom_value"
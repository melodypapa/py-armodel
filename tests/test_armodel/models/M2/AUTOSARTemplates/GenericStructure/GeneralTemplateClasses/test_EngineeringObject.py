"""
This module contains comprehensive tests for the EngineeringObject.py file
in the AUTOSAR GenericStructure module.
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.EngineeringObject import (
    AutosarEngineeringObject,
    EngineeringObject,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARLiteral,
)


class TestEngineeringObject:
    """
    Test class for EngineeringObject functionality.
    """

    def test_abstract_initialization(self):
        """
        Test that EngineeringObject cannot be instantiated directly (abstract class).
        """
        try:
            obj = EngineeringObject()
            assert False, "EngineeringObject should not be instantiable"
        except TypeError:
            pass  # Expected behavior

    def test_category_methods(self):
        """
        Test get/set methods for category.
        """
        # Create a concrete subclass for testing
        class ConcreteEngineeringObject(EngineeringObject):
            def __init__(self):
                super().__init__()

        concrete_obj = ConcreteEngineeringObject()

        # Test initial value
        assert concrete_obj.getCategory() is None

        # Test setting with ARLiteral
        ar_literal = ARLiteral().setValue("TestCategory")
        result = concrete_obj.setCategory(ar_literal)
        assert result is concrete_obj  # Verify method chaining
        assert concrete_obj.getCategory() == ar_literal

    def test_category_with_string(self):
        """
        Test setCategory method with string input (should convert to ARLiteral).
        """
        # Create a concrete subclass for testing
        class ConcreteEngineeringObject(EngineeringObject):
            def __init__(self):
                super().__init__()

        concrete_obj = ConcreteEngineeringObject()

        # Test setting with string
        result = concrete_obj.setCategory("TestString")
        assert result is concrete_obj  # Verify method chaining
        category = concrete_obj.getCategory()
        assert category is not None
        assert category.getValue() == "TestString"

    def test_domain_methods(self):
        """
        Test get/set methods for domain.
        """
        # Create a concrete subclass for testing
        class ConcreteEngineeringObject(EngineeringObject):
            def __init__(self):
                super().__init__()

        concrete_obj = ConcreteEngineeringObject()

        # Test initial value
        assert concrete_obj.getDomain() is None

        # Test setting domain
        domain = ARLiteral().setValue("TestDomain")
        result = concrete_obj.setDomain(domain)
        assert result is concrete_obj  # Verify method chaining
        assert concrete_obj.getDomain() == domain

    def test_revision_label_methods(self):
        """
        Test get/set methods for revision label.
        """
        # Create a concrete subclass for testing
        class ConcreteEngineeringObject(EngineeringObject):
            def __init__(self):
                super().__init__()

        concrete_obj = ConcreteEngineeringObject()

        # Test initial value
        assert concrete_obj.getRevisionLabel() is None

        # Test setting revision label
        revision_label = ARLiteral().setValue("1.0.0")
        result = concrete_obj.setRevisionLabel(revision_label)
        assert result is concrete_obj  # Verify method chaining
        assert concrete_obj.getRevisionLabel() == revision_label

    def test_short_label_methods(self):
        """
        Test get/set methods for short label.
        """
        # Create a concrete subclass for testing
        class ConcreteEngineeringObject(EngineeringObject):
            def __init__(self):
                super().__init__()

        concrete_obj = ConcreteEngineeringObject()

        # Test initial value
        assert concrete_obj.getShortLabel() is None

        # Test setting short label
        short_label = ARLiteral().setValue("ShortLabel")
        result = concrete_obj.setShortLabel(short_label)
        assert result is concrete_obj  # Verify method chaining
        assert concrete_obj.getShortLabel() == short_label


class TestAutosarEngineeringObject:
    """
    Test class for AutosarEngineeringObject functionality.
    """

    def test_initialization(self):
        """
        Test AutosarEngineeringObject initialization.
        """
        obj = AutosarEngineeringObject()

        # Verify basic properties
        assert obj is not None
        assert obj.getCategory() is None
        assert obj.getDomain() is None
        assert obj.getRevisionLabel() is None
        assert obj.getShortLabel() is None

"""
This module contains comprehensive tests for the EngineeringObject.py file
in the AUTOSAR GenericStructure module.
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.EngineeringObject import EngineeringObject, AutosarEngineeringObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral, NameToken, RevisionLabelString


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

    def test_concrete_subclass_initialization(self):
        """
        Test abstract __init__ defaults through a concrete subclass.
        """

        class ConcreteEngineeringObject(EngineeringObject):
            def __init__(self):
                super().__init__()

        concrete_obj = ConcreteEngineeringObject()

        assert concrete_obj.getShortLabel() is None
        assert concrete_obj.getCategory() is None
        assert concrete_obj.getRevisionLabels() == []
        assert concrete_obj.getDomain() is None

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

        # Test setting with NameToken
        category = NameToken().setValue("TestCategory")
        result = concrete_obj.setCategory(category)
        assert result is concrete_obj  # Verify method chaining
        assert concrete_obj.getCategory() == category

        # Test setting None is a no-op
        concrete_obj.setCategory(None)
        assert concrete_obj.getCategory() == category

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
        domain = NameToken().setValue("TestDomain")
        result = concrete_obj.setDomain(domain)
        assert result is concrete_obj  # Verify method chaining
        assert concrete_obj.getDomain() == domain

        # Test setting None is a no-op
        concrete_obj.setDomain(None)
        assert concrete_obj.getDomain() == domain

    def test_revision_label_methods(self):
        """
        Test get/add methods for revision labels.
        """

        # Create a concrete subclass for testing
        class ConcreteEngineeringObject(EngineeringObject):
            def __init__(self):
                super().__init__()

        concrete_obj = ConcreteEngineeringObject()

        # Test initial value
        assert concrete_obj.getRevisionLabels() == []

        # Test adding a revision label
        revision_label = RevisionLabelString().setValue("1.0.0")
        result = concrete_obj.addRevisionLabel(revision_label)
        assert result is concrete_obj  # Verify method chaining
        assert concrete_obj.getRevisionLabels() == [revision_label]

        # Test adding None is a no-op
        concrete_obj.addRevisionLabel(None)
        assert concrete_obj.getRevisionLabels() == [revision_label]

        # Test appending a second label preserves insertion order
        second_label = RevisionLabelString().setValue("1.1.0")
        concrete_obj.addRevisionLabel(second_label)
        assert concrete_obj.getRevisionLabels() == [revision_label, second_label]

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
        short_label = NameToken().setValue("ShortLabel")
        result = concrete_obj.setShortLabel(short_label)
        assert result is concrete_obj  # Verify method chaining
        assert concrete_obj.getShortLabel() == short_label

        # Test setting None is a no-op
        concrete_obj.setShortLabel(None)
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
        assert obj.getRevisionLabels() == []
        assert obj.getShortLabel() is None

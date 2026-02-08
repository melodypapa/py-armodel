"""
This module contains comprehensive tests for the AtpDefinition.py file
in the AUTOSAR GenericStructure module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.RolesAndRights.AtpDefinition import (
    AtpDefinition,
)


class TestAtpDefinition:
    """
    Test class for AtpDefinition functionality.
    """

    def test_abstract_initialization(self):
        """
        Test that AtpDefinition cannot be instantiated directly (abstract class).
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        try:
            obj = AtpDefinition(ar_root, "TestAtpDefinition")
            assert False, "AtpDefinition should not be instantiable"
        except TypeError as e:
            assert "abstract class" in str(e).lower()

    def test_atp_definition_concrete_implementation(self):
        """
        Test that a concrete implementation of AtpDefinition works correctly.
        This test covers the super().__init__(parent, short_name) call in AtpDefinition.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        class ConcreteAtpDefinition(AtpDefinition):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        obj = ConcreteAtpDefinition(ar_root, "ConcreteAtpDefinition")
        assert obj is not None
        assert obj.getShortName() == "ConcreteAtpDefinition"
        assert obj.getParent() == ar_root

    def test_atp_definition_inherits_from_referrable(self):
        """
        Test that AtpDefinition properly inherits from Referrable.
        """
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
            Referrable,
        )

        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        class ConcreteAtpDefinition(AtpDefinition):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        obj = ConcreteAtpDefinition(ar_root, "TestDefinition")
        assert isinstance(obj, Referrable)
        assert isinstance(obj, AtpDefinition)

    def test_atp_definition_short_name_property(self):
        """
        Test that shortName property works correctly.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        class ConcreteAtpDefinition(AtpDefinition):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        obj = ConcreteAtpDefinition(ar_root, "TestDefinition")
        assert obj.shortName == "TestDefinition"

        obj.shortName = "NewDefinitionName"
        assert obj.shortName == "NewDefinitionName"
        assert obj.getShortName() == "NewDefinitionName"

    def test_atp_definition_parent_reference(self):
        """
        Test that parent reference is properly set.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        class ConcreteAtpDefinition(AtpDefinition):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        obj = ConcreteAtpDefinition(ar_root, "TestDefinition")
        assert obj.getParent() == ar_root

    def test_atp_definition_full_name(self):
        """
        Test that full_name property works correctly.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        class ConcreteAtpDefinition(AtpDefinition):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        obj = ConcreteAtpDefinition(ar_root, "TestDefinition")
        # The full name should be parent's full name + / + short name
        assert obj.full_name == "/AUTOSAR/TestDefinition"
        assert obj.getFullName() == "/AUTOSAR/TestDefinition"

    def test_multiple_atp_definition_instances(self):
        """
        Test that multiple AtpDefinition instances can be created.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        class ConcreteAtpDefinition(AtpDefinition):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        obj1 = ConcreteAtpDefinition(ar_root, "Definition1")
        obj2 = ConcreteAtpDefinition(ar_root, "Definition2")

        assert obj1.getShortName() == "Definition1"
        assert obj2.getShortName() == "Definition2"
        assert obj1.getParent() == ar_root
        assert obj2.getParent() == ar_root

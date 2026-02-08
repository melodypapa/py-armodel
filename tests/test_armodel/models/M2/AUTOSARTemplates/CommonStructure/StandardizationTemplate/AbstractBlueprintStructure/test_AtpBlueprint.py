"""
This module contains comprehensive tests for the AtpBlueprint.py file
in the AUTOSAR CommonStructure module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure.AtpBlueprint import (
    AtpBlueprint,
)


class TestAtpBlueprint:
    """
    Test class for AtpBlueprint functionality.
    """

    def test_abstract_initialization(self):
        """
        Test that AtpBlueprint cannot be instantiated directly (abstract class).
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        try:
            obj = AtpBlueprint(ar_root, "TestAtpBlueprint")
            assert False, "AtpBlueprint should not be instantiable"
        except TypeError as e:
            assert "abstract class" in str(e).lower()

    def test_atp_blueprint_concrete_implementation(self):
        """
        Test that a concrete implementation of AtpBlueprint works correctly.
        This test covers the super().__init__(parent, short_name) call in AtpBlueprint.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        class ConcreteAtpBlueprint(AtpBlueprint):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        obj = ConcreteAtpBlueprint(ar_root, "ConcreteAtpBlueprint")
        assert obj is not None
        assert obj.getShortName() == "ConcreteAtpBlueprint"
        assert obj.getParent() == ar_root

    def test_atp_blueprint_inherits_from_identifiable(self):
        """
        Test that AtpBlueprint properly inherits from Identifiable.
        """
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
            Identifiable,
        )

        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        class ConcreteAtpBlueprint(AtpBlueprint):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        obj = ConcreteAtpBlueprint(ar_root, "TestBlueprint")
        assert isinstance(obj, Identifiable)
        assert isinstance(obj, AtpBlueprint)

    def test_atp_blueprint_short_name_property(self):
        """
        Test that shortName property works correctly.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        class ConcreteAtpBlueprint(AtpBlueprint):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        obj = ConcreteAtpBlueprint(ar_root, "TestBlueprint")
        assert obj.shortName == "TestBlueprint"

        obj.shortName = "NewBlueprintName"
        assert obj.shortName == "NewBlueprintName"
        assert obj.getShortName() == "NewBlueprintName"

    def test_atp_blueprint_admin_data(self):
        """
        Test that adminData can be set and retrieved.
        """
        from armodel.models.M2.MSR.AsamHdo.AdminData import AdminData

        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        class ConcreteAtpBlueprint(AtpBlueprint):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        obj = ConcreteAtpBlueprint(ar_root, "TestBlueprint")

        # Initially should be None
        assert obj.getAdminData() is None

        # Set admin data
        admin_data = AdminData()
        obj.setAdminData(admin_data)
        assert obj.getAdminData() is admin_data

        # Remove admin data
        obj.removeAdminData()
        assert obj.getAdminData() is None

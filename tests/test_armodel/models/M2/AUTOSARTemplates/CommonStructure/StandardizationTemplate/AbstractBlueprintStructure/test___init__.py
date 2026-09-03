"""
This module contains comprehensive tests for the AtpBlueprint.py file
in the AUTOSAR CommonStructure module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure import (
    AtpBlueprint,
    AtpBlueprintable,
    BlueprintPolicy,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import PackageableElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
    MultilanguageReferrable,
    Referrable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import String


class ConcreteAtpBlueprint(AtpBlueprint):
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)


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
            _obj = AtpBlueprint(ar_root, "TestAtpBlueprint")
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

        obj = ConcreteAtpBlueprint(ar_root, "ConcreteAtpBlueprint")
        assert obj is not None
        assert obj.getShortName() == "ConcreteAtpBlueprint"
        assert obj.getParent() == ar_root

    def test_atp_blueprint_inherits_from_identifiable(self):
        """
        Test that AtpBlueprint properly inherits from Identifiable.
        """
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable

        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        obj = ConcreteAtpBlueprint(ar_root, "TestBlueprint")
        assert isinstance(obj, Identifiable)
        assert isinstance(obj, AtpBlueprint)

    def test_atp_blueprint_short_name_property(self):
        """
        Test that shortName property works correctly.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

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

    def test_initial_blueprint_policys(self):
        """
        Test that blueprintPolicys is an empty list initially.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        obj = ConcreteAtpBlueprint(ar_root, "TestBlueprint")
        assert obj.blueprintPolicys == []
        assert obj.getBlueprintPolicys() == []

    def test_add_get_blueprint_policys(self):
        """
        Test addBlueprintPolicy/getBlueprintPolicys (incl. None no-op).
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        obj = ConcreteAtpBlueprint(ar_root, "TestBlueprint")

        value = ARObject.__new__(ARObject)
        assert obj.addBlueprintPolicy(value) is obj
        assert obj.getBlueprintPolicys() == [value]

        obj.addBlueprintPolicy(None)
        assert obj.getBlueprintPolicys() == [value]

    def test_atp_blueprint_heritage_closure(self):
        """
        Rule 0001.2 / 0001.11: AtpBlueprint is abstract; its most-derived direct base
        is Identifiable (spec Base closure = ARObject, Identifiable,
        MultilanguageReferrable, Referrable). AtpBlueprintable is NOT in the closure.
        """
        assert AtpBlueprint.__bases__[0] is Identifiable
        for base in (Identifiable, MultilanguageReferrable, Referrable, ARObject):
            assert base in AtpBlueprint.__mro__, "%s missing from MRO" % base
        assert AtpBlueprintable not in AtpBlueprint.__mro__

    def test_class_docstring_verbatim(self):
        """
        Rule 0001.4 / 0012.2.4: class docstring == spec Table C.12 Note verbatim.
        """
        note = "This meta-class represents the ability to act as a Blueprint. As this " "class is an abstract one, particular blueprint meta-classes inherit from " "this one."
        assert AtpBlueprint.__doc__ == note

    def test_blueprint_policy_docstrings_verbatim(self):
        """
        Rule 0001.4 / 0012.2.5: add/get docstrings start with the spec attribute Note
        verbatim ("This role indicates whether the blueprintable element will be
        modifiable or not modifiable."), not a "Gets/Sets the X" paraphrase.
        """
        note = "This role indicates whether the blueprintable element will be modifiable or not modifiable."
        assert AtpBlueprint.addBlueprintPolicy.__doc__ is not None
        assert AtpBlueprint.addBlueprintPolicy.__doc__.startswith(note)
        assert AtpBlueprint.getBlueprintPolicys.__doc__ is not None
        assert AtpBlueprint.getBlueprintPolicys.__doc__.startswith(note)


class ConcreteBlueprintPolicy(BlueprintPolicy):
    def __init__(self):
        super().__init__()


class TestBlueprintPolicy:
    """
    Test class for BlueprintPolicy (R23-11 AUTOSAR_FO_TPS_StandardizationTemplate
    Table C.18, p.164). Abstract, Base = ARObject only, one attribute attributeName.
    """

    def test_abstract_initialization(self):
        """
        Rule 0001.2: BlueprintPolicy cannot be instantiated directly (abstract class).
        """
        try:
            _obj = BlueprintPolicy()
            assert False, "BlueprintPolicy should not be instantiable"
        except TypeError as e:
            assert "abstract" in str(e).lower()

    def test_concrete_subclass_instantiation(self):
        """
        Rule 0001.2 / 0011: a concrete subclass instantiates and inherits attributeName
        (default None).
        """
        obj = ConcreteBlueprintPolicy()
        assert obj is not None
        assert obj.getAttributeName() is None

    def test_get_set_attribute_name_round_trip(self):
        """
        Rule 0001.6 / 0004: setAttributeName stores the value; getAttributeName returns it;
        None is a no-op and returns self for chaining.
        """
        obj = ConcreteBlueprintPolicy()
        value = String()
        value.setValue("TIMING-EVENT-PROTOTYPE")
        assert obj.setAttributeName(value) is obj
        assert obj.getAttributeName() is value
        obj.setAttributeName(None)
        assert obj.getAttributeName() is value

    def test_class_docstring_verbatim(self):
        """
        Rule 0001.4 / 0012.2.4: class docstring == spec Table C.18 Note verbatim.
        """
        note = "This meta-class represents the ability to indicate whether blueprintable elements will be modifiable or not modifiable."
        assert BlueprintPolicy.__doc__ == note

    def test_attribute_name_docstrings_verbatim(self):
        """
        Rule 0001.4 / 0012.2.5: get/set docstrings start with the spec attribute Note
        verbatim ("This identifies the related attribute of a BlueprintPolicy. For
        navigation over the model a subset of xpath expressions is used.").
        """
        note = "This identifies the related attribute of a BlueprintPolicy. For navigation over the model a subset of xpath expressions is used."
        assert BlueprintPolicy.setAttributeName.__doc__ is not None
        assert BlueprintPolicy.setAttributeName.__doc__.startswith(note)
        assert BlueprintPolicy.getAttributeName.__doc__ is not None
        assert BlueprintPolicy.getAttributeName.__doc__.startswith(note)


class ConcreteAtpBlueprintable(AtpBlueprintable):
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)


class TestAtpBlueprintable:
    """
    Test class for AtpBlueprintable heritage fix (R23-11 AUTOSAR_FO_TPS_
    StandardizationTemplate Table C.14, p.162). Abstract; Base closure =
    ARObject, Identifiable, MultilanguageReferrable, Referrable. Re-parented
    from PackageableElement to Identifiable (no PackageableElement/
    CollectableElement in the chain).
    """

    def test_abstract_initialization(self):
        """
        Rule 0001.2: AtpBlueprintable cannot be instantiated directly (abstract class).
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        try:
            _obj = AtpBlueprintable(ar_root, "TestAtpBlueprintable")
            assert False, "AtpBlueprintable should not be instantiable"
        except TypeError as e:
            assert "abstract" in str(e).lower()

    def test_direct_base_is_identifiable(self):
        """
        Rule 0001.2 / heritage fix: most-derived direct base is Identifiable,
        not PackageableElement.
        """
        assert AtpBlueprintable.__bases__[0] is Identifiable

    def test_mro_has_spec_closure(self):
        """
        Rule 0001.2: MRO == ARObject / Identifiable / MultilanguageReferrable /
        Referrable (spec Base closure).
        """
        for base in (Identifiable, MultilanguageReferrable, Referrable, ARObject):
            assert base in AtpBlueprintable.__mro__, "%s missing from MRO" % base

    def test_not_packageable_element(self):
        """
        Rule 0001.2 / heritage fix: PackageableElement (and CollectableElement)
        are NOT in the MRO -- AtpBlueprintable is a direct Identifiable, not a
        PackageableElement.
        """
        assert PackageableElement not in AtpBlueprintable.__mro__

    def test_concrete_subclass_instantiation(self):
        """
        Rule 0001.2 / 0011: a concrete subclass instantiates and reaches
        parent/short_name via the Identifiable chain.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        obj = ConcreteAtpBlueprintable(ar_root, "ConcreteAtpBlueprintable")
        assert obj is not None
        assert obj.getShortName() == "ConcreteAtpBlueprintable"
        assert obj.getParent() == ar_root

    def test_class_docstring_verbatim(self):
        """
        Rule 0001.4 / 0012.2.4: class docstring == spec Table C.14 Note verbatim.
        """
        note = "This meta-class represents the ability to be derived from a Blueprint. " "As this class is an abstract one, particular blueprintable meta-classes " "inherit from this one."
        assert AtpBlueprintable.__doc__ == note

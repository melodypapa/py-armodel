"""
This module contains comprehensive tests for the AbstractStructure.py file
in the AUTOSAR GenericStructure module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure import AtpBlueprintable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpClassifier, AtpFeature, AtpInstanceRef, AtpPrototype, AtpStructureElement, AtpType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.AnyInstanceRef import AnyInstanceRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType, String


class TestAtpFeature:
    """
    Test class for AtpFeature functionality.
    """

    def test_abstract_initialization(self):
        """
        Test that AtpFeature cannot be instantiated directly (abstract class).
        """
        try:
            parent = AUTOSAR.getInstance()
            ar_root = parent.createARPackage("AUTOSAR")
            _obj = AtpFeature(ar_root, "TestAtpFeature")
            assert False, "AtpFeature should not be instantiable"
        except TypeError:
            pass  # Expected behavior

    def test_concrete_subclass_is_identifiable(self):
        """
        Test that a concrete subclass of AtpFeature is an Identifiable.
        """

        class ConcreteAtpFeature(AtpFeature):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        obj = ConcreteAtpFeature(ar_root, "ConcreteAtpFeature")
        assert isinstance(obj, Identifiable)
        assert obj.getShortName() == "ConcreteAtpFeature"


class TestAtpInstanceRef:
    """
    Test class for AtpInstanceRef functionality.
    """

    def test_abstract_initialization(self):
        """
        Test that AtpInstanceRef cannot be instantiated directly (abstract class).
        """
        try:
            _obj = AtpInstanceRef()
            assert False, "AtpInstanceRef should not be instantiable"
        except TypeError:
            pass  # Expected behavior

    def test_get_set_atp_base_ref(self):
        """
        Test get/set methods for ATP base reference.
        """

        # Create a concrete subclass for testing
        class ConcreteAtpInstanceRef(AtpInstanceRef):
            def __init__(self):
                super().__init__()

        concrete_obj = ConcreteAtpInstanceRef()

        # Test initial value
        assert concrete_obj.getAtpBaseRef() is None

        # Test setting ATP base ref
        ref = RefType().setValue("/Package/Element")
        result = concrete_obj.setAtpBaseRef(ref)
        assert result is concrete_obj  # Verify method chaining
        assert concrete_obj.getAtpBaseRef() == ref
        # None is a no-op and does not overwrite an existing atpBaseRef
        assert concrete_obj.setAtpBaseRef(None) is concrete_obj
        assert concrete_obj.getAtpBaseRef() == ref

    def test_add_atp_context_element_ref_none_noop(self):
        """
        Test addAtpContextElementRef with None value is a no-op.
        """

        class ConcreteAtpInstanceRef(AtpInstanceRef):
            def __init__(self):
                super().__init__()

        concrete_obj = ConcreteAtpInstanceRef()
        assert concrete_obj.addAtpContextElementRef(None) is concrete_obj
        assert concrete_obj.getAtpContextElementRefs() == []

    def test_get_atp_context_element_refs(self):
        """
        Test getAtpContextElementRefs method returns empty list by default.
        """

        # Create a concrete subclass for testing
        class ConcreteAtpInstanceRef(AtpInstanceRef):
            def __init__(self):
                super().__init__()

        concrete_obj = ConcreteAtpInstanceRef()

        # Verify initial state
        refs = concrete_obj.getAtpContextElementRefs()
        assert refs == []
        assert isinstance(refs, list)

    def test_add_atp_context_element_ref(self):
        """
        Test addAtpContextElementRef method adds references correctly.
        """

        # Create a concrete subclass for testing
        class ConcreteAtpInstanceRef(AtpInstanceRef):
            def __init__(self):
                super().__init__()

        concrete_obj = ConcreteAtpInstanceRef()

        # Create mock RefType instances
        ref1 = RefType().setValue("ContextRef1")
        ref2 = RefType().setValue("ContextRef2")

        # Add first reference
        result = concrete_obj.addAtpContextElementRef(ref1)
        assert result is concrete_obj  # Verify method chaining
        assert concrete_obj.getAtpContextElementRefs() == [ref1]

        # Add second reference
        concrete_obj.addAtpContextElementRef(ref2)
        assert concrete_obj.getAtpContextElementRefs() == [ref1, ref2]

    def test_get_set_atp_target_ref(self):
        """
        Test get/set methods for ATP target reference.
        """

        # Create a concrete subclass for testing
        class ConcreteAtpInstanceRef(AtpInstanceRef):
            def __init__(self):
                super().__init__()

        concrete_obj = ConcreteAtpInstanceRef()

        # Test initial value
        assert concrete_obj.getAtpTargetRef() is None

        # Test setting ATP target ref
        ref = RefType().setValue("/Package/Target")
        result = concrete_obj.setAtpTargetRef(ref)
        assert result is concrete_obj  # Verify method chaining
        assert concrete_obj.getAtpTargetRef() == ref
        # None is a no-op and does not overwrite an existing atpTargetRef
        assert concrete_obj.setAtpTargetRef(None) is concrete_obj
        assert concrete_obj.getAtpTargetRef() == ref


class TestAnyInstanceRef:
    """
    Test class for AnyInstanceRef functionality.
    """

    def test_initialization(self):
        """
        Test AnyInstanceRef initialization.
        """
        obj = AnyInstanceRef()

        # Verify basic properties
        assert obj is not None

        # Verify default values for attributes
        assert obj.getBaseRef() is None
        assert obj.getContextElementRefs() == []
        assert obj.getTargetRef() is None

    def test_get_set_base_ref(self):
        """
        Test get/set methods for base reference.
        """
        obj = AnyInstanceRef()

        # Test initial value
        assert obj.getBaseRef() is None

        # Test setting base ref
        ref = RefType().setValue("/Package/Element")
        result = obj.setBaseRef(ref)
        assert result is obj  # Verify method chaining
        assert obj.getBaseRef() == ref

    def test_get_context_element_refs(self):
        """
        Test getContextElementRefs method returns empty list by default.
        """
        obj = AnyInstanceRef()

        # Verify initial state
        refs = obj.getContextElementRefs()
        assert refs == []
        assert isinstance(refs, list)

    def test_add_context_element_ref(self):
        """
        Test addContextElementRef method adds references correctly.
        """
        obj = AnyInstanceRef()

        # Create mock RefType instances
        ref1 = RefType().setValue("ContextRef1")
        ref2 = RefType().setValue("ContextRef2")

        # Add first reference
        result = obj.addContextElementRef(ref1)
        assert result is obj  # Verify method chaining
        assert obj.getContextElementRefs() == [ref1]

        # Add second reference
        obj.addContextElementRef(ref2)
        assert obj.getContextElementRefs() == [ref1, ref2]

    def test_get_set_target_ref(self):
        """
        Test get/set methods for target reference.
        """
        obj = AnyInstanceRef()

        # Test initial value
        assert obj.getTargetRef() is None

        # Test setting target ref
        ref = RefType().setValue("/Package/Target")
        result = obj.setTargetRef(ref)
        assert result is obj  # Verify method chaining
        assert obj.getTargetRef() == ref


class TestAtpBlueprintable:
    """
    Test class for AtpBlueprintable functionality.
    """

    def test_abstract_initialization(self):
        """
        Test that AtpBlueprintable cannot be instantiated directly (abstract class).
        """
        try:
            parent = AUTOSAR.getInstance()
            ar_root = parent.createARPackage("AUTOSAR")
            _obj = AtpBlueprintable(ar_root, "TestAtpBlueprintable")
            assert False, "AtpBlueprintable should not be instantiable"
        except TypeError:
            pass  # Expected behavior


class TestAtpStructureElement:
    """
    Test class for AtpStructureElement functionality.
    """

    def test_initialization(self):
        """
        Test that AtpStructureElement cannot be instantiated directly (abstract class).
        After fixing the bug, AtpStructureElement is now properly abstract.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        try:
            _obj = AtpStructureElement(ar_root, "TestAtpStructureElement")
            assert False, "AtpStructureElement should not be instantiable"
        except TypeError:
            pass  # Expected behavior after bug fix

    def test_atp_structure_element_abstract_initialization(self):
        # Test that AtpStructureElement cannot be instantiated directly
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        try:
            AtpStructureElement(ar_root, "test_element")
            assert False, "AtpStructureElement should not be instantiable"
        except TypeError:
            pass  # Expected behavior

    def test_atp_structure_element_concrete_implementation(self):
        # Test that a concrete implementation of AtpStructureElement works
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        class ConcreteAtpStructureElement(AtpStructureElement):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        element = ConcreteAtpStructureElement(ar_root, "test_element")
        assert isinstance(element, AtpStructureElement)
        assert element.getShortName() == "test_element"
        assert element.getParent() == ar_root

    def test_direct_bases_are_atp_classifier_and_atp_feature(self):
        # R23-11 Table 5.5 Base closure = ARObject, AtpClassifier, AtpFeature,
        # Identifiable, MultilanguageReferrable, Referrable. AtpClassifier and
        # AtpFeature are parallel branches (both derive from Identifiable), so
        # both are direct bases. AtpBlueprintable is NOT in the closure.
        assert AtpStructureElement.__bases__[0] is AtpClassifier
        assert AtpFeature in AtpStructureElement.__bases__
        assert issubclass(AtpStructureElement, AtpClassifier)
        assert issubclass(AtpStructureElement, AtpFeature)
        assert not issubclass(AtpStructureElement, AtpBlueprintable)

    def test_mro_matches_spec_base_closure(self):
        mro_names = [cls.__name__ for cls in AtpStructureElement.__mro__]
        spec_base_closure = [
            "ARObject",
            "AtpClassifier",
            "AtpFeature",
            "Identifiable",
            "MultilanguageReferrable",
            "Referrable",
        ]
        for name in spec_base_closure:
            assert name in mro_names
        assert mro_names[1] == "AtpClassifier"
        assert mro_names[2] == "AtpFeature"
        assert "AtpBlueprintable" not in mro_names

    def test_concrete_subclass_reaches_identifiable_members(self):
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        class ConcreteAtpStructureElement(AtpStructureElement):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        element = ConcreteAtpStructureElement(ar_root, "test_element")
        assert isinstance(element, Identifiable)
        assert isinstance(element, ARObject)
        uuid = String()
        uuid.setValue("urn:uuid:00000000-0000-0000-0000-000000000001")
        element.setUuid(uuid)
        assert element.getUuid().getValue() == "urn:uuid:00000000-0000-0000-0000-000000000001"
        assert element.getAtpFeatures() == []
        assert element.getShortName() == "test_element"

    def test_class_docstring_matches_spec_note(self):
        assert AtpStructureElement.__doc__ == ("A structure element is both a classifier and a feature. As a feature, its structure is given by the feature it owns as a classifier.")


class TestAtpType:
    """
    Test class for AtpType functionality.
    """

    def test_abstract_initialization(self):
        """
        Test that AtpType cannot be instantiated directly (abstract class).
        """
        try:
            parent = AUTOSAR.getInstance()
            ar_root = parent.createARPackage("AUTOSAR")
            _obj = AtpType(ar_root, "TestAtpType")
            assert False, "AtpType should not be instantiable"
        except TypeError:
            pass  # Expected behavior

    def test_atp_type_concrete_implementation(self):
        """
        Test that a concrete implementation of AtpType works correctly.
        This test covers the super().__init__(parent, short_name) call in AtpType.
        """
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpType

        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        class ConcreteAtpType(AtpType):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        obj = ConcreteAtpType(ar_root, "ConcreteAtpType")
        assert obj is not None
        assert obj.getShortName() == "ConcreteAtpType"
        assert obj.getParent() == ar_root

    def test_inherits_from_atp_classifier(self):
        """
        Test that AtpType's most-derived direct base is AtpClassifier (Table 5.6).
        """
        assert issubclass(AtpType, AtpClassifier)
        assert issubclass(AtpType, Identifiable)
        assert issubclass(AtpType, ARObject)
        mro = AtpType.__mro__
        assert mro[0] is AtpType
        assert mro[1] is AtpClassifier
        assert mro[2] is Identifiable

    def test_class_docstring_matches_spec_note(self):
        """
        Test that AtpType's class docstring is the verbatim Table 5.6 Note.
        """
        expected = "A type is a classifier that may serve to type prototypes. It is a reusable classifier."
        assert AtpType.__doc__ == expected


class TestAtpClassifier:
    """Test class for AtpClassifier functionality."""

    def test_abstract_initialization(self):
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        try:
            _obj = AtpClassifier(ar_root, "TestAtpClassifier")
            assert False, "AtpClassifier should not be instantiable"
        except TypeError:
            pass

    def test_concrete_subclass_base_and_atp_features(self):
        class ConcreteAtpClassifier(AtpClassifier):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        obj = ConcreteAtpClassifier(ar_root, "ConcreteAtpClassifier")
        # Spec Table 5.1: Base is Identifiable (most-derived)
        assert isinstance(obj, Identifiable)
        # Spec Table 5.1: atpFeature * aggr (atpDerived, no XML element)
        assert obj.getAtpFeatures() == []
        assert obj.addAtpFeature(None) is obj
        assert obj.getAtpFeatures() == []


class TestAtpPrototype:
    """
    Test class for AtpPrototype functionality (Table 5.4).
    """

    @staticmethod
    def _make_ref_type():
        return RefType().setValue("/Type/MyType").setDest("ATP-TYPE--SUBTYPES-ENUM").setBase("")

    def test_abstract_initialization(self):
        """
        Test that AtpPrototype cannot be instantiated directly (abstract class).
        """
        try:
            parent = AUTOSAR.getInstance()
            ar_root = parent.createARPackage("AUTOSAR")
            _obj = AtpPrototype(ar_root, "TestAtpPrototype")
            assert False, "AtpPrototype should not be instantiable"
        except TypeError:
            pass  # Expected behavior

    def test_inherits_from_atp_feature(self):
        """
        Test that AtpPrototype's most-derived direct base is AtpFeature (Table 5.4),
        and that it no longer carries AtpBlueprintable transitively.
        """

        class ConcreteAtpPrototype(AtpPrototype):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        assert issubclass(AtpPrototype, AtpFeature)
        assert issubclass(AtpPrototype, Identifiable)
        assert issubclass(AtpPrototype, ARObject)
        mro = AtpPrototype.__mro__
        assert mro[0] is AtpPrototype
        assert mro[1] is AtpFeature
        assert not issubclass(AtpPrototype, AtpBlueprintable)
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        obj = ConcreteAtpPrototype(ar_root, "ConcreteAtpPrototype")
        assert isinstance(obj, AtpFeature)
        assert isinstance(obj, Identifiable)
        assert obj.getShortName() == "ConcreteAtpPrototype"
        assert obj.getParent() is ar_root

    def test_atp_type_default_is_none(self):
        """
        Test that atpType defaults to None (Table 5.4: atpType AtpType 1 ref).
        """

        class ConcreteAtpPrototype(AtpPrototype):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        obj = ConcreteAtpPrototype(ar_root, "ConcreteAtpPrototype")
        assert obj.getAtpTypeRef() is None

    def test_set_atp_type_round_trip(self):
        """
        Test setting and getting atpType (Table 5.4: atpType AtpType 1 ref).
        """
        ref = self._make_ref_type()
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        class ConcreteAtpPrototype(AtpPrototype):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        obj = ConcreteAtpPrototype(ar_root, "ConcreteAtpPrototype")
        assert obj.setAtpTypeRef(ref) is obj
        assert obj.getAtpTypeRef() is ref
        assert obj.getAtpTypeRef().getValue() == "/Type/MyType"

    def test_set_atp_type_none_is_noop(self):
        """
        Test that setAtpTypeRef(None) is a no-op and does not overwrite an existing value.
        """
        ref = self._make_ref_type()
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        class ConcreteAtpPrototype(AtpPrototype):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        obj = ConcreteAtpPrototype(ar_root, "ConcreteAtpPrototype")
        obj.setAtpTypeRef(ref)
        obj.setAtpTypeRef(None)
        assert obj.getAtpTypeRef() is ref

    def test_class_docstring_matches_spec_note(self):
        """
        Test that AtpPrototype's class docstring is the verbatim Table 5.4 Note.
        """
        expected = (
            "A prototype is a typed feature. A prototype in a classifier indicates that "
            "instances of that classifier will have a feature, and the structure of that "
            "feature is given by the its type. An instance of that type will play the role "
            "indicated by the feature in the owning classifier. A feature is not an instance "
            "but an indication of an instance-to-be."
        )
        assert AtpPrototype.__doc__ == expected

"""
This module contains comprehensive tests for the AbstractStructure.py file
in the AUTOSAR GenericStructure module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpInstanceRef, AtpFeature, AtpStructureElement, AtpType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.AnyInstanceRef import AnyInstanceRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType


class TestAtpInstanceRef:
    """
    Test class for AtpInstanceRef functionality.
    """

    def test_abstract_initialization(self):
        """
        Test that AtpInstanceRef cannot be instantiated directly (abstract class).
        """
        try:
            obj = AtpInstanceRef()
            assert False, "AtpInstanceRef should not be instantiable"
        except NotImplementedError:
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
            obj = AtpFeature(ar_root, "TestAtpFeature")
            assert False, "AtpFeature should not be instantiable"
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
            obj = AtpStructureElement(ar_root, "TestAtpStructureElement")
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
            obj = AtpType(ar_root, "TestAtpType")
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
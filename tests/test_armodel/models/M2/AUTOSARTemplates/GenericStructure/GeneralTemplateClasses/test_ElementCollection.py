"""
This module contains comprehensive tests for the ElementCollection.py file
in the AUTOSAR GenericStructure module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.AnyInstanceRef import (
    AnyInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ElementCollection import (
    Collection,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
    NameToken,
    RefType,
)


class TestCollection:
    """
    Test class for Collection functionality.
    """

    def test_initialization(self):
        """
        Test Collection initialization with parent and short name.
        """
        # Create parent AUTOSAR structure
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        # Create Collection instance
        collection = Collection(ar_root, "TestCollection")

        # Verify basic properties
        assert collection is not None
        assert collection.getShortName() == "TestCollection"

        # Verify default values for attributes
        assert collection.getAutoCollect() is None
        assert collection.getCollectedInstances() == []
        assert collection.getCollectionSemantics() is None
        assert collection.getElementRefs() == []
        assert collection.getElementRole() is None
        assert collection.getSourceElementRefs() == []
        assert collection.getSourceInstances() == []

    def test_get_auto_collect(self):
        """
        Test getAutoCollect method returns None by default.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        collection = Collection(ar_root, "TestCollection")

        # Verify initial state
        auto_collect = collection.getAutoCollect()
        assert auto_collect is None

    def test_set_auto_collect(self):
        """
        Test setAutoCollect method sets the auto-collect setting correctly.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        collection = Collection(ar_root, "TestCollection")

        # Note: AutoCollectEnum is not defined in the source code, so using a mock
        class MockAutoCollectEnum:
            pass
        auto_collect_setting = MockAutoCollectEnum()

        # Set the auto-collect setting
        result = collection.setAutoCollect(auto_collect_setting)
        assert result is collection  # Verify method chaining
        assert collection.getAutoCollect() == auto_collect_setting

    def test_set_auto_collect_none(self):
        """
        Test setAutoCollect method handles None value correctly.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        collection = Collection(ar_root, "TestCollection")

        # Set initial value
        class MockAutoCollectEnum:
            pass
        initial_setting = MockAutoCollectEnum()
        collection.setAutoCollect(initial_setting)
        assert collection.getAutoCollect() == initial_setting

        # Set to None - should not change the value (per implementation logic)
        result = collection.setAutoCollect(None)
        assert result is collection  # Verify method chaining
        # Value should remain unchanged due to "if value is not None" check
        assert collection.getAutoCollect() == initial_setting

    def test_get_collected_instances(self):
        """
        Test getCollectedInstances method returns empty list by default.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        collection = Collection(ar_root, "TestCollection")

        # Verify initial state
        instances = collection.getCollectedInstances()
        assert instances == []
        assert isinstance(instances, list)

    def test_set_collected_instances(self):
        """
        Test setCollectedInstances method sets collected instances correctly.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        collection = Collection(ar_root, "TestCollection")

        # Create mock AnyInstanceRef instances
        instance1 = AnyInstanceRef()
        instance2 = AnyInstanceRef()
        instances = [instance1, instance2]

        # Set the collected instances
        result = collection.setCollectedInstances(instances)
        assert result is collection  # Verify method chaining
        assert collection.getCollectedInstances() == instances

    def test_set_collected_instances_none(self):
        """
        Test setCollectedInstances method handles None value correctly.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        collection = Collection(ar_root, "TestCollection")

        # Set initial values
        instance1 = AnyInstanceRef()
        initial_instances = [instance1]
        collection.setCollectedInstances(initial_instances)
        assert collection.getCollectedInstances() == initial_instances

        # Set to None - should not change the value (per implementation logic)
        result = collection.setCollectedInstances(None)
        assert result is collection  # Verify method chaining
        # Value should remain unchanged due to "if value is not None" check
        assert collection.getCollectedInstances() == initial_instances

    def test_get_collection_semantics(self):
        """
        Test getCollectionSemantics method returns None by default.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        collection = Collection(ar_root, "TestCollection")

        # Verify initial state
        semantics = collection.getCollectionSemantics()
        assert semantics is None

    def test_set_collection_semantics(self):
        """
        Test setCollectionSemantics method sets the collection semantics correctly.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        collection = Collection(ar_root, "TestCollection")

        # Create mock NameToken instance
        semantics = NameToken().setValue("TestSemantics")

        # Set the collection semantics
        result = collection.setCollectionSemantics(semantics)
        assert result is collection  # Verify method chaining
        assert collection.getCollectionSemantics() == semantics

    def test_set_collection_semantics_none(self):
        """
        Test setCollectionSemantics method handles None value correctly.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        collection = Collection(ar_root, "TestCollection")

        # Set initial value
        initial_semantics = NameToken().setValue("TestSemantics")
        collection.setCollectionSemantics(initial_semantics)
        assert collection.getCollectionSemantics() == initial_semantics

        # Set to None - should not change the value (per implementation logic)
        result = collection.setCollectionSemantics(None)
        assert result is collection  # Verify method chaining
        # Value should remain unchanged due to "if value is not None" check
        assert collection.getCollectionSemantics() == initial_semantics

    def test_get_element_refs(self):
        """
        Test getElementRefs method returns empty list by default.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        collection = Collection(ar_root, "TestCollection")

        # Verify initial state
        refs = collection.getElementRefs()
        assert refs == []
        assert isinstance(refs, list)

    def test_add_element_ref(self):
        """
        Test addElementRef method adds element references correctly.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        collection = Collection(ar_root, "TestCollection")

        # Create mock RefType instances
        ref1 = RefType().setValue("Ref1")
        ref2 = RefType().setValue("Ref2")

        # Add first reference
        result = collection.addElementRef(ref1)
        assert result is collection  # Verify method chaining
        assert collection.getElementRefs() == [ref1]

        # Add second reference
        collection.addElementRef(ref2)
        assert collection.getElementRefs() == [ref1, ref2]

    def test_add_element_ref_none(self):
        """
        Test addElementRef method handles None value correctly.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        collection = Collection(ar_root, "TestCollection")

        # Add None value - should not add to list
        result = collection.addElementRef(None)
        assert result is collection  # Verify method chaining
        assert collection.getElementRefs() == []

    def test_get_element_role(self):
        """
        Test getElementRole method returns None by default.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        collection = Collection(ar_root, "TestCollection")

        # Verify initial state
        role = collection.getElementRole()
        assert role is None

    def test_set_element_role(self):
        """
        Test setElementRole method sets the element role correctly.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        collection = Collection(ar_root, "TestCollection")

        # Create mock Identifier instance
        role = Identifier().setValue("TestRole")

        # Set the element role
        result = collection.setElementRole(role)
        assert result is collection  # Verify method chaining
        assert collection.getElementRole() == role

    def test_set_element_role_none(self):
        """
        Test setElementRole method handles None value correctly.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        collection = Collection(ar_root, "TestCollection")

        # Set initial value
        initial_role = Identifier().setValue("TestRole")
        collection.setElementRole(initial_role)
        assert collection.getElementRole() == initial_role

        # Set to None - should not change the value (per implementation logic)
        result = collection.setElementRole(None)
        assert result is collection  # Verify method chaining
        # Value should remain unchanged due to "if value is not None" check
        assert collection.getElementRole() == initial_role

    def test_get_source_element_refs(self):
        """
        Test getSourceElementRefs method returns empty list by default.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        collection = Collection(ar_root, "TestCollection")

        # Verify initial state
        refs = collection.getSourceElementRefs()
        assert refs == []
        assert isinstance(refs, list)

    def test_add_source_element_ref(self):
        """
        Test addSourceElementRef method adds source element references correctly.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        collection = Collection(ar_root, "TestCollection")

        # Create mock RefType instances
        ref1 = RefType().setValue("SourceRef1")
        ref2 = RefType().setValue("SourceRef2")

        # Add first reference
        result = collection.addSourceElementRef(ref1)
        assert result is collection  # Verify method chaining
        assert collection.getSourceElementRefs() == [ref1]

        # Add second reference
        collection.addSourceElementRef(ref2)
        assert collection.getSourceElementRefs() == [ref1, ref2]

    def test_add_source_element_ref_none(self):
        """
        Test addSourceElementRef method handles None value correctly.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        collection = Collection(ar_root, "TestCollection")

        # Add None value - should not add to list
        result = collection.addSourceElementRef(None)
        assert result is collection  # Verify method chaining
        assert collection.getSourceElementRefs() == []

    def test_get_source_instances(self):
        """
        Test getSourceInstances method returns empty list by default.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        collection = Collection(ar_root, "TestCollection")

        # Verify initial state
        instances = collection.getSourceInstances()
        assert instances == []
        assert isinstance(instances, list)

    def test_set_source_instances(self):
        """
        Test setSourceInstances method sets source instances correctly.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        collection = Collection(ar_root, "TestCollection")

        # Create mock AnyInstanceRef instances
        instance1 = AnyInstanceRef()
        instance2 = AnyInstanceRef()
        instances = [instance1, instance2]

        # Set the source instances
        result = collection.setSourceInstances(instances)
        assert result is collection  # Verify method chaining
        assert collection.getSourceInstances() == instances

    def test_set_source_instances_none(self):
        """
        Test setSourceInstances method handles None value correctly.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        collection = Collection(ar_root, "TestCollection")

        # Set initial values
        instance1 = AnyInstanceRef()
        initial_instances = [instance1]
        collection.setSourceInstances(initial_instances)
        assert collection.getSourceInstances() == initial_instances

        # Set to None - should not change the value (per implementation logic)
        result = collection.setSourceInstances(None)
        assert result is collection  # Verify method chaining
        # Value should remain unchanged due to "if value is not None" check
        assert collection.getSourceInstances() == initial_instances

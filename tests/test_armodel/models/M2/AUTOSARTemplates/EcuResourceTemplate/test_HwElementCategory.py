"""
This module contains comprehensive tests for the EcuResourceTemplate HwElementCategory.py file
in the AUTOSAR EcuResourceTemplate module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwElementCategory import (
    HwType,
    HwAttributeDef,
    HwCategory
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    RefType
)


class TestHwType:
    """
    Test class for HwType functionality.
    """

    def test_initialization(self):
        """
        Test HwType initialization with parent and short name.
        """
        # Create parent AUTOSAR structure
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        # Create HwType instance
        hw_type = HwType(ar_root, "TestHwType")

        # Verify basic properties
        assert hw_type is not None
        assert hw_type.getShortName() == "TestHwType"


class TestHwAttributeDef:
    """
    Test class for HwAttributeDef functionality.
    """

    def test_initialization(self):
        """
        Test HwAttributeDef initialization with parent and short name.
        """
        # Create parent AUTOSAR structure
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        # Create HwAttributeDef instance
        hw_attr_def = HwAttributeDef(ar_root, "TestHwAttributeDef")

        # Verify basic properties
        assert hw_attr_def is not None
        assert hw_attr_def.getShortName() == "TestHwAttributeDef"

        # Verify default values for attributes
        assert hw_attr_def.getHwAttributeLiterals() == []
        assert hw_attr_def.getIsRequired() is None
        assert hw_attr_def.getUnitRef() is None

    def test_get_hw_attribute_literals(self):
        """
        Test getHwAttributeLiterals method returns empty list by default.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        hw_attr_def = HwAttributeDef(ar_root, "TestHwAttributeDef")

        # Verify initial state
        literals = hw_attr_def.getHwAttributeLiterals()
        assert literals == []
        assert isinstance(literals, list)

    def test_set_hw_attribute_literals(self):
        """
        Test setHwAttributeLiterals method sets attribute literals correctly.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        hw_attr_def = HwAttributeDef(ar_root, "TestHwAttributeDef")

        # Create mock HwAttributeLiteralDef instances (using a simple class for testing)
        class MockHwAttributeLiteralDef:
            pass
        literal1 = MockHwAttributeLiteralDef()
        literal2 = MockHwAttributeLiteralDef()
        literals = [literal1, literal2]

        # Set the attribute literals
        result = hw_attr_def.setHwAttributeLiterals(literals)
        assert result is hw_attr_def  # Verify method chaining
        assert hw_attr_def.getHwAttributeLiterals() == literals

    def test_set_hw_attribute_literals_none(self):
        """
        Test setHwAttributeLiterals method handles None value correctly.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        hw_attr_def = HwAttributeDef(ar_root, "TestHwAttributeDef")

        # Set initial values
        class MockHwAttributeLiteralDef:
            pass
        initial_literal = MockHwAttributeLiteralDef()
        initial_literals = [initial_literal]
        hw_attr_def.setHwAttributeLiterals(initial_literals)
        assert hw_attr_def.getHwAttributeLiterals() == initial_literals

        # Set to None - should not change the value (per implementation logic)
        result = hw_attr_def.setHwAttributeLiterals(None)
        assert result is hw_attr_def  # Verify method chaining
        # Value should remain unchanged due to "if value is not None" check
        assert hw_attr_def.getHwAttributeLiterals() == initial_literals

    def test_get_is_required(self):
        """
        Test getIsRequired method returns None by default.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        hw_attr_def = HwAttributeDef(ar_root, "TestHwAttributeDef")

        # Verify initial state
        is_required = hw_attr_def.getIsRequired()
        assert is_required is None

    def test_set_is_required(self):
        """
        Test setIsRequired method sets the required flag correctly.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        hw_attr_def = HwAttributeDef(ar_root, "TestHwAttributeDef")

        # Create mock Boolean instance
        is_required = Boolean().setValue(True)

        # Set the required flag
        result = hw_attr_def.setIsRequired(is_required)
        assert result is hw_attr_def  # Verify method chaining
        assert hw_attr_def.getIsRequired() == is_required

    def test_set_is_required_none(self):
        """
        Test setIsRequired method handles None value correctly.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        hw_attr_def = HwAttributeDef(ar_root, "TestHwAttributeDef")

        # Set initial value
        initial_required = Boolean().setValue(True)
        hw_attr_def.setIsRequired(initial_required)
        assert hw_attr_def.getIsRequired() == initial_required

        # Set to None - should not change the value (per implementation logic)
        result = hw_attr_def.setIsRequired(None)
        assert result is hw_attr_def  # Verify method chaining
        # Value should remain unchanged due to "if value is not None" check
        assert hw_attr_def.getIsRequired() == initial_required

    def test_get_unit_ref(self):
        """
        Test getUnitRef method returns None by default.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        hw_attr_def = HwAttributeDef(ar_root, "TestHwAttributeDef")

        # Verify initial state
        unit_ref = hw_attr_def.getUnitRef()
        assert unit_ref is None

    def test_set_unit_ref(self):
        """
        Test setUnitRef method sets the unit reference correctly.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        hw_attr_def = HwAttributeDef(ar_root, "TestHwAttributeDef")

        # Create mock RefType instance
        unit_ref = RefType().setValue("UnitRef1")

        # Set the unit reference
        result = hw_attr_def.setUnitRef(unit_ref)
        assert result is hw_attr_def  # Verify method chaining
        assert hw_attr_def.getUnitRef() == unit_ref

    def test_set_unit_ref_none(self):
        """
        Test setUnitRef method handles None value correctly.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        hw_attr_def = HwAttributeDef(ar_root, "TestHwAttributeDef")

        # Set initial value
        initial_ref = RefType().setValue("UnitRef1")
        hw_attr_def.setUnitRef(initial_ref)
        assert hw_attr_def.getUnitRef() == initial_ref

        # Set to None - should not change the value (per implementation logic)
        result = hw_attr_def.setUnitRef(None)
        assert result is hw_attr_def  # Verify method chaining
        # Value should remain unchanged due to "if value is not None" check
        assert hw_attr_def.getUnitRef() == initial_ref


class TestHwCategory:
    """
    Test class for HwCategory functionality.
    """

    def test_initialization(self):
        """
        Test HwCategory initialization with parent and short name.
        """
        # Create parent AUTOSAR structure
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        # Create HwCategory instance
        hw_category = HwCategory(ar_root, "TestHwCategory")

        # Verify basic properties
        assert hw_category is not None
        assert hw_category.getShortName() == "TestHwCategory"

        # Verify default values for attributes
        assert hw_category.getHwAttributeDefs() == []

    def test_get_hw_attribute_defs(self):
        """
        Test getHwAttributeDefs method returns empty list by default.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        hw_category = HwCategory(ar_root, "TestHwCategory")

        # Verify initial state
        attr_defs = hw_category.getHwAttributeDefs()
        assert attr_defs == []
        assert isinstance(attr_defs, list)

    def test_create_hw_attribute_def(self):
        """
        Test createHwAttributeDef method creates and adds a new HwAttributeDef instance.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        hw_category = HwCategory(ar_root, "TestHwCategory")

        # Create a new HwAttributeDef
        new_attr_def = hw_category.createHwAttributeDef("NewAttributeDef")

        # Verify the created attribute definition
        assert new_attr_def is not None
        assert new_attr_def.getShortName() == "NewAttributeDef"
        # The instance should be in the list
        assert new_attr_def in hw_category.getHwAttributeDefs()

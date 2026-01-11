"""
This module contains comprehensive tests for the EcuResourceTemplate __init__.py file
in the AUTOSAR EcuResourceTemplate module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate import (
    HwDescriptionEntity,
    HwPin,
    HwPinGroupContent,
    HwPinGroup,
    HwElement
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
    RefType,
    String
)


class TestHwDescriptionEntity:
    """
    Test class for HwDescriptionEntity functionality.
    """

    def test_initialization(self):
        """
        Test HwDescriptionEntity initialization with parent and short name.
        """
        # Create parent AUTOSAR structure
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        # Create HwDescriptionEntity instance
        hw_entity = HwDescriptionEntity(ar_root, "TestHwDescriptionEntity")

        # Verify basic properties
        assert hw_entity is not None
        assert hw_entity.getShortName() == "TestHwDescriptionEntity"

        # Verify default values for attributes
        assert hw_entity.getHwAttributeValues() == []
        assert hw_entity.getHwCategoryRefs() == []
        assert hw_entity.getHwTypeRef() is None

    def test_get_hw_attribute_values(self):
        """
        Test getHwAttributeValues method returns empty list by default.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        hw_entity = HwDescriptionEntity(ar_root, "TestHwDescriptionEntity")

        # Verify initial state
        attr_values = hw_entity.getHwAttributeValues()
        assert attr_values == []
        assert isinstance(attr_values, list)

    def test_set_hw_attribute_values(self):
        """
        Test setHwAttributeValues method sets attribute values correctly.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        hw_entity = HwDescriptionEntity(ar_root, "TestHwDescriptionEntity")

        # Create mock HwAttributeValue instances (using a simple class for testing)
        class MockHwAttributeValue:
            pass
        value1 = MockHwAttributeValue()
        value2 = MockHwAttributeValue()
        values = [value1, value2]

        # Set the attribute values
        result = hw_entity.setHwAttributeValues(values)
        assert result is hw_entity  # Verify method chaining
        assert hw_entity.getHwAttributeValues() == values

    def test_set_hw_attribute_values_none(self):
        """
        Test setHwAttributeValues method handles None value correctly.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        hw_entity = HwDescriptionEntity(ar_root, "TestHwDescriptionEntity")

        # Set initial values
        class MockHwAttributeValue:
            pass
        initial_value = MockHwAttributeValue()
        initial_values = [initial_value]
        hw_entity.setHwAttributeValues(initial_values)
        assert hw_entity.getHwAttributeValues() == initial_values

        # Set to None - should not change the value (per implementation logic)
        result = hw_entity.setHwAttributeValues(None)
        assert result is hw_entity  # Verify method chaining
        # Value should remain unchanged due to "if value is not None" check
        assert hw_entity.getHwAttributeValues() == initial_values

    def test_get_hw_category_refs(self):
        """
        Test getHwCategoryRefs method returns empty list by default.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        hw_entity = HwDescriptionEntity(ar_root, "TestHwDescriptionEntity")

        # Verify initial state
        category_refs = hw_entity.getHwCategoryRefs()
        assert category_refs == []
        assert isinstance(category_refs, list)

    def test_add_hw_category_ref(self):
        """
        Test addHwCategoryRef method adds references correctly.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        hw_entity = HwDescriptionEntity(ar_root, "TestHwDescriptionEntity")

        # Create mock RefType instances
        ref1 = RefType().setValue("Category1")
        ref2 = RefType().setValue("Category2")

        # Add first reference
        result = hw_entity.addHwCategoryRef(ref1)
        assert result is hw_entity  # Verify method chaining
        assert hw_entity.getHwCategoryRefs() == [ref1]

        # Add second reference
        hw_entity.addHwCategoryRef(ref2)
        assert hw_entity.getHwCategoryRefs() == [ref1, ref2]

    def test_add_hw_category_ref_none(self):
        """
        Test addHwCategoryRef method handles None value correctly.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        hw_entity = HwDescriptionEntity(ar_root, "TestHwDescriptionEntity")

        # Add None value - should not add to list
        result = hw_entity.addHwCategoryRef(None)
        assert result is hw_entity  # Verify method chaining
        assert hw_entity.getHwCategoryRefs() == []

    def test_get_hw_type_ref(self):
        """
        Test getHwTypeRef method returns None by default.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        hw_entity = HwDescriptionEntity(ar_root, "TestHwDescriptionEntity")

        # Verify initial state
        type_ref = hw_entity.getHwTypeRef()
        assert type_ref is None

    def test_set_hw_type_ref(self):
        """
        Test setHwTypeRef method sets the type reference correctly.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        hw_entity = HwDescriptionEntity(ar_root, "TestHwDescriptionEntity")

        # Create mock RefType instance
        type_ref = RefType().setValue("HwType1")

        # Set the reference
        result = hw_entity.setHwTypeRef(type_ref)
        assert result is hw_entity  # Verify method chaining
        assert hw_entity.getHwTypeRef() == type_ref

    def test_set_hw_type_ref_none(self):
        """
        Test setHwTypeRef method handles None value correctly.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        hw_entity = HwDescriptionEntity(ar_root, "TestHwDescriptionEntity")

        # Set initial value
        initial_ref = RefType().setValue("HwType1")
        hw_entity.setHwTypeRef(initial_ref)
        assert hw_entity.getHwTypeRef() == initial_ref

        # Set to None - should not change the value (per implementation logic)
        result = hw_entity.setHwTypeRef(None)
        assert result is hw_entity  # Verify method chaining
        # Value should remain unchanged due to "if value is not None" check
        assert hw_entity.getHwTypeRef() == initial_ref


class TestHwPin:
    """
    Test class for HwPin functionality.
    """

    def test_initialization(self):
        """
        Test HwPin initialization with parent and short name.
        """
        # Create parent AUTOSAR structure
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        # Create HwPin instance
        hw_pin = HwPin(ar_root, "TestHwPin")

        # Verify basic properties
        assert hw_pin is not None
        assert hw_pin.getShortName() == "TestHwPin"

        # Verify default values for attributes (inherited and specific)
        assert hw_pin.getHwAttributeValues() == []
        assert hw_pin.getHwCategoryRefs() == []
        assert hw_pin.getHwTypeRef() is None
        assert hw_pin.getFunctionName() is None
        assert hw_pin.getPackagingPinName() is None
        assert hw_pin.getPinNumber() is None

    def test_get_function_name(self):
        """
        Test getFunctionName method returns None by default.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        hw_pin = HwPin(ar_root, "TestHwPin")

        # Verify initial state
        func_name = hw_pin.getFunctionName()
        assert func_name is None

    def test_set_function_name(self):
        """
        Test setFunctionName method sets the function name correctly.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        hw_pin = HwPin(ar_root, "TestHwPin")

        # Create mock String instance
        func_name = String().setValue("GPIO1")

        # Set the function name
        result = hw_pin.setFunctionName(func_name)
        assert result is hw_pin  # Verify method chaining
        assert hw_pin.getFunctionName() == func_name

    def test_set_function_name_none(self):
        """
        Test setFunctionName method handles None value correctly.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        hw_pin = HwPin(ar_root, "TestHwPin")

        # Set initial value
        initial_func = String().setValue("GPIO1")
        hw_pin.setFunctionName(initial_func)
        assert hw_pin.getFunctionName() == initial_func

        # Set to None - should not change the value (per implementation logic)
        result = hw_pin.setFunctionName(None)
        assert result is hw_pin  # Verify method chaining
        # Value should remain unchanged due to "if value is not None" check
        assert hw_pin.getFunctionName() == initial_func

    def test_get_packaging_pin_name(self):
        """
        Test getPackagingPinName method returns None by default.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        hw_pin = HwPin(ar_root, "TestHwPin")

        # Verify initial state
        packaging_name = hw_pin.getPackagingPinName()
        assert packaging_name is None

    def test_set_packaging_pin_name(self):
        """
        Test setPackagingPinName method sets the packaging pin name correctly.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        hw_pin = HwPin(ar_root, "TestHwPin")

        # Create mock String instance
        packaging_name = String().setValue("BGA500_PIN_1")

        # Set the packaging pin name
        result = hw_pin.setPackagingPinName(packaging_name)
        assert result is hw_pin  # Verify method chaining
        assert hw_pin.getPackagingPinName() == packaging_name

    def test_set_packaging_pin_name_none(self):
        """
        Test setPackagingPinName method handles None value correctly.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        hw_pin = HwPin(ar_root, "TestHwPin")

        # Set initial value
        initial_packaging = String().setValue("BGA500_PIN_1")
        hw_pin.setPackagingPinName(initial_packaging)
        assert hw_pin.getPackagingPinName() == initial_packaging

        # Set to None - should not change the value (per implementation logic)
        result = hw_pin.setPackagingPinName(None)
        assert result is hw_pin  # Verify method chaining
        # Value should remain unchanged due to "if value is not None" check
        assert hw_pin.getPackagingPinName() == initial_packaging

    def test_get_pin_number(self):
        """
        Test getPinNumber method returns None by default.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        hw_pin = HwPin(ar_root, "TestHwPin")

        # Verify initial state
        pin_number = hw_pin.getPinNumber()
        assert pin_number is None

    def test_set_pin_number(self):
        """
        Test setPinNumber method sets the pin number correctly.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        hw_pin = HwPin(ar_root, "TestHwPin")

        # Create mock Integer instance
        pin_number = Integer().setValue(1)

        # Set the pin number
        result = hw_pin.setPinNumber(pin_number)
        assert result is hw_pin  # Verify method chaining
        assert hw_pin.getPinNumber() == pin_number

    def test_set_pin_number_none(self):
        """
        Test setPinNumber method handles None value correctly.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        hw_pin = HwPin(ar_root, "TestHwPin")

        # Set initial value
        initial_number = Integer().setValue(1)
        hw_pin.setPinNumber(initial_number)
        assert hw_pin.getPinNumber() == initial_number

        # Set to None - should not change the value (per implementation logic)
        result = hw_pin.setPinNumber(None)
        assert result is hw_pin  # Verify method chaining
        # Value should remain unchanged due to "if value is not None" check
        assert hw_pin.getPinNumber() == initial_number


class TestHwPinGroupContent:
    """
    Test class for HwPinGroupContent functionality.
    """

    def test_initialization(self):
        """
        Test HwPinGroupContent initialization with default values.
        """
        # Create HwPinGroupContent instance
        hw_pin_group_content = HwPinGroupContent()

        # Verify basic properties
        assert hw_pin_group_content is not None

        # Verify default values for attributes
        assert hw_pin_group_content.getHwPin() is None
        assert hw_pin_group_content.getHwPinGroup() is None

    def test_get_hw_pin(self):
        """
        Test getHwPin method returns None by default.
        """
        hw_pin_group_content = HwPinGroupContent()

        # Verify initial state
        hw_pin = hw_pin_group_content.getHwPin()
        assert hw_pin is None

    def test_create_hw_pin(self):
        """
        Test createHwPin method creates and returns a new HwPin instance.
        """
        hw_pin_group_content = HwPinGroupContent()

        # Create a new HwPin (the createHwPin method creates the HwPin internally)
        new_pin = hw_pin_group_content.createHwPin("NewPin")

        # Verify the created pin
        assert new_pin is not None
        assert new_pin.getShortName() == "NewPin"
        # The instance should be stored in the hwPin attribute
        assert hw_pin_group_content.getHwPin() == new_pin

    def test_get_hw_pin_group(self):
        """
        Test getHwPinGroup method returns None by default.
        """
        hw_pin_group_content = HwPinGroupContent()

        # Verify initial state
        hw_pin_group = hw_pin_group_content.getHwPinGroup()
        assert hw_pin_group is None

    def test_set_hw_pin_group(self):
        """
        Test setHwPinGroup method sets the pin group correctly.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        hw_pin_group_content = HwPinGroupContent()

        # Create mock HwPinGroup instance
        hw_pin_group = HwPinGroup(ar_root, "TestPinGroup")

        # Set the pin group
        result = hw_pin_group_content.setHwPinGroup(hw_pin_group)
        assert result is hw_pin_group_content  # Verify method chaining
        assert hw_pin_group_content.getHwPinGroup() == hw_pin_group

    def test_set_hw_pin_group_none(self):
        """
        Test setHwPinGroup method handles None value correctly.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        hw_pin_group_content = HwPinGroupContent()

        # Set initial value
        initial_group = HwPinGroup(ar_root, "TestPinGroup")
        hw_pin_group_content.setHwPinGroup(initial_group)
        assert hw_pin_group_content.getHwPinGroup() == initial_group

        # Set to None - should not change the value (per implementation logic)
        result = hw_pin_group_content.setHwPinGroup(None)
        assert result is hw_pin_group_content  # Verify method chaining
        # Value should remain unchanged due to "if value is not None" check
        assert hw_pin_group_content.getHwPinGroup() == initial_group


class TestHwPinGroup:
    """
    Test class for HwPinGroup functionality.
    """

    def test_initialization(self):
        """
        Test HwPinGroup initialization with parent and short name.
        """
        # Create parent AUTOSAR structure
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        # Create HwPinGroup instance
        hw_pin_group = HwPinGroup(ar_root, "TestHwPinGroup")

        # Verify basic properties
        assert hw_pin_group is not None
        assert hw_pin_group.getShortName() == "TestHwPinGroup"

        # Verify default values for attributes (inherited and specific)
        assert hw_pin_group.getHwAttributeValues() == []
        assert hw_pin_group.getHwCategoryRefs() == []
        assert hw_pin_group.getHwTypeRef() is None
        assert hw_pin_group.getHwPinGroupContent() is None

    def test_get_hw_pin_group_content(self):
        """
        Test getHwPinGroupContent method returns None by default.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        hw_pin_group = HwPinGroup(ar_root, "TestHwPinGroup")

        # Verify initial state
        content = hw_pin_group.getHwPinGroupContent()
        assert content is None

    def test_set_hw_pin_group_content(self):
        """
        Test setHwPinGroupContent method sets the pin group content correctly.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        hw_pin_group = HwPinGroup(ar_root, "TestHwPinGroup")

        # Create mock HwPinGroupContent instance
        content = HwPinGroupContent()

        # Set the content
        result = hw_pin_group.setHwPinGroupContent(content)
        assert result is hw_pin_group  # Verify method chaining
        assert hw_pin_group.getHwPinGroupContent() == content

    def test_set_hw_pin_group_content_none(self):
        """
        Test setHwPinGroupContent method handles None value correctly.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        hw_pin_group = HwPinGroup(ar_root, "TestHwPinGroup")

        # Set initial value
        initial_content = HwPinGroupContent()
        hw_pin_group.setHwPinGroupContent(initial_content)
        assert hw_pin_group.getHwPinGroupContent() == initial_content

        # Set to None - should not change the value (per implementation logic)
        result = hw_pin_group.setHwPinGroupContent(None)
        assert result is hw_pin_group  # Verify method chaining
        # Value should remain unchanged due to "if value is not None" check
        assert hw_pin_group.getHwPinGroupContent() == initial_content


class TestHwElement:
    """
    Test class for HwElement functionality.
    """

    def test_initialization(self):
        """
        Test HwElement initialization with parent and short name.
        """
        # Create parent AUTOSAR structure
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        # Create HwElement instance
        hw_element = HwElement(ar_root, "TestHwElement")

        # Verify basic properties
        assert hw_element is not None
        assert hw_element.getShortName() == "TestHwElement"

        # Verify default values for attributes (inherited and specific)
        assert hw_element.getHwAttributeValues() == []
        assert hw_element.getHwCategoryRefs() == []
        assert hw_element.getHwTypeRef() is None
        assert hw_element.getHwElementConnections() == []
        assert hw_element.getHwPinGroups() == []
        assert hw_element.getNestedElementRefs() == []

    def test_get_hw_element_connections(self):
        """
        Test getHwElementConnections method returns empty list by default.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        hw_element = HwElement(ar_root, "TestHwElement")

        # Verify initial state
        connections = hw_element.getHwElementConnections()
        assert connections == []
        assert isinstance(connections, list)

    def test_set_hw_element_connections(self):
        """
        Test setHwElementConnections method sets connections correctly.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        hw_element = HwElement(ar_root, "TestHwElement")

        # Create mock HwElementConnector instances (using a simple class for testing)
        class MockHwElementConnector:
            pass
        conn1 = MockHwElementConnector()
        conn2 = MockHwElementConnector()
        connections = [conn1, conn2]

        # Set the connections
        result = hw_element.setHwElementConnections(connections)
        assert result is hw_element  # Verify method chaining
        assert hw_element.getHwElementConnections() == connections

    def test_set_hw_element_connections_none(self):
        """
        Test setHwElementConnections method handles None value correctly.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        hw_element = HwElement(ar_root, "TestHwElement")

        # Set initial values
        class MockHwElementConnector:
            pass
        initial_conn = MockHwElementConnector()
        initial_connections = [initial_conn]
        hw_element.setHwElementConnections(initial_connections)
        assert hw_element.getHwElementConnections() == initial_connections

        # Set to None - should not change the value (per implementation logic)
        result = hw_element.setHwElementConnections(None)
        assert result is hw_element  # Verify method chaining
        # Value should remain unchanged due to "if value is not None" check
        assert hw_element.getHwElementConnections() == initial_connections

    def test_get_hw_pin_groups(self):
        """
        Test getHwPinGroups method returns empty list by default.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        hw_element = HwElement(ar_root, "TestHwElement")

        # Verify initial state
        pin_groups = hw_element.getHwPinGroups()
        assert pin_groups == []
        assert isinstance(pin_groups, list)

    def test_create_hw_pin_group(self):
        """
        Test createHwPinGroup method creates and adds a new HwPinGroup instance.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        hw_element = HwElement(ar_root, "TestHwElement")

        # Create a new HwPinGroup
        new_pin_group = hw_element.createHwPinGroup("NewPinGroup")

        # Verify the created pin group
        assert new_pin_group is not None
        assert new_pin_group.getShortName() == "NewPinGroup"
        # The instance should be in the list
        assert new_pin_group in hw_element.getHwPinGroups()

    def test_get_nested_element_refs(self):
        """
        Test getNestedElementRefs method returns empty list by default.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        hw_element = HwElement(ar_root, "TestHwElement")

        # Verify initial state
        nested_refs = hw_element.getNestedElementRefs()
        assert nested_refs == []
        assert isinstance(nested_refs, list)

    def test_set_nested_element_refs(self):
        """
        Test setNestedElementRefs method sets nested element references correctly.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        hw_element = HwElement(ar_root, "TestHwElement")

        # Create mock RefType instances
        ref1 = RefType().setValue("NestedElement1")
        ref2 = RefType().setValue("NestedElement2")
        refs = [ref1, ref2]

        # Set the nested element references
        result = hw_element.setNestedElementRefs(refs)
        assert result is hw_element  # Verify method chaining
        assert hw_element.getNestedElementRefs() == refs

    def test_set_nested_element_refs_none(self):
        """
        Test setNestedElementRefs method handles None value correctly.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        hw_element = HwElement(ar_root, "TestHwElement")

        # Set initial values
        ref1 = RefType().setValue("NestedElement1")
        initial_refs = [ref1]
        hw_element.setNestedElementRefs(initial_refs)
        assert hw_element.getNestedElementRefs() == initial_refs

        # Set to None - should not change the value (per implementation logic)
        result = hw_element.setNestedElementRefs(None)
        assert result is hw_element  # Verify method chaining
        # Value should remain unchanged due to "if value is not None" check
        assert hw_element.getNestedElementRefs() == initial_refs

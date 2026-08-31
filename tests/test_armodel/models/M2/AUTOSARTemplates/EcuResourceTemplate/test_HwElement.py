"""
Test cases for the HwElement module.
These tests ensure coverage for the HwElement class.
"""

from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate import HwElement, HwElementConnector, HwPinGroup
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType


def test_initialization():
    hw_element = HwElement(None, "TestHwElement")
    assert hw_element.getHwElementConnections() == []
    assert hw_element.getHwPinGroups() == []
    assert hw_element.getNestedElementRefs() == []


def test_get_set_hw_element_connections():
    hw_element = HwElement(None, "TestHwElement")
    connector = HwElementConnector()
    assert hw_element.addHwElementConnection(connector) == hw_element
    assert hw_element.getHwElementConnections() == [connector]


def test_get_set_hw_element_connections_none_noop():
    hw_element = HwElement(None, "TestHwElement")
    hw_element.addHwElementConnection(None)
    assert hw_element.getHwElementConnections() == []


def test_create_hw_pin_group():
    hw_element = HwElement(None, "TestHwElement")
    pin_group = hw_element.createHwPinGroup("PG1")
    assert isinstance(pin_group, HwPinGroup)
    assert hw_element.getHwPinGroups() == [pin_group]


def test_create_hw_pin_group_duplicate_returns_existing():
    hw_element = HwElement(None, "TestHwElement")
    pin_group = hw_element.createHwPinGroup("PG1")
    same = hw_element.createHwPinGroup("PG1")
    assert same is pin_group
    assert len(hw_element.getHwPinGroups()) == 1


def test_get_set_nested_element_refs():
    hw_element = HwElement(None, "TestHwElement")
    ref = RefType()
    ref.setValue("/Elements/ElemA")
    assert hw_element.addNestedElementRef(ref) == hw_element
    assert hw_element.getNestedElementRefs() == [ref]


def test_get_set_nested_element_refs_none_noop():
    hw_element = HwElement(None, "TestHwElement")
    hw_element.addNestedElementRef(None)
    assert hw_element.getNestedElementRefs() == []

"""
Test cases for the HwElementConnector module.
These tests ensure coverage for the HwElementConnector class.
"""

from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate import HwElementConnector
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate import HwPinConnector
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate import HwPinGroupConnector
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType


def test_initialization():
    connector = HwElementConnector()
    assert connector.getHwElementRefs() == []
    assert connector.getHwPinConnections() == []
    assert connector.getHwPinGroupConnections() == []


def test_get_set_hw_element_refs():
    connector = HwElementConnector()
    ref1 = RefType()
    ref1.setValue("/Elements/ElemA")
    ref2 = RefType()
    ref2.setValue("/Elements/ElemB")
    assert connector.addHwElementRef(ref1) == connector
    connector.addHwElementRef(ref2)
    assert connector.getHwElementRefs() == [ref1, ref2]


def test_get_set_hw_element_refs_none_noop():
    connector = HwElementConnector()
    connector.addHwElementRef(None)
    assert connector.getHwElementRefs() == []


def test_get_set_hw_pin_connection():
    connector = HwElementConnector()
    pin = HwPinConnector()
    assert connector.addHwPinConnection(pin) == connector
    assert connector.getHwPinConnections() == [pin]


def test_get_set_hw_pin_connection_none_noop():
    connector = HwElementConnector()
    connector.addHwPinConnection(None)
    assert connector.getHwPinConnections() == []


def test_get_set_hw_pin_group_connection():
    connector = HwElementConnector()
    group = HwPinGroupConnector()
    assert connector.addHwPinGroupConnection(group) == connector
    assert connector.getHwPinGroupConnections() == [group]


def test_get_set_hw_pin_group_connection_none_noop():
    connector = HwElementConnector()
    connector.addHwPinGroupConnection(None)
    assert connector.getHwPinGroupConnections() == []

"""
Test cases for the HwElementConnector module.
These tests ensure coverage for the HwElementConnector class.
"""

from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate import HwElementConnector, HwPinConnector, HwPinGroupConnector
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType


def test_initialization():
    connector = HwElementConnector()
    assert connector.hwElementRefs == []
    assert connector.hwPinConnections == []
    assert connector.hwPinGroupConnections == []
    assert connector.getHwElementRefs() == []
    assert connector.getHwPinConnections() == []
    assert connector.getHwPinGroupConnections() == []


def test_no_variation_point_capability():
    """Table 2.8 has no variationPoint row (Rule 0015) — the VariationPointCapable mixin is removed."""
    assert not hasattr(HwElementConnector, "getVariationPoint")
    assert not hasattr(HwElementConnector, "setVariationPoint")


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


def test_member_docstrings_verbatim():
    """Member docstrings must carry the Table 2.8 Notes verbatim (Rule 0001.4/0012)."""
    assert HwElementConnector.__doc__ is not None, "Class docstring must contain spec Note"
    assert (
        "This meta-class represents the ability to connect two hardware elements. The details of the connection can be refined by hwPinGroupConnection." in HwElementConnector.__doc__
    ), "Class docstring must contain spec Note verbatim"
    assert "[constr_11002]" in HwElementConnector.__doc__, "Class docstring must carry constr_11002"

    notes = {
        "addHwElementRef": "This association connects two hardware elements.",
        "getHwElementRefs": "This association connects two hardware elements.",
        "addHwPinConnection": "This represents one particular connection between two hardware pins. This connection shall be used if pin-to-pin-connection is to be described but no description of the connection between the hierarchical composition of HwPinGroups (using HwPinGroupConnector) is required.",
        "getHwPinConnections": "This represents one particular connection between two hardware pins. This connection shall be used if pin-to-pin-connection is to be described but no description of the connection between the hierarchical composition of HwPinGroups (using HwPinGroupConnector) is required.",
        "addHwPinGroupConnection": "This represents one particular connection between two hardware pin groups.",
        "getHwPinGroupConnections": "This represents one particular connection between two hardware pin groups.",
    }
    for method_name, note in notes.items():
        method = getattr(HwElementConnector, method_name)
        assert method.__doc__ is not None, "%s must have a docstring" % method_name
        assert note in method.__doc__, "%s docstring must contain the spec Note verbatim" % method_name


def test_member_annotations():
    """get/add shall resolve to List[...] / Optional[...] with the HwElementConnector self-return (Rule 0003/0006 get_type_hints pin)."""
    import typing

    hints = typing.get_type_hints(HwElementConnector.addHwElementRef)
    assert hints["value"] == typing.Optional[RefType]
    assert hints["return"] is HwElementConnector
    assert typing.get_type_hints(HwElementConnector.getHwElementRefs)["return"] == typing.List[RefType]
    hints = typing.get_type_hints(HwElementConnector.addHwPinConnection)
    assert hints["value"] == typing.Optional[HwPinConnector]
    assert hints["return"] is HwElementConnector
    assert typing.get_type_hints(HwElementConnector.getHwPinConnections)["return"] == typing.List[HwPinConnector]
    hints = typing.get_type_hints(HwElementConnector.addHwPinGroupConnection)
    assert hints["value"] == typing.Optional[HwPinGroupConnector]
    assert hints["return"] is HwElementConnector
    assert typing.get_type_hints(HwElementConnector.getHwPinGroupConnections)["return"] == typing.List[HwPinGroupConnector]

from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate import HwPinConnector, HwPinGroupConnector
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType


class TestHwPinGroupConnector:
    """Test HwPinGroupConnector class (Table 2.9)"""

    def test_initialization(self):
        """Test HwPinGroupConnector initialization defaults"""
        connector = HwPinGroupConnector()
        assert connector.hwPinConnections == []
        assert connector.hwPinGroupRefs == []
        assert connector.getHwPinConnections() == []
        assert connector.getHwPinGroupRefs() == []

    def test_no_variation_point_capability(self):
        """Table 2.9 has no variationPoint row (Rule 0015) — the VariationPointCapable mixin is removed."""
        assert not hasattr(HwPinGroupConnector, "getVariationPoint")
        assert not hasattr(HwPinGroupConnector, "setVariationPoint")

    def test_add_hw_pin_connection(self):
        """Test addHwPinConnection method"""
        connector = HwPinGroupConnector()
        pin_conn = HwPinConnector()

        result = connector.addHwPinConnection(pin_conn)
        assert result is connector
        assert connector.getHwPinConnections() == [pin_conn]

    def test_add_hw_pin_connection_none(self):
        """Test addHwPinConnection with None value"""
        connector = HwPinGroupConnector()
        result = connector.addHwPinConnection(None)
        assert result is connector
        assert connector.getHwPinConnections() == []

    def test_add_hw_pin_group_ref(self):
        """Test addHwPinGroupRef method"""
        connector = HwPinGroupConnector()
        ref = RefType()
        ref.setValue("/Elements/ElemA/Group1")

        result = connector.addHwPinGroupRef(ref)
        assert result is connector
        assert connector.getHwPinGroupRefs() == [ref]

    def test_add_hw_pin_group_ref_none(self):
        """Test addHwPinGroupRef with None value"""
        connector = HwPinGroupConnector()
        result = connector.addHwPinGroupRef(None)
        assert result is connector
        assert connector.getHwPinGroupRefs() == []

    def test_method_chaining(self):
        """Test method chaining for all adders"""
        connector = HwPinGroupConnector()
        pin_conn1 = HwPinConnector()
        pin_conn2 = HwPinConnector()
        ref1 = RefType()
        ref2 = RefType()

        result = connector.addHwPinConnection(pin_conn1).addHwPinConnection(pin_conn2).addHwPinGroupRef(ref1).addHwPinGroupRef(ref2)

        assert result is connector
        assert connector.getHwPinConnections() == [pin_conn1, pin_conn2]
        assert connector.getHwPinGroupRefs() == [ref1, ref2]

    def test_member_docstrings_verbatim(self):
        """Member docstrings must carry the Table 2.9 Notes verbatim (Rule 0001.4/0012)."""
        assert HwPinGroupConnector.__doc__ is not None, "Class docstring must contain spec Note"
        assert "This meta-class represents the ability to connect two pin groups." in HwPinGroupConnector.__doc__, "Class docstring must contain spec Note verbatim"
        assert "[constr_11003]" in HwPinGroupConnector.__doc__, "Class docstring must carry constr_11003"

        notes = {
            "addHwPinConnection": "This represents one particular connection between two hardware pins. The connected pins shall match the connection provided by the parent hwPinGroup Connection.",
            "getHwPinConnections": "This represents one particular connection between two hardware pins. The connected pins shall match the connection provided by the parent hwPinGroup Connection.",
            "addHwPinGroupRef": "This association connects two hardware pin groups.",
            "getHwPinGroupRefs": "This association connects two hardware pin groups.",
        }
        for method_name, note in notes.items():
            method = getattr(HwPinGroupConnector, method_name)
            assert method.__doc__ is not None, "%s must have a docstring" % method_name
            assert note in method.__doc__, "%s docstring must contain the spec Note verbatim" % method_name

    def test_member_annotations(self):
        """get/add shall resolve to List[...] / Optional[...] with the HwPinGroupConnector self-return (Rule 0003/0006 get_type_hints pin)."""
        import typing

        hints = typing.get_type_hints(HwPinGroupConnector.addHwPinConnection)
        assert hints["value"] == typing.Optional[HwPinConnector]
        assert hints["return"] is HwPinGroupConnector
        assert typing.get_type_hints(HwPinGroupConnector.getHwPinConnections)["return"] == typing.List[HwPinConnector]
        hints = typing.get_type_hints(HwPinGroupConnector.addHwPinGroupRef)
        assert hints["value"] == typing.Optional[RefType]
        assert hints["return"] is HwPinGroupConnector
        assert typing.get_type_hints(HwPinGroupConnector.getHwPinGroupRefs)["return"] == typing.List[RefType]

from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate import HwPinConnector
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType


class TestHwPinConnector:
    """Test HwPinConnector class (Table 2.10)"""

    def test_initialization(self):
        """Test HwPinConnector initialization defaults"""
        connector = HwPinConnector()
        assert connector.hwPinRefs == []
        assert connector.getHwPinRefs() == []

    def test_no_variation_point_capability(self):
        """Table 2.10 has no variationPoint row (Rule 0015) — the VariationPointCapable mixin is removed."""
        assert not hasattr(HwPinConnector, "getVariationPoint")
        assert not hasattr(HwPinConnector, "setVariationPoint")

    def test_add_hw_pin_ref(self):
        """Test addHwPinRef method"""
        connector = HwPinConnector()
        ref = RefType()
        ref.setValue("/Elements/ElemA/Pin1")
        result = connector.addHwPinRef(ref)
        assert result is connector
        assert connector.getHwPinRefs() == [ref]

    def test_add_hw_pin_ref_none(self):
        """Test addHwPinRef with None value"""
        connector = HwPinConnector()
        result = connector.addHwPinRef(None)
        assert result is connector
        assert connector.getHwPinRefs() == []

    def test_add_multiple_hw_pin_refs(self):
        """Test addHwPinRef with multiple refs (constr_11004 expects exactly 2)"""
        connector = HwPinConnector()
        ref1 = RefType()
        ref1.setValue("/Elements/ElemA/Pin1")
        ref2 = RefType()
        ref2.setValue("/Elements/ElemA/Pin2")

        result = connector.addHwPinRef(ref1).addHwPinRef(ref2)

        assert result is connector
        refs = connector.getHwPinRefs()
        assert len(refs) == 2
        assert refs[0] is ref1
        assert refs[1] is ref2

    def test_member_docstrings_verbatim(self):
        """Member docstrings must carry the Table 2.10 Notes verbatim (Rule 0001.4/0012)."""
        assert HwPinConnector.__doc__ is not None, "Class docstring must contain spec Note"
        assert "This meta-class represents the ability to connect two pins." in HwPinConnector.__doc__, "Class docstring must contain spec Note verbatim"
        assert "[constr_11004]" in HwPinConnector.__doc__, "Class docstring must carry constr_11004"

        notes = {
            "addHwPinRef": "This association connects two hardware pins.",
            "getHwPinRefs": "This association connects two hardware pins.",
        }
        for method_name, note in notes.items():
            method = getattr(HwPinConnector, method_name)
            assert method.__doc__ is not None, "%s must have a docstring" % method_name
            assert note in method.__doc__, "%s docstring must contain the spec Note verbatim" % method_name

    def test_member_annotations(self):
        """get/add shall resolve to List[RefType] / Optional[RefType] with the HwPinConnector self-return (Rule 0003/0006 get_type_hints pin)."""
        import typing

        hints = typing.get_type_hints(HwPinConnector.addHwPinRef)
        assert hints["value"] == typing.Optional[RefType]
        assert hints["return"] is HwPinConnector
        assert typing.get_type_hints(HwPinConnector.getHwPinRefs)["return"] == typing.List[RefType]

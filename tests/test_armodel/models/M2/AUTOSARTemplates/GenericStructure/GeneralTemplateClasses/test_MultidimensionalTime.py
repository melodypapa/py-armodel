"""
This module contains tests for the MultidimensionalTime class in
GenericStructure.GeneralTemplateClasses.
"""

import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime import MultidimensionalTime
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import CseCodeType, Integer


class TestMultidimensionalTime:
    def test_class_docstring_verbatim(self):
        """Test that the class docstring is the Table 4.74 Note verbatim."""
        assert MultidimensionalTime.__doc__.strip() == "Specifies a time value based on [17] see [TPS_GST_00354]."

    def test_init_has_no_docstring(self):
        """Test that __init__ has no docstring (spec Notes live in inline member comments)."""
        assert MultidimensionalTime.__init__.__doc__ is None

    def test_cse_code_typed_cse_code_type(self):
        """Test that cseCode is typed CseCodeType per Table 4.74 (getter/setter annotations)."""
        getter_hints = typing.get_type_hints(MultidimensionalTime.getCseCode)
        assert getter_hints.get("return") == typing.Optional[CseCodeType]

        setter_hints = typing.get_type_hints(MultidimensionalTime.setCseCode)
        assert setter_hints.get("value") == typing.Optional[CseCodeType]
        assert setter_hints.get("return") is MultidimensionalTime

    def test_cse_code_factor_typed_integer(self):
        """Test that cseCodeFactor is typed Integer per Table 4.74 (getter/setter annotations)."""
        getter_hints = typing.get_type_hints(MultidimensionalTime.getCseCodeFactor)
        assert getter_hints.get("return") == typing.Optional[Integer]

        setter_hints = typing.get_type_hints(MultidimensionalTime.setCseCodeFactor)
        assert setter_hints.get("value") == typing.Optional[Integer]
        assert setter_hints.get("return") is MultidimensionalTime

    def test_initialization(self):
        """Test MultidimensionalTime initialization."""
        mdt = MultidimensionalTime()
        assert mdt is not None
        assert mdt.getCseCode() is None
        assert mdt.getCseCodeFactor() is None

    def test_cse_code_setter_getter(self):
        """Test cseCode setter and getter."""
        mdt = MultidimensionalTime()
        code = CseCodeType().setValue("100")
        result = mdt.setCseCode(code)
        assert result is mdt
        assert mdt.getCseCode() == code

    def test_cse_code_factor_setter_getter(self):
        """Test cseCodeFactor setter and getter."""
        mdt = MultidimensionalTime()
        factor = Integer().setValue(1000)
        result = mdt.setCseCodeFactor(factor)
        assert result is mdt
        assert mdt.getCseCodeFactor() == factor

    def test_all_properties(self):
        """Test setting all properties."""
        mdt = MultidimensionalTime()
        code = CseCodeType().setValue("0")
        factor = Integer().setValue(500)
        mdt.setCseCode(code).setCseCodeFactor(factor)
        assert mdt.getCseCode() == code
        assert mdt.getCseCodeFactor() == factor

    def test_set_cse_code_none_noop(self):
        """Test setCseCode(None) is a no-op."""
        mdt = MultidimensionalTime()
        code = CseCodeType().setValue("100")
        mdt.setCseCode(code)
        result = mdt.setCseCode(None)
        assert result is mdt
        assert mdt.getCseCode() == code

    def test_set_cse_code_factor_none_noop(self):
        """Test setCseCodeFactor(None) is a no-op."""
        mdt = MultidimensionalTime()
        factor = Integer().setValue(1000)
        mdt.setCseCodeFactor(factor)
        result = mdt.setCseCodeFactor(None)
        assert result is mdt
        assert mdt.getCseCodeFactor() == factor

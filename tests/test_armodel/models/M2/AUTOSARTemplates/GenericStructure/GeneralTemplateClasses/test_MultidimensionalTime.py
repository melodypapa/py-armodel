"""
This module contains tests for the MultidimensionalTime class in
GenericStructure.GeneralTemplateClasses.
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime import MultidimensionalTime
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import CseCodeType, Integer


class TestMultidimensionalTime:
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

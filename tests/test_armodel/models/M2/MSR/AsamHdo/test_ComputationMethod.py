"""
This module contains tests for the ComputationMethod module in MSR.AsamHdo.
"""
import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARPackage,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    CIdentifier,
    Identifier,
    Limit,
    PositiveUnlimitedInteger,
    RefType,
    String,
)
from armodel.models.M2.MSR.AsamHdo.ComputationMethod import *
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import (
    MultiLanguageOverviewParagraph,
)


class TestCompuContent:
    """Test class for CompuContent abstract class."""

    def test_compu_content_abstract_class(self):
        """Test that CompuContent cannot be instantiated directly."""
        # This should raise NotImplementedError
        with pytest.raises(TypeError):
            CompuContent()


class TestCompuConst:
    """Test class for CompuConst class."""

    def test_compu_const_initialization(self):
        """Test that a CompuConst object can be initialized with default values."""
        compu_const = CompuConst()
        assert compu_const.compuConstContentType is None

    def test_compu_const_content_type_methods(self):
        """Test the compuConstContentType getter and setter."""
        compu_const = CompuConst()
        # Use a concrete implementation like CompuConstTextContent instead of abstract CompuConstContent
        content_type = CompuConstTextContent()

        result = compu_const.setCompuConstContentType(content_type)
        assert compu_const.getCompuConstContentType() == content_type
        assert result == compu_const


class TestCompu:
    """Test class for Compu class."""

    def test_compu_initialization(self):
        """Test that a Compu object can be initialized with default values."""
        compu = Compu()
        assert compu.compuContent is None
        assert compu.compuDefaultValue is None

    def test_compu_content_methods(self):
        """Test the compuContent getter and setter."""
        compu = Compu()
        # Use a concrete implementation like CompuScales instead of abstract CompuContent
        content = CompuScales()

        result = compu.setCompuContent(content)
        assert compu.getCompuContent() == content
        assert result == compu

    def test_compu_default_value_methods(self):
        """Test the compuDefaultValue getter and setter."""
        compu = Compu()
        default_value = CompuConst()

        result = compu.setCompuDefaultValue(default_value)
        assert compu.getCompuDefaultValue() == default_value
        assert result == compu


class TestCompuConstContent:
    """Test class for CompuConstContent abstract class."""

    def test_compu_const_content_abstract_class(self):
        """Test that CompuConstContent cannot be instantiated directly."""
        # This should raise NotImplementedError
        with pytest.raises(TypeError):
            CompuConstContent()


class TestCompuConstTextContent:
    """Test class for CompuConstTextContent class."""

    def test_compu_const_text_content_initialization(self):
        """Test that a CompuConstTextContent object can be initialized with default values."""
        compu_const_text = CompuConstTextContent()
        assert compu_const_text.vt is None

    def test_compu_const_text_content_vt_methods(self):
        """Test the vt getter and setter."""
        compu_const_text = CompuConstTextContent()
        text_value = "test_text"

        result = compu_const_text.setVt(text_value)
        assert compu_const_text.getVt() == text_value
        assert result == compu_const_text


class TestCompuConstNumericContent:
    """Test class for CompuConstNumericContent class."""

    def test_compu_const_numeric_content_initialization(self):
        """Test that a CompuConstNumericContent object can be initialized with default values."""
        compu_const_numeric = CompuConstNumericContent()
        assert compu_const_numeric.v is None

    def test_compu_const_numeric_content_v_methods(self):
        """Test the v getter and setter."""
        compu_const_numeric = CompuConstNumericContent()
        numeric_value = 123.45

        result = compu_const_numeric.setV(numeric_value)
        assert compu_const_numeric.getV() == numeric_value
        assert result == compu_const_numeric


class TestCompuConstFormulaContent:
    """Test class for CompuConstFormulaContent class."""

    def test_compu_const_formula_content_initialization(self):
        """Test that a CompuConstFormulaContent object can be initialized with default values."""
        compu_const_formula = CompuConstFormulaContent()
        assert compu_const_formula.vf is None

    def test_compu_const_formula_content_vf_methods(self):
        """Test the vf getter and setter."""
        compu_const_formula = CompuConstFormulaContent()
        formula_value = "a + b"

        result = compu_const_formula.setVf(formula_value)
        assert compu_const_formula.getVf() == formula_value
        assert result == compu_const_formula


class TestCompuScaleContents:
    """Test class for CompuScaleContents abstract class."""

    def test_compu_scale_contents_abstract_class(self):
        """Test that CompuScaleContents cannot be instantiated directly."""
        # This should raise NotImplementedError
        with pytest.raises(TypeError):
            CompuScaleContents()


class TestCompuScaleConstantContents:
    """Test class for CompuScaleConstantContents class."""

    def test_compu_scale_constant_contents_initialization(self):
        """Test that a CompuScaleConstantContents object can be initialized with default values."""
        compu_scale_constant = CompuScaleConstantContents()
        assert compu_scale_constant.compuConst is None

    def test_compu_scale_constant_contents_compu_const_methods(self):
        """Test the compuConst getter and setter."""
        compu_scale_constant = CompuScaleConstantContents()
        compu_const = CompuConst()

        result = compu_scale_constant.setCompuConst(compu_const)
        assert compu_scale_constant.getCompuConst() == compu_const
        assert result == compu_scale_constant


class TestCompuRationalCoeffs:
    """Test class for CompuRationalCoeffs class."""

    def test_compu_rational_coeffs_initialization(self):
        """Test that a CompuRationalCoeffs object can be initialized with default values."""
        compu_rational_coeffs = CompuRationalCoeffs()
        assert compu_rational_coeffs.compuDenominator is None
        assert compu_rational_coeffs.compuNumerator is None

    def test_compu_rational_coeffs_denominator_methods(self):
        """Test the compuDenominator getter and setter."""
        compu_rational_coeffs = CompuRationalCoeffs()
        denominator = CompuNominatorDenominator()

        result = compu_rational_coeffs.setCompuDenominator(denominator)
        assert compu_rational_coeffs.getCompuDenominator() == denominator
        assert result == compu_rational_coeffs

    def test_compu_rational_coeffs_numerator_methods(self):
        """Test the compuNumerator getter and setter."""
        compu_rational_coeffs = CompuRationalCoeffs()
        numerator = CompuNominatorDenominator()

        result = compu_rational_coeffs.setCompuNumerator(numerator)
        assert compu_rational_coeffs.getCompuNumerator() == numerator
        assert result == compu_rational_coeffs


class TestCompuScaleRationalFormula:
    """Test class for CompuScaleRationalFormula class."""

    def test_compu_scale_rational_formula_initialization(self):
        """Test that a CompuScaleRationalFormula object can be initialized with default values."""
        compu_scale_rational = CompuScaleRationalFormula()
        assert compu_scale_rational.compuRationalCoeffs is None

    def test_compu_scale_rational_formula_coeffs_methods(self):
        """Test the compuRationalCoeffs getter and setter."""
        compu_scale_rational = CompuScaleRationalFormula()
        coeffs = CompuRationalCoeffs()

        result = compu_scale_rational.setCompuRationalCoeffs(coeffs)
        assert compu_scale_rational.getCompuRationalCoeffs() == coeffs
        assert result == compu_scale_rational


class TestCompuNominatorDenominator:
    """Test class for CompuNominatorDenominator class."""

    def test_compu_nominator_denominator_initialization(self):
        """Test that a CompuNominatorDenominator object can be initialized with default values."""
        compu_nominator_denominator = CompuNominatorDenominator()
        assert compu_nominator_denominator.v == []

    def test_compu_nominator_denominator_v_methods(self):
        """Test the add_v and get_vs methods."""
        compu_nominator_denominator = CompuNominatorDenominator()
        value = 1.5

        compu_nominator_denominator.add_v(value)
        vs = compu_nominator_denominator.get_vs()
        assert value in vs
        assert len(vs) == 1


class TestCompuScale:
    """Test class for CompuScale class."""

    def test_compu_scale_initialization(self):
        """Test that a CompuScale object can be initialized with default values."""
        compu_scale = CompuScale()
        assert compu_scale.a2lDisplayText is None
        assert compu_scale.compuInverseValue is None
        assert compu_scale.compuScaleContents is None
        assert compu_scale.desc is None
        assert compu_scale.lowerLimit is None
        assert compu_scale.mask is None
        assert compu_scale.shortLabel is None
        assert compu_scale.symbol is None
        assert compu_scale.upperLimit is None

    def test_compu_scale_a2l_display_text_methods(self):
        """Test the a2lDisplayText getter and setter."""
        compu_scale = CompuScale()
        display_text = String()

        result = compu_scale.setA2lDisplayText(display_text)
        assert compu_scale.getA2lDisplayText() == display_text
        assert result == compu_scale

    def test_compu_scale_inverse_value_methods(self):
        """Test the compuInverseValue getter and setter."""
        compu_scale = CompuScale()
        inverse_value = CompuConst()

        result = compu_scale.setCompuInverseValue(inverse_value)
        assert compu_scale.getCompuInverseValue() == inverse_value
        assert result == compu_scale

    def test_compu_scale_contents_methods(self):
        """Test the compuScaleContents getter and setter."""
        compu_scale = CompuScale()
        contents = CompuScaleConstantContents()

        result = compu_scale.setCompuScaleContents(contents)
        assert compu_scale.getCompuScaleContents() == contents
        assert result == compu_scale

    def test_compu_scale_desc_methods(self):
        """Test the desc getter and setter."""
        compu_scale = CompuScale()
        desc = MultiLanguageOverviewParagraph()

        result = compu_scale.setDesc(desc)
        assert compu_scale.getDesc() == desc
        assert result == compu_scale

    def test_compu_scale_lower_limit_methods(self):
        """Test the lowerLimit getter and setter."""
        compu_scale = CompuScale()
        lower_limit = Limit()

        result = compu_scale.setLowerLimit(lower_limit)
        assert compu_scale.getLowerLimit() == lower_limit
        assert result == compu_scale

    def test_compu_scale_mask_methods(self):
        """Test the mask getter and setter."""
        compu_scale = CompuScale()
        mask = PositiveUnlimitedInteger()

        result = compu_scale.setMask(mask)
        assert compu_scale.getMask() == mask
        assert result == compu_scale

    def test_compu_scale_short_label_methods(self):
        """Test the shortLabel getter and setter."""
        compu_scale = CompuScale()
        short_label = Identifier()

        result = compu_scale.setShortLabel(short_label)
        assert compu_scale.getShortLabel() == short_label
        assert result == compu_scale

    def test_compu_scale_symbol_methods(self):
        """Test the symbol getter and setter."""
        compu_scale = CompuScale()
        symbol = CIdentifier()

        result = compu_scale.setSymbol(symbol)
        assert compu_scale.getSymbol() == symbol
        assert result == compu_scale

    def test_compu_scale_upper_limit_methods(self):
        """Test the upperLimit getter and setter."""
        compu_scale = CompuScale()
        upper_limit = Limit()

        result = compu_scale.setUpperLimit(upper_limit)
        assert compu_scale.getUpperLimit() == upper_limit
        assert result == compu_scale


class TestCompuScales:
    """Test class for CompuScales class."""

    def test_compu_scales_initialization(self):
        """Test that a CompuScales object can be initialized with default values."""
        compu_scales = CompuScales()
        assert compu_scales.compuScales == []

    def test_compu_scales_add_compu_scale(self):
        """Test adding computation scales."""
        compu_scales = CompuScales()
        compu_scale = CompuScale()

        compu_scales.addCompuScale(compu_scale)
        scales = compu_scales.getCompuScales()
        assert compu_scale in scales
        assert len(scales) == 1


class TestCompuMethod:
    """Test class for CompuMethod class."""

    def test_compu_method_initialization(self):
        """Test that a CompuMethod object can be initialized with default values."""
        parent_obj = ARPackage(None, "parent_test")  # Using ARPackage as a concrete ARObject subclass
        compu_method = CompuMethod(parent_obj, "test_name")
        assert compu_method.compuInternalToPhys is None
        assert compu_method.compuPhysToInternal is None
        assert compu_method.displayFormat is None
        assert compu_method.unitRef is None

    def test_compu_method_internal_to_phys_methods(self):
        """Test the compuInternalToPhys getter and setter."""
        parent_obj = ARPackage(None, "parent_test")  # Using ARPackage as a concrete ARObject subclass
        compu_method = CompuMethod(parent_obj, "test_name")
        compu = Compu()

        result = compu_method.setCompuInternalToPhys(compu)
        assert compu_method.getCompuInternalToPhys() == compu
        assert result == compu_method

    def test_compu_method_phys_to_internal_methods(self):
        """Test the compuPhysToInternal getter and setter."""
        parent_obj = ARPackage(None, "parent_test")  # Using ARPackage as a concrete ARObject subclass
        compu_method = CompuMethod(parent_obj, "test_name")
        compu = Compu()

        result = compu_method.setCompuPhysToInternal(compu)
        assert compu_method.getCompuPhysToInternal() == compu
        assert result == compu_method

    def test_compu_method_display_format_methods(self):
        """Test the displayFormat getter and setter."""
        parent_obj = ARPackage(None, "parent_test")  # Using ARPackage as a concrete ARObject subclass
        compu_method = CompuMethod(parent_obj, "test_name")
        display_format = "test_format"

        result = compu_method.setDisplayFormat(display_format)
        assert compu_method.getDisplayFormat() == display_format
        assert result == compu_method

    def test_compu_method_unit_ref_methods(self):
        """Test the unitRef getter and setter."""
        parent_obj = ARPackage(None, "parent_test")  # Using ARPackage as a concrete ARObject subclass
        compu_method = CompuMethod(parent_obj, "test_name")
        unit_ref = RefType()

        result = compu_method.setUnitRef(unit_ref)
        assert compu_method.getUnitRef() == unit_ref
        assert result == compu_method

    def test_compu_method_category_texttable(self):
        """Test that the TEXTTABLE category constant is available."""
        assert hasattr(CompuMethod, 'CATEGORY_TEXTTABLE')
        assert CompuMethod.CATEGORY_TEXTTABLE == "TEXTTABLE"

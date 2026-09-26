"""
This module contains tests for the ComputationMethod module in MSR.AsamHdo.
"""

from abc import ABC
from inspect import cleandoc, getsource

import pytest

from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure import AtpBlueprintable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARPackage
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    CIdentifier,
    DisplayFormatString,
    Identifier,
    Limit,
    Numerical,
    PositiveUnlimitedInteger,
    PrimitiveIdentifier,
    RefType,
    String,
)
from armodel.models.M2.MSR.AsamHdo.ComputationMethod import (
    Compu,
    CompuConst,
    CompuConstContent,
    CompuConstFormulaContent,
    CompuConstNumericContent,
    CompuConstTextContent,
    CompuContent,
    CompuGenericMath,
    CompuMethod,
    CompuNominatorDenominator,
    CompuRationalCoeffs,
    CompuScale,
    CompuScaleConstantContents,
    CompuScaleContents,
    CompuScaleRationalFormula,
    CompuScales,
)
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultiLanguageOverviewParagraph


class TestCompuContent:
    """Test class for CompuContent (AUTOSAR_CP_TPS_SoftwareComponentTemplate, Table 5.63)."""

    def test_compu_content_has_spec_note(self):
        assert cleandoc(CompuContent.__doc__) == "This abstract meta-class represents the various definition means of a computation method."

    def test_compu_content_abstract_class(self):
        with pytest.raises(TypeError, match="CompuContent is an abstract class"):
            CompuContent()

    def test_compu_content_concrete_subclass_has_arobject_defaults(self):
        class ConcreteCompuContent(CompuContent):
            pass

        content = ConcreteCompuContent()
        assert content.getChecksum() is None
        assert content.getTimestamp() is None


class TestCompuConst:
    """Test class for CompuConst (AUTOSAR_CP_TPS_SoftwareComponentTemplate, Table 5.71)."""

    def test_compu_const_has_spec_note(self):
        assert cleandoc(CompuConst.__doc__) == "This meta-class represents the fact that the value of a computation method scale is constant."

    def test_compu_const_initialization(self):
        """Test that a CompuConst object can be initialized with default values."""
        compu_const = CompuConst()
        assert compu_const.compuConstContentType is None

    def test_compu_const_content_type_methods(self):
        """Test the compuConstContentType getter and setter."""
        compu_const = CompuConst()
        content_type = CompuConstTextContent()

        result = compu_const.setCompuConstContentType(content_type)
        assert compu_const.getCompuConstContentType() == content_type
        assert result == compu_const

    def test_compu_const_content_type_none_is_no_op(self):
        compu_const = CompuConst()
        content_type = CompuConstTextContent()
        compu_const.setCompuConstContentType(content_type)

        result = compu_const.setCompuConstContentType(None)

        assert result == compu_const
        assert compu_const.getCompuConstContentType() == content_type

    def test_compu_const_content_type_has_verbatim_spec_member_note(self):
        source = getsource(CompuConst.__init__)
        assert (
            "# This is the actual content of the constant compu method scale. Tags: xml.roleElement=false xml.roleWrapperElement=false xml.sequenceOffset=10 xml.typeElement=false xml.typeWrapperElement=false"
            in source
        )


class TestCompu:
    """Test class for Compu class."""

    def test_compu_has_spec_note(self):
        assert cleandoc(Compu.__doc__) == "This meta-class represents the ability to express one particular computation."

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

    def test_compu_setters_none_are_no_ops(self):
        compu = Compu()
        content = CompuScales()
        default_value = CompuConst()
        compu.setCompuContent(content)
        compu.setCompuDefaultValue(default_value)

        assert compu.setCompuContent(None) is compu
        assert compu.setCompuDefaultValue(None) is compu
        assert compu.getCompuContent() is content
        assert compu.getCompuDefaultValue() is default_value


class TestCompuConstContent:
    """Test class for CompuConstContent abstract class."""

    def test_compu_const_content_has_spec_note(self):
        assert cleandoc(CompuConstContent.__doc__) == ("This meta-class represents the fact that the constant value of the computation method can be numerical or textual.")

    def test_compu_const_content_abstract_class(self):
        """Test that CompuConstContent cannot be instantiated directly."""
        # This should raise NotImplementedError
        with pytest.raises(TypeError):
            CompuConstContent()

    def test_compu_const_content_concrete_subclass_has_arobject_defaults(self):
        class ConcreteCompuConstContent(CompuConstContent):
            pass

        content = ConcreteCompuConstContent()
        assert content.getChecksum() is None
        assert content.getTimestamp() is None


class TestCompuConstTextContent:
    """Test class for CompuConstTextContent class."""

    def test_compu_const_text_content_has_spec_note(self):
        assert cleandoc(CompuConstTextContent.__doc__) == "This meta-class represents the textual content of a scale."

    def test_compu_const_text_content_initialization(self):
        """Test that a CompuConstTextContent object can be initialized with default values."""
        compu_const_text = CompuConstTextContent()
        assert compu_const_text.vt is None

    def test_compu_const_text_content_vt_methods(self):
        """Test the vt getter and setter."""
        from armodel.models import VerbatimString

        compu_const_text = CompuConstTextContent()
        text_value = VerbatimString().setValue("test_text")

        result = compu_const_text.setVt(text_value)
        assert compu_const_text.getVt() == text_value
        assert result == compu_const_text

        assert compu_const_text.setVt(None) == compu_const_text
        assert compu_const_text.getVt() == text_value


class TestCompuConstNumericContent:
    """Test class for CompuConstNumericContent class."""

    def test_compu_const_numeric_content_has_spec_note(self):
        assert cleandoc(CompuConstNumericContent.__doc__) == (
            "This meta-class represents the fact that the constant value of the computation method is a numerical value. It is separated from CompuConstFormulaContent to support compatibility with ASAM HDO."
        )

    def test_compu_const_numeric_content_initialization(self):
        """Test that a CompuConstNumericContent object can be initialized with default values."""
        compu_const_numeric = CompuConstNumericContent()
        assert compu_const_numeric.v is None

    def test_compu_const_numeric_content_v_methods(self):
        """Test the v getter and setter."""
        from armodel.models import ARNumerical

        compu_const_numeric = CompuConstNumericContent()
        numeric_value = ARNumerical().setValue("123")

        result = compu_const_numeric.setV(numeric_value)
        assert compu_const_numeric.getV() == numeric_value
        assert result == compu_const_numeric

        assert compu_const_numeric.setV(None) == compu_const_numeric
        assert compu_const_numeric.getV() == numeric_value


class TestCompuConstFormulaContent:
    """Test class for CompuConstFormulaContent class."""

    def test_compu_const_formula_content_has_spec_note(self):
        assert cleandoc(CompuConstFormulaContent.__doc__) == (
            "This meta-class represents the fact that the constant value of the computation method is represented by a variation point. This difference is due to compatibility with ASAM HDO."
        )

    def test_compu_const_formula_content_initialization(self):
        """Test that a CompuConstFormulaContent object can be initialized with default values."""
        compu_const_formula = CompuConstFormulaContent()
        assert compu_const_formula.vf is None

    def test_compu_const_formula_content_vf_methods(self):
        """Test the vf getter and setter."""
        from armodel.models import ARNumerical

        compu_const_formula = CompuConstFormulaContent()
        formula_value = ARNumerical().setValue("42")

        result = compu_const_formula.setVf(formula_value)
        assert compu_const_formula.getVf() == formula_value
        assert result == compu_const_formula

        assert compu_const_formula.setVf(None) == compu_const_formula
        assert compu_const_formula.getVf() == formula_value


class TestCompuScaleContents:
    """Test class for CompuScaleContents abstract class."""

    def test_compu_scale_contents_abstract_class(self):
        """Test that CompuScaleContents cannot be instantiated directly."""
        with pytest.raises(TypeError):
            CompuScaleContents()

    def test_compu_scale_contents_spec_shape(self):
        """Test the abstract base and its inherited ARObject state."""
        assert CompuScaleContents.__bases__ == (ARObject, ABC)
        contents = CompuScaleConstantContents()
        assert isinstance(contents, CompuScaleContents)
        assert contents.parent is None
        assert contents.timestamp is None
        assert "This abstract meta-class represents the content of one particular scale." in CompuScaleContents.__doc__


class TestCompuScaleConstantContents:
    """Test class for CompuScaleConstantContents class."""

    def test_compu_scale_constant_contents_initialization(self):
        """Test that a CompuScaleConstantContents object can be initialized with default values."""
        compu_scale_constant = CompuScaleConstantContents()
        assert compu_scale_constant.compuConst is None
        assert "This meta-class represents the fact that a particular scale of the computation method is constant." in CompuScaleConstantContents.__doc__

    def test_compu_scale_constant_contents_compu_const_methods(self):
        """Test the compuConst getter and setter."""
        compu_scale_constant = CompuScaleConstantContents()
        compu_const = CompuConst()

        result = compu_scale_constant.setCompuConst(compu_const)
        assert compu_scale_constant.getCompuConst() == compu_const
        assert result == compu_scale_constant
        assert compu_scale_constant.setCompuConst(None) == compu_scale_constant
        assert compu_scale_constant.getCompuConst() == compu_const


class TestCompuRationalCoeffs:
    """Test class for CompuRationalCoeffs class."""

    def test_compu_rational_coeffs_initialization(self):
        """Test that a CompuRationalCoeffs object can be initialized with default values."""
        compu_rational_coeffs = CompuRationalCoeffs()
        assert compu_rational_coeffs.compuDenominator is None
        assert compu_rational_coeffs.compuNumerator is None
        assert "This meta-class represents the ability to express a rational function by specifying the coefficients of nominator and denominator." in CompuRationalCoeffs.__doc__

    def test_compu_rational_coeffs_denominator_methods(self):
        """Test the compuDenominator getter and setter."""
        compu_rational_coeffs = CompuRationalCoeffs()
        denominator = CompuNominatorDenominator()

        result = compu_rational_coeffs.setCompuDenominator(denominator)
        assert compu_rational_coeffs.getCompuDenominator() == denominator
        assert result == compu_rational_coeffs
        assert compu_rational_coeffs.setCompuDenominator(None) == compu_rational_coeffs
        assert compu_rational_coeffs.getCompuDenominator() == denominator

    def test_compu_rational_coeffs_numerator_methods(self):
        """Test the compuNumerator getter and setter."""
        compu_rational_coeffs = CompuRationalCoeffs()
        numerator = CompuNominatorDenominator()

        result = compu_rational_coeffs.setCompuNumerator(numerator)
        assert compu_rational_coeffs.getCompuNumerator() == numerator
        assert result == compu_rational_coeffs
        assert compu_rational_coeffs.setCompuNumerator(None) == compu_rational_coeffs
        assert compu_rational_coeffs.getCompuNumerator() == numerator


class TestCompuScaleRationalFormula:
    """Test class for CompuScaleRationalFormula class."""

    def test_compu_scale_rational_formula_initialization(self):
        """Test that a CompuScaleRationalFormula object can be initialized with default values."""
        compu_scale_rational = CompuScaleRationalFormula()
        assert compu_scale_rational.compuRationalCoeffs is None
        assert "This meta-class represents the fact that the computation in this scale is represented as rational term." in CompuScaleRationalFormula.__doc__

    def test_compu_scale_rational_formula_coeffs_methods(self):
        """Test the compuRationalCoeffs getter and setter."""
        compu_scale_rational = CompuScaleRationalFormula()
        coeffs = CompuRationalCoeffs()

        result = compu_scale_rational.setCompuRationalCoeffs(coeffs)
        assert compu_scale_rational.getCompuRationalCoeffs() == coeffs
        assert result == compu_scale_rational
        assert compu_scale_rational.setCompuRationalCoeffs(None) == compu_scale_rational
        assert compu_scale_rational.getCompuRationalCoeffs() == coeffs


class TestCompuNominatorDenominator:
    """Test class for CompuNominatorDenominator class."""

    def test_compu_nominator_denominator_initialization(self):
        """Test that a CompuNominatorDenominator object can be initialized with default values."""
        compu_nominator_denominator = CompuNominatorDenominator()
        assert compu_nominator_denominator.v == []
        assert "This class represents the ability to express a polynomial either as Nominator or as Denominator." in CompuNominatorDenominator.__doc__

    def test_compu_nominator_denominator_v_methods(self):
        """Test the v aggregation mutators and accessor."""
        compu_nominator_denominator = CompuNominatorDenominator()
        value = Numerical().setValue("1.5")

        result = compu_nominator_denominator.addV(value)
        assert compu_nominator_denominator.getVs() == [value]
        assert result == compu_nominator_denominator
        assert compu_nominator_denominator.addV(None) == compu_nominator_denominator
        assert compu_nominator_denominator.getVs() == [value]


class TestCompuScale:
    """Test class for CompuScale class."""

    def test_compu_scale_has_spec_note(self):
        assert cleandoc(CompuScale.__doc__) == "This meta-class represents the ability to specify one segment of a segmented computation method."

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

    def test_compu_scale_setters_preserve_values_on_none(self):
        compu_scale = CompuScale()
        values = {
            "a2lDisplayText": String(),
            "compuInverseValue": CompuConst(),
            "compuScaleContents": CompuScaleConstantContents(),
            "desc": MultiLanguageOverviewParagraph(),
            "lowerLimit": Limit(),
            "mask": PositiveUnlimitedInteger(),
            "shortLabel": Identifier(),
            "symbol": CIdentifier(),
            "upperLimit": Limit(),
        }
        for name, value in values.items():
            getattr(compu_scale, "set" + name[0].upper() + name[1:])(value)
        for name, value in values.items():
            setter = getattr(compu_scale, "set" + name[0].upper() + name[1:])
            getter = getattr(compu_scale, "get" + name[0].upper() + name[1:])
            assert setter(None) is compu_scale
            assert getter() is value


class TestCompuScales:
    """Test class for CompuScales class."""

    def test_compu_scales_initialization(self):
        """Test that a CompuScales object can be initialized with default values."""
        compu_scales = CompuScales()
        assert compu_scales.compuScales == []
        assert cleandoc(CompuScales.__doc__) == "This meta-class represents the ability to stepwise express a computation method."
        assert issubclass(CompuScales, CompuContent)

    def test_compu_scales_add_compu_scale(self):
        """Test adding computation scales."""
        compu_scales = CompuScales()
        compu_scale = CompuScale()

        result = compu_scales.addCompuScale(compu_scale)
        scales = compu_scales.getCompuScales()
        assert scales == [compu_scale]
        assert result == compu_scales
        assert compu_scales.addCompuScale(None) == compu_scales
        assert compu_scales.getCompuScales() == [compu_scale]

    def test_compu_scales_preserve_order(self):
        compu_scales = CompuScales()
        first = CompuScale()
        second = CompuScale()

        compu_scales.addCompuScale(first)
        compu_scales.addCompuScale(second)

        assert compu_scales.getCompuScales() == [first, second]


class TestCompuMethod:
    """Test class for CompuMethod class."""

    def test_compu_method_has_spec_note_and_base(self):
        assert cleandoc(CompuMethod.__doc__) == (
            "This meta-class represents the ability to express the relationship between a physical value and the mathematical representation. "
            "Note that this is still independent of the technical implementation in data types. It only specifies the formula how the internal value corresponds to its physical pendant. "
            "Tags: atp.recommendedPackage=CompuMethods"
        )
        assert issubclass(CompuMethod, AtpBlueprintable)

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

    def test_compu_method_setters_preserve_values_on_none(self):
        parent_obj = ARPackage(None, "parent_test")
        compu_method = CompuMethod(parent_obj, "test_name")
        internal = Compu()
        physical = Compu()
        display_format = DisplayFormatString().setValue("%1.2")
        unit_ref = RefType().setValue("/Units/Unit")

        compu_method.setCompuInternalToPhys(internal)
        compu_method.setCompuPhysToInternal(physical)
        compu_method.setDisplayFormat(display_format)
        compu_method.setUnitRef(unit_ref)

        assert compu_method.setCompuInternalToPhys(None) is compu_method
        assert compu_method.setCompuPhysToInternal(None) is compu_method
        assert compu_method.setDisplayFormat(None) is compu_method
        assert compu_method.setUnitRef(None) is compu_method
        assert compu_method.getCompuInternalToPhys() is internal
        assert compu_method.getCompuPhysToInternal() is physical
        assert compu_method.getDisplayFormat() is display_format
        assert compu_method.getUnitRef() is unit_ref

    def test_compu_method_category_texttable(self):
        """Test that the TEXTTABLE category constant is available."""
        assert hasattr(CompuMethod, "CATEGORY_TEXTTABLE")
        assert CompuMethod.CATEGORY_TEXTTABLE == "TEXTTABLE"


class TestCompuGenericMath:
    """Test class for CompuGenericMath class."""

    def test_compu_generic_math_initialization(self):
        compu_generic_math = CompuGenericMath()
        assert compu_generic_math.getLevel() is None

    def test_compu_generic_math_methods(self):
        compu_generic_math = CompuGenericMath()
        level = PrimitiveIdentifier().setValue("INFORMAL")

        assert compu_generic_math.setLevel(level) == compu_generic_math
        assert compu_generic_math.getLevel() == level

    def test_compu_generic_math_none_noop(self):
        compu_generic_math = CompuGenericMath()
        level = PrimitiveIdentifier().setValue("INFORMAL")
        compu_generic_math.setLevel(level)
        compu_generic_math.setLevel(None)
        assert compu_generic_math.getLevel() == level

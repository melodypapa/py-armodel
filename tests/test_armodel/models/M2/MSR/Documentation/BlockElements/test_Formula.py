"""This module contains tests for the MlFormula module in MSR.Documentation.BlockElements."""

from armodel.models.M2.MSR.Documentation.BlockElements import Caption
from armodel.models.M2.MSR.Documentation.BlockElements.Figure import LGraphic
from armodel.models.M2.MSR.Documentation.BlockElements.Formula import MlFormula
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import (
    MultiLanguagePlainText,
    MultiLanguageVerbatim,
)


class TestMlFormula:
    """Test class for MlFormula class."""

    def test_ml_formula_initialization(self):
        """Test that an MlFormula object can be initialized with default values."""
        formula = MlFormula()
        assert formula.formulaCaption is None
        assert formula.lGraphics == []
        assert formula.verbatim is None
        assert formula.texMath is None
        assert formula.genericMath is None

    def test_ml_formula_tex_math_methods(self):
        """Test the texMath getter and setter."""
        formula = MlFormula()
        tex_math = MultiLanguagePlainText()

        result = formula.setTexMath(tex_math)
        assert formula.getTexMath() == tex_math
        assert result == formula

        formula.setTexMath(None)
        assert formula.getTexMath() == tex_math

    def test_ml_formula_verbatim_methods(self):
        """Test the verbatim getter and setter."""
        formula = MlFormula()
        verbatim = MultiLanguageVerbatim()

        result = formula.setVerbatim(verbatim)
        assert formula.getVerbatim() == verbatim
        assert result == formula

        formula.setVerbatim(None)
        assert formula.getVerbatim() == verbatim

    def test_ml_formula_generic_math_methods(self):
        """Test the genericMath getter and setter."""
        formula = MlFormula()
        generic_math = MultiLanguagePlainText()

        result = formula.setGenericMath(generic_math)
        assert formula.getGenericMath() == generic_math
        assert result == formula

        formula.setGenericMath(None)
        assert formula.getGenericMath() == generic_math

    def test_ml_formula_formula_caption_methods(self):
        """Test the formulaCaption getter and setter."""
        formula = MlFormula()
        caption = Caption(None, "cap")

        result = formula.setFormulaCaption(caption)
        assert formula.getFormulaCaption() == caption
        assert result == formula

        formula.setFormulaCaption(None)
        assert formula.getFormulaCaption() == caption

    def test_ml_formula_l_graphics_methods(self):
        """Test adding and getting LGraphic objects."""
        formula = MlFormula()
        l_graphic = LGraphic()

        result = formula.addLGraphic(l_graphic)
        l_graphics = formula.getLGraphics()
        assert l_graphic in l_graphics
        assert result == formula

        formula.addLGraphic(None)
        assert formula.getLGraphics() == [l_graphic]

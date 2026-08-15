from typing import List, Optional

from armodel.models.M2.MSR.Documentation.BlockElements import Caption
from armodel.models.M2.MSR.Documentation.BlockElements.Figure import LGraphic
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements.PaginationAndView import Paginateable
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultiLanguagePlainText, MultiLanguageVerbatim


class MlFormula(Paginateable):
    """
    This meta-class represents the ability to express a formula in a documentation. The formula can be expressed by various means. If more than one representation is available, they need to be consistent. The rendering system can use the representation which is most appropriate.
    """

    # MlFormula method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.26, p.310
    # Spec verified: R23-11
    # Deviation: LGraphic.map reader/writer not wired (Map/Area classes out of scope) - transitive round-trip gap
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getFormulaCaption  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setFormulaCaption  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getGenericMath     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setGenericMath     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] addLGraphic        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getLGraphics       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getTexMath         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTexMath         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getVerbatim        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setVerbatim        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # This element specifies the identification or heading of a formula. Tags: xml.sequenceOffset=20
        self.formulaCaption: Optional[Caption] = None

        # this rpresents the semantic and mathematical descriptions which are processed by a math-processor. Tags: xml.sequenceOffset=80
        self.genericMath: Optional[MultiLanguagePlainText] = None

        # This represents a formula as an embedded figure. Tags: xml.roleWrapperElement=false xml.sequenceOffset=30
        self.lGraphics: List[LGraphic] = []

        # this is the TeX representation of TeX formula. A TeX formula can be processed by a TeX or a LaTeX processor. Tags: xml.sequenceOffset=60
        self.texMath: Optional[MultiLanguagePlainText] = None

        # this represents a formula using only text and white-space. It can be used to denote the formula in a kind of pseudo code or whatever appears approprate. Tags: xml.sequenceOffset=50
        self.verbatim: Optional[MultiLanguageVerbatim] = None

    def getFormulaCaption(self) -> Optional[Caption]:
        """
        This element specifies the identification or heading of a formula. Tags: xml.sequenceOffset=20

        Returns:
            The identification or heading of the formula
        """
        return self.formulaCaption

    def setFormulaCaption(self, value: Optional[Caption]) -> "MlFormula":
        """
        This element specifies the identification or heading of a formula. Tags: xml.sequenceOffset=20. A None value is a no-op and does not overwrite an existing formulaCaption.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.formulaCaption = value
        return self

    def getGenericMath(self) -> Optional[MultiLanguagePlainText]:
        """
        this rpresents the semantic and mathematical descriptions which are processed by a math-processor. Tags: xml.sequenceOffset=80

        Returns:
            The generic math representation of the formula
        """
        return self.genericMath

    def setGenericMath(self, value: Optional[MultiLanguagePlainText]) -> "MlFormula":
        """
        this rpresents the semantic and mathematical descriptions which are processed by a math-processor. Tags: xml.sequenceOffset=80. A None value is a no-op and does not overwrite an existing genericMath.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.genericMath = value
        return self

    def addLGraphic(self, value: Optional[LGraphic]) -> "MlFormula":
        """
        This represents a formula as an embedded figure. Tags: xml.roleWrapperElement=false xml.sequenceOffset=30. A None value is a no-op and is not appended.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.lGraphics.append(value)
        return self

    def getLGraphics(self) -> List[LGraphic]:
        """
        This represents a formula as an embedded figure. Tags: xml.roleWrapperElement=false xml.sequenceOffset=30

        Returns:
            The formulas as embedded figures
        """
        return self.lGraphics

    def getTexMath(self) -> Optional[MultiLanguagePlainText]:
        """
        this is the TeX representation of TeX formula. A TeX formula can be processed by a TeX or a LaTeX processor. Tags: xml.sequenceOffset=60

        Returns:
            The TeX representation of the formula
        """
        return self.texMath

    def setTexMath(self, value: Optional[MultiLanguagePlainText]) -> "MlFormula":
        """
        this is the TeX representation of TeX formula. A TeX formula can be processed by a TeX or a LaTeX processor. Tags: xml.sequenceOffset=60. A None value is a no-op and does not overwrite an existing texMath.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.texMath = value
        return self

    def getVerbatim(self) -> Optional[MultiLanguageVerbatim]:
        """
        this represents a formula using only text and white-space. It can be used to denote the formula in a kind of pseudo code or whatever appears approprate. Tags: xml.sequenceOffset=50

        Returns:
            The verbatim representation of the formula
        """
        return self.verbatim

    def setVerbatim(self, value: Optional[MultiLanguageVerbatim]) -> "MlFormula":
        """
        this represents a formula using only text and white-space. It can be used to denote the formula in a kind of pseudo code or whatever appears approprate. Tags: xml.sequenceOffset=50. A None value is a no-op and does not overwrite an existing verbatim.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.verbatim = value
        return self

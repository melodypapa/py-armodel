from __future__ import annotations

from typing import List, Optional
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.FormulaLanguage import FormulaExpression
from abc import ABC

from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultiLanguageOverviewParagraph
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure import AtpBlueprintable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARNumerical,
    PrimitiveIdentifier,
    CIdentifier,
    DisplayFormatString,
    Identifier,
    Numerical,
    PositiveUnlimitedInteger,
    String,
    VerbatimString,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Limit


class CompuContent(ARObject, ABC):
    """This abstract meta-class represents the various definition means of a computation method."""

    # CompuContent method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.63, p.387
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__ [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self):
        if type(self) is CompuContent:
            raise TypeError("CompuContent is an abstract class.")

        super().__init__()


class CompuConstContent(ARObject, ABC):
    """This meta-class represents the fact that the constant value of the computation method can be numerical or textual."""

    # CompuConstContent method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.72, p.390
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__ [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self):
        if type(self) is CompuConstContent:
            raise TypeError("CompuConstContent is an abstract class.")

        super().__init__()


class CompuConstTextContent(CompuConstContent):
    """This meta-class represents the textual content of a scale."""

    # CompuConstTextContent method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.67, p.388
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__ [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getVt [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] setVt [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # This represents a textual constant in the computation method.
        self.vt: Optional[VerbatimString] = None

    def getVt(self) -> Optional[VerbatimString]:
        """This represents a textual constant in the computation method."""
        return self.vt

    def setVt(self, value: Optional[VerbatimString]):
        """This represents a textual constant in the computation method. Does nothing if value is None."""
        if value is not None:
            self.vt = value
        return self


class CompuConstNumericContent(CompuConstContent):
    """This meta-class represents the fact that the constant value of the computation method is a numerical value. It is separated from CompuConstFormulaContent to support compatibility with ASAM HDO."""

    # CompuConstNumericContent method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.68, p.389
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__ [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getV [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] setV [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # This represents the numerical value.
        self.v: Optional[ARNumerical] = None

    def getV(self) -> Optional[ARNumerical]:
        """This represents the numerical value."""
        return self.v

    def setV(self, value: Optional[ARNumerical]):
        """This represents the numerical value. Does nothing if value is None."""
        if value is not None:
            self.v = value
        return self


class CompuConstFormulaContent(CompuConstContent):
    """This meta-class represents the fact that the constant value of the computation method is represented by a variation point. This difference is due to compatibility with ASAM HDO."""

    # CompuConstFormulaContent method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table B.1, p.900 (appendix)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__ [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getVf [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] setVf [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # Value calculated via a system constant. This element is included in every case where parameters should be generated from numerical values during compile time (not runtime!). Thus for example, the influence of the cylinder number on conversion formulae can be introduced in a repeatable manner. Stereotypes: atpVariation Tags: vh.latestBindingTime=codeGenerationTime xml.sequenceOffset=30
        self.vf: Optional[ARNumerical] = None

    def getVf(self) -> Optional[ARNumerical]:
        """Value calculated via a system constant. This element is included in every case where parameters should be generated from numerical values during compile time (not runtime!). Thus for example, the influence of the cylinder number on conversion formulae can be introduced in a repeatable manner. Stereotypes: atpVariation Tags: vh.latestBindingTime=codeGenerationTime xml.sequenceOffset=30"""
        return self.vf

    def setVf(self, value: Optional[ARNumerical]):
        """Value calculated via a system constant. This element is included in every case where parameters should be generated from numerical values during compile time (not runtime!). Thus for example, the influence of the cylinder number on conversion formulae can be introduced in a repeatable manner. Stereotypes: atpVariation Tags: vh.latestBindingTime=codeGenerationTime xml.sequenceOffset=30. Does nothing if value is None."""
        if value is not None:
            self.vf = value
        return self


class CompuConst(ARObject):
    """This meta-class represents the fact that the value of a computation method scale is constant."""

    # CompuConst method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.71, p.390
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getCompuConstContentType     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCompuConstContentType     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # This is the actual content of the constant compu method scale. Tags: xml.roleElement=false xml.roleWrapperElement=false xml.sequenceOffset=10 xml.typeElement=false xml.typeWrapperElement=false
        self.compuConstContentType: Optional[CompuConstContent] = None

    def getCompuConstContentType(self) -> Optional[CompuConstContent]:
        """This is the actual content of the constant compu method scale."""
        return self.compuConstContentType

    def setCompuConstContentType(self, value: Optional[CompuConstContent]):
        """This is the actual content of the constant compu method scale. None leaves the current value unchanged."""
        if value is not None:
            self.compuConstContentType = value
        return self


class Compu(ARObject):
    """This meta-class represents the ability to express one particular computation."""

    # Compu method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.62, p.386
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getCompuContent              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCompuContent              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getCompuDefaultValue         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCompuDefaultValue         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # This specifies the details of the computation. Stereotypes: atpSplitable Tags: atp.Splitkey=compuContent xml.roleElement=false xml.roleWrapperElement=false xml.sequenceOffset=20 xml.typeElement=false xml.typeWrapperElement=false
        self.compuContent: Optional[CompuContent] = None

        # This property can be used to specify an output value for a conversion formula, if the value to be converted lies outside the plausibility limit. Although this is possible for all conversion formulae, it is especially valid for variables with tabular conversion formulae. Tags: xml.sequenceOffset=70
        self.compuDefaultValue: Optional[CompuConst] = None

    def getCompuContent(self) -> Optional[CompuContent]:
        """This specifies the details of the computation. Stereotypes: atpSplitable Tags: atp.Splitkey=compuContent xml.roleElement=false xml.roleWrapperElement=false xml.sequenceOffset=20 xml.typeElement=false xml.typeWrapperElement=false"""
        return self.compuContent

    def setCompuContent(self, value: Optional[CompuContent]):
        """This specifies the details of the computation. Stereotypes: atpSplitable Tags: atp.Splitkey=compuContent xml.roleElement=false xml.roleWrapperElement=false xml.sequenceOffset=20 xml.typeElement=false xml.typeWrapperElement=false. None leaves the current value unchanged."""
        if value is not None:
            self.compuContent = value
        return self

    def getCompuDefaultValue(self) -> Optional[CompuConst]:
        """This property can be used to specify an output value for a conversion formula, if the value to be converted lies outside the plausibility limit. Although this is possible for all conversion formulae, it is especially valid for variables with tabular conversion formulae. Tags: xml.sequenceOffset=70"""
        return self.compuDefaultValue

    def setCompuDefaultValue(self, value: Optional[CompuConst]):
        """This property can be used to specify an output value for a conversion formula, if the value to be converted lies outside the plausibility limit. Although this is possible for all conversion formulae, it is especially valid for variables with tabular conversion formulae. Tags: xml.sequenceOffset=70. None leaves the current value unchanged."""
        if value is not None:
            self.compuDefaultValue = value
        return self


class CompuScaleContents(ARObject, ABC):
    """This abstract meta-class represents the content of one particular scale."""

    # CompuScaleContents method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.66, p.388
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__ [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self):
        if type(self) is CompuScaleContents:
            raise TypeError("CompuScaleContents is an abstract class.")

        super().__init__()


class CompuScaleConstantContents(CompuScaleContents):
    """This meta-class represents the fact that a particular scale of the computation method is constant."""

    # CompuScaleConstantContents method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.74, p.391
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__ [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getCompuConst [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCompuConst [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # This represents the fact that the scale is a constant. The use case is mainly a non interpolated scale. It is a simplification of the fact that a constant scale can also be expressed as rational function of order 0. Tags: xml.sequenceOffset=90
        self.compuConst: Optional[CompuConst] = None

    def getCompuConst(self) -> CompuConst:
        """This represents the fact that the scale is a constant. The use case is mainly a non interpolated scale. It is a simplification of the fact that a constant scale can also be expressed as rational function of order 0. Tags: xml.sequenceOffset=90"""
        return self.compuConst

    def setCompuConst(self, value: CompuConst):
        """This represents the fact that the scale is a constant. The use case is mainly a non interpolated scale. It is a simplification of the fact that a constant scale can also be expressed as rational function of order 0. Tags: xml.sequenceOffset=90. Does nothing if value is None."""
        if value is not None:
            self.compuConst = value
        return self


class CompuRationalCoeffs(ARObject):
    """This meta-class represents the ability to express a rational function by specifying the coefficients of nominator and denominator."""

    # CompuRationalCoeffs method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.69, p.389
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__ [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getCompuDenominator [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCompuDenominator [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getCompuNumerator [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCompuNumerator [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # This is the denominator of the expression. Tags: xml.sequenceOffset=30
        self.compuDenominator: Optional[CompuNominatorDenominator] = None
        # This is the numerator of the rational expression. Tags: xml.sequenceOffset=20
        self.compuNumerator: Optional[CompuNominatorDenominator] = None

    def getCompuDenominator(self) -> CompuNominatorDenominator:
        """This is the denominator of the expression. Tags: xml.sequenceOffset=30"""
        return self.compuDenominator

    def setCompuDenominator(self, value: CompuNominatorDenominator):
        """This is the denominator of the expression. Tags: xml.sequenceOffset=30. Does nothing if value is None."""
        if value is not None:
            self.compuDenominator = value
        return self

    def getCompuNumerator(self) -> CompuNominatorDenominator:
        """This is the numerator of the rational expression. Tags: xml.sequenceOffset=20"""
        return self.compuNumerator

    def setCompuNumerator(self, value: CompuNominatorDenominator):
        """This is the numerator of the rational expression. Tags: xml.sequenceOffset=20. Does nothing if value is None."""
        if value is not None:
            self.compuNumerator = value
        return self


class CompuScaleRationalFormula(CompuScaleContents):
    """This meta-class represents the fact that the computation in this scale is represented as rational term."""

    # CompuScaleRationalFormula method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.73, p.390
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__ [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getCompuRationalCoeffs [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCompuRationalCoeffs [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # This specifies the coefficients of the rational formula. Tags: xml.sequenceOffset=110
        self.compuRationalCoeffs: Optional[CompuRationalCoeffs] = None

    def getCompuRationalCoeffs(self) -> CompuRationalCoeffs:
        """This specifies the coefficients of the rational formula. Tags: xml.sequenceOffset=110"""
        return self.compuRationalCoeffs

    def setCompuRationalCoeffs(self, value: CompuRationalCoeffs):
        """This specifies the coefficients of the rational formula. Tags: xml.sequenceOffset=110. Does nothing if value is None."""
        if value is not None:
            self.compuRationalCoeffs = value
        return self


class CompuNominatorDenominator(ARObject):
    """This class represents the ability to express a polynomial either as Nominator or as Denominator."""

    # CompuNominatorDenominator method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.75, p.391
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__ [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addV [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getVs [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self):
        super().__init__()

        # this is the list of polynomial factors. Note that the first vf represents the power=0. The polynomial is v[0] * xˆ0 + v[1] * xˆ1 ... Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime xml.roleElement=true xml.roleWrapperElement=false xml.sequenceOffset=20 xml.typeElement=false xml.typeWrapperElement=false
        self.v: List[Numerical] = []

    def addV(self, value: Numerical):
        """this is the list of polynomial factors. Note that the first vf represents the power=0. The polynomial is v[0] * xˆ0 + v[1] * xˆ1 ... Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime xml.roleElement=true xml.roleWrapperElement=false xml.sequenceOffset=20 xml.typeElement=false xml.typeWrapperElement=false. Does nothing if value is None."""
        if value is not None:
            self.v.append(value)
        return self

    def getVs(self) -> List[Numerical]:
        """this is the list of polynomial factors. Note that the first vf represents the power=0. The polynomial is v[0] * xˆ0 + v[1] * xˆ1 ... Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime xml.roleElement=true xml.roleWrapperElement=false xml.sequenceOffset=20 xml.typeElement=false xml.typeWrapperElement=false."""
        return self.v


class CompuScale(ARObject, VariationPointCapable):
    """This meta-class represents the ability to specify one segment of a segmented computation method."""

    # CompuScale method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.64, p.388
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getA2lDisplayText            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setA2lDisplayText            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getCompuInverseValue         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCompuInverseValue         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getCompuScaleContents        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCompuScaleContents        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDesc                      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDesc                      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getLowerLimit                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setLowerLimit                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMask                      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMask                      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getShortLabel                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setShortLabel                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSymbol                    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSymbol                    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getUpperLimit                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setUpperLimit                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # The value of this attribute shall be taken for generating one display text (specifically the OutVal) within the equivalent of the enclosing CompuMethod in A2L.
        self.a2lDisplayText: Optional[String] = None

        # This is the inverse value of the constraint. This supports the case that the scale is not reversible per se. Tags: xml.sequenceOffset=60
        self.compuInverseValue: Optional[CompuConst] = None

        # This represents the computation details of the scale. Tags: xml.roleElement=false xml.roleWrapperElement=false xml.sequenceOffset=70 xml.typeElement=false xml.typeWrapperElement=false
        self.compuScaleContents: Optional[CompuScaleContents] = None

        # <desc> represents a general but brief description of the object in question. Tags: xml.sequenceOffset=30
        self.desc: Optional[MultiLanguageOverviewParagraph] = None

        # This specifies the lower limit of the scale. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime xml.sequenceOffset=40
        self.lowerLimit: Optional[Limit] = None

        # In difference to all the other computational methods every COMPU-SCALE will be applied including the bit MASK. Therefore it is allowed for this type of COMPU-METHOD, that COMPU-SCALES overlap. To calculate the string reverse to a value, the string has to be split and the according value for each substring has to be summed up. The sum is finally transmitted. The processing has to be done in order of the COMPU-SCALE elements. Tags: xml.sequenceOffset=35
        self.mask: Optional[PositiveUnlimitedInteger] = None

        # This element specifies a short name for the particular scale. The name can for example be used to derive a programming language identifier. Tags: xml.sequenceOffset=20
        self.shortLabel: Optional[Identifier] = None

        # The symbol, if provided, is used by code generators to get a C identifier for the CompuScale. The name will be used as is for the code generation, therefore it needs to be unique within the generation context. Tags: xml.sequenceOffset=25
        self.symbol: Optional[CIdentifier] = None

        # This specifies the upper limit of a of the scale. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime xml.sequenceOffset=50
        self.upperLimit: Optional[Limit] = None

    def getA2lDisplayText(self) -> String:
        """The value of this attribute shall be taken for generating one display text (specifically the OutVal) within the equivalent of the enclosing CompuMethod in A2L."""
        return self.a2lDisplayText

    def setA2lDisplayText(self, value: String):
        """The value of this attribute shall be taken for generating one display text (specifically the OutVal) within the equivalent of the enclosing CompuMethod in A2L. None leaves the current value unchanged."""
        if value is not None:
            self.a2lDisplayText = value
        return self

    def getCompuInverseValue(self) -> CompuConst:
        """This is the inverse value of the constraint. This supports the case that the scale is not reversible per se. Tags: xml.sequenceOffset=60"""
        return self.compuInverseValue

    def setCompuInverseValue(self, value: CompuConst):
        """This is the inverse value of the constraint. This supports the case that the scale is not reversible per se. Tags: xml.sequenceOffset=60. None leaves the current value unchanged."""
        if value is not None:
            self.compuInverseValue = value
        return self

    def getCompuScaleContents(self) -> CompuScaleContents:
        """This represents the computation details of the scale. Tags: xml.roleElement=false xml.roleWrapperElement=false xml.sequenceOffset=70 xml.typeElement=false xml.typeWrapperElement=false"""
        return self.compuScaleContents

    def setCompuScaleContents(self, value: CompuScaleContents):
        """This represents the computation details of the scale. Tags: xml.roleElement=false xml.roleWrapperElement=false xml.sequenceOffset=70 xml.typeElement=false xml.typeWrapperElement=false. None leaves the current value unchanged."""
        if value is not None:
            self.compuScaleContents = value
        return self

    def getDesc(self) -> MultiLanguageOverviewParagraph:
        """<desc> represents a general but brief description of the object in question. Tags: xml.sequenceOffset=30"""
        return self.desc

    def setDesc(self, value: MultiLanguageOverviewParagraph):
        """<desc> represents a general but brief description of the object in question. Tags: xml.sequenceOffset=30. None leaves the current value unchanged."""
        if value is not None:
            self.desc = value
        return self

    def getLowerLimit(self) -> Limit:
        """This specifies the lower limit of the scale. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime xml.sequenceOffset=40"""
        return self.lowerLimit

    def setLowerLimit(self, value: Limit):
        """This specifies the lower limit of the scale. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime xml.sequenceOffset=40. None leaves the current value unchanged."""
        if value is not None:
            self.lowerLimit = value
        return self

    def getMask(self) -> PositiveUnlimitedInteger:
        """In difference to all the other computational methods every COMPU-SCALE will be applied including the bit MASK. Therefore it is allowed for this type of COMPU-METHOD, that COMPU-SCALES overlap. To calculate the string reverse to a value, the string has to be split and the according value for each substring has to be summed up. The sum is finally transmitted. The processing has to be done in order of the COMPU-SCALE elements. Tags: xml.sequenceOffset=35"""
        return self.mask

    def setMask(self, value: PositiveUnlimitedInteger):
        """In difference to all the other computational methods every COMPU-SCALE will be applied including the bit MASK. Therefore it is allowed for this type of COMPU-METHOD, that COMPU-SCALES overlap. To calculate the string reverse to a value, the string has to be split and the according value for each substring has to be summed up. The sum is finally transmitted. The processing has to be done in order of the COMPU-SCALE elements. Tags: xml.sequenceOffset=35. None leaves the current value unchanged."""
        if value is not None:
            self.mask = value
        return self

    def getShortLabel(self) -> Identifier:
        """This element specifies a short name for the particular scale. The name can for example be used to derive a programming language identifier. Tags: xml.sequenceOffset=20"""
        return self.shortLabel

    def setShortLabel(self, value: Identifier):
        """This element specifies a short name for the particular scale. The name can for example be used to derive a programming language identifier. Tags: xml.sequenceOffset=20. None leaves the current value unchanged."""
        if value is not None:
            self.shortLabel = value
        return self

    def getSymbol(self) -> CIdentifier:
        """The symbol, if provided, is used by code generators to get a C identifier for the CompuScale. The name will be used as is for the code generation, therefore it needs to be unique within the generation context. Tags: xml.sequenceOffset=25"""
        return self.symbol

    def setSymbol(self, value: CIdentifier):
        """The symbol, if provided, is used by code generators to get a C identifier for the CompuScale. The name will be used as is for the code generation, therefore it needs to be unique within the generation context. Tags: xml.sequenceOffset=25. None leaves the current value unchanged."""
        if value is not None:
            self.symbol = value
        return self

    def getUpperLimit(self) -> Limit:
        """This specifies the upper limit of a of the scale. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime xml.sequenceOffset=50"""
        return self.upperLimit

    def setUpperLimit(self, value: Limit):
        """This specifies the upper limit of a of the scale. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime xml.sequenceOffset=50. None leaves the current value unchanged."""
        if value is not None:
            self.upperLimit = value
        return self


class CompuScales(CompuContent):
    """This meta-class represents the ability to stepwise express a computation method."""

    # CompuScales method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.65, p.388
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addCompuScale                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getCompuScales               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self):
        super().__init__()

        # This represents one scale within the compu method. Note that it contains a Variationpoint in order to support blueprints of enumerations. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=compuScale, compuScale.variation Point.shortLabel vh.latestBindingTime=blueprintDerivationTime xml.roleElement=true xml.roleWrapperElement=true xml.sequenceOffset=40 xml.typeElement=false xml.typeWrapperElement=false
        self.compuScales: List[CompuScale] = []

    def addCompuScale(self, compu_scale: CompuScale):
        """This represents one scale within the compu method. Note that it contains a Variationpoint in order to support blueprints of enumerations. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=compuScale, compuScale.variation Point.shortLabel vh.latestBindingTime=blueprintDerivationTime xml.roleElement=true xml.roleWrapperElement=true xml.sequenceOffset=40 xml.typeElement=false xml.typeWrapperElement=false. None leaves the current value unchanged."""
        if compu_scale is not None:
            self.compuScales.append(compu_scale)
        return self

    def getCompuScales(self) -> List[CompuScale]:
        """This represents one scale within the compu method. Note that it contains a Variationpoint in order to support blueprints of enumerations. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=compuScale, compuScale.variation Point.shortLabel vh.latestBindingTime=blueprintDerivationTime xml.roleElement=true xml.roleWrapperElement=true xml.sequenceOffset=40 xml.typeElement=false xml.typeWrapperElement=false"""
        return self.compuScales


class CompuMethod(AtpBlueprintable):
    """This meta-class represents the ability to express the relationship between a physical value and the mathematical representation. Note that this is still independent of the technical implementation in data types. It only specifies the formula how the internal value corresponds to its physical pendant. Tags: atp.recommendedPackage=CompuMethods"""

    # CompuMethod method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.61, p.380
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getCompuInternalToPhys       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCompuInternalToPhys       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getCompuPhysToInternal       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCompuPhysToInternal       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDisplayFormat             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDisplayFormat             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getUnitRef                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setUnitRef                   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    CATEGORY_TEXTTABLE = "TEXTTABLE"

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This specifies the computation from internal values to physical values. Stereotypes: atpSplitable Tags: atp.Splitkey=compuInternalToPhys xml.sequenceOffset=80
        self.compuInternalToPhys: Optional[Compu] = None

        # This represents the computation from physical values to the internal values. Stereotypes: atpSplitable Tags: atp.Splitkey=compuPhysToInternal xml.sequenceOffset=90
        self.compuPhysToInternal: Optional[Compu] = None

        # This property specifies, how the physical value shall be displayed e.g. in documents or measurement and calibration tools. Tags: xml.sequenceOffset=20
        self.displayFormat: Optional[DisplayFormatString] = None

        # This is the physical unit of the Physical values for which the CompuMethod applies. Tags: xml.sequenceOffset=30
        self.unitRef: Optional[RefType] = None

    def getCompuInternalToPhys(self) -> Optional[Compu]:
        """This specifies the computation from internal values to physical values. Stereotypes: atpSplitable Tags: atp.Splitkey=compuInternalToPhys xml.sequenceOffset=80"""
        return self.compuInternalToPhys

    def setCompuInternalToPhys(self, value: Optional[Compu]):
        """This specifies the computation from internal values to physical values. Stereotypes: atpSplitable Tags: atp.Splitkey=compuInternalToPhys xml.sequenceOffset=80. None leaves the current value unchanged."""
        if value is not None:
            self.compuInternalToPhys = value
        return self

    def getCompuPhysToInternal(self) -> Optional[Compu]:
        """This represents the computation from physical values to the internal values. Stereotypes: atpSplitable Tags: atp.Splitkey=compuPhysToInternal xml.sequenceOffset=90"""
        return self.compuPhysToInternal

    def setCompuPhysToInternal(self, value: Optional[Compu]):
        """This represents the computation from physical values to the internal values. Stereotypes: atpSplitable Tags: atp.Splitkey=compuPhysToInternal xml.sequenceOffset=90. None leaves the current value unchanged."""
        if value is not None:
            self.compuPhysToInternal = value
        return self

    def getDisplayFormat(self) -> Optional[DisplayFormatString]:
        """This property specifies, how the physical value shall be displayed e.g. in documents or measurement and calibration tools. Tags: xml.sequenceOffset=20"""
        return self.displayFormat

    def setDisplayFormat(self, value: Optional[DisplayFormatString]):
        """This property specifies, how the physical value shall be displayed e.g. in documents or measurement and calibration tools. Tags: xml.sequenceOffset=20. None leaves the current value unchanged."""
        if value is not None:
            self.displayFormat = value
        return self

    def getUnitRef(self) -> Optional[RefType]:
        """This is the physical unit of the Physical values for which the CompuMethod applies. Tags: xml.sequenceOffset=30"""
        return self.unitRef

    def setUnitRef(self, value: Optional[RefType]):
        """This is the physical unit of the Physical values for which the CompuMethod applies. Tags: xml.sequenceOffset=30. None leaves the current value unchanged."""
        if value is not None:
            self.unitRef = value
        return self


class CompuGenericMath(FormulaExpression):
    """
    This meta-class represents the ability to specify a generic formula expression.
    """

    # CompuGenericMath method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.60, p.374
    # Spec verified: R23-11
    # 2026-09-25 drift fix (Rule 0012.3): re-parented to FormulaExpression per spec Base row (most-derived) — see docs/plan/atp_mixed_string_hierarchy.md
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                 [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getLevel                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setLevel                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # Placeholder to describe an indicator of a language level for the mathematics e.g. INFORMAL, ASAMHDO. May be refined by particular use-cases.
        self.level: Optional[PrimitiveIdentifier] = None

    def getLevel(self) -> Optional[PrimitiveIdentifier]:
        """
        Placeholder to describe an indicator of a language level for the mathematics e.g. INFORMAL, ASAMHDO. May be refined by particular use-cases.
        """
        return self.level

    def setLevel(self, value: Optional[PrimitiveIdentifier]) -> CompuGenericMath:
        """
        Placeholder to describe an indicator of a language level for the mathematics e.g. INFORMAL, ASAMHDO. May be refined by particular use-cases. A None value is a no-op and does not overwrite an existing level.
        """
        if value is not None:
            self.level = value
        return self

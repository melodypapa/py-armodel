from __future__ import annotations

from typing import List, Optional
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.VariationPointCapable import VariationPointCapable
from abc import ABC

from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultiLanguageOverviewParagraph
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure import AtpBlueprintable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARNumerical,
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
    """
    Represents a single scale in a computation method with limits and content.
    Base: ARObject
    """

    # CompuScale method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getA2lDisplayText            [x] impl  [ ] docstring  [ ] test
    # [ ] setA2lDisplayText            [x] impl  [ ] docstring  [ ] test
    # [ ] getCompuInverseValue         [x] impl  [ ] docstring  [ ] test
    # [ ] setCompuInverseValue         [x] impl  [ ] docstring  [ ] test
    # [ ] getCompuScaleContents        [x] impl  [ ] docstring  [ ] test
    # [ ] setCompuScaleContents        [x] impl  [ ] docstring  [ ] test
    # [ ] getDesc                      [x] impl  [ ] docstring  [ ] test
    # [ ] setDesc                      [x] impl  [ ] docstring  [ ] test
    # [ ] getLowerLimit                [x] impl  [ ] docstring  [ ] test
    # [ ] setLowerLimit                [x] impl  [ ] docstring  [ ] test
    # [ ] getMask                      [x] impl  [ ] docstring  [ ] test
    # [ ] setMask                      [x] impl  [ ] docstring  [ ] test
    # [ ] getShortLabel                [x] impl  [ ] docstring  [ ] test
    # [ ] setShortLabel                [x] impl  [ ] docstring  [ ] test
    # [ ] getSymbol                    [x] impl  [ ] docstring  [ ] test
    # [ ] setSymbol                    [x] impl  [ ] docstring  [ ] test
    # [ ] getUpperLimit                [x] impl  [ ] docstring  [ ] test
    # [ ] setUpperLimit                [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.a2lDisplayText: String = None
        self.compuInverseValue: CompuConst = None
        self.compuScaleContents: CompuScaleContents = None
        self.desc: MultiLanguageOverviewParagraph = None
        self.lowerLimit: Limit = None
        self.mask: PositiveUnlimitedInteger = None
        self.shortLabel: Identifier = None
        self.symbol: CIdentifier = None
        self.upperLimit: Limit = None

    def getA2lDisplayText(self) -> String:
        return self.a2lDisplayText

    def setA2lDisplayText(self, value: String):
        self.a2lDisplayText = value
        return self

    def getCompuInverseValue(self) -> CompuConst:
        return self.compuInverseValue

    def setCompuInverseValue(self, value: CompuConst):
        self.compuInverseValue = value
        return self

    def getCompuScaleContents(self) -> CompuScaleContents:
        return self.compuScaleContents

    def setCompuScaleContents(self, value: CompuScaleContents):
        self.compuScaleContents = value
        return self

    def getDesc(self) -> MultiLanguageOverviewParagraph:
        return self.desc

    def setDesc(self, value: MultiLanguageOverviewParagraph):
        self.desc = value
        return self

    def getLowerLimit(self) -> Limit:
        return self.lowerLimit

    def setLowerLimit(self, value: Limit):
        self.lowerLimit = value
        return self

    def getMask(self) -> PositiveUnlimitedInteger:
        return self.mask

    def setMask(self, value: PositiveUnlimitedInteger):
        if value is not None:
            self.mask = value
        return self

    def getShortLabel(self) -> Identifier:
        return self.shortLabel

    def setShortLabel(self, value: Identifier):
        self.shortLabel = value
        return self

    def getSymbol(self) -> CIdentifier:
        return self.symbol

    def setSymbol(self, value: CIdentifier):
        self.symbol = value
        return self

    def getUpperLimit(self) -> Limit:
        return self.upperLimit

    def setUpperLimit(self, value: Limit):
        self.upperLimit = value
        return self


class CompuScales(CompuContent):
    """
    Container for multiple computation scales.
    Base: CompuContent
    """

    # CompuScales method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] addCompuScale                [x] impl  [ ] docstring  [ ] test
    # [ ] getCompuScales               [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.compuScales: List[CompuScale] = []

    def addCompuScale(self, compu_scale: CompuScale):
        self.compuScales.append(compu_scale)

    def getCompuScales(self) -> List[CompuScale]:
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

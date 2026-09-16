from typing import List, Optional
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.VariationPointCapable import VariationPointCapable
from abc import ABC

from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultiLanguageOverviewParagraph
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure import AtpBlueprintable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARNumerical, CIdentifier, Identifier, PositiveUnlimitedInteger, String, VerbatimString
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
    """
    Base class for computation methods.
    Base: ARObject
    """

    # Compu method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getCompuContent              [x] impl  [ ] docstring  [ ] test
    # [ ] setCompuContent              [x] impl  [ ] docstring  [ ] test
    # [ ] getCompuDefaultValue         [x] impl  [ ] docstring  [ ] test
    # [ ] setCompuDefaultValue         [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.compuContent: CompuContent = None
        self.compuDefaultValue: CompuConst = None

    def getCompuContent(self) -> CompuContent:
        return self.compuContent

    def setCompuContent(self, value: CompuContent):
        self.compuContent = value
        return self

    def getCompuDefaultValue(self) -> CompuConst:
        return self.compuDefaultValue

    def setCompuDefaultValue(self, value: CompuConst):
        self.compuDefaultValue = value
        return self


class CompuScaleContents(ARObject, ABC):
    """
    Abstract base class for computation scale contents.
    Base: ARObject
    """

    # CompuScaleContents method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        if type(self) is CompuScaleContents:
            raise TypeError("CompuScaleContents is an abstract class.")

        super().__init__()


class CompuScaleConstantContents(CompuScaleContents):
    """
    Represents constant contents of a computation scale.
    Base: CompuScaleContents
    """

    # CompuScaleConstantContents method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getCompuConst                [x] impl  [ ] docstring  [ ] test
    # [ ] setCompuConst                [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.compuConst: CompuConst = None

    def getCompuConst(self) -> CompuConst:
        return self.compuConst

    def setCompuConst(self, value: CompuConst):
        self.compuConst = value
        return self


class CompuRationalCoeffs(ARObject):
    """
    This meta-class represents the ability to express a rational function by specifying the coefficients of nominator and denominator.
    Base            : ARObject
    Aggregated by   : CompuScaleRationalFormula.compuRationalCoeffs
    """

    # CompuRationalCoeffs method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getCompuDenominator          [x] impl  [ ] docstring  [ ] test
    # [ ] setCompuDenominator          [x] impl  [ ] docstring  [ ] test
    # [ ] getCompuNumerator            [x] impl  [ ] docstring  [ ] test
    # [ ] setCompuNumerator            [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.compuDenominator: "CompuNominatorDenominator" = None
        self.compuNumerator: "CompuNominatorDenominator" = None

    def getCompuDenominator(self) -> "CompuNominatorDenominator":
        return self.compuDenominator

    def setCompuDenominator(self, value: "CompuNominatorDenominator"):
        self.compuDenominator = value
        return self

    def getCompuNumerator(self) -> "CompuNominatorDenominator":
        return self.compuNumerator

    def setCompuNumerator(self, value: "CompuNominatorDenominator"):
        self.compuNumerator = value
        return self


class CompuScaleRationalFormula(CompuScaleContents):
    """
    This meta-class represents the fact that the computation in this scale is represented as rational term.
    Base: CompuScaleContents
    """

    # CompuScaleRationalFormula method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getCompuRationalCoeffs       [x] impl  [ ] docstring  [ ] test
    # [ ] setCompuRationalCoeffs       [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.compuRationalCoeffs: CompuRationalCoeffs = None

    def getCompuRationalCoeffs(self) -> CompuRationalCoeffs:
        return self.compuRationalCoeffs

    def setCompuRationalCoeffs(self, value: CompuRationalCoeffs):
        self.compuRationalCoeffs = value
        return self


class CompuNominatorDenominator(ARObject):
    """
    This class represents the ability to express a polynomial either as Nominator or as Denominator.
    Base          : ARObject
    Aggregated by : CompuRationalCoeffs.compuDenominator, CompuRationalCoeffs.compuNumerator
    """

    # CompuNominatorDenominator method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] add_v                        [x] impl  [ ] docstring  [ ] test
    # [ ] get_vs                       [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.v: List[float] = []

    def add_v(self, v: float):
        self.v.append(v)

    def get_vs(self) -> List[float]:
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
    """
    Represents a computation method for converting between internal and physical values.
    Base: AtpBlueprintable
    """

    # CompuMethod method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getCompuInternalToPhys       [x] impl  [ ] docstring  [ ] test
    # [ ] setCompuInternalToPhys       [x] impl  [ ] docstring  [ ] test
    # [ ] getCompuPhysToInternal       [x] impl  [ ] docstring  [ ] test
    # [ ] setCompuPhysToInternal       [x] impl  [ ] docstring  [ ] test
    # [ ] getDisplayFormat             [x] impl  [ ] docstring  [ ] test
    # [ ] setDisplayFormat             [x] impl  [ ] docstring  [ ] test
    # [ ] getUnitRef                   [x] impl  [ ] docstring  [ ] test
    # [ ] setUnitRef                   [x] impl  [ ] docstring  [ ] test

    CATEGORY_TEXTTABLE = "TEXTTABLE"

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.compuInternalToPhys: Compu = None
        self.compuPhysToInternal: Compu = None
        self.displayFormat: str = None
        self.unitRef: RefType = None

    def getCompuInternalToPhys(self) -> Compu:
        return self.compuInternalToPhys

    def setCompuInternalToPhys(self, value: Compu):
        self.compuInternalToPhys = value
        return self

    def getCompuPhysToInternal(self) -> Compu:
        return self.compuPhysToInternal

    def setCompuPhysToInternal(self, value: Compu):
        self.compuPhysToInternal = value
        return self

    def getDisplayFormat(self) -> str:
        return self.displayFormat

    def setDisplayFormat(self, value: str):
        self.displayFormat = value
        return self

    def getUnitRef(self) -> RefType:
        return self.unitRef

    def setUnitRef(self, value: RefType):
        self.unitRef = value
        return self

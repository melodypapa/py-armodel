from typing import List
from abc import ABC

from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultiLanguageOverviewParagraph
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure import AtpBlueprintable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import ARElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import CIdentifier, Identifier, PositiveUnlimitedInteger, String
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Limit

class CompuContent(ARObject, ABC):
    """
    Abstract base class for computation content.
    Base: ARObject
    """
    def __init__(self):
        if type(self) == CompuContent:
            raise TypeError("CompuContent is an abstract class.")

        super().__init__()


class CompuConst(ARObject):
    """
    This meta-class represents the fact that the value of a computation method scale is constant.
    Base            : ARObject
    Aggregated by   : Compu.compuDefaultValue, CompuScale.compuInverseValue, CompuScaleConstantContents.compuCons
    """
    def __init__(self):
        super().__init__()

        self.compuConstContentType: 'CompuConstContent' = None

    def getCompuConstContentType(self) -> 'CompuConstContent':
        return self.compuConstContentType

    def setCompuConstContentType(self, value: 'CompuConstContent'):
        self.compuConstContentType = value
        return self

class Compu(ARObject):
    """
    Base class for computation methods.
    Base: ARObject
    """
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


class CompuConstContent(ARObject, ABC):
    """
    This meta-class represents the fact that the constant value of the computation method can be numerical or textual.
    Base            : ARObject
    Subclasses      : CompuConstFormulaContent, CompuConstNumericContent, CompuConstTextContent
    Aggregated by   : CompuConst.compuConstContentType
    """
    def __init__(self):
        if type(self) == CompuConstContent:
            raise TypeError("CompuConstContent is an abstract class.")

        super().__init__()


class CompuConstTextContent(CompuConstContent):
    """
    This meta-class represents the textual content of a scale.
    Base:           ARObject, CompuConstContent
    Aggregated by:  CompuConst.compuConstContentType
    """
    def __init__(self):
        super().__init__()

        self.vt: str = None

    def getVt(self) -> str:
        return self.vt

    def setVt(self, value: str):
        self.vt = value
        return self

class CompuConstNumericContent(CompuConstContent):
    """
    This meta-class represents the numeric content of a scale.
    Base: ARObject, CompuConstContent
    """
    def __init__(self):
        super().__init__()

        self.v: float = None

    def getV(self) -> float:
        return self.v

    def setV(self, value: float):
        self.v = value
        return self

class CompuConstFormulaContent(CompuConstContent):
    """
    This meta-class represents the formula content of a scale.
    Base: ARObject, CompuConstContent
    """
    def __init__(self):
        super().__init__()

        self.vf: str = None

    def getVf(self) -> str:
        return self.vf

    def setVf(self, value: str):
        self.vf = value
        return self




class CompuScaleContents(ARObject, ABC):
    """
    Abstract base class for computation scale contents.
    Base: ARObject
    """
    def __init__(self):
        if type(self) == CompuScaleContents:
            raise TypeError("CompuScaleContents is an abstract class.")

        super().__init__()


class CompuScaleConstantContents(CompuScaleContents):
    """
    Represents constant contents of a computation scale.
    Base: CompuScaleContents
    """
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
    def __init__(self):
        super().__init__()

        self.compuDenominator: 'CompuNominatorDenominator' = None
        self.compuNumerator: 'CompuNominatorDenominator' = None

    def getCompuDenominator(self) -> 'CompuNominatorDenominator':
        return self.compuDenominator

    def setCompuDenominator(self, value: 'CompuNominatorDenominator'):
        self.compuDenominator = value
        return self

    def getCompuNumerator(self) -> 'CompuNominatorDenominator':
        return self.compuNumerator

    def setCompuNumerator(self, value: 'CompuNominatorDenominator'):
        self.compuNumerator = value
        return self

class CompuScaleRationalFormula(CompuScaleContents):
    """
    This meta-class represents the fact that the computation in this scale is represented as rational term.
    Base: CompuScaleContents
    """
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
    def __init__(self):
        super().__init__()

        self.v: List[float] = []

    def add_v(self, v: float):
        self.v.append(v)

    def get_vs(self) -> List[float]:
        return self.v


class CompuScale(ARObject):
    """
    Represents a single scale in a computation method with limits and content.
    Base: ARObject
    """
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

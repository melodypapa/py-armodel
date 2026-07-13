from typing import List
from abc import ABC

from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultiLanguageOverviewParagraph
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpBlueprintable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import CIdentifier, Identifier, PositiveUnlimitedInteger, String
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Limit

class CompuContent(ARObject, ABC):
    """
    Abstract base class for computation content.
    Base: ARObject
    """
    # CompuContent method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        if type(self) is CompuContent:
            raise TypeError("CompuContent is an abstract class.")

        super().__init__()


class CompuConst(ARObject):
    """
    This meta-class represents the fact that the value of a computation method scale is constant.
    Base            : ARObject
    Aggregated by   : Compu.compuDefaultValue, CompuScale.compuInverseValue, CompuScaleConstantContents.compuCons
    """
    # CompuConst method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getCompuConstContentType     [x] impl  [ ] docstring  [ ] test
    # [ ] setCompuConstContentType     [x] impl  [ ] docstring  [ ] test

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


class CompuConstContent(ARObject, ABC):
    """
    This meta-class represents the fact that the constant value of the computation method can be numerical or textual.
    Base            : ARObject
    Subclasses      : CompuConstFormulaContent, CompuConstNumericContent, CompuConstTextContent
    Aggregated by   : CompuConst.compuConstContentType
    """
    # CompuConstContent method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        if type(self) is CompuConstContent:
            raise TypeError("CompuConstContent is an abstract class.")

        super().__init__()


class CompuConstTextContent(CompuConstContent):
    """
    This meta-class represents the textual content of a scale.
    Base:           ARObject, CompuConstContent
    Aggregated by:  CompuConst.compuConstContentType
    """
    # CompuConstTextContent method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getVt                        [x] impl  [ ] docstring  [ ] test
    # [ ] setVt                        [x] impl  [ ] docstring  [ ] test

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
    # CompuConstNumericContent method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getV                         [x] impl  [ ] docstring  [ ] test
    # [ ] setV                         [x] impl  [ ] docstring  [ ] test

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
    # CompuConstFormulaContent method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getVf                        [x] impl  [ ] docstring  [ ] test
    # [ ] setVf                        [x] impl  [ ] docstring  [ ] test

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


class CompuScale(ARObject):
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

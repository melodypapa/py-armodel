from typing import List
from abc import ABCMeta

from ....M2.MSR.Documentation.TextModel.MultilanguageData import MultiLanguageOverviewParagraph
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import ARElement
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import CIdentifier, Identifier, PositiveUnlimitedInteger, String
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Limit

class CompuContent(ARObject, metaclass=ABCMeta):
    def __init__(self):
        if type(self) == CompuContent:
            raise NotImplementedError("CompuContent is an abstract class.")

        super().__init__()


class CompuConst(ARObject):
    '''
    This meta-class represents the fact that the value of a computation method scale is constant.
    Base            : ARObject
    Aggregated by   : Compu.compuDefaultValue, CompuScale.compuInverseValue, CompuScaleConstantContents.compuCons
    '''
    def __init__(self):
        super().__init__()

        self.compuConstContentType = None           # type: CompuConstContent

    def getCompuConstContentType(self):
        return self.compuConstContentType

    def setCompuConstContentType(self, value):
        self.compuConstContentType = value
        return self

class Compu(ARObject):
    def __init__(self):
        super().__init__()

        self.compuContent = None                    # type: CompuContent
        self.compuDefaultValue = None               # type: CompuConst

    def getCompuContent(self):
        return self.compuContent

    def setCompuContent(self, value):
        self.compuContent = value
        return self

    def getCompuDefaultValue(self):
        return self.compuDefaultValue

    def setCompuDefaultValue(self, value):
        self.compuDefaultValue = value
        return self


class CompuConstContent(ARObject, metaclass=ABCMeta):
    '''
    This meta-class represents the fact that the constant value of the computation method can be numerical or textual.
    Base            : ARObject
    Subclasses      : CompuConstFormulaContent, CompuConstNumericContent, CompuConstTextContent
    Aggregated by   : CompuConst.compuConstContentType
    '''
    def __init__(self):
        if type(self) == CompuConstContent:
            raise NotImplementedError("CompuConstContent is an abstract class.")

        super().__init__()


class CompuConstTextContent(CompuConstContent):
    '''
    This meta-class represents the textual content of a scale.
    Base:           ARObject, CompuConstContent
    Aggregated by:  CompuConst.compuConstContentType
    '''
    def __init__(self):
        super().__init__()

        self.vt = None

    def getVt(self):
        return self.vt

    def setVt(self, value):
        self.vt = value
        return self

class CompuConstNumericContent(CompuConstContent):
    def __init__(self):
        super().__init__()

        self.v = None

    def getV(self):
        return self.v

    def setV(self, value):
        self.v = value
        return self
    
class CompuConstFormulaContent(CompuConstContent):
    def __init__(self):
        super().__init__()

        self.vf = None

    def getVf(self):
        return self.vf

    def setVf(self, value):
        self.vf = value
        return self




class CompuScaleContents(ARObject, metaclass=ABCMeta):
    def __init__(self):
        if type(self) == CompuScaleContents:
            raise NotImplementedError("CompuScaleContents is an abstract class.")

        super().__init__()


class CompuScaleConstantContents(CompuScaleContents):
    def __init__(self):
        super().__init__()

        self.compuConst = None     # type: CompuConst

    def getCompuConst(self):
        return self.compuConst

    def setCompuConst(self, value):
        self.compuConst = value
        return self

class CompuRationalCoeffs(ARObject):
    '''
    This meta-class represents the ability to express a rational function by specifying the coefficients of nominator and denominator.
    Base            : ARObject
    Aggregated by   : CompuScaleRationalFormula.compuRationalCoeffs
    '''
    def __init__(self):
        super().__init__()

        self.compuDenominator = None   # type: CompuNominatorDenominator
        self.compuNumerator = None     # type: CompuNominatorDenominator

    def getCompuDenominator(self):
        return self.compuDenominator

    def setCompuDenominator(self, value):
        self.compuDenominator = value
        return self

    def getCompuNumerator(self):
        return self.compuNumerator

    def setCompuNumerator(self, value):
        self.compuNumerator = value
        return self

class CompuScaleRationalFormula(CompuScaleContents):
    '''
    This meta-class represents the fact that the computation in this scale is represented as rational term.
    '''
    def __init__(self):
        super().__init__()

        self.compuRationalCoeffs = None         # type: CompuRationalCoeffs

    def getCompuRationalCoeffs(self):
        return self.compuRationalCoeffs

    def setCompuRationalCoeffs(self, value):
        self.compuRationalCoeffs = value
        return self

class CompuNominatorDenominator(ARObject):
    '''
    This class represents the ability to express a polynomial either as Nominator or as Denominator.
    Base          : ARObject
    Aggregated by : CompuRationalCoeffs.compuDenominator, CompuRationalCoeffs.compuNumerator
    '''
    def __init__(self):
        super().__init__()

        self.v = []             # type List[float]

    def add_v(self, v: float):
        self.v.append(v)

    def get_vs(self) -> List[float]:
        return self.v


class CompuScale(Compu):
    def __init__(self):
        super().__init__()

        self.a2lDisplayText = None                              # type: String
        self.compuInverseValue = None                           # type: CompuConst
        self.compuScaleContents = None                          # type: CompuScaleContents
        self.desc = None                                        # type: MultiLanguageOverviewParagraph
        self.lowerLimit = None                                  # type: Limit
        self.mask = None                                        # type: PositiveUnlimitedInteger
        self.shortLabel = None                                  # type: Identifier
        self.symbol = None                                      # type: CIdentifier
        self.upperLimit = None                                  # type: Limit

    def getA2lDisplayText(self):
        return self.a2lDisplayText

    def setA2lDisplayText(self, value):
        self.a2lDisplayText = value
        return self

    def getCompuInverseValue(self):
        return self.compuInverseValue

    def setCompuInverseValue(self, value):
        self.compuInverseValue = value
        return self

    def getCompuScaleContents(self):
        return self.compuScaleContents

    def setCompuScaleContents(self, value):
        self.compuScaleContents = value
        return self

    def getDesc(self):
        return self.desc

    def setDesc(self, value):
        self.desc = value
        return self

    def getLowerLimit(self):
        return self.lowerLimit

    def setLowerLimit(self, value):
        self.lowerLimit = value
        return self

    def getMask(self):
        return self.mask

    def setMask(self, value):
        self.mask = value
        return self

    def getShortLabel(self):
        return self.shortLabel

    def setShortLabel(self, value):
        self.shortLabel = value
        return self

    def getSymbol(self):
        return self.symbol

    def setSymbol(self, value):
        self.symbol = value
        return self

    def getUpperLimit(self):
        return self.upperLimit

    def setUpperLimit(self, value):
        self.upperLimit = value
        return self

class CompuScales(CompuContent):
    def __init__(self):
        super().__init__()

        self.compuScales = []              # type: List[CompuScale]

    def addCompuScale(self, compu_scale: CompuScale):
        self.compuScales.append(compu_scale)

    def getCompuScales(self) -> List[CompuScale]:
        return self.compuScales


class CompuMethod(ARElement):
    CATEGORY_TEXTTABLE = "TEXTTABLE"

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.compuInternalToPhys = None     # type: Compu
        self.compuPhysToInternal = None     # type: Compu
        self.displayFormat = None           # type: DisplayFormatString
        self.unitRef = None                 # type: RefType

    def getCompuInternalToPhys(self):
        return self.compuInternalToPhys

    def setCompuInternalToPhys(self, value):
        self.compuInternalToPhys = value
        return self

    def getCompuPhysToInternal(self):
        return self.compuPhysToInternal

    def setCompuPhysToInternal(self, value):
        self.compuPhysToInternal = value
        return self

    def getDisplayFormat(self):
        return self.displayFormat

    def setDisplayFormat(self, value):
        self.displayFormat = value
        return self

    def getUnitRef(self):
        return self.unitRef

    def setUnitRef(self, value):
        self.unitRef = value
        return self

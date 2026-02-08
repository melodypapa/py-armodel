from abc import ABC
from typing import (
    List,
    Union,
)

from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure import (
    AtpBlueprintable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    CIdentifier,
    Identifier,
    Limit,
    PositiveUnlimitedInteger,
    RefType,
    String,
)
from armodel.v2.models.M2.MSR.Documentation.TextModel.MultilanguageData import (
    MultiLanguageOverviewParagraph,
)


class CompuContent(ARObject, ABC):
    """
    Package: M2::MSR::AsamHdo::ComputationMethod
    Abstract base class for computation content.
    Base: ARObject
    """
    def __init__(self) -> None:
        if type(self) is CompuContent:
            raise TypeError("CompuContent is an abstract class.")

        super().__init__()


class CompuConst(ARObject):
    """
    Package: M2::MSR::AsamHdo::ComputationMethod
    This meta-class represents the fact that the value of a computation method scale is constant.
    Base            : ARObject
    Aggregated by   : Compu.compuDefaultValue, CompuScale.compuInverseValue, CompuScaleConstantContents.compuCons
    """

    def __init__(self) -> None:
        super().__init__()

        self.compuConstContentType: 'CompuConstContent' = None

    def getCompuConstContentType(self) -> 'CompuConstContent':
        return self.compuConstContentType

    def setCompuConstContentType(self, value: 'CompuConstContent'):
        self.compuConstContentType = value
        return self

class Compu(ARObject):
    """
    Package: M2::MSR::AsamHdo::ComputationMethod
    Base class for computation methods.
    Base: ARObject
    """

    def __init__(self) -> None:
        super().__init__()

        self.compuContent: Union[Union[CompuContent, None] , None] = None
        self.compuDefaultValue: Union[Union[CompuConst, None] , None] = None

    def getCompuContent(self) -> Union[CompuContent, None]:
        return self.compuContent

    def setCompuContent(self, value: CompuContent) -> "Compu":
        self.compuContent = value
        return self

    def getCompuDefaultValue(self) -> Union[CompuConst, None]:
        return self.compuDefaultValue

    def setCompuDefaultValue(self, value: CompuConst) -> "Compu":
        self.compuDefaultValue = value
        return self


class CompuConstContent(ARObject, ABC):
    """
    Package: M2::MSR::AsamHdo::ComputationMethod
    This meta-class represents the fact that the constant value of the computation method can be numerical or textual.
    Base            : ARObject
    Subclasses      : CompuConstFormulaContent, CompuConstNumericContent, CompuConstTextContent
    Aggregated by   : CompuConst.compuConstContentType
    """
    def __init__(self) -> None:
        if type(self) is CompuConstContent:
            raise TypeError("CompuConstContent is an abstract class.")

        super().__init__()


class CompuConstTextContent(CompuConstContent):
    """
    Package: M2::MSR::AsamHdo::ComputationMethod
    This meta-class represents the textual content of a scale.
    Base:           ARObject, CompuConstContent
    Aggregated by:  CompuConst.compuConstContentType
    """
    def __init__(self) -> None:
        super().__init__()

        self.vt: Union[str, None] = None

    def getVt(self) -> Union[str, None]:
        return self.vt

    def setVt(self, value: str) -> "CompuConstTextContent":
        self.vt = value
        return self

class CompuConstNumericContent(CompuConstContent):
    """
    Package: M2::MSR::AsamHdo::ComputationMethod
    This meta-class represents the numeric content of a scale.
    Base: ARObject, CompuConstContent
    """
    def __init__(self) -> None:
        super().__init__()

        self.v: Union[float, None] = None

    def getV(self) -> Union[float, None]:
        return self.v

    def setV(self, value: float) -> "CompuConstNumericContent":
        self.v = value
        return self

class CompuConstFormulaContent(CompuConstContent):
    """
    Package: M2::MSR::AsamHdo::ComputationMethod
    This meta-class represents the formula content of a scale.
    Base: ARObject, CompuConstContent
    """
    def __init__(self) -> None:
        super().__init__()

        self.vf: Union[str, None] = None

    def getVf(self) -> Union[str, None]:
        return self.vf

    def setVf(self, value: str) -> "CompuConstFormulaContent":
        self.vf = value
        return self




class CompuScaleContents(ARObject, ABC):
    """
    Package: M2::MSR::AsamHdo::ComputationMethod
    Abstract base class for computation scale contents.
    Base: ARObject
    """
    def __init__(self) -> None:
        if type(self) is CompuScaleContents:
            raise TypeError("CompuScaleContents is an abstract class.")

        super().__init__()


class CompuScaleConstantContents(CompuScaleContents):
    """
    Package: M2::MSR::AsamHdo::ComputationMethod
    Represents constant contents of a computation scale.
    Base: CompuScaleContents
    """
    def __init__(self) -> None:
        super().__init__()

        self.compuConst: Union[Union[CompuConst, None] , None] = None

    def getCompuConst(self) -> Union[CompuConst, None]:
        return self.compuConst

    def setCompuConst(self, value: CompuConst) -> "CompuScaleConstantContents":
        self.compuConst = value
        return self

class CompuRationalCoeffs(ARObject):
    """
    Package: M2::MSR::AsamHdo::ComputationMethod
    This meta-class represents the ability to express a rational function by specifying the coefficients of nominator and denominator.
    Base            : ARObject
    Aggregated by   : CompuScaleRationalFormula.compuRationalCoeffs
    """

    def __init__(self) -> None:
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
    Package: M2::MSR::AsamHdo::ComputationMethod
    This meta-class represents the fact that the computation in this scale is represented as rational term.
    Base: CompuScaleContents
    """
    def __init__(self) -> None:
        super().__init__()

        self.compuRationalCoeffs: Union[Union[CompuRationalCoeffs, None] , None] = None

    def getCompuRationalCoeffs(self) -> Union[CompuRationalCoeffs, None]:
        return self.compuRationalCoeffs

    def setCompuRationalCoeffs(self, value: CompuRationalCoeffs) -> "CompuScaleRationalFormula":
        self.compuRationalCoeffs = value
        return self

class CompuNominatorDenominator(ARObject):
    """
    Package: M2::MSR::AsamHdo::ComputationMethod
    This class represents the ability to express a polynomial either as Nominator or as Denominator.
    Base          : ARObject
    Aggregated by : CompuRationalCoeffs.compuDenominator, CompuRationalCoeffs.compuNumerator
    """

    def __init__(self) -> None:
        super().__init__()

        self.v: List[float] = []

    def add_v(self, v: float) -> None:
        self.v.append(v)

    def get_vs(self) -> List[float]:
        return self.v


class CompuScale(ARObject):
    """
    Package: M2::MSR::AsamHdo::ComputationMethod
    Represents a single scale in a computation method with limits and content.
    Base: ARObject
    """

    def __init__(self) -> None:
        super().__init__()

        self.a2lDisplayText: Union[Union[String, None] , None] = None
        self.compuInverseValue: Union[Union[CompuConst, None] , None] = None
        self.compuScaleContents: Union[Union[CompuScaleContents, None] , None] = None
        self.desc: Union[Union[MultiLanguageOverviewParagraph, None] , None] = None
        self.lowerLimit: Union[Union[Limit, None] , None] = None
        self.mask: Union[Union[PositiveUnlimitedInteger, None] , None] = None
        self.shortLabel: Union[Union[Identifier, None] , None] = None
        self.symbol: Union[Union[CIdentifier, None] , None] = None
        self.upperLimit: Union[Union[Limit, None] , None] = None

    def getA2lDisplayText(self) -> Union[String, None]:
        return self.a2lDisplayText

    def setA2lDisplayText(self, value: String) -> "CompuScale":
        self.a2lDisplayText = value
        return self

    def getCompuInverseValue(self) -> Union[CompuConst, None]:
        return self.compuInverseValue

    def setCompuInverseValue(self, value: CompuConst) -> "CompuScale":
        self.compuInverseValue = value
        return self

    def getCompuScaleContents(self) -> Union[CompuScaleContents, None]:
        return self.compuScaleContents

    def setCompuScaleContents(self, value: CompuScaleContents) -> "CompuScale":
        self.compuScaleContents = value
        return self

    def getDesc(self) -> Union[MultiLanguageOverviewParagraph, None]:
        return self.desc

    def setDesc(self, value: MultiLanguageOverviewParagraph) -> "CompuScale":
        self.desc = value
        return self

    def getLowerLimit(self) -> Union[Limit, None]:
        return self.lowerLimit

    def setLowerLimit(self, value: Limit) -> "CompuScale":
        self.lowerLimit = value
        return self

    def getMask(self) -> Union[PositiveUnlimitedInteger, None]:
        return self.mask

    def setMask(self, value: PositiveUnlimitedInteger) -> "CompuScale":
        if value is not None:
            self.mask = value
        return self

    def getShortLabel(self) -> Union[Identifier, None]:
        return self.shortLabel

    def setShortLabel(self, value: Identifier) -> "CompuScale":
        self.shortLabel = value
        return self

    def getSymbol(self) -> Union[CIdentifier, None]:
        return self.symbol

    def setSymbol(self, value: CIdentifier) -> "CompuScale":
        self.symbol = value
        return self

    def getUpperLimit(self) -> Union[Limit, None]:
        return self.upperLimit

    def setUpperLimit(self, value: Limit) -> "CompuScale":
        self.upperLimit = value
        return self

class CompuScales(CompuContent):
    """
    Package: M2::MSR::AsamHdo::ComputationMethod
    Container for multiple computation scales.
    Base: CompuContent
    """
    def __init__(self) -> None:
        super().__init__()

        self.compuScales: List[CompuScale] = []

    def addCompuScale(self, compu_scale: CompuScale) -> None:
        self.compuScales.append(compu_scale)

    def getCompuScales(self) -> List[CompuScale]:
        return self.compuScales


class CompuMethod(AtpBlueprintable):
    """
    Package: M2::MSR::AsamHdo::ComputationMethod
    Represents a computation method for converting between internal and physical values.
    Base: AtpBlueprintable
    """
    CATEGORY_TEXTTABLE = "TEXTTABLE"

    def __init__(self, parent: ARObject, short_name: str) -> None:
        super().__init__(parent, short_name)

        self.compuInternalToPhys: Union[Union[Compu, None] , None] = None
        self.compuPhysToInternal: Union[Union[Compu, None] , None] = None
        self.displayFormat: Union[str, None] = None
        self.unitRef: Union[Union[RefType, None] , None] = None

    def getCompuInternalToPhys(self) -> Union[Compu, None]:
        return self.compuInternalToPhys

    def setCompuInternalToPhys(self, value: Compu) -> "CompuMethod":
        self.compuInternalToPhys = value
        return self

    def getCompuPhysToInternal(self) -> Union[Compu, None]:
        return self.compuPhysToInternal

    def setCompuPhysToInternal(self, value: Compu) -> "CompuMethod":
        self.compuPhysToInternal = value
        return self

    def getDisplayFormat(self) -> Union[str, None]:
        return self.displayFormat

    def setDisplayFormat(self, value: str) -> "CompuMethod":
        self.displayFormat = value
        return self

    def getUnitRef(self) -> Union[RefType, None]:
        return self.unitRef

    def setUnitRef(self, value: RefType) -> "CompuMethod":
        self.unitRef = value
        return self

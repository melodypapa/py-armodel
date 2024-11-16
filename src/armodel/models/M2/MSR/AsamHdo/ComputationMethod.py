from typing import List
from abc import ABCMeta
from ...AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral
from ...AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from ....ar_ref import RefType
from ....general_structure import ARElement, Limit

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

        self.compu_const_content_type = None    # type: CompuConstContent


class Compu(ARObject):
    def __init__(self):
        super().__init__()

        '''required'''
        self.compu_content = None           # type: CompuContent

        '''optional'''
        self.compu_default_value = None     # type: CompuConst


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


class CompuConstNumericContent(CompuConstContent):

    def __init__(self):
        super().__init__()

        self.v = None


class CompuScaleContents(ARObject, metaclass=ABCMeta):
    def __init__(self):
        if type(self) == CompuScaleContents:
            raise NotImplementedError("CompuScaleContents is an abstract class.")

        super().__init__()


class CompuScaleConstantContents(CompuScaleContents):
    def __init__(self):
        super().__init__()

        self.compu_const = None     # type: CompuConst


class CompuRationalCoeffs(ARObject):
    '''
    This meta-class represents the ability to express a rational function by specifying the coefficients of nominator and denominator.
    Base            : ARObject
    Aggregated by   : CompuScaleRationalFormula.compuRationalCoeffs
    '''
    def __init__(self):
        super().__init__()

        self.compu_denominator = None   # type: CompuNominatorDenominator
        self.compu_numerator = None     # type: CompuNominatorDenominator


class CompuScaleRationalFormula(CompuScaleContents):
    '''
    This meta-class represents the fact that the computation in this scale is represented as rational term.
    '''
    def __init__(self):
        super().__init__()

        self.compu_rational_coeffs = None   # type: CompuRationalCoeffs


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

        self.symbol = None                      # type: ARLiteral
        self.lowerLimit = None                  # type: Limit
        self.upperLimit = None                  # type: Limit
        self.compuInverseValue = None           # type: CompuConst
        self.compuScaleContents = None          # type: CompuScaleContents
        self.short_label = None                 # type: ARLiteral


class CompuScales(CompuContent):
    def __init__(self):
        super().__init__()

        self.compu_scales = []              # type: List[CompuScale]

    def addCompuScale(self, compu_scale: CompuScale):
        self.compu_scales.append(compu_scale)

    def getCompuScales(self) -> List[CompuScale]:
        return self.compu_scales


class CompuMethod(ARElement):
    CATEGORY_TEXTTABLE = "TEXTTABLE"

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.compu_internal_to_phys = None  # type: Compu
        self.compu_phys_to_internal = None  # type: Compu
        self.display_format = None          # type: DisplayFormatString
        self.unit_ref = None                # type: RefType
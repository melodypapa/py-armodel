from abc import ABCMeta
from typing import List

from .M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARFloat, ARNumerical

from .M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from .M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from .data_def_properties import ValueList

class SwValues(ARObject):
    def __init__(self):
        super().__init__()

        self._v = []                    # type: List[ARNumerical]
        self.vt = None                  # type: float

    def addV(self, v: ARNumerical):
        self._v.append(v)

    def getVs(self) -> List[ARNumerical]:
        return self._v
    
class SwValueCont(ARObject):
    def __init__(self):
        super().__init__()

        self.sw_arraysize = None         # type: ValueList
        self.unit_ref = None             # type: RefType
        self.sw_values_phys = None        # type: SwValues

class SwGenericAxisParam(ARObject):
    def __init__(self):
        super().__init__()

        self.swGenericAxisParamTypeRef = None   # type: RefType
        self.vf = []                            # type: List[ARFloat]
class SwAxisGeneric(ARObject):
    def __init__(self):
        super().__init__()

        self.swAxisTypeRef = None               # type: RefType
        self.swGenericAxisParam = []            # type: List[SwGenericAxisParam]

class SwCalprmAxisTypeProps(ARObject, metaclass = ABCMeta):
    def __init__(self):
        if type(self) == SwCalprmAxisTypeProps:
            raise NotImplementedError("SwCalprmAxisTypeProps is an abstract class.")
        
        super().__init__()
        
        self.maxGradient = None         # type: ARFloat
        self.monotony = None            # type: MonotonyEnum

class SwAxisIndividual(SwCalprmAxisTypeProps):
    def __init__(self):
        super().__init__()

        self.compuMethodRef = None              # type: RefType
        self.dataConstrRef = None               # type: RefType
        self.inputVariableTypeRef = None        # type: RefType
        self.swAxisGeneric = None               # type: SwAxisGeneric
        self.swMaxAxisPoints = None             # type: ARNumerical
        self.swMinAxisPoints = None             # type: ARNumerical
        self.swVariableRefs = []                # type: List
        self.unitRef = None                     # type: RefType

    def setInputVariableTypeRef(self, ref: RefType):
        self.inputVariableTypeRef = ref
        return self
    
    def setCompuMethodRef(self, ref: RefType):
        self.compuMethodRef = ref
        return self
    
    def setSwMaxAxisPoints(self, points: int):
        self.swMaxAxisPoints = points
        return self
    
    def setSwMinAxisPoints(self, points: int):
        self.swMinAxisPoints = points
        return self
    
    def setDataConstrRef(self, ref: RefType):
        self.dataConstrRef = ref
        return self

class SwAxisGrouped(SwCalprmAxisTypeProps):
    def __init__(self):
        super().__init__()

        self.sharedAxisTypeRef = None           # type: RefType
        self.swAxisIndex = None                 # type: ARNumerical
        self.swCalprmRef = None                 # type: SwCalprmRefProxy

    def setSharedAxisTypeRef(self, ref: RefType):
        self.sharedAxisTypeRef = ref
        return self

class SwCalprmAxis(ARObject):
    def __init__(self):
        super().__init__()

        self.category = None                # type: CalprmAxisCategoryEnum
        self.displayFormat = None           # type: DisplayFormatString
        self.sw_axis_index = None             # type: AxisIndexType   
        self.swCalibrationAccess = None     # type: SwCalibrationAccessEnum
        self.sw_calprm_axis_type_props = None   # type: SwCalprmAxisTypeProps

class SwCalprmAxisSet(ARObject):
    def __init__(self):
        super().__init__()

        self._swCalprmAxis = []          # type: List[SwCalprmAxis]

    def addSwCalprmAxis(self, axis: SwCalprmAxis):
        self._swCalprmAxis.append(axis)

    def getSwCalprmAxises(self) -> List[SwCalprmAxis]:
        return self._swCalprmAxis
    


from armodel.models.M2.MSR.DataDictionary.CalibrationParameter import SwCalprmAxisTypeProps
from ...AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from ...AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARFloat, ARNumerical, RefType
from typing import List

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
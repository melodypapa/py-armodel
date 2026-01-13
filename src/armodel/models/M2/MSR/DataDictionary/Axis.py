from typing import List
from ....M2.MSR.DataDictionary.CalibrationParameter import SwCalprmAxisTypeProps
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARFloat, ARNumerical, RefType

class SwGenericAxisParam(ARObject):
    def __init__(self):
        super().__init__()

        self.swGenericAxisParamTypeRef = None           # type: RefType
        self.vfs = []                                   # type: List[ARFloat]

    def getSwGenericAxisParamTypeRef(self):
        return self.swGenericAxisParamTypeRef

    def setSwGenericAxisParamTypeRef(self, value):
        self.swGenericAxisParamTypeRef = value
        return self

    def getVfs(self):
        return self.vfs

    def addVf(self, value):
        self.vfs.append(value)
        return self

class SwAxisGeneric(ARObject):
    def __init__(self):
        super().__init__()

        self.swAxisTypeRef = None                   # type: RefType
        self.swGenericAxisParams = []               # type: List[SwGenericAxisParam]

    def getSwAxisTypeRef(self):
        return self.swAxisTypeRef

    def setSwAxisTypeRef(self, value):
        self.swAxisTypeRef = value
        return self

    def getSwGenericAxisParams(self):
        return self.swGenericAxisParams

    def addSwGenericAxisParam(self, value):
        self.swGenericAxisParams.append(value)
        return self

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

    def getCompuMethodRef(self):
        return self.compuMethodRef

    def setCompuMethodRef(self, value):
        self.compuMethodRef = value
        return self

    def getDataConstrRef(self):
        return self.dataConstrRef

    def setDataConstrRef(self, value):
        self.dataConstrRef = value
        return self

    def getInputVariableTypeRef(self):
        return self.inputVariableTypeRef

    def setInputVariableTypeRef(self, value):
        self.inputVariableTypeRef = value
        return self

    def getSwAxisGeneric(self):
        return self.swAxisGeneric

    def setSwAxisGeneric(self, value):
        self.swAxisGeneric = value
        return self

    def getSwMaxAxisPoints(self):
        return self.swMaxAxisPoints

    def setSwMaxAxisPoints(self, value):
        self.swMaxAxisPoints = value
        return self

    def getSwMinAxisPoints(self):
        return self.swMinAxisPoints

    def setSwMinAxisPoints(self, value):
        self.swMinAxisPoints = value
        return self

    def getSwVariableRefs(self):
        return self.swVariableRefs

    def setSwVariableRefs(self, value):
        self.swVariableRefs = value
        return self

    def getUnitRef(self):
        return self.unitRef

    def setUnitRef(self, value):
        self.unitRef = value
        return self


class SwAxisGrouped(SwCalprmAxisTypeProps):
    def __init__(self):
        super().__init__()

        self.sharedAxisTypeRef = None           # type: RefType
        self.swAxisIndex = None                 # type: ARNumerical
        self.swCalprmRef = None                 # type: RefType

    def getSharedAxisTypeRef(self):
        return self.sharedAxisTypeRef

    def setSharedAxisTypeRef(self, value):
        self.sharedAxisTypeRef = value
        return self

    def getSwAxisIndex(self):
        return self.swAxisIndex

    def setSwAxisIndex(self, value):
        self.swAxisIndex = value
        return self

    def getSwCalprmRef(self):
        return self.swCalprmRef

    def setSwCalprmRef(self, value):
        self.swCalprmRef = value
        return self
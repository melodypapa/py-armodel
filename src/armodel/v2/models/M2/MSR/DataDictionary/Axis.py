from typing import List, Union

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARNumerical,
    RefType,
)
from armodel.v2.models.M2.MSR.DataDictionary.CalibrationParameter import (
    SwCalprmAxisTypeProps,
)


class SwGenericAxisParam(ARObject):

    def __init__(self) -> None:
        super().__init__()

        self.swGenericAxisParamTypeRef: Union[RefType, None] = None
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

    def __init__(self) -> None:
        super().__init__()

        self.swAxisTypeRef: Union[RefType, None] = None
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
    def __init__(self) -> None:
        super().__init__()

        self.compuMethodRef: Union[RefType, None] = None
        self.dataConstrRef: Union[RefType, None] = None
        self.inputVariableTypeRef: Union[RefType, None] = None
        self.swAxisGeneric: Union[SwAxisGeneric, None] = None
        self.swMaxAxisPoints: Union[ARNumerical, None] = None
        self.swMinAxisPoints: Union[ARNumerical, None] = None
        self.swVariableRefs = []                # type: List
        self.unitRef: Union[RefType, None] = None

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
    def __init__(self) -> None:
        super().__init__()

        self.sharedAxisTypeRef: Union[RefType, None] = None
        self.swAxisIndex: Union[ARNumerical, None] = None
        self.swCalprmRef: Union[RefType, None] = None

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

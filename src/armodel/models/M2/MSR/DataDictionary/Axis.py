from typing import List, Optional
from armodel.models.M2.MSR.DataDictionary.CalibrationParameter import SwCalprmAxisTypeProps
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARNumerical, RefType


class SwGenericAxisParam(ARObject):
    """
    This meta-class describes a specific parameter of a generic axis. The name of the parameter is defined through a reference to a parameter type defined on a corresponding axis type. The value of the parameter is given here in case that it is not changeable during calibration. Example is shift / offset in a fixed axis.
    """

    # SwGenericAxisParam method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.53, p.356
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getSwGenericAxisParamTypeRef [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSwGenericAxisParamTypeRef [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getVfs                       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addVf                        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # Parameter type defined on a corresponding axis type. References can only be made to axis parameters types which are defined within the referenced axis type.
        self.swGenericAxisParamTypeRef: Optional[RefType] = None

        # This attribute represents the value of the generic axis parameter.
        self.vfs: List[ARNumerical] = []

    def getSwGenericAxisParamTypeRef(self) -> Optional[RefType]:
        """
        Parameter type defined on a corresponding axis type. References can only be made to axis parameters types which are defined within the referenced axis type.
        """
        return self.swGenericAxisParamTypeRef

    def setSwGenericAxisParamTypeRef(self, value: Optional[RefType]) -> "SwGenericAxisParam":
        """
        Parameter type defined on a corresponding axis type. References can only be made to axis parameters types which are defined within the referenced axis type.
        A None value is a no-op and does not overwrite an existing swGenericAxisParamTypeRef.
        """
        if value is not None:
            self.swGenericAxisParamTypeRef = value
        return self

    def getVfs(self) -> List[ARNumerical]:
        """
        This attribute represents the value of the generic axis parameter.
        """
        return self.vfs

    def addVf(self, value: Optional[ARNumerical]) -> "SwGenericAxisParam":
        """
        This attribute represents the value of the generic axis parameter.
        A None value is a no-op and is not appended to vfs.
        """
        if value is not None:
            self.vfs.append(value)
        return self


class SwAxisGeneric(ARObject):
    """
    This meta-class defines a generic axis. In a generic axis the axispoints points are calculated in the ECU. The ECU is equipped with a fixed calculation algorithm. Parameters for the algorithm can be stored in the data component of the ECU. Therefore these parameters are specified in the data declaration, not in the calibration data.
    """

    # SwAxisGeneric method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.51, p.355
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                 [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getSwAxisTypeRef         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSwAxisTypeRef         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSwGenericAxisParams   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addSwGenericAxisParam    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # Associated axis calculation strategy.
        self.swAxisTypeRef: Optional[RefType] = None

        # Specific parameter of a generic axis.
        self.swGenericAxisParams: List[SwGenericAxisParam] = []

    def getSwAxisTypeRef(self) -> Optional[RefType]:
        """
        Associated axis calculation strategy.
        """
        return self.swAxisTypeRef

    def setSwAxisTypeRef(self, value: Optional[RefType]) -> "SwAxisGeneric":
        """
        Associated axis calculation strategy.
        A None value is a no-op and does not overwrite an existing swAxisTypeRef.
        """
        if value is not None:
            self.swAxisTypeRef = value
        return self

    def getSwGenericAxisParams(self) -> List[SwGenericAxisParam]:
        """
        Specific parameter of a generic axis.
        """
        return self.swGenericAxisParams

    def addSwGenericAxisParam(self, value: Optional[SwGenericAxisParam]) -> "SwAxisGeneric":
        """
        Specific parameter of a generic axis.
        A None value is a no-op and is not appended to swGenericAxisParams.
        """
        if value is not None:
            self.swGenericAxisParams.append(value)
        return self


class SwAxisIndividual(SwCalprmAxisTypeProps):
    """
    Individual axis properties extending calibration axis type with compu
    method, data constraint, and variable references.
    """

    # SwAxisIndividual method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getCompuMethodRef            [x] impl  [ ] docstring  [ ] test
    # [ ] setCompuMethodRef            [x] impl  [ ] docstring  [ ] test
    # [ ] getDataConstrRef             [x] impl  [ ] docstring  [ ] test
    # [ ] setDataConstrRef             [x] impl  [ ] docstring  [ ] test
    # [ ] getInputVariableTypeRef      [x] impl  [ ] docstring  [ ] test
    # [ ] setInputVariableTypeRef      [x] impl  [ ] docstring  [ ] test
    # [ ] getSwAxisGeneric             [x] impl  [ ] docstring  [ ] test
    # [ ] setSwAxisGeneric             [x] impl  [ ] docstring  [ ] test
    # [ ] getSwMaxAxisPoints           [x] impl  [ ] docstring  [ ] test
    # [ ] setSwMaxAxisPoints           [x] impl  [ ] docstring  [ ] test
    # [ ] getSwMinAxisPoints           [x] impl  [ ] docstring  [ ] test
    # [ ] setSwMinAxisPoints           [x] impl  [ ] docstring  [ ] test
    # [ ] getSwVariableRefs            [x] impl  [ ] docstring  [ ] test
    # [ ] setSwVariableRefs            [x] impl  [ ] docstring  [ ] test
    # [ ] getUnitRef                   [x] impl  [ ] docstring  [ ] test
    # [ ] setUnitRef                   [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.compuMethodRef = None  # type: RefType
        self.dataConstrRef = None  # type: RefType
        self.inputVariableTypeRef = None  # type: RefType
        self.swAxisGeneric = None  # type: SwAxisGeneric
        self.swMaxAxisPoints = None  # type: ARNumerical
        self.swMinAxisPoints = None  # type: ARNumerical
        self.swVariableRefs = []  # type: List
        self.unitRef = None  # type: RefType

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
    """
    Grouped axis properties referencing a shared axis type with index and
    calibration reference.
    """

    # SwAxisGrouped method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getSharedAxisTypeRef         [x] impl  [ ] docstring  [ ] test
    # [ ] setSharedAxisTypeRef         [x] impl  [ ] docstring  [ ] test
    # [ ] getSwAxisIndex               [x] impl  [ ] docstring  [ ] test
    # [ ] setSwAxisIndex               [x] impl  [ ] docstring  [ ] test
    # [ ] getSwCalprmRef               [x] impl  [ ] docstring  [ ] test
    # [ ] setSwCalprmRef               [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self.sharedAxisTypeRef = None  # type: RefType
        self.swAxisIndex = None  # type: ARNumerical
        self.swCalprmRef = None  # type: RefType

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

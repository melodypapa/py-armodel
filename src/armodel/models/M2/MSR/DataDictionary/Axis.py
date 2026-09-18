from typing import List, Optional
from armodel.models.M2.MSR.DataDictionary.CalibrationParameter import SwCalprmAxisTypeProps
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARNumerical, Integer, RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.MSR.DataDictionary.DatadictionaryProxies import SwCalprmRefProxy, SwVariableRefProxy
from armodel.models.M2.MSR.DataDictionary.RecordLayout import AxisIndexType


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
    This meta-class describes an axis integrated into a parameter (field etc.). The integration makes this individual to each parameter. The so-called grouped axis represents the counterpart to this. It is conceived as an independent parameter (see class SwAxisGrouped).
    """

    # SwAxisIndividual method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.50, p.355
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getCompuMethodRef       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCompuMethodRef       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDataConstrRef        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDataConstrRef        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getInputVariableTypeRef [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setInputVariableTypeRef [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSwAxisGeneric        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSwAxisGeneric        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSwMaxAxisPoints      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSwMaxAxisPoints      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSwMinAxisPoints      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSwMinAxisPoints      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSwVariableRefs       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addSwVariableRef        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getUnitRef              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setUnitRef              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # This is the compuMethod which is expected for the axis. It is used in early stages if the particular input-value is not yet available.
        self.compuMethodRef: Optional[RefType] = None

        # Refers to constraints, e.g. for plausibility checks.
        self.dataConstrRef: Optional[RefType] = None

        # This is the datatype of the input value for the axis. This allows to define e.g. a type of curve, where the input value is finalized at the access point.
        self.inputVariableTypeRef: Optional[RefType] = None

        # this specifies the properties of a generic axis if applicable.
        self.swAxisGeneric: Optional[SwAxisGeneric] = None

        # Maximum number of base points contained in the axis of a map or curve.
        self.swMaxAxisPoints: Optional[Integer] = None

        # Minimum number of base points contained in the axis of a map or curve.
        self.swMinAxisPoints: Optional[Integer] = None

        # Refers to input variables of the axis. It is possible to specify more than one variable. Here the following is valid: • The variable with the highest priority shall be given first. It is used in the generation of the code and is also displayed first in the application system. • All variables referenced shall be of the same physical nature. This is usually detected in that the conversion formulae affected refer back to the same SI-units. In AUTOSAR this ensured by the constraint, that the referenced input variables shall use a type compatible to "inputVariableType". • This multiple referencing allows a base point distribution for more than one input variable to be used. One example of this are the temperature curves which can depend both on the induction air temperature and the engine temperature. These variables can be displayed simultaneously by MCD systems (adjustment systems), enabling operating points to be shown in the curves.
        self.swVariableRefs: List[SwVariableRefProxy] = []

        # This represents the physical unit of the input value of the axis. It is provided to support the case that the particular input variable is not yet known.
        self.unitRef: Optional[RefType] = None

    def getCompuMethodRef(self) -> Optional[RefType]:
        """This is the compuMethod which is expected for the axis. It is used in early stages if the particular input-value is not yet available."""
        return self.compuMethodRef

    def setCompuMethodRef(self, value: Optional[RefType]) -> "SwAxisIndividual":
        """This is the compuMethod which is expected for the axis. It is used in early stages if the particular input-value is not yet available. A None value is a no-op and does not overwrite an existing compuMethodRef."""
        if value is not None:
            self.compuMethodRef = value
        return self

    def getDataConstrRef(self) -> Optional[RefType]:
        """Refers to constraints, e.g. for plausibility checks."""
        return self.dataConstrRef

    def setDataConstrRef(self, value: Optional[RefType]) -> "SwAxisIndividual":
        """Refers to constraints, e.g. for plausibility checks. A None value is a no-op and does not overwrite an existing dataConstrRef."""
        if value is not None:
            self.dataConstrRef = value
        return self

    def getInputVariableTypeRef(self) -> Optional[RefType]:
        """This is the datatype of the input value for the axis. This allows to define e.g. a type of curve, where the input value is finalized at the access point."""
        return self.inputVariableTypeRef

    def setInputVariableTypeRef(self, value: Optional[RefType]) -> "SwAxisIndividual":
        """This is the datatype of the input value for the axis. This allows to define e.g. a type of curve, where the input value is finalized at the access point. A None value is a no-op and does not overwrite an existing inputVariableTypeRef."""
        if value is not None:
            self.inputVariableTypeRef = value
        return self

    def getSwAxisGeneric(self) -> Optional[SwAxisGeneric]:
        """this specifies the properties of a generic axis if applicable."""
        return self.swAxisGeneric

    def setSwAxisGeneric(self, value: Optional[SwAxisGeneric]) -> "SwAxisIndividual":
        """this specifies the properties of a generic axis if applicable. A None value is a no-op and does not overwrite an existing swAxisGeneric."""
        if value is not None:
            self.swAxisGeneric = value
        return self

    def getSwMaxAxisPoints(self) -> Optional[Integer]:
        """Maximum number of base points contained in the axis of a map or curve."""
        return self.swMaxAxisPoints

    def setSwMaxAxisPoints(self, value: Optional[Integer]) -> "SwAxisIndividual":
        """Maximum number of base points contained in the axis of a map or curve. A None value is a no-op and does not overwrite an existing swMaxAxisPoints."""
        if value is not None:
            self.swMaxAxisPoints = value
        return self

    def getSwMinAxisPoints(self) -> Optional[Integer]:
        """Minimum number of base points contained in the axis of a map or curve."""
        return self.swMinAxisPoints

    def setSwMinAxisPoints(self, value: Optional[Integer]) -> "SwAxisIndividual":
        """Minimum number of base points contained in the axis of a map or curve. A None value is a no-op and does not overwrite an existing swMinAxisPoints."""
        if value is not None:
            self.swMinAxisPoints = value
        return self

    def getSwVariableRefs(self) -> List[SwVariableRefProxy]:
        """Refers to input variables of the axis. It is possible to specify more than one variable. Here the following is valid: • The variable with the highest priority shall be given first. It is used in the generation of the code and is also displayed first in the application system. • All variables referenced shall be of the same physical nature. This is usually detected in that the conversion formulae affected refer back to the same SI-units. In AUTOSAR this ensured by the constraint, that the referenced input variables shall use a type compatible to \"inputVariableType\". • This multiple referencing allows a base point distribution for more than one input variable to be used. One example of this are the temperature curves which can depend both on the induction air temperature and the engine temperature. These variables can be displayed simultaneously by MCD systems (adjustment systems), enabling operating points to be shown in the curves."""
        return self.swVariableRefs

    def addSwVariableRef(self, value: Optional[SwVariableRefProxy]) -> "SwAxisIndividual":
        """Refers to input variables of the axis. It is possible to specify more than one variable. A None value is a no-op and is not appended to swVariableRefs."""
        if value is not None:
            self.swVariableRefs.append(value)
        return self

    def getUnitRef(self) -> Optional[RefType]:
        """This represents the physical unit of the input value of the axis. It is provided to support the case that the particular input variable is not yet known."""
        return self.unitRef

    def setUnitRef(self, value: Optional[RefType]) -> "SwAxisIndividual":
        """This represents the physical unit of the input value of the axis. It is provided to support the case that the particular input variable is not yet known. A None value is a no-op and does not overwrite an existing unitRef."""
        if value is not None:
            self.unitRef = value
        return self


class SwGenericAxisParamType(Identifiable):
    """
    This meta-class describes a generic axis parameter type, namely: • Plausibility checks can be specified via dataConstr. • Textual description (desc), as a formal description is not of any use, due to the large variety of possibilities. • If this parameter contains structures, these can be simulated through the recursive use of SwGeneric AxisParamTypes.
    """

    # SwGenericAxisParamType method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.54, p.356
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getDataConstrRef [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDataConstrRef [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent, short_name: str):
        super().__init__(parent, short_name)

        # This reference denoted data constraints applicable to the generic axis parameter.
        self.dataConstrRef: Optional[RefType] = None

    def getDataConstrRef(self) -> Optional[RefType]:
        """This reference denoted data constraints applicable to the generic axis parameter."""
        return self.dataConstrRef

    def setDataConstrRef(self, value: Optional[RefType]) -> "SwGenericAxisParamType":
        """This reference denoted data constraints applicable to the generic axis parameter. A None value is a no-op and does not overwrite an existing dataConstrRef."""
        if value is not None:
            self.dataConstrRef = value
        return self


class SwAxisGrouped(SwCalprmAxisTypeProps):
    """
    An SwAxisGrouped is an axis which is shared between multiple calibration parameters.
    """

    # SwAxisGrouped method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.55, p.357
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getSharedAxisTypeRef    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSharedAxisTypeRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSwAxisIndex          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSwAxisIndex          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSwCalprmRef          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSwCalprmRef          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # This is the datatype of the calibration parameter providing the shared axis.
        self.sharedAxisTypeRef: Optional[RefType] = None

        # Describes which axis of the referenced calibration parameter provides the values for the group axis. The index satisfies the following convention: • 0 = value axis. in this case, the interpolation result of the referenced parameter is used as a base point index. • The index should only be specified if the parameter under swCalprm contains more than one axis. It is standard practice for the axis index of parameters with more than one axis, to be set to 1, if data has not been assigned to swAxisIndex.
        self.swAxisIndex: Optional[AxisIndexType] = None

        # This property specifies the calibration parameter which serves as the input axis. In AUTOSAR, the type of the referenced Calibration parameter shall be compatible to the type specified by sharedAxisType. Please note that the multiplicity of this aggregation cannot be set to 0..1 based on the non-mainstream schema generation instructions defined at the aggregation. However, the multiplicity has to be factually considered 0..1 (i.e. a SwAxisGrouped that does not aggregate the role swCalprmRef is still valid according to the XML schema, depending on the use case documented in [constr_1015]).
        self.swCalprmRef: Optional[SwCalprmRefProxy] = None

    def getSharedAxisTypeRef(self) -> Optional[RefType]:
        """This is the datatype of the calibration parameter providing the shared axis."""
        return self.sharedAxisTypeRef

    def setSharedAxisTypeRef(self, value: Optional[RefType]) -> "SwAxisGrouped":
        """This is the datatype of the calibration parameter providing the shared axis. A None value is a no-op and does not overwrite an existing sharedAxisTypeRef."""
        if value is not None:
            self.sharedAxisTypeRef = value
        return self

    def getSwAxisIndex(self) -> Optional[AxisIndexType]:
        """Describes which axis of the referenced calibration parameter provides the values for the group axis. The index satisfies the following convention: • 0 = value axis. in this case, the interpolation result of the referenced parameter is used as a base point index. • The index should only be specified if the parameter under swCalprm contains more than one axis. It is standard practice for the axis index of parameters with more than one axis, to be set to 1, if data has not been assigned to swAxisIndex."""
        return self.swAxisIndex

    def setSwAxisIndex(self, value: Optional[AxisIndexType]) -> "SwAxisGrouped":
        """Describes which axis of the referenced calibration parameter provides the values for the group axis. The index satisfies the following convention: • 0 = value axis. in this case, the interpolation result of the referenced parameter is used as a base point index. • The index should only be specified if the parameter under swCalprm contains more than one axis. It is standard practice for the axis index of parameters with more than one axis, to be set to 1, if data has not been assigned to swAxisIndex. A None value is a no-op and does not overwrite an existing swAxisIndex."""
        if value is not None:
            self.swAxisIndex = value
        return self

    def getSwCalprmRef(self) -> Optional[SwCalprmRefProxy]:
        """This property specifies the calibration parameter which serves as the input axis. In AUTOSAR, the type of the referenced Calibration parameter shall be compatible to the type specified by sharedAxisType. Please note that the multiplicity of this aggregation cannot be set to 0..1 based on the non-mainstream schema generation instructions defined at the aggregation. However, the multiplicity has to be factually considered 0..1 (i.e. a SwAxisGrouped that does not aggregate the role swCalprmRef is still valid according to the XML schema, depending on the use case documented in [constr_1015])."""
        return self.swCalprmRef

    def setSwCalprmRef(self, value: Optional[SwCalprmRefProxy]) -> "SwAxisGrouped":
        """This property specifies the calibration parameter which serves as the input axis. In AUTOSAR, the type of the referenced Calibration parameter shall be compatible to the type specified by sharedAxisType. Please note that the multiplicity of this aggregation cannot be set to 0..1 based on the non-mainstream schema generation instructions defined at the aggregation. However, the multiplicity has to be factually considered 0..1 (i.e. a SwAxisGrouped that does not aggregate the role swCalprmRef is still valid according to the XML schema, depending on the use case documented in [constr_1015]). A None value is a no-op and does not overwrite an existing swCalprmRef."""
        if value is not None:
            self.swCalprmRef = value
        return self

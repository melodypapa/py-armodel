"""
This module contains application attribute classes for AUTOSAR software components.
"""

from typing import Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime import MultidimensionalTime
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum, Boolean, Float, RefType
from armodel.models.M2.MSR.Documentation.Annotation import GeneralAnnotation


class DataLimitKindEnum(AREnum):
    """
    Indicates whether the data element carries a minimum or maximum value, thereby limiting the current range of another value.
    """

    # DataLimitKindEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.45, p.154 (R23-11)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # Limitation to maximum value Tags: atp.EnumerationLiteralIndex=0
    MAX = "max"

    # Limitation to minimum value Tags: atp.EnumerationLiteralIndex=1
    MIN = "min"

    # No limitation applicable Tags: atp.EnumerationLiteralIndex=2
    NONE = "none"

    def __init__(self):
        super().__init__(
            (
                DataLimitKindEnum.MAX,
                DataLimitKindEnum.MIN,
                DataLimitKindEnum.NONE,
            )
        )


class FilterDebouncingEnum(AREnum):
    """
    This enumeration defines possible values for the filter debouncing strategy.
    """

    # FilterDebouncingEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.48, p.157 (R23-11)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # The signal is a mean value Tags: atp.EnumerationLiteralIndex=0
    DEBOUNCE_DATA = "debounceData"

    # Means that no modification of the signal has been applied. This is the default value Tags: atp.EnumerationLiteralIndex=1
    RAW_DATA = "rawData"

    # The signal is delivered by a GET operation after a certain amount of time Tags: atp.EnumerationLiteralIndex=2
    WAIT_TIME_DATE = "waitTimeDate"

    def __init__(self):
        super().__init__(
            (
                FilterDebouncingEnum.DEBOUNCE_DATA,
                FilterDebouncingEnum.RAW_DATA,
                FilterDebouncingEnum.WAIT_TIME_DATE,
            )
        )


class ProcessingKindEnum(AREnum):
    """
    Kind of processing which has been applied to a data element.
    """

    # ProcessingKindEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.44, p.153 (R23-11)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # Indicates that a raw signal has been manipulated by some application software components by using filters. Tags: atp.EnumerationLiteralIndex=0
    FILTERED = "filtered"

    # Indicates that none of the other option apply. Tags: atp.EnumerationLiteralIndex=1
    NONE = "none"

    # Specifies that a signal is taken directly from the basic software modules, i.e. from the ECU abstraction layer. It indicates to a developer that the control algorithm in the software has to provide filters. Tags: atp.EnumerationLiteralIndex=2
    RAW = "raw"

    def __init__(self):
        super().__init__(
            (
                ProcessingKindEnum.FILTERED,
                ProcessingKindEnum.NONE,
                ProcessingKindEnum.RAW,
            )
        )


class PulseTestEnum(AREnum):
    """
    This element indicates to the connected Actuator Software component whether the data-element can be used to generate pulse test sequences using the IoHwAbstraction layer
    """

    # PulseTestEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.49, p.157 (R23-11)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # Disables the pulse test Tags: atp.EnumerationLiteralIndex=0
    DISABLE = "disable"

    # Enables the pulse test Tags: atp.EnumerationLiteralIndex=1
    ENABLE = "enable"

    def __init__(self):
        super().__init__(
            (
                PulseTestEnum.DISABLE,
                PulseTestEnum.ENABLE,
            )
        )


class SignalFanEnum(AREnum):
    """
    Signal Fan inside the Composition Component Type.
    """

    # SignalFanEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.55, p.162
    # Spec verified: R23-11
    # [x] __init__                     [x] impl  [x] docstring  [ ] test

    # The connections internally in the CompositionSwComponentType via DelegationSwConnectors and AssemblySwConnectors are defined in a way that at least one data element present in the S/R interface or one ClientServerOperation in the C/S interface of the outer PortPrototype is involved in a 1:n or n:1 communication pattern. Tags: atp.EnumerationLiteralIndex=0
    NFOLD = "nfold"

    # The connections internally in the CompositionSwComponentType via DelegationSwConnectors and AssemblySwConnectors are defined in a way that each VariableDataPrototype present in the S/R interface or ClientServerOperation in the C/S interface of the outer PortPrototype is involved in a 1:1 communication pattern only. Tags: atp.EnumerationLiteralIndex=1
    SINGLE = "single"

    def __init__(self):
        super().__init__(
            (
                SignalFanEnum.NFOLD,
                SignalFanEnum.SINGLE,
            )
        )


class SenderReceiverAnnotation(GeneralAnnotation):
    """
    Annotation of the data elements in a port that realizes a sender/receiver interface.
    """

    # SenderReceiverAnnotation method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.41, p.152 (R23-11)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__             [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getComputed          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setComputed          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDataElementRef    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDataElementRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getLimitKind         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setLimitKind         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getProcessingKind    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setProcessingKind    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        if type(self) is SenderReceiverAnnotation:
            raise TypeError("SenderReceiverAnnotation is an abstract class.")

        super().__init__()

        # Flag whether this data element was not measured directly but instead was calculated from possibly several other measured or calculated values.
        self.computed: Optional[Boolean] = None

        # The instance of VariableDataPrototype annotated.
        self.dataElementRef: Optional[RefType] = None

        # This min or max has not to be mismatched with the min- and max for data-value in a compu-method. For example, this annotation shows when the result of the calculation performed in a RunnableEntity owned by one AtomicSwComponentType is transmitted to another AtomicSwComponentType whose RunnableEntity will use this value as a limit, e.g. the max.power which can be used by that software-component, or the current min. slip.
        self.limitKind: Optional[DataLimitKindEnum] = None

        # This attribute controls how data is processed according to the possible values of ProcessingKindEnum.
        self.processingKind: Optional[ProcessingKindEnum] = None

    def getComputed(self) -> Optional[Boolean]:
        """
        Flag whether this data element was not measured directly but instead was calculated from possibly several other measured or calculated values.
        """
        return self.computed

    def setComputed(self, value: Optional[Boolean]) -> "SenderReceiverAnnotation":
        """
        Flag whether this data element was not measured directly but instead was calculated from possibly several other measured or calculated values.
        A None value is a no-op and does not overwrite an existing computed.
        """
        if value is not None:
            self.computed = value
        return self

    def getDataElementRef(self) -> Optional[RefType]:
        """
        The instance of VariableDataPrototype annotated.
        """
        return self.dataElementRef

    def setDataElementRef(self, value: Optional[RefType]) -> "SenderReceiverAnnotation":
        """
        The instance of VariableDataPrototype annotated.
        A None value is a no-op and does not overwrite an existing dataElementRef.
        """
        if value is not None:
            self.dataElementRef = value
        return self

    def getLimitKind(self) -> Optional[DataLimitKindEnum]:
        """
        This min or max has not to be mismatched with the min- and max for data-value in a compu-method. For example, this annotation shows when the result of the calculation performed in a RunnableEntity owned by one AtomicSwComponentType is transmitted to another AtomicSwComponentType whose RunnableEntity will use this value as a limit, e.g. the max.power which can be used by that software-component, or the current min. slip.
        """
        return self.limitKind

    def setLimitKind(self, value: Optional[DataLimitKindEnum]) -> "SenderReceiverAnnotation":
        """
        This min or max has not to be mismatched with the min- and max for data-value in a compu-method. For example, this annotation shows when the result of the calculation performed in a RunnableEntity owned by one AtomicSwComponentType is transmitted to another AtomicSwComponentType whose RunnableEntity will use this value as a limit, e.g. the max.power which can be used by that software-component, or the current min. slip.
        A None value is a no-op and does not overwrite an existing limitKind.
        """
        if value is not None:
            self.limitKind = value
        return self

    def getProcessingKind(self) -> Optional[ProcessingKindEnum]:
        """
        This attribute controls how data is processed according to the possible values of ProcessingKindEnum.
        """
        return self.processingKind

    def setProcessingKind(self, value: Optional[ProcessingKindEnum]) -> "SenderReceiverAnnotation":
        """
        This attribute controls how data is processed according to the possible values of ProcessingKindEnum.
        A None value is a no-op and does not overwrite an existing processingKind.
        """
        if value is not None:
            self.processingKind = value
        return self


class ClientServerAnnotation(GeneralAnnotation):
    """
    Annotation to a port regarding a certain Operation.
    """

    # ClientServerAnnotation method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.46, p.155 (R23-11)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getOperationRef   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setOperationRef   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # This represents the ClientServerOperation that the Client ServerAnnotation corresponds to.
        self.operationRef: Optional[RefType] = None

    def getOperationRef(self) -> Optional[RefType]:
        """
        This represents the ClientServerOperation that the Client ServerAnnotation corresponds to.
        """
        return self.operationRef

    def setOperationRef(self, value: Optional[RefType]) -> "ClientServerAnnotation":
        """
        This represents the ClientServerOperation that the Client ServerAnnotation corresponds to.
        A None value is a no-op and does not overwrite an existing operationRef.
        """
        if value is not None:
            self.operationRef = value
        return self


class IoHwAbstractionServerAnnotation(GeneralAnnotation):
    """
    The IoHwAbstractionServerAnnotation will only be used from a sensor- or an actuator component while interacting with the IoHwAbstraction layer. Note that the "server" in the name of this meta-class is not meant to restrict the usage to ClientServer Interfaces.
    """

    # IoHwAbstractionServerAnnotation method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.47, p.157 (R23-11)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getAge                    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setAge                    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getArgumentRef            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setArgumentRef            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getBswResolution          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setBswResolution          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDataElementRef         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setDataElementRef         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getFailureMonitoringRef   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setFailureMonitoringRef   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getFilteringDebouncing    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setFilteringDebouncing    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPulseTest              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setPulseTest              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTriggerRef             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTriggerRef             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # In case of a SET operation, the age will be interpreted as Delay while in a GET operation (input) it specifies the Lifetime of the signal within the IoHwAbstraction Layer
        self.age: Optional[MultidimensionalTime] = None

        # Reference to the corresponding ArgumentDataPrototype.
        self.argumentRef: Optional[RefType] = None

        # This value is determined by an appropriate combination of the range, the unit as well as the data-elements type, i.e. (ecuSignalRange.upperLimit-ecuSignalRange.lower Limit) / (2ˆdatatypelength - 1)
        self.bswResolution: Optional[Float] = None

        # Reference to the corresponding VariableDataPrototype.
        self.dataElementRef: Optional[RefType] = None

        # This is only applicable in SET operations. If it is enabled, the IoHwAbstraction layer will monitor the result of the operation and issue an diagnostic signal. This means especially, that an additional client-server port has to be created. Tools can use this information to cross-check whether for each data-element in a SET operation with FailureMonitoring enabled an additional port is created The referenced port monitors a failure in the to be monitored VariableDataPrototype of the IoHwAbstraction layer. The referenced port has to be another port of the same Actuator or Sensor Component.
        self.failureMonitoringRef: Optional[RefType] = None

        # This attribute is used to indicate what kind of filtering/ debouncing has been put to the signal in the IoHw Abstraction layer. rawData means that no modification of the signal has been applied. This is the default value debounceData means that the signal is a mean value waitTimeData means that the signal is delivered by a GET operation after a certain amount of time
        self.filteringDebouncing: Optional[FilterDebouncingEnum] = None

        # This attribute indicates to the connected SensorActuator SwComponentType whether the VariableDataPrototype can be used to generate pulse test sequences using the IoHwAbstraction layer
        self.pulseTest: Optional[PulseTestEnum] = None

        # Reference to the corresponding Trigger.
        self.triggerRef: Optional[RefType] = None

    def getAge(self) -> Optional[MultidimensionalTime]:
        """
        In case of a SET operation, the age will be interpreted as Delay while in a GET operation (input) it specifies the Lifetime of the signal within the IoHwAbstraction Layer
        """
        return self.age

    def setAge(self, value: Optional[MultidimensionalTime]) -> "IoHwAbstractionServerAnnotation":
        """
        In case of a SET operation, the age will be interpreted as Delay while in a GET operation (input) it specifies the Lifetime of the signal within the IoHwAbstraction Layer
        A None value is a no-op and does not overwrite an existing age.
        """
        if value is not None:
            self.age = value
        return self

    def getArgumentRef(self) -> Optional[RefType]:
        """
        Reference to the corresponding ArgumentDataPrototype.
        """
        return self.argumentRef

    def setArgumentRef(self, value: Optional[RefType]) -> "IoHwAbstractionServerAnnotation":
        """
        Reference to the corresponding ArgumentDataPrototype.
        A None value is a no-op and does not overwrite an existing argumentRef.
        """
        if value is not None:
            self.argumentRef = value
        return self

    def getBswResolution(self) -> Optional[Float]:
        """
        This value is determined by an appropriate combination of the range, the unit as well as the data-elements type, i.e. (ecuSignalRange.upperLimit-ecuSignalRange.lower Limit) / (2ˆdatatypelength - 1)
        """
        return self.bswResolution

    def setBswResolution(self, value: Optional[Float]) -> "IoHwAbstractionServerAnnotation":
        """
        This value is determined by an appropriate combination of the range, the unit as well as the data-elements type, i.e. (ecuSignalRange.upperLimit-ecuSignalRange.lower Limit) / (2ˆdatatypelength - 1)
        A None value is a no-op and does not overwrite an existing bswResolution.
        """
        if value is not None:
            self.bswResolution = value
        return self

    def getDataElementRef(self) -> Optional[RefType]:
        """
        Reference to the corresponding VariableDataPrototype.
        """
        return self.dataElementRef

    def setDataElementRef(self, value: Optional[RefType]) -> "IoHwAbstractionServerAnnotation":
        """
        Reference to the corresponding VariableDataPrototype.
        A None value is a no-op and does not overwrite an existing dataElementRef.
        """
        if value is not None:
            self.dataElementRef = value
        return self

    def getFailureMonitoringRef(self) -> Optional[RefType]:
        """
        This is only applicable in SET operations. If it is enabled, the IoHwAbstraction layer will monitor the result of the operation and issue an diagnostic signal. This means especially, that an additional client-server port has to be created. Tools can use this information to cross-check whether for each data-element in a SET operation with FailureMonitoring enabled an additional port is created The referenced port monitors a failure in the to be monitored VariableDataPrototype of the IoHwAbstraction layer. The referenced port has to be another port of the same Actuator or Sensor Component.
        """
        return self.failureMonitoringRef

    def setFailureMonitoringRef(self, value: Optional[RefType]) -> "IoHwAbstractionServerAnnotation":
        """
        This is only applicable in SET operations. If it is enabled, the IoHwAbstraction layer will monitor the result of the operation and issue an diagnostic signal. This means especially, that an additional client-server port has to be created. Tools can use this information to cross-check whether for each data-element in a SET operation with FailureMonitoring enabled an additional port is created The referenced port monitors a failure in the to be monitored VariableDataPrototype of the IoHwAbstraction layer. The referenced port has to be another port of the same Actuator or Sensor Component.
        A None value is a no-op and does not overwrite an existing failureMonitoringRef.
        """
        if value is not None:
            self.failureMonitoringRef = value
        return self

    def getFilteringDebouncing(self) -> Optional[FilterDebouncingEnum]:
        """
        This attribute is used to indicate what kind of filtering/ debouncing has been put to the signal in the IoHw Abstraction layer. rawData means that no modification of the signal has been applied. This is the default value debounceData means that the signal is a mean value waitTimeData means that the signal is delivered by a GET operation after a certain amount of time
        """
        return self.filteringDebouncing

    def setFilteringDebouncing(self, value: Optional[FilterDebouncingEnum]) -> "IoHwAbstractionServerAnnotation":
        """
        This attribute is used to indicate what kind of filtering/ debouncing has been put to the signal in the IoHw Abstraction layer. rawData means that no modification of the signal has been applied. This is the default value debounceData means that the signal is a mean value waitTimeData means that the signal is delivered by a GET operation after a certain amount of time
        A None value is a no-op and does not overwrite an existing filteringDebouncing.
        """
        if value is not None:
            self.filteringDebouncing = value
        return self

    def getPulseTest(self) -> Optional[PulseTestEnum]:
        """
        This attribute indicates to the connected SensorActuator SwComponentType whether the VariableDataPrototype can be used to generate pulse test sequences using the IoHwAbstraction layer
        """
        return self.pulseTest

    def setPulseTest(self, value: Optional[PulseTestEnum]) -> "IoHwAbstractionServerAnnotation":
        """
        This attribute indicates to the connected SensorActuator SwComponentType whether the VariableDataPrototype can be used to generate pulse test sequences using the IoHwAbstraction layer
        A None value is a no-op and does not overwrite an existing pulseTest.
        """
        if value is not None:
            self.pulseTest = value
        return self

    def getTriggerRef(self) -> Optional[RefType]:
        """
        Reference to the corresponding Trigger.
        """
        return self.triggerRef

    def setTriggerRef(self, value: Optional[RefType]) -> "IoHwAbstractionServerAnnotation":
        """
        Reference to the corresponding Trigger.
        A None value is a no-op and does not overwrite an existing triggerRef.
        """
        if value is not None:
            self.triggerRef = value
        return self


class ModePortAnnotation(GeneralAnnotation):
    """
    Annotation to a port used for calibration regarding a certain ModeDeclarationGroupPrototype.
    """

    # ModePortAnnotation method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.51, p.159 (R23-11)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getModeGroupRef   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setModeGroupRef   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # The instance of annotated ModeDeclarationGroup Prototype.
        self.modeGroupRef: Optional[RefType] = None

    def getModeGroupRef(self) -> Optional[RefType]:
        """
        The instance of annotated ModeDeclarationGroup Prototype.
        """
        return self.modeGroupRef

    def setModeGroupRef(self, value: Optional[RefType]) -> "ModePortAnnotation":
        """
        The instance of annotated ModeDeclarationGroup Prototype.
        A None value is a no-op and does not overwrite an existing modeGroupRef.
        """
        if value is not None:
            self.modeGroupRef = value
        return self


class NvDataPortAnnotation(GeneralAnnotation):
    """
    Annotation to a port regarding a certain VariableDataPrototype.
    """

    # NvDataPortAnnotation method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.53, p.160 (R23-11)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__         [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getVariableRef   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setVariableRef   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # The instance of nv data annotated.
        self.variableRef: Optional[RefType] = None

    def getVariableRef(self) -> Optional[RefType]:
        """
        The instance of nv data annotated.
        """
        return self.variableRef

    def setVariableRef(self, value: Optional[RefType]) -> "NvDataPortAnnotation":
        """
        The instance of nv data annotated.
        A None value is a no-op and does not overwrite an existing variableRef.
        """
        if value is not None:
            self.variableRef = value
        return self


class ParameterPortAnnotation(GeneralAnnotation):
    """
    Annotation to a port used for calibration regarding a certain ParameterDataPrototype.
    """

    # ParameterPortAnnotation method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.50, pp.158-159 (R23-11)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getParameterRef   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setParameterRef   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # The instance of annotated ParameterDataPrototype.
        self.parameterRef: Optional[RefType] = None

    def getParameterRef(self) -> Optional[RefType]:
        """
        The instance of annotated ParameterDataPrototype.
        """
        return self.parameterRef

    def setParameterRef(self, value: Optional[RefType]) -> "ParameterPortAnnotation":
        """
        The instance of annotated ParameterDataPrototype.
        A None value is a no-op and does not overwrite an existing parameterRef.
        """
        if value is not None:
            self.parameterRef = value
        return self


class TriggerPortAnnotation(GeneralAnnotation):
    """
    Annotation to a port used for calibration regarding a certain Trigger.
    """

    # TriggerPortAnnotation method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.52, p.160 (R23-11)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__         [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getTriggerRef    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTriggerRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # The instance of annotated trigger.
        self.triggerRef: Optional[RefType] = None

    def getTriggerRef(self) -> Optional[RefType]:
        """
        The instance of annotated trigger.
        """
        return self.triggerRef

    def setTriggerRef(self, value: Optional[RefType]) -> "TriggerPortAnnotation":
        """
        The instance of annotated trigger.
        A None value is a no-op and does not overwrite an existing triggerRef.
        """
        if value is not None:
            self.triggerRef = value
        return self


class DelegatedPortAnnotation(GeneralAnnotation):
    """
    Annotation to a "delegated port" to specify the Signal Fan In or Signal Fan Out inside the CompositionSw ComponentType.
    """

    # DelegatedPortAnnotation method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.54, p.162
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getSignalFan                [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] setSignalFan                [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11

    def __init__(self):
        super().__init__()

        # Specifies the Signal Fan In or Signal Fan Out inside the Composition Type.
        self.signalFan: Optional[SignalFanEnum] = None

    def getSignalFan(self) -> Optional[SignalFanEnum]:
        """
        Specifies the Signal Fan In or Signal Fan Out inside the Composition Type.
        """
        return self.signalFan

    def setSignalFan(self, value: Optional[SignalFanEnum]) -> "DelegatedPortAnnotation":
        """
        Specifies the Signal Fan In or Signal Fan Out inside the Composition Type.
        A None value is a no-op and does not overwrite an existing signalFan.
        """
        if value is not None:
            self.signalFan = value
        return self


__all__ = [
    "SenderAnnotation",
    "ReceiverAnnotation",
    "DataLimitKindEnum",
    "FilterDebouncingEnum",
    "ProcessingKindEnum",
    "PulseTestEnum",
    "SignalFanEnum",
    "SenderReceiverAnnotation",
    "ClientServerAnnotation",
    "IoHwAbstractionServerAnnotation",
    "ModePortAnnotation",
    "NvDataPortAnnotation",
    "ParameterPortAnnotation",
    "TriggerPortAnnotation",
    "DelegatedPortAnnotation",
]


class ReceiverAnnotation(SenderReceiverAnnotation):
    """
    Annotation of a receiver port, specifying properties of data elements that don't affect communication or generation of the RTE. The given attributes are requirements on the required data.
    """

    # ReceiverAnnotation method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.43, p.153 (R23-11)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getSignalAge       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSignalAge       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # The maximum allowed age of the signal since it was originally read by a sensor. This is a requirement specified on the receiver side.
        self.signalAge: Optional[MultidimensionalTime] = None

    def getSignalAge(self) -> Optional[MultidimensionalTime]:
        """
        The maximum allowed age of the signal since it was originally read by a sensor. This is a requirement specified on the receiver side.
        """
        return self.signalAge

    def setSignalAge(self, value: Optional[MultidimensionalTime]) -> "ReceiverAnnotation":
        """
        The maximum allowed age of the signal since it was originally read by a sensor. This is a requirement specified on the receiver side.
        A None value is a no-op and does not overwrite an existing signalAge.
        """
        if value is not None:
            self.signalAge = value
        return self


class SenderAnnotation(SenderReceiverAnnotation):
    """
    Annotation of a sender port, specifying properties of data elements that don't affect communication or generation of the RTE.
    """

    # SenderAnnotation method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.42, p.153 (R23-11)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [ ] __init__  [ ] impl  [ ] docstring  [ ] test  [—] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

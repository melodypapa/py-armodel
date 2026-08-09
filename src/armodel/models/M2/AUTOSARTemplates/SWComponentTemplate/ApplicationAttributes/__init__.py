"""
This module contains application attribute classes for AUTOSAR software components.
"""

from typing import Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum, ARBoolean, RefType
from armodel.models.M2.MSR.Documentation.Annotation import GeneralAnnotation


class DataLimitKindEnum(AREnum):
    """
    Indicates whether the data element carries a minimum or maximum value, thereby limiting the current range of another value.
    """

    # DataLimitKindEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.45, p.153
    # Spec verified: R23-11
    # [x] __init__                     [x] impl  [x] docstring  [ ] test

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
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.48, p.157
    # Spec verified: R23-11
    # [x] __init__                     [x] impl  [x] docstring  [ ] test

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
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.44, p.153
    # Spec verified: R23-11
    # [x] __init__                     [x] impl  [x] docstring  [ ] test

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
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.49, p.157
    # Spec verified: R23-11
    # [x] __init__                     [x] impl  [x] docstring  [ ] test

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
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.41, p.152
    # Spec verified: R23-11
    # [x] __init__                  [x] impl  [x] docstring  [x] test
    # [x] getComputed               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setComputed               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getDataElementRef         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setDataElementRef         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getLimitKind              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setLimitKind              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getProcessingKind         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setProcessingKind         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # Flag whether this data element was not measured directly but instead was calculated from possibly several other measured or calculated values.
        self.computed: Optional[ARBoolean] = None

        # The instance of VariableDataPrototype annotated.
        self.dataElementRef: Optional[RefType] = None

        # This min or max has not to be mismatched with the min- and max for data-value in a compu-method.
        self.limitKind: Optional[DataLimitKindEnum] = None

        # This attribute controls how data is processed according to the possible values of ProcessingKindEnum.
        self.processingKind: Optional[ProcessingKindEnum] = None

    def getComputed(self) -> Optional[ARBoolean]:
        """
        Gets the flag whether this data element was not measured directly but instead was calculated from possibly several other measured or calculated values.

        Returns:
            ARBoolean flag, or None if not set
        """
        return self.computed

    def setComputed(self, value: Optional[ARBoolean]) -> "SenderReceiverAnnotation":
        """
        Sets the flag whether this data element was not measured directly but instead was calculated from possibly several other measured or calculated values.
        A None value is a no-op and does not overwrite an existing value.

        Args:
            value: The ARBoolean flag to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.computed = value
        return self

    def getDataElementRef(self) -> Optional[RefType]:
        """
        Gets the instance of VariableDataPrototype annotated.

        Returns:
            RefType referencing the VariableDataPrototype, or None if not set
        """
        return self.dataElementRef

    def setDataElementRef(self, value: Optional[RefType]) -> "SenderReceiverAnnotation":
        """
        Sets the instance of VariableDataPrototype annotated.
        A None value is a no-op and does not overwrite an existing reference.

        Args:
            value: The RefType to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.dataElementRef = value
        return self

    def getLimitKind(self) -> Optional[DataLimitKindEnum]:
        """
        Gets the limit kind of this data element annotation.

        Returns:
            DataLimitKindEnum, or None if not set
        """
        return self.limitKind

    def setLimitKind(self, value: Optional[DataLimitKindEnum]) -> "SenderReceiverAnnotation":
        """
        Sets the limit kind of this data element annotation.
        A None value is a no-op and does not overwrite an existing value.

        Args:
            value: The DataLimitKindEnum to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.limitKind = value
        return self

    def getProcessingKind(self) -> Optional[ProcessingKindEnum]:
        """
        Gets the processing kind of this data element annotation.

        Returns:
            ProcessingKindEnum, or None if not set
        """
        return self.processingKind

    def setProcessingKind(self, value: Optional[ProcessingKindEnum]) -> "SenderReceiverAnnotation":
        """
        Sets the processing kind of this data element annotation.
        A None value is a no-op and does not overwrite an existing value.

        Args:
            value: The ProcessingKindEnum to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.processingKind = value
        return self


class ClientServerAnnotation(GeneralAnnotation):
    """
    Annotation to a port regarding a certain Operation.
    """

    # ClientServerAnnotation method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.46, p.155
    # Spec verified: R23-11
    # [x] __init__                  [x] impl  [x] docstring  [x] test
    # [x] getOperationRef           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setOperationRef           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # This represents the ClientServerOperation that the ClientServerAnnotation corresponds to.
        self.operationRef: Optional[RefType] = None

    def getOperationRef(self) -> Optional[RefType]:
        """
        Gets the ClientServerOperation that the ClientServerAnnotation corresponds to.

        Returns:
            RefType referencing the ClientServerOperation, or None if not set
        """
        return self.operationRef

    def setOperationRef(self, value: Optional[RefType]) -> "ClientServerAnnotation":
        """
        Sets the ClientServerOperation that the ClientServerAnnotation corresponds to.
        A None value is a no-op and does not overwrite an existing reference.

        Args:
            value: The RefType to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.operationRef = value
        return self


class IoHwAbstractionServerAnnotation(GeneralAnnotation):
    """
    The IoHwAbstractionServerAnnotation will only be used from a sensor- or an actuator component while interacting with the IoHwAbstraction layer. Note that the 'server' in the name of this meta-class is not meant to restrict the usage to ClientServer Interfaces.
    """

    # IoHwAbstractionServerAnnotation method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.47, p.157
    # Spec verified: R23-11
    # [x] __init__                     [x] impl  [x] docstring  [x] test
    # [x] getFilteringDebouncing       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setFilteringDebouncing       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getPulseTest                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setPulseTest                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTriggerRef                [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTriggerRef                [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # This attribute is used to indicate what kind of filtering/debouncing has been put to the signal in the IoHwAbstraction layer.
        self.filteringDebouncing: Optional[FilterDebouncingEnum] = None

        # This attribute indicates to the connected SensorActuatorSwComponentType whether the VariableDataPrototype can be used to generate pulse test sequences using the IoHwAbstraction layer
        self.pulseTest: Optional[PulseTestEnum] = None

        # Reference to the corresponding Trigger.
        self.triggerRef: Optional[RefType] = None

    def getFilteringDebouncing(self) -> Optional[FilterDebouncingEnum]:
        """
        Gets the filtering/debouncing kind that has been put to the signal in the IoHwAbstraction layer.

        Returns:
            FilterDebouncingEnum, or None if not set
        """
        return self.filteringDebouncing

    def setFilteringDebouncing(self, value: Optional[FilterDebouncingEnum]) -> "IoHwAbstractionServerAnnotation":
        """
        Sets the filtering/debouncing kind that has been put to the signal in the IoHwAbstraction layer.
        A None value is a no-op and does not overwrite an existing value.

        Args:
            value: The FilterDebouncingEnum to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.filteringDebouncing = value
        return self

    def getPulseTest(self) -> Optional[PulseTestEnum]:
        """
        Gets the pulse test indication for the connected SensorActuatorSwComponentType.

        Returns:
            PulseTestEnum, or None if not set
        """
        return self.pulseTest

    def setPulseTest(self, value: Optional[PulseTestEnum]) -> "IoHwAbstractionServerAnnotation":
        """
        Sets the pulse test indication for the connected SensorActuatorSwComponentType.
        A None value is a no-op and does not overwrite an existing value.

        Args:
            value: The PulseTestEnum to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.pulseTest = value
        return self

    def getTriggerRef(self) -> Optional[RefType]:
        """
        Gets the reference to the corresponding Trigger.

        Returns:
            RefType referencing the Trigger, or None if not set
        """
        return self.triggerRef

    def setTriggerRef(self, value: Optional[RefType]) -> "IoHwAbstractionServerAnnotation":
        """
        Sets the reference to the corresponding Trigger.
        A None value is a no-op and does not overwrite an existing reference.

        Args:
            value: The RefType to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.triggerRef = value
        return self


class ModePortAnnotation(GeneralAnnotation):
    """
    Annotation to a port used for calibration regarding a certain ModeDeclarationGroupPrototype.
    """

    # ModePortAnnotation method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.51, p.159
    # Spec verified: R23-11
    # [x] __init__                  [x] impl  [x] docstring  [x] test
    # [x] getModeGroupRef           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setModeGroupRef           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # The instance of annotated ModeDeclarationGroupPrototype.
        self.modeGroupRef: Optional[RefType] = None

    def getModeGroupRef(self) -> Optional[RefType]:
        """
        Gets the instance of annotated ModeDeclarationGroupPrototype.

        Returns:
            RefType referencing the ModeDeclarationGroupPrototype, or None if not set
        """
        return self.modeGroupRef

    def setModeGroupRef(self, value: Optional[RefType]) -> "ModePortAnnotation":
        """
        Sets the instance of annotated ModeDeclarationGroupPrototype.
        A None value is a no-op and does not overwrite an existing reference.

        Args:
            value: The RefType to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.modeGroupRef = value
        return self


class NvDataPortAnnotation(GeneralAnnotation):
    """
    Annotation to a port regarding a certain VariableDataPrototype.
    """

    # NvDataPortAnnotation method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.53, p.160
    # Spec verified: R23-11
    # [x] __init__                  [x] impl  [x] docstring  [x] test
    # [x] getVariableRef            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setVariableRef            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # The instance of nv data annotated.
        self.variableRef: Optional[RefType] = None

    def getVariableRef(self) -> Optional[RefType]:
        """
        Gets the instance of nv data annotated.

        Returns:
            RefType referencing the VariableDataPrototype, or None if not set
        """
        return self.variableRef

    def setVariableRef(self, value: Optional[RefType]) -> "NvDataPortAnnotation":
        """
        Sets the instance of nv data annotated.
        A None value is a no-op and does not overwrite an existing reference.

        Args:
            value: The RefType to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.variableRef = value
        return self


class ParameterPortAnnotation(GeneralAnnotation):
    """
    Annotation to a port used for calibration regarding a certain ParameterDataPrototype.
    """

    # ParameterPortAnnotation method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.50, p.159
    # Spec verified: R23-11
    # [x] __init__                  [x] impl  [x] docstring  [x] test
    # [x] getParameterRef           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setParameterRef           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # The instance of annotated ParameterDataPrototype.
        self.parameterRef: Optional[RefType] = None

    def getParameterRef(self) -> Optional[RefType]:
        """
        Gets the instance of annotated ParameterDataPrototype.

        Returns:
            RefType referencing the ParameterDataPrototype, or None if not set
        """
        return self.parameterRef

    def setParameterRef(self, value: Optional[RefType]) -> "ParameterPortAnnotation":
        """
        Sets the instance of annotated ParameterDataPrototype.
        A None value is a no-op and does not overwrite an existing reference.

        Args:
            value: The RefType to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.parameterRef = value
        return self


class TriggerPortAnnotation(GeneralAnnotation):
    """
    Annotation to a port used for calibration regarding a certain Trigger.
    """

    # TriggerPortAnnotation method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.52, p.160
    # Spec verified: R23-11
    # [x] __init__                  [x] impl  [x] docstring  [x] test
    # [x] getTriggerRef             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTriggerRef             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # The instance of annotated trigger.
        self.triggerRef: Optional[RefType] = None

    def getTriggerRef(self) -> Optional[RefType]:
        """
        Gets the instance of annotated trigger.

        Returns:
            RefType referencing the Trigger, or None if not set
        """
        return self.triggerRef

    def setTriggerRef(self, value: Optional[RefType]) -> "TriggerPortAnnotation":
        """
        Sets the instance of annotated trigger.
        A None value is a no-op and does not overwrite an existing reference.

        Args:
            value: The RefType to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.triggerRef = value
        return self


class DelegatedPortAnnotation(GeneralAnnotation):
    """
    Annotation to a 'delegated port' to specify the Signal Fan In or Signal Fan Out inside the CompositionSwComponentType.
    """

    # DelegatedPortAnnotation method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.54, p.162
    # Spec verified: R23-11
    # [x] __init__                  [x] impl  [x] docstring  [x] test
    # [x] getSignalFan              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSignalFan              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # Specifies the Signal Fan In or Signal Fan Out of a delegated port.
        self.signalFan: Optional[SignalFanEnum] = None

    def getSignalFan(self) -> Optional[SignalFanEnum]:
        """
        Gets the Signal Fan In or Signal Fan Out of a delegated port.

        Returns:
            SignalFanEnum, or None if not set
        """
        return self.signalFan

    def setSignalFan(self, value: Optional[SignalFanEnum]) -> "DelegatedPortAnnotation":
        """
        Sets the Signal Fan In or Signal Fan Out of a delegated port.
        A None value is a no-op and does not overwrite an existing value.

        Args:
            value: The SignalFanEnum to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.signalFan = value
        return self


__all__ = [
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

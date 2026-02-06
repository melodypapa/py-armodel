"""
This module contains classes for representing AUTOSAR communication specifications
in the SWComponentTemplate module. It includes various communication specifications
for different types of port communication such as sender/receiver, client/server,
and mode switching communications, as well as non-volatile and parameter communications.
"""

from abc import ABC
from typing import List, Union

from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure import (
    ValueSpecification,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Describable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARBoolean,
    AREnum,
    ARNumerical,
    ARPositiveInteger,
    Boolean,
    PositiveInteger,
    RefType,
    TimeValue,
)
from armodel.v2.models.M2.MSR.DataDictionary.DataDefProperties import (
    SwDataDefProps,
)


class HandleInvalidEnum(AREnum):
    DONT_INVALIDATE = "dontInvalidate"
    EXTERNAL_REPLACEMENT = "externalReplacement"
    KEEP = "keep"
    REPLACE = "replace"

    def __init__(self) -> None:
        super().__init__((
            HandleInvalidEnum.DONT_INVALIDATE,
            HandleInvalidEnum.EXTERNAL_REPLACEMENT,
            HandleInvalidEnum.KEEP,
            HandleInvalidEnum.REPLACE
        ))


class PPortComSpec(ARObject, ABC):
    """
        Communication attributes of a provided PortPrototype. This class will contain attributes that are valid for
        all kinds of provide ports, independent of client-server or sender-receiver communication patterns.

        Abstract Class

        Package: M2::AUTOSARTemplates::SWComponentTemplate::Communication
        Base: ARObject
    """

    def __init__(self) -> None:
        if type(self) is PPortComSpec:
            raise TypeError("PPortComSpec is an abstract class.")
        super().__init__()


class RPortComSpec(ARObject, ABC):
    """
        Communication attributes of a provided PortPrototype. This class will contain attributes that are valid for
        all kinds of provide ports, independent of client-server or sender-receiver communication patterns.

        Abstract Class

        Package: M2::AUTOSARTemplates::SWComponentTemplate::Communication
        Base: ARObject
    """

    def __init__(self) -> None:
        if type(self) is RPortComSpec:
            raise TypeError("RPortComSpec is an abstract class.")

        super().__init__()


class CompositeNetworkRepresentation(ARObject):

    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    def __init__(self) -> None:
        super().__init__()

        self.leafElementIRef = None
        self.networkRepresentation: Union[Union[SwDataDefProps, None] , None] = None

    def getLeafElementIRef(self):
        return self.leafElementIRef

    def setLeafElementIRef(self, value):
        self.leafElementIRef = value
        return self

    def getNetworkRepresentation(self):
        return self.networkRepresentation

    def setNetworkRepresentation(self, value):
        self.networkRepresentation = value
        return self


class TransmissionAcknowledgementRequest(ARObject):

    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    def __init__(self) -> None:
        super().__init__()

        self.timeout: float = None


class SenderComSpec(PPortComSpec, ABC):
    def __init__(self) -> None:
        if type(self) is SenderComSpec:
            raise TypeError("SenderComSpec is an abstract class.")

        super().__init__()

        self.compositeNetworkRepresentations: List[CompositeNetworkRepresentation] = []
        self.dataElementRef: Union[Union[RefType, None] , None] = None
        self.networkRepresentation: Union[Union[SwDataDefProps, None] , None] = None
        self.handleOutOfRange: str = None
        self.transmissionAcknowledge: Union[Union[TransmissionAcknowledgementRequest, None] , None] = None
        self.usesEndToEndProtection: Union[Union[ARBoolean, None] , None] = None

    def addCompositeNetworkRepresentation(self, representation: CompositeNetworkRepresentation):
        self.compositeNetworkRepresentations.append(representation)

    def getCompositeNetworkRepresentations(self) -> List[CompositeNetworkRepresentation]:
        return self.compositeNetworkRepresentations

    def getDataElementRef(self):
        return self.dataElementRef

    def setDataElementRef(self, value):
        self.dataElementRef = value
        return self

    def getNetworkRepresentation(self):
        return self.networkRepresentation

    def setNetworkRepresentation(self, value):
        self.networkRepresentation = value
        return self

    def getHandleOutOfRange(self):
        return self.handleOutOfRange

    def setHandleOutOfRange(self, value):
        self.handleOutOfRange = value
        return self

    def getTransmissionAcknowledge(self):
        return self.transmissionAcknowledge

    def setTransmissionAcknowledge(self, value):
        self.transmissionAcknowledge = value
        return self

    def getUsesEndToEndProtection(self):
        return self.usesEndToEndProtection

    def setUsesEndToEndProtection(self, value):
        self.usesEndToEndProtection = value
        return self


class QueuedSenderComSpec(SenderComSpec):
    def __init__(self) -> None:
        super().__init__()


class NonqueuedSenderComSpec(SenderComSpec):
    def __init__(self) -> None:
        super().__init__()

        self.initValue: Union[Union[ValueSpecification, None] , None] = None

    def getInitValue(self):
        return self.initValue

    def setInitValue(self, value):
        self.initValue = value
        return self


class ClientComSpec(RPortComSpec):
    def __init__(self) -> None:
        super().__init__()

        self.operationRef: Union[Union[RefType, None] , None] = None

    def getOperationRef(self):
        return self.operationRef

    def setOperationRef(self, value):
        self.operationRef = value
        return self


class ModeSwitchReceiverComSpec(RPortComSpec):
    def __init__(self) -> None:
        super().__init__()

        self.enhancedModeApi: Union[Union[Boolean, None] , None] = None
        self.modeGroupRef: Union[Union[RefType, None] , None] = None
        self.supportsAsynchronousModeSwitch: Union[Union[Boolean, None] , None] = None

    def getEnhancedModeApi(self):
        return self.enhancedModeApi

    def setEnhancedModeApi(self, value):
        self.enhancedModeApi = value
        return self

    def getModeGroupRef(self):
        return self.modeGroupRef

    def setModeGroupRef(self, value):
        self.modeGroupRef = value
        return self

    def getSupportsAsynchronousModeSwitch(self):
        return self.supportsAsynchronousModeSwitch

    def setSupportsAsynchronousModeSwitch(self, value):
        self.supportsAsynchronousModeSwitch = value
        return self


class NvRequireComSpec(RPortComSpec):
    def __init__(self) -> None:
        super().__init__()

        self.initValue: Union[Union[ValueSpecification, None] , None] = None
        self.variableRef: Union[Union[RefType, None] , None] = None

    def getInitValue(self):
        return self.initValue

    def setInitValue(self, value: ValueSpecification):
        if value is not None:
            self.initValue = value
        return self

    def getVariableRef(self):
        return self.variableRef

    def setVariableRef(self, value: RefType):
        if value is not None:
            self.variableRef = value
        return self


class ParameterRequireComSpec(RPortComSpec):
    def __init__(self) -> None:
        super().__init__()

        self.initValue: Union[Union[ValueSpecification, None] , None] = None
        self.parameterRef: Union[Union[RefType, None] , None] = None

    def getInitValue(self):
        return self.initValue

    def setInitValue(self, value):
        self.initValue = value
        return self

    def getParameterRef(self):
        return self.parameterRef

    def setParameterRef(self, value):
        self.parameterRef = value
        return self


class ReceiverComSpec(RPortComSpec, ABC):

    def __init__(self) -> None:
        if type(self) is ReceiverComSpec:
            raise TypeError("ReceiverComSpec is an abstract class.")
        super().__init__()

        self.compositeNetworkRepresentations = []                            # type: List[CompositeNetworkRepresentation]
        self.dataElementRef = None                                           # type: RefType
        self.networkRepresentation = None                                    # type: SwDataDefProps
        self.handleOutOfRange = None                                         # type: HandleOutOfRangeEnum
        self.handleOutOfRangeStatus = None                                   # type: HandleOutOfRangeStatusEnum
        self.maxDeltaCounterInit = None                                      # type: PositiveInteger
        self.maxNoNewOrRepeatedData = None                                   # type: PositiveInteger
        self.usesEndToEndProtection = None                                   # type: ARBoolean

    def getDataElementRef(self):
        return self.dataElementRef

    def setDataElementRef(self, value):
        if value is not None:
            self.dataElementRef = value
        return self

    def getNetworkRepresentation(self):
        return self.networkRepresentation

    def setNetworkRepresentation(self, value):
        if value is not None:
            self.networkRepresentation = value
        return self

    def getHandleOutOfRange(self):
        return self.handleOutOfRange

    def setHandleOutOfRange(self, value):
        if value is not None:
            self.handleOutOfRange = value
        return self

    def getHandleOutOfRangeStatus(self):
        return self.handleOutOfRangeStatus

    def setHandleOutOfRangeStatus(self, value):
        if value is not None:
            self.handleOutOfRangeStatus = value
        return self

    def getMaxDeltaCounterInit(self):
        return self.maxDeltaCounterInit

    def setMaxDeltaCounterInit(self, value):
        if value is not None:
            self.maxDeltaCounterInit = value
        return self

    def getMaxNoNewOrRepeatedData(self):
        return self.maxNoNewOrRepeatedData

    def setMaxNoNewOrRepeatedData(self, value):
        if value is not None:
            self.maxNoNewOrRepeatedData = value
        return self

    def getUsesEndToEndProtection(self):
        return self.usesEndToEndProtection

    def setUsesEndToEndProtection(self, value):
        if value is not None:
            self.usesEndToEndProtection = value
        return self

    def addCompositeNetworkRepresentation(self, representation: CompositeNetworkRepresentation):
        if representation is not None:
            self.compositeNetworkRepresentations.append(representation)
        return self

    def getCompositeNetworkRepresentations(self) -> List[CompositeNetworkRepresentation]:
        return self.compositeNetworkRepresentations


class ModeSwitchedAckRequest(ARObject):

    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    def __init__(self) -> None:
        super().__init__()

        self.timeout: Union[Union[TimeValue, None] , None] = None

    def getTimeout(self):
        return self.timeout

    def setTimeout(self, value):
        if value is not None:
            self.timeout = value
        return self


class ModeSwitchSenderComSpec(PPortComSpec):
    def __init__(self) -> None:
        super().__init__()

        self.enhancedModeApi: Union[Union[ARBoolean, None] , None] = None
        self.modeGroupRef: Union[Union[RefType, None] , None] = None
        self.modeSwitchedAck: Union[Union[ModeSwitchedAckRequest, None] , None] = None
        self.queueLength: Union[Union[ARPositiveInteger, None] , None] = None

    def getEnhancedModeApi(self):
        return self.enhancedModeApi

    def setEnhancedModeApi(self, value):
        self.enhancedModeApi = value
        return self

    def getModeGroupRef(self):
        return self.modeGroupRef

    def setModeGroupRef(self, value):
        self.modeGroupRef = value
        return self

    def getModeSwitchedAck(self):
        return self.modeSwitchedAck

    def setModeSwitchedAck(self, value):
        self.modeSwitchedAck = value
        return self

    def getQueueLength(self):
        return self.queueLength

    def setQueueLength(self, value):
        self.queueLength = value
        return self


class ParameterProvideComSpec(PPortComSpec):
    def __init__(self) -> None:
        super().__init__()


class TransformationComSpecProps(Describable, ABC):
    def __init__(self) -> None:
        if type(self) is TransformationComSpecProps:
            raise TypeError("TransformationComSpecProps is an abstract class.")

        super().__init__()


class UserDefinedTransformationComSpecProps(TransformationComSpecProps):
    def __init__(self) -> None:
        super().__init__()


class ServerComSpec(PPortComSpec):
    def __init__(self) -> None:
        super().__init__()

        self.operationRef: Union[Union[RefType, None] , None] = None
        self.queueLength: Union[Union[PositiveInteger, None] , None] = None
        self.transformationComSpecProps: List[TransformationComSpecProps] = []

    def getOperationRef(self):
        return self.operationRef

    def setOperationRef(self, value):
        self.operationRef = value
        return self

    def getQueueLength(self):
        return self.queueLength

    def setQueueLength(self, value):
        self.queueLength = value
        return self

    def getTransformationComSpecProps(self) -> List[TransformationComSpecProps]:
        return self.transformationComSpecProps

    def addTransformationComSpecProps(self, transformation_com_spec_props: TransformationComSpecProps):
        if transformation_com_spec_props is not None:
            self.transformationComSpecProps.append(transformation_com_spec_props)
        return self


class NvProvideComSpec(PPortComSpec):
    def __init__(self) -> None:
        super().__init__()

        self.ramBlockInitValue: Union[Union[ValueSpecification, None] , None] = None
        self.romBlockInitValue: Union[Union[ValueSpecification, None] , None] = None
        self.variableRef: Union[Union[RefType, None] , None] = None

    def getRamBlockInitValue(self):
        return self.ramBlockInitValue

    def setRamBlockInitValue(self, value: ValueSpecification):
        if value is not None:
            self.ramBlockInitValue = value
        return self

    def getRomBlockInitValue(self):
        return self.romBlockInitValue

    def setRomBlockInitValue(self, value: ValueSpecification):
        if value is not None:
            self.romBlockInitValue = value
        return self

    def getVariableRef(self):
        return self.variableRef

    def setVariableRef(self, value: RefType):
        if value is not None:
            self.variableRef = value
        return self


class NonqueuedReceiverComSpec(ReceiverComSpec):
    def __init__(self) -> None:
        super().__init__()

        self.aliveTimeout: Union[Union[ARNumerical, None] , None] = None
        self.enableUpdated: Union[Union[ARBoolean, None] , None] = None
        self.filter = None
        self.handleDataStatus: Union[Union[ARBoolean, None] , None] = None
        self.handleNeverReceived: Union[Union[ARBoolean, None] , None] = None
        self.handleTimeoutType: str = ""
        self.initValue: Union[Union[ValueSpecification, None] , None] = None
        self.timeoutSubstitution: Union[Union[ValueSpecification, None] , None] = None

    def getAliveTimeout(self):
        return self.aliveTimeout

    def setAliveTimeout(self, value):
        self.aliveTimeout = value
        return self

    def getEnableUpdated(self):
        return self.enableUpdated

    def setEnableUpdated(self, value):
        self.enableUpdated = value
        return self

    def getFilter(self):
        return self.filter

    def setFilter(self, value):
        self.filter = value
        return self

    def getHandleDataStatus(self):
        return self.handleDataStatus

    def setHandleDataStatus(self, value):
        self.handleDataStatus = value
        return self

    def getHandleNeverReceived(self):
        return self.handleNeverReceived

    def setHandleNeverReceived(self, value):
        self.handleNeverReceived = value
        return self

    def getHandleTimeoutType(self):
        return self.handleTimeoutType

    def setHandleTimeoutType(self, value):
        self.handleTimeoutType = value
        return self

    def getInitValue(self):
        return self.initValue

    def setInitValue(self, value):
        self.initValue = value
        return self

    def getTimeoutSubstitution(self):
        return self.timeoutSubstitution

    def setTimeoutSubstitution(self, value):
        self.timeoutSubstitution = value
        return self


class QueuedReceiverComSpec(ReceiverComSpec):
    def __init__(self) -> None:
        super().__init__()

        self.queueLength: Union[Union[ARPositiveInteger, None] , None] = None

    def getQueueLength(self):
        return self.queueLength

    def setQueueLength(self, value):
        self.queueLength = value
        return self


class HandleOutOfRangeEnum(AREnum):
    """
    Enumeration for handle out of range behavior.
    """

    KEEP_OLD_VALUE = "keep-old-value"
    REPLACE_WITH_DEFAULT = "replace-with-default"
    REPLACE_WITH_LIMIT = "replace-with-limit"
    INVALIDATE = "invalidate"

    def __init__(self) -> None:
        super().__init__((
            HandleOutOfRangeEnum.KEEP_OLD_VALUE,
            HandleOutOfRangeEnum.REPLACE_WITH_DEFAULT,
            HandleOutOfRangeEnum.REPLACE_WITH_LIMIT,
            HandleOutOfRangeEnum.INVALIDATE,
        ))


class HandleOutOfRangeStatusEnum(AREnum):
    """
    Enumeration for handle out of range status.
    """

    SET_STATUS = "set-status"
    DO_NOT_SET_STATUS = "do-not-set-status"

    def __init__(self) -> None:
        super().__init__((
            HandleOutOfRangeStatusEnum.SET_STATUS,
            HandleOutOfRangeStatusEnum.DO_NOT_SET_STATUS,
        ))


class HandleTimeoutEnum(AREnum):
    """
    Enumeration for handle timeout behavior.
    """

    KEEP_OLD_VALUE = "keep-old-value"
    REPLACE_WITH_DEFAULT = "replace-with-default"
    INVALIDATE = "invalidate"

    def __init__(self) -> None:
        super().__init__((
            HandleTimeoutEnum.KEEP_OLD_VALUE,
            HandleTimeoutEnum.REPLACE_WITH_DEFAULT,
            HandleTimeoutEnum.INVALIDATE,
        ))


class TransmissionModeDefinitionEnum(AREnum):
    """
    Enumeration for transmission mode definition.
    """

    PERIODIC = "periodic"
    ON_CHANGE = "on-change"
    DIRECT = "direct"
    MIXED = "mixed"

    def __init__(self) -> None:
        super().__init__((
            TransmissionModeDefinitionEnum.PERIODIC,
            TransmissionModeDefinitionEnum.ON_CHANGE,
            TransmissionModeDefinitionEnum.DIRECT,
            TransmissionModeDefinitionEnum.MIXED,
        ))


__all__ = [
    'HandleInvalidEnum',
    'PPortComSpec',
    'RPortComSpec',
    'CompositeNetworkRepresentation',
    'TransmissionAcknowledgementRequest',
    'SenderComSpec',
    'QueuedSenderComSpec',
    'NonqueuedSenderComSpec',
    'ClientComSpec',
    'ModeSwitchReceiverComSpec',
    'NvRequireComSpec',
    'ParameterRequireComSpec',
    'ReceiverComSpec',
    'ModeSwitchedAckRequest',
    'ModeSwitchSenderComSpec',
    'ParameterProvideComSpec',
    'TransformationComSpecProps',
    'UserDefinedTransformationComSpecProps',
    'ServerComSpec',
    'NvProvideComSpec',
    'NonqueuedReceiverComSpec',
    'QueuedReceiverComSpec',
    'HandleOutOfRangeEnum',
    'HandleOutOfRangeStatusEnum',
    'HandleTimeoutEnum',
    'TransmissionModeDefinitionEnum',
]

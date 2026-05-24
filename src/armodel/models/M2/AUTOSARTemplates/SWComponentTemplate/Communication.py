"""
This module contains classes for representing AUTOSAR communication specifications
in the SWComponentTemplate module. It includes various communication specifications
for different types of port communication such as sender/receiver, client/server,
and mode switching communications, as well as non-volatile and parameter communications.
"""

from abc import ABC
from typing import List

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Describable
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps
from armodel.models.M2.AUTOSARTemplates.CommonStructure import ValueSpecification
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum, ARNumerical, ARPositiveInteger, Boolean
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, TimeValue
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARBoolean
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType


class HandleInvalidEnum(AREnum):
    """
    Strategies of handling the reception of invalidValue.
    """

    DONT_INVALIDATE = "dontInvalidate"
    EXTERNAL_REPLACEMENT = "externalReplacement"
    KEEP = "keep"
    REPLACE = "replace"

    def __init__(self):
        super().__init__((
            HandleInvalidEnum.DONT_INVALIDATE,
            HandleInvalidEnum.EXTERNAL_REPLACEMENT,
            HandleInvalidEnum.KEEP,
            HandleInvalidEnum.REPLACE
        ))


class PPortComSpec(ARObject, ABC):
    """
    Communication attributes of a provided PortPrototype. This class will contain attributes
    that are valid for all kinds of provide ports, independent of client-server or
    sender-receiver communication patterns.
    """

    def __init__(self):
        if type(self) is PPortComSpec:
            raise TypeError("PPortComSpec is an abstract class.")
        super().__init__()


class RPortComSpec(ARObject, ABC):
    """
    Communication attributes of a required PortPrototype. This class will contain attributes
    that are valid for all kinds of require ports, independent of client-server or
    sender-receiver communication patterns.
    """

    def __init__(self):
        if type(self) is RPortComSpec:
            raise TypeError("RPortComSpec is an abstract class.")

        super().__init__()


class CompositeNetworkRepresentation(ARObject):
    """
    This meta-class is used to define the network representation of leaf elements
    of composite application data types.
    """

    def __init__(self):
        super().__init__()

        self.leafElementIRef = None
        self.networkRepresentation: SwDataDefProps = None

    def getLeafElementIRef(self):
        """
        Gets the reference to the leaf element of a composite data type.

        Returns:
            The leaf element instance reference
        """
        return self.leafElementIRef

    def setLeafElementIRef(self, value):
        """
        Sets the reference to the leaf element of a composite data type.
        Only sets the value if it is not None.

        Args:
            value: The leaf element instance reference to set

        Returns:
            self for method chaining
        """
        self.leafElementIRef = value
        return self

    def getNetworkRepresentation(self):
        """
        Gets the network representation of this composite network representation.

        Returns:
            SwDataDefProps: The network representation
        """
        return self.networkRepresentation

    def setNetworkRepresentation(self, value):
        """
        Sets the network representation of this composite network representation.
        Only sets the value if it is not None.

        Args:
            value: The network representation to set

        Returns:
            self for method chaining
        """
        self.networkRepresentation = value
        return self


class TransmissionAcknowledgementRequest(ARObject):
    """
    Requests transmission acknowledgement that data has been sent successfully.
    Success/failure is reported via a SendPoint of a RunnableEntity.
    """

    def __init__(self):
        super().__init__()

        self.timeout: float = None

    def getTimeout(self):
        """
        Gets the timeout value for the transmission acknowledgement.

        Returns:
            float: The timeout value
        """
        return self.timeout

    def setTimeout(self, value):
        """
        Sets the timeout value for the transmission acknowledgement.
        Only sets the value if it is not None.

        Args:
            value: The timeout value to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.timeout = value
        return self


class SenderComSpec(PPortComSpec, ABC):
    """
    Communication attributes for a sender port (PPortPrototype typed by SenderReceiverInterface).
    """

    def __init__(self):
        if type(self) is SenderComSpec:
            raise TypeError("SenderComSpec is an abstract class.")

        super().__init__()

        self.compositeNetworkRepresentations: List[CompositeNetworkRepresentation] = []
        self.dataElementRef: RefType = None
        self.networkRepresentation: SwDataDefProps = None
        self.handleOutOfRange: str = None
        self.transmissionAcknowledge: TransmissionAcknowledgementRequest = None
        self.usesEndToEndProtection: ARBoolean = None

    def addCompositeNetworkRepresentation(self, representation: CompositeNetworkRepresentation):
        """
        Adds a composite network representation defined in the context of this SenderComSpec.
        """
        self.compositeNetworkRepresentations.append(representation)

    def getCompositeNetworkRepresentations(self) -> List[CompositeNetworkRepresentation]:
        """
        Gets the composite network representations defined in the context of this SenderComSpec.

        Returns:
            List[CompositeNetworkRepresentation]: The composite network representations
        """
        return self.compositeNetworkRepresentations

    def getDataElementRef(self):
        """
        Gets the data element these quality of service attributes apply to.

        Returns:
            RefType: The data element reference
        """
        return self.dataElementRef

    def setDataElementRef(self, value):
        """
        Sets the data element these quality of service attributes apply to.
        Only sets the value if it is not None.

        Args:
            value: The data element reference to set

        Returns:
            self for method chaining
        """
        self.dataElementRef = value
        return self

    def getNetworkRepresentation(self):
        """
        Gets the network representation used to define how the data element is mapped
        to a communication bus.

        Returns:
            SwDataDefProps: The network representation
        """
        return self.networkRepresentation

    def setNetworkRepresentation(self, value):
        """
        Sets the network representation used to define how the data element is mapped
        to a communication bus.
        Only sets the value if it is not None.

        Args:
            value: The network representation to set

        Returns:
            self for method chaining
        """
        self.networkRepresentation = value
        return self

    def getHandleOutOfRange(self):
        """
        Gets the strategy for handling out-of-range values.

        Returns:
            str: The handle out-of-range setting
        """
        return self.handleOutOfRange

    def setHandleOutOfRange(self, value):
        """
        Sets the strategy for handling out-of-range values.
        Only sets the value if it is not None.

        Args:
            value: The handle out-of-range setting

        Returns:
            self for method chaining
        """
        self.handleOutOfRange = value
        return self

    def getTransmissionAcknowledge(self):
        """
        Gets the transmission acknowledgement request for this sender com spec.

        Returns:
            TransmissionAcknowledgementRequest: The transmission acknowledgement
        """
        return self.transmissionAcknowledge

    def setTransmissionAcknowledge(self, value):
        """
        Sets the transmission acknowledgement request for this sender com spec.
        Only sets the value if it is not None.

        Args:
            value: The transmission acknowledgement request to set

        Returns:
            self for method chaining
        """
        self.transmissionAcknowledge = value
        return self

    def getUsesEndToEndProtection(self):
        """
        Gets whether the corresponding data element shall be transmitted using
        end-to-end protection.

        Returns:
            ARBoolean: True if end-to-end protection is used
        """
        return self.usesEndToEndProtection

    def setUsesEndToEndProtection(self, value):
        """
        Sets whether the corresponding data element shall be transmitted using
        end-to-end protection.
        Only sets the value if it is not None.

        Args:
            value: The end-to-end protection flag

        Returns:
            self for method chaining
        """
        self.usesEndToEndProtection = value
        return self


class QueuedSenderComSpec(SenderComSpec):
    """
    Communication attributes specific to distribution of events (PPortPrototype,
    SenderReceiverInterface and dataElement carries an 'event').
    """

    def __init__(self):
        super().__init__()


class NonqueuedSenderComSpec(SenderComSpec):
    """
    Communication attributes for non-queued sender/receiver communication (sender side).
    """

    def __init__(self):
        super().__init__()

        self.initValue: ValueSpecification = None

    def getInitValue(self):
        """
        Gets the initial value to be sent if sender component is not yet fully initialized,
        but receiver needs data already.

        Returns:
            ValueSpecification: The initial value
        """
        return self.initValue

    def setInitValue(self, value):
        """
        Sets the initial value to be sent if sender component is not yet fully initialized,
        but receiver needs data already.
        Only sets the value if it is not None.

        Args:
            value: The initial value to set

        Returns:
            self for method chaining
        """
        self.initValue = value
        return self


class ClientComSpec(RPortComSpec):
    """
    Client-specific communication attributes (RPortPrototype typed by ClientServerInterface).
    """

    def __init__(self):
        super().__init__()

        self.operationRef: RefType = None

    def getOperationRef(self):
        """
        Gets the reference to the operation these communication attributes apply to.

        Returns:
            RefType: The operation reference
        """
        return self.operationRef

    def setOperationRef(self, value):
        """
        Sets the reference to the operation these communication attributes apply to.
        Only sets the value if it is not None.

        Args:
            value: The operation reference to set

        Returns:
            self for method chaining
        """
        self.operationRef = value
        return self


class ModeSwitchReceiverComSpec(RPortComSpec):
    """
    Communication attributes of RPortPrototypes with respect to mode communication.
    """

    def __init__(self):
        super().__init__()

        self.enhancedModeApi: Boolean = None
        self.modeGroupRef: RefType = None
        self.supportsAsynchronousModeSwitch: Boolean = None

    def getEnhancedModeApi(self):
        """
        Gets whether the enhanced mode API is enabled.

        Returns:
            Boolean: True if enhanced mode API is enabled
        """
        return self.enhancedModeApi

    def setEnhancedModeApi(self, value):
        """
        Sets whether the enhanced mode API is enabled.
        Only sets the value if it is not None.

        Args:
            value: The enhanced mode API flag

        Returns:
            self for method chaining
        """
        self.enhancedModeApi = value
        return self

    def getModeGroupRef(self):
        """
        Gets the reference to the mode group.

        Returns:
            RefType: The mode group reference
        """
        return self.modeGroupRef

    def setModeGroupRef(self, value):
        """
        Sets the reference to the mode group.
        Only sets the value if it is not None.

        Args:
            value: The mode group reference to set

        Returns:
            self for method chaining
        """
        self.modeGroupRef = value
        return self

    def getSupportsAsynchronousModeSwitch(self):
        """
        Gets whether asynchronous mode switch is supported.

        Returns:
            Boolean: True if asynchronous mode switch is supported
        """
        return self.supportsAsynchronousModeSwitch

    def setSupportsAsynchronousModeSwitch(self, value):
        """
        Sets whether asynchronous mode switch is supported.
        Only sets the value if it is not None.

        Args:
            value: The asynchronous mode switch support flag

        Returns:
            self for method chaining
        """
        self.supportsAsynchronousModeSwitch = value
        return self


class NvRequireComSpec(RPortComSpec):
    """
    Communication attributes of RPortPrototypes with respect to Nv data communication
    on the required side.
    """

    def __init__(self):
        super().__init__()

        self.initValue: ValueSpecification = None
        self.variableRef: RefType = None

    def getInitValue(self):
        """
        Gets the initial value to be used in case the sending component is not yet initialized.

        Returns:
            ValueSpecification: The initial value
        """
        return self.initValue

    def setInitValue(self, value: ValueSpecification):
        """
        Sets the initial value to be used in case the sending component is not yet initialized.
        Only sets the value if it is not None.

        Args:
            value: The initial value to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.initValue = value
        return self

    def getVariableRef(self):
        """
        Gets the reference to the VariableDataPrototype within the NvDataInterface.

        Returns:
            RefType: The variable reference
        """
        return self.variableRef

    def setVariableRef(self, value: RefType):
        """
        Sets the reference to the VariableDataPrototype within the NvDataInterface.
        Only sets the value if it is not None.

        Args:
            value: The variable reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.variableRef = value
        return self


class ParameterRequireComSpec(RPortComSpec):
    """
    \"Communication\" specification that applies to parameters on the required side
    of a connection.
    """

    def __init__(self):
        super().__init__()

        self.initValue: ValueSpecification = None
        self.parameterRef: RefType = None

    def getInitValue(self):
        """
        Gets the initial value for the parameter.

        Returns:
            ValueSpecification: The initial value
        """
        return self.initValue

    def setInitValue(self, value):
        """
        Sets the initial value for the parameter.
        Only sets the value if it is not None.

        Args:
            value: The initial value to set

        Returns:
            self for method chaining
        """
        self.initValue = value
        return self

    def getParameterRef(self):
        """
        Gets the reference to the parameter in the ParameterInterface.

        Returns:
            RefType: The parameter reference
        """
        return self.parameterRef

    def setParameterRef(self, value):
        """
        Sets the reference to the parameter in the ParameterInterface.
        Only sets the value if it is not None.

        Args:
            value: The parameter reference to set

        Returns:
            self for method chaining
        """
        self.parameterRef = value
        return self


class ReceiverComSpec(RPortComSpec, ABC):
    """
    Receiver-specific communication attributes (RPortPrototype typed by SenderReceiverInterface).
    """

    def __init__(self):
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
        """
        Gets the data element these attributes belong to.

        Returns:
            RefType: The data element reference
        """
        return self.dataElementRef

    def setDataElementRef(self, value):
        """
        Sets the data element these attributes belong to.
        Only sets the value if it is not None.

        Args:
            value: The data element reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.dataElementRef = value
        return self

    def getNetworkRepresentation(self):
        """
        Gets the network representation used to define how the data element is mapped
        to a communication bus.

        Returns:
            SwDataDefProps: The network representation
        """
        return self.networkRepresentation

    def setNetworkRepresentation(self, value):
        """
        Sets the network representation used to define how the data element is mapped
        to a communication bus.
        Only sets the value if it is not None.

        Args:
            value: The network representation to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.networkRepresentation = value
        return self

    def getHandleOutOfRange(self):
        """
        Gets how values that are out of the specified range are handled
        according to the values of HandleOutOfRangeEnum.

        Returns:
            HandleOutOfRangeEnum: The handle out-of-range setting
        """
        return self.handleOutOfRange

    def setHandleOutOfRange(self, value):
        """
        Sets how values that are out of the specified range are handled.
        Only sets the value if it is not None.

        Args:
            value: The handle out-of-range setting

        Returns:
            self for method chaining
        """
        if value is not None:
            self.handleOutOfRange = value
        return self

    def getHandleOutOfRangeStatus(self):
        """
        Gets how return values are created in case of an out-of-range situation.

        Returns:
            HandleOutOfRangeStatusEnum: The out-of-range status handling
        """
        return self.handleOutOfRangeStatus

    def setHandleOutOfRangeStatus(self, value):
        """
        Sets how return values are created in case of an out-of-range situation.
        Only sets the value if it is not None.

        Args:
            value: The out-of-range status handling to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.handleOutOfRangeStatus = value
        return self

    def getMaxDeltaCounterInit(self):
        """
        Gets the initial maximum allowed gap between two counter values of two
        consecutively received valid Data.

        Returns:
            PositiveInteger: The max delta counter init value
        """
        return self.maxDeltaCounterInit

    def setMaxDeltaCounterInit(self, value):
        """
        Sets the initial maximum allowed gap between two counter values of two
        consecutively received valid Data.
        Only sets the value if it is not None.

        Args:
            value: The max delta counter init value to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.maxDeltaCounterInit = value
        return self

    def getMaxNoNewOrRepeatedData(self):
        """
        Gets the maximum amount of missing or repeated data which the receiver does not
        expect to exceed under normal communication conditions.

        Returns:
            PositiveInteger: The max no new or repeated data value
        """
        return self.maxNoNewOrRepeatedData

    def setMaxNoNewOrRepeatedData(self, value):
        """
        Sets the maximum amount of missing or repeated data which the receiver does not
        expect to exceed under normal communication conditions.
        Only sets the value if it is not None.

        Args:
            value: The max no new or repeated data value to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.maxNoNewOrRepeatedData = value
        return self

    def getUsesEndToEndProtection(self):
        """
        Gets whether the corresponding data element shall be transmitted using
        end-to-end protection.

        Returns:
            ARBoolean: True if end-to-end protection is used
        """
        return self.usesEndToEndProtection

    def setUsesEndToEndProtection(self, value):
        """
        Sets whether the corresponding data element shall be transmitted using
        end-to-end protection.
        Only sets the value if it is not None.

        Args:
            value: The end-to-end protection flag

        Returns:
            self for method chaining
        """
        if value is not None:
            self.usesEndToEndProtection = value
        return self

    def addCompositeNetworkRepresentation(self, representation: CompositeNetworkRepresentation):
        """
        Adds a composite network representation defined in the context of this ReceiverComSpec.
        Only adds the value if it is not None.

        Args:
            representation: The composite network representation to add

        Returns:
            self for method chaining
        """
        if representation is not None:
            self.compositeNetworkRepresentations.append(representation)
        return self

    def getCompositeNetworkRepresentations(self) -> List[CompositeNetworkRepresentation]:
        """
        Gets the composite network representations defined in the context of this ReceiverComSpec.

        Returns:
            List[CompositeNetworkRepresentation]: The composite network representations
        """
        return self.compositeNetworkRepresentations


class ModeSwitchedAckRequest(ARObject):
    """
    Requests acknowledgements that a mode switch has been proceeded successfully.
    """

    def __init__(self):
        super().__init__()

        self.timeout: TimeValue = None

    def getTimeout(self):
        """
        Gets the timeout value for the mode switched acknowledgement.

        Returns:
            TimeValue: The timeout value
        """
        return self.timeout

    def setTimeout(self, value):
        """
        Sets the timeout value for the mode switched acknowledgement.
        Only sets the value if it is not None.

        Args:
            value: The timeout value to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.timeout = value
        return self


class ModeSwitchSenderComSpec(PPortComSpec):
    """
    Communication attributes of PPortPrototypes with respect to mode communication.
    """

    def __init__(self):
        super().__init__()

        self.enhancedModeApi: ARBoolean = None
        self.modeGroupRef: RefType = None
        self.modeSwitchedAck: ModeSwitchedAckRequest = None
        self.queueLength: ARPositiveInteger = None

    def getEnhancedModeApi(self):
        """
        Gets whether the enhanced mode API is enabled.

        Returns:
            ARBoolean: True if enhanced mode API is enabled
        """
        return self.enhancedModeApi

    def setEnhancedModeApi(self, value):
        """
        Sets whether the enhanced mode API is enabled.
        Only sets the value if it is not None.

        Args:
            value: The enhanced mode API flag

        Returns:
            self for method chaining
        """
        self.enhancedModeApi = value
        return self

    def getModeGroupRef(self):
        """
        Gets the reference to the mode group.

        Returns:
            RefType: The mode group reference
        """
        return self.modeGroupRef

    def setModeGroupRef(self, value):
        """
        Sets the reference to the mode group.
        Only sets the value if it is not None.

        Args:
            value: The mode group reference to set

        Returns:
            self for method chaining
        """
        self.modeGroupRef = value
        return self

    def getModeSwitchedAck(self):
        """
        Gets the mode switched acknowledgement request.

        Returns:
            ModeSwitchedAckRequest: The mode switched acknowledgement
        """
        return self.modeSwitchedAck

    def setModeSwitchedAck(self, value):
        """
        Sets the mode switched acknowledgement request.
        Only sets the value if it is not None.

        Args:
            value: The mode switched acknowledgement request to set

        Returns:
            self for method chaining
        """
        self.modeSwitchedAck = value
        return self

    def getQueueLength(self):
        """
        Gets the length of the mode switch queue.

        Returns:
            ARPositiveInteger: The queue length
        """
        return self.queueLength

    def setQueueLength(self, value):
        """
        Sets the length of the mode switch queue.
        Only sets the value if it is not None.

        Args:
            value: The queue length to set

        Returns:
            self for method chaining
        """
        self.queueLength = value
        return self


class ParameterProvideComSpec(PPortComSpec):
    """
    \"Communication\" specification that applies to parameters on the provided side
    of a connection.
    """

    def __init__(self):
        super().__init__()


class TransformationComSpecProps(Describable, ABC):
    """
    TransformationComSpecProps holds all the attributes for transformers that are
    port specific.
    """

    def __init__(self):
        if type(self) is TransformationComSpecProps:
            raise TypeError("TransformationComSpecProps is an abstract class.")

        super().__init__()


class EndToEndTransformationComSpecProps(TransformationComSpecProps):
    """
    The class EndToEndTransformationComSpecProps specifies port specific configuration
    properties for EndToEnd transformer attributes.
    """

    def __init__(self):
        super().__init__()

        self.clearFromValidToInvalid: ARBoolean = None
        self.disableEndToEndCheck: ARBoolean = None
        self.disableEndToEndStateMachine: ARBoolean = None
        self.e2eProfileCompatibilityPropsRef: RefType = None
        self.maxDeltaCounter: PositiveInteger = None
        self.maxErrorStateInit: PositiveInteger = None
        self.maxErrorStateInvalid: PositiveInteger = None
        self.maxErrorStateValid: PositiveInteger = None
        self.maxNoNewOrRepeatedData: PositiveInteger = None
        self.minOkStateInit: PositiveInteger = None
        self.minOkStateInvalid: PositiveInteger = None
        self.minOkStateValid: PositiveInteger = None
        self.syncCounterInit: PositiveInteger = None
        self.windowSizeInit: PositiveInteger = None
        self.windowSizeInvalid: PositiveInteger = None
        self.windowSizeValid: PositiveInteger = None

    def getClearFromValidToInvalid(self) -> ARBoolean:
        """
        Gets whether the monitoring window is cleared on transition from state Valid
        to state Invalid.

        Returns:
            ARBoolean: True if monitoring window is cleared on transition
        """
        return self.clearFromValidToInvalid

    def setClearFromValidToInvalid(self, value: ARBoolean):
        """
        Sets whether the monitoring window is cleared on transition from state Valid
        to state Invalid.
        Only sets the value if it is not None.

        Args:
            value: The clear flag to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.clearFromValidToInvalid = value
        return self

    def getDisableEndToEndCheck(self) -> ARBoolean:
        """
        Gets whether the E2E check is disabled/enabled.
        The E2E header is removed from the payload independent from the setting
        of this attribute.

        Returns:
            ARBoolean: True if E2E check is disabled
        """
        return self.disableEndToEndCheck

    def setDisableEndToEndCheck(self, value: ARBoolean):
        """
        Sets whether the E2E check is disabled/enabled.
        Only sets the value if it is not None.

        Args:
            value: The disable flag to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.disableEndToEndCheck = value
        return self

    def getDisableEndToEndStateMachine(self) -> ARBoolean:
        """
        Gets whether the E2E state machine is disabled (only E2E check functionality
        is performed).

        Returns:
            ARBoolean: True if E2E state machine is disabled
        """
        return self.disableEndToEndStateMachine

    def setDisableEndToEndStateMachine(self, value: ARBoolean):
        """
        Sets whether the E2E state machine is disabled.
        Only sets the value if it is not None.

        Args:
            value: The disable flag to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.disableEndToEndStateMachine = value
        return self

    def getE2eProfileCompatibilityPropsRef(self) -> RefType:
        """
        Gets the reference to additional settings for the E2E state machine.

        Returns:
            RefType: The E2E profile compatibility props reference
        """
        return self.e2eProfileCompatibilityPropsRef

    def setE2eProfileCompatibilityPropsRef(self, value: RefType):
        """
        Sets the reference to additional settings for the E2E state machine.
        Only sets the value if it is not None.

        Args:
            value: The E2E profile compatibility props reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.e2eProfileCompatibilityPropsRef = value
        return self

    def getMaxDeltaCounter(self) -> PositiveInteger:
        """
        Gets the maximum allowed difference between two counter values of two
        consecutively received valid messages.

        Returns:
            PositiveInteger: The max delta counter value
        """
        return self.maxDeltaCounter

    def setMaxDeltaCounter(self, value: PositiveInteger):
        """
        Sets the maximum allowed difference between two counter values of two
        consecutively received valid messages.
        Only sets the value if it is not None.

        Args:
            value: The max delta counter value to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.maxDeltaCounter = value
        return self

    def getMaxErrorStateInit(self) -> PositiveInteger:
        """
        Gets the maximal number of checks in which ProfileStatus equal to
        E2E_P_ERROR was determined, within the last Window Size checks,
        for the state E2E_SM_INIT.

        Returns:
            PositiveInteger: The max error state init value
        """
        return self.maxErrorStateInit

    def setMaxErrorStateInit(self, value: PositiveInteger):
        """
        Sets the maximal number of checks in which ProfileStatus equal to
        E2E_P_ERROR was determined, within the last Window Size checks,
        for the state E2E_SM_INIT.
        Only sets the value if it is not None.

        Args:
            value: The max error state init value to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.maxErrorStateInit = value
        return self

    def getMaxErrorStateInvalid(self) -> PositiveInteger:
        """
        Gets the maximal number of checks in which ProfileStatus equal to
        E2E_P_ERROR was determined, within the last Window Size checks,
        for the state E2E_SM_INVALID.

        Returns:
            PositiveInteger: The max error state invalid value
        """
        return self.maxErrorStateInvalid

    def setMaxErrorStateInvalid(self, value: PositiveInteger):
        """
        Sets the maximal number of checks in which ProfileStatus equal to
        E2E_P_ERROR was determined, within the last Window Size checks,
        for the state E2E_SM_INVALID.
        Only sets the value if it is not None.

        Args:
            value: The max error state invalid value to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.maxErrorStateInvalid = value
        return self

    def getMaxErrorStateValid(self) -> PositiveInteger:
        """
        Gets the maximal number of checks in which ProfileStatus equal to
        E2E_P_ERROR was determined, within the last Window Size checks,
        for the state E2E_SM_VALID.

        Returns:
            PositiveInteger: The max error state valid value
        """
        return self.maxErrorStateValid

    def setMaxErrorStateValid(self, value: PositiveInteger):
        """
        Sets the maximal number of checks in which ProfileStatus equal to
        E2E_P_ERROR was determined, within the last Window Size checks,
        for the state E2E_SM_VALID.
        Only sets the value if it is not None.

        Args:
            value: The max error state valid value to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.maxErrorStateValid = value
        return self

    def getMaxNoNewOrRepeatedData(self) -> PositiveInteger:
        """
        Gets the maximum amount of missing or repeated data which the receiver does not
        expect to exceed under normal communication conditions.
        EndToEndTransformationDescription holds this attribute which is profile specific.

        Returns:
            PositiveInteger: The max no new or repeated data value
        """
        return self.maxNoNewOrRepeatedData

    def setMaxNoNewOrRepeatedData(self, value: PositiveInteger):
        """
        Sets the maximum amount of missing or repeated data which the receiver does not
        expect to exceed under normal communication conditions.
        Only sets the value if it is not None.

        Args:
            value: The max no new or repeated data value to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.maxNoNewOrRepeatedData = value
        return self

    def getMinOkStateInit(self) -> PositiveInteger:
        """
        Gets the minimal number of checks in which ProfileStatus equal to
        E2E_P_OK was determined, within the last WindowSize checks,
        for the state E2E_SM_INIT.

        Returns:
            PositiveInteger: The min ok state init value
        """
        return self.minOkStateInit

    def setMinOkStateInit(self, value: PositiveInteger):
        """
        Sets the minimal number of checks in which ProfileStatus equal to
        E2E_P_OK was determined, within the last WindowSize checks,
        for the state E2E_SM_INIT.
        Only sets the value if it is not None.

        Args:
            value: The min ok state init value to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.minOkStateInit = value
        return self

    def getMinOkStateInvalid(self) -> PositiveInteger:
        """
        Gets the minimal number of checks in which ProfileStatus equal to
        E2E_P_OK was determined, within the last WindowSize checks,
        for the state E2E_SM_INVALID.

        Returns:
            PositiveInteger: The min ok state invalid value
        """
        return self.minOkStateInvalid

    def setMinOkStateInvalid(self, value: PositiveInteger):
        """
        Sets the minimal number of checks in which ProfileStatus equal to
        E2E_P_OK was determined, within the last WindowSize checks,
        for the state E2E_SM_INVALID.
        Only sets the value if it is not None.

        Args:
            value: The min ok state invalid value to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.minOkStateInvalid = value
        return self

    def getMinOkStateValid(self) -> PositiveInteger:
        """
        Gets the minimal number of checks in which ProfileStatus equal to
        E2E_P_OK was determined, within the last WindowSize checks,
        for the state E2E_SM_VALID.

        Returns:
            PositiveInteger: The min ok state valid value
        """
        return self.minOkStateValid

    def setMinOkStateValid(self, value: PositiveInteger):
        """
        Sets the minimal number of checks in which ProfileStatus equal to
        E2E_P_OK was determined, within the last WindowSize checks,
        for the state E2E_SM_VALID.
        Only sets the value if it is not None.

        Args:
            value: The min ok state valid value to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.minOkStateValid = value
        return self

    def getSyncCounterInit(self) -> PositiveInteger:
        """
        Gets the number of Data required for validating the consistency of the counter
        that shall be received with a valid counter after the detection of an unexpected
        behavior of a received counter.
        EndToEndTransformationDescription holds this attribute which is profile specific.

        Returns:
            PositiveInteger: The sync counter init value
        """
        return self.syncCounterInit

    def setSyncCounterInit(self, value: PositiveInteger):
        """
        Sets the number of Data required for validating the consistency of the counter.
        Only sets the value if it is not None.

        Args:
            value: The sync counter init value to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.syncCounterInit = value
        return self

    def getWindowSizeInit(self) -> PositiveInteger:
        """
        Gets the size of the monitoring window of state Init for the E2E state machine.

        Returns:
            PositiveInteger: The window size init value
        """
        return self.windowSizeInit

    def setWindowSizeInit(self, value: PositiveInteger):
        """
        Sets the size of the monitoring window of state Init for the E2E state machine.
        Only sets the value if it is not None.

        Args:
            value: The window size init value to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.windowSizeInit = value
        return self

    def getWindowSizeInvalid(self) -> PositiveInteger:
        """
        Gets the size of the monitoring window of state Invalid for the E2E state machine.

        Returns:
            PositiveInteger: The window size invalid value
        """
        return self.windowSizeInvalid

    def setWindowSizeInvalid(self, value: PositiveInteger):
        """
        Sets the size of the monitoring window of state Invalid for the E2E state machine.
        Only sets the value if it is not None.

        Args:
            value: The window size invalid value to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.windowSizeInvalid = value
        return self

    def getWindowSizeValid(self) -> PositiveInteger:
        """
        Gets the size of the monitoring window of state Valid for the E2E state machine.

        Returns:
            PositiveInteger: The window size valid value
        """
        return self.windowSizeValid

    def setWindowSizeValid(self, value: PositiveInteger):
        """
        Sets the size of the monitoring window of state Valid for the E2E state machine.
        Only sets the value if it is not None.

        Args:
            value: The window size valid value to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.windowSizeValid = value
        return self


class UserDefinedTransformationComSpecProps(TransformationComSpecProps):
    """
    The UserDefinedTransformationComSpecProps is used to specify port specific
    configuration properties for custom transformers.
    """

    def __init__(self):
        super().__init__()


class ServerComSpec(PPortComSpec):
    """
    Communication attributes for a server port (PPortPrototype and ClientServerInterface).
    """

    def __init__(self):
        super().__init__()

        self.operationRef: RefType = None
        self.queueLength: PositiveInteger = None
        self.transformationComSpecProps: List[TransformationComSpecProps] = []

    def getOperationRef(self):
        """
        Gets the operation these communication attributes apply to.

        Returns:
            RefType: The operation reference
        """
        return self.operationRef

    def setOperationRef(self, value):
        """
        Sets the operation these communication attributes apply to.
        Only sets the value if it is not None.

        Args:
            value: The operation reference to set

        Returns:
            self for method chaining
        """
        self.operationRef = value
        return self

    def getQueueLength(self):
        """
        Gets the length of call queue on the server side.
        The queue is implemented by the RTE.

        Returns:
            PositiveInteger: The queue length
        """
        return self.queueLength

    def setQueueLength(self, value):
        """
        Sets the length of call queue on the server side.
        Only sets the value if it is not None.

        Args:
            value: The queue length to set

        Returns:
            self for method chaining
        """
        self.queueLength = value
        return self

    def getTransformationComSpecProps(self) -> List[TransformationComSpecProps]:
        """
        Gets the TransformationComSpecProps which define port-specific configuration
        for data transformation.

        Returns:
            List[TransformationComSpecProps]: The transformation com spec props
        """
        return self.transformationComSpecProps

    def addTransformationComSpecProps(self, transformationComSpecProps: TransformationComSpecProps):
        """
        Adds a TransformationComSpecProps which defines port-specific configuration
        for data transformation.
        Only adds the value if it is not None.

        Args:
            transformationComSpecProps: The transformation com spec props to add

        Returns:
            self for method chaining
        """
        if transformationComSpecProps is not None:
            self.transformationComSpecProps.append(transformationComSpecProps)
        return self


class NvProvideComSpec(PPortComSpec):
    """
    Communication attributes of PPortPrototypes with respect to Nv data communication
    on the provided side.
    """

    def __init__(self):
        super().__init__()

        self.ramBlockInitValue: ValueSpecification = None
        self.romBlockInitValue: ValueSpecification = None
        self.variableRef: RefType = None

    def getRamBlockInitValue(self):
        """
        Gets the initial value for the RAM block of Nv data.

        Returns:
            ValueSpecification: The RAM block init value
        """
        return self.ramBlockInitValue

    def setRamBlockInitValue(self, value: ValueSpecification):
        """
        Sets the initial value for the RAM block of Nv data.
        Only sets the value if it is not None.

        Args:
            value: The RAM block init value to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.ramBlockInitValue = value
        return self

    def getRomBlockInitValue(self):
        """
        Gets the initial value for the ROM block of Nv data.

        Returns:
            ValueSpecification: The ROM block init value
        """
        return self.romBlockInitValue

    def setRomBlockInitValue(self, value: ValueSpecification):
        """
        Sets the initial value for the ROM block of Nv data.
        Only sets the value if it is not None.

        Args:
            value: The ROM block init value to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.romBlockInitValue = value
        return self

    def getVariableRef(self):
        """
        Gets the reference to the VariableDataPrototype within the NvDataInterface.

        Returns:
            RefType: The variable reference
        """
        return self.variableRef

    def setVariableRef(self, value: RefType):
        """
        Sets the reference to the VariableDataPrototype within the NvDataInterface.
        Only sets the value if it is not None.

        Args:
            value: The variable reference to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.variableRef = value
        return self


class NonqueuedReceiverComSpec(ReceiverComSpec):
    """
    Communication attributes specific to non-queued receiving.
    """

    def __init__(self):
        super().__init__()

        self.aliveTimeout: ARNumerical = None
        self.enableUpdated: ARBoolean = None
        self.filter = None
        self.handleDataStatus: ARBoolean = None
        self.handleNeverReceived: ARBoolean = None
        self.handleTimeoutType: str = ""
        self.initValue: ValueSpecification = None
        self.timeoutSubstitution: ValueSpecification = None

    def getAliveTimeout(self):
        """
        Gets the amount of time (in seconds) after which the software component
        (via the RTE) needs to be notified if the corresponding data item has not
        been received. If aliveTimeout is 0, no timeout monitoring shall be performed.

        Returns:
            ARNumerical: The alive timeout value
        """
        return self.aliveTimeout

    def setAliveTimeout(self, value):
        """
        Sets the amount of time (in seconds) after which the software component
        needs to be notified.
        Only sets the value if it is not None.

        Args:
            value: The alive timeout value to set

        Returns:
            self for method chaining
        """
        self.aliveTimeout = value
        return self

    def getEnableUpdated(self):
        """
        Gets whether application code is entitled to check whether the value
        of the corresponding VariableDataPrototype has been updated.

        Returns:
            ARBoolean: True if update check is enabled
        """
        return self.enableUpdated

    def setEnableUpdated(self, value):
        """
        Sets whether application code is entitled to check whether the value
        of the corresponding VariableDataPrototype has been updated.
        Only sets the value if it is not None.

        Args:
            value: The enable updated flag

        Returns:
            self for method chaining
        """
        self.enableUpdated = value
        return self

    def getFilter(self):
        """
        Gets the applicable filter algorithm for filtering the value
        of the corresponding dataElement.

        Returns:
            The filter algorithm
        """
        return self.filter

    def setFilter(self, value):
        """
        Sets the applicable filter algorithm for filtering the value
        of the corresponding dataElement.
        Only sets the value if it is not None.

        Args:
            value: The filter algorithm to set

        Returns:
            self for method chaining
        """
        self.filter = value
        return self

    def getHandleDataStatus(self):
        """
        Gets whether the Rte_IStatus API shall exist.

        Returns:
            ARBoolean: True if handle data status is enabled
        """
        return self.handleDataStatus

    def setHandleDataStatus(self, value):
        """
        Sets whether the Rte_IStatus API shall exist.
        Only sets the value if it is not None.

        Args:
            value: The handle data status flag

        Returns:
            self for method chaining
        """
        self.handleDataStatus = value
        return self

    def getHandleNeverReceived(self):
        """
        Gets whether the 'never received' flag is available for the corresponding
        VariableDataPrototype.

        Returns:
            ARBoolean: True if never received flag is available
        """
        return self.handleNeverReceived

    def setHandleNeverReceived(self, value):
        """
        Sets whether the 'never received' flag is available for the corresponding
        VariableDataPrototype.
        Only sets the value if it is not None.

        Args:
            value: The handle never received flag

        Returns:
            self for method chaining
        """
        self.handleNeverReceived = value
        return self

    def getHandleTimeoutType(self):
        """
        Gets the behavior with respect to the handling of timeouts.

        Returns:
            str: The handle timeout type
        """
        return self.handleTimeoutType

    def setHandleTimeoutType(self, value):
        """
        Sets the behavior with respect to the handling of timeouts.
        Only sets the value if it is not None.

        Args:
            value: The handle timeout type to set

        Returns:
            self for method chaining
        """
        self.handleTimeoutType = value
        return self

    def getInitValue(self):
        """
        Gets the initial value to be used in case the sending component
        is not yet initialized.

        Returns:
            ValueSpecification: The initial value
        """
        return self.initValue

    def setInitValue(self, value):
        """
        Sets the initial value to be used in case the sending component
        is not yet initialized.
        Only sets the value if it is not None.

        Args:
            value: The initial value to set

        Returns:
            self for method chaining
        """
        self.initValue = value
        return self

    def getTimeoutSubstitution(self):
        """
        Gets the substitution value applicable in the case of a timeout.

        Returns:
            ValueSpecification: The timeout substitution value
        """
        return self.timeoutSubstitution

    def setTimeoutSubstitution(self, value):
        """
        Sets the substitution value applicable in the case of a timeout.
        Only sets the value if it is not None.

        Args:
            value: The timeout substitution value to set

        Returns:
            self for method chaining
        """
        self.timeoutSubstitution = value
        return self


class QueuedReceiverComSpec(ReceiverComSpec):
    """
    Communication attributes specific to queued receiving.
    """

    def __init__(self):
        super().__init__()

        self.queueLength: ARPositiveInteger = None

    def getQueueLength(self):
        """
        Gets the length of queue for received events.

        Returns:
            ARPositiveInteger: The queue length
        """
        return self.queueLength

    def setQueueLength(self, value):
        """
        Sets the length of queue for received events.
        Only sets the value if it is not None.

        Args:
            value: The queue length to set

        Returns:
            self for method chaining
        """
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

    def __init__(self):
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

    def __init__(self):
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

    def __init__(self):
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

    def __init__(self):
        super().__init__((
            TransmissionModeDefinitionEnum.PERIODIC,
            TransmissionModeDefinitionEnum.ON_CHANGE,
            TransmissionModeDefinitionEnum.DIRECT,
            TransmissionModeDefinitionEnum.MIXED,
        ))

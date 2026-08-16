"""
This module contains classes for representing AUTOSAR communication specifications
in the SWComponentTemplate module. It includes various communication specifications
for different types of port communication such as sender/receiver, client/server,
and mode switching communications, as well as non-volatile and parameter communications.
"""

from abc import ABC
from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Describable
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps
from armodel.models.M2.AUTOSARTemplates.CommonStructure import ValueSpecification
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum, ARPositiveInteger, Boolean
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, TimeValue
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARBoolean
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.InstanceRefs import ApplicationCompositeElementInPortInterfaceInstanceRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Filter import DataFilter
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements import VariableAccess


class HandleInvalidEnum(AREnum):
    """
    Strategies of handling the reception of invalidValue.
    """

    # HandleInvalidEnum method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    DONT_INVALIDATE = "dontInvalidate"
    EXTERNAL_REPLACEMENT = "externalReplacement"
    KEEP = "keep"
    REPLACE = "replace"

    def __init__(self):
        super().__init__((HandleInvalidEnum.DONT_INVALIDATE, HandleInvalidEnum.EXTERNAL_REPLACEMENT, HandleInvalidEnum.KEEP, HandleInvalidEnum.REPLACE))


class PPortComSpec(ARObject, ABC):
    """
    Communication attributes of a provided PortPrototype. This class will contain attributes
    that are valid for all kinds of provide ports, independent of client-server or
    sender-receiver communication patterns.
    """

    # PPortComSpec method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        if type(self) is PPortComSpec:
            raise TypeError("PPortComSpec is an abstract class.")
        super().__init__()


class RPortComSpec(ARObject, ABC):
    """
    Communication attributes of a required PortPrototype. This class will contain attributes that are valid for all kinds of require-ports, independent of client-server or sender-receiver communication patterns.
    """

    # RPortComSpec method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.59, p.167
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self):
        if type(self) is RPortComSpec:
            raise TypeError("RPortComSpec is an abstract class.")

        super().__init__()


class ReceptionComSpecProps(ARObject):
    """
    This meta-class defines a set of reception attributes which the application software is assumed to implement.
    """

    # ReceptionComSpecProps method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.64, p.174
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__             [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getDataUpdatePeriod  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setDataUpdatePeriod  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTimeout           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTimeout           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # This attribute defines the period in which the application shall check for updated data. This attribute is used for the configuration of the E2E protection, but may also indicate a general data reception period.
        self.dataUpdatePeriod: Optional[TimeValue] = None

        # This attribute defines the time interval after which the application shall assume that the to be received data reception has timed out, i.e. the respective data has not been received for that amount of time.
        self.timeout: Optional[TimeValue] = None

    def getDataUpdatePeriod(self) -> Optional[TimeValue]:
        """
        Gets the period in which the application shall check for updated data.

        This attribute defines the period in which the application shall check for updated data. This attribute is used for the configuration of the E2E protection, but may also indicate a general data reception period.

        Returns:
            TimeValue representing the data update period, or None if not set
        """
        return self.dataUpdatePeriod

    def setDataUpdatePeriod(self, value: Optional[TimeValue]) -> "ReceptionComSpecProps":
        """
        Sets the period in which the application shall check for updated data.
        A None value is a no-op and does not overwrite an existing data update period.

        This attribute defines the period in which the application shall check for updated data. This attribute is used for the configuration of the E2E protection, but may also indicate a general data reception period.

        Args:
            value: The data update period TimeValue to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.dataUpdatePeriod = value
        return self

    def getTimeout(self) -> Optional[TimeValue]:
        """
        Gets the time interval after which the application shall assume that the to be received data reception has timed out.

        This attribute defines the time interval after which the application shall assume that the to be received data reception has timed out, i.e. the respective data has not been received for that amount of time.

        Returns:
            TimeValue representing the timeout, or None if not set
        """
        return self.timeout

    def setTimeout(self, value: Optional[TimeValue]) -> "ReceptionComSpecProps":
        """
        Sets the time interval after which the application shall assume that the to be received data reception has timed out.
        A None value is a no-op and does not overwrite an existing timeout.

        This attribute defines the time interval after which the application shall assume that the to be received data reception has timed out, i.e. the respective data has not been received for that amount of time.

        Args:
            value: The timeout TimeValue to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.timeout = value
        return self


class CompositeNetworkRepresentation(ARObject):
    """
    This meta-class is used to define the network representation of leaf elements of composite application data types.
    """

    # CompositeNetworkRepresentation method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.74, p.181
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                 [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getLeafElementIRef       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setLeafElementIRef       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getNetworkRepresentation [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setNetworkRepresentation [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # This represents that leaf element of an application composite data type. InstanceRef implemented by: ApplicationCompositeElementInPortInterfaceInstanceRef
        self.leafElementIRef: Optional[ApplicationCompositeElementInPortInterfaceInstanceRef] = None

        # The SwDataDefProps owned by the CompositeNetworkRepresentation are used to define the network representation of the leaf element of an Application CompositeDataType. Stereotypes: atpSplitable Tags: atp.Splitkey=networkRepresentation
        self.networkRepresentation: Optional[SwDataDefProps] = None

    def getLeafElementIRef(self) -> Optional[ApplicationCompositeElementInPortInterfaceInstanceRef]:
        """
        Gets the leaf element of an application composite data type.

        This represents that leaf element of an application composite data type. InstanceRef implemented by: ApplicationCompositeElementInPortInterfaceInstanceRef

        Returns:
            ApplicationCompositeElementInPortInterfaceInstanceRef, or None if not set
        """
        return self.leafElementIRef

    def setLeafElementIRef(self, value: Optional[ApplicationCompositeElementInPortInterfaceInstanceRef]) -> "CompositeNetworkRepresentation":
        """
        Sets the leaf element of an application composite data type.
        A None value is a no-op and does not overwrite an existing leaf element reference.

        This represents that leaf element of an application composite data type. InstanceRef implemented by: ApplicationCompositeElementInPortInterfaceInstanceRef

        Args:
            value: The ApplicationCompositeElementInPortInterfaceInstanceRef to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.leafElementIRef = value
        return self

    def getNetworkRepresentation(self) -> Optional[SwDataDefProps]:
        """
        Gets the SwDataDefProps used to define the network representation of the leaf element of an Application CompositeDataType.

        The SwDataDefProps owned by the CompositeNetworkRepresentation are used to define the network representation of the leaf element of an Application CompositeDataType. Stereotypes: atpSplitable Tags: atp.Splitkey=networkRepresentation

        Returns:
            SwDataDefProps, or None if not set
        """
        return self.networkRepresentation

    def setNetworkRepresentation(self, value: Optional[SwDataDefProps]) -> "CompositeNetworkRepresentation":
        """
        Sets the SwDataDefProps used to define the network representation of the leaf element of an Application CompositeDataType.
        A None value is a no-op and does not overwrite an existing network representation.

        The SwDataDefProps owned by the CompositeNetworkRepresentation are used to define the network representation of the leaf element of an Application CompositeDataType. Stereotypes: atpSplitable Tags: atp.Splitkey=networkRepresentation

        Args:
            value: The SwDataDefProps to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.networkRepresentation = value
        return self
        self.networkRepresentation = value
        return self


class TransmissionAcknowledgementRequest(ARObject):
    """
    Requests transmission acknowledgement that data has been sent successfully.
    Success/failure is reported via a SendPoint of a RunnableEntity.
    """

    # TransmissionAcknowledgementRequest method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getTimeout                   [x] impl  [x] docstring  [ ] test
    # [ ] setTimeout                   [x] impl  [x] docstring  [ ] test

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

    # SenderComSpec method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] addCompositeNetworkRepresentation [x] impl  [x] docstring  [ ] test
    # [ ] getCompositeNetworkRepresentations [x] impl  [x] docstring  [ ] test
    # [ ] getDataElementRef            [x] impl  [x] docstring  [ ] test
    # [ ] setDataElementRef            [x] impl  [x] docstring  [ ] test
    # [ ] getNetworkRepresentation     [x] impl  [x] docstring  [ ] test
    # [ ] setNetworkRepresentation     [x] impl  [x] docstring  [ ] test
    # [ ] getHandleOutOfRange          [x] impl  [x] docstring  [ ] test
    # [ ] setHandleOutOfRange          [x] impl  [x] docstring  [ ] test
    # [ ] getTransmissionAcknowledge   [x] impl  [x] docstring  [ ] test
    # [ ] setTransmissionAcknowledge   [x] impl  [x] docstring  [ ] test
    # [ ] getUsesEndToEndProtection    [x] impl  [x] docstring  [ ] test
    # [ ] setUsesEndToEndProtection    [x] impl  [x] docstring  [ ] test

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

    # QueuedSenderComSpec method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()


class NonqueuedSenderComSpec(SenderComSpec):
    """
    Communication attributes for non-queued sender/receiver communication (sender side).
    """

    # NonqueuedSenderComSpec method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getInitValue                 [x] impl  [x] docstring  [ ] test
    # [ ] setInitValue                 [x] impl  [x] docstring  [ ] test

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

    # ClientComSpec method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getOperationRef              [x] impl  [x] docstring  [ ] test
    # [ ] setOperationRef              [x] impl  [x] docstring  [ ] test

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

    # ModeSwitchReceiverComSpec method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getEnhancedModeApi           [x] impl  [x] docstring  [ ] test
    # [ ] setEnhancedModeApi           [x] impl  [x] docstring  [ ] test
    # [ ] getModeGroupRef              [x] impl  [x] docstring  [ ] test
    # [ ] setModeGroupRef              [x] impl  [x] docstring  [ ] test
    # [ ] getSupportsAsynchronousModeSwitch [x] impl  [x] docstring  [ ] test
    # [ ] setSupportsAsynchronousModeSwitch [x] impl  [x] docstring  [ ] test

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

    # NvRequireComSpec method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getInitValue                 [x] impl  [x] docstring  [ ] test
    # [ ] setInitValue                 [x] impl  [x] docstring  [ ] test
    # [ ] getVariableRef               [x] impl  [x] docstring  [ ] test
    # [ ] setVariableRef               [x] impl  [x] docstring  [ ] test

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

    # ParameterRequireComSpec method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getInitValue                 [x] impl  [x] docstring  [ ] test
    # [ ] setInitValue                 [x] impl  [x] docstring  [ ] test
    # [ ] getParameterRef              [x] impl  [x] docstring  [ ] test
    # [ ] setParameterRef              [x] impl  [x] docstring  [ ] test

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

    # ReceiverComSpec method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.60, p.172
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] addCompositeNetworkRepresentation [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getCompositeNetworkRepresentations [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getDataElementRef            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setDataElementRef            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getHandleOutOfRange          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setHandleOutOfRange          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getHandleOutOfRangeStatus    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setHandleOutOfRangeStatus    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMaxDeltaCounterInit       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMaxDeltaCounterInit       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMaxNoNewOrRepeatedData    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMaxNoNewOrRepeatedData    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getNetworkRepresentation     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setNetworkRepresentation     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getReceptionProps            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setReceptionProps            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getReplaceWith               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setReplaceWith               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSyncCounterInit           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSyncCounterInit           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] addTransformationComSpecProps [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTransformationComSpecProps [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] getUsesEndToEndProtection    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setUsesEndToEndProtection    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        if type(self) is ReceiverComSpec:
            raise TypeError("ReceiverComSpec is an abstract class.")
        super().__init__()

        # This represents a CompositeNetworkRepresentation defined in the context of a ReceiverComSpec. The purpose of this aggregation is to be able to specify the network representation of leaf elements of Application CompositeDataTypes.
        self.compositeNetworkRepresentations: List[CompositeNetworkRepresentation] = []

        # Data element these attributes belong to.
        self.dataElementRef: Optional[RefType] = None

        # This attribute controls how values that are out of the specified range are handled according to the values of HandleOutOfRangeEnum.
        self.handleOutOfRange: Optional[HandleOutOfRangeEnum] = None

        # Control the way how return values are created in case of an out-of-range situation.
        self.handleOutOfRangeStatus: Optional[HandleOutOfRangeStatusEnum] = None

        # Initial maximum allowed gap between two counter values of two consecutively received valid Data, i.e. how many subsequent lost data is accepted. For example, if the receiver gets Data with counter 1 and MaxDeltaCounterInit is 1, then at the next reception the receiver can accept Counters with values 2 and 3, but not 4. Note that if the receiver does not receive new Data at a consecutive read, then the receiver increments the tolerance by 1. Caveat: The E2E wrapper approach involves technologies that are not subjected to the AUTOSAR standard and is superseded by the superior E2E transformer approach (which is fully standardized by AUTOSAR). Hence, new projects (without legacy constraints due to carry-over parts) shall use the fully standardized E2E transformer approach.
        self.maxDeltaCounterInit: Optional[PositiveInteger] = None

        # The maximum amount of missing or repeated Data which the receiver does not expect to exceed under normal communication conditions. Caveat: The E2E wrapper approach involves technologies that are not subjected to the AUTOSAR standard and is superseded by the superior E2E transformer approach (which is fully standardized by AUTOSAR). Hence, new projects (without legacy constraints due to carry-over parts) shall use the fully standardized E2E transformer approach.
        self.maxNoNewOrRepeatedData: Optional[PositiveInteger] = None

        # A networkRepresentation is used to define how the data Element is mapped to a communication bus.
        self.networkRepresentation: Optional[SwDataDefProps] = None

        # This aggregation represents the definition transmission props in the context of the enclosing ReceiverComSpec.
        self.receptionProps: Optional[ReceptionComSpecProps] = None

        # This aggregation is used to identify the AutosarData Prototype to be taken for sourcing an external replacement in the out-of-range and invalidValue handling.
        self.replaceWith: Optional[VariableAccess] = None

        # Number of Data required for validating the consistency of the counter that shall be received with a valid counter (i.e. counter within the allowed lock-in range) after the detection of an unexpected behavior of a received counter. Caveat: The E2E wrapper approach involves technologies that are not subjected to the AUTOSAR standard and is superseded by the superior E2E transformer approach (which is fully standardized by AUTOSAR). Hence, new projects (without legacy constraints due to carry-over parts) shall use the fully standardized E2E transformer approach.
        self.syncCounterInit: Optional[PositiveInteger] = None

        # This references the TransformationComSpecProps which define port-specific configuration for data transformation.
        self.transformationComSpecProps: List[TransformationComSpecProps] = []

        # This indicates whether the corresponding dataElement shall be transmitted using end-to-end protection. Caveat: The E2E wrapper approach involves technologies that are not subjected to the AUTOSAR standard and is superseded by the superior E2E transformer approach (which is fully standardized by AUTOSAR). Hence, new projects (without legacy constraints due to carry-over parts) shall use the fully standardized E2E transformer approach.
        self.usesEndToEndProtection: Optional[ARBoolean] = None

    def addCompositeNetworkRepresentation(self, representation: CompositeNetworkRepresentation) -> "ReceiverComSpec":
        """
        This represents a CompositeNetworkRepresentation defined in the context of a ReceiverComSpec. The purpose of this aggregation is to be able to specify the network representation of leaf elements of Application CompositeDataTypes. Stereotypes: atpSplitable Tags: atp.Splitkey=compositeNetworkRepresentation
        A None value is a no-op and does not append anything.
        """
        if representation is not None:
            self.compositeNetworkRepresentations.append(representation)
        return self

    def getCompositeNetworkRepresentations(self) -> List[CompositeNetworkRepresentation]:
        """
        This represents a CompositeNetworkRepresentation defined in the context of a ReceiverComSpec. The purpose of this aggregation is to be able to specify the network representation of leaf elements of Application CompositeDataTypes. Stereotypes: atpSplitable Tags: atp.Splitkey=compositeNetworkRepresentation
        """
        return self.compositeNetworkRepresentations

    def getDataElementRef(self) -> Optional[RefType]:
        """
        Data element these attributes belong to.
        """
        return self.dataElementRef

    def setDataElementRef(self, value: Optional[RefType]) -> "ReceiverComSpec":
        """
        Data element these attributes belong to.
        A None value is a no-op and does not overwrite an existing dataElementRef.
        """
        if value is not None:
            self.dataElementRef = value
        return self

    def getHandleOutOfRange(self) -> Optional["HandleOutOfRangeEnum"]:
        """
        This attribute controls how values that are out of the specified range are handled according to the values of HandleOutOfRangeEnum.
        """
        return self.handleOutOfRange

    def setHandleOutOfRange(self, value: Optional["HandleOutOfRangeEnum"]) -> "ReceiverComSpec":
        """
        This attribute controls how values that are out of the specified range are handled according to the values of HandleOutOfRangeEnum.
        A None value is a no-op and does not overwrite an existing handleOutOfRange.
        """
        if value is not None:
            self.handleOutOfRange = value
        return self

    def getHandleOutOfRangeStatus(self) -> Optional["HandleOutOfRangeStatusEnum"]:
        """
        Control the way how return values are created in case of an out-of-range situation.
        """
        return self.handleOutOfRangeStatus

    def setHandleOutOfRangeStatus(self, value: Optional["HandleOutOfRangeStatusEnum"]) -> "ReceiverComSpec":
        """
        Control the way how return values are created in case of an out-of-range situation.
        A None value is a no-op and does not overwrite an existing handleOutOfRangeStatus.
        """
        if value is not None:
            self.handleOutOfRangeStatus = value
        return self

    def getMaxDeltaCounterInit(self) -> Optional[PositiveInteger]:
        """
        Initial maximum allowed gap between two counter values of two consecutively received valid Data, i.e. how many subsequent lost data is accepted. For example, if the receiver gets Data with counter 1 and MaxDeltaCounterInit is 1, then at the next reception the receiver can accept Counters with values 2 and 3, but not 4. Note that if the receiver does not receive new Data at a consecutive read, then the receiver increments the tolerance by 1. Caveat: The E2E wrapper approach involves technologies that are not subjected to the AUTOSAR standard and is superseded by the superior E2E transformer approach (which is fully standardized by AUTOSAR). Hence, new projects (without legacy constraints due to carry-over parts) shall use the fully standardized E2E transformer approach. Stereotypes: atpVariation
        """
        return self.maxDeltaCounterInit

    def setMaxDeltaCounterInit(self, value: Optional[PositiveInteger]) -> "ReceiverComSpec":
        """
        Initial maximum allowed gap between two counter values of two consecutively received valid Data, i.e. how many subsequent lost data is accepted. For example, if the receiver gets Data with counter 1 and MaxDeltaCounterInit is 1, then at the next reception the receiver can accept Counters with values 2 and 3, but not 4. Note that if the receiver does not receive new Data at a consecutive read, then the receiver increments the tolerance by 1. Caveat: The E2E wrapper approach involves technologies that are not subjected to the AUTOSAR standard and is superseded by the superior E2E transformer approach (which is fully standardized by AUTOSAR). Hence, new projects (without legacy constraints due to carry-over parts) shall use the fully standardized E2E transformer approach. Stereotypes: atpVariation
        A None value is a no-op and does not overwrite an existing maxDeltaCounterInit.
        """
        if value is not None:
            self.maxDeltaCounterInit = value
        return self

    def getMaxNoNewOrRepeatedData(self) -> Optional[PositiveInteger]:
        """
        The maximum amount of missing or repeated Data which the receiver does not expect to exceed under normal communication conditions. Caveat: The E2E wrapper approach involves technologies that are not subjected to the AUTOSAR standard and is superseded by the superior E2E transformer approach (which is fully standardized by AUTOSAR). Hence, new projects (without legacy constraints due to carry-over parts) shall use the fully standardized E2E transformer approach.
        """
        return self.maxNoNewOrRepeatedData

    def setMaxNoNewOrRepeatedData(self, value: Optional[PositiveInteger]) -> "ReceiverComSpec":
        """
        The maximum amount of missing or repeated Data which the receiver does not expect to exceed under normal communication conditions. Caveat: The E2E wrapper approach involves technologies that are not subjected to the AUTOSAR standard and is superseded by the superior E2E transformer approach (which is fully standardized by AUTOSAR). Hence, new projects (without legacy constraints due to carry-over parts) shall use the fully standardized E2E transformer approach.
        A None value is a no-op and does not overwrite an existing maxNoNewOrRepeatedData.
        """
        if value is not None:
            self.maxNoNewOrRepeatedData = value
        return self

    def getNetworkRepresentation(self) -> Optional[SwDataDefProps]:
        """
        A networkRepresentation is used to define how the data Element is mapped to a communication bus. Stereotypes: atpSplitable Tags: atp.Splitkey=networkRepresentation
        """
        return self.networkRepresentation

    def setNetworkRepresentation(self, value: Optional[SwDataDefProps]) -> "ReceiverComSpec":
        """
        A networkRepresentation is used to define how the data Element is mapped to a communication bus. Stereotypes: atpSplitable Tags: atp.Splitkey=networkRepresentation
        A None value is a no-op and does not overwrite an existing networkRepresentation.
        """
        if value is not None:
            self.networkRepresentation = value
        return self

    def getReceptionProps(self) -> Optional["ReceptionComSpecProps"]:
        """
        This aggregation represents the definition transmission props in the context of the enclosing ReceiverComSpec.
        """
        return self.receptionProps

    def setReceptionProps(self, value: Optional["ReceptionComSpecProps"]) -> "ReceiverComSpec":
        """
        This aggregation represents the definition transmission props in the context of the enclosing ReceiverComSpec.
        A None value is a no-op and does not overwrite an existing receptionProps.
        """
        if value is not None:
            self.receptionProps = value
        return self

    def getReplaceWith(self) -> Optional["VariableAccess"]:
        """
        This aggregation is used to identify the AutosarData Prototype to be taken for sourcing an external replacement in the out-of-range and invalidValue handling.
        """
        return self.replaceWith

    def setReplaceWith(self, value: Optional["VariableAccess"]) -> "ReceiverComSpec":
        """
        This aggregation is used to identify the AutosarData Prototype to be taken for sourcing an external replacement in the out-of-range and invalidValue handling.
        A None value is a no-op and does not overwrite an existing replaceWith.
        """
        if value is not None:
            self.replaceWith = value
        return self

    def getSyncCounterInit(self) -> Optional[PositiveInteger]:
        """
        Number of Data required for validating the consistency of the counter that shall be received with a valid counter (i.e. counter within the allowed lock-in range) after the detection of an unexpected behavior of a received counter. Caveat: The E2E wrapper approach involves technologies that are not subjected to the AUTOSAR standard and is superseded by the superior E2E transformer approach (which is fully standardized by AUTOSAR). Hence, new projects (without legacy constraints due to carry-over parts) shall use the fully standardized E2E transformer approach.
        """
        return self.syncCounterInit

    def setSyncCounterInit(self, value: Optional[PositiveInteger]) -> "ReceiverComSpec":
        """
        Number of Data required for validating the consistency of the counter that shall be received with a valid counter (i.e. counter within the allowed lock-in range) after the detection of an unexpected behavior of a received counter. Caveat: The E2E wrapper approach involves technologies that are not subjected to the AUTOSAR standard and is superseded by the superior E2E transformer approach (which is fully standardized by AUTOSAR). Hence, new projects (without legacy constraints due to carry-over parts) shall use the fully standardized E2E transformer approach.
        A None value is a no-op and does not overwrite an existing syncCounterInit.
        """
        if value is not None:
            self.syncCounterInit = value
        return self

    def addTransformationComSpecProps(self, value: Optional["TransformationComSpecProps"]) -> "ReceiverComSpec":
        """
        This references the TransformationComSpecProps which define port-specific configuration for data transformation.
        A None value is a no-op and does not append anything.
        """
        if value is not None:
            self.transformationComSpecProps.append(value)
        return self

    def getTransformationComSpecProps(self) -> List["TransformationComSpecProps"]:
        """
        This references the TransformationComSpecProps which define port-specific configuration for data transformation.
        """
        return self.transformationComSpecProps

    def getUsesEndToEndProtection(self) -> Optional[ARBoolean]:
        """
        This indicates whether the corresponding dataElement shall be transmitted using end-to-end protection. Caveat: The E2E wrapper approach involves technologies that are not subjected to the AUTOSAR standard and is superseded by the superior E2E transformer approach (which is fully standardized by AUTOSAR). Hence, new projects (without legacy constraints due to carry-over parts) shall use the fully standardized E2E transformer approach. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime
        """
        return self.usesEndToEndProtection

    def setUsesEndToEndProtection(self, value: Optional[ARBoolean]) -> "ReceiverComSpec":
        """
        This indicates whether the corresponding dataElement shall be transmitted using end-to-end protection. Caveat: The E2E wrapper approach involves technologies that are not subjected to the AUTOSAR standard and is superseded by the superior E2E transformer approach (which is fully standardized by AUTOSAR). Hence, new projects (without legacy constraints due to carry-over parts) shall use the fully standardized E2E transformer approach. Stereotypes: atpVariation Tags: vh.latestBindingTime=preCompileTime
        A None value is a no-op and does not overwrite an existing usesEndToEndProtection.
        """
        if value is not None:
            self.usesEndToEndProtection = value
        return self


class ModeSwitchedAckRequest(ARObject):
    """
    Requests acknowledgements that a mode switch has been proceeded successfully.
    """

    # ModeSwitchedAckRequest method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getTimeout                   [x] impl  [x] docstring  [ ] test
    # [ ] setTimeout                   [x] impl  [x] docstring  [ ] test

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

    # ModeSwitchSenderComSpec method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getEnhancedModeApi           [x] impl  [x] docstring  [ ] test
    # [ ] setEnhancedModeApi           [x] impl  [x] docstring  [ ] test
    # [ ] getModeGroupRef              [x] impl  [x] docstring  [ ] test
    # [ ] setModeGroupRef              [x] impl  [x] docstring  [ ] test
    # [ ] getModeSwitchedAck           [x] impl  [x] docstring  [ ] test
    # [ ] setModeSwitchedAck           [x] impl  [x] docstring  [ ] test
    # [ ] getQueueLength               [x] impl  [x] docstring  [ ] test
    # [ ] setQueueLength               [x] impl  [x] docstring  [ ] test

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

    # ParameterProvideComSpec method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()


class TransformationComSpecProps(Describable, ABC):
    """
    TransformationComSpecProps holds all the attributes for transformers that are port specific.
    """

    # TransformationComSpecProps method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.86, p.197
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self):
        if type(self) is TransformationComSpecProps:
            raise TypeError("TransformationComSpecProps is an abstract class.")

        super().__init__()


class EndToEndTransformationComSpecProps(TransformationComSpecProps):
    """
    The class EndToEndTransformationComSpecProps specifies port specific configuration
    properties for EndToEnd transformer attributes.
    """

    # EndToEndTransformationComSpecProps method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getClearFromValidToInvalid   [x] impl  [x] docstring  [ ] test
    # [ ] setClearFromValidToInvalid   [x] impl  [x] docstring  [ ] test
    # [ ] getDisableEndToEndCheck      [x] impl  [x] docstring  [ ] test
    # [ ] setDisableEndToEndCheck      [x] impl  [x] docstring  [ ] test
    # [ ] getDisableEndToEndStateMachine [x] impl  [x] docstring  [ ] test
    # [ ] setDisableEndToEndStateMachine [x] impl  [x] docstring  [ ] test
    # [ ] getE2eProfileCompatibilityPropsRef [x] impl  [x] docstring  [ ] test
    # [ ] setE2eProfileCompatibilityPropsRef [x] impl  [x] docstring  [ ] test
    # [ ] getMaxDeltaCounter           [x] impl  [x] docstring  [ ] test
    # [ ] setMaxDeltaCounter           [x] impl  [x] docstring  [ ] test
    # [ ] getMaxErrorStateInit         [x] impl  [x] docstring  [ ] test
    # [ ] setMaxErrorStateInit         [x] impl  [x] docstring  [ ] test
    # [ ] getMaxErrorStateInvalid      [x] impl  [x] docstring  [ ] test
    # [ ] setMaxErrorStateInvalid      [x] impl  [x] docstring  [ ] test
    # [ ] getMaxErrorStateValid        [x] impl  [x] docstring  [ ] test
    # [ ] setMaxErrorStateValid        [x] impl  [x] docstring  [ ] test
    # [ ] getMaxNoNewOrRepeatedData    [x] impl  [x] docstring  [ ] test
    # [ ] setMaxNoNewOrRepeatedData    [x] impl  [x] docstring  [ ] test
    # [ ] getMinOkStateInit            [x] impl  [x] docstring  [ ] test
    # [ ] setMinOkStateInit            [x] impl  [x] docstring  [ ] test
    # [ ] getMinOkStateInvalid         [x] impl  [x] docstring  [ ] test
    # [ ] setMinOkStateInvalid         [x] impl  [x] docstring  [ ] test
    # [ ] getMinOkStateValid           [x] impl  [x] docstring  [ ] test
    # [ ] setMinOkStateValid           [x] impl  [x] docstring  [ ] test
    # [ ] getSyncCounterInit           [x] impl  [x] docstring  [ ] test
    # [ ] setSyncCounterInit           [x] impl  [x] docstring  [ ] test
    # [ ] getWindowSizeInit            [x] impl  [x] docstring  [ ] test
    # [ ] setWindowSizeInit            [x] impl  [x] docstring  [ ] test
    # [ ] getWindowSizeInvalid         [x] impl  [x] docstring  [ ] test
    # [ ] setWindowSizeInvalid         [x] impl  [x] docstring  [ ] test
    # [ ] getWindowSizeValid           [x] impl  [x] docstring  [ ] test
    # [ ] setWindowSizeValid           [x] impl  [x] docstring  [ ] test

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

    # UserDefinedTransformationComSpecProps method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()


class ServerComSpec(PPortComSpec):
    """
    Communication attributes for a server port (PPortPrototype and ClientServerInterface).
    """

    # ServerComSpec method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getOperationRef              [x] impl  [x] docstring  [ ] test
    # [ ] setOperationRef              [x] impl  [x] docstring  [ ] test
    # [ ] getQueueLength               [x] impl  [x] docstring  [ ] test
    # [ ] setQueueLength               [x] impl  [x] docstring  [ ] test
    # [ ] getTransformationComSpecProps [x] impl  [x] docstring  [ ] test
    # [ ] addTransformationComSpecProps [x] impl  [x] docstring  [ ] test

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

    # NvProvideComSpec method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getRamBlockInitValue         [x] impl  [x] docstring  [ ] test
    # [ ] setRamBlockInitValue         [x] impl  [x] docstring  [ ] test
    # [ ] getRomBlockInitValue         [x] impl  [x] docstring  [ ] test
    # [ ] setRomBlockInitValue         [x] impl  [x] docstring  [ ] test
    # [ ] getVariableRef               [x] impl  [x] docstring  [ ] test
    # [ ] setVariableRef               [x] impl  [x] docstring  [ ] test

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

    # NonqueuedReceiverComSpec method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.62, p.173
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getAliveTimeout              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setAliveTimeout              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getEnableUpdate              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setEnableUpdate              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getFilter                    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setFilter                    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getHandleDataStatus          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setHandleDataStatus          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getHandleNeverReceived       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setHandleNeverReceived       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getHandleTimeoutType         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setHandleTimeoutType         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getInitValue                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setInitValue                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTimeoutSubstitutionValue  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTimeoutSubstitutionValue  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # Specify the amount of time (in seconds) after which the software component (via the RTE) needs to be notified if the corresponding data item have not been received according to the specified timing description. If the aliveTimeout attribute is 0 no timeout monitoring shall be performed.
        self.aliveTimeout: Optional[TimeValue] = None

        # This attribute controls whether application code is entitled to check whether the value of the corresponding Variable DataPrototype has been updated.
        self.enableUpdate: Optional[ARBoolean] = None

        # The applicable filter algorithm for filtering the value of the corresponding dataElement.
        self.filter: Optional[DataFilter] = None

        # If this attribute is set to true, then the Rte_IStatus API shall exist. If the attribute does not exist or is set to false, then the Rte_IStatus API may still exist in response to the existence of further conditions.
        self.handleDataStatus: Optional[ARBoolean] = None

        # This attribute specifies whether for the corresponding VariableDataPrototype the "never received" flag is available. If yes, the RTE is supposed to assume that initially the VariableDataPrototype has not been received before. After the first reception of the corresponding VariableDataPrototype the flag is cleared. • If the value of this attribute is set to "true" the flag is required. • If set to "false", the RTE shall not support the "never received" functionality for the corresponding Variable DataPrototype.
        self.handleNeverReceived: Optional[ARBoolean] = None

        # This attribute controls the behavior with respect to the handling of timeouts.
        self.handleTimeoutType: Optional["HandleTimeoutEnum"] = None

        # Initial value to be used in case the sending component is not yet initialized. If the sender also specifies an initial value, then the receiver's value will be used.
        self.initValue: Optional[ValueSpecification] = None

        # This attribute represents the substitution value applicable in the case of a timeout.
        self.timeoutSubstitutionValue: Optional[ValueSpecification] = None

    def getAliveTimeout(self) -> Optional[TimeValue]:
        """
        Specify the amount of time (in seconds) after which the software component (via the RTE) needs to be notified if the corresponding data item have not been received according to the specified timing description. If the aliveTimeout attribute is 0 no timeout monitoring shall be performed.
        """
        return self.aliveTimeout

    def setAliveTimeout(self, value: Optional[TimeValue]) -> "NonqueuedReceiverComSpec":
        """
        Specify the amount of time (in seconds) after which the software component (via the RTE) needs to be notified if the corresponding data item have not been received according to the specified timing description. If the aliveTimeout attribute is 0 no timeout monitoring shall be performed.
        A None value is a no-op and does not overwrite an existing aliveTimeout.
        """
        if value is not None:
            self.aliveTimeout = value
        return self

    def getEnableUpdate(self) -> Optional[ARBoolean]:
        """
        This attribute controls whether application code is entitled to check whether the value of the corresponding Variable DataPrototype has been updated.
        """
        return self.enableUpdate

    def setEnableUpdate(self, value: Optional[ARBoolean]) -> "NonqueuedReceiverComSpec":
        """
        This attribute controls whether application code is entitled to check whether the value of the corresponding Variable DataPrototype has been updated.
        A None value is a no-op and does not overwrite an existing enableUpdate.
        """
        if value is not None:
            self.enableUpdate = value
        return self

    def getFilter(self) -> Optional[DataFilter]:
        """
        The applicable filter algorithm for filtering the value of the corresponding dataElement.
        """
        return self.filter

    def setFilter(self, value: Optional[DataFilter]) -> "NonqueuedReceiverComSpec":
        """
        The applicable filter algorithm for filtering the value of the corresponding dataElement.
        A None value is a no-op and does not overwrite an existing filter.
        """
        if value is not None:
            self.filter = value
        return self

    def getHandleDataStatus(self) -> Optional[ARBoolean]:
        """
        If this attribute is set to true, then the Rte_IStatus API shall exist. If the attribute does not exist or is set to false, then the Rte_IStatus API may still exist in response to the existence of further conditions.
        """
        return self.handleDataStatus

    def setHandleDataStatus(self, value: Optional[ARBoolean]) -> "NonqueuedReceiverComSpec":
        """
        If this attribute is set to true, then the Rte_IStatus API shall exist. If the attribute does not exist or is set to false, then the Rte_IStatus API may still exist in response to the existence of further conditions.
        A None value is a no-op and does not overwrite an existing handleDataStatus.
        """
        if value is not None:
            self.handleDataStatus = value
        return self

    def getHandleNeverReceived(self) -> Optional[ARBoolean]:
        """
        This attribute specifies whether for the corresponding VariableDataPrototype the "never received" flag is available. If yes, the RTE is supposed to assume that initially the VariableDataPrototype has not been received before. After the first reception of the corresponding VariableDataPrototype the flag is cleared. • If the value of this attribute is set to "true" the flag is required. • If set to "false", the RTE shall not support the "never received" functionality for the corresponding Variable DataPrototype.
        """
        return self.handleNeverReceived

    def setHandleNeverReceived(self, value: Optional[ARBoolean]) -> "NonqueuedReceiverComSpec":
        """
        This attribute specifies whether for the corresponding VariableDataPrototype the "never received" flag is available. If yes, the RTE is supposed to assume that initially the VariableDataPrototype has not been received before. After the first reception of the corresponding VariableDataPrototype the flag is cleared. • If the value of this attribute is set to "true" the flag is required. • If set to "false", the RTE shall not support the "never received" functionality for the corresponding Variable DataPrototype.
        A None value is a no-op and does not overwrite an existing handleNeverReceived.
        """
        if value is not None:
            self.handleNeverReceived = value
        return self

    def getHandleTimeoutType(self) -> Optional["HandleTimeoutEnum"]:
        """
        This attribute controls the behavior with respect to the handling of timeouts.
        """
        return self.handleTimeoutType

    def setHandleTimeoutType(self, value: Optional["HandleTimeoutEnum"]) -> "NonqueuedReceiverComSpec":
        """
        This attribute controls the behavior with respect to the handling of timeouts.
        A None value is a no-op and does not overwrite an existing handleTimeoutType.
        """
        if value is not None:
            self.handleTimeoutType = value
        return self

    def getInitValue(self) -> Optional[ValueSpecification]:
        """
        Initial value to be used in case the sending component is not yet initialized. If the sender also specifies an initial value, then the receiver's value will be used.
        """
        return self.initValue

    def setInitValue(self, value: Optional[ValueSpecification]) -> "NonqueuedReceiverComSpec":
        """
        Initial value to be used in case the sending component is not yet initialized. If the sender also specifies an initial value, then the receiver's value will be used.
        A None value is a no-op and does not overwrite an existing initValue.
        """
        if value is not None:
            self.initValue = value
        return self

    def getTimeoutSubstitutionValue(self) -> Optional[ValueSpecification]:
        """
        This attribute represents the substitution value applicable in the case of a timeout.
        """
        return self.timeoutSubstitutionValue

    def setTimeoutSubstitutionValue(self, value: Optional[ValueSpecification]) -> "NonqueuedReceiverComSpec":
        """
        This attribute represents the substitution value applicable in the case of a timeout.
        A None value is a no-op and does not overwrite an existing timeoutSubstitutionValue.
        """
        if value is not None:
            self.timeoutSubstitutionValue = value
        return self


class QueuedReceiverComSpec(ReceiverComSpec):
    """
    Communication attributes specific to queued receiving.
    """

    # QueuedReceiverComSpec method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] getQueueLength               [x] impl  [x] docstring  [ ] test
    # [ ] setQueueLength               [x] impl  [x] docstring  [ ] test

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
    A value of this type is taken for controlling the range checking behavior of the AUTOSAR RTE.
    """

    # HandleOutOfRangeEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.72, p.180
    # Spec verified: R23-11
    # (no methods)

    # The RTE will use the initValue if the actual value is out of the specified bounds. Tags: atp.EnumerationLiteralIndex=0
    DEFAULT = "default"

    # This indicates that the value replacement is sourced from the attribute replaceWith. Tags: atp.EnumerationLiteralIndex=1
    EXTERNAL_REPLACEMENT = "externalReplacement"

    # The RTE will ignore any attempt to send or receive the corresponding dataElement if the value is out of the specified range. Tags: atp.EnumerationLiteralIndex=2
    IGNORE = "ignore"

    # The RTE will use the invalidValue if the value is out of the specified bounds. Tags: atp.EnumerationLiteralIndex=3
    INVALID = "invalid"

    # A range check is not required. Tags: atp.EnumerationLiteralIndex=4
    NONE = "none"

    # The RTE will saturate the value of the dataElement such that it is limited to the applicable upper bound if it is greater than the upper bound. Consequently, it is limited to the applicable lower bound if the value is less than the lower bound. Tags: atp.EnumerationLiteralIndex=5
    SATURATE = "saturate"

    def __init__(self):
        super().__init__(
            [
                HandleOutOfRangeEnum.DEFAULT,
                HandleOutOfRangeEnum.EXTERNAL_REPLACEMENT,
                HandleOutOfRangeEnum.IGNORE,
                HandleOutOfRangeEnum.INVALID,
                HandleOutOfRangeEnum.NONE,
                HandleOutOfRangeEnum.SATURATE,
            ]
        )


class HandleOutOfRangeStatusEnum(AREnum):
    """
    This enumeration defines how the RTE handles values that are out of range.
    """

    # HandleOutOfRangeStatusEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.61, p.172
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # (no methods) — enum value form serialized on ReceiverComSpec.handleOutOfRangeStatus
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    # The RTE sets the return status to RTE_E_OUT_OF_RANGE if the received value is out of range and the attribute handleOutOfRange is not set to "none" or "invalid". Tags: atp.EnumerationLiteralIndex=0
    INDICATE = "indicate"

    # The RTE sets the return status to RTE_E_OK Tags: atp.EnumerationLiteralIndex=1
    SILENT = "silent"

    def __init__(self):
        super().__init__(
            [
                HandleOutOfRangeStatusEnum.INDICATE,
                HandleOutOfRangeStatusEnum.SILENT,
            ]
        )


class HandleTimeoutEnum(AREnum):
    """
    Strategies of handling a reception timeout violation.
    """

    # HandleTimeoutEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.65, p.174
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # (no methods) — enum value form serialized on NonqueuedReceiverComSpec.handleTimeoutType
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    # If set to none no replacement shall take place. Tags: atp.EnumerationLiteralIndex=0
    NONE = "none"

    # If set to replace, the replacement value shall be the ComInitValue. Tags: atp.EnumerationLiteralIndex=1
    REPLACE = "replace"

    # If set to replace, the replacement value shall be the timeout substitution value. Tags: atp.EnumerationLiteralIndex=2
    REPLACE_BY_TIMEOUT_SUBSTITUTION_VALUE = "replaceByTimeoutSubstitutionValue"

    def __init__(self):
        super().__init__(
            (
                HandleTimeoutEnum.NONE,
                HandleTimeoutEnum.REPLACE,
                HandleTimeoutEnum.REPLACE_BY_TIMEOUT_SUBSTITUTION_VALUE,
            )
        )


class TransmissionModeDefinitionEnum(AREnum):
    """
    Enumeration for transmission mode definition.
    """

    # TransmissionModeDefinitionEnum method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    PERIODIC = "periodic"
    ON_CHANGE = "on-change"
    DIRECT = "direct"
    MIXED = "mixed"

    def __init__(self):
        super().__init__(
            (
                TransmissionModeDefinitionEnum.PERIODIC,
                TransmissionModeDefinitionEnum.ON_CHANGE,
                TransmissionModeDefinitionEnum.DIRECT,
                TransmissionModeDefinitionEnum.MIXED,
            )
        )

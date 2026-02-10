"""
AUTOSAR Package - Communication

Package: M2::AUTOSARTemplates::SWComponentTemplate::Communication
"""

from abc import ABC
from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    RefType,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Describable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
)


class PPortComSpec(ARObject, ABC):
    """
    Communication attributes of a provided PortPrototype. This class will
    contain attributes that are valid for all kinds of provide ports,
    independent of client-server or sender-receiver communication patterns.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Communication::PPortComSpec

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 166, Classic Platform
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 199, Foundation R23-11)
    """
    def __init__(self):
        if type(self) is PPortComSpec:
            raise TypeError("PPortComSpec is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    def with_composite(self, value):
        """
        Set composite and return self for chaining.

        Args:
            value: The composite to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_composite("value")
        """
        self.composite = value  # Use property setter (gets validation)
        return self

    def with_transformation(self, value):
        """
        Set transformation and return self for chaining.

        Args:
            value: The transformation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_transformation("value")
        """
        self.transformation = value  # Use property setter (gets validation)
        return self

    def with_composite(self, value):
        """
        Set composite and return self for chaining.

        Args:
            value: The composite to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_composite("value")
        """
        self.composite = value  # Use property setter (gets validation)
        return self

    def with_transformation(self, value):
        """
        Set transformation and return self for chaining.

        Args:
            value: The transformation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_transformation("value")
        """
        self.transformation = value  # Use property setter (gets validation)
        return self

    def with_transformation(self, value):
        """
        Set transformation and return self for chaining.

        Args:
            value: The transformation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_transformation("value")
        """
        self.transformation = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class RPortComSpec(ARObject, ABC):
    """
    Communication attributes of a required PortPrototype. This class will
    contain attributes that are valid for all kinds of require-ports,
    independent of client-server or sender-receiver communication patterns.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Communication::RPortComSpec

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 167, Classic Platform
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 202, Foundation R23-11)
    """
    def __init__(self):
        if type(self) is RPortComSpec:
            raise TypeError("RPortComSpec is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class ReceptionComSpecProps(ARObject):
    """
    This meta-class defines a set of reception attributes which the application
    software is assumed to implement.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Communication::ReceptionComSpecProps

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 174, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute defines the period in which the application check for updated
                # data.
        # This attribute is used for the the E2E protection, but may also indicate data
                # reception period.
        self._dataUpdate: Optional["TimeValue"] = None

    @property
    def data_update(self) -> Optional["TimeValue"]:
        """Get dataUpdate (Pythonic accessor)."""
        return self._dataUpdate

    @data_update.setter
    def data_update(self, value: Optional["TimeValue"]) -> None:
        """
        Set dataUpdate with validation.

        Args:
            value: The dataUpdate to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dataUpdate = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"dataUpdate must be TimeValue or None, got {type(value).__name__}"
            )
        self._dataUpdate = value
                # be received data timed out, i.
        # e.
        # the respective data has not for that amount of time.
        self._timeout: Optional["TimeValue"] = None

    @property
    def timeout(self) -> Optional["TimeValue"]:
        """Get timeout (Pythonic accessor)."""
        return self._timeout

    @timeout.setter
    def timeout(self, value: Optional["TimeValue"]) -> None:
        """
        Set timeout with validation.

        Args:
            value: The timeout to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeout = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"timeout must be TimeValue or None, got {type(value).__name__}"
            )
        self._timeout = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDataUpdate(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for dataUpdate.

        Returns:
            The dataUpdate value

        Note:
            Delegates to data_update property (CODING_RULE_V2_00017)
        """
        return self.data_update  # Delegates to property

    def setDataUpdate(self, value: "TimeValue") -> "ReceptionComSpecProps":
        """
        AUTOSAR-compliant setter for dataUpdate with method chaining.

        Args:
            value: The dataUpdate to set

        Returns:
            self for method chaining

        Note:
            Delegates to data_update property setter (gets validation automatically)
        """
        self.data_update = value  # Delegates to property setter
        return self

    def getTimeout(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for timeout.

        Returns:
            The timeout value

        Note:
            Delegates to timeout property (CODING_RULE_V2_00017)
        """
        return self.timeout  # Delegates to property

    def setTimeout(self, value: "TimeValue") -> "ReceptionComSpecProps":
        """
        AUTOSAR-compliant setter for timeout with method chaining.

        Args:
            value: The timeout to set

        Returns:
            self for method chaining

        Note:
            Delegates to timeout property setter (gets validation automatically)
        """
        self.timeout = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_data_update(self, value: Optional["TimeValue"]) -> "ReceptionComSpecProps":
        """
        Set dataUpdate and return self for chaining.

        Args:
            value: The dataUpdate to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_data_update("value")
        """
        self.data_update = value  # Use property setter (gets validation)
        return self

    def with_timeout(self, value: Optional["TimeValue"]) -> "ReceptionComSpecProps":
        """
        Set timeout and return self for chaining.

        Args:
            value: The timeout to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_timeout("value")
        """
        self.timeout = value  # Use property setter (gets validation)
        return self



class TransmissionComSpecProps(ARObject):
    """
    This meta-class defines a set of transmission attributes which the
    application software is assumed to implement.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Communication::TransmissionComSpecProps

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 179, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2075, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute defines the period in which the application is to transmit the
                # respective data.
        # 1228 Document ID 62: AUTOSAR_CP_TPS_SoftwareComponentTemplate Template
                # R23-11.
        self._dataUpdate: Optional["TimeValue"] = None

    @property
    def data_update(self) -> Optional["TimeValue"]:
        """Get dataUpdate (Pythonic accessor)."""
        return self._dataUpdate

    @data_update.setter
    def data_update(self, value: Optional["TimeValue"]) -> None:
        """
        Set dataUpdate with validation.

        Args:
            value: The dataUpdate to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dataUpdate = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"dataUpdate must be TimeValue or None, got {type(value).__name__}"
            )
        self._dataUpdate = value
        # respective data the assumed to ensure.
        self._minimumSend: Optional["TimeValue"] = None

    @property
    def minimum_send(self) -> Optional["TimeValue"]:
        """Get minimumSend (Pythonic accessor)."""
        return self._minimumSend

    @minimum_send.setter
    def minimum_send(self, value: Optional["TimeValue"]) -> None:
        """
        Set minimumSend with validation.

        Args:
            value: The minimumSend to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._minimumSend = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"minimumSend must be TimeValue or None, got {type(value).__name__}"
            )
        self._minimumSend = value
        # transmit the respective data.
        self._transmission: Optional["TransmissionMode"] = None

    @property
    def transmission(self) -> Optional["TransmissionMode"]:
        """Get transmission (Pythonic accessor)."""
        return self._transmission

    @transmission.setter
    def transmission(self, value: Optional["TransmissionMode"]) -> None:
        """
        Set transmission with validation.

        Args:
            value: The transmission to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._transmission = None
            return

        if not isinstance(value, TransmissionMode):
            raise TypeError(
                f"transmission must be TransmissionMode or None, got {type(value).__name__}"
            )
        self._transmission = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDataUpdate(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for dataUpdate.

        Returns:
            The dataUpdate value

        Note:
            Delegates to data_update property (CODING_RULE_V2_00017)
        """
        return self.data_update  # Delegates to property

    def setDataUpdate(self, value: "TimeValue") -> "TransmissionComSpecProps":
        """
        AUTOSAR-compliant setter for dataUpdate with method chaining.

        Args:
            value: The dataUpdate to set

        Returns:
            self for method chaining

        Note:
            Delegates to data_update property setter (gets validation automatically)
        """
        self.data_update = value  # Delegates to property setter
        return self

    def getMinimumSend(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for minimumSend.

        Returns:
            The minimumSend value

        Note:
            Delegates to minimum_send property (CODING_RULE_V2_00017)
        """
        return self.minimum_send  # Delegates to property

    def setMinimumSend(self, value: "TimeValue") -> "TransmissionComSpecProps":
        """
        AUTOSAR-compliant setter for minimumSend with method chaining.

        Args:
            value: The minimumSend to set

        Returns:
            self for method chaining

        Note:
            Delegates to minimum_send property setter (gets validation automatically)
        """
        self.minimum_send = value  # Delegates to property setter
        return self

    def getTransmission(self) -> "TransmissionMode":
        """
        AUTOSAR-compliant getter for transmission.

        Returns:
            The transmission value

        Note:
            Delegates to transmission property (CODING_RULE_V2_00017)
        """
        return self.transmission  # Delegates to property

    def setTransmission(self, value: "TransmissionMode") -> "TransmissionComSpecProps":
        """
        AUTOSAR-compliant setter for transmission with method chaining.

        Args:
            value: The transmission to set

        Returns:
            self for method chaining

        Note:
            Delegates to transmission property setter (gets validation automatically)
        """
        self.transmission = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_data_update(self, value: Optional["TimeValue"]) -> "TransmissionComSpecProps":
        """
        Set dataUpdate and return self for chaining.

        Args:
            value: The dataUpdate to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_data_update("value")
        """
        self.data_update = value  # Use property setter (gets validation)
        return self

    def with_minimum_send(self, value: Optional["TimeValue"]) -> "TransmissionComSpecProps":
        """
        Set minimumSend and return self for chaining.

        Args:
            value: The minimumSend to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_minimum_send("value")
        """
        self.minimum_send = value  # Use property setter (gets validation)
        return self

    def with_transmission(self, value: Optional["TransmissionMode"]) -> "TransmissionComSpecProps":
        """
        Set transmission and return self for chaining.

        Args:
            value: The transmission to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_transmission("value")
        """
        self.transmission = value  # Use property setter (gets validation)
        return self



class TransmissionAcknowledgementRequest(ARObject):
    """
    Requests transmission acknowledgement that data has been sent successfully.
    Success/failure is reported via a SendPoint of a RunnableEntity.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Communication::TransmissionAcknowledgementRequest

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 180, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Number of seconds before an error is reported or in case redundancy, the
        # value is sent again.
        self._timeout: Optional["TimeValue"] = None

    @property
    def timeout(self) -> Optional["TimeValue"]:
        """Get timeout (Pythonic accessor)."""
        return self._timeout

    @timeout.setter
    def timeout(self, value: Optional["TimeValue"]) -> None:
        """
        Set timeout with validation.

        Args:
            value: The timeout to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeout = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"timeout must be TimeValue or None, got {type(value).__name__}"
            )
        self._timeout = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTimeout(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for timeout.

        Returns:
            The timeout value

        Note:
            Delegates to timeout property (CODING_RULE_V2_00017)
        """
        return self.timeout  # Delegates to property

    def setTimeout(self, value: "TimeValue") -> "TransmissionAcknowledgementRequest":
        """
        AUTOSAR-compliant setter for timeout with method chaining.

        Args:
            value: The timeout to set

        Returns:
            self for method chaining

        Note:
            Delegates to timeout property setter (gets validation automatically)
        """
        self.timeout = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_timeout(self, value: Optional["TimeValue"]) -> "TransmissionAcknowledgementRequest":
        """
        Set timeout and return self for chaining.

        Args:
            value: The timeout to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_timeout("value")
        """
        self.timeout = value  # Use property setter (gets validation)
        return self



class CompositeNetworkRepresentation(ARObject):
    """
    This meta-class is used to define the network representation of leaf
    elements of composite application data types.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Communication::CompositeNetworkRepresentation

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 181, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # data type.
        # by: ApplicationComposite.
        self._leafElementElementInPortInterfaceInstanceRef: Optional["ApplicationComposite"] = None

    @property
    def leaf_element_element_in_port_interface_instance_ref(self) -> Optional["ApplicationComposite"]:
        """Get leafElementElementInPortInterfaceInstanceRef (Pythonic accessor)."""
        return self._leafElementElementInPortInterfaceInstanceRef

    @leaf_element_element_in_port_interface_instance_ref.setter
    def leaf_element_element_in_port_interface_instance_ref(self, value: Optional["ApplicationComposite"]) -> None:
        """
        Set leafElementElementInPortInterfaceInstanceRef with validation.

        Args:
            value: The leafElementElementInPortInterfaceInstanceRef to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._leafElementElementInPortInterfaceInstanceRef = None
            return

        if not isinstance(value, ApplicationComposite):
            raise TypeError(
                f"leafElementElementInPortInterfaceInstanceRef must be ApplicationComposite or None, got {type(value).__name__}"
            )
        self._leafElementElementInPortInterfaceInstanceRef = value
        # network the leaf element of an Application.
        self._network: Optional["SwDataDefProps"] = None

    @property
    def network(self) -> Optional["SwDataDefProps"]:
        """Get network (Pythonic accessor)."""
        return self._network

    @network.setter
    def network(self, value: Optional["SwDataDefProps"]) -> None:
        """
        Set network with validation.

        Args:
            value: The network to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._network = None
            return

        if not isinstance(value, SwDataDefProps):
            raise TypeError(
                f"network must be SwDataDefProps or None, got {type(value).__name__}"
            )
        self._network = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getLeafElementElementInPortInterfaceInstanceRef(self) -> "ApplicationComposite":
        """
        AUTOSAR-compliant getter for leafElementElementInPortInterfaceInstanceRef.

        Returns:
            The leafElementElementInPortInterfaceInstanceRef value

        Note:
            Delegates to leaf_element_element_in_port_interface_instance_ref property (CODING_RULE_V2_00017)
        """
        return self.leaf_element_element_in_port_interface_instance_ref  # Delegates to property

    def setLeafElementElementInPortInterfaceInstanceRef(self, value: "ApplicationComposite") -> "CompositeNetworkRepresentation":
        """
        AUTOSAR-compliant setter for leafElementElementInPortInterfaceInstanceRef with method chaining.

        Args:
            value: The leafElementElementInPortInterfaceInstanceRef to set

        Returns:
            self for method chaining

        Note:
            Delegates to leaf_element_element_in_port_interface_instance_ref property setter (gets validation automatically)
        """
        self.leaf_element_element_in_port_interface_instance_ref = value  # Delegates to property setter
        return self

    def getNetwork(self) -> "SwDataDefProps":
        """
        AUTOSAR-compliant getter for network.

        Returns:
            The network value

        Note:
            Delegates to network property (CODING_RULE_V2_00017)
        """
        return self.network  # Delegates to property

    def setNetwork(self, value: "SwDataDefProps") -> "CompositeNetworkRepresentation":
        """
        AUTOSAR-compliant setter for network with method chaining.

        Args:
            value: The network to set

        Returns:
            self for method chaining

        Note:
            Delegates to network property setter (gets validation automatically)
        """
        self.network = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_leaf_element_element_in_port_interface_instance_ref(self, value: Optional["ApplicationComposite"]) -> "CompositeNetworkRepresentation":
        """
        Set leafElementElementInPortInterfaceInstanceRef and return self for chaining.

        Args:
            value: The leafElementElementInPortInterfaceInstanceRef to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_leaf_element_element_in_port_interface_instance_ref("value")
        """
        self.leaf_element_element_in_port_interface_instance_ref = value  # Use property setter (gets validation)
        return self

    def with_network(self, value: Optional["SwDataDefProps"]) -> "CompositeNetworkRepresentation":
        """
        Set network and return self for chaining.

        Args:
            value: The network to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_network("value")
        """
        self.network = value  # Use property setter (gets validation)
        return self



class ModeSwitchedAckRequest(ARObject):
    """
    Requests acknowledgements that a mode switch has been proceeded successfully

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Communication::ModeSwitchedAckRequest

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 190, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Number of seconds before an error is reported or in case redundancy, the
        # value is sent again.
        self._timeout: Optional["TimeValue"] = None

    @property
    def timeout(self) -> Optional["TimeValue"]:
        """Get timeout (Pythonic accessor)."""
        return self._timeout

    @timeout.setter
    def timeout(self, value: Optional["TimeValue"]) -> None:
        """
        Set timeout with validation.

        Args:
            value: The timeout to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeout = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"timeout must be TimeValue or None, got {type(value).__name__}"
            )
        self._timeout = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTimeout(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for timeout.

        Returns:
            The timeout value

        Note:
            Delegates to timeout property (CODING_RULE_V2_00017)
        """
        return self.timeout  # Delegates to property

    def setTimeout(self, value: "TimeValue") -> "ModeSwitchedAckRequest":
        """
        AUTOSAR-compliant setter for timeout with method chaining.

        Args:
            value: The timeout to set

        Returns:
            self for method chaining

        Note:
            Delegates to timeout property setter (gets validation automatically)
        """
        self.timeout = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_timeout(self, value: Optional["TimeValue"]) -> "ModeSwitchedAckRequest":
        """
        Set timeout and return self for chaining.

        Args:
            value: The timeout to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_timeout("value")
        """
        self.timeout = value  # Use property setter (gets validation)
        return self



class TransformationComSpecProps(Describable, ABC):
    """
    TransformationComSpecProps holds all the attributes for transformers that
    are port specific.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Communication::TransformationComSpecProps

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 196, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2075, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is TransformationComSpecProps:
            raise TypeError("TransformationComSpecProps is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class SenderComSpec(PPortComSpec, ABC):
    """
    Communication attributes for a sender port (PPortPrototype typed by
    SenderReceiverInterface).

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Communication::SenderComSpec

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 178, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2054, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is SenderComSpec:
            raise TypeError("SenderComSpec is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents a CompositeNetworkRepresentation defined in the context of a
                # SenderComSpec.
        # atpSplitable.
        self._composite: List["CompositeNetwork"] = []

    @property
    def composite(self) -> List["CompositeNetwork"]:
        """Get composite (Pythonic accessor)."""
        return self._composite
        # Data element these quality of service attributes apply to.
        self._dataElement: Optional["RefType"] = None

    @property
    def data_element(self) -> Optional["RefType"]:
        """Get dataElement (Pythonic accessor)."""
        return self._dataElement

    @data_element.setter
    def data_element(self, value: Optional["RefType"]) -> None:
        """
        Set dataElement with validation.

        Args:
            value: The dataElement to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dataElement = None
            return

        self._dataElement = value
        self._handleOutOf: Optional["HandleOutOfRange"] = None

    @property
    def handle_out_of(self) -> Optional["HandleOutOfRange"]:
        """Get handleOutOf (Pythonic accessor)."""
        return self._handleOutOf

    @handle_out_of.setter
    def handle_out_of(self, value: Optional["HandleOutOfRange"]) -> None:
        """
        Set handleOutOf with validation.

        Args:
            value: The handleOutOf to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._handleOutOf = None
            return

        if not isinstance(value, HandleOutOfRange):
            raise TypeError(
                f"handleOutOf must be HandleOutOfRange or None, got {type(value).__name__}"
            )
        self._handleOutOf = value
        # communication bus.
        self._network: Optional["SwDataDefProps"] = None

    @property
    def network(self) -> Optional["SwDataDefProps"]:
        """Get network (Pythonic accessor)."""
        return self._network

    @network.setter
    def network(self, value: Optional["SwDataDefProps"]) -> None:
        """
        Set network with validation.

        Args:
            value: The network to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._network = None
            return

        if not isinstance(value, SwDataDefProps):
            raise TypeError(
                f"network must be SwDataDefProps or None, got {type(value).__name__}"
            )
        self._network = value
                # of the enclosing SenderComSpec.
        # 1228 Document ID 62: AUTOSAR_CP_TPS_SoftwareComponentTemplate Template
                # R23-11.
        self._transmission: Optional["TransmissionComSpec"] = None

    @property
    def transmission(self) -> Optional["TransmissionComSpec"]:
        """Get transmission (Pythonic accessor)."""
        return self._transmission

    @transmission.setter
    def transmission(self, value: Optional["TransmissionComSpec"]) -> None:
        """
        Set transmission with validation.

        Args:
            value: The transmission to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._transmission = None
            return

        if not isinstance(value, TransmissionComSpec):
            raise TypeError(
                f"transmission must be TransmissionComSpec or None, got {type(value).__name__}"
            )
        self._transmission = value
        # end-to-end protection.
        self._usesEndToEnd: Optional["Boolean"] = None

    @property
    def uses_end_to_end(self) -> Optional["Boolean"]:
        """Get usesEndToEnd (Pythonic accessor)."""
        return self._usesEndToEnd

    @uses_end_to_end.setter
    def uses_end_to_end(self, value: Optional["Boolean"]) -> None:
        """
        Set usesEndToEnd with validation.

        Args:
            value: The usesEndToEnd to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._usesEndToEnd = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"usesEndToEnd must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._usesEndToEnd = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getComposite(self) -> List["CompositeNetwork"]:
        """
        AUTOSAR-compliant getter for composite.

        Returns:
            The composite value

        Note:
            Delegates to composite property (CODING_RULE_V2_00017)
        """
        return self.composite  # Delegates to property

    def getDataElement(self) -> "RefType":
        """
        AUTOSAR-compliant getter for dataElement.

        Returns:
            The dataElement value

        Note:
            Delegates to data_element property (CODING_RULE_V2_00017)
        """
        return self.data_element  # Delegates to property

    def setDataElement(self, value: "RefType") -> "SenderComSpec":
        """
        AUTOSAR-compliant setter for dataElement with method chaining.

        Args:
            value: The dataElement to set

        Returns:
            self for method chaining

        Note:
            Delegates to data_element property setter (gets validation automatically)
        """
        self.data_element = value  # Delegates to property setter
        return self

    def getHandleOutOf(self) -> "HandleOutOfRange":
        """
        AUTOSAR-compliant getter for handleOutOf.

        Returns:
            The handleOutOf value

        Note:
            Delegates to handle_out_of property (CODING_RULE_V2_00017)
        """
        return self.handle_out_of  # Delegates to property

    def setHandleOutOf(self, value: "HandleOutOfRange") -> "SenderComSpec":
        """
        AUTOSAR-compliant setter for handleOutOf with method chaining.

        Args:
            value: The handleOutOf to set

        Returns:
            self for method chaining

        Note:
            Delegates to handle_out_of property setter (gets validation automatically)
        """
        self.handle_out_of = value  # Delegates to property setter
        return self

    def getNetwork(self) -> "SwDataDefProps":
        """
        AUTOSAR-compliant getter for network.

        Returns:
            The network value

        Note:
            Delegates to network property (CODING_RULE_V2_00017)
        """
        return self.network  # Delegates to property

    def setNetwork(self, value: "SwDataDefProps") -> "SenderComSpec":
        """
        AUTOSAR-compliant setter for network with method chaining.

        Args:
            value: The network to set

        Returns:
            self for method chaining

        Note:
            Delegates to network property setter (gets validation automatically)
        """
        self.network = value  # Delegates to property setter
        return self

    def getTransmission(self) -> "TransmissionComSpec":
        """
        AUTOSAR-compliant getter for transmission.

        Returns:
            The transmission value

        Note:
            Delegates to transmission property (CODING_RULE_V2_00017)
        """
        return self.transmission  # Delegates to property

    def setTransmission(self, value: "TransmissionComSpec") -> "SenderComSpec":
        """
        AUTOSAR-compliant setter for transmission with method chaining.

        Args:
            value: The transmission to set

        Returns:
            self for method chaining

        Note:
            Delegates to transmission property setter (gets validation automatically)
        """
        self.transmission = value  # Delegates to property setter
        return self

    def getUsesEndToEnd(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for usesEndToEnd.

        Returns:
            The usesEndToEnd value

        Note:
            Delegates to uses_end_to_end property (CODING_RULE_V2_00017)
        """
        return self.uses_end_to_end  # Delegates to property

    def setUsesEndToEnd(self, value: "Boolean") -> "SenderComSpec":
        """
        AUTOSAR-compliant setter for usesEndToEnd with method chaining.

        Args:
            value: The usesEndToEnd to set

        Returns:
            self for method chaining

        Note:
            Delegates to uses_end_to_end property setter (gets validation automatically)
        """
        self.uses_end_to_end = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_data_element(self, value: Optional[RefType]) -> "SenderComSpec":
        """
        Set dataElement and return self for chaining.

        Args:
            value: The dataElement to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_data_element("value")
        """
        self.data_element = value  # Use property setter (gets validation)
        return self

    def with_handle_out_of(self, value: Optional["HandleOutOfRange"]) -> "SenderComSpec":
        """
        Set handleOutOf and return self for chaining.

        Args:
            value: The handleOutOf to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_handle_out_of("value")
        """
        self.handle_out_of = value  # Use property setter (gets validation)
        return self

    def with_network(self, value: Optional["SwDataDefProps"]) -> "SenderComSpec":
        """
        Set network and return self for chaining.

        Args:
            value: The network to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_network("value")
        """
        self.network = value  # Use property setter (gets validation)
        return self

    def with_transmission(self, value: Optional["TransmissionComSpec"]) -> "SenderComSpec":
        """
        Set transmission and return self for chaining.

        Args:
            value: The transmission to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_transmission("value")
        """
        self.transmission = value  # Use property setter (gets validation)
        return self

    def with_uses_end_to_end(self, value: Optional["Boolean"]) -> "SenderComSpec":
        """
        Set usesEndToEnd and return self for chaining.

        Args:
            value: The usesEndToEnd to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_uses_end_to_end("value")
        """
        self.uses_end_to_end = value  # Use property setter (gets validation)
        return self



class ServerComSpec(PPortComSpec):
    """
    Communication attributes for a server port (PPortPrototype and
    ClientServerInterface).

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Communication::ServerComSpec

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 188, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Operation these communication attributes apply to.
        self._operation: Optional["ClientServerOperation"] = None

    @property
    def operation(self) -> Optional["ClientServerOperation"]:
        """Get operation (Pythonic accessor)."""
        return self._operation

    @operation.setter
    def operation(self, value: Optional["ClientServerOperation"]) -> None:
        """
        Set operation with validation.

        Args:
            value: The operation to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._operation = None
            return

        if not isinstance(value, ClientServerOperation):
            raise TypeError(
                f"operation must be ClientServerOperation or None, got {type(value).__name__}"
            )
        self._operation = value
        # The queue is the RTE.
        # The value shall be greater or 1.
        # Setting the value of queueLength to 1 implies requests are rejected while
                # another request earlier is being processed.
        self._queueLength: Optional["PositiveInteger"] = None

    @property
    def queue_length(self) -> Optional["PositiveInteger"]:
        """Get queueLength (Pythonic accessor)."""
        return self._queueLength

    @queue_length.setter
    def queue_length(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set queueLength with validation.

        Args:
            value: The queueLength to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._queueLength = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"queueLength must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._queueLength = value
        # configuration for data transformation.
        self._transformation: List["TransformationCom"] = []

    @property
    def transformation(self) -> List["TransformationCom"]:
        """Get transformation (Pythonic accessor)."""
        return self._transformation

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getOperation(self) -> "ClientServerOperation":
        """
        AUTOSAR-compliant getter for operation.

        Returns:
            The operation value

        Note:
            Delegates to operation property (CODING_RULE_V2_00017)
        """
        return self.operation  # Delegates to property

    def setOperation(self, value: "ClientServerOperation") -> "ServerComSpec":
        """
        AUTOSAR-compliant setter for operation with method chaining.

        Args:
            value: The operation to set

        Returns:
            self for method chaining

        Note:
            Delegates to operation property setter (gets validation automatically)
        """
        self.operation = value  # Delegates to property setter
        return self

    def getQueueLength(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for queueLength.

        Returns:
            The queueLength value

        Note:
            Delegates to queue_length property (CODING_RULE_V2_00017)
        """
        return self.queue_length  # Delegates to property

    def setQueueLength(self, value: "PositiveInteger") -> "ServerComSpec":
        """
        AUTOSAR-compliant setter for queueLength with method chaining.

        Args:
            value: The queueLength to set

        Returns:
            self for method chaining

        Note:
            Delegates to queue_length property setter (gets validation automatically)
        """
        self.queue_length = value  # Delegates to property setter
        return self

    def getTransformation(self) -> List["TransformationCom"]:
        """
        AUTOSAR-compliant getter for transformation.

        Returns:
            The transformation value

        Note:
            Delegates to transformation property (CODING_RULE_V2_00017)
        """
        return self.transformation  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_operation(self, value: Optional["ClientServerOperation"]) -> "ServerComSpec":
        """
        Set operation and return self for chaining.

        Args:
            value: The operation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_operation("value")
        """
        self.operation = value  # Use property setter (gets validation)
        return self

    def with_queue_length(self, value: Optional["PositiveInteger"]) -> "ServerComSpec":
        """
        Set queueLength and return self for chaining.

        Args:
            value: The queueLength to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_queue_length("value")
        """
        self.queue_length = value  # Use property setter (gets validation)
        return self



class ModeSwitchSenderComSpec(PPortComSpec):
    """
    Communication attributes of PPortPrototypes with respect to mode
    communication

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Communication::ModeSwitchSenderComSpec

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 190, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This controls the creation of the enhanced mode API that information about
                # the previous mode and the next set to "true" the enhanced mode API is be
                # generated.
        # For more details please refer SWS_RTE.
        self._enhancedMode: Optional["Boolean"] = None

    @property
    def enhanced_mode(self) -> Optional["Boolean"]:
        """Get enhancedMode (Pythonic accessor)."""
        return self._enhancedMode

    @enhanced_mode.setter
    def enhanced_mode(self, value: Optional["Boolean"]) -> None:
        """
        Set enhancedMode with validation.

        Args:
            value: The enhancedMode to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._enhancedMode = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"enhancedMode must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._enhancedMode = value
        # attributes apply.
        self._modeGroup: Optional["RefType"] = None

    @property
    def mode_group(self) -> Optional["RefType"]:
        """Get modeGroup (Pythonic accessor)."""
        return self._modeGroup

    @mode_group.setter
    def mode_group(self, value: Optional["RefType"]) -> None:
        """
        Set modeGroup with validation.

        Args:
            value: The modeGroup to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._modeGroup = None
            return

        self._modeGroup = value
        # of the mode switch request is.
        self._modeSwitched: Optional["ModeSwitchedAck"] = None

    @property
    def mode_switched(self) -> Optional["ModeSwitchedAck"]:
        """Get modeSwitched (Pythonic accessor)."""
        return self._modeSwitched

    @mode_switched.setter
    def mode_switched(self, value: Optional["ModeSwitchedAck"]) -> None:
        """
        Set modeSwitched with validation.

        Args:
            value: The modeSwitched to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._modeSwitched = None
            return

        if not isinstance(value, ModeSwitchedAck):
            raise TypeError(
                f"modeSwitched must be ModeSwitchedAck or None, got {type(value).__name__}"
            )
        self._modeSwitched = value
        # The queue is the RTE.
        # The value shall be greater or 1.
        # Setting the value of queueLength to 1 implies requests are rejected while
                # another request earlier is being processed.
        self._queueLength: Optional["PositiveInteger"] = None

    @property
    def queue_length(self) -> Optional["PositiveInteger"]:
        """Get queueLength (Pythonic accessor)."""
        return self._queueLength

    @queue_length.setter
    def queue_length(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set queueLength with validation.

        Args:
            value: The queueLength to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._queueLength = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"queueLength must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._queueLength = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEnhancedMode(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for enhancedMode.

        Returns:
            The enhancedMode value

        Note:
            Delegates to enhanced_mode property (CODING_RULE_V2_00017)
        """
        return self.enhanced_mode  # Delegates to property

    def setEnhancedMode(self, value: "Boolean") -> "ModeSwitchSenderComSpec":
        """
        AUTOSAR-compliant setter for enhancedMode with method chaining.

        Args:
            value: The enhancedMode to set

        Returns:
            self for method chaining

        Note:
            Delegates to enhanced_mode property setter (gets validation automatically)
        """
        self.enhanced_mode = value  # Delegates to property setter
        return self

    def getModeGroup(self) -> "RefType":
        """
        AUTOSAR-compliant getter for modeGroup.

        Returns:
            The modeGroup value

        Note:
            Delegates to mode_group property (CODING_RULE_V2_00017)
        """
        return self.mode_group  # Delegates to property

    def setModeGroup(self, value: "RefType") -> "ModeSwitchSenderComSpec":
        """
        AUTOSAR-compliant setter for modeGroup with method chaining.

        Args:
            value: The modeGroup to set

        Returns:
            self for method chaining

        Note:
            Delegates to mode_group property setter (gets validation automatically)
        """
        self.mode_group = value  # Delegates to property setter
        return self

    def getModeSwitched(self) -> "ModeSwitchedAck":
        """
        AUTOSAR-compliant getter for modeSwitched.

        Returns:
            The modeSwitched value

        Note:
            Delegates to mode_switched property (CODING_RULE_V2_00017)
        """
        return self.mode_switched  # Delegates to property

    def setModeSwitched(self, value: "ModeSwitchedAck") -> "ModeSwitchSenderComSpec":
        """
        AUTOSAR-compliant setter for modeSwitched with method chaining.

        Args:
            value: The modeSwitched to set

        Returns:
            self for method chaining

        Note:
            Delegates to mode_switched property setter (gets validation automatically)
        """
        self.mode_switched = value  # Delegates to property setter
        return self

    def getQueueLength(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for queueLength.

        Returns:
            The queueLength value

        Note:
            Delegates to queue_length property (CODING_RULE_V2_00017)
        """
        return self.queue_length  # Delegates to property

    def setQueueLength(self, value: "PositiveInteger") -> "ModeSwitchSenderComSpec":
        """
        AUTOSAR-compliant setter for queueLength with method chaining.

        Args:
            value: The queueLength to set

        Returns:
            self for method chaining

        Note:
            Delegates to queue_length property setter (gets validation automatically)
        """
        self.queue_length = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_enhanced_mode(self, value: Optional["Boolean"]) -> "ModeSwitchSenderComSpec":
        """
        Set enhancedMode and return self for chaining.

        Args:
            value: The enhancedMode to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_enhanced_mode("value")
        """
        self.enhanced_mode = value  # Use property setter (gets validation)
        return self

    def with_mode_group(self, value: Optional[RefType]) -> "ModeSwitchSenderComSpec":
        """
        Set modeGroup and return self for chaining.

        Args:
            value: The modeGroup to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mode_group("value")
        """
        self.mode_group = value  # Use property setter (gets validation)
        return self

    def with_mode_switched(self, value: Optional["ModeSwitchedAck"]) -> "ModeSwitchSenderComSpec":
        """
        Set modeSwitched and return self for chaining.

        Args:
            value: The modeSwitched to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mode_switched("value")
        """
        self.mode_switched = value  # Use property setter (gets validation)
        return self

    def with_queue_length(self, value: Optional["PositiveInteger"]) -> "ModeSwitchSenderComSpec":
        """
        Set queueLength and return self for chaining.

        Args:
            value: The queueLength to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_queue_length("value")
        """
        self.queue_length = value  # Use property setter (gets validation)
        return self



class ParameterProvideComSpec(PPortComSpec):
    """
    "Communication" specification that applies to parameters on the provided
    side of a connection.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Communication::ParameterProvideComSpec

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 192, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The initial value applicable for the corresponding.
        self._initValue: Optional["ValueSpecification"] = None

    @property
    def init_value(self) -> Optional["ValueSpecification"]:
        """Get initValue (Pythonic accessor)."""
        return self._initValue

    @init_value.setter
    def init_value(self, value: Optional["ValueSpecification"]) -> None:
        """
        Set initValue with validation.

        Args:
            value: The initValue to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._initValue = None
            return

        if not isinstance(value, ValueSpecification):
            raise TypeError(
                f"initValue must be ValueSpecification or None, got {type(value).__name__}"
            )
        self._initValue = value
        self._parameter: Optional["ParameterData"] = None

    @property
    def parameter(self) -> Optional["ParameterData"]:
        """Get parameter (Pythonic accessor)."""
        return self._parameter

    @parameter.setter
    def parameter(self, value: Optional["ParameterData"]) -> None:
        """
        Set parameter with validation.

        Args:
            value: The parameter to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._parameter = None
            return

        if not isinstance(value, ParameterData):
            raise TypeError(
                f"parameter must be ParameterData or None, got {type(value).__name__}"
            )
        self._parameter = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getInitValue(self) -> "ValueSpecification":
        """
        AUTOSAR-compliant getter for initValue.

        Returns:
            The initValue value

        Note:
            Delegates to init_value property (CODING_RULE_V2_00017)
        """
        return self.init_value  # Delegates to property

    def setInitValue(self, value: "ValueSpecification") -> "ParameterProvideComSpec":
        """
        AUTOSAR-compliant setter for initValue with method chaining.

        Args:
            value: The initValue to set

        Returns:
            self for method chaining

        Note:
            Delegates to init_value property setter (gets validation automatically)
        """
        self.init_value = value  # Delegates to property setter
        return self

    def getParameter(self) -> "ParameterData":
        """
        AUTOSAR-compliant getter for parameter.

        Returns:
            The parameter value

        Note:
            Delegates to parameter property (CODING_RULE_V2_00017)
        """
        return self.parameter  # Delegates to property

    def setParameter(self, value: "ParameterData") -> "ParameterProvideComSpec":
        """
        AUTOSAR-compliant setter for parameter with method chaining.

        Args:
            value: The parameter to set

        Returns:
            self for method chaining

        Note:
            Delegates to parameter property setter (gets validation automatically)
        """
        self.parameter = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_init_value(self, value: Optional["ValueSpecification"]) -> "ParameterProvideComSpec":
        """
        Set initValue and return self for chaining.

        Args:
            value: The initValue to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_init_value("value")
        """
        self.init_value = value  # Use property setter (gets validation)
        return self

    def with_parameter(self, value: Optional["ParameterData"]) -> "ParameterProvideComSpec":
        """
        Set parameter and return self for chaining.

        Args:
            value: The parameter to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_parameter("value")
        """
        self.parameter = value  # Use property setter (gets validation)
        return self



class NvProvideComSpec(PPortComSpec):
    """
    Communication attributes of PPortPrototypes with respect to Nv data
    communication on the provided side.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Communication::NvProvideComSpec

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 195, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the initial value of the RAM Block that to the referenced
        # variable.
        self._ramBlockInit: Optional["ValueSpecification"] = None

    @property
    def ram_block_init(self) -> Optional["ValueSpecification"]:
        """Get ramBlockInit (Pythonic accessor)."""
        return self._ramBlockInit

    @ram_block_init.setter
    def ram_block_init(self, value: Optional["ValueSpecification"]) -> None:
        """
        Set ramBlockInit with validation.

        Args:
            value: The ramBlockInit to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ramBlockInit = None
            return

        if not isinstance(value, ValueSpecification):
            raise TypeError(
                f"ramBlockInit must be ValueSpecification or None, got {type(value).__name__}"
            )
        self._ramBlockInit = value
        # variable.
        self._romBlockInit: Optional["ValueSpecification"] = None

    @property
    def rom_block_init(self) -> Optional["ValueSpecification"]:
        """Get romBlockInit (Pythonic accessor)."""
        return self._romBlockInit

    @rom_block_init.setter
    def rom_block_init(self, value: Optional["ValueSpecification"]) -> None:
        """
        Set romBlockInit with validation.

        Args:
            value: The romBlockInit to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._romBlockInit = None
            return

        if not isinstance(value, ValueSpecification):
            raise TypeError(
                f"romBlockInit must be ValueSpecification or None, got {type(value).__name__}"
            )
        self._romBlockInit = value
        self._variable: Optional["RefType"] = None

    @property
    def variable(self) -> Optional["RefType"]:
        """Get variable (Pythonic accessor)."""
        return self._variable

    @variable.setter
    def variable(self, value: Optional["RefType"]) -> None:
        """
        Set variable with validation.

        Args:
            value: The variable to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._variable = None
            return

        self._variable = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getRamBlockInit(self) -> "ValueSpecification":
        """
        AUTOSAR-compliant getter for ramBlockInit.

        Returns:
            The ramBlockInit value

        Note:
            Delegates to ram_block_init property (CODING_RULE_V2_00017)
        """
        return self.ram_block_init  # Delegates to property

    def setRamBlockInit(self, value: "ValueSpecification") -> "NvProvideComSpec":
        """
        AUTOSAR-compliant setter for ramBlockInit with method chaining.

        Args:
            value: The ramBlockInit to set

        Returns:
            self for method chaining

        Note:
            Delegates to ram_block_init property setter (gets validation automatically)
        """
        self.ram_block_init = value  # Delegates to property setter
        return self

    def getRomBlockInit(self) -> "ValueSpecification":
        """
        AUTOSAR-compliant getter for romBlockInit.

        Returns:
            The romBlockInit value

        Note:
            Delegates to rom_block_init property (CODING_RULE_V2_00017)
        """
        return self.rom_block_init  # Delegates to property

    def setRomBlockInit(self, value: "ValueSpecification") -> "NvProvideComSpec":
        """
        AUTOSAR-compliant setter for romBlockInit with method chaining.

        Args:
            value: The romBlockInit to set

        Returns:
            self for method chaining

        Note:
            Delegates to rom_block_init property setter (gets validation automatically)
        """
        self.rom_block_init = value  # Delegates to property setter
        return self

    def getVariable(self) -> "RefType":
        """
        AUTOSAR-compliant getter for variable.

        Returns:
            The variable value

        Note:
            Delegates to variable property (CODING_RULE_V2_00017)
        """
        return self.variable  # Delegates to property

    def setVariable(self, value: "RefType") -> "NvProvideComSpec":
        """
        AUTOSAR-compliant setter for variable with method chaining.

        Args:
            value: The variable to set

        Returns:
            self for method chaining

        Note:
            Delegates to variable property setter (gets validation automatically)
        """
        self.variable = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_ram_block_init(self, value: Optional["ValueSpecification"]) -> "NvProvideComSpec":
        """
        Set ramBlockInit and return self for chaining.

        Args:
            value: The ramBlockInit to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ram_block_init("value")
        """
        self.ram_block_init = value  # Use property setter (gets validation)
        return self

    def with_rom_block_init(self, value: Optional["ValueSpecification"]) -> "NvProvideComSpec":
        """
        Set romBlockInit and return self for chaining.

        Args:
            value: The romBlockInit to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_rom_block_init("value")
        """
        self.rom_block_init = value  # Use property setter (gets validation)
        return self

    def with_variable(self, value: Optional[RefType]) -> "NvProvideComSpec":
        """
        Set variable and return self for chaining.

        Args:
            value: The variable to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_variable("value")
        """
        self.variable = value  # Use property setter (gets validation)
        return self



class ReceiverComSpec(RPortComSpec, ABC):
    """
    that if the receiver does not receive new Data at a consecutive read, then
    the receiver increments the tolerance by 1. Caveat: The E2E wrapper approach
    involves technologies that are not subjected to the AUTOSAR standard and is
    superseded by the superior E2E transformer approach (which is fully
    standardized by AUTOSAR). Hence, new projects (without legacy constraints
    due to carry-over parts) shall use the fully standardized E2E transformer
    approach. Stereotypes: atpVariation vh.latestBindingTime=preCompileTime
    maxNoNewOr PositiveInteger 0..1 attr The maximum amount of missing or
    repeated Data which RepeatedData the receiver does not expect to exceed
    under normal communication conditions. Caveat: The E2E wrapper approach
    involves technologies that are not subjected to the AUTOSAR standard and is
    superseded by the superior E2E transformer approach (which is fully
    standardized by AUTOSAR). Hence, new projects (without legacy constraints
    due to carry-over parts) shall use the fully standardized E2E transformer
    approach. network SwDataDefProps 0..1 aggr A networkRepresentation is used
    to define how the data Representation Element is mapped to a communication
    bus. Stereotypes: atpSplitable receptionProps ReceptionComSpec 0..1 aggr
    "This aggregation represents the definition transmission Props props in the
    context of the enclosing ReceiverComSpec. replaceWith VariableAccess 0..1
    aggr This aggregation is used to identify the AutosarData Prototype to be
    taken for sourcing an external replacement in the out-of-range and
    invalidValue handling. (cid:53) 171 of 1228 Document ID 62:
    AUTOSAR_CP_TPS_SoftwareComponentTemplate Software Component Template AUTOSAR
    CP R23-11 (cid:52)

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Communication::ReceiverComSpec

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 170, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2047, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is ReceiverComSpec:
            raise TypeError("ReceiverComSpec is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents a CompositeNetworkRepresentation defined in the context of a
                # ReceiverComSpec.
        # The of this aggregation is to be able to specify the of leaf elements of
                # Application.
        self._composite: List["CompositeNetwork"] = []

    @property
    def composite(self) -> List["CompositeNetwork"]:
        """Get composite (Pythonic accessor)."""
        return self._composite
        # Data element these attributes belong to.
        self._dataElement: Optional["RefType"] = None

    @property
    def data_element(self) -> Optional["RefType"]:
        """Get dataElement (Pythonic accessor)."""
        return self._dataElement

    @data_element.setter
    def data_element(self, value: Optional["RefType"]) -> None:
        """
        Set dataElement with validation.

        Args:
            value: The dataElement to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dataElement = None
            return

        self._dataElement = value
        # situation.
        self._handleOutOf: Optional["HandleOutOfRange"] = None

    @property
    def handle_out_of(self) -> Optional["HandleOutOfRange"]:
        """Get handleOutOf (Pythonic accessor)."""
        return self._handleOutOf

    @handle_out_of.setter
    def handle_out_of(self, value: Optional["HandleOutOfRange"]) -> None:
        """
        Set handleOutOf with validation.

        Args:
            value: The handleOutOf to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._handleOutOf = None
            return

        if not isinstance(value, HandleOutOfRange):
            raise TypeError(
                f"handleOutOf must be HandleOutOfRange or None, got {type(value).__name__}"
            )
        self._handleOutOf = value
                # received valid Data, i.
        # e.
        # how many data is accepted.
        # For example, if the Data with counter 1 and MaxDeltaCounter 1, then at the
                # next reception the receiver can accept values 2 and 3, but not 4.
        self._maxDelta: Optional["PositiveInteger"] = None

    @property
    def max_delta(self) -> Optional["PositiveInteger"]:
        """Get maxDelta (Pythonic accessor)."""
        return self._maxDelta

    @max_delta.setter
    def max_delta(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set maxDelta with validation.

        Args:
            value: The maxDelta to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxDelta = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"maxDelta must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._maxDelta = value
                # received with a valid counter (i.
        # e.
        # the allowed lock-in range) after the an unexpected behavior of a received E2E
                # wrapper approach involves are not subjected to the AUTOSAR is superseded by
                # the superior E2E (which is fully standardized by new projects (without legacy
                # to carry-over parts) shall use the fully transformer approach.
        self._syncCounterInit: Optional["PositiveInteger"] = None

    @property
    def sync_counter_init(self) -> Optional["PositiveInteger"]:
        """Get syncCounterInit (Pythonic accessor)."""
        return self._syncCounterInit

    @sync_counter_init.setter
    def sync_counter_init(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set syncCounterInit with validation.

        Args:
            value: The syncCounterInit to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._syncCounterInit = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"syncCounterInit must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._syncCounterInit = value
        # configuration for data transformation.
        self._transformation: List["TransformationCom"] = []

    @property
    def transformation(self) -> List["TransformationCom"]:
        """Get transformation (Pythonic accessor)."""
        return self._transformation
        # This indicates whether the corresponding dataElement be transmitted using
                # end-to-end protection.
        # E2E wrapper approach involves are not subjected to the AUTOSAR is superseded
                # by the superior E2E (which is fully standardized by new projects (without
                # legacy to carry-over parts) shall use the fully transformer approach.
        self._usesEndToEnd: Optional["Boolean"] = None

    @property
    def uses_end_to_end(self) -> Optional["Boolean"]:
        """Get usesEndToEnd (Pythonic accessor)."""
        return self._usesEndToEnd

    @uses_end_to_end.setter
    def uses_end_to_end(self, value: Optional["Boolean"]) -> None:
        """
        Set usesEndToEnd with validation.

        Args:
            value: The usesEndToEnd to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._usesEndToEnd = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"usesEndToEnd must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._usesEndToEnd = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getComposite(self) -> List["CompositeNetwork"]:
        """
        AUTOSAR-compliant getter for composite.

        Returns:
            The composite value

        Note:
            Delegates to composite property (CODING_RULE_V2_00017)
        """
        return self.composite  # Delegates to property

    def getDataElement(self) -> "RefType":
        """
        AUTOSAR-compliant getter for dataElement.

        Returns:
            The dataElement value

        Note:
            Delegates to data_element property (CODING_RULE_V2_00017)
        """
        return self.data_element  # Delegates to property

    def setDataElement(self, value: "RefType") -> "ReceiverComSpec":
        """
        AUTOSAR-compliant setter for dataElement with method chaining.

        Args:
            value: The dataElement to set

        Returns:
            self for method chaining

        Note:
            Delegates to data_element property setter (gets validation automatically)
        """
        self.data_element = value  # Delegates to property setter
        return self

    def getHandleOutOf(self) -> "HandleOutOfRange":
        """
        AUTOSAR-compliant getter for handleOutOf.

        Returns:
            The handleOutOf value

        Note:
            Delegates to handle_out_of property (CODING_RULE_V2_00017)
        """
        return self.handle_out_of  # Delegates to property

    def setHandleOutOf(self, value: "HandleOutOfRange") -> "ReceiverComSpec":
        """
        AUTOSAR-compliant setter for handleOutOf with method chaining.

        Args:
            value: The handleOutOf to set

        Returns:
            self for method chaining

        Note:
            Delegates to handle_out_of property setter (gets validation automatically)
        """
        self.handle_out_of = value  # Delegates to property setter
        return self

    def getMaxDelta(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for maxDelta.

        Returns:
            The maxDelta value

        Note:
            Delegates to max_delta property (CODING_RULE_V2_00017)
        """
        return self.max_delta  # Delegates to property

    def setMaxDelta(self, value: "PositiveInteger") -> "ReceiverComSpec":
        """
        AUTOSAR-compliant setter for maxDelta with method chaining.

        Args:
            value: The maxDelta to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_delta property setter (gets validation automatically)
        """
        self.max_delta = value  # Delegates to property setter
        return self

    def getSyncCounterInit(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for syncCounterInit.

        Returns:
            The syncCounterInit value

        Note:
            Delegates to sync_counter_init property (CODING_RULE_V2_00017)
        """
        return self.sync_counter_init  # Delegates to property

    def setSyncCounterInit(self, value: "PositiveInteger") -> "ReceiverComSpec":
        """
        AUTOSAR-compliant setter for syncCounterInit with method chaining.

        Args:
            value: The syncCounterInit to set

        Returns:
            self for method chaining

        Note:
            Delegates to sync_counter_init property setter (gets validation automatically)
        """
        self.sync_counter_init = value  # Delegates to property setter
        return self

    def getTransformation(self) -> List["TransformationCom"]:
        """
        AUTOSAR-compliant getter for transformation.

        Returns:
            The transformation value

        Note:
            Delegates to transformation property (CODING_RULE_V2_00017)
        """
        return self.transformation  # Delegates to property

    def getUsesEndToEnd(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for usesEndToEnd.

        Returns:
            The usesEndToEnd value

        Note:
            Delegates to uses_end_to_end property (CODING_RULE_V2_00017)
        """
        return self.uses_end_to_end  # Delegates to property

    def setUsesEndToEnd(self, value: "Boolean") -> "ReceiverComSpec":
        """
        AUTOSAR-compliant setter for usesEndToEnd with method chaining.

        Args:
            value: The usesEndToEnd to set

        Returns:
            self for method chaining

        Note:
            Delegates to uses_end_to_end property setter (gets validation automatically)
        """
        self.uses_end_to_end = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_data_element(self, value: Optional[RefType]) -> "ReceiverComSpec":
        """
        Set dataElement and return self for chaining.

        Args:
            value: The dataElement to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_data_element("value")
        """
        self.data_element = value  # Use property setter (gets validation)
        return self

    def with_handle_out_of(self, value: Optional["HandleOutOfRange"]) -> "ReceiverComSpec":
        """
        Set handleOutOf and return self for chaining.

        Args:
            value: The handleOutOf to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_handle_out_of("value")
        """
        self.handle_out_of = value  # Use property setter (gets validation)
        return self

    def with_max_delta(self, value: Optional["PositiveInteger"]) -> "ReceiverComSpec":
        """
        Set maxDelta and return self for chaining.

        Args:
            value: The maxDelta to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_delta("value")
        """
        self.max_delta = value  # Use property setter (gets validation)
        return self

    def with_sync_counter_init(self, value: Optional["PositiveInteger"]) -> "ReceiverComSpec":
        """
        Set syncCounterInit and return self for chaining.

        Args:
            value: The syncCounterInit to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sync_counter_init("value")
        """
        self.sync_counter_init = value  # Use property setter (gets validation)
        return self

    def with_uses_end_to_end(self, value: Optional["Boolean"]) -> "ReceiverComSpec":
        """
        Set usesEndToEnd and return self for chaining.

        Args:
            value: The usesEndToEnd to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_uses_end_to_end("value")
        """
        self.uses_end_to_end = value  # Use property setter (gets validation)
        return self



class ClientComSpec(RPortComSpec):
    """
    Client-specific communication attributes (RPortPrototype typed by
    ClientServerInterface).

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Communication::ClientComSpec

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 187, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute defines the maximum time interval in which application shall
        # expect the servers’s response (time the sending of the call invocation until
        # the arrival server’s response).
        self._endToEndCall: Optional["TimeValue"] = None

    @property
    def end_to_end_call(self) -> Optional["TimeValue"]:
        """Get endToEndCall (Pythonic accessor)."""
        return self._endToEndCall

    @end_to_end_call.setter
    def end_to_end_call(self, value: Optional["TimeValue"]) -> None:
        """
        Set endToEndCall with validation.

        Args:
            value: The endToEndCall to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._endToEndCall = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"endToEndCall must be TimeValue or None, got {type(value).__name__}"
            )
        self._endToEndCall = value
        self._operation: Optional["ClientServerOperation"] = None

    @property
    def operation(self) -> Optional["ClientServerOperation"]:
        """Get operation (Pythonic accessor)."""
        return self._operation

    @operation.setter
    def operation(self, value: Optional["ClientServerOperation"]) -> None:
        """
        Set operation with validation.

        Args:
            value: The operation to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._operation = None
            return

        if not isinstance(value, ClientServerOperation):
            raise TypeError(
                f"operation must be ClientServerOperation or None, got {type(value).__name__}"
            )
        self._operation = value
        # configuration for data transformation.
        self._transformation: List["TransformationCom"] = []

    @property
    def transformation(self) -> List["TransformationCom"]:
        """Get transformation (Pythonic accessor)."""
        return self._transformation

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEndToEndCall(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for endToEndCall.

        Returns:
            The endToEndCall value

        Note:
            Delegates to end_to_end_call property (CODING_RULE_V2_00017)
        """
        return self.end_to_end_call  # Delegates to property

    def setEndToEndCall(self, value: "TimeValue") -> "ClientComSpec":
        """
        AUTOSAR-compliant setter for endToEndCall with method chaining.

        Args:
            value: The endToEndCall to set

        Returns:
            self for method chaining

        Note:
            Delegates to end_to_end_call property setter (gets validation automatically)
        """
        self.end_to_end_call = value  # Delegates to property setter
        return self

    def getOperation(self) -> "ClientServerOperation":
        """
        AUTOSAR-compliant getter for operation.

        Returns:
            The operation value

        Note:
            Delegates to operation property (CODING_RULE_V2_00017)
        """
        return self.operation  # Delegates to property

    def setOperation(self, value: "ClientServerOperation") -> "ClientComSpec":
        """
        AUTOSAR-compliant setter for operation with method chaining.

        Args:
            value: The operation to set

        Returns:
            self for method chaining

        Note:
            Delegates to operation property setter (gets validation automatically)
        """
        self.operation = value  # Delegates to property setter
        return self

    def getTransformation(self) -> List["TransformationCom"]:
        """
        AUTOSAR-compliant getter for transformation.

        Returns:
            The transformation value

        Note:
            Delegates to transformation property (CODING_RULE_V2_00017)
        """
        return self.transformation  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_end_to_end_call(self, value: Optional["TimeValue"]) -> "ClientComSpec":
        """
        Set endToEndCall and return self for chaining.

        Args:
            value: The endToEndCall to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_end_to_end_call("value")
        """
        self.end_to_end_call = value  # Use property setter (gets validation)
        return self

    def with_operation(self, value: Optional["ClientServerOperation"]) -> "ClientComSpec":
        """
        Set operation and return self for chaining.

        Args:
            value: The operation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_operation("value")
        """
        self.operation = value  # Use property setter (gets validation)
        return self



class ModeSwitchReceiverComSpec(RPortComSpec):
    """
    Communication attributes of RPortPrototypes with respect to mode
    communication

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Communication::ModeSwitchReceiverComSpec

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 191, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This controls the creation of the enhanced mode API that information about
                # the previous mode and the next set to "true" the enhanced mode API is be
                # generated.
        # For more details please refer SWS_RTE.
        self._enhancedMode: Optional["Boolean"] = None

    @property
    def enhanced_mode(self) -> Optional["Boolean"]:
        """Get enhancedMode (Pythonic accessor)."""
        return self._enhancedMode

    @enhanced_mode.setter
    def enhanced_mode(self, value: Optional["Boolean"]) -> None:
        """
        Set enhancedMode with validation.

        Args:
            value: The enhancedMode to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._enhancedMode = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"enhancedMode must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._enhancedMode = value
        # attributes apply.
        self._modeGroup: Optional["RefType"] = None

    @property
    def mode_group(self) -> Optional["RefType"]:
        """Get modeGroup (Pythonic accessor)."""
        return self._modeGroup

    @mode_group.setter
    def mode_group(self, value: Optional["RefType"]) -> None:
        """
        Set modeGroup with validation.

        Args:
            value: The modeGroup to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._modeGroup = None
            return

        self._modeGroup = value
                # question whether it deal with asynchronous mode switch requests, i.
        # e.
        # if true, the RPortPrototype is able to deal with an switch request.
        self._supports: Optional["Boolean"] = None

    @property
    def supports(self) -> Optional["Boolean"]:
        """Get supports (Pythonic accessor)."""
        return self._supports

    @supports.setter
    def supports(self, value: Optional["Boolean"]) -> None:
        """
        Set supports with validation.

        Args:
            value: The supports to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._supports = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"supports must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._supports = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEnhancedMode(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for enhancedMode.

        Returns:
            The enhancedMode value

        Note:
            Delegates to enhanced_mode property (CODING_RULE_V2_00017)
        """
        return self.enhanced_mode  # Delegates to property

    def setEnhancedMode(self, value: "Boolean") -> "ModeSwitchReceiverComSpec":
        """
        AUTOSAR-compliant setter for enhancedMode with method chaining.

        Args:
            value: The enhancedMode to set

        Returns:
            self for method chaining

        Note:
            Delegates to enhanced_mode property setter (gets validation automatically)
        """
        self.enhanced_mode = value  # Delegates to property setter
        return self

    def getModeGroup(self) -> "RefType":
        """
        AUTOSAR-compliant getter for modeGroup.

        Returns:
            The modeGroup value

        Note:
            Delegates to mode_group property (CODING_RULE_V2_00017)
        """
        return self.mode_group  # Delegates to property

    def setModeGroup(self, value: "RefType") -> "ModeSwitchReceiverComSpec":
        """
        AUTOSAR-compliant setter for modeGroup with method chaining.

        Args:
            value: The modeGroup to set

        Returns:
            self for method chaining

        Note:
            Delegates to mode_group property setter (gets validation automatically)
        """
        self.mode_group = value  # Delegates to property setter
        return self

    def getSupports(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for supports.

        Returns:
            The supports value

        Note:
            Delegates to supports property (CODING_RULE_V2_00017)
        """
        return self.supports  # Delegates to property

    def setSupports(self, value: "Boolean") -> "ModeSwitchReceiverComSpec":
        """
        AUTOSAR-compliant setter for supports with method chaining.

        Args:
            value: The supports to set

        Returns:
            self for method chaining

        Note:
            Delegates to supports property setter (gets validation automatically)
        """
        self.supports = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_enhanced_mode(self, value: Optional["Boolean"]) -> "ModeSwitchReceiverComSpec":
        """
        Set enhancedMode and return self for chaining.

        Args:
            value: The enhancedMode to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_enhanced_mode("value")
        """
        self.enhanced_mode = value  # Use property setter (gets validation)
        return self

    def with_mode_group(self, value: Optional[RefType]) -> "ModeSwitchReceiverComSpec":
        """
        Set modeGroup and return self for chaining.

        Args:
            value: The modeGroup to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mode_group("value")
        """
        self.mode_group = value  # Use property setter (gets validation)
        return self

    def with_supports(self, value: Optional["Boolean"]) -> "ModeSwitchReceiverComSpec":
        """
        Set supports and return self for chaining.

        Args:
            value: The supports to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_supports("value")
        """
        self.supports = value  # Use property setter (gets validation)
        return self



class ParameterRequireComSpec(RPortComSpec):
    """
    "Communication" specification that applies to parameters on the required
    side of a connection.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Communication::ParameterRequireComSpec

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 193, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The initial value applicable for the corresponding.
        self._initValue: Optional["ValueSpecification"] = None

    @property
    def init_value(self) -> Optional["ValueSpecification"]:
        """Get initValue (Pythonic accessor)."""
        return self._initValue

    @init_value.setter
    def init_value(self, value: Optional["ValueSpecification"]) -> None:
        """
        Set initValue with validation.

        Args:
            value: The initValue to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._initValue = None
            return

        if not isinstance(value, ValueSpecification):
            raise TypeError(
                f"initValue must be ValueSpecification or None, got {type(value).__name__}"
            )
        self._initValue = value
        self._parameter: Optional["ParameterData"] = None

    @property
    def parameter(self) -> Optional["ParameterData"]:
        """Get parameter (Pythonic accessor)."""
        return self._parameter

    @parameter.setter
    def parameter(self, value: Optional["ParameterData"]) -> None:
        """
        Set parameter with validation.

        Args:
            value: The parameter to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._parameter = None
            return

        if not isinstance(value, ParameterData):
            raise TypeError(
                f"parameter must be ParameterData or None, got {type(value).__name__}"
            )
        self._parameter = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getInitValue(self) -> "ValueSpecification":
        """
        AUTOSAR-compliant getter for initValue.

        Returns:
            The initValue value

        Note:
            Delegates to init_value property (CODING_RULE_V2_00017)
        """
        return self.init_value  # Delegates to property

    def setInitValue(self, value: "ValueSpecification") -> "ParameterRequireComSpec":
        """
        AUTOSAR-compliant setter for initValue with method chaining.

        Args:
            value: The initValue to set

        Returns:
            self for method chaining

        Note:
            Delegates to init_value property setter (gets validation automatically)
        """
        self.init_value = value  # Delegates to property setter
        return self

    def getParameter(self) -> "ParameterData":
        """
        AUTOSAR-compliant getter for parameter.

        Returns:
            The parameter value

        Note:
            Delegates to parameter property (CODING_RULE_V2_00017)
        """
        return self.parameter  # Delegates to property

    def setParameter(self, value: "ParameterData") -> "ParameterRequireComSpec":
        """
        AUTOSAR-compliant setter for parameter with method chaining.

        Args:
            value: The parameter to set

        Returns:
            self for method chaining

        Note:
            Delegates to parameter property setter (gets validation automatically)
        """
        self.parameter = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_init_value(self, value: Optional["ValueSpecification"]) -> "ParameterRequireComSpec":
        """
        Set initValue and return self for chaining.

        Args:
            value: The initValue to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_init_value("value")
        """
        self.init_value = value  # Use property setter (gets validation)
        return self

    def with_parameter(self, value: Optional["ParameterData"]) -> "ParameterRequireComSpec":
        """
        Set parameter and return self for chaining.

        Args:
            value: The parameter to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_parameter("value")
        """
        self.parameter = value  # Use property setter (gets validation)
        return self



class NvRequireComSpec(RPortComSpec):
    """
    Communication attributes of RPortPrototypes with respect to Nv data
    communication on the required side.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Communication::NvRequireComSpec

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 194, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The initial value owned by the NvComSpec.
        self._initValue: Optional["ValueSpecification"] = None

    @property
    def init_value(self) -> Optional["ValueSpecification"]:
        """Get initValue (Pythonic accessor)."""
        return self._initValue

    @init_value.setter
    def init_value(self, value: Optional["ValueSpecification"]) -> None:
        """
        Set initValue with validation.

        Args:
            value: The initValue to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._initValue = None
            return

        if not isinstance(value, ValueSpecification):
            raise TypeError(
                f"initValue must be ValueSpecification or None, got {type(value).__name__}"
            )
        self._initValue = value
        self._variable: Optional["RefType"] = None

    @property
    def variable(self) -> Optional["RefType"]:
        """Get variable (Pythonic accessor)."""
        return self._variable

    @variable.setter
    def variable(self, value: Optional["RefType"]) -> None:
        """
        Set variable with validation.

        Args:
            value: The variable to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._variable = None
            return

        self._variable = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getInitValue(self) -> "ValueSpecification":
        """
        AUTOSAR-compliant getter for initValue.

        Returns:
            The initValue value

        Note:
            Delegates to init_value property (CODING_RULE_V2_00017)
        """
        return self.init_value  # Delegates to property

    def setInitValue(self, value: "ValueSpecification") -> "NvRequireComSpec":
        """
        AUTOSAR-compliant setter for initValue with method chaining.

        Args:
            value: The initValue to set

        Returns:
            self for method chaining

        Note:
            Delegates to init_value property setter (gets validation automatically)
        """
        self.init_value = value  # Delegates to property setter
        return self

    def getVariable(self) -> "RefType":
        """
        AUTOSAR-compliant getter for variable.

        Returns:
            The variable value

        Note:
            Delegates to variable property (CODING_RULE_V2_00017)
        """
        return self.variable  # Delegates to property

    def setVariable(self, value: "RefType") -> "NvRequireComSpec":
        """
        AUTOSAR-compliant setter for variable with method chaining.

        Args:
            value: The variable to set

        Returns:
            self for method chaining

        Note:
            Delegates to variable property setter (gets validation automatically)
        """
        self.variable = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_init_value(self, value: Optional["ValueSpecification"]) -> "NvRequireComSpec":
        """
        Set initValue and return self for chaining.

        Args:
            value: The initValue to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_init_value("value")
        """
        self.init_value = value  # Use property setter (gets validation)
        return self

    def with_variable(self, value: Optional[RefType]) -> "NvRequireComSpec":
        """
        Set variable and return self for chaining.

        Args:
            value: The variable to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_variable("value")
        """
        self.variable = value  # Use property setter (gets validation)
        return self



class UserDefinedTransformationComSpecProps(TransformationComSpecProps):
    """
    The UserDefinedTransformationComSpecProps is used to specify port specific
    configuration properties for custom transformers.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Communication::UserDefinedTransformationComSpecProps

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 200, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class QueuedSenderComSpec(SenderComSpec):
    """
    Communication attributes specific to distribution of events (PPortPrototype,
    SenderReceiverInterface and dataElement carries an "event").

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Communication::QueuedSenderComSpec

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 179, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class NonqueuedSenderComSpec(SenderComSpec):
    """
    Communication attributes for non-queued sender/receiver communication
    (sender side)

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Communication::NonqueuedSenderComSpec

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 179, Classic Platform
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 198, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The applicable filter algorithm for filtering the value of the.
        self._dataFilter: Optional["DataFilter"] = None

    @property
    def data_filter(self) -> Optional["DataFilter"]:
        """Get dataFilter (Pythonic accessor)."""
        return self._dataFilter

    @data_filter.setter
    def data_filter(self, value: Optional["DataFilter"]) -> None:
        """
        Set dataFilter with validation.

        Args:
            value: The dataFilter to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dataFilter = None
            return

        if not isinstance(value, DataFilter):
            raise TypeError(
                f"dataFilter must be DataFilter or None, got {type(value).__name__}"
            )
        self._dataFilter = value
        # data already.
        self._initValue: Optional["ValueSpecification"] = None

    @property
    def init_value(self) -> Optional["ValueSpecification"]:
        """Get initValue (Pythonic accessor)."""
        return self._initValue

    @init_value.setter
    def init_value(self, value: Optional["ValueSpecification"]) -> None:
        """
        Set initValue with validation.

        Args:
            value: The initValue to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._initValue = None
            return

        if not isinstance(value, ValueSpecification):
            raise TypeError(
                f"initValue must be ValueSpecification or None, got {type(value).__name__}"
            )
        self._initValue = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDataFilter(self) -> "DataFilter":
        """
        AUTOSAR-compliant getter for dataFilter.

        Returns:
            The dataFilter value

        Note:
            Delegates to data_filter property (CODING_RULE_V2_00017)
        """
        return self.data_filter  # Delegates to property

    def setDataFilter(self, value: "DataFilter") -> "NonqueuedSenderComSpec":
        """
        AUTOSAR-compliant setter for dataFilter with method chaining.

        Args:
            value: The dataFilter to set

        Returns:
            self for method chaining

        Note:
            Delegates to data_filter property setter (gets validation automatically)
        """
        self.data_filter = value  # Delegates to property setter
        return self

    def getInitValue(self) -> "ValueSpecification":
        """
        AUTOSAR-compliant getter for initValue.

        Returns:
            The initValue value

        Note:
            Delegates to init_value property (CODING_RULE_V2_00017)
        """
        return self.init_value  # Delegates to property

    def setInitValue(self, value: "ValueSpecification") -> "NonqueuedSenderComSpec":
        """
        AUTOSAR-compliant setter for initValue with method chaining.

        Args:
            value: The initValue to set

        Returns:
            self for method chaining

        Note:
            Delegates to init_value property setter (gets validation automatically)
        """
        self.init_value = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_data_filter(self, value: Optional["DataFilter"]) -> "NonqueuedSenderComSpec":
        """
        Set dataFilter and return self for chaining.

        Args:
            value: The dataFilter to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_data_filter("value")
        """
        self.data_filter = value  # Use property setter (gets validation)
        return self

    def with_init_value(self, value: Optional["ValueSpecification"]) -> "NonqueuedSenderComSpec":
        """
        Set initValue and return self for chaining.

        Args:
            value: The initValue to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_init_value("value")
        """
        self.init_value = value  # Use property setter (gets validation)
        return self



class NonqueuedReceiverComSpec(ReceiverComSpec):
    """
    Communication attributes specific to non-queued receiving.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Communication::NonqueuedReceiverComSpec

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 172, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2039, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 198, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specify the amount of time (in seconds) after which the (via the RTE) needs
                # to be notified if data item have not been received the specified timing
                # description.
        # aliveTimeout attribute is 0 no timeout monitoring performed.
        self._aliveTimeout: Optional["TimeValue"] = None

    @property
    def alive_timeout(self) -> Optional["TimeValue"]:
        """Get aliveTimeout (Pythonic accessor)."""
        return self._aliveTimeout

    @alive_timeout.setter
    def alive_timeout(self, value: Optional["TimeValue"]) -> None:
        """
        Set aliveTimeout with validation.

        Args:
            value: The aliveTimeout to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._aliveTimeout = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"aliveTimeout must be TimeValue or None, got {type(value).__name__}"
            )
        self._aliveTimeout = value
        # value of the corresponding Variable been updated.
        self._enableUpdate: Optional["Boolean"] = None

    @property
    def enable_update(self) -> Optional["Boolean"]:
        """Get enableUpdate (Pythonic accessor)."""
        return self._enableUpdate

    @enable_update.setter
    def enable_update(self, value: Optional["Boolean"]) -> None:
        """
        Set enableUpdate with validation.

        Args:
            value: The enableUpdate to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._enableUpdate = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"enableUpdate must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._enableUpdate = value
        self._filter: Optional["DataFilter"] = None

    @property
    def filter(self) -> Optional["DataFilter"]:
        """Get filter (Pythonic accessor)."""
        return self._filter

    @filter.setter
    def filter(self, value: Optional["DataFilter"]) -> None:
        """
        Set filter with validation.

        Args:
            value: The filter to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._filter = None
            return

        if not isinstance(value, DataFilter):
            raise TypeError(
                f"filter must be DataFilter or None, got {type(value).__name__}"
            )
        self._filter = value
        # If the attribute does not exist or is set to false, Rte_IStatus API may still
                # exist in response to the further conditions.
        self._handleData: Optional["Boolean"] = None

    @property
    def handle_data(self) -> Optional["Boolean"]:
        """Get handleData (Pythonic accessor)."""
        return self._handleData

    @handle_data.setter
    def handle_data(self, value: Optional["Boolean"]) -> None:
        """
        Set handleData with validation.

        Args:
            value: The handleData to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._handleData = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"handleData must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._handleData = value
                # flag is yes, the RTE is supposed to assume that VariableDataPrototype has not
                # been received the first reception of the corresponding flag is cleared.
        # the value of this attribute is set to "true" the flag is set to "false", the
                # RTE shall not support the "never for the corresponding Variable.
        self._handleNever: Optional["Boolean"] = None

    @property
    def handle_never(self) -> Optional["Boolean"]:
        """Get handleNever (Pythonic accessor)."""
        return self._handleNever

    @handle_never.setter
    def handle_never(self, value: Optional["Boolean"]) -> None:
        """
        Set handleNever with validation.

        Args:
            value: The handleNever to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._handleNever = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"handleNever must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._handleNever = value
        self._handleTimeout: Optional["HandleTimeoutEnum"] = None

    @property
    def handle_timeout(self) -> Optional["HandleTimeoutEnum"]:
        """Get handleTimeout (Pythonic accessor)."""
        return self._handleTimeout

    @handle_timeout.setter
    def handle_timeout(self, value: Optional["HandleTimeoutEnum"]) -> None:
        """
        Set handleTimeout with validation.

        Args:
            value: The handleTimeout to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._handleTimeout = None
            return

        if not isinstance(value, HandleTimeoutEnum):
            raise TypeError(
                f"handleTimeout must be HandleTimeoutEnum or None, got {type(value).__name__}"
            )
        self._handleTimeout = value
        # If the sender also specifies an initial the receiver’s value will be used.
        self._initValue: Optional["ValueSpecification"] = None

    @property
    def init_value(self) -> Optional["ValueSpecification"]:
        """Get initValue (Pythonic accessor)."""
        return self._initValue

    @init_value.setter
    def init_value(self, value: Optional["ValueSpecification"]) -> None:
        """
        Set initValue with validation.

        Args:
            value: The initValue to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._initValue = None
            return

        if not isinstance(value, ValueSpecification):
            raise TypeError(
                f"initValue must be ValueSpecification or None, got {type(value).__name__}"
            )
        self._initValue = value
        # timeout.
        self._timeout: Optional["ValueSpecification"] = None

    @property
    def timeout(self) -> Optional["ValueSpecification"]:
        """Get timeout (Pythonic accessor)."""
        return self._timeout

    @timeout.setter
    def timeout(self, value: Optional["ValueSpecification"]) -> None:
        """
        Set timeout with validation.

        Args:
            value: The timeout to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeout = None
            return

        if not isinstance(value, ValueSpecification):
            raise TypeError(
                f"timeout must be ValueSpecification or None, got {type(value).__name__}"
            )
        self._timeout = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAliveTimeout(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for aliveTimeout.

        Returns:
            The aliveTimeout value

        Note:
            Delegates to alive_timeout property (CODING_RULE_V2_00017)
        """
        return self.alive_timeout  # Delegates to property

    def setAliveTimeout(self, value: "TimeValue") -> "NonqueuedReceiverComSpec":
        """
        AUTOSAR-compliant setter for aliveTimeout with method chaining.

        Args:
            value: The aliveTimeout to set

        Returns:
            self for method chaining

        Note:
            Delegates to alive_timeout property setter (gets validation automatically)
        """
        self.alive_timeout = value  # Delegates to property setter
        return self

    def getEnableUpdate(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for enableUpdate.

        Returns:
            The enableUpdate value

        Note:
            Delegates to enable_update property (CODING_RULE_V2_00017)
        """
        return self.enable_update  # Delegates to property

    def setEnableUpdate(self, value: "Boolean") -> "NonqueuedReceiverComSpec":
        """
        AUTOSAR-compliant setter for enableUpdate with method chaining.

        Args:
            value: The enableUpdate to set

        Returns:
            self for method chaining

        Note:
            Delegates to enable_update property setter (gets validation automatically)
        """
        self.enable_update = value  # Delegates to property setter
        return self

    def getFilter(self) -> "DataFilter":
        """
        AUTOSAR-compliant getter for filter.

        Returns:
            The filter value

        Note:
            Delegates to filter property (CODING_RULE_V2_00017)
        """
        return self.filter  # Delegates to property

    def setFilter(self, value: "DataFilter") -> "NonqueuedReceiverComSpec":
        """
        AUTOSAR-compliant setter for filter with method chaining.

        Args:
            value: The filter to set

        Returns:
            self for method chaining

        Note:
            Delegates to filter property setter (gets validation automatically)
        """
        self.filter = value  # Delegates to property setter
        return self

    def getHandleData(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for handleData.

        Returns:
            The handleData value

        Note:
            Delegates to handle_data property (CODING_RULE_V2_00017)
        """
        return self.handle_data  # Delegates to property

    def setHandleData(self, value: "Boolean") -> "NonqueuedReceiverComSpec":
        """
        AUTOSAR-compliant setter for handleData with method chaining.

        Args:
            value: The handleData to set

        Returns:
            self for method chaining

        Note:
            Delegates to handle_data property setter (gets validation automatically)
        """
        self.handle_data = value  # Delegates to property setter
        return self

    def getHandleNever(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for handleNever.

        Returns:
            The handleNever value

        Note:
            Delegates to handle_never property (CODING_RULE_V2_00017)
        """
        return self.handle_never  # Delegates to property

    def setHandleNever(self, value: "Boolean") -> "NonqueuedReceiverComSpec":
        """
        AUTOSAR-compliant setter for handleNever with method chaining.

        Args:
            value: The handleNever to set

        Returns:
            self for method chaining

        Note:
            Delegates to handle_never property setter (gets validation automatically)
        """
        self.handle_never = value  # Delegates to property setter
        return self

    def getHandleTimeout(self) -> "HandleTimeoutEnum":
        """
        AUTOSAR-compliant getter for handleTimeout.

        Returns:
            The handleTimeout value

        Note:
            Delegates to handle_timeout property (CODING_RULE_V2_00017)
        """
        return self.handle_timeout  # Delegates to property

    def setHandleTimeout(self, value: "HandleTimeoutEnum") -> "NonqueuedReceiverComSpec":
        """
        AUTOSAR-compliant setter for handleTimeout with method chaining.

        Args:
            value: The handleTimeout to set

        Returns:
            self for method chaining

        Note:
            Delegates to handle_timeout property setter (gets validation automatically)
        """
        self.handle_timeout = value  # Delegates to property setter
        return self

    def getInitValue(self) -> "ValueSpecification":
        """
        AUTOSAR-compliant getter for initValue.

        Returns:
            The initValue value

        Note:
            Delegates to init_value property (CODING_RULE_V2_00017)
        """
        return self.init_value  # Delegates to property

    def setInitValue(self, value: "ValueSpecification") -> "NonqueuedReceiverComSpec":
        """
        AUTOSAR-compliant setter for initValue with method chaining.

        Args:
            value: The initValue to set

        Returns:
            self for method chaining

        Note:
            Delegates to init_value property setter (gets validation automatically)
        """
        self.init_value = value  # Delegates to property setter
        return self

    def getTimeout(self) -> "ValueSpecification":
        """
        AUTOSAR-compliant getter for timeout.

        Returns:
            The timeout value

        Note:
            Delegates to timeout property (CODING_RULE_V2_00017)
        """
        return self.timeout  # Delegates to property

    def setTimeout(self, value: "ValueSpecification") -> "NonqueuedReceiverComSpec":
        """
        AUTOSAR-compliant setter for timeout with method chaining.

        Args:
            value: The timeout to set

        Returns:
            self for method chaining

        Note:
            Delegates to timeout property setter (gets validation automatically)
        """
        self.timeout = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_alive_timeout(self, value: Optional["TimeValue"]) -> "NonqueuedReceiverComSpec":
        """
        Set aliveTimeout and return self for chaining.

        Args:
            value: The aliveTimeout to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_alive_timeout("value")
        """
        self.alive_timeout = value  # Use property setter (gets validation)
        return self

    def with_enable_update(self, value: Optional["Boolean"]) -> "NonqueuedReceiverComSpec":
        """
        Set enableUpdate and return self for chaining.

        Args:
            value: The enableUpdate to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_enable_update("value")
        """
        self.enable_update = value  # Use property setter (gets validation)
        return self

    def with_filter(self, value: Optional["DataFilter"]) -> "NonqueuedReceiverComSpec":
        """
        Set filter and return self for chaining.

        Args:
            value: The filter to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_filter("value")
        """
        self.filter = value  # Use property setter (gets validation)
        return self

    def with_handle_data(self, value: Optional["Boolean"]) -> "NonqueuedReceiverComSpec":
        """
        Set handleData and return self for chaining.

        Args:
            value: The handleData to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_handle_data("value")
        """
        self.handle_data = value  # Use property setter (gets validation)
        return self

    def with_handle_never(self, value: Optional["Boolean"]) -> "NonqueuedReceiverComSpec":
        """
        Set handleNever and return self for chaining.

        Args:
            value: The handleNever to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_handle_never("value")
        """
        self.handle_never = value  # Use property setter (gets validation)
        return self

    def with_handle_timeout(self, value: Optional["HandleTimeoutEnum"]) -> "NonqueuedReceiverComSpec":
        """
        Set handleTimeout and return self for chaining.

        Args:
            value: The handleTimeout to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_handle_timeout("value")
        """
        self.handle_timeout = value  # Use property setter (gets validation)
        return self

    def with_init_value(self, value: Optional["ValueSpecification"]) -> "NonqueuedReceiverComSpec":
        """
        Set initValue and return self for chaining.

        Args:
            value: The initValue to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_init_value("value")
        """
        self.init_value = value  # Use property setter (gets validation)
        return self

    def with_timeout(self, value: Optional["ValueSpecification"]) -> "NonqueuedReceiverComSpec":
        """
        Set timeout and return self for chaining.

        Args:
            value: The timeout to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_timeout("value")
        """
        self.timeout = value  # Use property setter (gets validation)
        return self



class QueuedReceiverComSpec(ReceiverComSpec):
    """
    Communication attributes specific to queued receiving.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Communication::QueuedReceiverComSpec

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 173, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Length of queue for received events.
        self._queueLength: Optional["PositiveInteger"] = None

    @property
    def queue_length(self) -> Optional["PositiveInteger"]:
        """Get queueLength (Pythonic accessor)."""
        return self._queueLength

    @queue_length.setter
    def queue_length(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set queueLength with validation.

        Args:
            value: The queueLength to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._queueLength = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"queueLength must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._queueLength = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getQueueLength(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for queueLength.

        Returns:
            The queueLength value

        Note:
            Delegates to queue_length property (CODING_RULE_V2_00017)
        """
        return self.queue_length  # Delegates to property

    def setQueueLength(self, value: "PositiveInteger") -> "QueuedReceiverComSpec":
        """
        AUTOSAR-compliant setter for queueLength with method chaining.

        Args:
            value: The queueLength to set

        Returns:
            self for method chaining

        Note:
            Delegates to queue_length property setter (gets validation automatically)
        """
        self.queue_length = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_queue_length(self, value: Optional["PositiveInteger"]) -> "QueuedReceiverComSpec":
        """
        Set queueLength and return self for chaining.

        Args:
            value: The queueLength to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_queue_length("value")
        """
        self.queue_length = value  # Use property setter (gets validation)
        return self


class HandleInvalidEnum(AREnum):
    """
    HandleInvalidEnum enumeration

Strategies of handling the reception of invalidValue. Aggregated by InvalidationPolicy.handleInvalid, ISignalPort.handleInvalid

Package: M2::AUTOSARTemplates::SWComponentTemplate::Communication
    """
    # Invalidation is switched off.
    dontInvalidate = "0"

    # Replace a received invalidValue. The replacement value is sourced from the aggregation in the role Replacement replaceWith.
    external = "1"

    # The application software is supposed to handle signal invalidation on RTE API level either by Data ReceiveErrorEvent or check of error code on read access.
    keep = "2"

    # Replace a received invalidValue. The replacement value is specified by the initValue.
    replace = "3"



class HandleOutOfRangeStatusEnum(AREnum):
    """
    HandleOutOfRangeStatusEnum enumeration

This enumeration defines how the RTE handles values that are out of range. Aggregated by ReceiverComSpec.handleOutOfRangeStatus

Package: M2::AUTOSARTemplates::SWComponentTemplate::Communication
    """
    # The RTE sets the return status to RTE_E_OUT_OF_RANGE if the received value is out of range and the attribute handleOutOfRange is not set to "none" or "invalid".
    indicate = "0"

    # The RTE sets the return status to RTE_E_OK
    silent = "1"



class HandleTimeoutEnum(AREnum):
    """
    HandleTimeoutEnum enumeration

Strategies of handling a reception timeout violation. Aggregated by NonqueuedReceiverComSpec.handleTimeoutType

Package: M2::AUTOSARTemplates::SWComponentTemplate::Communication
    """
    # If set to none no replacement shall take place.
    none = "0"

    # If set to replace, the replacement value shall be the ComInitValue.
    replace = "1"

    # If set to replace, the replacement value shall be the timeout substitution value.
    replaceByTimeoutSubstitutionValue = "2"



class HandleOutOfRangeEnum(AREnum):
    """
    HandleOutOfRangeEnum enumeration

A value of this type is taken for controlling the range checking behavior of the AUTOSAR RTE. Aggregated by ISignalProps.handleOutOfRange, ReceiverComSpec.handleOutOfRange, SenderComSpec.handle OutOfRange

Package: M2::AUTOSARTemplates::SWComponentTemplate::Communication
    """
    # The RTE will use the initValue if the actual value is out of the specified bounds.
    default = "0"

    # This indicates that the value replacement is sourced from the attribute replaceWith.
    externalReplacement = "1"

    # The RTE will ignore any attempt to send or receive the corresponding dataElement if the value is out of the specified range.
    ignore = "2"

    # The RTE will use the invalidValue if the value is out of the specified bounds.
    invalid = "3"

    # A range check is not required.
    none = "4"

    # The RTE will saturate the value of the dataElement such that it is limited to the applicable upper bound if it is greater than the upper bound. Consequently, it is limited to the applicable lower bound if the value is less than the lower bound.
    saturate = "5"



class TransmissionModeDefinitionEnum(AREnum):
    """
    TransmissionModeDefinitionEnum enumeration

This meta-class defines possible settings for the transmission mode. Aggregated by TransmissionComSpecProps.transmissionMode

Package: M2::AUTOSARTemplates::SWComponentTemplate::Communication
    """
    # The data is assumed to be transmitted in a cyclic manner. The cycle is defined by dataUpdatePeriod.
    cyclic = "0"

    # The data is assumed to be transmitted in a cyclic manner (with cycle time dataUpdatePeriod) and Change additionally there may be arbitrary transmission if the data value changes (minimumSendInterval to be respected, if defined).
    cyclicAndOn = "2"

    # The data is assumed to be transmitted in an arbitrary manner (minimumSendInterval to be respected, if defined).
    triggered = "1"

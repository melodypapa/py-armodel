from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import IPdu

    RefType,
)


class ContainerIPdu(IPdu):
    """
    Allows to collect several IPdus in one ContainerIPdu based on the
    headerType.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::ContainerIPdu

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 353, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines properties for an IPdu that is part of the.
        self._containedIPdu: List["ContainedIPduProps"] = []

    @property
    def contained_i_pdu(self) -> List["ContainedIPduProps"]:
        """Get containedIPdu (Pythonic accessor)."""
        return self._containedIPdu
        # This PduTriggering shall be collected inside the Container 2090 Document ID
        # 63: AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._containedPdu: List[RefType] = []

    @property
    def contained_pdu(self) -> List[RefType]:
        """Get containedPdu (Pythonic accessor)."""
        return self._containedPdu
        # When this timeout expires the ContainerIPdu is sent out.
        # respective timer is started when the first Ipdu is put ContainerIPdu.
        # This attribute is ignored on.
        self._container: Optional["TimeValue"] = None

    @property
    def container(self) -> Optional["TimeValue"]:
        """Get container (Pythonic accessor)."""
        return self._container

    @container.setter
    def container(self, value: Optional["TimeValue"]) -> None:
        """
        Set container with validation.

        Args:
            value: The container to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._container = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"container must be TimeValue or None, got {type(value).__name__}"
            )
        self._container = value
        # Defines if the transmission of the ContainerIPdu shall be right after the
        # first ContainedIPdu was put into attribute shall be ignored on receiver side.
        self._containerTrigger: RefType = None

    @property
    def container_trigger(self) -> RefType:
        """Get containerTrigger (Pythonic accessor)."""
        return self._containerTrigger

    @container_trigger.setter
    def container_trigger(self, value: RefType) -> None:
        """
        Set containerTrigger with validation.

        Args:
            value: The containerTrigger to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._containerTrigger = None
            return

        self._containerTrigger = value
        # Defines whether and which header type is used (header and length).
        self._headerType: Optional["ContainerIPduHeader"] = None

    @property
    def header_type(self) -> Optional["ContainerIPduHeader"]:
        """Get headerType (Pythonic accessor)."""
        return self._headerType

    @header_type.setter
    def header_type(self, value: Optional["ContainerIPduHeader"]) -> None:
        """
        Set headerType with validation.

        Args:
            value: The headerType to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._headerType = None
            return

        if not isinstance(value, ContainerIPduHeader):
            raise TypeError(
                f"headerType must be ContainerIPduHeader or None, got {type(value).__name__}"
            )
        self._headerType = value
        # This attribute defines the minimum queue size for containers.
        self._minimumRx: Optional["PositiveInteger"] = None

    @property
    def minimum_rx(self) -> Optional["PositiveInteger"]:
        """Get minimumRx (Pythonic accessor)."""
        return self._minimumRx

    @minimum_rx.setter
    def minimum_rx(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set minimumRx with validation.

        Args:
            value: The minimumRx to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._minimumRx = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"minimumRx must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._minimumRx = value
        # This attribute defines the minimum queue size for containers.
        self._minimumTx: Optional["PositiveInteger"] = None

    @property
    def minimum_tx(self) -> Optional["PositiveInteger"]:
        """Get minimumTx (Pythonic accessor)."""
        return self._minimumTx

    @minimum_tx.setter
    def minimum_tx(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set minimumTx with validation.

        Args:
            value: The minimumTx to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._minimumTx = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"minimumTx must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._minimumTx = value
        # Defines whether this ContainerIPdu has a fixed set of containedIPdus assigned
        # for reception.
        self._rxAccept: Optional["RxAcceptContainedI"] = None

    @property
    def rx_accept(self) -> Optional["RxAcceptContainedI"]:
        """Get rxAccept (Pythonic accessor)."""
        return self._rxAccept

    @rx_accept.setter
    def rx_accept(self, value: Optional["RxAcceptContainedI"]) -> None:
        """
        Set rxAccept with validation.

        Args:
            value: The rxAccept to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rxAccept = None
            return

        if not isinstance(value, RxAcceptContainedI):
            raise TypeError(
                f"rxAccept must be RxAcceptContainedI or None, got {type(value).__name__}"
            )
        self._rxAccept = value
        # Defines the size threshold which, when exceeded, sending of the ContainerIPdu
                # although the size has not been reached yet.
        # Unit: byte.
        self._thresholdSize: Optional["PositiveInteger"] = None

    @property
    def threshold_size(self) -> Optional["PositiveInteger"]:
        """Get thresholdSize (Pythonic accessor)."""
        return self._thresholdSize

    @threshold_size.setter
    def threshold_size(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set thresholdSize with validation.

        Args:
            value: The thresholdSize to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._thresholdSize = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"thresholdSize must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._thresholdSize = value
        # IPduM fills not updated areas of the ContainerPdu with byte-pattern.
        self._unusedBit: Optional["PositiveInteger"] = None

    @property
    def unused_bit(self) -> Optional["PositiveInteger"]:
        """Get unusedBit (Pythonic accessor)."""
        return self._unusedBit

    @unused_bit.setter
    def unused_bit(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set unusedBit with validation.

        Args:
            value: The unusedBit to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._unusedBit = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"unusedBit must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._unusedBit = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getContainedIPdu(self) -> List["ContainedIPduProps"]:
        """
        AUTOSAR-compliant getter for containedIPdu.

        Returns:
            The containedIPdu value

        Note:
            Delegates to contained_i_pdu property (CODING_RULE_V2_00017)
        """
        return self.contained_i_pdu  # Delegates to property

    def getContainedPdu(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for containedPdu.

        Returns:
            The containedPdu value

        Note:
            Delegates to contained_pdu property (CODING_RULE_V2_00017)
        """
        return self.contained_pdu  # Delegates to property

    def getContainer(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for container.

        Returns:
            The container value

        Note:
            Delegates to container property (CODING_RULE_V2_00017)
        """
        return self.container  # Delegates to property

    def setContainer(self, value: "TimeValue") -> "ContainerIPdu":
        """
        AUTOSAR-compliant setter for container with method chaining.

        Args:
            value: The container to set

        Returns:
            self for method chaining

        Note:
            Delegates to container property setter (gets validation automatically)
        """
        self.container = value  # Delegates to property setter
        return self

    def getContainerTrigger(self) -> RefType:
        """
        AUTOSAR-compliant getter for containerTrigger.

        Returns:
            The containerTrigger value

        Note:
            Delegates to container_trigger property (CODING_RULE_V2_00017)
        """
        return self.container_trigger  # Delegates to property

    def setContainerTrigger(self, value: RefType) -> "ContainerIPdu":
        """
        AUTOSAR-compliant setter for containerTrigger with method chaining.

        Args:
            value: The containerTrigger to set

        Returns:
            self for method chaining

        Note:
            Delegates to container_trigger property setter (gets validation automatically)
        """
        self.container_trigger = value  # Delegates to property setter
        return self

    def getHeaderType(self) -> "ContainerIPduHeader":
        """
        AUTOSAR-compliant getter for headerType.

        Returns:
            The headerType value

        Note:
            Delegates to header_type property (CODING_RULE_V2_00017)
        """
        return self.header_type  # Delegates to property

    def setHeaderType(self, value: "ContainerIPduHeader") -> "ContainerIPdu":
        """
        AUTOSAR-compliant setter for headerType with method chaining.

        Args:
            value: The headerType to set

        Returns:
            self for method chaining

        Note:
            Delegates to header_type property setter (gets validation automatically)
        """
        self.header_type = value  # Delegates to property setter
        return self

    def getMinimumRx(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for minimumRx.

        Returns:
            The minimumRx value

        Note:
            Delegates to minimum_rx property (CODING_RULE_V2_00017)
        """
        return self.minimum_rx  # Delegates to property

    def setMinimumRx(self, value: "PositiveInteger") -> "ContainerIPdu":
        """
        AUTOSAR-compliant setter for minimumRx with method chaining.

        Args:
            value: The minimumRx to set

        Returns:
            self for method chaining

        Note:
            Delegates to minimum_rx property setter (gets validation automatically)
        """
        self.minimum_rx = value  # Delegates to property setter
        return self

    def getMinimumTx(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for minimumTx.

        Returns:
            The minimumTx value

        Note:
            Delegates to minimum_tx property (CODING_RULE_V2_00017)
        """
        return self.minimum_tx  # Delegates to property

    def setMinimumTx(self, value: "PositiveInteger") -> "ContainerIPdu":
        """
        AUTOSAR-compliant setter for minimumTx with method chaining.

        Args:
            value: The minimumTx to set

        Returns:
            self for method chaining

        Note:
            Delegates to minimum_tx property setter (gets validation automatically)
        """
        self.minimum_tx = value  # Delegates to property setter
        return self

    def getRxAccept(self) -> "RxAcceptContainedI":
        """
        AUTOSAR-compliant getter for rxAccept.

        Returns:
            The rxAccept value

        Note:
            Delegates to rx_accept property (CODING_RULE_V2_00017)
        """
        return self.rx_accept  # Delegates to property

    def setRxAccept(self, value: "RxAcceptContainedI") -> "ContainerIPdu":
        """
        AUTOSAR-compliant setter for rxAccept with method chaining.

        Args:
            value: The rxAccept to set

        Returns:
            self for method chaining

        Note:
            Delegates to rx_accept property setter (gets validation automatically)
        """
        self.rx_accept = value  # Delegates to property setter
        return self

    def getThresholdSize(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for thresholdSize.

        Returns:
            The thresholdSize value

        Note:
            Delegates to threshold_size property (CODING_RULE_V2_00017)
        """
        return self.threshold_size  # Delegates to property

    def setThresholdSize(self, value: "PositiveInteger") -> "ContainerIPdu":
        """
        AUTOSAR-compliant setter for thresholdSize with method chaining.

        Args:
            value: The thresholdSize to set

        Returns:
            self for method chaining

        Note:
            Delegates to threshold_size property setter (gets validation automatically)
        """
        self.threshold_size = value  # Delegates to property setter
        return self

    def getUnusedBit(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for unusedBit.

        Returns:
            The unusedBit value

        Note:
            Delegates to unused_bit property (CODING_RULE_V2_00017)
        """
        return self.unused_bit  # Delegates to property

    def setUnusedBit(self, value: "PositiveInteger") -> "ContainerIPdu":
        """
        AUTOSAR-compliant setter for unusedBit with method chaining.

        Args:
            value: The unusedBit to set

        Returns:
            self for method chaining

        Note:
            Delegates to unused_bit property setter (gets validation automatically)
        """
        self.unused_bit = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_container(self, value: Optional["TimeValue"]) -> "ContainerIPdu":
        """
        Set container and return self for chaining.

        Args:
            value: The container to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_container("value")
        """
        self.container = value  # Use property setter (gets validation)
        return self

    def with_container_trigger(self, value: Optional[RefType]) -> "ContainerIPdu":
        """
        Set containerTrigger and return self for chaining.

        Args:
            value: The containerTrigger to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_container_trigger("value")
        """
        self.container_trigger = value  # Use property setter (gets validation)
        return self

    def with_header_type(self, value: Optional["ContainerIPduHeader"]) -> "ContainerIPdu":
        """
        Set headerType and return self for chaining.

        Args:
            value: The headerType to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_header_type("value")
        """
        self.header_type = value  # Use property setter (gets validation)
        return self

    def with_minimum_rx(self, value: Optional["PositiveInteger"]) -> "ContainerIPdu":
        """
        Set minimumRx and return self for chaining.

        Args:
            value: The minimumRx to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_minimum_rx("value")
        """
        self.minimum_rx = value  # Use property setter (gets validation)
        return self

    def with_minimum_tx(self, value: Optional["PositiveInteger"]) -> "ContainerIPdu":
        """
        Set minimumTx and return self for chaining.

        Args:
            value: The minimumTx to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_minimum_tx("value")
        """
        self.minimum_tx = value  # Use property setter (gets validation)
        return self

    def with_rx_accept(self, value: Optional["RxAcceptContainedI"]) -> "ContainerIPdu":
        """
        Set rxAccept and return self for chaining.

        Args:
            value: The rxAccept to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_rx_accept("value")
        """
        self.rx_accept = value  # Use property setter (gets validation)
        return self

    def with_threshold_size(self, value: Optional["PositiveInteger"]) -> "ContainerIPdu":
        """
        Set thresholdSize and return self for chaining.

        Args:
            value: The thresholdSize to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_threshold_size("value")
        """
        self.threshold_size = value  # Use property setter (gets validation)
        return self

    def with_unused_bit(self, value: Optional["PositiveInteger"]) -> "ContainerIPdu":
        """
        Set unusedBit and return self for chaining.

        Args:
            value: The unusedBit to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_unused_bit("value")
        """
        self.unused_bit = value  # Use property setter (gets validation)
        return self

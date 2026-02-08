from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class ContainedIPduProps(ARObject):
    """
    Defines the aspects of an IPdu which can be collected inside a
    ContainerIPdu.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::ContainedIPduProps

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 355, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines whether this ContainedIPdu shall be collected using a last-is-best or
        # queued semantics.
        self._collection: Optional["ContainedIPdu"] = None

    @property
    def collection(self) -> Optional["ContainedIPdu"]:
        """Get collection (Pythonic accessor)."""
        return self._collection

    @collection.setter
    def collection(self, value: Optional["ContainedIPdu"]) -> None:
        """
        Set collection with validation.

        Args:
            value: The collection to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._collection = None
            return

        if not isinstance(value, ContainedIPdu):
            raise TypeError(
                f"collection must be ContainedIPdu or None, got {type(value).__name__}"
            )
        self._collection = value
        # Reference to Pdu for which the ContainedIPduProps are.
        self._containedPdu: RefType = None

    @property
    def contained_pdu(self) -> RefType:
        """Get containedPdu (Pythonic accessor)."""
        return self._containedPdu

    @contained_pdu.setter
    def contained_pdu(self, value: RefType) -> None:
        """
        Set containedPdu with validation.

        Args:
            value: The containedPdu to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._containedPdu = None
            return

        self._containedPdu = value
        # Defines the header id this IPdu shall have in case this is put inside a
        # ContainerIPdu with headerType = 2090 Document ID 63:
        # AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._headerIdLong: Optional["PositiveInteger"] = None

    @property
    def header_id_long(self) -> Optional["PositiveInteger"]:
        """Get headerIdLong (Pythonic accessor)."""
        return self._headerIdLong

    @header_id_long.setter
    def header_id_long(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set headerIdLong with validation.

        Args:
            value: The headerIdLong to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._headerIdLong = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"headerIdLong must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._headerIdLong = value
        # Defines the header id this IPdu shall have in case this is put inside a
        # ContainerIPdu with headerType =.
        self._headerIdShort: Optional["PositiveInteger"] = None

    @property
    def header_id_short(self) -> Optional["PositiveInteger"]:
        """Get headerIdShort (Pythonic accessor)."""
        return self._headerIdShort

    @header_id_short.setter
    def header_id_short(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set headerIdShort with validation.

        Args:
            value: The headerIdShort to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._headerIdShort = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"headerIdShort must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._headerIdShort = value
        # Byte offset that describes the location of the Contained the ContainerPdu if
        # no header is used.
        self._offset: Optional["PositiveInteger"] = None

    @property
    def offset(self) -> Optional["PositiveInteger"]:
        """Get offset (Pythonic accessor)."""
        return self._offset

    @offset.setter
    def offset(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set offset with validation.

        Args:
            value: The offset to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._offset = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"offset must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._offset = value
        # Defines a priority of a ContainedTxPdu.
        # 255 represents priority and 0 represent the highest priority.
        self._priority: Optional["PositiveInteger"] = None

    @property
    def priority(self) -> Optional["PositiveInteger"]:
        """Get priority (Pythonic accessor)."""
        return self._priority

    @priority.setter
    def priority(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set priority with validation.

        Args:
            value: The priority to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._priority = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"priority must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._priority = value
        # Defines a IPdu specific sender timeout which can reduce timer when this
                # containedIPdu is put ContainerIPdu.
        # This attribute is ignored on.
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
        # Defines whether this IPdu does trigger the sending of the This attribute is
        # ignored on receiver side.
        self._trigger: RefType = None

    @property
    def trigger(self) -> RefType:
        """Get trigger (Pythonic accessor)."""
        return self._trigger

    @trigger.setter
    def trigger(self, value: RefType) -> None:
        """
        Set trigger with validation.

        Args:
            value: The trigger to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._trigger = None
            return

        self._trigger = value
        # The updateIndicationBit specifies the bit location of Update-Bit in the
                # Container PDU.
        # It to the receivers that the ContainedIPdu in the updated.
        self._update: Optional["PositiveInteger"] = None

    @property
    def update(self) -> Optional["PositiveInteger"]:
        """Get update (Pythonic accessor)."""
        return self._update

    @update.setter
    def update(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set update with validation.

        Args:
            value: The update to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._update = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"update must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._update = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCollection(self) -> "ContainedIPdu":
        """
        AUTOSAR-compliant getter for collection.

        Returns:
            The collection value

        Note:
            Delegates to collection property (CODING_RULE_V2_00017)
        """
        return self.collection  # Delegates to property

    def setCollection(self, value: "ContainedIPdu") -> "ContainedIPduProps":
        """
        AUTOSAR-compliant setter for collection with method chaining.

        Args:
            value: The collection to set

        Returns:
            self for method chaining

        Note:
            Delegates to collection property setter (gets validation automatically)
        """
        self.collection = value  # Delegates to property setter
        return self

    def getContainedPdu(self) -> RefType:
        """
        AUTOSAR-compliant getter for containedPdu.

        Returns:
            The containedPdu value

        Note:
            Delegates to contained_pdu property (CODING_RULE_V2_00017)
        """
        return self.contained_pdu  # Delegates to property

    def setContainedPdu(self, value: RefType) -> "ContainedIPduProps":
        """
        AUTOSAR-compliant setter for containedPdu with method chaining.

        Args:
            value: The containedPdu to set

        Returns:
            self for method chaining

        Note:
            Delegates to contained_pdu property setter (gets validation automatically)
        """
        self.contained_pdu = value  # Delegates to property setter
        return self

    def getHeaderIdLong(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for headerIdLong.

        Returns:
            The headerIdLong value

        Note:
            Delegates to header_id_long property (CODING_RULE_V2_00017)
        """
        return self.header_id_long  # Delegates to property

    def setHeaderIdLong(self, value: "PositiveInteger") -> "ContainedIPduProps":
        """
        AUTOSAR-compliant setter for headerIdLong with method chaining.

        Args:
            value: The headerIdLong to set

        Returns:
            self for method chaining

        Note:
            Delegates to header_id_long property setter (gets validation automatically)
        """
        self.header_id_long = value  # Delegates to property setter
        return self

    def getHeaderIdShort(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for headerIdShort.

        Returns:
            The headerIdShort value

        Note:
            Delegates to header_id_short property (CODING_RULE_V2_00017)
        """
        return self.header_id_short  # Delegates to property

    def setHeaderIdShort(self, value: "PositiveInteger") -> "ContainedIPduProps":
        """
        AUTOSAR-compliant setter for headerIdShort with method chaining.

        Args:
            value: The headerIdShort to set

        Returns:
            self for method chaining

        Note:
            Delegates to header_id_short property setter (gets validation automatically)
        """
        self.header_id_short = value  # Delegates to property setter
        return self

    def getOffset(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for offset.

        Returns:
            The offset value

        Note:
            Delegates to offset property (CODING_RULE_V2_00017)
        """
        return self.offset  # Delegates to property

    def setOffset(self, value: "PositiveInteger") -> "ContainedIPduProps":
        """
        AUTOSAR-compliant setter for offset with method chaining.

        Args:
            value: The offset to set

        Returns:
            self for method chaining

        Note:
            Delegates to offset property setter (gets validation automatically)
        """
        self.offset = value  # Delegates to property setter
        return self

    def getPriority(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for priority.

        Returns:
            The priority value

        Note:
            Delegates to priority property (CODING_RULE_V2_00017)
        """
        return self.priority  # Delegates to property

    def setPriority(self, value: "PositiveInteger") -> "ContainedIPduProps":
        """
        AUTOSAR-compliant setter for priority with method chaining.

        Args:
            value: The priority to set

        Returns:
            self for method chaining

        Note:
            Delegates to priority property setter (gets validation automatically)
        """
        self.priority = value  # Delegates to property setter
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

    def setTimeout(self, value: "TimeValue") -> "ContainedIPduProps":
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

    def getTrigger(self) -> RefType:
        """
        AUTOSAR-compliant getter for trigger.

        Returns:
            The trigger value

        Note:
            Delegates to trigger property (CODING_RULE_V2_00017)
        """
        return self.trigger  # Delegates to property

    def setTrigger(self, value: RefType) -> "ContainedIPduProps":
        """
        AUTOSAR-compliant setter for trigger with method chaining.

        Args:
            value: The trigger to set

        Returns:
            self for method chaining

        Note:
            Delegates to trigger property setter (gets validation automatically)
        """
        self.trigger = value  # Delegates to property setter
        return self

    def getUpdate(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for update.

        Returns:
            The update value

        Note:
            Delegates to update property (CODING_RULE_V2_00017)
        """
        return self.update  # Delegates to property

    def setUpdate(self, value: "PositiveInteger") -> "ContainedIPduProps":
        """
        AUTOSAR-compliant setter for update with method chaining.

        Args:
            value: The update to set

        Returns:
            self for method chaining

        Note:
            Delegates to update property setter (gets validation automatically)
        """
        self.update = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_collection(self, value: Optional["ContainedIPdu"]) -> "ContainedIPduProps":
        """
        Set collection and return self for chaining.

        Args:
            value: The collection to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_collection("value")
        """
        self.collection = value  # Use property setter (gets validation)
        return self

    def with_contained_pdu(self, value: Optional[RefType]) -> "ContainedIPduProps":
        """
        Set containedPdu and return self for chaining.

        Args:
            value: The containedPdu to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_contained_pdu("value")
        """
        self.contained_pdu = value  # Use property setter (gets validation)
        return self

    def with_header_id_long(self, value: Optional["PositiveInteger"]) -> "ContainedIPduProps":
        """
        Set headerIdLong and return self for chaining.

        Args:
            value: The headerIdLong to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_header_id_long("value")
        """
        self.header_id_long = value  # Use property setter (gets validation)
        return self

    def with_header_id_short(self, value: Optional["PositiveInteger"]) -> "ContainedIPduProps":
        """
        Set headerIdShort and return self for chaining.

        Args:
            value: The headerIdShort to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_header_id_short("value")
        """
        self.header_id_short = value  # Use property setter (gets validation)
        return self

    def with_offset(self, value: Optional["PositiveInteger"]) -> "ContainedIPduProps":
        """
        Set offset and return self for chaining.

        Args:
            value: The offset to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_offset("value")
        """
        self.offset = value  # Use property setter (gets validation)
        return self

    def with_priority(self, value: Optional["PositiveInteger"]) -> "ContainedIPduProps":
        """
        Set priority and return self for chaining.

        Args:
            value: The priority to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_priority("value")
        """
        self.priority = value  # Use property setter (gets validation)
        return self

    def with_timeout(self, value: Optional["TimeValue"]) -> "ContainedIPduProps":
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

    def with_trigger(self, value: Optional[RefType]) -> "ContainedIPduProps":
        """
        Set trigger and return self for chaining.

        Args:
            value: The trigger to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_trigger("value")
        """
        self.trigger = value  # Use property setter (gets validation)
        return self

    def with_update(self, value: Optional["PositiveInteger"]) -> "ContainedIPduProps":
        """
        Set update and return self for chaining.

        Args:
            value: The update to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_update("value")
        """
        self.update = value  # Use property setter (gets validation)
        return self

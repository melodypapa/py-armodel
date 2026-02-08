from typing import List, Optional
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.IEEE1722Tp import IEEE1722TpConnection


class IEEE1722TpAcfConnection(IEEE1722TpConnection):
    """
    ACF IEEE1722Tp connection.

    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::IEEE1722Tp::IEEE1722TpAcfConnection

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 656, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Definition of the transported busses over this ACF atpVariation.
        self._acfTransported: List["IEEE1722TpAcfBus"] = []

    @property
    def acf_transported(self) -> List["IEEE1722TpAcfBus"]:
        """Get acfTransported (Pythonic accessor)."""
        return self._acfTransported
        # When this timeout expires the IEEE1722Tp ACF is triggered for sending.
        # The respective timer is the first Pdu is put into the IEEE1722Tp seconds.
        self._collection: Optional["TimeValue"] = None

    @property
    def collection(self) -> Optional["TimeValue"]:
        """Get collection (Pythonic accessor)."""
        return self._collection

    @collection.setter
    def collection(self, value: Optional["TimeValue"]) -> None:
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

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"collection must be TimeValue or None, got {type(value).__name__}"
            )
        self._collection = value
        # Defines if this ACF-stream is allowed to collect of different bus kinds (i.
        # e.
        # whether it is collect CAN and LIN ACF-messages in one.
        self._mixedBusType: Optional["Boolean"] = None

    @property
    def mixed_bus_type(self) -> Optional["Boolean"]:
        """Get mixedBusType (Pythonic accessor)."""
        return self._mixedBusType

    @mixed_bus_type.setter
    def mixed_bus_type(self, value: Optional["Boolean"]) -> None:
        """
        Set mixedBusType with validation.

        Args:
            value: The mixedBusType to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._mixedBusType = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"mixedBusType must be Boolean or None, got {type(value).__name__}"
            )
        self._mixedBusType = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAcfTransported(self) -> List["IEEE1722TpAcfBus"]:
        """
        AUTOSAR-compliant getter for acfTransported.

        Returns:
            The acfTransported value

        Note:
            Delegates to acf_transported property (CODING_RULE_V2_00017)
        """
        return self.acf_transported  # Delegates to property

    def getCollection(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for collection.

        Returns:
            The collection value

        Note:
            Delegates to collection property (CODING_RULE_V2_00017)
        """
        return self.collection  # Delegates to property

    def setCollection(self, value: "TimeValue") -> "IEEE1722TpAcfConnection":
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

    def getMixedBusType(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for mixedBusType.

        Returns:
            The mixedBusType value

        Note:
            Delegates to mixed_bus_type property (CODING_RULE_V2_00017)
        """
        return self.mixed_bus_type  # Delegates to property

    def setMixedBusType(self, value: "Boolean") -> "IEEE1722TpAcfConnection":
        """
        AUTOSAR-compliant setter for mixedBusType with method chaining.

        Args:
            value: The mixedBusType to set

        Returns:
            self for method chaining

        Note:
            Delegates to mixed_bus_type property setter (gets validation automatically)
        """
        self.mixed_bus_type = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_collection(self, value: Optional["TimeValue"]) -> "IEEE1722TpAcfConnection":
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

    def with_mixed_bus_type(self, value: Optional["Boolean"]) -> "IEEE1722TpAcfConnection":
        """
        Set mixedBusType and return self for chaining.

        Args:
            value: The mixedBusType to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mixed_bus_type("value")
        """
        self.mixed_bus_type = value  # Use property setter (gets validation)
        return self

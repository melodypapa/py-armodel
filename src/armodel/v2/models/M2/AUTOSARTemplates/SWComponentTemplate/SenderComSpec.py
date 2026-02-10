from abc import ABC
from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import (
    PPortComSpec,
)

    RefType,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class SenderComSpec(PPortComSpec, ABC):
    """
    Communication attributes for a sender port (PPortPrototype typed by
    SenderReceiverInterface).

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Communication

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
        self._dataElement: RefType = None

    @property
    def data_element(self) -> RefType:
        """Get dataElement (Pythonic accessor)."""
        return self._dataElement

    @data_element.setter
    def data_element(self, value: RefType) -> None:
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

        if not isinstance(value, Boolean):
            raise TypeError(
                f"usesEndToEnd must be Boolean or None, got {type(value).__name__}"
            )
        self._usesEndToEnd = value

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

    def getDataElement(self) -> RefType:
        """
        AUTOSAR-compliant getter for dataElement.

        Returns:
            The dataElement value

        Note:
            Delegates to data_element property (CODING_RULE_V2_00017)
        """
        return self.data_element  # Delegates to property

    def setDataElement(self, value: RefType) -> "SenderComSpec":
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

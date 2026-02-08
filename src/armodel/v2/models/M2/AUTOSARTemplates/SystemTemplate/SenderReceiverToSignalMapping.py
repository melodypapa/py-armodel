from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    DataMapping,
    SystemSignal,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class SenderReceiverToSignalMapping(DataMapping):
    """
    Mapping of a sender receiver communication data element to a signal.

    Package: M2::AUTOSARTemplates::SystemTemplate::DataMapping::SenderReceiverToSignalMapping

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 1005, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 229, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # by: VariableDataPrototypeIn.
        self._dataElementSystemInstanceRef: RefType = None

    @property
    def data_element_system_instance_ref(self) -> RefType:
        """Get dataElementSystemInstanceRef (Pythonic accessor)."""
        return self._dataElementSystemInstanceRef

    @data_element_system_instance_ref.setter
    def data_element_system_instance_ref(self, value: RefType) -> None:
        """
        Set dataElementSystemInstanceRef with validation.

        Args:
            value: The dataElementSystemInstanceRef to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dataElementSystemInstanceRef = None
            return

        self._dataElementSystemInstanceRef = value
        # This mapping allows for the text-table translation between sending
        # DataPrototype that is defined in the Port and the physicalProps defined for
        # the System.
        self._senderToSignal: RefType = None

    @property
    def sender_to_signal(self) -> RefType:
        """Get senderToSignal (Pythonic accessor)."""
        return self._senderToSignal

    @sender_to_signal.setter
    def sender_to_signal(self, value: RefType) -> None:
        """
        Set senderToSignal with validation.

        Args:
            value: The senderToSignal to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._senderToSignal = None
            return

        self._senderToSignal = value
        # This mapping allows for the text-table translation between physicalProps
        # defined for the SystemSignal and a DataPrototype that is defined in the Port.
        self._signalTo: RefType = None

    @property
    def signal_to(self) -> RefType:
        """Get signalTo (Pythonic accessor)."""
        return self._signalTo

    @signal_to.setter
    def signal_to(self, value: RefType) -> None:
        """
        Set signalTo with validation.

        Args:
            value: The signalTo to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._signalTo = None
            return

        self._signalTo = value
        # Reference to the system signal used to carry the data.
        self._systemSignal: Optional["SystemSignal"] = None

    @property
    def system_signal(self) -> Optional["SystemSignal"]:
        """Get systemSignal (Pythonic accessor)."""
        return self._systemSignal

    @system_signal.setter
    def system_signal(self, value: Optional["SystemSignal"]) -> None:
        """
        Set systemSignal with validation.

        Args:
            value: The systemSignal to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._systemSignal = None
            return

        if not isinstance(value, SystemSignal):
            raise TypeError(
                f"systemSignal must be SystemSignal or None, got {type(value).__name__}"
            )
        self._systemSignal = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDataElementSystemInstanceRef(self) -> RefType:
        """
        AUTOSAR-compliant getter for dataElementSystemInstanceRef.

        Returns:
            The dataElementSystemInstanceRef value

        Note:
            Delegates to data_element_system_instance_ref property (CODING_RULE_V2_00017)
        """
        return self.data_element_system_instance_ref  # Delegates to property

    def setDataElementSystemInstanceRef(self, value: RefType) -> "SenderReceiverToSignalMapping":
        """
        AUTOSAR-compliant setter for dataElementSystemInstanceRef with method chaining.

        Args:
            value: The dataElementSystemInstanceRef to set

        Returns:
            self for method chaining

        Note:
            Delegates to data_element_system_instance_ref property setter (gets validation automatically)
        """
        self.data_element_system_instance_ref = value  # Delegates to property setter
        return self

    def getSenderToSignal(self) -> RefType:
        """
        AUTOSAR-compliant getter for senderToSignal.

        Returns:
            The senderToSignal value

        Note:
            Delegates to sender_to_signal property (CODING_RULE_V2_00017)
        """
        return self.sender_to_signal  # Delegates to property

    def setSenderToSignal(self, value: RefType) -> "SenderReceiverToSignalMapping":
        """
        AUTOSAR-compliant setter for senderToSignal with method chaining.

        Args:
            value: The senderToSignal to set

        Returns:
            self for method chaining

        Note:
            Delegates to sender_to_signal property setter (gets validation automatically)
        """
        self.sender_to_signal = value  # Delegates to property setter
        return self

    def getSignalTo(self) -> RefType:
        """
        AUTOSAR-compliant getter for signalTo.

        Returns:
            The signalTo value

        Note:
            Delegates to signal_to property (CODING_RULE_V2_00017)
        """
        return self.signal_to  # Delegates to property

    def setSignalTo(self, value: RefType) -> "SenderReceiverToSignalMapping":
        """
        AUTOSAR-compliant setter for signalTo with method chaining.

        Args:
            value: The signalTo to set

        Returns:
            self for method chaining

        Note:
            Delegates to signal_to property setter (gets validation automatically)
        """
        self.signal_to = value  # Delegates to property setter
        return self

    def getSystemSignal(self) -> "SystemSignal":
        """
        AUTOSAR-compliant getter for systemSignal.

        Returns:
            The systemSignal value

        Note:
            Delegates to system_signal property (CODING_RULE_V2_00017)
        """
        return self.system_signal  # Delegates to property

    def setSystemSignal(self, value: "SystemSignal") -> "SenderReceiverToSignalMapping":
        """
        AUTOSAR-compliant setter for systemSignal with method chaining.

        Args:
            value: The systemSignal to set

        Returns:
            self for method chaining

        Note:
            Delegates to system_signal property setter (gets validation automatically)
        """
        self.system_signal = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_data_element_system_instance_ref(self, value: Optional[RefType]) -> "SenderReceiverToSignalMapping":
        """
        Set dataElementSystemInstanceRef and return self for chaining.

        Args:
            value: The dataElementSystemInstanceRef to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_data_element_system_instance_ref("value")
        """
        self.data_element_system_instance_ref = value  # Use property setter (gets validation)
        return self

    def with_sender_to_signal(self, value: Optional[RefType]) -> "SenderReceiverToSignalMapping":
        """
        Set senderToSignal and return self for chaining.

        Args:
            value: The senderToSignal to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sender_to_signal("value")
        """
        self.sender_to_signal = value  # Use property setter (gets validation)
        return self

    def with_signal_to(self, value: Optional[RefType]) -> "SenderReceiverToSignalMapping":
        """
        Set signalTo and return self for chaining.

        Args:
            value: The signalTo to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_signal_to("value")
        """
        self.signal_to = value  # Use property setter (gets validation)
        return self

    def with_system_signal(self, value: Optional["SystemSignal"]) -> "SenderReceiverToSignalMapping":
        """
        Set systemSignal and return self for chaining.

        Args:
            value: The systemSignal to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_system_signal("value")
        """
        self.system_signal = value  # Use property setter (gets validation)
        return self

from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping import SenderRecCompositeTypeMapping

    RefType,
)


class SenderRecArrayTypeMapping(SenderRecCompositeTypeMapping):
    """
    If the ApplicationCompositeDataType is an Array, the "ArrayTypeMapping" will
    be used.

    Package: M2::AUTOSARTemplates::SystemTemplate::DataMapping::SenderRecArrayTypeMapping

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 235, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Each ApplicationArrayElement shall be mapped on a SystemSignal.
        self._arrayElement: List["SenderRecArray"] = []

    @property
    def array_element(self) -> List["SenderRecArray"]:
        """Get arrayElement (Pythonic accessor)."""
        return self._arrayElement
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

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getArrayElement(self) -> List["SenderRecArray"]:
        """
        AUTOSAR-compliant getter for arrayElement.

        Returns:
            The arrayElement value

        Note:
            Delegates to array_element property (CODING_RULE_V2_00017)
        """
        return self.array_element  # Delegates to property

    def getSenderToSignal(self) -> RefType:
        """
        AUTOSAR-compliant getter for senderToSignal.

        Returns:
            The senderToSignal value

        Note:
            Delegates to sender_to_signal property (CODING_RULE_V2_00017)
        """
        return self.sender_to_signal  # Delegates to property

    def setSenderToSignal(self, value: RefType) -> "SenderRecArrayTypeMapping":
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

    def setSignalTo(self, value: RefType) -> "SenderRecArrayTypeMapping":
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

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_sender_to_signal(self, value: Optional[RefType]) -> "SenderRecArrayTypeMapping":
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

    def with_signal_to(self, value: Optional[RefType]) -> "SenderRecArrayTypeMapping":
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

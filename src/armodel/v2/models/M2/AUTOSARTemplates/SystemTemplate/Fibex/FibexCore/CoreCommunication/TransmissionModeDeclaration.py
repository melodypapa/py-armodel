from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    ModeDriven,
    TransmissionMode,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class TransmissionModeDeclaration(ARObject):
    """
    AUTOSAR COM provides the possibility to define two different TRANSMISSION
    MODES (True and False) for each I-PDU. As TransmissionMode selector the
    signal content can be evaluated via transmissionModeCondition (implemented
    directly in the COM module) or mode conditions can be defined with the
    modeDrivenTrue Condition or modeDrivenFalseCondition (evaluated by BswM and
    invoking Com_SwitchIpduTxMode COM API). If modeDrivenTrueCondition and
    modeDrivenFalseCondition are defined they shall never evaluate to true both
    at the same time. The mixing of Transmission Mode Switch via API and signal
    value is not allowed.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::Timing::TransmissionModeDeclaration

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 392, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines the trigger for the Com_SwitchIpduTxMode Transmission Mode switch.
        # Only if all defined modeDriven evaluate to true (AND associated) the be
                # activated.
        # mode modeDrivenFalseCondition evaluate to true both at the same time.
        self._modeDriven: List["ModeDriven"] = []

    @property
    def mode_driven(self) -> List["ModeDriven"]:
        """Get modeDriven (Pythonic accessor)."""
        return self._modeDriven
        # Timing Specification if the COM Transmission Mode is true.
        # The Transmission Mode Selector is defined to be if at least one Condition
                # evaluates to true.
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

    def getModeDriven(self) -> List["ModeDriven"]:
        """
        AUTOSAR-compliant getter for modeDriven.

        Returns:
            The modeDriven value

        Note:
            Delegates to mode_driven property (CODING_RULE_V2_00017)
        """
        return self.mode_driven  # Delegates to property

    def getTransmission(self) -> "TransmissionMode":
        """
        AUTOSAR-compliant getter for transmission.

        Returns:
            The transmission value

        Note:
            Delegates to transmission property (CODING_RULE_V2_00017)
        """
        return self.transmission  # Delegates to property

    def setTransmission(self, value: "TransmissionMode") -> "TransmissionModeDeclaration":
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

    def with_transmission(self, value: Optional["TransmissionMode"]) -> "TransmissionModeDeclaration":
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

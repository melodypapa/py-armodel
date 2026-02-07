from abc import ABC
from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class CommConnectorPort(Identifiable, ABC):
    """
    The Ecu communication relationship defines which signals, Pdus and frames
    are actually received and transmitted by this ECU. For each signal, Pdu or
    Frame that is transmitted or received and used by the Ecu an association
    between an ISignalPort, IPduPort or FramePort with the corresponding
    Triggering shall be created. An ISignalPort shall be created only if the
    corresponding signal is handled by COM (RTE or Signal Gateway). If a Pdu
    Gateway ECU only routes the Pdu without being interested in the content only
    a FramePort and an IPduPort needs to be created.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreTopology::CommConnectorPort

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 303, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is CommConnectorPort:
            raise TypeError("CommConnectorPort is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Communication Direction of the Connector Port (input or output Port).
        self._communication: Optional["Communication"] = None

    @property
    def communication(self) -> Optional["Communication"]:
        """Get communication (Pythonic accessor)."""
        return self._communication

    @communication.setter
    def communication(self, value: Optional["Communication"]) -> None:
        """
        Set communication with validation.

        Args:
            value: The communication to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._communication = None
            return

        if not isinstance(value, Communication):
            raise TypeError(
                f"communication must be Communication or None, got {type(value).__name__}"
            )
        self._communication = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCommunication(self) -> "Communication":
        """
        AUTOSAR-compliant getter for communication.

        Returns:
            The communication value

        Note:
            Delegates to communication property (CODING_RULE_V2_00017)
        """
        return self.communication  # Delegates to property

    def setCommunication(self, value: "Communication") -> "CommConnectorPort":
        """
        AUTOSAR-compliant setter for communication with method chaining.

        Args:
            value: The communication to set

        Returns:
            self for method chaining

        Note:
            Delegates to communication property setter (gets validation automatically)
        """
        self.communication = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_communication(self, value: Optional["Communication"]) -> "CommConnectorPort":
        """
        Set communication and return self for chaining.

        Args:
            value: The communication to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_communication("value")
        """
        self.communication = value  # Use property setter (gets validation)
        return self

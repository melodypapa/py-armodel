from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class ISignalProps(ARObject):
    """
    Additional ISignal properties that may be stored in different files.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::ISignalProps

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 323, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute defines the outOfRangeHandling for received and sent signals.
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

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getHandleOutOf(self) -> "HandleOutOfRange":
        """
        AUTOSAR-compliant getter for handleOutOf.

        Returns:
            The handleOutOf value

        Note:
            Delegates to handle_out_of property (CODING_RULE_V2_00017)
        """
        return self.handle_out_of  # Delegates to property

    def setHandleOutOf(self, value: "HandleOutOfRange") -> "ISignalProps":
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

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_handle_out_of(self, value: Optional["HandleOutOfRange"]) -> "ISignalProps":
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

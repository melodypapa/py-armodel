from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription import TDEventBsw

    RefType,
)


class TDEventBswModeDeclaration(TDEventBsw):
    """
    This is used to describe timing events related to the mode communication on
    BSW level.

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingDescription::TimingDescription::TDEventBswModeDeclaration

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 76, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Optional parameter which refines the scope of the If the parameter is set,
        # the only if the mode declaration group prototype enter into the referenced
        # ModeDeclaration.
        self._entryMode: Optional["ModeDeclaration"] = None

    @property
    def entry_mode(self) -> Optional["ModeDeclaration"]:
        """Get entryMode (Pythonic accessor)."""
        return self._entryMode

    @entry_mode.setter
    def entry_mode(self, value: Optional["ModeDeclaration"]) -> None:
        """
        Set entryMode with validation.

        Args:
            value: The entryMode to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._entryMode = None
            return

        if not isinstance(value, ModeDeclaration):
            raise TypeError(
                f"entryMode must be ModeDeclaration or None, got {type(value).__name__}"
            )
        self._entryMode = value
        # Optional parameter which refines the scope of the If the parameter is set,
        # the only if the mode declaration group prototype exit from the referenced
        # ModeDeclaration.
        self._exitMode: Optional["ModeDeclaration"] = None

    @property
    def exit_mode(self) -> Optional["ModeDeclaration"]:
        """Get exitMode (Pythonic accessor)."""
        return self._exitMode

    @exit_mode.setter
    def exit_mode(self, value: Optional["ModeDeclaration"]) -> None:
        """
        Set exitMode with validation.

        Args:
            value: The exitMode to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._exitMode = None
            return

        if not isinstance(value, ModeDeclaration):
            raise TypeError(
                f"exitMode must be ModeDeclaration or None, got {type(value).__name__}"
            )
        self._exitMode = value
        # The scope of this timing event.
        # 277 Document ID 411: AUTOSAR_CP_TPS_TimingExtensions Timing Extensions for
                # Classic R23-11.
        self._mode: RefType = None

    @property
    def mode(self) -> RefType:
        """Get mode (Pythonic accessor)."""
        return self._mode

    @mode.setter
    def mode(self, value: RefType) -> None:
        """
        Set mode with validation.

        Args:
            value: The mode to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._mode = None
            return

        self._mode = value
        # The specific type of this timing event.
        self._tdEventBswDeclarationType: Optional["TDEventBswMode"] = None

    @property
    def td_event_bsw_declaration_type(self) -> Optional["TDEventBswMode"]:
        """Get tdEventBswDeclarationType (Pythonic accessor)."""
        return self._tdEventBswDeclarationType

    @td_event_bsw_declaration_type.setter
    def td_event_bsw_declaration_type(self, value: Optional["TDEventBswMode"]) -> None:
        """
        Set tdEventBswDeclarationType with validation.

        Args:
            value: The tdEventBswDeclarationType to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tdEventBswDeclarationType = None
            return

        if not isinstance(value, TDEventBswMode):
            raise TypeError(
                f"tdEventBswDeclarationType must be TDEventBswMode or None, got {type(value).__name__}"
            )
        self._tdEventBswDeclarationType = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEntryMode(self) -> "ModeDeclaration":
        """
        AUTOSAR-compliant getter for entryMode.

        Returns:
            The entryMode value

        Note:
            Delegates to entry_mode property (CODING_RULE_V2_00017)
        """
        return self.entry_mode  # Delegates to property

    def setEntryMode(self, value: "ModeDeclaration") -> "TDEventBswModeDeclaration":
        """
        AUTOSAR-compliant setter for entryMode with method chaining.

        Args:
            value: The entryMode to set

        Returns:
            self for method chaining

        Note:
            Delegates to entry_mode property setter (gets validation automatically)
        """
        self.entry_mode = value  # Delegates to property setter
        return self

    def getExitMode(self) -> "ModeDeclaration":
        """
        AUTOSAR-compliant getter for exitMode.

        Returns:
            The exitMode value

        Note:
            Delegates to exit_mode property (CODING_RULE_V2_00017)
        """
        return self.exit_mode  # Delegates to property

    def setExitMode(self, value: "ModeDeclaration") -> "TDEventBswModeDeclaration":
        """
        AUTOSAR-compliant setter for exitMode with method chaining.

        Args:
            value: The exitMode to set

        Returns:
            self for method chaining

        Note:
            Delegates to exit_mode property setter (gets validation automatically)
        """
        self.exit_mode = value  # Delegates to property setter
        return self

    def getMode(self) -> RefType:
        """
        AUTOSAR-compliant getter for mode.

        Returns:
            The mode value

        Note:
            Delegates to mode property (CODING_RULE_V2_00017)
        """
        return self.mode  # Delegates to property

    def setMode(self, value: RefType) -> "TDEventBswModeDeclaration":
        """
        AUTOSAR-compliant setter for mode with method chaining.

        Args:
            value: The mode to set

        Returns:
            self for method chaining

        Note:
            Delegates to mode property setter (gets validation automatically)
        """
        self.mode = value  # Delegates to property setter
        return self

    def getTdEventBswDeclarationType(self) -> "TDEventBswMode":
        """
        AUTOSAR-compliant getter for tdEventBswDeclarationType.

        Returns:
            The tdEventBswDeclarationType value

        Note:
            Delegates to td_event_bsw_declaration_type property (CODING_RULE_V2_00017)
        """
        return self.td_event_bsw_declaration_type  # Delegates to property

    def setTdEventBswDeclarationType(self, value: "TDEventBswMode") -> "TDEventBswModeDeclaration":
        """
        AUTOSAR-compliant setter for tdEventBswDeclarationType with method chaining.

        Args:
            value: The tdEventBswDeclarationType to set

        Returns:
            self for method chaining

        Note:
            Delegates to td_event_bsw_declaration_type property setter (gets validation automatically)
        """
        self.td_event_bsw_declaration_type = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_entry_mode(self, value: Optional["ModeDeclaration"]) -> "TDEventBswModeDeclaration":
        """
        Set entryMode and return self for chaining.

        Args:
            value: The entryMode to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_entry_mode("value")
        """
        self.entry_mode = value  # Use property setter (gets validation)
        return self

    def with_exit_mode(self, value: Optional["ModeDeclaration"]) -> "TDEventBswModeDeclaration":
        """
        Set exitMode and return self for chaining.

        Args:
            value: The exitMode to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_exit_mode("value")
        """
        self.exit_mode = value  # Use property setter (gets validation)
        return self

    def with_mode(self, value: Optional[RefType]) -> "TDEventBswModeDeclaration":
        """
        Set mode and return self for chaining.

        Args:
            value: The mode to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mode("value")
        """
        self.mode = value  # Use property setter (gets validation)
        return self

    def with_td_event_bsw_declaration_type(self, value: Optional["TDEventBswMode"]) -> "TDEventBswModeDeclaration":
        """
        Set tdEventBswDeclarationType and return self for chaining.

        Args:
            value: The tdEventBswDeclarationType to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_td_event_bsw_declaration_type("value")
        """
        self.td_event_bsw_declaration_type = value  # Use property setter (gets validation)
        return self

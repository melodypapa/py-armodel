from typing import Optional
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription import TDEventBsw


class TDEventBswModule(TDEventBsw):
    """
    This is used to describe timing events related to the interaction between
    BSW modules.

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingDescription::TimingDescription::TDEventBswModule

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 75, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The scope of this timing event.
        self._bswModuleEntry: Optional["BswModuleEntry"] = None

    @property
    def bsw_module_entry(self) -> Optional["BswModuleEntry"]:
        """Get bswModuleEntry (Pythonic accessor)."""
        return self._bswModuleEntry

    @bsw_module_entry.setter
    def bsw_module_entry(self, value: Optional["BswModuleEntry"]) -> None:
        """
        Set bswModuleEntry with validation.

        Args:
            value: The bswModuleEntry to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._bswModuleEntry = None
            return

        if not isinstance(value, BswModuleEntry):
            raise TypeError(
                f"bswModuleEntry must be BswModuleEntry or None, got {type(value).__name__}"
            )
        self._bswModuleEntry = value
        # The specific type of this timing event.
        self._tdEventBsw: Optional["TDEventBswModule"] = None

    @property
    def td_event_bsw(self) -> Optional["TDEventBswModule"]:
        """Get tdEventBsw (Pythonic accessor)."""
        return self._tdEventBsw

    @td_event_bsw.setter
    def td_event_bsw(self, value: Optional["TDEventBswModule"]) -> None:
        """
        Set tdEventBsw with validation.

        Args:
            value: The tdEventBsw to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tdEventBsw = None
            return

        if not isinstance(value, TDEventBswModule):
            raise TypeError(
                f"tdEventBsw must be TDEventBswModule or None, got {type(value).__name__}"
            )
        self._tdEventBsw = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBswModuleEntry(self) -> "BswModuleEntry":
        """
        AUTOSAR-compliant getter for bswModuleEntry.

        Returns:
            The bswModuleEntry value

        Note:
            Delegates to bsw_module_entry property (CODING_RULE_V2_00017)
        """
        return self.bsw_module_entry  # Delegates to property

    def setBswModuleEntry(self, value: "BswModuleEntry") -> "TDEventBswModule":
        """
        AUTOSAR-compliant setter for bswModuleEntry with method chaining.

        Args:
            value: The bswModuleEntry to set

        Returns:
            self for method chaining

        Note:
            Delegates to bsw_module_entry property setter (gets validation automatically)
        """
        self.bsw_module_entry = value  # Delegates to property setter
        return self

    def getTdEventBsw(self) -> "TDEventBswModule":
        """
        AUTOSAR-compliant getter for tdEventBsw.

        Returns:
            The tdEventBsw value

        Note:
            Delegates to td_event_bsw property (CODING_RULE_V2_00017)
        """
        return self.td_event_bsw  # Delegates to property

    def setTdEventBsw(self, value: "TDEventBswModule") -> "TDEventBswModule":
        """
        AUTOSAR-compliant setter for tdEventBsw with method chaining.

        Args:
            value: The tdEventBsw to set

        Returns:
            self for method chaining

        Note:
            Delegates to td_event_bsw property setter (gets validation automatically)
        """
        self.td_event_bsw = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_bsw_module_entry(self, value: Optional["BswModuleEntry"]) -> "TDEventBswModule":
        """
        Set bswModuleEntry and return self for chaining.

        Args:
            value: The bswModuleEntry to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_bsw_module_entry("value")
        """
        self.bsw_module_entry = value  # Use property setter (gets validation)
        return self

    def with_td_event_bsw(self, value: Optional["TDEventBswModule"]) -> "TDEventBswModule":
        """
        Set tdEventBsw and return self for chaining.

        Args:
            value: The tdEventBsw to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_td_event_bsw("value")
        """
        self.td_event_bsw = value  # Use property setter (gets validation)
        return self

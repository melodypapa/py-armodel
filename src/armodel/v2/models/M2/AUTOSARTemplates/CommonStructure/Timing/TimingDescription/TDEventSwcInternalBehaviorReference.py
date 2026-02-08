from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import TDEventSwc


class TDEventSwcInternalBehaviorReference(TDEventSwc):
    """
    This is used to reference timing description events related to the Software
    Component (SW-C) view which are specified in other timing views.

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingDescription::TimingDescription::TDEventSwcInternalBehaviorReference

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 63, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The referenced timing description event.
        self._referencedTDEventSwc: Optional["TDEventSwc"] = None

    @property
    def referenced_td_event_swc(self) -> Optional["TDEventSwc"]:
        """Get referencedTDEventSwc (Pythonic accessor)."""
        return self._referencedTDEventSwc

    @referenced_td_event_swc.setter
    def referenced_td_event_swc(self, value: Optional["TDEventSwc"]) -> None:
        """
        Set referencedTDEventSwc with validation.

        Args:
            value: The referencedTDEventSwc to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._referencedTDEventSwc = None
            return

        if not isinstance(value, TDEventSwc):
            raise TypeError(
                f"referencedTDEventSwc must be TDEventSwc or None, got {type(value).__name__}"
            )
        self._referencedTDEventSwc = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getReferencedTDEventSwc(self) -> "TDEventSwc":
        """
        AUTOSAR-compliant getter for referencedTDEventSwc.

        Returns:
            The referencedTDEventSwc value

        Note:
            Delegates to referenced_td_event_swc property (CODING_RULE_V2_00017)
        """
        return self.referenced_td_event_swc  # Delegates to property

    def setReferencedTDEventSwc(self, value: "TDEventSwc") -> "TDEventSwcInternalBehaviorReference":
        """
        AUTOSAR-compliant setter for referencedTDEventSwc with method chaining.

        Args:
            value: The referencedTDEventSwc to set

        Returns:
            self for method chaining

        Note:
            Delegates to referenced_td_event_swc property setter (gets validation automatically)
        """
        self.referenced_td_event_swc = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_referenced_td_event_swc(self, value: Optional["TDEventSwc"]) -> "TDEventSwcInternalBehaviorReference":
        """
        Set referencedTDEventSwc and return self for chaining.

        Args:
            value: The referencedTDEventSwc to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_referenced_td_event_swc("value")
        """
        self.referenced_td_event_swc = value  # Use property setter (gets validation)
        return self

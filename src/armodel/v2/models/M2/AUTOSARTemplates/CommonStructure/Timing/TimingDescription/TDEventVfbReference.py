from typing import Optional


class TDEventVfbReference(TDEventVfb):
    """
    This is used to reference timing description events related to the Virtual
    Functional Bus (VFB) view which are specified in other timing views.

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingDescription::TimingDescription::TDEventVfbReference

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 52, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The referenced timing description event.
        self._referencedTDEventVfb: Optional["TDEventVfb"] = None

    @property
    def referenced_td_event_vfb(self) -> Optional["TDEventVfb"]:
        """Get referencedTDEventVfb (Pythonic accessor)."""
        return self._referencedTDEventVfb

    @referenced_td_event_vfb.setter
    def referenced_td_event_vfb(self, value: Optional["TDEventVfb"]) -> None:
        """
        Set referencedTDEventVfb with validation.

        Args:
            value: The referencedTDEventVfb to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._referencedTDEventVfb = None
            return

        if not isinstance(value, TDEventVfb):
            raise TypeError(
                f"referencedTDEventVfb must be TDEventVfb or None, got {type(value).__name__}"
            )
        self._referencedTDEventVfb = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getReferencedTDEventVfb(self) -> "TDEventVfb":
        """
        AUTOSAR-compliant getter for referencedTDEventVfb.

        Returns:
            The referencedTDEventVfb value

        Note:
            Delegates to referenced_td_event_vfb property (CODING_RULE_V2_00017)
        """
        return self.referenced_td_event_vfb  # Delegates to property

    def setReferencedTDEventVfb(self, value: "TDEventVfb") -> "TDEventVfbReference":
        """
        AUTOSAR-compliant setter for referencedTDEventVfb with method chaining.

        Args:
            value: The referencedTDEventVfb to set

        Returns:
            self for method chaining

        Note:
            Delegates to referenced_td_event_vfb property setter (gets validation automatically)
        """
        self.referenced_td_event_vfb = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_referenced_td_event_vfb(self, value: Optional["TDEventVfb"]) -> "TDEventVfbReference":
        """
        Set referencedTDEventVfb and return self for chaining.

        Args:
            value: The referencedTDEventVfb to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_referenced_td_event_vfb("value")
        """
        self.referenced_td_event_vfb = value  # Use property setter (gets validation)
        return self

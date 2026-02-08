from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription import (
    TimingDescriptionEvent,
)


class TDEventBswInternalBehavior(TimingDescriptionEvent):
    """
    This is used to describe timing events related to the BswInternalBehavior of
    a BSW module.

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingDescription::TimingDescription

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 73, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The scope of this timing event.
        self._bswModuleEntity: Optional["BswModuleEntity"] = None

    @property
    def bsw_module_entity(self) -> Optional["BswModuleEntity"]:
        """Get bswModuleEntity (Pythonic accessor)."""
        return self._bswModuleEntity

    @bsw_module_entity.setter
    def bsw_module_entity(self, value: Optional["BswModuleEntity"]) -> None:
        """
        Set bswModuleEntity with validation.

        Args:
            value: The bswModuleEntity to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._bswModuleEntity = None
            return

        if not isinstance(value, BswModuleEntity):
            raise TypeError(
                f"bswModuleEntity must be BswModuleEntity or None, got {type(value).__name__}"
            )
        self._bswModuleEntity = value
        # The specific type of this timing event.
        self._tdEventBswBehaviorType: Optional["TDEventBswInternal"] = None

    @property
    def td_event_bsw_behavior_type(self) -> Optional["TDEventBswInternal"]:
        """Get tdEventBswBehaviorType (Pythonic accessor)."""
        return self._tdEventBswBehaviorType

    @td_event_bsw_behavior_type.setter
    def td_event_bsw_behavior_type(self, value: Optional["TDEventBswInternal"]) -> None:
        """
        Set tdEventBswBehaviorType with validation.

        Args:
            value: The tdEventBswBehaviorType to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tdEventBswBehaviorType = None
            return

        if not isinstance(value, TDEventBswInternal):
            raise TypeError(
                f"tdEventBswBehaviorType must be TDEventBswInternal or None, got {type(value).__name__}"
            )
        self._tdEventBswBehaviorType = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBswModuleEntity(self) -> "BswModuleEntity":
        """
        AUTOSAR-compliant getter for bswModuleEntity.

        Returns:
            The bswModuleEntity value

        Note:
            Delegates to bsw_module_entity property (CODING_RULE_V2_00017)
        """
        return self.bsw_module_entity  # Delegates to property

    def setBswModuleEntity(self, value: "BswModuleEntity") -> "TDEventBswInternalBehavior":
        """
        AUTOSAR-compliant setter for bswModuleEntity with method chaining.

        Args:
            value: The bswModuleEntity to set

        Returns:
            self for method chaining

        Note:
            Delegates to bsw_module_entity property setter (gets validation automatically)
        """
        self.bsw_module_entity = value  # Delegates to property setter
        return self

    def getTdEventBswBehaviorType(self) -> "TDEventBswInternal":
        """
        AUTOSAR-compliant getter for tdEventBswBehaviorType.

        Returns:
            The tdEventBswBehaviorType value

        Note:
            Delegates to td_event_bsw_behavior_type property (CODING_RULE_V2_00017)
        """
        return self.td_event_bsw_behavior_type  # Delegates to property

    def setTdEventBswBehaviorType(self, value: "TDEventBswInternal") -> "TDEventBswInternalBehavior":
        """
        AUTOSAR-compliant setter for tdEventBswBehaviorType with method chaining.

        Args:
            value: The tdEventBswBehaviorType to set

        Returns:
            self for method chaining

        Note:
            Delegates to td_event_bsw_behavior_type property setter (gets validation automatically)
        """
        self.td_event_bsw_behavior_type = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_bsw_module_entity(self, value: Optional["BswModuleEntity"]) -> "TDEventBswInternalBehavior":
        """
        Set bswModuleEntity and return self for chaining.

        Args:
            value: The bswModuleEntity to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_bsw_module_entity("value")
        """
        self.bsw_module_entity = value  # Use property setter (gets validation)
        return self

    def with_td_event_bsw_behavior_type(self, value: Optional["TDEventBswInternal"]) -> "TDEventBswInternalBehavior":
        """
        Set tdEventBswBehaviorType and return self for chaining.

        Args:
            value: The tdEventBswBehaviorType to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_td_event_bsw_behavior_type("value")
        """
        self.td_event_bsw_behavior_type = value  # Use property setter (gets validation)
        return self

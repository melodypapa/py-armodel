from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class RteEventInCompositionToOsTaskProxyMapping(Identifiable):
    """
    This meta-class is used to map an RteEvent to an OsTaskProxy in the context
    of a SwComposition. Several RteEventInCompositionToOsTaskProxyMappings can
    be used to define a pairing constraint that describes which RteEvents shall
    be mapped together into an OsTask. Optionally the relative position of the
    RteEvents in the OsTask can be defined in the mapping.

    Package: M2::AUTOSARTemplates::SystemTemplate::RteEventToOsTaskMapping

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 211, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute is used to describe the position of the Rte the OsTask as a
                # relative value, i.
        # e.
        # the values the relative position of the RteEvent in the Os.
        self._offset: Optional["PositiveInteger"] = None

    @property
    def offset(self) -> Optional["PositiveInteger"]:
        """Get offset (Pythonic accessor)."""
        return self._offset

    @offset.setter
    def offset(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set offset with validation.

        Args:
            value: The offset to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._offset = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"offset must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._offset = value
        # Reference to OsTaskProxy to which the RteEvent is.
        self._osTaskProxy: Optional["OsTaskProxy"] = None

    @property
    def os_task_proxy(self) -> Optional["OsTaskProxy"]:
        """Get osTaskProxy (Pythonic accessor)."""
        return self._osTaskProxy

    @os_task_proxy.setter
    def os_task_proxy(self, value: Optional["OsTaskProxy"]) -> None:
        """
        Set osTaskProxy with validation.

        Args:
            value: The osTaskProxy to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._osTaskProxy = None
            return

        if not isinstance(value, OsTaskProxy):
            raise TypeError(
                f"osTaskProxy must be OsTaskProxy or None, got {type(value).__name__}"
            )
        self._osTaskProxy = value
        # by: RteEventInComposition.
        self._rteEventInstanceRef: Optional["RTEEvent"] = None

    @property
    def rte_event_instance_ref(self) -> Optional["RTEEvent"]:
        """Get rteEventInstanceRef (Pythonic accessor)."""
        return self._rteEventInstanceRef

    @rte_event_instance_ref.setter
    def rte_event_instance_ref(self, value: Optional["RTEEvent"]) -> None:
        """
        Set rteEventInstanceRef with validation.

        Args:
            value: The rteEventInstanceRef to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rteEventInstanceRef = None
            return

        if not isinstance(value, RTEEvent):
            raise TypeError(
                f"rteEventInstanceRef must be RTEEvent or None, got {type(value).__name__}"
            )
        self._rteEventInstanceRef = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getOffset(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for offset.

        Returns:
            The offset value

        Note:
            Delegates to offset property (CODING_RULE_V2_00017)
        """
        return self.offset  # Delegates to property

    def setOffset(self, value: "PositiveInteger") -> "RteEventInCompositionToOsTaskProxyMapping":
        """
        AUTOSAR-compliant setter for offset with method chaining.

        Args:
            value: The offset to set

        Returns:
            self for method chaining

        Note:
            Delegates to offset property setter (gets validation automatically)
        """
        self.offset = value  # Delegates to property setter
        return self

    def getOsTaskProxy(self) -> "OsTaskProxy":
        """
        AUTOSAR-compliant getter for osTaskProxy.

        Returns:
            The osTaskProxy value

        Note:
            Delegates to os_task_proxy property (CODING_RULE_V2_00017)
        """
        return self.os_task_proxy  # Delegates to property

    def setOsTaskProxy(self, value: "OsTaskProxy") -> "RteEventInCompositionToOsTaskProxyMapping":
        """
        AUTOSAR-compliant setter for osTaskProxy with method chaining.

        Args:
            value: The osTaskProxy to set

        Returns:
            self for method chaining

        Note:
            Delegates to os_task_proxy property setter (gets validation automatically)
        """
        self.os_task_proxy = value  # Delegates to property setter
        return self

    def getRteEventInstanceRef(self) -> "RTEEvent":
        """
        AUTOSAR-compliant getter for rteEventInstanceRef.

        Returns:
            The rteEventInstanceRef value

        Note:
            Delegates to rte_event_instance_ref property (CODING_RULE_V2_00017)
        """
        return self.rte_event_instance_ref  # Delegates to property

    def setRteEventInstanceRef(self, value: "RTEEvent") -> "RteEventInCompositionToOsTaskProxyMapping":
        """
        AUTOSAR-compliant setter for rteEventInstanceRef with method chaining.

        Args:
            value: The rteEventInstanceRef to set

        Returns:
            self for method chaining

        Note:
            Delegates to rte_event_instance_ref property setter (gets validation automatically)
        """
        self.rte_event_instance_ref = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_offset(self, value: Optional["PositiveInteger"]) -> "RteEventInCompositionToOsTaskProxyMapping":
        """
        Set offset and return self for chaining.

        Args:
            value: The offset to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_offset("value")
        """
        self.offset = value  # Use property setter (gets validation)
        return self

    def with_os_task_proxy(self, value: Optional["OsTaskProxy"]) -> "RteEventInCompositionToOsTaskProxyMapping":
        """
        Set osTaskProxy and return self for chaining.

        Args:
            value: The osTaskProxy to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_os_task_proxy("value")
        """
        self.os_task_proxy = value  # Use property setter (gets validation)
        return self

    def with_rte_event_instance_ref(self, value: Optional["RTEEvent"]) -> "RteEventInCompositionToOsTaskProxyMapping":
        """
        Set rteEventInstanceRef and return self for chaining.

        Args:
            value: The rteEventInstanceRef to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_rte_event_instance_ref("value")
        """
        self.rte_event_instance_ref = value  # Use property setter (gets validation)
        return self

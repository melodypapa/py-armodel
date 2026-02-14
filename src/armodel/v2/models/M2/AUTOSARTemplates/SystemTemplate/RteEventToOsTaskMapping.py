"""
AUTOSAR Package - RteEventToOsTaskMapping

Package: M2::AUTOSARTemplates::SystemTemplate::RteEventToOsTaskMapping
"""


from __future__ import annotations

from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
    Integer,
    PositiveInteger,
    RTEEvent,
)


class OsTaskProxy(ARElement):
    """
    This meta-class represents a proxy for an OsTask in the System Description.

    Package: M2::AUTOSARTemplates::SystemTemplate::RteEventToOsTaskMapping::OsTaskProxy

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 208, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute specifies the period in seconds of this task of a cyclically
                # activated task.
        # Please note that this informative and not directly relevant for the But the
                # attribute value can be mapped OS configuration to support configuration work
                # a fixed set of OsTasks.
        self._period: Optional["TimeValue"] = None

    @property
    def period(self) -> Optional["TimeValue"]:
        """Get period (Pythonic accessor)."""
        return self._period

    @period.setter
    def period(self, value: Optional["TimeValue"]) -> None:
        """
        Set period with validation.

        Args:
            value: The period to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._period = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"period must be TimeValue or None, got {type(value).__name__}"
            )
        self._period = value
        self._preemptability: Optional["OsTaskPreemptability"] = None

    @property
    def preemptability(self) -> Optional["OsTaskPreemptability"]:
        """Get preemptability (Pythonic accessor)."""
        return self._preemptability

    @preemptability.setter
    def preemptability(self, value: Optional["OsTaskPreemptability"]) -> None:
        """
        Set preemptability with validation.

        Args:
            value: The preemptability to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._preemptability = None
            return

        if not isinstance(value, OsTaskPreemptability):
            raise TypeError(
                f"preemptability must be OsTaskPreemptability or None, got {type(value).__name__}"
            )
        self._preemptability = value
        # only the relative ordering of.
        self._priority: Optional[PositiveInteger] = None

    @property
    def priority(self) -> Optional[PositiveInteger]:
        """Get priority (Pythonic accessor)."""
        return self._priority

    @priority.setter
    def priority(self, value: Optional[PositiveInteger]) -> None:
        """
        Set priority with validation.

        Args:
            value: The priority to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._priority = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"priority must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._priority = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getPeriod(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for period.

        Returns:
            The period value

        Note:
            Delegates to period property (CODING_RULE_V2_00017)
        """
        return self.period  # Delegates to property

    def setPeriod(self, value: "TimeValue") -> OsTaskProxy:
        """
        AUTOSAR-compliant setter for period with method chaining.

        Args:
            value: The period to set

        Returns:
            self for method chaining

        Note:
            Delegates to period property setter (gets validation automatically)
        """
        self.period = value  # Delegates to property setter
        return self

    def getPreemptability(self) -> "OsTaskPreemptability":
        """
        AUTOSAR-compliant getter for preemptability.

        Returns:
            The preemptability value

        Note:
            Delegates to preemptability property (CODING_RULE_V2_00017)
        """
        return self.preemptability  # Delegates to property

    def setPreemptability(self, value: "OsTaskPreemptability") -> OsTaskProxy:
        """
        AUTOSAR-compliant setter for preemptability with method chaining.

        Args:
            value: The preemptability to set

        Returns:
            self for method chaining

        Note:
            Delegates to preemptability property setter (gets validation automatically)
        """
        self.preemptability = value  # Delegates to property setter
        return self

    def getPriority(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for priority.

        Returns:
            The priority value

        Note:
            Delegates to priority property (CODING_RULE_V2_00017)
        """
        return self.priority  # Delegates to property

    def setPriority(self, value: PositiveInteger) -> OsTaskProxy:
        """
        AUTOSAR-compliant setter for priority with method chaining.

        Args:
            value: The priority to set

        Returns:
            self for method chaining

        Note:
            Delegates to priority property setter (gets validation automatically)
        """
        self.priority = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_period(self, value: Optional["TimeValue"]) -> OsTaskProxy:
        """
        Set period and return self for chaining.

        Args:
            value: The period to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_period("value")
        """
        self.period = value  # Use property setter (gets validation)
        return self

    def with_preemptability(self, value: Optional["OsTaskPreemptability"]) -> OsTaskProxy:
        """
        Set preemptability and return self for chaining.

        Args:
            value: The preemptability to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_preemptability("value")
        """
        self.preemptability = value  # Use property setter (gets validation)
        return self

    def with_priority(self, value: Optional[PositiveInteger]) -> OsTaskProxy:
        """
        Set priority and return self for chaining.

        Args:
            value: The priority to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_priority("value")
        """
        self.priority = value  # Use property setter (gets validation)
        return self



class AppOsTaskProxyToEcuTaskProxyMapping(Identifiable):
    """
    This meta-class is used to map an OsTaskProxy that was created in the
    context of a SwComponent to an OsTaskProxy that was created in the context
    of an Ecu.

    Package: M2::AUTOSARTemplates::SystemTemplate::RteEventToOsTaskMapping::AppOsTaskProxyToEcuTaskProxyMapping

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 209, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to an OsTaskProxy that is created in the a SwComponent.
        self._appTaskProxy: Optional[OsTaskProxy] = None

    @property
    def app_task_proxy(self) -> Optional[OsTaskProxy]:
        """Get appTaskProxy (Pythonic accessor)."""
        return self._appTaskProxy

    @app_task_proxy.setter
    def app_task_proxy(self, value: Optional[OsTaskProxy]) -> None:
        """
        Set appTaskProxy with validation.

        Args:
            value: The appTaskProxy to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._appTaskProxy = None
            return

        if not isinstance(value, OsTaskProxy):
            raise TypeError(
                f"appTaskProxy must be OsTaskProxy or None, got {type(value).__name__}"
            )
        self._appTaskProxy = value
        self._ecuTaskProxy: Optional[OsTaskProxy] = None

    @property
    def ecu_task_proxy(self) -> Optional[OsTaskProxy]:
        """Get ecuTaskProxy (Pythonic accessor)."""
        return self._ecuTaskProxy

    @ecu_task_proxy.setter
    def ecu_task_proxy(self, value: Optional[OsTaskProxy]) -> None:
        """
        Set ecuTaskProxy with validation.

        Args:
            value: The ecuTaskProxy to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ecuTaskProxy = None
            return

        if not isinstance(value, OsTaskProxy):
            raise TypeError(
                f"ecuTaskProxy must be OsTaskProxy or None, got {type(value).__name__}"
            )
        self._ecuTaskProxy = value
                # a relative value, i.
        # e.
        # the only the relative position of the appTask the ecuTaskProxy.
        self._offset: Optional[Integer] = None

    @property
    def offset(self) -> Optional[Integer]:
        """Get offset (Pythonic accessor)."""
        return self._offset

    @offset.setter
    def offset(self, value: Optional[Integer]) -> None:
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

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"offset must be Integer or int or None, got {type(value).__name__}"
            )
        self._offset = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAppTaskProxy(self) -> OsTaskProxy:
        """
        AUTOSAR-compliant getter for appTaskProxy.

        Returns:
            The appTaskProxy value

        Note:
            Delegates to app_task_proxy property (CODING_RULE_V2_00017)
        """
        return self.app_task_proxy  # Delegates to property

    def setAppTaskProxy(self, value: OsTaskProxy) -> AppOsTaskProxyToEcuTaskProxyMapping:
        """
        AUTOSAR-compliant setter for appTaskProxy with method chaining.

        Args:
            value: The appTaskProxy to set

        Returns:
            self for method chaining

        Note:
            Delegates to app_task_proxy property setter (gets validation automatically)
        """
        self.app_task_proxy = value  # Delegates to property setter
        return self

    def getEcuTaskProxy(self) -> OsTaskProxy:
        """
        AUTOSAR-compliant getter for ecuTaskProxy.

        Returns:
            The ecuTaskProxy value

        Note:
            Delegates to ecu_task_proxy property (CODING_RULE_V2_00017)
        """
        return self.ecu_task_proxy  # Delegates to property

    def setEcuTaskProxy(self, value: OsTaskProxy) -> AppOsTaskProxyToEcuTaskProxyMapping:
        """
        AUTOSAR-compliant setter for ecuTaskProxy with method chaining.

        Args:
            value: The ecuTaskProxy to set

        Returns:
            self for method chaining

        Note:
            Delegates to ecu_task_proxy property setter (gets validation automatically)
        """
        self.ecu_task_proxy = value  # Delegates to property setter
        return self

    def getOffset(self) -> Integer:
        """
        AUTOSAR-compliant getter for offset.

        Returns:
            The offset value

        Note:
            Delegates to offset property (CODING_RULE_V2_00017)
        """
        return self.offset  # Delegates to property

    def setOffset(self, value: Integer) -> AppOsTaskProxyToEcuTaskProxyMapping:
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

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_app_task_proxy(self, value: Optional[OsTaskProxy]) -> AppOsTaskProxyToEcuTaskProxyMapping:
        """
        Set appTaskProxy and return self for chaining.

        Args:
            value: The appTaskProxy to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_app_task_proxy("value")
        """
        self.app_task_proxy = value  # Use property setter (gets validation)
        return self

    def with_ecu_task_proxy(self, value: Optional[OsTaskProxy]) -> AppOsTaskProxyToEcuTaskProxyMapping:
        """
        Set ecuTaskProxy and return self for chaining.

        Args:
            value: The ecuTaskProxy to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ecu_task_proxy("value")
        """
        self.ecu_task_proxy = value  # Use property setter (gets validation)
        return self

    def with_offset(self, value: Optional[Integer]) -> AppOsTaskProxyToEcuTaskProxyMapping:
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



class RteEventInCompositionToOsTaskProxyMapping(Identifiable):
    """
    This meta-class is used to map an RteEvent to an OsTaskProxy in the context
    of a SwComposition. Several RteEventInCompositionToOsTaskProxyMappings can
    be used to define a pairing constraint that describes which RteEvents shall
    be mapped together into an OsTask. Optionally the relative position of the
    RteEvents in the OsTask can be defined in the mapping.

    Package: M2::AUTOSARTemplates::SystemTemplate::RteEventToOsTaskMapping::RteEventInCompositionToOsTaskProxyMapping

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
        self._offset: Optional[PositiveInteger] = None

    @property
    def offset(self) -> Optional[PositiveInteger]:
        """Get offset (Pythonic accessor)."""
        return self._offset

    @offset.setter
    def offset(self, value: Optional[PositiveInteger]) -> None:
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

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"offset must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._offset = value
        self._osTaskProxy: Optional[OsTaskProxy] = None

    @property
    def os_task_proxy(self) -> Optional[OsTaskProxy]:
        """Get osTaskProxy (Pythonic accessor)."""
        return self._osTaskProxy

    @os_task_proxy.setter
    def os_task_proxy(self, value: Optional[OsTaskProxy]) -> None:
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

    def getOffset(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for offset.

        Returns:
            The offset value

        Note:
            Delegates to offset property (CODING_RULE_V2_00017)
        """
        return self.offset  # Delegates to property

    def setOffset(self, value: PositiveInteger) -> RteEventInCompositionToOsTaskProxyMapping:
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

    def getOsTaskProxy(self) -> OsTaskProxy:
        """
        AUTOSAR-compliant getter for osTaskProxy.

        Returns:
            The osTaskProxy value

        Note:
            Delegates to os_task_proxy property (CODING_RULE_V2_00017)
        """
        return self.os_task_proxy  # Delegates to property

    def setOsTaskProxy(self, value: OsTaskProxy) -> RteEventInCompositionToOsTaskProxyMapping:
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

    def getRteEventInstanceRef(self) -> RTEEvent:
        """
        AUTOSAR-compliant getter for rteEventInstanceRef.

        Returns:
            The rteEventInstanceRef value

        Note:
            Delegates to rte_event_instance_ref property (CODING_RULE_V2_00017)
        """
        return self.rte_event_instance_ref  # Delegates to property

    def setRteEventInstanceRef(self, value: RTEEvent) -> RteEventInCompositionToOsTaskProxyMapping:
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

    def with_offset(self, value: Optional[PositiveInteger]) -> RteEventInCompositionToOsTaskProxyMapping:
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

    def with_os_task_proxy(self, value: Optional[OsTaskProxy]) -> RteEventInCompositionToOsTaskProxyMapping:
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

    def with_rte_event_instance_ref(self, value: Optional["RTEEvent"]) -> RteEventInCompositionToOsTaskProxyMapping:
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



class RteEventInCompositionSeparation(Identifiable):
    """
    This meta-class is used to define a separation constraint in the context of
    a SwComposition. The referenced RteEvents are not allowed to be mapped into
    the same OsTask.

    Package: M2::AUTOSARTemplates::SystemTemplate::RteEventToOsTaskMapping::RteEventInCompositionSeparation

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 212, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # the same OsTask.
        # by: RteEventInComposition.
        self._rteEventInstanceRef: List["RTEEvent"] = []

    @property
    def rte_event_instance_ref(self) -> List["RTEEvent"]:
        """Get rteEventInstanceRef (Pythonic accessor)."""
        return self._rteEventInstanceRef

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getRteEventInstanceRef(self) -> List["RTEEvent"]:
        """
        AUTOSAR-compliant getter for rteEventInstanceRef.

        Returns:
            The rteEventInstanceRef value

        Note:
            Delegates to rte_event_instance_ref property (CODING_RULE_V2_00017)
        """
        return self.rte_event_instance_ref  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class RteEventInSystemToOsTaskProxyMapping(Identifiable):
    """
    This meta-class is used to map an RteEvent to an OsTaskProxy in the context
    of the System. Several Rte EventToOsTaskProxyMappings can be used to define
    a pairing constraint that describes which Rte Events shall be mapped
    together into an OsTask. Optionally the position of the RteEvents in the
    OsTask can be defined.

    Package: M2::AUTOSARTemplates::SystemTemplate::RteEventToOsTaskMapping::RteEventInSystemToOsTaskProxyMapping

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 213, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute is used to describe the position of the Rte the OsTask as a
                # relative value, i.
        # e.
        # the values the relative position of the RteEvent in the Os.
        self._offset: Optional[Integer] = None

    @property
    def offset(self) -> Optional[Integer]:
        """Get offset (Pythonic accessor)."""
        return self._offset

    @offset.setter
    def offset(self, value: Optional[Integer]) -> None:
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

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"offset must be Integer or int or None, got {type(value).__name__}"
            )
        self._offset = value
        # AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._osTaskProxy: Optional[OsTaskProxy] = None

    @property
    def os_task_proxy(self) -> Optional[OsTaskProxy]:
        """Get osTaskProxy (Pythonic accessor)."""
        return self._osTaskProxy

    @os_task_proxy.setter
    def os_task_proxy(self, value: Optional[OsTaskProxy]) -> None:
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

    def getOffset(self) -> Integer:
        """
        AUTOSAR-compliant getter for offset.

        Returns:
            The offset value

        Note:
            Delegates to offset property (CODING_RULE_V2_00017)
        """
        return self.offset  # Delegates to property

    def setOffset(self, value: Integer) -> RteEventInSystemToOsTaskProxyMapping:
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

    def getOsTaskProxy(self) -> OsTaskProxy:
        """
        AUTOSAR-compliant getter for osTaskProxy.

        Returns:
            The osTaskProxy value

        Note:
            Delegates to os_task_proxy property (CODING_RULE_V2_00017)
        """
        return self.os_task_proxy  # Delegates to property

    def setOsTaskProxy(self, value: OsTaskProxy) -> RteEventInSystemToOsTaskProxyMapping:
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

    def getRteEventInstanceRef(self) -> RTEEvent:
        """
        AUTOSAR-compliant getter for rteEventInstanceRef.

        Returns:
            The rteEventInstanceRef value

        Note:
            Delegates to rte_event_instance_ref property (CODING_RULE_V2_00017)
        """
        return self.rte_event_instance_ref  # Delegates to property

    def setRteEventInstanceRef(self, value: RTEEvent) -> RteEventInSystemToOsTaskProxyMapping:
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

    def with_offset(self, value: Optional[Integer]) -> RteEventInSystemToOsTaskProxyMapping:
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

    def with_os_task_proxy(self, value: Optional[OsTaskProxy]) -> RteEventInSystemToOsTaskProxyMapping:
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

    def with_rte_event_instance_ref(self, value: Optional["RTEEvent"]) -> RteEventInSystemToOsTaskProxyMapping:
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



class RteEventInSystemSeparation(Identifiable):
    """
    This meta-class is used to define a separation constraint in the context of
    the System. The referenced RteEvents are not allowed to be mapped into the
    same OsTask.

    Package: M2::AUTOSARTemplates::SystemTemplate::RteEventToOsTaskMapping::RteEventInSystemSeparation

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 214, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # the same OsTask.
        # by: RteEventInSystem.
        self._rteEventInstanceRef: List["RTEEvent"] = []

    @property
    def rte_event_instance_ref(self) -> List["RTEEvent"]:
        """Get rteEventInstanceRef (Pythonic accessor)."""
        return self._rteEventInstanceRef

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getRteEventInstanceRef(self) -> List["RTEEvent"]:
        """
        AUTOSAR-compliant getter for rteEventInstanceRef.

        Returns:
            The rteEventInstanceRef value

        Note:
            Delegates to rte_event_instance_ref property (CODING_RULE_V2_00017)
        """
        return self.rte_event_instance_ref  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====


class OsTaskPreemptabilityEnum(AREnum):
    """
    OsTaskPreemptabilityEnum enumeration

Enumeration that defines the possible preemptability values for OsTask. Aggregated by OsTaskProxy.preemptability

Package: M2::AUTOSARTemplates::SystemTemplate::RteEventToOsTaskMapping
    """
    # Task is preemptable.
    full = "1"

    # Task is not preemptable.
    none = "0"

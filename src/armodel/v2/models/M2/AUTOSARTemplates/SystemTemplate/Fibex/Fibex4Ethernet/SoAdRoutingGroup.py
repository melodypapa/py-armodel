from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore import FibexElement

    RefType,
)


class SoAdRoutingGroup(FibexElement):
    """
    Routing of Pdus in the SoAd can be activated or deactivated. The ShortName
    of this element shall contain the RoutingGroupId.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::ObsoleteModel

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2057, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute defines the type of a RoutingGroup.
        # There are RoutingGroups that activate the data path for unicast events of an
                # event group.
        # And there are activate the data path for initial are triggered, namely events
                # that are sent out server side after a client got subscribed.
        # that this attribute is only valid for event Receiver communication) and
                # omitted in MethodActivationRoutingGroups.
        self._eventGroup: RefType = None

    @property
    def event_group(self) -> RefType:
        """Get eventGroup (Pythonic accessor)."""
        return self._eventGroup

    @event_group.setter
    def event_group(self, value: RefType) -> None:
        """
        Set eventGroup with validation.

        Args:
            value: The eventGroup to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._eventGroup = None
            return

        self._eventGroup = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEventGroup(self) -> RefType:
        """
        AUTOSAR-compliant getter for eventGroup.

        Returns:
            The eventGroup value

        Note:
            Delegates to event_group property (CODING_RULE_V2_00017)
        """
        return self.event_group  # Delegates to property

    def setEventGroup(self, value: RefType) -> "SoAdRoutingGroup":
        """
        AUTOSAR-compliant setter for eventGroup with method chaining.

        Args:
            value: The eventGroup to set

        Returns:
            self for method chaining

        Note:
            Delegates to event_group property setter (gets validation automatically)
        """
        self.event_group = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_event_group(self, value: Optional[RefType]) -> "SoAdRoutingGroup":
        """
        Set eventGroup and return self for chaining.

        Args:
            value: The eventGroup to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_event_group("value")
        """
        self.event_group = value  # Use property setter (gets validation)
        return self

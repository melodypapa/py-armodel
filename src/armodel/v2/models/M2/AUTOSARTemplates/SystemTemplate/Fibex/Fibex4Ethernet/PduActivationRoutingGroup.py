from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class PduActivationRoutingGroup(Identifiable):
    """
    Group of Pdus that can be activated or deactivated for transmission over a
    socket connection.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::ServiceInstances::PduActivationRoutingGroup

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 488, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute defines the type of a RoutingGroup.
        # There are RoutingGroups that activate the data path for unicast events of an
                # event group.
        # And there are activate the data path for initial are triggered, namely events
                # that are sent out server side after a client got subscribed.
        # Please this attribute is only valid for event Receiver communication) and
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
        # PduIdentifiers assigned for transmission over Udp in case the referencing
        # PduActivationRoutingGroup is.
        self._iPduIdentifier: List["SoConIPduIdentifier"] = []

    @property
    def i_pdu_identifier(self) -> List["SoConIPduIdentifier"]:
        """Get iPduIdentifier (Pythonic accessor)."""
        return self._iPduIdentifier

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

    def setEventGroup(self, value: RefType) -> "PduActivationRoutingGroup":
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

    def getIPduIdentifier(self) -> List["SoConIPduIdentifier"]:
        """
        AUTOSAR-compliant getter for iPduIdentifier.

        Returns:
            The iPduIdentifier value

        Note:
            Delegates to i_pdu_identifier property (CODING_RULE_V2_00017)
        """
        return self.i_pdu_identifier  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_event_group(self, value: Optional[RefType]) -> "PduActivationRoutingGroup":
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

from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class DdsCpServiceInstanceEvent(ARObject):
    """
    This element represents an event as part of the Provided Service Instance.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::Dds

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 475, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to the PduTriggerung used for the upper layer this DdsEvent
        # message.
        self._ddsEvent: RefType = None

    @property
    def dds_event(self) -> RefType:
        """Get ddsEvent (Pythonic accessor)."""
        return self._ddsEvent

    @dds_event.setter
    def dds_event(self, value: RefType) -> None:
        """
        Set ddsEvent with validation.

        Args:
            value: The ddsEvent to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ddsEvent = None
            return

        self._ddsEvent = value
        # Reference to the QOS Profile used for this Event.
        # atp.
        # Status=candidate.
        self._ddsEventQos: Optional["DdsCpQosProfile"] = None

    @property
    def dds_event_qos(self) -> Optional["DdsCpQosProfile"]:
        """Get ddsEventQos (Pythonic accessor)."""
        return self._ddsEventQos

    @dds_event_qos.setter
    def dds_event_qos(self, value: Optional["DdsCpQosProfile"]) -> None:
        """
        Set ddsEventQos with validation.

        Args:
            value: The ddsEventQos to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ddsEventQos = None
            return

        if not isinstance(value, DdsCpQosProfile):
            raise TypeError(
                f"ddsEventQos must be DdsCpQosProfile or None, got {type(value).__name__}"
            )
        self._ddsEventQos = value
        # Reference to the DDS Topic used for this Event.
        self._ddsEventTopic: Optional["DdsCpTopic"] = None

    @property
    def dds_event_topic(self) -> Optional["DdsCpTopic"]:
        """Get ddsEventTopic (Pythonic accessor)."""
        return self._ddsEventTopic

    @dds_event_topic.setter
    def dds_event_topic(self, value: Optional["DdsCpTopic"]) -> None:
        """
        Set ddsEventTopic with validation.

        Args:
            value: The ddsEventTopic to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ddsEventTopic = None
            return

        if not isinstance(value, DdsCpTopic):
            raise TypeError(
                f"ddsEventTopic must be DdsCpTopic or None, got {type(value).__name__}"
            )
        self._ddsEventTopic = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDdsEvent(self) -> RefType:
        """
        AUTOSAR-compliant getter for ddsEvent.

        Returns:
            The ddsEvent value

        Note:
            Delegates to dds_event property (CODING_RULE_V2_00017)
        """
        return self.dds_event  # Delegates to property

    def setDdsEvent(self, value: RefType) -> "DdsCpServiceInstanceEvent":
        """
        AUTOSAR-compliant setter for ddsEvent with method chaining.

        Args:
            value: The ddsEvent to set

        Returns:
            self for method chaining

        Note:
            Delegates to dds_event property setter (gets validation automatically)
        """
        self.dds_event = value  # Delegates to property setter
        return self

    def getDdsEventQos(self) -> "DdsCpQosProfile":
        """
        AUTOSAR-compliant getter for ddsEventQos.

        Returns:
            The ddsEventQos value

        Note:
            Delegates to dds_event_qos property (CODING_RULE_V2_00017)
        """
        return self.dds_event_qos  # Delegates to property

    def setDdsEventQos(self, value: "DdsCpQosProfile") -> "DdsCpServiceInstanceEvent":
        """
        AUTOSAR-compliant setter for ddsEventQos with method chaining.

        Args:
            value: The ddsEventQos to set

        Returns:
            self for method chaining

        Note:
            Delegates to dds_event_qos property setter (gets validation automatically)
        """
        self.dds_event_qos = value  # Delegates to property setter
        return self

    def getDdsEventTopic(self) -> "DdsCpTopic":
        """
        AUTOSAR-compliant getter for ddsEventTopic.

        Returns:
            The ddsEventTopic value

        Note:
            Delegates to dds_event_topic property (CODING_RULE_V2_00017)
        """
        return self.dds_event_topic  # Delegates to property

    def setDdsEventTopic(self, value: "DdsCpTopic") -> "DdsCpServiceInstanceEvent":
        """
        AUTOSAR-compliant setter for ddsEventTopic with method chaining.

        Args:
            value: The ddsEventTopic to set

        Returns:
            self for method chaining

        Note:
            Delegates to dds_event_topic property setter (gets validation automatically)
        """
        self.dds_event_topic = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_dds_event(self, value: Optional[RefType]) -> "DdsCpServiceInstanceEvent":
        """
        Set ddsEvent and return self for chaining.

        Args:
            value: The ddsEvent to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_dds_event("value")
        """
        self.dds_event = value  # Use property setter (gets validation)
        return self

    def with_dds_event_qos(self, value: Optional["DdsCpQosProfile"]) -> "DdsCpServiceInstanceEvent":
        """
        Set ddsEventQos and return self for chaining.

        Args:
            value: The ddsEventQos to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_dds_event_qos("value")
        """
        self.dds_event_qos = value  # Use property setter (gets validation)
        return self

    def with_dds_event_topic(self, value: Optional["DdsCpTopic"]) -> "DdsCpServiceInstanceEvent":
        """
        Set ddsEventTopic and return self for chaining.

        Args:
            value: The ddsEventTopic to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_dds_event_topic("value")
        """
        self.dds_event_topic = value  # Use property setter (gets validation)
        return self

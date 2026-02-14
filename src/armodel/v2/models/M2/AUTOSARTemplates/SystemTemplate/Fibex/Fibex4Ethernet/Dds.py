"""
AUTOSAR Package - Dds

Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::Dds
"""


from __future__ import annotations

from abc import ABC
from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
    Float,
    PositiveInteger,
    RefType,
    String,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import (
    AbstractServiceInstance,
    ISignal,
)


class DdsCpISignalToDdsTopicMapping(ARObject):
    """
    Mapping of an ISignal to a DdsTopic.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::Dds::DdsCpISignalToDdsTopicMapping

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 293, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to the DdsTopic.
        self._ddsTopic: Optional[DdsCpTopic] = None

    @property
    def dds_topic(self) -> Optional[DdsCpTopic]:
        """Get ddsTopic (Pythonic accessor)."""
        return self._ddsTopic

    @dds_topic.setter
    def dds_topic(self, value: Optional[DdsCpTopic]) -> None:
        """
        Set ddsTopic with validation.

        Args:
            value: The ddsTopic to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ddsTopic = None
            return

        if not isinstance(value, DdsCpTopic):
            raise TypeError(
                f"ddsTopic must be DdsCpTopic or None, got {type(value).__name__}"
            )
        self._ddsTopic = value
        self._iSignal: Optional["ISignal"] = None

    @property
    def i_signal(self) -> Optional["ISignal"]:
        """Get iSignal (Pythonic accessor)."""
        return self._iSignal

    @i_signal.setter
    def i_signal(self, value: Optional["ISignal"]) -> None:
        """
        Set iSignal with validation.

        Args:
            value: The iSignal to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._iSignal = None
            return

        if not isinstance(value, ISignal):
            raise TypeError(
                f"iSignal must be ISignal or None, got {type(value).__name__}"
            )
        self._iSignal = value

    def with_dds_domain(self, value):
        """
        Set dds_domain and return self for chaining.

        Args:
            value: The dds_domain to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_dds_domain("value")
        """
        self.dds_domain = value  # Use property setter (gets validation)
        return self

    def with_dds_qos_profile(self, value):
        """
        Set dds_qos_profile and return self for chaining.

        Args:
            value: The dds_qos_profile to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_dds_qos_profile("value")
        """
        self.dds_qos_profile = value  # Use property setter (gets validation)
        return self

    def with_provided_dds(self, value):
        """
        Set provided_dds and return self for chaining.

        Args:
            value: The provided_dds to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_provided_dds("value")
        """
        self.provided_dds = value  # Use property setter (gets validation)
        return self

    def with_consumed_dds(self, value):
        """
        Set consumed_dds and return self for chaining.

        Args:
            value: The consumed_dds to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_consumed_dds("value")
        """
        self.consumed_dds = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDdsTopic(self) -> DdsCpTopic:
        """
        AUTOSAR-compliant getter for ddsTopic.

        Returns:
            The ddsTopic value

        Note:
            Delegates to dds_topic property (CODING_RULE_V2_00017)
        """
        return self.dds_topic  # Delegates to property

    def setDdsTopic(self, value: DdsCpTopic) -> DdsCpISignalToDdsTopicMapping:
        """
        AUTOSAR-compliant setter for ddsTopic with method chaining.

        Args:
            value: The ddsTopic to set

        Returns:
            self for method chaining

        Note:
            Delegates to dds_topic property setter (gets validation automatically)
        """
        self.dds_topic = value  # Delegates to property setter
        return self

    def getISignal(self) -> ISignal:
        """
        AUTOSAR-compliant getter for iSignal.

        Returns:
            The iSignal value

        Note:
            Delegates to i_signal property (CODING_RULE_V2_00017)
        """
        return self.i_signal  # Delegates to property

    def setISignal(self, value: ISignal) -> DdsCpISignalToDdsTopicMapping:
        """
        AUTOSAR-compliant setter for iSignal with method chaining.

        Args:
            value: The iSignal to set

        Returns:
            self for method chaining

        Note:
            Delegates to i_signal property setter (gets validation automatically)
        """
        self.i_signal = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_dds_topic(self, value: Optional[DdsCpTopic]) -> DdsCpISignalToDdsTopicMapping:
        """
        Set ddsTopic and return self for chaining.

        Args:
            value: The ddsTopic to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_dds_topic("value")
        """
        self.dds_topic = value  # Use property setter (gets validation)
        return self

    def with_i_signal(self, value: Optional["ISignal"]) -> DdsCpISignalToDdsTopicMapping:
        """
        Set iSignal and return self for chaining.

        Args:
            value: The iSignal to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_i_signal("value")
        """
        self.i_signal = value  # Use property setter (gets validation)
        return self



class DdsCpServiceInstance(AbstractServiceInstance, ABC):
    """
    Provided and Consumed Dds Service Instances that are available at the
    ApplicationEndpoint.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::Dds::DdsCpServiceInstance

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 472, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is DdsCpServiceInstance:
            raise TypeError("DdsCpServiceInstance is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to the DdsTopic used as fragment for the topic of field setters.
        self._ddsFieldReply: Optional[DdsCpTopic] = None

    @property
    def dds_field_reply(self) -> Optional[DdsCpTopic]:
        """Get ddsFieldReply (Pythonic accessor)."""
        return self._ddsFieldReply

    @dds_field_reply.setter
    def dds_field_reply(self, value: Optional[DdsCpTopic]) -> None:
        """
        Set ddsFieldReply with validation.

        Args:
            value: The ddsFieldReply to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ddsFieldReply = None
            return

        if not isinstance(value, DdsCpTopic):
            raise TypeError(
                f"ddsFieldReply must be DdsCpTopic or None, got {type(value).__name__}"
            )
        self._ddsFieldReply = value
        self._ddsField: Optional[DdsCpTopic] = None

    @property
    def dds_field(self) -> Optional[DdsCpTopic]:
        """Get ddsField (Pythonic accessor)."""
        return self._ddsField

    @dds_field.setter
    def dds_field(self, value: Optional[DdsCpTopic]) -> None:
        """
        Set ddsField with validation.

        Args:
            value: The ddsField to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ddsField = None
            return

        if not isinstance(value, DdsCpTopic):
            raise TypeError(
                f"ddsField must be DdsCpTopic or None, got {type(value).__name__}"
            )
        self._ddsField = value
        self._ddsMethod: Optional[DdsCpTopic] = None

    @property
    def dds_method(self) -> Optional[DdsCpTopic]:
        """Get ddsMethod (Pythonic accessor)."""
        return self._ddsMethod

    @dds_method.setter
    def dds_method(self, value: Optional[DdsCpTopic]) -> None:
        """
        Set ddsMethod with validation.

        Args:
            value: The ddsMethod to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ddsMethod = None
            return

        if not isinstance(value, DdsCpTopic):
            raise TypeError(
                f"ddsMethod must be DdsCpTopic or None, got {type(value).__name__}"
            )
        self._ddsMethod = value
        # atp.
        # Status=candidate.
        self._ddsServiceQos: Optional[DdsCpQosProfile] = None

    @property
    def dds_service_qos(self) -> Optional[DdsCpQosProfile]:
        """Get ddsServiceQos (Pythonic accessor)."""
        return self._ddsServiceQos

    @dds_service_qos.setter
    def dds_service_qos(self, value: Optional[DdsCpQosProfile]) -> None:
        """
        Set ddsServiceQos with validation.

        Args:
            value: The ddsServiceQos to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ddsServiceQos = None
            return

        if not isinstance(value, DdsCpQosProfile):
            raise TypeError(
                f"ddsServiceQos must be DdsCpQosProfile or None, got {type(value).__name__}"
            )
        self._ddsServiceQos = value
        # instance of the.
        self._serviceInstance: Optional[PositiveInteger] = None

    @property
    def service_instance(self) -> Optional[PositiveInteger]:
        """Get serviceInstance (Pythonic accessor)."""
        return self._serviceInstance

    @service_instance.setter
    def service_instance(self, value: Optional[PositiveInteger]) -> None:
        """
        Set serviceInstance with validation.

        Args:
            value: The serviceInstance to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._serviceInstance = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"serviceInstance must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._serviceInstance = value
        # encoded in the USER_DATA QoS DomainParticipant associated with the Service
        # its value is propagated by DDS Discovery.
        self._serviceInterface: Optional[String] = None

    @property
    def service_interface(self) -> Optional[String]:
        """Get serviceInterface (Pythonic accessor)."""
        return self._serviceInterface

    @service_interface.setter
    def service_interface(self, value: Optional[String]) -> None:
        """
        Set serviceInterface with validation.

        Args:
            value: The serviceInterface to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._serviceInterface = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"serviceInterface must be String or str or None, got {type(value).__name__}"
            )
        self._serviceInterface = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDdsFieldReply(self) -> DdsCpTopic:
        """
        AUTOSAR-compliant getter for ddsFieldReply.

        Returns:
            The ddsFieldReply value

        Note:
            Delegates to dds_field_reply property (CODING_RULE_V2_00017)
        """
        return self.dds_field_reply  # Delegates to property

    def setDdsFieldReply(self, value: DdsCpTopic) -> DdsCpServiceInstance:
        """
        AUTOSAR-compliant setter for ddsFieldReply with method chaining.

        Args:
            value: The ddsFieldReply to set

        Returns:
            self for method chaining

        Note:
            Delegates to dds_field_reply property setter (gets validation automatically)
        """
        self.dds_field_reply = value  # Delegates to property setter
        return self

    def getDdsField(self) -> DdsCpTopic:
        """
        AUTOSAR-compliant getter for ddsField.

        Returns:
            The ddsField value

        Note:
            Delegates to dds_field property (CODING_RULE_V2_00017)
        """
        return self.dds_field  # Delegates to property

    def setDdsField(self, value: DdsCpTopic) -> DdsCpServiceInstance:
        """
        AUTOSAR-compliant setter for ddsField with method chaining.

        Args:
            value: The ddsField to set

        Returns:
            self for method chaining

        Note:
            Delegates to dds_field property setter (gets validation automatically)
        """
        self.dds_field = value  # Delegates to property setter
        return self

    def getDdsMethod(self) -> DdsCpTopic:
        """
        AUTOSAR-compliant getter for ddsMethod.

        Returns:
            The ddsMethod value

        Note:
            Delegates to dds_method property (CODING_RULE_V2_00017)
        """
        return self.dds_method  # Delegates to property

    def setDdsMethod(self, value: DdsCpTopic) -> DdsCpServiceInstance:
        """
        AUTOSAR-compliant setter for ddsMethod with method chaining.

        Args:
            value: The ddsMethod to set

        Returns:
            self for method chaining

        Note:
            Delegates to dds_method property setter (gets validation automatically)
        """
        self.dds_method = value  # Delegates to property setter
        return self

    def getDdsServiceQos(self) -> DdsCpQosProfile:
        """
        AUTOSAR-compliant getter for ddsServiceQos.

        Returns:
            The ddsServiceQos value

        Note:
            Delegates to dds_service_qos property (CODING_RULE_V2_00017)
        """
        return self.dds_service_qos  # Delegates to property

    def setDdsServiceQos(self, value: DdsCpQosProfile) -> DdsCpServiceInstance:
        """
        AUTOSAR-compliant setter for ddsServiceQos with method chaining.

        Args:
            value: The ddsServiceQos to set

        Returns:
            self for method chaining

        Note:
            Delegates to dds_service_qos property setter (gets validation automatically)
        """
        self.dds_service_qos = value  # Delegates to property setter
        return self

    def getServiceInstance(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for serviceInstance.

        Returns:
            The serviceInstance value

        Note:
            Delegates to service_instance property (CODING_RULE_V2_00017)
        """
        return self.service_instance  # Delegates to property

    def setServiceInstance(self, value: PositiveInteger) -> DdsCpServiceInstance:
        """
        AUTOSAR-compliant setter for serviceInstance with method chaining.

        Args:
            value: The serviceInstance to set

        Returns:
            self for method chaining

        Note:
            Delegates to service_instance property setter (gets validation automatically)
        """
        self.service_instance = value  # Delegates to property setter
        return self

    def getServiceInterface(self) -> String:
        """
        AUTOSAR-compliant getter for serviceInterface.

        Returns:
            The serviceInterface value

        Note:
            Delegates to service_interface property (CODING_RULE_V2_00017)
        """
        return self.service_interface  # Delegates to property

    def setServiceInterface(self, value: String) -> DdsCpServiceInstance:
        """
        AUTOSAR-compliant setter for serviceInterface with method chaining.

        Args:
            value: The serviceInterface to set

        Returns:
            self for method chaining

        Note:
            Delegates to service_interface property setter (gets validation automatically)
        """
        self.service_interface = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_dds_field_reply(self, value: Optional[DdsCpTopic]) -> DdsCpServiceInstance:
        """
        Set ddsFieldReply and return self for chaining.

        Args:
            value: The ddsFieldReply to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_dds_field_reply("value")
        """
        self.dds_field_reply = value  # Use property setter (gets validation)
        return self

    def with_dds_field(self, value: Optional[DdsCpTopic]) -> DdsCpServiceInstance:
        """
        Set ddsField and return self for chaining.

        Args:
            value: The ddsField to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_dds_field("value")
        """
        self.dds_field = value  # Use property setter (gets validation)
        return self

    def with_dds_method(self, value: Optional[DdsCpTopic]) -> DdsCpServiceInstance:
        """
        Set ddsMethod and return self for chaining.

        Args:
            value: The ddsMethod to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_dds_method("value")
        """
        self.dds_method = value  # Use property setter (gets validation)
        return self

    def with_dds_service_qos(self, value: Optional[DdsCpQosProfile]) -> DdsCpServiceInstance:
        """
        Set ddsServiceQos and return self for chaining.

        Args:
            value: The ddsServiceQos to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_dds_service_qos("value")
        """
        self.dds_service_qos = value  # Use property setter (gets validation)
        return self

    def with_service_instance(self, value: Optional[PositiveInteger]) -> DdsCpServiceInstance:
        """
        Set serviceInstance and return self for chaining.

        Args:
            value: The serviceInstance to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_service_instance("value")
        """
        self.service_instance = value  # Use property setter (gets validation)
        return self

    def with_service_interface(self, value: Optional[String]) -> DdsCpServiceInstance:
        """
        Set serviceInterface and return self for chaining.

        Args:
            value: The serviceInterface to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_service_interface("value")
        """
        self.service_interface = value  # Use property setter (gets validation)
        return self



class DdsCpServiceInstanceEvent(ARObject):
    """
    This element represents an event as part of the Provided Service Instance.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::Dds::DdsCpServiceInstanceEvent

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 475, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to the PduTriggerung used for the upper layer this DdsEvent
        # message.
        self._ddsEvent: Optional[RefType] = None

    @property
    def dds_event(self) -> Optional[RefType]:
        """Get ddsEvent (Pythonic accessor)."""
        return self._ddsEvent

    @dds_event.setter
    def dds_event(self, value: Optional[RefType]) -> None:
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
        # atp.
        # Status=candidate.
        self._ddsEventQos: Optional[DdsCpQosProfile] = None

    @property
    def dds_event_qos(self) -> Optional[DdsCpQosProfile]:
        """Get ddsEventQos (Pythonic accessor)."""
        return self._ddsEventQos

    @dds_event_qos.setter
    def dds_event_qos(self, value: Optional[DdsCpQosProfile]) -> None:
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
        self._ddsEventTopic: Optional[DdsCpTopic] = None

    @property
    def dds_event_topic(self) -> Optional[DdsCpTopic]:
        """Get ddsEventTopic (Pythonic accessor)."""
        return self._ddsEventTopic

    @dds_event_topic.setter
    def dds_event_topic(self, value: Optional[DdsCpTopic]) -> None:
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

    def setDdsEvent(self, value: RefType) -> DdsCpServiceInstanceEvent:
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

    def getDdsEventQos(self) -> DdsCpQosProfile:
        """
        AUTOSAR-compliant getter for ddsEventQos.

        Returns:
            The ddsEventQos value

        Note:
            Delegates to dds_event_qos property (CODING_RULE_V2_00017)
        """
        return self.dds_event_qos  # Delegates to property

    def setDdsEventQos(self, value: DdsCpQosProfile) -> DdsCpServiceInstanceEvent:
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

    def getDdsEventTopic(self) -> DdsCpTopic:
        """
        AUTOSAR-compliant getter for ddsEventTopic.

        Returns:
            The ddsEventTopic value

        Note:
            Delegates to dds_event_topic property (CODING_RULE_V2_00017)
        """
        return self.dds_event_topic  # Delegates to property

    def setDdsEventTopic(self, value: DdsCpTopic) -> DdsCpServiceInstanceEvent:
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

    def with_dds_event(self, value: Optional[RefType]) -> DdsCpServiceInstanceEvent:
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

    def with_dds_event_qos(self, value: Optional[DdsCpQosProfile]) -> DdsCpServiceInstanceEvent:
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

    def with_dds_event_topic(self, value: Optional[DdsCpTopic]) -> DdsCpServiceInstanceEvent:
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



class DdsCpServiceInstanceOperation(ARObject):
    """
    This element represents an operation as part of the Provided Service
    Instance.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::Dds::DdsCpServiceInstanceOperation

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 475, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to the PduTriggering used for the upper layer of this DdsOperation
                # response message.
        # atp.
        # Status=candidate.
        self._ddsOperation: Optional[RefType] = None

    @property
    def dds_operation(self) -> Optional[RefType]:
        """Get ddsOperation (Pythonic accessor)."""
        return self._ddsOperation

    @dds_operation.setter
    def dds_operation(self, value: Optional[RefType]) -> None:
        """
        Set ddsOperation with validation.

        Args:
            value: The ddsOperation to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ddsOperation = None
            return

        self._ddsOperation = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDdsOperation(self) -> RefType:
        """
        AUTOSAR-compliant getter for ddsOperation.

        Returns:
            The ddsOperation value

        Note:
            Delegates to dds_operation property (CODING_RULE_V2_00017)
        """
        return self.dds_operation  # Delegates to property

    def setDdsOperation(self, value: RefType) -> DdsCpServiceInstanceOperation:
        """
        AUTOSAR-compliant setter for ddsOperation with method chaining.

        Args:
            value: The ddsOperation to set

        Returns:
            self for method chaining

        Note:
            Delegates to dds_operation property setter (gets validation automatically)
        """
        self.dds_operation = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_dds_operation(self, value: Optional[RefType]) -> DdsCpServiceInstanceOperation:
        """
        Set ddsOperation and return self for chaining.

        Args:
            value: The ddsOperation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_dds_operation("value")
        """
        self.dds_operation = value  # Use property setter (gets validation)
        return self



class DdsCpConfig(ARElement):
    """
    Collection of DDS definitions. (cid:53) 525 of 2090 Document ID 63:
    AUTOSAR_CP_TPS_SystemTemplate System Template AUTOSAR CP R23-11 (cid:52)

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::Dds::DdsCpConfig

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 525, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Collection of DDS Domain definitions.
        self._ddsDomain: List[DdsCpDomain] = []

    @property
    def dds_domain(self) -> List[DdsCpDomain]:
        """Get ddsDomain (Pythonic accessor)."""
        return self._ddsDomain
        # Collection of DDS QOS Profiles.
        self._ddsQosProfile: List[DdsCpQosProfile] = []

    @property
    def dds_qos_profile(self) -> List[DdsCpQosProfile]:
        """Get ddsQosProfile (Pythonic accessor)."""
        return self._ddsQosProfile

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDdsDomain(self) -> List[DdsCpDomain]:
        """
        AUTOSAR-compliant getter for ddsDomain.

        Returns:
            The ddsDomain value

        Note:
            Delegates to dds_domain property (CODING_RULE_V2_00017)
        """
        return self.dds_domain  # Delegates to property

    def getDdsQosProfile(self) -> List[DdsCpQosProfile]:
        """
        AUTOSAR-compliant getter for ddsQosProfile.

        Returns:
            The ddsQosProfile value

        Note:
            Delegates to dds_qos_profile property (CODING_RULE_V2_00017)
        """
        return self.dds_qos_profile  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class DdsCpDomain(Identifiable):
    """
    Definition of a DDS Domain.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::Dds::DdsCpDomain

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 526, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Collection of DDS Partition definitions.
        self._ddsPartition: List[DdsCpPartition] = []

    @property
    def dds_partition(self) -> List[DdsCpPartition]:
        """Get ddsPartition (Pythonic accessor)."""
        return self._ddsPartition
        # Collection of DDS Topics.
        self._ddsTopic: List[DdsCpTopic] = []

    @property
    def dds_topic(self) -> List[DdsCpTopic]:
        """Get ddsTopic (Pythonic accessor)."""
        return self._ddsTopic
        # Definition of the DDS Domain Id.
        self._domainId: Optional[PositiveInteger] = None

    @property
    def domain_id(self) -> Optional[PositiveInteger]:
        """Get domainId (Pythonic accessor)."""
        return self._domainId

    @domain_id.setter
    def domain_id(self, value: Optional[PositiveInteger]) -> None:
        """
        Set domainId with validation.

        Args:
            value: The domainId to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._domainId = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"domainId must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._domainId = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDdsPartition(self) -> List[DdsCpPartition]:
        """
        AUTOSAR-compliant getter for ddsPartition.

        Returns:
            The ddsPartition value

        Note:
            Delegates to dds_partition property (CODING_RULE_V2_00017)
        """
        return self.dds_partition  # Delegates to property

    def getDdsTopic(self) -> List[DdsCpTopic]:
        """
        AUTOSAR-compliant getter for ddsTopic.

        Returns:
            The ddsTopic value

        Note:
            Delegates to dds_topic property (CODING_RULE_V2_00017)
        """
        return self.dds_topic  # Delegates to property

    def getDomainId(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for domainId.

        Returns:
            The domainId value

        Note:
            Delegates to domain_id property (CODING_RULE_V2_00017)
        """
        return self.domain_id  # Delegates to property

    def setDomainId(self, value: PositiveInteger) -> DdsCpDomain:
        """
        AUTOSAR-compliant setter for domainId with method chaining.

        Args:
            value: The domainId to set

        Returns:
            self for method chaining

        Note:
            Delegates to domain_id property setter (gets validation automatically)
        """
        self.domain_id = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_domain_id(self, value: Optional[PositiveInteger]) -> DdsCpDomain:
        """
        Set domainId and return self for chaining.

        Args:
            value: The domainId to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_domain_id("value")
        """
        self.domain_id = value  # Use property setter (gets validation)
        return self



class DdsCpTopic(Identifiable):
    """
    Definition of a DDS Partition.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::Dds::DdsCpTopic

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 526, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to the DDS Partition this topic is.
        self._ddsPartition: Optional[DdsCpPartition] = None

    @property
    def dds_partition(self) -> Optional[DdsCpPartition]:
        """Get ddsPartition (Pythonic accessor)."""
        return self._ddsPartition

    @dds_partition.setter
    def dds_partition(self, value: Optional[DdsCpPartition]) -> None:
        """
        Set ddsPartition with validation.

        Args:
            value: The ddsPartition to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ddsPartition = None
            return

        if not isinstance(value, DdsCpPartition):
            raise TypeError(
                f"ddsPartition must be DdsCpPartition or None, got {type(value).__name__}"
            )
        self._ddsPartition = value
        self._topicName: Optional[String] = None

    @property
    def topic_name(self) -> Optional[String]:
        """Get topicName (Pythonic accessor)."""
        return self._topicName

    @topic_name.setter
    def topic_name(self, value: Optional[String]) -> None:
        """
        Set topicName with validation.

        Args:
            value: The topicName to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._topicName = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"topicName must be String or str or None, got {type(value).__name__}"
            )
        self._topicName = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDdsPartition(self) -> DdsCpPartition:
        """
        AUTOSAR-compliant getter for ddsPartition.

        Returns:
            The ddsPartition value

        Note:
            Delegates to dds_partition property (CODING_RULE_V2_00017)
        """
        return self.dds_partition  # Delegates to property

    def setDdsPartition(self, value: DdsCpPartition) -> DdsCpTopic:
        """
        AUTOSAR-compliant setter for ddsPartition with method chaining.

        Args:
            value: The ddsPartition to set

        Returns:
            self for method chaining

        Note:
            Delegates to dds_partition property setter (gets validation automatically)
        """
        self.dds_partition = value  # Delegates to property setter
        return self

    def getTopicName(self) -> String:
        """
        AUTOSAR-compliant getter for topicName.

        Returns:
            The topicName value

        Note:
            Delegates to topic_name property (CODING_RULE_V2_00017)
        """
        return self.topic_name  # Delegates to property

    def setTopicName(self, value: String) -> DdsCpTopic:
        """
        AUTOSAR-compliant setter for topicName with method chaining.

        Args:
            value: The topicName to set

        Returns:
            self for method chaining

        Note:
            Delegates to topic_name property setter (gets validation automatically)
        """
        self.topic_name = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_dds_partition(self, value: Optional[DdsCpPartition]) -> DdsCpTopic:
        """
        Set ddsPartition and return self for chaining.

        Args:
            value: The ddsPartition to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_dds_partition("value")
        """
        self.dds_partition = value  # Use property setter (gets validation)
        return self

    def with_topic_name(self, value: Optional[String]) -> DdsCpTopic:
        """
        Set topicName and return self for chaining.

        Args:
            value: The topicName to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_topic_name("value")
        """
        self.topic_name = value  # Use property setter (gets validation)
        return self



class DdsCpPartition(Identifiable):
    """
    Definition of a DDS Partition.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::Dds::DdsCpPartition

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 527, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Definition of the DDS Partition Name.
        # ’*’ may be used to default partition.
        self._partitionName: Optional[String] = None

    @property
    def partition_name(self) -> Optional[String]:
        """Get partitionName (Pythonic accessor)."""
        return self._partitionName

    @partition_name.setter
    def partition_name(self, value: Optional[String]) -> None:
        """
        Set partitionName with validation.

        Args:
            value: The partitionName to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._partitionName = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"partitionName must be String or str or None, got {type(value).__name__}"
            )
        self._partitionName = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getPartitionName(self) -> String:
        """
        AUTOSAR-compliant getter for partitionName.

        Returns:
            The partitionName value

        Note:
            Delegates to partition_name property (CODING_RULE_V2_00017)
        """
        return self.partition_name  # Delegates to property

    def setPartitionName(self, value: String) -> DdsCpPartition:
        """
        AUTOSAR-compliant setter for partitionName with method chaining.

        Args:
            value: The partitionName to set

        Returns:
            self for method chaining

        Note:
            Delegates to partition_name property setter (gets validation automatically)
        """
        self.partition_name = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_partition_name(self, value: Optional[String]) -> DdsCpPartition:
        """
        Set partitionName and return self for chaining.

        Args:
            value: The partitionName to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_partition_name("value")
        """
        self.partition_name = value  # Use property setter (gets validation)
        return self



class DdsCpQosProfile(Identifiable):
    """
    Definition of a DDS QOS Profile.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::Dds::DdsCpQosProfile

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 528, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines the DDS DEADLINE QoS policy.
        self._deadline: Optional[DdsDeadline] = None

    @property
    def deadline(self) -> Optional[DdsDeadline]:
        """Get deadline (Pythonic accessor)."""
        return self._deadline

    @deadline.setter
    def deadline(self, value: Optional[DdsDeadline]) -> None:
        """
        Set deadline with validation.

        Args:
            value: The deadline to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._deadline = None
            return

        if not isinstance(value, DdsDeadline):
            raise TypeError(
                f"deadline must be DdsDeadline or None, got {type(value).__name__}"
            )
        self._deadline = value
        self._destinationOrder: Optional[DdsDestinationOrder] = None

    @property
    def destination_order(self) -> Optional[DdsDestinationOrder]:
        """Get destinationOrder (Pythonic accessor)."""
        return self._destinationOrder

    @destination_order.setter
    def destination_order(self, value: Optional[DdsDestinationOrder]) -> None:
        """
        Set destinationOrder with validation.

        Args:
            value: The destinationOrder to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._destinationOrder = None
            return

        if not isinstance(value, DdsDestinationOrder):
            raise TypeError(
                f"destinationOrder must be DdsDestinationOrder or None, got {type(value).__name__}"
            )
        self._destinationOrder = value
        # atp.
        # Status=candidate.
        self._durability: Optional[DdsDurabilityService] = None

    @property
    def durability(self) -> Optional[DdsDurabilityService]:
        """Get durability (Pythonic accessor)."""
        return self._durability

    @durability.setter
    def durability(self, value: Optional[DdsDurabilityService]) -> None:
        """
        Set durability with validation.

        Args:
            value: The durability to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._durability = None
            return

        if not isinstance(value, DdsDurabilityService):
            raise TypeError(
                f"durability must be DdsDurabilityService or None, got {type(value).__name__}"
            )
        self._durability = value
        self._history: Optional[DdsHistory] = None

    @property
    def history(self) -> Optional[DdsHistory]:
        """Get history (Pythonic accessor)."""
        return self._history

    @history.setter
    def history(self, value: Optional[DdsHistory]) -> None:
        """
        Set history with validation.

        Args:
            value: The history to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._history = None
            return

        if not isinstance(value, DdsHistory):
            raise TypeError(
                f"history must be DdsHistory or None, got {type(value).__name__}"
            )
        self._history = value
        self._latencyBudget: Optional[DdsLatencyBudget] = None

    @property
    def latency_budget(self) -> Optional[DdsLatencyBudget]:
        """Get latencyBudget (Pythonic accessor)."""
        return self._latencyBudget

    @latency_budget.setter
    def latency_budget(self, value: Optional[DdsLatencyBudget]) -> None:
        """
        Set latencyBudget with validation.

        Args:
            value: The latencyBudget to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._latencyBudget = None
            return

        if not isinstance(value, DdsLatencyBudget):
            raise TypeError(
                f"latencyBudget must be DdsLatencyBudget or None, got {type(value).__name__}"
            )
        self._latencyBudget = value
        self._lifespan: Optional[DdsLifespan] = None

    @property
    def lifespan(self) -> Optional[DdsLifespan]:
        """Get lifespan (Pythonic accessor)."""
        return self._lifespan

    @lifespan.setter
    def lifespan(self, value: Optional[DdsLifespan]) -> None:
        """
        Set lifespan with validation.

        Args:
            value: The lifespan to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._lifespan = None
            return

        if not isinstance(value, DdsLifespan):
            raise TypeError(
                f"lifespan must be DdsLifespan or None, got {type(value).__name__}"
            )
        self._lifespan = value
        self._liveliness: Optional[DdsLiveliness] = None

    @property
    def liveliness(self) -> Optional[DdsLiveliness]:
        """Get liveliness (Pythonic accessor)."""
        return self._liveliness

    @liveliness.setter
    def liveliness(self, value: Optional[DdsLiveliness]) -> None:
        """
        Set liveliness with validation.

        Args:
            value: The liveliness to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._liveliness = None
            return

        if not isinstance(value, DdsLiveliness):
            raise TypeError(
                f"liveliness must be DdsLiveliness or None, got {type(value).__name__}"
            )
        self._liveliness = value
        # atp.
        # Status=candidate.
        self._ownership: Optional[DdsOwnershipStrength] = None

    @property
    def ownership(self) -> Optional[DdsOwnershipStrength]:
        """Get ownership (Pythonic accessor)."""
        return self._ownership

    @ownership.setter
    def ownership(self, value: Optional[DdsOwnershipStrength]) -> None:
        """
        Set ownership with validation.

        Args:
            value: The ownership to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ownership = None
            return

        if not isinstance(value, DdsOwnershipStrength):
            raise TypeError(
                f"ownership must be DdsOwnershipStrength or None, got {type(value).__name__}"
            )
        self._ownership = value
        self._reliability: Optional[DdsReliability] = None

    @property
    def reliability(self) -> Optional[DdsReliability]:
        """Get reliability (Pythonic accessor)."""
        return self._reliability

    @reliability.setter
    def reliability(self, value: Optional[DdsReliability]) -> None:
        """
        Set reliability with validation.

        Args:
            value: The reliability to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._reliability = None
            return

        if not isinstance(value, DdsReliability):
            raise TypeError(
                f"reliability must be DdsReliability or None, got {type(value).__name__}"
            )
        self._reliability = value
        self._resourceLimits: Optional[DdsResourceLimits] = None

    @property
    def resource_limits(self) -> Optional[DdsResourceLimits]:
        """Get resourceLimits (Pythonic accessor)."""
        return self._resourceLimits

    @resource_limits.setter
    def resource_limits(self, value: Optional[DdsResourceLimits]) -> None:
        """
        Set resourceLimits with validation.

        Args:
            value: The resourceLimits to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._resourceLimits = None
            return

        if not isinstance(value, DdsResourceLimits):
            raise TypeError(
                f"resourceLimits must be DdsResourceLimits or None, got {type(value).__name__}"
            )
        self._resourceLimits = value
        self._topicData: Optional[DdsTopicData] = None

    @property
    def topic_data(self) -> Optional[DdsTopicData]:
        """Get topicData (Pythonic accessor)."""
        return self._topicData

    @topic_data.setter
    def topic_data(self, value: Optional[DdsTopicData]) -> None:
        """
        Set topicData with validation.

        Args:
            value: The topicData to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._topicData = None
            return

        if not isinstance(value, DdsTopicData):
            raise TypeError(
                f"topicData must be DdsTopicData or None, got {type(value).__name__}"
            )
        self._topicData = value
        self._transportPriority: Optional[DdsTransportPriority] = None

    @property
    def transport_priority(self) -> Optional[DdsTransportPriority]:
        """Get transportPriority (Pythonic accessor)."""
        return self._transportPriority

    @transport_priority.setter
    def transport_priority(self, value: Optional[DdsTransportPriority]) -> None:
        """
        Set transportPriority with validation.

        Args:
            value: The transportPriority to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._transportPriority = None
            return

        if not isinstance(value, DdsTransportPriority):
            raise TypeError(
                f"transportPriority must be DdsTransportPriority or None, got {type(value).__name__}"
            )
        self._transportPriority = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDeadline(self) -> DdsDeadline:
        """
        AUTOSAR-compliant getter for deadline.

        Returns:
            The deadline value

        Note:
            Delegates to deadline property (CODING_RULE_V2_00017)
        """
        return self.deadline  # Delegates to property

    def setDeadline(self, value: DdsDeadline) -> DdsCpQosProfile:
        """
        AUTOSAR-compliant setter for deadline with method chaining.

        Args:
            value: The deadline to set

        Returns:
            self for method chaining

        Note:
            Delegates to deadline property setter (gets validation automatically)
        """
        self.deadline = value  # Delegates to property setter
        return self

    def getDestinationOrder(self) -> DdsDestinationOrder:
        """
        AUTOSAR-compliant getter for destinationOrder.

        Returns:
            The destinationOrder value

        Note:
            Delegates to destination_order property (CODING_RULE_V2_00017)
        """
        return self.destination_order  # Delegates to property

    def setDestinationOrder(self, value: DdsDestinationOrder) -> DdsCpQosProfile:
        """
        AUTOSAR-compliant setter for destinationOrder with method chaining.

        Args:
            value: The destinationOrder to set

        Returns:
            self for method chaining

        Note:
            Delegates to destination_order property setter (gets validation automatically)
        """
        self.destination_order = value  # Delegates to property setter
        return self

    def getDurability(self) -> DdsDurabilityService:
        """
        AUTOSAR-compliant getter for durability.

        Returns:
            The durability value

        Note:
            Delegates to durability property (CODING_RULE_V2_00017)
        """
        return self.durability  # Delegates to property

    def setDurability(self, value: DdsDurabilityService) -> DdsCpQosProfile:
        """
        AUTOSAR-compliant setter for durability with method chaining.

        Args:
            value: The durability to set

        Returns:
            self for method chaining

        Note:
            Delegates to durability property setter (gets validation automatically)
        """
        self.durability = value  # Delegates to property setter
        return self

    def getHistory(self) -> DdsHistory:
        """
        AUTOSAR-compliant getter for history.

        Returns:
            The history value

        Note:
            Delegates to history property (CODING_RULE_V2_00017)
        """
        return self.history  # Delegates to property

    def setHistory(self, value: DdsHistory) -> DdsCpQosProfile:
        """
        AUTOSAR-compliant setter for history with method chaining.

        Args:
            value: The history to set

        Returns:
            self for method chaining

        Note:
            Delegates to history property setter (gets validation automatically)
        """
        self.history = value  # Delegates to property setter
        return self

    def getLatencyBudget(self) -> DdsLatencyBudget:
        """
        AUTOSAR-compliant getter for latencyBudget.

        Returns:
            The latencyBudget value

        Note:
            Delegates to latency_budget property (CODING_RULE_V2_00017)
        """
        return self.latency_budget  # Delegates to property

    def setLatencyBudget(self, value: DdsLatencyBudget) -> DdsCpQosProfile:
        """
        AUTOSAR-compliant setter for latencyBudget with method chaining.

        Args:
            value: The latencyBudget to set

        Returns:
            self for method chaining

        Note:
            Delegates to latency_budget property setter (gets validation automatically)
        """
        self.latency_budget = value  # Delegates to property setter
        return self

    def getLifespan(self) -> DdsLifespan:
        """
        AUTOSAR-compliant getter for lifespan.

        Returns:
            The lifespan value

        Note:
            Delegates to lifespan property (CODING_RULE_V2_00017)
        """
        return self.lifespan  # Delegates to property

    def setLifespan(self, value: DdsLifespan) -> DdsCpQosProfile:
        """
        AUTOSAR-compliant setter for lifespan with method chaining.

        Args:
            value: The lifespan to set

        Returns:
            self for method chaining

        Note:
            Delegates to lifespan property setter (gets validation automatically)
        """
        self.lifespan = value  # Delegates to property setter
        return self

    def getLiveliness(self) -> DdsLiveliness:
        """
        AUTOSAR-compliant getter for liveliness.

        Returns:
            The liveliness value

        Note:
            Delegates to liveliness property (CODING_RULE_V2_00017)
        """
        return self.liveliness  # Delegates to property

    def setLiveliness(self, value: DdsLiveliness) -> DdsCpQosProfile:
        """
        AUTOSAR-compliant setter for liveliness with method chaining.

        Args:
            value: The liveliness to set

        Returns:
            self for method chaining

        Note:
            Delegates to liveliness property setter (gets validation automatically)
        """
        self.liveliness = value  # Delegates to property setter
        return self

    def getOwnership(self) -> DdsOwnershipStrength:
        """
        AUTOSAR-compliant getter for ownership.

        Returns:
            The ownership value

        Note:
            Delegates to ownership property (CODING_RULE_V2_00017)
        """
        return self.ownership  # Delegates to property

    def setOwnership(self, value: DdsOwnershipStrength) -> DdsCpQosProfile:
        """
        AUTOSAR-compliant setter for ownership with method chaining.

        Args:
            value: The ownership to set

        Returns:
            self for method chaining

        Note:
            Delegates to ownership property setter (gets validation automatically)
        """
        self.ownership = value  # Delegates to property setter
        return self

    def getReliability(self) -> DdsReliability:
        """
        AUTOSAR-compliant getter for reliability.

        Returns:
            The reliability value

        Note:
            Delegates to reliability property (CODING_RULE_V2_00017)
        """
        return self.reliability  # Delegates to property

    def setReliability(self, value: DdsReliability) -> DdsCpQosProfile:
        """
        AUTOSAR-compliant setter for reliability with method chaining.

        Args:
            value: The reliability to set

        Returns:
            self for method chaining

        Note:
            Delegates to reliability property setter (gets validation automatically)
        """
        self.reliability = value  # Delegates to property setter
        return self

    def getResourceLimits(self) -> DdsResourceLimits:
        """
        AUTOSAR-compliant getter for resourceLimits.

        Returns:
            The resourceLimits value

        Note:
            Delegates to resource_limits property (CODING_RULE_V2_00017)
        """
        return self.resource_limits  # Delegates to property

    def setResourceLimits(self, value: DdsResourceLimits) -> DdsCpQosProfile:
        """
        AUTOSAR-compliant setter for resourceLimits with method chaining.

        Args:
            value: The resourceLimits to set

        Returns:
            self for method chaining

        Note:
            Delegates to resource_limits property setter (gets validation automatically)
        """
        self.resource_limits = value  # Delegates to property setter
        return self

    def getTopicData(self) -> DdsTopicData:
        """
        AUTOSAR-compliant getter for topicData.

        Returns:
            The topicData value

        Note:
            Delegates to topic_data property (CODING_RULE_V2_00017)
        """
        return self.topic_data  # Delegates to property

    def setTopicData(self, value: DdsTopicData) -> DdsCpQosProfile:
        """
        AUTOSAR-compliant setter for topicData with method chaining.

        Args:
            value: The topicData to set

        Returns:
            self for method chaining

        Note:
            Delegates to topic_data property setter (gets validation automatically)
        """
        self.topic_data = value  # Delegates to property setter
        return self

    def getTransportPriority(self) -> DdsTransportPriority:
        """
        AUTOSAR-compliant getter for transportPriority.

        Returns:
            The transportPriority value

        Note:
            Delegates to transport_priority property (CODING_RULE_V2_00017)
        """
        return self.transport_priority  # Delegates to property

    def setTransportPriority(self, value: DdsTransportPriority) -> DdsCpQosProfile:
        """
        AUTOSAR-compliant setter for transportPriority with method chaining.

        Args:
            value: The transportPriority to set

        Returns:
            self for method chaining

        Note:
            Delegates to transport_priority property setter (gets validation automatically)
        """
        self.transport_priority = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_deadline(self, value: Optional[DdsDeadline]) -> DdsCpQosProfile:
        """
        Set deadline and return self for chaining.

        Args:
            value: The deadline to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_deadline("value")
        """
        self.deadline = value  # Use property setter (gets validation)
        return self

    def with_destination_order(self, value: Optional[DdsDestinationOrder]) -> DdsCpQosProfile:
        """
        Set destinationOrder and return self for chaining.

        Args:
            value: The destinationOrder to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_destination_order("value")
        """
        self.destination_order = value  # Use property setter (gets validation)
        return self

    def with_durability(self, value: Optional[DdsDurabilityService]) -> DdsCpQosProfile:
        """
        Set durability and return self for chaining.

        Args:
            value: The durability to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_durability("value")
        """
        self.durability = value  # Use property setter (gets validation)
        return self

    def with_history(self, value: Optional[DdsHistory]) -> DdsCpQosProfile:
        """
        Set history and return self for chaining.

        Args:
            value: The history to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_history("value")
        """
        self.history = value  # Use property setter (gets validation)
        return self

    def with_latency_budget(self, value: Optional[DdsLatencyBudget]) -> DdsCpQosProfile:
        """
        Set latencyBudget and return self for chaining.

        Args:
            value: The latencyBudget to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_latency_budget("value")
        """
        self.latency_budget = value  # Use property setter (gets validation)
        return self

    def with_lifespan(self, value: Optional[DdsLifespan]) -> DdsCpQosProfile:
        """
        Set lifespan and return self for chaining.

        Args:
            value: The lifespan to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_lifespan("value")
        """
        self.lifespan = value  # Use property setter (gets validation)
        return self

    def with_liveliness(self, value: Optional[DdsLiveliness]) -> DdsCpQosProfile:
        """
        Set liveliness and return self for chaining.

        Args:
            value: The liveliness to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_liveliness("value")
        """
        self.liveliness = value  # Use property setter (gets validation)
        return self

    def with_ownership(self, value: Optional[DdsOwnershipStrength]) -> DdsCpQosProfile:
        """
        Set ownership and return self for chaining.

        Args:
            value: The ownership to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ownership("value")
        """
        self.ownership = value  # Use property setter (gets validation)
        return self

    def with_reliability(self, value: Optional[DdsReliability]) -> DdsCpQosProfile:
        """
        Set reliability and return self for chaining.

        Args:
            value: The reliability to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_reliability("value")
        """
        self.reliability = value  # Use property setter (gets validation)
        return self

    def with_resource_limits(self, value: Optional[DdsResourceLimits]) -> DdsCpQosProfile:
        """
        Set resourceLimits and return self for chaining.

        Args:
            value: The resourceLimits to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_resource_limits("value")
        """
        self.resource_limits = value  # Use property setter (gets validation)
        return self

    def with_topic_data(self, value: Optional[DdsTopicData]) -> DdsCpQosProfile:
        """
        Set topicData and return self for chaining.

        Args:
            value: The topicData to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_topic_data("value")
        """
        self.topic_data = value  # Use property setter (gets validation)
        return self

    def with_transport_priority(self, value: Optional[DdsTransportPriority]) -> DdsCpQosProfile:
        """
        Set transportPriority and return self for chaining.

        Args:
            value: The transportPriority to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_transport_priority("value")
        """
        self.transport_priority = value  # Use property setter (gets validation)
        return self



class DdsTopicData(ARObject):
    """
    Describes the DDS TOPIC_DATA QoS policy.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::Dds::DdsTopicData

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 529, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # See "TOPIC_DATA" chapter in DDS.
        self._topicData: Optional[String] = None

    @property
    def topic_data(self) -> Optional[String]:
        """Get topicData (Pythonic accessor)."""
        return self._topicData

    @topic_data.setter
    def topic_data(self, value: Optional[String]) -> None:
        """
        Set topicData with validation.

        Args:
            value: The topicData to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._topicData = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"topicData must be String or str or None, got {type(value).__name__}"
            )
        self._topicData = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTopicData(self) -> String:
        """
        AUTOSAR-compliant getter for topicData.

        Returns:
            The topicData value

        Note:
            Delegates to topic_data property (CODING_RULE_V2_00017)
        """
        return self.topic_data  # Delegates to property

    def setTopicData(self, value: String) -> DdsTopicData:
        """
        AUTOSAR-compliant setter for topicData with method chaining.

        Args:
            value: The topicData to set

        Returns:
            self for method chaining

        Note:
            Delegates to topic_data property setter (gets validation automatically)
        """
        self.topic_data = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_topic_data(self, value: Optional[String]) -> DdsTopicData:
        """
        Set topicData and return self for chaining.

        Args:
            value: The topicData to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_topic_data("value")
        """
        self.topic_data = value  # Use property setter (gets validation)
        return self



class DdsDurability(ARObject):
    """
    Describes the DDS DURABILITY QoS policy.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::Dds::DdsDurability

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 530, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # See "DURABILITY" chapter in DDS.
        self._durabilityKind: Optional[DdsDurabilityKindEnum] = None

    @property
    def durability_kind(self) -> Optional[DdsDurabilityKindEnum]:
        """Get durabilityKind (Pythonic accessor)."""
        return self._durabilityKind

    @durability_kind.setter
    def durability_kind(self, value: Optional[DdsDurabilityKindEnum]) -> None:
        """
        Set durabilityKind with validation.

        Args:
            value: The durabilityKind to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._durabilityKind = None
            return

        if not isinstance(value, DdsDurabilityKindEnum):
            raise TypeError(
                f"durabilityKind must be DdsDurabilityKindEnum or None, got {type(value).__name__}"
            )
        self._durabilityKind = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDurabilityKind(self) -> DdsDurabilityKindEnum:
        """
        AUTOSAR-compliant getter for durabilityKind.

        Returns:
            The durabilityKind value

        Note:
            Delegates to durability_kind property (CODING_RULE_V2_00017)
        """
        return self.durability_kind  # Delegates to property

    def setDurabilityKind(self, value: DdsDurabilityKindEnum) -> DdsDurability:
        """
        AUTOSAR-compliant setter for durabilityKind with method chaining.

        Args:
            value: The durabilityKind to set

        Returns:
            self for method chaining

        Note:
            Delegates to durability_kind property setter (gets validation automatically)
        """
        self.durability_kind = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_durability_kind(self, value: Optional[DdsDurabilityKindEnum]) -> DdsDurability:
        """
        Set durabilityKind and return self for chaining.

        Args:
            value: The durabilityKind to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_durability_kind("value")
        """
        self.durability_kind = value  # Use property setter (gets validation)
        return self



class DdsDurabilityService(ARObject):
    """
    Describes the DDS DURABILITY_SERVICE QoS policy.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::Dds::DdsDurabilityService

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 530, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # See "DURABILITY_SERVICE" chapter in DDS.
        # atp.
        # Status=candidate SamplesPer.
        self._durability: Optional[PositiveInteger] = None

    @property
    def durability(self) -> Optional[PositiveInteger]:
        """Get durability (Pythonic accessor)."""
        return self._durability

    @durability.setter
    def durability(self, value: Optional[PositiveInteger]) -> None:
        """
        Set durability with validation.

        Args:
            value: The durability to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._durability = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"durability must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._durability = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDurability(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for durability.

        Returns:
            The durability value

        Note:
            Delegates to durability property (CODING_RULE_V2_00017)
        """
        return self.durability  # Delegates to property

    def setDurability(self, value: PositiveInteger) -> DdsDurabilityService:
        """
        AUTOSAR-compliant setter for durability with method chaining.

        Args:
            value: The durability to set

        Returns:
            self for method chaining

        Note:
            Delegates to durability property setter (gets validation automatically)
        """
        self.durability = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_durability(self, value: Optional[PositiveInteger]) -> DdsDurabilityService:
        """
        Set durability and return self for chaining.

        Args:
            value: The durability to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_durability("value")
        """
        self.durability = value  # Use property setter (gets validation)
        return self



class DdsDeadline(ARObject):
    """
    Describes the DDS DEADLINE QoS policy.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::Dds::DdsDeadline

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 532, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # See "DEADLINE" chapter of DDS.
        # in seconds.
        self._deadlinePeriod: Optional[Float] = None

    @property
    def deadline_period(self) -> Optional[Float]:
        """Get deadlinePeriod (Pythonic accessor)."""
        return self._deadlinePeriod

    @deadline_period.setter
    def deadline_period(self, value: Optional[Float]) -> None:
        """
        Set deadlinePeriod with validation.

        Args:
            value: The deadlinePeriod to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._deadlinePeriod = None
            return

        if not isinstance(value, (Float, float)):
            raise TypeError(
                f"deadlinePeriod must be Float or float or None, got {type(value).__name__}"
            )
        self._deadlinePeriod = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDeadlinePeriod(self) -> Float:
        """
        AUTOSAR-compliant getter for deadlinePeriod.

        Returns:
            The deadlinePeriod value

        Note:
            Delegates to deadline_period property (CODING_RULE_V2_00017)
        """
        return self.deadline_period  # Delegates to property

    def setDeadlinePeriod(self, value: Float) -> DdsDeadline:
        """
        AUTOSAR-compliant setter for deadlinePeriod with method chaining.

        Args:
            value: The deadlinePeriod to set

        Returns:
            self for method chaining

        Note:
            Delegates to deadline_period property setter (gets validation automatically)
        """
        self.deadline_period = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_deadline_period(self, value: Optional[Float]) -> DdsDeadline:
        """
        Set deadlinePeriod and return self for chaining.

        Args:
            value: The deadlinePeriod to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_deadline_period("value")
        """
        self.deadline_period = value  # Use property setter (gets validation)
        return self



class DdsLatencyBudget(ARObject):
    """
    Describes the DDS LATENCY_BUDGET QoS policy.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::Dds::DdsLatencyBudget

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 532, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # See "LATENCY_BUDGET" chapter of DDS.
        # given in seconds.
        self._latencyBudget: Optional[Float] = None

    @property
    def latency_budget(self) -> Optional[Float]:
        """Get latencyBudget (Pythonic accessor)."""
        return self._latencyBudget

    @latency_budget.setter
    def latency_budget(self, value: Optional[Float]) -> None:
        """
        Set latencyBudget with validation.

        Args:
            value: The latencyBudget to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._latencyBudget = None
            return

        if not isinstance(value, (Float, float)):
            raise TypeError(
                f"latencyBudget must be Float or float or None, got {type(value).__name__}"
            )
        self._latencyBudget = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getLatencyBudget(self) -> Float:
        """
        AUTOSAR-compliant getter for latencyBudget.

        Returns:
            The latencyBudget value

        Note:
            Delegates to latency_budget property (CODING_RULE_V2_00017)
        """
        return self.latency_budget  # Delegates to property

    def setLatencyBudget(self, value: Float) -> DdsLatencyBudget:
        """
        AUTOSAR-compliant setter for latencyBudget with method chaining.

        Args:
            value: The latencyBudget to set

        Returns:
            self for method chaining

        Note:
            Delegates to latency_budget property setter (gets validation automatically)
        """
        self.latency_budget = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_latency_budget(self, value: Optional[Float]) -> DdsLatencyBudget:
        """
        Set latencyBudget and return self for chaining.

        Args:
            value: The latencyBudget to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_latency_budget("value")
        """
        self.latency_budget = value  # Use property setter (gets validation)
        return self



class DdsOwnership(ARObject):
    """
    Describes the DDS OWNERSHIP QoS policy.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::Dds::DdsOwnership

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 532, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # See "OWNERSHIP" chapter of DDS.
        # atp.
        # Status=candidate.
        self._ownershipKind: Optional["DdsOwnershipKind"] = None

    @property
    def ownership_kind(self) -> Optional["DdsOwnershipKind"]:
        """Get ownershipKind (Pythonic accessor)."""
        return self._ownershipKind

    @ownership_kind.setter
    def ownership_kind(self, value: Optional["DdsOwnershipKind"]) -> None:
        """
        Set ownershipKind with validation.

        Args:
            value: The ownershipKind to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ownershipKind = None
            return

        if not isinstance(value, DdsOwnershipKind):
            raise TypeError(
                f"ownershipKind must be DdsOwnershipKind or None, got {type(value).__name__}"
            )
        self._ownershipKind = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getOwnershipKind(self) -> "DdsOwnershipKind":
        """
        AUTOSAR-compliant getter for ownershipKind.

        Returns:
            The ownershipKind value

        Note:
            Delegates to ownership_kind property (CODING_RULE_V2_00017)
        """
        return self.ownership_kind  # Delegates to property

    def setOwnershipKind(self, value: "DdsOwnershipKind") -> DdsOwnership:
        """
        AUTOSAR-compliant setter for ownershipKind with method chaining.

        Args:
            value: The ownershipKind to set

        Returns:
            self for method chaining

        Note:
            Delegates to ownership_kind property setter (gets validation automatically)
        """
        self.ownership_kind = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_ownership_kind(self, value: Optional["DdsOwnershipKind"]) -> DdsOwnership:
        """
        Set ownershipKind and return self for chaining.

        Args:
            value: The ownershipKind to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ownership_kind("value")
        """
        self.ownership_kind = value  # Use property setter (gets validation)
        return self



class DdsOwnershipStrength(ARObject):
    """
    Describes the DDS OWNERSHIP_STRENGTH QoS policy.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::Dds::DdsOwnershipStrength

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 533, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # See "OWNERSHIP_STRENGTH" chapter of DDS.
        # atp.
        # Status=candidate.
        self._ownership: Optional[PositiveInteger] = None

    @property
    def ownership(self) -> Optional[PositiveInteger]:
        """Get ownership (Pythonic accessor)."""
        return self._ownership

    @ownership.setter
    def ownership(self, value: Optional[PositiveInteger]) -> None:
        """
        Set ownership with validation.

        Args:
            value: The ownership to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ownership = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"ownership must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._ownership = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getOwnership(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for ownership.

        Returns:
            The ownership value

        Note:
            Delegates to ownership property (CODING_RULE_V2_00017)
        """
        return self.ownership  # Delegates to property

    def setOwnership(self, value: PositiveInteger) -> DdsOwnershipStrength:
        """
        AUTOSAR-compliant setter for ownership with method chaining.

        Args:
            value: The ownership to set

        Returns:
            self for method chaining

        Note:
            Delegates to ownership property setter (gets validation automatically)
        """
        self.ownership = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_ownership(self, value: Optional[PositiveInteger]) -> DdsOwnershipStrength:
        """
        Set ownership and return self for chaining.

        Args:
            value: The ownership to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ownership("value")
        """
        self.ownership = value  # Use property setter (gets validation)
        return self



class DdsLiveliness(ARObject):
    """
    Describes the DDS LIVELINESS QoS policy.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::Dds::DdsLiveliness

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 534, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # See "LIVELINESS" chapter of DDS.
        # given in seconds.
        self._livelinessLease: Optional[Float] = None

    @property
    def liveliness_lease(self) -> Optional[Float]:
        """Get livelinessLease (Pythonic accessor)."""
        return self._livelinessLease

    @liveliness_lease.setter
    def liveliness_lease(self, value: Optional[Float]) -> None:
        """
        Set livelinessLease with validation.

        Args:
            value: The livelinessLease to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._livelinessLease = None
            return

        if not isinstance(value, (Float, float)):
            raise TypeError(
                f"livelinessLease must be Float or float or None, got {type(value).__name__}"
            )
        self._livelinessLease = value
        self._livenessKind: Optional[DdsLivenessKindEnum] = None

    @property
    def liveness_kind(self) -> Optional[DdsLivenessKindEnum]:
        """Get livenessKind (Pythonic accessor)."""
        return self._livenessKind

    @liveness_kind.setter
    def liveness_kind(self, value: Optional[DdsLivenessKindEnum]) -> None:
        """
        Set livenessKind with validation.

        Args:
            value: The livenessKind to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._livenessKind = None
            return

        if not isinstance(value, DdsLivenessKindEnum):
            raise TypeError(
                f"livenessKind must be DdsLivenessKindEnum or None, got {type(value).__name__}"
            )
        self._livenessKind = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getLivelinessLease(self) -> Float:
        """
        AUTOSAR-compliant getter for livelinessLease.

        Returns:
            The livelinessLease value

        Note:
            Delegates to liveliness_lease property (CODING_RULE_V2_00017)
        """
        return self.liveliness_lease  # Delegates to property

    def setLivelinessLease(self, value: Float) -> DdsLiveliness:
        """
        AUTOSAR-compliant setter for livelinessLease with method chaining.

        Args:
            value: The livelinessLease to set

        Returns:
            self for method chaining

        Note:
            Delegates to liveliness_lease property setter (gets validation automatically)
        """
        self.liveliness_lease = value  # Delegates to property setter
        return self

    def getLivenessKind(self) -> DdsLivenessKindEnum:
        """
        AUTOSAR-compliant getter for livenessKind.

        Returns:
            The livenessKind value

        Note:
            Delegates to liveness_kind property (CODING_RULE_V2_00017)
        """
        return self.liveness_kind  # Delegates to property

    def setLivenessKind(self, value: DdsLivenessKindEnum) -> DdsLiveliness:
        """
        AUTOSAR-compliant setter for livenessKind with method chaining.

        Args:
            value: The livenessKind to set

        Returns:
            self for method chaining

        Note:
            Delegates to liveness_kind property setter (gets validation automatically)
        """
        self.liveness_kind = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_liveliness_lease(self, value: Optional[Float]) -> DdsLiveliness:
        """
        Set livelinessLease and return self for chaining.

        Args:
            value: The livelinessLease to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_liveliness_lease("value")
        """
        self.liveliness_lease = value  # Use property setter (gets validation)
        return self

    def with_liveness_kind(self, value: Optional[DdsLivenessKindEnum]) -> DdsLiveliness:
        """
        Set livenessKind and return self for chaining.

        Args:
            value: The livenessKind to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_liveness_kind("value")
        """
        self.liveness_kind = value  # Use property setter (gets validation)
        return self



class DdsReliability(ARObject):
    """
    Describes the DDS RELIABILITY QoS policy.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::Dds::DdsReliability

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 534, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # See "RELIABILITY" chapter of DDS.
        self._reliabilityKind: Optional[DdsReliabilityKindEnum] = None

    @property
    def reliability_kind(self) -> Optional[DdsReliabilityKindEnum]:
        """Get reliabilityKind (Pythonic accessor)."""
        return self._reliabilityKind

    @reliability_kind.setter
    def reliability_kind(self, value: Optional[DdsReliabilityKindEnum]) -> None:
        """
        Set reliabilityKind with validation.

        Args:
            value: The reliabilityKind to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._reliabilityKind = None
            return

        if not isinstance(value, DdsReliabilityKindEnum):
            raise TypeError(
                f"reliabilityKind must be DdsReliabilityKindEnum or None, got {type(value).__name__}"
            )
        self._reliabilityKind = value
        # given in seconds.
        self._reliabilityMax: Optional[Float] = None

    @property
    def reliability_max(self) -> Optional[Float]:
        """Get reliabilityMax (Pythonic accessor)."""
        return self._reliabilityMax

    @reliability_max.setter
    def reliability_max(self, value: Optional[Float]) -> None:
        """
        Set reliabilityMax with validation.

        Args:
            value: The reliabilityMax to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._reliabilityMax = None
            return

        if not isinstance(value, (Float, float)):
            raise TypeError(
                f"reliabilityMax must be Float or float or None, got {type(value).__name__}"
            )
        self._reliabilityMax = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getReliabilityKind(self) -> DdsReliabilityKindEnum:
        """
        AUTOSAR-compliant getter for reliabilityKind.

        Returns:
            The reliabilityKind value

        Note:
            Delegates to reliability_kind property (CODING_RULE_V2_00017)
        """
        return self.reliability_kind  # Delegates to property

    def setReliabilityKind(self, value: DdsReliabilityKindEnum) -> DdsReliability:
        """
        AUTOSAR-compliant setter for reliabilityKind with method chaining.

        Args:
            value: The reliabilityKind to set

        Returns:
            self for method chaining

        Note:
            Delegates to reliability_kind property setter (gets validation automatically)
        """
        self.reliability_kind = value  # Delegates to property setter
        return self

    def getReliabilityMax(self) -> Float:
        """
        AUTOSAR-compliant getter for reliabilityMax.

        Returns:
            The reliabilityMax value

        Note:
            Delegates to reliability_max property (CODING_RULE_V2_00017)
        """
        return self.reliability_max  # Delegates to property

    def setReliabilityMax(self, value: Float) -> DdsReliability:
        """
        AUTOSAR-compliant setter for reliabilityMax with method chaining.

        Args:
            value: The reliabilityMax to set

        Returns:
            self for method chaining

        Note:
            Delegates to reliability_max property setter (gets validation automatically)
        """
        self.reliability_max = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_reliability_kind(self, value: Optional[DdsReliabilityKindEnum]) -> DdsReliability:
        """
        Set reliabilityKind and return self for chaining.

        Args:
            value: The reliabilityKind to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_reliability_kind("value")
        """
        self.reliability_kind = value  # Use property setter (gets validation)
        return self

    def with_reliability_max(self, value: Optional[Float]) -> DdsReliability:
        """
        Set reliabilityMax and return self for chaining.

        Args:
            value: The reliabilityMax to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_reliability_max("value")
        """
        self.reliability_max = value  # Use property setter (gets validation)
        return self



class DdsTransportPriority(ARObject):
    """
    Describes the DDS TRANSPORT_PRIORITY QoS policy.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::Dds::DdsTransportPriority

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 535, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # See "TRANSPORT_PRIORITY" chapter of DDS.
        self._transportPriority: Optional[PositiveInteger] = None

    @property
    def transport_priority(self) -> Optional[PositiveInteger]:
        """Get transportPriority (Pythonic accessor)."""
        return self._transportPriority

    @transport_priority.setter
    def transport_priority(self, value: Optional[PositiveInteger]) -> None:
        """
        Set transportPriority with validation.

        Args:
            value: The transportPriority to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._transportPriority = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"transportPriority must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._transportPriority = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTransportPriority(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for transportPriority.

        Returns:
            The transportPriority value

        Note:
            Delegates to transport_priority property (CODING_RULE_V2_00017)
        """
        return self.transport_priority  # Delegates to property

    def setTransportPriority(self, value: PositiveInteger) -> DdsTransportPriority:
        """
        AUTOSAR-compliant setter for transportPriority with method chaining.

        Args:
            value: The transportPriority to set

        Returns:
            self for method chaining

        Note:
            Delegates to transport_priority property setter (gets validation automatically)
        """
        self.transport_priority = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_transport_priority(self, value: Optional[PositiveInteger]) -> DdsTransportPriority:
        """
        Set transportPriority and return self for chaining.

        Args:
            value: The transportPriority to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_transport_priority("value")
        """
        self.transport_priority = value  # Use property setter (gets validation)
        return self



class DdsLifespan(ARObject):
    """
    Describes the DDS LIFESPAN QoS policy.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::Dds::DdsLifespan

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 536, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # See "LIFESPAN" chapter of DDS.
        # in seconds.
        self._lifespanDuration: Optional[Float] = None

    @property
    def lifespan_duration(self) -> Optional[Float]:
        """Get lifespanDuration (Pythonic accessor)."""
        return self._lifespanDuration

    @lifespan_duration.setter
    def lifespan_duration(self, value: Optional[Float]) -> None:
        """
        Set lifespanDuration with validation.

        Args:
            value: The lifespanDuration to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._lifespanDuration = None
            return

        if not isinstance(value, (Float, float)):
            raise TypeError(
                f"lifespanDuration must be Float or float or None, got {type(value).__name__}"
            )
        self._lifespanDuration = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getLifespanDuration(self) -> Float:
        """
        AUTOSAR-compliant getter for lifespanDuration.

        Returns:
            The lifespanDuration value

        Note:
            Delegates to lifespan_duration property (CODING_RULE_V2_00017)
        """
        return self.lifespan_duration  # Delegates to property

    def setLifespanDuration(self, value: Float) -> DdsLifespan:
        """
        AUTOSAR-compliant setter for lifespanDuration with method chaining.

        Args:
            value: The lifespanDuration to set

        Returns:
            self for method chaining

        Note:
            Delegates to lifespan_duration property setter (gets validation automatically)
        """
        self.lifespan_duration = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_lifespan_duration(self, value: Optional[Float]) -> DdsLifespan:
        """
        Set lifespanDuration and return self for chaining.

        Args:
            value: The lifespanDuration to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_lifespan_duration("value")
        """
        self.lifespan_duration = value  # Use property setter (gets validation)
        return self



class DdsDestinationOrder(ARObject):
    """
    Describes the DDS DESTINATION_ORDER QoS policy.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::Dds::DdsDestinationOrder

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 536, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # See "DESTINATION_ORDER" chapter of DDS.
        # Tags: atp.
        # Status=candidate.
        self._destination: Optional[DdsDestinationOrder] = None

    @property
    def destination(self) -> Optional[DdsDestinationOrder]:
        """Get destination (Pythonic accessor)."""
        return self._destination

    @destination.setter
    def destination(self, value: Optional[DdsDestinationOrder]) -> None:
        """
        Set destination with validation.

        Args:
            value: The destination to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._destination = None
            return

        if not isinstance(value, DdsDestinationOrder):
            raise TypeError(
                f"destination must be DdsDestinationOrder or None, got {type(value).__name__}"
            )
        self._destination = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDestination(self) -> DdsDestinationOrder:
        """
        AUTOSAR-compliant getter for destination.

        Returns:
            The destination value

        Note:
            Delegates to destination property (CODING_RULE_V2_00017)
        """
        return self.destination  # Delegates to property

    def setDestination(self, value: DdsDestinationOrder) -> DdsDestinationOrder:
        """
        AUTOSAR-compliant setter for destination with method chaining.

        Args:
            value: The destination to set

        Returns:
            self for method chaining

        Note:
            Delegates to destination property setter (gets validation automatically)
        """
        self.destination = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_destination(self, value: Optional[DdsDestinationOrder]) -> DdsDestinationOrder:
        """
        Set destination and return self for chaining.

        Args:
            value: The destination to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_destination("value")
        """
        self.destination = value  # Use property setter (gets validation)
        return self



class DdsHistory(ARObject):
    """
    Describes the DDS HISTORY QoS policy.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::Dds::DdsHistory

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 537, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # See "HISTORY" chapter of DDS.
        self._historyKind: Optional[DdsHistoryKindEnum] = None

    @property
    def history_kind(self) -> Optional[DdsHistoryKindEnum]:
        """Get historyKind (Pythonic accessor)."""
        return self._historyKind

    @history_kind.setter
    def history_kind(self, value: Optional[DdsHistoryKindEnum]) -> None:
        """
        Set historyKind with validation.

        Args:
            value: The historyKind to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._historyKind = None
            return

        if not isinstance(value, DdsHistoryKindEnum):
            raise TypeError(
                f"historyKind must be DdsHistoryKindEnum or None, got {type(value).__name__}"
            )
        self._historyKind = value
        # atp.
        # Status=candidate.
        self._historyOrder: Optional[PositiveInteger] = None

    @property
    def history_order(self) -> Optional[PositiveInteger]:
        """Get historyOrder (Pythonic accessor)."""
        return self._historyOrder

    @history_order.setter
    def history_order(self, value: Optional[PositiveInteger]) -> None:
        """
        Set historyOrder with validation.

        Args:
            value: The historyOrder to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._historyOrder = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"historyOrder must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._historyOrder = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getHistoryKind(self) -> DdsHistoryKindEnum:
        """
        AUTOSAR-compliant getter for historyKind.

        Returns:
            The historyKind value

        Note:
            Delegates to history_kind property (CODING_RULE_V2_00017)
        """
        return self.history_kind  # Delegates to property

    def setHistoryKind(self, value: DdsHistoryKindEnum) -> DdsHistory:
        """
        AUTOSAR-compliant setter for historyKind with method chaining.

        Args:
            value: The historyKind to set

        Returns:
            self for method chaining

        Note:
            Delegates to history_kind property setter (gets validation automatically)
        """
        self.history_kind = value  # Delegates to property setter
        return self

    def getHistoryOrder(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for historyOrder.

        Returns:
            The historyOrder value

        Note:
            Delegates to history_order property (CODING_RULE_V2_00017)
        """
        return self.history_order  # Delegates to property

    def setHistoryOrder(self, value: PositiveInteger) -> DdsHistory:
        """
        AUTOSAR-compliant setter for historyOrder with method chaining.

        Args:
            value: The historyOrder to set

        Returns:
            self for method chaining

        Note:
            Delegates to history_order property setter (gets validation automatically)
        """
        self.history_order = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_history_kind(self, value: Optional[DdsHistoryKindEnum]) -> DdsHistory:
        """
        Set historyKind and return self for chaining.

        Args:
            value: The historyKind to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_history_kind("value")
        """
        self.history_kind = value  # Use property setter (gets validation)
        return self

    def with_history_order(self, value: Optional[PositiveInteger]) -> DdsHistory:
        """
        Set historyOrder and return self for chaining.

        Args:
            value: The historyOrder to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_history_order("value")
        """
        self.history_order = value  # Use property setter (gets validation)
        return self



class DdsResourceLimits(ARObject):
    """
    Describes the DDS RESOURCE_LIMITS QoS policy.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::Dds::DdsResourceLimits

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 537, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # See "RESOURCE_LIMITS" chapter of DDS.
        # 2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._maxInstances: Optional[PositiveInteger] = None

    @property
    def max_instances(self) -> Optional[PositiveInteger]:
        """Get maxInstances (Pythonic accessor)."""
        return self._maxInstances

    @max_instances.setter
    def max_instances(self, value: Optional[PositiveInteger]) -> None:
        """
        Set maxInstances with validation.

        Args:
            value: The maxInstances to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxInstances = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"maxInstances must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._maxInstances = value
        self._maxSamples: Optional[PositiveInteger] = None

    @property
    def max_samples(self) -> Optional[PositiveInteger]:
        """Get maxSamples (Pythonic accessor)."""
        return self._maxSamples

    @max_samples.setter
    def max_samples(self, value: Optional[PositiveInteger]) -> None:
        """
        Set maxSamples with validation.

        Args:
            value: The maxSamples to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxSamples = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"maxSamples must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._maxSamples = value
        self._maxSamplesPerInstance: Optional[PositiveInteger] = None

    @property
    def max_samples_per_instance(self) -> Optional[PositiveInteger]:
        """Get maxSamplesPerInstance (Pythonic accessor)."""
        return self._maxSamplesPerInstance

    @max_samples_per_instance.setter
    def max_samples_per_instance(self, value: Optional[PositiveInteger]) -> None:
        """
        Set maxSamplesPerInstance with validation.

        Args:
            value: The maxSamplesPerInstance to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxSamplesPerInstance = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"maxSamplesPerInstance must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._maxSamplesPerInstance = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMaxInstances(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for maxInstances.

        Returns:
            The maxInstances value

        Note:
            Delegates to max_instances property (CODING_RULE_V2_00017)
        """
        return self.max_instances  # Delegates to property

    def setMaxInstances(self, value: PositiveInteger) -> DdsResourceLimits:
        """
        AUTOSAR-compliant setter for maxInstances with method chaining.

        Args:
            value: The maxInstances to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_instances property setter (gets validation automatically)
        """
        self.max_instances = value  # Delegates to property setter
        return self

    def getMaxSamples(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for maxSamples.

        Returns:
            The maxSamples value

        Note:
            Delegates to max_samples property (CODING_RULE_V2_00017)
        """
        return self.max_samples  # Delegates to property

    def setMaxSamples(self, value: PositiveInteger) -> DdsResourceLimits:
        """
        AUTOSAR-compliant setter for maxSamples with method chaining.

        Args:
            value: The maxSamples to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_samples property setter (gets validation automatically)
        """
        self.max_samples = value  # Delegates to property setter
        return self

    def getMaxSamplesPerInstance(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for maxSamplesPerInstance.

        Returns:
            The maxSamplesPerInstance value

        Note:
            Delegates to max_samples_per_instance property (CODING_RULE_V2_00017)
        """
        return self.max_samples_per_instance  # Delegates to property

    def setMaxSamplesPerInstance(self, value: PositiveInteger) -> DdsResourceLimits:
        """
        AUTOSAR-compliant setter for maxSamplesPerInstance with method chaining.

        Args:
            value: The maxSamplesPerInstance to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_samples_per_instance property setter (gets validation automatically)
        """
        self.max_samples_per_instance = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_max_instances(self, value: Optional[PositiveInteger]) -> DdsResourceLimits:
        """
        Set maxInstances and return self for chaining.

        Args:
            value: The maxInstances to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_instances("value")
        """
        self.max_instances = value  # Use property setter (gets validation)
        return self

    def with_max_samples(self, value: Optional[PositiveInteger]) -> DdsResourceLimits:
        """
        Set maxSamples and return self for chaining.

        Args:
            value: The maxSamples to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_samples("value")
        """
        self.max_samples = value  # Use property setter (gets validation)
        return self

    def with_max_samples_per_instance(self, value: Optional[PositiveInteger]) -> DdsResourceLimits:
        """
        Set maxSamplesPerInstance and return self for chaining.

        Args:
            value: The maxSamplesPerInstance to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_samples_per_instance("value")
        """
        self.max_samples_per_instance = value  # Use property setter (gets validation)
        return self



class DdsCpProvidedServiceInstance(DdsCpServiceInstance):
    """
    This meta-class represents the ability to describe the existence and
    configuration of a provided service instance in a concrete implementation on
    top of DDS.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::Dds::DdsCpProvidedServiceInstance

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 472, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The local address over which the Service is provided.
        # atpSplitable; atpVariation.
        self._localUnicast: Optional["ApplicationEndpoint"] = None

    @property
    def local_unicast(self) -> Optional["ApplicationEndpoint"]:
        """Get localUnicast (Pythonic accessor)."""
        return self._localUnicast

    @local_unicast.setter
    def local_unicast(self, value: Optional["ApplicationEndpoint"]) -> None:
        """
        Set localUnicast with validation.

        Args:
            value: The localUnicast to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._localUnicast = None
            return

        if not isinstance(value, ApplicationEndpoint):
            raise TypeError(
                f"localUnicast must be ApplicationEndpoint or None, got {type(value).__name__}"
            )
        self._localUnicast = value
        self._minorVersion: Optional[PositiveInteger] = None

    @property
    def minor_version(self) -> Optional[PositiveInteger]:
        """Get minorVersion (Pythonic accessor)."""
        return self._minorVersion

    @minor_version.setter
    def minor_version(self, value: Optional[PositiveInteger]) -> None:
        """
        Set minorVersion with validation.

        Args:
            value: The minorVersion to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._minorVersion = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"minorVersion must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._minorVersion = value
        # Stereotypes: atpSplitable; atpVariation Event Tags:.
        self._providedDds: List[DdsCpServiceInstance] = []

    @property
    def provided_dds(self) -> List[DdsCpServiceInstance]:
        """Get providedDds (Pythonic accessor)."""
        return self._providedDds
        # This reference defines the remote unicast addresses of consumers.
        # shall ONLY be used if the remote unicast the clients is determined from the
                # not at runtime.
        # atpVariation.
        self._staticRemote: List[ApplicationEndpoint] = []

    @property
    def static_remote(self) -> List[ApplicationEndpoint]:
        """Get staticRemote (Pythonic accessor)."""
        return self._staticRemote

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getLocalUnicast(self) -> "ApplicationEndpoint":
        """
        AUTOSAR-compliant getter for localUnicast.

        Returns:
            The localUnicast value

        Note:
            Delegates to local_unicast property (CODING_RULE_V2_00017)
        """
        return self.local_unicast  # Delegates to property

    def setLocalUnicast(self, value: "ApplicationEndpoint") -> DdsCpProvidedServiceInstance:
        """
        AUTOSAR-compliant setter for localUnicast with method chaining.

        Args:
            value: The localUnicast to set

        Returns:
            self for method chaining

        Note:
            Delegates to local_unicast property setter (gets validation automatically)
        """
        self.local_unicast = value  # Delegates to property setter
        return self

    def getMinorVersion(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for minorVersion.

        Returns:
            The minorVersion value

        Note:
            Delegates to minor_version property (CODING_RULE_V2_00017)
        """
        return self.minor_version  # Delegates to property

    def setMinorVersion(self, value: PositiveInteger) -> DdsCpProvidedServiceInstance:
        """
        AUTOSAR-compliant setter for minorVersion with method chaining.

        Args:
            value: The minorVersion to set

        Returns:
            self for method chaining

        Note:
            Delegates to minor_version property setter (gets validation automatically)
        """
        self.minor_version = value  # Delegates to property setter
        return self

    def getProvidedDds(self) -> List[DdsCpServiceInstance]:
        """
        AUTOSAR-compliant getter for providedDds.

        Returns:
            The providedDds value

        Note:
            Delegates to provided_dds property (CODING_RULE_V2_00017)
        """
        return self.provided_dds  # Delegates to property

    def getStaticRemote(self) -> List[ApplicationEndpoint]:
        """
        AUTOSAR-compliant getter for staticRemote.

        Returns:
            The staticRemote value

        Note:
            Delegates to static_remote property (CODING_RULE_V2_00017)
        """
        return self.static_remote  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_local_unicast(self, value: Optional["ApplicationEndpoint"]) -> DdsCpProvidedServiceInstance:
        """
        Set localUnicast and return self for chaining.

        Args:
            value: The localUnicast to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_local_unicast("value")
        """
        self.local_unicast = value  # Use property setter (gets validation)
        return self

    def with_minor_version(self, value: Optional[PositiveInteger]) -> DdsCpProvidedServiceInstance:
        """
        Set minorVersion and return self for chaining.

        Args:
            value: The minorVersion to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_minor_version("value")
        """
        self.minor_version = value  # Use property setter (gets validation)
        return self



class DdsCpConsumedServiceInstance(DdsCpServiceInstance):
    """
    This meta-class represents the ability to describe the existence and
    configuration of a consumed (required) service instance in a concrete
    implementation on top of DDS.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::Dds::DdsCpConsumedServiceInstance

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 474, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Collection of consumed events.
        # Stereotypes: atpSplitable; atpVariation.
        self._consumedDds: List[DdsCpServiceInstance] = []

    @property
    def consumed_dds(self) -> List[DdsCpServiceInstance]:
        """Get consumedDds (Pythonic accessor)."""
        return self._consumedDds
        # The local address over which the Service is consumed.
        # atpSplitable; atpVariation.
        self._localUnicast: Optional["ApplicationEndpoint"] = None

    @property
    def local_unicast(self) -> Optional["ApplicationEndpoint"]:
        """Get localUnicast (Pythonic accessor)."""
        return self._localUnicast

    @local_unicast.setter
    def local_unicast(self, value: Optional["ApplicationEndpoint"]) -> None:
        """
        Set localUnicast with validation.

        Args:
            value: The localUnicast to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._localUnicast = None
            return

        if not isinstance(value, ApplicationEndpoint):
            raise TypeError(
                f"localUnicast must be ApplicationEndpoint or None, got {type(value).__name__}"
            )
        self._localUnicast = value
        # Value can be set to that represents the Minor Version of the or to ANY.
        self._minorVersion: Optional["AnyVersionString"] = None

    @property
    def minor_version(self) -> Optional["AnyVersionString"]:
        """Get minorVersion (Pythonic accessor)."""
        return self._minorVersion

    @minor_version.setter
    def minor_version(self, value: Optional["AnyVersionString"]) -> None:
        """
        Set minorVersion with validation.

        Args:
            value: The minorVersion to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._minorVersion = None
            return

        if not isinstance(value, AnyVersionString):
            raise TypeError(
                f"minorVersion must be AnyVersionString or None, got {type(value).__name__}"
            )
        self._minorVersion = value
        # shall ONLY be used if the remote unicast the server is determined from the
                # not at runtime.
        # atpVariation.
        self._staticRemote: Optional["ApplicationEndpoint"] = None

    @property
    def static_remote(self) -> Optional["ApplicationEndpoint"]:
        """Get staticRemote (Pythonic accessor)."""
        return self._staticRemote

    @static_remote.setter
    def static_remote(self, value: Optional["ApplicationEndpoint"]) -> None:
        """
        Set staticRemote with validation.

        Args:
            value: The staticRemote to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._staticRemote = None
            return

        if not isinstance(value, ApplicationEndpoint):
            raise TypeError(
                f"staticRemote must be ApplicationEndpoint or None, got {type(value).__name__}"
            )
        self._staticRemote = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getConsumedDds(self) -> List[DdsCpServiceInstance]:
        """
        AUTOSAR-compliant getter for consumedDds.

        Returns:
            The consumedDds value

        Note:
            Delegates to consumed_dds property (CODING_RULE_V2_00017)
        """
        return self.consumed_dds  # Delegates to property

    def getLocalUnicast(self) -> "ApplicationEndpoint":
        """
        AUTOSAR-compliant getter for localUnicast.

        Returns:
            The localUnicast value

        Note:
            Delegates to local_unicast property (CODING_RULE_V2_00017)
        """
        return self.local_unicast  # Delegates to property

    def setLocalUnicast(self, value: "ApplicationEndpoint") -> DdsCpConsumedServiceInstance:
        """
        AUTOSAR-compliant setter for localUnicast with method chaining.

        Args:
            value: The localUnicast to set

        Returns:
            self for method chaining

        Note:
            Delegates to local_unicast property setter (gets validation automatically)
        """
        self.local_unicast = value  # Delegates to property setter
        return self

    def getMinorVersion(self) -> "AnyVersionString":
        """
        AUTOSAR-compliant getter for minorVersion.

        Returns:
            The minorVersion value

        Note:
            Delegates to minor_version property (CODING_RULE_V2_00017)
        """
        return self.minor_version  # Delegates to property

    def setMinorVersion(self, value: "AnyVersionString") -> DdsCpConsumedServiceInstance:
        """
        AUTOSAR-compliant setter for minorVersion with method chaining.

        Args:
            value: The minorVersion to set

        Returns:
            self for method chaining

        Note:
            Delegates to minor_version property setter (gets validation automatically)
        """
        self.minor_version = value  # Delegates to property setter
        return self

    def getStaticRemote(self) -> "ApplicationEndpoint":
        """
        AUTOSAR-compliant getter for staticRemote.

        Returns:
            The staticRemote value

        Note:
            Delegates to static_remote property (CODING_RULE_V2_00017)
        """
        return self.static_remote  # Delegates to property

    def setStaticRemote(self, value: "ApplicationEndpoint") -> DdsCpConsumedServiceInstance:
        """
        AUTOSAR-compliant setter for staticRemote with method chaining.

        Args:
            value: The staticRemote to set

        Returns:
            self for method chaining

        Note:
            Delegates to static_remote property setter (gets validation automatically)
        """
        self.static_remote = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_local_unicast(self, value: Optional["ApplicationEndpoint"]) -> DdsCpConsumedServiceInstance:
        """
        Set localUnicast and return self for chaining.

        Args:
            value: The localUnicast to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_local_unicast("value")
        """
        self.local_unicast = value  # Use property setter (gets validation)
        return self

    def with_minor_version(self, value: Optional["AnyVersionString"]) -> DdsCpConsumedServiceInstance:
        """
        Set minorVersion and return self for chaining.

        Args:
            value: The minorVersion to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_minor_version("value")
        """
        self.minor_version = value  # Use property setter (gets validation)
        return self

    def with_static_remote(self, value: Optional["ApplicationEndpoint"]) -> DdsCpConsumedServiceInstance:
        """
        Set staticRemote and return self for chaining.

        Args:
            value: The staticRemote to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_static_remote("value")
        """
        self.static_remote = value  # Use property setter (gets validation)
        return self


class DdsDurabilityKindEnum(AREnum):
    """
    DdsDurabilityKindEnum enumeration

Defines the DDS DURABILITY kind. Tags: atp.Status=candidate Aggregated by DdsDurability.durabilityKind

Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::Dds
    """
    # See "DURABILITY" chapter of DDS.
    persistenttransienttransientLocalvolatile = "0"



class DdsDurabilityServiceHistoryKindEnum(AREnum):
    """
    DdsDurabilityServiceHistoryKindEnum enumeration

Defines the DDS DURABILITY_SERVICE HISTORY kind. Tags: atp.Status=candidate Aggregated by DdsDurabilityService.durabilityServiceHistoryKind

Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::Dds
    """
    # See "DURABILITY_SERVICE" chapter of DDS.
    keepAllkeepLast = "1"



class DdsOwnershipKindEnum(AREnum):
    """
    DdsOwnershipKindEnum enumeration

Defines the DDS OWNERSHIP kind. Tags: atp.Status=candidate Aggregated by DdsOwnership.ownershipKind

Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::Dds
    """
    # See "OWNERSHIP" chapter of DDS.
    exclusiveshared = "0"



class DdsLivenessKindEnum(AREnum):
    """
    DdsLivenessKindEnum enumeration

Defines the DDS LIVELINESS kind. Tags: atp.Status=candidate Aggregated by DdsLiveliness.livenessKind

Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::Dds
    """
    # See "LIVELINESS" chapter of DDS.
    automaticmanualByParticipantmanualByTopic = "1"



class DdsReliabilityKindEnum(AREnum):
    """
    DdsReliabilityKindEnum enumeration

See "RELIABILITY" chapter of DDS. Tags: atp.Status=candidate Aggregated by DdsReliability.reliabilityKind

Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::Dds
    """
    # See "RELIABILITY" chapter of DDS.
    bestEffortreliable = "0"



class DdsDestinationOrderKindEnum(AREnum):
    """
    DdsDestinationOrderKindEnum enumeration

Defines the DDS DESTINATION_ORDER kind. Tags: atp.Status=candidate Aggregated by DdsDestinationOrder.destinationOrderKind

Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::Dds
    """
    # See "DESTINATION_ORDER" chapter of DDS.
    byReceptionTimestampbySourceTimestamp = "1"



class DdsHistoryKindEnum(AREnum):
    """
    DdsHistoryKindEnum enumeration

Defines the DDS HISTORY kind. Tags: atp.Status=candidate Aggregated by DdsHistory.historyKind

Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::Dds
    """
    # See "HISTORY" chapter of DDS.
    keepAllkeepLast = "0"

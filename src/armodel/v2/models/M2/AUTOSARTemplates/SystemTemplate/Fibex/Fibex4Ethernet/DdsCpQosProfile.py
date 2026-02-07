from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

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
        self._deadline: Optional["DdsDeadline"] = None

    @property
    def deadline(self) -> Optional["DdsDeadline"]:
        """Get deadline (Pythonic accessor)."""
        return self._deadline

    @deadline.setter
    def deadline(self, value: Optional["DdsDeadline"]) -> None:
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
        # Defines the DDS DESTINATION_ORDER QoS policy.
        self._destinationOrder: Optional["DdsDestinationOrder"] = None

    @property
    def destination_order(self) -> Optional["DdsDestinationOrder"]:
        """Get destinationOrder (Pythonic accessor)."""
        return self._destinationOrder

    @destination_order.setter
    def destination_order(self, value: Optional["DdsDestinationOrder"]) -> None:
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
        # Defines the DDS DURABILITY_SERVICE QoS policy.
        # atp.
        # Status=candidate.
        self._durability: Optional["DdsDurabilityService"] = None

    @property
    def durability(self) -> Optional["DdsDurabilityService"]:
        """Get durability (Pythonic accessor)."""
        return self._durability

    @durability.setter
    def durability(self, value: Optional["DdsDurabilityService"]) -> None:
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
        # Defines the DDS HISTORY QoS policy.
        self._history: Optional["DdsHistory"] = None

    @property
    def history(self) -> Optional["DdsHistory"]:
        """Get history (Pythonic accessor)."""
        return self._history

    @history.setter
    def history(self, value: Optional["DdsHistory"]) -> None:
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
        # Defines the DDS LATENCY_BUDGET QoS policy.
        self._latencyBudget: Optional["DdsLatencyBudget"] = None

    @property
    def latency_budget(self) -> Optional["DdsLatencyBudget"]:
        """Get latencyBudget (Pythonic accessor)."""
        return self._latencyBudget

    @latency_budget.setter
    def latency_budget(self, value: Optional["DdsLatencyBudget"]) -> None:
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
        # Defines the DDS LIFESPAN QoS policy.
        self._lifespan: Optional["DdsLifespan"] = None

    @property
    def lifespan(self) -> Optional["DdsLifespan"]:
        """Get lifespan (Pythonic accessor)."""
        return self._lifespan

    @lifespan.setter
    def lifespan(self, value: Optional["DdsLifespan"]) -> None:
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
        # Defines the DDS LIVELINESS QoS policy.
        self._liveliness: Optional["DdsLiveliness"] = None

    @property
    def liveliness(self) -> Optional["DdsLiveliness"]:
        """Get liveliness (Pythonic accessor)."""
        return self._liveliness

    @liveliness.setter
    def liveliness(self, value: Optional["DdsLiveliness"]) -> None:
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
        # Defines the DDS OWNERSHIP_STRENGTH QoS policy.
        # atp.
        # Status=candidate.
        self._ownership: Optional["DdsOwnershipStrength"] = None

    @property
    def ownership(self) -> Optional["DdsOwnershipStrength"]:
        """Get ownership (Pythonic accessor)."""
        return self._ownership

    @ownership.setter
    def ownership(self, value: Optional["DdsOwnershipStrength"]) -> None:
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
        # Defines the DDS RELIABILITY QoS policy.
        self._reliability: Optional["DdsReliability"] = None

    @property
    def reliability(self) -> Optional["DdsReliability"]:
        """Get reliability (Pythonic accessor)."""
        return self._reliability

    @reliability.setter
    def reliability(self, value: Optional["DdsReliability"]) -> None:
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
        # Defines the DDS RESOURCE_LIMITS QoS policy.
        self._resourceLimits: Optional["DdsResourceLimits"] = None

    @property
    def resource_limits(self) -> Optional["DdsResourceLimits"]:
        """Get resourceLimits (Pythonic accessor)."""
        return self._resourceLimits

    @resource_limits.setter
    def resource_limits(self, value: Optional["DdsResourceLimits"]) -> None:
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
        # Defines the DDS TOPIC_DATA QoS policy.
        self._topicData: Optional["DdsTopicData"] = None

    @property
    def topic_data(self) -> Optional["DdsTopicData"]:
        """Get topicData (Pythonic accessor)."""
        return self._topicData

    @topic_data.setter
    def topic_data(self, value: Optional["DdsTopicData"]) -> None:
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
        # Defines the DDS TRANSPORT_PRIORITY QoS policy.
        self._transportPriority: Optional["DdsTransportPriority"] = None

    @property
    def transport_priority(self) -> Optional["DdsTransportPriority"]:
        """Get transportPriority (Pythonic accessor)."""
        return self._transportPriority

    @transport_priority.setter
    def transport_priority(self, value: Optional["DdsTransportPriority"]) -> None:
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

    def getDeadline(self) -> "DdsDeadline":
        """
        AUTOSAR-compliant getter for deadline.
        
        Returns:
            The deadline value
        
        Note:
            Delegates to deadline property (CODING_RULE_V2_00017)
        """
        return self.deadline  # Delegates to property

    def setDeadline(self, value: "DdsDeadline") -> "DdsCpQosProfile":
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

    def getDestinationOrder(self) -> "DdsDestinationOrder":
        """
        AUTOSAR-compliant getter for destinationOrder.
        
        Returns:
            The destinationOrder value
        
        Note:
            Delegates to destination_order property (CODING_RULE_V2_00017)
        """
        return self.destination_order  # Delegates to property

    def setDestinationOrder(self, value: "DdsDestinationOrder") -> "DdsCpQosProfile":
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

    def getDurability(self) -> "DdsDurabilityService":
        """
        AUTOSAR-compliant getter for durability.
        
        Returns:
            The durability value
        
        Note:
            Delegates to durability property (CODING_RULE_V2_00017)
        """
        return self.durability  # Delegates to property

    def setDurability(self, value: "DdsDurabilityService") -> "DdsCpQosProfile":
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

    def getHistory(self) -> "DdsHistory":
        """
        AUTOSAR-compliant getter for history.
        
        Returns:
            The history value
        
        Note:
            Delegates to history property (CODING_RULE_V2_00017)
        """
        return self.history  # Delegates to property

    def setHistory(self, value: "DdsHistory") -> "DdsCpQosProfile":
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

    def getLatencyBudget(self) -> "DdsLatencyBudget":
        """
        AUTOSAR-compliant getter for latencyBudget.
        
        Returns:
            The latencyBudget value
        
        Note:
            Delegates to latency_budget property (CODING_RULE_V2_00017)
        """
        return self.latency_budget  # Delegates to property

    def setLatencyBudget(self, value: "DdsLatencyBudget") -> "DdsCpQosProfile":
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

    def getLifespan(self) -> "DdsLifespan":
        """
        AUTOSAR-compliant getter for lifespan.
        
        Returns:
            The lifespan value
        
        Note:
            Delegates to lifespan property (CODING_RULE_V2_00017)
        """
        return self.lifespan  # Delegates to property

    def setLifespan(self, value: "DdsLifespan") -> "DdsCpQosProfile":
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

    def getLiveliness(self) -> "DdsLiveliness":
        """
        AUTOSAR-compliant getter for liveliness.
        
        Returns:
            The liveliness value
        
        Note:
            Delegates to liveliness property (CODING_RULE_V2_00017)
        """
        return self.liveliness  # Delegates to property

    def setLiveliness(self, value: "DdsLiveliness") -> "DdsCpQosProfile":
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

    def getOwnership(self) -> "DdsOwnershipStrength":
        """
        AUTOSAR-compliant getter for ownership.
        
        Returns:
            The ownership value
        
        Note:
            Delegates to ownership property (CODING_RULE_V2_00017)
        """
        return self.ownership  # Delegates to property

    def setOwnership(self, value: "DdsOwnershipStrength") -> "DdsCpQosProfile":
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

    def getReliability(self) -> "DdsReliability":
        """
        AUTOSAR-compliant getter for reliability.
        
        Returns:
            The reliability value
        
        Note:
            Delegates to reliability property (CODING_RULE_V2_00017)
        """
        return self.reliability  # Delegates to property

    def setReliability(self, value: "DdsReliability") -> "DdsCpQosProfile":
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

    def getResourceLimits(self) -> "DdsResourceLimits":
        """
        AUTOSAR-compliant getter for resourceLimits.
        
        Returns:
            The resourceLimits value
        
        Note:
            Delegates to resource_limits property (CODING_RULE_V2_00017)
        """
        return self.resource_limits  # Delegates to property

    def setResourceLimits(self, value: "DdsResourceLimits") -> "DdsCpQosProfile":
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

    def getTopicData(self) -> "DdsTopicData":
        """
        AUTOSAR-compliant getter for topicData.
        
        Returns:
            The topicData value
        
        Note:
            Delegates to topic_data property (CODING_RULE_V2_00017)
        """
        return self.topic_data  # Delegates to property

    def setTopicData(self, value: "DdsTopicData") -> "DdsCpQosProfile":
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

    def getTransportPriority(self) -> "DdsTransportPriority":
        """
        AUTOSAR-compliant getter for transportPriority.
        
        Returns:
            The transportPriority value
        
        Note:
            Delegates to transport_priority property (CODING_RULE_V2_00017)
        """
        return self.transport_priority  # Delegates to property

    def setTransportPriority(self, value: "DdsTransportPriority") -> "DdsCpQosProfile":
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

    def with_deadline(self, value: Optional["DdsDeadline"]) -> "DdsCpQosProfile":
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

    def with_destination_order(self, value: Optional["DdsDestinationOrder"]) -> "DdsCpQosProfile":
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

    def with_durability(self, value: Optional["DdsDurabilityService"]) -> "DdsCpQosProfile":
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

    def with_history(self, value: Optional["DdsHistory"]) -> "DdsCpQosProfile":
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

    def with_latency_budget(self, value: Optional["DdsLatencyBudget"]) -> "DdsCpQosProfile":
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

    def with_lifespan(self, value: Optional["DdsLifespan"]) -> "DdsCpQosProfile":
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

    def with_liveliness(self, value: Optional["DdsLiveliness"]) -> "DdsCpQosProfile":
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

    def with_ownership(self, value: Optional["DdsOwnershipStrength"]) -> "DdsCpQosProfile":
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

    def with_reliability(self, value: Optional["DdsReliability"]) -> "DdsCpQosProfile":
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

    def with_resource_limits(self, value: Optional["DdsResourceLimits"]) -> "DdsCpQosProfile":
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

    def with_topic_data(self, value: Optional["DdsTopicData"]) -> "DdsCpQosProfile":
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

    def with_transport_priority(self, value: Optional["DdsTransportPriority"]) -> "DdsCpQosProfile":
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
from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import String
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


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
        self._topicData: Optional["String"] = None

    @property
    def topic_data(self) -> Optional["String"]:
        """Get topicData (Pythonic accessor)."""
        return self._topicData

    @topic_data.setter
    def topic_data(self, value: Optional["String"]) -> None:
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

        if not isinstance(value, String):
            raise TypeError(
                f"topicData must be String or None, got {type(value).__name__}"
            )
        self._topicData = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTopicData(self) -> "String":
        """
        AUTOSAR-compliant getter for topicData.

        Returns:
            The topicData value

        Note:
            Delegates to topic_data property (CODING_RULE_V2_00017)
        """
        return self.topic_data  # Delegates to property

    def setTopicData(self, value: "String") -> "DdsTopicData":
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

    def with_topic_data(self, value: Optional["String"]) -> "DdsTopicData":
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

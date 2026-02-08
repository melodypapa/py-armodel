from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    DdsCpPartition,
    String,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


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
        self._ddsPartition: Optional["DdsCpPartition"] = None

    @property
    def dds_partition(self) -> Optional["DdsCpPartition"]:
        """Get ddsPartition (Pythonic accessor)."""
        return self._ddsPartition

    @dds_partition.setter
    def dds_partition(self, value: Optional["DdsCpPartition"]) -> None:
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
        # Definition of the DDS Topic Name.
        self._topicName: Optional["String"] = None

    @property
    def topic_name(self) -> Optional["String"]:
        """Get topicName (Pythonic accessor)."""
        return self._topicName

    @topic_name.setter
    def topic_name(self, value: Optional["String"]) -> None:
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

        if not isinstance(value, String):
            raise TypeError(
                f"topicName must be String or None, got {type(value).__name__}"
            )
        self._topicName = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDdsPartition(self) -> "DdsCpPartition":
        """
        AUTOSAR-compliant getter for ddsPartition.

        Returns:
            The ddsPartition value

        Note:
            Delegates to dds_partition property (CODING_RULE_V2_00017)
        """
        return self.dds_partition  # Delegates to property

    def setDdsPartition(self, value: "DdsCpPartition") -> "DdsCpTopic":
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

    def getTopicName(self) -> "String":
        """
        AUTOSAR-compliant getter for topicName.

        Returns:
            The topicName value

        Note:
            Delegates to topic_name property (CODING_RULE_V2_00017)
        """
        return self.topic_name  # Delegates to property

    def setTopicName(self, value: "String") -> "DdsCpTopic":
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

    def with_dds_partition(self, value: Optional["DdsCpPartition"]) -> "DdsCpTopic":
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

    def with_topic_name(self, value: Optional["String"]) -> "DdsCpTopic":
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

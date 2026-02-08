from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    DdsCpPartition,
    DdsCpTopic,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)


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
        self._ddsPartition: List["DdsCpPartition"] = []

    @property
    def dds_partition(self) -> List["DdsCpPartition"]:
        """Get ddsPartition (Pythonic accessor)."""
        return self._ddsPartition
        # Collection of DDS Topics.
        self._ddsTopic: List["DdsCpTopic"] = []

    @property
    def dds_topic(self) -> List["DdsCpTopic"]:
        """Get ddsTopic (Pythonic accessor)."""
        return self._ddsTopic
        # Definition of the DDS Domain Id.
        self._domainId: Optional["PositiveInteger"] = None

    @property
    def domain_id(self) -> Optional["PositiveInteger"]:
        """Get domainId (Pythonic accessor)."""
        return self._domainId

    @domain_id.setter
    def domain_id(self, value: Optional["PositiveInteger"]) -> None:
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

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"domainId must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._domainId = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDdsPartition(self) -> List["DdsCpPartition"]:
        """
        AUTOSAR-compliant getter for ddsPartition.

        Returns:
            The ddsPartition value

        Note:
            Delegates to dds_partition property (CODING_RULE_V2_00017)
        """
        return self.dds_partition  # Delegates to property

    def getDdsTopic(self) -> List["DdsCpTopic"]:
        """
        AUTOSAR-compliant getter for ddsTopic.

        Returns:
            The ddsTopic value

        Note:
            Delegates to dds_topic property (CODING_RULE_V2_00017)
        """
        return self.dds_topic  # Delegates to property

    def getDomainId(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for domainId.

        Returns:
            The domainId value

        Note:
            Delegates to domain_id property (CODING_RULE_V2_00017)
        """
        return self.domain_id  # Delegates to property

    def setDomainId(self, value: "PositiveInteger") -> "DdsCpDomain":
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

    def with_domain_id(self, value: Optional["PositiveInteger"]) -> "DdsCpDomain":
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

from typing import List

from armodel.v2.models.M2.AUTOSARTemplates import (
    IdsCommonElement,
    IdsmRateLimitation,
    IdsmTrafficLimitation,
)


class IdsmProperties(IdsCommonElement):
    """
    This meta-class provides the ability to aggregate filters for security
    events.

    Package: M2::AUTOSARTemplates::SecurityExtractTemplate::IdsmProperties

    Sources:
      - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (Page 63, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This aggregation represents the collection of rate filters for security
        # events in the enclosing 97 Document ID 980:
        # AUTOSAR_FO_TPS_SecurityExtractTemplate Template R23-11.
        self._rateLimitation: List["IdsmRateLimitation"] = []

    @property
    def rate_limitation(self) -> List["IdsmRateLimitation"]:
        """Get rateLimitation (Pythonic accessor)."""
        return self._rateLimitation
        # This aggregation represents the collection of traffic filters for security
        # events in the enclosing.
        self._trafficLimitation: List["IdsmTrafficLimitation"] = []

    @property
    def traffic_limitation(self) -> List["IdsmTrafficLimitation"]:
        """Get trafficLimitation (Pythonic accessor)."""
        return self._trafficLimitation

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getRateLimitation(self) -> List["IdsmRateLimitation"]:
        """
        AUTOSAR-compliant getter for rateLimitation.

        Returns:
            The rateLimitation value

        Note:
            Delegates to rate_limitation property (CODING_RULE_V2_00017)
        """
        return self.rate_limitation  # Delegates to property

    def getTrafficLimitation(self) -> List["IdsmTrafficLimitation"]:
        """
        AUTOSAR-compliant getter for trafficLimitation.

        Returns:
            The trafficLimitation value

        Note:
            Delegates to traffic_limitation property (CODING_RULE_V2_00017)
        """
        return self.traffic_limitation  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

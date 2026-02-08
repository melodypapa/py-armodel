from typing import List
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore import FibexElement


class ConsumedProvidedServiceInstanceGroup(FibexElement):
    """
    The AUTOSAR ServiceDiscovery is able to start and to stop ClientServices and
    Server Services,respectively, at runtime. A SdServiceGroup contains several
    ClientServices and Server Services, respectively.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::ServiceInstances::ConsumedProvidedServiceInstanceGroup

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 523, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference assigns a set of ProvidedServiceInstances to the
                # ConsumedProvidedServiceInstanceGroup.
        # atpVariation.
        self._consumed: List["ConsumedService"] = []

    @property
    def consumed(self) -> List["ConsumedService"]:
        """Get consumed (Pythonic accessor)."""
        return self._consumed
        # This reference assigns a set of ConsumedService Instances to the
        # ConsumedProvidedServiceInstance atpVariation.
        self._providedService: List["ProvidedService"] = []

    @property
    def provided_service(self) -> List["ProvidedService"]:
        """Get providedService (Pythonic accessor)."""
        return self._providedService

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getConsumed(self) -> List["ConsumedService"]:
        """
        AUTOSAR-compliant getter for consumed.

        Returns:
            The consumed value

        Note:
            Delegates to consumed property (CODING_RULE_V2_00017)
        """
        return self.consumed  # Delegates to property

    def getProvidedService(self) -> List["ProvidedService"]:
        """
        AUTOSAR-compliant getter for providedService.

        Returns:
            The providedService value

        Note:
            Delegates to provided_service property (CODING_RULE_V2_00017)
        """
        return self.provided_service  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

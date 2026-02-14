"""
AUTOSAR Package - IntrusionDetectionSystem

Package: M2::AUTOSARTemplates::AdaptivePlatform::PlatformModuleDeployment::IntrusionDetectionSystem
"""


from abc import ABC
from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class PlatformModule(Identifiable):
    """
    Platform module configuration.

    Tags: atp.Status=candidate

    Package: M2::AUTOSARTemplates::AdaptivePlatform::PlatformModuleDeployment

    Sources:
      - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (Foundation R23-11)
    """

    def __init__(self) -> None:
        super().__init__()


class TimeBaseResource(Identifiable):
    """
    Time base resource configuration.

    Package: M2::AUTOSARTemplates::AdaptivePlatform::PlatformModuleDeployment

    Sources:
      - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (Foundation R23-11)
    """

    def __init__(self) -> None:
        super().__init__()


class IdsPlatformInstantiation(Identifiable, ABC):
    """
    This meta-class acts as an abstract base class for platform modules that
    implement the intrusion detection system.

    Package: M2::AUTOSARTemplates::AdaptivePlatform::PlatformModuleDeployment::IntrusionDetectionSystem::IdsPlatformInstantiation

    Sources:
      - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (Page 63, Foundation R23-11)
    """
    def __init__(self) -> None:
        if type(self) is IdsPlatformInstantiation:
            raise TypeError("IdsPlatformInstantiation is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This association contains the network configuration that shall be applied to
                # an instance of an IDS entity.
        # atp.
        # Status=candidate.
        self._network: List[PlatformModule] = []

    @property
    def network(self) -> List[PlatformModule]:
        """Get network (Pythonic accessor)."""
        return self._network
        # This reference identifies the applicable time base atpVariation.
        self._timeBase: Optional[TimeBaseResource] = None

    @property
    def time_base(self) -> Optional[TimeBaseResource]:
        """Get timeBase (Pythonic accessor)."""
        return self._timeBase

    @time_base.setter
    def time_base(self, value: Optional[TimeBaseResource]) -> None:
        """
        Set timeBase with validation.

        Args:
            value: The timeBase to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeBase = None
            return

        if not isinstance(value, TimeBaseResource):
            raise TypeError(
                f"timeBase must be TimeBaseResource or None, got {type(value).__name__}"
            )
        self._timeBase = value

    def with_network(self, value: List[PlatformModule]) -> "IdsPlatformInstantiation":
        """
        Set network and return self for chaining.

        Args:
            value: The network to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_network("value")
        """
        self.network = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getNetwork(self) -> List[PlatformModule]:
        """
        AUTOSAR-compliant getter for network.

        Returns:
            The network value

        Note:
            Delegates to network property (CODING_RULE_V2_00017)
        """
        return self.network  # Delegates to property

    def getTimeBase(self) -> Optional[TimeBaseResource]:
        """
        AUTOSAR-compliant getter for timeBase.

        Returns:
            The timeBase value

        Note:
            Delegates to time_base property (CODING_RULE_V2_00017)
        """
        return self.time_base  # Delegates to property

    def setTimeBase(self, value: TimeBaseResource) -> "IdsPlatformInstantiation":
        """
        AUTOSAR-compliant setter for timeBase with method chaining.

        Args:
            value: The timeBase to set

        Returns:
            self for method chaining

        Note:
            Delegates to time_base property setter (gets validation automatically)
        """
        self.time_base = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_time_base(self, value: Optional[TimeBaseResource]) -> "IdsPlatformInstantiation":
        """
        Set timeBase and return self for chaining.

        Args:
            value: The timeBase to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_time_base("value")
        """
        self.time_base = value  # Use property setter (gets validation)
        return self



class IdsmModuleInstantiation(IdsPlatformInstantiation):
    """
    This meta-class defines the attributes for the IdsM configuration on a
    specific machine.

    Package: M2::AUTOSARTemplates::AdaptivePlatform::PlatformModuleDeployment::IntrusionDetectionSystem::IdsmModuleInstantiation

    Sources:
      - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (Page 63, Foundation R23-11)
    """
    def __init__(self) -> None:
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

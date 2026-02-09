"""
AUTOSAR Package - TimingCpSoftwareCluster

Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingCpSoftwareCluster
"""

from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class TDCpSoftwareClusterMappingSet(ARElement):
    """
    This is used to gather of classic platform software cluster mappings.
    
    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingCpSoftwareCluster::TDCpSoftwareClusterMappingSet
    
    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 156, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Maps a temporal resource to a mapping between a providing CP software cluster
        # and requesting CP software atpVariation.
        self._tdCpSoftware: List["TDCpSoftwareCluster"] = []

    @property
    def td_cp_software(self) -> List["TDCpSoftwareCluster"]:
        """Get tdCpSoftware (Pythonic accessor)."""
        return self._tdCpSoftware

    def with_td_cp_software(self, value):
        """
        Set td_cp_software and return self for chaining.

        Args:
            value: The td_cp_software to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_td_cp_software("value")
        """
        self.td_cp_software = value  # Use property setter (gets validation)
        return self

    def with_requestor(self, value):
        """
        Set requestor and return self for chaining.

        Args:
            value: The requestor to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_requestor("value")
        """
        self.requestor = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTdCpSoftware(self) -> List["TDCpSoftwareCluster"]:
        """
        AUTOSAR-compliant getter for tdCpSoftware.
        
        Returns:
            The tdCpSoftware value
        
        Note:
            Delegates to td_cp_software property (CODING_RULE_V2_00017)
        """
        return self.td_cp_software  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class TDCpSoftwareClusterMapping(Identifiable):
    """
    This is used to specify a mapping between a software cluster that provides
    temporal and dynamic resources and the software clusters that need these
    resources.
    
    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingCpSoftwareCluster::TDCpSoftwareClusterMapping
    
    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 157, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is the software cluster that provides the temporal and.
        self._provider: Optional["CpSoftwareCluster"] = None

    @property
    def provider(self) -> Optional["CpSoftwareCluster"]:
        """Get provider (Pythonic accessor)."""
        return self._provider

    @provider.setter
    def provider(self, value: Optional["CpSoftwareCluster"]) -> None:
        """
        Set provider with validation.
        
        Args:
            value: The provider to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._provider = None
            return

        if not isinstance(value, CpSoftwareCluster):
            raise TypeError(
                f"provider must be CpSoftwareCluster or None, got {type(value).__name__}"
            )
        self._provider = value
        self._requestor: List["CpSoftwareCluster"] = []

    @property
    def requestor(self) -> List["CpSoftwareCluster"]:
        """Get requestor (Pythonic accessor)."""
        return self._requestor
        # The timing description representing the temporal and resource.
        self._timing: Optional["TimingDescription"] = None

    @property
    def timing(self) -> Optional["TimingDescription"]:
        """Get timing (Pythonic accessor)."""
        return self._timing

    @timing.setter
    def timing(self, value: Optional["TimingDescription"]) -> None:
        """
        Set timing with validation.
        
        Args:
            value: The timing to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timing = None
            return

        if not isinstance(value, TimingDescription):
            raise TypeError(
                f"timing must be TimingDescription or None, got {type(value).__name__}"
            )
        self._timing = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getProvider(self) -> "CpSoftwareCluster":
        """
        AUTOSAR-compliant getter for provider.
        
        Returns:
            The provider value
        
        Note:
            Delegates to provider property (CODING_RULE_V2_00017)
        """
        return self.provider  # Delegates to property

    def setProvider(self, value: "CpSoftwareCluster") -> "TDCpSoftwareClusterMapping":
        """
        AUTOSAR-compliant setter for provider with method chaining.
        
        Args:
            value: The provider to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to provider property setter (gets validation automatically)
        """
        self.provider = value  # Delegates to property setter
        return self

    def getRequestor(self) -> List["CpSoftwareCluster"]:
        """
        AUTOSAR-compliant getter for requestor.
        
        Returns:
            The requestor value
        
        Note:
            Delegates to requestor property (CODING_RULE_V2_00017)
        """
        return self.requestor  # Delegates to property

    def getTiming(self) -> "TimingDescription":
        """
        AUTOSAR-compliant getter for timing.
        
        Returns:
            The timing value
        
        Note:
            Delegates to timing property (CODING_RULE_V2_00017)
        """
        return self.timing  # Delegates to property

    def setTiming(self, value: "TimingDescription") -> "TDCpSoftwareClusterMapping":
        """
        AUTOSAR-compliant setter for timing with method chaining.
        
        Args:
            value: The timing to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to timing property setter (gets validation automatically)
        """
        self.timing = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_provider(self, value: Optional["CpSoftwareCluster"]) -> "TDCpSoftwareClusterMapping":
        """
        Set provider and return self for chaining.
        
        Args:
            value: The provider to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_provider("value")
        """
        self.provider = value  # Use property setter (gets validation)
        return self

    def with_timing(self, value: Optional["TimingDescription"]) -> "TDCpSoftwareClusterMapping":
        """
        Set timing and return self for chaining.
        
        Args:
            value: The timing to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_timing("value")
        """
        self.timing = value  # Use property setter (gets validation)
        return self



class TDCpSoftwareClusterResourceMapping(Identifiable):
    """
    This is used to assign an unequivocal global resource identification to a
    temporal and dynamic resource.
    
    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingCpSoftwareCluster::TDCpSoftwareClusterResourceMapping
    
    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 158, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The specific resource identification assigned to the and dynamic resource.
        self._resource: Optional["CpSoftwareCluster"] = None

    @property
    def resource(self) -> Optional["CpSoftwareCluster"]:
        """Get resource (Pythonic accessor)."""
        return self._resource

    @resource.setter
    def resource(self, value: Optional["CpSoftwareCluster"]) -> None:
        """
        Set resource with validation.
        
        Args:
            value: The resource to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._resource = None
            return

        if not isinstance(value, CpSoftwareCluster):
            raise TypeError(
                f"resource must be CpSoftwareCluster or None, got {type(value).__name__}"
            )
        self._resource = value
        self._timing: Optional["TimingDescription"] = None

    @property
    def timing(self) -> Optional["TimingDescription"]:
        """Get timing (Pythonic accessor)."""
        return self._timing

    @timing.setter
    def timing(self, value: Optional["TimingDescription"]) -> None:
        """
        Set timing with validation.
        
        Args:
            value: The timing to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timing = None
            return

        if not isinstance(value, TimingDescription):
            raise TypeError(
                f"timing must be TimingDescription or None, got {type(value).__name__}"
            )
        self._timing = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getResource(self) -> "CpSoftwareCluster":
        """
        AUTOSAR-compliant getter for resource.
        
        Returns:
            The resource value
        
        Note:
            Delegates to resource property (CODING_RULE_V2_00017)
        """
        return self.resource  # Delegates to property

    def setResource(self, value: "CpSoftwareCluster") -> "TDCpSoftwareClusterResourceMapping":
        """
        AUTOSAR-compliant setter for resource with method chaining.
        
        Args:
            value: The resource to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to resource property setter (gets validation automatically)
        """
        self.resource = value  # Delegates to property setter
        return self

    def getTiming(self) -> "TimingDescription":
        """
        AUTOSAR-compliant getter for timing.
        
        Returns:
            The timing value
        
        Note:
            Delegates to timing property (CODING_RULE_V2_00017)
        """
        return self.timing  # Delegates to property

    def setTiming(self, value: "TimingDescription") -> "TDCpSoftwareClusterResourceMapping":
        """
        AUTOSAR-compliant setter for timing with method chaining.
        
        Args:
            value: The timing to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to timing property setter (gets validation automatically)
        """
        self.timing = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_resource(self, value: Optional["CpSoftwareCluster"]) -> "TDCpSoftwareClusterResourceMapping":
        """
        Set resource and return self for chaining.
        
        Args:
            value: The resource to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_resource("value")
        """
        self.resource = value  # Use property setter (gets validation)
        return self

    def with_timing(self, value: Optional["TimingDescription"]) -> "TDCpSoftwareClusterResourceMapping":
        """
        Set timing and return self for chaining.
        
        Args:
            value: The timing to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_timing("value")
        """
        self.timing = value  # Use property setter (gets validation)
        return self

from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class SystemSignalGroupToCommunicationResourceMapping(Identifiable):
    """
    This meta class maps a communication resource to a SystemSignalGroup. This
    mapping can be used in an early process stage in which the DataMapping
    linking the Ports and mapped CpSoftwareCluster CommunicationResource(s) to
    SystemSignals of a SystemSignalGroup is not yet available.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::SoftwareCluster::SystemSignalGroupToCommunicationResourceMapping
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 290, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Communication resource for which the mapping applies.
        self._softwareCluster: Optional["CpSoftwareCluster"] = None

    @property
    def software_cluster(self) -> Optional["CpSoftwareCluster"]:
        """Get softwareCluster (Pythonic accessor)."""
        return self._softwareCluster

    @software_cluster.setter
    def software_cluster(self, value: Optional["CpSoftwareCluster"]) -> None:
        """
        Set softwareCluster with validation.
        
        Args:
            value: The softwareCluster to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._softwareCluster = None
            return

        if not isinstance(value, CpSoftwareCluster):
            raise TypeError(
                f"softwareCluster must be CpSoftwareCluster or None, got {type(value).__name__}"
            )
        self._softwareCluster = value
        # SystemSignalGroup to which the communication is assigned.
        self._systemSignal: RefType = None

    @property
    def system_signal(self) -> RefType:
        """Get systemSignal (Pythonic accessor)."""
        return self._systemSignal

    @system_signal.setter
    def system_signal(self, value: RefType) -> None:
        """
        Set systemSignal with validation.
        
        Args:
            value: The systemSignal to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._systemSignal = None
            return

        self._systemSignal = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSoftwareCluster(self) -> "CpSoftwareCluster":
        """
        AUTOSAR-compliant getter for softwareCluster.
        
        Returns:
            The softwareCluster value
        
        Note:
            Delegates to software_cluster property (CODING_RULE_V2_00017)
        """
        return self.software_cluster  # Delegates to property

    def setSoftwareCluster(self, value: "CpSoftwareCluster") -> "SystemSignalGroupToCommunicationResourceMapping":
        """
        AUTOSAR-compliant setter for softwareCluster with method chaining.
        
        Args:
            value: The softwareCluster to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to software_cluster property setter (gets validation automatically)
        """
        self.software_cluster = value  # Delegates to property setter
        return self

    def getSystemSignal(self) -> RefType:
        """
        AUTOSAR-compliant getter for systemSignal.
        
        Returns:
            The systemSignal value
        
        Note:
            Delegates to system_signal property (CODING_RULE_V2_00017)
        """
        return self.system_signal  # Delegates to property

    def setSystemSignal(self, value: RefType) -> "SystemSignalGroupToCommunicationResourceMapping":
        """
        AUTOSAR-compliant setter for systemSignal with method chaining.
        
        Args:
            value: The systemSignal to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to system_signal property setter (gets validation automatically)
        """
        self.system_signal = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_software_cluster(self, value: Optional["CpSoftwareCluster"]) -> "SystemSignalGroupToCommunicationResourceMapping":
        """
        Set softwareCluster and return self for chaining.
        
        Args:
            value: The softwareCluster to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_software_cluster("value")
        """
        self.software_cluster = value  # Use property setter (gets validation)
        return self

    def with_system_signal(self, value: Optional[RefType]) -> "SystemSignalGroupToCommunicationResourceMapping":
        """
        Set systemSignal and return self for chaining.
        
        Args:
            value: The systemSignal to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_system_signal("value")
        """
        self.system_signal = value  # Use property setter (gets validation)
        return self
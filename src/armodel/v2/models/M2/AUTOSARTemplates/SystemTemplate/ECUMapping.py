from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class ECUMapping(Identifiable):
    """
    ECUMapping allows to assign an ECU hardware type (defined in the ECU
    Resource Template) to an ECUInstance used in a physical topology.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::ECUResourceMapping::ECUMapping
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 182, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The ECUMapping contains the mapping of all CommunicationControllers of the
        # ECU.
        self._commController: List["Communication"] = []

    @property
    def comm_controller(self) -> List["Communication"]:
        """Get commController (Pythonic accessor)."""
        return self._commController
        # Reference to a HwElement of category ECU in the ECU.
        self._ecu: Optional["HwElement"] = None

    @property
    def ecu(self) -> Optional["HwElement"]:
        """Get ecu (Pythonic accessor)."""
        return self._ecu

    @ecu.setter
    def ecu(self, value: Optional["HwElement"]) -> None:
        """
        Set ecu with validation.
        
        Args:
            value: The ecu to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ecu = None
            return

        if not isinstance(value, HwElement):
            raise TypeError(
                f"ecu must be HwElement or None, got {type(value).__name__}"
            )
        self._ecu = value
        # Reference to the EcuInstance in the System Template.
        self._ecuInstance: Optional["EcuInstance"] = None

    @property
    def ecu_instance(self) -> Optional["EcuInstance"]:
        """Get ecuInstance (Pythonic accessor)."""
        return self._ecuInstance

    @ecu_instance.setter
    def ecu_instance(self, value: Optional["EcuInstance"]) -> None:
        """
        Set ecuInstance with validation.
        
        Args:
            value: The ecuInstance to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ecuInstance = None
            return

        if not isinstance(value, EcuInstance):
            raise TypeError(
                f"ecuInstance must be EcuInstance or None, got {type(value).__name__}"
            )
        self._ecuInstance = value
        # of the ECU.
        self._hwPortMapping: RefType = None

    @property
    def hw_port_mapping(self) -> RefType:
        """Get hwPortMapping (Pythonic accessor)."""
        return self._hwPortMapping

    @hw_port_mapping.setter
    def hw_port_mapping(self, value: RefType) -> None:
        """
        Set hwPortMapping with validation.
        
        Args:
            value: The hwPortMapping to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        self._hwPortMapping = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCommController(self) -> List["Communication"]:
        """
        AUTOSAR-compliant getter for commController.
        
        Returns:
            The commController value
        
        Note:
            Delegates to comm_controller property (CODING_RULE_V2_00017)
        """
        return self.comm_controller  # Delegates to property

    def getEcu(self) -> "HwElement":
        """
        AUTOSAR-compliant getter for ecu.
        
        Returns:
            The ecu value
        
        Note:
            Delegates to ecu property (CODING_RULE_V2_00017)
        """
        return self.ecu  # Delegates to property

    def setEcu(self, value: "HwElement") -> "ECUMapping":
        """
        AUTOSAR-compliant setter for ecu with method chaining.
        
        Args:
            value: The ecu to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to ecu property setter (gets validation automatically)
        """
        self.ecu = value  # Delegates to property setter
        return self

    def getEcuInstance(self) -> "EcuInstance":
        """
        AUTOSAR-compliant getter for ecuInstance.
        
        Returns:
            The ecuInstance value
        
        Note:
            Delegates to ecu_instance property (CODING_RULE_V2_00017)
        """
        return self.ecu_instance  # Delegates to property

    def setEcuInstance(self, value: "EcuInstance") -> "ECUMapping":
        """
        AUTOSAR-compliant setter for ecuInstance with method chaining.
        
        Args:
            value: The ecuInstance to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to ecu_instance property setter (gets validation automatically)
        """
        self.ecu_instance = value  # Delegates to property setter
        return self

    def getHwPortMapping(self) -> RefType:
        """
        AUTOSAR-compliant getter for hwPortMapping.
        
        Returns:
            The hwPortMapping value
        
        Note:
            Delegates to hw_port_mapping property (CODING_RULE_V2_00017)
        """
        return self.hw_port_mapping  # Delegates to property

    def setHwPortMapping(self, value: RefType) -> "ECUMapping":
        """
        AUTOSAR-compliant setter for hwPortMapping with method chaining.
        
        Args:
            value: The hwPortMapping to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to hw_port_mapping property setter (gets validation automatically)
        """
        self.hw_port_mapping = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_ecu(self, value: Optional["HwElement"]) -> "ECUMapping":
        """
        Set ecu and return self for chaining.
        
        Args:
            value: The ecu to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_ecu("value")
        """
        self.ecu = value  # Use property setter (gets validation)
        return self

    def with_ecu_instance(self, value: Optional["EcuInstance"]) -> "ECUMapping":
        """
        Set ecuInstance and return self for chaining.
        
        Args:
            value: The ecuInstance to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_ecu_instance("value")
        """
        self.ecu_instance = value  # Use property setter (gets validation)
        return self

    def with_hw_port_mapping(self, value: RefType) -> "ECUMapping":
        """
        Set hwPortMapping and return self for chaining.
        
        Args:
            value: The hwPortMapping to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_hw_port_mapping("value")
        """
        self.hw_port_mapping = value  # Use property setter (gets validation)
        return self
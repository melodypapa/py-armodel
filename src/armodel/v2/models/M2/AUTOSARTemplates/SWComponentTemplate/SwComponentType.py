from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class SwComponentType(ARElement, ABC):
    """
    Base class for AUTOSAR software components.
    
    Package: M2::AUTOSARTemplates::SWComponentTemplate::Components::SwComponentType
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 330, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 64, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2060, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 245, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (Page 22, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 466, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 210, Foundation R23-11)
    """
    def __init__(self):
        if type(self) is SwComponentType:
            raise TypeError("SwComponentType is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the collection of ConsistencyNeeds by the enclosing
                # SwComponentType.
        # atpVariation.
        self._consistency: List["ConsistencyNeeds"] = []

    @property
    def consistency(self) -> List["ConsistencyNeeds"]:
        """Get consistency (Pythonic accessor)."""
        return self._consistency
        # The PortPrototypes through which this SwComponent communicate.
        # of PortPrototype is subject to variability purpose to support the conditional
                # existence of atpVariation.
        self._port: List[RefType] = []

    @property
    def port(self) -> List[RefType]:
        """Get port (Pythonic accessor)."""
        return self._port
        # A port group being part of this component.
        # atpVariation.
        self._portGroup: List[RefType] = []

    @property
    def port_group(self) -> List[RefType]:
        """Get portGroup (Pythonic accessor)."""
        return self._portGroup
        # Reference to constraints that are valid for this Sw ComponentType.
        self._swcMapping: List[RefType] = []

    @property
    def swc_mapping(self) -> List[RefType]:
        """Get swcMapping (Pythonic accessor)."""
        return self._swcMapping
        # This adds a documentation to the SwComponentType.
        # Stereotypes: atpSplitable; atpVariation.
        self._swComponent: Optional["SwComponent"] = None

    @property
    def sw_component(self) -> Optional["SwComponent"]:
        """Get swComponent (Pythonic accessor)."""
        return self._swComponent

    @sw_component.setter
    def sw_component(self, value: Optional["SwComponent"]) -> None:
        """
        Set swComponent with validation.
        
        Args:
            value: The swComponent to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swComponent = None
            return

        if not isinstance(value, SwComponent):
            raise TypeError(
                f"swComponent must be SwComponent or None, got {type(value).__name__}"
            )
        self._swComponent = value
        # This allows for the specification of which UnitGroups are the context of
        # referencing SwComponentType.
        self._unitGroup: List[RefType] = []

    @property
    def unit_group(self) -> List[RefType]:
        """Get unitGroup (Pythonic accessor)."""
        return self._unitGroup

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getConsistency(self) -> List["ConsistencyNeeds"]:
        """
        AUTOSAR-compliant getter for consistency.
        
        Returns:
            The consistency value
        
        Note:
            Delegates to consistency property (CODING_RULE_V2_00017)
        """
        return self.consistency  # Delegates to property

    def getPort(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for port.
        
        Returns:
            The port value
        
        Note:
            Delegates to port property (CODING_RULE_V2_00017)
        """
        return self.port  # Delegates to property

    def getPortGroup(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for portGroup.
        
        Returns:
            The portGroup value
        
        Note:
            Delegates to port_group property (CODING_RULE_V2_00017)
        """
        return self.port_group  # Delegates to property

    def getSwcMapping(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for swcMapping.
        
        Returns:
            The swcMapping value
        
        Note:
            Delegates to swc_mapping property (CODING_RULE_V2_00017)
        """
        return self.swc_mapping  # Delegates to property

    def getSwComponent(self) -> "SwComponent":
        """
        AUTOSAR-compliant getter for swComponent.
        
        Returns:
            The swComponent value
        
        Note:
            Delegates to sw_component property (CODING_RULE_V2_00017)
        """
        return self.sw_component  # Delegates to property

    def setSwComponent(self, value: "SwComponent") -> "SwComponentType":
        """
        AUTOSAR-compliant setter for swComponent with method chaining.
        
        Args:
            value: The swComponent to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to sw_component property setter (gets validation automatically)
        """
        self.sw_component = value  # Delegates to property setter
        return self

    def getUnitGroup(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for unitGroup.
        
        Returns:
            The unitGroup value
        
        Note:
            Delegates to unit_group property (CODING_RULE_V2_00017)
        """
        return self.unit_group  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_sw_component(self, value: Optional["SwComponent"]) -> "SwComponentType":
        """
        Set swComponent and return self for chaining.
        
        Args:
            value: The swComponent to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_sw_component("value")
        """
        self.sw_component = value  # Use property setter (gets validation)
        return self
from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class FlexrayTpEcu(ARObject):
    """
    ECU specific TP configuration parameters. Each TpEcu element has a reference
    to exactly one ECUInstance in the topology.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::FlexrayTpEcu
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 596, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # With this switch Tx and Rx Cancellation can be turned on 2090 Document ID 63:
        # AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._cancellation: Optional["Boolean"] = None

    @property
    def cancellation(self) -> Optional["Boolean"]:
        """Get cancellation (Pythonic accessor)."""
        return self._cancellation

    @cancellation.setter
    def cancellation(self, value: Optional["Boolean"]) -> None:
        """
        Set cancellation with validation.
        
        Args:
            value: The cancellation to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._cancellation = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"cancellation must be Boolean or None, got {type(value).__name__}"
            )
        self._cancellation = value
        # The period between successive calls to the Main Function the AUTOSAR TP.
        # Specified in seconds.
        self._cycleTimeMain: Optional["TimeValue"] = None

    @property
    def cycle_time_main(self) -> Optional["TimeValue"]:
        """Get cycleTimeMain (Pythonic accessor)."""
        return self._cycleTimeMain

    @cycle_time_main.setter
    def cycle_time_main(self, value: Optional["TimeValue"]) -> None:
        """
        Set cycleTimeMain with validation.
        
        Args:
            value: The cycleTimeMain to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._cycleTimeMain = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"cycleTimeMain must be TimeValue or None, got {type(value).__name__}"
            )
        self._cycleTimeMain = value
        # Connection to the ECUInstance in the Topology.
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
        # The full duplex mechanisms is enabled if this attribute is to true.
        # Otherwise half duplex is enabled.
        self._fullDuplex: Optional["Boolean"] = None

    @property
    def full_duplex(self) -> Optional["Boolean"]:
        """Get fullDuplex (Pythonic accessor)."""
        return self._fullDuplex

    @full_duplex.setter
    def full_duplex(self, value: Optional["Boolean"]) -> None:
        """
        Set fullDuplex with validation.
        
        Args:
            value: The fullDuplex to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._fullDuplex = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"fullDuplex must be Boolean or None, got {type(value).__name__}"
            )
        self._fullDuplex = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCancellation(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for cancellation.
        
        Returns:
            The cancellation value
        
        Note:
            Delegates to cancellation property (CODING_RULE_V2_00017)
        """
        return self.cancellation  # Delegates to property

    def setCancellation(self, value: "Boolean") -> "FlexrayTpEcu":
        """
        AUTOSAR-compliant setter for cancellation with method chaining.
        
        Args:
            value: The cancellation to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to cancellation property setter (gets validation automatically)
        """
        self.cancellation = value  # Delegates to property setter
        return self

    def getCycleTimeMain(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for cycleTimeMain.
        
        Returns:
            The cycleTimeMain value
        
        Note:
            Delegates to cycle_time_main property (CODING_RULE_V2_00017)
        """
        return self.cycle_time_main  # Delegates to property

    def setCycleTimeMain(self, value: "TimeValue") -> "FlexrayTpEcu":
        """
        AUTOSAR-compliant setter for cycleTimeMain with method chaining.
        
        Args:
            value: The cycleTimeMain to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to cycle_time_main property setter (gets validation automatically)
        """
        self.cycle_time_main = value  # Delegates to property setter
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

    def setEcuInstance(self, value: "EcuInstance") -> "FlexrayTpEcu":
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

    def getFullDuplex(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for fullDuplex.
        
        Returns:
            The fullDuplex value
        
        Note:
            Delegates to full_duplex property (CODING_RULE_V2_00017)
        """
        return self.full_duplex  # Delegates to property

    def setFullDuplex(self, value: "Boolean") -> "FlexrayTpEcu":
        """
        AUTOSAR-compliant setter for fullDuplex with method chaining.
        
        Args:
            value: The fullDuplex to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to full_duplex property setter (gets validation automatically)
        """
        self.full_duplex = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_cancellation(self, value: Optional["Boolean"]) -> "FlexrayTpEcu":
        """
        Set cancellation and return self for chaining.
        
        Args:
            value: The cancellation to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_cancellation("value")
        """
        self.cancellation = value  # Use property setter (gets validation)
        return self

    def with_cycle_time_main(self, value: Optional["TimeValue"]) -> "FlexrayTpEcu":
        """
        Set cycleTimeMain and return self for chaining.
        
        Args:
            value: The cycleTimeMain to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_cycle_time_main("value")
        """
        self.cycle_time_main = value  # Use property setter (gets validation)
        return self

    def with_ecu_instance(self, value: Optional["EcuInstance"]) -> "FlexrayTpEcu":
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

    def with_full_duplex(self, value: Optional["Boolean"]) -> "FlexrayTpEcu":
        """
        Set fullDuplex and return self for chaining.
        
        Args:
            value: The fullDuplex to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_full_duplex("value")
        """
        self.full_duplex = value  # Use property setter (gets validation)
        return self
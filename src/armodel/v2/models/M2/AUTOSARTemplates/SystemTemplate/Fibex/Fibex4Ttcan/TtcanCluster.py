from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class TtcanCluster(ARObject):
    """
    TTCAN bus specific cluster attributes.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ttcan::TtcanTopology::TtcanCluster
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 76, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Length of a basic-cycle.
        # Unit: NTUs.
        self._basicCycleLength: Optional["Integer"] = None

    @property
    def basic_cycle_length(self) -> Optional["Integer"]:
        """Get basicCycleLength (Pythonic accessor)."""
        return self._basicCycleLength

    @basic_cycle_length.setter
    def basic_cycle_length(self, value: Optional["Integer"]) -> None:
        """
        Set basicCycleLength with validation.
        
        Args:
            value: The basicCycleLength to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._basicCycleLength = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"basicCycleLength must be Integer or None, got {type(value).__name__}"
            )
        self._basicCycleLength = value
        # Unit measuring all times and providing a constant of the For level 1, this is
        # always the CAN bit seconds.
        self._ntu: Optional["TimeValue"] = None

    @property
    def ntu(self) -> Optional["TimeValue"]:
        """Get ntu (Pythonic accessor)."""
        return self._ntu

    @ntu.setter
    def ntu(self, value: Optional["TimeValue"]) -> None:
        """
        Set ntu with validation.
        
        Args:
            value: The ntu to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ntu = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"ntu must be TimeValue or None, got {type(value).__name__}"
            )
        self._ntu = value
        # Possible operation modes.
        self._operationMode: Optional["Boolean"] = None

    @property
    def operation_mode(self) -> Optional["Boolean"]:
        """Get operationMode (Pythonic accessor)."""
        return self._operationMode

    @operation_mode.setter
    def operation_mode(self, value: Optional["Boolean"]) -> None:
        """
        Set operationMode with validation.
        
        Args:
            value: The operationMode to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._operationMode = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"operationMode must be Boolean or None, got {type(value).__name__}"
            )
        self._operationMode = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBasicCycleLength(self) -> "Integer":
        """
        AUTOSAR-compliant getter for basicCycleLength.
        
        Returns:
            The basicCycleLength value
        
        Note:
            Delegates to basic_cycle_length property (CODING_RULE_V2_00017)
        """
        return self.basic_cycle_length  # Delegates to property

    def setBasicCycleLength(self, value: "Integer") -> "TtcanCluster":
        """
        AUTOSAR-compliant setter for basicCycleLength with method chaining.
        
        Args:
            value: The basicCycleLength to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to basic_cycle_length property setter (gets validation automatically)
        """
        self.basic_cycle_length = value  # Delegates to property setter
        return self

    def getNtu(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for ntu.
        
        Returns:
            The ntu value
        
        Note:
            Delegates to ntu property (CODING_RULE_V2_00017)
        """
        return self.ntu  # Delegates to property

    def setNtu(self, value: "TimeValue") -> "TtcanCluster":
        """
        AUTOSAR-compliant setter for ntu with method chaining.
        
        Args:
            value: The ntu to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to ntu property setter (gets validation automatically)
        """
        self.ntu = value  # Delegates to property setter
        return self

    def getOperationMode(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for operationMode.
        
        Returns:
            The operationMode value
        
        Note:
            Delegates to operation_mode property (CODING_RULE_V2_00017)
        """
        return self.operation_mode  # Delegates to property

    def setOperationMode(self, value: "Boolean") -> "TtcanCluster":
        """
        AUTOSAR-compliant setter for operationMode with method chaining.
        
        Args:
            value: The operationMode to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to operation_mode property setter (gets validation automatically)
        """
        self.operation_mode = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_basic_cycle_length(self, value: Optional["Integer"]) -> "TtcanCluster":
        """
        Set basicCycleLength and return self for chaining.
        
        Args:
            value: The basicCycleLength to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_basic_cycle_length("value")
        """
        self.basic_cycle_length = value  # Use property setter (gets validation)
        return self

    def with_ntu(self, value: Optional["TimeValue"]) -> "TtcanCluster":
        """
        Set ntu and return self for chaining.
        
        Args:
            value: The ntu to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_ntu("value")
        """
        self.ntu = value  # Use property setter (gets validation)
        return self

    def with_operation_mode(self, value: Optional["Boolean"]) -> "TtcanCluster":
        """
        Set operationMode and return self for chaining.
        
        Args:
            value: The operationMode to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_operation_mode("value")
        """
        self.operation_mode = value  # Use property setter (gets validation)
        return self
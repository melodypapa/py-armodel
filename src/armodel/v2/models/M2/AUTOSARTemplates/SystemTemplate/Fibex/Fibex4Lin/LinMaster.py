from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class LinMaster(ARObject):
    """
    Describing the properties of the refering ecu as a LIN master.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Lin::LinTopology::LinMaster
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 94, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # LinSlaves that are handled by the LinMaster.
        self._linSlave: List["LinSlaveConfig"] = []

    @property
    def lin_slave(self) -> List["LinSlaveConfig"]:
        """Get linSlave (Pythonic accessor)."""
        return self._linSlave
        # Time base is mandatory for the master.
        # It is not used for Spec states: "The time_base value specifies the base in
                # the master node to generate the frame transfer time.
        # " base shall be specified AUTOSAR conform in.
        self._timeBase: Optional["TimeValue"] = None

    @property
    def time_base(self) -> Optional["TimeValue"]:
        """Get timeBase (Pythonic accessor)."""
        return self._timeBase

    @time_base.setter
    def time_base(self, value: Optional["TimeValue"]) -> None:
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

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"timeBase must be TimeValue or None, got {type(value).__name__}"
            )
        self._timeBase = value
        # The attribute timeBaseJitter is a mandatory attribute for and not used for
                # slaves.
        # Spec states: "The jitter value specifies the the maximum and minimum delay
                # base start point to the frame header sending (falling edge of BREAK signal).
        # " shall be specified AUTOSAR conform in.
        self._timeBaseJitter: Optional["TimeValue"] = None

    @property
    def time_base_jitter(self) -> Optional["TimeValue"]:
        """Get timeBaseJitter (Pythonic accessor)."""
        return self._timeBaseJitter

    @time_base_jitter.setter
    def time_base_jitter(self, value: Optional["TimeValue"]) -> None:
        """
        Set timeBaseJitter with validation.
        
        Args:
            value: The timeBaseJitter to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeBaseJitter = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"timeBaseJitter must be TimeValue or None, got {type(value).__name__}"
            )
        self._timeBaseJitter = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getLinSlave(self) -> List["LinSlaveConfig"]:
        """
        AUTOSAR-compliant getter for linSlave.
        
        Returns:
            The linSlave value
        
        Note:
            Delegates to lin_slave property (CODING_RULE_V2_00017)
        """
        return self.lin_slave  # Delegates to property

    def getTimeBase(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for timeBase.
        
        Returns:
            The timeBase value
        
        Note:
            Delegates to time_base property (CODING_RULE_V2_00017)
        """
        return self.time_base  # Delegates to property

    def setTimeBase(self, value: "TimeValue") -> "LinMaster":
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

    def getTimeBaseJitter(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for timeBaseJitter.
        
        Returns:
            The timeBaseJitter value
        
        Note:
            Delegates to time_base_jitter property (CODING_RULE_V2_00017)
        """
        return self.time_base_jitter  # Delegates to property

    def setTimeBaseJitter(self, value: "TimeValue") -> "LinMaster":
        """
        AUTOSAR-compliant setter for timeBaseJitter with method chaining.
        
        Args:
            value: The timeBaseJitter to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to time_base_jitter property setter (gets validation automatically)
        """
        self.time_base_jitter = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_time_base(self, value: Optional["TimeValue"]) -> "LinMaster":
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

    def with_time_base_jitter(self, value: Optional["TimeValue"]) -> "LinMaster":
        """
        Set timeBaseJitter and return self for chaining.
        
        Args:
            value: The timeBaseJitter to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_time_base_jitter("value")
        """
        self.time_base_jitter = value  # Use property setter (gets validation)
        return self
from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class SwitchFlowMeteringEntry(Identifiable):
    """
    Defines a Flow Metering Entry for a switch.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::EthernetTopology::SwitchFlowMeteringEntry
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 143, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines whether color-aware or color-blind mode shall be.
        self._colorMode: Optional["FlowMeteringColor"] = None

    @property
    def color_mode(self) -> Optional["FlowMeteringColor"]:
        """Get colorMode (Pythonic accessor)."""
        return self._colorMode

    @color_mode.setter
    def color_mode(self, value: Optional["FlowMeteringColor"]) -> None:
        """
        Set colorMode with validation.
        
        Args:
            value: The colorMode to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._colorMode = None
            return

        if not isinstance(value, FlowMeteringColor):
            raise TypeError(
                f"colorMode must be FlowMeteringColor or None, got {type(value).__name__}"
            )
        self._colorMode = value
        # Committed Burst Size (CBS) (accepted burst size in token bucket).
        self._committedBurst: Optional["PositiveInteger"] = None

    @property
    def committed_burst(self) -> Optional["PositiveInteger"]:
        """Get committedBurst (Pythonic accessor)."""
        return self._committedBurst

    @committed_burst.setter
    def committed_burst(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set committedBurst with validation.
        
        Args:
            value: The committedBurst to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._committedBurst = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"committedBurst must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._committedBurst = value
        # Committed Information Rate (CIR) (accepted rate in token bucket) in bits per
        # second.
        self._committed: Optional["PositiveInteger"] = None

    @property
    def committed(self) -> Optional["PositiveInteger"]:
        """Get committed (Pythonic accessor)."""
        return self._committed

    @committed.setter
    def committed(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set committed with validation.
        
        Args:
            value: The committed to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._committed = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"committed must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._committed = value
        # Coupling Flag that defines if unused "green" tokens in the are transferred to
        # the second bucket as.
        self._couplingFlag: Optional["Boolean"] = None

    @property
    def coupling_flag(self) -> Optional["Boolean"]:
        """Get couplingFlag (Pythonic accessor)."""
        return self._couplingFlag

    @coupling_flag.setter
    def coupling_flag(self, value: Optional["Boolean"]) -> None:
        """
        Set couplingFlag with validation.
        
        Args:
            value: The couplingFlag to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._couplingFlag = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"couplingFlag must be Boolean or None, got {type(value).__name__}"
            )
        self._couplingFlag = value
        # Excess burst size (EBS) (accepted burst size in yellow bucket).
        self._excessBurst: Optional["PositiveInteger"] = None

    @property
    def excess_burst(self) -> Optional["PositiveInteger"]:
        """Get excessBurst (Pythonic accessor)."""
        return self._excessBurst

    @excess_burst.setter
    def excess_burst(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set excessBurst with validation.
        
        Args:
            value: The excessBurst to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._excessBurst = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"excessBurst must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._excessBurst = value
        # Excess Information Rate (EIR) (accepted rate in yellow bucket) in bits per
        # second.
        self._excess: Optional["PositiveInteger"] = None

    @property
    def excess(self) -> Optional["PositiveInteger"]:
        """Get excess (Pythonic accessor)."""
        return self._excess

    @excess.setter
    def excess(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set excess with validation.
        
        Args:
            value: The excess to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._excess = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"excess must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._excess = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getColorMode(self) -> "FlowMeteringColor":
        """
        AUTOSAR-compliant getter for colorMode.
        
        Returns:
            The colorMode value
        
        Note:
            Delegates to color_mode property (CODING_RULE_V2_00017)
        """
        return self.color_mode  # Delegates to property

    def setColorMode(self, value: "FlowMeteringColor") -> "SwitchFlowMeteringEntry":
        """
        AUTOSAR-compliant setter for colorMode with method chaining.
        
        Args:
            value: The colorMode to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to color_mode property setter (gets validation automatically)
        """
        self.color_mode = value  # Delegates to property setter
        return self

    def getCommittedBurst(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for committedBurst.
        
        Returns:
            The committedBurst value
        
        Note:
            Delegates to committed_burst property (CODING_RULE_V2_00017)
        """
        return self.committed_burst  # Delegates to property

    def setCommittedBurst(self, value: "PositiveInteger") -> "SwitchFlowMeteringEntry":
        """
        AUTOSAR-compliant setter for committedBurst with method chaining.
        
        Args:
            value: The committedBurst to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to committed_burst property setter (gets validation automatically)
        """
        self.committed_burst = value  # Delegates to property setter
        return self

    def getCommitted(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for committed.
        
        Returns:
            The committed value
        
        Note:
            Delegates to committed property (CODING_RULE_V2_00017)
        """
        return self.committed  # Delegates to property

    def setCommitted(self, value: "PositiveInteger") -> "SwitchFlowMeteringEntry":
        """
        AUTOSAR-compliant setter for committed with method chaining.
        
        Args:
            value: The committed to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to committed property setter (gets validation automatically)
        """
        self.committed = value  # Delegates to property setter
        return self

    def getCouplingFlag(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for couplingFlag.
        
        Returns:
            The couplingFlag value
        
        Note:
            Delegates to coupling_flag property (CODING_RULE_V2_00017)
        """
        return self.coupling_flag  # Delegates to property

    def setCouplingFlag(self, value: "Boolean") -> "SwitchFlowMeteringEntry":
        """
        AUTOSAR-compliant setter for couplingFlag with method chaining.
        
        Args:
            value: The couplingFlag to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to coupling_flag property setter (gets validation automatically)
        """
        self.coupling_flag = value  # Delegates to property setter
        return self

    def getExcessBurst(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for excessBurst.
        
        Returns:
            The excessBurst value
        
        Note:
            Delegates to excess_burst property (CODING_RULE_V2_00017)
        """
        return self.excess_burst  # Delegates to property

    def setExcessBurst(self, value: "PositiveInteger") -> "SwitchFlowMeteringEntry":
        """
        AUTOSAR-compliant setter for excessBurst with method chaining.
        
        Args:
            value: The excessBurst to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to excess_burst property setter (gets validation automatically)
        """
        self.excess_burst = value  # Delegates to property setter
        return self

    def getExcess(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for excess.
        
        Returns:
            The excess value
        
        Note:
            Delegates to excess property (CODING_RULE_V2_00017)
        """
        return self.excess  # Delegates to property

    def setExcess(self, value: "PositiveInteger") -> "SwitchFlowMeteringEntry":
        """
        AUTOSAR-compliant setter for excess with method chaining.
        
        Args:
            value: The excess to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to excess property setter (gets validation automatically)
        """
        self.excess = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_color_mode(self, value: Optional["FlowMeteringColor"]) -> "SwitchFlowMeteringEntry":
        """
        Set colorMode and return self for chaining.
        
        Args:
            value: The colorMode to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_color_mode("value")
        """
        self.color_mode = value  # Use property setter (gets validation)
        return self

    def with_committed_burst(self, value: Optional["PositiveInteger"]) -> "SwitchFlowMeteringEntry":
        """
        Set committedBurst and return self for chaining.
        
        Args:
            value: The committedBurst to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_committed_burst("value")
        """
        self.committed_burst = value  # Use property setter (gets validation)
        return self

    def with_committed(self, value: Optional["PositiveInteger"]) -> "SwitchFlowMeteringEntry":
        """
        Set committed and return self for chaining.
        
        Args:
            value: The committed to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_committed("value")
        """
        self.committed = value  # Use property setter (gets validation)
        return self

    def with_coupling_flag(self, value: Optional["Boolean"]) -> "SwitchFlowMeteringEntry":
        """
        Set couplingFlag and return self for chaining.
        
        Args:
            value: The couplingFlag to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_coupling_flag("value")
        """
        self.coupling_flag = value  # Use property setter (gets validation)
        return self

    def with_excess_burst(self, value: Optional["PositiveInteger"]) -> "SwitchFlowMeteringEntry":
        """
        Set excessBurst and return self for chaining.
        
        Args:
            value: The excessBurst to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_excess_burst("value")
        """
        self.excess_burst = value  # Use property setter (gets validation)
        return self

    def with_excess(self, value: Optional["PositiveInteger"]) -> "SwitchFlowMeteringEntry":
        """
        Set excess and return self for chaining.
        
        Args:
            value: The excess to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_excess("value")
        """
        self.excess = value  # Use property setter (gets validation)
        return self
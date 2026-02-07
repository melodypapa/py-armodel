from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class ISignalTriggering(Identifiable):
    """
    A ISignalTriggering allows an assignment of ISignals to physical channels.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::ISignalTriggering
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 330, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 229, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference shall be used if an ISignal is transported PhysicalChannel.
        # This reference forms an XOR the ISignalTriggering-ISignalGroup.
        self._iSignal: Optional["ISignal"] = None

    @property
    def i_signal(self) -> Optional["ISignal"]:
        """Get iSignal (Pythonic accessor)."""
        return self._iSignal

    @i_signal.setter
    def i_signal(self, value: Optional["ISignal"]) -> None:
        """
        Set iSignal with validation.
        
        Args:
            value: The iSignal to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._iSignal = None
            return

        if not isinstance(value, ISignal):
            raise TypeError(
                f"iSignal must be ISignal or None, got {type(value).__name__}"
            )
        self._iSignal = value
        # This reference shall be used if an ISignalGroup is the PhysicalChannel.
        # This reference XOR relationship with the ISignal.
        self._iSignalGroup: RefType = None

    @property
    def i_signal_group(self) -> RefType:
        """Get iSignalGroup (Pythonic accessor)."""
        return self._iSignalGroup

    @i_signal_group.setter
    def i_signal_group(self, value: RefType) -> None:
        """
        Set iSignalGroup with validation.
        
        Args:
            value: The iSignalGroup to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._iSignalGroup = None
            return

        self._iSignalGroup = value
        # References to the ISignalPort on every ECU of the sends and/or receives the
                # ISignal.
        # both the sender and the receiver side included when the system is completely
                # defined.
        self._iSignalPort: List["ISignalPort"] = []

    @property
    def i_signal_port(self) -> List["ISignalPort"]:
        """Get iSignalPort (Pythonic accessor)."""
        return self._iSignalPort

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getISignal(self) -> "ISignal":
        """
        AUTOSAR-compliant getter for iSignal.
        
        Returns:
            The iSignal value
        
        Note:
            Delegates to i_signal property (CODING_RULE_V2_00017)
        """
        return self.i_signal  # Delegates to property

    def setISignal(self, value: "ISignal") -> "ISignalTriggering":
        """
        AUTOSAR-compliant setter for iSignal with method chaining.
        
        Args:
            value: The iSignal to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to i_signal property setter (gets validation automatically)
        """
        self.i_signal = value  # Delegates to property setter
        return self

    def getISignalGroup(self) -> RefType:
        """
        AUTOSAR-compliant getter for iSignalGroup.
        
        Returns:
            The iSignalGroup value
        
        Note:
            Delegates to i_signal_group property (CODING_RULE_V2_00017)
        """
        return self.i_signal_group  # Delegates to property

    def setISignalGroup(self, value: RefType) -> "ISignalTriggering":
        """
        AUTOSAR-compliant setter for iSignalGroup with method chaining.
        
        Args:
            value: The iSignalGroup to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to i_signal_group property setter (gets validation automatically)
        """
        self.i_signal_group = value  # Delegates to property setter
        return self

    def getISignalPort(self) -> List["ISignalPort"]:
        """
        AUTOSAR-compliant getter for iSignalPort.
        
        Returns:
            The iSignalPort value
        
        Note:
            Delegates to i_signal_port property (CODING_RULE_V2_00017)
        """
        return self.i_signal_port  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_i_signal(self, value: Optional["ISignal"]) -> "ISignalTriggering":
        """
        Set iSignal and return self for chaining.
        
        Args:
            value: The iSignal to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_i_signal("value")
        """
        self.i_signal = value  # Use property setter (gets validation)
        return self

    def with_i_signal_group(self, value: Optional[RefType]) -> "ISignalTriggering":
        """
        Set iSignalGroup and return self for chaining.
        
        Args:
            value: The iSignalGroup to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_i_signal_group("value")
        """
        self.i_signal_group = value  # Use property setter (gets validation)
        return self
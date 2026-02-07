from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class DiagnosticJ1939SpnMapping(DiagnosticMapping):
    """
    This meta-class represents the ability to define a mapping between an SPN
    and a SystemSignal. The existence of a mapping means that neither the SPN
    nor the SystemSignal need to be updated if the relation between the two
    changes.
    
    Package: M2::AUTOSARTemplates::DiagnosticExtract::DiagnosticMapping::DiagnosticJ1939Mapping::DiagnosticJ1939SpnMapping
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 267, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This additional reference has a supporting role in that it sending nodes of a
                # given SPN.
        # It is positively a given SPN is sent by more than one node.
        # the reference targets the Diagnostic semantics of the reference is bound to
                # that is in turn referenced by the.
        self._sendingNode: List["DiagnosticJ1939Node"] = []

    @property
    def sending_node(self) -> List["DiagnosticJ1939Node"]:
        """Get sendingNode (Pythonic accessor)."""
        return self._sendingNode
        # This reference goes to the SPN that shall be associated SystemSignal.
        self._spn: Optional["DiagnosticJ1939Spn"] = None

    @property
    def spn(self) -> Optional["DiagnosticJ1939Spn"]:
        """Get spn (Pythonic accessor)."""
        return self._spn

    @spn.setter
    def spn(self, value: Optional["DiagnosticJ1939Spn"]) -> None:
        """
        Set spn with validation.
        
        Args:
            value: The spn to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._spn = None
            return

        if not isinstance(value, DiagnosticJ1939Spn):
            raise TypeError(
                f"spn must be DiagnosticJ1939Spn or None, got {type(value).__name__}"
            )
        self._spn = value
        # This reference goes to the SystemSignal that shall be an SPN.
        self._systemSignal: Optional["SystemSignal"] = None

    @property
    def system_signal(self) -> Optional["SystemSignal"]:
        """Get systemSignal (Pythonic accessor)."""
        return self._systemSignal

    @system_signal.setter
    def system_signal(self, value: Optional["SystemSignal"]) -> None:
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

        if not isinstance(value, SystemSignal):
            raise TypeError(
                f"systemSignal must be SystemSignal or None, got {type(value).__name__}"
            )
        self._systemSignal = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSendingNode(self) -> List["DiagnosticJ1939Node"]:
        """
        AUTOSAR-compliant getter for sendingNode.
        
        Returns:
            The sendingNode value
        
        Note:
            Delegates to sending_node property (CODING_RULE_V2_00017)
        """
        return self.sending_node  # Delegates to property

    def getSpn(self) -> "DiagnosticJ1939Spn":
        """
        AUTOSAR-compliant getter for spn.
        
        Returns:
            The spn value
        
        Note:
            Delegates to spn property (CODING_RULE_V2_00017)
        """
        return self.spn  # Delegates to property

    def setSpn(self, value: "DiagnosticJ1939Spn") -> "DiagnosticJ1939SpnMapping":
        """
        AUTOSAR-compliant setter for spn with method chaining.
        
        Args:
            value: The spn to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to spn property setter (gets validation automatically)
        """
        self.spn = value  # Delegates to property setter
        return self

    def getSystemSignal(self) -> "SystemSignal":
        """
        AUTOSAR-compliant getter for systemSignal.
        
        Returns:
            The systemSignal value
        
        Note:
            Delegates to system_signal property (CODING_RULE_V2_00017)
        """
        return self.system_signal  # Delegates to property

    def setSystemSignal(self, value: "SystemSignal") -> "DiagnosticJ1939SpnMapping":
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

    def with_spn(self, value: Optional["DiagnosticJ1939Spn"]) -> "DiagnosticJ1939SpnMapping":
        """
        Set spn and return self for chaining.
        
        Args:
            value: The spn to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_spn("value")
        """
        self.spn = value  # Use property setter (gets validation)
        return self

    def with_system_signal(self, value: Optional["SystemSignal"]) -> "DiagnosticJ1939SpnMapping":
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
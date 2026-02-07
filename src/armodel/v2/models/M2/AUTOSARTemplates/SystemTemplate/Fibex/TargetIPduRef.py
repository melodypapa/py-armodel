from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class TargetIPduRef(ARObject):
    """
    Target destination of the referencing mapping.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Multiplatform::TargetIPduRef
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 841, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # If no I-Pdu has been received a default value will be.
        self._defaultValue: RefType = None

    @property
    def default_value(self) -> RefType:
        """Get defaultValue (Pythonic accessor)."""
        return self._defaultValue

    @default_value.setter
    def default_value(self, value: RefType) -> None:
        """
        Set defaultValue with validation.
        
        Args:
            value: The defaultValue to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._defaultValue = None
            return

        self._defaultValue = value
        # IPdu Reference.
        self._targetIPdu: RefType = None

    @property
    def target_i_pdu(self) -> RefType:
        """Get targetIPdu (Pythonic accessor)."""
        return self._targetIPdu

    @target_i_pdu.setter
    def target_i_pdu(self, value: RefType) -> None:
        """
        Set targetIPdu with validation.
        
        Args:
            value: The targetIPdu to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._targetIPdu = None
            return

        self._targetIPdu = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDefaultValue(self) -> RefType:
        """
        AUTOSAR-compliant getter for defaultValue.
        
        Returns:
            The defaultValue value
        
        Note:
            Delegates to default_value property (CODING_RULE_V2_00017)
        """
        return self.default_value  # Delegates to property

    def setDefaultValue(self, value: RefType) -> "TargetIPduRef":
        """
        AUTOSAR-compliant setter for defaultValue with method chaining.
        
        Args:
            value: The defaultValue to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to default_value property setter (gets validation automatically)
        """
        self.default_value = value  # Delegates to property setter
        return self

    def getTargetIPdu(self) -> RefType:
        """
        AUTOSAR-compliant getter for targetIPdu.
        
        Returns:
            The targetIPdu value
        
        Note:
            Delegates to target_i_pdu property (CODING_RULE_V2_00017)
        """
        return self.target_i_pdu  # Delegates to property

    def setTargetIPdu(self, value: RefType) -> "TargetIPduRef":
        """
        AUTOSAR-compliant setter for targetIPdu with method chaining.
        
        Args:
            value: The targetIPdu to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to target_i_pdu property setter (gets validation automatically)
        """
        self.target_i_pdu = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_default_value(self, value: Optional[RefType]) -> "TargetIPduRef":
        """
        Set defaultValue and return self for chaining.
        
        Args:
            value: The defaultValue to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_default_value("value")
        """
        self.default_value = value  # Use property setter (gets validation)
        return self

    def with_target_i_pdu(self, value: Optional[RefType]) -> "TargetIPduRef":
        """
        Set targetIPdu and return self for chaining.
        
        Args:
            value: The targetIPdu to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_target_i_pdu("value")
        """
        self.target_i_pdu = value  # Use property setter (gets validation)
        return self
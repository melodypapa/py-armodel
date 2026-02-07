from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class InvalidationPolicy(ARObject):
    """
    Specifies whether the component can actively invalidate a particular
    dataElement. If no invalidationPolicy points to a dataElement this is
    considered to yield the identical result as if the handleInvalid attribute
    was set to dontInvalidate.
    
    Package: M2::AUTOSARTemplates::SWComponentTemplate::PortInterface::InvalidationPolicy
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 97, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to the dataElement for which the Invalidation.
        self._dataElement: RefType = None

    @property
    def data_element(self) -> RefType:
        """Get dataElement (Pythonic accessor)."""
        return self._dataElement

    @data_element.setter
    def data_element(self, value: RefType) -> None:
        """
        Set dataElement with validation.
        
        Args:
            value: The dataElement to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dataElement = None
            return

        self._dataElement = value
        # This attribute controls how invalidation is applied to the.
        self._handleInvalid: Optional["HandleInvalidEnum"] = None

    @property
    def handle_invalid(self) -> Optional["HandleInvalidEnum"]:
        """Get handleInvalid (Pythonic accessor)."""
        return self._handleInvalid

    @handle_invalid.setter
    def handle_invalid(self, value: Optional["HandleInvalidEnum"]) -> None:
        """
        Set handleInvalid with validation.
        
        Args:
            value: The handleInvalid to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._handleInvalid = None
            return

        if not isinstance(value, HandleInvalidEnum):
            raise TypeError(
                f"handleInvalid must be HandleInvalidEnum or None, got {type(value).__name__}"
            )
        self._handleInvalid = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDataElement(self) -> RefType:
        """
        AUTOSAR-compliant getter for dataElement.
        
        Returns:
            The dataElement value
        
        Note:
            Delegates to data_element property (CODING_RULE_V2_00017)
        """
        return self.data_element  # Delegates to property

    def setDataElement(self, value: RefType) -> "InvalidationPolicy":
        """
        AUTOSAR-compliant setter for dataElement with method chaining.
        
        Args:
            value: The dataElement to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to data_element property setter (gets validation automatically)
        """
        self.data_element = value  # Delegates to property setter
        return self

    def getHandleInvalid(self) -> "HandleInvalidEnum":
        """
        AUTOSAR-compliant getter for handleInvalid.
        
        Returns:
            The handleInvalid value
        
        Note:
            Delegates to handle_invalid property (CODING_RULE_V2_00017)
        """
        return self.handle_invalid  # Delegates to property

    def setHandleInvalid(self, value: "HandleInvalidEnum") -> "InvalidationPolicy":
        """
        AUTOSAR-compliant setter for handleInvalid with method chaining.
        
        Args:
            value: The handleInvalid to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to handle_invalid property setter (gets validation automatically)
        """
        self.handle_invalid = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_data_element(self, value: Optional[RefType]) -> "InvalidationPolicy":
        """
        Set dataElement and return self for chaining.
        
        Args:
            value: The dataElement to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_data_element("value")
        """
        self.data_element = value  # Use property setter (gets validation)
        return self

    def with_handle_invalid(self, value: Optional["HandleInvalidEnum"]) -> "InvalidationPolicy":
        """
        Set handleInvalid and return self for chaining.
        
        Args:
            value: The handleInvalid to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_handle_invalid("value")
        """
        self.handle_invalid = value  # Use property setter (gets validation)
        return self
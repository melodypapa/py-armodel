"""
AUTOSAR Package - ArObject

Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::ArObject

Manually maintained: Extended attributes support (CODING_RULE_V2_00014)
"""

from abc import ABC
from typing import Any, Dict, Optional


# Manually maintained: Base class marker to prevent regeneration
class ARType_ManuallyMaintained:  # Marker class to prevent regeneration
    pass




class ARObject(ABC):
    """
    Implicit base class of all classes in meta-model. Base
    
    Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::ArObject::ARObject
    
    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 191, Foundation
      R23-11)
    """
    def __init__(self):
        if type(self) is ARObject:
            raise TypeError("ARObject is an abstract class.")
        super().__init__()

        # Extended attributes for custom properties (CODING_RULE_V2_00014)
        self._extended_attributes: Dict[str, Any] = {}

    def getTagName(self) -> str:
        """
        Get the XML tag name for this element.
        
        Returns:
            The tag name (class name by default)
        """
        return self.__class__.__name__

    # ===== Extended attributes methods (CODING_RULE_V2_00014) =====
    def setExtendedAttribute(self, key: str, value: Any) -> None:
        """Set a custom extended attribute."""
        self._extended_attributes[key] = value

    def getExtendedAttribute(self, key: str) -> Any:
        """Get a custom extended attribute."""
        return self._extended_attributes.get(key)

    def getExtendedAttributes(self) -> Dict[str, Any]:
        """Get all extended attributes."""
        return self._extended_attributes

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Checksum calculated by the user’s tool environment for May be used in an own
                # tool environment to an ArObject has changed.
        # The checksum semantic meaning for an AUTOSAR model and no requirement for
                # AUTOSAR tools to manage.
        self._checksum: Optional["String"] = None

    @property
    def checksum(self) -> Optional["String"]:
        """Get checksum (Pythonic accessor)."""
        return self._checksum

    @checksum.setter
    def checksum(self, value: Optional["String"]) -> None:
        """
        Set checksum with validation.
        
        Args:
            value: The checksum to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._checksum = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"checksum must be String or None, got {type(value).__name__}"
            )
        self._checksum = value
        # Timestamp calculated by the user’s tool environment for May be used in an own
                # tool environment to last change of an ArObject.
        # The timestamp semantic meaning for an AUTOSAR model and no requirement for
                # AUTOSAR tools to manage.
        self._timestamp: Optional["DateTime"] = None

    @property
    def timestamp(self) -> Optional["DateTime"]:
        """Get timestamp (Pythonic accessor)."""
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value: Optional["DateTime"]) -> None:
        """
        Set timestamp with validation.
        
        Args:
            value: The timestamp to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timestamp = None
            return

        if not isinstance(value, DateTime):
            raise TypeError(
                f"timestamp must be DateTime or None, got {type(value).__name__}"
            )
        self._timestamp = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getChecksum(self) -> "String":
        """
        AUTOSAR-compliant getter for checksum.
        
        Returns:
            The checksum value
        
        Note:
            Delegates to checksum property (CODING_RULE_V2_00017)
        """
        return self.checksum  # Delegates to property

    def setChecksum(self, value: "String") -> "ARObject":
        """
        AUTOSAR-compliant setter for checksum with method chaining.
        
        Args:
            value: The checksum to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to checksum property setter (gets validation automatically)
        """
        self.checksum = value  # Delegates to property setter
        return self

    def getTimestamp(self) -> "DateTime":
        """
        AUTOSAR-compliant getter for timestamp.
        
        Returns:
            The timestamp value
        
        Note:
            Delegates to timestamp property (CODING_RULE_V2_00017)
        """
        return self.timestamp  # Delegates to property

    def setTimestamp(self, value: "DateTime") -> "ARObject":
        """
        AUTOSAR-compliant setter for timestamp with method chaining.
        
        Args:
            value: The timestamp to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to timestamp property setter (gets validation automatically)
        """
        self.timestamp = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_checksum(self, value: Optional["String"]) -> "ARObject":
        """
        Set checksum and return self for chaining.
        
        Args:
            value: The checksum to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_checksum("value")
        """
        self.checksum = value  # Use property setter (gets validation)
        return self

    def with_timestamp(self, value: Optional["DateTime"]) -> "ARObject":
        """
        Set timestamp and return self for chaining.
        
        Args:
            value: The timestamp to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_timestamp("value")
        """
        self.timestamp = value  # Use property setter (gets validation)
        return self

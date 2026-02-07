"""
Base ARObject class for V2 models.

V2 Implementation:
- Extensible design for V2 modules (CODING_RULE_V2_00014)
- Abstract base class with proper @abstractmethod decorator
- Extended attributes for custom V2 module properties
- Modern Python patterns with type hints
"""
from abc import ABC
from typing import Any, Dict, Optional


class ARObject(ABC):
    """
    Base class for all AUTOSAR objects - extensible for V2 modules.

    This class provides extension points for other V2 modules to add
    custom functionality without modifying the base class.

    Extension Points:
    - _extended_attributes: Dict for custom properties
    - getTagName(): Can be overridden for custom XML tags
    - Template methods for pre/post processing hooks
    """

    def __init__(self) -> None:
        """
        Initialize ARObject with extensible attributes.

        Raises:
            TypeError: If instantiated directly (abstract class).
        """
        if type(self) is ARObject:
            raise TypeError("ARObject is an abstract class.")

        # Core attributes (V1 compatible)
        self.parent: Optional["ARObject"] = None
        self.uuid: Optional[str] = None

        # Extensible attributes dict for custom V2 module properties
        # Allows V2 modules to add properties without modifying base class
        self._extended_attributes: Dict[str, Any] = {}

    def getTagName(self) -> str:
        """
        Get the XML tag name for this object.

        Can be overridden by subclasses for custom XML tag names.

        Returns:
            XML tag name as string (defaults to class name).
        """
        return self.__class__.__name__

    def getExtendedAttribute(self, key: str) -> Any:
        """
        Get extended attribute for custom V2 module properties.

        This allows V2 modules to store custom data without modifying
        the base class.

        Args:
            key: Attribute key name.

        Returns:
            Attribute value or None if not found.
        """
        return self._extended_attributes.get(key)

    def setExtendedAttribute(self, key: str, value: Any) -> None:
        """
        Set extended attribute for custom V2 module properties.

        This allows V2 modules to store custom data without modifying
        the base class.

        Args:
            key: Attribute key name.
            value: Attribute value.
        """
        self._extended_attributes[key] = value


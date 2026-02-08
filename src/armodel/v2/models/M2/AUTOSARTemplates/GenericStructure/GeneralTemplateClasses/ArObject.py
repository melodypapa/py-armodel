"""
Base ARObject class for V2 models.

V2 Implementation:
- Extensible design for V2 modules (CODING_RULE_V2_00014)
- Abstract base class with proper @abstractmethod decorator
- Extended attributes for custom V2 module properties
- AUTOSAR M2 properties (checksum, timestamp)
- Modern Python patterns with type hints
"""
from abc import (
    ABC,
    abstractmethod,
)
from typing import (
    Any,
    Dict,
    Optional,
)


class ARObject(ABC):
    """
    Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::ArObject
    Base class for all AUTOSAR objects - extensible for V2 modules.

    This class provides extension points for other V2 modules to add
    custom functionality without modifying the base class.

    Extension Points:
    - _extended_attributes: Dict for custom properties
    - getTagName(): Can be overridden for custom XML tags
    - Template methods for pre/post processing hooks
    - AUTOSAR M2 properties (checksum, timestamp)

    AUTOSAR M2 Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 191, Foundation R23-11)
    """

    @abstractmethod
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

        # AUTOSAR M2 attributes
        # Checksum calculated by the user's tool environment
        self._checksum: Optional[str] = None

        # Timestamp calculated by the user's tool environment
        self._timestamp: Optional[str] = None

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

    # ===== AUTOSAR M2 Properties (CODING_RULE_V2_00016) =====

    @property
    def checksum(self) -> Optional[str]:
        """
        Get checksum (Pythonic accessor).

        Checksum calculated by the user's tool environment.
        May be used in another tool environment to check if an ARObject has changed.
        """
        return self._checksum

    @checksum.setter
    def checksum(self, value: Optional[str]) -> None:
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

        if not isinstance(value, str):
            raise TypeError(
                f"checksum must be str or None, got {type(value).__name__}"
            )
        self._checksum = value

    @property
    def timestamp(self) -> Optional[str]:
        """
        Get timestamp (Pythonic accessor).

        Timestamp calculated by the user's tool environment for last change of an ARObject.
        The timestamp semantic meaning is defined by the AUTOSAR model.
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value: Optional[str]) -> None:
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

        if not isinstance(value, str):
            raise TypeError(
                f"timestamp must be str or None, got {type(value).__name__}"
            )
        self._timestamp = value

    # ===== AUTOSAR-compatible methods (CODING_RULE_V2_00017) =====

    def getChecksum(self) -> str:
        """
        AUTOSAR-compliant getter for checksum.

        Returns:
            The checksum value

        Note:
            Delegates to checksum property (CODING_RULE_V2_00017)
        """
        return self.checksum

    def setChecksum(self, value: str) -> "ARObject":
        """
        AUTOSAR-compliant setter for checksum with method chaining.

        Args:
            value: The checksum to set

        Returns:
            self for method chaining

        Note:
            Delegates to checksum property setter (gets validation automatically)
        """
        self.checksum = value
        return self

    def getTimestamp(self) -> str:
        """
        AUTOSAR-compliant getter for timestamp.

        Returns:
            The timestamp value

        Note:
            Delegates to timestamp property (CODING_RULE_V2_00017)
        """
        return self.timestamp

    def setTimestamp(self, value: str) -> "ARObject":
        """
        AUTOSAR-compliant setter for timestamp with method chaining.

        Args:
            value: The timestamp to set

        Returns:
            self for method chaining

        Note:
            Delegates to timestamp property setter (gets validation automatically)
        """
        self.timestamp = value
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_checksum(self, value: Optional[str]) -> "ARObject":
        """
        Set checksum and return self for chaining.

        Args:
            value: The checksum to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_checksum("value")
        """
        self.checksum = value
        return self

    def with_timestamp(self, value: Optional[str]) -> "ARObject":
        """
        Set timestamp and return self for chaining.

        Args:
            value: The timestamp to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_timestamp("value")
        """
        self.timestamp = value
        return self


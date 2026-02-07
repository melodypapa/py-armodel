"""
Context classes for V2 ARXML reader/writer demo.
"""
import logging
from typing import Dict, List, Optional
from pathlib import Path


class DeserializationContext:
    """
    Context for deserialization with V1-compatible error handling.
    """

    def __init__(self, version: str, warning: bool = False,
                 schema_mappings: Dict = None, file_path: Path = None):
        """
        Args:
            version: AUTOSAR version
            warning: If True, log errors instead of raising (V1 compatible)
            schema_mappings: Schema mappings
            file_path: File being read
        """
        self.version = version
        self.warning = warning
        self.mappings = schema_mappings or {}
        self.file_path = file_path
        self._current_path: List[str] = []

        # Setup logger for warning mode
        self.logger = logging.getLogger(__name__)

    def raise_or_log(self, message: str, line_number: Optional[int] = None) -> None:
        """
        Raise exception or log warning based on mode.

        Args:
            message: Error message
            line_number: Line number in XML file

        Raises:
            ReadError: If warning mode is disabled (default)
        """
        if self.warning:
            # Log warning, don't raise
            self.logger.warning(
                "%s: %s",
                self._format_location(line_number),
                message
            )
        else:
            # Raise exception (default, V1 compatible)
            from .errors import ReadError
            raise ReadError(
                message=message,
                element_path=self.get_path(),
                line_number=line_number,
                file_path=self.file_path
            )

    def _format_location(self, line_number: Optional[int]) -> str:
        """Format location string for logging."""
        parts = []
        if self.file_path:
            parts.append(str(self.file_path))
        if line_number:
            parts.append(f"line {line_number}")
        if self._current_path:
            parts.append(self.get_path())

        return " > ".join(parts) if parts else "unknown"

    def push_element(self, tag_name: str) -> None:
        """Track current element path."""
        self._current_path.append(tag_name)

    def pop_element(self) -> None:
        """Pop element from path."""
        self._current_path.pop()

    def get_path(self) -> str:
        """Get current element path string."""
        return "/".join(self._current_path)

    def get_class_for_element(self, tag_name: str) -> Optional[type]:
        """Map XML tag name to model class."""
        return self.mappings.get("tag_to_class", {}).get(tag_name)

    def map_attribute_to_field(self, cls: type, attr_name: str) -> str:
        """Map XML attribute name to Python field name."""
        class_mappings = self.mappings.get("attribute_mappings", {}).get(cls.__name__, {})
        return class_mappings.get(attr_name, attr_name.lower())


class SerializationContext:
    """
    Context for serialization.
    """

    def __init__(self, version: str, schema_mappings: Dict):
        self.version = version
        self.mappings = schema_mappings

    def get_element_tag(self, class_name: str) -> str:
        """Get XML tag name for Python class."""
        return self.mappings.get("element_names", {}).get(class_name, class_name)

    def get_child_tag(self, class_name: str, field_name: str) -> str:
        """Get XML child tag for Python field."""
        class_children = self.mappings.get("child_elements", {}).get(class_name, {})
        return class_children.get(field_name, field_name.upper().replace("_", "-"))

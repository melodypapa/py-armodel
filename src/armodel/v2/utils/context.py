"""
Context classes for V2 ARXML reader/writer.
"""
import logging
from pathlib import Path
from typing import (
    Dict,
    List,
    Optional,
)


class DeserializationContext:
    """Context for deserialization with V1-compatible error handling."""

    def __init__(self, version: str, warning: bool = False,
                 schema_mappings: Optional[Dict] = None, file_path: Optional[Path] = None) -> None:
        self.version = version
        self.warning = warning
        self.mappings = schema_mappings or {}
        self.file_path = file_path
        self._current_path: List[str] = []
        self.logger = logging.getLogger(__name__)

    def raise_or_log(self, message: str, line_number: Optional[int] = None) -> None:
        """Raise exception or log warning based on mode."""
        if self.warning:
            self.logger.warning("%s: %s", self._format_location(line_number), message)
        else:
            from armodel.v2.utils.errors import ReadError
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

    def map_attribute_to_field(self, model_class: type, attr_name: str) -> str:
        """Map XML attribute name to model class field name.

        Args:
            model_class: The model class
            attr_name: The XML attribute name (kebab-case)

        Returns:
            The field name in snake_case
        """
        # Convert kebab-case to snake_case
        # XML attributes use kebab-case (e.g., "some-attr")
        # Python fields use snake_case (e.g., "some_attr")
        return attr_name.lower().replace("-", "_")

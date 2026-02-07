"""
V2 ARXML reader demo - deserializes ARXML to model objects using reflection.
"""
import xml.etree.ElementTree as ET
from typing import Dict, Any, Optional
from pathlib import Path

from ..models.models import AUTOSAR
from ..utils.context import DeserializationContext
from .schema_registry import SchemaRegistry
from .element_handler import ElementHandler
from ..utils.errors import ReadError


class ARXMLReader:
    """
    V2 ARXML reader - deserializes ARXML using reflection.
    """

    def __init__(self, options: Optional[Dict[str, Any]] = None):
        """
        Initialize reader.

        Args:
            options: Optional configuration dict
                - warning: bool (default: False) - If True, log errors instead of raising
        """
        self.options = options or {}
        self.warning = self.options.get("warning", False)

    def load(self, file_path: str, document: AUTOSAR) -> None:
        """
        Load ARXML file into AUTOSAR document.

        Args:
            file_path: Path to ARXML file
            document: AUTOSAR document to populate

        Raises:
            ReadError: If error during reading (unless warning=True)
        """
        file_path = Path(file_path)

        # Parse XML with ElementTree
        tree = ET.parse(file_path)
        root = tree.getroot()

        # Detect AUTOSAR version (default to 3.2.3 for demo)
        version = "3.2.3"

        # Create deserialization context
        ctx = DeserializationContext(
            version=version,
            warning=self.warning,
            schema_mappings=SchemaRegistry.get_mappings(version),
            file_path=file_path
        )

        # Deserialize root element
        root_obj = self._deserialize_element(root, None, ctx)

        # Update document
        if isinstance(root_obj, AUTOSAR):
            document.ar_packages = root_obj.ar_packages
        else:
            raise ReadError(f"Root element must be AUTOSAR, got {type(root_obj).__name__}")

    def _deserialize_element(self, elem: ET.Element, parent_obj: Any,
                            ctx: DeserializationContext) -> Any:
        """
        Deserialize XML element to model object using reflection.

        Args:
            elem: XML element to deserialize
            parent_obj: Parent model object
            ctx: Deserialization context

        Returns:
            Deserialized model instance
        """
        # Strip namespace from tag name
        tag_name = self._strip_namespace(elem.tag)

        ctx.push_element(tag_name)
        try:
            # Get model class for this tag
            model_class = ElementHandler.get_class(tag_name, ctx.version)

            # Handle container elements (not model classes, just wrappers)
            if model_class is None:
                # Check if this is a known container element
                if tag_name in ["AR-PACKAGES", "ELEMENTS"]:
                    # Process children and add them directly to parent
                    for child_elem in elem:
                        child_obj = self._deserialize_element(child_elem, parent_obj, ctx)
                        if child_obj is not None:
                            # Add child to parent directly
                            self._add_child_to_parent(parent_obj, child_obj, child_elem, ctx)
                    # Return None to indicate this was a container
                    return None

                # Check if this is a simple text element (SHORT-NAME, CATEGORY, etc.)
                if tag_name in ["SHORT-NAME", "CATEGORY", "LONG-NAME", "DESC"]:
                    # This is handled by extracting text from the element
                    # The parent object should have been notified through the schema mapping
                    # For now, we'll skip these as they're handled via child element mapping
                    return None

                # Unknown element
                ctx.raise_or_log(
                    f"Unknown XML element '{tag_name}'",
                    line_number=None
                )
                return None

            # Create instance
            instance = model_class()

            # Set parent reference
            if parent_obj is not None:
                instance.parent = parent_obj

            # Extract text content for simple elements
            if elem.text and elem.text.strip():
                if hasattr(instance, 'short_name') and instance.short_name is None:
                    instance.short_name = elem.text.strip()

            # Set attributes from XML
            for attr_name, attr_value in elem.items():
                field_name = ctx.map_attribute_to_field(model_class, attr_name)
                if hasattr(instance, field_name):
                    setattr(instance, field_name, attr_value)

            # Deserialize child elements
            for child_elem in elem:
                child_tag = self._strip_namespace(child_elem.tag)

                # Handle simple text elements directly
                if child_tag in ["SHORT-NAME", "CATEGORY", "LONG-NAME", "DESC"]:
                    field_map = {
                        "SHORT-NAME": "short_name",
                        "CATEGORY": "category",
                        "LONG-NAME": "long_name",
                        "DESC": "desc"
                    }
                    field_name = field_map.get(child_tag)

                    if field_name and hasattr(instance, field_name):
                        if child_elem.text and child_elem.text.strip():
                            setattr(instance, field_name, child_elem.text.strip())
                    continue

                # Handle complex child elements
                child_obj = self._deserialize_element(child_elem, instance, ctx)

                if child_obj is None:
                    continue

                # Add child to parent using reflection
                self._add_child_to_parent(instance, child_obj, child_elem, ctx)

            return instance

        finally:
            ctx.pop_element()

    def _add_child_to_parent(self, parent: Any, child: Any,
                            child_elem: ET.Element, ctx: DeserializationContext) -> None:
        """
        Add child object to parent using reflection.
        """
        child_tag = self._strip_namespace(child_elem.tag)

        # Get child property name from schema mappings
        child_property = self._get_child_property(parent.__class__, child_tag, ctx)

        if child_property and hasattr(parent, child_property):
            collection = getattr(parent, child_property)
            if isinstance(collection, list):
                collection.append(child)
                # Set parent reference
                if hasattr(child, 'parent'):
                    child.parent = parent

    def _get_child_property(self, parent_class: type, child_tag: str,
                           ctx: DeserializationContext) -> str:
        """Get the property name for a child element."""
        mappings = ctx.mappings.get("child_elements", {}).get(parent_class.__name__, {})
        for prop_name, tag_spec in mappings.items():
            # tag_spec can be a string or list of possible tags
            if isinstance(tag_spec, list):
                # Check if child_tag matches any in the list
                if child_tag in tag_spec:
                    return prop_name
                # Also check if any tag in list ends with child_tag (for matching with/without namespace)
                for tag in tag_spec:
                    if tag.endswith(child_tag) or child_tag.endswith(tag):
                        return prop_name
            else:
                # Single tag name
                if tag_spec == child_tag or tag_spec.endswith(child_tag) or child_tag.endswith(tag_spec):
                    return prop_name
        return None

    def _strip_namespace(self, tag: str) -> str:
        """Strip namespace from XML tag name."""
        if "}" in tag:
            return tag.split("}")[1]
        return tag

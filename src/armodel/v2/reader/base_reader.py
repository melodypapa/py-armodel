"""
V2 ARXML reader - deserializes ARXML to model objects using reflection.
"""
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any, Dict, Optional

from armodel.v2.models.models import AUTOSAR
from armodel.v2.reader.element_handler import ElementHandler
from armodel.v2.reader.schema_registry import SchemaRegistry
from armodel.v2.utils.context import DeserializationContext
from armodel.v2.utils.errors import ReadError


class ARXMLReader:
    """V2 ARXML reader - deserializes ARXML using reflection."""

    def __init__(self, options: Optional[Dict[str, Any]] = None):
        self.options = options or {}
        self.warning = self.options.get("warning", False)

    def load(self, file_path: str, document: AUTOSAR) -> None:
        """Load ARXML file into AUTOSAR document."""
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
        """Deserialize XML element to model object using reflection."""
        # Strip namespace from tag name
        tag_name = self._strip_namespace(elem.tag)

        ctx.push_element(tag_name)
        try:
            # Get model class for this tag
            model_class = ElementHandler.get_class(tag_name, ctx.version)

            if model_class is None:
                # Handle container elements (not model classes, just wrappers)
                if tag_name in ["AR-PACKAGES", "ELEMENTS"]:
                    # Process children and add them directly to parent
                    for child_elem in elem:
                        child_obj = self._deserialize_element(child_elem, parent_obj, ctx)
                        if child_obj is not None:
                            self._add_child_to_parent(parent_obj, child_obj, child_elem, ctx)
                    return None

                # Handle simple text elements
                if tag_name in ["SHORT-NAME", "CATEGORY", "LONG-NAME", "DESC"]:
                    # Map tag to field name
                    field_map = {
                        "SHORT-NAME": "short_name",
                        "CATEGORY": "category",
                        "LONG-NAME": "long_name",
                        "DESC": "desc"
                    }
                    field_name = field_map.get(tag_name)

                    if field_name and hasattr(parent_obj, field_name) and elem.text and elem.text.strip():
                        setattr(parent_obj, field_name, elem.text.strip())
                    return None

                ctx.raise_or_log(f"Unknown XML element '{tag_name}'")
                return None

            # Create instance
            instance = model_class()

            # Set parent reference
            if parent_obj is not None:
                instance.parent = parent_obj

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

                    if field_name and hasattr(instance, field_name) and child_elem.text and child_elem.text.strip():
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
        """Add child object to parent using reflection."""
        child_tag = self._strip_namespace(child_elem.tag)

        # Get child property name from schema mappings
        child_property = self._get_child_property(parent.__class__, child_tag, ctx)

        if child_property and hasattr(parent, child_property):
            collection = getattr(parent, child_property)
            if isinstance(collection, list):
                collection.append(child)
                if hasattr(child, 'parent'):
                    child.parent = parent

    def _get_child_property(self, parent_class: type, child_tag: str,
                           ctx: DeserializationContext) -> str:
        """Get the property name for a child element."""
        mappings = ctx.mappings.get("child_elements", {}).get(parent_class.__name__, {})
        for prop_name, tag_spec in mappings.items():
            if isinstance(tag_spec, list):
                if child_tag in tag_spec:
                    return prop_name
                for tag in tag_spec:
                    if tag.endswith(child_tag) or child_tag.endswith(tag):
                        return prop_name
            else:
                if tag_spec == child_tag or tag_spec.endswith(child_tag) or child_tag.endswith(tag_spec):
                    return prop_name
        return None

    def _strip_namespace(self, tag: str) -> str:
        """Strip namespace from XML tag name."""
        if "}" in tag:
            return tag.split("}")[1]
        return tag

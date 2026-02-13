"""
V2 ARXML reader - deserializes ARXML to model objects using reflection.
"""
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import (
    Any,
    Dict,
    Optional,
    Union,
    cast,
)

from armodel.utils.context import DeserializationContext
from armodel.utils.errors import ReadError
from armodel.v2.models import AUTOSAR
from armodel.v2.reader.element_handler import ElementHandler
from armodel.v2.reader.schema_registry import SchemaRegistry


class ARXMLReader:
    """V2 ARXML reader - deserializes ARXML using reflection."""

    def __init__(self, options: Optional[Dict[str, Any]] = None) -> None:
        self.options = options or {}
        self.warning = self.options.get("warning", False)

    def _create_primitive_value(self, target_obj: Any, field_name: str,
                               value: str) -> Any:
        """Create a primitive type object for the given field.

        Args:
            target_obj: The target object with the field
            field_name: Name of the field to set
            value: String value from XML

        Returns:
            The appropriate value (primitive type object or string)
        """
        # Map field names to their expected primitive types
        primitive_type_map = {
            "short_name": "Identifier",
            "category": "CategoryString",
            "desc": "String",
        }

        # Get the expected type name for this field
        type_name = primitive_type_map.get(field_name)
        if not type_name:
            return value

        # Try to import and create the primitive type
        try:
            from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
                CategoryString,
                Identifier,
                String,
            )

            type_class_map = {
                "Identifier": Identifier,
                "CategoryString": CategoryString,
                "String": String,
            }

            type_class = type_class_map.get(type_name)
            if type_class:
                instance = type_class()
                if hasattr(instance, 'value'):
                    instance.value = value
                    return instance
        except Exception:
            pass

        return value

    def _map_tag_to_field(self, tag_name: str) -> str:
        """Map XML tag name to Python field name.

        Args:
            tag_name: XML tag name (e.g., "SHORT-NAME", "BASE-TYPE-SIZE")

        Returns:
            Python field name in snake_case (e.g., "short_name", "base_type_size")
        """
        # Common mappings
        tag_to_field_map = {
            "SHORT-NAME": "short_name",
            "CATEGORY": "category",
            "LONG-NAME": "long_name",
            "DESC": "desc",
            "BASE-TYPE-SIZE": "base_type_size",
            "MEM-ALIGNMENT": "mem_alignment",
            "NATIVE-DECLARATION": "native",
            "BASE-TYPE-ENCODING": "base_type_encoding",
            "BYTE-ORDER": "byte_order",
        }

        if tag_name in tag_to_field_map:
            return tag_to_field_map[tag_name]

        # Default: convert kebab-case to snake_case
        return tag_name.lower().replace("-", "_")

    def _is_property_element(self, tag_name: str) -> bool:
        """Check if an element looks like a property element (not a model class).

        Property elements are typically all-caps with hyphens and contain text content.
        Examples: SHORT-NAME, CATEGORY, BASE-TYPE-SIZE, etc.

        Args:
            tag_name: XML tag name

        Returns:
            True if this looks like a property element
        """
        # Property elements typically have hyphens and are uppercase
        return "-" in tag_name and tag_name == tag_name.upper()

    def load(self, file_path: Union[str, Path], document: AUTOSAR) -> None:
        """Load ARXML file into AUTOSAR document."""
        file_path = Path(file_path) if isinstance(file_path, str) else file_path

        # Parse XML with ElementTree
        tree = ET.parse(file_path)
        root = tree.getroot()

        # Detect AUTOSAR version from schema location
        version = self._detect_autosar_version(root, file_path)

        # Create deserialization context
        ctx = DeserializationContext(
            version=version,
            warning=self.warning,
            schema_mappings=SchemaRegistry.get_mappings(version),
            file_path=file_path
        )

        # Deserialize root element
        # For AUTOSAR, use the document instance directly (singleton)
        tag_name = self._strip_namespace(root.tag)
        if tag_name == "AUTOSAR":
            root_obj = document
            # Process children of AUTOSAR
            for child_elem in root:
                child_obj = self._deserialize_element(child_elem, document, ctx)
                if child_obj is not None:
                    self._add_child_to_parent(root_obj, child_obj, child_elem, ctx)
        else:
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

                # Handle simple text elements that map to object properties
                # These are typically primitive type properties like SHORT-NAME, CATEGORY, etc.
                field_name = self._map_tag_to_field(tag_name)

                if field_name and hasattr(parent_obj, field_name) and elem.text and elem.text.strip():
                    value = self._create_primitive_value(parent_obj, field_name, elem.text.strip())
                    setattr(parent_obj, field_name, value)
                    return None

                # Skip unknown property elements (those that look like properties but aren't recognized)
                # This handles flattened XML structures where properties appear directly on parent
                # instead of being nested in a child object
                if self._is_property_element(tag_name):
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
                # These map to object properties like short_name, category, base_type_size, etc.
                field_name = self._map_tag_to_field(child_tag)

                if field_name and hasattr(instance, field_name) and child_elem.text and child_elem.text.strip():
                    value = self._create_primitive_value(instance, field_name, child_elem.text.strip())
                    setattr(instance, field_name, value)
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
                           ctx: DeserializationContext) -> Optional[str]:
        """Get the property name for a child element."""
        mappings: Dict[str, Any] = ctx.mappings.get("child_elements", {}).get(parent_class.__name__, {})
        for prop_name, tag_spec in mappings.items():
            if isinstance(tag_spec, list):
                if child_tag in tag_spec:
                    return cast(Optional[str], prop_name)
                for tag in tag_spec:
                    if tag.endswith(child_tag) or child_tag.endswith(tag):
                        return cast(Optional[str], prop_name)
            else:
                if tag_spec == child_tag or tag_spec.endswith(child_tag) or child_tag.endswith(tag_spec):
                    return cast(Optional[str], prop_name)
        return None

    def _detect_autosar_version(self, root: ET.Element, file_path: Path) -> str:
        """Detect AUTOSAR version from XML schema location.

        Args:
            root: Root XML element
            file_path: Path to the ARXML file

        Returns:
            AUTOSAR version string (e.g., "3.2.3", "4.0.3", "R23-11")
        """
        # Mapping from XSD files to AUTOSAR versions
        xsd_to_version = {
            "AUTOSAR_3.2.3.xsd": "3.2.3",
            "AUTOSAR_4.0.3.xsd": "4.0.3",
            "AUTOSAR_4.1.1.xsd": "4.1.1",
            "AUTOSAR_4.1.2.xsd": "4.1.2",
            "AUTOSAR_4.1.3.xsd": "4.1.3",
            "AUTOSAR_4.2.1.xsd": "4.2.1",
            "AUTOSAR_4.2.2.xsd": "4.2.2",
            "AUTOSAR_4.3.0.xsd": "4.3.0",
            "AUTOSAR_R19-11.xsd": "R19-11",
            "AUTOSAR_R20-11.xsd": "R20-11",
            "AUTOSAR_R21-11.xsd": "R21-11",
            "AUTOSAR_R22-11.xsd": "R22-11",
            "AUTOSAR_R23-11.xsd": "R23-11",
            "AUTOSAR_R24-11.xsd": "R24-11",
        }

        # Check schemaLocation attribute
        schema_loc = root.attrib.get(
            "{http://www.w3.org/2001/XMLSchema-instance}schemaLocation",
            ""
        )

        if schema_loc:
            # Extract XSD filename from schema location
            # Format: "http://autosar.org/schema/r4.0 AUTOSAR_4-0-3.xsd"
            parts = schema_loc.split()
            if len(parts) >= 2:
                xsd_file = parts[1].split("/")[-1]
                if xsd_file in xsd_to_version:
                    return xsd_to_version[xsd_file]

        # Try to detect from xmlns attribute (fallback)
        xmlns = root.attrib.get("xmlns", "")
        if "schema/r4.0" in xmlns:
            return "4.0.3"  # Default for 4.0.x series
        elif "schema/r3.2.3" in xmlns:
            return "3.2.3"

        # Default fallback
        return "3.2.3"

    def _strip_namespace(self, tag: str) -> str:
        """Strip namespace from XML tag name."""
        if "}" in tag:
            return tag.split("}")[1]
        return tag

"""
V2 ARXML writer demo - serializes model objects to ARXML using reflection.
"""
import xml.etree.ElementTree as ET
from typing import Dict, Any, Optional
from pathlib import Path

from ..models.models import AUTOSAR
from ..utils.context import SerializationContext
from ..reader.schema_registry import SchemaRegistry
from ..utils.errors import WriteError


class ARXMLWriter:
    """
    V2 ARXML writer - serializes model objects to XML using reflection.
    """

    def __init__(self, options: Optional[Dict[str, Any]] = None):
        """
        Initialize writer.

        Args:
            options: Optional configuration dict
                - format: bool (default: True) - pretty print output
                - encoding: str (default: "utf-8")
                - xml_declaration: bool (default: True)
        """
        self.options = options or {}
        self.format = self.options.get("format", True)
        self.encoding = self.options.get("encoding", "utf-8")
        self.xml_declaration = self.options.get("xml_declaration", True)

    def save(self, file_path: str, document: AUTOSAR) -> None:
        """
        Save AUTOSAR document to ARXML file.

        Args:
            file_path: Output file path
            document: AUTOSAR document to serialize

        Raises:
            WriteError: If serialization fails
        """
        file_path = Path(file_path)

        # Get AUTOSAR version (default to 3.2.3 for demo)
        version = "3.2.3"

        # Create serialization context
        ctx = SerializationContext(
            version=version,
            schema_mappings=SchemaRegistry.get_mappings(version)
        )

        # Serialize document to XML
        root = self._serialize_object(document, ctx)

        # Add namespaces
        root.set("xmlns", "http://autosar.org/3.2.3")
        root.set("xsi:schemaLocation", "http://autosar.org/3.2.3 AUTOSAR_3-2-3.xsd")
        root.set("xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")

        # Write to file
        tree = ET.ElementTree(root)

        if self.format:
            # Pretty print (Python 3.9+)
            ET.indent(tree, space="  ")

        tree.write(
            file_path,
            encoding=self.encoding,
            xml_declaration=self.xml_declaration
        )

    def _serialize_object(self, obj: Any, ctx: SerializationContext) -> ET.Element:
        """
        Serialize model object to XML element using reflection.

        Args:
            obj: Model instance to serialize
            ctx: Serialization context

        Returns:
            XML element
        """
        # Get XML tag name for this object's class
        class_name = obj.__class__.__name__
        tag_name = ctx.get_element_tag(class_name)

        # Create XML element
        elem = ET.Element(tag_name)

        # Serialize attributes (UUID, etc.)
        if hasattr(obj, 'uuid') and obj.uuid is not None:
            elem.set("UUID", obj.uuid)

        # Serialize child elements
        self._serialize_children(obj, elem, ctx)

        return elem

    def _serialize_children(self, obj: Any, elem: ET.Element, ctx: SerializationContext) -> None:
        """Serialize child objects to XML elements."""
        class_name = obj.__class__.__name__

        # Get child element mappings for this class
        child_mappings = ctx.mappings.get("child_elements", {}).get(class_name, {})

        # Special handling for AUTOSAR root element
        if class_name == "AUTOSAR":
            # Serialize ar_packages
            if hasattr(obj, 'ar_packages'):
                packages_elem = ET.SubElement(elem, "AR-PACKAGES")
                for pkg in obj.ar_packages:
                    pkg_elem = self._serialize_object(pkg, ctx)
                    packages_elem.append(pkg_elem)
            return

        # Special handling for ARPackage
        if class_name == "ARPackage":
            # Serialize short_name
            if hasattr(obj, 'short_name') and obj.short_name is not None:
                short_name_elem = ET.SubElement(elem, "SHORT-NAME")
                short_name_elem.text = obj.short_name

            # Serialize child packages
            if hasattr(obj, 'ar_packages') and obj.ar_packages:
                packages_elem = ET.SubElement(elem, "AR-PACKAGES")
                for pkg in obj.ar_packages:
                    pkg_elem = self._serialize_object(pkg, ctx)
                    packages_elem.append(pkg_elem)

            # Serialize elements (components, etc.)
            if hasattr(obj, 'elements') and obj.elements:
                elements_elem = ET.SubElement(elem, "ELEMENTS")
                for element in obj.elements:
                    elem_elem = self._serialize_object(element, ctx)
                    elements_elem.append(elem_elem)
            return

        # Generic handling for other objects (like SwComponentType)
        for field_name, child_tag in child_mappings.items():
            if hasattr(obj, field_name):
                child_value = getattr(obj, field_name)

                if child_value is None:
                    continue

                # Handle primitive values (strings)
                if not isinstance(child_value, list):
                    child_elem = ET.SubElement(elem, child_tag)
                    child_elem.text = str(child_value)

"""
ARXML Writer for V2 models.
"""
import sys
import xml.etree.ElementTree as ET
from typing import Any, Optional

from armodel.v2.models.models import (
    AUTOSAR,
    ARPackage,
)


class ARXMLWriter:
    """Writer for ARXML files."""

    def __init__(self, options: Optional[dict] = None) -> None:
        """
        Initialize the ARXML writer.

        Args:
            options: Optional writer configuration
        """
        self.options = options or {}
        self.format = self.options.get("format", True)

    def _to_primitive_value(self, value: Any) -> Optional[str]:
        """
        Convert AUTOSAR primitive type objects to their string values.

        Args:
            value: The value to convert (can be Identifier, String, etc. or a plain str)

        Returns:
            The string value, or None if value is None
        """
        if value is None:
            return None

        # Check if it's an AUTOSAR primitive type (has getValue method or value property)
        if hasattr(value, 'getValue'):
            return value.getValue()
        elif hasattr(value, 'value'):
            return str(value.value) if value.value is not None else None
        else:
            # Plain string or other type
            return str(value) if value else None

    def save(self, file_path: str, document: AUTOSAR) -> None:
        """
        Save AUTOSAR document to ARXML file.

        Args:
            file_path: Path to output ARXML file
            document: AUTOSAR document to save
        """
        # Create root element
        root = ET.Element("AUTOSAR")
        root.set("xmlns", "http://autosar.org/3.2.3")

        # Add AR-PACKAGES container
        ar_packages_elem = ET.SubElement(root, "AR-PACKAGES")

        # Serialize each AR-PACKAGE
        for pkg in document.ar_packages:
            self._serialize_package(pkg, ar_packages_elem)

        # Write to file
        tree = ET.ElementTree(root)

        # Format XML with indentation (Python 3.9+ has ET.indent)
        if sys.version_info >= (3, 9) and self.format:
            ET.indent(tree, space="  ")

        tree.write(file_path, encoding="utf-8", xml_declaration=True)

    def _serialize_package(self, pkg: ARPackage, parent: ET.Element) -> None:
        """Serialize ARPackage to XML element."""
        pkg_elem = ET.SubElement(parent, "AR-PACKAGE")

        # Add SHORT-NAME (convert Identifier to string if needed)
        if pkg.short_name:
            short_name_elem = ET.SubElement(pkg_elem, "SHORT-NAME")
            short_name_elem.text = self._to_primitive_value(pkg.short_name)

        # Add nested AR-PACKAGES
        if pkg.ar_packages:
            sub_packages_elem = ET.SubElement(pkg_elem, "AR-PACKAGES")
            for sub_pkg in pkg.ar_packages:
                self._serialize_package(sub_pkg, sub_packages_elem)

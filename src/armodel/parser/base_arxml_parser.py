"""
Base ARXML parser with common utility methods.

Extends AbstractARXMLParser with reusable parsing patterns:
- read_collection(): Generic collection reader with handler map
- set_attributes(): Bulk attribute setter
- read_optional(): Conditional element reader
"""
from typing import Callable, Dict, Any, List
import xml.etree.ElementTree as ET
from .abstract_arxml_parser import AbstractARXMLParser


class BaseARXMLParser(AbstractARXMLParser):
    """
    Base parser with common utility methods for all specialized parsers.

    Provides reusable patterns for:
    - Collection parsing with tag-based routing
    - Bulk attribute setting
    - Optional element reading
    """

    def read_collection(
        self,
        parent: ET.Element,
        path: str,
        handler_map: Dict[str, Callable[[ET.Element], Any]],
    ) -> List[Any]:
        """
        Read a collection of child elements using a handler map.

        Args:
            parent: Parent XML element
            path: XPath path to children (e.g., "EVENTS/*")
            handler_map: Dict mapping tag names to handler functions

        Returns:
            List of results from handler functions

        Raises:
            ValueError: If unsupported tag encountered and warning=False
        """
        results = []
        child_elements = self.findall(parent, path)

        for child_element in child_elements:
            tag_name = self.getTagName(child_element)

            if tag_name in handler_map:
                result = handler_map[tag_name](child_element)
                if result is not None:
                    results.append(result)
            else:
                error_msg = f"Unsupported element <{tag_name}> in path {path}"
                self.notImplemented(error_msg)

        return results

    def set_attributes(
        self,
        obj: Any,
        element: ET.Element,
        attribute_map: Dict[str, tuple],
    ) -> None:
        """
        Set multiple attributes on an object from XML element.

        Args:
            obj: Object to set attributes on (must have setter methods)
            element: XML element containing the data
            attribute_map: Dict mapping {
                attribute_name: (xml_path, getter_function)
            }

        Example:
            parser.set_attributes(behavior, element, {
                'shortName': ('SHORT-NAME', parser.getShortName),
                'desc': ('DESC', lambda e: e.text),
            })
        """
        for attr_name, (xml_path, getter_func) in attribute_map.items():
            value = getter_func(element)
            if value is not None:
                setter_name = f'set{attr_name[0].upper()}{attr_name[1:]}'
                setter = getattr(obj, setter_name)
                setter(value)

    def read_optional(
        self,
        parent: ET.Element,
        path: str,
        reader_func: Callable[[ET.Element], Any],
    ) -> Any:
        """
        Read an optional element if it exists.

        Args:
            parent: Parent XML element
            path: XPath to optional element
            reader_func: Function to read the element if found

        Returns:
            Result of reader_func, or None if element not found
        """
        child = self.find(parent, path)
        if child is not None:
            return reader_func(child)
        return None

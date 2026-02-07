"""
Element handler for V2 ARXML reader.
Maps XML tag names to model classes.
"""
from armodel.v2.models.models import AUTOSAR, ARPackage
from armodel.v2.reader.schema_registry import SchemaRegistry

# Register model classes
SchemaRegistry.register_class("AUTOSAR", AUTOSAR)
SchemaRegistry.register_class("AR-PACKAGE", ARPackage)


class ElementHandler:
    """Handler for mapping XML elements to model classes."""

    @classmethod
    def get_class(cls, tag_name: str, version: str = "3.2.3"):
        """Get model class for XML tag name."""
        mappings = SchemaRegistry.get_mappings(version)
        return mappings.get("tag_to_class", {}).get(tag_name)

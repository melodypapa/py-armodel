"""
Element handler for V2 ARXML reader.
Maps XML tag names to model classes.
"""
from armodel.v2.models import (
    AUTOSAR,
    ARPackage,
)
from armodel.v2.reader.schema_registry import SchemaRegistry

# Register core model classes
SchemaRegistry.register_class("AUTOSAR", AUTOSAR)
SchemaRegistry.register_class("AR-PACKAGE", ARPackage)

# Lazy import mappings for additional element types
# This avoids circular import issues during module loading
_ELEMENT_TYPE_MAPPINGS = {
    "SW-BASE-TYPE": "armodel.v2.models.M2.MSR.AsamHdo.SwBaseType.SwBaseType",
}


def _lazy_import(class_path: str):
    """Lazily import a class from its module path.

    Args:
        class_path: Full module path to the class (e.g., "module.submodule.ClassName")

    Returns:
        The class object or None if import fails
    """
    try:
        parts = class_path.rsplit(".", 1)
        if len(parts) != 2:
            return None

        module_path, class_name = parts
        import importlib
        module = importlib.import_module(module_path)
        return getattr(module, class_name)
    except Exception:
        return None


class ElementHandler:
    """Handler for mapping XML elements to model classes."""

    @classmethod
    def get_class(cls, tag_name: str, version: str = "3.2.3"):
        """Get model class for XML tag name."""
        # First check the schema registry for already registered classes
        mappings = SchemaRegistry.get_mappings(version)
        model_class = mappings.get("tag_to_class", {}).get(tag_name)
        if model_class is not None:
            return model_class

        # Try lazy import from element type mappings
        class_path = _ELEMENT_TYPE_MAPPINGS.get(tag_name)
        if class_path:
            model_class = _lazy_import(class_path)
            if model_class is not None:
                # Cache the class in the registry for future use
                SchemaRegistry.register_class(tag_name, model_class)
                return model_class

        return None

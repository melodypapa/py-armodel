"""
Schema registry for V2 ARXML reader.
Hardcoded mappings for demo (will be XSD-generated in production).
"""
from typing import Dict


class SchemaRegistry:
    """Registry for version-specific schema mappings."""

    _MAPPINGS_3_2_3 = {
        "tag_to_class": {},
        "child_elements": {
            "AUTOSAR": {
                "ar_packages": ["AR-PACKAGE", "AR-PACKAGES"],
            },
            "ARPackage": {
                "short_name": "SHORT-NAME",
                "ar_packages": ["AR-PACKAGE", "AR-PACKAGES"],
                "elements": ["ELEMENTS", "APPLICATION-SOFTWARE-COMPONENT-TYPE"],
            },
        },
        "attribute_mappings": {},
    }
    _CACHE: Dict[str, Dict] = {}

    @classmethod
    def get_mappings(cls, version: str) -> Dict:
        """Get schema mappings for the given AUTOSAR version."""
        if version not in cls._CACHE:
            cls._CACHE[version] = cls._MAPPINGS_3_2_3.copy()
        return cls._CACHE[version]

    @classmethod
    def register_class(cls, tag_name: str, model_class: type) -> None:
        """Register a model class for an XML tag name."""
        for mappings in cls._CACHE.values():
            mappings["tag_to_class"][tag_name] = model_class
        cls._MAPPINGS_3_2_3["tag_to_class"][tag_name] = model_class

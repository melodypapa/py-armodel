"""
Schema registry for V2 ARXML reader/writer demo.
Hardcoded mappings for AUTOSAR 3.2.3 (in production, generated from XSD).
"""
from typing import Dict, Optional


class SchemaRegistry:
    """
    Registry for version-specific schema mappings.
    """

    # Hardcoded mappings for AUTOSAR 3.2.3 demo
    _MAPPINGS_3_2_3 = {
        "element_names": {
            "AUTOSAR": "AUTOSAR",
            "ARPackage": "AR-PACKAGE",
            "SwComponentType": "APPLICATION-SOFTWARE-COMPONENT-TYPE",
        },
        "child_elements": {
            "AUTOSAR": {
                # Map: Python field name -> list of possible XML tags that go into this field
                "ar_packages": ["AR-PACKAGE", "AR-PACKAGES"],  # Accept both tag and container
            },
            "ARPackage": {
                "short_name": "SHORT-NAME",
                "ar_packages": ["AR-PACKAGE", "AR-PACKAGES"],
                # elements collection can contain various component types
                "elements": ["ELEMENTS", "APPLICATION-SOFTWARE-COMPONENT-TYPE"],
            },
            "SwComponentType": {
                "short_name": "SHORT-NAME",
                "category": "CATEGORY",
            }
        },
        "attribute_mappings": {
            "SwComponentType": {
                "UUID": "uuid",
            }
        },
        "tag_to_class": {
            # Will be populated with model class references
        }
    }

    _CACHE: Dict[str, Dict] = {}

    @classmethod
    def get_mappings(cls, version: str) -> Dict:
        """
        Get schema mappings for the given AUTOSAR version.

        Args:
            version: AUTOSAR version (e.g., "3.2.3", "R23-11")

        Returns:
            Dictionary of mappings
        """
        if version not in cls._CACHE:
            # For demo, return 3.2.3 mappings for all versions
            cls._CACHE[version] = cls._MAPPINGS_3_2_3.copy()

        return cls._CACHE[version]

    @classmethod
    def register_class(cls, tag_name: str, model_class: type) -> None:
        """Register a model class for an XML tag name."""
        # Register in all cached mappings
        for mappings in cls._CACHE.values():
            mappings["tag_to_class"][tag_name] = model_class

        # Also register in the base mapping
        cls._MAPPINGS_3_2_3["tag_to_class"][tag_name] = model_class

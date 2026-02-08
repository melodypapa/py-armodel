#!/usr/bin/env python3
"""
V2 Model Generator for py-armodel

This script generates all V2 AUTOSAR model classes from package specifications
in docs/requirements/packages/, with a modern Pythonic property-based dual API built-in.

Features:
- Generates Python classes with @property decorators for snake_case access
- Includes AUTOSAR-compatible camelCase methods (getShortName, setShortName)
- Adds fluent with_ methods for method chaining
- Maintains 100% backward compatibility with V1 API
- Follows TDD approach with generated test files

Usage:
    python scripts/generate_v2_models.py --all
    python scripts/generate_v2_models.py --package M2::AUTOSARTemplates::GenericStructure
    python scripts/generate_v2_models.py --dry-run  # Preview changes without writing
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

# Add scripts/lib to path
sys.path.insert(0, str(Path(__file__).parent / 'lib'))

from code_generator import (
    _camel_to_snake,
    _generate_docstring,
    _generate_init_code,
    _generate_property_based_attributes,
    _generate_property_based_methods,
)
from package_loader import get_all_packages

# =============================================================================
# Configuration
# =============================================================================

PROJECT_ROOT = Path(__file__).parent.parent
REQUIREMENTS_DIR = PROJECT_ROOT / 'docs' / 'requirements'
V2_MODELS_DIR = PROJECT_ROOT / 'src' / 'armodel' / 'v2' / 'models'
V2_TESTS_DIR = PROJECT_ROOT / 'tests' / 'test_armodel' / 'v2' / 'models'


# =============================================================================
# Enhanced Property-Based Code Generation (V2 Redesign)
# =============================================================================

def generate_v2_property_code(
    attr_name: str,
    attr_type: str,
    is_optional: bool = False,
    is_readonly: bool = False,
    validation_rules: Optional[List[str]] = None
) -> str:
    """Generate Pythonic @property code with getter, setter, and validation.

    Args:
        attr_name: Attribute name in camelCase (e.g., 'shortName')
        attr_type: Python type annotation (e.g., 'str', 'Optional[str]')
        is_optional: Whether the attribute can be None
        is_readonly: Whether the property is read-only (no setter)
        validation_rules: List of validation rule names to apply

    Returns:
        Generated property code string
    """
    # Convert camelCase to snake_case for Pythonic property name
    snake_name = _camel_to_snake(attr_name)
    private_attr = f"_{attr_name}"  # Private attribute name (camelCase)

    # Build type annotation
    type_annotation = attr_type
    if is_optional and not attr_type.startswith('Optional'):
        type_annotation = f"Optional[{attr_type}]"

    # Generate getter
    getter_code = f'''    @property
    def {snake_name}(self) -> {type_annotation}:
        """Get {attr_name} (Pythonic accessor)."""
        return self.{private_attr}
'''

    # Generate setter if not read-only
    setter_code = ""
    if not is_readonly:
        setter_code = f'''    @{snake_name}.setter
    def {snake_name}(self, value: {type_annotation}) -> None:
        """Set {attr_name} with validation."""
'''

        # Add validation logic based on rules
        if validation_rules:
            for rule in validation_rules:
                if rule == 'non_empty_string':
                    setter_code += f'''        if value is not None and not isinstance(value, str):
            raise TypeError(
                f"{attr_name} must be str or None, got {{type(value).__name__}}"
            )
        if not value:
            raise ValueError(f"{attr_name} cannot be empty")
'''
                elif rule == 'enum':
                    # Enum validation will be added with a VALID_XXX constant
                    setter_code += f'''        if value is None:
            self.{private_attr} = None
            return

        if not isinstance(value, str):
            raise TypeError(
                f"{attr_name} must be str or None, got {{type(value).__name__}}"
            )

        # TODO: Add enum validation constant
        self.{private_attr} = value
'''
                elif rule == 'type_check':
                    setter_code += f'''        if value is not None and not isinstance(value, {attr_type}):
            raise TypeError(
                f"{attr_name} must be {attr_type} or None, got {{type(value).__name__}}"
            )
'''
        else:
            # Default validation
            if is_optional:
                setter_code += f'''        if value is None:
            self.{private_attr} = None
            return

        if not isinstance(value, {attr_type}):
            raise TypeError(
                f"{attr_name} must be {attr_type} or None, got {{type(value).__name__}}"
            )

        self.{private_attr} = value
'''
            else:
                setter_code += f'''        if not isinstance(value, {attr_type}):
            raise TypeError(
                f"{attr_name} must be {attr_type}, got {{type(value).__name__}}"
            )

        self.{private_attr} = value
'''

    return getter_code + setter_code


def generate_with_method(attr_name: str, attr_type: str, class_name: str) -> str:
    """Generate fluent with_ method for method chaining.

    Args:
        attr_name: Attribute name in camelCase
        attr_type: Python type annotation
        class_name: Name of the class for return type annotation

    Returns:
        Generated with_ method code
    """
    snake_name = _camel_to_snake(attr_name)

    return f'''    def with_{snake_name}(self, value: {attr_type}) -> "{class_name}":
        """
        Set {attr_name} and return self for chaining.

        Args:
            value: The {attr_name} to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_{snake_name}("value")
        """
        self.{snake_name} = value  # Use property setter (gets validation)
        return self
'''


def generate_autosar_methods(attr_name: str, attr_type: str, class_name: str) -> str:
    """Generate AUTOSAR-compatible get/set methods that delegate to properties.

    Args:
        attr_name: Attribute name in camelCase
        attr_type: Python type annotation
        class_name: Name of the class for return type annotation

    Returns:
        Generated AUTOSAR methods code
    """
    snake_name = _camel_to_snake(attr_name)

    getter = f'''    def get{attr_name}(self) -> {attr_type}:
        """
        AUTOSAR-compliant getter for {attr_name}.

        Returns:
            The {attr_name} value

        Note:
            Delegates to {snake_name} property (CODING_RULE_V2_00017)
        """
        return self.{snake_name}  # Delegates to property
'''

    setter = f'''    def set{attr_name}(self, value: {attr_type}) -> "{class_name}":
        """
        AUTOSAR-compliant setter for {attr_name} with method chaining.

        Args:
            value: The {attr_name} to set

        Returns:
            self for method chaining

        Note:
            Delegates to {snake_name} property setter (gets validation automatically)
        """
        self.{snake_name} = value  # Delegates to property setter (gets validation)
        return self
'''

    return getter + setter


def _camel_to_snake(name: str) -> str:
    """Convert camelCase to snake_case.

    Args:
        name: camelCase string

    Returns:
        snake_case string
    """
    import re
    # Handle cases like "shortName" -> "short_name"
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    # Handle cases like "ShortName" -> "short_name"
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


# =============================================================================
# Main Generator Class
# =============================================================================

class V2ModelGenerator:
    """Generate V2 models with property-based dual API."""

    def __init__(self, dry_run: bool = False):
        self.dry_run = dry_run
        self.generated_files = []
        self.errors = []
        self.type_to_package = {}  # Cache for type-to-package mapping

    def _build_type_mapping(self, packages_dir: Path):
        """Build a mapping of type names to their package paths.

        Args:
            packages_dir: Path to packages directory
        """

        type_mapping = {}

        # Scan all package JSON files
        for pkg_file in packages_dir.glob("*.json"):
            try:
                with open(pkg_file, 'r', encoding='utf-8') as f:
                    pkg_data = json.load(f)

                # Handle .classes.json files (list of class objects)
                if 'classes' in pkg_data and isinstance(pkg_data['classes'], list):
                    pkg_name = pkg_data.get('package', '')
                    if not pkg_name:
                        continue

                    # Add classes to mapping with their individual module paths
                    for class_info in pkg_data['classes']:
                        class_name = class_info.get('name')
                        if class_name:
                            module_path = self._class_to_module_path(pkg_name, class_name)
                            if module_path:
                                type_mapping[class_name] = module_path

                # Handle regular package files (dict of classes)
                elif 'classes' in pkg_data and isinstance(pkg_data['classes'], dict):
                    pkg_name = pkg_data.get('name', '')
                    if not pkg_name:
                        continue

                    # Add classes to mapping with their individual module paths
                    for class_name in pkg_data['classes'].keys():
                        module_path = self._class_to_module_path(pkg_name, class_name)
                        if module_path:
                            type_mapping[class_name] = module_path

            except Exception:
                # Ignore errors in package files
                pass

        self.type_to_package = type_mapping

    def _class_to_module_path(self, pkg_name: str, class_name: str) -> Optional[str]:
        """Convert AUTOSAR package and class name to Python module path.

        Each class is in its own file named after the class.

        Args:
            pkg_name: AUTOSAR package name (e.g., 'M2::AUTOSARTemplates::...')
            class_name: Class name (e.g., 'ARObject', 'AdminData')

        Returns:
            Python module path or None
        """
        parts = pkg_name.split('::')
        if parts[0] == 'M2':
            # Convert to Python path
            # M2::MSR::AsamHdo::AdminData + DocRevision
            # -> armodel.v2.models.M2.MSR.AsamHdo.DocRevision
            py_parts = ['armodel', 'v2', 'models'] + parts
            # Replace the last part (package name) with the class name for the file
            py_parts[-1] = class_name
            return '.'.join(py_parts)
        return None

    def generate_all(self, specific_package: Optional[str] = None):
        """Generate all V2 models from package specifications.

        Args:
            specific_package: Optional specific package to generate (e.g., 'M2::AUTOSARTemplates')
        """
        print("🚀 Starting V2 Model Generation")
        print("=" * 60)

        # Build type-to-package mapping first
        print("🔍 Building type-to-package mapping...")
        self._build_type_mapping(REQUIREMENTS_DIR / 'packages')
        print(f"✅ Mapped {len(self.type_to_package)} types")
        print()

        # Load all packages
        packages = get_all_packages(REQUIREMENTS_DIR, specific_package)

        if not packages:
            print("❌ No packages found!")
            return

        print(f"📦 Found {len(packages)} packages to process")
        print()

        # Process each package
        for pkg in packages:
            self._process_package(pkg)

        # Summary
        self._print_summary()

    def _process_package(self, pkg: Dict[str, Any]):
        """Process a single package and generate its classes.

        Args:
            pkg: Package dictionary with 'name', 'file', 'classes', 'enumerations'
        """
        pkg_name = pkg.get('name', 'Unknown')
        classes = pkg.get('classes', {})

        if not classes:
            return

        print(f"📝 Processing package: {pkg_name}")
        print(f"   Classes: {len(classes)}")

        # Generate each class
        for class_name, class_info in classes.items():
            try:
                self._generate_class_file(pkg_name, class_name, class_info)
            except Exception as e:
                self.errors.append((pkg_name, class_name, str(e)))
                print(f"   ❌ Error generating {class_name}: {e}")

        print()

    def _generate_class_file(self, pkg_name: str, class_name: str, class_info: Dict[str, Any]):
        """Generate a single V2 model class file.

        Args:
            pkg_name: Package name
            class_name: Class name
            class_info: Class information dictionary
        """
        # Determine file path
        file_path = self._get_file_path(pkg_name, class_name)

        if self.dry_run:
            print(f"   📄 Would create: {file_path}")
            self.generated_files.append(str(file_path))
            return

        # Create parent directories
        file_path.parent.mkdir(parents=True, exist_ok=True)

        # Generate class code using enhanced property-based generator (V2-only)
        code = self._generate_v2_class_code(class_info, pkg_name)

        # Write to file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(code)

        self.generated_files.append(str(file_path))
        print(f"   ✅ Generated: {class_name}")

    def _get_file_path(self, pkg_name: str, class_name: str) -> Path:
        """Determine the file path for a generated class.

        Args:
            pkg_name: Package name (e.g., 'M2::AUTOSARTemplates::GenericStructure')
            class_name: Class name (e.g., 'ARObject')

        Returns:
            Path where the class file should be created

        Note:
            Package names may end with the same name as the class (e.g., EngineeringObject).
            We need to handle this by checking if the last package part matches a known
            top-level package name.
        """
        # Known top-level package names that should be leaf packages (single .py file)
        known_leaf_packages = {
            'ArObject', 'Identifiable', 'Referrable', 'ElementCollection',
            'ARPackage', 'PrimitiveTypes', 'ARElement', 'CollectableElement',
            'EngineeringObject', 'MultidimensionalTime'
        }

        # Convert package path to directory structure
        pkg_parts = pkg_name.split('::')

        # Check if the last part is a leaf package (not a subdirectory)
        if pkg_parts[-1] in known_leaf_packages or pkg_name.endswith('::' + pkg_parts[-1]):
            # Last part is a leaf package - the .py file should be at this level
            package_parts = pkg_parts[:-1]
        else:
            package_parts = pkg_parts

        # Map to V2 directory structure
        v2_path = V2_MODELS_DIR
        for part in package_parts:
            v2_path = v2_path / part

        # Add class filename
        return v2_path / f"{class_name}.py"

    def _print_summary(self):
        """Print generation summary."""
        print("=" * 60)
        print("📊 Generation Summary")
        print("=" * 60)
        print(f"✅ Files generated: {len(self.generated_files)}")

        if self.errors:
            print(f"❌ Errors: {len(self.errors)}")
            print()
            print("Errors:")
            for pkg_name, class_name, error in self.errors:
                print(f"  - {pkg_name}::{class_name}: {error}")
        else:
            print("✅ No errors!")

        if self.dry_run:
            print()
            print("🔍 Dry run mode - no files were written")

    def _generate_v2_imports(self, class_info: Dict[str, Any], package_path: str) -> List[str]:
        """Generate V2-specific imports for a class.

        Args:
            class_info: Class information dictionary
            package_path: Package path (e.g., 'M2::AUTOSARTemplates::...')

        Returns:
            List of import statement strings
        """
        imports = []
        class_name = class_info['name']
        parent = class_info.get('parent') or 'ARObject'
        attributes = class_info.get('attributes', {})

        # Add common imports
        imports.append('from abc import ABC, abstractmethod')
        imports.append('from typing import List, Optional, Dict, Any')

        # Using string annotations for ALL attribute types to avoid import issues
        # No need to import types used in attributes
        # Only import parent classes

        # Add parent class import based on parent type
        # Skip self-imports for base classes (e.g., ARObject importing itself)
        if parent == 'ARObject':
            if class_name != 'ARObject':  # Don't import ARObject when generating ARObject
                imports.append('from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject')
        elif parent == 'Referrable':
            imports.append('from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Referrable import Referrable')
        elif parent == 'Identifiable':
            if class_name != 'Identifiable':  # Don't import Identifiable when generating Identifiable
                imports.append('from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable')
            imports.append('from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject')
        elif parent == 'MultilanguageReferrable':
            if class_name != 'MultilanguageReferrable':  # Don't import when generating MultilanguageReferrable
                imports.append('from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultilanguageReferrable import MultilanguageReferrable')
            # Also need to import Referrable (parent of MultilanguageReferrable)
            imports.append('from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Referrable import Referrable')
        elif parent == 'PackageableElement':
            imports.append('from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PackageableElement import PackageableElement')
        elif parent == 'CollectableElement':
            imports.append('from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ElementCollection import CollectableElement')

        return imports

    def _generate_v2_class_code(self, class_info: Dict[str, Any], package_path: str) -> str:
        """Generate V2 class code with property-based dual API.

        This is a V2-specific generator that doesn't rely on V1 type_resolver.

        Args:
            class_info: Class information dictionary
            package_path: Package path (e.g., 'M2::AUTOSARTemplates::...')

        Returns:
            Generated Python class code
        """
        class_name = class_info['name']
        is_abstract = class_info.get('is_abstract', False)
        parent = class_info.get('parent') or 'ARObject'
        attributes = class_info.get('attributes', {})

        # Generate imports
        imports = self._generate_v2_imports(class_info, package_path)

        # Generate docstring
        docstring = _generate_docstring(class_info, package_path)

        # Class declaration
        # Don't include parent in bases if it's the same as class_name (e.g., ARObject inheriting from ARObject)
        bases = []
        if parent != class_name:  # Only add parent if it's not a self-reference
            bases.append(parent)
        if is_abstract:
            bases.append('ABC')

        # If no bases (e.g., ARObject with no parent), inherit from object implicitly
        if not bases:
            class_decl = f"class {class_name}:"
        else:
            class_decl = f"class {class_name}({', '.join(bases)}):"

        # Generate __init__ code
        has_short_name_init = False  # Simplified for now
        is_arobject_child = (parent == 'ARObject' and class_name != 'ARObject')
        init_code = _generate_init_code(
            class_name, docstring, is_abstract, has_short_name_init, is_arobject_child
        )

        # For now, use string annotations for ALL types to avoid import issues
        # This is a temporary workaround until all type definitions are added to package specs
        use_string_annotations = True

        # Generate property-based attributes
        attr_code = _generate_property_based_attributes(
            class_name, parent, attributes, use_string_annotations, frozenset()
        )

        # Generate property-based methods
        methods_code = _generate_property_based_methods(
            class_name, parent, attributes, use_string_annotations, frozenset()
        )

        # Combine all parts
        code_parts = imports + [''] + [class_decl, init_code, ''] + attr_code + [''] + methods_code

        return '\n'.join(code_parts)


# =============================================================================
# CLI Entry Point
# =============================================================================

def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        prog='generate_v2_models.py',
        description='Generate V2 AUTOSAR models from package specifications',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --all                    Generate all V2 models
  %(prog)s -p M2::Generic           Generate specific package
  %(prog)s --dry-run               Preview changes without writing
        """
    )

    parser.add_argument(
        '--all', '-a',
        action='store_true',
        help='Generate all V2 models'
    )

    parser.add_argument(
        '--package', '-p',
        type=str,
        metavar='PACKAGE',
        help='Specific package to generate (e.g., M2::AUTOSARTemplates::GenericStructure)'
    )

    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Preview changes without writing files'
    )

    return parser.parse_args()


def main():
    """Main entry point."""
    args = parse_args()

    if not args.all and not args.package:
        print("❌ Error: Please specify --all or --package")
        print("Use --help for usage information")
        sys.exit(1)

    generator = V2ModelGenerator(dry_run=args.dry_run)

    try:
        if args.all:
            generator.generate_all()
        elif args.package:
            generator.generate_all(specific_package=args.package)
    except KeyboardInterrupt:
        print("\n\n⚠️  Generation interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Fatal error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()

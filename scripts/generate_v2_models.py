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
from typing import Any, Dict, List, Optional, Set

# =============================================================================
# AUTOSAR Primitive Types
# =============================================================================
# These are the actual importable AUTOSAR primitive type classes from V1 PrimitiveTypes.py
# These need to be imported in V2 models because they are used in isinstance() checks
AUTOSAR_PRIMITIVE_TYPES: Set[str] = {
    'Identifier',
    'String',
    'NameToken',
    'Boolean',
    'Float',
    'Integer',
    'PositiveInteger',
    'RefType',
}

AUTOSAR_PRIMITIVE_TYPES_MODULE = (
    'armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes'
)

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


def _generate_enumeration_code(enum_info: Dict[str, Any], package_path: str, standalone: bool = True) -> str:
    """Generate Python code for an AUTOSAR enumeration.

    Args:
        enum_info: Enumeration information dictionary
        package_path: Package path (e.g., 'M2::AUTOSARTemplates::...')
        standalone: If True, generate as standalone file with imports; if False, generate just class code

    Returns:
        Generated Python code string
    """
    enum_name = enum_info.get('name', 'UnknownEnum')
    note = enum_info.get('note', '')
    literals = enum_info.get('literals', [])

    # Build docstring
    docstring_lines = [f"{enum_name} enumeration"]
    if note:
        docstring_lines.append("")
        docstring_lines.append(note)

    docstring_lines.append(f"\nPackage: {package_path}")
    docstring = '\n'.join(docstring_lines)

    # Build enum literal class attributes
    literal_lines = []
    for literal in literals:
        name = literal.get('name', '')
        index = literal.get('index', 0)
        description = literal.get('description', '')

        if name:
            # Add comment with description
            if description:
                # Clean up HTML tags in description and extra text
                desc_clean = description.replace('<br>', '\n').replace('<br/>', '\n')
                desc_clean = desc_clean.replace('&lt;', '<').replace('&gt;', '>')
                desc_clean = desc_clean.replace('&amp;', '&')
                # Remove trailing "Tags:" text if present
                if 'Tags:' in desc_clean:
                    desc_clean = desc_clean.split('Tags:')[0].strip()
                literal_lines.append(f'    # {desc_clean}')
            literal_lines.append(f'    {name} = "{index}"')
            literal_lines.append('')

    # Remove trailing empty line
    if literal_lines and literal_lines[-1] == '':
        literal_lines.pop()

    if standalone:
        # Standalone file with imports
        enum_code = f'''"""
AUTOSAR Enumeration - {enum_name}

{docstring}
"""
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
)


class {enum_name}(AREnum):
    """
    {docstring}
    """
{chr(10).join(literal_lines)}
'''
    else:
        # Just the class definition (for combined package files)
        enum_code = f'''class {enum_name}(AREnum):
    """
    {docstring}
    """
{chr(10).join(literal_lines)}
'''

    return enum_code


def _generate_primitive_code(prim_info: Dict[str, Any], package_path: str, standalone: bool = True) -> str:
    """Generate Python code for an AUTOSAR primitive type.

    Args:
        prim_info: Primitive information dictionary
        package_path: Package path (e.g., 'M2::AUTOSARTemplates::...')
        standalone: If True, generate as standalone file with imports; if False, generate just class code

    Returns:
        Generated Python code string
    """
    prim_name = prim_info.get('name', 'UnknownPrimitive')
    note = prim_info.get('note', '')
    attributes = prim_info.get('attributes', {})

    # Build docstring
    docstring_lines = [f"{prim_name} primitive type"]
    if note:
        docstring_lines.append("")
        docstring_lines.append(note)

    docstring_lines.append(f"\nPackage: {package_path}")

    docstring = '\n'.join(docstring_lines)

    # Determine the appropriate base class
    # Most primitives are type aliases that inherit from ARLiteral or ARType
    # For now, we'll use ARLiteral as the default base class
    base_class = 'ARLiteral'

    # Check if this is a string type (most primitives are strings)
    # If the name contains "String", "Name", "Identifier", "Token", etc., use ARLiteral
    # If it's a numeric type, use ARNumerical
    prim_lower = prim_name.lower()
    if any(x in prim_lower for x in ['integer', 'float', 'numerical', 'boolean']):
        base_class = 'ARNumerical'

    if standalone:
        # Standalone file with imports
        primitive_code = f'''"""
AUTOSAR Primitive Type - {prim_name}

{docstring}
"""
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    {base_class},
)


class {prim_name}({base_class}):
    """
    {docstring}
    """
    pass


'''
    else:
        # Just the class definition (for combined package files)
        primitive_code = f'''class {prim_name}({base_class}):
    """
    {docstring}
    """
    pass


'''

    return primitive_code


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

        # Load from class-package.json (primary source)
        class_package_json = packages_dir.parent / 'class-package.json'
        if class_package_json.exists():
            try:
                with open(class_package_json, 'r', encoding='utf-8') as f:
                    class_data = json.load(f)

                if 'types' in class_data and isinstance(class_data['types'], list):
                    for type_info in class_data['types']:
                        type_name = type_info.get('name')
                        python_file = type_info.get('python_file', '')
                        package_structure = type_info.get('package_structure', 'leaf')

                        if type_name and python_file:
                            # Convert python_file path to module path
                            # src/armodel/v2/models/M2/AUTOSARTemplates/.../PrimitiveTypes.py
                            # -> armodel.v2.models.M2.AUTOSARTemplates....PrimitiveTypes
                            module_path = python_file.replace('src/', '').replace('.py', '').replace('/', '.')
                            type_mapping[type_name] = module_path
            except Exception as e:
                print(f"Warning: Could not load class-package.json: {e}")

        # Scan all package JSON files (fallback) - only for types not in class-package.json
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
                    # Only add if not already in mapping (class-package.json is primary source)
                    for class_info in pkg_data['classes']:
                        class_name = class_info.get('name')
                        if class_name and class_name not in type_mapping:
                            module_path = self._class_to_module_path(pkg_name, class_name)
                            if module_path:
                                type_mapping[class_name] = module_path

                # Handle .enums.json files (list of enum objects)
                if 'enumerations' in pkg_data and isinstance(pkg_data['enumerations'], list):
                    pkg_name = pkg_data.get('package', '')
                    if not pkg_name:
                        continue

                    # Add enumerations to mapping with their individual module paths
                    # Only add if not already in mapping (class-package.json is primary source)
                    for enum_info in pkg_data['enumerations']:
                        enum_name = enum_info.get('name')
                        if enum_name and enum_name not in type_mapping:
                            module_path = self._class_to_module_path(pkg_name, enum_name)
                            if module_path:
                                type_mapping[enum_name] = module_path

                # Handle .primitives.json files (list of primitive objects)
                if 'primitives' in pkg_data and isinstance(pkg_data['primitives'], list):
                    pkg_name = pkg_data.get('package', '')
                    if not pkg_name:
                        continue

                    # Add primitives to mapping with their individual module paths
                    # Only add if not already in mapping (class-package.json is primary source)
                    for prim_info in pkg_data['primitives']:
                        prim_name = prim_info.get('name')
                        if prim_name and prim_name not in type_mapping:
                            module_path = self._class_to_module_path(pkg_name, prim_name)
                            if module_path:
                                type_mapping[prim_name] = module_path

                # Handle regular package files (dict of classes)
                elif 'classes' in pkg_data and isinstance(pkg_data['classes'], dict):
                    pkg_name = pkg_data.get('name', '')
                    if not pkg_name:
                        continue

                    # Add classes to mapping with their individual module paths
                    # Only add if not already in mapping (class-package.json is primary source)
                    for class_name in pkg_data['classes'].keys():
                        if class_name not in type_mapping:
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
        """Process a single package and generate a combined file with all types.

        Args:
            pkg: Package dictionary with 'name', 'file', 'classes', 'enumerations', 'primitives'
        """
        pkg_name = pkg.get('name', 'Unknown')
        classes = pkg.get('classes', {})
        enumerations = pkg.get('enumerations', {})
        primitives = pkg.get('primitives', {})

        if not (classes or enumerations or primitives):
            return

        print(f"📝 Processing package: {pkg_name}")
        if classes:
            print(f"   Classes: {len(classes)}")
        if enumerations:
            print(f"   Enumerations: {len(enumerations)}")
        if primitives:
            print(f"   Primitives: {len(primitives)}")

        # Generate ONE combined file for the package
        try:
            self._generate_package_file(pkg_name, classes, enumerations, primitives)
        except Exception as e:
            self.errors.append((pkg_name, "package", str(e)))
            print(f"   ❌ Error generating package file: {e}")

        print()

    def _generate_package_file(
        self,
        pkg_name: str,
        classes: Dict[str, Any],
        enumerations: Dict[str, Any],
        primitives: Dict[str, Any]
    ):
        """Generate a single combined file for all types in a package.

        Args:
            pkg_name: Package name (e.g., 'M2::AUTOSARTemplates::...')
            classes: Dictionary of class information
            enumerations: Dictionary of enumeration information
            primitives: Dictionary of primitive information
        """
        # Determine if this is a leaf or non-leaf package
        is_leaf = self._is_leaf_package(pkg_name)

        # Determine file path
        file_path = self._get_package_file_path(pkg_name, is_leaf)

        # Skip packages that are manually maintained (contain base classes)
        if self._is_manually_maintained_package(file_path):
            print(f"   ⏭️  Skipping manually maintained package: {file_path.name}")
            return

        if self.dry_run:
            print(f"   📄 Would create: {file_path}")
            self.generated_files.append(str(file_path))
            return

        # Create parent directories if needed
        file_path.parent.mkdir(parents=True, exist_ok=True)

        # Generate combined code for all types
        code = self._generate_combined_package_code(pkg_name, classes, enumerations, primitives, is_leaf)

        # Write to file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(code)

        self.generated_files.append(str(file_path))
        total_types = len(classes) + len(enumerations) + len(primitives)
        print(f"   ✅ Generated: {file_path.name} ({total_types} types)")

    def _is_manually_maintained_package(self, file_path: Path) -> bool:
        """Check if a package is manually maintained and should not be overwritten.

        Args:
            file_path: Path to the package file

        Returns:
            True if package is manually maintained, False otherwise
        """
        # If file doesn't exist, it's not manually maintained (yet)
        if not file_path.exists():
            return False

        # Check if file contains base class markers
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Markers for manually maintained base files
            base_class_markers = [
                'class ARType(ABC):',
                'class AREnum(',
                'class ARLiteral(',
                'class ARNumerical(',
                '# Manually maintained:',  # Comment marker for manually maintained files
            ]

            return any(marker in content for marker in base_class_markers)
        except Exception:
            return False

    def _is_leaf_package(self, pkg_name: str) -> bool:
        """Determine if a package is a leaf or non-leaf package.

        Args:
            pkg_name: Package name (e.g., 'M2::AUTOSARTemplates::...')

        Returns:
            True if leaf package (no subdirectories), False if non-leaf
        """
        # Convert package name to directory path
        dir_path = V2_MODELS_DIR / pkg_name.replace('::', '/')

        if not dir_path.exists():
            # Directory doesn't exist yet, treat as leaf
            return True

        if not dir_path.is_dir():
            # Not a directory, treat as leaf
            return True

        # Check for subdirectories (excluding __pycache__)
        subdirs = []
        for item in dir_path.iterdir():
            if item.is_dir() and not item.name.startswith('__'):
                subdirs.append(item.name)

        return len(subdirs) == 0

    def _get_package_file_path(self, pkg_name: str, is_leaf: bool) -> Path:
        """Get the file path for a package.

        Args:
            pkg_name: Package name (e.g., 'M2::AUTOSARTemplates::...')
            is_leaf: Whether this is a leaf package

        Returns:
            Path where the package file should be created
        """
        # Convert package name to directory path
        dir_path = V2_MODELS_DIR / pkg_name.replace('::', '/')

        # Get the last component of the package path
        package_short_name = pkg_name.split('::')[-1]

        if is_leaf:
            # Leaf package: Use PackageName.py
            file_path = dir_path.parent / f"{package_short_name}.py"
        else:
            # Non-leaf package: Use PackageName/__init__.py
            file_path = dir_path / "__init__.py"

        return file_path

    def _sort_classes_by_dependency(self, classes: Dict[str, Any]) -> List[str]:
        """Sort classes by dependency (parent classes before child classes).

        Uses topological sort to ensure that parent classes are defined before
        child classes that inherit from them.

        Args:
            classes: Dictionary of class information

        Returns:
            List of class names in dependency order
        """
        # Build dependency graph: {class_name: [parent_class_names]}
        graph = {}
        for class_name, class_info in classes.items():
            parent = class_info.get('parent')
            if parent and parent != 'ARObject' and parent in classes:
                # Only track dependencies for parent classes that are in the same file
                graph[class_name] = [parent]
            else:
                graph[class_name] = []

        # Topological sort using Kahn's algorithm
        in_degree = {class_name: len(parents) for class_name, parents in graph.items()}
        queue = [class_name for class_name, degree in in_degree.items() if degree == 0]
        result = []

        while queue:
            class_name = queue.pop(0)
            result.append(class_name)

            # Remove edges from this node
            for other_class, parents in graph.items():
                if class_name in parents:
                    parents.remove(class_name)
                    in_degree[other_class] -= 1
                    if in_degree[other_class] == 0:
                        queue.append(other_class)

        # If not all classes are in result, there's a cycle
        if len(result) != len(classes):
            # Fall back to original order if there's a cycle
            return list(classes.keys())

        return result

    def _generate_combined_package_code(
        self,
        pkg_name: str,
        classes: Dict[str, Any],
        enumerations: Dict[str, Any],
        primitives: Dict[str, Any],
        is_leaf: bool
    ) -> str:
        """Generate combined code for all types in a package.

        Args:
            pkg_name: Package name
            classes: Dictionary of class information
            enumerations: Dictionary of enumeration information
            primitives: Dictionary of primitive information
            is_leaf: Whether this is a leaf package

        Returns:
            Combined Python code string
        """
        code_parts = []

        # Add file header
        package_short_name = pkg_name.split('::')[-1]
        code_parts.append(f'"""')
        code_parts.append(f'AUTOSAR Package - {package_short_name}')
        code_parts.append(f'')
        code_parts.append(f'Package: {pkg_name}')
        code_parts.append(f'"""\n')

        # Collect all imports needed by all types in this package
        all_imports = self._collect_package_imports(pkg_name, classes, enumerations, primitives)

        # Add imports section (already formatted and sorted)
        if all_imports:
            code_parts.append(all_imports)
            code_parts.append('')

        # Generate code for each type
        # 1. Classes (sorted by dependency to ensure parents are defined before children)
        sorted_class_names = self._sort_classes_by_dependency(classes)
        for class_name in sorted_class_names:
            class_info = classes[class_name]
            code_parts.append('\n')
            code_parts.append(self._generate_v2_class_code(class_info, pkg_name, skip_imports=True))

        # 2. Enumerations
        for enum_name, enum_info in enumerations.items():
            code_parts.append('\n')
            code_parts.append(_generate_enumeration_code(enum_info, pkg_name, standalone=False))

        # 3. Primitives
        for prim_name, prim_info in primitives.items():
            code_parts.append('\n')
            code_parts.append(_generate_primitive_code(prim_info, pkg_name, standalone=False))

        return '\n'.join(code_parts)

    def _collect_package_imports(
        self,
        pkg_name: str,
        classes: Dict[str, Any],
        enumerations: Dict[str, Any],
        primitives: Dict[str, Any]
    ) -> str:
        """Collect all imports needed by all types in a package.

        Groups imports by source module and formats them as block imports.

        Args:
            pkg_name: Package name
            classes: Dictionary of class information
            enumerations: Dictionary of enumeration information
            primitives: Dictionary of primitive information

        Returns:
            Single string containing all formatted import statements
        """
        from collections import defaultdict

        # Get the module path for this package
        package_module_path = self._get_package_module_path(pkg_name)

        # Group imports by module path
        # Structure: {module_path: set(type_names)}
        stdlib_imports = {
            'abc': {'ABC', 'abstractmethod'},
            'typing': {'List', 'Optional', 'Dict', 'Any'},
        }

        local_imports = defaultdict(set)  # {module_path: {type_names}}

        # Collect imports from each class
        for class_info in classes.values():
            # Add parent class import
            parent = class_info.get('parent') or 'ARObject'
            class_name = class_info['name']

            parent_imports = self._get_import_for_type(parent, class_name, package_module_path)
            for module_path, type_names in parent_imports.items():
                local_imports[module_path].update(type_names)

            # Collect AUTOSAR primitive types used in attributes
            # These need to be imported for isinstance() checks (not just string annotations)
            attributes = class_info.get('attributes', {})
            for attr_name, attr_info in attributes.items():
                attr_type = attr_info.get('type', 'Any')
                is_ref = attr_info.get('is_ref', False)
                
                # Add AUTOSAR primitive types
                if attr_type in AUTOSAR_PRIMITIVE_TYPES:
                    local_imports[AUTOSAR_PRIMITIVE_TYPES_MODULE].add(attr_type)
                
                # Add RefType for reference attributes (used in with_ methods without quotes)
                if is_ref:
                    local_imports[AUTOSAR_PRIMITIVE_TYPES_MODULE].add('RefType')

        # Add imports for enumerations
        if enumerations:
            module_path = 'armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes'
            local_imports[module_path].add('AREnum')

        # Add imports for primitives
        if primitives:
            module_path = 'armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes'
            local_imports[module_path].add('ARLiteral')
            local_imports[module_path].add('ARNumerical')

        # Format imports as complete blocks
        import_blocks = []

        # 1. Stdlib imports (use simple format for clarity)
        for module in sorted(stdlib_imports.keys()):
            types = sorted(stdlib_imports[module])
            import_blocks.append(f'from {module} import {", ".join(types)}')

        # 2. Local imports (use block style for consistency)
        for module_path in sorted(local_imports.keys()):
            types = sorted(local_imports[module_path])

            # Use block style for multi-import statements
            block_lines = [f'from {module_path} import (']
            block_lines.extend(f'    {type_name},' for type_name in types)
            block_lines.append(')')
            import_blocks.append('\n'.join(block_lines))

        # Join all import blocks with newlines
        return '\n'.join(import_blocks)

    def _get_import_for_type(self, type_name: str, current_class: str, current_module_path: Optional[str] = None) -> Dict[str, set]:
        """Get import information for a given type.

        Args:
            type_name: Type name to import
            current_class: Current class being generated (to avoid self-import)
            current_module_path: Module path of current class (to avoid same-module imports)

        Returns:
            Dictionary mapping module paths to sets of type names to import
        """
        imports = {}

        # Skip self-imports
        if type_name == current_class:
            return imports

        # Map type names to their import paths
        type_to_import = self.type_to_package.get(type_name)

        if type_to_import:
            # Skip same-module imports (even for parent classes)
            # Since we use topological sort, parent classes are defined before child classes
            # in the same file, so Python will find them without needing imports
            if current_module_path and type_to_import == current_module_path:
                # Skip same-module imports - the type is defined in the same file
                return imports
            
            # Type is in a different module, add its import
            # type_to_import is the full module path
            imports[type_to_import] = {type_name}
        else:
            # Type might be in the same package, check if it's in the current package
            # For now, skip types not in mapping (could be same-package or stdlib)
            pass

        return imports

    def _get_package_module_path(self, pkg_name: str) -> str:
        """Get the Python module path for a package.

        Args:
            pkg_name: AUTOSAR package name (e.g., 'M2::AUTOSARTemplates::...')

        Returns:
            Python module path
        """
        # Convert to Python path
        # M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::ARPackage
        # -> armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage
        parts = pkg_name.split('::')
        if parts[0] == 'M2':
            py_parts = ['armodel', 'v2', 'models'] + parts
            return '.'.join(py_parts)
        return pkg_name

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

    def _generate_enumeration_file(self, pkg_name: str, enum_name: str, enum_info: Dict[str, Any]):
        """Generate a single enumeration file.

        Args:
            pkg_name: Package name
            enum_name: Enumeration name
            enum_info: Enumeration information dictionary
        """
        # Determine file path (same pattern as classes)
        file_path = self._get_file_path(pkg_name, enum_name)

        if self.dry_run:
            print(f"   📄 Would create: {file_path}")
            self.generated_files.append(str(file_path))
            return

        # Create parent directories
        file_path.parent.mkdir(parents=True, exist_ok=True)

        # Generate enumeration code
        code = _generate_enumeration_code(enum_info, pkg_name)

        # Write to file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(code)

        self.generated_files.append(str(file_path))
        print(f"   ✅ Generated enumeration: {enum_name}")

    def _generate_primitive_file(self, pkg_name: str, prim_name: str, prim_info: Dict[str, Any]):
        """Generate a single primitive file.

        Args:
            pkg_name: Package name
            prim_name: Primitive name
            prim_info: Primitive information dictionary
        """
        # Determine file path (same pattern as classes)
        file_path = self._get_file_path(pkg_name, prim_name)

        if self.dry_run:
            print(f"   📄 Would create: {file_path}")
            self.generated_files.append(str(file_path))
            return

        # Create parent directories
        file_path.parent.mkdir(parents=True, exist_ok=True)

        # Generate primitive code
        code = _generate_primitive_code(prim_info, pkg_name)

        # Write to file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(code)

        self.generated_files.append(str(file_path))
        print(f"   ✅ Generated primitive: {prim_name}")

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

        Automatically calculates imports from:
        - Parent class
        - Attribute types
        - AUTOSAR primitive types (for isinstance() checks)
        - Uses class-package.json to determine import paths

        Args:
            class_info: Class information dictionary
            package_path: Package path (e.g., 'M2::AUTOSARTemplates::...')

        Returns:
            List of import statement strings
        """
        from collections import defaultdict

        imports = []
        class_name = class_info['name']
        parent = class_info.get('parent') or 'ARObject'
        attributes = class_info.get('attributes', {})

        # Get the module path for this class
        class_module_path = self._get_package_module_path(package_path)

        # Group imports by module path
        stdlib_imports = {
            'abc': {'ABC', 'abstractmethod'},
            'typing': {'List', 'Optional', 'Dict', 'Any'},
        }

        local_imports = defaultdict(set)  # {module_path: {type_names}}

        # Add parent class import
        parent_imports = self._get_import_for_type(parent, class_name, class_module_path)
        for module_path, type_names in parent_imports.items():
            local_imports[module_path].update(type_names)

        # Collect AUTOSAR primitive types used in attributes
        # These need to be imported for isinstance() checks (not just string annotations)
        primitive_types_used = set()
        for attr_name, attr_info in attributes.items():
            attr_type = attr_info.get('type', 'Any')
            if attr_type in AUTOSAR_PRIMITIVE_TYPES:
                primitive_types_used.add(attr_type)

        # Add AUTOSAR primitive types import if any are used
        if primitive_types_used:
            local_imports[AUTOSAR_PRIMITIVE_TYPES_MODULE].update(primitive_types_used)

        # Format imports as complete blocks
        # 1. Stdlib imports (use simple format for clarity)
        for module in sorted(stdlib_imports.keys()):
            types = sorted(stdlib_imports[module])
            imports.append(f'from {module} import {", ".join(types)}')

        # 2. Local imports (use block style for consistency)
        for module_path in sorted(local_imports.keys()):
            types = sorted(local_imports[module_path])

            # Use block style for multi-import statements
            block_lines = [f'from {module_path} import (']
            block_lines.extend(f'    {type_name},' for type_name in types)
            block_lines.append(')')
            imports.append('\n'.join(block_lines))

        return imports

    def _generate_v2_class_code(self, class_info: Dict[str, Any], package_path: str, skip_imports: bool = False) -> str:
        """Generate V2 class code with property-based dual API.

        This is a V2-specific generator that doesn't rely on V1 type_resolver.

        Args:
            class_info: Class information dictionary
            package_path: Package path (e.g., 'M2::AUTOSARTemplates::...')
            skip_imports: If True, skip import generation (for combined package files)

        Returns:
            Generated Python class code
        """
        class_name = class_info['name']
        is_abstract = class_info.get('is_abstract', False)
        parent = class_info.get('parent') or 'ARObject'
        attributes = class_info.get('attributes', {})

        # Generate imports (only if not skipping)
        if not skip_imports:
            imports = self._generate_v2_imports(class_info, package_path)
        else:
            imports = []

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

        # Use string annotations for ALL types to avoid circular imports (CODING_RULE_V2_00002)
        # This is required because many types have circular dependencies
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

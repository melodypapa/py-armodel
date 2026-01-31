import sys
#!/usr/bin/env python3
"""
Package Implementation Fix Script for py-armodel

This script fixes missing AUTOSAR M2 package implementations and generates test cases.
It performs the following:
- Generates missing classes based on requirements
- Generates pytest test cases for generated classes
- Runs ruff check on generated code
- Runs pytest to verify generated code

Usage:
    python scripts/fix-package-implementation.py
    python scripts/fix-package-implementation.py --package M2::AUTOSARTemplates::BswModuleTemplate
    python scripts/fix-package-implementation.py -p M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior
    python scripts/fix-package-implementation.py --package M2::AUTOSARTemplates::BswModuleTemplate --dry-run
"""

import argparse
import ast
import json
import subprocess
from pathlib import Path
from typing import Dict, List, Optional, Any, Set, Tuple


def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description='Fix missing AUTOSAR M2 package implementations and generate tests',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --package M2::xxx::xxx                   Fix single package
  %(prog)s -p M2::xxx::xxx::xxx                     Fix subpackage
  %(prog)s --package M2::xxx::xxx --dry-run         Preview fixes
  %(prog)s --package M2::xxx::xxx --merge           Merge updates into existing classes
        """
    )
    parser.add_argument(
        '--package', '-p',
        type=str,
        help='Specific package to fix (format: M2::xxx::xxxx)'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Preview fixes without modifying files'
    )
    parser.add_argument(
        '--merge',
        action='store_true',
        help='Merge generated code into existing classes (preserves manual changes)'
    )
    return parser.parse_args()


def load_requirements_index(requirements_dir: Path) -> Dict[str, Any]:
    """Load the requirements index.json file."""
    index_file = requirements_dir / 'index.json'
    if not index_file.exists():
        raise FileNotFoundError(f"Requirements index file not found: {index_file}")
    
    with open(index_file, 'r', encoding='utf-8') as f:
        return json.load(f)


def load_package_json(requirements_dir: Path, package_file: str) -> Optional[Dict[str, Any]]:
    """Load a package JSON file."""
    if package_file.startswith('packages/'):
        package_path = requirements_dir / package_file
    else:
        package_path = requirements_dir / 'packages' / package_file
    
    if not package_path.exists():
        print(f"Warning: Package file not found: {package_path}")
        return None
    
    with open(package_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def get_all_packages(requirements_dir: Path, specific_package: Optional[str] = None) -> List[Dict[str, Any]]:
    """Get all packages from requirements, optionally filtered by specific package."""
    index = load_requirements_index(requirements_dir)
    packages = []
    
    def process_package(pkg_data: Any, parent_path: str = '') -> List[Dict[str, Any]]:
        """Recursively process packages."""
        pkg_list = []
        
        if isinstance(pkg_data, str):
            pkg_name = pkg_data
            pkg_file = None
        else:
            pkg_name = pkg_data.get('name', '')
            pkg_file = pkg_data.get('file', '')
        
        if parent_path:
            full_path = f"{parent_path}::{pkg_name}"
        else:
            full_path = pkg_name
        
        should_process_subpackages = False
        if specific_package:
            exact_match = full_path == specific_package
            starts_with = full_path.startswith(specific_package + '::')
            parent_of = specific_package.startswith(full_path + '::')
            
            if exact_match:
                should_process_subpackages = True
            elif starts_with:
                should_process_subpackages = True
            elif parent_of:
                should_process_subpackages = True
            else:
                return pkg_list
        else:
            should_process_subpackages = True
        
        pkg_json = None
        if pkg_file:
            if pkg_file.startswith('packages/'):
                pkg_json = load_package_json(requirements_dir, pkg_file)
            else:
                pkg_json = load_package_json(requirements_dir, f"packages/{pkg_file}")
        elif not isinstance(pkg_data, str) and 'path' in pkg_data:
            pkg_path = pkg_data['path'].replace('::', '_')
            pkg_json = load_package_json(requirements_dir, f"packages/{pkg_path}.json")
        
        if pkg_json:
            classes = {}
            enumerations = {}
            
            if 'files' in pkg_json and 'classes' in pkg_json['files']:
                classes_file = pkg_json['files']['classes']
                if classes_file:
                    if classes_file.startswith('packages/'):
                        classes_path = requirements_dir / classes_file
                    else:
                        classes_path = requirements_dir / 'packages' / classes_file
                    if classes_path.exists():
                        with open(classes_path, 'r', encoding='utf-8') as f:
                            classes_data = json.load(f)
                            for cls in classes_data.get('classes', []):
                                classes[cls['name']] = cls
            
            if 'files' in pkg_json and 'enumerations' in pkg_json['files']:
                enums_file = pkg_json['files']['enumerations']
                if enums_file:
                    if enums_file.startswith('packages/'):
                        enums_path = requirements_dir / enums_file
                    else:
                        enums_path = requirements_dir / 'packages' / enums_file
                    if enums_path.exists():
                        with open(enums_path, 'r', encoding='utf-8') as f:
                            enums_data = json.load(f)
                            for enum in enums_data.get('enumerations', []):
                                enumerations[enum['name']] = enum
            
            if classes or enumerations or (specific_package and full_path == specific_package):
                pkg_list.append({
                    'name': full_path,
                    'file': pkg_file or f"packages/{pkg_data.get('path', pkg_name).replace('::', '_')}.json",
                    'classes': classes,
                    'enumerations': enumerations
                })
            
            if 'subpackages' in pkg_json and should_process_subpackages:
                for subpkg in pkg_json['subpackages']:
                    pkg_list.extend(process_package(subpkg, full_path))
        
        return pkg_list
    
    for pkg in index.get('packages', []):
        packages.extend(process_package(pkg, ''))
    
    return packages


# Import functions from compare-package-implementation.py
# We'll inline the key functions to keep this script self-contained

# Global dry_run flag
dry_run_mode = False

# Global cache to track created classes
created_classes = set()

# Type index cache for fast lookups
_type_index_cache: Optional[Dict[str, str]] = None
_wildcard_exports_cache: Optional[Dict[str, Set[str]]] = None

# Track generation issues
generation_report = {
    'unresolved_types': {},  # class_name: [(type_name, context), ...]
    'warnings': [],
    'errors': [],
}


def build_type_index(project_root: Path) -> None:
    """Build a global index of all types and their import paths."""
    global _type_index_cache, _wildcard_exports_cache

    _type_index_cache = {}
    _wildcard_exports_cache = {}

    models_dir = project_root / 'src' / 'armodel' / 'models' / 'M2'

    print("  Building type index...")

    for py_file in models_dir.rglob('*.py'):
        try:
            with open(py_file, 'r', encoding='utf-8') as f:
                content = f.read()

            # Extract class names from file
            try:
                tree = ast.parse(content, filename=str(py_file))
                for node in ast.walk(tree):
                    if isinstance(node, ast.ClassDef):
                        class_name = node.name
                        # Only store first occurrence (most specific)
                        if class_name not in _type_index_cache:
                            file_rel_path = py_file.relative_to(models_dir)
                            import_path = _generate_import_path(models_dir, file_rel_path, class_name)
                            _type_index_cache[class_name] = import_path
            except SyntaxError:
                # Skip files with syntax errors
                pass

        except (IOError, UnicodeDecodeError):
            continue

    print(f"  Indexed {len(_type_index_cache)} types")


def _generate_import_path(models_dir: Path, file_rel_path: Path, class_name: str) -> str:
    """Generate correct import path considering wildcard exports."""
    # Check if class is re-exported via wildcard in parent __init__.py
    if file_rel_path.name != '__init__.py':
        # For a class in Foo/Bar.py, check Foo/__init__.py
        parent_init = file_rel_path.parent.parent / '__init__.py'
        module_name = file_rel_path.stem

        while parent_init.is_relative_to(models_dir):
            init_file = models_dir / parent_init
            if init_file.exists():
                with open(init_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                # Check for wildcard import from this module
                if f'from .{module_name} import *' in content:
                    # Class is re-exported - use parent module
                    parts = list(parent_init.relative_to(models_dir).parent.parts)
                    module_path = 'armodel.models.M2.' + '.'.join(parts)
                    return f'from {module_path} import {class_name}'
                # Check for direct import
                if f'from .{module_name} import {class_name}' in content:
                    parts = list(parent_init.relative_to(models_dir).parent.parts)
                    module_path = 'armodel.models.M2.' + '.'.join(parts)
                    return f'from {module_path} import {class_name}'

            # Go up one level
            parent_init = parent_init.parent.parent / '__init__.py'
            if parent_init == models_dir / '__init__.py':
                break

    # Default: direct import from the file
    if file_rel_path.name == '__init__.py':
        parts = list(file_rel_path.parent.parts)
    else:
        parts = list(file_rel_path.parent.parts) + [file_rel_path.stem]

    module_path = 'armodel.models.M2.' + '.'.join(parts)
    return f'from {module_path} import {class_name}'


def find_type_in_codebase_cached(project_root: Path, type_name: str) -> Optional[str]:
    """Find a type in the codebase using cached index."""
    if _type_index_cache is None:
        build_type_index(project_root)

    return _type_index_cache.get(type_name)
def generate_imports(class_info: Dict[str, Any], package_path: str, project_root: Path, requirements_dir: Path, class_name: str = '') -> List[str]:
    """Generate necessary import statements for a class based on its attributes and structure."""
    imports = set()

    is_abstract = class_info.get('is_abstract', False)
    parent = class_info.get('parent') or 'ARObject'  # Handle null/None/empty parent
    attributes = class_info.get('attributes', {})

    typing_imports = set()

    if is_abstract:
        imports.add('from abc import ABC')

    # Import ARObject if needed for __init__ signature or for attributes
    needs_ar_object = (
        (not is_abstract or (is_abstract and any(attr_info.get('multiplicity') in ['*', '0..1'] for attr_info in attributes.values()))) or
        _parent_has_init_args(parent)  # parent has (parent, short_name) params
    )
    if needs_ar_object:
        imports.add('from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject')

    # Import RefType if any attribute has is_ref: true
    has_ref_attributes = any(attr_info.get('is_ref', False) for attr_info in attributes.values())
    if has_ref_attributes:
        imports.add('from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType')

    # Try to find parent class in codebase
    parent_import = find_type_in_codebase_cached(project_root, parent)
    if parent_import:
        imports.add(parent_import)
    else:
        # Try to create missing parent class from JSON
        if parent not in ['Any', 'ARObject']:
            created = create_missing_class_from_json(project_root, requirements_dir, parent)
            if created:
                print(f"  ℹ️  Created missing parent class: {parent}")
            else:
                # Track unresolved parent
                if class_name:
                    _track_unresolved_type(class_name, parent, 'parent class')
                print(f"  ⚠️  Parent class '{parent}' not found in codebase or JSON (using Any)")

    for attr_name, attr_info in attributes.items():
        attr_type = attr_info.get('type', 'Any')
        multiplicity = attr_info.get('multiplicity', '1')

        if multiplicity == '*':
            typing_imports.add('List')
        elif multiplicity == '0..1':
            typing_imports.add('Optional')

        # Skip self-referencing types (when class has attribute of its own type)
        if attr_type == class_name:
            continue

        # Try to find type in codebase
        type_import = find_type_in_codebase_cached(project_root, attr_type)
        if type_import:
            # Filter out self-imports (importing from the same file)
            if f' import {class_name}' not in type_import:
                imports.add(type_import)
        elif attr_type not in ['Any', 'str', 'int', 'float', 'bool']:
            # Try to create missing class from JSON
            created = create_missing_class_from_json(project_root, requirements_dir, attr_type)
            if created:
                print(f"  ℹ️  Created missing type class: {attr_type}")
                # Try to find it again after creation
                type_import = find_type_in_codebase_cached(project_root, attr_type)
                if type_import:
                    if f' import {class_name}' not in type_import:
                        imports.add(type_import)
                else:
                    if class_name:
                        _track_unresolved_type(class_name, attr_type, f'attribute {attr_name}')
                    print(f"  ⚠️  Type '{attr_type}' for attribute '{attr_name}' not found (using Any)")
                    attr_info['type'] = 'Any'
                    typing_imports.add('Any')
            else:
                if class_name:
                    _track_unresolved_type(class_name, attr_type, f'attribute {attr_name}')
                print(f"  ⚠️  Type '{attr_type}' for attribute '{attr_name}' not found (using Any)")
                attr_info['type'] = 'Any'
                typing_imports.add('Any')

    if typing_imports:
        imports.add(f'from typing import {", ".join(sorted(typing_imports))}')

    return sorted(list(imports))


def _track_unresolved_type(class_name: str, type_name: str, context: str) -> None:
    """Track an unresolved type reference."""
    if class_name not in generation_report['unresolved_types']:
        generation_report['unresolved_types'][class_name] = []
    generation_report['unresolved_types'][class_name].append((type_name, context))


def find_type_in_codebase(project_root: Path, type_name: str, current_package_path: str) -> Optional[str]:
    """Find a type in the codebase and return the absolute import path."""
    models_dir = project_root / 'src' / 'armodel' / 'models' / 'M2'
    
    for py_file in models_dir.rglob('*.py'):
        try:
            with open(py_file, 'r', encoding='utf-8') as f:
                file_content = f.read()
            
            if f'class {type_name}(' in file_content:
                file_rel_path = py_file.relative_to(models_dir)
                
                # Convert file path to module path (absolute import)
                if py_file.name == '__init__.py':
                    module_parts = list(file_rel_path.parent.parts) if file_rel_path.parent != Path('.') else []
                    module_path = 'armodel.models.M2.' + '.'.join(module_parts) if module_parts else 'armodel.models.M2'
                else:
                    module_parts = list(file_rel_path.parent.parts) if file_rel_path.parent != Path('.') else []
                    module_path = 'armodel.models.M2.' + '.'.join(module_parts) if module_parts else 'armodel.models.M2'
                    module_path += f'.{file_rel_path.stem}'
                
                return f'from {module_path} import {type_name}'
        except (IOError, UnicodeDecodeError):
            continue
    
    return None


def find_class_in_requirements(requirements_dir: Path, type_name: str) -> Optional[Dict[str, Any]]:
    """Find a class definition in the requirements JSON files."""
    index = load_requirements_index(requirements_dir)
    
    def search_packages(pkg_data: Any, parent_path: str = '') -> Optional[Dict[str, Any]]:
        """Recursively search for a class in packages."""
        if isinstance(pkg_data, str):
            pkg_name = pkg_data
            pkg_file = None
        else:
            pkg_name = pkg_data.get('name', '')
            pkg_file = pkg_data.get('file', '')
        
        if parent_path:
            full_path = f"{parent_path}::{pkg_name}"
        else:
            full_path = pkg_name
        
        pkg_json = None
        if pkg_file:
            if pkg_file.startswith('packages/'):
                pkg_json = load_package_json(requirements_dir, pkg_file)
            else:
                pkg_json = load_package_json(requirements_dir, f"packages/{pkg_file}")
        elif not isinstance(pkg_data, str) and 'path' in pkg_data:
            pkg_path = pkg_data['path'].replace('::', '_')
            pkg_json = load_package_json(requirements_dir, f"packages/{pkg_path}.json")
        
        if pkg_json and 'files' in pkg_json and 'classes' in pkg_json['files']:
            classes_file = pkg_json['files']['classes']
            if classes_file:
                if classes_file.startswith('packages/'):
                    classes_path = requirements_dir / classes_file
                else:
                    classes_path = requirements_dir / 'packages' / classes_file
                if classes_path.exists():
                    with open(classes_path, 'r', encoding='utf-8') as f:
                        classes_data = json.load(f)
                        for cls in classes_data.get('classes', []):
                            if cls['name'] == type_name:
                                return {'class_info': cls, 'package_path': full_path}
        
        if pkg_json and 'subpackages' in pkg_json:
            for subpkg in pkg_json['subpackages']:
                result = search_packages(subpkg, full_path)
                if result:
                    return result
        
        return None
    
    for pkg in index.get('packages', []):
        result = search_packages(pkg, '')
        if result:
            return result
    
    return None


def create_missing_class_from_json(project_root: Path, requirements_dir: Path, type_name: str) -> bool:
    """Create a missing class from JSON requirements if found."""
    if type_name in created_classes:
        return True

    created_classes.add(type_name)

    class_data = find_class_in_requirements(requirements_dir, type_name)

    if not class_data:
        return False

    class_info = class_data['class_info']
    package_path = class_data['package_path']

    # Determine the file location
    if package_path.startswith('M2::'):
        relative = package_path[4:].replace('::', '/')
        package_dir = project_root / 'src' / 'armodel' / 'models' / 'M2' / relative
        # Check if package file exists (e.g., BswBehavior.py)
        package_file = package_dir.parent / f'{package_dir.name}.py'
    else:
        relative = package_path.replace('::', '/')
        package_dir = project_root / 'src' / 'armodel' / 'models' / relative
        package_file = package_dir.parent / f'{package_dir.name}.py'

    # Check if this package is implemented as a single file (not a directory)
    if package_file.exists():
        print(f"  ⚠️  Package is a single file ({package_file.name}), cannot create {type_name}")
        # Don't track as error since this is expected for some packages
        return False

    class_file = package_dir / f'{type_name}.py'

    # Skip if already exists
    if class_file.exists():
        # Update cache for existing class too
        _update_cache_for_new_class(project_root, type_name, package_path)
        return True

    if dry_run_mode:
        print(f"  [Would create missing class from JSON: {type_name}]")
        # Still update cache for dry-run so subsequent lookups work
        _update_cache_for_new_class(project_root, type_name, package_path)
        return True

    try:
        package_dir.mkdir(parents=True, exist_ok=True)
        code = generate_class_code(class_info, package_path, project_root, requirements_dir)

        # Validate code before writing
        is_valid, errors = validate_code(code, type_name)
        if not is_valid:
            print(f"  ✗ Validation failed for {type_name}:")
            for error in errors:
                print(f"    {error}")
            generation_report['errors'].append(f"{type_name}: {'; '.join(errors)}")
            return False

        with open(class_file, 'w', encoding='utf-8') as f:
            f.write(code + '\n')

        # Update cache with new class
        _update_cache_for_new_class(project_root, type_name, package_path)

        # Update __init__.py
        parent_init = package_dir / '__init__.py'
        if parent_init.exists():
            with open(parent_init, 'r', encoding='utf-8') as f:
                init_content = f.read()
            if f'from .{type_name} import {type_name}' not in init_content:
                with open(parent_init, 'a', encoding='utf-8') as f:
                    f.write(f'\nfrom .{type_name} import {type_name}\n')

        # Generate test case for the imported class
        module_path = f'armodel.models.M2.{package_path[4:].replace("::", ".")}.{type_name}'
        test_dir = project_root / 'tests' / 'test_armodel' / 'models' / 'M2' / relative
        test_file = test_dir / f'test_{type_name}.py'

        test_code = generate_test_case(type_name, class_info, package_path, module_path)

        if dry_run_mode:
            print(f"  [Would create test file: {test_file.relative_to(project_root)}]")
        else:
            test_dir.mkdir(parents=True, exist_ok=True)
            with open(test_file, 'w', encoding='utf-8') as f:
                f.write(test_code + '\n')

            test_parent_init = test_dir / '__init__.py'
            if not test_parent_init.exists():
                with open(test_parent_init, 'w', encoding='utf-8') as f:
                    f.write('')

        return True
    except Exception as e:
        print(f"  ✗ Error creating class '{type_name}': {e}")
        generation_report['errors'].append(f"{type_name}: {e}")
        return False


def _update_cache_for_new_class(project_root: Path, type_name: str, package_path: str) -> None:
    """Update the type index cache with a newly created class."""
    if _type_index_cache is None:
        return

    # Calculate file path for new class
    if package_path.startswith('M2::'):
        relative = package_path[4:].replace('::', '/')
    else:
        relative = package_path.replace('::', '/')

    models_dir = project_root / 'src' / 'armodel' / 'models' / 'M2'
    file_rel_path = models_dir / relative / f'{type_name}.py'

    # Generate import path
    import_path = _generate_import_path(models_dir, file_rel_path.relative_to(models_dir), type_name)

    # Update cache
    _type_index_cache[type_name] = import_path


# Parent classes that have __init__(parent, short_name) signature
# Based on comprehensive analysis of the codebase
_PARENTS_WITH_INIT_ARGS = {
    # Core AUTOSAR hierarchy (in inheritance order)
    'ARObject',  # Base - has no-arg __init__, but children override it
    'Referrable',
    'MultilanguageReferrable',
    'Identifiable',
    'ARElement',
    'AtpClassifier',
    'AtpType',
    'AtpPrototype',
    'AtpStructureElement',
    'AtpBlueprintable',
    # Template classes
    'ServiceNeeds',
    # Behavior classes
    'InternalBehavior',
    'Implementation',
    'SwcInternalBehavior',
    'BswInternalBehavior',
    'ExecutableEntity',
    # Component classes
    'PortInterface',
    'SwComponentType',
    'PortPrototype',
    'AbstractProvidedPortPrototype',
    'AbstractRequiredPortPrototype',
    'PPortPrototype',
    'RPortPrototype',
    'PRPortPrototype',
    # Data types
    'ApplicationDataType',
    'ImplementationDataType',
    'AutosarDataType',
    # Common structure
    'PackageableElement',
    'ImplementationProps',
    'SwcBswMapping',
    # Container classes
    'CollectableElement',
    'ElementCollection',
    'ARPackage',  # Special container with factory methods
}


def _parent_has_init_args(parent: str) -> bool:
    """Check if parent class has __init__(parent, short_name) signature."""
    return parent in _PARENTS_WITH_INIT_ARGS


def _is_container_class(class_name: str, parent: str, attributes: Dict[str, Any]) -> bool:
    """Check if a class should have container management methods.

    Returns True for classes that:
    - Inherit from CollectableElement, ElementCollection, or ARPackage
    - Have attributes ending with 's' (suggesting collections)
    """
    # Check parent class
    container_parents = {
        'CollectableElement', 'ElementCollection', 'ARPackage',
        'AtpStructureElement', 'Identifiable', 'ARElement'
    }

    if parent in container_parents:
        return True

    # Check if class name suggests it's a container
    container_suffixes = [
        'Set', 'Group', 'Collection', 'Mapping', 'Definitions',
        'Elements', 'Instances', 'Mappings', 'Sequence'
    ]

    for suffix in container_suffixes:
        if class_name.endswith(suffix):
            return True

    # Check for list-type attributes that suggest container behavior
    for attr_name, attr_info in attributes.items():
        if attr_info.get('multiplicity') == '*':
            # Has list attribute - likely a container
            return True

    return False


def _should_have_addElement_method(class_name: str, parent: str) -> bool:
    """Check if a class should have addElement-style factory methods."""
    # These classes typically have create* methods for each element type
    factory_parents = {
        'ARPackage',
        'AtpStructureElement',
        'Identifiable',
        'ARElement',
        'InternalBehavior',
        'SwcInternalBehavior',
        'BswInternalBehavior',
    }
    return parent in factory_parents


def _should_have_create_methods(class_name: str, parent: str) -> bool:
    """Check if a class should have createXxxx methods (i.e., inherits from Identifiable).

    Create methods are only for classes that:
    - Inherit from Identifiable (which has elements collection and addElement method)
    - Are container classes that own child objects
    """
    create_method_parents = {
        'Identifiable',
        'ARPackage',
        'ARElement',
        'InternalBehavior',
        'SwcInternalBehavior',
        'BswInternalBehavior',
        'Implementation',
        'AUTOSAR',
        'AtpStructureElement',
        'CollectableElement',
    }
    return parent in create_method_parents


def generate_class_code(class_info: Dict[str, Any], package_path: str, project_root: Path, requirements_dir: Path) -> str:
    """Generate Python class code from requirements JSON."""
    class_name = class_info['name']
    is_abstract = class_info.get('is_abstract', False)
    parent = class_info.get('parent') or 'ARObject'  # Handle null/None/empty parent
    attributes = class_info.get('attributes', {})
    note = class_info.get('note', '')
    sources = class_info.get('sources', [])

    imports = generate_imports(class_info, package_path, project_root, requirements_dir, class_name)
    
    # Generate docstring
    docstring_lines = []
    docstring_lines.append('    """')
    if note:
        docstring_lines.append(f'    {note}')
    
    if sources:
        docstring_lines.append('    ')
        docstring_lines.append('    Sources:')
        for source in sources:
            docstring_lines.append(f'      - {source.get("pdf_file", "")} (Page {source.get("page_number", "")}, {source.get("autosar_standard", "")} {source.get("standard_release", "")})')
    
    docstring_lines.append('    """')
    docstring = '\n'.join(docstring_lines)
    
    bases = [parent]
    if is_abstract:
        bases.append('ABC')
    
    class_decl = f"class {class_name}({', '.join(bases)}):"

    # Check if parent has __init__(parent, short_name)
    parent_has_args = _parent_has_init_args(parent)
    # ARObject is special: it has no-arg init but children have (parent, short_name)
    is_arobject_child = (parent == 'ARObject')

    if is_abstract:
        if parent_has_args and not is_arobject_child:
            init_code = f'''{docstring}
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is {class_name}:
            raise TypeError("{class_name} is an abstract class.")
        super().__init__(parent, short_name)'''
        elif is_arobject_child:
            init_code = f'''{docstring}
    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is {class_name}:
            raise TypeError("{class_name} is an abstract class.")
        super().__init__()
        self.parent = parent
        self.short_name = short_name'''
        else:
            init_code = f'''{docstring}
    def __init__(self):
        if type(self) is {class_name}:
            raise TypeError("{class_name} is an abstract class.")
        super().__init__()'''
    else:
        if parent_has_args and not is_arobject_child:
            init_code = f'''{docstring}
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)'''
        elif is_arobject_child:
            init_code = f'''{docstring}
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__()
        self.parent = parent
        self.short_name = short_name'''
        else:
            init_code = f'''{docstring}
    def __init__(self):
        super().__init__()'''
    
    def _format_attr_comment(note: str) -> str:
        """Format attribute note as multi-line comment based on periods."""
        # Split by '. ' and create multi-line comment
        sentences = [s.strip() for s in note.split('.') if s.strip()]
        # Add period back to each sentence if it doesn't end with one
        sentences = [s if s.endswith('.') else s + '.' for s in sentences]

        if len(sentences) == 1:
            return f'# {sentences[0]}'
        else:
            lines = ['#']
            for sentence in sentences:
                lines.append(f'# {sentence}')
            return '\n        '.join(lines)

    attr_code = []
    for attr_name, attr_info in attributes.items():
        attr_type = attr_info.get('type', 'Any')
        multiplicity = attr_info.get('multiplicity', '1')
        is_ref = attr_info.get('is_ref', False)
        attr_note = attr_info.get('note', '')

        # Use string annotation (forward reference) for self-referencing types
        is_self_reference = (attr_type == class_name)

        # Map is_ref to RefType for references
        if is_ref and attr_type == 'Any':
            attr_type = 'RefType'
        elif is_ref and multiplicity in ['*', '0..1']:
            # Keep the original type but note it's a reference
            pass

        # Determine Python attribute name (plural for lists)
        if multiplicity == '*':
            # Pluralize the attribute name for lists
            py_attr_name = attr_name + 's' if not attr_name.endswith('s') else attr_name
        else:
            py_attr_name = attr_name

        if multiplicity == '*':
            if is_ref:
                # Reference list
                if is_self_reference:
                    py_type = f'List["{class_name}"]'
                else:
                    py_type = 'List[RefType]'
            else:
                # Owned list
                if is_self_reference:
                    py_type = f'List["{class_name}"]'
                else:
                    py_type = f'List[{attr_type}]'

            # Add comment if note exists
            if attr_note:
                attr_code.append(f'        {_format_attr_comment(attr_note)}')
            attr_code.append(f'        self.{py_attr_name}: {py_type} = []')
        elif multiplicity == '0..1':
            if is_ref:
                py_type = 'RefType'
            else:
                if is_self_reference:
                    py_type = f'Optional["{class_name}"]'
                else:
                    py_type = f'Optional[{attr_type}]'

            # Add comment if note exists
            if attr_note:
                attr_code.append(f'        {_format_attr_comment(attr_note)}')
            attr_code.append(f'        self.{py_attr_name}: {py_type} = None')
        else:
            if is_ref:
                py_type = 'RefType'
            else:
                if is_self_reference:
                    py_type = f'"{class_name}"'
                else:
                    py_type = attr_type

            # Add comment if note exists
            if attr_note:
                attr_code.append(f'        {_format_attr_comment(attr_note)}')
            attr_code.append(f'        self.{py_attr_name}: {py_type} = None')
    
    methods_code = []
    for attr_name, attr_info in attributes.items():
        attr_type = attr_info.get('type', 'Any')
        multiplicity = attr_info.get('multiplicity', '1')
        is_ref = attr_info.get('is_ref', False)
        attr_note = attr_info.get('note', '')

        # Use string annotation (forward reference) for self-referencing types
        is_self_reference = (attr_type == class_name)

        # Determine Python attribute name (plural for lists)
        if multiplicity == '*':
            py_attr_name = attr_name + 's' if not attr_name.endswith('s') else attr_name
        else:
            py_attr_name = attr_name

        # Map is_ref to RefType
        if is_ref:
            if multiplicity == '*':
                actual_type = 'RefType'
            elif multiplicity == '0..1':
                actual_type = 'RefType'
            else:
                actual_type = 'RefType'
        else:
            actual_type = attr_type

        if multiplicity == '*':
            if is_ref:
                # Reference list - use RefType
                return_type = 'List[RefType]'
                param_type = 'List[RefType]'
                value_type = 'RefType'
            else:
                # Owned list
                if is_self_reference:
                    return_type = f'List["{class_name}"]'
                    param_type = f'List["{class_name}"]'
                    value_type = f'"{class_name}"'
                else:
                    return_type = f'List[{actual_type}]'
                    param_type = f'List[{actual_type}]'
                    value_type = actual_type

            # Method name uses plural form (e.g., getConstantMemories)
            method_name = py_attr_name

            getter_code = f'''    def get{method_name[0].upper()}{method_name[1:]}(self) -> {return_type}:
        return self.{py_attr_name}

'''
        else:
            # Single value - use singular form
            method_name = py_attr_name

            if is_ref:
                return_type = 'RefType'
                param_type = 'RefType'
            elif is_self_reference:
                return_type = f'"{class_name}"'
                param_type = f'"{class_name}"'
            else:
                return_type = actual_type
                param_type = actual_type

            getter_code = f'''    def get{method_name[0].upper()}{method_name[1:]}(self) -> {return_type}:
        return self.{py_attr_name}

'''

        methods_code.append(getter_code)

        if multiplicity == '*':
            setter_code = f'''    def set{method_name[0].upper()}{method_name[1:]}(self, value: {param_type}) -> "{class_name}":
        self.{py_attr_name} = value
        return self

'''
        else:
            setter_code = f'''    def set{method_name[0].upper()}{method_name[1:]}(self, value: {param_type}) -> "{class_name}":
        self.{py_attr_name} = value
        return self

'''

        methods_code.append(setter_code)

        # Add add or create method for list attributes based on kind
        if multiplicity == '*':
            attr_kind = attr_info.get('kind', 'attribute')

            # For references or non-container classes, use addXxxx methods
            # For owned attributes in container classes, use createXxxx methods
            should_use_create = (
                attr_kind == 'attribute' and
                not is_ref and
                _should_have_create_methods(class_name, parent)
            )

            if should_use_create:
                # Generate createXxxx method for owned child objects
                singular_attr_name = attr_name if not attr_name.endswith('s') else attr_name[:-1]
                child_type = actual_type if '[' not in actual_type else actual_type.split('[')[0].strip('"')

                create_method_code = f'''    def create{singular_attr_name[0].upper()}{singular_attr_name[1:]}(self, short_name: str) -> {child_type}:
        """Creates and adds a {singular_attr_name} to this {class_name}."""
        if (short_name not in self.elements):
            new_element = {child_type}(self, short_name)
            # Only call addElement if child has getShortName method (Referrable subclasses)
            if hasattr(new_element, 'getShortName'):
                self.addElement(new_element)
            self.{py_attr_name}.append(new_element)
        return new_element

'''
                methods_code.append(create_method_code)
            else:
                # Generate addXxxx method for references or existing objects
                # Method name uses plural form
                add_method_code = f'''    def add{method_name[0].upper()}{method_name[1:]}(self, value: {value_type}) -> "{class_name}":
        """Adds a value to the {py_attr_name} list."""
        self.{py_attr_name}.append(value)
        return self

'''
                methods_code.append(add_method_code)

    # Ensure only 1 blank line between methods (no trailing blank lines at end)
    code_parts = imports + [''] + [class_decl, init_code, ''] + attr_code + [''] + methods_code

    return '\n'.join(code_parts)


def generate_test_case(class_name: str, class_info: Dict[str, Any], package_path: str, module_path: str) -> str:
    """Generate pytest test case code for a generated class."""
    is_abstract = class_info.get('is_abstract', False)
    attributes = class_info.get('attributes', {})
    parent = class_info.get('parent') or 'ARObject'  # Handle null/None/empty parent
    parent_has_args = _parent_has_init_args(parent)

    test_code = f'''"""
Auto-generated test cases for {class_name}.
Generated by fix-package-implementation.py.
"""

import pytest

from {module_path} import {class_name}
from armodel import AUTOSAR


class Test{class_name}:
    """Test cases for {class_name} class."""'''

    if is_abstract:
        if parent_has_args:
            test_code += f'''

    def test_abstract_class_cannot_be_instantiated(self):
        """Test that {class_name} is abstract and cannot be instantiated directly."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")

        with pytest.raises(TypeError) as err:
            obj = {class_name}(ar_root, "test_{class_name.lower()}")
        assert str(err.value) == "{class_name} is an abstract class."'''
        else:
            test_code += f'''

    def test_abstract_class_cannot_be_instantiated(self):
        """Test that {class_name} is abstract and cannot be instantiated directly."""
        with pytest.raises(TypeError) as err:
            obj = {class_name}()
        assert str(err.value) == "{class_name} is an abstract class."'''
    else:
        if parent_has_args:
            test_code += f'''

    def test_initialization(self):
        """Test initialization of {class_name} with proper attributes."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        obj = {class_name}(ar_root, "test_{class_name.lower()}")

        assert obj.short_name == "test_{class_name.lower()}"'''
        else:
            test_code += f'''

    def test_initialization(self):
        """Test initialization of {class_name}."""
        obj = {class_name}()
        assert obj is not None'''

    # For abstract classes, only test the abstract check - don't try to test getters/setters
    if not is_abstract:
        for attr_name, attr_info in attributes.items():
            attr_type = attr_info.get('type', 'Any')
            multiplicity = attr_info.get('multiplicity', '1')

            # Determine Python attribute name (plural for lists)
            if multiplicity == '*':
                py_attr_name = attr_name + 's' if not attr_name.endswith('s') else attr_name
            else:
                py_attr_name = attr_name

            # Determine object instantiation pattern
            if parent_has_args:
                obj_instantiation = f'''        obj = {class_name}(ar_root, "test_{class_name.lower()}")'''
                setup_code = '''        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
'''
            else:
                obj_instantiation = f'''        obj = {class_name}()'''
                setup_code = ''

            if multiplicity == '*':
                # Compute singular form for create method names (before f-string)
                singular_attr_for_test = attr_name if not attr_name.endswith('s') else attr_name[:-1]
                singular_capitalized = singular_attr_for_test[0].upper() + singular_attr_for_test[1:]

                test_code += f'''

    def test_get_{attr_name}(self):
        """Test getting {attr_name} list."""
{setup_code}{obj_instantiation}

        result = obj.get{py_attr_name[0].upper()}{py_attr_name[1:]}()
        assert isinstance(result, list)

    def test_set_{attr_name}(self):
        """Test setting {attr_name} list."""
{setup_code}{obj_instantiation}

        test_value = []
        result = obj.set{py_attr_name[0].upper()}{py_attr_name[1:]}(test_value)

        assert result == obj
        assert obj.get{py_attr_name[0].upper()}{py_attr_name[1:]}() == test_value

    def test_add_{attr_name}(self):
        """Test adding/creating {attr_name}."""
{setup_code}{obj_instantiation}

        initial_count = len(obj.get{py_attr_name[0].upper()}{py_attr_name[1:]}())
        # Test uses create method for owned attributes, add method for references
        attr_kind = {repr(attr_info.get('kind', 'attribute'))}
        is_ref = {attr_info.get('is_ref', False)}
        should_use_create = (attr_kind == 'attribute' and not is_ref and {_should_have_create_methods(class_name, parent)})

        if should_use_create:
            # For create method, use singular form of attribute name
            result = obj.create{singular_capitalized}("test_value")
            assert result is not None
        else:
            result = obj.add{py_attr_name[0].upper()}{py_attr_name[1:]}(None)
            assert result == obj
        assert len(obj.get{py_attr_name[0].upper()}{py_attr_name[1:]}()) >= initial_count'''
            else:
                test_code += f'''

    def test_get_{attr_name}(self):
        """Test getting {attr_name}."""
{setup_code}{obj_instantiation}

        result = obj.get{py_attr_name[0].upper()}{py_attr_name[1:]}()
        assert result == None

    def test_set_{attr_name}(self):
        """Test setting {attr_name}."""
{setup_code}{obj_instantiation}

        test_value = None
        result = obj.set{py_attr_name[0].upper()}{py_attr_name[1:]}(test_value)

        assert result == obj
        assert obj.get{py_attr_name[0].upper()}{py_attr_name[1:]}() == test_value'''
    
    return test_code


def print_generation_report() -> None:
    """Print the generation report with all issues."""
    if not generation_report['unresolved_types'] and not generation_report['errors']:
        return

    print("\n" + "=" * 60)
    print("Generation Report")
    print("=" * 60)

    if generation_report['unresolved_types']:
        print("\n⚠️  Unresolved Types (downgraded to Any):")
        for class_name, types in generation_report['unresolved_types'].items():
            print(f"\n  {class_name}:")
            for type_name, context in types:
                print(f"    - {type_name} ({context})")

    if generation_report['errors']:
        print("\n❌ Errors:")
        for error in generation_report['errors']:
            print(f"  - {error}")

    if generation_report['warnings']:
        print("\n⚠️  Warnings:")
        for warning in generation_report['warnings']:
            print(f"  - {warning}")


def validate_code(code: str, class_name: str) -> Tuple[bool, List[str]]:
    """Validate that generated code is syntactically correct.

    Returns:
        (is_valid, list of errors)
    """
    errors = []
    try:
        ast.parse(code)
        return True, []
    except SyntaxError as e:
        error_msg = f"Syntax error at line {e.lineno}: {e.msg}"
        if e.text:
            error_msg += f"\n  {e.text.strip()}"
        errors.append(error_msg)
        return False, errors


def format_code_with_ruff(file_path: Path) -> bool:
    """Format a Python file using ruff.

    Returns:
        True if formatting succeeded, False otherwise
    """
    try:
        result = subprocess.run(
            ['python3', '-m', 'ruff', 'format', str(file_path)],
            capture_output=True,
            text=True,
            timeout=30
        )
        return result.returncode == 0
    except (subprocess.TimeoutExpired, FileNotFoundError):
        # ruff not available, skip formatting
        return False


def parse_existing_class(class_file: Path) -> Dict[str, Any]:
    """Parse an existing class file to extract methods and attributes.

    Returns:
        Dictionary with 'methods', 'attributes', 'imports', 'docstring'
    """
    result = {
        'methods': {},  # method_name: (signature, full_code)
        'attributes': set(),  # attribute names
        'imports': [],  # import lines
        'docstring': '',  # class docstring
        'class_def': '',  # class definition line
        'init_code': '',  # __init__ method code
    }

    try:
        with open(class_file, 'r', encoding='utf-8') as f:
            content = f.read()

        tree = ast.parse(content, filename=str(class_file))

        # Extract imports
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    result['imports'].append(f'import {alias.name}')
            elif isinstance(node, ast.ImportFrom):
                module = node.module or ''
                names = ', '.join(alias.name for alias in node.names)
                result['imports'].append(f'from {module} import {names}')

        # Find class definition
        for node in tree.body:
            if isinstance(node, ast.ClassDef):
                result['class_def'] = f'class {node.name}({", ".join([ast.unparse(base) for base in node.bases])}):'

                # Extract docstring
                if (node.body and isinstance(node.body[0], ast.Expr) and
                    isinstance(node.body[0].value, ast.Constant)):
                    result['docstring'] = ast.unparse(node.body[0].value)

                # Extract methods and attributes
                for item in node.body:
                    if isinstance(item, ast.FunctionDef):
                        method_name = item.name
                        method_code = ast.unparse(item)

                        if method_name == '__init__':
                            result['init_code'] = method_code
                        else:
                            # Extract just the signature line
                            signature = f'def {method_name}({ast.unparse(item.args)}):'
                            result['methods'][method_name] = (signature, method_code)

                    elif isinstance(item, ast.Assign) or isinstance(item, ast.AnnAssign):
                        # Extract attribute assignments from __init__
                        for target in item.targets if isinstance(item, ast.Assign) else [item.target]:
                            if isinstance(target, ast.Name):
                                result['attributes'].add(target.id)
                break

    except (SyntaxError, IOError, UnicodeDecodeError) as e:
        print(f"  ⚠️  Could not parse existing class: {e}")

    return result


def merge_class_with_existing(
    generated_code: str,
    existing_info: Dict[str, Any],
    class_name: str
) -> Tuple[str, List[str]]:
    """Merge generated class code with existing implementation.

    Returns:
        (merged_code, list_of_changes_made)
    """
    changes = []

    # Parse generated code
    try:
        gen_tree = ast.parse(generated_code)
    except SyntaxError:
        return generated_code, ['Failed to parse generated code']

    # Extract generated methods
    gen_methods = {}
    gen_docstring = ''
    gen_init_code = ''
    gen_bases = []

    for node in gen_tree.body:
        if isinstance(node, ast.ClassDef):
            # Extract bases for class definition
            gen_bases = [ast.unparse(base) for base in node.bases]

            # Extract docstring
            if (node.body and isinstance(node.body[0], ast.Expr) and
                isinstance(node.body[0].value, ast.Constant)):
                gen_docstring = node.body[0].value.value

            # Extract methods
            for item in node.body:
                if isinstance(item, ast.FunctionDef):
                    method_code = ast.unparse(item)
                    if item.name == '__init__':
                        gen_init_code = method_code
                    else:
                        gen_methods[item.name] = method_code
            break

    # Build merged code
    merged_lines = []
    added_methods = []

    # Collect and merge imports
    existing_imports = set(existing_info.get('imports', []))
    all_imports = set(existing_imports)

    # Add imports from generated code
    for line in generated_code.split('\n'):
        stripped = line.strip()
        if stripped.startswith('import ') or stripped.startswith('from '):
            if stripped not in all_imports:
                all_imports.add(stripped)

    # Write imports
    for imp in sorted(all_imports):
        merged_lines.append(imp)

    merged_lines.append('')

    # Write class definition
    bases_str = ', '.join(gen_bases) if gen_bases else 'ARObject'
    merged_lines.append(f'class {class_name}({bases_str}):')

    # Write docstring (prefer generated if it has sources)
    docstring = gen_docstring if 'Sources:' in gen_docstring else existing_info.get('docstring', gen_docstring)
    if docstring:
        merged_lines.append('    """')
        for line in docstring.split('\n'):
            merged_lines.append(f'    {line}')
        merged_lines.append('    """')

    # Helper function to indent code properly for class body
    def indent_code(code: str, indent: int = 4) -> List[str]:
        """Indent code lines for class body."""
        lines = []
        for line in code.split('\n'):
            if line.strip():  # Only indent non-empty lines
                lines.append(' ' * indent + line)
            else:
                lines.append(line)
        return lines

    # Write __init__ (prefer existing, otherwise generated)
    init_code = existing_info.get('init_code') or gen_init_code
    if init_code:
        merged_lines.append('')
        merged_lines.extend(indent_code(init_code))

    # Write existing methods
    existing_methods = existing_info.get('methods', {})
    for method_name in sorted(existing_methods.keys()):
        _, method_code = existing_methods[method_name]
        merged_lines.append('')
        merged_lines.extend(indent_code(method_code))

    # Write generated methods that don't exist
    for method_name in sorted(gen_methods.keys()):
        if method_name not in existing_methods:
            merged_lines.append('')
            merged_lines.extend(indent_code(gen_methods[method_name]))
            added_methods.append(method_name)
            changes.append(f"Added method: {method_name}")

    if added_methods:
        changes.append(f"Added {len(added_methods)} missing method(s)")

    return '\n'.join(merged_lines) + '\n', changes


def fix_missing_class(class_name: str, class_info: Dict[str, Any], package_path: str, project_root: Path, requirements_dir: Path, dry_run: bool = False, merge: bool = False) -> bool:
    """Fix a missing class by generating and writing the class code."""
    print(f"\n[Fix] Generating missing class: {class_name}")

    if package_path.startswith('M2::'):
        relative = package_path[4:].replace('::', '/')
        package_dir = project_root / 'src' / 'armodel' / 'models' / 'M2' / relative
        # Check if package file exists (e.g., BswBehavior.py)
        package_file = package_dir.parent / f'{package_dir.name}.py'
    else:
        relative = package_path.replace('::', '/')
        package_dir = project_root / 'src' / 'armodel' / 'models' / relative
        package_file = package_dir.parent / f'{package_dir.name}.py'

    # Check if this package is implemented as a single file (not a directory)
    if package_file.exists():
        print(f"  ✗ Error: Package is a single file ({package_file.name})")
        print(f"     Class '{class_name}' should be added to {package_file.relative_to(project_root)}")
        print("     This requires manual implementation or script enhancement.")
        generation_report['errors'].append(
            f"{class_name}: Package is a file, not a directory. "
            f"Add to {package_file.relative_to(project_root)}"
        )
        return False

    module_path = f'armodel.models.M2.{package_path[4:].replace("::", ".")}.{class_name}'

    class_file = package_dir / f'{class_name}.py'

    if not class_file.exists():
        package_dir.mkdir(parents=True, exist_ok=True)
        class_file = package_dir / f'{class_name}.py'
    
    try:
        code = generate_class_code(class_info, package_path, project_root, requirements_dir)
    except Exception as e:
        print(f"  ✗ Error generating code: {e}")
        generation_report['errors'].append(f"{class_name}: {e}")
        return False

    # Validate generated code before writing
    is_valid, errors = validate_code(code, class_name)
    if not is_valid:
        print("  ✗ Validation failed:")
        for error in errors:
            print(f"    {error}")
        generation_report['errors'].append(f"{class_name}: {'; '.join(errors)}")
        return False

    # Check if file exists and handle merge mode
    if class_file.exists() and merge:
        print("  [Merge] Existing class found, merging...")
        existing_info = parse_existing_class(class_file)
        merged_code, changes = merge_class_with_existing(code, existing_info, class_name)

        if changes:
            print("  [Merge] Changes made:")
            for change in changes:
                print(f"    - {change}")
        else:
            print("  [Merge] No changes needed - class is up to date")
            return True

        # Create backup
        backup_file = class_file.with_suffix('.py.backup')
        if not dry_run:
            import shutil
            shutil.copy2(class_file, backup_file)
            print(f"  [Merge] Backup created: {backup_file.relative_to(project_root)}")

        code = merged_code

    if dry_run:
        if class_file.exists() and merge:
            print(f"  [Dry Run] Would merge changes into: {class_file.relative_to(project_root)}")
        else:
            print(f"  [Dry Run] Would create file: {class_file.relative_to(project_root)}")
        print("  [Dry Run] Class code preview:")
        print("  " + "\n  ".join(code.split('\n')[:10]))
        if len(code.split('\n')) > 10:
            print("  ...")
        return True

    try:
        class_file.parent.mkdir(parents=True, exist_ok=True)
        with open(class_file, 'w', encoding='utf-8') as f:
            f.write(code + '\n')

        # Auto-format the generated code with ruff
        if not dry_run:
            format_code_with_ruff(class_file)

        if merge and class_file.exists():
            print(f"  ✓ Merged: {class_file.relative_to(project_root)}")
        else:
            print(f"  ✓ Created: {class_file.relative_to(project_root)}")
        
        parent_init = package_dir / '__init__.py'
        if parent_init.exists():
            with open(parent_init, 'r', encoding='utf-8') as f:
                init_content = f.read()
            
            if f'from .{class_name} import {class_name}' not in init_content:
                with open(parent_init, 'a', encoding='utf-8') as f:
                    f.write(f'\nfrom .{class_name} import {class_name}\n')
                print(f"  ✓ Updated: {parent_init.relative_to(project_root)}")
        
        test_dir = project_root / 'tests' / 'test_armodel' / 'models' / 'M2' / relative
        test_file = test_dir / f'test_{class_name}.py'
        
        test_code = generate_test_case(class_name, class_info, package_path, module_path)
        
        if dry_run:
            print(f"  [Dry Run] Would create test file: {test_file.relative_to(project_root)}")
        else:
            test_dir.mkdir(parents=True, exist_ok=True)
            with open(test_file, 'w', encoding='utf-8') as f:
                f.write(test_code + '\n')
            print(f"  ✓ Created test: {test_file.relative_to(project_root)}")
            
            test_parent_init = test_dir / '__init__.py'
            if not test_parent_init.exists():
                with open(test_parent_init, 'w', encoding='utf-8') as f:
                    f.write('')
        
        return True
    except Exception as e:
        print(f"  ✗ Error: {e}")
        return False


def run_tests(comparisons: List[Dict[str, Any]], project_root: Path, dry_run: bool = False) -> Dict[str, Any]:
    """Run pytest on generated test files to verify the generated class code."""
    import subprocess
    
    print("\n" + "=" * 60)
    print("Running Tests on Generated Classes")
    print("=" * 60)
    
    if dry_run:
        print("[DRY RUN MODE - Tests will not be executed]")
        return {'tests_run': 0, 'tests_passed': 0, 'tests_failed': 0, 'test_files': []}
    
    test_files = []
    stats = {
        'tests_run': 0,
        'tests_passed': 0,
        'tests_failed': 0,
        'test_files': []
    }
    
    for comp in comparisons:
        pkg_name = comp['package']
        classes = comp['classes']
        
        for cls in classes:
            if cls['status'] == '❌ Missing':
                class_name = cls['name']
                
                if pkg_name.startswith('M2::'):
                    relative = pkg_name[4:].replace('::', '/')
                    test_file = project_root / 'tests' / 'test_armodel' / 'models' / 'M2' / relative / f'test_{class_name}.py'
                
                if test_file.exists():
                    test_files.append(str(test_file))
    
    if not test_files:
        print("No new test files found to run.")
        return stats
    
    print(f"Found {len(test_files)} test file(s) to run")
    
    # Run ruff check first
    class_files = []
    for comp in comparisons:
        pkg_name = comp['package']
        classes = comp['classes']
        
        for cls in classes:
            if cls['status'] == '❌ Missing':
                class_name = cls['name']
                
                if pkg_name.startswith('M2::'):
                    relative = pkg_name[4:].replace('::', '/')
                    class_file = project_root / 'src' / 'armodel' / 'models' / 'M2' / relative / f'{class_name}.py'
                
                if class_file.exists():
                    class_files.append(str(class_file))
    
    if class_files:
        print("\nRunning ruff check on generated class files...")
        try:
            result = subprocess.run(
                ['python3', '-m', 'ruff', 'check'] + class_files,
                cwd=project_root,
                capture_output=True,
                text=True,
                timeout=60
            )
            
            if result.returncode == 0:
                print(f"  ✓ Ruff check passed for {len(class_files)} file(s)")
            else:
                print("  ✗ Ruff check failed:")
                print(f"  {result.stdout}")
                print(f"  {result.stderr}")
        except Exception as e:
            print(f"  ✗ Error running ruff: {e}")
    
    # Run pytest on each test file
    for test_file in test_files:
        print(f"\nRunning: {test_file}")
        try:
            result = subprocess.run(
                ['python3', '-m', 'pytest', test_file, '-v'],
                cwd=project_root,
                capture_output=True,
                text=True,
                timeout=60
            )
            
            if result.returncode == 0:
                print("  ✓ All tests passed")
                
                for line in result.stdout.split('\n'):
                    if 'passed' in line:
                        print(f"  {line.strip()}")
                
                stats['tests_passed'] += 1
            else:
                print("  ✗ Some tests failed")
                print(f"  Output:\n{result.stdout}")
                print(f"  Errors:\n{result.stderr}")
                stats['tests_failed'] += 1
            
            stats['tests_run'] += 1
            stats['test_files'].append(test_file)
            
        except subprocess.TimeoutExpired:
            print("  ✗ Test timed out")
            stats['tests_failed'] += 1
        except Exception as e:
            print(f"  ✗ Error running test: {e}")
            stats['tests_failed'] += 1
    
    return stats


def main():
    """Main entry point."""
    args = parse_args()
    
    # Show help if no arguments provided
    if len(sys.argv) == 1:
        parser = argparse.ArgumentParser(
            description='Fix missing AUTOSAR M2 package implementations and generate tests',
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog="""
Examples:
  python scripts/fix-package-implementation.py --package M2::xxx::xxx                  Fix single package
  python scripts/fix-package-implementation.py -p M2::xxx::xxx::xxx                     Fix subpackage
  python scripts/fix-package-implementation.py --package M2::xxx::xxx --dry-run         Preview fixes
        """)
        parser.print_help()
        return 0
    
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    requirements_dir = project_root / 'docs' / 'requirements'
    
    print("=" * 60)
    print("Package Implementation Fix Script")
    print("=" * 60)
    print(f"Project root: {project_root}")
    print(f"Requirements directory: {requirements_dir}")
    if args.package:
        print(f"Package filter: {args.package}")
    print()
    
    print("Loading requirements...")
    try:
        packages = get_all_packages(requirements_dir, args.package)
        if not packages:
            print("Error: No packages found")
            if args.package:
                print(f"  Package '{args.package}' not found in requirements")
            return 1
        print(f"  Found {len(packages)} package(s) to process")
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return 1
    
    print("\nFinding missing classes...")
    comparisons = []
    
    for pkg in packages:
        pkg_name = pkg['name']
        required_classes = pkg['classes']
        
        classes = []
        for cls_name, cls_info in required_classes.items():
            class_file = None
            if pkg_name.startswith('M2::'):
                relative = pkg_name[4:].replace('::', '/')
                package_dir = project_root / 'src' / 'armodel' / 'models' / 'M2' / relative
                class_file = package_dir / f'{cls_name}.py'
            
            if class_file and class_file.exists():
                status = '✅ Implemented'
                implemented = True
                location = str(class_file.relative_to(project_root))
                notes = "Line 1"
            else:
                status = '❌ Missing'
                implemented = False
                location = '-'
                notes = 'Not found in implementation'
            
            classes.append({
                'name': cls_name,
                'status': status,
                'required': True,
                'implemented': implemented,
                'location': location,
                'notes': notes
            })
        
        comparisons.append({
            'package': pkg_name,
            'classes': classes,
            'required_classes_data': required_classes
        })
    
    missing_count = sum(1 for comp in comparisons for cls in comp['classes'] if cls['status'] == '❌ Missing')

    if args.merge:
        print(f"  Merge mode: Will process {len([cls for comp in comparisons for cls in comp['classes']])} class(es)")
    elif missing_count == 0:
        print("  No missing classes found!")
        return 0
    else:
        print(f"  Found {missing_count} missing class(es)")
    
    print("\n" + "=" * 60)
    print("Applying Fixes")
    print("=" * 60)

    if args.merge:
        print("[MERGE MODE - Will merge into existing classes]")
    if args.dry_run:
        print("[DRY RUN MODE - No files will be modified]")
    
    # Set global dry_run flag
    global dry_run_mode
    dry_run_mode = args.dry_run
    
    stats = {'classes_fixed': 0, 'errors': 0}
    
    for comp in comparisons:
        pkg_name = comp['package']
        classes = comp['classes']
        required_classes_data = comp.get('required_classes_data', {})

        print(f"\nPackage: {pkg_name}")

        for cls in classes:
            # In merge mode, process all classes (including existing ones)
            should_process = (cls['status'] == '❌ Missing') or args.merge

            if should_process:
                class_info = required_classes_data.get(cls['name'], {})
                if class_info:
                    if fix_missing_class(cls['name'], class_info, pkg_name, project_root, requirements_dir, args.dry_run, args.merge):
                        stats['classes_fixed'] += 1
                    else:
                        stats['errors'] += 1
                else:
                    print(f"  ✗ Warning: No class info found for {cls['name']}")
                    stats['errors'] += 1
    
    print("\n" + "=" * 60)
    print("Fix Summary")
    print("=" * 60)
    print(f"Classes fixed: {stats['classes_fixed']}")
    print(f"Errors: {stats['errors']}")

    # Print generation report with unresolved types and errors
    print_generation_report()
    
    if args.dry_run:
        print("\n[DRY RUN COMPLETE - No files were modified]")
        return 0
    
    if stats['classes_fixed'] > 0:
        test_stats = run_tests(comparisons, project_root, args.dry_run)
        
        print("\n" + "=" * 60)
        print("Test Summary")
        print("=" * 60)
        print(f"Test files run: {test_stats['tests_run']}")
        print(f"Tests passed: {test_stats['tests_passed']}")
        print(f"Tests failed: {test_stats['tests_failed']}")
        
        if test_stats['tests_failed'] == 0:
            print("\n✅ All fixes applied and tests passed!")
            return 0
        else:
            print(f"\n⚠️ {test_stats['tests_failed']} test(s) failed")
            return 1
    
    return 0


if __name__ == '__main__':
    exit(main())
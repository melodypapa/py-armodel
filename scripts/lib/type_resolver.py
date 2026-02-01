#!/usr/bin/env python3
"""
Type Resolver Module for py-armodel

This module handles type discovery and import resolution for AUTOSAR classes.
"""

import ast
from pathlib import Path
from typing import Dict, List, Optional, Set, Any, Tuple


# Global caches for type lookups
_type_index_cache: Optional[Dict[str, str]] = None
_wildcard_exports_cache: Optional[Dict[str, Set[str]]] = None

# Track generation issues
generation_report = {
    'unresolved_types': {},  # class_name: [(type_name, context), ...]
    'warnings': [],
    'errors': [],
}

# Track missing types that need to be generated
_missing_types_to_generate = set()


def build_type_index(project_root: Path) -> None:
    """Build a global index of all types and their import paths.

    Args:
        project_root: Root directory of the project
    """
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
    """Generate correct import path considering wildcard exports.

    Args:
        models_dir: Path to M2 models directory
        file_rel_path: Relative path from models_dir to the file
        class_name: Name of the class to generate import for

    Returns:
        Import statement string
    """
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
    """Find a type in the codebase using cached index.

    Args:
        project_root: Root directory of the project
        type_name: Name of the type to find

    Returns:
        Import statement if found, None otherwise
    """
    global _type_index_cache
    if _type_index_cache is None:
        build_type_index(project_root)

    return _type_index_cache.get(type_name)


def find_type_in_codebase(
    project_root: Path,
    type_name: str,
    current_package_path: str = ''
) -> Optional[str]:
    """Find a type in the codebase and return the absolute import path.

    Note: This is a non-cached version. Consider using find_type_in_codebase_cached
    for better performance when doing multiple lookups.

    Args:
        project_root: Root directory of the project
        type_name: Name of the type to find
        current_package_path: Current package path (for future use)

    Returns:
        Import statement if found, None otherwise
    """
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


def _track_unresolved_type(class_name: str, type_name: str, context: str) -> None:
    """Track an unresolved type reference.

    Args:
        class_name: Name of the class with the unresolved type
        type_name: Name of the unresolved type
        context: Context where the type is used (e.g., 'parent class', 'attribute foo')
    """
    if class_name not in generation_report['unresolved_types']:
        generation_report['unresolved_types'][class_name] = []
    generation_report['unresolved_types'][class_name].append((type_name, context))


def _has_short_name_in_init(class_info: Dict[str, Any], requirements_dir: Path) -> bool:
    """Check if any base class in the hierarchy has __init__(parent, short_name) signature.

    This checks the bases array in the JSON requirements to see if any base class
    (or its ancestors) has short_name in its __init__ method.

    Args:
        class_info: Class information dictionary from requirements
        requirements_dir: Path to requirements directory

    Returns:
        True if any base class has short_name in __init__, False otherwise
    """
    from . import package_loader

    # Classes known to have __init__(parent, short_name) signature
    classes_with_short_name = {
        # Core AUTOSAR hierarchy (Referrable lineage)
        'Referrable', 'MultilanguageReferrable', 'Identifiable', 'ARElement', 'PackageableElement',
        # ATP Blueprintable hierarchy
        'AtpBlueprintable', 'AtpClassifier', 'AtpType', 'AtpPrototype', 'AtpStructureElement', 'AtpFeature',
        # Other classes with short_name
        'CollectableElement', 'ElementCollection', 'ARPackage',
        # Specific component and behavior classes
        'InternalBehavior', 'Implementation', 'SwcInternalBehavior', 'BswInternalBehavior', 'ExecutableEntity',
        # Component classes
        'PortInterface', 'SwComponentType', 'PortPrototype', 'AbstractProvidedPortPrototype',
        'AbstractRequiredPortPrototype', 'PPortPrototype', 'RPortPrototype', 'PRPortPrototype',
        # Data types
        'ApplicationDataType', 'ImplementationDataType', 'AutosarDataType',
        # Data prototypes
        'DataPrototype', 'AutosarDataPrototype', 'VariableDataPrototype',
        'ApplicationCompositeElementDataPrototype', 'ApplicationArrayElement', 'ApplicationRecordElement',
        'ParameterDataPrototype',
        # Other structure classes
        'ImplementationProps', 'SwcBswMapping', 'ServiceNeeds',
    }

    # Get all base classes from JSON
    bases = class_info.get('bases', [])

    for base_name in bases:
        # Check if this base class has short_name
        if base_name in classes_with_short_name:
            return True

        # Check the base class's own bases (recursively)
        base_data = package_loader.find_class_in_requirements(requirements_dir, base_name)
        if base_data:
            base_info = base_data['class_info']
            if _has_short_name_in_init(base_info, requirements_dir):
                return True

    return False


def generate_imports(
    class_info: Dict[str, Any],
    package_path: str,
    project_root: Path,
    requirements_dir: Path,
    class_name: str = ''
) -> List[str]:
    """Generate necessary import statements for a class based on its attributes and structure.

    Args:
        class_info: Class information dictionary from requirements
        package_path: Full package path (e.g., 'M2::AUTOSARTemplates::...')
        project_root: Root directory of the project
        requirements_dir: Path to requirements directory
        class_name: Name of the class being generated

    Returns:
        Sorted list of import statements
    """
    from . import package_loader

    imports = set()
    is_abstract = class_info.get('is_abstract', False)
    parent = class_info.get('parent') or 'ARObject'
    attributes = class_info.get('attributes', {})

    typing_imports = set()

    if is_abstract:
        imports.add('from abc import ABC')

    # Import ARObject if needed for __init__ signature or for attributes
    has_short_name_init = _has_short_name_in_init(class_info, requirements_dir)
    needs_ar_object = (
        (not is_abstract or (is_abstract and any(
            attr_info.get('multiplicity') in ['*', '0..1']
            for attr_info in attributes.values()
        ))) or
        has_short_name_init or (parent == 'ARObject')
    )
    if needs_ar_object:
        imports.add(
            'from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject'
        )

    # Import RefType if any attribute has is_ref: true
    has_ref_attributes = any(attr_info.get('is_ref', False) for attr_info in attributes.values())
    if has_ref_attributes:
        imports.add(
            'from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType'
        )

    # Try to find parent class in codebase
    parent_import = find_type_in_codebase_cached(project_root, parent)
    if parent_import:
        imports.add(parent_import)
    elif parent not in ['Any', 'ARObject']:
        # Parent class not found in codebase - use Any for typing
        if class_name:
            _track_unresolved_type(class_name, parent, 'parent class')
        print(f"  ⚠️  Parent class '{parent}' not found in codebase (using Any)")

    for attr_name, attr_info in attributes.items():
        attr_type = attr_info.get('type', 'Any')
        multiplicity = attr_info.get('multiplicity', '1')
        is_ref = attr_info.get('is_ref', False)

        if multiplicity == '*':
            typing_imports.add('List')
        elif multiplicity == '0..1':
            typing_imports.add('Optional')

        # Skip self-referencing types
        if attr_type == class_name:
            continue

        # Skip importing type when it's a reference (RefType is used instead)
        if is_ref:
            continue

        # Try to find type in codebase
        type_import = find_type_in_codebase_cached(project_root, attr_type)
        if type_import:
            # Filter out self-imports
            if f' import {class_name}' not in type_import:
                imports.add(type_import)
        elif attr_type not in ['Any', 'str', 'int', 'float', 'bool']:
            # Type not found - check if it's an enumeration in requirements
            enum_data = package_loader.find_enum_in_requirements(requirements_dir, attr_type)
            if enum_data:
                print(f"  ℹ️  Type '{attr_type}' for attribute '{attr_name}' is an enumeration")
                enum_package_path = enum_data['package_path']
                if enum_package_path.startswith('M2::'):
                    enum_module_path = (
                        f'armodel.models.M2.{enum_package_path[4:].replace("::", ".")}.{attr_type}'
                    )
                else:
                    enum_module_path = f'armodel.models.M2.{enum_package_path.replace("::", ".")}.{attr_type}'
                imports.add(f'from {enum_module_path} import {attr_type}')
                # Skip the rest - use the actual enum type, not Any
                continue
            else:
                # Type not found in codebase or requirements - check if it's a class to generate
                class_data = package_loader.find_class_in_requirements(requirements_dir, attr_type)
                if class_data:
                    # This is a class in the JSON requirements - mark for generation
                    global _missing_types_to_generate
                    _missing_types_to_generate.add(attr_type)
                    print(f"  ℹ️  Type '{attr_type}' for attribute '{attr_name}' will be generated")
                else:
                    # Type not found anywhere - use Any typing
                    if class_name:
                        _track_unresolved_type(class_name, attr_type, f'attribute {attr_name}')
                    print(f"  ⚠️  Type '{attr_type}' for attribute '{attr_name}' not found in JSON DB (using Any)")

                # Store original type name and use Any for type annotation
                attr_info['original_type'] = attr_type
                attr_info['type'] = 'Any'
                typing_imports.add('Any')

    if typing_imports:
        imports.add(f'from typing import {", ".join(sorted(typing_imports))}')

    return sorted(list(imports))


def get_generation_report() -> Dict[str, Any]:
    """Get the current generation report.

    Returns:
        Dictionary containing unresolved types, warnings, and errors
    """
    return generation_report


def reset_generation_report() -> None:
    """Reset the generation report."""
    global generation_report
    generation_report = {
        'unresolved_types': {},
        'warnings': [],
        'errors': [],
    }


def get_missing_types_to_generate() -> set:
    """Get the set of missing types that need to be generated.

    Returns:
        Set of type names that should be recursively generated
    """
    global _missing_types_to_generate
    return _missing_types_to_generate.copy()


def clear_missing_types_to_generate() -> None:
    """Clear the set of missing types to generate."""
    global _missing_types_to_generate
    _missing_types_to_generate = set()


def update_cache_for_new_class(project_root: Path, type_name: str, package_path: str) -> None:
    """Update the type index cache with a newly created class.

    Args:
        project_root: Root directory of the project
        type_name: Name of the newly created class
        package_path: Full package path (e.g., 'M2::AUTOSARTemplates::...')
    """
    global _type_index_cache
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

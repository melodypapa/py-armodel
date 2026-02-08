#!/usr/bin/env python3
"""
Package Loader Module for py-armodel

This module handles loading and processing AUTOSAR package definitions
from JSON requirements files.
"""

import json
from pathlib import Path
from typing import Any, Dict, List, Optional


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


def _load_classes_from_file(
    requirements_dir: Path,
    pkg_json: Dict[str, Any]
) -> Dict[str, Any]:
    """Load classes from a package's classes file."""
    classes = {}

    if 'files' not in pkg_json or 'classes' not in pkg_json['files']:
        return classes

    classes_file = pkg_json['files']['classes']
    if not classes_file:
        return classes

    if classes_file.startswith('packages/'):
        classes_path = requirements_dir / classes_file
    else:
        classes_path = requirements_dir / 'packages' / classes_file

    if not classes_path.exists():
        return classes

    with open(classes_path, 'r', encoding='utf-8') as f:
        classes_data = json.load(f)
        for cls in classes_data.get('classes', []):
            classes[cls['name']] = cls

    return classes


def _load_enumerations_from_file(
    requirements_dir: Path,
    pkg_json: Dict[str, Any]
) -> Dict[str, Any]:
    """Load enumerations from a package's enumerations file."""
    enumerations = {}

    if 'files' not in pkg_json or 'enumerations' not in pkg_json['files']:
        return enumerations

    enums_file = pkg_json['files']['enumerations']
    if not enums_file:
        return enumerations

    if enums_file.startswith('packages/'):
        enums_path = requirements_dir / enums_file
    else:
        enums_path = requirements_dir / 'packages' / enums_file

    if not enums_path.exists():
        return enumerations

    with open(enums_path, 'r', encoding='utf-8') as f:
        enums_data = json.load(f)
        for enum in enums_data.get('enumerations', []):
            enumerations[enum['name']] = enum

    return enumerations


def _load_primitives_from_file(
    requirements_dir: Path,
    pkg_json: Dict[str, Any]
) -> Dict[str, Any]:
    """Load primitives from a package's primitives file."""
    primitives = {}

    if 'files' not in pkg_json or 'primitives' not in pkg_json['files']:
        return primitives

    primitives_file = pkg_json['files']['primitives']
    if not primitives_file:
        return primitives

    if primitives_file.startswith('packages/'):
        primitives_path = requirements_dir / primitives_file
    else:
        primitives_path = requirements_dir / 'packages' / primitives_file

    if not primitives_path.exists():
        return primitives

    with open(primitives_path, 'r', encoding='utf-8') as f:
        primitives_data = json.load(f)
        for prim in primitives_data.get('primitives', []):
            primitives[prim['name']] = prim

    return primitives


def _get_package_file_path(pkg_data: Any) -> Optional[str]:
    """Extract the package file path from package data."""
    if isinstance(pkg_data, str):
        return None

    pkg_file = pkg_data.get('file', '')
    if pkg_file:
        return pkg_file if pkg_file.startswith('packages/') else f"packages/{pkg_file}"

    if 'path' in pkg_data:
        return f"packages/{pkg_data['path'].replace('::', '_')}.json"

    return None


def _should_process_package(
    full_path: str,
    specific_package: Optional[str]
) -> bool:
    """Determine if a package should be processed based on filter."""
    if not specific_package:
        return True

    exact_match = full_path == specific_package
    starts_with = full_path.startswith(specific_package + '::')
    parent_of = specific_package.startswith(full_path + '::')

    return exact_match or starts_with or parent_of


def _process_package_recursive(
    pkg_data: Any,
    parent_path: str,
    requirements_dir: Path,
    specific_package: Optional[str],
    should_process_subpackages: bool
) -> List[Dict[str, Any]]:
    """Recursively process packages and their subpackages."""
    pkg_list = []

    if isinstance(pkg_data, str):
        pkg_name = pkg_data
    else:
        pkg_name = pkg_data.get('name', '')

    full_path = f"{parent_path}::{pkg_name}" if parent_path else pkg_name

    # Determine if we should process this package's subpackages
    process_subpackages = should_process_subpackages and _should_process_package(
        full_path, specific_package
    )

    if not process_subpackages and specific_package:
        return pkg_list

    # Load package JSON
    pkg_file = _get_package_file_path(pkg_data)
    pkg_json = load_package_json(requirements_dir, pkg_file) if pkg_file else None

    if pkg_json:
        classes = _load_classes_from_file(requirements_dir, pkg_json)
        enumerations = _load_enumerations_from_file(requirements_dir, pkg_json)
        primitives = _load_primitives_from_file(requirements_dir, pkg_json)

        # Include package if it has content or matches specific package
        if classes or enumerations or primitives or (specific_package and full_path == specific_package):
            pkg_list.append({
                'name': full_path,
                'file': pkg_file or f"packages/{pkg_data.get('path', pkg_name).replace('::', '_')}.json",
                'classes': classes,
                'enumerations': enumerations,
                'primitives': primitives
            })

        # Process subpackages if needed
        if 'subpackages' in pkg_json and process_subpackages:
            for subpkg in pkg_json['subpackages']:
                pkg_list.extend(_process_package_recursive(
                    subpkg, full_path, requirements_dir, specific_package, True
                ))

    return pkg_list


def get_all_packages(
    requirements_dir: Path,
    specific_package: Optional[str] = None
) -> List[Dict[str, Any]]:
    """Get all packages from requirements, optionally filtered by specific package.

    Args:
        requirements_dir: Path to requirements directory
        specific_package: Optional package filter (e.g., 'M2::AUTOSARTemplates::BswModuleTemplate')

    Returns:
        List of package dictionaries containing name, file, classes, and enumerations
    """
    index = load_requirements_index(requirements_dir)
    packages = []

    for pkg in index.get('packages', []):
        packages.extend(_process_package_recursive(
            pkg, '', requirements_dir, specific_package, True
        ))

    return packages


def _search_packages_for_class(
    pkg_data: Any,
    parent_path: str,
    requirements_dir: Path,
    type_name: str
) -> Optional[Dict[str, Any]]:
    """Recursively search for a class in packages."""
    if isinstance(pkg_data, str):
        pkg_name = pkg_data
        pkg_file = None
    else:
        pkg_name = pkg_data.get('name', '')
        pkg_file = pkg_data.get('file', '')

    full_path = f"{parent_path}::{pkg_name}" if parent_path else pkg_name

    pkg_file_path = _get_package_file_path(pkg_data) if not isinstance(pkg_data, str) else None
    pkg_json = load_package_json(requirements_dir, pkg_file_path) if pkg_file_path else None

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
            result = _search_packages_for_class(subpkg, full_path, requirements_dir, type_name)
            if result:
                return result

    return None


def find_class_in_requirements(
    requirements_dir: Path,
    type_name: str
) -> Optional[Dict[str, Any]]:
    """Find a class definition in the requirements JSON files.

    Args:
        requirements_dir: Path to requirements directory
        type_name: Class name to search for

    Returns:
        Dictionary with 'class_info' and 'package_path' if found, None otherwise
    """
    index = load_requirements_index(requirements_dir)

    for pkg in index.get('packages', []):
        result = _search_packages_for_class(pkg, '', requirements_dir, type_name)
        if result:
            return result

    return None


def _search_packages_for_enum(
    pkg_data: Any,
    parent_path: str,
    requirements_dir: Path,
    type_name: str
) -> Optional[Dict[str, Any]]:
    """Recursively search for an enumeration in packages."""
    if isinstance(pkg_data, str):
        pkg_name = pkg_data
        pkg_file = None
    else:
        pkg_name = pkg_data.get('name', '')
        pkg_file = pkg_data.get('file', '')

    full_path = f"{parent_path}::{pkg_name}" if parent_path else pkg_name

    pkg_file_path = _get_package_file_path(pkg_data) if not isinstance(pkg_data, str) else None
    pkg_json = load_package_json(requirements_dir, pkg_file_path) if pkg_file_path else None

    if pkg_json and 'files' in pkg_json and 'enumerations' in pkg_json['files']:
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
                        if enum['name'] == type_name:
                            return {'enum_info': enum, 'package_path': full_path}

    if pkg_json and 'subpackages' in pkg_json:
        for subpkg in pkg_json['subpackages']:
            result = _search_packages_for_enum(subpkg, full_path, requirements_dir, type_name)
            if result:
                return result

    return None


def find_enum_in_requirements(
    requirements_dir: Path,
    type_name: str
) -> Optional[Dict[str, Any]]:
    """Find an enumeration definition in the requirements JSON files.

    Args:
        requirements_dir: Path to requirements directory
        type_name: Enumeration name to search for

    Returns:
        Dictionary with 'enum_info' and 'package_path' if found, None otherwise
    """
    index = load_requirements_index(requirements_dir)

    for pkg in index.get('packages', []):
        result = _search_packages_for_enum(pkg, '', requirements_dir, type_name)
        if result:
            return result

    return None


def _search_packages_for_primitive(
    pkg_data: Any,
    parent_path: str,
    requirements_dir: Path,
    type_name: str
) -> Optional[Dict[str, Any]]:
    """Recursively search for a primitive in packages."""
    if isinstance(pkg_data, str):
        pkg_name = pkg_data
        pkg_file = None
    else:
        pkg_name = pkg_data.get('name', '')
        pkg_file = pkg_data.get('file', '')

    full_path = f"{parent_path}::{pkg_name}" if parent_path else pkg_name

    pkg_file_path = _get_package_file_path(pkg_data) if not isinstance(pkg_data, str) else None
    pkg_json = load_package_json(requirements_dir, pkg_file_path) if pkg_file_path else None

    if pkg_json and 'files' in pkg_json and 'primitives' in pkg_json['files']:
        primitives_file = pkg_json['files']['primitives']
        if primitives_file:
            if primitives_file.startswith('packages/'):
                primitives_path = requirements_dir / primitives_file
            else:
                primitives_path = requirements_dir / 'packages' / primitives_file

            if primitives_path.exists():
                with open(primitives_path, 'r', encoding='utf-8') as f:
                    primitives_data = json.load(f)
                    for prim in primitives_data.get('primitives', []):
                        if prim['name'] == type_name:
                            return {'primitive_info': prim, 'package_path': full_path}

    if pkg_json and 'subpackages' in pkg_json:
        for subpkg in pkg_json['subpackages']:
            result = _search_packages_for_primitive(subpkg, full_path, requirements_dir, type_name)
            if result:
                return result

    return None


def find_primitive_in_requirements(
    requirements_dir: Path,
    type_name: str
) -> Optional[Dict[str, Any]]:
    """Find a primitive definition in the requirements JSON files.

    Args:
        requirements_dir: Path to requirements directory
        type_name: Primitive name to search for

    Returns:
        Dictionary with 'primitive_info' and 'package_path' if found, None otherwise
    """
    index = load_requirements_index(requirements_dir)

    for pkg in index.get('packages', []):
        result = _search_packages_for_primitive(pkg, '', requirements_dir, type_name)
        if result:
            return result

    return None

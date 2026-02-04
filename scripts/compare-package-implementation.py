#!/usr/bin/env python3
"""
Package Implementation Comparison Script for py-armodel

This script compares AUTOSAR M2 package requirements with actual Python implementations.
It generates a markdown report showing:
- Classes that are correctly implemented
- Classes that are missing
- Classes that are extra (not documented)
- Enumerations and their values
- Any discrepancies between requirements and implementation

Usage:
    python scripts/compare-package-implementation.py
    python scripts/compare-package-implementation.py --package M2::AUTOSARTemplates::BswModuleTemplate
    python scripts/compare-package-implementation.py --package M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior
"""

import sys
import argparse
import ast
import json
import os
from pathlib import Path
from typing import Dict, List, Tuple, Optional, Any


def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        prog='compare-package-implementation.py',
        description='Compare AUTOSAR M2 package requirements with Python implementations',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --all                                    Compare all packages
  %(prog)s -p M2::xxx::xxx                          Compare single package
  %(prog)s -p M2::xxx::xxx::xxx                     Compare subpackage
                """
    )
    parser.add_argument(
        '--package', '-p',
        type=str,
        metavar='PACKAGE',
        help='Specific package to compare (format: M2::xxx::xxxx)'
    )
    parser.add_argument(
        '--all',
        action='store_true',
        help='Compare all packages'
    )
    parser.add_argument(
        '--output', '-o',
        type=str,
        metavar='OUTPUT',
        help='Output file path (default: reports/package_comparison.md)'
    )
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Enable verbose output'
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
    # package_file may be a relative path like "packages/M2.json" or just "M2.json"
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
    """
    Get all packages from requirements, optionally filtered by specific package.
    
    Returns list of package dictionaries with:
    - name: Package name (e.g., M2::AUTOSARTemplates::BswModuleTemplate)
    - file: Package JSON file path
    - classes: Dict of classes {name: class_info}
    - enumerations: Dict of enumerations {name: enum_info}
    """
    index = load_requirements_index(requirements_dir)
    packages = []
    
    def process_package(pkg_data: Any, parent_path: str = '') -> List[Dict[str, Any]]:
        """Recursively process packages."""
        pkg_list = []
        
        # Handle string input (from index.json subpackages)
        if isinstance(pkg_data, str):
            pkg_name = pkg_data
            pkg_file = None
        else:
            pkg_name = pkg_data.get('name', '')
            pkg_file = pkg_data.get('file', '')
        
        # Build full package path
        if parent_path:
            full_path = f"{parent_path}::{pkg_name}"
        else:
            full_path = pkg_name
        
        # Filter if specific package requested
        should_process_subpackages = False
        if specific_package:
            exact_match = full_path == specific_package
            starts_with = full_path.startswith(specific_package + '::')
            parent_of = specific_package.startswith(full_path + '::')
            
            if exact_match:
                # Exact match - include this package and its subpackages
                should_process_subpackages = True
            elif starts_with:
                # Starts with target (is a subpackage of target) - include
                should_process_subpackages = True
            elif parent_of:
                # Parent of target - don't include but process subpackages
                should_process_subpackages = True
            else:
                # Not related - skip entirely
                return pkg_list
        else:
            # No filter - process everything
            should_process_subpackages = True
        
        # Load package data
        pkg_json = None
        if pkg_file:
            # pkg_file may already include 'packages/' prefix
            if pkg_file.startswith('packages/'):
                pkg_json = load_package_json(requirements_dir, pkg_file)
            else:
                pkg_json = load_package_json(requirements_dir, f"packages/{pkg_file}")
        elif not isinstance(pkg_data, str) and 'path' in pkg_data:
            # Try to construct file path from package path
            pkg_path = pkg_data['path'].replace('::', '_')
            pkg_json = load_package_json(requirements_dir, f"packages/{pkg_path}.json")
        
        if pkg_json:
            # Load classes and enumerations
            classes = {}
            enumerations = {}
            
            # Load classes file
            if 'files' in pkg_json and 'classes' in pkg_json['files']:
                classes_file = pkg_json['files']['classes']
                if classes_file:
                    # classes_file may already include 'packages/' prefix
                    if classes_file.startswith('packages/'):
                        classes_path = requirements_dir / classes_file
                    else:
                        classes_path = requirements_dir / 'packages' / classes_file
                    if classes_path.exists():
                        with open(classes_path, 'r', encoding='utf-8') as f:
                            classes_data = json.load(f)
                            for cls in classes_data.get('classes', []):
                                classes[cls['name']] = cls
            
            # Load enumerations file
            if 'files' in pkg_json and 'enumerations' in pkg_json['files']:
                enums_file = pkg_json['files']['enumerations']
                if enums_file:
                    # enums_file may already include 'packages/' prefix
                    if enums_file.startswith('packages/'):
                        enums_path = requirements_dir / enums_file
                    else:
                        enums_path = requirements_dir / 'packages' / enums_file
                    if enums_path.exists():
                        with open(enums_path, 'r', encoding='utf-8') as f:
                            enums_data = json.load(f)
                            for enum in enums_data.get('enumerations', []):
                                enumerations[enum['name']] = enum
            
            # Only add to list if it has classes or enumerations, or if it's an exact match
            if classes or enumerations or (specific_package and full_path == specific_package):
                pkg_list.append({
                    'name': full_path,
                    'file': pkg_file or f"packages/{pkg_data.get('path', pkg_name).replace('::', '_')}.json",
                    'classes': classes,
                    'enumerations': enumerations
                })
            
            # Process subpackages from pkg_json
            if 'subpackages' in pkg_json and should_process_subpackages:
                for subpkg in pkg_json['subpackages']:
                    pkg_list.extend(process_package(subpkg, full_path))
        
        return pkg_list
    
    # Start from top-level packages
    for pkg in index.get('packages', []):
        packages.extend(process_package(pkg, ''))
    
    return packages


def get_package_has_subpackages(requirements_dir: Path, package_path: str) -> bool:
    """
    Check if a package has subpackages based on requirements JSON.
    
    Args:
        requirements_dir: Path to requirements directory
        package_path: Package path (e.g., M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior)
    
    Returns:
        True if package has subpackages, False otherwise
    """
    # Remove M2:: prefix (4 characters)
    if package_path.startswith('M2::'):
        package_path = package_path[4:]
    
    # Replace :: with _ to match JSON file naming
    json_name = 'M2_' + package_path.replace('::', '_') + '.json'
    json_file = requirements_dir / 'packages' / json_name
    
    if not json_file.exists():
        return False
    
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return bool(data.get('subpackages', []))
    except (json.JSONDecodeError, IOError):
        return False


def package_path_to_python_path(
    package_path: str,
    project_root: Path,
    requirements_dir: Optional[Path] = None
) -> Tuple[Optional[Path], Optional[Path]]:
    """
    Convert a package path to Python file/directory path.

    Returns a tuple of (file_path, directory_path). Either or both may be non-None.

    This function scans what ACTUALLY exists on the filesystem, regardless of
    what the requirements say the structure should be. Structure mismatch detection
    is handled separately in scan_implementation().

    Args:
        package_path: Package path (e.g., M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior)
        project_root: Root directory of the project
        requirements_dir: Path to requirements directory (optional, used for structure mismatch detection)

    Returns:
        (file_path, directory_path) tuple

    Examples:
        M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior (implemented as directory)
        -> (None, BswBehavior/ directory) if directory exists
        -> (None, None) if not found

        M2::AUTOSARTemplates::BswModuleTemplate::BswOverview (implemented as directory)
        -> (None, BswOverview/ directory) if directory exists
        -> (None, None) if not found
    """
    # Remove M2:: prefix (4 characters)
    if package_path.startswith('M2::'):
        package_path = package_path[4:]
    
    # Replace :: with /
    relative_path = package_path.replace('::', '/')
    
    # Build full path
    python_path = project_root / 'src' / 'armodel' / 'models' / 'M2' / relative_path

    # Check what actually exists on the filesystem
    # This is the primary check - we scan whatever is actually implemented
    py_file = python_path.with_suffix('.py')
    file_path = py_file if py_file.exists() else None
    dir_path = python_path if python_path.is_dir() else None

    # If requirements_dir is provided, check for expected structure for reporting
    # But don't let it prevent us from scanning what actually exists
    expected_has_subpackages = None
    if requirements_dir:
        full_package_path = 'M2::' + package_path.replace('/', '::')
        expected_has_subpackages = get_package_has_subpackages(requirements_dir, full_package_path)

    # Note: Structure mismatch detection is done in scan_implementation()
    # This function just returns what actually exists
    
    # Not found
    if not file_path and not dir_path:
        return (None, None)
    
    return (file_path, dir_path)


def extract_classes_from_python(file_path: Path, module_prefix: str = '') -> Dict[str, Dict[str, Any]]:
    """
    Extract class information from a Python file using AST.
    
    Returns: {class_name: {is_abstract: bool, bases: List[str], line_number: int}}
    """
    classes = {}
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            tree = ast.parse(content, filename=str(file_path))
            
            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef):
                    # Determine if abstract
                    is_abstract = False
                    
                    # Check ABC inheritance
                    for base in node.bases:
                        if isinstance(base, ast.Name) and base.id == 'ABC':
                            is_abstract = True
                            break
                    
                    # Check @abstractmethod decorator
                    if not is_abstract:
                        for decorator in node.decorator_list:
                            if isinstance(decorator, ast.Name) and decorator.id == 'abstractmethod':
                                is_abstract = True
                                break
                    
                    # Check __init__ for TypeError check pattern
                    if not is_abstract:
                        for item in node.body:
                            if isinstance(item, ast.FunctionDef) and item.name == '__init__':
                                for stmt in ast.walk(item):
                                    if isinstance(stmt, ast.If):
                                        for body_stmt in ast.walk(stmt):
                                            if isinstance(body_stmt, ast.Raise):
                                                if isinstance(body_stmt.exc, ast.Call):
                                                    if isinstance(body_stmt.exc.func, ast.Name):
                                                        if body_stmt.exc.func.id == 'TypeError':
                                                            is_abstract = True
                                                            break
                                        if is_abstract:
                                            break
                                if is_abstract:
                                    break
                    
                    # Extract base classes (excluding common ones)
                    SKIP_BASES = {'ABC', 'object', 'Enum', 'AREnum'}
                    bases = []
                    for base in node.bases:
                        if isinstance(base, ast.Name):
                            if base.id not in SKIP_BASES:
                                bases.append(base.id)
                        elif isinstance(base, ast.Subscript):
                            if isinstance(base.value, ast.Name) and base.value.id not in SKIP_BASES:
                                bases.append(base.value.id)
                    
                    full_name = f"{module_prefix}.{node.name}" if module_prefix else node.name
                    
                    classes[node.name] = {
                        'is_abstract': is_abstract,
                        'bases': bases,
                        'line_number': node.lineno,
                        'full_name': full_name
                    }
    except (SyntaxError, UnicodeDecodeError) as e:
        print(f"Warning: Could not parse {file_path}: {e}")
    
    return classes


def extract_enums_from_python(file_path: Path, module_prefix: str = '') -> Dict[str, Dict[str, Any]]:
    """
    Extract enumeration information from a Python file using AST.
    
    Returns: {enum_name: {literals: List[str], line_number: int}}
    """
    enums = {}
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            tree = ast.parse(content, filename=str(file_path))
            
            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef):
                    # Check if it's an enum (inherits from Enum or AREnum)
                    is_enum = False
                    for base in node.bases:
                        if isinstance(base, ast.Name) and base.id in ('Enum', 'AREnum'):
                            is_enum = True
                            break
                    
                    if is_enum:
                        # Extract enum literals
                        literals = []
                        for item in node.body:
                            if isinstance(item, ast.Assign):
                                for target in item.targets:
                                    if isinstance(target, ast.Name):
                                        # Check if value is a string
                                        if isinstance(item.value, ast.Constant) and isinstance(item.value.value, str):
                                            literals.append(item.value.value)
                                        elif isinstance(item.value, ast.Str):  # Python 3.7 compatibility
                                            literals.append(item.value.s)
                        
                        full_name = f"{module_prefix}.{node.name}" if module_prefix else node.name
                        enums[node.name] = {
                            'literals': literals,
                            'line_number': node.lineno,
                            'full_name': full_name
                        }
    except (SyntaxError, UnicodeDecodeError) as e:
        print(f"Warning: Could not parse {file_path}: {e}")
    
    return enums


def scan_implementation(
    project_root: Path,
    package_path: str,
    requirements_dir: Optional[Path] = None
) -> Dict[str, Dict[str, Any]]:
    """
    Scan Python implementation for a given package path.
    
    Args:
        project_root: Root directory of the project
        package_path: Package path (e.g., M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior)
        requirements_dir: Path to requirements directory (used to check expected package structure)
    
    Returns: {
        'classes': {class_name: {is_abstract, bases, line_number, location}},
        'enumerations': {enum_name: {literals, line_number, location}},
        'structure_mismatch': str (optional) - description of structure mismatch if any
    }
    """
    result = {
        'classes': {},
        'enumerations': {}
    }
    
    file_path, dir_path = package_path_to_python_path(package_path, project_root, requirements_dir)
    
    # Check for structure mismatch
    if requirements_dir:
        # Remove M2:: prefix (4 characters)
        pkg_path_check = package_path[4:] if package_path.startswith('M2::') else package_path
        relative_path = pkg_path_check.replace('::', '/')
        python_path = project_root / 'src' / 'armodel' / 'models' / 'M2' / relative_path
        
        py_file = python_path.with_suffix('.py')
        py_file_exists = py_file.exists()
        dir_exists = python_path.is_dir()
        
        has_subpackages = get_package_has_subpackages(requirements_dir, package_path)
        
        # Check for hybrid structure (both file and directory exist)
        if py_file_exists and dir_exists:
            result['structure_mismatch'] = (
                f"Hybrid structure: both {py_file.name} and {python_path.name}/ exist. "
                f"Requirements say this is a {'non-leaf' if has_subpackages else 'leaf'} package. "
                f"Expected: {'directory' if has_subpackages else 'single file'}."
            )
        # Check for wrong structure
        elif has_subpackages and py_file_exists and not dir_exists:
            result['structure_mismatch'] = (
                f"Wrong structure: Package should be a directory (has subpackages) "
                f"but is implemented as a single file {py_file.name}"
            )
        elif not has_subpackages and dir_exists and not py_file_exists:
            result['structure_mismatch'] = (
                f"Wrong structure: Package should be a single file (no subpackages) "
                f"but is implemented as a directory {python_path.name}/"
            )
    
    if not file_path and not dir_path:
        return result
    
    # Build module prefix
    if package_path.startswith('M2::'):
        relative = package_path[4:].replace('::', '.')
        module_prefix = f'armodel.models.M2.{relative}'
    else:
        module_prefix = package_path.replace('::', '.')
    
    # Scan file if exists
    if file_path:
        classes = extract_classes_from_python(file_path, module_prefix)
        enums = extract_enums_from_python(file_path, module_prefix)
        
        for name, info in classes.items():
            info['location'] = str(file_path.relative_to(project_root))
            result['classes'][name] = info
        
        for name, info in enums.items():
            info['location'] = str(file_path.relative_to(project_root))
            result['enumerations'][name] = info
    
    # Scan directory if exists
    if dir_path:
        for py_file in dir_path.rglob('*.py'):
            if py_file.name == '__init__.py':
                continue
            
            # Calculate module prefix for this file
            rel_path = py_file.relative_to(dir_path.parent)
            file_module = str(rel_path.with_suffix('')).replace(os.sep, '.')
            file_prefix = f"{module_prefix}.{file_module}" if file_module else module_prefix
            
            classes = extract_classes_from_python(py_file, file_prefix)
            enums = extract_enums_from_python(py_file, file_prefix)
            
            for name, info in classes.items():
                info['location'] = str(py_file.relative_to(project_root))
                result['classes'][name] = info
            
            for name, info in enums.items():
                info['location'] = str(py_file.relative_to(project_root))
                result['enumerations'][name] = info
    
    return result


def detect_duplicates(
    comparisons: List[Dict[str, Any]]
) -> Dict[str, Any]:
    """
    Detect duplicate class and enum definitions across different package paths.
    
    This validates CODING_RULE_STYLE_00009: Classes MUST be importable from only
    one module path (their mapped location). Finding a class in multiple package
    paths indicates a violation.
    
    Args:
        comparisons: List of comparison results from compare_packages()
    
    Returns: {
        'duplicate_classes': {class_name: [{package, location, full_name}, ...]},
        'duplicate_enums': {enum_name: [{package, location, full_name}, ...]},
        'summary': {
            'total_duplicate_classes': int,
            'total_duplicate_enums': int,
            'affected_packages': set of package names
        }
    }
    """
    result = {
        'duplicate_classes': {},
        'duplicate_enums': {},
        'summary': {
            'total_duplicate_classes': 0,
            'total_duplicate_enums': 0,
            'affected_packages': set()
        }
    }
    
    # Track all classes and enums across packages
    class_registry: Dict[str, List[Dict[str, Any]]] = {}
    enum_registry: Dict[str, List[Dict[str, Any]]] = {}
    
    for comp in comparisons:
        pkg_name = comp['package']
        
        # Collect implemented classes
        for cls in comp['classes']:
            if cls['implemented']:
                cls_name = cls['name']
                if cls_name not in class_registry:
                    class_registry[cls_name] = []
                
                class_registry[cls_name].append({
                    'package': pkg_name,
                    'location': cls['location'],
                    'full_name': f"armodel.models.M2.{pkg_name[4:].replace('::', '.')}.{cls_name}" if pkg_name.startswith('M2::') else f"{pkg_name.replace('::', '.')}.{cls_name}"
                })
        
        # Collect implemented enums
        for enum in comp['enumerations']:
            if enum['implemented']:
                enum_name = enum['name']
                if enum_name not in enum_registry:
                    enum_registry[enum_name] = []
                
                enum_registry[enum_name].append({
                    'package': pkg_name,
                    'location': enum['location'],
                    'full_name': f"armodel.models.M2.{pkg_name[4:].replace('::', '.')}.{enum_name}" if pkg_name.startswith('M2::') else f"{pkg_name.replace('::', '.')}.{enum_name}"
                })
    
    # Find duplicate classes (defined in more than one package)
    for cls_name, locations in class_registry.items():
        if len(locations) > 1:
            result['duplicate_classes'][cls_name] = locations
            result['summary']['total_duplicate_classes'] += 1
            for loc in locations:
                result['summary']['affected_packages'].add(loc['package'])
    
    # Find duplicate enums (defined in more than one package)
    for enum_name, locations in enum_registry.items():
        if len(locations) > 1:
            result['duplicate_enums'][enum_name] = locations
            result['summary']['total_duplicate_enums'] += 1
            for loc in locations:
                result['summary']['affected_packages'].add(loc['package'])
    
    # Convert set to list for JSON serialization
    result['summary']['affected_packages'] = sorted(result['summary']['affected_packages'])
    
    return result


def compare_packages(
    requirements_packages: List[Dict[str, Any]],
    project_root: Path,
    requirements_dir: Optional[Path] = None
) -> List[Dict[str, Any]]:
    """
    Compare requirements with implementations for all packages.
    
    Args:
        requirements_packages: List of package dictionaries from requirements
        project_root: Root directory of the project
        requirements_dir: Path to requirements directory (used to check expected package structure)
    
    Returns list of comparison results.
    """
    comparisons = []
    
    for pkg in requirements_packages:
        pkg_name = pkg['name']
        required_classes = pkg['classes']
        required_enums = pkg['enumerations']
        
        # Scan implementation
        implementation = scan_implementation(project_root, pkg_name, requirements_dir)
        impl_classes = implementation['classes']
        impl_enums = implementation['enumerations']
        
        # Compare classes
        class_comparisons = []
        for cls_name, cls_info in required_classes.items():
            if cls_name in impl_classes:
                # Class implemented
                impl_info = impl_classes[cls_name]
                status = '✅ Implemented'
                notes = f"Line {impl_info['line_number']}"
                class_comparisons.append({
                    'name': cls_name,
                    'status': status,
                    'required': True,
                    'implemented': True,
                    'location': impl_info['location'],
                    'notes': notes
                })
            else:
                # Class missing
                status = '❌ Missing'
                class_comparisons.append({
                    'name': cls_name,
                    'status': status,
                    'required': True,
                    'implemented': False,
                    'location': '-',
                    'notes': 'Not found in implementation'
                })
        
        # Find extra classes
        for cls_name, impl_info in impl_classes.items():
            if cls_name not in required_classes:
                status = '➕ Extra'
                class_comparisons.append({
                    'name': cls_name,
                    'status': status,
                    'required': False,
                    'implemented': True,
                    'location': impl_info['location'],
                    'notes': 'Not documented in requirements'
                })
        
        # Compare enumerations
        enum_comparisons = []
        for enum_name, enum_info in required_enums.items():
            if enum_name in impl_enums:
                # Enum implemented - compare literals
                impl_info = impl_enums[enum_name]
                required_literals = set(l['name'] for l in enum_info.get('literals', []))
                impl_literals = set(impl_info['literals'])
                
                if required_literals == impl_literals:
                    status = '✅ Implemented'
                    notes = f"Line {impl_info['line_number']}"
                    enum_comparisons.append({
                        'name': enum_name,
                        'status': status,
                        'required': True,
                        'implemented': True,
                        'location': impl_info['location'],
                        'required_literals': sorted(required_literals),
                        'implemented_literals': sorted(impl_literals),
                        'notes': notes
                    })
                else:
                    # Literal mismatch
                    missing = required_literals - impl_literals
                    extra = impl_literals - required_literals
                    notes_parts = [f"Line {impl_info['line_number']}"]
                    if missing:
                        notes_parts.append(f"Missing: {', '.join(sorted(missing))}")
                    if extra:
                        notes_parts.append(f"Extra: {', '.join(sorted(extra))}")
                    
                    status = '⚠️ Literal Mismatch'
                    enum_comparisons.append({
                        'name': enum_name,
                        'status': status,
                        'required': True,
                        'implemented': True,
                        'location': impl_info['location'],
                        'required_literals': sorted(required_literals),
                        'implemented_literals': sorted(impl_literals),
                        'notes': '; '.join(notes_parts)
                    })
            else:
                # Enum missing
                status = '❌ Missing'
                required_literals = [l['name'] for l in enum_info.get('literals', [])]
                enum_comparisons.append({
                    'name': enum_name,
                    'status': status,
                    'required': True,
                    'implemented': False,
                    'location': '-',
                    'required_literals': required_literals,
                    'implemented_literals': [],
                    'notes': 'Not found in implementation'
                })
        
        # Find extra enums
        for enum_name, impl_info in impl_enums.items():
            if enum_name not in required_enums:
                status = '➕ Extra'
                enum_comparisons.append({
                    'name': enum_name,
                    'status': status,
                    'required': False,
                    'implemented': True,
                    'location': impl_info['location'],
                    'required_literals': [],
                    'implemented_literals': impl_info['literals'],
                    'notes': 'Not documented in requirements'
                })
        
        comparisons.append({
            'package': pkg_name,
            'classes': class_comparisons,
            'enumerations': enum_comparisons,
            'required_classes_data': required_classes,
            'required_enums_data': required_enums,
            'structure_mismatch': implementation.get('structure_mismatch'),
            'summary': {
                'required_classes': len(required_classes),
                'implemented_classes': sum(1 for c in class_comparisons if c['implemented'] and c['required']),
                'missing_classes': sum(1 for c in class_comparisons if c['status'] == '❌ Missing'),
                'extra_classes': sum(1 for c in class_comparisons if c['status'] == '➕ Extra'),
                'required_enums': len(required_enums),
                'implemented_enums': sum(1 for e in enum_comparisons if e['implemented'] and e['required']),
                'missing_enums': sum(1 for e in enum_comparisons if e['status'] == '❌ Missing'),
                'extra_enums': sum(1 for e in enum_comparisons if e['status'] == '➕ Extra'),
                'enum_mismatches': sum(1 for e in enum_comparisons if e['status'] == '⚠️ Literal Mismatch')
            }
        })
    
    return comparisons


def generate_markdown_report(comparisons: List[Dict[str, Any]], output_path: str, verbose: bool = False):
    """Generate a markdown comparison report."""
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('# Package Implementation Comparison Report\n\n')
        f.write('This report compares AUTOSAR M2 package requirements with actual Python implementations.\n\n')
        
        # Overall summary
        total_packages = len(comparisons)
        total_required_classes = sum(c['summary']['required_classes'] for c in comparisons)
        total_implemented_classes = sum(c['summary']['implemented_classes'] for c in comparisons)
        total_missing_classes = sum(c['summary']['missing_classes'] for c in comparisons)
        total_extra_classes = sum(c['summary']['extra_classes'] for c in comparisons)
        total_required_enums = sum(c['summary']['required_enums'] for c in comparisons)
        total_implemented_enums = sum(c['summary']['implemented_enums'] for c in comparisons)
        total_missing_enums = sum(c['summary']['missing_enums'] for c in comparisons)
        total_extra_enums = sum(c['summary']['extra_enums'] for c in comparisons)
        total_enum_mismatches = sum(c['summary']['enum_mismatches'] for c in comparisons)
        
        f.write('## Overall Summary\n\n')
        f.write(f'- **Total Packages**: {total_packages}\n')
        f.write('\n### Classes\n')
        f.write(f'- **Required**: {total_required_classes}\n')
        f.write(f'- **Implemented**: {total_implemented_classes}\n')
        f.write(f'- **Missing**: {total_missing_classes}\n')
        f.write(f'- **Extra**: {total_extra_classes}\n')
        f.write('\n### Enumerations\n')
        f.write(f'- **Required**: {total_required_enums}\n')
        f.write(f'- **Implemented**: {total_implemented_enums}\n')
        f.write(f'- **Missing**: {total_missing_enums}\n')
        f.write(f'- **Extra**: {total_extra_enums}\n')
        f.write(f'- **Literal Mismatches**: {total_enum_mismatches}\n')
        
        # Detect duplicates
        duplicates = detect_duplicates(comparisons)
        
        # Add duplicate counts to summary
        total_duplicate_classes = duplicates['summary']['total_duplicate_classes']
        total_duplicate_enums = duplicates['summary']['total_duplicate_enums']
        
        if total_duplicate_classes > 0 or total_duplicate_enums > 0:
            f.write('\n### Duplicates (CODING_RULE_STYLE_00009 Violation)\n')
            f.write(f'- **Duplicate Classes**: {total_duplicate_classes}\n')
            f.write(f'- **Duplicate Enums**: {total_duplicate_enums}\n')
        
        # Determine overall status
        total_issues = total_missing_classes + total_missing_enums + total_enum_mismatches + total_duplicate_classes + total_duplicate_enums
        if total_issues == 0 and total_extra_classes == 0 and total_extra_enums == 0:
            overall_status = '✅ Complete'
        elif total_missing_classes > 0 or total_missing_enums > 0:
            overall_status = '❌ Incomplete'
        else:
            overall_status = '⚠️ Partial'
        
        f.write('\n### Overall Status\n')
        f.write(f'**{overall_status}**\n\n')
        
        # Legend
        f.write('## Legend\n\n')
        f.write('- ✅ Implemented: Class/enum is implemented and matches requirements\n')
        f.write('- ❌ Missing: Class/enum is required but not found in implementation\n')
        f.write('- ⚠️ Literal Mismatch: Enum exists but has different literal values\n')
        f.write('- ➕ Extra: Class/enum exists in implementation but not in requirements\n')
        f.write('- 🔄 Duplicate: Class/enum is defined in multiple package paths (CODING_RULE_STYLE_00009 violation)\n\n')
        
        # Duplicate definitions report
        if duplicates['summary']['total_duplicate_classes'] > 0 or duplicates['summary']['total_duplicate_enums'] > 0:
            f.write('## 🔄 Duplicate Definitions (CODING_RULE_STYLE_00009 Violation)\n\n')
            f.write('**Note**: Classes and enums should only be importable from their mapped module path. ')
            f.write('Finding duplicates in multiple package paths indicates a violation of the package structure convention.\n\n')
            
            f.write(f'- **Duplicate Classes**: {duplicates["summary"]["total_duplicate_classes"]}\n')
            f.write(f'- **Duplicate Enums**: {duplicates["summary"]["total_duplicate_enums"]}\n')
            f.write(f'- **Affected Packages**: {len(duplicates["summary"]["affected_packages"])}\n\n')
            
            if duplicates['duplicate_classes']:
                f.write('### Duplicate Classes\n\n')
                for cls_name in sorted(duplicates['duplicate_classes'].keys()):
                    locations = duplicates['duplicate_classes'][cls_name]
                    f.write(f'#### {cls_name}\n\n')
                    f.write(f'Found in **{len(locations)}** locations:\n\n')
                    f.write('| Package | Location | Full Import Path |\n')
                    f.write('|---------|----------|------------------|\n')
                    for loc in locations:
                        f.write(f"| {loc['package']} | {loc['location']} | `{loc['full_name']}` |\n")
                    f.write('\n')
            
            if duplicates['duplicate_enums']:
                f.write('### Duplicate Enums\n\n')
                for enum_name in sorted(duplicates['duplicate_enums'].keys()):
                    locations = duplicates['duplicate_enums'][enum_name]
                    f.write(f'#### {enum_name}\n\n')
                    f.write(f'Found in **{len(locations)}** locations:\n\n')
                    f.write('| Package | Location | Full Import Path |\n')
                    f.write('|---------|----------|------------------|\n')
                    for loc in locations:
                        f.write(f"| {loc['package']} | {loc['location']} | `{loc['full_name']}` |\n")
                    f.write('\n')
            
            f.write('---\n\n')
        
        # Packages with problems summary
        packages_with_problems = [c for c in comparisons if c['summary']['missing_classes'] > 0 or c['summary']['missing_enums'] > 0 or c['summary']['enum_mismatches'] > 0]
        
        if packages_with_problems:
            f.write('## Packages with Problems\n\n')
            f.write(f'**Total packages with issues**: {len(packages_with_problems)} out of {total_packages}\n\n')
            
            # Group packages by category
            categories = {}
            for comp in packages_with_problems:
                pkg_name = comp['package']
                # Extract category (first two parts after M2::)
                parts = pkg_name.split('::')
                if len(parts) >= 3:
                    category = '::'.join(parts[:3])
                else:
                    category = pkg_name
                
                if category not in categories:
                    categories[category] = []
                categories[category].append(comp)
            
            # Sort categories alphabetically
            for category in sorted(categories.keys()):
                f.write(f'### {category}\n\n')
                for comp in categories[category]:
                    pkg_name = comp['package']
                    summary = comp['summary']
                    issues = []
                    if summary['missing_classes'] > 0:
                        issues.append(f'{summary["missing_classes"]} missing classes')
                    if summary['missing_enums'] > 0:
                        issues.append(f'{summary["missing_enums"]} missing enums')
                    if summary['enum_mismatches'] > 0:
                        issues.append(f'{summary["enum_mismatches"]} literal mismatches')
                    
                    f.write(f'- **{pkg_name}**: {", ".join(issues)}\n')
                f.write('\n')
        
        # Package details
        f.write('## Package Details\n\n')
        
        for comp in comparisons:
            pkg_name = comp['package']
            summary = comp['summary']
            
            f.write(f'### Package: {pkg_name}\n\n')
            
            # Package summary
            f.write('**Summary:**\n')
            f.write(f'- Classes: {summary["implemented_classes"]}/{summary["required_classes"]} implemented')
            if summary['missing_classes'] > 0:
                f.write(f', {summary["missing_classes"]} missing')
            if summary['extra_classes'] > 0:
                f.write(f', {summary["extra_classes"]} extra')
            f.write('\n')
            f.write(f'- Enums: {summary["implemented_enums"]}/{summary["required_enums"]} implemented')
            if summary['missing_enums'] > 0:
                f.write(f', {summary["missing_enums"]} missing')
            if summary['enum_mismatches'] > 0:
                f.write(f', {summary["enum_mismatches"]} literal mismatches')
            if summary['extra_enums'] > 0:
                f.write(f', {summary["extra_enums"]} extra')
            f.write('\n\n')
            
            # Structure mismatch warning
            if comp.get('structure_mismatch'):
                f.write('⚠️ **Structure Mismatch Warning**\n\n')
                f.write(f"{comp['structure_mismatch']}\n\n")
            
            # Classes table
            if comp['classes']:
                f.write('#### Classes\n\n')
                f.write('| Status | Class Name | Location | Notes |\n')
                f.write('|--------|------------|----------|-------|\n')
                
                for cls in sorted(comp['classes'], key=lambda x: (x['status'], x['name'])):
                    f.write(f"| {cls['status']} | {cls['name']} | {cls['location']} | {cls['notes']} |\n")
                
                f.write('\n')
            
            # Enumerations table
            if comp['enumerations']:
                f.write('#### Enumerations\n\n')
                f.write('| Status | Enum Name | Required Literals | Implemented Literals | Location | Notes |\n')
                f.write('|--------|-----------|-------------------|----------------------|----------|-------|\n')
                
                for enum in sorted(comp['enumerations'], key=lambda x: (x['status'], x['name'])):
                    req_lit = ', '.join(enum['required_literals']) if enum['required_literals'] else '-'
                    impl_lit = ', '.join(enum['implemented_literals']) if enum['implemented_literals'] else '-'
                    f.write(f"| {enum['status']} | {enum['name']} | {req_lit} | {impl_lit} | {enum['location']} | {enum['notes']} |\n")
                
                f.write('\n')
        
        # Final status
        f.write('---\n\n')
        f.write('*Report generated by compare-package-implementation.py*\n')


def main():
    """Main entry point."""
    args = parse_args()
    
    # Show help if no arguments provided
    if len(sys.argv) == 1:
        parser = argparse.ArgumentParser(
            prog='compare-package-implementation.py',
            description='Compare AUTOSAR M2 package requirements with Python implementations',
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog="""
Examples:
  %(prog)s --all                                    Compare all packages
  %(prog)s -p M2::xxx::xxx                          Compare single package
  %(prog)s -p M2::xxx::xxx::xxx                     Compare subpackage
                """
        )
        parser.print_help()
        return 0
    
    # Define paths
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    requirements_dir = project_root / 'docs' / 'requirements'
    
    # Default output path
    if args.output:
        output_path = args.output
    else:
        output_path = str(project_root / 'reports' / 'package_comparison.md')
    
    print("=" * 60)
    print("Package Implementation Comparison Script")
    print("=" * 60)
    print(f"Project root: {project_root}")
    print(f"Requirements directory: {requirements_dir}")
    print(f"Output file: {output_path}")
    if args.package:
        print(f"Package filter: {args.package}")
    print()
    
    # Load requirements
    print("Loading requirements...")
    try:
        packages = get_all_packages(requirements_dir, args.package)
        if not packages:
            print("Error: No packages found")
            if args.package:
                print(f"  Package '{args.package}' not found in requirements")
            return 1
        print(f"  Found {len(packages)} package(s) to compare")
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return 1
    
    # Compare with implementation
    print("Comparing with implementation...")
    comparisons = compare_packages(packages, project_root, requirements_dir)
    print("  Comparison complete")
    
    # Generate report
    print("Generating markdown report...")
    # Ensure reports directory exists
    reports_dir = project_root / 'reports'
    reports_dir.mkdir(parents=True, exist_ok=True)
    generate_markdown_report(comparisons, output_path, args.verbose)
    print(f"  Report written to: {output_path}")
    
    # Print summary
    print()
    print("=" * 60)
    print("Summary")
    print("=" * 60)
    
    total_classes = sum(c['summary']['required_classes'] for c in comparisons)
    impl_classes = sum(c['summary']['implemented_classes'] for c in comparisons)
    missing_classes = sum(c['summary']['missing_classes'] for c in comparisons)
    extra_classes = sum(c['summary']['extra_classes'] for c in comparisons)
    
    total_enums = sum(c['summary']['required_enums'] for c in comparisons)
    impl_enums = sum(c['summary']['implemented_enums'] for c in comparisons)
    missing_enums = sum(c['summary']['missing_enums'] for c in comparisons)
    enum_mismatches = sum(c['summary']['enum_mismatches'] for c in comparisons)
    extra_enums = sum(c['summary']['extra_enums'] for c in comparisons)
    
    print(f"Classes: {impl_classes}/{total_classes} implemented")
    if missing_classes > 0:
        print(f"  ❌ {missing_classes} missing")
    if extra_classes > 0:
        print(f"  ➕ {extra_classes} extra")
    
    print(f"Enumerations: {impl_enums}/{total_enums} implemented")
    if missing_enums > 0:
        print(f"  ❌ {missing_enums} missing")
    if enum_mismatches > 0:
        print(f"  ⚠️ {enum_mismatches} literal mismatches")
    if extra_enums > 0:
        print(f"  ➕ {extra_enums} extra")
    
    # Detect and report duplicates
    duplicates = detect_duplicates(comparisons)
    total_duplicate_classes = duplicates['summary']['total_duplicate_classes']
    total_duplicate_enums = duplicates['summary']['total_duplicate_enums']
    
    if total_duplicate_classes > 0 or total_duplicate_enums > 0:
        print("\n🔄 Duplicate Definitions (CODING_RULE_STYLE_00009 Violation):")
        if total_duplicate_classes > 0:
            print(f"  ❌ {total_duplicate_classes} class(es) defined in multiple locations")
        if total_duplicate_enums > 0:
            print(f"  ❌ {total_duplicate_enums} enum(s) defined in multiple locations")
        print("  See the report for detailed location information")
    
    total_issues = missing_classes + missing_enums + enum_mismatches + total_duplicate_classes + total_duplicate_enums
    
    if total_issues == 0 and extra_classes == 0 and extra_enums == 0:
        print("\n✅ All requirements are satisfied!")
        return 0
    elif total_issues > 0:
        print(f"\n❌ {total_issues} issue(s) found")
        print("  Run 'python scripts/fix-package-implementation.py' to fix them.")
        return 1
    else:
        print(f"\n⚠️ All requirements satisfied, but {extra_classes + extra_enums} extra element(s) found")
        return 0


if __name__ == '__main__':
    exit(main())

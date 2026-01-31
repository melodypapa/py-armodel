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

import argparse
import ast
import json
import os
import re
from pathlib import Path
from typing import Dict, List, Set, Tuple, Optional, Any


def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description='Compare AUTOSAR M2 package requirements with Python implementations',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                                          Compare all packages
  %(prog)s --package M2::AUTOSARTemplates::BswModuleTemplate  Compare single package
  %(prog)s -p M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior  Compare subpackage
  %(prog)s --package M2::AUTOSARTemplates::BswModuleTemplate --fix  Fix issues found
  %(prog)s --package M2::AUTOSARTemplates::BswModuleTemplate --fix --dry-run  Preview fixes
        """
    )
    parser.add_argument(
        '--package', '-p',
        type=str,
        help='Specific package to compare (format: M2::xxx::xxxx)'
    )
    parser.add_argument(
        '--output', '-o',
        type=str,
        help='Output file path (default: docs/requirements/package_comparison.md)'
    )
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Enable verbose output'
    )
    parser.add_argument(
        '--fix',
        action='store_true',
        help='Automatically fix missing classes and enumeration mismatches'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Preview fixes without modifying files (use with --fix)'
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


def package_path_to_python_path(package_path: str, project_root: Path) -> Tuple[Optional[Path], Optional[Path]]:
    """
    Convert a package path to Python file/directory path.
    
    Returns a tuple of (file_path, directory_path). Either or both may be non-None.
    
    Examples:
        M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior
        -> (BswBehavior.py file, BswBehavior/ directory) if both exist
        -> (BswBehavior.py file, None) if only file exists
        -> (None, BswBehavior/ directory) if only directory exists
        
        M2::AUTOSARTemplates::BswModuleTemplate
        -> (None, BswModuleTemplate/ directory)
    """
    # Remove M2:: prefix (4 characters)
    if package_path.startswith('M2::'):
        package_path = package_path[4:]
    
    # Replace :: with /
    relative_path = package_path.replace('::', '/')
    
    # Build full path
    python_path = project_root / 'src' / 'armodel' / 'models' / 'M2' / relative_path
    
    # Check if .py file exists (for packages that are single files)
    py_file = python_path.with_suffix('.py')
    file_path = py_file if py_file.exists() else None
    
    # Check if directory exists (for packages with multiple files)
    dir_path = python_path if python_path.is_dir() else None
    
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


def scan_implementation(project_root: Path, package_path: str) -> Dict[str, Dict[str, Any]]:
    """
    Scan Python implementation for a given package path.
    
    Returns: {
        'classes': {class_name: {is_abstract, bases, line_number, location}},
        'enumerations': {enum_name: {literals, line_number, location}}
    }
    """
    result = {
        'classes': {},
        'enumerations': {}
    }
    
    file_path, dir_path = package_path_to_python_path(package_path, project_root)
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


def compare_packages(
    requirements_packages: List[Dict[str, Any]],
    project_root: Path
) -> List[Dict[str, Any]]:
    """
    Compare requirements with implementations for all packages.
    
    Returns list of comparison results.
    """
    comparisons = []
    
    for pkg in requirements_packages:
        pkg_name = pkg['name']
        required_classes = pkg['classes']
        required_enums = pkg['enumerations']
        
        # Scan implementation
        implementation = scan_implementation(project_root, pkg_name)
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


def generate_class_code(class_info: Dict[str, Any], package_path: str) -> str:
    """Generate Python class code from requirements JSON."""
    class_name = class_info['name']
    is_abstract = class_info.get('is_abstract', False)
    parent = class_info.get('parent', 'ARObject')
    attributes = class_info.get('attributes', {})
    
    # Build import statements
    imports = [
        'from typing import List, Optional, Dict',
    ]
    
    # Add ABC import for abstract classes
    if is_abstract:
        imports.insert(0, 'from abc import ABC')
    
    # Build class declaration
    bases = [parent]
    if is_abstract:
        bases.append('ABC')
    
    class_decl = f"class {class_name}({', '.join(bases)}):"
    
    # Build __init__ method
    if is_abstract:
        init_code = f'''    def __init__(self):
        if type(self) is {class_name}:
            raise TypeError("{class_name} is an abstract class.")
        super().__init__()'''
    else:
        init_code = f'''    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)'''
    
    # Build attributes
    attr_code = []
    for attr_name, attr_info in attributes.items():
        attr_type = attr_info.get('type', 'Any')
        multiplicity = attr_info.get('multiplicity', '1')
        is_ref = attr_info.get('is_ref', False)
        
        # Determine Python type
        if multiplicity == '*':
            py_type = f'List[{attr_type}]'
            attr_code.append(f'        self.{attr_name}: {py_type} = []')
            attr_code.append(f'        self.{attr_name}_mapping: Dict[str, List[{attr_type}]] = {{}}')
        elif multiplicity == '0..1':
            py_type = f'Optional[{attr_type}]'
            attr_code.append(f'        self.{attr_name}: {py_type} = None')
        else:
            py_type = attr_type
            attr_code.append(f'        self.{attr_name}: {py_type}')
    
    # Build getter/setter methods
    methods_code = []
    for attr_name, attr_info in attributes.items():
        attr_type = attr_info.get('type', 'Any')
        multiplicity = attr_info.get('multiplicity', '1')
        
        # Getter
        if multiplicity == '*':
            getter_code = f'''    def get{attr_name[0].upper()}{attr_name[1:]}(self) -> List[{attr_type}]:
        return self.{attr_name}'''
        else:
            getter_code = f'''    def get{attr_name[0].upper()}{attr_name[1:]}(self) -> {attr_type}:
        return self.{attr_name}'''
        
        methods_code.append(getter_code)
        
        # Setter
        if multiplicity == '*':
            setter_code = f'''    def set{attr_name[0].upper()}{attr_name[1:]}(self, value: List[{attr_type}]):
        self.{attr_name} = value
        return self'''
        else:
            setter_code = f'''    def set{attr_name[0].upper()}{attr_name[1:]}(self, value: {attr_type}):
        self.{attr_name} = value
        return self'''
        
        methods_code.append(setter_code)
    
    # Combine all parts
    code_parts = imports + [''] + [class_decl, init_code, ''] + attr_code + [''] + methods_code
    
    return '\n'.join(code_parts)


def generate_enum_code(enum_info: Dict[str, Any], package_path: str) -> str:
    """Generate Python enumeration code from requirements JSON."""
    enum_name = enum_info['name']
    literals = enum_info.get('literals', [])
    
    # Build import statement
    imports = [
        'from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum',
    ]
    
    # Build enum declaration
    enum_decl = f"class {enum_name}(AREnum):"
    
    # Build literal definitions
    literal_code = []
    literal_refs = []
    for literal in literals:
        literal_name = literal['name'].upper().replace('-', '_')
        literal_value = literal['name']
        literal_code.append(f'    {literal_name} = "{literal_value}"')
        literal_refs.append(f'{enum_name}.{literal_name}')
    
    # Build __init__ method
    literal_refs_str = ',\n            '.join(literal_refs)
    init_code = f'''    def __init__(self):
        super().__init__((
            {literal_refs_str},
        ))'''
    
    # Combine all parts
    code_parts = imports + [''] + [enum_decl] + literal_code + [''] + [init_code]
    
    return '\n'.join(code_parts)


def fix_missing_class(class_name: str, class_info: Dict[str, Any], package_path: str, project_root: Path, dry_run: bool = False) -> bool:
    """Fix a missing class by generating and writing the class code."""
    print(f"\n[Fix] Generating missing class: {class_name}")
    
    # Determine target file location
    # Remove M2:: prefix
    if package_path.startswith('M2::'):
        relative = package_path[4:].replace('::', '/')
        package_dir = project_root / 'src' / 'armodel' / 'models' / 'M2' / relative
    
    # Check if class file exists
    class_file = package_dir / f'{class_name}.py'
    
    # Check if package directory exists
    if not class_file.exists():
        if package_dir.is_dir():
            # Create file in package directory
            class_file = package_dir / f'{class_name}.py'
        else:
            # Create subdirectory for the class
            class_subdir = package_dir / class_name
            class_subdir.mkdir(parents=True, exist_ok=True)
            class_file = class_subdir / f'{class_name}.py'
    
    # Generate class code
    code = generate_class_code(class_info, package_path)
    
    if dry_run:
        print(f"  [Dry Run] Would create file: {class_file.relative_to(project_root)}")
        print(f"  [Dry Run] Class code preview:")
        print("  " + "\n  ".join(code.split('\n')[:10]))
        if len(code.split('\n')) > 10:
            print("  ...")
        return True
    
    # Write class file
    try:
        class_file.parent.mkdir(parents=True, exist_ok=True)
        with open(class_file, 'w', encoding='utf-8') as f:
            f.write(code + '\n')
        print(f"  ✓ Created: {class_file.relative_to(project_root)}")
        
        # Update parent __init__.py if needed
        parent_init = package_dir / '__init__.py'
        if parent_init.exists():
            with open(parent_init, 'r', encoding='utf-8') as f:
                init_content = f.read()
            
            if f'from .{class_name} import {class_name}' not in init_content:
                # Add import
                with open(parent_init, 'a', encoding='utf-8') as f:
                    f.write(f'\nfrom .{class_name} import {class_name}\n')
                print(f"  ✓ Updated: {parent_init.relative_to(project_root)}")
        
        return True
    except Exception as e:
        print(f"  ✗ Error: {e}")
        return False


def fix_enum_literals(enum_name: str, enum_info: Dict[str, Any], impl_info: Dict[str, Any], package_path: str, project_root: Path, dry_run: bool = False) -> bool:
    """Fix enumeration literal mismatches."""
    required_literals = [l['name'] for l in enum_info.get('literals', [])]
    impl_literals = impl_info.get('implemented_literals', [])
    
    print(f"\n[Fix] Fixing enum literals: {enum_name}")
    print(f"  Required: {', '.join(required_literals)}")
    print(f"  Current:  {', '.join(impl_literals)}")
    
    # Determine target file location
    location = impl_info.get('location', '')
    if not location:
        print(f"  ✗ Error: Cannot determine file location")
        return False
    
    enum_file = project_root / location
    
    if dry_run:
        print(f"  [Dry Run] Would update: {enum_file.relative_to(project_root)}")
        return True
    
    # Generate new enum code
    code = generate_enum_code(enum_info, package_path)
    
    # Write enum file
    try:
        # Create backup
        backup_file = enum_file.with_suffix('.py.bak')
        if enum_file.exists():
            with open(enum_file, 'r', encoding='utf-8') as f:
                original_content = f.read()
            with open(backup_file, 'w', encoding='utf-8') as f:
                f.write(original_content)
            print(f"  ✓ Backup created: {backup_file.relative_to(project_root)}")
        
        # Write new code
        enum_file.parent.mkdir(parents=True, exist_ok=True)
        with open(enum_file, 'w', encoding='utf-8') as f:
            f.write(code + '\n')
        print(f"  ✓ Updated: {enum_file.relative_to(project_root)}")
        
        return True
    except Exception as e:
        print(f"  ✗ Error: {e}")
        return False


def apply_fixes(comparisons: List[Dict[str, Any]], project_root: Path, requirements_dir: Path, dry_run: bool = False) -> Dict[str, int]:
    """Apply fixes for missing classes and enum mismatches."""
    print("\n" + "=" * 60)
    print("Applying Fixes")
    print("=" * 60)
    
    if dry_run:
        print("[DRY RUN MODE - No files will be modified]")
    
    stats = {
        'classes_fixed': 0,
        'enums_fixed': 0,
        'errors': 0
    }
    
    for comp in comparisons:
        pkg_name = comp['package']
        classes = comp['classes']
        enums = comp['enumerations']
        required_classes_data = comp.get('required_classes_data', {})
        required_enums_data = comp.get('required_enums_data', {})
        
        print(f"\nPackage: {pkg_name}")
        
        # Fix missing classes
        for cls in classes:
            if cls['status'] == '❌ Missing':
                # Get class info from requirements
                class_info = required_classes_data.get(cls['name'], {})
                if class_info:
                    if fix_missing_class(cls['name'], class_info, pkg_name, project_root, dry_run):
                        stats['classes_fixed'] += 1
                    else:
                        stats['errors'] += 1
                else:
                    print(f"  ✗ Warning: No class info found for {cls['name']}")
                    stats['errors'] += 1
        
        # Fix enum mismatches
        for enum in enums:
            if enum['status'] == '⚠️ Literal Mismatch':
                # Get enum info from requirements
                enum_info = required_enums_data.get(enum['name'], {})
                
                if enum_info and fix_enum_literals(enum['name'], enum_info, enum, pkg_name, project_root, dry_run):
                    stats['enums_fixed'] += 1
                else:
                    if not enum_info:
                        print(f"  ✗ Warning: No enum info found for {enum['name']}")
                    stats['errors'] += 1
    
    return stats


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
        f.write(f'\n### Classes\n')
        f.write(f'- **Required**: {total_required_classes}\n')
        f.write(f'- **Implemented**: {total_implemented_classes}\n')
        f.write(f'- **Missing**: {total_missing_classes}\n')
        f.write(f'- **Extra**: {total_extra_classes}\n')
        f.write(f'\n### Enumerations\n')
        f.write(f'- **Required**: {total_required_enums}\n')
        f.write(f'- **Implemented**: {total_implemented_enums}\n')
        f.write(f'- **Missing**: {total_missing_enums}\n')
        f.write(f'- **Extra**: {total_extra_enums}\n')
        f.write(f'- **Literal Mismatches**: {total_enum_mismatches}\n')
        
        # Determine overall status
        total_issues = total_missing_classes + total_missing_enums + total_enum_mismatches
        if total_issues == 0 and total_extra_classes == 0 and total_extra_enums == 0:
            overall_status = '✅ Complete'
        elif total_missing_classes > 0 or total_missing_enums > 0:
            overall_status = '❌ Incomplete'
        else:
            overall_status = '⚠️ Partial'
        
        f.write(f'\n### Overall Status\n')
        f.write(f'**{overall_status}**\n\n')
        
        # Legend
        f.write('## Legend\n\n')
        f.write('- ✅ Implemented: Class/enum is implemented and matches requirements\n')
        f.write('- ❌ Missing: Class/enum is required but not found in implementation\n')
        f.write('- ⚠️ Literal Mismatch: Enum exists but has different literal values\n')
        f.write('- ➕ Extra: Class/enum exists in implementation but not in requirements\n\n')
        
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
    
    # Define paths
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    requirements_dir = project_root / 'docs' / 'requirements'
    
    # Default output path
    if args.output:
        output_path = args.output
    else:
        output_path = str(requirements_dir / 'package_comparison.md')
    
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
            print(f"Error: No packages found")
            if args.package:
                print(f"  Package '{args.package}' not found in requirements")
            return 1
        print(f"  Found {len(packages)} package(s) to compare")
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return 1
    
    # Compare with implementation
    print("Comparing with implementation...")
    comparisons = compare_packages(packages, project_root)
    print(f"  Comparison complete")
    
    # Generate report
    print("Generating markdown report...")
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
    
    total_issues = missing_classes + missing_enums + enum_mismatches
    
    # Apply fixes if --fix flag is set
    if args.fix and total_issues > 0:
        stats = apply_fixes(comparisons, project_root, requirements_dir, args.dry_run)
        
        print("\n" + "=" * 60)
        print("Fix Summary")
        print("=" * 60)
        print(f"Classes fixed: {stats['classes_fixed']}")
        print(f"Enums fixed: {stats['enums_fixed']}")
        print(f"Errors: {stats['errors']}")
        
        if args.dry_run:
            print("\n[DRY RUN COMPLETE - No files were modified]")
    
    if total_issues == 0 and extra_classes == 0 and extra_enums == 0:
        print("\n✅ All requirements are satisfied!")
        return 0
    elif total_issues > 0:
        if args.fix:
            if args.dry_run:
                return 1
            elif stats['classes_fixed'] > 0 or stats['enums_fixed'] > 0:
                print(f"\n✅ Fixes applied! Run again to verify.")
                return 0
        print(f"\n❌ {total_issues} issue(s) found")
        return 1
    else:
        print(f"\n⚠️ All requirements satisfied, but {extra_classes + extra_enums} extra element(s) found")
        return 0


if __name__ == '__main__':
    exit(main())

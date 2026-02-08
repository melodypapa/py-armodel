#!/usr/bin/env python3
"""Add missing type imports to V2 model files."""

import subprocess
import re
from pathlib import Path
from collections import defaultdict

# Map of class names to their import paths
CLASS_IMPORT_MAP = {
    'Boolean': 'armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes',
    'ARElement': 'armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable',
    'ARObject': 'armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject',
    'Identifiable': 'armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable',
    'AutosarDataPrototype': 'armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes',
    'PositiveInteger': 'armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes',
    'DataLinkLayerRule': 'armodel.v2.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.Firewall.DataLinkLayerRule',
    'DdsRule': 'armodel.v2.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.Firewall.DdsRule',
    'DoIpRule': 'armodel.v2.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.Firewall.DoIpRule',
    'NetworkLayerRule': 'armodel.v2.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.Firewall.NetworkLayerRule',
    'PayloadBytePattern': 'armodel.v2.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.Firewall.PayloadBytePattern',
    'SomeipProtocolRule': 'armodel.v2.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.Firewall.SomeipProtocolRule',
    'SomeipSdRule': 'armodel.v2.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.Firewall.SomeipSdRule',
    'TransportLayerRule': 'armodel.v2.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.Firewall.TransportLayerRule',
    'Field': 'armodel.v2.models.M2.AUTOSARTemplates.AdaptivePlatform.ApplicationDesign.PortInterface',
    'FirewallRule': 'armodel.v2.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.Firewall.FirewallRule',
    # Add more mappings as needed
}

def analyze_undefined_names(file_path: Path) -> set:
    """Analyze a file to find undefined names."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Run ruff to get F821 errors
        result = subprocess.run(
            ['ruff', 'check', str(file_path), '--output-format', 'concise'],
            capture_output=True,
            text=True
        )
        
        undefined_names = set()
        for line in result.stdout.split('\n'):
            if 'F821' in line:
                # Extract the undefined name
                # Format: file:line:col: F821 Undefined name `ClassName`
                match = re.search(r"Undefined name `([^']+)`", line)
                if match:
                    undefined_names.add(match.group(1))
        
        return undefined_names
    except Exception as e:
        print(f"Error analyzing {file_path}: {e}", file=sys.stderr)
        return set()

def add_missing_imports(file_path: Path, undefined_names: set) -> bool:
    """Add missing imports to a file."""
    if not undefined_names:
        return False
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # Find where to add imports (after existing imports)
        import_insert_pos = 0
        has_imports = False
        for i, line in enumerate(lines):
            if line.strip().startswith('from ') or line.strip().startswith('import '):
                has_imports = True
            elif has_imports and line.strip() == '':
                import_insert_pos = i + 1
                break
            elif not line.strip() and has_imports:
                # We found the first blank line after imports
                import_insert_pos = i + 1
                break
        
        # Build import statements
        imports_to_add = []
        imports_by_module = defaultdict(list)
        
        for name in undefined_names:
            if name in CLASS_IMPORT_MAP:
                imports_by_module[CLASS_IMPORT_MAP[name]].append(name)
            else:
                # Try to find the class in the codebase
                imports_by_module[f'armodel.v2.models.M2.AUTOSARTemplates'].append(name)
        
        # Create import statements
        for module_path, names in imports_by_module.items():
            if len(names) == 1:
                imports_to_add.append(f"from {module_path} import {names[0]}\n")
            else:
                names_str = ',\n    '.join(names)
                imports_to_add.append(f"from {module_path} import (\n    {names_str},\n)\n")
        
        if not imports_to_add:
            return False
        
        # Insert imports
        lines[import_insert_pos:import_insert_pos] = imports_to_add
        
        # Write back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(lines)
        
        return True
    except Exception as e:
        print(f"Error processing {file_path}: {e}", file=sys.stderr)
        return False

def main():
    """Main function."""
    v2_dir = Path('/Users/ray/Workspace/py-armodel/worktree/src/armodel/v2/models/M2/AUTOSARTemplates')
    
    if not v2_dir.exists():
        print(f"Directory not found: {v2_dir}")
        return
    
    # Get list of all Python files
    py_files = list(v2_dir.rglob('*.py'))
    
    fixed_count = 0
    for py_file in py_files:
        undefined_names = analyze_undefined_names(py_file)
        if undefined_names:
            if add_missing_imports(py_file, undefined_names):
                print(f"Fixed imports in: {py_file}")
                fixed_count += 1
    
    print(f"\nTotal files fixed: {fixed_count}")

if __name__ == '__main__':
    import sys
    main()
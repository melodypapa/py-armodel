# AUTOSAR M2 Class Generation System Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use @superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Build an automated system to generate 1,195 missing AUTOSAR M2 model classes from M2 documentation with XSD validation.

**Architecture:** Four-component pipeline (DeviationParser → M2DocumentationAnalyzer → PythonClassGenerator → XSDValidator) that extracts class definitions from markdown docs, generates Python code following project patterns, and validates against XSD schemas.

**Tech Stack:** Python 3.10+, lxml (XSD parsing), regex (markdown parsing), pytest (testing), existing project structure (src/armodel/models/M2/)

---

## Task 1: Create Project Structure and Utilities

**Files:**
- Create: `scripts/__init__.py`
- Create: `scripts/deviation_parser.py`
- Create: `scripts/m2_documentation_analyzer.py`
- Create: `scripts/python_class_generator.py`
- Create: `scripts/xsd_validator.py`
- Create: `scripts/test_generator.py`
- Create: `scripts/generate_missing_classes.py`

### Step 1: Create scripts package init file

```bash
touch scripts/__init__.py
```

### Step 2: Verify scripts directory structure

Run: `ls -la scripts/`
Expected: See `__init__.py` and existing scripts like `run_tests.py`

### Step 3: Commit

```bash
git add scripts/__init__.py
git commit -m "feat: add scripts package init for class generation tooling"
```

---

## Task 2: Implement DeviationParser Class

**Files:**
- Create: `scripts/deviation_parser.py`
- Test: `tests/test_armodel/test_deviation_parser.py`

### Step 1: Write the failing test

Create: `tests/test_armodel/test_deviation_parser.py`

```python
import pytest
from scripts.deviation_parser import DeviationParser

def test_parse_missing_classes():
    """Test that parser extracts missing classes from deviation report."""
    parser = DeviationParser('docs/requirements/deviation_package.md')
    missing_classes = parser.get_missing_classes()

    # Should have 1195 missing classes
    assert len(missing_classes) == 1195

    # Check a known missing class
    bsw_event = next((c for c in missing_classes if c['name'] == 'BswEvent'), None)
    assert bsw_event is not None
    assert bsw_event['m2_path'] == 'M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior::BswEvent'
    assert bsw_event['expected_path'] == 'armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.BswEvent'
    assert bsw_event['is_abstract'] == True

def test_group_classes_by_domain():
    """Test that classes are grouped by AUTOSAR domain."""
    parser = DeviationParser('docs/requirements/deviation_package.md')
    grouped = parser.get_classes_by_domain()

    # Should have domains like CommonStructure, BswModuleTemplate, etc.
    assert 'CommonStructure' in grouped
    assert 'BswModuleTemplate' in grouped

    # CommonStructure should have ~150 missing classes
    assert len(grouped['CommonStructure']) > 100
```

### Step 2: Run test to verify it fails

Run: `pytest tests/test_armodel/test_deviation_parser.py -v`
Expected: FAIL with "ModuleNotFoundError: No module named 'scripts.deviation_parser'"

### Step 3: Write minimal implementation

Create: `scripts/deviation_parser.py`

```python
import re
from typing import List, Dict, Any

class DeviationParser:
    """Parses deviation report to extract missing AUTOSAR classes."""

    def __init__(self, deviation_file: str):
        """Initialize parser with deviation report file path.

        Args:
            deviation_file: Path to deviation_package.md
        """
        self.deviation_file = deviation_file
        self._missing_classes = None

    def get_missing_classes(self) -> List[Dict[str, Any]]:
        """Extract all missing classes from deviation report.

        Returns:
            List of dicts with keys: name, m2_path, expected_path, is_abstract
        """
        if self._missing_classes is not None:
            return self._missing_classes

        self._missing_classes = []
        with open(self.deviation_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Parse deviation table rows marked as MISSING
        # Pattern: | ✗ MISSING | M2: M2::... | Expected: ... |
        pattern = r'\| ✗ MISSING \| M2: (.*?)\s*<br>Expected: (.*?)\s*<br>Actual: Not Found \|'
        matches = re.findall(pattern, content)

        for m2_path, expected_path in matches:
            class_name = self._extract_class_name(m2_path)
            is_abstract = '(abstract)' in m2_path or '(interface)' in m2_path

            self._missing_classes.append({
                'name': class_name,
                'm2_path': m2_path,
                'expected_path': expected_path,
                'is_abstract': is_abstract
            })

        return self._missing_classes

    def get_classes_by_domain(self) -> Dict[str, List[Dict[str, Any]]]:
        """Group missing classes by AUTOSAR domain.

        Returns:
            Dict mapping domain name to list of classes
        """
        classes = self.get_missing_classes()
        grouped = {}

        for cls in classes:
            # Extract domain from M2 path (second component after M2::AUTOSARTemplates::)
            # e.g., M2::AUTOSARTemplates::CommonStructure::... -> CommonStructure
            parts = cls['m2_path'].split('::')
            if len(parts) >= 3:
                domain = parts[2]
                if domain not in grouped:
                    grouped[domain] = []
                grouped[domain].append(cls)

        return grouped

    def _extract_class_name(self, m2_path: str) -> str:
        """Extract class name from M2 path.

        Args:
            m2_path: M2 path like "M2::AUTOSARTemplates::...::ClassName"

        Returns:
            Class name (without abstract/interface markers)
        """
        # Get last component
        parts = m2_path.split('::')
        name = parts[-1]

        # Remove qualifiers like " (abstract)" or " (interface)"
        name = re.sub(r'\s*\(.*?\)', '', name)

        return name
```

### Step 4: Run test to verify it passes

Run: `pytest tests/test_armodel/test_deviation_parser.py::test_parse_missing_classes -v`
Expected: PASS

### Step 5: Run second test

Run: `pytest tests/test_armodel/test_deviation_parser.py::test_group_classes_by_domain -v`
Expected: PASS

### Step 6: Commit

```bash
git add scripts/deviation_parser.py tests/test_armodel/test_deviation_parser.py
git commit -m "feat: implement DeviationParser to extract missing classes from deviation report"
```

---

## Task 3: Implement M2DocumentationAnalyzer Class

**Files:**
- Create: `scripts/m2_documentation_analyzer.py`
- Test: `tests/test_armodel/test_m2_documentation_analyzer.py`

### Step 1: Write the failing test

Create: `tests/test_armodel/test_m2_documentation_analyzer.py`

```python
import pytest
from scripts.m2_documentation_analyzer import M2DocumentationAnalyzer

def test_analyzer_loads_m2_docs():
    """Test that analyzer scans and indexes M2 documentation."""
    analyzer = M2DocumentationAnalyzer('docs/requirements/M2')

    # Should find ~1709 documentation files
    assert len(analyzer.get_all_classes()) > 1500

def test_get_class_metadata():
    """Test extracting metadata for a specific class."""
    analyzer = M2DocumentationAnalyzer('docs/requirements/M2')

    metadata = analyzer.get_class_metadata('ARElement')

    assert metadata is not None
    assert metadata['package'] == 'M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::ARPackage'
    assert metadata['type'] == 'Abstract'
    assert metadata['parent'] == 'PackageableElement'
    assert 'ARObject' in metadata['base_classes']
    assert len(metadata['children']) > 0  # ARElement has many children

def test_cache_parsing_results():
    """Test that analyzer caches results for fast reload."""
    import os
    import json

    analyzer = M2DocumentationAnalyzer('docs/requirements/M2', cache_file='/tmp/test_m2_cache.json')

    # First run - should parse files
    class_count_1 = len(analyzer.get_all_classes())

    # Create new instance with same cache
    analyzer2 = M2DocumentationAnalyzer('docs/requirements/M2', cache_file='/tmp/test_m2_cache.json')
    class_count_2 = len(analyzer2.get_all_classes())

    assert class_count_1 == class_count_2

    # Cleanup
    if os.path.exists('/tmp/test_m2_cache.json'):
        os.remove('/tmp/test_m2_cache.json')
```

### Step 2: Run test to verify it fails

Run: `pytest tests/test_armodel/test_m2_documentation_analyzer.py -v`
Expected: FAIL with "ModuleNotFoundError: No module named 'scripts.m2_documentation_analyzer'"

### Step 3: Write minimal implementation

Create: `scripts/m2_documentation_analyzer.py`

```python
import os
import re
import json
from pathlib import Path
from typing import Dict, List, Optional, Any

class M2DocumentationAnalyzer:
    """Analyzes M2 documentation to extract class metadata."""

    def __init__(self, m2_docs_dir: str, cache_file: Optional[str] = None):
        """Initialize analyzer with M2 documentation directory.

        Args:
            m2_docs_dir: Path to docs/requirements/M2/
            cache_file: Optional path to cache parsing results
        """
        self.m2_docs_dir = Path(m2_docs_dir)
        self.cache_file = cache_file
        self._class_index = None

        # Try loading from cache first
        if cache_file and Path(cache_file).exists():
            self._load_from_cache()

    def get_all_classes(self) -> Dict[str, Dict[str, Any]]:
        """Get all classes from M2 documentation.

        Returns:
            Dict mapping class name to metadata
        """
        if self._class_index is None:
            self._build_index()
        return self._class_index

    def get_class_metadata(self, class_name: str) -> Optional[Dict[str, Any]]:
        """Get metadata for a specific class.

        Args:
            class_name: Name of the class to look up

        Returns:
            Dict with keys: package, type, parent, base_classes, children, document_source
            or None if class not found
        """
        all_classes = self.get_all_classes()
        return all_classes.get(class_name)

    def _build_index(self):
        """Scan all markdown files and build class index."""
        self._class_index = {}

        # Find all .md files in M2 directory
        md_files = list(self.m2_docs_dir.rglob('*.md'))

        for md_file in md_files:
            self._parse_md_file(md_file)

        # Save to cache if specified
        if self.cache_file:
            self._save_to_cache()

    def _parse_md_file(self, md_file: Path):
        """Parse a single markdown documentation file.

        Args:
            md_file: Path to .md file
        """
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Extract class name from filename (convert PascalCase to class name)
        class_name = md_file.stem

        # Initialize metadata
        metadata = {
            'package': self._extract_section(content, 'Package'),
            'type': self._extract_section(content, 'Type'),
            'parent': self._extract_section(content, 'Parent'),
            'base_classes': self._extract_list(content, 'Base Classes'),
            'subclasses': self._extract_list(content, 'Subclasses'),
            'children': self._extract_list(content, 'Children'),
            'document_source': self._extract_document_source(content)
        }

        self._class_index[class_name] = metadata

    def _extract_section(self, content: str, section_name: str) -> Optional[str]:
        """Extract a section value from markdown.

        Args:
            content: Markdown file content
            section_name: Name of section (e.g., "Package", "Type")

        Returns:
            Section value or None
        """
        pattern = rf'## {section_name}\s*\n\s*(.*?)\s*\n'
        match = re.search(pattern, content, re.DOTALL)
        return match.group(1).strip() if match else None

    def _extract_list(self, content: str, section_name: str) -> List[str]:
        """Extract a bulleted list from markdown.

        Args:
            content: Markdown file content
            section_name: Name of section with list

        Returns:
            List of items (without bullet points)
        """
        items = []

        # Find the section
        pattern = rf'## {section_name}\s*\n(.*?)(?=\n##|\Z)'
        match = re.search(pattern, content, re.DOTALL)

        if match:
            section_content = match.group(1)
            # Extract bullet points
            for line in section_content.split('\n'):
                line = line.strip()
                if line.startswith('* '):
                    items.append(line[2:].strip())

        return items

    def _extract_document_source(self, content: str) -> List[Dict[str, str]]:
        """Extract document source table.

        Args:
            content: Markdown file content

        Returns:
            List of dicts with pdf_file, page, standard, release
        """
        sources = []

        # Find document source table
        pattern = r'## Document Source\s*\n(.*?)(?=\n##|\Z)'
        match = re.search(pattern, content, re.DOTALL)

        if match:
            table_content = match.group(1)
            # Extract table rows (simplified - skip header)
            rows = re.findall(r'\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|', table_content)
            for pdf, page, standard, release in rows[1:]:  # Skip header
                if pdf and pdf != 'PDF File':  # Skip header row
                    sources.append({
                        'pdf_file': pdf.strip(),
                        'page': page.strip(),
                        'standard': standard.strip(),
                        'release': release.strip()
                    })

        return sources

    def _save_to_cache(self):
        """Save index to cache file."""
        if self.cache_file:
            with open(self.cache_file, 'w', encoding='utf-8') as f:
                json.dump(self._class_index, f, indent=2)

    def _load_from_cache(self):
        """Load index from cache file."""
        if self.cache_file and Path(self.cache_file).exists():
            with open(self.cache_file, 'r', encoding='utf-8') as f:
                self._class_index = json.load(f)
```

### Step 4: Run tests to verify they pass

Run: `pytest tests/test_armodel/test_m2_documentation_analyzer.py -v`
Expected: All tests PASS

### Step 5: Commit

```bash
git add scripts/m2_documentation_analyzer.py tests/test_armodel/test_m2_documentation_analyzer.py
git commit -m "feat: implement M2DocumentationAnalyzer to index class definitions from markdown docs"
```

---

## Task 4: Implement PythonClassGenerator Class - Basic Structure

**Files:**
- Create: `scripts/python_class_generator.py`
- Test: `tests/test_armodel/test_python_class_generator.py`

### Step 1: Write the failing test for basic class generation

Create: `tests/test_armodel/test_python_class_generator.py`

```python
import pytest
import os
import tempfile
import shutil
from scripts.python_class_generator import PythonClassGenerator

def test_generate_simple_concrete_class():
    """Test generating a simple concrete class."""
    # Create temporary directory
    with tempfile.TemporaryDirectory() as tmpdir:
        generator = PythonClassGenerator(
            base_path=tmpdir,
            m2_analyzer=None  # Will provide metadata directly
        )

        metadata = {
            'name': 'TestComponent',
            'package': 'M2::AUTOSARTemplates::SwComponentTemplate',
            'type': 'Concrete',
            'parent': 'Referrable',
            'base_classes': ['ARObject', 'Referrable'],
            'children': []
        }

        output_file = generator.generate_class(metadata)

        # Verify file was created
        assert os.path.exists(output_file)
        assert output_file.endswith('SwComponentTemplate/TestComponent.py')

        # Verify content
        with open(output_file, 'r') as f:
            content = f.read()

        assert 'class TestComponent(Referrable):' in content
        assert 'def __init__' in content
        assert 'def getShortName' in content
        assert 'def setShortName' in content

def test_generate_abstract_class():
    """Test generating an abstract class."""
    with tempfile.TemporaryDirectory() as tmpdir:
        generator = PythonClassGenerator(base_path=tmpdir, m2_analyzer=None)

        metadata = {
            'name': 'AbstractTest',
            'package': 'M2::AUTOSARTemplates::CommonStructure',
            'type': 'Abstract',
            'parent': None,
            'base_classes': ['ARObject'],
            'children': []
        }

        output_file = generator.generate_class(metadata)

        with open(output_file, 'r') as f:
            content = f.read()

        # Should import ABC
        assert 'from abc import ABC' in content or 'from abc import ABC, abstractmethod' in content
        assert 'class AbstractTest(ABC' in content
```

### Step 2: Run test to verify it fails

Run: `pytest tests/test_armodel/test_python_class_generator.py::test_generate_simple_concrete_class -v`
Expected: FAIL with "ModuleNotFoundError: No module named 'scripts.python_class_generator'"

### Step 3: Write minimal implementation

Create: `scripts/python_class_generator.py`

```python
import os
from pathlib import Path
from typing import Dict, List, Optional, Any
from templates import CLASS_TEMPLATE, ABSTRACT_CLASS_TEMPLATE

class PythonClassGenerator:
    """Generates Python class files from M2 metadata."""

    def __init__(self, base_path: str, m2_analyzer=None):
        """Initialize generator.

        Args:
            base_path: Base path for generated files (e.g., src/armodel/models/M2/AUTOSARTemplates/)
            m2_analyzer: Optional M2DocumentationAnalyzer for looking up parent classes
        """
        self.base_path = Path(base_path)
        self.m2_analyzer = m2_analyzer

    def generate_class(self, metadata: Dict[str, Any]) -> str:
        """Generate Python class file.

        Args:
            metadata: Class metadata with keys: name, package, type, parent, base_classes, children

        Returns:
            Path to generated file
        """
        # Determine file path from package
        file_path = self._get_file_path(metadata['name'], metadata['package'])

        # Generate class content
        if metadata.get('type') == 'Abstract':
            content = self._generate_abstract_class(metadata)
        else:
            content = self._generate_concrete_class(metadata)

        # Create directory if needed
        file_path.parent.mkdir(parents=True, exist_ok=True)

        # Write file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

        # Update parent __init__.py for wildcard export
        self._update_parent_init(file_path, metadata['name'])

        return str(file_path)

    def _get_file_path(self, class_name: str, m2_package: str) -> Path:
        """Convert M2 package path to Python file path.

        Args:
            class_name: Name of class
            m2_package: M2 package like "M2::AUTOSARTemplates::SwComponentTemplate"

        Returns:
            Path object for the .py file
        """
        # Convert M2::AUTOSARTemplates::SwComponentTemplate -> SwComponentTemplate/
        # For leaf packages, create ClassName.py
        # For non-leaf, create ClassName/__init__.py

        # Remove M2::AUTOSARTemplates:: prefix
        path_parts = m2_package.replace('M2::AUTOSARTemplates::', '').split('::')

        # Build path
        full_path = self.base_path
        for part in path_parts:
            full_path = full_path / part

        # Check if this is a leaf package (no subdirectories with .md files)
        # For now, assume it's a leaf and create .py file
        return full_path / f"{class_name}.py"

    def _generate_abstract_class(self, metadata: Dict[str, Any]) -> str:
        """Generate abstract class content.

        Args:
            metadata: Class metadata

        Returns:
            Python code string
        """
        parent = metadata.get('parent', 'ABC')

        # Build base class list
        bases = ['ABC']
        if parent and parent != 'ABC':
            bases.append(parent)
        bases.extend(metadata.get('base_classes', []))
        bases = list(set(bases))  # Remove duplicates

        class_def = f"class {metadata['name']}({', '.join(bases)}):"

        return f'''\"\"\"{metadata['name']} AUTOSAR M2 model class.

AUTOSAR Package: {metadata['package']}
Type: Abstract
\"\"\"

from abc import ABC, abstractmethod
from typing import Optional

{class_def}
    """{metadata['name']} (abstract)."""

    def __init__(self):
        """Initialize {metadata['name']}.\"\"\"
        super().__init__()
        self._parent = None

    def getParent(self) -> Optional["{metadata['name']}"]:
        \"\"\"Get parent element.

        Returns:
            Parent object or None
        \"\"\"
        return self._parent

    def setParent(self, parent: Optional["{metadata['name']}"]) -> "{metadata['name']}":
        \"\"\"Set parent element.

        Args:
            parent: Parent object

        Returns:
            self for method chaining
        \"\"\"
        self._parent = parent
        return self
'''

    def _generate_concrete_class(self, metadata: Dict[str, Any]) -> str:
        """Generate concrete class content.

        Args:
            metadata: Class metadata

        Returns:
            Python code string
        """
        parent = metadata.get('parent', 'ARObject')

        return f'''\"\"\"{metadata['name']} AUTOSAR M2 model class.

AUTOSAR Package: {metadata['package']}
\"\"\"

from typing import Optional

class {metadata['name']}({parent}):
    """{metadata['name']}."""

    def __init__(self):
        """Initialize {metadata['name']}.\"\"\"
        super().__init__()
        self._parent = None
        self._shortName = None

    def getParent(self) -> Optional["{metadata['name']}"]:
        \"\"\"Get parent element.

        Returns:
            Parent object or None
        \"\"\"
        return self._parent

    def setParent(self, parent: Optional["{metadata['name']}"]) -> "{metadata['name']}":
        \"\"\"Set parent element.

        Args:
            parent: Parent object

        Returns:
            self for method chaining
        \"\"\"
        self._parent = parent
        return self

    def getShortName(self) -> Optional[str]:
        \"\"\"Get short name.

        Returns:
            Short name string
        \"\"\"
        return self._shortName

    def setShortName(self, shortName: str) -> "{metadata['name']}":
        \"\"\"Set short name.

        Args:
            shortName: Short name string

        Returns:
            self for method chaining
        \"\"\"
        self._shortName = shortName
        return self
'''

    def _update_parent_init(self, class_file: Path, class_name: str):
        """Add wildcard export to parent __init__.py.

        Args:
            class_file: Path to generated class file
            class_name: Name of class to export
        """
        parent_init = class_file.parent / '__init__.py'

        # Check if parent __init__.py exists
        if not parent_init.exists():
            # Create it with wildcard export
            with open(parent_init, 'w', encoding='utf-8') as f:
                f.write(f'from .{class_name} import *  # noqa: F401, F403\n')
        else:
            # Read existing content
            with open(parent_init, 'r', encoding='utf-8') as f:
                content = f.read()

            # Check if already exported
            if f'from .{class_name} import' not in content:
                # Add export
                with open(parent_init, 'a', encoding='utf-8') as f:
                    f.write(f'from .{class_name} import *  # noqa: F401, F403\n')
```

### Step 4: Run tests to verify they pass

Run: `pytest tests/test_armodel/test_python_class_generator.py -v`
Expected: All tests PASS

### Step 5: Commit

```bash
git add scripts/python_class_generator.py tests/test_armodel/test_python_class_generator.py
git commit -m "feat: implement PythonClassGenerator for basic class generation"
```

---

## Task 5: Implement Main Orchestration Script

**Files:**
- Create: `scripts/generate_missing_classes.py`

### Step 1: Create main script with CLI interface

Create: `scripts/generate_missing_classes.py`

```python
#!/usr/bin/env python3
"""Generate missing AUTOSAR M2 model classes from deviation report.

Usage:
    python scripts/generate_missing_classes.py [--domain DOMAIN] [--dry-run]
"""

import argparse
import sys
from pathlib import Path

from scripts.deviation_parser import DeviationParser
from scripts.m2_documentation_analyzer import M2DocumentationAnalyzer
from scripts.python_class_generator import PythonClassGenerator


def main():
    parser = argparse.ArgumentParser(
        description='Generate missing AUTOSAR M2 model classes'
    )
    parser.add_argument(
        '--domain',
        help='Only generate classes for specific domain (e.g., CommonStructure)'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Print what would be generated without creating files'
    )
    parser.add_argument(
        '--base-path',
        default='src/armodel/models/M2/AUTOSARTemplates',
        help='Base path for generated classes'
    )

    args = parser.parse_args()

    print('=' * 80)
    print('AUTOSAR M2 Class Generation')
    print('=' * 80)

    # Step 1: Parse deviation report
    print('\n[1/4] Parsing deviation report...')
    deviation_parser = DeviationParser('docs/requirements/deviation_package.md')
    missing_classes = deviation_parser.get_missing_classes()
    print(f'  Found {len(missing_classes)} missing classes')

    # Step 2: Analyze M2 documentation
    print('\n[2/4] Analyzing M2 documentation...')
    m2_analyzer = M2DocumentationAnalyzer(
        'docs/requirements/M2',
        cache_file='docs/requirements/m2_cache.json'
    )
    all_classes = m2_analyzer.get_all_classes()
    print(f'  Indexed {len(all_classes)} classes from M2 docs')

    # Step 3: Filter by domain if specified
    if args.domain:
        print(f'\n[3/4] Filtering by domain: {args.domain}')
        grouped = deviation_parser.get_classes_by_domain()
        classes_to_generate = grouped.get(args.domain, [])
        print(f'  {len(classes_to_generate)} classes to generate')
    else:
        print(f'\n[3/4] All domains selected')
        classes_to_generate = missing_classes

    # Step 4: Generate classes
    print(f'\n[4/4] Generating {len(classes_to_generate)} classes...')
    generator = PythonClassGenerator(
        base_path=args.base_path,
        m2_analyzer=m2_analyzer
    )

    generated = 0
    failed = 0

    for cls in classes_to_generate:
        # Get metadata from M2 docs
        metadata = m2_analyzer.get_class_metadata(cls['name'])

        if metadata is None:
            print(f'  ⚠ WARNING: No metadata found for {cls["name"]}')
            failed += 1
            continue

        # Add name to metadata
        metadata['name'] = cls['name']

        if args.dry_run:
            print(f'  Would generate: {cls["name"]} -> {cls["expected_path"]}')
        else:
            try:
                output_file = generator.generate_class(metadata)
                print(f'  ✓ Generated: {cls["name"]}')
                generated += 1
            except Exception as e:
                print(f'  ✗ Failed: {cls["name"]} - {e}')
                failed += 1

    print('\n' + '=' * 80)
    print(f'Summary: {generated} generated, {failed} failed')
    print('=' * 80)

    return 0 if failed == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
```

### Step 2: Make script executable

```bash
chmod +x scripts/generate_missing_classes.py
```

### Step 3: Test dry-run mode

Run: `python scripts/generate_missing_classes.py --dry-run --domain CommonStructure 2>&1 | head -30`
Expected: See list of classes that would be generated

### Step 4: Commit

```bash
git add scripts/generate_missing_classes.py
git commit -m "feat: add main orchestration script for class generation"
```

---

## Task 6: Implement XSDValidator Class

**Files:**
- Create: `scripts/xsd_validator.py`
- Test: `tests/test_armodel/test_xsd_validator.py`

### Step 1: Write the failing test

Create: `tests/test_armodel/test_xsd_validator.py`

```python
import pytest
from scripts.xsd_validator import XSDValidator

def test_validator_initializes():
    """Test that validator loads XSD schema."""
    validator = XSDValidator('docs/requirements/xsd/AUTOSAR_00046.xsd')
    assert validator.schema is not None

def test_validate_package_path():
    """Test package path validation."""
    validator = XSDValidator('docs/requirements/xsd/AUTOSAR_00046.xsd')

    # Valid path
    result = validator.validate_package_path(
        'M2::AUTOSARTemplates::CommonStructure::InternalBehavior',
        'armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.InternalBehavior'
    )
    assert result['valid'] == True

    # Invalid path (mismatch)
    result = validator.validate_package_path(
        'M2::AUTOSARTemplates::CommonStructure::InternalBehavior',
        'armodel.models.M2.WRONG.InternalBehavior'
    )
    assert result['valid'] == False
```

### Step 2: Run test to verify it fails

Run: `pytest tests/test_armodel/test_xsd_validator.py -v`
Expected: FAIL with "ModuleNotFoundError: No module named 'scripts.xsd_validator'"

### Step 3: Write minimal implementation

Create: `scripts/xsd_validator.py`

```python
from lxml import etree
from typing import Dict, Any, List

class XSDValidator:
    """Validates generated Python classes against XSD schema."""

    def __init__(self, xsd_file: str):
        """Initialize validator with XSD schema file.

        Args:
            xsd_file: Path to XSD schema file
        """
        self.xsd_file = xsd_file
        self.schema = None
        self._load_schema()

    def _load_schema(self):
        """Load XSD schema."""
        with open(self.xsd_file, 'r', encoding='utf-8') as f:
            schema_doc = etree.parse(f)
            self.schema = etree.XMLSchema(schema_doc)

    def validate_package_path(self, m2_path: str, python_path: str) -> Dict[str, Any]:
        """Validate that Python path matches M2 package hierarchy.

        Args:
            m2_path: M2 namespace path
            python_path: Python module path

        Returns:
            Dict with 'valid' boolean and 'message' string
        """
        # Convert M2 path to expected Python path
        expected_parts = m2_path.replace('M2::AUTOSARTemplates::', '').split('::')
        expected_python = 'armodel.models.M2.AUTOSARTemplates.' + '.'.join(expected_parts)

        if python_path == expected_python:
            return {'valid': True, 'message': 'Path matches'}
        else:
            return {
                'valid': False,
                'message': f'Path mismatch: expected {expected_python}, got {python_path}'
            }

    def validate_class(self, class_name: str, class_metadata: Dict[str, Any]) -> Dict[str, Any]:
        """Validate a generated class against XSD.

        Args:
            class_name: Name of the class
            class_metadata: Class metadata from M2 docs

        Returns:
            Dict with validation results
        """
        results = {
            'class_name': class_name,
            'package_valid': True,
            'inheritance_valid': True,
            'warnings': []
        }

        # Validate package path
        path_validation = self.validate_package_path(
            class_metadata['package'],
            f"armodel.models.M2.{class_metadata['package'].replace('M2::', '').replace('::', '.')}"
        )

        if not path_validation['valid']:
            results['package_valid'] = False
            results['warnings'].append(path_validation['message'])

        # TODO: Add more validation (inheritance, properties, etc.)

        return results
```

### Step 4: Run tests to verify they pass

Run: `pytest tests/test_armodel/test_xsd_validator.py -v`
Expected: All tests PASS

### Step 5: Commit

```bash
git add scripts/xsd_validator.py tests/test_armodel/test_xsd_validator.py
git commit -m "feat: implement XSDValidator for schema validation"
```

---

## Task 7: Integrate Validation into Generation Pipeline

**Files:**
- Modify: `scripts/generate_missing_classes.py`

### Step 1: Add validation to main script

Edit: `scripts/generate_missing_classes.py`

```python
# Add import at top
from scripts.xsd_validator import XSDValidator

# Add validation after generation
def main():
    # ... existing code ...

    # Step 5: Validate generated classes
    if not args.dry_run and generated > 0:
        print(f'\n[5/5] Validating generated classes...')
        validator = XSDValidator('docs/requirements/xsd/AUTOSAR_00046.xsd')

        validation_results = []
        for cls in classes_to_generate[:generated]:  # Validate only successfully generated
            metadata = m2_analyzer.get_class_metadata(cls['name'])
            if metadata:
                result = validator.validate_class(cls['name'], metadata)
                validation_results.append(result)

        # Print validation summary
        valid_count = sum(1 for r in validation_results if r['package_valid'])
        print(f'  Validation: {valid_count}/{len(validation_results)} passed')

        if any(not r['package_valid'] for r in validation_results):
            print('\n  Warnings:')
            for r in validation_results:
                if not r['package_valid']:
                    print(f'    - {r["class_name"]}: {r["warnings"]}')
```

### Step 2: Test validation integration

Run: `python scripts/generate_missing_classes.py --domain CommonStructure --dry-run`
Expected: See validation step in output

### Step 3: Commit

```bash
git add scripts/generate_missing_classes.py
git commit -m "feat: integrate XSD validation into generation pipeline"
```

---

## Task 8: End-to-End Test with Pilot Generation

**Files:**
- Create: `tests/integration/test_class_generation_workflow.py`

### Step 1: Write integration test

Create: `tests/integration/test_class_generation_workflow.py`

```python
import pytest
import tempfile
import shutil
from pathlib import Path
from scripts.generate_missing_classes import main as generate_main
import sys
import os

def test_generate_single_domain_integration():
    """Integration test: Generate a small domain end-to-end."""
    # Use temporary directory
    with tempfile.TemporaryDirectory() as tmpdir:
        # Save original directory
        original_cwd = os.getcwd()

        try:
            # Change to temp directory
            os.chdir(tmpdir)

            # Create minimal project structure
            Path('src/armodel/models/M2/AUTOSARTemplates').mkdir(parents=True)

            # Run generation for a small domain (dry-run first)
            sys.argv = [
                'generate_missing_classes.py',
                '--dry-run',
                '--domain', 'CommonStructure',
                '--base-path', f'{tmpdir}/src/armodel/models/M2/AUTOSARTemplates'
            ]

            result = generate_main()

            # Should complete without error
            assert result == 0

        finally:
            os.chdir(original_cwd)
```

### Step 2: Run integration test

Run: `pytest tests/integration/test_class_generation_workflow.py -v`
Expected: PASS

### Step 3: Commit

```bash
git add tests/integration/test_class_generation_workflow.py
git commit -m "test: add integration test for class generation workflow"
```

---

## Task 9: Generate Documentation

**Files:**
- Create: `docs/development/class_generation_tooling.md`

### Step 1: Write documentation

Create: `docs/development/class_generation_tooling.md`

```markdown
# AUTOSAR M2 Class Generation Tooling

## Overview

The class generation system automates creation of AUTOSAR M2 model classes from M2 documentation with XSD validation.

## Usage

### Generate All Missing Classes

```bash
python scripts/generate_missing_classes.py
```

### Generate Specific Domain

```bash
python scripts/generate_missing_classes.py --domain CommonStructure
```

### Dry Run (Preview)

```bash
python scripts/generate_missing_classes.py --dry-run --domain BswModuleTemplate
```

## Architecture

- **DeviationParser**: Extracts missing classes from deviation report
- **M2DocumentationAnalyzer**: Indexes M2 markdown documentation
- **PythonClassGenerator**: Generates Python class files
- **XSDValidator**: Validates against XSD schema

## Development

### Running Tests

```bash
pytest tests/test_armodel/test_deviation_parser.py
pytest tests/test_armodel/test_m2_documentation_analyzer.py
pytest tests/test_armodel/test_python_class_generator.py
pytest tests/test_armodel/test_xsd_validator.py
pytest tests/integration/test_class_generation_workflow.py
```

### Adding New Features

1. Update relevant parser/generator class
2. Add unit tests
3. Update integration test
4. Update this documentation
```

### Step 2: Commit documentation

```bash
git add docs/development/class_generation_tooling.md
git commit -m "docs: add class generation tooling documentation"
```

---

## Task 10: Final Quality Gates

### Step 1: Run full test suite

Run: `python scripts/run_tests.py --unit`
Expected: All tests PASS including new tests

### Step 2: Run linting

Run: `npm run flake8`
Expected: No syntax errors

### Step 3: Test dry-run on real data

Run: `python scripts/generate_missing_classes.py --dry-run --domain CommonStructure`
Expected: See list of ~150 classes to generate

### Step 4: Verify git status

Run: `git status`
Expected: All changes committed

### Step 5: Push to remote

```bash
git push -u origin feature/autosar-m2-class-generation
```

---

## Next Steps After This Plan

Once all tasks in this plan are complete:

1. **Create Pull Request** with description of tooling
2. **Pilot Implementation**: Generate one small domain (e.g., GenericStructure ~50 classes)
3. **Validate**: Run quality gates, fix any issues
4. **Review**: Get feedback on generated code quality
5. **Iterate**: Improve generator based on pilot results
6. **Rollout**: Generate remaining domains incrementally

---

**End of Implementation Plan**

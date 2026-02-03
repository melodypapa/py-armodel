# Python Code Rules

This document defines the coding standards and conventions for the `autosar-pdf2txt` project, combining project-specific requirements with [PEP 8 - Style Guide for Python Code](https://peps.python.org/pep-0008/). All contributors must follow these rules to maintain code consistency and quality.

## Maturity Levels

Each coding rule has a maturity level that indicates its status:

- **draft**: Newly created rule, under review, or not yet enforced
- **accept**: Accepted rule, currently enforced in the codebase
- **invalid**: Deprecated rule, superseded by new standards, or no longer applicable

All existing rules in this document are currently at maturity level **accept**.

## Table of Contents

1. [Code Layout](#code-layout)
2. [Import Organization](#import-organization)
3. [Naming Conventions](#naming-conventions)
4. [Type Hints](#type-hints)
5. [Docstrings](#docstrings)
6. [Whitespace in Expressions](#whitespace-in-expressions)
7. [Code Style](#code-style)
   - Dataclass Usage
   - Validation in `__post_init__`
   - Regular Expressions
   - Context Managers
   - String Methods
   - List Comprehensions
   - Dunder Methods
   - Python Package Structure
8. [Error Handling](#error-handling)
9. [Testing Standards](#testing-standards)
10. [Logging Standards](#logging-standards)
11. [Programming Recommendations](#programming-recommendations)

---

## Code Layout

### CODING_RULE_LAYOUT_00001: Indentation

**Maturity**: accept

**Use 4 spaces per indentation level** (PEP 8). Never use tabs.

```python
# Correct
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)

# Correct - hanging indent
foo = long_function_name(
    var_one, var_two,
    var_three, var_four)
```

### CODING_RULE_LAYOUT_00002: Maximum Line Length

**Maturity**: accept

**Limit all lines to a maximum of 79 characters** (PEP 8 standard).

For docstrings and comments, limit to **72 characters**.

```python
# Correct
def function_with_long_name(
    parameter_one: str,
    parameter_two: int,
) -> bool:
    """This is a docstring that is wrapped at 72 characters
    to maintain readability.
    """
    return parameter_one == str(parameter_two)

# Wrong - line too long
def function_with_long_name(parameter_one: str, parameter_two: int) -> bool:
    return parameter_one == str(parameter_two)
```

### CODING_RULE_LAYOUT_00003: Line Breaking

**Maturity**: accept

**Break long lines using Python's implicit line continuation** inside parentheses, brackets, and braces (PEP 8).

```python
# Correct - implicit continuation
result = (some_function(arg1, arg2)
          + another_function(arg3, arg4))

# Wrong - backslash continuation (use only when necessary)
income = (gross_wages + taxable_interest +
          (dividends - qualified_dividends) -
          ira_deduction)
```

### CODING_RULE_LAYOUT_00004: Binary Operator Placement

**Maturity**: accept

**Break before binary operators** for better readability (PEP 8 - Knuth's style):

```python
# Correct
income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_loan_interest)

# Wrong
income = (gross_wages +
          taxable_interest +
          (dividends - qualified_dividends) -
          ira_deduction -
          student_loan_interest)
```

### CODING_RULE_LAYOUT_00005: Blank Lines

**Maturity**: accept

**Separate top-level function and class definitions with two blank lines** (PEP 8).

**Method definitions inside a class are surrounded by a single blank line** (PEP 8).

```python
# Correct
class MyClass:
    """Example class."""

    def method_one(self):
        """First method."""
        pass

    def method_two(self):
        """Second method."""
        pass


def function_one():
    """Top-level function."""
    pass


def function_two():
    """Another top-level function."""
    pass
```

### CODING_RULE_LAYOUT_00006: Source File Encoding

**Maturity**: accept

**Code should always use UTF-8 encoding** (PEP 8). No encoding declaration needed.

### CODING_RULE_LAYOUT_00007: String Quotes

**Maturity**: accept

**Use double quotes for strings** (project convention). Single quotes only when string contains double quotes.

**For triple-quoted strings (docstrings), always use double quotes** (PEP 8).

```python
# Correct
message = "Hello, World!"
quote = "He said, \"Hello\""
docstring = """This is a docstring."""

# Wrong
message = 'Hello, World!'
docstring = '''This is a docstring.'''
```

---

## Import Organization

### CODING_RULE_IMPORT_00001: Import Order

**Maturity**: accept

**Imports must be organized into three distinct sections with blank lines between:**

1. **Standard library imports** - Python built-in modules
2. **Third-party imports** - External packages
3. **Local imports** - Project modules (absolute import paths)

**Example:**
```python
# 1. Standard library imports
import argparse
import logging
import sys
from dataclasses import dataclass, field
from io import StringIO
from pathlib import Path
from typing import List, Optional, Set, Tuple

# 2. Third-party imports
import pdfplumber

# 3. Local imports (absolute paths)
from autosar_pdf2txt.models import AutosarClass, AutosarPackage
from autosar_pdf2txt.parser import PdfParser
from autosar_pdf2txt.writer import MarkdownWriter
```

### CODING_RULE_IMPORT_00002: Import Section Separation

**Maturity**: accept

**Each section separated by exactly one blank line.**

### CODING_RULE_IMPORT_00003: Import Alphabetical Order

**Maturity**: accept

**Within each section, imports sorted alphabetically.**

---

## Naming Conventions

### CODING_RULE_NAMING_00001: Class Names

**Maturity**: accept

**Style:** `PascalCase`

```python
class AutosarClass:
    """Represents an AUTOSAR class."""

class PdfParser:
    """Parse AUTOSAR PDF files."""

class TestAutosarClass:
    """Tests for AutosarClass class."""
```

### CODING_RULE_NAMING_00002: Function and Method Names

**Maturity**: accept

**Style:** `snake_case`

```python
def parse_pdf(pdf_path: str) -> List[AutosarPackage]:
    """Parse a PDF file."""

def add_class(cls: AutosarClass) -> None:
    """Add a class to the package."""

def test_init_concrete_class() -> None:
    """Test creating a concrete class."""
```

### CODING_RULE_NAMING_00003: Constant Names

**Maturity**: accept

**Style:** `UPPER_CASE`

```python
CLASS_PATTERN = re.compile(r"^Class\s+(.+?)(?:\s*\((abstract)\))?\s*$")
PACKAGE_PATTERN = re.compile(r"^Package\s+(M2::)?(.+)$")
BASE_PATTERN = re.compile(r"^Base\s+(.+)$")
```

### CODING_RULE_NAMING_00004: Private Attribute Names

**Maturity**: accept

**Style:** `_leading_underscore`

```python
def _validate_backend(self) -> None:
    """Validate that pdfplumber backend is available."""

def _extract_class_definitions(self, pdf_path: str) -> List[ClassDefinition]:
    """Extract all class definitions from the PDF."""
```

### CODING_RULE_NAMING_00005: Instance Variable Names

**Maturity**: accept

**Style:** `snake_case`

```python
def __init__(self) -> None:
    self.parent_package: Optional[AutosarPackage] = None
    self.current_path: str = ""
```

---

## Type Hints

### CODING_RULE_TYPE_00001: Mandatory Type Annotations

**Maturity**: accept

**All** function parameters and return values must have type hints.

**Example:**
```python
def get_class(self, name: str) -> AutosarClass | None:
    """Get a class by name."""
    for cls in self.classes:
        if cls.name == name:
            return cls
    return None

def add_subpackage(self, pkg: "AutosarPackage") -> None:
    """Add a subpackage to this package."""
    pkg_names = {p.name for p in self.subpackages}
    if pkg.name in pkg_names:
        raise ValueError(f"Subpackage '{pkg.name}' already exists")
    self.subpackages.append(pkg)
```

### CODING_RULE_TYPE_00002: Union Types

**Maturity**: accept

**Use Python 3.10+ syntax** with `|` for union types:

```python
# Preferred (Python 3.10+):
def get_class(self, name: str) -> AutosarClass | None:
    """Get a class by name."""

# Not preferred (old style):
# from typing import Optional
# def get_class(self, name: str) -> Optional[AutosarClass]:
```

### CODING_RULE_TYPE_00003: Collection Types

**Maturity**: accept

**Use imported generics** from `typing` module:

```python
from typing import List, Set, Tuple, Dict

def parse_pdf(self, pdf_path: str) -> List[AutosarPackage]:
    """Parse a PDF file."""

def process_names(self, names: Set[str]) -> Tuple[str, int]:
    """Process unique names."""

def build_map(self) -> Dict[str, AutosarPackage]:
    """Build a package map."""
```

### CODING_RULE_TYPE_00004: Forward References

**Maturity**: accept

**Use string literals** for circular dependencies:

```python
@dataclass
class AutosarPackage:
    name: str
    subpackages: List["AutosarPackage"] = field(default_factory=list)

def get_subpackage(self, name: str) -> "AutosarPackage | None":
    """Get a subpackage by name."""
```

### CODING_RULE_TYPE_00005: Dataclass Field Types

**Maturity**: accept

**Use `field(default_factory=list)`** for mutable defaults:

```python
from dataclasses import dataclass, field

@dataclass
class AutosarPackage:
    name: str
    classes: List[AutosarClass] = field(default_factory=list)
    subpackages: List["AutosarPackage"] = field(default_factory=list)
```

---

## Docstrings

### CODING_RULE_DOC_00001: Google-Style Docstrings

**Maturity**: accept

**All public classes, methods, and functions must have Google-style docstrings.**

### CODING_RULE_DOC_00002: Class Docstrings

**Maturity**: accept

**Class docstrings must include:** Description, Requirements, Attributes, Examples

```python
@dataclass
class AutosarClass:
    """Represents an AUTOSAR class.

    Requirements:
        SWR_MODEL_00001: AUTOSAR Class Representation

    Attributes:
        name: The name of the class.
        is_abstract: Whether the class is abstract.

    Examples:
        >>> cls = AutosarClass("RunnableEntity", False)
        >>> abstract_cls = AutosarClass("InternalBehavior", True)
    """
```

### CODING_RULE_DOC_00003: Method Docstrings

**Maturity**: accept

**Method docstrings must include:** Description, Requirements, Args, Returns, Raises

```python
def add_class(self, cls: AutosarClass) -> None:
    """Add a class to the package.

    Requirements:
        SWR_MODEL_00006: Add Class to Package

    Args:
        cls: The AutosarClass to add.

    Raises:
        ValueError: If a class with the same name already exists.
    """
```

### CODING_RULE_DOC_00004: Requirements Section

**Maturity**: accept

**Every public method** must include a "Requirements:" section with relevant requirement IDs:

```python
def parse_pdf(self, pdf_path: str) -> List[AutosarPackage]:
    """Parse a PDF file and extract the package hierarchy.

    Requirements:
        SWR_PARSER_00003: PDF File Parsing

    Args:
        pdf_path: Path to the PDF file.

    Returns:
        List of top-level AutosarPackage objects.

    Raises:
        FileNotFoundError: If the PDF file doesn't exist.
        Exception: If PDF parsing fails.
    """
```

### CODING_RULE_DOC_00005: Docstring Language

**Maturity**: accept

**All docstrings must be in English.**

```python
def __post_init__(self) -> None:
    """Validate the class fields.

    Requirements:
        SWR_MODEL_00002: AUTOSAR Class Name Validation

    Raises:
        ValueError: If name is empty or contains only whitespace.
    """
```

---

## Whitespace in Expressions

### CODING_RULE_WS_00001: Avoid Extraneous Whitespace

**Maturity**: accept

**Avoid extraneous whitespace in the following situations** (PEP 8):

**Immediately inside parentheses, brackets, or braces:**

```python
# Correct
spam(ham[1], {eggs: 2})

# Wrong
spam( ham[ 1 ], { eggs: 2 } )
```

**Between a trailing comma and following close parenthesis:**

```python
# Correct
foo = (0,)

# Wrong
foo = (0, )
```

**Immediately before a comma, semicolon, or colon:**

```python
# Correct
if x == 4: print(x, y); x, y = y, x

# Wrong
if x == 4 : print(x , y) ; x , y = y , x
```

**Immediately before the open parenthesis that starts the argument list of a function call:**

```python
# Correct
spam(1)

# Wrong
spam (1)
```

**Immediately before the open parenthesis that starts an indexing or slicing:**

```python
# Correct
dct['key'] = lst[index]

# Wrong
dct ['key'] = lst [index]
```

### CODING_RULE_WS_00002: Whitespace Around Operators

**Maturity**: accept

**Always surround these binary operators with a single space on either side** (PEP 8):

- Assignment (`=`)
- Augmented assignment (`+=`, `-=`)
- Comparisons (`==`, `<`, `>`, `!=`, `<=`, `>=`, `in`, `not in`, `is`, `is not`)
- Booleans (`and`, `or`, `not`)

```python
# Correct
i = i + 1
submitted += 1
x = x * 2 - 1
hypot2 = x * x + y * y
c = (a + b) * (a - b)

# Wrong
i=i+1
submitted +=1
x = x * 2 - 1
hypot2 = x * x + y * y
c = (a + b) * (a - b)
```

### CODING_RULE_WS_00003: Keyword Arguments

**Maturity**: accept

**Don't use spaces around the `=` sign when used to indicate a keyword argument** (PEP 8):

```python
# Correct
def complex(real, imag=0.0):
    return magic(r=real, i=imag)

# Wrong
def complex(real, imag = 0.0):
    return magic(r = real, i = imag)
```

**When combining with type annotation, do use spaces around the `=` sign:**

```python
# Correct
def munge(sep: AnyStr = None):
    pass

# Wrong
def munge(input: AnyStr=None):
    pass
```

### CODING_RULE_WS_00004: Function Annotations

**Maturity**: accept

**Function annotations should use spaces around the `->` arrow** (PEP 8):

```python
# Correct
def munge(input: AnyStr) -> AnyStr:
    pass

def munge() -> PosInt:
    pass

# Wrong
def munge(input:AnyStr):
    pass

def munge()->PosInt:
    pass
```

### CODING_RULE_WS_00005: Trailing Whitespace

**Maturity**: accept

**Avoid trailing whitespace anywhere** (PEP 8):

```python
# Wrong
x = 1     # trailing whitespace here
```

### CODING_RULE_WS_00006: Compound Statements

**Maturity**: accept

**Avoid compound statements (multiple statements on the same line)** (PEP 8):

```python
# Correct
if foo == 'blah':
    do_blah_thing()
do_one()
do_two()

# Wrong
if foo == 'blah': do_blah_thing()
do_one(); do_two(); do_three()
```

---

## Code Style

### CODING_RULE_STYLE_00001: Dataclass Usage

**Maturity**: accept

**Use `@dataclass` decorator for model classes:**

```python
from dataclasses import dataclass, field

@dataclass
class AutosarClass:
    """Represents an AUTOSAR class."""
    name: str
    is_abstract: bool
```

### CODING_RULE_STYLE_00002: Validation in `__post_init__`

**Maturity**: accept

**Validate dataclass fields immediately after initialization:**

```python
def __post_init__(self) -> None:
    """Validate the class fields."""
    if not self.name or not self.name.strip():
        raise ValueError("Class name cannot be empty")
```

### CODING_RULE_STYLE_00003: Regular Expressions

**Maturity**: accept

**Compile regex patterns as class constants:**

```python
class PdfParser:
    """Parse AUTOSAR PDF files."""

    CLASS_PATTERN = re.compile(r"^Class\s+(.+?)(?:\s*\((abstract)\))?\s*$")
    PACKAGE_PATTERN = re.compile(r"^Package\s+(M2::)?(.+)$")
```

### CODING_RULE_STYLE_00004: Context Managers

**Maturity**: accept

**Use context managers for resource management:**

```python
# File operations
with pdfplumber.open(pdf_path) as pdf:
    text = page.extract_text()

# String buffers
text_buffer = StringIO()
text_buffer.write(text + "\n")
full_text = text_buffer.getvalue()
```

### CODING_RULE_STYLE_00005: String Methods

**Maturity**: accept

**Prefer `str.strip()` and explicit checks:**

```python
# Good
if not self.name or not self.name.strip():
    raise ValueError("Class name cannot be empty")

# Good
line = line.strip()
if not line:
    continue

# Good
class_names = {c.name for c in self.classes}
if cls.name in class_names:
    raise ValueError(f"Class '{cls.name}' already exists")
```

### CODING_RULE_STYLE_00006: List Comprehensions

**Maturity**: accept

**Use list comprehensions for transformations:**

```python
# Parse package path
package_parts = [p.strip() for p in class_def.package_path.split("::")]

# Split and filter
base_classes = [
    bc.strip() for bc in base_classes_str.split(",") if bc.strip()
]
```

### CODING_RULE_STYLE_00007: Dunder Methods

**Maturity**: accept

**Implement `__str__` and `__repr__` for dataclasses:**

```python
def __str__(self) -> str:
    """Return string representation of the class."""
    suffix = " (abstract)" if self.is_abstract else ""
    return f"{self.name}{suffix}"

def __repr__(self) -> str:
    """Return detailed representation for debugging."""
    return f"AutosarClass(name='{self.name}', is_abstract={self.is_abstract})"
```

### CODING_RULE_STYLE_00008: Python Package Structure

**Maturity**: accept

**Follow the py-armodel package structure conventions to align AUTOSAR M2 model hierarchy with Python package structure.**

**Leaf Packages (no subdirectories):**
- Classes defined in a single `.py` file
- Package name = filename (without `.py` extension)
- File name typically matches the primary class name or package concept
- Import path includes the filename as the package name

```python
# File: src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ImplementationDataTypes.py
# This is a leaf package (no subdirectories)

from abc import ABCMeta
from typing import List

class AbstractImplementationDataTypeElement(Identifiable):
    """Base class for implementation data type elements."""
    pass

class ImplementationDataTypeElement(AbstractImplementationDataTypeElement):
    """Implementation data type element class."""
    pass

class ImplementationDataType(AbstractImplementationDataType):
    """Implementation data type class."""
    pass

# Import statement:
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes import ImplementationDataType
# Module path: armodel.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes
```

**Non-Leaf Packages (have subdirectories):**
- Classes defined in `__init__.py` of the directory
- Package name = directory name
- May contain multiple subdirectories with their own classes

```python
# File: src/armodel/models/M2/AUTOSARTemplates/CommonStructure/__init__.py
# This is a non-leaf package (has subdirectories like InternalBehavior/, Implementation.py, etc.)

from abc import ABCMeta
from typing import List

class ValueSpecification(ARObject, metaclass=ABCMeta):
    """Value specification base class."""
    pass

class ConstantSpecification(ARElement):
    """Constant specification class."""
    pass

# Import statement:
from armodel.models.M2.AUTOSARTemplates.CommonStructure import ValueSpecification
# Module path: armodel.models.M2.AUTOSARTemplates.CommonStructure
```

**Directory Structure Examples:**

```
src/armodel/models/M2/AUTOSARTemplates/
├── CommonStructure/                      # Non-leaf package (has subdirs)
│   ├── __init__.py                       # Classes defined here
│   ├── InternalBehavior.py               # Leaf package
│   ├── ImplementationDataTypes.py        # Leaf package (primary class)
│   └── Filter.py                         # Leaf package
├── SWComponentTemplate/                  # Non-leaf package
│   ├── __init__.py                       # Classes defined here
│   ├── Components/                       # Non-leaf sub-package
│   │   ├── __init__.py
│   │   └── ...
│   └── Datatypes/                        # Non-leaf sub-package
│       ├── __init__.py
│       └── ...
└── AutosarTopLevelStructure/            # Non-leaf package
    └── __init__.py                       # Classes defined here
```

**Package Structure Decision Tree:**

```
Does the package contain subdirectories?
│
├── YES → Non-Leaf Package
│   - Create directory with __init__.py
│   - Define classes in __init__.py
│   - Package name = directory name
│
└── NO  → Leaf Package
    - Create single .py file
    - Define all classes in that .py file
    - Package name = filename (without .py)
    - File name typically matches primary class or package concept
```

**Alignment with AUTOSAR M2 Model:**

The package structure conventions ensure alignment between the AUTOSAR M2 model hierarchy and Python package structure:

```
AUTOSAR M2 Path:                          Python Path:
M2::AUTOSARTemplates::CommonStructure::    armodel.models.M2.AUTOSARTemplates.CommonStructure
  ImplementationDataTypes::                  .ImplementationDataTypes
    ImplementationDataType                   .ImplementationDataType

File Structure:
AUTOSARTemplates/CommonStructure/ImplementationDataTypes.py
  (contains ImplementationDataType class)
```

### CODING_RULE_STYLE_00009: Class Organization per AUTOSAR Mapping

**Maturity**: accept

**Classes MUST be importable from the module path specified in `docs/requirements/mapping.json`.**

The AUTOSAR mapping specification (derived from AUTOSAR standard) defines the exact package path where each class should be located. Classes MUST be importable from their mapped module path.

**Definition Location:**
- Classes should be defined in the module file corresponding to their mapped package path
- If a class is mapped to `M2::AUTOSARTemplates::Package::SubPackage`, it MUST be importable from `armodel.models.M2.AUTOSARTemplates.Package.SubPackage`

**Import Path Verification:**
```python
# Given mapping entry:
# {
#   "name": "HwAttributeValue",
#   "type": "Class",
#   "package_path": "M2::AUTOSARTemplates::EcuResourceTemplate::HwElementCategory"
# }

# CORRECT - Import from mapped location:
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwElementCategory import HwAttributeValue

# WRONG - Import from non-mapped location:
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwAttributeValue import HwAttributeValue  # DO NOT USE
```

**Implementation Guidelines:**
1. Define the class in the correct module file based on the mapping
2. Do NOT create redundant files named after classes if they don't match the package structure
3. Use forward references or `TYPE_CHECKING` to avoid circular imports when necessary
4. Run `test_class_mapping.py` integration test to verify compliance

**Example - Correct Implementation:**
```python
# File: src/armodel/models/M2/AUTOSARTemplates/EcuResourceTemplate/HwElementCategory.py
# This module contains classes defined in the HwElementCategory package per AUTOSAR mapping

from typing import Optional
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class HwAttributeValue(ARObject):
    """Hardware attribute value class - defined here per mapping.json specification."""
    def __init__(self):
        super().__init__()
        self.hwAttributeDefRef: Optional[RefType] = None
        self.value: Optional[str] = None
    # ... methods
```

**Example - Incorrect Implementation:**
```python
# WRONG - Do NOT create separate file just for the class name
# File: src/armodel/models/M2/AUTOSARTemplates/EcuResourceTemplate/HwAttributeValue.py
class HwAttributeValue(ARObject):
    pass  # This violates the mapping specification

# Import will fail:
# from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwElementCategory import HwAttributeValue
# ImportError: cannot import name 'HwAttributeValue' from 'HwElementCategory'
```

**Related Rules:**
- CODING_RULE_STYLE_00008: Python Package Structure
- CODING_RULE_TYPE_00004: Forward References

**Verification:**
Run the class mapping integration test to verify all classes are at their correct locations:
```bash
pytest tests/integration_tests/test_class_mapping.py::TestClassMapping::test_all_types_combined -v
```

---

## Error Handling

### CODING_RULE_ERROR_00001: Validation Errors

**Maturity**: accept

**Use `ValueError` for invalid arguments:**

```python
def add_class(self, cls: AutosarClass) -> None:
    """Add a class to the package."""
    class_names = {c.name for c in self.classes}
    if cls.name in class_names:
        raise ValueError(f"Class '{cls.name}' already exists in package '{self.name}'")
    self.classes.append(cls)
```

### CODING_RULE_ERROR_00002: Immediate Validation

**Maturity**: accept

**Validate inputs immediately and raise errors:**

```python
def __post_init__(self) -> None:
    """Validate the package fields."""
    if not self.name or not self.name.strip():
        raise ValueError("Package name cannot be empty")
```

### CODING_RULE_ERROR_00003: Exception Chaining

**Maturity**: accept

**Use `raise ... from e` to preserve exception context:**

```python
try:
    with pdfplumber.open(pdf_path) as pdf:
        text = page.extract_text()
except Exception as e:
    raise Exception(f"Failed to parse PDF with pdfplumber: {e}") from e
```

### CODING_RULE_ERROR_00004: Import Validation

**Maturity**: accept

**Validate required dependencies in `__init__`:**

```python
def _validate_backend(self) -> None:
    """Validate that pdfplumber backend is available."""
    try:
        import pdfplumber as _  # noqa: F401
    except ImportError:
        raise ImportError(
            "pdfplumber is not installed. Install it with: pip install pdfplumber"
        )
```

---

## Testing Standards

### CODING_RULE_TEST_00001: Test Structure

**Maturity**: accept

**Test structure requirements:**
- Mirror source structure in `tests/` directory
- Test classes named `Test<ClassName>` for models
- Test methods named `test_<method_name>_<scenario>` or `test_<scenario>`
- All test docstrings in English

**Example:**
```python
class TestAutosarClass:
    """Tests for AutosarClass class."""

    def test_init_concrete_class(self) -> None:
        """Test creating a concrete class."""
        cls = AutosarClass(name="RunnableEntity", is_abstract=False)
        assert cls.name == "RunnableEntity"
        assert cls.is_abstract is False

    def test_post_init_empty_name(self) -> None:
        """Test empty name raises ValueError."""
        with pytest.raises(ValueError, match="Class name cannot be empty"):
            AutosarClass(name="", is_abstract=False)
```

### CODING_RULE_TEST_00002: Test Coverage Goals

**Maturity**: accept

**Coverage requirements:**
- Target 100% coverage for all modules
- Test success paths, error paths, and edge cases
- Test nested structures and complex scenarios

### CODING_RULE_TEST_00003: Test Patterns

**Maturity**: accept

**Exception Testing:**
```python
def test_add_class_duplicate(self) -> None:
    """Test adding duplicate class raises ValueError."""
    pkg = AutosarPackage(name="TestPackage")
    cls1 = AutosarClass(name="DuplicateClass", is_abstract=False)
    cls2 = AutosarClass(name="DuplicateClass", is_abstract=True)
    pkg.add_class(cls1)
    with pytest.raises(ValueError, match="already exists"):
        pkg.add_class(cls2)
```

**Mocking:**
```python
from unittest.mock import MagicMock, patch

@patch("sys.argv", ["autosar-extract", "nonexistent.pdf"])
@patch("autosar_pdf2txt.cli.autosar_cli.Path")
def test_non_existent_path_error(self, mock_path: MagicMock) -> None:
    """Test non-existent path error handling."""
    # Test implementation
```

---

## Logging Standards

### CODING_RULE_LOG_00001: Logging Levels

**Maturity**: accept

**INFO level** - Standard progress messages (default)
  - PDF files being parsed
  - Number of packages found
  - Output file location

**DEBUG level** - Detailed debug information (with `-v` flag)
  - Full file paths
  - Package names
  - Detailed operation trace

**WARNING level** - Non-critical issues
  - Skipping non-PDF files
  - Empty directories

**ERROR level** - Critical failures

**Example:**
```python
# Standard progress
logging.info(f"Parsing PDF: {pdf_path}")
logging.info(f"Found {len(packages)} top-level packages")

# Debug information
logging.debug(f"  Full path: {pdf_path.absolute()}")
logging.debug(f"    - {pkg.name}")

# Warnings
logging.warning(f"Skipping non-PDF file: {input_path}")

# Errors
logging.error(f"Path not found: {input_path}")
logging.error(f"{e}")
```

### CODING_RULE_LOG_00002: Logging Configuration

**Maturity**: accept

**Configure logging based on verbose flag:**

```python
log_level = logging.DEBUG if args.verbose else logging.INFO
logging.basicConfig(
    level=log_level,
    format="%(levelname)s: %(message)s",
)
```

### CODING_RULE_LOG_00003: CLI Error Handling

**Maturity**: accept

**Return exit codes (0 for success, 1 for error):**

```python
def main() -> int:
    """Main entry point for the CLI.

    Returns:
        Exit code (0 for success, 1 for error).
    """
    try:
        # Parse and process
        return 0
    except Exception as e:
        logging.error(f"{e}")
        if args.verbose:
            logging.exception("Detailed error traceback:")
        return 1
```

---

## Additional Best Practices

### CODING_RULE_BP_00001: Query Methods

**Maturity**: accept

**Provide boolean query methods for existence checks:**

```python
def has_class(self, name: str) -> bool:
    """Check if a class exists in the package."""
    return any(cls.name == name for cls in self.classes)

def has_subpackage(self, name: str) -> bool:
    """Check if a subpackage exists in the package."""
    return any(pkg.name == name for pkg in self.subpackages)
```

### CODING_RULE_BP_00002: Path Operations

**Maturity**: accept

**Use `pathlib.Path` for file system operations:**

```python
from pathlib import Path

path = Path(input_path)
if not path.exists():
    logging.error(f"Path not found: {input_path}")
    return 1

if path.is_file():
    pdf_paths.append(path)
elif path.is_dir():
    pdf_files_in_dir = sorted(path.glob("*.pdf"))
```

---

## Programming Recommendations

### CODING_RULE_PR_00001: Type Comparisons

**Maturity**: accept

**Object type comparisons should always use `isinstance()`** (PEP 8):

```python
# Correct
if isinstance(obj, int):
    pass

# Wrong
if type(obj) is type(1):
    pass
```

### CODING_RULE_PR_00002: Sequence Checks

**Maturity**: accept

**For sequences (strings, lists, tuples), use the fact that empty sequences are false** (PEP 8):

```python
# Correct
if not seq:
    pass

if seq:
    pass

# Wrong
if len(seq):
    pass

if not len(seq):
    pass
```

### CODING_RULE_PR_00003: String Prefix/Suffix Checks

**Maturity**: accept

**Use `''.startswith()` and `''.endswith()` instead of string slicing** (PEP 8):

```python
# Correct
if foo.startswith('bar'):
    pass

# Wrong
if foo[:3] == 'bar':
    pass
```

### CODING_RULE_PR_00004: None Comparisons

**Maturity**: accept

**Comparisons to `None` should always be done with `is` or `is not`** (PEP 8):

```python
# Correct
if foo is None:
    pass

if foo is not None:
    pass

# Wrong
if foo == None:
    pass

if not foo is None:
    pass
```

### CODING_RULE_PR_00005: Boolean Comparisons

**Maturity**: accept

**Don't compare boolean values to `True` or `False` using `==`** (PEP 8):

```python
# Correct
if greeting:
    pass

if not greeting:
    pass

# Wrong
if greeting == True:
    pass

if greeting is True:
    pass
```

### CODING_RULE_PR_00006: Exception Handling

**Maturity**: accept

**When catching exceptions, mention specific exceptions** instead of using bare `except:` (PEP 8):

```python
# Correct
try:
    import platform_specific_module
except ImportError:
    platform_specific_module = None

# Wrong
try:
    import platform_specific_module
except:
    platform_specific_module = None
```

**Limit the `try` clause to the absolute minimum amount of code:**

```python
# Correct
try:
    value = collection[key]
except KeyError:
    return key_not_found(key)
else:
    return handle_value(value)

# Wrong - too broad
try:
    return handle_value(collection[key])
except KeyError:
    return key_not_found(key)
```

### CODING_RULE_PR_00007: Resource Management

**Maturity**: accept

**Use `with` statements for resource management** (PEP 8):

```python
# Correct
with open('/path/to/file') as f:
    data = f.read()

# Wrong
f = open('/path/to/file')
data = f.read()
f.close()
```

### CODING_RULE_PR_00008: Return Statement Consistency

**Maturity**: accept

**Be consistent in return statements** (PEP 8). Either all return statements return an expression, or none:

```python
# Correct
def foo(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return None

# Correct
def bar(x):
    if x < 0:
        return None
    return math.sqrt(x)

# Wrong
def foo(x):
    if x >= 0:
        return math.sqrt(x)

# Wrong
def bar(x):
    if x < 0:
        return
    return math.sqrt(x)
```

### CODING_RULE_PR_00009: Use `def` Instead of Lambda Assignment

**Maturity**: accept

**Always use a `def` statement instead of an assignment statement that binds a lambda expression** (PEP 8):

```python
# Correct
def f(x):
    return 2 * x

# Wrong
f = lambda x: 2 * x
```

### CODING_RULE_PR_00010: Exception Classes

**Maturity**: accept

**Derive exceptions from `Exception` rather than `BaseException`** (PEP 8):

```python
# Correct
class MyError(Exception):
    """My custom error."""

# Wrong
class MyError(BaseException):
    """My custom error."""
```

**Use the suffix "Error" on exception class names** when the exception is an error.

---

## Enforcement

These rules are enforced through:

1. **Code review** - All PRs must be reviewed for compliance
2. **Linting** - `ruff check src/ tests/` for style violations
3. **Type checking** - `mypy src/autosar_pdf2txt/` for type correctness
4. **Testing** - `pytest tests/ -v --cov=src/autosar_pdf2txt` for coverage

### Running CI Checks

```bash
# Install dev dependencies
pip install pytest pytest-cov ruff mypy

# Run all checks
ruff check src/ tests/
mypy src/autosar_pdf2txt/
pytest tests/ -v --cov=src/autosar_pdf2txt --cov-report=term
```

---

## References

This document combines project-specific coding standards with these industry-standard style guides:

- [PEP 8 - Style Guide for Python Code](https://peps.python.org/pep-0008/) - Code layout, naming conventions, and general Python style
- [PEP 484 - Type Hints](https://peps.python.org/pep-0484/) - Type annotation standards
- [PEP 257 - Docstring Conventions](https://peps.python.org/pep-0257/) - Docstring formatting (complementary to Google-style)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html) - Additional best practices
- [Pytest Documentation](https://docs.pytest.org/) - Testing conventions

## Summary of Key Additions from PEP 8

The following sections from PEP 8 have been integrated into this document:

1. **Code Layout** (CODING_RULE_LAYOUT_00001 - CODING_RULE_LAYOUT_00007)
   - Indentation (4 spaces)
   - Line length limits (79 characters code, 72 characters comments/docstrings)
   - Line breaking before binary operators
   - Blank lines between functions and classes
   - UTF-8 encoding
   - String quote conventions

2. **Whitespace in Expressions** (CODING_RULE_WS_00001 - CODING_RULE_WS_00006)
   - Avoid extraneous whitespace
   - Operator spacing rules
   - Keyword argument formatting
   - Function annotation formatting
   - No trailing whitespace
   - Avoid compound statements

3. **Programming Recommendations** (CODING_RULE_PR_00001 - CODING_RULE_PR_00010)
   - Type comparisons with `isinstance()`
   - Sequence boolean checks
   - String prefix/suffix methods
   - `None` comparisons with `is`/`is not`
   - Boolean comparison rules
   - Exception handling best practices
   - Resource management with `with`
   - Return statement consistency
   - Use `def` instead of lambda assignment
   - Exception class design

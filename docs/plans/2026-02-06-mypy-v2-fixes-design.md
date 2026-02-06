# Design: Mypy V2 Models Error Fixing

**Date**: 2026-02-06
**Author**: Claude Code
**Status**: Design Complete

## Problem Statement

The V2 models in `src/armodel/v2/models/` have **6,348 mypy errors** across 170 files, preventing adoption of type safety. The errors fall into these categories:

| Error Type | Count | Description |
|------------|-------|-------------|
| `no-untyped-def` | 4,088 | Functions without return type annotations |
| `assignment` | 1,253 | Type assignment mismatches (None to typed variables) |
| `abstract` | 268 | Abstract class issues |
| `return-value` | 255 | Return value mismatches |
| `name-defined` | 201 | Names not defined (missing imports) |
| `arg-type` | 192 | Argument type mismatches |
| Other | 92 | Various minor issues |

## Solution Overview

Semi-automated fixer using mypy's JSON output and AUTOSAR requirements metadata to apply targeted fixes with high confidence while flagging complex cases for manual review.

### Approach: Option C - Mypy JSON-Driven Fixing

**Why this approach?**
- Most precise - only touch code mypy actually complains about
- JSON output gives exact line numbers and column positions
- Easy to track progress and verify after each iteration
- Can handle edge cases safely by falling back to manual review

## Architecture

### Core Components

#### 1. MypyErrorParser
Parse mypy JSON output to extract structured error information:
```python
{
  "file": "src/armodel/v2/models/...",
  "line": 42,
  "column": 5,
  "error_code": "no-untyped-def",
  "message": "Function is missing a return type annotation"
}
```

#### 2. TypeResolver
Load and query `docs/requirements/mapping.json` and package `.classes.json` files:
- Resolve type names to import paths
- Look up attribute types and multiplicities
- Determine if type should be optional (multiplicity "0..1")

Example resolution:
```
Type name: ARFloat
↓
Package path: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::PrimitiveTypes
↓
Python import: from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (ARFloat,)
```

#### 3. ASTFixer
Apply targeted AST modifications using Python's `ast` module:
- Parse source code to AST
- Use `ast.NodeTransformer` for precise modifications
- Unparse back to source with `ast.unparse()`
- Validate modified AST before writing

#### 4. ProgressTracker
Track fixing progress across iterations:
```json
{
  "last_run": "2026-02-06T10:00:00",
  "files_fixed": 150,
  "errors_remaining": 1200,
  "categories_completed": ["no-untyped-def", "assignment"]
}
```

### Error Categorization and Fix Strategies

#### Category 1: `no-untyped-def` (4,088 errors)

**Pattern-based fixes:**

- **`__init__` methods** → Add `-> None`
  ```python
  def __init__(self):  # BEFORE
  def __init__(self) -> None:  # AFTER
  ```

- **Getter methods (`get*`)** → Infer from attribute type
  ```python
  def getRole(self):  # BEFORE
  def getRole(self) -> ARLiteral:  # AFTER (inferred from self.role type)
  ```

- **Setter methods (`set*`)** → Add param + return `self` for chaining
  ```python
  def setRole(self, value):  # BEFORE
  def setRole(self, value: ARLiteral) -> 'ClassName':  # AFTER
  ```

- **Boolean methods (`is*`, `has*`, `validate*`)** → Add `-> bool`
  ```python
  def isValid(self):  # BEFORE
  def isValid(self) -> bool:  # AFTER
  ```

- **Collection adders (`add*`)** → Add param type + return `self`
  ```python
  def addItem(self, item):  # BEFORE
  def addItem(self, item: ItemType) -> 'ClassName':  # AFTER
  ```

#### Category 2: `assignment` (1,253 errors)

**Pattern: None assigned to non-optional typed variable**

```python
# BEFORE (error)
self.role: ARLiteral = None

# AFTER (fixed)
self.role: ARLiteral | None = None  # V2 style (Python 3.10+)
```

**Type inference strategy:**
- Scan `__init__` for attribute assignments
- Build symbol table of attribute names to types
- Check requirements metadata for multiplicity "0..1" (optional)
- Update type annotation to include `| None`

#### Category 3: `name-defined` (201 errors)

**Pattern: Type used in annotation but not imported**

```python
# BEFORE (error) - Name "ARFloat" is not defined
self.coefficient: ARFloat = None

# AFTER (fixed) - Import added
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARFloat,
)
```

**Import generation:**
- Look up type name in `docs/requirements/mapping.json`
- Convert package path to Python import path
- Generate block-style import (V2 coding rule)
- Insert at correct position (after existing imports)

#### Category 4: Manual Review Required

**Errors requiring manual intervention:**

- **Property setter overrides** (255 `return-value` errors)
  - Subclass setter has incompatible type with base class
  - Generate report with file:line and suggested fixes
  - Manual review needed to decide correct type

- **Abstract class instantiation** (268 `abstract` errors)
  - May indicate actual bugs or missing implementations
  - Flag for manual review with context
  - Don't auto-fix

- **Complex generic types**
  - `Dict[str, List['SomeClass']]` annotations
  - Skip if can't infer confidently

## V2 Coding Rules Compliance

All fixes must strictly adhere to V2 coding rules:

### CODING_RULE_V2_00001: Absolute Imports Only
```python
# Required
from armodel.v2.models.M2.AUTOSARTemplates.SomeModule import (SomeClass,)

# Forbidden
from .SomeModule import SomeClass
```

### CODING_RULE_V2_00002: No TYPE_CHECKING Blocks
```python
# Required - runtime imports
from armodel.v2.models.M2.AUTOSARTemplates.SomeModule import (SomeClass,)

# Forbidden
if TYPE_CHECKING:
    from armodel.v2.models.M2.AUTOSARTemplates.SomeModule import SomeClass
```

### CODING_RULE_V2_00003: Explicit __all__ Exports
```python
# When adding classes to __init__.py, update __all__
from armodel.v2.models.M2.AUTOSARTemplates.SomeModule import (
    ClassOne,
    ClassTwo,
)

__all__ = [
    "ClassOne",
    "ClassTwo",
]
```

### CODING_RULE_V2_00005: String Annotations for Forward References
```python
# Required - use string notation
def setParent(self, parent: 'ParentClass') -> 'ChildClass':
    pass
```

### CODING_RULE_V2_00012: Explicit Class Imports
```python
# Required - import individual classes
from armodel.v2.models.M2.AUTOSARTemplates.SomeModule import (
    ClassOne,
    ClassTwo,
)

# Forbidden - no wildcards
from armodel.v2.models.M2.AUTOSARTemplates.SomeModule import *
```

### CODING_RULE_V2_00013: Block Import Style
```python
# Required - multi-line with parentheses
from armodel.v2.models.M2.AUTOSARTemplates.SomeModule import (
    ClassOne,
    ClassTwo,
    ClassThree,
)
```

## Testing and Verification

### Pre-Fix Safety Checks
1. Create backup of each file: `file.py.backup`
2. Verify modified AST can be parsed to valid Python
3. Run syntax check: `python -m py_compile file.py`

### Per-File Verification
After fixing a file:
```bash
mypy src/armodel/v2/models/path/to/File.py --no-error-summary
```
Only proceed if error count decreases.

### Checkpoint Verification
After each major category:
1. Run full mypy on V2 models
2. Compare error count before/after
3. Run pytest on affected modules
4. Commit changes with descriptive message

### Final Verification
1. Full mypy with no errors
2. `pytest tests/test_armodel/models_v2/` - all pass
3. `ruff check src/armodel/v2/models` - V2 rules pass
4. Spot-check random files for correctness

## Implementation File Structure

### Main Script
**`scripts/mypy_fix_v2_models.py`** (~500 lines)
- CLI argument parsing
- Main orchestration logic
- Progress tracking

### Supporting Modules (in `scripts/mypy_fixers/`)
- `error_parser.py` - Parse mypy JSON output
- `type_resolver.py` - Resolve types using requirements metadata
- `ast_transformers.py` - AST modification helpers
- `import_generator.py` - Generate V2-compliant imports
- `progress_tracker.py` - Track fix progress

### Output Artifacts
```
.mypy_fix_backup/           # Original file backups
.mypy_fix_progress.json     # Progress tracking
.mypy_fix_report.md         # Final summary report
manual_fixes.md            # Errors requiring manual review
```

### CLI Interface
```bash
# Preview changes
python scripts/mypy_fix_v2_models.py --dry-run

# Initial run
python scripts/mypy_fix_v2_models.py --init

# Resume from progress
python scripts/mypy_fix_v2_models.py --continue

# Fix specific category
python scripts/mypy_fix_v2_models.py --category=no-untyped-def

# Check progress only
python scripts/mypy_fix_v2_models.py --verify
```

## Implementation Phases

### Phase 1: Infrastructure Setup
- Create main script skeleton with CLI parsing
- Implement `MypyErrorParser` to parse JSON output
- Implement `ProgressTracker` for state persistence
- **Test**: Run mypy, parse output, display error statistics

### Phase 2: Type Resolver
- Load `docs/requirements/mapping.json` and package `.classes.json`
- Implement type name → import path resolution
- Build attribute type lookup from requirements
- **Test**: Resolve common types (ARFloat, ARLiteral, etc.)

### Phase 3: Core Fixers
- Implement `no-untyped-def` fixer for `__init__` methods
- Implement `assignment` fixer (add `| None` to types)
- Implement `name-defined` fixer (generate imports)
- **Test**: Fix single file, verify mypy error count decreases

### Phase 4: Advanced Fixers
- Implement getter/setter type inference
- Implement boolean method type annotation
- Implement collection adder type annotation
- **Test**: Run on subset of problematic files

### Phase 5: Iterative Run
- Run full fixer on all V2 models
- Generate `manual_fixes.md` for edge cases
- Iterate: fix → verify → address manual fixes
- **Goal**: Reduce errors from 6,348 to <500

### Phase 6: Final Polish
- Manual review and fixes for remaining errors
- Full test suite verification
- Update CI/CD to include mypy check
- Document lessons learned

## Confidence Scoring

### High Confidence (Auto-Fix)
- `__init__ → None` additions
- `| None` for optional attributes
- Import generation from requirements metadata

### Medium Confidence (Fix with Comment)
- Type inference from requirements (may need context)
- Setter parameter types from attribute types
- Complex forward references

### Low Confidence (Report Only)
- Property setter overrides (need design review)
- Abstract class errors (may indicate bugs)
- Multiple inheritance type conflicts

## Expected Outcomes

### Quantitative Goals
- Reduce errors from **6,348 to <500** (90%+ reduction)
- Fix all **high-confidence** errors automatically
- Flag **medium/low-confidence** errors for manual review

### Qualitative Goals
- All automated fixes follow V2 coding rules
- No test regressions from fixes
- Improved type safety across V2 models
- Foundation for enabling strict mypy checking

## Risks and Mitigations

### Risk 1: AST Modification Breaks Code
**Mitigation**: Validate modified AST before writing, keep backups, run syntax checks

### Risk 2: Incorrect Type Inference
**Mitigation**: Use requirements metadata as source of truth, confidence scoring, manual review flagging

### Risk 3: V2 Coding Rule Violations
**Mitigation**: Post-fix ruff checks, block import enforcement, __all__ validation

### Risk 4: Test Regressions
**Mitigation**: Per-file pytest checks, incremental verification, full test suite at milestones

## Success Criteria

1. **Zero automated mypy errors**: `mypy src/armodel/v2/models` shows only manual-fix errors
2. **All tests pass**: `pytest` continues to pass
3. **No regressions**: V1 API compatibility maintained
4. **V2 coding rules followed**: `ruff check src/armodel/v2/models` passes
5. **Documentation**: Manual fixes documented with resolution guidance

## References

- V2 coding rules: `docs/development/coding_rules_v2.md`
- V2 migration guide: `docs/development/v2_migration_guide.md`
- Requirements metadata: `docs/requirements/mapping.json`
- Mypy config: `pyproject.toml` (line 129-159)
- Original issue plan: Transcript at `/Users/ray/.claude/projects/-Users-ray-Workspace-py-armodel/49fef7d9-54da-4d3b-9efe-1078958bb8fe.jsonl`

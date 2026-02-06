# Design: Mypy V2 Models Error Fixing

**Date**: 2026-02-06
**Author**: Claude Code
**Status**: Updated - Manual Approach

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

**Manual, incremental fixing approach** with mypy error analysis tools. After testing automated fixes, the risk of unintended modifications is too high. Instead, we'll use a careful manual approach with tooling support.

### Approach: Manual Fixes with Mypy Analysis Tools

**Why manual instead of automated?**
- **Safety**: Manual review prevents unintended modifications
- **Context awareness**: Human can understand business logic and design intent
- **Learning**: Manual fixing helps understand type patterns across the codebase
- **V2 coding rules**: Better compliance with V2-specific coding standards
- **Test-driven**: Can verify each fix with immediate testing

## Manual Fixing Strategy

### Phase 1: High-Confidence Fixes (Quick Wins)

#### Fix Pattern 1: `__init__` Methods (Estimated: 800-1000 fixes)

**Pattern**: Add `-> None` to `__init__` methods

**Example**:
```python
# BEFORE
def __init__(self):
    super().__init__()
    self.attr: str = None

# AFTER
def __init__(self) -> None:
    super().__init__()
    self.attr: Union[str, None] = None
```

**Manual process**:
1. Run: `mypy src/armodel/v2/models --show-error-codes | grep "no-untyped-def" | grep "__init__"`
2. For each file:
   - Open file
   - Find `__init__` methods without return type
   - Add `-> None`
   - Also check for `self.attr: Type = None` patterns and fix to `Union[Type, None]`
   - Add `from typing import Union` if needed
   - Save file
   - Run mypy on that file to verify
   - Run tests for affected module

**Files to prioritize** (by error count):
- `ServiceNeeds.py` - 287 errors
- `CoreTopology.py` - 247 errors
- `ServiceInstances.py` - 241 errors
- `ARPackage.py` - 233 errors
- `BswBehavior.py` - 228 errors

#### Fix Pattern 2: None Assignments (Estimated: 1200-1300 fixes)

**Pattern**: Change `self.attr: Type = None` to `Union[Type, None]`

**Example**:
```python
# BEFORE
def __init__(self):
    self.groupName: str = None
    self.groupId: str = None

# AFTER
def __init__(self) -> None:
    self.groupName: Union[str, None] = None
    self.groupId: Union[str, None] = None
```

**Manual process**:
1. Run: `mypy src/armodel/v2/models --show-error-codes | grep "assignment"`
2. Group errors by file
3. For each file:
   - Open file
   - Find all `self.attr: Type = None` patterns
   - Replace with `Union[Type, None]`
   - Add `from typing import Union` at top (if not present)
   - Save file
   - Run mypy on that file to verify
   - Run tests

### Phase 2: Medium-Confidence Fixes

#### Fix Pattern 3: Getter Methods (Estimated: 1500-2000 fixes)

**Pattern**: Add return type based on attribute type

**Example**:
```python
# BEFORE
def getGroupName(self):
    return self.groupName

# AFTER
def getGroupName(self) -> Union[str, None]:
    return self.groupName
```

**Manual process**:
1. Identify getter methods: `def get*(self):`
2. Find the corresponding attribute (usually `self.*_name` or `self.*Name`)
3. Check attribute type annotation
4. Add matching return type to getter
5. Verify with mypy

#### Fix Pattern 4: Setter Methods (Estimated: 800-1000 fixes)

**Pattern**: Add parameter type and return type

**Example**:
```python
# BEFORE
def setGroupName(self, value):
    self.groupName = value
    return self

# AFTER
def setGroupName(self, value: Union[str, None]) -> 'ClassName':
    self.groupName = value
    return self
```

**Manual process**:
1. Identify setter methods: `def set*(self, value):`
2. Find the corresponding attribute
3. Add parameter type matching attribute type
4. Add return type of self (use string notation)
5. Verify with mypy

### Phase 3: Import Fixes (201 errors)

**Pattern**: Add missing imports for type annotations

**Example**:
```python
# Add to imports
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARLiteral,
    ARFloat,
)
```

**Manual process**:
1. Run: `mypy src/armodel/v2/models --show-error-codes | grep "name-defined"`
2. For each undefined name:
   - Use `docs/requirements/mapping.json` to find package path
   - Generate import statement (V2 block style)
   - Add to file imports
   - Verify

### Phase 4: Manual Review Required (Skip or Flag)

These errors require careful manual review:

- **`abstract` (268 errors)**: May indicate design issues
- **`return-value` (255 errors)**: Type incompatibilities
- **`arg-type` (192 errors)**: Complex type mismatches

**Strategy**: Create tracking document for these, address individually with careful analysis.

## Tooling Support (Read-Only)

### Error Analysis Script (Safe, Read-Only)

Create read-only scripts to help with manual fixing:

```python
# scripts/mypy_analyze.py (READ-ONLY)
"""Analyze mypy errors and generate fix recommendations."""

def categorize_errors():
    """Group errors by file and type."""
    pass

def suggest_fixes(filepath):
    """Suggest fixes for a specific file (DOES NOT MODIFY)."""
    pass

def generate_fix_report():
    """Generate markdown report of recommended fixes."""
    pass
```

### Mypy Error Filtering

```bash
# Get __init__ errors
mypy src/armodel/v2/models --show-error-codes 2>&1 | grep "no-untyped-def" | grep "__init__"

# Get assignment errors by file
mypy src/armodel/v2/models --show-error-codes 2>&1 | grep "assignment" | cut -d: -f1 | sort -u

# Get top 10 files with most errors
mypy src/armodel/v2/models --show-error-codes 2>&1 | grep "error:" | cut -d: -f1 | sort | uniq -c | sort -rn | head -10
```

## Execution Plan

### Iteration 1: Quick Wins (1-2 weeks)

**Target**: Reduce from 6,348 to ~4,000 errors

**Fixes**:
1. All `__init__` methods (~800-1000 fixes)
2. None assignments in `__init__` (~1200-1300 fixes)

**Process**:
- Fix 10-20 files per day
- Run tests after each file
- Commit changes frequently
- Track progress in spreadsheet

### Iteration 2: Getters/Setters (2-3 weeks)

**Target**: Reduce from ~4,000 to ~2,000 errors

**Fixes**:
- Getter return types (~1500-2000 fixes)
- Setter parameter types (~800-1000 fixes)

**Process**:
- Focus on one module at a time
- Use type inference from attributes
- Verify with tests

### Iteration 3: Imports and Cleanup (1 week)

**Target**: Reduce to ~1,500 errors (remaining need manual review)

**Fixes**:
- Missing imports (~200 fixes)
- Clean up any regressions

### Iteration 4: Complex Cases (Ongoing)

**Target**: Reduce to <500 errors (manual-fix only)

**Process**:
- Address each remaining error individually
- Document patterns and decisions
- Update type stubs if needed

## Verification Process

### Per-File Verification

After each file is fixed:

```bash
# 1. Check mypy errors reduced
mypy src/armodel/v2/models/path/to/File.py

# 2. Run tests for module
pytest tests/test_armodel/models_v2/path/to/test_file.py

# 3. Run ruff to check V2 coding rules
ruff check src/armodel/v2/models/path/to/File.py
```

### Milestone Verification

After each iteration:

```bash
# 1. Full mypy check
mypy src/armodel/v2/models --show-error-codes

# 2. Full test suite
pytest tests/test_armodel/models_v2/

# 3. V2 coding rules check
ruff check src/armodel/v2/models

# 4. Commit with message
git commit -m "fix(mypy): Iteration N - X files fixed, reduced errors from A to B"
```

## V2 Coding Rules Checklist

For each fix, verify:

- [ ] CODING_RULE_V2_00001: Absolute imports only
- [ ] CODING_RULE_V2_00002: No TYPE_CHECKING blocks
- [ ] CODING_RULE_V2_00003: Explicit `__all__` exports (in `__init__.py`)
- [ ] CODING_RULE_V2_00005: String annotations for forward references
- [ ] CODING_RULE_V2_00012: Explicit class imports (no wildcards)
- [ ] CODING_RULE_V2_00013: Block import style

## Progress Tracking

### Metrics to Track

- Total errors (from mypy)
- Errors by category
- Files fixed
- Tests passing
- Time spent

### Weekly Goals

- Week 1-2: Fix 1000+ errors (__init__ + assignments)
- Week 3-5: Fix 2000+ errors (getters/setters)
- Week 6: Fix 500+ errors (imports + cleanup)
- Week 7+: Address remaining complex cases

## Expected Outcomes

### Quantitative Goals

- **Iteration 1**: 6,348 → ~4,000 errors (37% reduction)
- **Iteration 2**: ~4,000 → ~2,000 errors (50% reduction from start)
- **Iteration 3**: ~2,000 → ~1,500 errors (76% reduction from start)
- **Iteration 4**: ~1,500 → <500 errors (92% reduction from start)

### Qualitative Goals

- All fixes manually reviewed for correctness
- V2 coding rules maintained
- No test regressions
- Better understanding of type patterns in codebase
- Foundation for strict mypy checking

## Risk Mitigation

### Risk 1: Introducing Bugs

**Mitigation**:
- Run tests after each file
- Review changes before committing
- Keep changes small and focused

### Risk 2: V2 Coding Rule Violations

**Mitigation**:
- Run ruff after each fix
- Manual review of imports
- Use V2 coding rules checklist

### Risk 3: Time Overrun

**Mitigation**:
- Focus on high-impact fixes first
- Track progress weekly
- Adjust scope if needed
- Document patterns for faster fixing

## Success Criteria

1. **<500 mypy errors** remaining (92%+ reduction from 6,348)
2. **All tests passing** (no regressions)
3. **V2 coding rules** maintained (ruff check passes)
4. **Documented patterns** for remaining errors
5. **Foundation** for enabling strict mypy checking in future

## References

- V2 coding rules: `docs/development/coding_rules_v2.md`
- V2 migration guide: `docs/development/v2_migration_guide.md`
- Requirements metadata: `docs/requirements/mapping.json`
- Mypy config: `pyproject.toml` (line 129-159)
- Original automated design: `docs/plans/2026-02-06-mypy-v2-fixes-design.md.bak`

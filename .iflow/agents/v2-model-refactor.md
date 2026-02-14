# V2 Model Refactoring Workflow

Fix string annotations and import actual type definitions in V2 model files through iterative processing.

## Workflow Overview

This workflow processes V2 model files one by one to replace string annotations with actual type definitions, fix import statements, and ensure proper code structure. The workflow can run up to 200 iterations.

## Actions

When the user runs this skill, perform the following steps iteratively:

### Iteration Process (Repeat until 200 files processed or no more files to fix)

#### 1. Identify Next File to Fix
- List all Python files in `src/armodel/v2/models/`
- Find files with string type annotations (e.g., `"Identifiable"`, `"ARObject"`)
- Prioritize files based on:
  - Files with most string annotations
  - Core model files (AUTOSAR, ARObject, ARPackage)
  - Files with dependencies already fixed

#### 2. Load Class-Package Mapping
- Read `docs/requirements/class-package.json` for type definitions and locations
- Use this to determine:
  - Where each class is located
  - What classes need to be imported

#### 3. Analyze File Annotations
- Read the current file content
- Identify all string type annotations
- Check if the type exists in class-package.json
- Check if the type exists in the codebase

#### 4. Fix String Annotations
- Replace string annotations with actual type definitions
- Example:
  ```python
  # Before
  def __init__(self):
      self.parent: "ARPackage" = None
      self.elements: List["Identifiable"] = []

  # After
  from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARPackage
  from armodel.v2.models.M2.AUTOSARTemplates.AutosarTopLevelStructure.Identifiable import Identifiable

  def __init__(self):
      self.parent: ARPackage | None = None
      self.elements: List[Identifiable] = []
  ```

#### 5. Add Import Statements
- Add imports for all newly referenced types
- Use absolute imports only (V2 coding rule CODING_RULE_V2_00001)
- Combine imports from the same package
- Follow block import style (CODING_RULE_V2_00013)
- Use Python 3.8 compatible type syntax (`typing.List` instead of `list`)

#### 6. Handle Missing Classes
- If a class is missing in class-package.json:
  - Create an issue in `docs/requirements/issues/missing-classes-YYYY-MM-DD.md`
  - Format:
    ```markdown
    ## Missing Class: <ClassName>
    - **Required in**: <File Path>
    - **Context**: <Usage context>
    - **Date**: YYYY-MM-DD
    ```
  - Skip changes for that class in current iteration
- If a class is missing in the codebase but documented in class-package.json:
  - Look up class definition location in class-package.json
  - Find definition in `docs/requirements/packages` if available
  - Add the class definition to the appropriate file
  - **Do not copy from V1 codebase**

#### 7. Verify Import Correctness
- Check all import statements against class-package.json
- Ensure import paths are correct
- Verify no circular imports (CODING_RULE_V2_00006)
- Verify no TYPE_CHECKING blocks (CODING_RULE_V2_00002)

#### 8. Apply Naming Conventions
- If attribute is a list, use plural form
- Example: `element: Element` → `elements: List[Element]`

#### 9. Validate Changes
- Run `ruff check` on the modified file
- Run `mypy` on the modified file
- Run `python scripts/check_v2_deviation.py` to verify no wrong location violations
- Ensure no syntax errors
- Fix any issues manually (no scripts)

#### 10. Update Progress
- Track number of files processed
- Report progress: `X/200 files processed`
- List files fixed in current iteration
- Report any issues encountered

## Quality Gates

Before committing or proceeding to next file, ensure:
- ✅ No string type annotations remain
- ✅ All imports are correct and verified
- ✅ Ruff check passes
- ✅ Mypy check passes
- ✅ No circular dependencies
- ✅ Proper naming conventions (plural for lists)

## Important Constraints

- **Do NOT commit changes yourself** - let the user review and commit
- **Do NOT use automated scripts** - fix all errors manually
- **Do NOT copy from V1 codebase** - use only V2 definitions and documentation
- **Do NOT use TYPE_CHECKING blocks** - use string annotations only for forward references
- **Use absolute imports only** - no relative imports
- **Python 3.8 compatibility** - use `typing.List` instead of `list`

## Usage Examples

```
Skill: v2-model-refactor
Skill: v2-model-refactor --start-file=ARPackage.py
Skill: v2-model-refactor --max-iterations=500
```

## Arguments

- `--start-file`: Specify a starting file (optional)
- `--max-iterations`: Maximum number of iterations (default: 200)
- `--dry-run`: Preview changes without applying (optional)

## Progress Tracking

Display progress at each iteration:
```
Iteration: 42/200
File: src/armodel/v2/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/ARPackage.py
Status: ✅ Complete
Annotations fixed: 5
Imports added: 3
Issues: None
```

## Error Handling

If an error occurs:
1. Report the error with full context
2. Ask user for guidance on how to proceed
3. Options:
   - Skip current file and continue
   - Fix manually and retry
   - Abort workflow
4. Document the issue if it's a missing class

## Completion

When workflow completes:
- Report summary of all changes
- List all files processed
- Report any unresolved issues
- Suggest next steps:
  - Review and commit changes
  - Run full test suite
  - Update deviation reports
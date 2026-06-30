# Mypy Type Analysis Report - M2 Models

**Date:** 2026-07-01
**Module:** `src/armodel/models/M2/`
**Mypy Version:** 1.19.1

## Executive Summary

- **Total Errors:** 1,021 type errors
- **Error Categories:** 14 distinct error code types
- **Primary Issues:** Type incompatibility (752 errors), Argument types (131 errors), Name definitions (44 errors)

## Error Distribution

| Error Type | Count | Percentage |
|------------|-------|------------|
| Incompatible (return/assignment/attribute) | 752 | 73.7% |
| Argument (arg-type) | 131 | 12.8% |
| Name (name-defined) | 44 | 4.3% |
| Cannot (import/module not found) | 27 | 2.6% |
| Need (annotation) | 23 | 2.3% |
| Skipping (unanalyzed) | 14 | 1.4% |
| Module (import) | 11 | 1.1% |
| Invalid (decorator/metadata) | 7 | 0.7% |
| Item (list index) | 6 | 0.6% |
| Function (signature) | 2 | 0.2% |
| Value (literal) | 1 | 0.1% |
| Unsupported (operand) | 1 | 0.1% |
| Signature | 1 | 0.1% |
| Missing (lib) | 1 | 0.1% |

## Critical Issues

### 1. Import/Module Not Found (27 errors)

Missing module implementations causing import-not-found errors:

**MeasurementCalibrationSupport (20 errors):**
- `RptServicePoint`, `RptSupportData`, `RptSwPrototypingAccess`
- `McFunctionDataRefSet`, `RptAccessEnum`, `RptComponent`
- `RptEnablerImplTypeEnum`, `RptExecutableEntity`, `RptExecutableEntityEvent`
- `RptExecutionContext`, `RptExecutionControlEnum`, `RptPreparationEnum`
- `ImplementationElementInParameterInstanceRef`, `McDataAccessDetails`
- `McDataInstance`, `McFunction`, `McParameterElementGroup`
- `McSupportData`, `McSwEmulationMethodSupport`, `RoleBasedMcDataAssignment`

**SignalServiceTranslation (6 errors):**
- `SignalServiceTranslationControlEnum`
- `SignalServiceTranslationElementProps`
- `SignalServiceTranslationEventProps`
- `SignalServiceTranslationProps`
- `SignalServiceTranslationPropsSet`

**BlueprintMapping (1 error):**
- `BlueprintMappingSet`

### 2. Type Incompatibility - Return Values (Sample)

```python
# src/armodel/models/M2/MSR/Documentation/TextModel/MultilanguageData.py:40
# Expected: list[LOverviewParagraph], Got: list[str]

# src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/Identifiable.py:57
# Expected: ARObject, Got: Optional[ARObject]

# src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/FibexCore/CoreCommunication.py:96
# Expected: PduToFrameMapping, Got: Optional[Referrable]
```

### 3. Type Incompatibility - Assignment (Sample)

```python
# src/armodel/models/M2/MSR/DataDictionary/SystemConstant.py:20
# Expression: None, Variable: SwDataDefProps

# src/armodel/models/M2/MSR/AsamHdo/Units.py:25-31
# Expression: None, Variable: ARNumerical (7 instances)
```

### 4. Argument Type Mismatches (Sample)

```python
# src/armodel/models/M2/MSR/Documentation/TextModel/MultilanguageData.py:36
# list.append() expected str, got LOOverviewParagraph

# src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ModeDeclaration.py:278
# filter() Callable[[Any], bool], expected Callable[[Referrable], TypeGuard[ModeDeclaration]]

# src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Multiplatform.py:229
# list.append() expected IPduMapping, got FrameMapping
```

### 5. Name Definition Errors (44 errors)

```python
# src/armodel/models/M2/MSR/DataDictionary/ServiceProcessTask.py:12
# Name "ArgumentDirectionEnum" is not defined
```

## Files with Most Errors (Top 30)

| Count | File |
|-------|------|
| 3 | `CommonStructure/Implementation.py:109` |
| 2 | `GenericStructure/GeneralTemplateClasses/Identifiable.py:64` |
| 2 | `GenericStructure/GeneralTemplateClasses/ARPackage.py:344` |
| 2 | `CommonStructure/Timing/TimingConstraint/SynchronizationTiming.py:53` |
| 2 | `CommonStructure/Timing/TimingConstraint/SynchronizationPointConstraint.py:17` |
| 2 | `CommonStructure/Timing/TimingConstraint/OffsetConstraint.py:16` |
| 2 | `CommonStructure/Timing/TimingConstraint/LatencyTimingConstraint.py:36` |
| 2 | `CommonStructure/Timing/TimingConstraint/ExecutionTimeConstraint.py:36` |
| 2 | `CommonStructure/Timing/TimingConstraint/EventTriggeringConstraint.py:26` |
| 2 | `CommonStructure/Timing/TimingConstraint/AgeConstraint.py:17` |

## Recommended Actions

### Priority 1: Fix Import Errors
1. Create missing modules in `MeasurementCalibrationSupport/` directory
2. Create missing modules in `SignalServiceTranslation/` directory  
3. Create `BlueprintMappingSet` module
4. Ensure all `__init__.py` files properly export new modules

### Priority 2: Fix Type Annotations
1. Add `Optional[]` wrapper where `None` is valid return value
2. Fix list type annotations (e.g., `list[str]` vs `list[LOverviewParagraph]`)
3. Add proper TypeGuard annotations for filter functions
4. Fix `Optional` vs non-Optional return type mismatches

### Priority 3: Fix Assignment/Attribute Errors
1. Initialize optional attributes with `None` properly typed as `Optional[T]`
2. Use proper type guards or isinstance checks before assignments
3. Fix dataclass field type annotations

### Priority 4: Address Missing Definitions
1. Import or define `ArgumentDirectionEnum` and other undefined names
2. Verify all type references exist in codebase

## Running Type Check

```bash
# Full check
python -m mypy src/armodel/models/M2/ --show-error-codes

# With untyped defs checked
python -m mypy src/armodel/models/M2/ --show-error-codes --check-untyped-defs

# Specific file
python -m mypy src/armodel/models/M2/AUTOSARTemplates/CommonStructure/Implementation.py
```

## Notes

- Many errors relate to AUTOSAR model complexity with optional fields
- TypeGuard pattern needed for filter functions returning specific types
- Some errors may cascade from import issues - fix imports first
- Consider `# type: ignore` for intentionally dynamic AUTOSAR reflection code

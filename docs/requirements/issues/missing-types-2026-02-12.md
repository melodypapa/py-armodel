# Missing Types Report

Generated: 2026-02-12

## FeatureModelTemplate

### FMConditionByFeatures
- **Issue**: The specification uses `FMConditionByFeatures` as a type, but the actual class names are:
  - `FMConditionByFeaturesAndAttributes` (used for restrictionAndAttributes and restriction)
  - `FMConditionByFeaturesAndSwSystemconsts` (used for fmSyscondAndSwSystemconsts)
- **Source**: `M2_AUTOSARTemplates_FeatureModelTemplate.classes.json`
- **Action**: Need to replace `FMConditionByFeatures` references with the correct class names based on context
- **Context**:
  - `FMFeatureRestriction.restrictionAndAttributes` → `FMConditionByFeaturesAndAttributes`
  - `FMFeatureRelation.restriction` → `FMConditionByFeaturesAndAttributes`
  - `FMFeatureMapCondition.fmCondAndAttributes` → `FMConditionByFeaturesAndAttributes`
  - `FMFeatureMapAssertion.fmSyscondAndSwSystemconsts` → `FMConditionByFeaturesAndSwSystemconsts`

### RefType
- **Issue**: Not found in class-package.json but used in code
- **Status**: Needs investigation

## Summary
- Total missing types identified: 2
- Files affected: FeatureModelTemplate.py
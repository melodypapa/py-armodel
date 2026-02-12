# Missing Classes in class-package.json

**Date**: 2026-02-11
**Updated**: 2026-02-12
**File**: `src/armodel/v2/models/M2/MSR/Documentation/Chapters.py`
**Issue**: Classes referenced in code but missing from `class-package.json`

## Resolved Issues

### ~~1. TopicContentOrMsr~~ **RESOLVED**

**Status**: Fixed - Was actually `TopicContentOrMsrQuery` which exists in class-package.json

**Resolution**: All references to `TopicContentOrMsr` have been corrected to `TopicContentOrMsrQuery`:
- Fixed in `ChapterContent` class
- Fixed in `Topic1` class
- Removed string annotations, using actual type definition

## Outstanding Issues

### 1. TraceableTable

**Location**: Referenced in `TopicContent` class
**Usage**:
- Line 1413: `self._traceableTable: "TraceableTable" = None`
- Lines 1495, 1507, 1557: Methods using TraceableTable type

**Context**: This appears to be a specialized table type with tracing capabilities.

**Related Classes Found** (may be relevant):
- `Traceable` - exists in M2::MSR::Documentation::BlockElements::RequirementsTracing
- `TraceableText` - exists in M2::MSR::Documentation::BlockElements::RequirementsTracing

**Action Required**:

This class needs to be:
1. Located in the AUTOSAR specification (possibly in MSR::Documentation::BlockElements)
2. Verified if it's actually `Table` with traceable capability, or a separate class
3. Added to `docs/requirements/class-package.json` with proper package path if it exists
4. Imported or defined in the appropriate location
5. String annotations replaced with actual type definitions once resolved

**Temporary Workaround**: Keep string annotation `"TraceableTable"` until the class is located and added to class-package.json.

## Impact

- String annotation remains in the code for TraceableTable
- Type checking may fail for traceableTable property
- Import statement cannot be completed until this is resolved

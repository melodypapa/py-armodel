# V2 Coding Rules Todo

## Completed ✅

- [x] Check violations of current v2 codebase `src/armodel/v2` with `docs/development/coding_rules_v2.md`
- [x] Fix all violations

## Summary (2026-02-12)

### All Violations Fixed:
- **180 V1 imports** → converted to V2 imports
- **0 relative imports** (CODING_RULE_V2_00001)
- **0 TYPE_CHECKING blocks** (CODING_RULE_V2_00002)
- **206/206 __init__.py files with __all__** (CODING_RULE_V2_00003)
- **0 wildcard imports** (CODING_RULE_V2_00012)

### Files Modified:
- 180 files with V1 imports (batch fixed)
- 9 MSR Documentation files with additional fixes:
  - BlockElements/__init__.py
  - OasisExchangeTable.py
  - RequirementsTracing.py
  - Chapters.py
  - MsrQuery.py
  - ChapterOrMsrQuery.py
  - Topic1.py
  - Annotation.py
  - Figure.py, ListElements.py, MultilanguageData.py, InlineTextElements.py, LanguageDataModel.py

### Issues Created:
- `docs/requirements/issues/missing-classes-chapters.md` - TraceableTable
- `docs/requirements/issues/missing-classes-msrquery.md` - MsrQueryResult

### Verification:
```bash
# All return 0:
grep -r 'from armodel\.models' src/armodel/v2/models/M2/ | wc -l
grep -r '^from \.\.' src/armodel/v2/models/M2/ | wc -l
grep -r 'if TYPE_CHECKING:' src/armodel/v2/models/M2/ | wc -l
grep -r 'import \*' src/armodel/v2/models/M2/ | wc -l
```

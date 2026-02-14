# V2 Coding Rules Todo

## Completed ✅

### Todo Document Reorganization (2026-02-14)
- Restructured document with dated sections for better tracking
- Committed and pushed reorganization to feature branch
- 12 insertions(+), 59 deletions(-)

### Quality Fixes for GitHub Workflow (2026-02-14)
- Fixed 2,896 Ruff whitespace issues across V2 models
- Created feature branch: feature/v2-quality-fixes-2026-02-14
- Created GitHub issue #464: https://github.com/melodypapa/py-armodel/issues/464
- Created PR #465: https://github.com/melodypapa/py-armodel/pull/465
- Changes: 4,638 insertions(+), 3,993 deletions(-) across 35 files

### V2 Coding Rules Compliance (2026-02-12)

#### All Violations Fixed:
- **180 V1 imports** → converted to V2 imports
- **0 relative imports** (CODING_RULE_V2_00001)
- **0 TYPE_CHECKING blocks** (CODING_RULE_V2_00002)
- **206/206 __init__.py files with __all__** (CODING_RULE_V2_00003)
- **0 wildcard imports** (CODING_RULE_V2_00012)

#### Files Modified:
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

#### Issues Created:
- `docs/requirements/issues/missing-classes-chapters.md` - TraceableTable
- `docs/requirements/issues/missing-classes-msrquery.md` - MsrQueryResult

#### Verification:
```bash
# All return 0:
grep -r 'from armodel\.models' src/armodel/v2/models/M2/ | wc -l
grep -r '^from \.\.' src/armodel/v2/models/M2/ | wc -l
grep -r 'if TYPE_CHECKING:' src/armodel/v2/models/M2/ | wc -l
grep -r 'import \*' src/armodel/v2/models/M2/ | wc -l
```

---

## Pending 📋

### V2 Model Enhancements
- [ ] Complete missing class implementations (refer to missing-issues documents)
- [ ] Add type annotations to improve MyPy compliance
- [ ] Improve test coverage for V2 models

### Documentation
- [ ] Update V2 migration guide with latest patterns
- [ ] Add examples of common V2 usage patterns

### Quality Improvements
- [ ] Reduce MyPy errors from 6348 to <1000
- [x] Eliminate trailing whitespace issues (completed 2026-02-14, 2,896 fixes)
- [ ] Resolve duplicate module errors

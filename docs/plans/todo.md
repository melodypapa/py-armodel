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

---

## In Progress 🔄

### Quality Fixes for GitHub Workflow (2026-02-14)

**Status**: Quality gate analysis completed, awaiting user decision

#### Issues Found:
1. **Ruff**: 8,509 trailing whitespace errors (auto-fixable with `ruff check --fix`)
2. **MyPy**: Critical error - duplicate module in `src/armodel/v2/models/M2/AUTOSARTemplates/CommonStructure/Timing/TimingConstraint/__init__.py`
3. **Flake8**: 30,535 errors (mostly in .venv/ and build/ directories, not source code)

#### Next Steps:
- [ ] Fix Ruff whitespace issues: `ruff check --fix src/armodel/v2/models/`
- [ ] Resolve MyPy duplicate module error in TimingConstraint
- [ ] Re-run quality checks
- [ ] Create GitHub issue for changes
- [ ] Create feature branch
- [ ] Commit changes
- [ ] Push to GitHub
- [ ] Create pull request

#### Modified Files (from git status):
```
M  .iflow/agents/v2-model-refactor.md
A  docs/requirements/issues/missing-classes-2026-02-14.md
M  reports/v2_validation_report.md
M  scripts/check_v2_deviation.py
M  src/armodel/v2/models/M2/AUTOSARTemplates/AdaptivePlatform/PlatformModuleDeployment/CryptoDeployment.py
M  src/armodel/v2/models/M2/AUTOSARTemplates/AdaptivePlatform/PlatformModuleDeployment/Firewall.py
M  src/armodel/v2/models/M2/AUTOSARTemplates/AdaptivePlatform/PlatformModuleDeployment/IntrusionDetectionSystem.py
M  src/armodel/v2/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py
M  src/armodel/v2/models/M2/AUTOSARTemplates/CommonStructure/SwcBswMapping.py
M  src/armodel/v2/models/M2/AUTOSARTemplates/EcuResourceTemplate/HwElementCategory.py
M  src/armodel/v2/models/M2/AUTOSARTemplates/EcuResourceTemplate/__init__.py
M  src/armodel/v2/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/ElementCollection.py
M  src/armodel/v2/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/GeneralAnnotation.py
M  src/armodel/v2/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/Identifiable.py
M  src/armodel/v2/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/PrimitiveTypes.py
D  src/armodel/v2/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/Referrable.py
M  src/armodel/v2/models/M2/AUTOSARTemplates/SystemTemplate/RteEventToOsTaskMapping.py
M  src/armodel/v2/models/M2/MSR/AsamHdo/ComputationMethod.py
M  src/armodel/v2/models/M2/MSR/DataDictionary/SystemConstant.py
M  src/armodel/v2/models/M2/MSR/Documentation/BlockElements/OasisExchangeTable.py
M  src/armodel/v2/models/M2/MSR/Documentation/BlockElements/RequirementsTracing.py
M  src/armodel/v2/models/M2/MSR/Documentation/BlockElements/__init__.py
M  src/armodel/v2/models/M2/MSR/Documentation/Chapters.py
M  src/armodel/v2/models/M2/MSR/Documentation/MsrQuery.py
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
- [ ] Eliminate trailing whitespace issues
- [ ] Resolve duplicate module errors

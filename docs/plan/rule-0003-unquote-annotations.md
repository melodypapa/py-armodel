# Plan: Remove Quoted Annotations Repo-wide (Rule 0003)

- Status: **Not started** — plan only, no code changes beyond the `PrimitiveTypes.py` precedent
- Written: 2026-10-14
- Triggered by: the `SymbolString` sync (Group21 row) — `PrimitiveTypes.py` was given
  `from __future__ import annotations` and its 9 quoted setter returns unquoted
- Related rules: **Rule 0003** (bare-name annotations, never quoted), Rule 0005
  (runtime-cycle-breaker imports), Rule 0022 (`__init__` member annotations)
- CI: `python-package.yml` runs a **`["3.8", "3.9", "3.10", "3.11", "3.12", "3.13"]`**
  matrix, so 3.8 behaviour is a hard gate, not a nicety

## 1. Summary

Rule 0003 requires annotations to be **bare names, never quoted strings**, at every
position (top-level *and* nested like `Optional["Foo"]`). Its stated reason is that on
Python 3.8 a quoted annotation under PEP 563 is stored with its quote characters intact,
so `typing.get_type_hints()` returns an unresolved `ForwardRef` instead of the class
(bpo-39291).

`PrimitiveTypes.py` is now compliant (future import added, 9 quotes removed). The other
**94 files carry 1045 quoted annotations** and are all still missing the future import,
which is the *reason* their quotes are load-bearing rather than a violation today.

After `PrimitiveTypes.py`, an AST survey (docstrings excluded) finds
**0 quoted annotations in any module that already has the future import** — i.e. no
outstanding Rule 0003 quote violation exists in `src/armodel` right now. This plan is
about removing the *workaround* (and the 3.8 latent risk it carries), not about fixing a
live violation.

## 2. Current inventory

| Bucket | Files | Annotations | Note |
|---|---:|---:|---|
| Model modules (`src/armodel/models/**`) | 89 | ~1010 | in scope for Rule 0003 pins |
| `data_models/ecuc/os.py` | 1 | 90 | largest single file |
| `transformer/abstract.py` | 1 | 1 | **live bug — see §3** |
| `validation/validator.py` | 1 | 1 | |
| `parser/arxml_parser.py` | 1 | 12 | 10 are arg annotations |
| `writer/arxml_writer.py` | 1 | 9 | 8 are arg annotations |
| **Total** | **94** | **1045** | 0 currently in future-import modules |

Position split: **1019 return annotations**, **26 in nested/arg/assign positions**
(`Optional["OsTask"]`, `event: "TDEventCom"`, `self.occurrenceExpression:
"Optional[TDEventOccurrenceExpression]"`). The nested ones are the form Rule 0003 calls
out as having broken the 3.8 CI job, so they must go too.

Only **1 of 94** files uses `TYPE_CHECKING` (`transformer/abstract.py`). The other 93
import every annotated name at runtime, so the Rule 0003 runtime-globals precondition is
already satisfied for them.

Largest files (`data_models/ecuc/os.py` 90, `AdaptivePlatform/.../Firewall` 72,
`MSR/Documentation/BlockElements/Figure.py` 51, `SystemTemplate/InstanceRefs.py` 40) are
mechanical bulk; the interesting cases are the handful in §3.

## 3. Live bug to fix first (independent of the quote work)

`src/armodel/transformer/abstract.py:15` annotates `root: "AUTOSAR"` while `AUTOSAR` is
imported **only** under `if TYPE_CHECKING:`. Verified on 3.13:

```
typing.get_type_hints(AbstractTransformer.remove)
→ NameError: name 'AUTOSAR' is not defined
```

`AUTOSAR` is not a runtime global of that module (`hasattr(mod, 'AUTOSAR') is False`).
This is Rule 0003's runtime-globals requirement failing **today**, on every Python
version, and it is the exact bpo-39291 shape the rule warns about. No test currently
covers it, which is why it survived.

Fix per Rule 0003 + the repo's established cycle-breaker pattern (see
`EthernetTopology.py:8085`, `ArObject.py:5303`): move the import to the **bottom** of the
module with `# noqa: E402` so the name is a module global once the module finishes
loading. Note `AbstractTransformer` is not a model class and has no 9-step sync row —
this is a small standalone fix, not a spec sync.

## 4. Per-module procedure

For each file, in one commit (or one small batch of related files):

1. **Confirm the module lacks the future import** (`from __future__ import annotations`).
   If it already has one, just unquote — that combination is a real Rule 0003 violation
   and should have been caught earlier.
2. **Audit runtime globals.** For every name appearing in a de-quoted annotation, confirm
   it is importable at runtime in that module. Red flags: `TYPE_CHECKING`-only imports,
   `if TYPE_CHECKING` blocks, names defined *after* the class that reference the class
   itself. If a name is not a runtime global, apply the bottom-of-module cycle-breaker
   import (Rule 0005) rather than leaving a quote.
3. **Add the future import** as the first statement after the module docstring:
   ```python
   from __future__ import annotations
   ```
   Keep it above all other imports (it must precede any code it applies to).
4. **Unquote.** Strip the quotes from the annotation only — never from a docstring. A
   regex on source text is unsafe here; use `ast` to locate annotations, or a targeted
   rewrite per line. Watch for:
   - `-> "X"` → `-> X`
   - `Optional["X"]` → `Optional[X]`
   - `self.x: "Optional[Y]" = None` → `self.x: Optional[Y] = None` (the whole annotation
     is quoted — unquoting only `Optional[Y]` would leave `"Optional[Y]"` invalid)
5. **Run the verification battery** (§5). Stop on any failure; do not batch past a red.

### Batch order (small → large, risk first)

| Batch | Scope | Why first |
|---|---|---|
| 1 | `transformer/abstract.py` (§3) + the other ≤2-annotation files | live bug; tiny, fast confidence |
| 2 | `parser/arxml_parser.py`, `writer/arxml_writer.py` | nested arg-annotation form; highest 3.8 exposure |
| 3 | the ~30 files with 3–15 annotations | bulk, low individual risk |
| 4 | the 11 files with >15 annotations | bulk, larger diffs |
| 5 | `data_models/ecuc/os.py` (90) + `AdaptivePlatform/.../Firewall` (72) | largest; isolate last |

## 5. Verification (per batch)

All must be green before the batch is committed:

```bash
uv run pytest tests/ -q --no-cov          # full suite; expect 0 failed
uv run ruff check src tests scripts       # import order (I001) will fire on the new import
uv run black --check <touched files>      # the new import must be black-clean
uv run mypy                              # must stay at the known baseline
uv run python .agents/skills/sync-autosar-class/audit_class.py <Class>
```

Plus the two annotation-specific gates:

- **Re-run the AST survey** — the count of quoted annotations must drop by exactly the
  batch size, and must reach **0** when the last batch lands. Any residue means a quote
  was missed or a docstring got mangled.
- **3.8 verification.** `requires-python = ">=3.8"` and CI tests 3.8. The quoted-annotation
  `ForwardRef` failure is 3.8-specific: on 3.9+ `get_type_hints` double-resolves and masks
  it. So **a green local run on 3.13 is not sufficient evidence** — each batch must either
  run the suite under 3.8 locally (`uv python install 3.8` then a 3.8 venv) or land and let
  the CI 3.8 job confirm before the next batch starts.

Baseline to compare against (measured 2026-10-14, pre-existing, unrelated to this work):
`pytest` 26245 passed / 0 failed · `ruff` clean · `mypy` **13 errors in 3 files**
(`parser/connector_xlsx_parser.py`, `parser/excel_parser.py`, `report/os_export.py`) ·
`black --check src tests` **90 files would be reformatted** (pre-existing drift; do not
try to fix it here, and never reformat a file you are not otherwise touching).

## 6. Risks

| Risk | Mitigation |
|---|---|
| **3.8 `ForwardRef` masked locally.** The whole point of the change is invisible on 3.9+. | Gate each batch on a real 3.8 run (or CI) before starting the next. |
| **`ruff I001` import-order failures.** A new top-of-file import is a new ordering constraint. | Expected; run `ruff check` per batch and fix ordering, don't disable the rule. |
| **Cycle-breaker import ordering.** Bottom-of-module imports need `# noqa: E402`. | Follow the existing documented pattern; keep the comment explaining why. |
| **Accidental docstring edits.** A text-level unquote can corrupt prose like `Optional["X"]: The ...` in a `Returns:` block. | Use `ast`, not regex, to select annotation nodes. (This already produced 3 false positives during the survey — `ModeDeclaration.py`, `Identifiable.py`, `Chapters.py`.) |
| **Untested annotation surface.** 299 test files / 2545 `get_type_hints` pins depend on these annotations resolving. | Full suite per batch. |
| Scope creep into unrelated pre-existing lint/type debt. | Baseline numbers in §5 are fixed; only ever compare, never "fix" the 13 mypy errors or 90 black files here. |

## 7. Definition of done

- [ ] `transformer/abstract.py` `get_type_hints(AbstractTransformer.remove)` returns
      without `NameError`, and a regression test covers it
- [ ] AST survey reports **0 quoted annotations** in `src/armodel`
- [ ] `pytest` 0 failed · `ruff` clean · `mypy` at the 13-error baseline ·
      `black` unchanged on the repo-wide 90
- [ ] 3.8 CI job green (or a local 3.8 run recorded in the commit message)
- [ ] Rule 0003 in `.agents/skills/sync-autosar-class/rules.md` left as-is — it is
      already correct; this plan brings the code up to it

## 8. Out of scope

- The pre-existing 13 mypy errors and 90 black-formatting files (unrelated debt).
- Any model class sync / 9-step workflow — this is a mechanical refactor, not a spec sync,
  so it needs no `# Spec verified:` stamps and no `docs/plan/sync-todo/` rows.
- `docs/examples/method_deviation_by_class.md` — no spec deviation is involved.

## 9. Reference — the completed precedent

`PrimitiveTypes.py`, 2026-10-14 (the `SymbolString` row): future import added, 9
self-returning setters unquoted (`Identifier`/`CIdentifier` `setBlueprintValue` +
`setNamePattern`, `Limit.setIntervalType`, `Ref` `setBase` + `setBlueprintValue` +
`setIndex`, `SymbolString.setNamePattern`). Verified: every affected
`typing.get_type_hints(...)['return']` still resolves to the concrete class; the module has
no `TYPE_CHECKING` block, so all annotated names are runtime globals; full suite 26245
passed / 0 failed; ruff + black clean; mypy at the 13-error baseline; `audit_class.py`
PASS. Recorded in the `SymbolString` tracker entry and the Group21 row's Step 8 note.

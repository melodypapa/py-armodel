# Group16 Remaining-16 Re-sync Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or
> superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Bring the **16 remaining `[ ]` rows** of `docs/plan/sync-todo/Group16.md` to a compliant, stamped state
by re-running the `sync-autosar-class` 9-step workflow for each, one class per isolated subagent session.
This is the follow-on to `2026-10-03-group16-issue-class-resync.md` (the 11 issue classes, now all done).

**Origin:** a read-only rules audit (2026-10-03) of the 16 rows that had "Steps 1–8 `[x]`" claims from earlier
sessions but **no stamp**. That claim proved false on the 11 already re-synced (e.g. `TimeSyncServerConfiguration`
had zero changes despite an all-`[x]` checklist), so **no `[x]` claim is trusted here** — every class gets a full
9-step re-run.

**Architecture:** identical to the previous plan — one isolated subagent per class runs Steps 1–9a; the orchestrator
independently re-verifies the 9a battery, presents the **Step 9b gate** (user confirmation), writes the marker only on
confirmation, then commits `feat:` + `docs:` (row flip + `regen_sync_todo.py --write/--check`).
The persistent queue is `docs/plan/sync-todo/Group16.md` — never the conversation.

**Tech Stack:** Python 3.8-compatible typing (`Optional[T]` / `List[T]`), pytest, ruff, Black (line-length 200),
in-repo skill `.agents/skills/sync-autosar-class/`.

## Status

**Progress: 2 of 16 done (G16-1, G16-2) — 14 rows remain (G16-3…G16-16).** Queue state at audit time:
15 `[x]` / 14 `[ ]` in `docs/plan/sync-todo/Group16.md`.

| # | Class | Severity | Defect(s) | Status |
|---|---|---|---|---|
| G16-1 | `EthernetPriorityRegeneration` | HIGH | reader missing base `readReferrable`; checklist scatter; stale suffix; bare-`int` test | ✅ `a513bd3ec` / `c5d19e82c` |
| G16-2 | `TimeSynchronization` | HIGH | Rule 0001.6 `set/get` for a `Referrable` child; checklist scatter; mirror test pins wrong shape | ✅ `f4a1df5bc` / `55168dad8` |
| G16-3 | `MacMulticastGroup` | MED | `MacAddressString` type drift; checklist scatter; stale suffix | pending |
| G16-4 | `GenericTp` | MED | `String` type drift ×2 attrs; checklist scatter; stale suffix | pending |
| G16-5 | `TcpTp` | MED | `naglesAlgorithm` Boolean drift; checklist scatter (16 rows); stale suffix | pending |
| G16-6 | `DoIpEntity` | MED | checklist scatter | pending |
| G16-7 | `TpPort` | MED | checklist scatter; `Tags:` tail kept; bare-`int` test | pending |
| G16-8 | `VlanConfig` | MED | checklist scatter; stale suffix | pending |
| G16-9 | `UdpTp` | MED | checklist scatter; stale suffix | pending |
| G16-10 | `RequestResponseDelay` | LOW | stale suffix only (single block already correct) | pending |
| G16-11 | `TcpOptionFilterSet` | LOW | stale suffix; mirror test lacks `[]` default assertion | pending |
| G16-12 | `RuntimeAddressConfigurationEnum` | LOW | **R4.3.1 fallback**; checklist `(no methods)` vs `[x] __init__` contradiction | pending |
| G16-13 | `IpAddressKeepEnum` | LOW | checklist contradiction | pending |
| G16-14 | `Ipv6AddressSourceEnum` | LOW | checklist contradiction; md literal cell is `router Advertisement` (space) vs code `routerAdvertisement` — user call (Step C) | pending |
| G16-15 | `Ipv4AddressSourceEnum` | LOW | checklist contradiction | pending |
| G16-16 | `PduCollectionSemanticsEnum` | LOW | checklist contradiction | pending |

## Audit merge — independent read-only audit of all 29 rows (2026-10-03)

A second audit ran over **all 29** Group16 rows (the 16 here + the 13 already stamped) against
`.agents/skills/sync-autosar-class/rules.md`, with scripted checks (AST structure, spec-table cross-check over the
markdown corpus, reader/writer coverage, reader/writer helper type vs spec `Type`). It **corroborated this plan's
G16-3/G16-4/G16-5 defects independently** and surfaced the queue-level items below, which this plan did not track.
The audit changed no tracked file.

**Verified clean — do not re-litigate:**
- 6-column checklist + `# Columns:` line + release column; checklist rows == methods in source order; no
  `T | None`/`list[T]`; PEP 526 only; `__init__` has no docstring; blank line between attribute blocks;
  spec `Package` tail matches the source file; class docstrings == spec `Note` verbatim; attribute set/order/quota
  match the table; most-derived base correct; 1:1 mirror test for every row.
- **Reader/writer coverage claims: 0/29 findings** — every `[x] reader` / `[x] writer` row has a live
  parser/writer call site.
- Gates at audit time: `ruff check` + `black --check -l 200` clean on the 6 Group16 source files;
  `scripts/eval_skill_static_checks.py` all-pass (no Group16 class in the Rule 0023 legacy list);
  `scripts/regen_sync_todo.py --check` up to date; `tests/test_armodel/models/test_member_annotations.py` 3 passed;
  **full unit suite 17408 passed / 0 failed** (`.venv/bin/python -m pytest tests/test_armodel/ -q --no-header`, 44 s).
- Row↔marker consistency: 15 `[x]` rows ↔ markers present with the right release; no `[x]` row without a hash.

**Queue-level findings — owner: orchestrator (docs-only; not a per-class subagent task):**

| # | Rule | Finding | Action |
|---|---|---|---|
| Q1 | 0017.4 | 12 of the 14 pending rows' Step 9 line reads *"9b deferred to batch confirmation (user instruction)"* — the exact placeholder 0017.4 forbids ("a deferred-confirmation note is not the confirmation"). `SdServerConfig`'s Step 9 line (row already `[x]`) carries **both** "9b CONFIRMED … marker written" **and** "9b deferred to batch confirmation". | At each 9b gate write the real confirmation text; delete the leftover `deferred` clause from `SdServerConfig` (docs-only, any time). |
| Q2 | 0014 | **16 classes have no `## <Class>` entry** in `docs/examples/method_deviation_by_class.md`: all 14 pending rows **plus the 2 stamped shapers** `CouplingPortAsynchronousTrafficShaper` / `CouplingPortCreditBasedShaper`. The other 13 stamped rows all have entries (mostly "No deviations"). | Step 8 must create the entry — make it an explicit sub-item of every "Steps 1–9a" step below. |
| Q3 | 0017.2 | `GenericTp` / `TcpTp` / `UdpTp` rows cite commit **`26c26b088`, which does not exist** (6 occurrences, Group16.md L232-233 / L244-245 / L256-257). The real commit is **`26c80b088`**. Every other hash in the queue resolves. | Correct the typo (docs-only) when those rows flip. |
| Q4 | 0016.7 | The 2 stamped shaper rows (Group16.md L154, L159) have **no 9-step sub-checklist at all** (0 `Step N —` lines); every other row has 9. | Restore the 9-step block with Step 9 recording the confirmed 9b. |
| Q5 | 0016.7 | The 5 pending enum rows each carry **duplicate, contradictory** queue steps: `- [—] Step 5/6 — N/A standalone enum` **and** `- [x] Step 5/6 …` (10 stray lines: L22-23, 36-37, 50-51, 64-65, 270-271). | Drop the `[—] N/A` pair; the AREnum adaptation belongs *inside* the step text, not as a second row. |
| Q6 | 0017.1 | The only 9a evidence on all 14 pending rows is dated **2026-09-28 ("6771 passed / 0 failed battery")**; the suite is now 17408 tests and the tree has moved a long way since (569 commits after 2026-09-28, 71 of them today). | Treat that evidence as void — every row's 9a is re-run in this pass. |
| Q7 | 0017.1 | Stale drift notes on the 2 shaper rows say the `# XSD verified` marker "is intentionally **retained** … must still be present", but the row headers **and** the source (`EthernetTopology.py:227`, `:308`) read `# Spec verified: R23-11`. | Rewrite those notes to match the current state. |

**Ruled out by the audit (do not "fix"):**
- `TpPort.dynamicallyAssigned`, `TcpTp.keepAlives`, `SocketConnectionBundle.pathMtuDiscoveryEnabled`
  — `getChildElementOptionalBooleanValue` **is** the correct helper: it returns a `Boolean`
  (`parser/abstract_arxml_parser.py:337`), not a raw `bool` and not an `ARLiteral`.
- No `TcpOptionFilterSetParam` type exists in spec or code. `TcpOptionFilterSet.tcpOptionFilterLists`
  (Table 6.122) and its sibling `TcpOptionFilterList.allowedTcpOptions` (spec `allowedTcpOption`,
  Table 6.123, `PositiveInteger *`) are correct — the plural is the Rule 0001.5 `s` suffix.
- `Ipv6AddressSourceEnum.linkLocal_doip` / `Ipv4AddressSourceEnum.autoIp_doip` literal fixes hold.
- An earlier "row `[ ]` but marker present" flag on `EthernetPriorityRegeneration` / `TimeSynchronization` was an
  artifact of a stale status snapshot in the audit script; both rows are `[x]` with 9b CONFIRMED.

**Pending user decision (do not act unilaterally):** the `Tags:` question — see G16-7 Step B and the
`Tags:` note under G16-13…G16-16. Rule 0012.2.5.2 says drop the `Tags:`/`Stereotypes:` tail, but
**171 of 172 stamped enums** and **29 stamped `SystemTemplate` classes** keep theirs. Confirm the intended scope
before stripping.

---

## Global Constraints

- **Work only in the `.g16-wt` worktree.** The main checkout `/Users/ray/Workspace/py-armodel` belongs to a
  concurrent session — never edit it, never `git checkout`/`switch`/`commit` there.
- **Every command needs the `PYTHONPATH` prefix** (the shared venv's editable `.pth` points at the main checkout):
  `cd /Users/ray/Workspace/py-armodel/.g16-wt && PYTHONPATH=/Users/ray/Workspace/py-armodel/.g16-wt/src /Users/ray/Workspace/py-armodel/.venv/bin/python -m pytest ...`
  — *this applies to the **main checkout's** interpreter only.* The worktree's own `.venv` (Python 3.13.11,
  pytest/ruff/black installed via `uv sync --extra pytest --extra lint`) resolves `armodel` to
  `/Users/ray/Workspace/py-armodel/.g16-wt/src/armodel/__init__.py` (verified), so plain
  `.venv/bin/python -m pytest …` run from the worktree needs no prefix.
- **`uv run` is unusable** (sandbox cannot write `~/.cache/uv`). **`flake8` is not installed** — ruff +
  `black --check` are the lint gates. **`pypdf` is missing** → `pdf_page.py` fails; take `p.NN` from the existing
  `# Spec:` line / the queue, or use the macOS PDFKit fallback (below).
- **PDF page fallback (verified):** `/usr/bin/python3` + Quartz PDFKit reads the corpus PDFs. Calibrate against a
  known citation (e.g. `Table F.38: CouplingPortRoleEnum` → printed `p.2013` = pageIndex+1) before trusting a page.
- **Worktree-integrity watch:** during the 11-class run, an external process staged **17 spurious
  `docs/superpowers/**` deletions**. If `git status` shows staged `D` entries under `docs/superpowers/` that no
  commit made, restore them with
  `git restore --source=HEAD --staged --worktree docs/superpowers/` and report — **never commit them**.
- **One class per subagent session** (Rule 0017.1), chained per Rule 0017.5. **9b stays mandatory for every class**
  — never self-stamp from subagent evidence.
- **Never collapse a finished todo row** (Rule 0024 removed); a finished row keeps its 9-step sub-checklist.
- **Commits per class:** one `feat: <ClassName> synced.`, then one
  `docs: mark <ClassName> done in Group16 queue + regen reports` (must run `python3 scripts/regen_sync_todo.py
  --write` and pass `--check`; the regen takes ~2.5 min).
- **Scope discipline:** fix the class's *own* violations; report other classes' defects in the tracker/queue.
- Resolved user decisions (binding):
  - **Rule 0001.4 `Mult=1`:** keep `Optional[T]`, record an accepted deviation (repo precedent 106:14).
  - **`# Spec:` suffix:** use the canonical form `# Spec: <PDF>, Table X.Y, p.NN` — **no trailing `(R23-11)` /
    `(R4.3.1)` token** (batch standard set during the 11-class run; 227 legacy occurrences exist, don't fix those).
  - **Checklist layout:** a single 6-column block **before `__init__`**; never rows scattered inside `__init__`.
  - **Step 8 = tracker entry (Q2), not just a note:** every class in this plan must end its run with a
    `## <ClassName>` heading (backticked or bare) in `docs/examples/method_deviation_by_class.md` — a
    "No deviations" table is enough, but *absent* is a Rule 0014 violation. All 14 pending rows are absent today.
  - **Step 9 text (Q1):** write the confirmation as `**9b CONFIRMED <date> (user)**` the moment it is given —
    never the `9b deferred to batch confirmation` placeholder (Rule 0017.4), and never leave both on one line.
  - **Queue hygiene (Q3/Q4/Q5/Q7)** — broken commit hash, missing shaper sub-checklists, duplicate enum
    `Step 5/6 — N/A` lines, stale shaper drift notes: orchestrator docs-only fixes, done in the same commit as
    the related row flip or standalone.
- Never edit integration fixture `.arxml` files (Rule 0019).

## Environment (already done — do not redo)

- Worktree `/Users/ray/Workspace/py-armodel/.g16-wt` on branch `feature/g16-remaining-resync` (re-created off `main`
  `73a2f14d3` on 2026-10-03 after `feature/g16-issue-classes-sync` merged as PR #913 and the old worktree was
  retired); hidden via a `.g16-wt/` entry in `.git/info/exclude` (local-only). Worktree venv: Python 3.13.11,
  `black` pinned 24.8.0 (26.x false-flags ~35 untouched files).
- `tests/integration_tests/custom_files/` (gitignored) present so round-trip fixtures resolve.
- Sanity check: `PYTHONPATH=.g16-wt/src .venv/bin/python -c "import armodel; print(armodel.__file__)"` must print
  the `.g16-wt` path.
- **Known baseline:** the 8 `*_SystemMapping.arxml` `file_compare` integration fixtures fail identically on pristine
  HEAD → treat as **delta 0**; anything else new is a real failure.

### Completed passes — patterns to reuse

- **Reader base-helper gap:** `readXxx` must call its direct base's reader helper when the writer calls the base
  writer. Fixed twice now: `SocketConnectionBundle` (missing `readReferrable`) and
  `EthernetPriorityRegeneration` (missing `readReferrable`). Symptom (RED): `getChecksum()`/`getTimestamp()` are
  `None` after a round-trip.
- **Type drift:** the reader/writer must use the spec-typed leaf helper (`getChildElementOptionalString` /
  `…BooleanValue` / `…PositiveInteger` / a typed ARLiteral-subclass construction), never the generic
  `getChildElementOptionalLiteral` when the field is a spec type — otherwise the field holds a plain `ARLiteral`.
- **Rule 0001.6:** a `0..1 aggr` child whose spec `Base` lists `Referrable`/`Identifiable` needs
  `createXxx(short_name)` + `getXxx()`; a plain `ARObject` child keeps `setXxx`/`getXxx`.
- **Checklist layout:** rebuild as one 6-column block before `__init__`; the member comments inside `__init__`
  become the verbatim spec `Note`s.
- **`createTimeXxx` semantics** (Rule 0004): return the existing element when the short name already exists, else
  construct + assign + return it.

---

### G16-1: `EthernetPriorityRegeneration` — ✅ DONE

- feat `a513bd3ec`, docs `c5d19e82c`. Stamped `# Spec verified: R23-11`.
- Fixed: reader base-helper gap; checklist rebuilt; suffix; typed-primitive test.
- Spec: R23-11 Table 3.74, p.128; `EthernetTopology.py` ~L506; `Base = ARObject , Referrable`.

---

### G16-2: `TimeSynchronization` — ✅ DONE

- feat `f4a1df5bc`, docs `55168dad8`. Stamped `# Spec verified: R23-11`.
- All original Steps A–F landed: `setTimeSyncServer` → **`createTimeSyncServer(short_name)`** + `getTimeSyncServer`
  (Rule 0001.6; duplicate short name returns the existing child, Rule 0004); parser reads into
  `sync.createTimeSyncServer(self.getShortName(server_element))` (`arxml_parser.py:9867`); checklist rebuilt as one
  top block; ` (R23-11)` suffix dropped; mirror + parser/writer tests rewritten; `## TimeSynchronization` entry
  added to the deviation tracker (Rule 0014).
- Spec: R23-11 Table 6.145, p.469; `EthernetTopology.py` ~L2924; `Base = ARObject` → `__init__(self)`.
- Post-commit audit cross-check: row `[x]` ↔ marker `R23-11` ↔ live reader coverage for `createTimeSyncServer`;
  suite 17408 passed.

### G16-3: `MacMulticastGroup` — MED

**Files:** `EthernetTopology.py` L36 (annotation at L52); parser `readMacMulticastGroup` (`arxml_parser.py:10594`,
read at `:10596-10600`); writer `writeMacMulticastGroup` (`arxml_writer.py:11280`, literal write at `:11284`);
mirror `test_MacMulticastGroup.py`.

- [ ] **Step A:** `macMulticastAddress` is spec `MacAddressString` but the reader/writer use the generic literal
      pair → produce a plain `ARLiteral`. Construct the typed `MacAddressString` on read (mirror the
      `Ipv4Configuration` fix) and keep the writer's `setChildElementOptionalLiteral` (it accepts ARLiteral
      subclasses) — or use the typed writer helper if one exists.
      **Audit evidence:** `EthernetTopology.py:52` declares `self.macMulticastAddress: Optional[MacAddressString]`,
      but `arxml_parser.py:10596-10600` reads it with `getChildElementOptionalLiteral` (returns `ARLiteral`) and
      `arxml_writer.py:11284` writes it with `setChildElementOptionalLiteral`. `MacAddressString(ARLiteral)` lives
      at `PrimitiveTypes.py:1263`, so the field never holds its declared type. (The audit's helper scan keyed on
      *primitive* spec types — `String`/`Boolean`/`Integer` — so it caught G16-4/G16-5 but not this one; the
      same defect class.)
- [ ] **Step B:** checklist rows inside `__init__` (L49–50) → single top block; drop the ` (R23-11)` suffix
      (`# Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.48, p.104`; `Base = ARObject , Identifiable ,
      MultilanguageReferrable , Referrable`).
- [ ] **Step C:** Steps 1–9a as prescribed.

### G16-4: `GenericTp` — MED

**Files:** `EthernetTopology.py` L3626; parser `readGenericTp` (~L10051); writer (~L10071); mirror test.

- [ ] **Step A:** `tpAddress`/`tpTechnology` are spec `String` but read via `getChildElementOptionalLiteral` → use
      `getChildElementOptionalString`/`setChildElementOptionalString` (Rule 0013.2/0001.3).
      **Audit evidence (independent confirmation):** spec Table 6.126 rows are `tpAddress | String | 0..1 | attr`
      and `tpTechnology | String | 0..1 | attr`; model declares `Optional[String]` (`EthernetTopology.py:3645`,
      `:3650`); parser `arxml_parser.py:10049-10050` and writer `arxml_writer.py:10071-10072` both use the
      *literal* pair. `String(ARLiteral)` (`PrimitiveTypes.py:323`) means the field ends up holding a plain
      `ARLiteral`, never a `String`.
      **Table-selection trap:** Table 6.126's body renders **above** its caption — body `md L12137-12145`,
      caption `Table 6.126: GenericTp` at `L12147`, with Table 6.127's body immediately below. Anchor on the
      `| Class | GenericTp |` header row, not the caption.
- [ ] **Step B:** checklist rows inside `__init__` (L3639–3645) → single top block; drop the ` (R23-11)` suffix
      (`# Spec: … Table 6.126, p.459`).
- [ ] **Step C:** Steps 1–9a as prescribed.

### G16-5: `TcpTp` — MED

**Files:** `EthernetTopology.py` L3786 (annotation at L3825); parser `readTcpTp` (keepAlives OK at
`arxml_parser.py:10042`, `naglesAlgorithm` literal helper at `:10043`); writer (`arxml_writer.py:10063-10064`);
mirror test.

- [ ] **Step A:** `naglesAlgorithm` is spec `Boolean` but read via `getChildElementOptionalLiteral` → use
      `getChildElementOptionalBooleanValue`/`setChildElementOptionalBooleanValue` (sibling `keepAlives` is correct).
      **Audit evidence (independent confirmation):** model declares `Optional[Boolean]`
      (`EthernetTopology.py:3825`); parser `arxml_parser.py:10043` + writer `arxml_writer.py:10064` use the
      *literal* pair. `Boolean(ARType)` (`PrimitiveTypes.py:567`) is **not** an `ARLiteral` subclass, so
      `getNaglesAlgorithm()` hands back an object whose `.value` is `str` where the declared type promises `bool`.
      The correct helper already exists and is typed: `getChildElementOptionalBooleanValue`
      (`parser/abstract_arxml_parser.py:337-346`) builds a `Boolean` and carries `timestamp` across —
      `keepAlives` at `arxml_parser.py:10042` is the working in-file model.
- [ ] **Step B:** all 8 accessor rows inside `__init__` (L3799–3835) → single top block; drop the ` (R23-11)` suffix
      (`# Spec: … Table 6.129, p.460`).
- [ ] **Step C:** Steps 1–9a as prescribed.

### G16-6: `DoIpEntity` — MED

**Files:** `EthernetTopology.py` L2687 (rows inside `__init__` at L2700–2701); reader `getDoIpEntity` (parser 9841);
writer `setDoIpEntity` (9892); mirror test.

- [ ] **Step A:** checklist rows inside `__init__` → single top block.
- [ ] **Step B:** Steps 1–9a as prescribed (spec R23-11 Table 6.150, p.471; `Base = ARObject` → `__init__(self)`).

### G16-7: `TpPort` — MED

**Files:** `EthernetTopology.py` L3698 (rows inside `__init__` at L3711–3717); reader (parser 10033–10034); writer
(10051–10052); mirror test.

- [ ] **Step A:** checklist rows inside `__init__` → single top block.
- [ ] **Step B:** `dynamicallyAssigned` keeps the `Tags: atp.Status=obsolete` tail in the inline comment/getter/
      setter docstrings → drop the `Tags:` tail (Rule 0012.2.5.2).
      **Scope note (audit, needs the user's call before Step B touches docstrings):** Rule 0012.2.5.2 names the
      **inline `__init__` comment** explicitly ("drop `Stereotypes:`/`Tags:` tail") → that part is unambiguous.
      For **docstrings** the same rule says "copied verbatim", and repo precedent keeps the tail:
      **171 of 172 stamped enums** and **29 stamped `SystemTemplate` classes** still carry `Tags:`. So: strip it
      from the inline comment, and confirm with the user whether the getter/setter docstrings lose it too — if it
      is dropped, record `atp.Status=obsolete` in the tracker entry (it is provenance, not decoration).
- [ ] **Step C:** mirror test passes a bare `int` (`setPortNumber(7)`) → typed `PositiveInteger`.
- [ ] **Step D:** Steps 1–9a as prescribed (spec R23-11 Table 6.133, p.461; `Base = ARObject`).

### G16-8: `VlanConfig` — MED

**Files:** `EthernetTopology.py` L3960 (rows inside `__init__` at L3973–3974); reader
`readEthernetPhysicalChannelVlan` (parser L10397); writer (L10476); mirror test.

- [ ] **Step A:** checklist rows inside `__init__` → single top block; drop the ` (R23-11)` suffix
      (`# Spec: … Table 3.50, p.106`).
- [ ] **Step B:** Steps 1–9a as prescribed.

### G16-9: `UdpTp` — MED

**Files:** `EthernetTopology.py` L3752 (rows inside `__init__` at L3765–3766); mirror test.

- [ ] **Step A:** checklist rows inside `__init__` → single top block; drop the ` (R23-11)` suffix
      (`# Spec: … Table 6.128, p.459`).
- [ ] **Step B:** Steps 1–9a as prescribed. Note `udpTpPort` → `TpPort` is a plain `ARObject` child ⇒ `setUdpTpPort`
      is correct (Rule 0001.6) — do NOT invent a factory.

### G16-10: `RequestResponseDelay` — LOW

**Files:** `ServiceInstances.py` L1964 (single block already correct at L1972–1976); reader (parser L10081–10082);
writer (L10098–10099); mirror test.

- [ ] **Step A:** drop the ` (R23-11)` suffix (`# Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.171, p.515`).
- [ ] **Step B:** Steps 1–9a as prescribed (spec R23-11 Table 6.171, p.515; `Base = ARObject`; both attrs
      `Optional[TimeValue]`). Family: siblings `SdServerConfig`/`InitialSdDelayConfig` are stamped — this is the
      family's last unstamped member.

### G16-11: `TcpOptionFilterSet` — LOW

**Files:** `TcpOptionFilterSet.py` L47 (single block correct at L55–57); mirror test.

- [ ] **Step A:** drop the ` (R23-11)` suffix (`# Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.122, p.457`).
- [ ] **Step B:** add a defaults/initialization assertion to the mirror test (`getTcpOptionFilterLists() == []`).
- [ ] **Step C:** Steps 1–9a as prescribed (spec R23-11 Table 6.122, p.457; `Base = ARElement`;
      `createTcpOptionFilterList` + `getTcpOptionFilterLists` are correct for the `Identifiable` child).
      Family: sibling `TcpOptionFilterList` is stamped — this is the last unstamped member.

### G16-12: `RuntimeAddressConfigurationEnum` — LOW, **R4.3.1 fallback**

**Files:** `EthernetCommunication.py` L24; mirror test.

- [ ] **Step A:** **no R23-11 table exists** (grep confirmed) — R4.3.1 `AUTOSAR_TPS_SystemTemplate.md` Table 6.121
      (md L7439) is the source ⇒ marker **`# Spec verified: R4.3.1`** and every checklist row's release column
      **`R4.3.1`** (Rule 0016.3 class-scoped fallback). `# Spec: AUTOSAR_TPS_SystemTemplate.pdf (R4.3.1),
      Table 6.121, p.320`.
- [ ] **Step B:** the checklist block asserts `# (no methods)` **and** carries `# [x] __init__` — remove the
      contradiction (keep the `__init__` row; drop the `(no methods)` line).
- [ ] **Step C:** Steps 1–9a as prescribed (AREnum adaptation: Steps 5/6 N/A; literals `none`/`sd` 1:1 with the
      `Literal` rows).
- [ ] **Step D (queue hygiene, Q5):** this row **and G16-13…G16-16** each carry a duplicate pair
      `- [—] Step 5/6 — N/A standalone enum` sitting *above* the real `- [x] Step 5/6 …` lines (10 stray lines at
      Group16.md L22-23, L36-37, L50-51, L64-65, L270-271). Drop the `[—]` pair when the row flips; keep the
      N/A rationale *inside* the step text. Docs-only, orchestrator.
- **Current `# Spec:` line is also the wrong shape:** it reads
  `R4.3.1/AUTOSAR_TPS_SystemTemplate.pdf, Table 6.121, p.320 (R4.3.1)` — Rule 0019's *multi-corpus* form, used for
  a single-corpus R4.3.1 fallback. Step A's target form is the Rule 0002 fallback template.

### G16-13: `IpAddressKeepEnum` — LOW

**Files:** `EthernetTopology.py` L2296 (contradiction at L2304–2305); mirror test.

- [ ] **Step A:** remove the `# (no methods)` vs `[x] __init__` contradiction.
- [ ] **Step B:** Steps 1–9a as prescribed (spec R23-11 Table 6.138, p.466; literals `forget`/`storePersistently`).
- [ ] **Step C — shared with G16-12/G16-14/G16-15/G16-16 (`Tags:` scope, user decision first):** all 5 pending
      enums keep the `Tags: atp.EnumerationLiteralIndex=…` / `Tags: atp.EnumerationValue=…` tail in their literal
      comments (verified for `RuntimeAddressConfigurationEnum`, `IpAddressKeepEnum`, `Ipv6AddressSourceEnum`,
      `Ipv4AddressSourceEnum`, `PduCollectionSemanticsEnum`). Rule 0012.2.5.2 says drop such tails, but
      **171 of 172 stamped enums** keep theirs — confirm the intended scope with the user before stripping;
      if dropped, the `atp.EnumerationLiteralIndex` / `xml.name` values go into the tracker entry.

### G16-14: `Ipv6AddressSourceEnum` — LOW

**Files:** `EthernetTopology.py` L2322 (contradiction at L2330–2331); mirror test.

- [ ] **Step A:** remove the checklist contradiction.
- [ ] **Step B:** Steps 1–9a as prescribed (spec R23-11 Table 6.140, p.467; 5 literals incl. `linkLocal_doip`).
- [ ] **Step C (spec-content, confirm before stamping):** the 5th literal's markdown cell is literally
      `router Advertisement` — with a space — at `autosar/R23-11/markdown/AUTOSAR_CP_TPS_SystemTemplate.md:12438`,
      while the code has `routerAdvertisement`. The other 4 literals match 1:1. This looks like a PDF-extraction
      artifact, but the row's own `linkLocal_doip` fix was made *md-primary* (Rule 0015), so **ask the user**:
      keep `routerAdvertisement` + record an accepted artifact deviation in the tracker entry, or rename the
      literal (and every consumer) to match the markdown cell.

### G16-15: `Ipv4AddressSourceEnum` — LOW

**Files:** `EthernetTopology.py` L2094 (contradiction at L2102–2103); mirror test.

- [ ] **Step A:** remove the checklist contradiction.
- [ ] **Step B:** Steps 1–9a as prescribed (spec R23-11 Table 6.137, p.465; 4 literals incl. `autoIp_doip`).

### G16-16: `PduCollectionSemanticsEnum` — LOW

**Files:** `ServiceInstances.py` L405 (contradiction at L413–414); mirror test.

- [ ] **Step A:** remove the checklist contradiction.
- [ ] **Step B:** Steps 1–9a as prescribed (spec R23-11 Table 6.165, p.490; literals `lastIsBest`/`queued`;
      Package `…::ServiceInstances`).

---

## Reported, not fixed (other classes' items — drain in their own passes)

These were surfaced during the audits and deliberately left alone (Rules 0004/0013.1):

- `EthernetCommunication.py` module-header comment cites stale R4.3.1 table ids for the siblings
  (`IPv6ExtHeaderFilterList` 6.129→6.121, `TcpOptionFilterSet` 6.130→6.122, `TcpOptionFilterList` 6.131→6.123).
- `SomeipSdServerServiceInstanceConfig` — misplaced stub in
  `GenericStructure/GeneralTemplateClasses/ArObject.py`, no parser/writer handler
  (`InitialSdDelayConfig.initialOfferBehavior` does not round-trip through it) — Rule 0001.10, own sync needed.
- `ProvidedServiceInstance.getSdServerConfig`/`setSdServerConfig` — untyped accessors (Rule 0001.3).
- `CouplingPortTrafficClassAssignment.priority` — `0..8` `attr` (Table 3.75), own sync row.
- `MacMulticastConfiguration` — `pass` stub queued in Group32; the `MAC-MULTICAST-CONFIGURATION` dispatch branch
  in `NetworkEndpoint`'s helper stays unimplemented until that child syncs.
- `.g16-wt/AGENTS.md` and `.g16-wt/CLAUDE.md` reference `tests/test_files/`, which does not exist in this worktree.
- **NEW (2026-10-03 audit) — `SocketConnectionBundle.udpChecksumHandling` reader drift (Rule 0013.2), stamped
  class:** the model declares `self.udpChecksumHandling: Optional[UdpChecksumCalculationEnum]`
  (`EthernetCommunication.py:233`, class at `:185`, marker `# Spec verified: R4.3.1` at `:192`), but
  `arxml_parser.py:9986` (`readSocketConnectionBundle`) reads it with `getChildElementOptionalLiteral` → the
  field holds a plain `ARLiteral`, never the declared enum. The sibling `SocketAddress` path does it correctly
  (`arxml_parser.py:10364-10366` builds `UdpChecksumCalculationEnum()` and copies the value). The writer side
  (`arxml_writer.py:10004`) is fine — `AREnum(ARLiteral)` (`PrimitiveTypes.py:269`), so the literal writer
  accepts it. Fixing it means a Rule 0017.1 drift re-open of an already-stamped row → **user decision**, not this
  plan's scope.
- **Cross-ref:** the queue-level items **Q1–Q7** in "Audit merge" above (broken commit hash, missing shaper
  sub-checklists, duplicate enum `Step 5/6` lines, 16 missing Rule 0014 tracker entries, stale shaper drift
  notes, void 9a evidence) are orchestrator docs-only fixes and are tracked there rather than repeated here.

## Notes for the next session

- The queue is `docs/plan/sync-todo/Group16.md`; **resume at G16-3 (`MacMulticastGroup`)** — G16-1 and G16-2 are
  done (`a513bd3ec`/`c5d19e82c`, `f4a1df5bc`/`55168dad8`); **14 rows remain** (G16-3…G16-16).
- Read the **Audit merge** section before touching a row: it carries the Q1–Q7 queue findings, the "verified
  clean" list (so finished work isn't re-opened), and the ruled-out false positives.
- The 9a evidence written on all 14 pending rows is from **2026-09-28** and is void (Q6) — re-run it per row.
- Audit gate commands that must pass at each 9a (they all pass on the audited tree):
  `.venv/bin/python -m pytest tests/test_armodel/ -q --no-header` (17408 passed),
  `.venv/bin/python -m ruff check <files>`, `.venv/bin/python -m black --check -l 200 <files>`,
  `python3 scripts/eval_skill_static_checks.py`, `python3 scripts/regen_sync_todo.py --check`.
  Note the worktree `.venv` **does** have ruff/black/pytest (installed with `uv sync --extra pytest --extra lint`), so
  the `PYTHONPATH` prefix + main-checkout interpreter is only needed if that venv is removed.
- Never trust a row's "Steps 1–8 `[x]`" claim: this run has twice found those claims false
  (`TimeSyncServerConfiguration`, `EthernetPriorityRegeneration`). Always re-run the 9 steps.
- The regen script takes ~2.5 min per invocation; it must run after every row flip (`--write` then `--check`).
- `CouplingPortRoleEnum` → `Table F.38, p.2013` is the calibration point for the PDFKit page-number fallback.
- If the main checkout's session finishes, the worktree can be retired with `git worktree remove .g16-wt` and the
  `.git/info/exclude` entry dropped, after `feature/g16-issue-classes-sync` is merged.

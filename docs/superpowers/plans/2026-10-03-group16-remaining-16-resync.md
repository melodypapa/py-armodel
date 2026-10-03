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

| # | Class | Severity | Defect(s) | Status |
|---|---|---|---|---|
| G16-1 | `EthernetPriorityRegeneration` | HIGH | reader missing base `readReferrable`; checklist scatter; stale suffix; bare-`int` test | ✅ `a513bd3ec` / `c5d19e82c` |
| G16-2 | `TimeSynchronization` | HIGH | Rule 0001.6 `set/get` for a `Referrable` child; checklist scatter; mirror test pins wrong shape | pending |
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
| G16-14 | `Ipv6AddressSourceEnum` | LOW | checklist contradiction | pending |
| G16-15 | `Ipv4AddressSourceEnum` | LOW | checklist contradiction | pending |
| G16-16 | `PduCollectionSemanticsEnum` | LOW | checklist contradiction | pending |

## Global Constraints

- **Work only in the `.g16-wt` worktree.** The main checkout `/Users/ray/Workspace/py-armodel` belongs to a
  concurrent session — never edit it, never `git checkout`/`switch`/`commit` there.
- **Every command needs the `PYTHONPATH` prefix** (the shared venv's editable `.pth` points at the main checkout):
  `cd /Users/ray/Workspace/py-armodel/.g16-wt && PYTHONPATH=/Users/ray/Workspace/py-armodel/.g16-wt/src /Users/ray/Workspace/py-armodel/.venv/bin/python -m pytest ...`
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
- Never edit integration fixture `.arxml` files (Rule 0019).

## Environment (already done — do not redo)

- Worktree `/Users/ray/Workspace/py-armodel/.g16-wt` on branch `feature/g16-issue-classes-sync`; hidden via a
  `.g16-wt/` entry in `.git/info/exclude` (local-only).
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

### G16-2: `TimeSynchronization` — HIGH (Rule 0001.6) + MED

**Files:** `EthernetTopology.py` (~L2920); parser `getTimeSynchronization` (~L9830); writer
`setTimeSynchronization` (~L9891); mirror `test_TimeSynchronization.py`; parser/writer tests.

- [ ] **Step A:** `timeSyncServer` (`0..1 aggr`, child `TimeSyncServerConfiguration` — spec `Base = ARObject ,
      Referrable`) must expose **`createTimeSyncServer(short_name)`** + `getTimeSyncServer()` instead of
      `setTimeSyncServer`/`getTimeSyncServer`. `timeSyncClient`'s child is a plain `ARObject` ⇒ keep `set`.
- [ ] **Step B:** parser: replace `TimeSyncServerConfiguration(None, shortName)` + `sync.setTimeSyncServer(server)`
      with `server = sync.createTimeSyncServer(self.getShortName(server_element))` then read into it. Writer reads
      via `getTimeSyncServer()`. No chained mutators.
- [ ] **Step C:** checklist rows scattered inside `__init__` → rebuild a single block before `__init__`.
- [ ] **Step D:** mirror test pins `setTimeSyncServer` → replace with `createTimeSyncServer` coverage (creation,
      duplicate-short-name returns existing, `getTimeSyncServer`) + parser round-trip asserting child field values.
- [ ] **Step E:** drop the stale ` (R23-11)` suffix (`# Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.145, p.469`).
- [ ] **Step F:** Steps 1–9a as prescribed (spec R23-11 Table 6.145, p.469; `Base = ARObject` → `__init__(self)`).

### G16-3: `MacMulticastGroup` — MED

**Files:** `EthernetTopology.py` L36; parser `readMacMulticastGroup` (~L10598); writer (`arxml_writer` ~L11284);
mirror `test_MacMulticastGroup.py`.

- [ ] **Step A:** `macMulticastAddress` is spec `MacAddressString` but the reader/writer use the generic literal
      pair → produce a plain `ARLiteral`. Construct the typed `MacAddressString` on read (mirror the
      `Ipv4Configuration` fix) and keep the writer's `setChildElementOptionalLiteral` (it accepts ARLiteral
      subclasses) — or use the typed writer helper if one exists.
- [ ] **Step B:** checklist rows inside `__init__` (L49–50) → single top block; drop the ` (R23-11)` suffix
      (`# Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 3.48, p.104`; `Base = ARObject , Identifiable ,
      MultilanguageReferrable , Referrable`).
- [ ] **Step C:** Steps 1–9a as prescribed.

### G16-4: `GenericTp` — MED

**Files:** `EthernetTopology.py` L3626; parser `readGenericTp` (~L10051); writer (~L10071); mirror test.

- [ ] **Step A:** `tpAddress`/`tpTechnology` are spec `String` but read via `getChildElementOptionalLiteral` → use
      `getChildElementOptionalString`/`setChildElementOptionalString` (Rule 0013.2/0001.3).
- [ ] **Step B:** checklist rows inside `__init__` (L3639–3645) → single top block; drop the ` (R23-11)` suffix
      (`# Spec: … Table 6.126, p.459`).
- [ ] **Step C:** Steps 1–9a as prescribed.

### G16-5: `TcpTp` — MED

**Files:** `EthernetTopology.py` L3786; parser `readTcpTp` (keepAlives OK at L10045, `naglesAlgorithm` uses the
literal helper); writer (~L10064); mirror test.

- [ ] **Step A:** `naglesAlgorithm` is spec `Boolean` but read via `getChildElementOptionalLiteral` → use
      `getChildElementOptionalBooleanValue`/`setChildElementOptionalBooleanValue` (sibling `keepAlives` is correct).
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

### G16-13: `IpAddressKeepEnum` — LOW

**Files:** `EthernetTopology.py` L2296 (contradiction at L2304–2305); mirror test.

- [ ] **Step A:** remove the `# (no methods)` vs `[x] __init__` contradiction.
- [ ] **Step B:** Steps 1–9a as prescribed (spec R23-11 Table 6.138, p.466; literals `forget`/`storePersistently`).

### G16-14: `Ipv6AddressSourceEnum` — LOW

**Files:** `EthernetTopology.py` L2322 (contradiction at L2330–2331); mirror test.

- [ ] **Step A:** remove the checklist contradiction.
- [ ] **Step B:** Steps 1–9a as prescribed (spec R23-11 Table 6.140, p.467; 5 literals incl. `linkLocal_doip`).

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

## Notes for the next session

- The queue is `docs/plan/sync-todo/Group16.md`; **resume at G16-2 (`TimeSynchronization`)** — G16-1 is done.
- Never trust a row's "Steps 1–8 `[x]`" claim: this run has twice found those claims false
  (`TimeSyncServerConfiguration`, `EthernetPriorityRegeneration`). Always re-run the 9 steps.
- The regen script takes ~2.5 min per invocation; it must run after every row flip (`--write` then `--check`).
- `CouplingPortRoleEnum` → `Table F.38, p.2013` is the calibration point for the PDFKit page-number fallback.
- If the main checkout's session finishes, the worktree can be retired with `git worktree remove .g16-wt` and the
  `.git/info/exclude` entry dropped, after `feature/g16-issue-classes-sync` is merged.

# Group16 Issue-Class Re-sync Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Bring the 11 rule-violating classes queued in `docs/plan/sync-todo/Group16.md` to a compliant, stamped state by re-running the `sync-autosar-class` 9-step workflow for each, one class per isolated subagent session.

**Architecture:** The defect list comes from the Group16 review (2026-10-03). Each class gets a **fresh subagent context** running Steps 1–9a in an **isolated git worktree**; the orchestrator independently verifies the 9a battery, presents the Step 9b gate, writes the `# Spec verified:` / `# XSD verified:` marker only on confirmation, then commits and flips the queue row. The persistent queue is `docs/plan/sync-todo/Group16.md` — never the conversation.

**Tech Stack:** Python 3.8-compatible typing (`Optional[T]` / `List[T]`), pytest, ruff, Black (line-length 200), the in-repo `sync-autosar-class` skill (`.agents/skills/sync-autosar-class/`).

## Global Constraints

- **Work only in the `.g16-wt` worktree.** The main checkout `/Users/ray/Workspace/py-armodel` belongs to a concurrent session that switches its branch; never edit it, never `git checkout`/`switch`/`commit` there.
- **Every command needs the `PYTHONPATH` prefix**: the shared venv's editable `.pth` points at the *main* checkout, so without it tests exercise the wrong source tree.
  `cd /Users/ray/Workspace/py-armodel/.g16-wt && PYTHONPATH=/Users/ray/Workspace/py-armodel/.g16-wt/src /Users/ray/Workspace/py-armodel/.venv/bin/python -m pytest ...`
- **`uv run` is unusable** in this sandbox (cannot write `~/.cache/uv`). `flake8` is not installed — ruff + `black --check` are the lint gates.
- **One class per subagent session** (Rule 0017.1), chained per Rule 0017.5. **9b stays mandatory for every class** — never self-stamp from subagent evidence.
- **Never collapse a finished todo row.** Rule 0024 was removed from the skill (commit `d9fa5ac19`); a finished row keeps its 9-step sub-checklist and write-ups as the durable audit trail.
- **Commits per class:** one `feat: <ClassName> synced.`, then one `docs: mark <ClassName> done in Group16 queue + regen reports` (which must run `python3 scripts/regen_sync_todo.py --write` and pass `--check`).
- **Scope discipline:** fix the class's *own* violations; do **not** fix other classes' defects — report them in the tracker / queue instead.
- Resolved user decisions (2026-10-03), binding:
  - **Rule 0007:** relocate all three mis-housed classes (do not record as deviations).
  - **Rule 0001.4 `Mult=1`:** keep `Optional[T]` and record an **accepted** deviation (repo-wide precedent: 106 `Optional` vs 14 plain among stamped classes).
- Never edit integration fixture `.arxml` files (Rule 0019).

## Environment setup (already done — do not redo)

- Worktree: `/Users/ray/Workspace/py-armodel/.g16-wt` on branch `feature/g16-issue-classes-sync`.
- Hidden from the main checkout via a `.g16-wt/` entry in `.git/info/exclude` (local-only, never committed).
- `tests/integration_tests/custom_files/` (gitignored) copied into the worktree so the round-trip fixtures resolve.
- Sanity check: `PYTHONPATH=.g16-wt/src .venv/bin/python -c "import armodel; print(armodel.__file__)"` must print the `.g16-wt` path.

## Status

| # | Class | Defect(s) | Status |
|---|---|---|---|
| 1 | `InitialSdDelayConfig` | Rule 0007 | ✅ `84dc59b64` |
| 2 | `SdServerConfig` | Rule 0007, Rule 0001.4 | ✅ `f509df9d9` |
| 3 | `IPSecConfig` | Rule 0007, Rule 0001.6 | ✅ `d75eb10bf` |
| 4 | `NetworkEndpoint` | Rule 0001.7, Rule 0006, stale checklist | pending |
| 5 | `TimeSyncServerConfiguration` | Rule 0001.7 | pending |
| 6 | `IPv6ExtHeaderFilterList` | Rule 0001.7, Rule 0003 | pending |
| 7 | `TcpOptionFilterList` | Rule 0003 | pending |
| 8 | `Ipv4Configuration` | Rule 0006 | pending |
| 9 | `SocketConnectionIpduIdentifier` | Rule 0006 | pending |
| 10 | `SocketConnectionBundle` | Rule 0001.4, Rule 0006 | pending |
| 11 | `CouplingPortAbstractShaper` (+ 2 stamped siblings) | Rule 0006 | pending |

### Completed passes — what they established (patterns to reuse)

- **Rule 0007 relocation recipe:** move the class + its checklist block to the spec-`Package` module, repoint every consumer (parser, writer, mirror test, sibling tests), keep `armodel.<ClassName>` resolving, then verify **both import orders** in fresh interpreters plus `typing.get_type_hints` on the moved accessors and their aggregators.
- **Import-cycle discipline (Rule 0005):** `EthernetTopology.py` ends with a bottom-of-module runtime import of `InitialSdDelayConfig, RequestResponseDelay`; `ServiceInstances.py` ends with `ApplicationEndpoint, SdClientConfig, SdServerConfig`; `SecureCommunication.py` ends with `CommunicationDirectionType`. Extend an existing breaker rather than adding a new one.
- **`readARObject`/`writeARObject`:** both `InitialSdDelayConfig` and `SdServerConfig` helpers were missing the pair, silently dropping the `AR:AR-OBJECT` `S`/`T` attributes. Check this for every class whose helpers construct an `ARObject` in a shared `getXxx`/`setXxx` pair.
- **`createXxx` vs `addXxx` (Rule 0001.6):** a `*` aggregated child whose spec `Base` lists `Referrable`/`Identifiable` needs `createXxx(short_name)` + `getXxxs()`. `IPSecRule` needed the fix; `TagWithOptionalValue` (plain `ARObject`) correctly keeps `addCapabilityRecord`.
- **Pair order (Rule 0001.11):** scalar pairs are getter-first, list/aggregated pairs are **mutator-first**.

---

### Task 4: `NetworkEndpoint` — Rule 0001.7 coverage gap + Rule 0006

**Files:**
- Modify: `src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/EthernetTopology.py` (class ~L3011)
- Modify: `src/armodel/parser/arxml_parser.py` (`readNetworkEndPoint`, ~L9874)
- Modify: `src/armodel/writer/arxml_writer.py` (`writeNetworkEndPoint`, ~L9922)
- Modify: `tests/test_armodel/models/M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/test_NetworkEndpoint.py`
- Tests: `tests/test_armodel/parser/`, `tests/test_armodel/writer/`

**Interfaces:** spec R23-11 Table 6.134, p.463, `Base = ARObject , Identifiable , MultilanguageReferrable , Referrable` (so `__init__(self, parent, short_name)`). Five spec attributes: `fullyQualifiedDomainName` (`String`, `0..1`, attr), `infrastructureServices` (`InfrastructureServices`, `0..1`, aggr), `ipSecConfig` (`IPSecConfig`, `0..1`, aggr), `networkEndpointAddress` (`NetworkEndpointAddress`, `*`, aggr), `priority` (`PositiveInteger`, `0..1`, attr).

- [ ] **Step 1: Close the `fullyQualifiedDomainName` reader/writer gap (Rule 0001.7).**
  `FULLY-QUALIFIED-DOMAIN-NAME` currently appears in **neither** `arxml_parser.py` nor `arxml_writer.py` — the attribute has a field + accessor pair and a `[x] reader` / `[x] writer` checklist claim, but is dropped on round-trip. Add the read (`getChildElementOptionalString`) and write (`setChildElementOptionalString`) elements in XSD `sequenceOffset` position, inside the matched `readNetworkEndPoint`/`writeNetworkEndPoint` pair.
- [ ] **Step 2: Write the failing round-trip test first (Rule 0006, Step 5 Red).**
  Assert the **field value** round-trips (`parsed.getFullyQualifiedDomainName().getValue() == "some.example.host"`), not just presence.
- [ ] **Step 3: Fix the stale checklist rows.**
  `getIpSecConfig`/`setIpSecConfig` are marked `[—] reader` / `[—] writer` although the helpers **do** wire `IP-SEC-CONFIG`; correct them (found during the `IPSecConfig` pass).
- [ ] **Step 4: Close the mirror-test coverage gap (Rule 0006).**
  `getNetworkEndpointAddresses` is never asserted in `test_NetworkEndpoint.py`.
- [ ] **Step 5: Steps 1–9a as prescribed** (docstring wipe+rewrite verbatim, PEP 526 members, Rule 0008 spacing, member/checklist order = markdown order, both import orders, full suite + integration delta).

---

### Task 5: `TimeSyncServerConfiguration` — Rule 0001.7 coverage gap

**Files:**
- Modify: `src/armodel/models/.../Fibex4Ethernet/EthernetTopology.py` (class ~L2758)
- Modify: `src/armodel/parser/arxml_parser.py` (`getTimeSynchronization`, ~L9830)
- Modify: `src/armodel/writer/arxml_writer.py` (`setTimeSynchronization`, ~L9891)
- Tests: mirror + parser + writer

**Interfaces:** spec R23-11 Table 6.147, p.470, `Base = ARObject , Referrable` → `__init__(self, parent, short_name)`. Four attributes: `priority` (`PositiveInteger`, `0..1`), `syncInterval` (`TimeValue`, `0..1`), `timeSyncServerIdentifier` (`String`, `0..1`), `timeSyncTechnology` (`TimeSyncTechnologyEnum`, `0..1`).

- [ ] **Step 1: Cover the three unhandled attributes (Rule 0001.7).**
  The parser's `TIME-SYNC-SERVER` branch sets **only** `setTimeSyncTechnology`; the writer's server branch writes **only** `TIME-SYNC-TECHNOLOGY`. `PRIORITY`, `SYNC-INTERVAL` and `TIME-SYNC-SERVER-IDENTIFIER` are read/written nowhere → 3 of 4 attributes are silently dropped, while the checklist claims `[x] reader` / `[x] writer` on all of them. Add all six call sites in XSD `sequenceOffset` order.
  **Watch out:** `setPriority`/`getPriority` are extremely common method names — a repo-wide grep count is *not* evidence. Check the call is inside `getTimeSynchronization`/`setTimeSynchronization` specifically.
- [ ] **Step 2: Write the failing round-trip test first**, asserting each of the four field values.
- [ ] **Step 3: Steps 1–9a as prescribed.**

---

### Task 6: `IPv6ExtHeaderFilterList` — Rule 0001.7 + Rule 0003

**Files:**
- Modify: `src/armodel/models/.../Fibex4Ethernet/IPv6HeaderFilterList.py` (class ~L11)
- Modify: `src/armodel/parser/arxml_parser.py`, `src/armodel/writer/arxml_writer.py`
- Tests: mirror + parser + writer

**Interfaces:** spec R23-11 Table 6.121, p.456, `Base = ARObject , Identifiable , MultilanguageReferrable , Referrable`. **One** attribute: `allowedIPv6ExtHeader` (`PositiveInteger`, `*`, **attr**).

- [ ] **Step 1: Implement the missing wrapper-list reader/writer (Rule 0001.7).**
  The checklist marks reader/writer `[—]` with the justification "consumed as ref target via `ALLOWED-I-PV-6-EXT-HEADERS-REF`". That is **wrong**: the R23-11 table lists `allowedIPv6ExtHeader` as an `attr`, and `AUTOSAR_00052.xsd` L66606 defines its own `ALLOWED-I-PV-6-EXT-HEADERS` wrapper of unbounded `ALLOWED-I-PV-6-EXT-HEADER` (`AR:POSITIVE-INTEGER`) items. The `…-REF` element (XSD L107861) belongs to `SocketAddress`. Add the wrapper-list reader (`iterate WRAPPER/ITEM` → `addAllowedIPv6ExtHeader`) and writer (emit the wrapper **only when non-empty**), and fix the checklist rows.
- [ ] **Step 2: Remove the quoted annotation (Rule 0003).**
  `def addAllowedIPv6ExtHeader(self, value: PositiveInteger) -> "IPv6ExtHeaderFilterList":` — the module lacks `from __future__ import annotations`. Per Rule 0003/0005 either add PEP 563 and unquote (**then all of that module's quoted signatures must be unquoted in the same change**, Rule 0022) or restructure. Note the Rule 0022 gate test only catches *nested* quotes, so automation is blind here.
- [ ] **Step 3: Write the failing round-trip test first**, including the **empty-wrapper** case (assert no wrapper tag is emitted and re-parsing yields `[]`).
- [ ] **Step 4: Steps 1–9a as prescribed.**

---

### Task 7: `TcpOptionFilterList` — Rule 0003

**Files:**
- Modify: `src/armodel/models/.../Fibex4Ethernet/TcpOptionFilterSet.py` (class ~L12)
- Tests: mirror (+ parser/writer if the wrapper list needs coverage)

**Interfaces:** spec R23-11 Table 6.123, p.457, `Base = ARObject , Identifiable , MultilanguageReferrable , Referrable`. One attribute: `allowedTcpOption` (`PositiveInteger`, `*`, attr) → `allowedTcpOptions: List[PositiveInteger]` + `addAllowedTcpOption`/`getAllowedTcpOptions`.

- [ ] **Step 1: Remove the quoted annotation (Rule 0003).**
  `def addAllowedTcpOption(self, value: PositiveInteger) -> "TcpOptionFilterList":` — same fix as Task 6 Step 2; check the module's PEP 563 status first and unquote every quoted signature in it if you add the future import.
- [ ] **Step 2: Verify the reader/writer coverage** for the `*` attr (a wrapper list) — it currently has call sites; confirm they live inside the class's own helper, not a sibling's.
- [ ] **Step 3: Steps 1–9a as prescribed.**

---

### Task 8: `Ipv4Configuration` — Rule 0006

**Files:**
- Modify: `tests/test_armodel/models/.../Fibex4Ethernet/test_Ipv4Configuration.py`

**Interfaces:** spec R23-11 Table 6.136, p.465, `Base = ARObject , NetworkEndpointAddress` → `class Ipv4Configuration(NetworkEndpointAddress)` / `__init__(self)`. Eight attributes, incl. `dnsServerAddress` (`Ip4AddressString`, `*`) → `addDnsServerAddress`/`getDnsServerAddresses`.

- [ ] **Step 1: Add the missing getter coverage (Rule 0006).**
  The mirror test calls `addDnsServerAddress` but never asserts `getDnsServerAddresses()` — the list contents and the `[]` default are unverified.
- [ ] **Step 2: Confirm the `0..1` vs `*` quota shapes** against Table 6.136 and the member/checklist order (Rule 0001.11).
- [ ] **Step 3: Steps 1–9a as prescribed.**

---

### Task 9: `SocketConnectionIpduIdentifier` — Rule 0006

**Files:**
- Rename: `tests/test_armodel/models/.../Fibex4Ethernet/test_SocketConnectionIpduIdentifier2.py` → `test_SocketConnectionIpduIdentifier.py`
- Source: `src/armodel/models/.../Fibex4Ethernet/EthernetCommunication.py` (class ~L49)

**Interfaces:** spec **R4.3.1** Table 6.122, p.321 (class-scoped Rule 0016.3 fallback → marker and every row `R4.3.1`), `Base = ARObject` → `__init__(self)`. Six attributes.

- [ ] **Step 1: Rename the test file to the Rule 0006 convention** (`test_<ClassName>.py`; the inner `class TestSocketConnectionIpduIdentifier` is already correct).
- [ ] **Step 2: Check the `routingGroup` `*` `ref` accessor shape.**
  It is modelled as `setRoutingGroupRefs(List)` / `getRoutingGroupRefs()`. Rule 0001.4 wants the list shape with a plural getter **and** an `addXxx` mutator; verify against the rule and the sibling classes before changing (the writer calls `getRoutingGroupRefs()` five times — confirm which are the class's own path).
- [ ] **Step 3: Steps 1–9a as prescribed** (including a live round-trip through `readSocketConnectionBundle`/`writeSocketConnectionBundle`).

---

### Task 10: `SocketConnectionBundle` — Rule 0001.4 + Rule 0006

**Files:**
- Rename: `tests/test_armodel/models/.../Fibex4Ethernet/test_SocketConnectionBundle2.py` → `test_SocketConnectionBundle.py`
- Source: `src/armodel/models/.../Fibex4Ethernet/EthernetCommunication.py` (class ~L183)

**Interfaces:** spec **R4.3.1** Table 6.118, p.316, `Base = ARObject, Referrable` → `__init__(self, parent, short_name)`. Seven attributes, incl. `bundledConnection` (`SocketConnection`, `1..*`, aggr), `pdu` (`SocketConnectionIpduIdentifier`, `*`, aggr), `serverPort` (`SocketAddress`, `1`, ref).

- [ ] **Step 1: Record the `serverPortRef` accepted deviation (Rule 0001.4).**
  Spec `Mult = 1`; code uses `Optional[RefType]`. Per the resolved user decision, **keep `Optional`** and record an accepted deviation in `docs/examples/method_deviation_by_class.md`:
  `type (PDF Mult 1 vs py Optional[RefType]; repo-wide Optional-for-required convention, 106:14 stamped precedent, user-confirmed 2026-10-03)`
- [ ] **Step 2: Rename the test file to the Rule 0006 convention.**
- [ ] **Step 3: Verify `1..*` renders as `List[T]`** (it does) and that the mutator-first pair order holds (`addBundledConnection`/`getBundledConnections`, `addPdu`/`getPdus`).
- [ ] **Step 4: Steps 1–9a as prescribed.**

---

### Task 11: `CouplingPortAbstractShaper` (+ 2 already-stamped siblings) — Rule 0006

**Files:**
- Rename: `tests/test_armodel/models/.../Fibex4Ethernet/test_coupling_port_abstract_shaper_model.py` → `test_CouplingPortAbstractShaper.py`
- Rename: `.../test_coupling_port_asynchronous_traffic_shaper_model.py` → `test_CouplingPortAsynchronousTrafficShaper.py`
- Rename: `.../test_coupling_port_credit_based_shaper_model.py` → `test_CouplingPortCreditBasedShaper.py`
- Source: `src/armodel/models/.../Fibex4Ethernet/EthernetTopology.py` (L175, and the two stamped subclasses)

**Interfaces:** all three are XSD-only (`# XSD verified: AUTOSAR_00052.xsd`), so the marker stays `XSD verified` and the rows stay `release = R23-11`.

- [ ] **Step 1: Handle the two `[x]` rows per Rule 0017.1 first.**
  `CouplingPortAsynchronousTrafficShaper` and `CouplingPortCreditBasedShaper` are already `[x]` and stamped — this is the **drift/extension exception**: the user must say so explicitly, then reset each row to `[ ]` with a `drift R23-11` note before re-running. Do not silently re-sync a finished row.
- [ ] **Step 2: Rename all three test files** to the Rule 0006 `test_<ClassName>.py` convention and keep `class Test<ClassName>`.
- [ ] **Step 3: Re-run Steps 1–9a for `CouplingPortAbstractShaper`** (the abstract class: Steps 5/6 are N/A — no own XML element; the `SHAPER` choice round-trips via `CouplingPortFifo`).
- [ ] **Step 4: Re-run the 9b gate for the two siblings against their existing `# XSD verified:` stamps** (re-stamp only on fresh confirmation).

---

## Reported, not fixed (other classes' items — drain in their own passes)

These were surfaced during Tasks 1–3 and deliberately left alone. They must **not** be treated as patterns to copy (Rules 0004/0013.1):

- `ProvidedServiceInstance.getSdServerConfig`/`setSdServerConfig` — untyped accessors (Rule 0001.3).
- `docs/examples/method_deviation_by_class.md`: the `SdClientConfig` entry still records `capabilityRecord` as `type (spec many vs py single)` although the class models `List[TagWithOptionalValue]` and is stamped `R4.3.1` — a stale row to remove.
- `SomeipSdServerServiceInstanceConfig` — a misplaced stub in `GenericStructure/GeneralTemplateClasses/ArObject.py` with no parser/writer handler, so `InitialSdDelayConfig.initialOfferBehavior` does not round-trip through that aggregator (Rule 0001.10, own sync needed).
- `RequestResponseDelay` — spec-faithful 6-column R23-11 checklist but **not yet stamped**; its Group16 row is still pending.
- Sibling SD-config helpers (`getRequestResponseDelay`/`setRequestResponseDelay`, `getSdClientConfig`/`setSdClientConfig`) still omit the `readARObject`/`writeARObject` pair.
- `.g16-wt/AGENTS.md` and `.g16-wt/CLAUDE.md` both reference `tests/test_files/`, which does not exist in this worktree.

## Notes for the next session

- The queue is `docs/plan/sync-todo/Group16.md`; resume at the first row still `[ ]`. Re-run the Phase-0 closure only if the file is missing (Rule 0017.1) — it is not.
- If the main checkout's session finishes, the worktree can be retired with `git worktree remove .g16-wt` and the `.git/info/exclude` entry dropped, after `feature/g16-issue-classes-sync` is merged.
- `regen_sync_todo.py --write` must run from the worktree and `--check` must pass before committing a row flip.

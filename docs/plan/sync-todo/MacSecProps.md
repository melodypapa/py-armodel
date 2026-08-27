# Sync todo: MacSecProps member-type cluster (SystemTemplate::SecureCommunication)

Input class: `MacSecProps` (Table 3.118), referenced by `CouplingPort.macSecProps` (List, aggr).
This is a **sub-sync** of the Ethernet sync (`docs/plan/sync-todo/Ethernet.md`). Its member closure
is resolved here per Rule 0016 (own Phase 0, 2026-08-27). Generated: 2026-08-27.

**Authority note — markdown is GARBLED for this cluster.** The `Table 3.118` block in
`autosar/R23-11/markdown/AUTOSAR_CP_TPS_SystemTemplate.md` mislabels `MacSecLocalKayProps`'s content as
`MacSecProps` and omits the real 5 attributes. The **PDF** (`autosar/R23-11/pdf/AUTOSAR_CP_TPS_SystemTemplate.pdf`,
file-pages 172–177 = printed pp.173–177) is the authoritative source for every class below. All `# Spec:`
lines cite the PDF page, not the markdown.

**Scope decisions (Rule 0016.4 / user 2026-08-27):**
- `CryptoServiceKey` (ref target of `MacSecKayParticipant.ckn`/`sak`) → typed as **`RefType`** (cross-domain
  class, no model class in `src/`; repo convention for cross-domain refs). **SKIP — not queued**, does not
  block `# Spec verified:`.
- `MacSecParticipantSet` (Table 3.121) → **EXCLUDED**: nothing in the `MacSecProps` chain references it
  (it is a top-level `ARPackage.element` aggregating `MacSecKayParticipant`; the dependency arrow points the
  other way). Not in closure.
- `MacAddressString`, `PositiveInteger`, `Boolean`, `TimeValue`, `String` → primitives (exist). `RefType` →
  framework. `EthernetCluster` → exists. None queued.

**All 10 classes share Package** `M2::AUTOSARTemplates::SystemTemplate::SecureCommunication` → source file
`src/armodel/models/M2/AUTOSARTemplates/SystemTemplate/SecureCommunication.py` (leaf package, Rule 0007).
Tests mirror under `tests/test_armodel/models/M2/AUTOSARTemplates/SystemTemplate/`; reader/writer round-trip
tests under `tests/test_armodel/parser/` + `tests/test_armodel/writer/`.

**Closure status legend:** `exists-fix` = class written but UNSTAMPED and (for enums) literal values wrong /
for classes refs typed generic `RefType` → must be corrected + stamped. `missing` = no model class yet.

## Queue (dependency-first, member-type-first — Rule 0016.5)

### Phase A — Enums (no deps; Steps 5/6 N/A for standalone enums)

- [x] MacSecRoleEnum (enum · Table 3.127 · p.177 · **exists-fix**: literal values corrected `"PEER"`/`"KEY-SERVER"` → `peer`/`keyServer` per spec camelCase names; **STAMPED R23-11** — commit f955e5ac) — used by MacSecLocalKayProps.role
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red) — **N/A** (standalone enum, serialized as attribute value on MacSecLocalKayProps.role)
  - [x] Step 6 — Update parser & writer (Green) — **N/A**
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - [x] Step 9 — Verify (9a) + confirm (9b)

- [x] MacSecFailPermissiveModeEnum (enum · Table 3.128 · p.178 · **exists-fix**: literals currently
  `"NEVER"`/`"TIMEOUT"` but spec literal names are `never`(idx0)/`timeout`(idx1) → must become
  `NEVER="never"`, `TIMEOUT="timeout"`; used by MacSecProps.onFailPermissiveMode) <!-- commit: ac4d0c88 -->
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red) — **N/A** (standalone enum, serialized on MacSecProps.onFailPermissiveMode)
  - [x] Step 6 — Update parser & writer (Green) — **N/A**
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - [x] Step 9 — Verify (9a) + confirm (9b)

- [x] MacSecCapabilityEnum (enum · Table 3.126 · p.177 · **missing**: literals
  `intergrityWithoutConfidentiality`(idx0)/`intergrityAndConfidentiality`(idx1) — note spec spelling
  "intergrity"; used by MacSecCryptoAlgoConfig.capability) <!-- commit: cd2ca48a -->
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red) — **N/A** (standalone enum)
  - [x] Step 6 — Update parser & writer (Green) — **N/A**
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - [x] Step 9 — Verify (9a) + confirm (9b)

- [x] MacSecConfidentialityOffsetEnum (enum · Table 3.125 · p.177 · **missing**: literals
  `CONFIDENTIALITY-OFFSET-0`(idx0)/`CONFIDENTIALITY-OFFSET-30`(idx1)/`CONFIDENTIALITY-OFFSET-50`(idx2)
  (xml.name form); used by MacSecCryptoAlgoConfig.confidentialityOffset) <!-- commit: 45f49f30 -->
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red) — **N/A** (standalone enum)
  - [x] Step 6 — Update parser & writer (Green) — **N/A**
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - [x] Step 9 — Verify (9a) + confirm (9b)

### Phase B — Leaf value types (deps: primitives only)

- [x] MacSecGlobalKayProps (class · Table 3.120 · p.174 · **missing**: Base = full chain
  ARElement,ARObject,CollectableElement,Identifiable,MultilanguageReferrable,PackageableElement,Referrable,
  UploadableDesignElement,UploadablePackageElement; attrs bypassEtherType(PositiveInteger 0..255 attr),
  bypassVlan(PositiveInteger 0..255 attr); used by MacSecLocalKayProps.globalKayProps ref) <!-- commit: 7ddad6b1 -->
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
    (tracker: UploadableDesignElement/UploadablePackageElement XSD-only base classes not modeled — ARElement used as most-derived base; list-vs-attr form resolved per XSD + user 2026-08-27 — bypassEtherTypes/bypassVlans as List[PositiveInteger]; no open deviations)
  - [x] Step 9 — Verify (9a) + confirm (9b)
- [x] MacSecCipherSuiteConfig (class · Table 3.124 · p.176 · **missing**: Base ARObject; attrs
  cipherSuite(String 0..1 attr), cipherSuitePriority(PositiveInteger 0..1 attr); used by
  MacSecCryptoAlgoConfig.cipherSuiteConfig aggr 0..4) <!-- commit: 9962a8d5 -->
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - [x] Step 9 — Verify (9a) + confirm (9b)

### Phase C — Mid-tier (deps: Phase A + B)

- [x] MacSecCryptoAlgoConfig (class · Table 3.123 · p.175 · **missing**: Base ARObject; attrs
  capability(MacSecCapabilityEnum 0..1 attr), cipherSuiteConfig(MacSecCipherSuiteConfig 0..4 aggr),
  confidentialityOffset(MacSecConfidentialityOffsetEnum 0..1 attr), replayProtection(Boolean 0..1 attr),
  replayProtectionWindow(PositiveInteger 0..1 attr); used by MacSecKayParticipant.cryptoAlgoConfig aggr 0..1) <!-- commit: 6cc501b6 -->
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [x] MacSecLocalKayProps (class · Table 3.119 · p.174 · **exists-fix**: all 6 fields present and correct
  (destinationMacAddress, globalKayProps, keyServerPriority, mkaParticipant, role, sourceMacAddress);
  refs KEPT as generic `RefType` per repo convention (no typed-ref precedent in codebase, user 2026-08-28 —
  CryptoServiceKey precedent, does not depend on MacSecKayParticipant); docstrings verified verbatim vs PDF;
  dedicated writer/reader round-trip tests added incl. empty MKA-PARTICIPANT-REFS wrapper; **STAMPED R23-11** —
  commit b33bd3c5) <!-- commit: b33bd3c5 -->
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - [x] Step 9 — Verify (9a) + confirm (9b)

### Phase D — Aggregating class (deps: Phase C)

- [x] MacSecKayParticipant (class · Table 3.122 · p.175 · **missing**: Base ARObject,Identifiable,
  MultilanguageReferrable,Referrable; attrs ckn(CryptoServiceKey 0..1 ref → RefType),
  cryptoAlgoConfig(MacSecCryptoAlgoConfig 0..1 aggr), sak(CryptoServiceKey 0..1 ref → RefType);
  referenced by MacSecLocalKayProps.mkaParticipant ref 0..*, aggregated by MacSecParticipantSet (excluded);
  **STAMPED R23-11** — commit e2fac560)
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
    (tracker: ckn/sak are CryptoServiceKey refs typed generic `RefType` per repo convention (user 2026-08-28, no typed-ref precedent) — pre-decided in Phase 0, NOT an open deviation; no placeholders; no open deviations)
  - [x] Step 9 — Verify (9a) + confirm (9b)

### Phase E — Input class (deps: Phase A + C)

- [x] MacSecProps (class · Table 3.118 · p.173 · **exists-fix**: fields correct vs PDF
  (autoStart Boolean, macSecKayConfig MacSecLocalKayProps aggr, onFailPermissiveMode
  MacSecFailPermissiveModeEnum attr, onFailPermissiveModeTimeout TimeValue, sakRekeyTimeSpan TimeValue);
  original gap — "deeper member r/w coverage missing (MacSecLocalKayProps sub-tree not round-tripped)" —
  is now CLOSED: MacSecLocalKayProps stamped (b33bd3c5, dedicated round-trip tests) and CouplingPort
  tests (test_coupling_port.py test_write_mac_sec_props + test_round_trip_mac_sec_props) round-trip the
  full MacSecProps→MacSecLocalKayProps tree via readCouplingPort/writeCouplingPort; **STAMPED R23-11** —
  commit a150ffd2. Aggregated by CouplingPort.macSecProps (List). Unblocks `CouplingPort`
  in Ethernet.md once stamped.)
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - [x] Step 9 — Verify (9a) + confirm (9b)

## Termination

All 10 rows `[x]` = MacSecProps cluster synced + `CouplingPort` (Ethernet.md) unblocked for stamping.
Each class commits to the feature branch on its own 9b confirmation (Rule 0017.2); the Ethernet.md
`MacSecProps` row flips to `[x]` only after the full sub-queue lands.

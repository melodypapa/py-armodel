# Sync todo: Group 20 — Crypto, DoIP, Firewall, ECU resource, LogTrace & obsolete

Input: full-repo orphan audit 2026-09-23 (unstamped ∧ untracked, M2 only) · Queue order = row order
(resume = first class row still `[ ]`; all class rows `[x]` = sync finished — Rule 0017.3)
> **Rule — already-verified short-circuit (added 2026-09-04):** before running the 9-step
> sync for a row, check whether the class already carries `# Spec verified: <RELEASE>` or
> `# XSD verified: <xsd-file>` in its own class body (verify the marker in the source — a
> row in this todo is not proof). If it does **and** a quick deviation check finds nothing
> new (base vs the spec `Base` closure, member types vs its table, verbatim docstrings,
> reader/writer coverage, checklist shape per Rules 0002/0012), **skip the 9 steps**: mark
> the row `- [x] <Class> — already verified (<marker>, <file>)` and move on. If the check
> finds a new deviation, do **not** mark it verified — keep the row queued, run the steps
> for the deviation only, and record it in Step 8 (Rule 0012.3: an existing marker is not
> proof).

## Queue (dependency-first)

- [ ] `DoIpLogicAddress` — Identifiable — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SystemTemplate/TransportProtocols.py
  - note: deviation-tracked in method_deviation_by_class_v2.md — review entries at Step 1
  - note (Step 1): Table 6.207 p.555 (body after caption, md L14524-14532): Class =
    DoIpLogicAddress (concrete); Package =
    M2::AUTOSARTemplates::SystemTemplate::TransportProtocols; Note = "The logical
    DoIP address."; Base = "ARObject, Identifiable, MultilanguageReferrable,
    Referrable" → most-derived Identifiable (claimed base correct); Aggregated by
    DoIpConfig.logicAddress + DoIpTpConfig.doIpLogicAddress; Attribute rows:
    address (Integer, 0..1, attr), doIpLogicAddressProps
    (AbstractDoIpLogicAddressProps, 0..1, aggr; md renders "doIpLogic
    AddressProps" — line-wrap artifact). XSD 00052: group DO-IP-LOGIC-ADDRESS
    L48810 = ADDRESS (0..1) then DO-IP-LOGIC-ADDRESS-PROPS (0..1, choice of
    DO-IP-LOGIC-TARGET-ADDRESS-PROPS / DO-IP-LOGIC-TESTER-ADDRESS-PROPS); no
    VARIATION-POINT → not VP-capable. Drift: fabricated class docstring, bare
    field annotations (no Optional), untyped accessors, stale 3-col checklist,
    setDoIpLogicAddressProps setter violating Rule 0001.6 (0..1 Referrable
    abstract child needs create factories). Tracker review: no
    method_deviation_by_class_v2.md section exists for this class (nothing to
    reconcile).
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - note (Steps 5/6): read/writeDoIpLogicAddress + readDoIpLogicAddressProps
    pre-existed (writer unchanged); reader migrated from direct props
    construction + setDoIpLogicAddressProps to createDoIpLogicTargetAddressProps /
    createDoIpLogicTesterAddressProps factories (no chained mutators); parser
    DoIP import trimmed (F401); new test_arxml_parser_doip_logic_address.py (3
    tests) + test_writer_doip_logic_address.py (3 tests) pass.
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - note (Step 8): no open deviations — setter removal is Rule 0001.6
    conformance, not a deviation; verbatim docstrings restored; Optional[T]
    annotations + typed accessors; 6-col checklist written (no stamp markers
    per batch mode).
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-27 (12437 passed / 0 failed, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

- [ ] `DoIpTpConnection` — TpConnection — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SystemTemplate/TransportProtocols.py
  - note (Step 1): Table 6.206 p.555 (caption-above render, body md L14511-14520):
    Class = DoIpTpConnection (concrete); Package =
    M2::AUTOSARTemplates::SystemTemplate::DiagnosticConnection (info only — class
    stays in TransportProtocols.py alongside its consumers); Note = "A connection
    identifies the sender and the receiver of this particular communication. The
    DoIp module routes a tpSdu through this connection."; Base = "ARObject,
    TpConnection" → most-derived TpConnection (claimed base correct); Aggregated
    by DoIpTpConfig.tpConnection; Attribute rows: doIpSourceAddress
    (DoIpLogicAddress, 0..1, ref → doIpSourceAddressRef Optional[RefType], Rule
    0001.5 Ref suffix), doIpTargetAddress (DoIpLogicAddress, 0..1, ref →
    doIpTargetAddressRef), tpSdu (PduTriggering, 0..1, ref → tpSduRef). XSD 00052:
    group DO-IP-TP-CONNECTION L49407 = DO-IP-SOURCE-ADDRESS-REF,
    DO-IP-TARGET-ADDRESS-REF, TP-SDU-REF (all 0..1, DEST enums); no
    VARIATION-POINT (unlike CanTpConnection) → not VP-capable; IDENT carried via
    TpConnectionIdent (inherited TpConnection machinery). Drift: fabricated class
    docstring, bare field annotations (no Optional), untyped accessors, stale
    3-col checklist. read/writeDoIpTpConnection pre-existed and are unchanged.
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - note (Steps 5/6): readDoIpTpConnection (IDENT via readTpConnection/
    createTpConnectionIdent + 3 refs) and writeDoIpTpConnection (IDENT if set +
    3 refs, XSD order) pre-existed — no parser/writer changes needed; new
    test_arxml_parser_doip_tp_connection.py (2 tests: full w/ IDENT + empty) and
    test_writer_doip_tp_connection.py (3 tests: XSD order w/ IDENT, empty omits
    refs, round-trip) pass; short name lives in IDENT (TpConnection is not
    Referrable), not on the connection itself.
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - note (Step 8): no open deviations — verbatim docstrings restored;
    Optional[RefType] annotations + typed accessors; 6-col checklist written (no
    stamp markers per batch mode); no method_deviation_by_class_v2.md section
    exists for this class.
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-27 (12452 passed / 0 failed, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

- [ ] `CryptoKeySlotTypeEnum` — AREnum — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/AdaptivePlatform/PlatformModuleDeployment/CryptoDeployment/__init__.py
  - note (Step 1): XSD-only — no `Enumeration` table in R23-11 markdown (only the
    CryptoKeySlot Table B.5 attribute row references the type), none in R4.3.1
    markdown, pdf_page.py finds no PDF table (Rule 0016.3 fallback exhausted).
    XSD 00052: complexType CRYPTO-KEY-SLOT-TYPE-ENUM L132660 + simpleType
    --SIMPLE L132672; literals MACHINE (Index=0) and APPLICATION (Index=1) with
    wire values "MACHINE"/"APPLICATION" (xml.name values — no PDF Literal column
    to supply camelCase); class Note = "This enumeration defines the options for
    the usage of a Key Slot in the platform." Tags: atp.Status=candidate.
    Upstream doc: AUTOSAR_AP_TPS_PlatformModuleDeployment (AdaptivePlatform).
    Impl pre-exists from an unstamped prior pass and matches the XSD verbatim —
    no drift; location kept beside consumer CryptoKeySlot (Rule 0007).
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red) (N/A: standalone enum — round-trips as an attribute value on consumer CryptoKeySlot.slotType, covered by test_crypto_key_slot.py parser/writer suites)
  - [x] Step 6 — Update parser & writer (Green) (N/A: standalone enum)
  - note (Steps 2–6): impl + reader/writer coverage pre-exist from an unstamped
    prior pass; new tests written first this pass (literal order via
    getEnumValues, instantiability via Enum().setValue(Enum.MEMBER), class
    docstring verbatim vs XSD Note) — 16 passed with no source change
    (Red→Green collapsed against the pre-existing unstamped implementation);
    docstrings verified verbatim against XSD 00052 documentation/appinfo.
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - note (Step 8): no deviation, no tracker section for this enum — member
    values are the XSD wire strings by design for XSD-only enums (no PDF
    Literal column); nothing to record in method_deviation_by_class.md.
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-27 (12454 passed / 0 failed, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

- [ ] `CryptoObjectTypeEnum` — AREnum — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/AdaptivePlatform/PlatformModuleDeployment/CryptoDeployment/__init__.py
  - note: deviation-tracked in method_deviation_by_class.md — review entries at Step 1
  - note (Step 1): XSD-only — no `Enumeration` table in R23-11 markdown (only the
    CryptoKeySlot Table B.5 `cryptoObjectType` attribute row at md L1273
    references the type), none in R4.3.1 markdown, pdf_page.py finds no PDF
    table (Rule 0016.3 fallback exhausted). XSD 00052: complexType
    CRYPTO-OBJECT-TYPE-ENUM L132716 + simpleType --SIMPLE L132728; 6 literals
    by EnumerationLiteralIndex: UNDEFINED=0, SYMMETRIC-KEY=1, PRIVATE-KEY=2,
    PUBLIC-KEY=3, SIGNATURE=4, SECRET-SEED=5 (XSD renders them alphabetically;
    index gives the canonical order), wire values = xml.name exact strings;
    class Note = "Enumeration of all types of crypto objects, i.e. types of
    content that can be stored to a key slot." Tags: atp.Status=candidate.
    Upstream doc: AUTOSAR_AP_TPS_PlatformModuleDeployment (AdaptivePlatform).
    Impl pre-exists (unstamped prior pass) and matches the XSD verbatim — no
    drift. Tracker review: no `CryptoObjectTypeEnum` section exists; the class
    appears only inside the `CryptoKeySlot` entry's `missing` rows, which are
    stale (all four members implemented with reader/writer coverage) — removed
    in this commit per Rule 0014.
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red) (N/A: standalone enum — round-trips as an attribute value on consumer CryptoKeySlot.cryptoObjectType, covered by test_crypto_key_slot.py parser/writer suites)
  - [x] Step 6 — Update parser & writer (Green) (N/A: standalone enum)
  - note (Steps 2–6): impl + coverage pre-exist from the unstamped prior pass;
    new tests written first this pass (literal order via getEnumValues,
    instantiability via Enum().setValue(Enum.MEMBER), class docstring verbatim
    vs XSD Note) — pass with no source change (Red→Green collapsed);
    docstrings verified verbatim against XSD 00052 documentation/appinfo.
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - note (Step 8): no deviation for the enum itself — member values are the XSD
    wire strings by design for XSD-only enums; the stale `CryptoKeySlot`
    tracker `missing` rows referencing this enum were removed instead (Rule
    0014).
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-27 (12456 passed / 0 failed, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

- [ ] `CryptoKeySlotAllowedModification` — ARObject — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/AdaptivePlatform/PlatformModuleDeployment/CryptoDeployment/__init__.py
  - note: deviation-tracked in method_deviation_by_class.md — review entries at Step 1
  - note (Step 1): XSD-only — no `Class` table in R23-11 markdown, none in
    R4.3.1 markdown, pdf_page.py finds no PDF table (Rule 0016.3 fallback
    exhausted). XSD 00052: complexType CRYPTO-KEY-SLOT-ALLOWED-MODIFICATION
    L25782 (composes AR-OBJECT group + own group; attributeGroup AR-OBJECT) →
    Base most-derived = ARObject, claimed base correct; element group L25744
    carries the 4 attribute rows in displayed order: allowContentTypeChange
    (BOOLEAN 0..1), exportability (BOOLEAN 0..1), maxNumberOfAllowedUpdates
    (POSITIVE-INTEGER 0..1), restrictUpdate (BOOLEAN 0..1) — types/notes
    verbatim. Class Note = "This meta-class restricts the allowed modification
    of a key stored in the key slot." Tags: atp.Status=candidate. Aggregated by
    CryptoKeySlot.keySlotAllowedModification (0..1) via KEY-SLOT-ALLOWED-
    MODIFICATION; owns reusable read/writeCryptoKeySlotAllowedModification
    helpers called from read/writeCryptoKeySlot (Rule 0001.7 abstract
    XML-bearing base). No VARIATION-POINT → not VP-capable. Upstream doc:
    AUTOSAR_AP_TPS_PlatformModuleDeployment (AdaptivePlatform). Impl pre-exists
    (unstamped prior pass), matches XSD verbatim — no drift. Tracker review: no
    own section; the stale `CryptoKeySlot` `missing` row for
    keySlotAllowedModification was already removed with the CryptoObjectTypeEnum
    commit.
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - note (Steps 2–6): impl + reader/writer helpers pre-exist from the unstamped
    prior pass (reader populates via guarded setters, writer reads via getters,
    no chained mutators); new model tests written first this pass (class Note
    + all 4 getter/setter docstrings verbatim vs XSD, get_type_hints return
    pin) — the docstring test initially FAILED (multi-line setter docstrings
    carry per-line indentation that .strip() does not normalize) and was fixed
    to inspect.cleandoc — genuine Red→Green within this pass; round-trip
    coverage asserted through consumer CryptoKeySlot in test_crypto_key_slot.py
    parser/writer suites (field values + empty case + write→parse round-trip).
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - note (Step 8): no deviation — 4 spec rows → 4 PEP 526 fields + accessor
    pairs in displayed order, matched read/write helper names; the stale
    `CryptoKeySlot` tracker row referencing this class was removed with the
    CryptoObjectTypeEnum commit (Rule 0014).
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-27 (12458 passed / 0 failed, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

- [ ] `CryptoKeySlotContentAllowedUsage` — ARObject — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/AdaptivePlatform/PlatformModuleDeployment/CryptoDeployment/__init__.py
  - note: deviation-tracked in method_deviation_by_class.md — review entries at Step 1
  - note (Step 1): XSD-only — no `Class` table in R23-11 markdown, none in
    R4.3.1 markdown, pdf_page.py finds no PDF table (Rule 0016.3 fallback
    exhausted). XSD 00052: complexType CRYPTO-KEY-SLOT-CONTENT-ALLOWED-USAGE
    L25811 (composes AR-OBJECT group + own group; attributeGroup AR-OBJECT) →
    Base most-derived = ARObject, claimed base correct; element group L25795
    carries the single attribute row allowedKeyslotUsage (STRING 0..1, note
    verbatim "This attribute defines for which operations the KeySlot may be
    used."). Class Note = "This meta-class restricts the allowed usage of a key
    stored in the key slot." Tags: atp.Status=candidate. Aggregated by
    CryptoKeySlot.keySlotContentAllowedUsage (`*`, singular spec name → plural
    py list keySlotContentAllowedUsages + add/get accessors per Rule 0001.4)
    via KEY-SLOT-CONTENT-ALLOWED-USAGES wrapper / CRYPTO-KEY-SLOT-CONTENT-
    ALLOWED-USAGE items; owns reusable read/writeCryptoKeySlotContentAllowedUsage
    helpers called from read/writeCryptoKeySlot (Rule 0001.7). No
    VARIATION-POINT → not VP-capable. Upstream doc:
    AUTOSAR_AP_TPS_PlatformModuleDeployment (AdaptivePlatform). Impl pre-exists
    (unstamped prior pass), matches XSD verbatim — no drift. Tracker review: no
    own section; the stale `CryptoKeySlot` `missing` row for
    keySlotContentAllowedUsage was already removed with the CryptoObjectTypeEnum
    commit.
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - note (Steps 2–6): impl + reader/writer helpers pre-exist from the unstamped
    prior pass; new model tests written first this pass (class Note + getter/
    setter docstrings verbatim vs XSD via inspect.cleandoc, get_type_hints
    return pin) — pass with no source change (Red→Green collapsed); round-trip
    coverage asserted through consumer CryptoKeySlot in test_crypto_key_slot.py
    parser/writer suites (two-item wrapper list with per-item values + empty
    case + write→parse round-trip).
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - note (Step 8): no deviation — 1 spec row → 1 PEP 526 field + accessor pair,
    singular-spec/plural-py list shape per Rule 0001.4, matched read/write
    helper names; the stale `CryptoKeySlot` tracker row referencing this class
    was removed with the CryptoObjectTypeEnum commit (Rule 0014).
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-27 (12460 passed / 0 failed, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

- [ ] `DataLinkLayerRule` — ARObject — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/AdaptivePlatform/PlatformModuleDeployment/Firewall/__init__.py
  - note: deviation-tracked in method_deviation_by_class.md — review entries at Step 1
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `NetworkLayerRule` — ARObject — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/AdaptivePlatform/PlatformModuleDeployment/Firewall/__init__.py
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `TransportLayerRule` — ARObject — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/AdaptivePlatform/PlatformModuleDeployment/Firewall/__init__.py
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `PayloadBytePatternRule` — ARObject — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/AdaptivePlatform/PlatformModuleDeployment/Firewall/__init__.py
  - note: deviation-tracked in method_deviation_by_class.md — review entries at Step 1
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `SomeipProtocolRule` — ARObject — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/AdaptivePlatform/PlatformModuleDeployment/Firewall/__init__.py
  - note: deviation-tracked in method_deviation_by_class.md — review entries at Step 1
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `SomeipSdRule` — ARObject — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/AdaptivePlatform/PlatformModuleDeployment/Firewall/__init__.py
  - note: deviation-tracked in method_deviation_by_class.md — review entries at Step 1
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `DoIpRule` — ARObject — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/AdaptivePlatform/PlatformModuleDeployment/Firewall/__init__.py
  - note: deviation-tracked in method_deviation_by_class.md — review entries at Step 1
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `MemorySection` — Identifiable — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/MemorySectionUsage.py
  - note: deviation-tracked in method_deviation_by_class.md — review entries at Step 1
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `SectionNamePrefix` — ImplementationProps — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/MemorySectionUsage.py
  - note: deviation-tracked in method_deviation_by_class.md — review entries at Step 1
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `HardwareConfiguration` — ARObject — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/__init__.py
  - note: deviation-tracked in method_deviation_by_class.md — review entries at Step 1
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `SoftwareContext` — ARObject — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/__init__.py
  - note: deviation-tracked in method_deviation_by_class.md — review entries at Step 1
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [x] `DltApplication` — Identifiable — already verified (# Spec verified: R23-11, LogAndTraceExtract.py)
  - module: M2/AUTOSARTemplates/LogAndTraceExtract.py
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [x] `DltArgument` — Identifiable — already verified (# Spec verified: R23-11, LogAndTraceExtract.py)
  - module: M2/AUTOSARTemplates/LogAndTraceExtract.py
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [x] `DltContext` — ARElement — already verified (# Spec verified: R23-11, LogAndTraceExtract.py)
  - module: M2/AUTOSARTemplates/LogAndTraceExtract.py
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `SoAdRoutingGroup` — FibexElement — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/ObsoleteModel.py
  - note: deviation-tracked in method_deviation_by_class.md — review entries at Step 1
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `StackUsage` — Identifiable — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/StackUsage.py
  - note: deviation-tracked in method_deviation_by_class.md — review entries at Step 1
  - after `HardwareConfiguration`
  - after `SoftwareContext`
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `MeasuredStackUsage` — StackUsage — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/StackUsage.py
  - note: deviation-tracked in method_deviation_by_class.md — review entries at Step 1
  - after `StackUsage`
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `RoughEstimateStackUsage` — StackUsage — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/StackUsage.py
  - note: deviation-tracked in method_deviation_by_class.md — review entries at Step 1
  - after `StackUsage`
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `WorstCaseStackUsage` — StackUsage — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/StackUsage.py
  - note: deviation-tracked in method_deviation_by_class.md — review entries at Step 1
  - after `StackUsage`
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

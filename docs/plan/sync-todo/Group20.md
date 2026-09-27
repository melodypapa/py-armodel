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
  - note (Step 1): XSD-only — no `Class` table in R23-11 markdown, none in R4.3.1
    markdown, pdf_page.py finds no PDF table (Rule 0016.3 fallback exhausted).
    XSD 00052: complexType DATA-LINK-LAYER-RULE L27236 (abstract="false";
    element group L27182 carries the attribute rows) → Base most-derived =
    ARObject, claimed base correct; attribute rows in group sequence order:
    destinationMacAddress (MAC-ADDRESS-STRING 0..1), destinationMacAddressMask
    (MAC-ADDRESS-STRING 0..1), etherType (POSITIVE-INTEGER 0..1),
    sourceMacAddress (MAC-ADDRESS-STRING 0..1), sourceMacAddressMask
    (MAC-ADDRESS-STRING 0..1), vlanId (POSITIVE-INTEGER 0..1), vlanPriority
    (POSITIVE-INTEGER 0..1) — notes verbatim. Class Note = "Configuration of
    filter rules on the DataLink layer" Tags: atp.Status=candidate. Aggregated
    by FirewallRule.dataLinkLayerRule (0..1). No VARIATION-POINT → not
    VP-capable. Upstream doc: AUTOSAR_AP_TPS_PlatformModuleDeployment
    (AdaptivePlatform). Drift vs prior markdown-minimal impl: all 7 fields were
    Optional[str] → re-typed to Optional[MacAddressString]/Optional[PositiveInteger]
    (Rule 0001.3 conformance fix, not a deviation); members reordered to the XSD
    group sequence (was etherType-first); setters were unguarded → None-no-op.
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - note (Steps 5/6): readFirewallRule previously created a bare
    DataLinkLayerRule() (identity-only child, Rule 0001.7 debt); now routes
    through new reusable readDataLinkLayerRule/writeDataLinkLayerRule helpers
    (reader populates via guarded setters with the MacSecLocalKayProps
    MacAddressString conversion pattern; writer emits the 7 children in XSD
    sequence order via setChildElementOptionalLiteral/PositiveInteger). New
    test_data_link_layer_rule.py parser suite (4 tests) + writer suite
    (4 tests: values, XSD order, partial/empty cases, write→parse round-trip)
    pass; Red→Green verified (5 failed before parser/writer update).
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - note (Step 8): no open deviation for this class — re-typing/ordering/setter
    guards are Rule 0001.3/1.11/1.4 conformance; the stale `dataLinkLayerRule
    missing` row in the `FirewallRule` tracker section was removed per Rule
    0014. Reader/writer coverage note: referenced member types
    MacAddressString/PositiveInteger already exist in PrimitiveTypes.
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-27 (12470 passed / 0 failed, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

- [ ] `NetworkLayerRule` — ARObject — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/AdaptivePlatform/PlatformModuleDeployment/Firewall/__init__.py
  - note (Step 1): XSD-only — no `Class` table in R23-11 markdown, none in R4.3.1
    markdown, pdf_page.py finds no PDF table (Rule 0016.3 fallback exhausted).
    XSD 00052: element group NETWORK-LAYER-RULE L84252 with `<xsd:sequence/>`
    (empty) and NO complexType → abstract class, Base most-derived = ARObject
    (claimed base correct); zero own attribute rows. Class Note =
    "Configuration of filter rules on the Network layer" Tags:
    atp.Status=candidate. Aggregated by FirewallRule.networkLayerRule (0..1),
    whose element wraps a choice of the concrete subtypes IPV-4-RULE
    (complexType L74487, group L74389) / IPV-6-RULE (complexType L75007, group
    L74941) — Ipv4Rule/Ipv6Rule not in the codebase: reported missing per Rule
    0001.10, class kept instantiable as the aggregation placeholder (abstract
    TypeError guard + five-place dispatch deferred to the subtype sync; the
    guard now would crash the existing placeholder reader path). No
    VARIATION-POINT → not VP-capable. Upstream doc:
    AUTOSAR_AP_TPS_PlatformModuleDeployment (AdaptivePlatform). Drift: stale
    placeholder docstring "Configuration of rules on the Network Layer"
    (FirewallRule attribute Note, not the class Note) → wiped and rewritten.
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - note (Steps 5/6): Steps 5/6 completed as round-trip coverage of the
    identity-only placeholder serialization inside read/writeFirewallRule —
    the class has an empty group (no own XML-bearing attributes), so per Rule
    0001.7 no own read/writeNetworkLayerRule helpers are owed; parser/writer
    unchanged. New test_network_layer_rule.py parser suite (3 tests: element
    present w/ subtype child, absent, empty) + writer suite (3 tests: emitted
    when set, omitted when None, write→parse round-trip) pass against the
    existing wiring (Red→Green collapsed).
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - note (Step 8): no own tracker section; the `FirewallRule` tracker row
    `networkLayerRule | Ipv4Rule | missing` stays — it refers to the concrete
    subtype Ipv4Rule, which is still not implemented (missing referenced
    classes: Ipv4Rule, Ipv6Rule, reported per Rule 0001.10).
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-27 (12479 passed / 0 failed, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

- [ ] `TransportLayerRule` — ARObject — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/AdaptivePlatform/PlatformModuleDeployment/Firewall/__init__.py
  - note (Step 1): XSD-only — no `Class` table in R23-11 markdown, none in R4.3.1
    markdown, pdf_page.py finds no PDF table (Rule 0016.3 fallback exhausted).
    XSD 00052: element group TRANSPORT-LAYER-RULE L126190 with its 5 attribute
    rows belonging to the concrete subtypes (no own rows) and NO complexType →
    abstract class, Base most-derived = ARObject (claimed base correct); zero
    own attribute rows. Class Note = "Configuration of filter rules on
    Transport Layer level." Tags: atp.Status=candidate. Aggregated by
    FirewallRule.transportLayerRule (0..1), whose element wraps a choice of the
    concrete subtypes TCP-RULE (group L120616, complexType L120644) / UDP-RULE
    (group L127866, complexType L127875) — TcpRule/UdpRule not in the codebase:
    reported missing per Rule 0001.10, class kept instantiable as the
    aggregation placeholder (abstract TypeError guard + five-place dispatch
    deferred to the subtype sync; the guard now would crash the existing
    placeholder reader path). No VARIATION-POINT → not VP-capable. Upstream
    doc: AUTOSAR_AP_TPS_PlatformModuleDeployment (AdaptivePlatform). Drift:
    stale placeholder docstring "Configuration of rules on the Transport
    Layer" (FirewallRule attribute Note, not the class Note) → wiped and
    rewritten.
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - note (Steps 5/6): Steps 5/6 completed as round-trip coverage of the
    identity-only placeholder serialization inside read/writeFirewallRule —
    the class has an empty own group (no own XML-bearing attributes), so per
    Rule 0001.7 no own read/writeTransportLayerRule helpers are owed;
    parser/writer unchanged. New test_transport_layer_rule.py parser suite
    (3 tests: element present w/ subtype child, absent, empty) + writer suite
    (3 tests: emitted when set, omitted when None, write→parse round-trip)
    pass against the existing wiring (Red→Green collapsed).
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - note (Step 8): no own tracker section; the `FirewallRule` tracker row
    `transportLayerRule | TcpRule | missing` stays — it refers to the concrete
    subtype TcpRule, which is still not implemented (missing referenced
    classes: TcpRule, UdpRule, reported per Rule 0001.10).
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-27 (12488 passed / 0 failed, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

- [ ] `PayloadBytePatternRule` — ARObject — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/AdaptivePlatform/PlatformModuleDeployment/Firewall/__init__.py
  - note: deviation-tracked in method_deviation_by_class.md — review entries at Step 1
  - note (Step 1): XSD-only — no `Class` table in R23-11 markdown (only the FirewallRule
    Table 6.236 `payloadBytePatternRule 0..*` attribute row references the type), none in
    R4.3.1 markdown, pdf_page.py finds no PDF table (Rule 0016.3 fallback exhausted).
    XSD 00052: group PAYLOAD-BYTE-PATTERN-RULE L88452 + complexType L88473; class Note =
    "Configuration of a generic firewall rule that defines the individual bytes of a
    message that shall match." Tags: atp.Status=candidate; single member
    payloadBytePatternRulePart (0..*, wrapper PAYLOAD-BYTE-PATTERN-RULE-PARTS >
    PAYLOAD-BYTE-PATTERN-RULE-PART items). Part type PayloadBytePatternRulePart is in the
    Rule 0016.1 closure (aggregated child, XSD-only, same package) — implemented fully in
    the same commit (offset/value PositiveInteger, L88508) though not a queued row
    (flagged decision).
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - note (Steps 5/6): reader readPayloadBytePatternRule/readPayloadBytePatternRulePart +
    writer writePayloadBytePatternRule/writePayloadBytePatternRulePart new; readFirewallRule
    upgraded from empty-placeholder loop to full nested read (wrapper PAYLOAD-BYTE-PATTERN-RULES
    > PAYLOAD-BYTE-PATTERN-RULE > PAYLOAD-BYTE-PATTERN-RULE-PARTS > PAYLOAD-BYTE-PATTERN-RULE-PART
    per XSD L59059/L88459); FirewallRule checklist reader/writer columns for
    addPayloadBytePatternRule/getPayloadBytePatternRules flipped to real coverage; new
    test_payload_byte_pattern_rule.py parser suite (5 tests) + writer suite (5 tests) pass.
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - note (Step 8): stale `payloadBytePatternRule` missing row removed from the
    method_deviation_by_class.md FirewallRule section (Rule 0014); no open deviations —
    verbatim XSD docstrings restored, Optional[T] annotations, 6-col checklists written
    for both classes (no stamp markers per batch mode).
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-27 (77 passed / 0 failed, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

- [ ] `SomeipProtocolRule` — ARObject — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/AdaptivePlatform/PlatformModuleDeployment/Firewall/__init__.py
  - note: deviation-tracked in method_deviation_by_class.md — review entries at Step 1
  - note (Step 1): XSD-only — no `Class` table in R23-11 markdown (only the FirewallRule
    Table 6.236 `someipRule 0..1` attribute row references the type), none in R4.3.1
    markdown, pdf_page.py finds no PDF table (Rule 0016.3 fallback exhausted). XSD 00052:
    group SOMEIP-PROTOCOL-RULE L110026 + complexType L110084; class Note = "Configuration
    of SOME/IP firewall rules" Tags: atp.Status=candidate; 8 members 0..1 in XSD order:
    clientId, lengthVerification (AR:BOOLEAN), majorVersion, messageType, methodId,
    protocolVersion, returnCode, serviceInterfaceId (XSD notes carry verbatim double-space
    quirks "majorVersion  in" / "protocolVersion  in" / "returnCode  in" — kept).
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - note (Steps 5/6): read/writeSomeipProtocolRule new (8 attrs, XSD order;
    LENGTH-VERIFICATION via getChildElementOptionalBooleanValue /
    setChildElementOptionalBooleanValue per Pdu.hasDynamicLength precedent);
    readFirewallRule upgraded from empty-placeholder to full read, writeFirewallRule from
    empty SOMEIP-RULE SubElement to full write; new test_someip_protocol_rule.py parser
    suite (4 tests) + writer suite (4 tests) pass.
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - note (Step 8): stale `someipRule` missing row removed from the
    method_deviation_by_class.md FirewallRule section (Rule 0014); no open deviations —
    verbatim XSD docstrings restored (incl. double-space quirks), Optional[T]
    annotations, 6-col checklist written (no stamp markers per batch mode).
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-27 (90 passed / 0 failed, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

- [ ] `SomeipSdRule` — ARObject — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/AdaptivePlatform/PlatformModuleDeployment/Firewall/__init__.py
  - note: deviation-tracked in method_deviation_by_class.md — review entries at Step 1
  - note (Step 1): XSD-only — no `Class` table in R23-11 markdown (only the FirewallRule
    Table 6.236 `someipSdRule 0..1` attribute row references the type), none in R4.3.1
    markdown, pdf_page.py finds no PDF table (Rule 0016.3 fallback exhausted). XSD 00052:
    group SOMEIP-SD-RULE L110594 + complexType L110652; class Note = "Configuration of
    SOME/IP Service Discovery firewall rules" Tags: atp.Status=candidate; 8 members 0..1
    POSITIVE-INTEGER in XSD order: entryType, eventGroupId, maxMajorVersion,
    maxMinorVersion, minMajorVersion, minMinorVersion, serviceInstanceId,
    serviceInterfaceId.
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - note (Steps 5/6): read/writeSomeipSdRule new (8 attrs, XSD order);
    readFirewallRule upgraded from empty-placeholder to full read, writeFirewallRule
    from empty SOMEIP-SD-RULE SubElement to full write; new test_someip_sd_rule.py
    parser suite (4 tests) + writer suite (4 tests) pass.
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - note (Step 8): stale `someipSdRule` missing row removed from the
    method_deviation_by_class.md FirewallRule section (Rule 0014); no open deviations —
    verbatim XSD docstrings restored, Optional[T] annotations, 6-col checklist written
    (no stamp markers per batch mode).
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-27 (95 passed / 0 failed, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

- [ ] `DoIpRule` — ARObject — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/AdaptivePlatform/PlatformModuleDeployment/Firewall/__init__.py
  - note: deviation-tracked in method_deviation_by_class.md — review entries at Step 1
  - note (Step 1): XSD-only — no `Class` table in R23-11 markdown (only the FirewallRule
    Table 6.236 `doIpRule 0..1` attribute row references the type), none in R4.3.1
    markdown, pdf_page.py finds no PDF table (Rule 0016.3 fallback exhausted). XSD 00052:
    group DO-IP-RULE L49263 + complexType L49327; class Note = "Configuration of a
    generic firewall rule" Tags: atp.Status=candidate; 9 members 0..1 POSITIVE-INTEGER in
    XSD order: destinationMaxAddress, destinationMinAddress, inverseProtocolVersion,
    payloadLength, payloadType, protocolVersion, sourceMaxAddress, sourceMinAddress,
    udsService (XSD notes carry verbatim quirks — double spaces "messages  in which" on
    inverseProtocolVersion/payloadLength/payloadType/protocolVersion, lowercase
    "inverseprotocolVersion" on inverseProtocolVersion, trailing ".." on sourceMinAddress —
    all kept).
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - note (Steps 5/6): read/writeDoIpRule new (9 attrs, XSD order); readFirewallRule
    upgraded from empty-placeholder to full read, writeFirewallRule from empty DO-IP-RULE
    SubElement to full write; new test_do_ip_rule.py parser suite (4 tests) + writer
    suite (4 tests) pass.
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - note (Step 8): stale `doIpRule` missing row removed from the
    method_deviation_by_class.md FirewallRule section (Rule 0014); no open deviations —
    verbatim XSD docstrings restored (incl. whitespace quirks), Optional[T] annotations,
    6-col checklist written (no stamp markers per batch mode).
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-27 (108 passed / 0 failed, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

- [ ] `MemorySection` — Identifiable — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/MemorySectionUsage.py
  - note: deviation-tracked in method_deviation_by_class.md — review entries at Step 1
  - [x] Step 1 — Sync members & description from spec
  - note (Step 1): Table 8.2, p.144 (R23-11; old checklist said p.143 — corrected via
    pdf_page.py), Base = ARObject, Identifiable, MultilanguageReferrable, Referrable
    (most-derived Identifiable per Rule 0001.2); 7 members in markdown order: alignment
    (AlignmentType 0..1), executableEntity (Ref ExecutableEntity 0..*), option (Identifier
    0..*), prefix (Ref SectionNamePrefix 0..1), size (PositiveInteger 0..1), swAddrmethod
    (Ref SwAddrMethod 0..1), symbol (Identifier 0..1); memClassSymbol absent from the R23-11
    attribute rows but present in R4.3.1 Table 9.2, p.145 and in the R23-11 XSD
    (MEM-CLASS-SYMBOL atp.Status="removed", group MEMORY-SECTION, AUTOSAR_00052.xsd L80899)
    → Rule 0019 combine case, kept as legacy member; cross-checked vs SWComponentTemplate
    Tables 5.89/5.90 (same sets/order).
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - note (Steps 2-4): test_MemorySectionUsage.py extended — verbatim Note constants, base
    chain, initialization defaults, get_type_hints annotations, get/set + None-no-op
    round-trips, full-docstring assertions for both classes of the module; initial run
    5 failed / 13 passed (genuine Red on the old paraphrased docstrings), 18 passed after
    the verbatim rewrite.
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - note (Steps 5/6): new parser suite tests/test_armodel/parser/test_memory_section_usage.py
    (TestReadMemorySections, 4 tests) + writer suite tests/test_armodel/writer/
    test_memory_section_usage.py (TestWriteMemorySections, 4 tests); reader retyped to
    getChildElementOptionalAlignmentType / getChildElementOptionalCIdentifier /
    getChildElementIdentifierValueList / getChildElementOptionalIdentifier (new typed
    helpers in abstract_arxml_parser.py), writer to setChildElementOptionalAlignmentType /
    setChildElementOptionalCIdentifier / setChildElementOptionalIdentifier (new typed
    helpers in abstract_arxml_writer.py); VARIATION-POINT emission moved after SYMBOL
    (writeIdentifiable with write_variation_point=False + trailing writeVariationPoint)
    per XSD seqOffset=10000; round-trip run 8 failed / 8 passed Red → all Green.
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - note (Step 8): method_deviation_by_class.md MemorySection section rewritten — full
    6-column member table, page corrected 143→144, memClassSymbol recorded as accepted
    legacy (R4.3.1 Table 9.2, p.145) Rule 0019 deviation; swAddrMethodRef naming kept for
    cross-class consistency with stamped siblings (flagged decision).
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-27 (12579 passed / 0 failed, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

- [ ] `SectionNamePrefix` — ImplementationProps — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/MemorySectionUsage.py
  - note: deviation-tracked in method_deviation_by_class.md — review entries at Step 1
  - [x] Step 1 — Sync members & description from spec
  - note (Step 1): Table 8.8, p.147 (R23-11), Base = ARObject, ImplementationProps,
    Referrable (most-derived ImplementationProps per Rule 0001.2); single member
    implementedIn (Ref DependencyOnArtifact 0..1) → implementedInRef (Rule 0001.5);
    inherited symbol covered by the IMPLEMENTATION-PROPS group (AUTOSAR_00052.xsd
    L102807 group SECTION-NAME-PREFIX / L102840 complexType); class Note cross-checked
    vs SWComponentTemplate Table 5.90 (same row set).
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - note (Steps 2-4): shared test_MemorySectionUsage.py — verbatim Note constants, base
    chain (ImplementationProps), initialization defaults, get/set + None-no-op round-trip,
    full-docstring assertions.
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - note (Steps 5/6): parser suite TestReadSectionNamePrefixes (3 tests) + writer suite
    TestWriteSectionNamePrefixes (5 tests) in the new tests/test_armodel/{parser,writer}/
    test_memory_section_usage.py files; reader switched readReferrable →
    readImplementationProps so the inherited SYMBOL round-trips (Rule 0001.7) and
    VARIATION-POINT read added (Referrable-level VP, per the readBswModuleCallPoint
    precedent); writer switched writeReferrable → writeImplementationProps + trailing
    writeVariationPoint (XSD group order REFERRABLE → IMPLEMENTATION-PROPS →
    SECTION-NAME-PREFIX → VARIATION-POINT); Red (SYMBOL/VARIATION-POINT dropped) → all
    Green.
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - note (Step 8): method_deviation_by_class.md SectionNamePrefix section rewritten —
    6-column member table (implementedInRef ok per Rule 0001.5); no open deviations.
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-27 (12579 passed / 0 failed, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

- [ ] `HardwareConfiguration` — ARObject — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/__init__.py
  - note: deviation-tracked in method_deviation_by_class.md — review entries at Step 1
  - note (Step 1): Table 8.18, p.161 (R23-11, AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate;
    pdf_page.py confirms p.161); Class = HardwareConfiguration (concrete; XSD stereotype
    atpObject); Package = M2::AUTOSARTemplates::CommonStructure::ResourceConsumption;
    Note = "Describes in which mode the hardware is operating while needing this resource
    consumption."; Base = ARObject → claimed base correct (closure tip); Aggregated by
    ExecutionTime/HeapUsage/StackUsage .hardwareConfiguration; 3 attribute rows in
    displayed order: additionalInformation (String 0..1 attr — md Note renders "Hardware
    Configuration", a line-wrap artifact of "HardwareConfiguration" per the XSD
    documentation), processorMode (String 0..1 attr), processorSpeed (String 0..1 attr).
    XSD 00052: group HARDWARE-CONFIGURATION L65234 (complexType L65262) = ADDITIONAL-
    INFORMATION, PROCESSOR-MODE, PROCESSOR-SPEED (all 0..1 STRING); no VARIATION-POINT →
    table and XSD agree 1:1, no XSD-only attrs. Drift: __init__ docstring present,
    paraphrase accessor docstrings, member comments carried constraint texts
    (constr_10315..10317) beyond the Note, stale 4-col checklist.
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - note (Steps 2-4): test_ResourceConsumption.py::TestHardwareConfiguration rewritten —
    verbatim Note constants, base chain, defaults, get_type_hints annotations, get/set +
    None-no-op round-trip, __init__-has-no-docstring, full verbatim docstring assertions;
    initial run 3 failed / 5 passed (genuine Red: wrapped class docstring, __init__
    docstring, paraphrase accessors), 8 passed after the verbatim rewrite.
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - note (Steps 5/6): readHardwareConfiguration / setHardwareConfiguration pre-existed
    (setters/getters, matched-name pairs, XSD group order) — no parser/writer change; new
    tests/test_armodel/parser/test_hardware_configuration.py (TestReadHardwareConfiguration,
    3 tests: field values, absent + partial children) and tests/test_armodel/writer/
    test_hardware_configuration.py (TestWriteHardwareConfiguration, 4 tests: field values,
    XSD element order, None-config omission, write→parse round-trip) pass; round-trip
    serializes with the AUTOSAR default namespace for the namespace-aware find.
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - note (Step 8): method_deviation_by_class.md HardwareConfiguration section rewritten —
    6-column member table (all ok), source path corrected from the nonexistent
    HardwareConfiguration.py to the package __init__.py; no open deviations.
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-27 (12589 passed / 0 failed, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

- [ ] `SoftwareContext` — ARObject — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/__init__.py
  - note: deviation-tracked in method_deviation_by_class.md — review entries at Step 1
  - note (Step 1): Table 8.20, p.163 (R23-11, AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate;
    pdf_page.py confirms p.163); Class = SoftwareContext (concrete; XSD stereotype
    atpObject); Package = M2::AUTOSARTemplates::CommonStructure::ResourceConsumption;
    Note = "Specifies the context of the software for this resource consumption.";
    Base = ARObject → claimed base correct (closure tip); Aggregated by
    ExecutionTime/HeapUsage/StackUsage .softwareContext; 2 attribute rows in displayed
    order: input (String 0..1 attr), state (String 0..1 attr — md Note renders "the
    Execution Time is provided", a line-wrap artifact of "ExecutionTime" per the XSD
    documentation). XSD 00052: group SOFTWARE-CONTEXT L109295 (complexType L109317) =
    INPUT, STATE (both 0..1 STRING); no VARIATION-POINT → table and XSD agree 1:1, no
    XSD-only attrs. Drift: __init__ docstring present, paraphrase accessor docstrings,
    stale 4-col checklist.
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - note (Steps 2-4): test_ResourceConsumption.py::TestSoftwareContext rewritten —
    verbatim Note constants, base chain, defaults, get_type_hints annotations, get/set +
    None-no-op round-trip, __init__-has-no-docstring, full verbatim docstring assertions;
    initial run 2 failed / 6 passed (genuine Red: __init__ docstring, paraphrase
    accessors), all passed after the verbatim rewrite.
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - note (Steps 5/6): readSoftwareContext / setSoftwareContext pre-existed (setters/
    getters, matched-name pairs, XSD group order) — no parser/writer change; new
    tests/test_armodel/parser/test_software_context.py (TestReadSoftwareContext, 3 tests:
    field values, absent + partial children) and tests/test_armodel/writer/
    test_software_context.py (TestWriteSoftwareContext, 4 tests: field values, XSD
    element order, None-context omission, write→parse round-trip) pass.
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - note (Step 8): method_deviation_by_class.md SoftwareContext section rewritten —
    6-column member table (all ok), source path corrected from the nonexistent
    SoftwareContext.py to the package __init__.py; no open deviations.
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-27 (12600 passed / 0 failed, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

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
  - note (Step 1): Table F.115 p.2057 (appendix, md L75702-75710 of
    AUTOSAR_CP_TPS_SystemTemplate.md; PDF page confirmed via pypdf — pdf_page.py
    regex misses F.NN captions): Class = SoAdRoutingGroup (atp.Status=obsolete);
    Package = M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::
    ObsoleteModel (repo location matches spec's own package — Rule 0007 in
    place); Note = "Routing of Pdus in the SoAd can be activated or
    deactivated. The ShortName of this element shall contain the RoutingGroupId.
    Tags: atp.Status=obsolete atp.recommendedPackage=SoAdRoutingGroups"; Base =
    "ARObject, CollectableElement, FibexElement, Identifiable,
    MultilanguageReferrable, PackageableElement, Referrable" → most-derived
    FibexElement (claimed base correct; CollectableElement not in Python chain
    is a FibexElement-level matter); Aggregated by ARPackage.element; 1
    attribute: eventGroupControlType (EventGroupControlTypeEnum, 0..1, attr).
    XSD 00052: group SO-AD-ROUTING-GROUP = single EVENT-GROUP-CONTROL-TYPE
    (0..1), no atp.Status=removed members; XML order = base groups then
    EVENT-GROUP-CONTROL-TYPE last (matches writer). R23-11 is the primary
    corpus (R4.3.1 Table 6.125 p.323 exists but Rule 0016.3 fallback not
    needed). Member type EventGroupControlTypeEnum pre-exists in
    ServiceInstances.py with the 4 spec literals — reused, not a stub. Drift
    fixed: fabricated class docstring, bare field annotation, untyped
    accessors, stale checklist. Import note: top-level
    `from ...ServiceInstances import EventGroupControlTypeEnum` added to
    ObsoleteModel.py — safe (no model module runtime-imports ObsoleteModel;
    ARPackage fully loads before models/__init__ L102).
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - note (Steps 5/6): readSoAdRoutingGroup (readIdentifiable +
    getChildElementOptionalLiteral EVENT-GROUP-CONTROL-TYPE →
    EventGroupControlTypeEnum.setValue → setEventGroupControlType) and
    writeSoAdRoutingGroup (SO-AD-ROUTING-GROUP SubElement + writeIdentifiable +
    setChildElementOptionalLiteral via getEventGroupControlType) pre-existed
    with matched-name pairs — no parser/writer changes needed; new
    test_so_ad_routing_group.py (5 tests: write all fields, empty omits
    optional tag, ET round-trip, reader empty, full-document round-trip via
    ARPackage) and typed-literal parser test pass immediately.
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - note (Step 8): no own method_deviation_by_class.md section exists for this
    class; referenced-type mentions in MethodActivationRoutingGroup /
    EventHandler deviation rows remain valid; no new deviations — verbatim
    docstrings restored, Optional[T] annotation + typed accessors, 6-col
    checklist written (no stamp markers per batch mode). Did NOT add
    `from __future__ import annotations` (would break sibling
    SocketConnection's top-level quoted annotations); setter self-return stays
    quoted per module convention.
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-27 (12611 passed / 0 failed, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

- [ ] `StackUsage` — Identifiable — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/StackUsage.py
  - note: deviation-tracked in method_deviation_by_class.md — review entries at Step 1
  - after `HardwareConfiguration`
  - after `SoftwareContext`
  - note (Step 1): Table 8.9, p.149 (R23-11, AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate;
    pdf_page.py confirms p.149); Class = StackUsage (abstract — abstract guard kept; the
    reader instantiates only subclasses via the readStackUsages tag dispatch); Package =
    M2::AUTOSARTemplates::CommonStructure::ResourceConsumption::StackUsage; Note =
    "Describes the stack memory usage of a software."; Base = "ARObject, Identifiable,
    MultilanguageReferrable, Referrable" → most-derived Identifiable (claimed base
    correct); Subclasses = MeasuredStackUsage, RoughEstimateStackUsage,
    WorstCaseStackUsage; Aggregated by ResourceConsumption.stackUsage; 4 attribute rows
    in displayed order: executableEntity (ExecutableEntity, 0..1, ref →
    executableEntityRef per Rule 0001.5), hardwareConfiguration (HardwareConfiguration,
    0..1, aggr; md renders "hardware Configuration" — line-wrap artifact), hwElement
    (HwElement, 0..1, ref → hwElementRef), softwareContext (SoftwareContext, 0..1,
    aggr). XSD 00052: group STACK-USAGE L111994 = EXECUTABLE-ENTITY-REF,
    HARDWARE-CONFIGURATION, HW-ELEMENT-REF, SOFTWARE-CONTEXT, VARIATION-POINT
    (seqOffset=10000, atpIdentityContributor → VariationPointCapable mixin retained;
    readIdentifiable reads the VP). Table and XSD agree 1:1, no XSD-only attrs. Drift:
    fabricated class-docstring second sentence, __init__ docstrings, paraphrase accessor
    docstrings, stale 4-col checklist, TYPE_CHECKING-only HC/SC imports (get_type_hints
    NameError → Rule 0001.8), writer VP emitted inside the identifiable block, reader
    order EXEC → HW-ELEM → HW-CONFIG → SOFT-CTX vs XSD. Tracker review: the StackUsage
    section held ("No deviations") — refreshed with the member table.
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - note (Steps 2-4): TestStackUsage added (abstract-instantiation TypeError, base chain
    incl. the Subclasses row, verbatim Note constants, defaults via a concrete subclass,
    get_type_hints pins, get/set + None-no-op round-trips, __init__-has-no-docstring,
    verbatim docstrings); initial run 4 failed / 10 passed (genuine Red), 14 passed after
    the verbatim rewrite. HC/SC moved from TYPE_CHECKING-only to a bottom-of-module
    runtime cycle-breaker import (Rule 0005) with the parent __init__'s StackUsage import
    moved after the HC/SC class definitions so both import directions resolve.
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - note (Steps 5/6): new tests/test_armodel/parser/test_stack_usage.py (5 tests:
    polymorphic dispatch MEASURED/ROUGH/WORST-STACK-USAGE → subclass, inherited + own
    field values incl. VP shortLabel, empty + absent wrapper) + tests/test_armodel/
    writer/test_stack_usage.py (6 tests: dispatch tags + field values, XSD element order,
    VP write, empty usage omits optionals, empty list, write→parse round-trip). Red =
    VARIATION-POINT emitted inside the identifiable block → setStackUsage now uses
    writeIdentifiable(write_variation_point=False) + trailing writeVariationPoint after
    SOFTWARE-CONTEXT (MemorySection precedent, XSD seqOffset=10000); readStackUsage
    reordered to the XSD group order. 25 passed.
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - note (Step 8): no open deviations — the Rule 0005 import fix and the VP position fix
    are conformance, not deviations; tracker section refreshed (member table, all ok).
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-27 (12633 passed / 0 failed, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

- [ ] `MeasuredStackUsage` — StackUsage — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/StackUsage.py
  - note: deviation-tracked in method_deviation_by_class.md — review entries at Step 1
  - after `StackUsage`
  - note (Step 1): Table 8.11, p.150 (R23-11, AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate;
    pdf_page.py confirms p.150); Class = MeasuredStackUsage; Package =
    M2::AUTOSARTemplates::CommonStructure::ResourceConsumption::StackUsage; Note = "The
    stack usage has been measured."; Base = "ARObject, Identifiable, MultilanguageReferrable,
    Referrable, StackUsage" → most-derived StackUsage (claimed base correct);
    Aggregated by ResourceConsumption.stackUsage; 4 attribute rows in displayed order:
    averageMemoryConsumption (PositiveInteger, 0..1, attr; md renders "averageMemory
    Consumption" — line-wrap artifact), maximumMemoryConsumption (PositiveInteger, 0..1,
    attr; md renders "maximum Memory Consumption"), minimumMemoryConsumption
    (PositiveInteger, 0..1, attr; md renders "minimum Memory Consumption"), testPattern
    (String, 0..1, attr). XSD 00052: complexType MEASURED-STACK-USAGE L80881 + group
    MEASURED-STACK-USAGE L80847 = AVERAGE-MEMORY-CONSUMPTION, MAXIMUM-MEMORY-CONSUMPTION,
    MINIMUM-MEMORY-CONSUMPTION, TEST-PATTERN (reader/writer already in this order).
    Table and XSD agree 1:1, no XSD-only attrs. Drift: fabricated class-docstring second
    sentence, __init__ docstring, paraphrase accessor docstrings, testPattern inline Note
    ("The test pattern used to acquire..." vs spec "Description of the test pattern used
    to acquire..."), stale 4-col checklist. Tracker review: the MeasuredStackUsage section
    held ("No deviations") — refreshed with the member table.
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - note (Steps 2-4): TestMeasuredStackUsage extended (base chain, verbatim class Note,
    defaults, get_type_hints pins Optional[PositiveInteger]x3/Optional[String], 4 get/set +
    None-no-op round-trips, __init__-has-no-docstring, verbatim accessor docstrings with
    setter tails); initial run 3 failed / 20 passed (genuine Red: fabricated class-docstring
    second sentence, __init__ docstring, paraphrase accessor docstrings), 23 passed after
    the verbatim rewrite (Rule 0012.2 wipe + rewrite).
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - note (Steps 5/6): existing coverage from the Table 8.9 step already asserts all four
    fields end-to-end — parser test_read_measured_field_values (AVERAGE/MAXIMUM/MINIMUM/
    TEST-PATTERN values) and writer tests (field values, XSD element order incl. the
    AVERAGE→MAXIMUM→MINIMUM→TEST-PATTERN tail, empty-usage omits optionals, write→parse
    round-trip with value assertions); extended rather than duplicated — no new tests
    needed, reader/writer unchanged, 34 passed across the three test files.
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - note (Step 8): no open deviations — the docstring/Note drift fixes are conformance;
    tracker section refreshed (member table, all ok).
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-27 (12642 passed / 0 failed, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

- [ ] `RoughEstimateStackUsage` — StackUsage — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/StackUsage.py
  - note: deviation-tracked in method_deviation_by_class.md — review entries at Step 1
  - after `StackUsage`
  - note (Step 1): Table 8.12, p.151 (R23-11, AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate;
    pdf_page.py confirms p.151); Class = RoughEstimateStackUsage; Package =
    M2::AUTOSARTemplates::CommonStructure::ResourceConsumption::StackUsage; Note = "Rough
    estimation of the stack usage."; Base = "ARObject, Identifiable, MultilanguageReferrable,
    Referrable, StackUsage" → most-derived StackUsage (claimed base correct);
    Aggregated by ResourceConsumption.stackUsage; 1 attribute row: memoryConsumption
    (PositiveInteger, 0..1, attr; md renders "memory Consumption" — line-wrap artifact).
    XSD 00052: group ROUGH-ESTIMATE-STACK-USAGE L99477 = MEMORY-CONSUMPTION
    (complexType L99493). Table and XSD agree 1:1, no XSD-only attrs. Drift: fabricated
    class-docstring second sentence, __init__ docstring, paraphrase accessor docstrings,
    stale 4-col checklist. Tracker review: the RoughEstimateStackUsage section held
    ("No deviations") — refreshed with the member table.
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - note (Steps 2-4): TestRoughEstimateStackUsage extended (base chain, verbatim class
    Note, defaults, get_type_hints pin Optional[PositiveInteger], get/set + None-no-op
    round-trip, __init__-has-no-docstring, verbatim accessor docstrings with setter
    tails); initial run 3 failed / 26 passed (genuine Red: fabricated class-docstring
    second sentence, __init__ docstring, paraphrase accessor docstrings), 29 passed after
    the verbatim rewrite (Rule 0012.2 wipe + rewrite).
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - note (Steps 5/6): existing coverage from the Table 8.9 step already asserts the field
    end-to-end — parser test_read_rough_and_worst_field_values (MEMORY-CONSUMPTION value +
    inherited-optional absence) and writer tests (field value, write→parse round-trip with
    value assertion); extended rather than duplicated — no new tests needed, reader/writer
    unchanged, 40 passed across the three test files.
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - note (Step 8): no open deviations — the docstring drift fixes are conformance; tracker
    section refreshed (member table, all ok).
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-27 (12648 passed / 0 failed, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

- [ ] `WorstCaseStackUsage` — StackUsage — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/CommonStructure/ResourceConsumption/StackUsage.py
  - note: deviation-tracked in method_deviation_by_class.md — review entries at Step 1
  - after `StackUsage`
  - note (Step 1): Table 8.10, p.150 (R23-11, AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate;
    pdf_page.py confirms p.150); Class = WorstCaseStackUsage; Package =
    M2::AUTOSARTemplates::CommonStructure::ResourceConsumption::StackUsage; Note = "Provides
    a formal worst case stack usage."; Base = "ARObject, Identifiable, MultilanguageReferrable,
    Referrable, StackUsage" → most-derived StackUsage (claimed base correct);
    Aggregated by ResourceConsumption.stackUsage; 1 attribute row: memoryConsumption
    (PositiveInteger, 0..1, attr; md renders "memory Consumption" — line-wrap artifact;
    Note "Worst case stack consumption. Unit: byte." — distinct from RoughEstimate's).
    XSD 00052: group WORST-CASE-STACK-USAGE L130916 = MEMORY-CONSUMPTION (complexType
    L130932). Table and XSD agree 1:1, no XSD-only attrs. Drift: fabricated class-docstring
    second sentence, __init__ docstring, paraphrase accessor docstrings, stale 4-col
    checklist. Tracker review: the WorstCaseStackUsage section held ("No deviations") —
    refreshed with the member table.
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - note (Steps 2-4): TestWorstCaseStackUsage extended (base chain, verbatim class Note,
    defaults, get_type_hints pin Optional[PositiveInteger], get/set + None-no-op
    round-trip, __init__-has-no-docstring, verbatim accessor docstrings with setter
    tails); initial run 3 failed / 32 passed (genuine Red: fabricated class-docstring
    second sentence, __init__ docstring, paraphrase accessor docstrings), 35 passed after
    the verbatim rewrite (Rule 0012.2 wipe + rewrite).
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - note (Steps 5/6): existing coverage from the Table 8.9 step already asserts the fields
    end-to-end — parser test_read_rough_and_worst_field_values (MEMORY-CONSUMPTION value +
    EXECUTABLE-ENTITY-REF inheritance + optional absence) and writer tests (field values,
    empty-usage omits optionals, write→parse round-trip with value assertions); extended
    rather than duplicated — no new tests needed, reader/writer unchanged, 46 passed across
    the three test files.
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - note (Step 8): no open deviations — the docstring drift fixes are conformance; tracker
    section refreshed (member table, all ok).
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-27 (12654 passed / 0 failed, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

## Queue addendum — missing referenced classes (queued 2026-09-27, post-batch)

Appended per user instruction ("add the missing classes with 9-steps check into todo list")
after the member-closure audit of the 22 batch rows above. Dependency-first order; the
owning/base classes (DataLinkLayerRule, PayloadBytePatternRule, TransportLayerRule) are
synced above (stamps deferred to the batch 9b). Ipv4Rule/Ipv6Rule (PDF Table 6.236
networkLayerRule type column) were queued at the end of this addendum per user arbitration
2026-09-27 ("Enqueue both") under a NON-STANDARD-source premise ("XSD-absent in
00052/00044; markdown has only ECUC-mapping appendix mentions") — that premise was WRONG:
both classes ARE XSD-defined in 00052 under the dashed spellings IPV-4-RULE (group L74389,
complexType L74485) / IPV-6-RULE (group L74941, complexType L75007); the rows below are
amended to XSD-only per Rule 0015 (markdown ECUC-mapping appendix demoted to supplementary
evidence) and the classes synced (stamps deferred to the batch 9b). The `... | missing`
tracker rows they motivated (`networkLayerRule | Ipv4Rule | missing`,
`transportLayerRule | TcpRule | missing`) are resolved — the classes landed.

- [x] `MacAddressString` — ARLiteral — R23-11 markdown · Table 4.53 (FO_TPS_GenericStructureTemplate)
  - module: M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/PrimitiveTypes.py
  - note: member type of DataLinkLayerRule (destinationMacAddress/-Mask, sourceMacAddress/-Mask
    re-typed from Optional[str] this batch); exists unstamped — queued per Rule 0016.4
    (exists ≠ stamp)
  - note (Step 1): Table 4.53 "MacAddressString", AUTOSAR_FO_TPS_GenericStructureTemplate.md
    L2981 (R4.3.1 fallback Table 4.64 L2395). src has docstring + Tags (pattern
    ([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}, customType MAC-ADDRESS-STRING, xsd type string) but
    stale 4-col checklist and no stamp — Step 1 cross-checks docstring/Tags verbatim against
    the table (Rule 0002).
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - note (Steps 2-4): TestMacAddressString added to test_PrimitiveTypes.py (initialization,
    setValue round-trip + chaining, verbatim hex-pair storage, class-docstring verbatim check);
    initial run 1 failed / 3 passed (genuine Red: the Table 4.53 Note was line-wrapped, not
    verbatim), 4 passed after the single-line verbatim rewrite. Implementation was already
    complete per spec (bare ARLiteral subclass; the Primitive table has no Attribute rows) —
    Step 3 confirmed no drift; Step 4 rewrote the docstring.
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - note (Steps 5/6): the MAC reader/writer path was already implemented by the
    DataLinkLayerRule re-type (parser readDataLinkLayerRule instantiates MacAddressString for
    the four MAC elements; writer writes via setChildElementOptionalLiteral) — existing
    parser/writer DataLinkLayerRule tests extended with MacAddressString isinstance assertions
    on all four MAC fields rather than duplicated (8 passed across both files); no parser/writer
    source change needed.
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - note (Step 8): no open deviations — the Table 4.53 Note line-wrap fix is conformance;
    checklist replaced with the 6-column format (no stamp line — batch 9b pending).
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-27 (12663 passed / 0 failed, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

- [x] `PayloadBytePatternRulePart` — ARObject — XSD-only (00052 complexType L88508)
  - module: M2/AUTOSARTemplates/AdaptivePlatform/PlatformModuleDeployment/Firewall/__init__.py
  - note: aggregated member of PayloadBytePatternRule (payloadBytePatternRulePart 0..*) —
    implemented fully (offset/value PositiveInteger) + reader/writer + tests in 8f863fe9d
    (the owner's Step 1 note flagged this as a queued-row decision); row covers the
    remaining verification/stamp flow per Rule 0016.4 (exists ≠ stamp) — re-run only the
    steps the Rule 0002 cross-check fails
  - note (Step 1): XSD 00052 complexType PAYLOAD-BYTE-PATTERN-RULE-PART L88508; wrapper
    PAYLOAD-BYTE-PATTERN-RULE-PARTS L88459 (owner group L88452, complexType L88473); no
    table in either corpus — Rule 0015 XSD-only.
  - note (verified 2026-09-27): XSD cross-check pass — offset/value both Optional[PositiveInteger]
    0..1 in XSD order OFFSET→VALUE, base ARObject (AR-OBJECT group = empty-seq implicit base),
    docstrings verbatim from XSD documentation (class docstring matches sibling Tag style),
    checklist 6-col all [x]; model/parser/writer tests already fully covered (15 passed:
    defaults, None no-op, verbatim docstrings, field-value reader asserts, OFFSET-before-VALUE
    writer order, write→reparse round-trip); no deviations, no code change.
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-27 (12663 passed / 0 failed, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

- [x] `TcpRule` — TransportLayerRule — XSD-only (00052 complexType L120644)
  - module: M2/AUTOSARTemplates/AdaptivePlatform/PlatformModuleDeployment/Firewall/__init__.py
  - note: member type of FirewallRule.transportLayerRule (00052 L59090-59097 choice
    TCP-RULE|UDP-RULE; PDF Table 6.236 type column) — missing class reported per Rule
    0001.10 in this batch
  - note (Step 1): XSD 00052 group TCP-RULE L120616 + complexType L120644; class Note
    "Configuration of TCP filter rules."; atp.Status=candidate, atpObject; sequence =
    AR-OBJECT + TRANSPORT-LAYER-RULE + TCP-RULE; own members (verified L120623-L120640)
    numberOfParallelTcpSessions (POSITIVE-INTEGER 0..1), stateManagementBasedOnTcpFlags
    (BOOLEAN 0..1), timeoutCheck (POSITIVE-INTEGER 0..1, Note has no trailing period).
    No table in either corpus — Rule 0015 XSD-only.
  - note (Step 8): the inherited TRANSPORT-LAYER-RULE group members (checksumVerification,
    max/minDestinationPortNumber, max/minSourcePortNumber) are not modeled — the base
    TransportLayerRule (previous batch, stamp deferred) is an empty placeholder; TcpRule
    carries only its own TCP-RULE group members. No other deviations.
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-27 (12678 passed / 0 failed, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

- [x] `IcmpRule` — ARObject — XSD-only (00052 complexType L67721)
  - module: M2/AUTOSARTemplates/AdaptivePlatform/PlatformModuleDeployment/Firewall/__init__.py
  - note: queued 2026-09-27 per Rule 0001.10 — member type of Ipv4Rule.icmpRule/Ipv6Rule.icmpRule;
    XSD-only 00052 complexType L67721; supersedes the earlier "not queued" decision
  - note (Step 1): XSD 00052 group ICMP-RULE L67693 + complexType L67721; class Note
    "Configuration of filter rules for ICMP (Internet Control Message Protocol).";
    atp.Status=candidate, atpObject; sequence = AR-OBJECT + ICMP-RULE → base ARObject;
    own members (verified L67700-L67716) checksumVerification (BOOLEAN 0..1), code
    (POSITIVE-INTEGER 0..1), type (POSITIVE-INTEGER 0..1). No table in either corpus —
    Rule 0015 XSD-only.
  - note (Step 8): no deviations. The ICMP-RULE element never appears standalone — it is a
    nested child of IPV-4-RULE/IPV-6-RULE (00052 L74433/L74973), so until those wrappers
    synced the reader/writer coverage exercised readIcmpRule/writeIcmpRule directly on
    ICMP-RULE fragments (XSD order CHECKSUM-VERIFICATION → CODE → TYPE); the nested
    FirewallRule path is covered by the Ipv4Rule/Ipv6Rule reader/writer tests.
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-27 (12698 passed / 0 failed, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

- [ ] `Ipv4Rule` — NetworkLayerRule (TBC at Step 1) — R23-11 markdown ECUC-mapping appendix (no table, no XSD)
  - module: M2/AUTOSARTemplates/AdaptivePlatform/PlatformModuleDeployment/Firewall/__init__.py
  - note: PDF Table 6.236 types FirewallRule.networkLayerRule as Ipv4Rule; queued per user
    arbitration 2026-09-27 ("Enqueue both") — NON-STANDARD source: members derived from the
    R23-11 markdown ECUC-mapping appendix (AUTOSAR_CP_TPS_SystemTemplate.md L47645+; BSW
    Parameter FirewallNetworkLayerIpv4FilterConfig, mapping rule "1:1 mapping valid" to
    ECUC_Fw_00140). No class table in either corpus, IPV4-RULE absent from 00052/00044
    XSDs → Rule 0015 deviation documented at Step 8; regular stamp not possible (source is
    neither a spec table nor an XSD complexType) — marker decision arbitrated at 9b.
  - note (Step 1): member evidence (mmt.qualifiedName paths): checksumVerification
    (L47659, shared with TransportLayerRule/IcmpRule), differentiatedServiceCodePoint
    (L47679), doNotFragment (L47695), explicitCongestionNotification (L47711),
    sourceIpAddress (L47773), destinationIpAddress (L47777), sourceNetworkMask (L47816),
    destinationNetworkMask (L47820) — descriptions only, TYPES TBC at Step 1. No Base row
    in any corpus: candidate bases NetworkLayerRule (XSD family + ECU container name
    "FirewallNetworkLayer*") vs ARObject — arbitrate at Step 1. IcmpRule (code/type/
    checksumVerification, L48161/L48179/L49116) is appendix-only, NOT a table type ref —
    not queued; revisit if a later sync references it.
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `Ipv6Rule` — NetworkLayerRule (TBC at Step 1) — R23-11 markdown ECUC-mapping appendix (no table, no XSD)
  - module: M2/AUTOSARTemplates/AdaptivePlatform/PlatformModuleDeployment/Firewall/__init__.py
  - note: PDF Table 6.236 networkLayerRule family (tracker row names Ipv4Rule; Ipv6Rule is
    the IPv6 sibling in the same ECU container family FirewallNetworkLayer*FilterConfig);
    queued per user arbitration 2026-09-27 ("Enqueue both") — NON-STANDARD source: members
    derived from the R23-11 markdown ECUC-mapping appendix (AUTOSAR_CP_TPS_SystemTemplate.md
    L48463+). No class table in either corpus, IPV6-RULE absent from 00052/00044 XSDs →
    Rule 0015 deviation documented at Step 8; regular stamp not possible — marker decision
    arbitrated at 9b.
  - note (Step 1): member evidence (mmt.qualifiedName paths): trafficClass (L48463),
    flowLabel (L48479), hopLimit (L48502), sourceIpAddress (L47781/L47867),
    destinationIpAddress (L47736/L47871), sourceNetworkMask (L47824/L47828 context),
    destinationNetworkMask (L47740) — descriptions only, TYPES TBC at Step 1 (no
    checksumVerification: IPv6 has no header checksum). No Base row in any corpus: same
    candidate-base arbitration as Ipv4Rule.
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [x] `UdpRule` — TransportLayerRule — XSD-only (00052 complexType L127875)
  - module: M2/AUTOSARTemplates/AdaptivePlatform/PlatformModuleDeployment/Firewall/__init__.py
  - note: member type of FirewallRule.transportLayerRule (same TCP-RULE|UDP-RULE choice) —
    missing class reported per Rule 0001.10 in this batch
  - note (Step 1): XSD 00052 group UDP-RULE L127866 (empty sequence) + complexType L127875;
    class Note "Configuration of UDP filter rules."; atp.Status=candidate, atpObject;
    sequence = AR-OBJECT + TRANSPORT-LAYER-RULE + UDP-RULE — no own members (identity-only
    subtype, same shape as TransportLayerRule). No table in either corpus — Rule 0015
    XSD-only.
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-27 (12687 passed / 0 failed, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

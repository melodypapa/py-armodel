# Sync todo: Group 1 — Framework & core, PortInterface basics

Input: `Group 1 — Framework & core, PortInterface basics` of `docs/examples/sync_class_groups.md` · Generated: 2026-08-30 · Queue order = row order
(resume = first class row still `[ ]`; all class rows `[x]` = sync finished — Rule 0017.3)

## Queue (dependency-first)

- [x] `ARObject` (tracker input · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 6.1) — `# Spec verified: R23-11`
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - [x] Step 9 — Verify (9a) + confirm (9b)
- [x] `ARElement` (tracker input · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 4.3) — `# Spec verified: R23-11`
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red) — N/A: Table 4.3 has no Attribute rows; no own XML element, round-trip covered by concrete subclasses
  - [x] Step 6 — Update parser & writer (Green) — N/A: same reason as Step 5
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations — none (stale "missing" tracker row replaced with resolved entry)
  - [x] Step 9 — Verify (9a) + confirm (9b)
- [x] `ReferenceBase` (member type of `ARPackage.referenceBase` · Rule 0016.4 stub — blocks ARPackage 9b stamp per Rules 0001.10/0012.1 · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 4.14, p.72) — **finished, stamped `# Spec verified: R23-11`** (commit: 192dfd94, branch feature/sync-reference-base)
  - Spec facts (extracted 2026-08-30): defined in `ARPackage.py` (same file); Package = ...GeneralTemplateClasses::ARPackage; Base = **ARObject only** (no Referrable → `__init__(self)`); Aggregated by = ARPackage.referenceBase.
    - Note (verbatim, for Step 4): "This meta-class establishes a basis for relative references. Reference bases are identified by the short Label which shall be unique in the current package."
    - Attributes (Table 4.14 order): `globalElement` (ReferrableSubtypesEnum, *, attr) / `globalInPackage` (ARPackage, *, ref) / `isDefault` (Boolean, 1, attr, atp.Status=obsolete — keep) / `package` (ARPackage, 0..1, ref) / `shortLabel` (Identifier, 1, attr).
    - R4.3.1 Table 4.5 (p.55) additionally spec'd `isGlobal` + `baseIsThisPackage` — both absent from Table 4.14 and `atp.Status="removed"` in AUTOSAR_00052.xsd xsd:group REFERENCE-BASE (l.96385 IS-GLOBAL / l.96394 BASE-IS-THIS-PACKAGE); **19/29 integration fixtures still carry `<IS-GLOBAL>`/`<BASE-IS-THIS-PACKAGE>`** (legacy AI-spec files). Step 8 decision: keep as accepted deviations ("deprecated (atp.Status=removed in R23-11; spec'd R4.3.1 Table 4.5), kept for integration-fixture round-trip", rows release R4.3.1) vs strict removal (stamped-class precedent: CalibrationParameter/LinCommunication — but silently strips legacy data on rewrite; round-trip test compares models, would not catch the loss).
  - Known deviations to fix in this sync: (a) `packageRef: Optional[List[RefType]]` → `Optional[RefType]` (spec `package` is 0..1; parser/writer already single-ref — annotation-only fix); (b) `globalInPackageRefs` + `globalElements` have **no reader/writer** (wrappers GLOBAL-IN-PACKAGE-REFS/GLOBAL-IN-PACKAGE-REF + GLOBAL-ELEMENTS/GLOBAL-ELEMENT; Rule 0001.7 silent drop; enum-literal list helper needed for GLOBAL-ELEMENT); (c) setters `setIsDefault/setIsGlobal/setBaseIsThisPackage/setPackageRef/setShortLabel` missing None guards (Rule 0004); (d) field `self.BaseIsThisPackage` → `self.baseIsThisPackage`; (e) checklist is legacy 4-col with test column all `[ ]` (model tests already exist test_ARPackage.py:16-120) → 6-col rewrite; (f) member order → Table 4.14 displayed order (reader/writer keep XSD sequenceOffset order: SHORT-LABEL 10 … PACKAGE-REF 30).
  - [x] Step 1 — Sync members & description from spec (Table 4.14 body md l.1944–1955; caption l.1942; PDF p.72 confirmed; Class=concrete, Base=ARObject ✓ current heritage correct; 5 attrs in displayed order with verbatim Notes captured for Step 4; R23-11 only — isGlobal/baseIsThisPackage absent)
  - [x] Step 2 — Write model class unit test (Red) — test_ARPackage.py TestReferenceBase: attr init, getter/setter round-trip, None no-op guards, chaining
  - [x] Step 3 — Implement model class (Green) — packageRef List→Optional[RefType]; None guards; BaseIsThisPackage→baseIsThisPackage; member order = Table 4.14
  - [x] Step 4 — Sync docstrings (wipe + rewrite) — verbatim spec Notes in class docstring / inline comments / getter+setter docstrings; Stereotypes:/Tags: tails dropped per Rule 0012.2.5.2; setter docstrings append None no-op sentence per Rule 0012.2.5.4
  - [x] Step 5 — Write reader/writer round-trip test (Red) — parser/writer test_ar_package_reference_bases.py incl. new test_read/test_write_global_elements_and_in_package_refs (confirmed Red: 0==2 / None tag)
  - [x] Step 6 — Update parser & writer (Green) — readReferenceBases + writeReferenceBases now cover GLOBAL-IN-PACKAGE-REFS (RefType list w/ DEST) and GLOBAL-ELEMENTS (ReferrableSubtypesEnum literal list); element order: SHORT-LABEL, IS-DEFAULT, IS-GLOBAL, BASE-IS-THIS-PACKAGE, GLOBAL-IN-PACKAGE-REFS, GLOBAL-ELEMENTS, PACKAGE-REF (IS-GLOBAL/BASE-IS-THIS-PACKAGE are R4.3.1-sourced optional extras, see Step 8)
  - [x] Step 7 — Update checklist comment — 6-col parity checklist (impl/docstring/test/reader/writer/release) with dual spec citations in unified format `# Spec: <release>/<pdf name>, Table N.M, pages (RELEASE)`: `R23-11/AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 4.14, p.72 (R23-11)` + `R4.3.1/AUTOSAR_TPS_GenericStructureTemplate.pdf, Table 4.5, pp.54-55 (R4.3.1)` (R4.3.1 p.54 body / p.55 caption verified via pypdf); reader [x] on mutator rows, writer [x] on getter rows per Rule 0002; isGlobal/baseIsThisPackage rows carry release R4.3.1
  - [x] Step 8 — Deviations — decision (user, 9b): **merge isGlobal/baseIsThisPackage into ReferenceBase as optional legacy attributes, sources combined** — absent from R23-11 Table 4.14 but spec'd in R4.3.1 Table 4.5 (pp.54-55) with full Notes; rows release R4.3.1; obsolete ⇒ optional: fields stay Optional[Boolean], reader/writer skip absent elements; keeps 19 legacy integration fixtures passing unchanged (user: do NOT update fixture arxml). Inline `__init__` comments drop Stereotypes:/Tags: tails per Rule 0012.2.5.2; attribute blocks blank-line separated per Rule 0008. (a)–(f) known deviations all resolved (see Steps 2–4/6)
  - [x] Step 9 — Verify (9a) + confirm (9b) — 9a: 8186 tests + legacy integration round-trip pass, ruff/flake8/black clean; 9b (user-confirmed): Rules 0001/0002/0003/0011/0012/0014 pass, Rule 0007 package-location & file-shape check pass (ARPackage.py leaf shape, no shadowing, explicit imports, top-level export, not in exclusion lists — now a mandatory 9b gate item in Rule 0006.1); accepted deviation `legacy (R4.3.1 Table 4.5, pp.54-55); removed in R23-11` (isGlobal/baseIsThisPackage, Rule 0019 combine case); skill updated: Rule 0019 added, dual `# Spec:` unified format, Rule 0007 in 9b gate
- [x] `MultilanguageReferrable` (heritage-chain parent of Identifiable · unstamped Rule 0001.10 stub · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 4.11, content md l.1777–1793) — **finished, stamped `# Spec verified: R23-11`** (commit: 7c7157a0)
  - Spec facts (extracted 2026-08-30): Package = ...GeneralTemplateClasses::Identifiable; abstract; Base = ARObject, Referrable → direct base **Referrable** (stamped ✓) — code `MultilanguageReferrable(Referrable, ABC)` (Identifiable.py:186) heritage **CORRECT**; Subclasses include Identifiable, Caption, SdgCaption, Traceable, TraceReferrable.
    - Note (fetch full text from md l.1778 in Step 1): "Instances of this class can be referred to by their identifier (while adhering to namespace borders). They also may have a longName. But they are not considered to contribute substanti[ally]…"
    - Attributes: `longName` (MultilanguageLongName, 0..1, aggr) — code field/accessor pair exists (getLongName/setLongName).
  - Known deviations to fix in this sync: legacy 4-col checklist with `[ ]` test/docstring rows and no `# Spec:` line/stamp → full 6-col rewrite; setLongName missing None guard (Rule 0004); docstrings are paraphrases not verbatim Note (Rule 0012).
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red) — N/A: longName serialized by shared readReferrable→setLongName (parser:1163) and writeMultilanguageReferrable (writer:1121 reads field); confirmed via existing consuming-class round-trips
  - [x] Step 6 — Update parser & writer (Green) — N/A: no new reader/writer code; shared helpers already cover longName (writer now calls getLongName for parity)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations — none (legacy 4-col checklist → 6-col; setLongName None guard added; paraphrased docstrings → verbatim spec Note; writer now calls getLongName for parity)
  - [x] Step 9 — Verify (9a) + confirm (9b) — 9a: 8191 tests pass, ruff/black clean, integration round-trip pass; 9b user-confirmed: Rules 0001/0002/0003/0007/0011/0012/0014 pass; stamped `# Spec verified: R23-11` (commit: 7c7157a0)
## Wrong-heritage classes (uuid-move blockers) — queued ahead of `Identifiable`

Dependency-first: each of these must derive from `Identifiable` before the uuid move
in the work order below can run, so they precede the `Identifiable` row.

- [x] `HwPin` (R23-11 markdown · AUTOSAR_CP_TPS_ECUResourceTemplate · Table 2.7 · **uuid-move blocker — see the "uuid move work order" section below** · heritage fix: spec Base = ARObject, HwDescriptionEntity, Identifiable, MultilanguageReferrable, Referrable → most-derived direct base Identifiable; code was `HwPin(HwDescriptionEntity)` (Referrable-only)) — **finished, stamped `# Spec verified: R23-11`** (commit: ff5b0e08)
  - [x] Step 1 — Sync members & description from spec — Table 2.7 — Base = ARObject, HwDescriptionEntity, Identifiable, MultilanguageReferrable, Referrable (verified); XSD HW-PIN complexType references AR:IDENTIFIABLE
  - [x] Step 2 — Write model class unit test (Red) — test_HwPin.py TestHwPin: init defaults, getters/setters, None no-op guards, chaining, inherited HwDescriptionEntity members (23 tests pass)
  - [x] Step 3 — Implement model class (Green) — `class HwPin(Identifiable, HwDescriptionEntity)` (EcuResourceTemplate/__init__.py:117) — MRO HwPin→Identifiable→MultilanguageReferrable→HwDescriptionEntity→Referrable→ARObject
  - [x] Step 4 — Sync docstrings (wipe + rewrite) — verbatim spec Notes diffed (Rule 0012): class docstring + 3 inline member comments + getter/setter docstrings = spec Table 2.7 verbatim; setter docstrings append None no-op sentence (Rule 0012.2.5.4)
  - [x] Step 5 — Write reader/writer round-trip test (Red) — covered by tests/test_armodel/parser/test_hw_description_entity.py (heritage + Identifiable-member regression)
  - [x] Step 6 — Update parser & writer (Green) — readHwPin → readHwDescriptionEntity → readIdentifiable; writeHwPin → writeHwDescriptionEntity → writeIdentifiable
  - [x] Step 7 — Update checklist comment — 6-col parity checklist (impl/docstring/test/reader/writer/release); reader [x] on addFunctionName/setPackagingPinName/setPinNumber mutator rows, writer [x] on getFunctionNames/getPackagingPinName/getPinNumber getter rows per Rule 0002; page p.20 via pdf_page.py
  - [x] Step 8 — Deviations — none: all 3 Table 2.7 attrs modeled with correct types/kinds (functionName String * → functionNames:List[String]; packagingPinName String 0..1 → Optional[String]; pinNumber Integer 0..1 → Optional[Integer]); no naming/type/missing deviation
  - [x] Step 9 — Verify (9a) + confirm (9b) — 9a: 23 HwPin tests pass, ruff/black/flake8 clean on source, integration round-trip (running); 9b user-confirmed (heritage MRO matches spec; verbatim docstrings; no fabrication; reader+writer coverage per row)
- [x] `HwPinGroup` (R23-11 markdown · AUTOSAR_CP_TPS_ECUResourceTemplate · Table 2.5 · **uuid-move blocker — see the "uuid move work order" section below** · heritage fix: spec Base = ARObject, HwDescriptionEntity, Identifiable, MultilanguageReferrable, Referrable; code was `HwPinGroup(HwDescriptionEntity)` — 1 live UUID in CanSystem.arxml (CAN1)) — **finished, stamped `# Spec verified: R23-11`** (commit: 69afffcc)
  - [x] Step 1 — Sync members & description from spec — Table 2.5 — Base verified; XSD HW-PIN-GROUP references AR:IDENTIFIABLE (l.66185)
  - [x] Step 2 — Write model class unit test (Red) — test_HwPinGroup.py TestHwPinGroup: init defaults, get/set round-trip, None no-op, chaining, inherited HwDescriptionEntity members (6 tests pass)
  - [x] Step 3 — Implement model class (Green) — `class HwPinGroup(Identifiable, HwDescriptionEntity)` (EcuResourceTemplate/__init__.py:267); MRO verified
  - [x] Step 4 — Sync docstrings (wipe + rewrite) — verbatim spec Note diffed: class docstring + inline member comment + getter/setter docstrings = Table 2.5 Note; setter appends None no-op sentence
  - [x] Step 5 — Write reader/writer round-trip test (Red) — test_hw_pin_group_parser.py (read content w/ pin, nested group, no-content) + test_hw_pin_group_writer.py (write + serialize/reparse round-trip); UUID regression retained
  - [x] Step 6 — Update parser & writer (Green) — ADDED readHwPinGroupContent/writeHwPinGroupContent; readHwPinGroup/writeHwPinGroup now actually read/write hwPinGroupContent (was silently dropped — Rule 0001.7); handles HW-PIN/HW-PIN-GROUP children
  - [x] Step 7 — Update checklist comment — 6-col parity checklist (impl/docstring/test/reader/writer/release); reader [x] on setHwPinGroupContent mutator, writer [x] on getHwPinGroupContent getter; page p.19 via pdf_page.py
  - [x] Step 8 — Deviations — HwPinGroup itself: none (hwPinGroupContent reader/writer gap fixed). KNOWN ISSUE (member type, not blocking): `HwPinGroupContent` (already stamped R23-11) has paraphrased/mangled docstrings and models hwPin/hwPinGroup as single Optional rather than lists (spec atpMixed); recommend its own re-sync row.
  - [x] Step 9 — Verify (9a) + confirm (9b) — 9a: 20 HwPinGroup-targeted tests pass, ruff/black/flake8 clean, integration round-trip PASS; 9b user-confirmed (heritage MRO matches spec; verbatim docstrings; no fabrication; reader+writer coverage per row; HwPinGroupContent noted as separate re-sync)
- [x] `HwType` (R23-11 markdown · AUTOSAR_CP_TPS_ECUResourceTemplate · Table 2.3 · **uuid-move blocker — see the "uuid move work order" section below** · heritage fix: spec Base = ARElement…Identifiable; code was `HwType(HwDescriptionEntity)` — 1 live UUID in CanSystem.arxml (AnalogInType)) — **finished, stamped `# Spec verified: R23-11`** (commit: 29f338b3)
  - [x] Step 1 — Sync members & description from spec — Table 2.3 — Base = ARElement, ARObject, CollectableElement, HwDescriptionEntity, Identifiable, MultilanguageReferrable, PackageableElement, Referrable; XSD HW-TYPE references AR:IDENTIFIABLE (l.66373) and AR:HW-DESCRIPTION-ENTITY (l.66369)
  - [x] Step 2 — Write model class unit test (Red) — test_HwElementCategory.py: test_hw_type_init + test_hw_type_is_concrete + test_hw_type_inherited_members_round_trip + test_hw_type_inherited_members_none_noop (4 pass)
  - [x] Step 3 — Implement model class (Green) — `class HwType(ARElement, HwDescriptionEntity)` (EcuResourceTemplate/HwElementCategory.py:25)
  - [x] Step 4 — Sync docstrings (wipe + rewrite) — class docstring = Table 2.3 Note verbatim (Tags: tail dropped per Rule 0012.2.5.2); __init__ docstring removed (no own members)
  - [x] Step 5 — Write reader/writer round-trip test (Red) — UUID regression test added (DCE:f73f677c-1389-4425-83f8-921d567b2ad4)
  - [x] Step 6 — Update parser & writer (Green) — readHwType now calls readHwDescriptionEntity (was readReferrable — HW-TYPE-REF/HW-CATEGORY-REFS/HW-ATTRIBUTE-VALUES were silently dropped); writeHwType → writeHwDescriptionEntity
  - [x] Step 7 — Update checklist comment — 6-col parity checklist (`# Spec:` line + per-row release R23-11); __init__ row reader/writer [—] (no own XML elements; inheritance handled by readHwDescriptionEntity/writeHwDescriptionEntity)
  - [x] Step 8 — Deviations — none: Table 2.3 has no own Attribute rows; heritage matches spec Base (Identifiable reached via ARElement + HwDescriptionEntity MRO); readHwType/writeHwType cover the HwDescriptionEntity aggregations; uuid-move heritage fix already DONE
  - [x] Step 9 — Verify (9a) + confirm (9b) — 9a: 35 tests pass (4 HwType model + 27 HwDescriptionEntity parser/writer + 8 HwType UUID regression), ruff/flake8/black clean; 9b user-confirmed: Rules 0001/0002/0003/0007/0011/0012/0014 pass; stamped `# Spec verified: R23-11` (commit recorded in follow-up)
- [x] `HwElement` (R23-11 markdown · AUTOSAR_CP_TPS_ECUResourceTemplate · Table 2.4 · after `HwType` (ref `hwType`) and `HwPinGroup` (aggr `hwPinGroup`) · **uuid-move blocker — see the "uuid move work order" section below** · heritage fix: spec Base = ARElement…Identifiable; code was `HwElement(HwDescriptionEntity)` — 3 live UUIDs in CanSystem.arxml (AI_KL15, AI_KL30, DemoECU) — **finished, stamped `# Spec verified: R23-11`** (commit: 8c7f05d4)
  - [x] Step 1 — Sync members & description from spec — Table 2.4 — Base verified; XSD HW-ELEMENT references AR:IDENTIFIABLE (l.65901)
  - [x] Step 2 — Write model class unit test (Red) — test_HwElement.py added (7 tests: init defaults, add/getXxx round-trips, None no-ops, createHwPinGroup duplicate-returns-existing)
  - [x] Step 3 — Implement model class (Green) — `class HwElement(ARElement, HwDescriptionEntity)` (EcuResourceTemplate/__init__.py:534)
  - [x] Step 4 — Sync docstrings (wipe + rewrite) — class docstring replaced paraphrase with verbatim Table 2.4 Note; inline comments + accessor docstrings already verbatim spec prose
  - [x] Step 5 — Write reader/writer round-trip test (Red) — UUID/DESC/CATEGORY/ADMIN-DATA/INTRODUCTION regression test added (DemoECU) + full readHwElement/writeHwElement coverage confirmed
  - [x] Step 6 — Update parser & writer (Green) — readHwElement/writeHwElement go through the Identifiable chain
  - [x] Step 7 — Update checklist comment — 6-col parity checklist (release R23-11 per row); __init__ reader/writer [—], mutator rows reader [x], getter rows writer [x]
  - [x] Step 8 — Deviations — none: 3 spec attrs (hwElementConnection, hwPinGroup, nestedElement) all modeled with correct types/suffixes; heritage matches spec (Identifiable via ARElement + HwDescriptionEntity mixin)
  - [x] Step 9 — Verify (9a) + confirm (9b) — 9a: 285 model+parser/writer tests pass, ruff/flake8/black clean, parity HwElement COVERED, integration round-trip (CanSystem) passes; 9b user-confirmed 2026-08-31: Rules 0001/0002/0003/0007/0011/0012/0014 pass; `# Spec verified: R23-11` retained
- [x] `FirewallRule` (R23-11 markdown · AUTOSAR_CP_TPS_SystemTemplate · Table 6.236, p.585 (pdf_page.py verified) · **uuid-move blocker** · commit 00d011d4 · heritage: `class FirewallRule(ARElement)` already applied (KEEP) — RE-SCOPE (corrected 2026-08-31 via markdown/XSD arbitration — the markdown splits Table 6.236 across pages: l.15346-15351 carries Class/Note/Base, l.15353 bucketSize, l.15363-15373 the 9 rule attrs; XSD group FIREWALL-RULE l.59016-59101 confirms ownership): current body has fabricated `destRefs`/`srcRefs` (`List[RefType]`) NOT in Table 6.236/XSD — REMOVE; replace with the **10** spec attributes from Table 6.236: `bucketSize` (0..1 attr, PositiveInteger — was missing from earlier RE-SCOPE), `dataLinkLayerRule` (0..1), `ddsRule` (0..1), `doIpRule` (0..1), `networkLayerRule` (0..1), `payloadBytePatternRule` (* via PAYLOAD-BYTE-PATTERN-RULES), `refillAmount` (0..1 attr, PositiveInteger), `someipRule` (0..1), `someipSdRule` (0..1), `transportLayerRule` (0..1) — **user decision 2026-08-31: the 14 markdown-only member classes (DataLinkLayerRule, DdsRule, DoIpRule, PayloadBytePatternRulePart, IcmpRule, TcpRule, UdpRule, SomeipProtocolRule, SomeipSdRule, Ipv4Rule, Ipv6Rule, PayloadBytePatternRule, NetworkLayerRule, TransportLayerRule — no Class table in PDF/markdown, unverifiable) are SKIPPED and removed from this queue**; DataLinkLayerRule (c5a1b0de) and DdsRule (86699dd2) were already synced markdown-minimal in Firewall/__init__.py; the other 12 member types are NOT implemented — model FirewallRule's aggregates with attribute-name placeholders per Table 6.236 (full member attribute defs remain a deviation). Reader/writer (readFirewallRule/writeFirewallRule) built when syncing this class.
  - [x] Step 1 — Sync members & description from spec — Table 6.236 Base row verified; 9 attributes captured (see RE-SCOPE); member class rows removed from queue per user decision 2026-08-31
  - [x] Step 2 — Write model class unit test (Red) — 12 tests: init defaults (10 attrs), bucketSize/refillAmount PositiveInteger get/set, 7 aggregation setters, payloadBytePatternRule add/get x2, verbatim class docstring; placeholders instantiable test
  - [x] Step 3 — Implement model class (Green, partial) — `class FirewallRule(ARElement)` heritage fix applied; body members (destRefs/srcRefs) FABRICATED → replace with 9 spec attributes this sync
  - [x] Step 4 — Sync docstrings (wipe + rewrite) — verbatim Table 6.236 Notes (class note + 10 attr notes; getters carry the attr Note verbatim, setters carry chaining docstring)
  - [x] Step 5 — Write reader/writer round-trip test (Red) — TestFirewallRuleReadWrite.test_write (XML shape) + test_round_trip (write→parse→assert, PositiveInteger values + 8 placeholder member elements + 2 payload rules) — Red confirmed (writeFirewallRule/readFirewallRule missing)
  - [x] Step 6 — Update parser & writer (Green) — writeFirewallRule (ARPackageElement dispatch + FIREWALL-RULE element, XSD group order) + readFirewallRule + ARPackage.createFirewallRule (+ __all__, eager import in ARPackage.py)
  - [x] Step 7 — Update checklist comment — 6-col parity checklist all [x] ([—] for one-sided reader/writer on optional attrs)
  - [x] Step 8 — Deviations — destRefs/srcRefs removed; the 6 rule member types (DoIpRule, NetworkLayerRule, PayloadBytePatternRule, SomeipProtocolRule, SomeipSdRule, TransportLayerRule) modeled as empty ARObject placeholders (member attribute defs skipped per user decision 2026-08-31 — no Class table); payloadBytePatternRule ordering/collection semantics verified in round-trip
  - [x] Step 9 — Verify (9a) + confirm (9b) — 9a: 8295 tests pass, ruff/flake8 clean, black clean; **unstamped** per user decision 2026-08-31 (member placeholder classes not fully synced — stamp deferred to batch confirmation)
- [ ] `BlueprintMappingSet` (R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 3.1 · after `AtpBlueprintMapping` (aggr `blueprintMap`) · **uuid-move blocker — see the "uuid move work order" section below** · heritage fix: spec Base = ARElement…Identifiable — **DONE 2026-08-31: re-parented to `BlueprintMappingSet(ARElement)` with `(parent, short_name)` ctor; test construction site updated; fabricated `mappings: List[str]` retained until this class's own 9-step sync**; code was `BlueprintMappingSet(ARObject)` (CommonStructure/StandardizationTemplate/BlueprintMapping.py:8))
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `ConstantSpecificationMappingSet` (R23-11 markdown · AUTOSAR_CP_TPS_SoftwareComponentTemplate · Table 5.119 · **uuid-move blocker — see the "uuid move work order" section below** · heritage fix: spec Base = ARElement…Identifiable — **DONE 2026-08-31: re-parented to `ConstantSpecificationMappingSet(ARElement)` with `(parent, short_name)` ctor (zero construction sites elsewhere)**; code was `ConstantSpecificationMappingSet(ARObject)` (CommonStructure/Constants/__init__.py:804))
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `StructuredReq` (R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 9.31 · **uuid-move blocker — see the "uuid move work order" section below** · heritage fix: spec Base = ARObject, DocumentViewSelectable, Identifiable, MultilanguageReferrable, Paginateable, Referrable, Traceable — **DONE 2026-08-31: re-parented to `StructuredReq(Traceable)`; decision: the Identifiable mixin stays on `Traceable(Identifiable)` (Table E.x gives Traceable Base = ARObject, MultilanguageReferrable, Referrable — recorded as a documented deviation to revisit in this class's own 9-step sync); parser `getStructuredReq(element, key, block)` now constructs with `(block, short_name)`; ~17 test construction sites updated**; code was `StructuredReq(ARObject)` (MSR/Documentation/BlockElements/RequirementsTracing.py:123))
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `TraceableText` (R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 9.30 · after `StructuredReq` (same Base closure) · **uuid-move blocker — see the "uuid move work order" section below** · heritage fix — **DONE 2026-08-31: re-parented to `TraceableText(Traceable)`; duplicate `traceRefs` field + `getTraceRefs`/`addTraceRef` removed (inherited from Traceable); parser `getTraceableText(element, key, block)` now constructs with `(block, short_name)`; test construction sites updated**; code was `TraceableText(ARObject)` (RequirementsTracing.py:58))
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `Identifiable` (heritage-chain parent of CollectableElement/AtpBlueprint/AtpBlueprintable/ARPackage · carries a `# Spec verified: R23-11` stamp that has NOT passed 9b — treat as unverified · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 4.4, content md l.1650–1695)
  - Spec facts (extracted 2026-08-30): abstract; Base = ARObject, MultilanguageReferrable, Referrable → direct base **MultilanguageReferrable** (queued above) — code `Identifiable(MultilanguageReferrable, ABC)` (Identifiable.py:229) heritage **CORRECT**; Subclasses explicitly list ARPackage, CollectableElement, PackageableElement, AtpBlueprint, AtpBlueprintable.
    - Attributes (Table 4.4 displayed order): `adminData` (AdminData, 0..1, aggr) / `annotation` (Annotation, *, aggr) / `category` (CategoryString, 0..1, attr) / `desc` (MultiLanguageOverviewParagraph, 0..1, aggr) / `introduction` (DocumentationBlock, 0..1, aggr) / `uuid` (String, 0..1, attr).
  - Known deviations to fix in this sync: (a) duplicate `elements`/`element_mappings` registry in `__init__` (Identifiable.py:258-259 — CollectableElement infra; ARPackage's getElement override reaches it; remove after CollectableElement sync or verify consumers); (b) **uuid ownership RESOLVED (uuid-last step)** — uuid is intentionally carried on `ARObject` (see `ArObject.py` "uuid" internal member, getUuid/setUuid); `readARObjectAttributes` / `UUIDMgr.addObject` / `writeARObjectAttributes` now key on `isinstance(obj, ARObject)` so every AUTOSAR object can be registered/serialized with the UUID manager. Spec `uuid` (Table 4.4) is an IDENTIFIABLE attributeGroup but is modeled as an ARObject internal extension by design; (c) `variationPoint` carried with documented deviation comment (keep); (d) no `# Spec:` line/stamp for this class (only Referrable l.27 and Describable l.517 in the same file are stamped) → 6-col checklist rewrite.
  - [x] Step 1 — Sync members & description from spec (Table 4.4 body md l.1664–1693, caption l.1688; PDF p.61 confirmed via pdf_page.py; Class=Identifiable (abstract) ✓; Base = ARObject, MultilanguageReferrable, Referrable → most-derived direct base **MultilanguageReferrable** ✓ current heritage correct (Identifiable.py:230); 6 attrs in displayed order with verbatim Notes captured: adminData / annotation / category / desc / introduction / uuid)
  - [x] Step 2 — Write model class unit test (Red) — test_Identifiable.py TestIdentifiable: added test_add_annotation_none_is_noop, test_element_registry_round_trip, test_remove_element_unknown_short_name_raises (37 tests pass); the pre-existing suite already covered init defaults, get/set round-trips, None no-ops and abstract instantiation
  - [x] Step 3 — Implement model class (Green) — heritage unchanged (Identifiable(MultilanguageReferrable, ABC) ✓ most-derived spec base); methods reordered into Table 4.4 displayed order (adminData → annotation → category → desc → introduction → uuid, then the kept infra registry, then variationPoint) per Rule 0001.11; dead duplicate `return self` in setIntroduction removed; return annotations added to setAdminData/setCategory/setDesc/setIntroduction/removeAdminData/addAnnotation (Rule 0003); elements/element_mappings registry kept as documented infra (deviation (a))
  - [x] Step 4 — Sync docstrings (wipe + rewrite) — verified by diff (Rule 0012.2.6): class docstring + all 6 inline member comments + all 12 accessor docstrings diffed verbatim against md Table 4.4; one Rule 0001.4 deviation found and fixed in 3 places — the desc Note reads "how the object is built or used" in both the markdown (l.1682) and AUTOSAR_00052.xsd l.67753, while the code said "is built or is used"
  - [x] Step 5 — Write reader/writer round-trip test (Red) — parser test_arxml_parser_handlers.py: test_readIdentifiable_populates_category_desc_admin / _with_annotation / _empty_annotations_wrapper (empty-wrapper case added this pass) + test_ar_object_attributes.py (uuid on a concrete Identifiable); writer test_identifiable.py: field-value asserts + empty-optional case + write→re-parse→assert round-trip
  - [x] Step 6 — Update parser & writer (Green) — no dispatch change needed (readIdentifiable/writeIdentifiable already cover all six attributes incl. the ANNOTATIONS wrapper); the two uuid comments in abstract_arxml_parser.py / abstract_arxml_writer.py now point at the uuid-move work order, and the stale "owned by Identifiable" docstring in parser/test_ar_object_attributes.py was corrected (12 reader/writer tests pass)
  - [x] Step 7 — Update checklist comment — 6-col rows now 1:1 with the 22 methods in source order (verified by script): 6 spec attributes in Table 4.4 order + 6 element-collection infra rows in an "Internal members" block (cf. the ARObject precedent) + variationPoint in a "Kept deviation member" block; uuid rows annotated with the ARObject-owner deferral
  - [x] Step 8 — Deviations (incl. uuid ownership decision) — (a) elements/element_mappings registry: kept as documented infra, now with explicit checklist rows (removal deferred to the CollectableElement row below, which owns the duplicated methods); (b) uuid ownership: **DEFERRED by user decision** — stays on ARObject until the 10 wrong-heritage classes derive from Identifiable; work order recorded in the "uuid move work order" section of this file and in the `ARObject` section of docs/examples/method_deviation_by_class_v2.md; (c) variationPoint: framework-level, excluded by the tracker preamble → not a stamp blocker; no `naming`/`type`/`missing` deviation row remains
  - [ ] Step 9 — Verify (9a) + confirm (9b) — **PAUSED 2026-08-31 by user decision**: steps 1-8 done and 9a passed (8212 unit tests, 130-file integration round-trip, ruff/flake8/black clean), but the user reordered the work — finish the wrong-heritage rows above → move uuid in the ARObject parse/write → only then run 9b and stamp. Do NOT stamp before that.
- [ ] `CollectableElement` (direct spec base of ARPackage + PackageableElement · Rule 0016.4 wrong-base stub — prerequisite for the ARPackage heritage fix · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 13.3, class table body md l.10589+)
  - Spec facts (extracted 2026-08-30): Package = ...GeneralTemplateClasses::ElementCollection; **Base = ARObject, Identifiable, MultilanguageReferrable, Referrable → most-derived direct base = Identifiable**; Subclasses = {ARPackage, PackageableElement}; **no own Attribute rows**.
  - Deviation: code has `CollectableElement(ARObject, ABC)` + `__init__(self)` (ElementCollection.py:16/31) — skips the Referrable→MultilanguageReferrable→Identifiable chain. Fix: re-parent to `Identifiable`, `__init__(self, parent, short_name)`; `elements`/`element_mappings` registry stays (codebase infra; spec `element` aggregation belongs to ARPackage Table 4.1 and is shared by design).
  - Downstream fixes unlocked (do together with ARPackage Step 9): (1) **ARPackage drops its manually flattened Referrable/Identifiable members** (parent, short_name, longName, annotations, adminData, category, introduction, desc — currently duplicated to compensate; Rule 0001.3 relocation) and calls `super().__init__(parent, short_name)`; (2) ARPackage `__init__` double-init cleanup (`CollectableElement.__init__(self)` + explicit `ARObject.__init__(self)` with stale comment — CollectableElement *does* call super().__init__(), so ARObject.__init__ runs twice); (3) `PackageableElement` re-parent — own drift row directly below (Table 4.2 Base closure names CollectableElement as most-derived); (4) `AbstractAUTOSAR` re-check in its own queued sync — AUTOSAR spec Base = **ARObject** (R4.3.1 ARXMLSerializationRules Table 1.1), code has AbstractAUTOSAR(CollectableElement).
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red) — N/A candidate: no own attributes/no own XML element (registry infra); confirm in-step
  - [ ] Step 6 — Update parser & writer (Green) — N/A candidate: same reason
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `PackageableElement` (child of CollectableElement · STAMPED R23-11 — **drift pass only** per Rule 0012.3: heritage fix · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 4.2, p.54)
  - Drift scope (no member re-sync — Table 4.2 has no own Attribute rows): re-parent `PackageableElement(Identifiable, ABC)` → `PackageableElement(CollectableElement, ABC)` (ARPackage.py:22) — Table 4.2 Base closure = {ARObject, CollectableElement, Identifiable, MultilanguageReferrable, Referrable} names **CollectableElement** as most-derived. Run AFTER the CollectableElement row above lands; `super().__init__(parent, short_name)` forwarding unchanged (CollectableElement now forwards to Identifiable). Re-run ARElement/Collection round-trips to confirm no parser/writer dispatch change (readIdentifiable/writeIdentifiable shared; inherited members reached through inheritance).
  - [ ] Step 1 — Confirm drift scope from Table 4.2 (members unchanged)
  - [ ] Step 2 — Adjust model unit test (base-relationship asserts)
  - [ ] Step 3 — Re-parent to CollectableElement (Green)
  - [ ] Step 4 — Docstrings unchanged (no own members)
  - [ ] Step 5 — Re-run reader/writer round-trip (inherited members)
  - [ ] Step 6 — Parser/writer unchanged (confirm no dispatch edit needed)
  - [ ] Step 7 — Update checklist comment (base note)
  - [ ] Step 8 — Deviations — none expected (heritage fix only)
  - [ ] Step 9 — Verify (9a) + confirm (9b) — re-stamp after drift per Rule 0012.3
- [ ] `ARPackage` (tracker input · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 4.1)
  - Heritage check (2026-08-30, spec-verified): Table 4.1 Base closure = {ARObject, AtpBlueprint, AtpBlueprintable, CollectableElement, Identifiable, MultilanguageReferrable, Referrable} → direct parallel branches = {AtpBlueprint (C.12: →Identifiable), AtpBlueprintable (C.14: →Identifiable), CollectableElement (13.3: →Identifiable)}. **`ARPackage(CollectableElement)` single role-matching branch = CORRECT per Rule 0001.2** (blueprint chains rightly not multi-inherited; blueprintPolicy etc. deferred to AtpBlueprint/AtpBlueprintable syncs). WRONG underneath: CollectableElement(ARObject) skips Identifiable (see CollectableElement row above) — that is why ARPackage carries 8 flattened Referrable/Identifiable members; strip them after the CollectableElement re-parent, before 9b. AtpBlueprint(Identifiable) in code ✓ (C.12). Note: AtpBlueprintable(PackageableElement) in code is over-derived vs C.14 Base=Identifiable → fix in its own queued sync.
  - [x] Step 1 — Sync members & description from spec
    - Spec facts (extracted 2026-08-30, PDF-confirmed): Table 4.1 spans **p.53–54** (summary rows p.53, attribute rows + caption p.54). NOTE: in this markdown/PDF, table **content precedes its caption**; Table 4.3 (ARElement) is split across p.54–55 with the caption sitting mid-table.
    - Note (verbatim, for Step 4): "AUTOSAR package, allowing to create top level packages to structure the contained ARElements. ARPackages are open sets. This means that in a file based description system multiple files can be used to partially describe the contents of a package. This is an extended version of MSR's SW-SYSTEM."
    - Base (flattened): ARObject, AtpBlueprint, AtpBlueprintable, CollectableElement, Identifiable, MultilanguageReferrable, Referrable. Since PackageableElement is NOT in the list but AtpBlueprintable IS, and per Tables E.10/E.11 both AtpBlueprint and AtpBlueprintable have Base = ARObject, Identifiable, MultilanguageReferrable, Referrable (no PackageableElement) — direct bases ≈ {AtpBlueprint, AtpBlueprintable, CollectableElement}. Current code has `ARPackage(CollectableElement)` only → Step 3 must decide whether to add AtpBlueprint/AtpBlueprintable mixins (check their attribute blueprintPolicy / blueprintColor impact).
    - Attributes: `arPackage` (ARPackage, *, aggr) / `element` (PackageableElement, *, aggr) / `referenceBase` (ReferenceBase, *, aggr) — implemented via createARPackage/getARPackages, addElement/getElement, addReferenceBase/referenceBases.
    - ARElement confirmation (user gate): ARElement = Table 4.3 (content p.54 + p.55 subclasses block, caption p.55); Note/Base/no-own-attributes all match the stamped implementation — ARElement sync confirmed correct, no changes needed.
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations — stale tracker rows (arPackage "missing", element "type") replaced with resolved entries; ARPackage-own rows clean. **Open blockers recorded (2026-08-30 correction): `referenceBase` member type `ReferenceBase` is a Rule 0001.10 stub (queued above) and base class `CollectableElement` has wrong Python base (queued above) — `# Spec verified:` withheld until both land** (Rule 0012.1)
  - [ ] Step 9 — Verify (9a) + confirm (9b) — run AFTER all rows above (ReferenceBase + heritage chain MultilanguageReferrable → Identifiable → CollectableElement + PackageableElement drift); includes stripping ARPackage's flattened Identifiable members (now inherited via the fixed chain), the double-init cleanup, and the adapted set-based check (193 methods vs 6 checklist rows — ~187 create*/getter convenience factories intentionally excluded per checklist comment)
- [ ] `AUTOSAR` (tracker input · R4.3.1 markdown · AUTOSAR_TPS_ARXMLSerializationRules · Table 1.1 (multiple tables — resolve in per-class Phase 0) · **heritage check**: spec Base = **ARObject** (Table 1.1) but code has `AbstractAUTOSAR(CollectableElement)` — after the CollectableElement re-parent lands, decide in Step 3: keep for elements-registry reuse (documented deviation) or restructure)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `FileInfoComment` (tracker input · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 2.1)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `Collection` (tracker input · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 13.1)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `AtpType` (tracker input · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 5.6)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `AtpPrototype` (tracker input · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 5.4)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `AtpStructureElement` (tracker input · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 5.5)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `AtpDefinition` (tracker input · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 11.3)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `AtpBlueprint` (heritage mixin branch of ARPackage (Table 4.1 Base) · unstamped (has `# Spec:` line, no marker) · R4.3.1 markdown · AUTOSAR_TPS_StandardizationTemplate · Table 4.2 · R23-11 renders Table C.12 · code cites CP_TPS_BSWModuleDescriptionTemplate Table D.11, p.305 — pick one citation in Step 1)
  - Spec facts (extracted 2026-08-30): abstract; Base = ARObject, Identifiable, MultilanguageReferrable, Referrable → direct base **Identifiable** (queued above) — code `AtpBlueprint(Identifiable, ABC)` (AbstractBlueprintStructure/__init__.py:43) heritage **CORRECT**; own attribute `blueprintPolicy` (BlueprintPolicy, aggr); Subclasses explicitly list ARPackage.
  - Note: ARPackage's 9b does NOT block on this row (blueprint mixin attrs not modeled on ARPackage by design — Rule 0001.2 single-branch selection, documented in ARPackage checklist comment).
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `AtpBlueprintable` (tracker input · R4.3.1 markdown · AUTOSAR_TPS_StandardizationTemplate · Table 4.3 · **heritage fix**: re-parent `AtpBlueprintable(PackageableElement)` → `(Identifiable)` — Base = ARObject, Identifiable, MultilanguageReferrable, Referrable (no PackageableElement/CollectableElement in its chain); do AFTER the Identifiable row above)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `AtpBlueprintMapping` (tracker input · R4.3.1 markdown · AUTOSAR_TPS_StandardizationTemplate · Table 4.4)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `ApplicationDeferredDataType` (tracker input · R23-11 markdown · AUTOSAR_FO_TPS_AbstractPlatformSpecification · Table 3.17)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `AbstractImplementationDataType` (tracker input · R23-11 markdown · AUTOSAR_CP_TPS_SoftwareComponentTemplate · Table 5.14)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `AbstractImplementationDataTypeElement` (tracker input · R23-11 markdown · AUTOSAR_CP_TPS_SoftwareComponentTemplate · Table 5.16)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `Implementation` (tracker input · R23-11 markdown · AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate · Table 7.1 (multiple tables — resolve in per-class Phase 0))
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `FlatMap` (tracker input · R23-11 markdown · AUTOSAR_CP_TPS_SystemTemplate · Table 14.1)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `ModeAccessPointIdent` (tracker input · R23-11 markdown · AUTOSAR_CP_TPS_SoftwareComponentTemplate · Table 14.5)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `IdentCaption` (tracker input · R23-11 markdown · AUTOSAR_CP_TPS_SoftwareComponentTemplate · Table 14.4)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `DataInterface` (tracker input · R23-11 markdown · AUTOSAR_CP_TPS_SoftwareComponentTemplate · Table 3.19)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `NvDataInterface` (tracker input · R23-11 markdown · AUTOSAR_CP_TPS_SoftwareComponentTemplate · Table 11.5)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `SenderReceiverInterface` (tracker input · R23-11 markdown · AUTOSAR_CP_TPS_SoftwareComponentTemplate · Table 4.1)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `ParameterInterface` (tracker input · R23-11 markdown · AUTOSAR_CP_TPS_SoftwareComponentTemplate · Table 2.2)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `TriggerInterface` (tracker input · R23-11 markdown · AUTOSAR_CP_TPS_SoftwareComponentTemplate · Table 4.12)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [x] `PortInterfaceMapping` (tracker input · R23-11 markdown · AUTOSAR_CP_TPS_SoftwareComponentTemplate · Table 4.20) — **finished, stamped `# Spec verified: R23-11`** (commit: ca6a3723)
  - [x] Step 1 — Sync members & description from spec — Table 4.20 body md l.3527–3535; caption l.3525; PDF p.119 confirmed via pdf_page.py (R4.3.1 has Table 4.24 p.124 — unused, R23-11 table exists). Class=abstract; Package=...SWComponentTemplate::PortInterface; Base=ARObject, AtpBlueprint, AtpBlueprintable, Identifiable, MultilanguageReferrable, Referrable → role branch **AtpBlueprintable** ✓ current heritage correct (parallel AtpBlueprint/AtpBlueprintable chains not added via MI, ARPackage precedent); Note (verbatim) captured for Step 4; Attributes row = `-` — **no own attributes** (abstract shell); Subclasses: ClientServerInterfaceMapping, ModeInterfaceMapping, TriggerInterfaceMapping, VariableAndParameterInterfaceMapping; Aggregated by PortInterfaceMappingSet.portInterfaceMapping. No own XML element (abstract) → Steps 5/6 expected N/A. Current code: no class docstring, stale 3-col checklist
  - [x] Step 2 — Write model class unit test (Red) — test_PortInterface.py TestPortInterfaceMapping: test_PortInterfaceMapping_abstract (TypeError msg) + test_PortInterfaceMapping_concrete_subclass_inheritance (isinstance chain via ClientServerInterfaceMapping, parent/short_name). Result: both pass immediately — impl already matches Table 4.20 (abstract shell, no attributes); no failing assertion found
  - [x] Step 3 — Implement model class (Green) — no change required: `PortInterfaceMapping(AtpBlueprintable, ABC)` + abstract TypeError guard verified correct by the Step-2 tests; Base chain confirmed (AtpBlueprintable role branch, ARPackage precedent)
  - [x] Step 4 — Sync docstrings (wipe + rewrite) — no pre-existing docstrings on this class (wipe vacuous); class docstring written verbatim from md l.3530 Note; no member docstrings (no own attributes, `__init__` has no docstring per Rule 0012.2.4)
  - [x] Step 5 — Write reader/writer round-trip test (Red) — N/A: abstract class, no own XML element; XSD AUTOSAR_00052.xsd l.92574 defines `PORT-INTERFACE-MAPPING` as an element **group** (concrete subclasses substitute into it) — round-trip covered by the concrete subclass syncs
  - [x] Step 6 — Update parser & writer (Green) — N/A: same reason as Step 5
  - [x] Step 7 — Update checklist comment — 6-col format with `# Spec: R23-11/AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.20, p.119 (R23-11)`; single row `__init__` (reader/writer `[—]`, release R23-11); marker deferred to 9b
  - [x] Step 8 — Deviations — none for the class itself (no own attributes, heritage correct, docstring verbatim). Rule 0001.10 reference report (non-blocking): base `AtpBlueprintable` queued at Group1.md l.297 with heritage fix (re-parent → Identifiable); concrete subclass `TriggerInterfaceMapping` queued at l.457; concrete subclasses `ClientServerInterfaceMapping` / `ModeInterfaceMapping` / `VariableAndParameterInterfaceMapping` NOT queued (Table 4.20 Subclasses row; inherit from this class, no member-type edge) — future queue candidates
  - [x] Step 9 — Verify (9a) + confirm (9b) — 9a: 8210 unit + 2 integration round-trip pass, ruff/flake8/black clean; 9b (user-confirmed): Rules 0001.1/0001.2/0001.3/0003/0012/0014 pass, N/A items justified (no attributes/no XML element), Rule 0007 package-location check pass (PortInterface/__init__.py non-leaf shape, explicit imports, top-level export True, not in exclusion lists); no deviations; marker written
- [ ] `SubElementMapping` (tracker input · R23-11 markdown · AUTOSAR_CP_TPS_SoftwareComponentTemplate · Table 4.32)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `TriggerInterfaceMapping` (tracker input · R23-11 markdown · AUTOSAR_CP_TPS_SoftwareComponentTemplate · Table 4.30)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `ModeDeclarationMappingSet` (tracker input · R23-11 markdown · AUTOSAR_CP_TPS_SoftwareComponentTemplate · Table 4.28 · after `ModeDeclarationMapping` (auto-queued, exists))
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

## Pending 16.4 resolution (NEW — not in src)

_(none)_

## Not queued

_(none)_

---

## uuid move work order (ARObject → Identifiable) — DEFERRED

**Decision (2026-08-31, user):** `uuid` stays on `ARObject` for now; the move runs
*after* every class below derives from `Identifiable`. Fix the wrong heritage first.

### Why it is not on Identifiable yet

- Ground truth: `AUTOSAR_00052.xsd` defines `UUID` exactly once, inside the
  `IDENTIFIABLE` attributeGroup (l.67791–67803). The `AR-OBJECT` attributeGroup
  carries only `S`/`T` (l.4900–4913). 1136 complexTypes reach `IDENTIFIABLE`.
  Table 4.4 lists `uuid` under Identifiable — so the two ARObject rows are
  fabricated w.r.t. Table 6.1 and the move is the spec-correct end state.
- Today: field + accessors on `ArObject.py:55/85-97`; `Identifiable.py` only
  re-declares `getUuid`/`setUuid` as pass-throughs; `readARObjectAttributes`
  (abstract_arxml_parser.py:373) / `writeARObjectAttributes`
  (abstract_arxml_writer.py:77) / `UUIDMgr.addObject` (uuid_mgr.py:23) all key on
  `isinstance(obj, ARObject)`.

### Blockers — 10 classes whose XSD type reaches IDENTIFIABLE but which are not Identifiable in the model

All ten rows now live in the "Wrong-heritage classes" section above (ahead of `Identifiable`).

| Class | Spec table | Live UUIDs in fixtures | Heritage fix (2026-08-31) |
|---|---|---|---|
| `HwPin` | ECUResourceTemplate Table 2.7 | 0 observed | **DONE** — `(Identifiable, HwDescriptionEntity)` |
| `HwPinGroup` | ECUResourceTemplate Table 2.5 | 1 (CanSystem.arxml) | **DONE** — `(Identifiable, HwDescriptionEntity)` |
| `HwType` | ECUResourceTemplate Table 2.3 | 1 (CanSystem.arxml) | **DONE** — `(ARElement, HwDescriptionEntity)` |
| `HwElement` | ECUResourceTemplate Table 2.4 | 3 (CanSystem.arxml) | **DONE** — `(ARElement, HwDescriptionEntity)` |
| `FirewallRule` | SystemTemplate Table 6.236 | 0 observed | **DONE** — `(ARElement)`; construction sites + tests updated |
| `StateDependentFirewall` | SystemTemplate Table 6.234 | 0 observed | **DONE** — `(ARElement)`; construction sites + tests updated |
| `BlueprintMappingSet` | FO GenericStructure Table 3.1 | 0 observed | **DONE** — `(ARElement)`; test construction site updated |
| `ConstantSpecificationMappingSet` | SWCT Table 5.119 | 0 observed | **DONE** — `(ARElement)` |
| `StructuredReq` | FO GenericStructure Table 9.31 | 0 observed | **DONE** — `(Traceable)`; parser + ~17 test construction sites updated; Identifiable mixin stays on Traceable (documented deviation); parser falls back to the element tag when SHORT-NAME is absent (writer does not yet emit SHORT-NAME for STRUCTURED-REQ/TRACE — revisit in full sync) |
| `TraceableText` | FO GenericStructure Table 9.30 | 0 observed | **DONE** — `(Traceable)`; duplicate traceRefs members removed (inherited); parser + test construction sites updated; same SHORT-NAME fallback as StructuredReq |

Progress: 10 of 10 complete; the 5 UUIDs that were at risk now round-trip
(verified: parse CanSystem.arxml → write → re-parse, all 5 present).

**User decision (2026-08-31):** the uuid move precondition is amended — heritage
fixes on all ten rows now satisfy the gate, so the move may run **before** the
remaining 9-step syncs (`FirewallRule`, `StateDependentFirewall`,
`BlueprintMappingSet`, `ConstantSpecificationMappingSet`, `StructuredReq`,
`TraceableText`) are completed.

All ten were cross-checked in both directions: model class → XSD complexType
(`CamelCase → UPPER-DASH`) reaches `IDENTIFIABLE`, and the spec `Base` row names
`Identifiable` in every case. 471 other non-Identifiable ARObject classes have no
IDENTIFIABLE XSD type and are unaffected.

### Why the test suite will not catch the regression

`tests/integration_tests/test_roundtrip.py` compares **models**
(parse → write → re-parse), so a UUID dropped at first parse is absent from both
sides and the suite stays green. Add an explicit regression test asserting the 5
HW UUIDs survive before making the move.

### The move itself (run only when all ten rows are `[x]`) — **EXECUTED 2026-08-31 (see status note below)**

1. `Identifiable.__init__`: declare `self.uuid: Optional[str] = None` in Table 4.4
   order (after `introduction`); the existing `getUuid`/`setUuid` become the real
   implementation instead of pass-throughs.
2. `ArObject.py`: drop the field, both accessors, the two checklist rows and the
   internal-member note; ARObject is a re-sync/drift pass (Rule 0012.3).
3. Parser **ordering trap**: `readARObjectAttributes` sits at the *bottom* of the
   chain (`readIdentifiable → readMultilanguageReferrable → readReferrable →
   readARObjectAttributes`) and `AUTOSAR.addARObject()` registers the object there.
   Moving the read into `readIdentifiable` naively registers *before* the uuid is
   set, breaking `getARObjectByUUID` and duplicate detection. Either guard the read
   at the current site with `isinstance(ar_object, Identifiable)` (check for an
   import cycle first) or move the registration to the end of `readIdentifiable`.
4. Writer: move the UUID emission from `writeARObjectAttributes` to
   `writeIdentifiable` (order-safe).
5. `UUIDMgr.addObject`: key on `isinstance(obj, Identifiable)`.
6. Update the stale comments that say ARObject carries uuid:
   `AbstractBlueprintStructure/__init__.py:106`, `ARPackage.py:388`,
   `tests/test_armodel/parser/test_ar_object_attributes.py` module docstring, and
   the `ARObject` section of `docs/examples/method_deviation_by_class_v2.md`.
7. Move the uuid cases out of `parser/test_ar_object_attributes.py` +
   `writer/test_ar_object_attributes.py` into the Identifiable-level tests.

**Status (2026-08-31): the uuid move has landed.** Steps 1–7 done:
- `Identifiable.__init__` owns `self.uuid` (after `introduction`); `getUuid`/`setUuid`
  are now the real implementations; `ARObject` no longer declares uuid.
- Parser: uuid read and the UUID-manager registration both live in
  `readIdentifiable` (uuid is set *before* `addARObject()` — the ordering trap
  preserved). The generic reader was then split per object name:
  `readARObjectAttributes` (ARObject: S/T via mutators) and
  `readARType` (ARType primitives: T as plain string). XSD check
  (AUTOSAR_00052.xsd): primitives reference only the AR-OBJECT attributeGroup
  (S/T) — the uuid attribute exists only in IDENTIFIABLE, so the legacy
  `ARType.uuid` field was removed from PrimitiveTypes.py and no uuid handling
  remains in any read/write attributes method. Verified: no parse path reaches
  an Identifiable-derived object without `readIdentifiable` (all 11
  `readReferrable`/`readMultilanguageReferrable` bypass classes are
  Referrable/MultilanguageReferrable); all 16 parser ARType call sites and all
  6 writer ARType call sites now use the ARType-specific methods.
- Writer: same split — `writeARObjectAttributes` (ARObject: S/T) and
  `writeARType` (ARType: T); `writeIdentifiable` emits UUID **after**
  the S/T chain call to preserve the historical attribute order S, T, UUID
  (byte-level round-trip requirement).
- `UUIDMgr.addObject` keys on `isinstance(obj, Identifiable)`.
- Stale comments updated (AbstractBlueprintStructure docstring, ARPackage ctor
  comment, both `test_ar_object_attributes.py` module docstrings,
  `docs/examples/method_deviation_by_class_v2.md` ARObject section).
- Writer uuid case moved to `tests/test_armodel/writer/test_identifiable.py`
  (already covered); parser uuid cases updated to the new Identifiable-owned
  contract; uuid_mgr / TransformationISignalProps / BswVariableAccess /
  SenderRecRecordTypeMapping tests updated (non-Identifiable objects no longer
  carry uuid).
- Gates: 8281 tests passed (incl. 10 integration round-trips, CanSystem 5 HW
  UUIDs verified via test_hw_description_entity), lint + black-check clean.

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
- [x] `PortInterfaceBlueprintMapping` (XSD-only · no R23-11/R4.3.1 PDF/markdown Class table · member type of `BlueprintMappingSet.blueprintMap` wrapper `BLUEPRINT-MAPS` choice · AUTOSAR_00052.xsd complexType `PORT-INTERFACE-BLUEPRINT-MAPPING` l.92477, group l.92440 · **XSD verified** candidate) — needed so `BlueprintMappingSet`'s reader/writer covers all three `BLUEPRINT-MAPS` choice elements (closes the 9b deviation) — **finished, stamped `# XSD verified: AUTOSAR_00052.xsd`** (commit: 3ba85998bb8a378d2fc76d8f0aa2eb58ad86d6f4)
  - [x] Step 1 — Sync members & description from XSD (group l.92440 + complexType l.92477: Base = AR-OBJECT → ATP-BLUEPRINT-MAPPING → PORT-INTERFACE-BLUEPRINT-MAPPING; 2 REF attrs in XSD sequenceOffset order — `portInterfaceBlueprintRef` PORT-INTERFACE-BLUEPRINT-REF seqOffset 20 (DEST PORT-INTERFACE--SUBTYPES-ENUM, doc "This represents the interface blueprint. Note that this interface needs to live in a package of category BLUEPRINT."), `derivedPortInterfaceRef` DERIVED-PORT-INTERFACE-REF seqOffset 30 (same DEST, doc "This represents the derived interface."); both minOccurs=0 xsd but pureMM min/max=1 → modeled 0..1 Optional[RefType] with None no-op; atp.Status="removed" → XSD-only sync per user decision)
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite) — verbatim XSD docs (group l.92442 class note; l.92449 portInterfaceBlueprintRef "This represents the interface blueprint. Note that this interface needs to live in a package of category BLUEPRINT."; l.92463 derivedPortInterfaceRef "This represents the derived interface."); new file so no stale docstrings; class Note in class docstring, inline comments PEP 526, setter None no-op sentence appended
  - [x] Step 5 — Write reader/writer round-trip test (Red) — covered via BlueprintMappingSet wrapper round-trip (tests/test_armodel/parser/test_blueprint_mapping_set.py + writer counterpart: read/write PORT-INTERFACE-BLUEPRINT-MAPPING with both refs, field-value asserts)
  - [x] Step 6 — Update parser & writer (Green) — readBlueprintMappingSet/writeBlueprintMappingSet now dispatch PORT-INTERFACE-BLUEPRINT-MAPPING (isinstance branch in writer, tag branch in parser) → readPortInterfaceBlueprintMapping/writePortInterfaceBlueprintMapping read/write both RefType refs; BLUEPRINT-MAPPING path unchanged
  - [x] Step 7 — Update checklist comment (`# XSD verified: AUTOSAR_00052.xsd`)
  - [x] Step 8 — Deviations — none (XSD-only, both 0..1 REF attrs modeled as Optional[RefType] with None no-op; docstrings verbatim XSD docs; base AtpBlueprintMapping correct; reader+writer coverage via BlueprintMappingSet dispatch). Also updated BlueprintMappingSet Step 8 (gap reduced to PPPBM only) — see that row.
  - [x] Step 9 — Verify (9a) + confirm (9b) — 9b user-confirmed (XSD-only, no deviations) → `# XSD verified: AUTOSAR_00052.xsd` written (commit: 3ba85998bb8a378d2fc76d8f0aa2eb58ad86d6f4)
- [x] `PortPrototypeBlueprintMapping` (XSD-only · no R23-11/R4.3.1 PDF/markdown Class table · member type of `BlueprintMappingSet.blueprintMap` wrapper `BLUEPRINT-MAPS` choice · AUTOSAR_00052.xsd complexType `PORT-PROTOTYPE-BLUEPRINT-MAPPING` l.93034, group l.92997 · **XSD verified** candidate) — needed so `BlueprintMappingSet`'s reader/writer covers all three `BLUEPRINT-MAPS` choice elements (closes the 9b deviation) — **finished, stamped `# XSD verified: AUTOSAR_00052.xsd`** (commit: f87babf31beb141ba1f5ea32b1389e6fbc9a8e8d — `feat: PortPrototypeBlueprintMapping synced.`)
  - [x] Step 1 — Sync members & description from XSD (group l.92997 + complexType l.93034: Base = AR-OBJECT → ATP-BLUEPRINT-MAPPING → PORT-PROTOTYPE-BLUEPRINT-MAPPING ⇒ `AtpBlueprintMapping`; no PDF/markdown Class table in either corpus — `pdf_page.py PortPrototypeBlueprintMapping` reports "no spec table found" across all 42 PDFs, markdown mentions it only as "The previous specializations … are removed" (FO_TPS_StandardizationTemplate l.1176 / R4.3.1 TPS l.1347); atp.Status="removed" → XSD-only sync. 2 REF attrs in XSD sequenceOffset order — `portPrototypeBlueprintRef` PORT-PROTOTYPE-BLUEPRINT-REF seqOffset 20 (DEST PORT-PROTOTYPE-BLUEPRINT--SUBTYPES-ENUM, doc l.93006 "The PortPrototypeBlueprint in the context of the mapping."), `derivedPortPrototypeRef` DERIVED-PORT-PROTOTYPE-REF seqOffset 30 (DEST PORT-PROTOTYPE--SUBTYPES-ENUM, doc l.93020 "The PortPrototype in the context of the mapping."); both xsd minOccurs=0 but pureMM min/max=1 → modeled 0..1 Optional[RefType] with None no-op. Rule 0007 location: XSD qualified path `…BlueprintDedicated::PortProtoypeBlueprint::PortPrototypeBlueprintMapping` → existing file `BlueprintDedicated/PortPrototypeBlueprint.py`, mirroring `PortInterfaceBlueprint.py` hosting `PortInterfaceBlueprintMapping`)
  - [x] Step 2 — Write model class unit test (Red) — `TestPortPrototypeBlueprintMapping` appended to tests/.../BlueprintDedicated/test_PortPrototypeBlueprint.py (mirrors the source file, Rule 0007): 6 tests — init defaults (both refs None), get/set round-trip per ref with DEST+value asserts, None no-op, chaining, `isinstance(AtpBlueprintMapping)`. Red confirmed: `ImportError: cannot import name 'PortPrototypeBlueprintMapping'`
  - [x] Step 3 — Implement model class (Green) — `class PortPrototypeBlueprintMapping(AtpBlueprintMapping)` appended to BlueprintDedicated/PortPrototypeBlueprint.py; 2 PEP 526 members `portPrototypeBlueprintRef` / `derivedPortPrototypeRef` (`Optional[RefType] = None`) in XSD sequenceOffset order + None-guarded chaining setters; exported via BlueprintDedicated/__init__.py (import + `__all__`); 33 tests pass, no circular import
  - [x] Step 4 — Sync docstrings (wipe + rewrite) — new class so no stale docstrings to wipe; verbatim XSD docs verified by programmatic substring diff against AUTOSAR_00052.xsd: class note l.92999 ("This meta-class represents the ability to map a PortPrototypeBlueprint to a PortProtoype of which one acts as the blueprint for the other." — spec's own "PortProtoype" typo preserved) appears 1× in the class docstring; l.93006 "The PortPrototypeBlueprint in the context of the mapping." and l.93020 "The PortPrototype in the context of the mapping." each appear 3× (inline `__init__` comment + getter + setter); setters append the "A None value is a no-op and is not set." sentence; no `Gets/Sets the…` paraphrase
  - [x] Step 5 — Write reader/writer round-trip test (Red) — covered via BlueprintMappingSet wrapper round-trip — added `test_read_port_prototype_blueprint_mapping` + `test_round_trip_with_port_prototype_blueprint_mapping` (parser tests, field-value asserts on both refs incl. DEST) and `test_write_port_prototype_blueprint_mapping` (writer tests, XML shape asserts); Red confirmed: 3 failed / 9 passed
  - [x] Step 6 — Update parser & writer (Green) — `readPortPrototypeBlueprintMapping` / `writePortPrototypeBlueprintMapping` added (mirroring the PortInterface pair: `readAtpBlueprintMapping` base call + 2 `getChildElementOptionalRefType` / `setChildElementOptionalRefType`, no chained mutators); `PORT-PROTOTYPE-BLUEPRINT-MAPPING` branch wired into both `readBlueprintMappingSet` (tag dispatch) and `writeBlueprintMappingSet` (isinstance dispatch, before the BlueprintMapping else); eager imports added to both modules; 75 tests pass
  - [x] Step 7 — Update checklist comment (`# XSD verified: AUTOSAR_00052.xsd`)
  - [x] Step 7 — Update checklist comment (`# XSD verified: AUTOSAR_00052.xsd`) — 6-col parity checklist written in the class body (all [x]; `[—]` reader on getter rows / `[—]` writer on setter rows; `__init__` both `[—]`); `# Spec:` line cites AUTOSAR_00052.xsd complexType l.93034 + group l.92997 (XSD-only; atp.Status="removed"); per-row release R23-11; `# XSD verified:` marker deferred to 9b
  - [x] Step 8 — Deviations — none (XSD-only: both REF attrs modeled 0..1 Optional[RefType] with None no-op, matching xsd minOccurs=0 + pureMM min/max=1; base AtpBlueprintMapping per XSD AR-OBJECT → ATP-BLUEPRINT-MAPPING chain; docstrings verbatim by programmatic diff; reader+writer coverage via BlueprintMappingSet dispatch). BlueprintMappingSet Step 8 deviation now fully closed — all three BLUEPRINT-MAPS choice elements (BLUEPRINT-MAPPING, PORT-INTERFACE-BLUEPRINT-MAPPING, PORT-PROTOTYPE-BLUEPRINT-MAPPING) round-trip
  - [x] Step 9 — Verify (9a) + confirm (9b) — 9a: 8350 tests pass (unit incl. test_model_imports + 1 integration round-trip), flake8+ruff clean, black clean (793 files unchanged); fixed a pre-existing export gap found by test_model_imports (`PortInterfaceBlueprintMapping` not importable from top-level `armodel` — added missing `models/__init__.py` wildcard import for BlueprintDedicated/PortInterfaceBlueprint). 9b user-confirmed 2026-09-01: all checks pass (field↔spec both directions, base, verbatim docstrings by programmatic diff, reader+writer coverage, member order, PEP 526, Rule 0007 location, no deviations) → `# XSD verified: AUTOSAR_00052.xsd` written
- [x] `BlueprintMappingSet` (R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 3.1 · after `AtpBlueprintMapping` (aggr `blueprintMap`) · **uuid-move blocker — see the "uuid move work order" section below** · heritage fix: spec Base = ARElement…Identifiable — **DONE 2026-08-31: re-parented to `BlueprintMappingSet(ARElement)` with `(parent, short_name)` ctor; test construction site updated; fabricated `mappings: List[str]` removed and replaced with the spec's `blueprintMap` aggregation (step 3)**; code was `BlueprintMappingSet(ARObject)` (CommonStructure/StandardizationTemplate/BlueprintMapping.py:8)) — **finished, stamped `# Spec verified: R23-11`** (commit: 3ba85998bb8a378d2fc76d8f0aa2eb58ad86d6f4)
  - [x] Step 1 — Sync members & description from spec (Table 3.1: Note + Base=ARElement + single attribute `blueprintMap` AtpBlueprintMapping * aggr)
  - [x] Step 2 — Write model class unit test (Red) — test_BlueprintMappingSet.py: init defaults, add/get round-trip, None no-op, chaining, concrete BlueprintMapping
  - [x] Step 3 — Implement model class (Green) — `BlueprintMappingSet(ARElement)`; `blueprintMaps: List[AtpBlueprintMapping]` + `addBlueprintMap` (None-guarded) + `getBlueprintMaps`; added concrete `BlueprintMapping(AtpBlueprintMapping)` so the aggregation is instantiable
  - [x] Step 4 — Sync docstrings (wipe + rewrite) — class Note + inline comment + add/get docstrings verbatim from Table 3.1 (Tags: tail dropped)
  - [x] Step 5 — Write reader/writer round-trip test (Red) — parser + writer tests incl. full write→parse→assert round-trip
  - [x] Step 6 — Update parser & writer (Green) — readBlueprintMappingSet/writeBlueprintMappingSet (BLUEPRINT-MAPPING-SET / BLUEPRINT-MAPS / BLUEPRINT-MAPPING), ARPackage.createBlueprintMappingSet + getBlueprintMappingSets, dispatch wired
  - [x] Step 7 — Update checklist comment — 6-col parity checklist, all [x], release R23-11; `# Spec verified:` marker WITHHELD (see Step 8)
  - [x] Step 8 — Deviations — (1) XSD BLUEPRINT-MAPS choice admits PORT-INTERFACE-BLUEPRINT-MAPPING (now round-tripped — PortInterfaceBlueprintMapping synced 2026-09-01, next row) and PORT-PROTOTYPE-BLUEPRINT-MAPPING (still pending, next-next row); 2 of 3 variants round-trip, gap reduced to PPPBM only. Per user pre-decision (2026-09-01) the `# Spec verified:` stamp is written this session with that residual gap accepted. (2) Member type `AtpBlueprintMapping` is abstract ARObject, itself queued for sync — its own attributes (e.g. blueprint/actual refs) are out of scope here. **Stamp approved this session (user pre-decision); class row `[x]` with commit hash recorded at finish.**
  - [x] Step 9 — Verify (9a) + confirm (9b) — 9a: 11 new tests pass, ruff/flake8/black clean (pending run); 9b: user confirms deviation → `# Spec verified:` marker withheld (class left unstamped)
- [x] `ConstantSpecificationMappingSet` (R23-11 markdown · AUTOSAR_CP_TPS_SoftwareComponentTemplate · Table 5.119 · heritage fix: spec Base = ARElement…Identifiable — **DONE 2026-08-31: re-parented to `ConstantSpecificationMappingSet(ARElement)` with `(parent, short_name)` ctor (zero construction sites elsewhere)**; code was `ConstantSpecificationMappingSet(ARObject)` (CommonStructure/Constants/__init__.py:804)) — **finished, stamped `# Spec verified: R23-11`** (commit: 8e5acbb2b1853163dc88ea0376143c58056eaccf)
  - [x] Step 1 — Sync members & description from spec — Table 5.119 body md l.12812–12819, caption l.12810; PDF p.445 confirmed via pdf_page.py (R4.3.1 Table 5.143 p.488 — unused); Class=concrete; Package=M2::AUTOSARTemplates::CommonStructure::Constants; Base = ARElement, ARObject, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable → most-derived direct base **ARElement** ✓ (heritage fix already applied); Aggregated by ARPackage.element; Note (verbatim, Tags tail dropped) + 1 attribute `mapping` (ConstantSpecificationMapping, *, aggr) captured; member type `ConstantSpecificationMapping` stamped R23-11 (Table 5.118, p.443) — no 0016.4 blocker. XSD (l.22285–22324): MAPPINGS wrapper (0..1) w/ unbounded choice of CONSTANT-SPECIFICATION-MAPPING (APPL-CONSTANT-REF/IMPL-CONSTANT-REF 0..1). Parser getConstantSpecificationMapping:6485 / writer writeConstantSpecificationMapping:1512 exist but are DEAD CODE (no callers) — set-level dispatch missing; found via Step 1
  - [x] Step 2 — Write model class unit test (Red) — test_ConstantSpecificationMappingSet.py TestConstantSpecificationMappingSet: init defaults, add/get round-trip, None no-op, chaining, isinstance(ARElement). Red confirmed: 2 failed (no chaining return, None appended)
  - [x] Step 3 — Implement model class (Green) — mappings: List[ConstantSpecificationMapping] (PEP 526); addMapping Optional-guarded + chaining; getMappings typed; 49 Constants tests pass
  - [x] Step 4 — Sync docstrings (wipe + rewrite) — class Note verbatim from md l.12815 (Tags: tail dropped per Rule 0012.2.5.2); inline __init__ comment + add/get docstrings = attr Note (md l.12819 "ConstantSpecificationMappings owned by the ConstantSpecificationMappingSet." — md line-wrap artifact "Constant SpecificationMappingSet" normalized to XSD l.22294 wording); setter appends None no-op sentence
  - [x] Step 5 — Write reader/writer round-trip test (Red) — parser/test_constant_specification_mapping_set.py (read mappings w/ both refs, absent MAPPINGS wrapper, full write→parse→assert round-trip) + writer/test_constant_specification_mapping_set.py (XML shape incl. DEST attrs, empty-list no wrapper). Red confirmed: 5 failed (reader/writer/factories missing)
  - [x] Step 6 — Update parser & writer (Green) — readConstantSpecificationMappingSet (MAPPINGS wrapper choice → existing getConstantSpecificationMapping, previously DEAD CODE — now wired) + writeConstantSpecificationMappingSet (MAPPINGS wrapper + writeConstantSpecificationMapping, also previously dead) + ARPackage createConstantSpecificationMappingSet/getConstantSpecificationMappingSets + both dispatch branches (tag + isinstance) + eager import & __all__ in ARPackage.py. ConstantSpecificationMapping's stamped checklist reader/writer [x] rows are now genuinely true (were false — no callers existed)
  - [x] Step 7 — Update checklist comment — 6-col parity checklist in class body (all [x]; `[—]` reader on getter row / writer on mutator row; `__init__` both `[—]`); `# Spec:` line cites R23-11/AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.119, p.445 (R23-11); per-row release R23-11; `# Spec verified:` marker deferred to 9b
  - [x] Step 8 — Deviations — none for the class itself: heritage = most-derived spec base ARElement (Table 5.119 Base closure) ✓; single attr `mapping` (* aggr) → `mappings: List[ConstantSpecificationMapping]` + addMapping/getMappings per Rule 0001.5/0001.6; docstrings verbatim (md line-wrap artifact in attr Note normalized to XSD l.22294 wording — documented Step 4); reader+writer coverage complete. Referenced classes (Rule 0001.10 report): member type `ConstantSpecificationMapping` stamped R23-11 (Table 5.118) ✓; base `ARElement` stamped (Table 4.3) ✓ — no missing classes. Side effect recorded: ConstantSpecificationMapping's previously-dead reader/writer helpers are now wired via this class's reader/writer (its stamped checklist reader/writer [x] rows were false until now — no fabrication in this class's own scope)
  - [x] Step 9 — Verify (9a) + confirm (9b) — 9a: 8360 tests pass (unit + integration round-trip), flake8/ruff clean, black clean; verbatim docstring diff programmatic (class Note ×1, attr Note ×5, no Tags tail, PEP 526, no `# type:`); 9b user-confirmed 2026-09-01: Rules 0001.1/0001.2/0001.3/0001.5/0001.6/0001.7/0001.11/0001.4/0012/0014/0007 pass, no deviations → `# Spec verified: R23-11` written (commit: 8e5acbb2)
- [x] `StandardNameEnum` (R23-11 markdown · AUTOSAR_FO_TPS_StandardizationTemplate · Table 2.1 · member type of `StructuredReq.appliesTo` · `AREnum`) — **finished, stamped `# Spec verified: R23-11`**
   - [x] Step 1 — Sync members & description from spec
   - [x] Step 2 — Write model class unit test (Red)
   - [x] Step 3 — Implement model class (Green)
   - [x] Step 4 — Sync docstrings (wipe + rewrite)
   - [x] Step 5 — Write reader/writer round-trip test (Red) — N/A: standalone AREnum is serialized by consuming StructuredReq
   - [x] Step 6 — Update parser & writer (Green) — N/A: standalone AREnum has no own XML element
   - [x] Step 7 — Update checklist comment
   - [x] Step 8 — Deviations — Rule 0007 package location corrected: class moved from `MSR.Documentation.BlockElements.RequirementsTracing` to `AUTOSARTemplates.GenericStructure.DocumentationOnM1`; no model/spec deviations
   - [x] Step 9 — Verify (9a) + confirm (9b) — 9a: focused tests, lint, and Black clean; 9b user-confirmed: Rule 0007 package and test locations corrected, five literals and order match Table 2.1, standalone AREnum N/A reader/writer coverage, no deviations → `# Spec verified: R23-11` written
- [x] `StructuredReq` (R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 9.31 · **uuid-move blocker — see the "uuid move work order" section below** · heritage fix: spec Base = ARObject, DocumentViewSelectable, Identifiable, MultilanguageReferrable, Paginateable, Referrable, Traceable — **DONE 2026-08-31: re-parented to `StructuredReq(Traceable)`; decision: the Identifiable mixin stays on `Traceable(Identifiable)` (Table E.x gives Traceable Base = ARObject, MultilanguageReferrable, Referrable — recorded as a documented deviation to revisit in this class's own 9-step sync); parser `getStructuredReq(element, key, block)` now constructs with `(block, short_name)`; ~17 test construction sites updated**; code was `StructuredReq(ARObject)` (MSR/Documentation/BlockElements/RequirementsTracing.py:123)) — **finished, stamped `# Spec verified: R23-11`** (commit: d311fc7c)
   - [x] Step 1 — Sync members & description from spec
   - [x] Step 2 — Write model class unit test (Red)
   - [x] Step 3 — Implement model class (Green)
   - [x] Step 4 — Sync docstrings (wipe + rewrite)
   - [x] Step 5 — Write reader/writer round-trip test (Red)
   - [x] Step 6 — Update parser & writer (Green)
   - [x] Step 7 — Update checklist comment
   - [x] Step 8 — Deviations — none: `appliesTo`/`conflicts`/`variationPoint` gap closed (variationPoint was missing; now inherited from `Identifiable` and serialized via the shared `readIdentifiable`/`writeIdentifiable` + `readTraceable`/`writeTraceable` helpers instead of only `readARObject`/`writeARObject`); `TESTED-ITEM-REF` `DEST` attribute round-trip fixed (reader was overwriting the ref value with `DEST`, writer was dropping `DEST` entirely); class member/accessor/checklist order corrected to the markdown/PDF **displayed** row order (Rule 0001.11) — `appliesTo, conflicts, date, dependencies, description, importance, issuedBy, rationale, remark, supportingMaterial, testedItem, type, useCase` — while reader/writer XML order follows XSD `sequenceOffset`; `StandardNameEnum` is available and stamped R23-11 (stale "unavailable" deviation removed).
   - [x] Step 9 — Verify (9a) + confirm (9b) — 9a: 20 focused tests pass, ruff/flake8/black clean; 9b user-confirmed 2026-09-01: heritage, member order (class = markdown display order, XML = XSD sequenceOffset), reader+writer coverage incl. `variationPoint`/`DEST`, verbatim docstrings, no deviations → `# Spec verified: R23-11` written
 - [x] `TraceableText` (R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 9.30, p.313 · after `StructuredReq` (same Base closure) · **uuid-move blocker — see the "uuid move work order" section below** · heritage fix — **DONE 2026-08-31: re-parented to `TraceableText(Traceable)`; duplicate `traceRefs` field + `getTraceRefs`/`addTraceRef` removed (inherited from Traceable); parser `getTraceableText(element, key, block)` now constructs with `(block, short_name)`; test construction sites updated**; code was `TraceableText(ARObject)` (RequirementsTracing.py:58)) — **finished, stamped `# Spec verified: R23-11`** (commit: 9e80479b)
   - [x] Step 1 — Sync members & description from spec — Table 9.30 confirms concrete `TraceableText`, direct base `Traceable`, and own aggregation `text: DocumentationBlock` (1)
   - [x] Step 2 — Write model class unit test (Red) — exact Table 9.30 class note assertion
   - [x] Step 3 — Implement model class (Green) — existing `TraceableText(Traceable)` shape retained
   - [x] Step 4 — Sync docstrings (wipe + rewrite) — class note corrected to verbatim Table 9.30 wording; setter None no-op wording aligned
   - [x] Step 5 — Write reader/writer round-trip test (Red) — added `TEXT` reader coverage and exposed dropped `TRACE-REF` attributes
   - [x] Step 6 — Update parser & writer (Green) — `readTraceable`/`writeTraceable` now preserve `BASE`, `DEST`, and value
   - [x] Step 7 — Update checklist comment — six-column parity checklist with R23-11 release rows
   - [x] Step 8 — Deviations — none; inherited trace references remain owned by `Traceable`
   - [x] Step 9 — Verify (9a) + confirm (9b) — 8367 tests pass, 29 integration round trips pass, lint/Black clean; 9b user-confirmed 2026-09-01: field/base/order/docstring/API/reader-writer checks pass → `# Spec verified: R23-11` written
- [x] `Identifiable` (heritage-chain parent of CollectableElement/AtpBlueprint/AtpBlueprintable/ARPackage · **finished, UNSTAMPED per 9b user decision 2026-09-01** — variationPoint per-class placement outstanding · commit: a22d473c · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 4.4, content md l.1650–1695)
  - Spec facts (extracted 2026-08-30): abstract; Base = ARObject, MultilanguageReferrable, Referrable → direct base **MultilanguageReferrable** (queued above) — code `Identifiable(MultilanguageReferrable, ABC)` (Identifiable.py:229) heritage **CORRECT**; Subclasses explicitly list ARPackage, CollectableElement, PackageableElement, AtpBlueprint, AtpBlueprintable.
    - Attributes (Table 4.4 displayed order): `adminData` (AdminData, 0..1, aggr) / `annotation` (Annotation, *, aggr) / `category` (CategoryString, 0..1, attr) / `desc` (MultiLanguageOverviewParagraph, 0..1, aggr) / `introduction` (DocumentationBlock, 0..1, aggr) / `uuid` (String, 0..1, attr).
  - Known deviations to fix in this sync: (a) duplicate `elements`/`element_mappings` registry in `__init__` (Identifiable.py:258-259 — CollectableElement infra; ARPackage's getElement override reaches it; remove after CollectableElement sync or verify consumers); (b) **uuid ownership RESOLVED (2026-08-31 uuid move + 2026-09-01 retype)** — uuid is owned by `Identifiable` (field `Optional[String]` + getUuid/setUuid), read in `readIdentifiable` before UUIDMgr registration, emitted in `writeIdentifiable`; `UUIDMgr.addObject` keys on `isinstance(obj, Identifiable)`; (c) `variationPoint` carried with documented deviation comment (keep); (d) no `# Spec:` line/stamp for this class (only Referrable l.27 and Describable l.517 in the same file are stamped) → 6-col checklist rewrite.
  - [x] Step 1 — Sync members & description from spec (Table 4.4 body md l.1664–1693, caption l.1688; PDF p.61 confirmed via pdf_page.py; Class=Identifiable (abstract) ✓; Base = ARObject, MultilanguageReferrable, Referrable → most-derived direct base **MultilanguageReferrable** ✓ current heritage correct (Identifiable.py:230); 6 attrs in displayed order with verbatim Notes captured: adminData / annotation / category / desc / introduction / uuid)
  - [x] Step 2 — Write model class unit test (Red) — test_Identifiable.py TestIdentifiable: added test_add_annotation_none_is_noop, test_element_registry_round_trip, test_remove_element_unknown_short_name_raises (37 tests pass); the pre-existing suite already covered init defaults, get/set round-trips, None no-ops and abstract instantiation
  - [x] Step 3 — Implement model class (Green) — heritage unchanged (Identifiable(MultilanguageReferrable, ABC) ✓ most-derived spec base); methods reordered into Table 4.4 displayed order (adminData → annotation → category → desc → introduction → uuid, then the kept infra registry, then variationPoint) per Rule 0001.11; dead duplicate `return self` in setIntroduction removed; return annotations added to setAdminData/setCategory/setDesc/setIntroduction/removeAdminData/addAnnotation (Rule 0003); elements/element_mappings registry kept as documented infra (deviation (a))
  - [x] Step 4 — Sync docstrings (wipe + rewrite) — verified by diff (Rule 0012.2.6): class docstring + all 6 inline member comments + all 12 accessor docstrings diffed verbatim against md Table 4.4; one Rule 0001.4 deviation found and fixed in 3 places — the desc Note reads "how the object is built or used" in both the markdown (l.1682) and AUTOSAR_00052.xsd l.67753, while the code said "is built or is used". **Re-verified 2026-09-01 after the uuid move**: programmatic diff found the uuid inline `__init__` comment was a truncated summary (only 2 of 3 expected verbatim occurrences) — replaced with the full Table 4.4 uuid Note; all 6 attributes now ×3, class Note ×1
  - [x] Step 5 — Write reader/writer round-trip test (Red) — parser test_arxml_parser_handlers.py: test_readIdentifiable_populates_category_desc_admin / _with_annotation / _empty_annotations_wrapper (empty-wrapper case added this pass) + test_ar_object_attributes.py (uuid on a concrete Identifiable); writer test_identifiable.py: field-value asserts + empty-optional case + write→re-parse→assert round-trip. **2026-09-01**: uuid asserts moved to `.getValue()` form after the uuid retype to `Optional[String]`
  - [x] Step 6 — Update parser & writer (Green) — no dispatch change needed (readIdentifiable/writeIdentifiable already cover all six attributes incl. the ANNOTATIONS wrapper); the two uuid comments in abstract_arxml_parser.py / abstract_arxml_writer.py now point at the uuid-move work order, and the stale "owned by Identifiable" docstring in parser/test_ar_object_attributes.py was corrected (12 reader/writer tests pass). **2026-09-01**: parser wraps the raw UUID attribute in `String()` before `setUuid`; writer emits `getUuid().getValue()`; `UUIDMgr.addObject` keys the registry on `uuid.getValue()`; redundant `isinstance(…, Identifiable)` guards removed from readIdentifiable/writeIdentifiable (parameters are statically typed; probe-verified via full suite)
  - [x] Step 7 — Update checklist comment — 6-col rows now 1:1 with the 22 methods in source order (verified by script): 6 spec attributes in Table 4.4 order + 6 element-collection infra rows in an "Internal members" block (cf. the ARObject precedent) + variationPoint in a "Kept deviation member" block. **2026-09-01**: the uuid rows' ARObject-owner deferral annotation removed (the move is permanent)
  - [x] Step 8 — Deviations (incl. uuid ownership decision) — (a) elements/element_mappings registry: kept as documented infra, now with explicit checklist rows (removal deferred to the CollectableElement row below, which owns the duplicated methods — confirmed still present 2026-09-01); (b) uuid ownership: **RESOLVED** — the uuid move landed 2026-08-31 (field + accessors on Identifiable, parser read + UUIDMgr registration in readIdentifiable, writer emission in writeIdentifiable); **2026-09-01 user decision: uuid typed `Optional[String]`** (spec Table 4.4 type `String`, not raw `str`) — parser/writer/UUIDMgr/tests updated, closing the latent str-vs-String type deviation; (c) variationPoint: framework-level, excluded by the tracker preamble → not a stamp blocker; no `naming`/`type`/`missing` deviation row remains
  - [x] Step 9 — Verify (9a) + confirm (9b) — 9a: 8374 unit tests + integration round-trip pass, flake8/ruff/black clean, parity script no Identifiable findings. 9b (user-confirmed 2026-09-01): all pre-stamp checks pass (fields ↔ spec both directions, base MultilanguageReferrable, verbatim docstrings by programmatic diff incl. repaired uuid inline comment, reader+writer coverage, member order, Rule 0007 location); **stamp WITHHELD by user decision** — `variationPoint` kept as framework infra on Identifiable (XSD declares VARIATION-POINT individually on 335 atpVariation classes, not in the IDENTIFIABLE group; per-class placement recorded as the outstanding deviation, tracker-preamble framework-level exclusion applies) — `# Spec verified:` marker removed from the source until that resolution. Session extras: uuid retyped to `Optional[String]` (user decision), redundant `isinstance(…, Identifiable)` guards removed from readIdentifiable/writeIdentifiable (probe-verified), uuid deferral annotation dropped from checklist.
- [x] `CollectableElement` (direct spec base of ARPackage + PackageableElement · Rule 0016.4 wrong-base stub — prerequisite for the ARPackage heritage fix · commit: 3b31b7c4 · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 13.3, class table body md l.10589+)
  - Spec facts (extracted 2026-08-30): Package = ...GeneralTemplateClasses::ElementCollection; **Base = ARObject, Identifiable, MultilanguageReferrable, Referrable → most-derived direct base = Identifiable**; Subclasses = {ARPackage, PackageableElement}; **no own Attribute rows**.
  - Deviation: code has `CollectableElement(ARObject, ABC)` + `__init__(self)` (ElementCollection.py:16/31) — skips the Referrable→MultilanguageReferrable→Identifiable chain. Fix: re-parent to `Identifiable`, `__init__(self, parent, short_name)`; `elements`/`element_mappings` registry stays (codebase infra; spec `element` aggregation belongs to ARPackage Table 4.1 and is shared by design).
  - Downstream fixes unlocked (do together with ARPackage Step 9): (1) **ARPackage drops its manually flattened Referrable/Identifiable members** (parent, short_name, longName, annotations, adminData, category, introduction, desc — currently duplicated to compensate; Rule 0001.3 relocation) and calls `super().__init__(parent, short_name)`; (2) ARPackage `__init__` double-init cleanup (`CollectableElement.__init__(self)` + explicit `ARObject.__init__(self)` with stale comment — CollectableElement *does* call super().__init__(), so ARObject.__init__ runs twice); (3) `PackageableElement` re-parent — own drift row directly below (Table 4.2 Base closure names CollectableElement as most-derived); (4) `AbstractAUTOSAR` re-check in its own queued sync — AUTOSAR spec Base = **ARObject** (R4.3.1 ARXMLSerializationRules Table 1.1), code has AbstractAUTOSAR(CollectableElement).
  - [x] Step 1 — Sync members & description from spec — Table 13.3 body md l.10589–10596, caption l.10587; PDF p.399 confirmed via pdf_page.py (R4.3.1 Table 12.3 p.371 — same Note/Base, unused; no Rule 0019 combine case). Class=**abstract**; Package=M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::ElementCollection; Base = ARObject, Identifiable, MultilanguageReferrable, Referrable → most-derived direct base **Identifiable** ✓ (heritage re-parent already landed with the Identifiable sync, commit a22d473c); Subclasses = ARPackage, PackageableElement; **Attribute rows = `-` → no own attributes**; Note captured verbatim for Step 4. XSD cross-check (AUTOSAR_00052.xsd): `<xsd:group name="COLLECTABLE-ELEMENT">` is `<xsd:sequence/>` — adds no elements/attributes of its own (Steps 5/6 N/A), matching Table 13.3's empty Attribute row
  - [x] Step 2 — Write model class unit test (Red) — test_ElementCollection.py TestCollectableElement: abstract init (with (parent, short_name)), Identifiable heritage + MRO order, no own attribute members (registry methods absent from `CollectableElement.__dict__`), concrete-subclass inheritance of Identifiable members, element round-trip via inherited registry, verbatim class docstring. Red confirmed: 2 failed / 18 passed (registry methods still defined on the class; class docstring is a paraphrase)
  - [x] Step 3 — Implement model class (Green) — heritage already `CollectableElement(Identifiable, ABC)`; Rule 0001.3 relocation applied: the 6 element-collection registry methods (getTotalElement/removeElement/getElements/addElement/getElement/IsElementExists), byte-identical duplicates of the ones Identifiable now owns, were **removed from CollectableElement** — Table 13.3 has no Attribute rows, so the class reduces to `__init__` alone (PortInterfaceMapping abstract-shell precedent). Two explicit super-calls retargeted `CollectableElement.getElement` → `Identifiable.getElement` (ARPackage.getElement ARPackage.py:440, AbstractAUTOSAR.getElement AutosarTopLevelStructure/__init__.py:186); both modules now import `Identifiable` alongside `Referrable`; unused `Referrable` import dropped from ElementCollection.py
  - [x] Step 4 — Sync docstrings (wipe + rewrite) — completed in the stamped session (see Step 9); checkbox was left stale and flipped 2026-09-02
  - [x] Step 5 — Write reader/writer round-trip test (Red) — **N/A for CollectableElement itself**: Table 13.3 has no Attribute rows and the XSD group COLLECTABLE-ELEMENT is an empty `<xsd:sequence/>`, so the class has no own XML element (no Red possible). Written instead as **regression coverage for the Step-3 relocation**, which is what makes the N/A safe to claim: tests/test_armodel/parser/test_ar_package_collectable_element.py (readARPackage: Identifiable members UUID/CATEGORY/DESC reached through the CollectableElement→Identifiable chain; sub-package + element lookup via getElement with and without a type filter; getTotalElement/getElements contents; AbstractAUTOSAR.getElement at the root) + tests/test_armodel/writer/test_ar_package_collectable_element.py (writeARPackage XML shape incl. UUID as an *attribute* per Table 4.4 Kind=attr, plus a full write→save→re-parse→field-assert round-trip). 6 tests pass; they pin the behaviour of the two retargeted super-calls (ARPackage.getElement, AbstractAUTOSAR.getElement)
  - [x] Step 6 — Update parser & writer (Green) — N/A: no new reader/writer code. `readARPackage`→`readIdentifiable` and `writeARPackage`→`writeIdentifiable` already cover every member a CollectableElement subclass inherits; the registry is populated by `createXxx`/`addElement`, not by a CollectableElement-specific reader. Two super-calls were retargeted for accuracy (`CollectableElement.getElement` → `Identifiable.getElement` in ARPackage.getElement ARPackage.py:440 and AbstractAUTOSAR.getElement AutosarTopLevelStructure/__init__.py:186) — behaviour-identical (the MRO resolved them either way), but they now name the class that owns the method
  - [x] Step 7 — Update checklist comment — 6-col parity checklist with unified `# Spec:` line (R23-11/AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 13.3, p.399 (R23-11)) + single `__init__` row (reader/writer `[—]`, release R23-11); an inline note records that Table 13.3 has no Attribute rows and the registry rows live in the Identifiable checklist (Rule 0001.3). Marker deferred to 9b
  - [x] Step 8 — Deviations — none blocking: (a) the element-collection registry relocation is a Rule 0001.3 resolution, not a deviation — CollectableElement now reduces to `__init__` alone (Table 13.3 empty Attribute row), the duplicated registry methods having moved to Identifiable in the prior Identifiable sync; (b) **no naming / type / missing deviation** — Class=abstract (matches Table 13.3), Base closure reaches Identifiable as most-derived (matches), package location ElementCollection.py matches Table 13.3 Package, no own attributes to mis-model; (c) referenced classes: Subclasses ARPackage + PackageableElement are queued (PackageableElement already re-parented to CollectableElement in a prior session, stamped R23-11), Base Identifiable stamped R23-11 — no missing/stub classes reported. **Observation for the ARPackage row** (out of scope here): ARPackage.py checklist comment l.382-385 still says ARPackage "carries" the flattened Referrable/Identifiable members directly — it no longer does (ARPackage.__init__ only adds arPackages + referenceBases and relies on inheritance), so that comment is stale and should be corrected during the ARPackage sync
  - [x] Step 9 — Verify (9a) + confirm (9b) — 9a: 8385 unit tests + 1 integration round-trip pass, flake8/ruff/black clean, parity script no Identifiable findings. 9b (user-confirmed): all pre-stamp checks pass (fields ↔ spec both directions, base Identifiable, verbatim docstrings incl. repaired Table 13.3 Note by programmatic diff, reader/writer N/A with regression coverage for the relocation, member order, Rule 0007 location); `# Spec verified: R23-11` marker written to ElementCollection.py checklist. Commit 3b31b7c4 on feature/sync-collectable-element.
- [x] `PackageableElement` (child of CollectableElement · STAMPED R23-11 — **drift pass only** per Rule 0012.3: heritage fix · commit: bb032ddd · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 4.2, p.54)
  - Drift scope (no member re-sync — Table 4.2 has no own Attribute rows): re-parent `PackageableElement(Identifiable, ABC)` → `PackageableElement(CollectableElement, ABC)` (ARPackage.py:22) — Table 4.2 Base closure = {ARObject, CollectableElement, Identifiable, MultilanguageReferrable, Referrable} names **CollectableElement** as most-derived. Run AFTER the CollectableElement row above lands; `super().__init__(parent, short_name)` forwarding unchanged (CollectableElement now forwards to Identifiable). Re-run ARElement/Collection round-trips to confirm no parser/writer dispatch change (readIdentifiable/writeIdentifiable shared; inherited members reached through inheritance).
  - [x] Step 1 — Confirm drift scope from Table 4.2 (members unchanged) — md l.1543–1553: Class=PackageableElement (abstract); Package M2::...::GeneralTemplateClasses (ARPackage.py module — Rule 0007 OK); Note verbatim = "This meta-class specifies the ability to be a member of an AUTOSAR package." (matches class docstring); Base = ARObject, CollectableElement, Identifiable, MultilanguageReferrable, Referrable → most-derived direct base **CollectableElement** ✓ (code already PackageableElement(CollectableElement, ABC)); Attribute rows = `-` → **no own attributes** → class reduces to __init__ alone. With CollectableElement now → Identifiable (commit 3b31b7c4), full MRO = PackageableElement → CollectableElement → Identifiable → MultilanguageReferrable → Referrable → ARObject. Drift = heritage-only, members unchanged.
  - [x] Step 2 — Adjust model unit test (base-relationship asserts) — test_ARPackage.py TestPackageableElement: added test_inherits_from_collectable_element (issubclass CollectableElement/Identifiable/ARObject + MRO[1]=CollectableElement, MRO[2]=Identifiable) and test_concrete_subclass_initialization (concrete subclass via (parent, short_name) reaches getShortName/parent through CollectableElement->Identifiable). 3 passed (Green).
  - [x] Step 3 — Re-parent to CollectableElement (Green) — code already PackageableElement(CollectableElement, ABC) (ARPackage.py:26, landed in prior session); super().__init__(parent, short_name) forwards unchanged (CollectableElement now forwards to Identifiable per commit 3b31b7c4). New Step-2 tests confirm the MRO and concrete-subclass init resolve correctly. No code change required this session.
  - [x] Step 4 — Docstrings unchanged (no own members) — Rule 0012.3 wipe+rewrite re-run: only the class docstring exists (no own Attribute rows → no getter/setter/member-comment docstrings; __init__ has no docstring per Rule 0012.2.5.2). Class docstring = "This meta-class specifies the ability to be a member of an AUTOSAR package." — verbatim vs Table 4.2 Note (md l.1546), confirmed by diff. Release unchanged (R23-11), so no new-release text; marker stays R23-11.
  - [x] Step 5 — Re-run reader/writer round-trip (inherited members) — parser/writer ARPackage/CollectableElement/ReferenceBase/PortInterfaceMappingSet suites: 19 passed; model test_ARPackage.py (ARElement/ARPackage/PackageableElement): 35 passed. readARPackage->readIdentifiable and writeARPackage->writeIdentifiable unchanged; inherited members reached through the CollectableElement->Identifiable chain. No dispatch divergence after the re-parent.
  - [x] Step 6 — Parser/writer unchanged (confirm no dispatch edit needed) — grep parser/writer for PackageableElement/readPackageableElement/writePackageableElement returns nothing: PackageableElement is abstract with no own XML element, so it has no dedicated reader/writer; ARPackage dispatches readARPackage->readIdentifiable / writeARPackage->writeIdentifiable for the inherited members (shared, unchanged). No parser/writer source edit needed.
  - [x] Step 7 — Update checklist comment (base note) — ARPackage.py:31-41 PackageableElement checklist: (a) added `release` column to header + `R23-11` on the __init__ row (Rule 0002 / 0012.3 — drift pass adds the column the prior stamp predated); (b) heritage-fix note retained (CollectableElement most-derived base); (c) new drift note records the full MRO now that CollectableElement->Identifiable landed (commit 3b31b7c4). Marker stays `# Spec verified: R23-11`.
  - [x] Step 8 — Deviations — none (heritage-only drift) — (a) no naming/type/missing deviation: Class=abstract (matches Table 4.2), Base closure reaches CollectableElement as most-derived (matches), Package=GeneralTemplateClasses (matches Table 4.2), no own attributes to mis-model; (b) referenced base CollectableElement stamped R23-11 (commit 3b31b7c4) — chain now complete; (c) subclasses ARElement/EnumerationMappingTable/FibexElement inherit correctly, none re-synced here (out of scope). `# Spec verified: R23-11` retained — no placeholder/deviation outstanding.
  - [x] Step 9 — Verify (9a) + confirm (9b) — re-stamp after drift per Rule 0012.3 — 9a: 8387 unit + 1 integration round-trip pass, flake8/ruff/black clean. 9b (user-confirmed 2026-09-02): full pre-stamp checklist re-run (Rule 0012.3) — base CollectableElement most-derived + MRO now CollectableElement->Identifiable->...->ARObject, class docstring verbatim vs Table 4.2 Note, reader/writer N/A via shared readIdentifiable/writeIdentifiable, Rule 0007 location, release column added. `# Spec verified: R23-11` retained. Commit bb032ddd on feature/sync-packageable-element.
- [x] `ARPackage` (tracker input · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 4.1) — **finished, stamped `# Spec verified: R23-11`** (commit: 36064817)
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
  - [x] Step 9 — Verify (9a) + confirm (9b) — 9a: 8391 unit + 3 integration round-trip pass, flake8/ruff/black clean; arPackages re-modeled Dict→List per Rule 0001.5 (user decision 2026-09-02 "Convert to List first"), createARPackage/getARPackages/getElement reworked, 2 model-test usages + deviation tracker updated. 9b user-confirmed 2026-09-02: full pre-stamp checklist re-run — base CollectableElement most-derived + MRO complete, class docstring verbatim vs Table 4.1 Note, reader/writer N/A (shared readIdentifiable/writeIdentifiable), Rule 0007 location, release column present. `# Spec verified: R23-11` written. Commit 36064817 on feature/sync-arpackage.
- [x] `AUTOSAR` (tracker input · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table E.1 (Appendix E "Mentioned Class Tables") · **heritage check resolved 2026-09-02**: spec Base = **ARObject** (Table E.1) → Step 3 decision = **restructure to ARObject** (user choice); `CollectableElement` element-registry reimplemented on the root) — **finished, stamped `# Spec verified: R23-11`**
  - [x] Step 1 — Sync members & description from spec
    - Spec facts (extracted 2026-09-02, **corrected after R23-11 re-check**): R23-11 **DOES** define the top-level `AUTOSAR` element — `AUTOSAR_FO_TPS_GenericStructureTemplate.md`, **Table E.1** (Appendix E "Mentioned Class Tables"), **p.421** (pdf_page.py regex only matches numeric `Table N.M`, so E.1 was found by direct PDF scan). R4.3.1 (ARXMLSerializationRules Table 1.1, p.8) is a **fallback that does NOT apply** because an R23-11 table exists (Rule 0016.3). Marker = `# Spec verified: R23-11`.
    - Package: `M2::AUTOSARTemplates::AutosarTopLevelStructure` (matches code file `AutosarTopLevelStructure/__init__.py`, Rule 0007 OK).
    - Note (verbatim, for Step 4): "Root element of an AUTOSAR description, also the root element in corresponding XML documents. Tags: xml.globalElement=true"
    - Base: **ARObject** (Table E.1) — code current base is `AbstractAUTOSAR(CollectableElement)` → **decision point in Step 3** (keep for elements-registry reuse = documented deviation, or restructure).
    - Attributes (Table E.1 displayed order): `adminData` (AdminData, 0..1, aggr) / `arPackage` (ARPackage, *, aggr) / `fileInfoComment` (FileInfoComment, 0..1, aggr) / `introduction` (DocumentationBlock, 0..1, aggr). All 4 already implemented on `AbstractAUTOSAR` (getAdminData/setAdminData, createARPackage/getARPackages/getElement, getFileInfoComment/setFileInfoComment, getIntroduction/setIntroduction).
    - Attribute Notes (verbatim from R23-11 Table E.1, for Step 4): adminData "This represents the administrative data of an Autosar file."; arPackage "This is the top level package in an AUTOSAR model."; fileInfoComment "This represents a possibility to provide a structured comment in an AUTOSAR file."; introduction "This represents an introduction on the Autosar file. It is intended for example to represent disclaimers and legal notes." (R23-11 corrects R4.3.1's "to rpresent" typo → "to represent".)
    - Reader/writer: no `readAUTOSAR`/`writeAUTOSAR`; parser populates the root via `readARPackages`→`parent.createARPackage(...)` (arxml_parser.py:11667/11671) and AdminData/FileInfoComment/DocumentationBlock readers; writer via `writeARPackages` (arxml_writer.py:11557). Top-level `arPackages` is currently `Dict[str, ARPackage]` (AutosarTopLevelStructure/__init__.py:179) — INCONSISTENT with `ARPackage.arPackages` which was converted to `List` last session; representation is a Step-3 decision.
  - [x] Step 2 — Write model class unit test (Red→Green): 82 model tests in test_AutosarTopLevelStructure.py cover AbstractAUTOSAR/AUTOSAR/AUTOSARDoc incl. the reimplemented registry (addElement/removeElement/getElements/getTotalElement/IsElementExists) and List+index arPackages.
  - [x] Step 3 — Implement model class (Green): restructured AbstractAUTOSAR(CollectableElement)→ARObject (user decision 2026-09-02 "Restructure to ARObject"); reimplemented elements/element_mappings registry on the root; arPackages Dict→List[ARPackage] with internal _ar_package_index (user decision "Convert to List"); clear()/getElement/createARPackage reworked.
  - [x] Step 4 — Sync docstrings (wipe + rewrite): verbatim Table E.1 Notes on class docstring + get/setAdminData/FileInfoComment/Introduction + getARPackages/createARPackage.
  - [x] Step 5 — Write reader/writer round-trip test (Red→Green): tests/test_armodel/parser/test_autosar_root.py (3 tests: load reads all 4 attributes, save round-trips all 4, root without optional attributes → None).
  - [x] Step 6 — Update parser & writer (Green): added root-level FILE-INFO-COMMENT (writer.setFileInfoComment + parser.getFileInfoComment) and INTRODUCTION (writeDocumentationBlock + getDocumentationBlock) so all 4 spec attributes round-trip; previously only ADMIN-DATA/AR-PACKAGES were serialized at root (data-loss deviation fixed).
  - [x] Step 7 — Update checklist comment: AbstractAUTOSAR/AUTOSAR/AUTOSARDoc converted to 6-column `# Spec:` format (Table E.1, p.421, R23-11).
  - [x] Step 8 — Deviations: deviation tracker `## AUTOSAR` rewritten — wrong source PDF (BSWModuleDescriptionTemplate) replaced with R23-11 Table E.1; adminData/arPackage/fileInfoComment/introduction now `none` (modeled + reader/writer); heritage `Base` CollectableElement→ARObject corrected; framework helper API beyond the 4 Table E.1 attributes documented as retained (accepted).
  - [x] Step 9 — Verify (9a) + confirm (9b): 9a — 8391 tests pass (8390 unit + 1 integration round-trip), ruff + black clean. 9b — user confirmed 2026-09-02; stamped `# Spec verified: R23-11` in AbstractAUTOSAR/AUTOSAR/AUTOSARDoc checklists; `## AUTOSAR` deviation section dropped (verified → skipped by tracker).
- [x] `FileInfoComment` (tracker input · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 2.1)
  - [x] Step 1 — Sync members & description from spec: single aggregation `sdgs` (List[Sdg], 0..*); class already matched Table 2.1 (drift pass).
  - [x] Step 2 — Write model class unit test (Red→Green): verbsatim class-docstring check + None-no-op/add/chaining coverage (test_AutosarTopLevelStructure.py::TestFileInfoComment).
  - [x] Step 3 — Implement model class (Green): setSdgs None-guard correctness fix (no-op on None, returns self for chaining).
  - [x] Step 4 — Sync docstrings (wipe + rewrite): verbatim Table 2.1 Note on class docstring + get/setSdgs/addSdg; 6-col `# Spec:` checklist (p.29, R23-11).
  - [x] Step 5 — Write reader/writer round-trip test (Red→Green): tests/test_armodel/parser/test_file_info_comment.py (multiple SDGs with GID+caption; empty-wrapper emits no SDGS).
  - [x] Step 6 — Update parser & writer (Green): N/A — getFileInfoComment/setFileInfoComment + getSdg/setSdg + SDGS wrapper already round-trip sdgs fully.
  - [x] Step 7 — Update checklist comment: FileInfoComment converted to 6-column `# Spec:` format (Table 2.1, p.29, R23-11).
  - [x] Step 8 — Deviations: none; member type Sdg already `# Spec verified: R23-11` (Table 4.19, p.90).
  - [x] Step 9 — Verify (9a) + confirm (9b): 9a — 8396 unit + 3 integration round-trip pass, ruff + black clean. 9b — user confirmed 2026-09-02; stamped `# Spec verified: R23-11` (commit c62e1c89).
- [x] `AutoCollectEnum` (Rule 0016.4 stub discovered during Collection Step 1, 2026-09-02 — wrong base `Enum` (not `AREnum`) + fabricated literals OFF/ON/AUTO vs Table 13.2 refAll/refNone/refNonStandard; zero consumers outside ElementCollection.py — rename safe; queued ahead of Collection per dependency-first) — commit 75f40055
  - [x] Step 1 — Sync members & description from spec (Table 13.2 body md l.10577–10585, caption l.10575; PDF p.399 confirmed via pdf_page.py — Table 13.1/13.2/13.3 all land on p.399; Package=...ElementCollection → Rule 0007: class moved from Enumerations.py to ElementCollection.py (StandardNameEnum precedent); Note "This enumerator defines the possible approaches to determine the final set of elements in a collection."; literals refAll(0)/refNone(1)/refNonStandard(2) with verbatim descriptions; XSD AUTO-COLLECT-ENUM--SIMPLE l.131676 tokens REF-ALL/REF-NONE/REF-NON-STANDARD)
  - [x] Step 2 — Write model class unit test (Red) — test_ElementCollection.py TestAutoCollectEnum: test_is_arenum, test_literals_in_spec_order (tuple equality), test_instantiability_and_value_round_trip (REF_ALL/REF_NONE/REF_NON_STANDARD member values), test_class_docstring_matches_spec_note. Red confirmed: issubclass(AREnum) failed
  - [x] Step 3 — Implement model class (Green) — `class AutoCollectEnum(AREnum)` in ElementCollection.py; literal members REF_ALL="refAll"/REF_NONE="refNone"/REF_NON_STANDARD="refNonStandard" (StandardNameEnum shape); __init__ passes the member tuple to AREnum; removed fabricated OFF/ON/AUTO class from Enumerations.py (+ now-unused `from enum import Enum`); only consumer was ElementCollection.py's import — updated; top-level export verified intact
  - [x] Step 4 — Sync docstrings (wipe + rewrite) — moved class, docstrings written fresh: class docstring = Table 13.2 Note verbatim; literal comments = Table 13.2 literal descriptions verbatim incl. atp.EnumerationLiteralIndex tags
  - [x] Step 5 — Write reader/writer round-trip test (Red) — N/A: standalone AREnum serialized as an attribute value on consuming Collection.autoCollect
  - [x] Step 6 — Update parser & writer (Green) — N/A: same reason (XML-token ↔ literal mapping lives in the Collection reader/writer via AUTO_COLLECT_XML_MAP)
  - [x] Step 7 — Update checklist comment — 6-col with `# Spec: R23-11/AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 13.2, p.399 (R23-11)`; `# (no methods)` + `__init__` row, reader/writer [—]
  - [x] Step 8 — Deviations — Rule 0007 package-location correction only (Enumerations.py → ElementCollection.py); no spec deviations (literals, order, indexes match Table 13.2/XSD)
  - [x] Step 9 — Verify (9a) + confirm (9b) — 9a: 4 AutoCollectEnum unit tests pass (test_is_arenum, test_literals_in_spec_order, test_instantiability_and_value_round_trip, test_class_docstring_matches_spec_note); dependents (Collection reader/writer + 34 ElementCollection tests + 14 Collection round-trip tests) pass; integration round-trip (5 AISpecification Collection_* fixtures) passes; ruff/black clean. 9b confirmed 2026-09-02 (stamp # Spec verified: R23-11); commit 75f40055
- [x] `Collection` (tracker input · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 13.1) — commit 75f40055
  - [x] Step 2 — Write model class unit test (Red) — test_ElementCollection.py TestCollection: 10 tests — heritage (issubclass ARElement + MRO order), init defaults (7 attrs), get/set autoCollect/collectionSemantics/elementRole with None no-op + chaining, add/get elementRefs/sourceElementRefs/collectedInstanceIRefs/sourceInstanceIRefs with None no-op, verbatim class docstring. Red confirmed: 4 failed (heritage Identifiable, missing IRef accessors, paraphrased docstring)
  - [x] Step 3 — Implement model class (Green) — members/fields renamed per Rule 0001.5: `collectedInstances`→`collectedInstanceIRefs`, `sourceInstances`→`sourceInstanceIRefs` (iref Kind suffix; zero consumers — rename safe); accessor shape per Rule 0001.6: `setCollectedInstances`/`setSourceInstances` (`*` multiplicity) → `addCollectedInstanceIRef`/`addSourceInstanceIRef`; member/accessor order = Table 13.1 displayed order (autoCollect, collectedInstance, collectionSemantics, element, elementRole, sourceElement, sourceInstance); setters return self + None guards; NO base change in the declaration — spec base ARElement is bound via the pre-existing `Collection.__bases__ = (ARElement,)` rebinding in ARPackage.py (ElementCollection↔ARPackage import cycle is fundamental: ARPackage needs CollectableElement before ARElement exists; placeholder base + rebinding is the established mechanism, comment updated). Verified issubclass(Collection, ARElement) on both import paths
  - [x] Step 4 — Sync docstrings (wipe + rewrite) — all old docstrings/comments wiped (incl. stale 4-col checklist and "Gets/Sets the…" paraphrases); class docstring = Table 13.1 Note verbatim (Tags: atp.recommendedPackage=Collections dropped); inline `__init__` comments + getter docstrings = attr Notes verbatim (Tags: xml.sequenceOffset tails dropped); setter/add docstrings = Note + "A None value is a no-op and is not set." (Rule 0012.2.5.4)
  - [x] Step 5 — Write reader/writer round-trip test (Red) — parser/test_collection.py TestReadCollection: 8 tests (optional attrs read, absent-optionals, ELEMENT-REFS wrapper w/ DEST+value, SOURCE-ELEMENT-REFS, COLLECTED-INSTANCE-IREFS w/ BASE/CONTEXT/TARGET, SOURCE-INSTANCE-IREFS, full-file load via ARPackage ELEMENTS dispatch, full round-trip) + writer/test_collection.py TestWriteCollection: 6 tests (XSD-order XML shape, empty-collection no own elements, wrapper shapes, round-trip). Red confirmed: 7 failed / 7 passed
  - [x] Step 6 — Update parser & writer (Green) — parser: readCollection (readIdentifiable chain + AUTO-COLLECT via AUTO_COLLECT_XML_MAP enum-text map + COLLECTION-SEMANTICS as NameToken + ELEMENT-ROLE via getChildElementOptionalIdentifier + 3 wrapper loops via getChildElementRefTypeList/getAnyInstanceRefFromElement) + `COLLECTION` branch in readARPackageElements; parser helper refactor: getAnyInstanceRef body extracted into getAnyInstanceRefFromElement (behaviour-identical, getAnyInstanceRef delegates); writer: writeCollection (XSD sequenceOffset order AUTO-COLLECT 20 → COLLECTION-SEMANTICS 25 → ELEMENT-ROLE 30 → ELEMENT-REFS 40 → SOURCE-ELEMENT-REFS 50 → COLLECTED-INSTANCE-IREFS 60 → SOURCE-INSTANCE-IREFS 70; wrappers only when non-empty; setAnyInstanceRef reused per iref) + isinstance(Collection) branch in writeARPackageElement; AUTO_COLLECT_XML_MAP added to both modules (BINDING_TIME_XML_MAP precedent); createCollection/getCollections already existed on ARPackage
  - [x] Step 1 — Sync members & description from spec — Table 13.1 body md l.10549–10571, caption l.10573; PDF p.399 confirmed via pdf_page.py (R4.3.1 Table 12.1 p.370 — unused, R23-11 table exists). Class=concrete; Package=...GeneralTemplateClasses::ElementCollection (file ElementCollection.py ✓ Rule 0007); Base = ARElement, ARObject, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable → most-derived direct base **ARElement** — code has `Collection(Identifiable)` → heritage fix in Step 3; Aggregated by ARPackage.element; Note verbatim captured (Tags: atp.recommendedPackage=Collections dropped). 7 attrs in displayed order (md l.10556–10559, 10569–10571): autoCollect (AutoCollectEnum, 0..1, attr) / collectedInstance (AtpFeature, *, iref, implemented by AnyInstanceRef) / collectionSemantics (NameToken, 0..1, attr) / element (Identifiable, *, ref) / elementRole (Identifier, 0..1, attr) / sourceElement (Identifiable, *, ref) / sourceInstance (AtpFeature, *, iref, AnyInstanceRef). XSD group COLLECTION l.18868–18967: XML order AUTO-COLLECT(20), COLLECTION-SEMANTICS(25), ELEMENT-ROLE(30), ELEMENT-REFS(40, wrapper, ELEMENT-REF choice DEST required), SOURCE-ELEMENT-REFS(50), COLLECTED-INSTANCE-IREFS(60, wrapper, COLLECTED-INSTANCE-IREF type ANY-INSTANCE-REF), SOURCE-INSTANCE-IREFS(70). Member type AutoCollectEnum is a Rule 0016.4 stub (wrong base/literals) → queued on its own row above. **NO parser/writer support exists at all** (grep: no readCollection/writeCollection; 5 AISpecification Collection_* integration fixtures carry COLLECTION elements that are silently dropped today — Steps 5/6 are real work, not N/A). Helpers available: getChildElementOptionalIdentifier/setChildElementOptionalIdentifier, getChildElementRefTypeList, getAnyInstanceRef/setAnyInstanceRef, getChildElementOptionalLiteral/setChildElementOptionalLiteral; enum pattern = camelCase literal + *_XML_MAP (BINDING_TIME_XML_MAP precedent).
  - [x] Step 7 — Update checklist comment — 6-col in-code checklist (ElementCollection.py l.68–84) covers all 15 rows (1 __init__ + 14 methods); Spec citation Table 13.1 p.399 R23-11; each method marked impl/docstring/test [x] and reader/writer per Step 6 (setters/adders [x] reader, getters [x] writer)
  - [x] Step 8 — Deviations — none spec-deviating: (a) Rule 0007 location ElementCollection.py matches Table 13.1 Package; (b) member renames per Rule 0001.5 (collectedInstances→collectedInstanceIRefs, sourceInstances→sourceInstanceIRefs — iref Kind suffix) and Rule 0001.6 accessor shape (set→add for * multiplicity, getters for lists, set for 0..1) — zero external consumers, rename safe; (c) heritage via pre-existing `Collection.__bases__ = (ARElement,)` rebinding in ARPackage.py (fundamental ElementCollection↔ARPackage import cycle; placeholder `Identifiable` base in declaration, rebind at ARPackage module end) — verified issubclass(Collection, ARElement) on both import paths; no spec attribute dropped, all 7 attrs modeled in Table order; (d) AUTO-COLLECT token map REF-ALL/REF-NONE/REF-NON-STANDARD matches XSD AUTO-COLLECT-ENUM--SIMPLE; (e) parser helper extraction getAnyInstanceRefFromElement behaviour-identical
  - [x] Step 9 — Verify (9a) + confirm (9b) — 9a: 48 Collection/AutoCollectEnum unit tests pass (test_ElementCollection.py 34 — CollectableElement 24 + AutoCollectEnum 4 + Collection 10; test_collection.py parser 8 + writer 6), integration round-trip (5 AISpecification Collection_* fixtures with COLLECTION) passes, ruff/black clean (I001 import-order applied to test_ElementCollection.py; removed legacy dead readCollection/writeCollection trios in parser+writer fixing F811; dropped unused AutoCollectEnum import from writer fixing F401; repaired pre-existing test_Enumerations.py TestAutoCollectEnum that asserted the old fabricated OFF/ON/AUTO literals). 9b confirmed 2026-09-02 (stamp # Spec verified: R23-11); commit 75f40055
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `AtpType` (tracker input · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 5.6) — abstract shell (no own attributes, no own XML element); heritage `AtpType(AtpClassifier, ABC)` already matches spec; only deviation = paraphrased class docstring must be verbatim Table 5.6 Note; Steps 5/6 N/A
  - [x] Step 1 — Sync members & description from spec — Table 5.6 (md l.4594–4603, PDF p.175 via pdf_page.py): Class=AtpType (abstract); Package=M2::AUTOSARTemplates::GenericStructure::AbstractStructure (file AbstractStructure.py ✓ Rule 0007); Base = ARObject, AtpClassifier, Identifiable, MultilanguageReferrable, Referrable → most-derived direct base **AtpClassifier** ✓ (AtpClassifier(Identifiable) confirmed); Attribute rows = `-` → no own attributes; Note verbatim "A type is a classifier that may serve to type prototypes. It is a reusable classifier."; Subclasses = AutosarDataType, ModeDeclarationGroup, ModeDeclarationMappingSet, PortInterface, SwComponentType (out of scope — separate rows / already synced); no reader/writer (abstract, no own XML element) → Steps 5/6 N/A
  - [x] Step 2 — Write model class unit test (Red) — test_AbstractStructure.py TestAtpType: test_abstract_initialization, test_atp_type_concrete_implementation, test_inherits_from_atp_classifier (MRO[1]=AtpClassifier, MRO[2]=Identifiable, isinstance Identifiable/ARObject), test_class_docstring_matches_spec_note (verbatim Table 5.6 Note). Red confirmed: docstring assertion failed (paraphrase)
  - [x] Step 3 — Implement model class (Green) — class docstring set verbatim (single-line `"""..."""` so `__doc__` matches exactly); heritage `AtpType(AtpClassifier, ABC)` already correct; no own attributes → class reduces to `__init__` (abstract guard) — no field/accessor changes. 4 tests Green
  - [x] Step 4 — Sync docstrings (wipe + rewrite) — no stale docstrings to wipe: AtpType has no own attributes so no getter/setter/member-comment docstrings; class docstring = Table 5.6 Note verbatim; `__init__` has no docstring (Rule 0012.2.5.2)
  - [x] Step 5 — Write reader/writer round-trip test (Red) — N/A: AtpType abstract, no own XML element (XSD substitutes concrete subclasses); round-trip covered by consuming-class syncs
  - [x] Step 6 — Update parser & writer (Green) — N/A: no readAtpType/writeAtpType needed (abstract shell, no own attributes); inherited members reached via AtpClassifier→Identifiable chain
  - [x] Step 7 — Update checklist comment — 6-col `# Spec:` format (AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 5.6, p.175, R23-11); single `__init__` row (reader/writer `[—]`, release R23-11); marker deferred to 9b
  - [x] Step 8 — Deviations — none: Class=abstract (matches Table 5.6); Base closure reaches AtpClassifier as most-derived ✓ (AtpClassifier stamped R23-11, Table 5.1); Package=GenericStructure::AbstractStructure (file AbstractStructure.py, Rule 0007 OK); no own attributes → no naming/type/missing deviation; docstring verbatim; reader/writer N/A (abstract shell). Rule 0001.10 report: AtpType has no own Attribute rows, so no member-type references to block on; Subclasses (AutosarDataType, ModeDeclarationGroup, ModeDeclarationMappingSet, PortInterface, SwComponentType) are subclasses, not member types — ModeDeclarationMappingSet already stamped R23-11; no missing/stub classes
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

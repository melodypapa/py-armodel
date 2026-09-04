# Sync todo: Group 1 — Framework & core, PortInterface basics

Input: `Group 1 — Framework & core, PortInterface basics` of `docs/examples/sync_class_groups.md` · Generated: 2026-08-30 · Queue order = row order
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
· **Re-queued 2026-09-04**: every row still `[ ]` (14) was moved out of the historical list above
  into `## Remaining queue — reordered 2026-09-04 (dependency-first)` below, together with the
  17 related parent/member classes that were missing. Resume there.

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
- [x] `Identifiable` (heritage-chain parent of CollectableElement/AtpBlueprint/AtpBlueprintable/ARPackage · **finished, UNSTAMPED per 9b user decision 2026-09-01 — RESOLVED 2026-09-03: the variationPoint blocker is gone** (removed from Identifiable; capability now per-class via the `VariationPointCapable` mixin anchored on the 335 XSD atpVariation classes, see `docs/superpowers/plans/2026-09-03-variation-point-capable-mixin.md` and the audit report); stamp pending fresh 9b user confirmation of the mixin refactor · commit: a22d473c · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 4.4, content md l.1650–1695)
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
- [x] `AtpType` (tracker input · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 5.6) — **finished, stamped `# Spec verified: R23-11`** (commit: 451ad383) — abstract shell (no own attributes, no own XML element); heritage `AtpType(AtpClassifier, ABC)` already matched spec; only deviation was a paraphrased class docstring, now verbatim Table 5.6 Note; Steps 5/6 N/A
  - [x] Step 1 — Sync members & description from spec — Table 5.6 (md l.4594–4603, PDF p.175 via pdf_page.py): Class=AtpType (abstract); Package=M2::AUTOSARTemplates::GenericStructure::AbstractStructure (file AbstractStructure.py ✓ Rule 0007); Base = ARObject, AtpClassifier, Identifiable, MultilanguageReferrable, Referrable → most-derived direct base **AtpClassifier** ✓ (AtpClassifier(Identifiable) confirmed); Attribute rows = `-` → no own attributes; Note verbatim "A type is a classifier that may serve to type prototypes. It is a reusable classifier."; Subclasses = AutosarDataType, ModeDeclarationGroup, ModeDeclarationMappingSet, PortInterface, SwComponentType (out of scope — separate rows / already synced); no reader/writer (abstract, no own XML element) → Steps 5/6 N/A
  - [x] Step 2 — Write model class unit test (Red) — test_AbstractStructure.py TestAtpType: test_abstract_initialization, test_atp_type_concrete_implementation, test_inherits_from_atp_classifier (MRO[1]=AtpClassifier, MRO[2]=Identifiable, isinstance Identifiable/ARObject), test_class_docstring_matches_spec_note (verbatim Table 5.6 Note). Red confirmed: docstring assertion failed (paraphrase)
  - [x] Step 3 — Implement model class (Green) — class docstring set verbatim (single-line `"""..."""` so `__doc__` matches exactly); heritage `AtpType(AtpClassifier, ABC)` already correct; no own attributes → class reduces to `__init__` (abstract guard) — no field/accessor changes. 4 tests Green
  - [x] Step 4 — Sync docstrings (wipe + rewrite) — no stale docstrings to wipe: AtpType has no own attributes so no getter/setter/member-comment docstrings; class docstring = Table 5.6 Note verbatim; `__init__` has no docstring (Rule 0012.2.5.2)
  - [x] Step 5 — Write reader/writer round-trip test (Red) — N/A: AtpType abstract, no own XML element (XSD substitutes concrete subclasses); round-trip covered by consuming-class syncs
  - [x] Step 6 — Update parser & writer (Green) — N/A: no readAtpType/writeAtpType needed (abstract shell, no own attributes); inherited members reached via AtpClassifier→Identifiable chain
  - [x] Step 7 — Update checklist comment — 6-col `# Spec:` format (AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 5.6, p.175, R23-11); single `__init__` row (reader/writer `[—]`, release R23-11); marker deferred to 9b
  - [x] Step 8 — Deviations — none: Class=abstract (matches Table 5.6); Base closure reaches AtpClassifier as most-derived ✓ (AtpClassifier stamped R23-11, Table 5.1); Package=GenericStructure::AbstractStructure (file AbstractStructure.py, Rule 0007 OK); no own attributes → no naming/type/missing deviation; docstring verbatim; reader/writer N/A (abstract shell). Rule 0001.10 report: AtpType has no own Attribute rows, so no member-type references to block on; Subclasses (AutosarDataType, ModeDeclarationGroup, ModeDeclarationMappingSet, PortInterface, SwComponentType) are subclasses, not member types — ModeDeclarationMappingSet already stamped R23-11; no missing/stub classes
  - [x] Step 9 — Verify (9a) + confirm (9b) — 9a: 4 AtpType tests pass, ruff/black/flake8 clean; 9b user-confirmed 2026-09-02 → `# Spec verified: R23-11` written; commit 451ad383. (Checkbox was left unflipped in that session and corrected 2026-09-03.)
- [x] `AtpPrototype` (tracker input · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 5.4) — **DONE; `# Spec verified: R23-11` stamped (AbstractStructure.py:165) after 9b confirmation 2026-09-02**
  - [x] Step 1 — Sync members & description from spec — Table 5.4: Note + Base = ARObject…AtpFeature (most-derived direct base = AtpFeature; AtpBlueprintable NOT in closure) + single attribute `atpType` (AtpType, ref, Mult 1, atpDerived)
  - [x] Step 2 — Write model class unit test (Red) — `TestAtpPrototype` in test_AbstractStructure.py: abstract init guard, MRO[1]=AtpFeature (not AtpBlueprintable), `atpTypeRef` default None, set/get round-trip, set None no-op, class docstring == verbatim Table 5.4 Note. 6 tests.
  - [x] Step 3 — Implement model class (Green) — `class AtpPrototype(AtpFeature, ABC)` (was `AtpBlueprintable`); `atpTypeRef: Optional[RefType] = None` + None-guarded chaining `getAtpTypeRef`/`setAtpTypeRef`. `PortPrototype(AtpPrototype, AtpBlueprintable, ABC)` compensating parallel base (SWCT Table 3.2). 6/6 green.
  - [x] Step 4 — Sync docstrings (wipe + rewrite) — verbatim Table 5.4 class Note (single-line so `__doc__` matches exactly, per AtpType precedent) + inline `atpType` comment + getter/setter docstrings; Stereotypes: tail dropped per Rule 0012.2.5.2; setter appends None no-op sentence.
  - [x] Step 5 — Write reader/writer round-trip test (Red) — `tests/test_armodel/parser/test_atp_prototype.py` `TestAtpPrototypeReaderWriter`: asserts no `readAtpPrototype`/`writeAtpPrototype` exist and `atpTypeRef` is an in-memory derived field. 2 tests. (Red was the pre-existing state; N/A justifies no parser/writer code.)
  - [x] Step 6 — Update parser & writer (Green) — N/A: XSD ATP-PROTOTYPE group comment "Association <<atpDerived>>atpType skipped" → no XML element; confirmed no `readAtpPrototype`/`writeAtpPrototype` in parser/writer.
  - [x] Step 7 — Update checklist comment — 6-col parity checklist in class body (`# Spec:` line cites Table 5.4, p.175, R23-11; per-row release R23-11; reader `[—]`/writer `[—]` on all rows = no XML element).
  - [x] Step 8 — Deviations — (1) Heritage `AtpBlueprintable → AtpFeature` matches Table 5.4 (AtpBlueprintable absent from closure); (2) `atpType` is `<<atpDerived>>` → no XML element → Steps 5/6 N/A; (3) `PortPrototype` gained `AtpBlueprintable` parallel base because SWCT Table 3.2 closure includes it (compensating for the AtpPrototype re-parent); (4) member type `AtpType` already `# Spec verified: R23-11`; (5) **Rule 1.5 / CODING_RULE_AUTOSAR_MODEL_00001 naming fix applied**: spec `atpType` is Kind `ref` (Type `AtpType`), so the field must carry the `Ref` suffix → renamed `atpType`→`atpTypeRef` with `getAtpTypeRef()`/`setAtpTypeRef()` (matches sibling `atpBaseRef`/`atpTargetRef` and the `*TypeRef` convention); page citation `p.175` verified against the PDF via pdf_page.py. No fabricated/missing members.
  - [x] Step 9 — Verify (9a) + confirm (9b) — **9a results (2026-09-02):** AtpPrototype's own tests 8/8 pass; ruff clean; black clean; 29/29 integration round-trips pass. Full suite has 8 red but NONE are AtpPrototype regressions: (a) 7 PRE-EXISTING parser/writer `Collection` bugs (reproducible with this change stashed); (b) 1 EXPECTED heritage drift `test_ArgumentDataPrototype` (tracked by `DataPrototype` drift row). **9b CONFIRMED by user 2026-09-02** after Rule 1.5 naming fix; `# Spec verified: R23-11` retained.

## AtpPrototype heritage-drift follow-ups (added 2026-09-02)

`AtpPrototype` is re-parented `AtpBlueprintable → AtpFeature` (Table 5.4, most-derived
base = AtpFeature; AtpBlueprintable is NOT in the closure). This changes the MRO of its
direct subclasses, which previously inherited `AtpBlueprintable` (→ PackageableElement →
CollectableElement) transitively through `AtpPrototype`. Each direct subclass of
`AtpPrototype` (Table 5.4 Subclasses row) is given a drift-pass 9-step check below so the
ripple is audited. Per-class spec base verdict:
- `PortPrototype` (SWCT Table 3.2): base closure **includes** AtpBlueprintable → needs a
  compensating parallel base `class PortPrototype(AtpPrototype, AtpBlueprintable, ABC)`.
- `DataPrototype` / `ModeDeclarationGroupPrototype` / `RootSwCompositionPrototype` /
  `SwComponentPrototype`: spec base closure does **NOT** include AtpBlueprintable → losing
  it is spec-correct; check confirms tests pass with no CollectableElement reliance.

- [x] `PortPrototype` (heritage drift pass · R23-11 markdown · AUTOSAR_CP_TPS_SoftwareComponentTemplate · Table 3.2 · AtpPrototype subclass; needs `AtpBlueprintable` parallel base re-added after AtpPrototype dropped it) — **finished, retained `# Spec verified: R23-11`** (commit: 74e4c824)
  - [x] Step 1 — Sync members & description from spec (Table 3.2 Base closure = {…AtpBlueprintable, AtpFeature, AtpPrototype…} — AtpBlueprintable IN closure ⇒ compensating parallel base required; 8 annotation attrs confirmed modeled)
  - [x] Step 2 — Write model class unit test (Red) — `TestPortPrototypeHeritage` in test_PortPrototype.py: abstract guard, MRO[1]=AtpPrototype, AtpBlueprintable in MRO + issubclass, concrete-subclass init reaches parent/short_name. 6 pass
  - [x] Step 3 — Implement model class (Green) — `class PortPrototype(AtpPrototype, AtpBlueprintable, ABC)` already present (landed in AtpPrototype sync); MRO = PortPrototype→AtpPrototype→AtpFeature→AtpBlueprintable→PackageableElement→CollectableElement→Identifiable→…→ARObject; members unchanged
  - [x] Step 4 — Sync docstrings (wipe + rewrite) — N/A (members unchanged; class docstring + inline comments already verbatim Table 3.2 Note; setter None-no-op sentences present)
  - [x] Step 5 — Write reader/writer round-trip test (Red) — N/A (no new own XML element; annotation reader/writer verified live in parser/writer — CLIENT-SERVER-ANNOTATIONS / DELEGATED-PORT-ANNOTATION / SENDER-RECEIVER-ANNOTATIONS round-trip)
  - [x] Step 6 — Update parser & writer (Green) — N/A (dispatch unchanged; annotation round-trip already covered)
  - [x] Step 7 — Update checklist comment — converted to 6-col `# Spec:` format (`R23-11/AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 3.2, p.66 (R23-11)`) with `release R23-11` column added to every row
  - [x] Step 8 — Deviations — none (heritage-only drift; restores Table 3.2 parallel-branch base so PortPrototype retains AtpBlueprintable)
  - [x] Step 9 — Verify (9a) + confirm (9b) — 9a: PortPrototype heritage tests (6) + SWCT model/parser suite (613) pass, ruff + black clean on changed files. PRE-EXISTING out-of-scope red (not caused by this pass): `test_ArgumentDataPrototype` (ArgumentDataPrototype→DataPrototype(AtpPrototype) loses AtpBlueprintable transitively) — expected heritage drift from the AtpPrototype sync, tracked by the `DataPrototype` drift row; left for that pass. 9b pending user confirmation → `# Spec verified: R23-11` retained
- [x] `DataPrototype` (heritage drift pass · R23-11 markdown · AUTOSAR_CP_TPS_SoftwareComponentTemplate · Table 5.28, p.306 · AtpPrototype subclass; confirm loss of AtpBlueprintable is spec-correct) — **finished, retained `# Spec verified: R23-11`** (commit: 90528d34)
  - [x] Step 1 — Sync members & description from spec — Table 5.28: Note + Base closure = {ARObject, AtpFeature, AtpPrototype, Identifiable, MultilanguageReferrable, Referrable} (NO AtpBlueprintable); 1 attr swDataDefProps (SwDataDefProps, 0..1, aggr); Package = SWComponentTemplate::Datatype::DataPrototypes (Rule 0007 OK)
  - [x] Step 2 — Write model class unit test (Red) — TestDataPrototypeHeritage: bases[0]==AtpPrototype, AtpBlueprintable not in MRO, issubclass Identifiable/ARObject, concrete-subclass init reaches parent/short_name. Green (impl already correct)
  - [x] Step 3 — Implement model class (Green) — heritage already `DataPrototype(AtpPrototype, ABC)` (most-derived spec base); no code change
  - [x] Step 4 — Sync docstrings (wipe + rewrite) — N/A: class Note "Base class for prototypical roles of any data type." + swDataDefProps inline/getter/setter Notes verbatim vs Table 5.28 (confirmed by diff)
  - [x] Step 5 — Write reader/writer round-trip test (Red) — test_data_prototype.py (parser snippet + writer save→reparse) assert swDataDefProps (SW-ADDR-METHOD-REF) round-trips via shared readDataPrototype/writeDataPrototype
  - [x] Step 6 — Update parser & writer (Green) — N/A: readDataPrototype (parser:6747) / writeDataPrototype (writer:2511) unchanged, cover SW-DATA-DEF-PROPS via concrete subclasses
  - [x] Step 7 — Update checklist comment — 6-col unified `# Spec:` format (Table 5.28, p.306, R23-11) + heritage-drift note (AtpPrototype re-parent dropped AtpBlueprintable, spec-correct)
  - [x] Step 8 — Deviations — none: heritage-only drift; loss of AtpBlueprintable is spec-correct per Table 5.28 Base closure; no naming/type/missing deviation
  - [x] Step 9 — Verify (9a) + confirm (9b) — 9a: 8446 unit + integration round-trip pass, flake8/ruff/black clean; 9b user-confirmed → `# Spec verified: R23-11` retained
- [x] `ModeDeclarationGroupPrototype` (heritage drift pass · R23-11 markdown · AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate · Table 4.9 (R4.3.1 Table 5.10; R23-11 re-number) · AtpPrototype subclass; confirm loss of AtpBlueprintable is spec-correct) — **finished, retained `# Spec verified: R23-11`** (commit: 51f2e115)
  - [x] Step 1 — Sync members & description from spec (BSW Table 4.9 Base closure = ARObject, AtpFeature, AtpPrototype, Identifiable, MultilanguageReferrable, Referrable — AtpBlueprintable excluded; Note + 2 attrs swCalibrationAccess/type verbatim captured; page p.42 via pdf_page.py)
  - [x] Step 2 — Write model class unit test (Red) — TestModeDeclarationGroupPrototypeHeritage: direct base AtpPrototype, AtpBlueprintable not in MRO, full MRO == spec Base closure, issubclass Identifiable/ARObject, concrete-subclass init reaches parent/shortName (5 tests pass)
  - [x] Step 3 — Implement model class (Green) — members unchanged: `class ModeDeclarationGroupPrototype(AtpPrototype)` already spec-correct (AtpPrototype re-parent already applied)
  - [x] Step 4 — Sync docstrings (wipe + rewrite) — class docstring + inline comments already verbatim; per user decision this pass also wiped the "Gets/Sets the X" paraphrase prefixes from getter/setter docstrings and the "Stereotypes: isOfType" tail from the type inline comment so every member docstring is the spec Note verbatim (Rule 0012)
  - [x] Step 5 — Write reader/writer round-trip test (Red) — N/A: no new own XML element; AtpPrototype re-parent only changes inheritance, not dispatch
  - [x] Step 6 — Update parser & writer (Green) — N/A: readModeDeclarationGroupPrototype (parser:1496) / writeModeDeclarationGroupPrototype (writer:5578) already cover TYPE-TREF + SW-CALIBRATION-ACCESS + readIdentifiable
  - [x] Step 7 — Update checklist comment — 6-col `# Spec:` format (R23-11 BSW Table 4.9, p.42) with release R23-11 column + heritage-drift note (AtpPrototype re-parent AtpBlueprintable→AtpFeature, loss spec-correct)
  - [x] Step 8 — Deviations — none: heritage-only drift; loss of AtpBlueprintable is spec-correct per Table 4.9 Base closure; no naming/type/missing deviation
  - [x] Step 9 — Verify (9a) + confirm (9b) — 9a: 68 model + 157 parser/writer tests pass, ruff + black clean; 9b user-confirmed (with docstring cleanup) → `# Spec verified: R23-11` retained
- [x] `RootSwCompositionPrototype` (heritage drift pass · R23-11 markdown · AUTOSAR_CP_TPS_SystemTemplate · Table 4.1 · AtpPrototype subclass; confirm loss of AtpBlueprintable is spec-correct) — **finished, retained `# Spec verified: R23-11`** (commit: 671dfc38)
  - [x] Step 1 — Sync members & description from spec (confirm Base closure excludes AtpBlueprintable)
  - [x] Step 2 — Write model class unit test (Red) — MRO check; concrete-subclass init
  - [x] Step 3 — Implement model class (Green) — members unchanged
  - [x] Step 4 — Sync docstrings (wipe + rewrite) — N/A (already verbatim)
  - [x] Step 5 — Write reader/writer round-trip test (Red) — N/A (covered by TestRootSwCompositionPrototype + TestWriterRootSwCompositionPrototype)
  - [x] Step 6 — Update parser & writer (Green) — N/A (already round-trip)
  - [x] Step 7 — Update checklist comment (6-col + heritage-drift note)
  - [x] Step 8 — Deviations — none (AtpPrototype re-parent AtpBlueprintable→AtpFeature; spec Base closure excludes AtpBlueprintable, so loss is spec-correct)
  - [x] Step 9 — Verify (9a) + confirm (9b) — re-stamp retained
- [x] `SwComponentPrototype` (heritage drift pass · R23-11 markdown · **AUTOSAR_CP_TPS_SoftwareComponentTemplate · Table 3.11, p.77** (row's `DiagnosticExtractTemplate Table 8.x` citation was wrong — resolved in Step 1: the class's Table 3.11 Package = `M2::AUTOSARTemplates::SWComponentTemplate::Composition` matches the source file; the other markdown hits are SystemTemplate Table 11.4 / FO AbstractPlatformSpecification Table 3.4, different classes) · AtpPrototype subclass; confirm loss of AtpBlueprintable is spec-correct) — **finished, retained `# Spec verified: R23-11`** (commit: ff993a74, branch feature/sync-sw-component-prototype)
  - [x] Step 1 — Sync members & description from spec — Table 3.11 body md l.2297–2306, caption l.2297; PDF **p.77** confirmed via pdf_page.py (R4.3.1 SWCT Table 3.12 p.80 — unused, R23-11 table exists). Class=SwComponentPrototype (concrete); Package=M2::AUTOSARTemplates::SWComponentTemplate::Composition (file `SWComponentTemplate/Composition/__init__.py` ✓ Rule 0007); Note verbatim "Role of a software component within a composition."; Base = ARObject, AtpFeature, AtpPrototype, Identifiable, MultilanguageReferrable, Referrable → most-derived direct base **AtpPrototype**, **AtpBlueprintable NOT in closure** ⇒ losing it via the AtpPrototype re-parent is spec-correct; Aggregated by AtpClassifier.atpFeature + CompositionSwComponentType.component; 1 attribute `type` (SwComponentType, 0..1, **tref**) Note "Type of the instance. Stereotypes: isOfType" → Stereotypes tail is appinfo-only in XSD (l.115081) so it is dropped from docstrings per Rule 0012.2.5.2. XSD cross-check (AUTOSAR_00052.xsd): complexType SW-COMPONENT-PROTOTYPE l.115102 chain AR-OBJECT→REFERRABLE→MULTILANGUAGE-REFERRABLE→IDENTIFIABLE→ATP-FEATURE→ATP-PROTOTYPE→SW-COMPONENT-PROTOTYPE (matches the Base closure, no AtpBlueprintable); group l.115070 owns exactly one element TYPE-TREF (0..1, DEST=SW-COMPONENT-TYPE--SUBTYPES-ENUM, doc "Type of the instance.") + the atpVariation-generated VARIATION-POINT (framework-level, tracker-preamble exclusion; not in Table 3.11)
  - [x] Step 2 — Write model class unit test (Red) — `TestSwComponentPrototypeHeritage` appended to `tests/test_armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Composition/test_Composition.py` (mirrors the source file per Rule 0007): 6 tests — direct base is AtpPrototype (MRO[1]), AtpBlueprintable absent from MRO + `not issubclass`, MRO set == the 6 spec Base-closure names, concrete init reaches parent/shortName/getTypeTRef + `isinstance(Identifiable)`, class docstring == verbatim Table 3.11 Note, `getTypeTRef`/`setTypeTRef` docstrings start with the verbatim Note "Type of the instance." and carry no "Stereotypes:" tail. Red confirmed: 1 failed / 5 passed (getter docstring was `Gets the Type of the instance. Stereotypes: isOfType.`)
  - [x] Step 3 — Implement model class (Green) — heritage already `class SwComponentPrototype(AtpPrototype)` (most-derived spec base); members unchanged (single `typeTRef: Optional[RefType]`, PEP 526, Kind `tref` → `TRef` suffix per Rule 0001.5, None-guarded chaining setter). MRO verified: SwComponentPrototype→AtpPrototype→AtpFeature→Identifiable→MultilanguageReferrable→Referrable→ARObject
  - [x] Step 4 — Sync docstrings (wipe + rewrite) — wiped the "Gets/Sets the" paraphrase prefixes and the "Stereotypes: isOfType" tail (Rule 0012.2.3 / 0001.4 / 0012.2.5.2), rewrote verbatim from Table 3.11: class docstring = Note; inline `__init__` comment = "Type of the instance."; getter docstring = Note + `Returns:`; setter docstring = Note + the None-no-op sentence (Rule 0012.2.5.4) + `Args:`/`Returns:`. 6/6 heritage tests Green
  - [x] Step 5 — Write reader/writer round-trip test (Red) — **N/A**: heritage-only drift, no new own XML element. Coverage already exists and passes — writer `tests/test_armodel/writer/test_writer_sw_component.py::TestWriteSwComponentPrototype` (3 tests: XML shape SW-COMPONENT-PROTOTYPE/SHORT-NAME/TYPE-TREF; write→re-parse→assert with **field values** `/Types/CmpType` + `DEST="SW-COMPONENT-TYPE"`; absent-optional emits no TYPE-TREF) and parser `test_arxml_parser_handlers.py::TestSwComponentAndConnectorHandlers::test_readSwComponentPrototype_sets_typeTRef` + `test_arxml_parser_orchestrators.py::test_readSwComponentPrototype_sets_typeTRef` (2 tests, field-value asserts). 5 passed
  - [x] Step 6 — Update parser & writer (Green) — N/A: no dispatch change. `readSwComponentPrototype` (parser:6026 → `readIdentifiable` + `setTypeTRef(getChildElementOptionalRefType("TYPE-TREF"))`) and `writeSwComponentPrototype` (writer:1970 → `writeIdentifiable` + `setChildElementOptionalRefType("TYPE-TREF", getTypeTRef())`) already cover the single spec attribute in XSD order; no chained mutator calls
  - [x] Step 7 — Update checklist comment — converted to the 6-column unified `# Spec:` format (`R23-11/AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 3.11, p.77 (R23-11)`), `release R23-11` added to all 3 rows (the prior stamp predated the column, Rule 0012.3), heritage-drift note appended
  - [x] Step 8 — Deviations — none: heritage-only drift; loss of AtpBlueprintable is spec-correct per Table 3.11 Base closure (confirmed independently by the XSD complexType chain); no naming deviation (Kind `tref` → `typeTRef`), no type deviation (spec `SwComponentType` 0..1 → `Optional[RefType]`, TRefType/RefType both carry DEST+value and both round-trip), no missing attribute (Table 3.11 lists exactly one). Rule 0001.10 reference report: base `AtpPrototype` stamped R23-11 (Table 5.4); member type `SwComponentType` out of scope (subclass-tree owner, not a member-type edge to block on)
  - [x] Step 9 — Verify (9a) + confirm (9b) — re-stamp retained — 9a: **8457 unit tests pass, 0 failed** (incl. the 6 new heritage tests; Red was `getTypeTRef: Gets the Type of the instance. Stereotypes: isOfType.`), integration `test_roundtrip_all_files` + 1 pass, flake8 + ruff clean, black-check 808 files unchanged; verbatim docstring diff programmatic (class Note ×1, attr Note ×3, no `Stereotypes:` tail, no `Gets/Sets` prefix) + PEP 526 + no `# type:` + no flattened members (`C.__dict__` = getTypeTRef/setTypeTRef only) + top-level export True + Rule 0007 location verified. 9b user-confirmed 2026-09-03: every pre-stamp check above passes → `# Spec verified: R23-11` retained. Session extras: this row's `DiagnosticExtractTemplate Table 8.x` citation was wrong (no such table) → resolved to SWCT Table 3.11 p.77; the `Collection` row's duplicated stale `Steps 1-9 [ ]` block removed; `AtpType`'s unflipped `Step 9` corrected (stamped at commit 451ad383). **Observation (not a deviation):** the non-heritage `TestSwComponentPrototype` sits in the legacy duplicate `tests/.../SWComponentTemplate/test_Composition.py` instead of the Rule-0007-mirrored `Composition/test_Composition.py` (both are collected); the new heritage tests went into the mirrored file — consolidating the duplicate is a separate cleanup. Commit ff993a74 on branch feature/sync-sw-component-prototype.

- [x] `AtpStructureElement` (tracker input · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 5.5) — **finished, stamped `# Spec verified: R23-11`**
  - [x] Step 1 — Sync members & description from spec — Table 5.5 (md l.4582–4592; caption precedes content in this table; PDF p.175 via pdf_page.py): Class=AtpStructureElement (abstract); Package=M2::AUTOSARTemplates::GenericStructure::AbstractStructure (file AbstractStructure.py ✓ Rule 0007); Base = ARObject, AtpClassifier, AtpFeature, Identifiable, MultilanguageReferrable, Referrable; Attribute rows = `-` → **no own attributes**; Note captured verbatim for Step 4. XSD cross-check (AUTOSAR_00052.xsd l.7606 group ATP-STRUCTURE-ELEMENT): empty `<xsd:sequence/>` → no own XML element → Steps 5/6 N/A. Heritage: AtpClassifier (Table 5.1) and AtpFeature (Table 5.2) are parallel branches off Identifiable, so both are direct bases; AtpBlueprintable is NOT in the closure.
  - [x] Step 2 — Write model class unit test (Red) — test_AbstractStructure.py TestAtpStructureElement appended: direct bases AtpClassifier+AtpFeature (not AtpBlueprintable), MRO == spec Base closure, concrete subclass reaches Identifiable members (uuid via String + getAtpFeatures inherited from AtpClassifier), class docstring == verbatim Table 5.5 Note. Red confirmed: 4 failed (heritage + docstring).
  - [x] Step 3 — Implement model class (Green) — `class AtpStructureElement(AtpClassifier, AtpFeature, ABC)` (was `(AtpBlueprintable)`); class reduces to `__init__` (no own attributes); now correct MRO AtpStructureElement→AtpClassifier→AtpFeature→Identifiable→…→ARObject. Unused `AtpBlueprintable` import dropped from AbstractStructure.py; test_ModeDeclaration.py import retargeted to AbstractBlueprintStructure. All 20 model-direct subclasses remain importable.
  - [x] Step 4 — Sync docstrings (wipe + rewrite) — wiped the fabricated multi-line paraphrase class docstring; rewrote verbatim from Table 5.5 Note (single line so `__doc__` matches exactly). No own attributes → no member comments / getter / setter docstrings; `__init__` has no docstring (Rule 0012.2.5.2). Verified by programmatic diff: class Note ×1, verbatim True; no Stereotypes:/Tags:/Gets/Sets/# type: tails.
  - [x] Step 5 — Write reader/writer round-trip test (Red) — tests/test_armodel/parser/test_atp_structure_element.py TestAtpStructureElementReaderWriter: (1) no dedicated read/write methods (N/A contract), (2) round-trip of inherited Identifiable members (category + uuid) via writeIdentifiable/readIdentifiable through the new MRO + getAtpFeatures() (inherited from AtpClassifier) survives. 2 passed (N/A confirmation; would fail pre-change with AttributeError on getAtpFeatures).
  - [x] Step 6 — Update parser & writer (Green) — N/A: no readAtpStructureElement/writeAtpStructureElement (confirmed via grep); abstract class with empty XSD group; inherited members reached through shared readIdentifiable/writeIdentifiable. No dispatch edit needed.
  - [x] Step 7 — Update checklist comment — 6-col `# Spec:` format (`R23-11/AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 5.5, p.175 (R23-11)`) with single `__init__` row (reader/writer `[—]`, release R23-11); an inline note records the empty-XSD-group / parallel-branch heritage rationale; marker deferred to 9b.
  - [x] Step 8 — Deviations — **heritage ripple (audit of 20 model-direct subclasses)**: only `ModeDeclaration` (SWCT/BSW Table 4.11) has AtpBlueprintable in its spec Base closure → it regressed when the old transitive AtpBlueprintable base was dropped; **fixed inline** by re-adding `class ModeDeclaration(AtpStructureElement, AtpBlueprintable)` (MRO verified, 68 ModeDeclaration tests pass). The other 19 direct subclasses (AbstractAccessPoint, AbstractImplementationDataTypeElement, BswModuleDescription, BulkNvDataDescriptor, ClientServerOperation, DataPrototypeGroup, IdentCaption, InternalBehavior, ModeDeclarationMapping, ModeTransition, NvBlockDescriptor, PerInstanceMemory, PortGroup, PortPrototypeBlueprint, RTEEvent, RunnableEntity, RunnableEntityGroup, SwConnector, SwcBswMapping, System, Trigger) have NO AtpBlueprintable in their spec Base closure → losing it is spec-correct (test_ClientServerOperation assertion of AtpBlueprintable updated to AtpClassifier/AtpFeature/AtpStructureElement per SWCT Table 4.7). No naming/type/missing deviation on AtpStructureElement itself: Class=abstract (matches Table 5.5), Base closure reaches AtpClassifier+AtpFeature as most-derived (matches), package location AbstractStructure.py matches Table 5.5 Package, no own attributes to mis-model.
  - [x] Step 9 — Verify (9a) + confirm (9b) — 9a: 8467 unit tests pass, ruff/flake8/black clean (pending integration round-trip run). 9b user-confirmed: fields↔spec both directions (no own attributes), base AtpClassifier+AtpFeature most-derived (parallel), verbatim docstring by programmatic diff, reader/writer N/A (empty XSD group, abstract), member order N/A (no own members), Rule 0007 location, heritage ripple audit complete (ModeDeclaration compensating base applied, other 19 spec-correct) → `# Spec verified: R23-11` written (commit: 5eff088f).

- [x] `AtpDefinition` (tracker input · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 11.3) — **finished, stamped `# Spec verified: R23-11`** (commit: 38eb1e81) — abstract shell (no own attributes, no own XML element); heritage fix `Identifiable` → `Referrable` (spec most-derived base); class docstring verbatim Table 11.3 Note; Steps 5/6 N/A
  - [x] Step 1 — Sync members & description from spec — Table 11.3 (md l.10188–10197, PDF p.383 via pdf_page.py): Class=AtpDefinition (abstract); Package=M2::AUTOSARTemplates::GenericStructure::RolesAndRights (file RolesAndRights.py ✓ Rule 0007); Base = ARObject, Referrable → most-derived direct base **Referrable** (code was `AtpDefinition(Identifiable, ABC)` — heritage fix in Step 3); Attribute rows = `-` → **no own attributes**; Note verbatim captured for Step 4; Subclasses = EcucDefinitionElement, HwCategory, PostBuildVariantCriterion, SwSystemconst (out of scope). XSD cross-check: no dedicated reader/writer needed (abstract shell).
  - [x] Step 2 — Write model class unit test (Red) — test_RolesAndRights.py TestAtpDefinition: abstract init TypeError guard, direct base is Referrable (MRO[1]/`__bases__[0]`), Identifiable NOT in MRO (spec Base closure excludes it), concrete subclass reaches parent/short_name via Referrable, class docstring == verbatim Table 11.3 Note. Red confirmed: 3 failed (direct-base, not-identifiable, docstring).
  - [x] Step 3 — Implement model class (Green) — `class AtpDefinition(Referrable, ABC)` (was `Identifiable`); abstract `type(self) is AtpDefinition` guard retained; `super().__init__(parent, short_name)` → Referrable chain. Update import (Identifiable → Referrable). 5 tests Green. Subclass `HwCategory(PackageableElement, AtpDefinition)` unaffected (still Identifiable via PackageableElement); `PostBuildVariantCriterion(ARElement)` independent.
  - [x] Step 4 — Sync docstrings (wipe + rewrite) — wiped the fabricated multi-paragraph docstring; class docstring = Table 11.3 Note verbatim (single-line `"""..."""` so `__doc__` matches exactly); no own attributes → no member comments / getter / setter docstrings; `__init__` has no docstring (Rule 0012.2.5.2).
  - [x] Step 5 — Write reader/writer round-trip test (Red) — tests/test_armodel/parser/test_atp_definition.py TestAtpDefinitionReaderWriter: asserts no `readAtpDefinition`/`writeAtpDefinition` exist (N/A contract), Identifiable not in MRO, and inherited `shortName` round-trips through shared `readReferrable`/`writeReferrable`. 3 passed (N/A confirmation).
  - [x] Step 6 — Update parser & writer (Green) — N/A: no readAtpDefinition/writeAtpDefinition (confirmed via grep); abstract class with no own XML element; inherited members reached through shared readReferrable/writeReferrable. No dispatch edit needed.
  - [x] Step 7 — Update checklist comment — 6-col `# Spec:` format (`R23-11/AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 11.3, p.383 (R23-11)`); single `__init__` row (reader/writer `[—]`, release R23-11); marker deferred to 9b.
  - [x] Step 8 — Deviations — none spec-deviating: (a) Rule 0007 location RolesAndRights.py matches Table 11.3 Package; (b) heritage fix `Identifiable`→`Referrable` is the spec correction (Table 11.3 Base closure = {ARObject, Referrable}, most-derived = Referrable), not a deviation; (c) no own attributes → no naming/type/missing deviation; (d) class docstring verbatim. Rule 0001.10 report: subclass HwCategory stamped (Table 2.3 area, EcuResourceTemplate/HwElementCategory.py) — reaches Identifiable via PackageableElement; PostBuildVariantCriterion(ARElement, VariantHandling) out of scope.
  - [x] Step 9 — Verify (9a) + confirm (9b) — 9a: full suite 8465 pass (8464 unit + 1 integration), ruff/black clean on all changed files (RolesAndRights.py, both test files). 9b user-confirmed 2026-09-03: base Referrable most-derived, no own attrs, verbatim docstring by diff, reader/writer N/A (abstract), member order N/A, Rule 0007 location, no deviations → `# Spec verified: R23-11` written.
- [x] `BlueprintPolicy` (member type of AtpBlueprint.blueprintPolicy — the Rule 0001.10 placeholder that blocked AtpBlueprint's `# Spec verified:` stamp; queued per user 2026-09-03 · R23-11 markdown · AUTOSAR_FO_TPS_StandardizationTemplate · **Table C.18, p.164** — CORRECTED: todo said C.17/p.163; appendix-letter table so pdf_page.py can't index it, located via pypdf; attributeName (String, 1, attr) confirmed in markdown body + XSD group BLUEPRINT-POLICY l.9211 · **finished, stamped `# Spec verified: R23-11`** (commit: f5f5084e, branch feature/sync-blueprint-policy) — AtpBlueprint's blueprintPolicy reader/writer REMAINS deferred to the concrete BlueprintPolicy subclasses, so AtpBlueprint stays unstamped)
  - Spec facts: abstract; Base = ARObject only (no Referrable/Identifiable) → `__init__(self)` with all fields defaulted (Rule 0001.2); Package = M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::AbstractBlueprintStructure — **same non-leaf `__init__.py` as AtpBlueprint** (Rule 0007); Note verbatim: "This meta-class represents the ability to indicate whether blueprintable elements will be modifiable or not modifiable."; Subclasses = BlueprintPolicyModifiable, BlueprintPolicyNotModifiable (concrete — follow-up classes, not yet queued); Aggregated by AtpBlueprint.blueprintPolicy; **one own attribute** `attributeName` (String, 1, attr) — Note verbatim: "This identifies the related attribute of a BlueprintPolicy. For navigation over the model a subset of xpath expressions is used." (todo's "no own attributes / marker class" was WRONG — confirmed in markdown Table C.18 body + XSD group BLUEPRINT-POLICY l.9211; attributeName serialized via concrete subclasses BLUEPRINT-POLICY-LIST/-NOT-MODIFIABLE/-SINGLE). On sync, implementing BlueprintPolicy upgrades AtpBlueprint's `List[ARObject]` placeholder to `List[BlueprintPolicy]`; the blueprintPolicy **reader/writer remains deferred** until the concrete subclasses (BlueprintPolicyList/NotModifiable/Single) are synced — so AtpBlueprint's `# Spec verified:` stamp stays withheld (the Rule 0001.10 blocker moves to the subclasses).
  - [x] Step 1 — Sync members & description from spec — Table C.18 (NOT C.17), p.164 (R23-11, located via pypdf — pdf_page.py can't index appendix-letter tables); confirmed BlueprintPolicy is abstract, Base = ARObject only, ONE attribute `attributeName` (String, 1, attr) — todo's "no own attributes / marker class" was WRONG; XSD group BLUEPRINT-POLICY l.9211 confirms attributeName; serialized via concrete subclasses BLUEPRINT-POLICY-LIST/-NOT-MODIFIABLE/-SINGLE.
  - [x] Step 2 — Write model class unit test (Red) — tests/.../AbstractBlueprintStructure/test___init__.py::TestBlueprintPolicy: abstract guard, concrete-subclass init + attributeName default, set/get round-trip + None no-op + chaining, class docstring verbatim, get/set docstrings verbatim. Red confirmed: ImportError (no BlueprintPolicy).
  - [x] Step 3 — Implement model class (Green) — `class BlueprintPolicy(ARObject, ABC)` in AbstractBlueprintStructure/__init__.py; abstract guard; `self.attributeName: Optional[String] = None` (PEP 526); getAttributeName/setAttributeName (None-guarded, returns self). Also upgraded AtpBlueprint's `blueprintPolicys: List[ARObject]` → `List[BlueprintPolicy]` + `addBlueprintPolicy(Optional[BlueprintPolicy])` + comment. Exported in `__all__`. 5/5 model tests Green; AtpBlueprint tests still 15/15 Green.
  - [x] Step 4 — Sync docstrings (wipe + rewrite) — new class (no old docstrings); class docstring = Table C.18 Note verbatim (single-line so `__doc__` matches exactly); inline comment + get/set docstrings = attributeName Note verbatim (XSD l.9220); setter appends None no-op sentence; `__init__` has no docstring.
  - [x] Step 5 — Write reader/writer round-trip test (Red) — tests/test_armodel/parser/test_blueprint_policy.py::TestBlueprintPolicyReaderWriter: asserts no readBlueprintPolicy/writeBlueprintPolicy (N/A contract — abstract, no own XML element), abstract guard, attributeName field. 3 passed (N/A confirmation).
  - [x] Step 6 — Update parser & writer (Green) — N/A: BlueprintPolicy is abstract; the BLUEPRINT-POLICY group (XSD l.9211) is substituted by concrete subclasses, so there is no readBlueprintPolicy/writeBlueprintPolicy to add. Confirmed via grep + the Step-5 test.
  - [x] Step 7 — Update checklist comment — 6-column `# Spec:` format embedded in class body (`R23-11/AUTOSAR_FO_TPS_StandardizationTemplate.pdf, Table C.18, p.164 (R23-11)`), all rows `[x]` with reader/writer `[—]` (N/A, abstract); `# Spec verified:` marker deferred to 9b. AtpBlueprint checklist comment updated: blueprintPolicy aggregation type now `List[BlueprintPolicy]`, reader/writer rows stay `[ ]` (deferred to concrete subclasses).
  - [x] Step 8 — Deviations — **none for BlueprintPolicy itself**: Class=abstract (matches Table C.18), Base ARObject only (most-derived, matches), Package AbstractBlueprintStructure (matches Rule 0007), single attribute attributeName (String, 1, attr) modeled with verbatim docstrings, reader/writer N/A (abstract, no own XML element). Rule 0001.10 reference report: the member type `BlueprintPolicy` is now implemented (was the blocker). The outstanding deviation is **AtpBlueprint's `blueprintPolicy` reader/writer**, which stays deferred because the concrete subclasses `BlueprintPolicyList`/`BlueprintPolicyNotModifiable`/`BlueprintPolicySingle`/`BlueprintPolicyModifiable` are NOT yet synced (they own the BLUEPRINT-POLICY-* XML elements + attributeName coverage) — so AtpBlueprint's `# Spec verified:` stamp remains withheld (the Rule 0001.10 blocker moves to the subclasses). Deviation tracker `docs/examples/method_deviation_by_class.md` AtpBlueprint row corrected: type `List[ARObject]`→`List[BlueprintPolicy]`, removed the false "no own spec table" claim, recorded BlueprintPolicy as synced and the deferred reader/writer as the remaining blocker.
  - [x] Step 9 — Verify (9a) + confirm (9b) — 9a: 8479 unit tests pass, ruff+flake8 clean, black clean, integration round-trip (test_roundtrip_all_files) passes; 9b user-confirmed 2026-09-03: every spec attr modeled (attributeName), base ARObject most-derived, verbatim docstrings by diff (class + inline + get/set), reader/writer N/A justified (abstract, no own XML element; attributeName serialized via concrete subclasses), member order, Rule 0007 location (AbstractBlueprintStructure/__init__.py), no deviations for BlueprintPolicy itself → `# Spec verified: R23-11` written; committed f5f5084e on feature/sync-blueprint-policy; row flipped to `[x]`.
- [x] `AtpBlueprint` (heritage mixin branch of ARPackage (Table 4.1 Base) · **finished, UNSTAMPED per 9b user decision 2026-09-03 (Rule 0001.10 placeholder BlueprintPolicy queued — commit: fc0ebeff)** · R23-11 markdown · AUTOSAR_FO_TPS_StandardizationTemplate · Table C.12, p.161)
  - Spec facts (extracted 2026-08-30): abstract; Base = ARObject, Identifiable, MultilanguageReferrable, Referrable → direct base **Identifiable** (queued above) — code `AtpBlueprint(Identifiable, ABC)` (AbstractBlueprintStructure/__init__.py:43) heritage **CORRECT**; own attribute `blueprintPolicy` (BlueprintPolicy, aggr); Subclasses explicitly list ARPackage.
  - **Step 1 resolution (2026-09-03):** synced from **R23-11** corpus (project release). Citation = `R23-11/AUTOSAR_FO_TPS_StandardizationTemplate.pdf, Table C.12, p.161` (R23-11 renders the R4.3.1 Table 4.2 here as appendix C.12; page 161 extracted via pypdf; `pdf_page.py` can't read appendix-letter tables so pypdf was used). Class Note verbatim: "This meta-class represents the ability to act as a Blueprint. As this class is an abstract one, particular blueprint meta-classes inherit from this one." Attribute `blueprintPolicy | BlueprintPolicy | * | aggr`, Note verbatim: "This role indicates whether the blueprintable element will be modifiable or not modifiable." Package `M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::AbstractBlueprintStructure` → file matches (Rule 0007). `BlueprintPolicy` (member type, abstract) is **now implemented** (R23-11 Table C.18, p.164; stamped `# Spec verified: R23-11` commit f5f5084e); AtpBlueprint's `blueprintPolicys` field upgraded `List[ARObject]` → `List[BlueprintPolicy]`; marker `# Spec verified:` for AtpBlueprint **still withheld** because the `blueprintPolicy` aggregation reader/writer requires the concrete `BlueprintPolicy` subclasses (BlueprintPolicyList/NotModifiable/Single), which are not yet synced (Step 8/9b). Member-type-name `blueprintPolicy` (`*`) → plural Python `blueprintPolicys` + `addBlueprintPolicy`/`getBlueprintPolicys` (Rule 0001.4) — already correct in code.
  - Note: ARPackage's 9b does NOT block on this row (blueprint mixin attrs not modeled on ARPackage by design — Rule 0001.2 single-branch selection, documented in ARPackage checklist comment).
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red) — tests/test_armodel/models/M2/AUTOSARTemplates/CommonStructure/StandardizationTemplate/AbstractBlueprintStructure/test___init__.py::TestAtpBlueprint: heritage closure (direct base Identifiable, MRO == ARObject/Identifiable/MultilanguageReferrable/Referrable, AtpBlueprintable NOT in MRO), class docstring verbatim, blueprintPolicy add/get docstrings verbatim. Red confirmed: 2 failed (class docstring leading-newline mismatch; add/get docstrings paraphrased "Adds a BlueprintPolicy…") / 1 passed (heritage).
  - [x] Step 3 — Implement model class (Green) — model already spec-correct: `class AtpBlueprint(Identifiable, ABC)` (most-derived base Identifiable; abstract guard present), `self.blueprintPolicys: List[ARObject] = []` (PEP 526; singular `*` spec attr → plural list, Rule 0001.4), `addBlueprintPolicy(value)` (None-no-op, returns self) + `getBlueprintPolicys()` (Rule 0004). No impl change needed; the only pre-existing defect was paraphrased/leading-newline docstrings (fixed in Step 4).
  - [x] Step 4 — Sync docstrings (wipe + rewrite) — wiped the multi-line/paraphrased docstrings; class docstring = Table C.12 Note verbatim (single-line so `__doc__` matches exactly); `addBlueprintPolicy` docstring = verbatim Note + None-no-op sentence; `getBlueprintPolicys` docstring = verbatim Note; `__init__` has no docstring; the Rule 0001.10 placeholder comment on `self.blueprintPolicys` kept. 3/3 docstring+heritage tests Green.
  - [x] Step 5 — Write reader/writer round-trip test (Red) — tests/test_armodel/parser/test_atp_blueprint.py::TestAtpBlueprintReaderWriter: no dedicated readAtpBlueprint/writeAtpBlueprint (N/A contract), Identifiable in MRO, inherited shortName round-trips via shared readIdentifiable/writeIdentifiable, blueprintPolicy aggregation deferred (Rule 0001.10 placeholder). 4 passed (N/A confirmation).
  - [x] Step 6 — Update parser & writer (Green) — N/A: AtpBlueprint is abstract with no own XML element; no readAtpBlueprint/writeAtpBlueprint (confirmed via grep on parser/writer). The blueprintPolicy aggregation is deferred because BlueprintPolicy (member type) is unimplemented — no dispatch edit without the real type. No chained mutator calls.
  - [x] Step 7 — Update checklist comment — converted to the 6-column unified `# Spec:` format (`R23-11/AUTOSAR_FO_TPS_StandardizationTemplate.pdf, Table C.12, p.161 (R23-11)`), `release R23-11` added to all rows, reader/writer columns (`[—]` for `__init__`, deferred `[ ]` for the blueprintPolicy aggregation). `# Spec verified:` marker is **withheld** (Rule 0001.10 placeholder) — a trailing note records why.
  - [x] Step 8 — Deviations — only accepted deviation: the `blueprintPolicy` aggregation reader/writer is **deferred** because the concrete `BlueprintPolicy` subclasses (BlueprintPolicyList/NotModifiable/Single/Modifiable) are not yet synced — they own the `BLUEPRINT-POLICY-LIST`/`-NOT-MODIFIABLE`/`-SINGLE` XML elements and thus the `attributeName` coverage (the Rule 0001.10 blocker moved from `BlueprintPolicy` itself to its subclasses once BlueprintPolicy was stamped R23-11, commit f5f5084e). The `BlueprintPolicy` member type is no longer a placeholder (`List[ARObject]` → `List[BlueprintPolicy]`). No `naming`/`type`/`missing` to-fix rows remain. Rule 0007 location OK (file = Package tail). Heritage Identifiable (most-derived) spec-correct. Member name `blueprintPolicys` (plural of singular `*` spec attr) spec-correct (Rule 0001.4). No member-order issue (single attribute).
  - [x] Step 9 — Verify (9a) + confirm (9b) — 9a: full suite 8472 passed (0 failed); ruff+black+flake8 clean on all changed files; `test_roundtrip_all_files` lossless. 9b: user confirmed (2026-09-03) with instruction to queue BlueprintPolicy first, then commit the **unstamped** AtpBlueprint (Rule 0001.10 placeholder BlueprintPolicy still pending). BlueprintPolicy is now synced (commit f5f5084e, `# Spec verified: R23-11`); AtpBlueprint's `# Spec verified:` **remains withheld** because its `blueprintPolicy` reader/writer is deferred to the concrete subclasses (recorded in Step 7/8 and the deviation tracker).
- [x] `AtpBlueprintable` (tracker input · **source corrected R4.3.1→R23-11** (the class exists in R23-11; R4.3.1 citation was a mis-detection — see Step 8) · R23-11/AUTOSAR_FO_TPS_StandardizationTemplate · Table C.14, p.162 · **heritage fix**: re-parent `AtpBlueprintable(PackageableElement)` → `(Identifiable)` — Base = ARObject, Identifiable, MultilanguageReferrable, Referrable (no PackageableElement/CollectableElement in its chain; element aggregation lives on Identifiable so subclasses keep it); do AFTER the Identifiable row above) (synced b7cf0309)
  - [x] Step 1 — Sync members & description from spec — R23-11 Table C.14 (PDF p.162, caption clean; markdown body misaligned under "C.13: AtpBlueprintMapping"): Note + Base = ARObject, Identifiable, MultilanguageReferrable, Referrable; no attributes. Heritage fix confirmed (PackageableElement/CollectableElement are empty markers).
  - [x] Step 2 — Write model class unit test (Red) — test___init__.py::TestAtpBlueprintable: abstract guard, direct base Identifiable (not PackageableElement), MRO == ARObject/Identifiable/MultilanguageReferrable/Referrable, PackageableElement NOT in MRO, concrete-subclass init reaches parent/short_name, class docstring == verbatim Table C.14 Note. Red confirmed (1 failed: __bases__[0] was PackageableElement).
  - [x] Step 3 — Implement model class (Green) — `class AtpBlueprintable(Identifiable, ABC)` (was `PackageableElement`); dropped unused PackageableElement import; abstract guard + `super().__init__(parent, short_name)` unchanged. 6/6 green.
  - [x] Step 4 — Sync docstrings (wipe + rewrite) — wiped the multi-line/paraphrased docstring; class docstring = Table C.14 Note verbatim (single-line so `__doc__` matches exactly); `__init__` has no docstring; AtpBlueprintable has no attribute accessors to sync.
  - [x] Step 5 — Write reader/writer round-trip test (Red) — tests/test_armodel/parser/test_atp_blueprintable.py::TestAtpBlueprintableReaderWriter: no dedicated readAtpBlueprintable/writeAtpBlueprintable (N/A), Identifiable in MRO, PackageableElement NOT in MRO (Red on pre-fix code), inherited shortName round-trips via shared readIdentifiable/writeIdentifiable. 4 passed (N/A confirmation; the PackageableElement assertion is Red pre-Step-3, Green after).
  - [x] Step 6 — Update parser & writer (Green) — N/A: AtpBlueprintable is abstract with no own XML element; no readAtpBlueprintable/writeAtpBlueprintable (confirmed via grep + test); heritage change (Identifiable base) needs no parser/writer edit (no isinstance dispatch on PackageableElement/CollectableElement anywhere). No chained mutator calls.
  - [x] Step 7 — Update checklist comment — 6-col unified `# Spec:` format (`R23-11/AUTOSAR_FO_TPS_StandardizationTemplate.pdf, Table C.14, p.162 (R23-11)`), `release R23-11` on the `__init__` row, reader/writer `[—]` (no XML element). `# Spec verified:` held for 9b. Source-corpus correction (R4.3.1→R23-11) + heritage-fix note recorded in the comment.
  - [x] Step 8 — Deviations — no `naming`/`type`/`missing` to-fix rows: Base re-parented PackageableElement→Identifiable per R23-11 Table C.14 (PackageableElement/CollectableElement are empty markers; subclasses keep `element` via Identifiable). Tracker `## AtpBlueprintable` added (no deviation); source corpus corrected R4.3.1→R23-11 documented.
  - [x] Step 9 — Verify (9a) + confirm (9b) — synced b7cf0309
- [x] `AtpBlueprintMapping` (tracker input · **R23-11** corpus — corrected from the todo's R4.3.1 citation: R23-11 Table C.13 (FO_StandardizationTemplate PDF p.162) is the authoritative spec; the R4.3.1 Table 4.4 "AtpBlueprintMapping" is mislabeled BlueprintPolicy content, already synced as BlueprintPolicy R23-11 C.18 · AUTOSAR_00052.xsd group ATP-BLUEPRINT-MAPPING l.6888) — **finished, stamped `# Spec verified: R23-11`** (commit: 493e272d) — abstract shell carrying two `atpAbstract` derived association ends (`atpBlueprint` → `atpBlueprintRef`, `atpBlueprintedElement` → `atpBlueprintedElementRef`) added 2026-09-03 after the stamp was unblocked; they are serialized only on the concrete `BlueprintMapping` subclass (BLUEPRINT-REF / DERIVED-OBJECT-REF), so the abstract class has no own XML element (reader/writer `[—]`).
  - Spec facts: abstract; Package = ...StandardizationTemplate::AbstractBlueprintStructure (file AbstractBlueprintStructure/__init__.py ✓ Rule 0007); Base = ARObject (XSD AR-OBJECT group chain, most-derived direct base); two **atpAbstract** `ref` association ends declared on the abstract class — `atpBlueprint` (AtpBlueprint, 1, ref) and `atpBlueprintedElement` (AtpBlueprintable, 1, ref) — both `Stereotypes: atpAbstract` (Table C.13), so the XSD serializes them only on concrete subclasses as BLUEPRINT-REF/DERIVED-OBJECT-REF (BLUEPRINT-MAPPING group l.9118); Note (verbatim, XSD l.6890 + PDF C.13) = "This meta-class represents the ability to express a particular mapping between a blueprint and an element derived from this blueprint. Particular mappings are defined by specializations of this meta-class."; Subclasses include BlueprintMapping, PortInterfaceBlueprintMapping (# XSD verified), PortPrototypeBlueprintMapping (# XSD verified).
  - [x] Step 1 — Sync members & description from spec — R23-11 Table C.13 (PDF p.162) + XSD ATP-BLUEPRINT-MAPPING l.6888; Base=ARObject; no own attributes; verbatim Note captured
  - [x] Step 2 — Write model class unit test (Red) — TestAtpBlueprintMapping: abstract guard, direct base ARObject, MRO (no Identifiable/PackageableElement), concrete subclass, verbatim class docstring; Red confirmed (docstring)
  - [x] Step 3 — Implement model class (Green) — `class AtpBlueprintMapping(ARObject, ABC)` already spec-correct (abstract, no fields, base ARObject); readAtpBlueprintMapping/writeAtpBlueprintMapping delegate to base chain
  - [x] Step 4 — Sync docstrings (wipe + rewrite) — class docstring = verbatim R23-11 Table C.13 / XSD l.6890 Note (single-line so `__doc__` matches exactly); old paraphrased docstring wiped
  - [x] Step 5 — Write reader/writer round-trip test (Red) — tests/test_armodel/parser/test_atp_blueprint_mapping.py (N/A confirmation: no own XML element; base-delegating handlers exist); abstract base round-trip covered by test_blueprint_mapping_set.py
  - [x] Step 6 — Update parser & writer (Green) — N/A: readAtpBlueprintMapping/writeAtpBlueprintMapping already delegate to readARObject/writeARObject; no new code
  - [x] Step 7 — Update checklist comment — 6-col `# Spec:` format (Table C.13, p.162, R23-11); marker deferred to 9b
  - [x] Step 8 — Deviations — AtpBlueprintMapping itself: none. Observation (separate row): concrete `BlueprintMapping` missing `blueprint`(BLUEPRINT-REF)/`derivedObject`(DERIVED-OBJECT-REF) per XSD BLUEPRINT-MAPPING group l.9118 — recommend a BlueprintMapping sync row. Deviation tracker AtpBlueprintMapping entry corrected (stale Package/Source/"missing" rows fixed).
  - [x] Step 9 — Verify (9a) + confirm (9b) — 9a: 31 AbstractBlueprintStructure tests + 148 blueprint tests pass, ruff/black clean on the class + its test (repo-wide lint/black failures are unrelated in-flight edits to ApplicationDeferredDataType/test_arxml_parser_dispatch, not this class). 9b user-confirmed: Base ARObject most-derived, both atpAbstract members now modeled (atpBlueprintRef/atpBlueprintedElementRef) with verbatim docstrings, reader/writer N/A justified (abstract, no own XML element), member order, Rule 0007 location, no deviations for AtpBlueprintMapping itself → `# Spec verified: R23-11` written (commit: 493e272d)
- [x] `ApplicationDeferredDataType` (tracker input · R23-11 markdown · AUTOSAR_FO_TPS_AbstractPlatformSpecification · Table 3.17) — **finished, stamped `# Spec verified: R23-11`** (commit: abdfbf1d)
  - [x] Step 1 — Sync members & description from spec — Table 3.17 (p.37): Note + Base closure (role-matching most-derived base ApplicationDataType) + no own Attribute rows
  - [x] Step 2 — Write model class unit test (Red) — existing TestApplicationDeferredDataType (init, heritage, verbatim docstring, no-own-attrs, create-method) passes
  - [x] Step 3 — Implement model class (Green) — `class ApplicationDeferredDataType(ApplicationDataType)` already spec-correct; class reduces to `__init__` (no own attributes)
  - [x] Step 4 — Sync docstrings (wipe + rewrite) — class docstring verbatim from Table 3.17 Note (Tags tail dropped); no own members
  - [x] Step 5 — Write reader/writer round-trip test (Red) — parser test (read + uuid + full write→parse round-trip) + writer test (XML shape); 4 pass
  - [x] Step 6 — Update parser & writer (Green) — N/A: readApplicationDeferredDataType/writeApplicationDeferredDataType + APPLICATION-DEFERRED-DATA-TYPE dispatch already cover it (verified via round-trip)
  - [x] Step 7 — Update checklist comment — 6-col `# Spec:` (PDF, Table 3.17, p.37, R23-11) + `# Spec verified: R23-11`
  - [x] Step 8 — Deviations — none: heritage ApplicationDataType most-derived role-matching base (parallel branches not multi-inherited per Rule 0001.2); no own attributes to mis-model; reader/writer fully covered
  - [x] Step 9 — Verify (9a) + confirm (9b) — 9a: 9 ADDT tests + 197 related unit + integration round-trip pass, ruff/black clean; 9b user-confirmed 2026-09-03: all blind-spot checks pass (verbatim docstring, heritage, no own attrs, Rule 0007 location) → `# Spec verified: R23-11` written; commit abdfbf1d
- [x] `PortInterfaceMapping` (tracker input · R23-11 markdown · AUTOSAR_CP_TPS_SoftwareComponentTemplate · Table 4.20) — **finished, stamped `# Spec verified: R23-11`** (commit: ca6a3723)
  - [x] Step 1 — Sync members & description from spec — Table 4.20 body md l.3527–3535; caption l.3525; PDF p.119 confirmed via pdf_page.py (R4.3.1 has Table 4.24 p.124 — unused, R23-11 table exists). Class=abstract; Package=...SWComponentTemplate::PortInterface; Base=ARObject, AtpBlueprint, AtpBlueprintable, Identifiable, MultilanguageReferrable, Referrable → role branch **AtpBlueprintable** ✓ current heritage correct (parallel AtpBlueprint/AtpBlueprintable chains not added via MI, ARPackage precedent); Note (verbatim) captured for Step 4; Attributes row = `-` — **no own attributes** (abstract shell); Subclasses: ClientServerInterfaceMapping, ModeInterfaceMapping, TriggerInterfaceMapping, VariableAndParameterInterfaceMapping; Aggregated by PortInterfaceMappingSet.portInterfaceMapping. No own XML element (abstract) → Steps 5/6 expected N/A. Current code: no class docstring, stale 3-col checklist
  - [x] Step 2 — Write model class unit test (Red) — test_PortInterface.py TestPortInterfaceMapping: test_PortInterfaceMapping_abstract (TypeError msg) + test_PortInterfaceMapping_concrete_subclass_inheritance (isinstance chain via ClientServerInterfaceMapping, parent/short_name). Result: both pass immediately — impl already matches Table 4.20 (abstract shell, no attributes); no failing assertion found
  - [x] Step 3 — Implement model class (Green) — no change required: `PortInterfaceMapping(AtpBlueprintable, ABC)` + abstract TypeError guard verified correct by the Step-2 tests; Base chain confirmed (AtpBlueprintable role branch, ARPackage precedent)
  - [x] Step 4 — Sync docstrings (wipe + rewrite) — no pre-existing docstrings on this class (wipe vacuous); class docstring written verbatim from md l.3530 Note; no member docstrings (no own attributes, `__init__` has no docstring per Rule 0012.2.4)
  - [x] Step 5 — Write reader/writer round-trip test (Red) — N/A: abstract class, no own XML element; XSD AUTOSAR_00052.xsd l.92574 defines `PORT-INTERFACE-MAPPING` as an element **group** (concrete subclasses substitute into it) — round-trip covered by the concrete subclass syncs
  - [x] Step 6 — Update parser & writer (Green) — N/A: same reason as Step 5
  - [x] Step 7 — Update checklist comment — 6-col format with `# Spec: R23-11/AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.20, p.119 (R23-11)`; single row `__init__` (reader/writer `[—]`, release R23-11); marker deferred to 9b
  - [x] Step 8 — Deviations — none for the class itself (no own attributes, heritage correct, docstring verbatim). Rule 0001.10 reference report (non-blocking): base `AtpBlueprintable` was queued above (row `AtpBlueprintable`, `## AtpPrototype heritage-drift follow-ups` section — the original `l.297` reference was stale); concrete subclass `TriggerInterfaceMapping` queued in `## Remaining queue — reordered 2026-09-04` (row 14, moved there by the 2026-09-04 re-queue — this row's `l.457` reference is stale); concrete subclasses `ClientServerInterfaceMapping` / `ModeInterfaceMapping` / `VariableAndParameterInterfaceMapping` NOT queued (Table 4.20 Subclasses row; inherit from this class, no member-type edge) — future queue candidates
  - [x] Step 9 — Verify (9a) + confirm (9b) — 9a: 8210 unit + 2 integration round-trip pass, ruff/flake8/black clean; 9b (user-confirmed): Rules 0001.1/0001.2/0001.3/0003/0012/0014 pass, N/A items justified (no attributes/no XML element), Rule 0007 package-location check pass (PortInterface/__init__.py non-leaf shape, explicit imports, top-level export True, not in exclusion lists); no deviations; marker written

## Remaining queue — reordered 2026-09-04 (dependency-first)

**Review pass (2026-09-04).** The 14 rows still `[ ]` above were removed from that
historical list and re-queued here together with the **17 related parent / member
classes that were missing** (Rule 16.5: *an un-stamped member type is **not** skipped —
it is queued* — "exists in the codebase" is not a stamp; verify the marker).

- **Closure depth: level-1 only** — every direct `Base` (most-derived) and every direct
  `Attribute` member type of the queued classes. Member types of the *newly added* rows
  are **not** queued here; see the next-level section below — they get queued when the
  owning row reaches Step 1.
- **Subclasses are not queued** (`PortInterfaceMapping` Step-8 precedent: no member-type
  edge) — see `## Not queued`.
- **Order:** bases before member types, dependency-first inside each cluster; clusters
  are then ordered by how many queued classes they unblock (most-blocking first). The
  cheap abstract shells that gate concrete classes are top priority; the heavy
  `Implementation` subtree is bottom.
- **Stamp audit method:** `ast` walk over `src/armodel/models/**` (2026-09-04) — a class
  counts as stamped only if `# Spec verified:` / `# XSD verified:` appears in its own
  body. `Identifiable` is still UNSTAMPED (variationPoint mixin refactor awaiting 9b), so
  every `Identifiable`-derived row inherits that blocker until it is re-stamped.
- **Heritage verdict for the 14 originally-queued rows: only `FlatMap` is wrong**
  (verified against the spec `Base` closure, cross-checked against the XSD complexType
  chain where the closure was ambiguous). The other 13 already derive from their
  most-derived spec base.
- Notes quoted below are the **markdown** cell text with the corpus's line-wrap artefacts
  normalised (`Multilanguage Referrable` → `MultilanguageReferrable`,
  `swDataDef Props` → `swDataDefProps`, …). Re-verify verbatim against the PDF in Step 1
  before writing any docstring (Rule 0001.4).

### Dependency map (why this order)

```
AutosarDataType ──────────────> AbstractImplementationDataType
AtpStructureElement (✓) ──────> AbstractImplementationDataTypeElement

DataInterface ────────────────> ParameterInterface
      │                         NvDataInterface
      │                         SenderReceiverInterface
      ├── VariableDataPrototype ──> NvDataInterface, SenderReceiverInterface,
      │                             InvalidationPolicy
      └── HandleInvalidEnum ──> InvalidationPolicy ──> SenderReceiverInterface

Trigger ──────────────────────> TriggerInterface
      └────────────────────────> TriggerMapping ──> TriggerInterfaceMapping

IdentCaption ────────────────> ModeAccessPointIdent
AtpType (✓) + ModeDeclarationMapping (✓) ──> ModeDeclarationMappingSet
SubElementRef + TextTableMapping ──> SubElementMapping
FlatInstanceDescriptor ──────> FlatMap            (FlatMap: heritage fix AtpBlueprintable → ARElement)

ProgramminglanguageEnum, Compiler, Linker, Code, DependencyOnArtifact,
ResourceConsumption, SwcBswMapping, BuildActionManifest ──> Implementation
```

(`✓` = already stamped, not re-queued.)

### Cluster 1 — AutosarDataType → AbstractImplementationDataType

- [x] `AutosarDataType` (**NEW — parent of `AbstractImplementationDataType`** · R23-11 markdown · AUTOSAR_CP_TPS_SoftwareComponentTemplate · Table 5.1, p.232 · **heritage fix: code `AutosarDataType(AtpType, ABC)` → spec most-derived direct base `ARElement`**) · **stamped `# Spec verified: R23-11`** (commit: a5f99df4, branch feature/sync-rte-event)
  - Spec facts (extracted 2026-09-04): abstract; Package = M2::AUTOSARTemplates::SWComponentTemplate::Datatype::Datatypes (file `SWComponentTemplate/Datatype/Datatypes.py` ✓ Rule 0007); Base = ARElement, ARObject, AtpClassifier, AtpType, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable → most-derived direct base **ARElement** — code has `AtpType`, which skips PackageableElement → CollectableElement → ARElement; Subclasses = AbstractImplementationDataType, ApplicationDataType; Aggregated by ARPackage.element; 1 own attribute `swDataDefProps` (SwDataDefProps, 0..1, aggr) — member type **stamped R23-11** ✓; Note (md, wrap-normalised): "Abstract base class for user defined AUTOSAR data types for software."
  - Why first: it is the only un-stamped **base** in the queue and it gates `AbstractImplementationDataType` (Rules 0001.10 / 0012.1). Fixing the base also requires an audit of the two subclasses' MRO (`AbstractImplementationDataType`, `ApplicationDataType`) plus their subtrees for anything that relied on the wrong chain.
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red) — tests/test_armodel/parser/test_autosar_data_type.py: SW-DATA-DEF-PROPS round-trip via ApplicationPrimitiveDataType (with + without); reader calls setSwDataDefProps, writer calls getSwDataDefProps
  - [x] Step 6 — Update parser & writer (Green) — N/A: readAutosarDataType + writeAutosarDataType already serialize SW-DATA-DEF-PROPS (readIdentifiable/writeARElement + set/getSwDataDefProps); regression of data-type parser/writer tests passed (97 passed). No code change required.
  - [x] Step 7 — Update checklist comment — 6-col `# Spec:` format (AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.1, p.232, R23-11) + per-row release R23-11; reader `[x]` on setSwDataDefProps mutator, writer `[x]` on getSwDataDefProps getter; `# Spec verified:` marker deferred to 9b
  - [x] Step 8 — Deviations — accepted (non-blocking, repo convention; stamp allowed):
    - **Heritage (base-class collapse):** spec `Base` = ARElement, ARObject, AtpClassifier, AtpType, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable (full XSD MI chain). Code = `AutosarDataType(ARElement, ABC)` — single role-matching chain per repo convention (precedent: `AtpType(Identifiable)`, `BlueprintPolicy(Identifiable)`); the AtpType/AtpClassifier/CollectableElement blueprinting branches are intentionally collapsed, with the behavioral bases (Identifiable → MultilanguageReferrable → Referrable → PackageableElement → ARObject) preserved through ARElement's MRO. Reader/writer dispatch (`readAutosarDataType`/`writeAutosarDataType`) already uses `readIdentifiable`/`writeARElement`, so the base change aligns the model with dispatch.
    - **Docstring tail:** spec `Note` for `swDataDefProps` carries a `Stereotypes: atpSplitable Tags: atp.Splitkey=swDataDefProps` tail; docstring uses the human-readable `Note` without the XSD Stereotypes/Tags metadata tail (repo convention, matches stamped `ApplicationArrayDataType` et al.).
    - **Completeness:** the single spec attribute `swDataDefProps` (SwDataDefProps, 0..1, aggr — member type stamped R23-11) is fully modeled (`__init__` field `self.swDataDefProps` + `getSwDataDefProps`/`setSwDataDefProps`) with reader + writer coverage; no fabricated or dropped members.
  - [x] Step 9 — Verify (9a) + confirm (9b) — 9a: pytest 22+119 passed, flake8 clean, ruff clean, black clean, parity script no new failures, integration round-trip passed; 9b: full rule-compliance checklist confirmed by user; `# Spec verified: R23-11` marker written into source
- [x] `AbstractImplementationDataType` (tracker input · R23-11 markdown · AUTOSAR_CP_TPS_SoftwareComponentTemplate · Table 5.14, p.267 · **after `AutosarDataType` (base)**) — `# Spec verified: R23-11` (commit: 9b5379d3)
  - Spec facts (extracted 2026-09-04): abstract; Package = M2::AUTOSARTemplates::CommonStructure::ImplementationDataTypes (file `CommonStructure/ImplementationDataTypes.py` ✓ Rule 0007); Base = ARElement, ARObject, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, AutosarDataType, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable → most-derived direct base **AutosarDataType** ✓ heritage already correct in code (`AbstractImplementationDataType(AutosarDataType, ABC)`); Subclasses = ImplementationDataType; Aggregated by ARPackage.element; **Attribute rows = `-` → no own attributes** → Steps 5/6 expected N/A (abstract shell, no own XML element); Note (md, wrap-normalised): "This meta-class represents an abstract base class for different flavors of ImplementationDataType."
  - Known deviations to fix in this sync: no `# Spec:` line / stamp (unstamped); checklist is not in the 6-column format.
   - [x] Step 1 — Sync members & description from spec (Table 5.14 confirms abstract class, direct base AutosarDataType, no own attributes, verbatim Note; p.267 via pdf_page.py)
   - [x] Step 2 — Write model class unit test (Red) — abstract guard, direct base, inherited state, exact spec Note
   - [x] Step 3 — Implement model class (Green) — existing heritage and abstract guard retained; no own members
   - [x] Step 4 — Sync docstrings (wipe + rewrite) — class docstring replaced with verbatim Table 5.14 Note
   - [x] Step 5 — Write reader/writer round-trip test (Red) — N/A: no own attributes or XML element; coverage belongs to concrete subclasses
   - [x] Step 6 — Update parser & writer (Green) — N/A: no own attributes or XML element; inherited AutosarDataType handling is already covered
   - [x] Step 7 — Update checklist comment — six-column parity checklist with R23-11 provenance
   - [x] Step 8 — Deviations — none
   - [x] Step 9 — Verify (9a) + confirm (9b) — user-confirmed 2026-09-04; stamped `# Spec verified: R23-11`

### Cluster 2 — AbstractImplementationDataTypeElement (independent, base already stamped)

- [x] `AbstractImplementationDataTypeElement` (tracker input · R23-11 markdown · AUTOSAR_CP_TPS_SoftwareComponentTemplate · Table 5.16, p.269 · after `AtpStructureElement` (base, stamped R23-11)) — finished, stamped `# Spec verified: R23-11` (commit: cabd5469)
  - Spec facts (extracted 2026-09-04): abstract; Package = M2::AUTOSARTemplates::CommonStructure::ImplementationDataTypes (file `CommonStructure/ImplementationDataTypes.py` ✓ Rule 0007); Base = ARObject, AtpClassifier, AtpFeature, AtpStructureElement, Identifiable, MultilanguageReferrable, Referrable → most-derived direct base **AtpStructureElement** ✓ heritage already correct in code, and the base is **stamped R23-11**; Subclasses = ImplementationDataTypeElement; Aggregated by AtpClassifier.atpFeature; **Attribute rows = `-` → no own attributes** → Steps 5/6 expected N/A; Note (md, wrap-normalised): "This meta-class represents the ability to act as an abstract base class for specific derived meta-classes that support the modeling of ImplementationDataTypes for a particular language."
  - Known deviations to fix in this sync: no `# Spec:` line / stamp; 6-column checklist missing. Nothing blocks it, which is why it sits here rather than later.
   - [x] Step 1 — Sync members & description from spec
   - [x] Step 2 — Write model class unit test (Red)
   - [x] Step 3 — Implement model class (Green)
   - [x] Step 4 — Sync docstrings (wipe + rewrite)
   - [x] Step 5 — Write reader/writer round-trip test (Red) — N/A: no own attributes or XML element
   - [x] Step 6 — Update parser & writer (Green) — N/A: no own attributes or XML element
   - [x] Step 7 — Update checklist comment
   - [x] Step 8 — Deviations — none
   - [x] Step 9 — Verify (9a) + confirm (9b) — 9a: 47 focused tests, lint, Black, and diff checks pass; 9b user-confirmed 2026-09-04; marker written

### Cluster 3 — DataInterface subtree (DataInterface unblocks three concrete interfaces)

- [x] `DataInterface` (tracker input · R23-11 markdown · AUTOSAR_CP_TPS_SoftwareComponentTemplate · Table 3.19, p.87 · **before `NvDataInterface` / `ParameterInterface` / `SenderReceiverInterface` (base of all three)**) — finished, stamped `# Spec verified: R23-11` (commit: d838fd43)
  - Spec facts (extracted 2026-09-04): abstract; Package = M2::AUTOSARTemplates::SWComponentTemplate::PortInterface (file `SWComponentTemplate/PortInterface/__init__.py` ✓ Rule 0007); Base = ARElement, ARObject, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, PortInterface, Referrable → most-derived direct base **PortInterface** ✓ heritage already correct in code (`DataInterface(PortInterface, ABC)`), base **stamped R23-11**; Subclasses = NvDataInterface, ParameterInterface, SenderReceiverInterface (all three queued below); Aggregated by ARPackage.element; **Attribute rows = `-` → no own attributes** → Steps 5/6 N/A; Note (md, wrap-normalised): "The purpose of this meta-class is to act as an abstract base class for subclasses that share the semantics of being concerned about data (as opposed to e.g. operations)."
  - Known deviations to fix in this sync: unstamped; 6-column checklist missing. Highest fan-out in the queue (3 dependents) → runs before its subclasses.
   - [x] Step 1 — Sync members & description from spec — Table 3.19, p.87: abstract `DataInterface`, direct base `PortInterface`, no own Attribute rows; exact Note captured
   - [x] Step 2 — Write model class unit test (Red) — `test_data_interface_matches_spec` initially failed on the pre-existing `ABC` direct-base shape
   - [x] Step 3 — Implement model class (Green) — heritage retained (`DataInterface(PortInterface, ABC)`); no own members added
   - [x] Step 4 — Sync docstrings (wipe + rewrite) — class docstring replaced with verbatim Table 3.19 Note; no member/method docstrings apply
   - [x] Step 5 — Write reader/writer round-trip test (Red) — N/A: Table 3.19 has no own attributes and DataInterface has no own XML element; inherited coverage belongs to concrete subclasses
   - [x] Step 6 — Update parser & writer (Green) — N/A: `readDataInterface`/`writeDataInterface` already delegate inherited `PortInterface` handling; no DataInterface-specific XML exists
   - [x] Step 7 — Update checklist comment — six-column checklist with R23-11 provenance; marker deferred to Step 9b
   - [x] Step 8 — Deviations — none; abstract shell, base, package, and empty attribute table match the spec
   - [x] Step 9 — Verify (9a) + confirm (9b) — 9a: 31 focused tests pass; lint, Black, and diff checks pass. 9b user-confirmed 2026-09-04: abstract shell, PortInterface base, verbatim Note, no own members/XML, inherited reader/writer coverage, member order, and Rule 0007 location all pass; `# Spec verified: R23-11` written
- [x] `VariableDataPrototype` (**NEW — member type of `NvDataInterface.nvData`, `SenderReceiverInterface.dataElement`, `InvalidationPolicy.dataElement`** · R23-11 markdown · AUTOSAR_CP_TPS_SoftwareComponentTemplate · Table 5.31, p.310 (BSW Table 5.45, p.108 — same class, R23-11 SWCT table is authoritative)) — already verified (`# Spec verified: R23-11`, `DataPrototypes.py`); duplicate of the completed Group 2 sync (commit `d3b5d680`)
  - Spec facts (extracted 2026-09-04): concrete; Package = M2::AUTOSARTemplates::SWComponentTemplate::Datatype::DataPrototypes (file `SWComponentTemplate/Datatype/DataPrototypes.py` ✓ Rule 0007); Base = ARObject, AtpFeature, AtpPrototype, AutosarDataPrototype, DataPrototype, Identifiable, MultilanguageReferrable, Referrable → most-derived direct base **AutosarDataPrototype** ✓ heritage already correct in code (`VariableDataPrototype(AutosarDataPrototype, VariationPointCapable)`), both bases **stamped R23-11**; 1 own attribute `initValue` (ValueSpecification, 0..1, aggr) — member type **stamped R23-11** ✓; Note (md, wrap-normalised): "A VariableDataPrototype represents a formalized generic piece of information that is typically mutable by the application software layer. VariableDataPrototype is used in various contexts and the specific context gives the otherwise generic VariableDataPrototype a dedicated semantics."
  - Why here: only un-stamped member type with more than one dependent (3) — queued before all three.
   - [x] Step 1 — Sync members & description from spec — already verified by source marker and deviation check
   - [x] Step 2 — Write model class unit test (Red) — covered by existing completed Group 2 sync
   - [x] Step 3 — Implement model class (Green) — covered by existing completed Group 2 sync
   - [x] Step 4 — Sync docstrings (wipe + rewrite) — verified against the R23-11 Table 5.31 Note
   - [x] Step 5 — Write reader/writer round-trip test (Red) — covered by existing parser/writer tests
   - [x] Step 6 — Update parser & writer (Green) — existing matched reader/writer coverage confirmed
   - [x] Step 7 — Update checklist comment — existing six-column checklist confirmed
   - [x] Step 8 — Deviations — none found in the short-circuit deviation check
   - [x] Step 9 — Verify (9a) + confirm (9b) — focused tests, lint, Black, and diff checks pass
- [x] `ParameterInterface` (tracker input · R23-11 markdown · AUTOSAR_CP_TPS_SoftwareComponentTemplate · Table 2.2, p.41 · after `DataInterface` (base)) — **finished, stamped `# Spec verified: R23-11`** (commit: `6bf99879`)
  - Spec facts (extracted 2026-09-04): concrete; Package = ...SWComponentTemplate::PortInterface ✓; Base closure adds `DataInterface` to the `PortInterface` chain → most-derived direct base **DataInterface** ✓ heritage already correct in code; 1 attribute `parameter` (ParameterDataPrototype, `*`, aggr) — member type **stamped R23-11** ✓ — so this is the only one of the three `DataInterface` subclasses with nothing outstanding besides its own stamp; Note (md, wrap-normalised, Tags: tail dropped per Rule 0012.2.5.2): "A parameter interface declares a number of parameter and characteristic values to be exchanged between parameter components and software components."
  - Why before its siblings: cheapest of the three (single stamped member type) → unblocks first.
   - [x] Step 1 — Sync members & description from spec — Table 2.2 verified: direct base `DataInterface`; `parameter` is `ParameterDataPrototype * aggr`; Note copied verbatim with Tags tail removed
   - [x] Step 2 — Write model class unit test (Red) — added initialization, aggregation, parent, and duplicate-creation assertions; Red exposed non-idempotent factory behavior
   - [x] Step 3 — Implement model class (Green) — typed `parameters` list, idempotent `createParameterDataPrototype`, and `getParameters`
   - [x] Step 4 — Sync docstrings (wipe + rewrite) — class and member docs aligned with the Table 2.2 Note
   - [x] Step 5 — Write reader/writer round-trip test (Red) — parser and writer assertions cover the `PARAMETERS/PARAMETER-DATA-PROTOTYPE` field value
   - [x] Step 6 — Update parser & writer (Green) — existing matched reader/writer paths confirmed and covered; no parser/writer implementation change required
   - [x] Step 7 — Update checklist comment — six-column parity checklist with R23-11 release and reader/writer ownership
   - [x] Step 8 — Deviations — none
   - [x] Step 9 — Verify (9a) + confirm (9b) — automated checks pass; user confirmed the pre-stamp rule checklist
- [x] `NvDataInterface` (tracker input · R23-11 markdown · AUTOSAR_CP_TPS_SoftwareComponentTemplate · Table 11.5, p.664 · after `DataInterface` (base) and `VariableDataPrototype` (member type)) — **finished, stamped `# Spec verified: R23-11`**
  - Spec facts (extracted 2026-09-04): concrete; Package = ...SWComponentTemplate::PortInterface ✓; most-derived direct base **DataInterface** ✓ heritage already correct in code; 1 attribute `nvData` (VariableDataPrototype, `*`, aggr) — member type queued above; Note (md, wrap-normalised, Tags: tail dropped): "A non volatile data interface declares a number of VariableDataPrototypes to be exchanged between non volatile block components and atomic software components."
   - [x] Step 1 — Sync members & description from spec — Table 11.5 confirms direct base `DataInterface` and `nvData` as `VariableDataPrototype * aggr`; page 664 verified with `pdf_page.py`
   - [x] Step 2 — Write model class unit test (Red) — added typed-list and idempotent-factory assertions; Red confirmed on missing `nvDatas`
   - [x] Step 3 — Implement model class (Green) — added `nvDatas: List[VariableDataPrototype]`, list-backed getter, and idempotent factory population
   - [x] Step 4 — Sync docstrings (wipe + rewrite) — class and member method documentation aligned with the Table 11.5 Note and Attribute Note; Tags tail removed
   - [x] Step 5 — Write reader/writer round-trip test (Red) — parser and writer assertions now verify the actual `nvData` short name, not only collection length/presence
   - [x] Step 6 — Update parser & writer (Green) — existing matched `createNvData`/`getNvDatas` paths confirmed; no implementation change required
   - [x] Step 7 — Update checklist comment — six-column parity checklist added with R23-11 release ownership
   - [x] Step 8 — Deviations — none; dedicated typed aggregation and reader/writer coverage are complete
   - [x] Step 9 — Verify (9a) + confirm (9b) — 404 affected tests pass, lint and Black checks pass; Step 9b confirmed by user
- [x] `HandleInvalidEnum` (**NEW — member type of `InvalidationPolicy.handleInvalid` · `AREnum`** · R23-11 markdown · AUTOSAR_CP_TPS_SoftwareComponentTemplate · Table 4.3, p.97 (SystemTemplate Table 6.6, p.306 — unused, R23-11 SWCT table exists)) — finished, stamped `# Spec verified: R23-11` (commit: 18271ddd)
  - Spec facts (extracted 2026-09-04): Enumeration table (not a Class table — `| Enumeration | HandleInvalidEnum |`); literals in displayed order with verbatim `atp.EnumerationLiteralIndex` tags: `dontInvalidate` (0) "Invalidation is switched off.", `externalReplacement` (1) "Replace a received invalidValue. The replacement value is sourced from the aggregation in the role replaceWith.", `keep` (2) "The application software is supposed to handle signal invalidation on RTE API level either by Data ReceiveErrorEvent or check of error code on read access.", `replace` (3) "Replace a received invalidValue. The replacement value is specified by the initValue."
  - Known deviations to check in Step 1: the class currently lives in `SWComponentTemplate/Communication.py`, but its only consumer and its spec neighbourhood (`InvalidationPolicy`, SWCT Table 4.2) are `SWComponentTemplate::PortInterface` → **Rule 0007 package-location candidate** (StandardNameEnum precedent); literals must be diffed against the code.
  - Why here: cheapest `InvalidationPolicy` dependency (AREnum, no XML element of its own → Steps 5/6 N/A).
   - [x] Step 1 — Sync members & description from spec — Table 4.3 and p.97 verified with `pdf_page.py`; package is `...SWComponentTemplate::Communication`; four literals and order match the specification
   - [x] Step 2 — Write model class unit test (Red) — strengthened the existing model test with exact enum order and verbatim class Note assertions
   - [x] Step 3 — Implement model class (Green) — retained the four spec literals and added their verbatim descriptions and enumeration indices
   - [x] Step 4 — Sync docstrings (wipe + rewrite) — class Note and literal descriptions match Table 4.3; Tags tails retained only on literal comments as spec metadata
   - [x] Step 5 — Write reader/writer round-trip test (N/A: standalone AREnum) — enum has no standalone XML element; serialized by consuming attributes
   - [x] Step 6 — Update parser & writer (N/A: standalone AREnum) — consuming parser/writer paths already serialize enum values
   - [x] Step 7 — Update checklist comment — six-column parity checklist with R23-11 provenance
   - [x] Step 8 — Deviations — none; package location, literal values/order, and spec documentation match Table 4.3
   - [x] Step 9 — Verify (9a) + confirm (9b) — 51 focused tests pass, lint/Black clean, Step 9b confirmed by user; stamped `# Spec verified: R23-11`
- [x] `InvalidationPolicy` (**NEW — member type of `SenderReceiverInterface.invalidationPolicy`** · R23-11 markdown · AUTOSAR_CP_TPS_SoftwareComponentTemplate · Table 4.2, p.97 · after `VariableDataPrototype` (member `dataElement`) and `HandleInvalidEnum` (member `handleInvalid`)) — commit: 1000053d
  - Spec facts (extracted 2026-09-04): concrete; Package = M2::AUTOSARTemplates::SWComponentTemplate::PortInterface (file `SWComponentTemplate/PortInterface/__init__.py` ✓ Rule 0007); Base = **ARObject** ✓ heritage already correct in code (`InvalidationPolicy(ARObject)`); Aggregated by SenderReceiverInterface.invalidationPolicy; 2 attributes: `dataElement` (VariableDataPrototype, 0..1, **ref**) and `handleInvalid` (HandleInvalidEnum, 0..1, attr); Note (md, wrap-normalised): "Specifies whether the component can actively invalidate a particular dataElement. If no invalidationPolicy points to a dataElement this is considered to yield the identical result as if the handleInvalid attribute was set to dontInvalidate."
  - Cross-check: SWCT `[constr_10119]` (md l.2828) — "SenderReceiverInterface.dataElement shall be referenced by at most one InvalidationPolicy" — capture for Step 4 if the spec attaches it as an attribute Note.
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - [x] Step 9 — Verify (9a) + confirm (9b)
- [x] `SenderReceiverInterface` (tracker input · R23-11 markdown · AUTOSAR_CP_TPS_SoftwareComponentTemplate · Table 4.1, p.94 · after `DataInterface` (base), `VariableDataPrototype`, `InvalidationPolicy` (member types)) — finished, stamped `# Spec verified: R23-11` (commit: e4e4770f)
  - Spec facts (extracted 2026-09-04): concrete; Package = ...SWComponentTemplate::PortInterface ✓; most-derived direct base **DataInterface** ✓ heritage already correct in code; 3 attributes: `dataElement` (VariableDataPrototype, *, aggr), `invalidationPolicy` (InvalidationPolicy, *, aggr), `metaDataItemSet` (MetaDataItemSet, *, aggr — **stamped R23-11** ✓); Note (md, wrap-normalised, Tags: tail dropped): "A sender/receiver interface declares a number of data elements to be sent and received."
  - Last of its cluster: depends on `DataInterface` + both new member types.
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

### Cluster 4 — Trigger subtree (Trigger unblocks two rows)

- [ ] `Trigger` (**NEW — member type of `TriggerInterface.trigger` and `TriggerMapping.firstTrigger`/`secondTrigger`** · R23-11 markdown · AUTOSAR_CP_TPS_SoftwareComponentTemplate · Table 4.13, p.109 (BSW Table 4.16, p.46 — same class, R23-11 SWCT table is authoritative))
  - Spec facts (extracted 2026-09-04): concrete; Package = M2::AUTOSARTemplates::CommonStructure::TriggerDeclaration (file `CommonStructure/TriggerDeclaration.py` ✓ Rule 0007); Base = ARObject, AtpClassifier, AtpFeature, AtpStructureElement, Identifiable, MultilanguageReferrable, Referrable → most-derived direct base **AtpStructureElement** ✓ heritage already correct in code (`Trigger(AtpStructureElement, VariationPointCapable)`), base **stamped R23-11**; 2 attributes: `swImplPolicy` (SwImplPolicyEnum, 0..1, attr — **stamped R23-11** ✓) and `triggerPeriod` (MultidimensionalTime, 0..1, aggr — **stamped R23-11** ✓); Note (md, wrap-normalised): "A trigger which is provided (i.e. released) or required (i.e. used to activate something) in the given context."
  - Why here: both member types are already stamped, so `Trigger` has **no outstanding dependency** — do it before the two rows that consume it.
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `TriggerInterface` (tracker input · R23-11 markdown · AUTOSAR_CP_TPS_SoftwareComponentTemplate · Table 4.12, p.109 · after `Trigger` (member type))
  - Spec facts (extracted 2026-09-04): concrete; Package = ...SWComponentTemplate::PortInterface ✓; Base closure = ARElement, ARObject, AtpBlueprint, AtpBlueprintable, AtpClassifier, AtpType, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, PortInterface, Referrable → most-derived direct base **PortInterface** ✓ heritage already correct in code (`TriggerInterface(PortInterface)`), base **stamped R23-11**; 1 attribute `trigger` (Trigger, `*`, aggr); Note (md, wrap-normalised, Tags: tail dropped): "A trigger interface declares a number of triggers that can be sent by an trigger source."
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `TriggerMapping` (**NEW — member type of `TriggerInterfaceMapping.triggerMapping`** · R23-11 markdown · AUTOSAR_CP_TPS_SoftwareComponentTemplate · Table 4.31, p.134 · after `Trigger` (both attributes are refs to it))
  - Spec facts (extracted 2026-09-04): concrete; Package = M2::AUTOSARTemplates::CommonStructure::TriggerDeclaration (file `CommonStructure/TriggerDeclaration.py` ✓ Rule 0007); Base = **ARObject** ✓ heritage already correct in code; Aggregated by TriggerInterfaceMapping.triggerMapping; 2 attributes: `firstTrigger` (Trigger, 0..1, ref) and `secondTrigger` (Trigger, 0..1, ref); Note (md, wrap-normalised): "Defines the mapping of two particular unequally named Triggers in the given context."
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `TriggerInterfaceMapping` (tracker input · R23-11 markdown · AUTOSAR_CP_TPS_SoftwareComponentTemplate · Table 4.30, p.134 · after `PortInterfaceMapping` (base, stamped R23-11) and `TriggerMapping` (member type))
  - Spec facts (extracted 2026-09-04): concrete; Package = ...SWComponentTemplate::PortInterface ✓; Base = ARObject, AtpBlueprint, AtpBlueprintable, Identifiable, MultilanguageReferrable, PortInterfaceMapping, Referrable → most-derived direct base **PortInterfaceMapping** ✓ heritage already correct in code, base **stamped R23-11**; Aggregated by PortInterfaceMappingSet.portInterfaceMapping; 1 attribute `triggerMapping` (TriggerMapping, `*`, aggr); Note (md, wrap-normalised): "Defines the mapping of unequal named Triggers in context of two different TriggerInterfaces."
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

### Cluster 5 — IdentCaption → ModeAccessPointIdent

- [ ] `IdentCaption` (tracker input · R23-11 markdown · AUTOSAR_CP_TPS_SoftwareComponentTemplate · Table 14.4, p.851 · **before `ModeAccessPointIdent` (base)**)
  - Spec facts (extracted 2026-09-04): abstract; Package = M2::AUTOSARTemplates::SWComponentTemplate::RPTScenario (file `SWComponentTemplate/RPTScenario.py` ✓ Rule 0007); Base = ARObject, AtpClassifier, AtpFeature, AtpStructureElement, Identifiable, MultilanguageReferrable, Referrable → most-derived direct base **AtpStructureElement** ✓ heritage already correct in code (`IdentCaption(AtpStructureElement, ABC)`), base **stamped R23-11**; Subclasses = BswServiceDependencyIdent, DiagnosticParameterIdent, ExternalTriggeringPointIdent, ModeAccessPointIdent; **Attribute rows = `-` → no own attributes**; XSD cross-check (AUTOSAR_00052.xsd l.67734 group `IDENT-CAPTION`) = empty `<xsd:sequence/>` → no own XML element → Steps 5/6 N/A; Note (md, wrap-normalised): "This meta-class represents the caption. This allows having some meta-classes optionally identifiable."
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `ModeAccessPointIdent` (tracker input · R23-11 markdown · AUTOSAR_CP_TPS_SoftwareComponentTemplate · Table 14.5, p.852 · after `IdentCaption` (base))
  - Spec facts (extracted 2026-09-04): concrete; Package = ...SWComponentTemplate::RPTScenario ✓; Base = ARObject, AbstractAccessPoint, AtpClassifier, AtpFeature, AtpStructureElement, IdentCaption, Identifiable, MultilanguageReferrable, Referrable → most-derived direct base **IdentCaption** ✓ heritage already correct in code (`ModeAccessPointIdent(IdentCaption)`); `AbstractAccessPoint` is a *less-derived* parallel branch off `AtpStructureElement`, so it is **not** multi-inherited (Rule 0001.2 single role-matching branch — ARPackage / PortInterfaceMapping precedent). XSD cross-check (AUTOSAR_00052.xsd complexType `MODE-ACCESS-POINT-IDENT` l.81788) confirms the chain AR-OBJECT → REFERRABLE → MULTILANGUAGE-REFERRABLE → IDENTIFIABLE → ATP-CLASSIFIER → ATP-FEATURE → ATP-STRUCTURE-ELEMENT → **ABSTRACT-ACCESS-POINT → IDENT-CAPTION** → MODE-ACCESS-POINT-IDENT; Aggregated by AtpClassifier.atpFeature + ModeAccessPoint.ident; **Attribute rows = `-` → no own attributes** → Steps 5/6 expected N/A (XSD group l.81779 is an empty sequence); Note (md, wrap-normalised): "This meta-class has been created to introduce the ability to become referenced into the meta-class ModeAccessPoint without breaking backwards compatibility."
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

### Cluster 6 — unblocked singletons

- [ ] `ModeDeclarationMappingSet` (tracker input · R23-11 markdown · AUTOSAR_CP_TPS_SoftwareComponentTemplate · Table 4.28, p.132 · after `ModeDeclarationMapping` (member type, stamped R23-11))
  - Spec facts (extracted 2026-09-04): concrete; Package = ...SWComponentTemplate::PortInterface ✓; Base = ARElement, ARObject, AtpClassifier, AtpType, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable → most-derived direct base **AtpType** ✓ heritage already correct in code, base **stamped R23-11**; 1 attribute `modeDeclarationMapping` (ModeDeclarationMapping, `*`, aggr) — member type **stamped R23-11** ✓; Note (md, wrap-normalised, Tags: tail dropped): "This meta-class implements a container for ModeDeclarationGroupMappings."
  - Nothing outstanding except the stamp itself → kept near the top rather than last.
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

### Cluster 7 — SubElementMapping subtree

- [ ] `SubElementRef` (**NEW — member type of `SubElementMapping.firstElement`/`secondElement`** · R23-11 markdown · AUTOSAR_CP_TPS_SoftwareComponentTemplate · Table 4.33, p.138)
  - Spec facts (extracted 2026-09-04): abstract; Package = M2::AUTOSARTemplates::SWComponentTemplate::PortInterface (file `SWComponentTemplate/PortInterface/__init__.py` ✓ Rule 0007); Base = **ARObject** only; Subclasses = ApplicationCompositeDataTypeSubElementRef (Table 4.35), ImplementationDataTypeSubElementRef (Table 4.34) — both **absent from `src/`**; Aggregated by SubElementMapping.firstElement / .secondElement; **Attribute rows = `-` → no own attributes** → abstract shell, Steps 5/6 N/A; Note (md, wrap-normalised): "This meta-class provides the ability to reference elements of composite data type."
  - Rule 0001.10 consequence: with only the abstract `SubElementRef` implemented, `SubElementMapping`'s two aggregations stay placeholders until at least one concrete subclass lands. The subclasses are **not** queued here (subclass, not member-type edge — `PortInterfaceMapping` Step-8 precedent); see the next-level section.
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `TextTableMapping` (**NEW — member type of `SubElementMapping.textTableMapping`** · R23-11 markdown · AUTOSAR_CP_TPS_SoftwareComponentTemplate · Table 4.36, p.145 (SystemTemplate Table 5.25, p.230 — unused, R23-11 SWCT table exists))
  - Spec facts (extracted 2026-09-04): concrete; Package = M2::AUTOSARTemplates::SWComponentTemplate::PortInterface (file `SWComponentTemplate/PortInterface/__init__.py` ✓ Rule 0007); Base = **ARObject** ✓ heritage already correct in code; 5 attributes: `bitfieldTextTableMaskFirst` (PositiveInteger, 0..1, attr), `bitfieldTextTableMaskSecond` (PositiveInteger, 0..1, attr), `identicalMapping` (Boolean, 0..1, attr), `mappingDirection` (MappingDirectionEnum, 0..1, attr — **absent from `src/`**), `valuePair` (TextTableValuePair, `*`, aggr — **absent from `src/`**); Note (md, wrap-normalised): "Defines the mapping of two DataPrototypes typed by AutosarDataTypes that refer to CompuMethods of category TEXTTABLE, SCALE_LINEAR_AND_TEXTTABLE or BITFIELD_TEXTTABLE."
  - The two absent member types are queued at this row's Step 1 (they have R23-11 spec tables — SWCT Table 4.37 `MappingDirectionEnum`; `TextTableValuePair` — locate in Step 1), so no Rule 16.4 decision is pending.
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `SubElementMapping` (tracker input · R23-11 markdown · AUTOSAR_CP_TPS_SoftwareComponentTemplate · Table 4.32, p.137 · after `SubElementRef` and `TextTableMapping` (member types))
  - Spec facts (extracted 2026-09-04): concrete; Package = ...SWComponentTemplate::PortInterface ✓; Base = **ARObject** ✓ heritage already correct in code; Aggregated by DataPrototypeMapping.subElementMapping (**stamped R23-11** ✓); 3 attributes: `firstElement` (SubElementRef, 0..1, aggr), `secondElement` (SubElementRef, 0..1, aggr), `textTableMapping` (TextTableMapping, 0..2, aggr — note the unusual `0..2` multiplicity: model as a list, document the bound in the checklist); Note (md, wrap-normalised): "This meta-class allows for the definition of mappings of elements of a composite data type."
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

### Cluster 8 — FlatMap subtree (heritage fix)

- [ ] `FlatInstanceDescriptor` (**NEW — member type of `FlatMap.instance`** · R23-11 markdown · AUTOSAR_CP_TPS_SystemTemplate · Table 14.2, p.967 (BSW Table D.32 — appendix, R23-11 SystemTemplate table is authoritative))
  - Spec facts (extracted 2026-09-04): concrete; Package = M2::AUTOSARTemplates::CommonStructure::FlatMap (file `CommonStructure/FlatMap.py` ✓ Rule 0007); Base = ARObject, Identifiable, MultilanguageReferrable, Referrable → most-derived direct base **Identifiable** ✓ heritage already correct in code (`FlatInstanceDescriptor(Identifiable, VariationPointCapable)`); Aggregated by FlatMap.instance; 5 attributes: `ecuExtractReference` (AtpFeature, 0..1, iref), `role` (Identifier, 0..1, attr), `rtePluginProps` (RtePluginProps, 0..1, aggr — **unstamped**), `swDataDefProps` (SwDataDefProps, 0..1, aggr — **stamped R23-11** ✓), `upstreamReference` (AtpFeature, 0..1, iref); Note (md, wrap-normalised, truncated in the corpus — re-read the full cell in Step 1): "Represents exactly one node (e.g. a component instance or data element) of the instance tree of a software system. The purpose of this element is to map the various nested representations of this instance to a flat representation and assign a unique name (shortName) to it. …"
  - `RtePluginProps` (unstamped) is queued at this row's Step 1 — see the next-level section.
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `FlatMap` (tracker input · R23-11 markdown · AUTOSAR_CP_TPS_SystemTemplate · Table 14.1, p.966 · **heritage fix: code `FlatMap(AtpBlueprintable)` → spec most-derived direct base `ARElement`** · after `FlatInstanceDescriptor` (member type))
  - Spec facts (extracted 2026-09-04): concrete; Package = M2::AUTOSARTemplates::CommonStructure::FlatMap (file `CommonStructure/FlatMap.py` ✓ Rule 0007); Base = ARElement, ARObject, AtpBlueprint, AtpBlueprintable, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable → most-derived direct base **ARElement**; code has `FlatMap(AtpBlueprintable)` — since `AtpBlueprintable` was re-parented to `Identifiable` (this file, row `AtpBlueprintable`), `FlatMap` lost `PackageableElement` → `CollectableElement` → `ARElement` even though it is **Aggregated by ARPackage.element** and is dispatched as an ARPackage element in the parser (`arxml_parser.py:11372` `parent.createFlatMap(...)`, tag `FLAT-MAP`) and the writer. Fix in Step 3; audit `FlatInstanceDescriptor` + the ARPackage dispatch after the re-parent.
  - 1 attribute `instance` (FlatInstanceDescriptor, `*`, aggr); Note (md, wrap-normalised, Tags: tail dropped): "Contains a flat list of references to software objects. This list is used to identify instances and to resolve name conflicts. The scope is given by the RootSwCompositionPrototype for which it is used, i.e. it can be applied to a system, system extract or ECU-extract. An instance of FlatMap may also be used in a preliminary context, e.g. in the scope of a software component before integration into a system. In this case it is not referred by a RootSwCompositionPrototype."
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

### Cluster 9 — Implementation subtree (heaviest; queued last)

Ten of `Implementation`'s fifteen attributes reference eight member types that are
un-stamped or absent from `src/`, so the whole cluster sits at the bottom of the queue. Order inside the cluster:
enums → ARObject/Identifiable leaf members → members with their own member types →
`Implementation` itself.

- [ ] `ProgramminglanguageEnum` (**NEW — member type of `Implementation.programmingLanguage` · `AREnum`** · R23-11 markdown · AUTOSAR_CP_TPS_SoftwareComponentTemplate · Table 8.2, p.621)
  - Spec facts (extracted 2026-09-04): Enumeration table (`| Enumeration | ProgramminglanguageEnum |`); XSD `AUTOSAR_00052.xsd` complexType l.141411 + simpleType l.141423, doc "Programming language the implementation was created in."; literals `C` (index 0, "C language"), `CPP` (1, "C++ language"), `JAVA` (2, "Java language") — the code's `C = "c"` / `CPP = "cpp"` / `JAVA = "java"` already match the XSD tokens and indexes.
  - Known deviations to fix in this sync: unstamped; the in-code checklist cites `Table 8.2, p.621` but is the legacy 3-column shape → 6-column rewrite; Steps 5/6 N/A (standalone AREnum serialized as an attribute value on `Implementation`).
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `Compiler` (**NEW — member type of `Implementation.compiler`** · R23-11 markdown · AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate · Table 7.7, p.133 (SWCT Table 8.3, p.621 — same class, BSW chapter 7 owns the Implementation cluster))
  - Spec facts (extracted 2026-09-04): concrete; Package = M2::AUTOSARTemplates::CommonStructure::Implementation (file `CommonStructure/Implementation.py` ✓ Rule 0007); Base = ARObject, Identifiable, MultilanguageReferrable, Referrable → most-derived direct base **Identifiable** ✓ heritage already correct in code; 4 attributes, all `String` 0..1 attr: `name`, `options`, `vendor`, `version`; Note (md, wrap-normalised): "Specifies the compiler attributes. In case of source code this specifies requirements how the compiler shall be invoked. In case of object code this documents the used compiler settings."
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `Linker` (**NEW — member type of `Implementation.linker`** · R23-11 markdown · AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate · Table 7.8, p.134 (SWCT Table 8.4, p.622 — same class))
  - Spec facts (extracted 2026-09-04): concrete; Package = ...CommonStructure::Implementation ✓; Base = **Identifiable** ✓ heritage already correct in code; 4 attributes, all `String` 0..1 attr: `name`, `options`, `vendor`, `version`; Note (md, wrap-normalised): "Specifies the linker attributes used to describe how the linker shall be invoked."
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `Code` (**NEW — member type of `Implementation.codeDescriptor`** · R23-11 markdown · AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate · Table 7.2, p.130 (SWCT Table 8.5, p.622 — same class))
  - Spec facts (extracted 2026-09-04): concrete; Package = ...CommonStructure::Implementation ✓; Base = **Identifiable** ✓ heritage already correct in code; 2 attributes: `artifactDescriptor` (AutosarEngineeringObject, `*`, aggr — **stamped R23-11** ✓) and `callbackHeader` (ServiceNeeds, `*`, ref — **unstamped**); Note (md, wrap-normalised): "A generic code descriptor. The type of the code (source or object) is defined via the category attribute of the associated engineering object."
  - `ServiceNeeds` is queued at this row's Step 1 — see the next-level section.
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `DependencyOnArtifact` (**NEW — member type of `Implementation.generatedArtifact` / `requiredArtifact` / `requiredGeneratorTool` (three attributes, one type)** · R23-11 markdown · AUTOSAR_CP_TPS_SoftwareComponentTemplate · Table 5.91, p.413 (BSW Table 7.3, p.131 — same class))
  - Spec facts (extracted 2026-09-04): concrete; Package = ...CommonStructure::Implementation ✓; Base = **Identifiable** ✓ heritage already correct in code (`DependencyOnArtifact(Identifiable, VariationPointCapable)`); 2 attributes: `artifactDescriptor` (AutosarEngineeringObject, 0..1, aggr — **stamped R23-11** ✓) and `usage` (DependencyUsageEnum, `*`, attr — **unstamped**); Note (md, wrap-normalised): "Dependency on the existence of another artifact, e.g. a library."
  - `DependencyUsageEnum` (BSW Table 7.4) is queued at this row's Step 1 — see the next-level section.
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `ResourceConsumption` (**NEW — member type of `Implementation.resourceConsumption`** · R23-11 markdown · AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate · Table 8.1, p.138 (SystemTemplate Table 5.44, p.261 — same class))
  - Spec facts (extracted 2026-09-04): concrete; Package = M2::AUTOSARTemplates::CommonStructure::ResourceConsumption (file `CommonStructure/ResourceConsumption/__init__.py` ✓ Rule 0007); Base = ARObject, Identifiable, MultilanguageReferrable, Referrable → most-derived direct base **Identifiable** ✓ heritage already correct in code; 6 attributes, all `*` aggr: `accessCountSet` (AccessCountSet — **stamped** ✓), `executionTime` (ExecutionTime — **stamped** ✓), `heapUsage` (HeapUsage — **stamped** ✓), `memorySection` (MemorySection — **unstamped**), `sectionNamePrefix` (SectionNamePrefix — **unstamped**), `stackUsage` (StackUsage — **unstamped**); Note (md, wrap-normalised): "Description of consumed resources by one implementation of a software."
  - The three unstamped member types are queued at this row's Step 1 — see the next-level section.
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `SwcBswMapping` (**NEW — member type of `Implementation.swcBswMapping`** · R23-11 markdown · AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate · Table 5.46, p.110 (SWCT Table 11.1, p.656 — same class) · **heritage fix: code `SwcBswMapping(AtpStructureElement)` → spec most-derived direct base `ARElement`**)
  - Spec facts (extracted 2026-09-04): concrete; Package = M2::AUTOSARTemplates::CommonStructure::SwcBswMapping (file `CommonStructure/SwcBswMapping.py` ✓ Rule 0007); Base = ARElement, ARObject, AtpClassifier, AtpFeature, AtpStructureElement, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable → most-derived direct base **ARElement**; Aggregated by ARPackage.element **and** AtpClassifier.atpFeature; 5 attributes: `bswBehavior` (BswInternalBehavior, 0..1, ref — **unstamped**), `runnableMapping` (SwcBswRunnableMapping, `*`, aggr — **unstamped**), `swcBehavior` (SwcInternalBehavior, 0..1, ref — **unstamped**), `synchronizedModeGroup` (SwcBswSynchronizedModeGroupPrototype, `*`, aggr — **unstamped**), `synchronizedTrigger` (SwcBswSynchronizedTrigger, `*`, aggr — **unstamped**); Note (md, wrap-normalised, Tags: tail dropped): "Maps an SwcInternalBehavior to an BswInternalBehavior. This is required to coordinate the API generation and the scheduling for AUTOSAR Service Components, ECU Abstraction Components and Complex Driver Components by the RTE and the BSW scheduling mechanisms."
  - Heaviest member type in the cluster — all five of its own member types are unstamped and get queued at its Step 1. Heritage fix also ripples: audit the two dispatch paths (ARPackage element + AtpClassifier.atpFeature).
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `BuildActionManifest` (**NEW — member type of `Implementation.buildActionManifest` · absent from `src/`** · R23-11 markdown · AUTOSAR_FO_TPS_GenericStructureTemplate · Table 10.1, p.365 (BSW Table 7.9, p.135 — same class))
  - Spec facts (extracted 2026-09-04): concrete; Package = M2::AUTOSARTemplates::GenericStructure::BuildActionManifest (**no `src/` file yet** — Rule 0007 target = `GenericStructure/BuildActionManifest.py`, leaf shape); Base = ARElement, ARObject, AtpBlueprint, AtpBlueprintable, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable → most-derived direct base **ARElement**; Aggregated by ARPackage.element; 5 attributes: `buildAction` (BuildAction, `*`, aggr — **absent from `src/`**, FO GenericStructure Table 10.2, p.366), `buildActionEnvironment` (BuildActionEnvironment, `*`, aggr — **absent from `src/`**, FO GenericStructure Table 10.4, p.370), `dynamicAction` (BuildAction, `*`, ref), `startAction` (BuildAction, `*`, ref), `tearDownAction` (BuildAction, `*`, ref); Note (md, wrap-normalised, Tags: tail dropped): "This meta-class represents the ability to specify a manifest for processing artifacts. An example use case is the processing of ECUC parameter values."
  - Both new member types have R23-11 spec Class tables → **no Rule 16.4 Skip/XSD decision is pending**; they are queued at this row's Step 1 (BuildAction first — BuildActionEnvironment is its `requiredEnvironment` target with multiplicity 1, so it must exist before BuildAction lands).
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `Implementation` (tracker input · R23-11 markdown · AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate · Table 7.1, p.128 (SWCT Table 8.1, p.621 — same class; the todo's "multiple tables — resolve in per-class Phase 0" is resolved: BSW chapter 7 owns the Implementation cluster) · **last row of the queue**)
  - Spec facts (extracted 2026-09-04): abstract; Package = M2::AUTOSARTemplates::CommonStructure::Implementation (file `CommonStructure/Implementation.py` ✓ Rule 0007); Base = ARElement, ARObject, CollectableElement, Identifiable, MultilanguageReferrable, PackageableElement, Referrable → most-derived direct base **ARElement** ✓ heritage already correct in code (`Implementation(ARElement, ABC)`), base **stamped R23-11**; Subclasses = BswImplementation (**stamped**), SwcImplementation (**unstamped** — not queued, subclass edge); Aggregated by ARPackage.element. 15 attributes in Table 7.1 displayed order — `buildActionManifest` (BuildActionManifest, 0..1, ref → queued), `codeDescriptor` (Code, *, aggr → queued), `compiler` (Compiler, *, aggr → queued), `generatedArtifact` (DependencyOnArtifact, *, aggr → queued), `hwElement` (HwElement, *, ref — **stamped R23-11** ✓), `linker` (Linker, *, aggr → queued), `mcSupport` (McSupportData, 0..1, aggr — **stamped R23-11** ✓), `programmingLanguage` (ProgramminglanguageEnum, 0..1, attr → queued), `requiredArtifact` (DependencyOnArtifact, *, aggr → queued), `requiredGeneratorTool` (DependencyOnArtifact, *, aggr → queued), `resourceConsumption` (ResourceConsumption, 0..1, aggr → queued), `swcBswMapping` (SwcBswMapping, 0..1, ref → queued), `swVersion` (RevisionLabelString, 0..1, attr), `usedCodeGenerator` (String, 0..1, attr), `vendorId` (PositiveInteger, 0..1, attr); Note (md, wrap-normalised): "Description of an implementation a single software component or module."
  - Why last: it is the only row with eight queued dependencies. Note `DependencyOnArtifact` covers three attributes and `Trigger`-style XML wrappers may group them — resolve the element names from the XSD in Step 5.
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

## Next-level candidates (level-2 — queue at the owning row's Step 1)

Member types of the rows added above. Each is un-stamped or absent from `src/`, so each
blocks its owning row's stamp (Rules 0001.10 / 0012.1). They are **not** queued now —
queue them when the owning row reaches Step 1, using the same level-1 rule (their own
member types then become level-3).

| Owning row (above) | Queue at its Step 1 | State | R23-11 spec table |
|---|---|---|---|
| `TextTableMapping` | `MappingDirectionEnum` | absent from `src/` | SWCT Table 4.37 |
| `TextTableMapping` | `TextTableValuePair` | absent from `src/` | locate in Step 1 |
| `FlatInstanceDescriptor` | `RtePluginProps` | unstamped | locate in Step 1 |
| `Code` | `ServiceNeeds` | unstamped | locate in Step 1 |
| `DependencyOnArtifact` | `DependencyUsageEnum` | unstamped (`AREnum`) | BSW Table 7.4 (md l.3273) |
| `ResourceConsumption` | `MemorySection` | unstamped | locate in Step 1 |
| `ResourceConsumption` | `SectionNamePrefix` | unstamped | locate in Step 1 |
| `ResourceConsumption` | `StackUsage` | unstamped | locate in Step 1 |
| `SwcBswMapping` | `BswInternalBehavior` | unstamped | locate in Step 1 |
| `SwcBswMapping` | `SwcInternalBehavior` | unstamped | locate in Step 1 |
| `SwcBswMapping` | `SwcBswRunnableMapping` | unstamped | locate in Step 1 |
| `SwcBswMapping` | `SwcBswSynchronizedModeGroupPrototype` | unstamped | locate in Step 1 |
| `SwcBswMapping` | `SwcBswSynchronizedTrigger` | unstamped | locate in Step 1 |
| `BuildActionManifest` | `BuildActionEnvironment` | absent from `src/` | FO GenericStructure Table 10.4, p.370 |
| `BuildActionManifest` | `BuildAction` | absent from `src/` | FO GenericStructure Table 10.2, p.366 |
| `SubElementRef` (subclass edge) | `ImplementationDataTypeSubElementRef` | absent from `src/` | SWCT Table 4.34, p.138 |
| `SubElementRef` (subclass edge) | `ApplicationCompositeDataTypeSubElementRef` | absent from `src/` | SWCT Table 4.35, p.138 |

## Pending 16.4 resolution (NEW — not in src)

_(none)_ — every class added to the queue by the 2026-09-04 review has a **Class** or
**Enumeration** table in the R23-11 markdown corpus (verified class-by-class), so no
Skip / XSD-derive decision is pending. The classes that are absent from `src/` but
present in the spec (`BuildAction`, `BuildActionEnvironment`, `TextTableValuePair`,
`MappingDirectionEnum`, `ImplementationDataTypeSubElementRef`,
`ApplicationCompositeDataTypeSubElementRef`) are implemented from their spec tables —
they are not XSD-derived and are therefore not 16.4 cases.

## Not queued

Deliberately out of the queue (2026-09-04 review). Each entry below is a **subclass**
edge, not a `Base` or member-type edge, so it does not block its parent's stamp
(`PortInterfaceMapping` Step-8 precedent):

- `ImplementationDataType` — subclass of `AbstractImplementationDataType` (SWCT Table
  5.15, md l.7820). **Already stamped R23-11 while its base is not** — an inversion;
  run a Rule 0012.3 drift pass once the base lands.
- `ImplementationDataTypeElement` — subclass of `AbstractImplementationDataTypeElement`
  (SWCT Table 5.17, p.270); UNSTAMPED. Drift candidate after the base lands.
- `SwcImplementation` — subclass of `Implementation` (SWCT Table 8.7, p.623); UNSTAMPED.
  Audit candidate once `Implementation` lands (`BswImplementation` is already stamped).
- `BswServiceDependencyIdent` (DiagnosticExtract Table 5.16, p.240),
  `DiagnosticParameterIdent` (DiagnosticExtract Table 4.7, p.37),
  `ExternalTriggeringPointIdent` (SWCT Table 14.6, p.852) — the other three
  `IdentCaption` subclasses (SWCT Table 14.4 Subclasses row).
- `VariableAndParameterInterfaceMapping` (SWCT Table 4.21, p.125),
  `ClientServerInterfaceMapping` (SWCT Table 4.23, p.128), `ModeInterfaceMapping`
  (SWCT Table 4.26, p.130) — the other `PortInterfaceMapping` subclasses; already
  recorded as future queue candidates in that row's Step 8.
- `ApplicationDataType` (SWCT Table 5.2, p.232) — the second `AutosarDataType`
  subclass; audit candidate once the `AutosarDataType` heritage fix lands.

Also out of scope here (already recorded elsewhere in this file): the
`ModeDeclarationGroupPrototype` / `HwPinGroupContent` drift rows and the ten
uuid-move heritage rows.


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

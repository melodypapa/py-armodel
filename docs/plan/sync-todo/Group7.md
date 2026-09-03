# Sync todo: Group 7 — ECU resource, Crypto/IDS, DoIP, Firewall, remaining

Input: `Group 7 — ECU resource, Crypto/IDS, DoIP, Firewall, remaining` of `docs/examples/sync_class_groups.md` · Generated: 2026-08-30 · Queue order = row order
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

> **Moved:** `HwPin`, `HwPinGroup`, `HwType`, `HwElement`, `FirewallRule`, `StateDependentFirewall` — wrong-heritage uuid-move blockers — moved into `Group1.md` ahead of the `Identifiable` row
> (dependency-first: the uuid move cannot run until they derive from `Identifiable`).

- [ ] `HwAttributeDef` (tracker input · R23-11 markdown · AUTOSAR_CP_TPS_ECUResourceTemplate · Table 2.13 · *(existing member)*)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `HwCategory` (tracker input · R23-11 markdown · AUTOSAR_CP_TPS_ECUResourceTemplate · Table 2.11 · after `HwAttributeDef` (aggr `hwAttributeDef`))
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `HwAttributeValue` (tracker input · R23-11 markdown · AUTOSAR_CP_TPS_ECUResourceTemplate · Table 2.2)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `HwAttributeLiteralDef` (tracker input · R23-11 markdown · AUTOSAR_CP_TPS_ECUResourceTemplate · Table 2.14)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `CryptoKeySlot` (tracker input · no R23-11/R4.3.1 table found → XSD-only candidate (confirm in per-class Phase 0))
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `AbstractDoIpLogicAddressProps` (tracker input · R23-11 markdown · AUTOSAR_CP_TPS_SystemTemplate · Table 6.208)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `DoIpLogicTargetAddressProps` (tracker input · R23-11 markdown · AUTOSAR_CP_TPS_SystemTemplate · Table 6.209)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `DoIpLogicTesterAddressProps` (tracker input · R23-11 markdown · AUTOSAR_CP_TPS_SystemTemplate · Table 6.210)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `DoIpTpConfig` (tracker input · R23-11 markdown · AUTOSAR_CP_TPS_SystemTemplate · Table 6.205 · after the DoIp props classes)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [x] `FirewallRuleProps` (tracker input · R23-11 markdown · AUTOSAR_CP_TPS_SystemTemplate · Table 6.235, p.584 (pdf_page.py verified) · after `FirewallRule` (ref target of its `matchingEgressRule`/`matchingIngressRule`) · spec facts (extracted 2026-08-31 from markdown l.15333-15342): Note = "Firewall rule that is defined by an action that is performed if the referenced pattern matches."; Base = ARObject; Aggregated by = StateDependentFirewall.firewallRuleProps (* aggr); 3 attributes: `action` (FirewallActionEnum, 0..1, attr — "Action that is performed by the firewall if the matching Rule is fulfilled."), `matchingEgressRule` (ordered) (FirewallRule, *, ref — "This element defines an egress rule expression against which the network traffic is matched."), `matchingIngressRule` (ordered) (FirewallRule, *, ref — "This element defines an ingress rule expression against which the network traffic is matched."))
  - [x] Step 1 — Sync members & description from spec — DONE with StateDependentFirewall batch 2026-08-31 (dependency-first: StateDependentFirewall.firewallRuleProps requires this class)
  - [x] Step 2 — Write model class unit test (Red) — test___init__.py TestFirewallRuleProps: defaults, action get/set, matchingEgressRuleRef/IngressRuleRef add/get, verbatim docstring
  - [x] Step 3 — Implement model class (Green) — fabricated allowAny/direction/protocol replaced with 3 spec attributes
  - [x] Step 4 — Sync docstrings (wipe + rewrite) — verbatim Table 6.235 Notes
  - [x] Step 5 — Write reader/writer round-trip test (Red) — covered by TestStateDependentFirewallReadWrite.test_round_trip (FIREWALL-RULE-PROPS written inside FIREWALL-RULE-PROPSS wrapper)
  - [x] Step 6 — Update parser & writer (Green) — writeFirewallRuleProps/readFirewallRuleProps (ACTION + MATCHING-EGRESS-RULE-REFS + MATCHING-INGRESS-RULE-REFS)
  - [x] Step 7 — Update checklist comment — 6-col parity checklist all [x]
  - [x] Step 8 — Deviations — none beyond FirewallActionEnum derivation (see below)
  - [x] Step 9 — Verify (9a) + confirm (9b) — 9a: 8307 tests pass, ruff/flake8 clean, black clean; **unstamped** per user decision 2026-08-31 (batch confirmation deferred)
- [ ] `IdsPlatformInstantiation` (tracker input · no R23-11/R4.3.1 table found → XSD-only candidate (confirm in per-class Phase 0))
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `IdsmModuleInstantiation` (tracker input · no R23-11/R4.3.1 table found → XSD-only candidate (confirm in per-class Phase 0))
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `PlatformModuleEthernetEndpointConfiguration` (tracker input · no R23-11/R4.3.1 table found → XSD-only candidate (confirm in per-class Phase 0))
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `ECUMapping` (tracker input · R23-11 markdown · AUTOSAR_CP_TPS_SystemTemplate · Table 3.133 · after both NEW classes above (aggrs))
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `VariableDataPrototypeInSystemInstanceRef` (tracker input · no R23-11/R4.3.1 table found → XSD-only candidate (confirm in per-class Phase 0))
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `ComponentInSystemInstanceRef` (tracker input · no R23-11/R4.3.1 table found → XSD-only candidate (confirm in per-class Phase 0))
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `PortPrototypeBlueprintInitValue` (tracker input · R23-11 markdown · AUTOSAR_FO_TPS_StandardizationTemplate · Table 4.10 · *(existing member)*)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `PortPrototypeBlueprint` (tracker input · R23-11 markdown · AUTOSAR_FO_TPS_StandardizationTemplate · Table 4.9 · after `PortPrototypeBlueprintInitValue` (aggr `initValue`))
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `Keyword` (tracker input · R4.3.1 markdown · AUTOSAR_TPS_StandardizationTemplate · Table 6.2 · *(existing member)*)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `KeywordSet` (tracker input · R4.3.1 markdown · AUTOSAR_TPS_StandardizationTemplate · Table 6.1 · after `Keyword` (aggr `keyword`))
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `DiagnosticServiceTable` (tracker input · R23-11 markdown · AUTOSAR_CP_TPS_DiagnosticExtractTemplate · Table 4.16 · after `DiagnosticServiceInstance` (ref `serviceInstance`))
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] `DiagnosticCommonElement` (tracker input · R23-11 markdown · AUTOSAR_CP_TPS_DiagnosticExtractTemplate · Table 4.1)
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

- [x] `FirewallActionEnum` — not in `src` (NEW) → **Derive-from-XSD DONE 2026-08-31** (XSD FIREWALL-ACTION-ENUM complexType: literals BLOCK index 0 "Firewall blocks the communication" / ALLOW index 1 "Firewall allows the communication"; AREnum subclass in Firewall/__init__.py, `# XSD` spec line in checklist; unstamped per user decision 2026-08-31)
- `CommunicationControllerMapping` — not in `src` (NEW) · R23-11 markdown · Table 3.134 · **(NEW)**; 16.4 decision required: **Skip** (deviation row) or **Derive-from-XSD** (then move into the queue with a 9-step sub-checklist)
- `HwPortMapping` — not in `src` (NEW) · R23-11 markdown · Table 3.135 · **(NEW)**; 16.4 decision required: **Skip** (deviation row) or **Derive-from-XSD** (then move into the queue with a 9-step sub-checklist)
- `DiagnosticServiceInstance` — not in `src` (NEW) · R23-11 markdown · Table 4.26 · **(NEW)**; 16.4 decision required: **Skip** (deviation row) or **Derive-from-XSD** (then move into the queue with a 9-step sub-checklist)

## Not queued

_(none)_

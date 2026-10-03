# Sync todo: Group 16 — Ethernet Fibex

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

> **Parent-dependency audit 2026-09-26 (all Group1-20 pending rows, spec-table Base chains):** every pending row's Base row extracted from the R23-11/R4.3.1 markdown (260/293 found; 33 = enums/XSD-only/user-arbitrated) and every parent classified against src stamps + the queue. Findings: DiagnosticEnvCompareCondition (Group14) and MixedContentForUnitNames (Group8) queued NEW above their children; DiagnosticEnvModeElement row-header Base corrected. ESTABLISHED SKIPS (no rows, per precedent): UploadableDesignElement / UploadablePackageElement (attribute-less abstract bases, empty XSD groups — most-derived-base collapse, Group5-audit precedent; appear in Base cells of InitialSdDelayConfig / MacMulticastGroup rows below); AREnum leaf classes (no Base row by construction); the Firewall member-rule family (user arbitration 2026-08-31: no Class table in either corpus → skipped, see Group1 FirewallRule Done row); ARList (resolved under "List", FO GST Table 9.8, Group9 row).

## Queue (dependency-first)

- [ ] `RuntimeAddressConfigurationEnum` — AREnum — R4.3.1 markdown · Table 6.121 (TPS_SystemTemplate), p.320 — commit c5bb32232
  - commit: c5bb32232 (feat; steps 1-8; verbatim Note + attr notes, PEP 526 types, None-no-op accessors, 6-col checklist) — class body already spec-faithful (prior unstamped sync) — 6-col checklist + mirror test added
  - [—] Step 5 — N/A standalone enum
  - [—] Step 6 — N/A standalone enum
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations — see feat note above
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-28 (6771 passed / 0 failed battery, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

- [ ] `IpAddressKeepEnum` — AREnum — R23-11 markdown · Table 6.138 (CP_TPS_SystemTemplate), p.466 — commit c5bb32232
  - commit: c5bb32232 (feat; steps 1-8; verbatim Note + attr notes, PEP 526 types, None-no-op accessors, 6-col checklist) — class body already spec-faithful — 6-col checklist + mirror test added
  - [—] Step 5 — N/A standalone enum
  - [—] Step 6 — N/A standalone enum
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations — see feat note above
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-28 (6771 passed / 0 failed battery, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

- [ ] `Ipv6AddressSourceEnum` — AREnum — R23-11 markdown · Table 6.140 (CP_TPS_SystemTemplate), p.467 — commit c5bb32232
  - commit: c5bb32232 (feat; steps 1-8; verbatim Note + attr notes, PEP 526 types, None-no-op accessors, 6-col checklist) — literal value fixed LinkLocalDoIP → linkLocal_doip (markdown literal; XSD 00052 token LINK-LOCAL--DOIP deviates, md-primary per Rule 0015)
  - [—] Step 5 — N/A standalone enum
  - [—] Step 6 — N/A standalone enum
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations — see feat note above
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-28 (6771 passed / 0 failed battery, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

- [ ] `Ipv4AddressSourceEnum` — AREnum — R23-11 markdown · Table 6.137 (CP_TPS_SystemTemplate), p.465 — commit 6c97ddc10
  - commit: 6c97ddc10 (feat; steps 1-8; verbatim Note + attr notes, PEP 526 types, None-no-op accessors, 6-col checklist) — queue-row add-back 2026-09-28 (class synced in the same commit as Ipv4Configuration/NetworkEndpoint but the row was omitted from this queue; member type of Ipv4Configuration.ipv4AddressSource — its row notes "ipv4AddressSource now typed Ipv4AddressSourceEnum"; Group6 pending-resolution note lists it too) — class body carries `# Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.137, p.465` checklist, NO `# Spec verified:` yet
  - [—] Step 5 — N/A standalone enum
  - [—] Step 6 — N/A standalone enum
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations — see feat note above (literal AUTO_IP_DOIP = autoIp_doip; mirror test test_Ipv4AddressSourceEnum.py)
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `DoIpEntity` — ARObject — R23-11 markdown · Table 6.150 (CP_TPS_SystemTemplate), p.471 — commit b1e4750b1
  - commit: b1e4750b1 (feat; steps 1-8; verbatim Note + attr notes, PEP 526 types, None-no-op accessors, 6-col checklist) — verbatim Note + typed doIpEntityRole; rw (getDoIpEntity/setDoIpEntity) already complete
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations — see feat note above
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-28 (6771 passed / 0 failed battery, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

- [ ] `TpPort` — ARObject — R23-11 markdown · Table 6.133 (CP_TPS_SystemTemplate), p.461 — commit b1e4750b1
  - commit: b1e4750b1 (feat; steps 1-8; verbatim Note + attr notes, PEP 526 types, None-no-op accessors, 6-col checklist) — verbatim Note + 2 attr notes (dynamicallyAssigned carries atp.Status=obsolete tag verbatim); rw via getTpPort/setTpPort complete
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations — see feat note above
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-28 (6771 passed / 0 failed battery, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

- [x] `InitialSdDelayConfig` — ARObject — R23-11 markdown · Table 6.170 (CP_TPS_SystemTemplate), p.514 — commit 84dc59b64 (# Spec verified: R23-11, stamped 2026-10-03; Rule 0007 fix — relocated into `…::Fibex4Ethernet::ServiceInstances`)
  - re-sync pass: Rule 0007 fix — spec Package is `…::Fibex4Ethernet::ServiceInstances`, so the class is relocated out of EthernetTopology.py into ServiceInstances.py (user-approved). The d7240be74 dedup had kept the wrong carrier.
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red) — `test_InitialSdDelayConfig.py` rewritten; 1 failed (`test_defined_in_spec_package`: `__module__` == EthernetTopology), 7 passed
  - [x] Step 3 — Implement model class (Green) — class moved to ServiceInstances.py (before RequestResponseDelay); removed from EthernetTopology.py; its `InitialSdDelayConfig` reference is now TYPE_CHECKING-only (same as the pre-existing RequestResponseDelay); parser/writer + all 5 consumer test modules repointed (`test_InitialSdDelayConfig`, `test_ServiceInstances`, `test_EthernetTopology`, `test_sd_client_config`, `test_writer_frame_channel` — the last two found by the full-suite run, not the initial grep). 8 passed
  - [x] Step 4 — Sync docstrings (wipe + rewrite) — all docstrings/member comments wiped (verified `__doc__ is None` for class + 9 methods), then rewritten programmatically from the markdown Table 6.170 cells; every class/`__init__`/getter/setter text diffed char-for-char against the markdown Note — clean; `__init__` has no docstring; 8 passed
  - [x] Step 5 — Write reader/writer round-trip test (Red) — new `tests/test_armodel/parser/test_initial_sd_delay_config.py` (`TestInitialSdDelayConfigReader`) + `tests/test_armodel/writer/test_initial_sd_delay_config.py` (`TestInitialSdDelayConfigWriter`/`RoundTrip`); all 4 attrs asserted by value through the 3 existing aggregators. RED: reader 1 failed / 6 passed (S/T not read); writer 2 failed / 5 passed (S/T not written) — the helper never calls `readARObject`/`writeARObject` (direct base ARObject, XSD `AR:AR-OBJECT` attributeGroup l.4900)
  - [x] Step 6 — Update parser & writer (Green) — added `self.readARObject(child_element, config)` (parser l.10173) and `self.writeARObject(child_element, config)` (writer l.10226) so the ARObject-level `S`/`T` attributes are no longer dropped; 4 attrs already covered in both directions inside the helper (parser l.10174-10177 setters, writer l.10227-10230 getters) and all 3 existing aggregators call it. No chained mutator calls in touched lines. 304 passed
  - [x] Step 7 — Update checklist comment — 6-column block, 9 rows in source order, `[x]` impl/docstring/test on every row, reader `[x]` on the 4 setters, writer `[x]` on the 4 getters, `[—]` on `__init__`; `# Spec:` corrected to `AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.170, p.514` (dropped the Rule-0019-only `(R23-11)` suffix). NO `# Spec verified:` marker written (9b gate)
  - [x] Step 8 — Deviations — no open deviation. Recorded in `docs/examples/method_deviation_by_class.md` (`## InitialSdDelayConfig`, "No deviations" row + Note). Rule 0001.10 report: `SomeipSdServerServiceInstanceConfig` (4th `Aggregated by` parent) is a misplaced stub in `GenericStructure/GeneralTemplateClasses/ArObject.py` with no parser/writer handler — own sync needed; sibling SD-config helpers also miss the `readARObject`/`writeARObject` pair (to reconcile in their own passes)
  - [x] Step 9 — Verify (9a) + confirm (9b) — **9b CONFIRMED 2026-10-03** (user); marker `# Spec verified: R23-11` written. 9a evidence: (2026-10-03): ruff clean + black clean on all 11 touched files; 478 passed on the mirror + touched parser/writer tests; `test_member_annotations.py` 3 passed; set-based checklist==methods 9/9 with every method test-covered and no `# Spec verified:` marker in the class block; full unit suite 17299 passed; integration round-trip 10 passed / 1 failed aggregate — the same 8 `*_SystemMapping.arxml` `file_compare` fixtures fail identically on a pristine HEAD worktree (missing `COMMUNICATION-DIRECTION` in SENDER-RECEIVER-TO-SIGNAL-MAPPING, unrelated to this class), so the delta is zero.

- [ ] `EthernetPriorityRegeneration` — Referrable — R23-11 markdown · Table 3.74 (CP_TPS_SystemTemplate), p.128 — commit b1e4750b1
  - commit: b1e4750b1 (feat; steps 1-8; verbatim Note + attr notes, PEP 526 types, None-no-op accessors, 6-col checklist) — verbatim Note + 2 attr notes; rw via readEthernetPriorityRegeneration complete
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations — see feat note above
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-28 (6771 passed / 0 failed battery, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

- [x] `TimeSyncServerConfiguration` — Referrable — R23-11 markdown · Table 6.147 (CP_TPS_SystemTemplate), p.470 — commit 155cc2f7f (# Spec verified: R23-11, stamped 2026-10-03; Rule 0001.7 3-attribute reader/writer gap closed + malformed checklist rebuilt)
  - re-sync 2026-10-03 (Group16 Task 5): prior "steps 1-8" claim was false — zero code changes, malformed checklist, reader/writer gap. Steps 1-8 reset to `[ ]` and walked in this session.
  - Step 1 finding: own Table 6.147, p.470 (pypdf absent → page taken from existing `# Spec:` line); `Class` header confirmed; Base most-derived = `Referrable` → `__init__(self, parent, short_name)`; 4 attrs displayed order = priority/syncInterval/timeSyncServerIdentifier/timeSyncTechnology (all `0..1 attr`) matching the source. Defect: Rule 0001.7 — parser server branch set only `setTimeSyncTechnology`, writer only `TIME-SYNC-TECHNOLOGY`; PRIORITY/SYNC-INTERVAL/TIME-SYNC-SERVER-IDENTIFIER read/written nowhere. Checklist malformed — only the `__init__` row at top, accessor rows misplaced inside `__init__` as member comments.
  - [x] Step 1 — Sync members & description from spec — see finding bullet above
  - [x] Step 2 — Write model class unit test (Red) — model layer already spec-correct (prior stamped pass); strengthened mirror test (typed primitives + getter-first order pin) 5 passed — no model-layer RED exhibitable; real RED is Step 5
  - [x] Step 3 — Implement model class (Green) — no model change needed (fields/accessors already correct)
  - [x] Step 4 — Sync docstrings (wipe + rewrite) — misplaced checklist rows wiped from `__init__`; class docstring + 8 accessor docstrings diffed verbatim vs markdown Note cells (no textual delta); `__init__` has no docstring
  - [x] Step 5 — Write reader/writer round-trip test (Red) — new parser + writer test files; RED 3 failed / 2 passed (PRIORITY absent in writer; getPriority() None on round-trip; reader attrs None)
  - [x] Step 6 — Update parser & writer (Green) — added 6 call sites (priority/syncInterval/timeSyncServerIdentifier read+write) in XSD order PRIORITY, SYNC-INTERVAL, TIME-SYNC-SERVER-IDENTIFIER, TIME-SYNC-TECHNOLOGY; 8 passed
  - [x] Step 7 — Update checklist comment — 6-col block rebuilt at TOP, 9 rows source order, reader [x] on setters / writer [x] on getters; `# Spec:` suffix normalised; NO marker
  - [x] Step 8 — Deviations — none; `## TimeSyncServerConfiguration` "No deviations" entry added to docs/examples/method_deviation_by_class.md. Report-only: `TimeSynchronization.timeSyncServer` uses set/get for a Referrable child (Rule 0001.6, own queue row)
  - [x] Step 9 — Verify (9a) + confirm (9b) — **9b CONFIRMED 2026-10-03** (user; instruction was to match the `TimeSyncClientConfiguration` checklist style, whose only difference was the `# Spec verified:` line ⇒ marker written). 9a re-verified independently by the orchestrator: mirror + new parser `test_time_sync_server_configuration.py` + new writer `test_time_sync_server_configuration.py` + `test_member_annotations.py` 13 passed; full unit suite 17347 passed; `ruff check` + `black --check` clean on 6 touched `.py` files; set-based checklist==methods 9/9 in source order (all methods tested); integration 1 failed / 10 passed = the 8 known pre-existing `*_SystemMapping*.arxml` `file_compare` fixtures only (delta 0). All four attrs now round-trip by value. Report-only: `TimeSynchronization.timeSyncServer` uses set/get for a `Referrable` child (Rule 0001.6, own queue row).

- [ ] `CouplingPortAbstractShaper` — Identifiable — XSD-only abstract class — R23-11 XSD · xsd:group COUPLING-PORT-ABSTRACT-SHAPER (00052.xsd L23449, atp.Status="candidate")
  - module: M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/EthernetTopology.py
  - note (arbitration RESOLVED 2026-09-30): the 2026-09-28 "no own construct in any XSD" claim was WRONG — the XSD DOES carry the abstract class as the empty group COUPLING-PORT-ABSTRACT-SHAPER (L23449-23455, documentation "Abstract class for the definition of coupling port shapers." — matches the class docstring verbatim; mmt.qualifiedName="CouplingPortAbstractShaper"). KEEP as accepted deviation: the repo maps the XSD polymorphic choice (CouplingPortFifo.shaper, L23763: COUPLING-PORT-ASYNCHRONOUS-TRAFFIC-SHAPER | COUPLING-PORT-CREDIT-BASED-SHAPER) onto this registry-based abstract base + concrete subclasses; retirement (ConcreteTDEventVfb pattern) rejected — concrete children are real XSD classes. Consequence recorded: the concrete children are queued as NEW rows below; the registry stays unwired ({} after import) until they exist and register themselves. Checklist rebuilt XSD-only (`# Spec:` cites the XSD group line; release column R23-11).
  - [x] Step 1 — Sync members & description from spec — XSD group located (L23449); abstract class, empty sequence, no attributes; no PDF/markdown table in any corpus → XSD-only variant
  - [x] Step 2 — Write model class unit test (Red) — existing test_coupling_port_abstract_shaper_model.py (3 passed; registry/dispatch pins)
  - [x] Step 3 — Implement model class (Green) — no change (ABC + abstract guard + registry are the accepted mapping)
  - [x] Step 4 — Sync docstrings (wipe + rewrite) — N/A class docstring already = XSD documentation verbatim; no per-attr members (empty sequence)
  - [x] Step 5 — Write reader/writer round-trip test (Red) — N/A abstract class (no own XML element; the SHAPER choice round-trips via CouplingPortFifo, queued Group30)
  - [x] Step 6 — Update parser & writer (Green) — N/A abstract class (readCouplingPortFifo L12216 / writeCouplingPortFifo L11152 dispatch through the registry)
  - [x] Step 7 — Update checklist comment — rebuilt 6-column XSD-only with accepted-deviation note
  - [x] Step 8 — Deviations — accepted deviation documented in the checklist comment + docs/examples/method_deviation_by_class.md (## CouplingPortAbstractShaper); children queued (see new rows)
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9b deferred to batch confirmation (user instruction)

- [x] `CouplingPortAsynchronousTrafficShaper` — CouplingPortAbstractShaper — XSD-only · xsd:group COUPLING-PORT-ASYNCHRONOUS-TRAFFIC-SHAPER (00052.xsd L23458, atp.Status=candidate) — commit d41997345 (stamped 2026-10-02, # XSD verified: AUTOSAR_00052.xsd)

- [x] `CouplingPortCreditBasedShaper` — CouplingPortAbstractShaper — XSD-only · xsd:group COUPLING-PORT-CREDIT-BASED-SHAPER (00052.xsd L23597, atp.Status=candidate) — commit c5cfd1dc4 (stamped 2026-10-02, # XSD verified: AUTOSAR_00052.xsd)

- [ ] `MacMulticastGroup` — Identifiable — R23-11 markdown · Table 3.48 (CP_TPS_SystemTemplate), p.104 — commit b1e4750b1
  - commit: b1e4750b1 (feat; steps 1-8; verbatim Note + attr notes, PEP 526 types, None-no-op accessors, 6-col checklist) — verbatim Note + macMulticastAddress; rw via readMacMulticastGroup complete
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations — see feat note above
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-28 (6771 passed / 0 failed battery, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

- [x] `IPSecConfig` — ARObject — R23-11 markdown · Table 6.221 (CP_TPS_SystemTemplate), p.571 — commit d75eb10bf (# Spec verified: R23-11, stamped 2026-10-03)
  - Rule 0001.6 shape fix at the 9b gate: `ipSecRule` is a `* aggr` whose child `IPSecRule` lists `Identifiable` in its spec `Base`, so the pair is `createIPSecRule(short_name)` + `getIPSecRules()` (dedupe by short name over the owning field list — plain `ARObject` aggregator, Rule 0004). The parser now calls `config.createIPSecRule(self.getShortName(child_element))` instead of constructing `IPSecRule(config, short_name)` + `addIPSecRule(rule)`; mirror/writer tests updated accordingly.
  - module: M2/AUTOSARTemplates/SystemTemplate/SecureCommunication.py (Rule 0007 relocation 2026-10-03; was Fibex/Fibex4Ethernet/EthernetTopology.py)
  - commit: 6c97ddc10 (feat; steps 1-8; verbatim Note + attr notes, PEP 526 types, None-no-op accessors, 6-col checklist) — queue-row add-back 2026-09-28 (class synced in the same commit as Ipv4Configuration/NetworkEndpoint but the row was omitted from this queue; member type of NetworkEndpoint.ipSecConfig)
  - note (re-completion 2026-09-30): minimal-class deviation RESOLVED — TRAILING-CAPTION trap identified (markdown caption "Table 6.221: IPSecConfig" carries IPSecRule's body BELOW it; the real IPSecConfig body renders ABOVE the caption: Class header cell IPSecConfig, Base ARObject, Aggregated by NetworkEndpoint.ipSecConfig, attrs ipSecConfigProps ref 0..1 + ipSecRule aggr *). Added ipSecRules dedicated typed list + addIPSecRule/getIPSecRules; wired readIPSecConfig/writeIPSecConfig (XSD group IP-SEC-CONFIG L73645: IP-SEC-CONFIG-PROPS-REF → IP-SEC-RULES wrapper of unbounded IP-SEC-RULE); NetworkEndpoint read/write wiring at XSD position (after INFRASTRUCTURE-SERVICES, before NETWORK-ENDPOINT-ADDRESSES); cascade member classes synced in the same pass: IPSecRule (041bc7125), IPSecConfigProps (38cd00c06), 5 IPsec enums (28454d15e..07673b907) — IPSecConfigProps also got ARPackage.element dispatch + createIPSecConfigProps. Housing kept in EthernetTopology.py (consumer adjacency; SecureCommunication.py already imports EthernetTopology-side names — rehouse would cycle). Tests: test_IPSecConfig.py (model, 10), test_ipsec_config.py (parser 4 + writer 5)
  - note (Rule 0007 relocation 2026-10-03): the housing-kept-in-EthernetTopology decision above is superseded — the class now lives in SecureCommunication.py (user-approved; the cycle it feared does not exist because SecureCommunication imports nothing from EthernetTopology at runtime). Mirror test moved per Rule 0006 to tests/test_armodel/models/M2/AUTOSARTemplates/SystemTemplate/test_IPSecConfig.py; consumers re-pointed (arxml_parser.py, arxml_writer.py, parser/writer tests); EthernetTopology keeps a runtime `IPSecConfig` import for NetworkEndpoint.ipSecConfig and drops the now-unused `IPSecRule` (ruff F401). Steps 1-8 re-verified (members/base/Mult/Kind/Note unchanged vs Table 6.221, incl. the trailing-caption trap; docstrings diffed verbatim 7/7). 9a green: 9389 targeted + 4 annotation-gate + 17327 full-unit passed; ruff/black clean; checklist==methods set+order pass; integration 1 failed/10 passed = the 8 known pre-existing `*_SystemMapping.arxml` file_compare fixtures (no fixture carries IP-SEC-CONFIG). Step 9 stays `[ ]` pending 9b (no stamp, no commit).
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations — minimal-class deviation resolved (see re-completion note); no tracker entries existed for this class
  - [x] Step 9 — Verify (9a) + confirm (9b) — 9b CONFIRMED 2026-10-03 (user); marker `# Spec verified: R23-11` written. 9a: ruff + black clean on 7 touched files; 9393 passed on the SystemTemplate/parser/writer battery + both annotation gates; checklist==methods 5/5 in source order; full unit suite 17327 passed; integration 1 failed/10 passed — the 8 `*_SystemMapping.arxml` file_compare fixtures only, delta 0; both import orders + all `get_type_hints` pins resolve.

- [x] `NetworkEndpoint` — Identifiable — R23-11 markdown · Table 6.134 (CP_TPS_SystemTemplate), p.463 — commit 84587c11f (# Spec verified: R23-11, stamped 2026-10-03; Rule 0001.7 FQDN reader/writer gap closed, stale checklist rows fixed, Rule 0006 mirror gap closed)
  - commit: 6c97ddc10 (feat; steps 1-8; verbatim Note + attr notes, PEP 526 types, None-no-op accessors, 6-col checklist) — verbatim Note + 5 attr notes; Step 8 deviation: ipSecConfig AGGR RW UNWIRED (IPSecConfig created minimal — ipSecRule aggr omitted, member classes IPSecRule/IPSecConfigProps not modeled, would cascade into SecureCommunication family) — flagged for user
  - note (re-sync 2026-10-03; no `# Spec verified:` marker ⇒ full 9-step re-run, Group16 Task 4): Step 1 re-extracted Table 6.134 — `Class` header confirmed (not Enumeration), Base `ARObject , Identifiable , MultilanguageReferrable , Referrable` → `Identifiable`, `__init__(self, parent, short_name)`; 5 attrs in displayed order: fullyQualifiedDomainName (String, 0..1, attr), infrastructureServices (InfrastructureServices, 0..1, aggr), ipSecConfig (IPSecConfig, 0..1, aggr), networkEndpointAddress (NetworkEndpointAddress, *, aggr), priority (PositiveInteger, 0..1, attr); p.463 unchanged. Defects confirmed: (a) Rule 0001.7 — `FULLY-QUALIFIED-DOMAIN-NAME` absent from parser+writer (XSD group `NETWORK-ENDPOINT` L84073, `sequenceOffset` FIRST — before INFRASTRUCTURE-SERVICES); (b) stale checklist rows `getIpSecConfig`/`setIpSecConfig` `[—] reader/writer` although helpers wire `IP-SEC-CONFIG` (parser L9877-9881, writer L9927-9929); (c) Rule 0006 — `getNetworkEndpointAddresses` never asserted in mirror test. Also found: the `networkEndpointAddress` pair is getter-first but must be mutator-first (Rule 0001.11), and the `Tags: xml.namePlural=…` tail on that Note must be dropped (Rule 0012.2.5.2).
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations — none; `## NetworkEndpoint` entry added to `docs/examples/method_deviation_by_class.md` (no field/type/naming/missing deviation)
  - [x] Step 9 — Verify (9a) + confirm (9b) — **9b CONFIRMED 2026-10-03** (user); marker `# Spec verified: R23-11` written. 9a re-verified independently by the orchestrator: mirror + reader `test_network_endpoint.py` + writer `test_network_endpoint.py` + `test_member_annotations.py` 21 passed; full unit suite 17341 passed; `ruff check` + `black --check` clean on all 6 touched `.py` files; set-based checklist==methods 11/11 in source order (all methods tested); integration 1 failed / 10 passed = the 8 known pre-existing `*_SystemMapping*.arxml` `file_compare` fixtures only (delta 0); `armodel.NetworkEndpoint` resolves. FQDN now round-trips (`getFullyQualifiedDomainName().getValue()`), `NETWORK-ENDPOINT-ADDRESSES` None/empty-wrapper case covered. No deviations. Report-only: `MAC-MULTICAST-CONFIGURATION` dispatch still absent — `MacMulticastConfiguration` is a `pass` stub queued in Group32 (its own sync item); `p.463` not re-verified via `pdf_page.py` (venv lacks `pypdf`) but matches the plan + prior `# Spec:` line.

- [ ] `VlanConfig` — Identifiable — R23-11 markdown · Table 3.50 (CP_TPS_SystemTemplate), p.106 — commit b1e4750b1
  - commit: b1e4750b1 (feat; steps 1-8; verbatim Note + attr notes, PEP 526 types, None-no-op accessors, 6-col checklist) — verbatim Note + vlanIdentifier; rw via readEthernetPhysicalChannelVlan complete
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations — see feat note above
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-28 (6771 passed / 0 failed battery, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

- [ ] `Ipv4Configuration` — NetworkEndpointAddress — R23-11 markdown · Table 6.136 (CP_TPS_SystemTemplate), p.465 — commit 6c97ddc10
  - commit: 6c97ddc10 (feat; steps 1-8; verbatim Note + attr notes, PEP 526 types, None-no-op accessors, 6-col checklist) — verbatim Note + 8 attr notes; ipv4AddressSource now typed Ipv4AddressSourceEnum; ctor no-arg (NetworkEndpointAddress chain)
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations — see feat note above
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-28 (6771 passed / 0 failed battery, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

- [ ] `GenericTp` — TransportProtocolConfiguration — R23-11 markdown · Table 6.126 (CP_TPS_SystemTemplate), p.459 — commit 26c26b088
  - commit: 26c26b088 (feat; steps 1-8; verbatim Note + attr notes, PEP 526 types, None-no-op accessors, 6-col checklist) — verbatim Note + 2 attr notes; ctor kept no-arg (TransportProtocolConfiguration family contract)
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations — see feat note above
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-28 (6771 passed / 0 failed battery, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

- [ ] `TcpTp` — TcpUdpConfig — R23-11 markdown · Table 6.129 (CP_TPS_SystemTemplate), p.460 — commit 26c26b088
  - commit: 26c26b088 (feat; steps 1-8; verbatim Note + attr notes, PEP 526 types, None-no-op accessors, 6-col checklist) — verbatim Note + 8 attr notes; NEW rw coverage RECEIVE-WINDOW-MIN + TCP-RETRANSMISSION-TIMEOUT (XSD order verified); ctor no-arg
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations — see feat note above
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-28 (6771 passed / 0 failed battery, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

- [ ] `UdpTp` — TcpUdpConfig — R23-11 markdown · Table 6.128 (CP_TPS_SystemTemplate), p.459 — commit 26c26b088
  - commit: 26c26b088 (feat; steps 1-8; verbatim Note + attr notes, PEP 526 types, None-no-op accessors, 6-col checklist) — verbatim Note + udpTpPort aggr; ctor no-arg
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations — see feat note above
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-28 (6771 passed / 0 failed battery, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

- [ ] `PduCollectionSemanticsEnum` — AREnum — R23-11 markdown · Table 6.165 (CP_TPS_SystemTemplate), p.490 — commit 4b7c8dc79
  - commit: 4b7c8dc79 (feat; steps 1-8; verbatim Note + attr notes, PEP 526 types, None-no-op accessors, 6-col checklist) — queue-row add-back 2026-09-28 (class synced in the same commit as SocketConnectionIpduIdentifier/SocketConnectionBundle but the row was omitted from this queue; member type of SocketConnectionIpduIdentifier.pduCollectionSemantics — its row notes "pduCollectionSemantics/Trigger now typed enums") — class body carries `# Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.165, p.490` checklist, NO `# Spec verified:` yet; sibling PduCollectionTriggerEnum (Table 6.41) is stamped
  - [—] Step 5 — N/A standalone enum
  - [—] Step 6 — N/A standalone enum
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations — see feat note above (literals lastIsBest/queued; mirror test test_PduCollectionSemanticsEnum.py)
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `SocketConnectionIpduIdentifier` — ARObject — R4.3.1 markdown · Table 6.122 (TPS_SystemTemplate), p.321 — commit 4b7c8dc79
  - commit: 4b7c8dc79 (feat; steps 1-8; verbatim Note + attr notes, PEP 526 types, None-no-op accessors, 6-col checklist) — R4.3.1 sync: verbatim Note + 6 attrs; FABRICATED PduRef member + PDU-REF parser/writer lines REMOVED (element absent from BOTH XSDs — Rule 0001.3/0014); pduCollectionSemantics/Trigger now typed enums (reader wires literals → enum instances)
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations — see feat note above
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-28 (6771 passed / 0 failed battery, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

- [ ] `SocketConnectionBundle` — Referrable — R4.3.1 markdown · Table 6.118 (TPS_SystemTemplate), p.316 — commit 4b7c8dc79
  - commit: 4b7c8dc79 (feat; steps 1-8; verbatim Note + attr notes, PEP 526 types, None-no-op accessors, 6-col checklist) — R4.3.1 sync: verbatim Note + 7 attrs; parser populates pdus via addPdu (Rule 0013); ctor (parent, short_name) per Referrable
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations — see feat note above
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-28 (6771 passed / 0 failed battery, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

- [ ] `RequestResponseDelay` — ARObject — R23-11 markdown · Table 6.171 (CP_TPS_SystemTemplate), p.515 — commit d7240be74
  - commit: d7240be74 (feat; steps 1-8; verbatim Note + attr notes, PEP 526 types, None-no-op accessors, 6-col checklist) — verbatim Note + maxValue/minValue; rw via getRequestResponseDelay complete
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations — see feat note above
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-28 (6771 passed / 0 failed battery, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

- [x] `SdServerConfig` — ARObject — R4.3.1 markdown · Table 6.171 (TPS_SystemTemplate), p.355 — commit f509df9d9 (# Spec verified: R4.3.1, stamped 2026-10-03)
  - commit: d7240be74 (feat; steps 1-8; verbatim Note + attr notes, PEP 526 types, None-no-op accessors, 6-col checklist) — R4.3.1 sync: verbatim Note + 7 attrs; setCapabilityRecords replaced by addCapabilityRecord (aggr * mutator per Rule 0013); reader already used addCapabilityRecord
  - module: M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/EthernetTopology.py (relocated 2026-10-03, Rule 0007)
  - re-pass 2026-10-03: full 9-step re-run for this class (steps 1-8 walked; Step 9 stays `[ ]` pending 9b). Rule 0007 relocation `ServiceInstances.py` → `EthernetTopology.py` (placed immediately before `SdClientConfig`), all consumers re-pointed (parser L1034, writer L929, `test_SdServerConfig.py`, `test_ServiceInstances.py`, `test_event_handler.py`, `test_writer_frame_channel.py`); `SdServerConfig` added to `ServiceInstances.py`'s bottom cycle-breaker import for the `EventHandler`/`ProvidedServiceInstance` annotations; both import orders + `armodel.SdServerConfig` resolve. Reader/writer gap closed: `capabilityRecord` (`* aggr`) now read via `getTagWithOptionalValues` → `addCapabilityRecord` and written via `setTagWithOptionalValues`, in XSD `sequenceOffset` order (parser L10230-10231, writer L10235). All class/method docstrings + `__init__` member comments wiped and rewritten from the R4.3.1 markdown `Note` cells (22/22 diff clean). `# Spec:` normalised to `AUTOSAR_TPS_SystemTemplate.pdf (R4.3.1), Table 6.171, p.355`; NO marker (9b gate). Accepted deviation: `ttl` `Optional[PositiveInteger]` kept per user decision (PDF Mult 1) — recorded in `docs/examples/method_deviation_by_class.md`.
  - closed at the 9b gate (this class's own compliance): (1) the helper now calls `readARObject`/`writeARObject`, so the `AR:AR-OBJECT` `S`/`T` attributes round-trip again (parser L10230 / writer L10235), pinned by `test_round_trip_preserves_arobject_checksum_and_timestamp`; (2) the `capabilityRecord` pair is now mutator-first (`addCapabilityRecord` → `getCapabilityRecords`) in both source and checklist per Rule 0001.11. Still open in *other* classes (reported, untouched): `ProvidedServiceInstance.getSdServerConfig`/`setSdServerConfig` are untyped accessors (Rule 0001.3) — a `ProvidedServiceInstance`-sync item.
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations — see feat note above
  - [x] Step 9 — Verify (9a) + confirm (9b) — 9b CONFIRMED 2026-10-03 (user); marker `# Spec verified: R4.3.1` written. 9a re-run 2026-10-03 on the relocated class (mirror 14 passed; reader 4 + writer 8 passed; 902 passed on the touched + sibling battery; ruff/black clean); 9b deferred to batch confirmation (user instruction)

- [ ] `TcpOptionFilterList` — Identifiable — R23-11 markdown · Table 6.123 (CP_TPS_SystemTemplate), p.457 — commit 2d5b3256b
  - commit: 2d5b3256b (feat; steps 1-8; verbatim Note + attr notes, PEP 526 types, None-no-op accessors, 6-col checklist) — prior R4.3.1 sync upgraded to R23-11 (Rule 0016.3 — class HAS R23-11 Table 6.123): Note "White list..." → "Permitted list..."
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations — see feat note above
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-28 (6771 passed / 0 failed battery, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

- [ ] `TcpOptionFilterSet` — ARElement — R23-11 markdown · Table 6.122 (CP_TPS_SystemTemplate), p.457 — commit 2d5b3256b
  - commit: 2d5b3256b (feat; steps 1-8; verbatim Note + attr notes, PEP 526 types, None-no-op accessors, 6-col checklist) — prior R4.3.1 sync upgraded to R23-11: member notes "white lists" → "permitted lists"
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations — see feat note above
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-28 (6771 passed / 0 failed battery, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

- [ ] `IPv6ExtHeaderFilterList` — Identifiable — R23-11 markdown · Table 6.121 (CP_TPS_SystemTemplate), p.456 — commit 2d5b3256b
  - commit: 2d5b3256b (prior R4.3.1→R23-11 upgrade) — re-sync 2026-10-03 (Group16 Task 6): prior "reader/writer N/A (ref target via ALLOWED-I-PV-6-EXT-HEADERS-REF)" claim was WRONG — the R23-11 table lists allowedIPv6ExtHeader as an `attr`, and XSD 00052 L66606 defines group I-PV-6-EXT-HEADER-FILTER-LIST with its own ALLOWED-I-PV-6-EXT-HEADERS wrapper of unbounded ALLOWED-I-PV-6-EXT-HEADER (AR:POSITIVE-INTEGER) items; the …-REF element (L107861) belongs to SocketAddress. Also Rule 0003 quoted return annotation. Steps 1-8 reset to `[ ]` and walked in this session.
  - [x] Step 1 — Sync members & description from spec — own Table 6.121, p.456 (pypdf absent → page from existing `# Spec:` line); `Class` header confirmed; Base most-derived = `Identifiable` → `__init__(self, parent, short_name)`; 1 attr `allowedIPv6ExtHeader` (PositiveInteger, `*`, attr)
  - [x] Step 2 — Write model class unit test (Red) — added `test_no_quoted_top_level_annotations` + `get_type_hints` return pin; RED 1 failed / 5 passed
  - [x] Step 3 — Implement model class (Green) — added `from __future__ import annotations`, unquoted `-> IPv6ExtHeaderFilterList`, reordered list pair mutator-first (Rule 0001.11)
  - [x] Step 4 — Sync docstrings (wipe + rewrite) — class docstring + attr inline comment + getter/add docstrings diffed verbatim vs markdown Note; `__init__` has no docstring; no legacy rows inside `__init__`
  - [x] Step 5 — Write reader/writer round-trip test (Red) — new parser + writer test files; RED 7 failed (helper pair absent); covers wrapper/item values, empty wrapper not emitted, re-parse `[]`
  - [x] Step 6 — Update parser & writer (Green) — added matched pair `readIPv6ExtHeaderFilterList`/`writeIPv6ExtHeaderFilterList` (readIdentifiable + ALLOWED-I-PV-6-EXT-HEADERS wrapper / item each; writer emits wrapper only when non-empty) + imports; 7 passed
  - [x] Step 7 — Update checklist comment — single 6-col block at TOP, 3 rows source order (__init__, add, get); reader [x] on the mutator and writer [x] on the getter; `# Spec:` normalised (dropped the `(R23-11)` suffix); NO marker
  - [x] Step 8 — Deviations — none; `## IPv6ExtHeaderFilterList` "No deviations" entry added to docs/examples/method_deviation_by_class.md. Report-only: `IPv6ExtHeaderFilterSet` (spec Aggregated-by parent) is a `pass` stub in ARPackage.py L9695 with no parser/writer handler (own sync); sibling `TcpOptionFilterList` accessor pair is getter-first (Rule 0001.11, Task 7)
  - [x] Step 9 — Verify (9a) + confirm (9b) — **9b CONFIRMED 2026-10-03** (user); marker `# Spec verified: R23-11` written. 9a re-verified independently by the orchestrator: mirror + new parser `test_ipv6_ext_header_filter_list.py` + new writer `test_ipv6_ext_header_filter_list.py` + annotation/PEP-563 gates 16 passed; full unit suite 17356 passed; ruff + black clean on 6 touched `.py` files; checklist==methods 3/3 in source order (all tested); integration 1 failed / 10 passed = the 8 known pre-existing `*_SystemMapping*.arxml` `file_compare` fixtures only (delta 0). Report-only: `IPv6ExtHeaderFilterSet` aggregator is a `pass` stub (own sync); sibling `TcpOptionFilterList` getter-first (Rule 0001.11, Task 7).

- [ ] `TimeSynchronization` — ARObject — R23-11 markdown · Table 6.145 (CP_TPS_SystemTemplate), p.469 — commit b1e4750b1
  - commit: b1e4750b1 (feat; steps 1-8; verbatim Note + attr notes, PEP 526 types, None-no-op accessors, 6-col checklist) — verbatim Note + 2 aggr notes; rw via getTimeSynchronization/setTimeSynchronization complete
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations — see feat note above
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-28 (6771 passed / 0 failed battery, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

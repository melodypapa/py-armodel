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

- [ ] `InitialSdDelayConfig` — ARObject — R23-11 markdown · Table 6.170 (CP_TPS_SystemTemplate), p.514 — commit d7240be74
  - commit: d7240be74 (feat; steps 1-8; verbatim Note + attr notes, PEP 526 types, None-no-op accessors, 6-col checklist) — DEDUPLICATED: canonical definition in EthernetTopology.py; ServiceInstances.py copy deleted and re-imported (identical-name duplicate rows in this queue resolved to one class)
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations — see feat note above
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-28 (6771 passed / 0 failed battery, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

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

- [ ] `TimeSyncServerConfiguration` — Referrable — R23-11 markdown · Table 6.147 (CP_TPS_SystemTemplate), p.470 — commit b1e4750b1
  - commit: b1e4750b1 (feat; steps 1-8; verbatim Note + attr notes, PEP 526 types, None-no-op accessors, 6-col checklist) — verbatim Note + 4 attr notes; parsed within readTimeSynchronization (server construction at parser:9458)
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations — see feat note above
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-28 (6771 passed / 0 failed battery, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

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

- [ ] `CouplingPortAsynchronousTrafficShaper` — CouplingPortAbstractShaper — NEW row (discovered 2026-09-30 as missing CouplingPortAbstractShaper concrete child / CouplingPortFifo.shaper choice member, Rule 0001.10/0016.4) — XSD-only · xsd:group COUPLING-PORT-ASYNCHRONOUS-TRAFFIC-SHAPER (00052.xsd L23458, atp.Status="candidate")
  - module: M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/EthernetTopology.py
  - note: no Class/Enumeration table in any corpus (candidate-status CP class). XSD members: committedBurstSize (PositiveInteger 0..1), committedInformationRate (PositiveInteger 0..1), trafficShaperGroup (ref 0..1). Must register itself in CouplingPortAbstractShaper._shaper_registry ("COUPLING-PORT-ASYNCHRONOUS-TRAFFIC-SHAPER") at import time; consumer dispatch = readCouplingPortFifo/writeCouplingPortFifo SHAPER choice.
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

- [ ] `CouplingPortCreditBasedShaper` — CouplingPortAbstractShaper — NEW row (discovered 2026-09-30 as missing CouplingPortAbstractShaper concrete child / CouplingPortFifo.shaper choice member, Rule 0001.10/0016.4) — XSD-only · xsd:group COUPLING-PORT-CREDIT-BASED-SHAPER (00052.xsd L23597, atp.Status="candidate")
  - module: M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/EthernetTopology.py
  - note: no Class/Enumeration table in any corpus (candidate-status CP class). XSD members: idleSlope (PositiveInteger 0..1), lowerBoundary (PositiveInteger 0..1), upperBoundary (PositiveInteger 0..1). Must register itself in CouplingPortAbstractShaper._shaper_registry ("COUPLING-PORT-CREDIT-BASED-SHAPER") at import time; consumer dispatch = readCouplingPortFifo/writeCouplingPortFifo SHAPER choice.
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

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

- [ ] `IPSecConfig` — ARObject — R23-11 markdown · Table 6.221 (CP_TPS_SystemTemplate), p.571 — commit 6c97ddc10
  - module: M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/EthernetTopology.py
  - commit: 6c97ddc10 (feat; steps 1-8; verbatim Note + attr notes, PEP 526 types, None-no-op accessors, 6-col checklist) — queue-row add-back 2026-09-28 (class synced in the same commit as Ipv4Configuration/NetworkEndpoint but the row was omitted from this queue; member type of NetworkEndpoint.ipSecConfig)
  - note (re-completion 2026-09-30): minimal-class deviation RESOLVED — TRAILING-CAPTION trap identified (markdown caption "Table 6.221: IPSecConfig" carries IPSecRule's body BELOW it; the real IPSecConfig body renders ABOVE the caption: Class header cell IPSecConfig, Base ARObject, Aggregated by NetworkEndpoint.ipSecConfig, attrs ipSecConfigProps ref 0..1 + ipSecRule aggr *). Added ipSecRules dedicated typed list + addIPSecRule/getIPSecRules; wired readIPSecConfig/writeIPSecConfig (XSD group IP-SEC-CONFIG L73645: IP-SEC-CONFIG-PROPS-REF → IP-SEC-RULES wrapper of unbounded IP-SEC-RULE); NetworkEndpoint read/write wiring at XSD position (after INFRASTRUCTURE-SERVICES, before NETWORK-ENDPOINT-ADDRESSES); cascade member classes synced in the same pass: IPSecRule (041bc7125), IPSecConfigProps (38cd00c06), 5 IPsec enums (28454d15e..07673b907) — IPSecConfigProps also got ARPackage.element dispatch + createIPSecConfigProps. Housing kept in EthernetTopology.py (consumer adjacency; SecureCommunication.py already imports EthernetTopology-side names — rehouse would cycle). Tests: test_IPSecConfig.py (model, 10), test_ipsec_config.py (parser 4 + writer 5)
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations — minimal-class deviation resolved (see re-completion note); no tracker entries existed for this class
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9b deferred to batch confirmation (user instruction)

- [ ] `NetworkEndpoint` — Identifiable — R23-11 markdown · Table 6.134 (CP_TPS_SystemTemplate), p.463 — commit 6c97ddc10
  - commit: 6c97ddc10 (feat; steps 1-8; verbatim Note + attr notes, PEP 526 types, None-no-op accessors, 6-col checklist) — verbatim Note + 5 attr notes; Step 8 deviation: ipSecConfig AGGR RW UNWIRED (IPSecConfig created minimal — ipSecRule aggr omitted, member classes IPSecRule/IPSecConfigProps not modeled, would cascade into SecureCommunication family) — flagged for user
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations — see feat note above
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-28 (6771 passed / 0 failed battery, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

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

- [ ] `SdServerConfig` — ARObject — R4.3.1 markdown · Table 6.171 (TPS_SystemTemplate), p.355 — commit d7240be74
  - commit: d7240be74 (feat; steps 1-8; verbatim Note + attr notes, PEP 526 types, None-no-op accessors, 6-col checklist) — R4.3.1 sync: verbatim Note + 7 attrs; setCapabilityRecords replaced by addCapabilityRecord (aggr * mutator per Rule 0013); reader already used addCapabilityRecord
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations — see feat note above
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-28 (6771 passed / 0 failed battery, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

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
  - commit: 2d5b3256b (feat; steps 1-8; verbatim Note + attr notes, PEP 526 types, None-no-op accessors, 6-col checklist) — prior R4.3.1 sync upgraded to R23-11: Note "White list..." → "Permitted list..."; reader/writer N/A (ref target via ALLOWED-I-PV-6-EXT-HEADERS-REF) per prior arbitration
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations — see feat note above
  - [ ] Step 9 — Verify (9a) + confirm (9b) — 9a passed 2026-09-28 (6771 passed / 0 failed battery, lint clean, black-check clean); 9b deferred to batch confirmation (user instruction)

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

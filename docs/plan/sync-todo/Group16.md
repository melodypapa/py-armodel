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

- [x] `TcpProps` — ARObject — already verified (R23-11 · Table 3.111, p.155; short-circuit 2026-09-27)
  - module: M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/EthernetTopology.py
  - note (short-circuit 2026-09-27): class body already carries `# Spec verified: R23-11` — all 18 tcp* attributes (Boolean/PositiveInteger/TimeValue per row) match the table (7 rows in the visible fragment + page-split continuation rows corroborated by constraints 5119–5124), full get/set pairs with reader/writer coverage, 6-col checklist all [x]. Deviation check found nothing new. No code change needed — row flipped without a class commit.

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

- [ ] `CouplingPortAbstractShaper` — Identifiable — ARBITRATION REQUIRED (no Class/Enumeration table in R23-11, R4.3.1 or R4.4.0 corpora; no own construct in any XSD — only COUPLING-PORT-SHAPER / COUPLING-PORT-CREDIT-BASED-SHAPER / COUPLING-PORT-ASYNCHRONOUS-TRAFFIC-SHAPER exist)
  - module: M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/EthernetTopology.py
  - note (Step 1 finding 2026-09-28): repo-invented abstract registry base over the real XSD shaper classes (same "Abstract*" pattern as the retired ConcreteTDEventVfb case, but its concrete children DO exist in the XSD). Current body is an ABC with a shaper registry + abstract guard, model test present. NOTHING TO SYNC — no spec text exists. User arbitration needed: keep as accepted deviation (documented helper base) or retire like ConcreteTDEventVfb.
  - [ ] Step 1 — Sync members & description from spec — BLOCKED: no spec source (arbitration)
  - [ ] Step 2 — Write model class unit test (Red) — existing test_coupling_port_abstract_shaper_model.py
  - [ ] Step 3 — Implement model class (Green) — no change
  - [ ] Step 4 — Sync docstrings (wipe + rewrite) — N/A (no spec Note)
  - [ ] Step 5 — Write reader/writer round-trip test (Red) — N/A
  - [ ] Step 6 — Update parser & writer (Green) — N/A
  - [ ] Step 7 — Update checklist comment — existing
  - [ ] Step 8 — Deviations — whole-class arbitration pending
  - [ ] Step 9 — Verify (9a) + confirm (9b) — deferred to user arbitration

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

- [ ] `InitialSdDelayConfig` — ARObject — source TBC (locate table at Step 1)
  - module: M2/AUTOSARTemplates/SystemTemplate/Fibex/Fibex4Ethernet/ServiceInstances.py
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

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

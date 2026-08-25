# Sync todo: Fibex4Ethernet ethernet-related class cluster (SystemTemplate / SoftwareComponentTemplate)

Input scope: 17 ethernet-related classes in `M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet`,
selected by user from `docs/examples/method_deviation_by_class.md` (all without a `# Spec verified:`
stamp). Generated: 2026-08-23. Queue updated 2026-08-24: the previously "Skip (placeholder)" member
types are now PROMOTED into the queue as class rows and MUST be synced before their dependents per
Rule 0016.5 (member-type-first ordering). Queue re-audited 2026-08-24 against markdown: XSD-only
atpVariation `...RefConditional` / `...Conditional` wrappers, the obsolete SoAd enum classes, and the
ad-hoc technology enum classes were REMOVED from the queue (markdown is authoritative — Rule 0002 /
user decision); rows retargeted to the real markdown-documented classes.
(resume = first class row still `[ ]`; all class rows `[x]` = sync finished)

Closure confirmed by user 2026-08-23: queue the 17 input classes + their missing member-type classes;
framework bases (ARObject…Identifiable, CommunicationCluster/Controller/Connector, Referrable,
Describable, NetworkEndpointAddress, CouplingPortStructuralElement, FibexElement) excluded per standing
project decision — existing and not modified in this pass.

Two specs in scope:
- `AUTOSAR_CP_TPS_SystemTemplate.md` (Tables 3.47…3.68 topology; Tables 6.117…6.168 services;
  Tables 6.172/6.173/6.207, F.117/F.118 timing + DoIP classes)
- `AUTOSAR_CP_TPS_SoftwareComponentTemplate.md` (ConsumedEventGroup/ConsumedServiceInstance)

Already stamped, therefore NOT queued (Rule 0012.3): `ProvidedServiceInstance` (R23-11).

Referenced member types that EXIST (no queue row, Rule 0012.3): CouplingPortScheduler,
EthernetPriorityRegeneration, EthernetPhysicalChannel, SoAdRoutingGroup, TpConnectionIdent,
NetworkEndpoint, NetworkEndpointAddress, MacMulticastGroup, CouplingPortStructuralElement,
DoIpLogicAddress (TransportProtocols.py), and the Ethernet switch enums used by CouplingPort members.

Missing/stub member types PROMOTED into the queue (Rule 0016.4/0016.5) — each now has its own class
row below and must sync BEFORE the class that references it. All rows below are real markdown classes
(no XSD-only wrappers are queued).

## Queue (dependency / member-type-first, then their dependents)

### Member types — sync FIRST (Rule 0016.5)

- [x] SomeipSdClientServiceInstanceConfig (ARElement value type · Table F.117 · p.2059 · used by ConsumedServiceInstance.sdClientTimerConfig · source ServiceInstances.py · adds initialFindBehavior aggr InitialSdDelayConfig, priority attr, serviceFindTimeToLive attr) <!-- commit: fa198376 -->
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - [x] Step 9 — Verify (9a) + confirm (9b)
- [ ] SomeipSdClientEventGroupTimingConfig (ARElement value type · Table 6.173 · p.1162 · used by ConsumedEventGroup.sdClientTimerConfig · source ServiceInstances.py · adds requestResponseDelay aggr RequestResponseDelay, subscribeEventgroupRetryDelay attr TimeValue, subscribeEventgroupRetryMax attr, timeToLive attr) · steps complete commit 0e472ca8 — STAMP DEFERRED (batch 9b pending)
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - [x] Step 9 — Verify (9a) + confirm (9b)
- [ ] SomeipSdServerEventGroupTimingConfig (ARElement value type · Table 6.172 · p.1162 · used by EventHandler.sdServerEgTimingConfig · source ServiceInstances.py · adds requestResponseDelay aggr RequestResponseDelay) · steps complete commit 601f7bd5 — STAMP DEFERRED (batch 9b pending)
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - [x] Step 9 — Verify (9a) + confirm (9b)
- [ ] SomeipServiceVersion (ARObject value type · Table F.118 · used by ConsumedServiceInstance.blacklistedVersion · source ServiceInstances.py · adds majorVersion, minorVersion) · steps complete commit 152f3113 — STAMP DEFERRED (batch 9b pending)
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - [x] Step 9 — Verify (9a) + confirm (9b)
- [ ] DhcpServerConfiguration (value type · Table 3.79 · used by InfrastructureServices.dhcpServerConfiguration, VlanMembership.dhcpAddressAssignment) · steps complete commit ecfa6c40 — STAMP DEFERRED (batch 9b pending)
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - [x] Step 9 — Verify (9a) + confirm (9b)
- [ ] CouplingPortTrafficClassAssignment (value type · Table 3.75 · used by CouplingPortDetails.ethernetTrafficClassAssignments) · steps complete commit c63eaa99 — STAMP DEFERRED (batch 9b pending)
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - [x] Step 9 — Verify (9a) + confirm (9b)
- [ ] CanXlProps (value type · existing EthernetCommunication.py · used by EthernetCommunicationConnector.canXlPropsRefs / apApplicationEndpoint)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] TagWithOptionalValue (value type · Table 6.159 (CP) / 4.76 (FO) · used by SdClientConfig.capabilityRecord, AbstractServiceInstance.capabilityRecords)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

### Input ethernet classes — sync AFTER their member types (Rule 0016.5)

- [ ] ConsumedEventGroup (markdown SoftwareComponentTemplate · Table 6.168 · p.978 · source Fibex4Ethernet/ServiceInstances.py · depends on SomeipSdClientEventGroupTimingConfig above; sdClientTimerConfig is a ref to it; adds instanceIdentifier)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] ConsumedServiceInstance (markdown SoftwareComponentTemplate · Table 6.167 · p.980 · source Fibex4Ethernet/ServiceInstances.py · base AbstractServiceInstance below; depends on SomeipSdClientServiceInstanceConfig / SomeipServiceVersion above; adds blacklistedVersion, eventMulticastSubscriptionAddress, sdClientTimerConfig refs)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] AbstractServiceInstance (markdown SystemTemplate · Table 6.158 · p.476 · source Fibex4Ethernet/ServiceInstances.py · base of ConsumedServiceInstance / ProvidedServiceInstance; depends on TagWithOptionalValue above; fixes methodActivationRoutingGroup & routingGroupRefs member types)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] ApplicationEndpoint (markdown SystemTemplate · Table 6.124 · p.457 · source Fibex4Ethernet/ServiceInstances.py · adds discoveryTechnology, remotingTechnology, serializationTechnologyRef; these tech member types are XSD/ad-hoc — handle inside this sync)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] SocketAddress (markdown SystemTemplate · Table 6.118 · p.452 · source Fibex4Ethernet/ServiceInstances.py · fixes applicationEndpoint type; adds ipAddress)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] SoAdConfig (markdown SystemTemplate · Table 6.117 · p.451 · source Fibex4Ethernet/ServiceInstances.py · adds logicAddress ref to existing DoIpLogicAddress)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] EventHandler (markdown SystemTemplate · Table 6.166 · p.492 · source Fibex4Ethernet/ServiceInstances.py · depends on SomeipSdServerEventGroupTimingConfig above; adds eventGroupIdentifier, eventMulticastAddress, pduActivationRoutingGroup, sdServerEgTimingConfig)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] Ipv6Configuration (markdown SystemTemplate · Table 6.139 · p.466 · source Fibex4Ethernet/NetworkEndpoint.py · fixes dnsServerAddresses naming → dnsServerAddress)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] InfrastructureServices (markdown SystemTemplate · Table 6.144 · p.469 · source Fibex4Ethernet/NetworkEndpoint.py · depends on DhcpServerConfiguration above; adds dhcpServerConfiguration)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] CouplingPortFifo (markdown SystemTemplate · Table 3.68 · p.124 · source Fibex4Ethernet/EthernetTopology.py · fixes assignedTrafficClass type)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] CouplingPortDetails (markdown SystemTemplate · Table 3.63 · p.121 · source Fibex4Ethernet/EthernetTopology.py · depends on CouplingPortTrafficClassAssignment above; fixes ethernetPriorityRegeneration / ethernetTrafficClassAssignment member types)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] CouplingPort (markdown SystemTemplate · Table 3.54 · p.109 · source Fibex4Ethernet/EthernetTopology.py · member of EthernetCluster.couplingPorts & EthernetCommunicationController.couplingPorts; adds couplingPortSpeed, vlanModifierRef → EthernetPhysicalChannel Ref)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] EthernetCluster (markdown SystemTemplate · Table 3.47 · p.103 · source Fibex4Ethernet/EthernetTopology.py · adds couplingPorts to EthernetCluster; closes open items)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] EthernetCommunicationController (markdown SystemTemplate · Table 3.61 · p.115 · source Fibex4Ethernet/EthernetTopology.py · closes open items)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] EthernetCommunicationConnector (markdown SystemTemplate · Table 3.62 · p.117 · source Fibex4Ethernet/EthernetTopology.py · depends on CanXlProps above; adds apApplicationEndpoint, canXlPropsRefs, ipV6PathMtuEnabled, ipV6PathMtuTimeout, pncFilterDataMask, unicastNetworkEndpointRefs → NetworkEndpoint Ref)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] SdClientConfig (no PDF table · p.870 source EthernetTopology.py · depends on TagWithOptionalValue above; fixes capabilityRecord type)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] SocketConnection (obsolete · p.2057 · source Fibex4Ethernet/EthernetCommunication.py · adds autosarConnector, doIpSourceAddressRef/doIpTargetAddressRef, ident → TpConnectionIdent, localPortRef/remotePortRef → SocketAddress Ref, nPduRef, socketProtocol)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
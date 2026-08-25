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
- [ ] CouplingPortTrafficClassAssignment (value type · Table 3.75 · used by CouplingPortDetails.ethernetTrafficClassAssignments) · steps complete commit 30c86e62 — STAMP DEFERRED (batch 9b pending)
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - [x] Step 9 — Verify (9a) + confirm (9b)
- [ ] CanXlProps (value type · existing EthernetCommunication.py · used by EthernetCommunicationConnector.canXlPropsRefs / apApplicationEndpoint) · steps complete commit 4169b432 — STAMP DEFERRED (batch 9b pending)
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - [x] Step 9 — Verify (9a) + confirm (9b)
- [ ] TagWithOptionalValue (value type · Table 6.159 (CP) / 4.76 (FO) · used by SdClientConfig.capabilityRecord, AbstractServiceInstance.capabilityRecords) · steps complete commit 5241d431 — STAMP DEFERRED (batch 9b pending)
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - [x] Step 9 — Verify (9a) + confirm (9b)

### Member types — ADDED 2026-08-25 after user review (docs/plan/check.md) — Rule 0016.4/0016.5: sync BEFORE their consumers

- [ ] Ipv4DhcpServerConfiguration (value type · Table 3.80 · p.132 · used by DhcpServerConfiguration.ipv4DhcpServerConfiguration · source EthernetTopology.py · resolves DhcpServerConfiguration stub deviation; attrs addressRangeLowerBound, addressRangeUpperBound, defaultGateway, defaultLeaseTime, dnsServerAddresses *, networkMask) — STAMP DEFERRED (batch 9b pending)
  - [x] Step 1 — Sync members & description from spec
    (Table 3.80 in markdown AUTOSAR_CP_TPS_SystemTemplate.md:3568–3575 + PDF p.132;
    Base ARObject+Describable → Describable; 6 attr rows incl. dnsServerAddress * with xml.namePlural=DNS-SERVER-ADDRESSES)
  - [x] Step 2 — Write model class unit test (Red)
    (TestEthernetTopology.test_ipv4_dhcp_server_configuration_* added; Red confirmed — AttributeError)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
    (fresh implementation: class Note verbatim + per-attribute Notes verbatim, spec typo "Pv4" kept verbatim; None-no-op sentences appended)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
    (tests/test_armodel/writer/test_dhcp_server_configuration.py TestIpv4DhcpServerConfigurationWrite/RoundTrip; Red confirmed — 5 failed)
  - [x] Step 6 — Update parser & writer (Green)
    (writer setIpv4DhcpServerConfiguration + DNS-SERVER-ADDRESSES wrapper loop wired into setDhcpServerConfiguration;
    parser getIpv4DhcpServerConfiguration via mutators wired into getDhcpServerConfiguration)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
    (tracker: new Ipv4DhcpServerConfiguration section, zero deviations; DhcpServerConfiguration stub row removed)
  - [x] Step 9 — Verify (9a) + confirm (9b)
    (9a automated verification only — pytest 7270 passed, black/black-check/lint clean; 9b stamp DEFERRED to batch pass)
- [ ] Ipv6DhcpServerConfiguration (value type · Table 3.81 · p.132 · used by DhcpServerConfiguration.ipv6DhcpServerConfiguration · source EthernetTopology.py · resolves DhcpServerConfiguration stub deviation; same attr set as Ipv4 variant with Ip6AddressString types) — STAMP DEFERRED (batch 9b pending)
  - [x] Step 1 — Sync members & description from spec
    (Table 3.81 in markdown AUTOSAR_CP_TPS_SystemTemplate.md:3577–3616 + PDF p.132;
    Base ARObject+Describable → Describable; 6 attr rows, Ip6AddressString types)
  - [x] Step 2 — Write model class unit test (Red)
    (TestEthernetTopology.test_ipv6_dhcp_server_configuration_* added; Red confirmed — 3 failed AttributeError)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
    (fresh implementation: class Note + per-attribute Notes verbatim incl. spec's "Notation 255.255.255.255" on defaultGateway/networkMask rows kept verbatim)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
    (test_dhcp_server_configuration.py TestIpv6DhcpServerConfigurationWrite/RoundTrip; Red confirmed — 6 failed)
  - [x] Step 6 — Update parser & writer (Green)
    (writer setIpv6DhcpServerConfiguration wired into setDhcpServerConfiguration replacing empty-SubElement branch;
    parser getIpv6DhcpServerConfiguration via mutators wired into getDhcpServerConfiguration)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
    (tracker: new Ipv6DhcpServerConfiguration section, zero deviations; DhcpServerConfiguration Ipv6 stub row removed)
  - [x] Step 9 — Verify (9a) + confirm (9b)
    (9a automated verification only — pytest 7279 passed, black/black-check/lint clean; 9b stamp DEFERRED to batch pass)
- [ ] AnyServiceInstanceId (primitive · FO_TPS_GenericStructureTemplate Table E.6 · p.423 · used by ConsumedServiceInstance.instanceIdentifier · resolves String placeholder) — STAMP DEFERRED (batch 9b pending)
  - [x] Step 1 — Sync members & description from spec
    (Table E.6 in markdown AUTOSAR_FO_TPS_GenericStructureTemplate.md:11455–11461 + PDF p.423;
    Primitive in GeneralTemplateClasses::PrimitiveTypes; Note verbatim, Tags stripped per Rule 0012)
  - [x] Step 2 — Write model class unit test (Red)
    (TestAnyServiceInstanceId in test_PrimitiveTypes.py; Red confirmed — ImportError at collection)
  - [x] Step 3 — Implement model class (Green)
    (ARLiteral subclass mirroring PositiveInteger/CategoryString conventions)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
    (fresh implementation: class docstring = Table E.6 Note verbatim incl. Tags block per primitive convention)
  - [x] Step 5 — Write reader/writer round-trip test (N/A — standalone primitive, no own XML element;
    round-tripped via consuming class ConsumedServiceInstance.instanceIdentifier in its RE-FIX row)
  - [x] Step 6 — Update parser & writer (N/A — same reason as Step 5)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
    (none; ConsumedServiceInstance instanceIdentifier placeholder row resolved by the RE-FIX row)
  - [x] Step 9 — Verify (9a) + confirm (9b)
    (9a automated verification only — pytest 7283 passed, black/black-check/lint clean; 9b stamp DEFERRED to batch pass)
- [ ] AnyVersionString (primitive · FO_TPS_GenericStructureTemplate Table E.7 · used by ConsumedServiceInstance.minorVersion · resolves String placeholder)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] ServiceVersionAcceptanceKindEnum (enum · Table F.113 · used by ConsumedServiceInstance.versionDrivenFindBehavior · resolves ARLiteral placeholder · Steps 5/6 N/A if standalone enum)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (N/A if standalone enum)
  - [ ] Step 6 — Update parser & writer (N/A if standalone enum)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] PduActivationRoutingGroup (Table 6.161 · used by ConsumedEventGroup.pduActivationRoutingGroups AND AbstractServiceInstance.methodActivationRoutingGroup · Identifiable child → createXxx(short_name))
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] StaticSocketConnection (Table 6.201 · used by SocketAddress.staticSocketConnections · resolves ARObject placeholder)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] UdpChecksumCalculationEnum (enum · Table 6.119 · used by SocketAddress.udpChecksumHandling · resolves ARLiteral placeholder · Steps 5/6 N/A if standalone enum)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (N/A if standalone enum)
  - [ ] Step 6 — Update parser & writer (N/A if standalone enum)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)

## RE-FIX rows (user review docs/plan/check.md 2026-08-25 — consumers of the member types above; re-run after their member classes land)

- [ ] DhcpServerConfiguration RE-FIX (class docstring partial + member docstrings incorrect per user; full verbatim Notes incl. Tables 3.80/3.81 aggregation roles once Ipv4/Ipv6 subclasses are real)
- [ ] ConsumedServiceInstance RE-FIX (member types incorrect per user: retype instanceIdentifier → AnyServiceInstanceId, minorVersion → AnyVersionString, versionDrivenFindBehavior → ServiceVersionAcceptanceKindEnum once those classes land; remove resolved deviation rows)
- [ ] ConsumedEventGroup RE-FIX (missing member class per user: type pduActivationRoutingGroups → List[PduActivationRoutingGroup] with reader/writer coverage once it lands; remove resolved deviation row)
- [ ] SocketAddress RE-FIX (type staticSocketConnections → List[StaticSocketConnection], udpChecksumHandling → UdpChecksumCalculationEnum once they land; remove resolved deviation rows)
- [ ] CanXlProps NOT CONFIRMED by user (reason pending clarification; canConfig placeholder may resolve via CanControllerConfiguration Table 3.14)

### Input ethernet classes — sync AFTER their member types (Rule 0016.5)

- [ ] ConsumedEventGroup (markdown SoftwareComponentTemplate · Table 6.168 · p.978 · source Fibex4Ethernet/ServiceInstances.py · depends on SomeipSdClientEventGroupTimingConfig above; sdClientTimerConfig is a ref to it; adds instanceIdentifier) · steps complete commit d17132bf — STAMP DEFERRED (batch 9b pending); RE-FIX queued: type pduActivationRoutingGroups → List[PduActivationRoutingGroup]
  NOTE: Table 6.168 verified in AUTOSAR_CP_TPS_SystemTemplate.md + PDF pp.504–505 — the table has NO
  instanceIdentifier row; the XSD marks it atp.Status="removed" since 4.4.0, so it was NOT modeled
  (Rule 0015 / "the table wins"). Queue note above is stale.
  - [x] Step 1 — Sync members & description from spec
    (Table 6.168 verified in markdown AUTOSAR_CP_TPS_SystemTemplate.md:13315–13351 + PDF pp.504–505;
    NO instanceIdentifier row exists — XSD marks it atp.Status="removed" since 4.4.0, Rule 0015: not modeled)
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - [x] Step 9 — Verify (9a) + confirm (9b)
- [ ] ConsumedServiceInstance (markdown SoftwareComponentTemplate · Table 6.167 · p.980 · source Fibex4Ethernet/ServiceInstances.py · base AbstractServiceInstance below; depends on SomeipSdClientServiceInstanceConfig / SomeipServiceVersion above; adds blacklistedVersion, eventMulticastSubscriptionAddress, sdClientTimerConfig refs) · steps complete commit 7f27fb60 — STAMP DEFERRED (batch 9b pending)
  NOTE: Table 6.167 verified in AUTOSAR_CP_TPS_SystemTemplate.md:13252–13262 + PDF p.501 (pdf_page.py
  authoritative) — the SoftwareComponentTemplate citation above was stale; Base row includes
  AbstractServiceInstance; 14 Attribute rows across two page blocks.
  - [x] Step 1 — Sync members & description from spec
    (Table 6.167 verified in markdown AUTOSAR_CP_TPS_SystemTemplate.md:13252–13262 + PDF p.501;
    Base row = ARObject, AbstractServiceInstance, Identifiable, MultilanguageReferrable, Referrable;
    14 Attribute rows across two page blocks)
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - [x] Step 9 — Verify (9a) + confirm (9b)
    (9a automated verification only — pytest 7223 passed, black/black-check/lint clean,
    checklist==methods 1:1 source order, verbatim Note diff OK; 9b stamp DEFERRED to batch pass)
- [ ] AbstractServiceInstance (markdown SystemTemplate · Table 6.158 · p.476 · source Fibex4Ethernet/ServiceInstances.py · base of ConsumedServiceInstance / ProvidedServiceInstance; depends on TagWithOptionalValue above; fixes methodActivationRoutingGroup & routingGroupRefs member types) · steps complete commit 9b0023ed — STAMP DEFERRED (batch 9b pending)
  NOTE: Table 6.158 verified in AUTOSAR_CP_TPS_SystemTemplate.md:12736–12752 + PDF p.477 (pdf_page.py
  authoritative). No explicit Base row in the table — XSD group ABSTRACT-SERVICE-INSTANCE is
  incorporated into IDENTIFIABLE-extending subclasses; Python base stays (Identifiable, ABC). No
  class-level Note row; post-table prose paragraph used as class docstring. 4 Attribute rows: capabilityRecord (* aggr
  TagWithOptionalValue), majorVersion (0..1 attr PositiveInteger), methodActivationRoutingGroup (0..1
  aggr PduActivationRoutingGroup — class not yet implemented, ARObject placeholder),
  routingGroup (* ref SoAdRoutingGroup, atp.Status=obsolete).
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
    (tests written first; suite green against HEAD since runtime behavior already conformed —
    red gate proven via mutation check: guard removal → test_add_get_routingGroupRefs FAILED,
    source restored byte-identical)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
    (old class docstring + trailing # type: comments wiped; class Note → class docstring;
    per-attribute Note verbatim → __init__ comments + getter/setter docstrings; None-no-op
    sentences appended on guarded setters/adders; Stereotypes/Tags tails dropped per Rule 0012)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
    (tests/test_armodel/writer/test_abstract_service_instance.py: write_all_fields,
    round_trip_preserves_all_values, reader_empty_fields, provided-side base-attrs round trip;
    Red confirmed — 3 failed / 2 passed before parser+writer wiring)
  - [x] Step 6 — Update parser & writer (Green)
    (reader: getTagWithOptionalValues/addCapabilityRecord/setMajorVersion/addRoutingGroupRef wired
    into readConsumedServiceInstance AND readProvidedServiceInstance via mutators; writer: matched
    setTagWithOptionalValues/getCapabilityRecords/getMajorVersion/getRoutingGroupRefs pairs; no
    chained mutators; methodActivationRoutingGroup reader/writer pending — class not implemented)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
    (tracker entry updated: page 476→477; stale routingGroupRefs type row removed; placeholder row
    added for methodActivationRoutingGroup per Rule 0001.10/0014)
  - [x] Step 9 — Verify (9a) + confirm (9b)
    (9a automated verification only — pytest 7232 passed incl. lossless integration round trip,
    black/black-check/lint clean, checklist==methods 1:1 source order, verbatim Note diff OK,
    no receiver-chain mutators in new code; 9b stamp DEFERRED to batch pass)
- [ ] ApplicationEndpoint (markdown SystemTemplate · Table 6.124 · p.458 · source Fibex4Ethernet/ServiceInstances.py · adds discoveryTechnology, remotingTechnology, serializationTechnologyRef; these tech member types are XSD/ad-hoc — handle inside this sync) · steps complete commit 92517479 — STAMP DEFERRED (batch 9b pending)
  NOTE: Table 6.124 verified in AUTOSAR_CP_TPS_SystemTemplate.md:12091–12115 + PDF p.458 (pdf_page.py
  authoritative; p.457 above was stale). The table has NO discoveryTechnology/remotingTechnology/
  serializationTechnologyRef rows; XSD marks all three atp.Status="removed" — NOT modeled
  (Rule 0015 / "the table wins"); tracker records them as deprecated. Queue note above is stale.
  - [x] Step 1 — Sync members & description from spec
    (page-split table: rows before caption = pp.457–458 group 1 (consumedServiceInstance,
    maxNumberOfConnections), after caption group 2 (networkEndpoint, priority, providedServiceInstance,
    tlsCryptoMapping, tpConfiguration); Base = ARObject, Identifiable, MultilanguageReferrable,
    Referrable → Identifiable; Aggregated by SocketAddress.applicationEndpoint → no ARPackage dispatch)
  - [x] Step 2 — Write model class unit test (Red)
    (TestApplicationEndpoint added to test_ServiceInstances.py; Red confirmed — 7 failed / 1 passed)
  - [x] Step 3 — Implement model class (Green)
    (typed Optional/List fields, guarded setters, typed IsElementExists/getElement create factories;
    66 passed in file incl. siblings)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
    (class Note verbatim → class docstring; per-attribute Note verbatim → __init__ comments +
    getter/setter docstrings; None-no-op sentences appended; Tags tails dropped per Rule 0012)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
    (tests/test_armodel/writer/test_application_endpoint.py: write_all_fields,
    write_empty_fields_omits_optional_tags, round_trip_preserves_all_values, reader_empty_fields;
    Red confirmed — 2 failed / 2 passed before parser+writer wiring)
  - [x] Step 6 — Update parser & writer (Green)
    (reader: readIdentifiable added + setMaxNumberOfConnections/setTlsCryptoMappingRef wired into
    readSocketAddressApplicationEndpoint; writer matched getMaxNumberOfConnections/
    getTlsCryptoMappingRef pairs in XSD sequence order; no chained mutators)
  - [x] Step 7 — Update checklist comment
    (# Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.124, p.458; 15 method rows, source order)
  - [x] Step 8 — Deviations
    (tracker entry updated: page 457→458, package corrected to EthernetTopology, stale
    consumedServiceInstance missing row removed, three atp.Status="removed" technology members recorded)
  - [x] Step 9 — Verify (9a) + confirm (9b)
    (9a automated verification only — pytest 7244 passed incl. lossless integration round trip,
    black/black-check/lint clean, checklist==methods 1:1 source order, verbatim Note diff OK,
    no receiver-chain mutators in new code; 9b stamp DEFERRED to batch pass)
- [ ] SocketAddress (markdown SystemTemplate · Table 6.118 · p.453 · source Fibex4Ethernet/ServiceInstances.py · fixes applicationEndpoint type; adds ipAddress) · steps complete commit 1d699cf8 — STAMP DEFERRED (batch 9b pending)
  NOTE: Table 6.118 verified in AUTOSAR_CP_TPS_SystemTemplate.md:11940–11969 (page-split table:
  group 1 before caption, group 2 after) + PDF p.453 (pdf_page.py authoritative; p.452 above was
  stale). The table has NO ipAddress row (and NO portAddress row); both are deprecated XSD-only
  elements ("replaced by the aggregated NetworkEndpoint/ApplicationEndpoint") — NOT modeled, the
  pre-existing portAddress field/accessors/reader/writer removed (Rule 0015 / "the table wins");
  tracker records the resolution. Queue note "adds ipAddress" is stale.
  - [x] Step 1 — Sync members & description from spec
    (page-split table: rows before caption = allowedIPv6ExtHeaders, allowedTcpOptions,
    applicationEndpoint, connector, differentiatedServiceField, flowLabel; after caption =
    multicastConnector, pathMtuDiscoveryEnabled, pduCollectionMaxBufferSize, pduCollectionTimeout,
    staticSocketConnection, udpChecksumHandling; Base = ARObject, Identifiable,
    MultilanguageReferrable, Referrable → Identifiable; Aggregated by SoAdConfig.socketAddress →
    no ARPackage dispatch)
  - [x] Step 2 — Write model class unit test (Red)
    (TestSocketAddress added to test_ServiceInstances.py; Red confirmed — 13 failed)
  - [x] Step 3 — Implement model class (Green)
    (typed Optional/List fields, guarded setters returning self, createApplicationEndpoint with
    IsElementExists/getElement + addElement; legacy test_SocketAddress updated to synced API;
    79 passed in file incl. siblings)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
    (class Note verbatim → class docstring; per-attribute Note verbatim → __init__ comments +
    getter/setter docstrings; None-no-op sentences appended; Stereotypes/Tags tails dropped per
    Rule 0012)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
    (tests/test_armodel/writer/test_socket_address.py: write_all_fields,
    write_empty_fields_omits_optional_tags, round_trip_preserves_all_values, reader_empty_fields;
    Red confirmed — 4 failed incl. stale setPortAddress AttributeError before parser+writer wiring)
  - [x] Step 6 — Update parser & writer (Green)
    (reader: ALLOWED-I-PV-6-EXT-HEADERS-REF/ALLOWED-TCP-OPTIONS-REF/DIFFERENTIATED-SERVICE-FIELD/
    FLOW-LABEL/PATH-MTU-DISCOVERY-ENABLED/PDU-COLLECTION-MAX-BUFFER-SIZE/PDU-COLLECTION-TIMEOUT/
    UDP-CHECKSUM-HANDLING wired via mutators in XSD sequence order, PORT-ADDRESS read removed;
    writer matched getXxx pairs same order; no chained mutators)
  - [x] Step 7 — Update checklist comment
    (# Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.118, p.453; 25 method rows, source order;
    staticSocketConnections reader/writer [—] pending child class)
  - [x] Step 8 — Deviations
    (tracker entry added: staticSocketConnections ARObject placeholder + udpChecksumHandling
    ARLiteral placeholder per Rule 0001.10; portAddress/ipAddress Rule 0015 resolution recorded;
    stale queue note documented)
  - [x] Step 9 — Verify (9a) + confirm (9b)
    (9a automated verification only — pytest 7261 passed incl. lossless integration round trip,
    black/black-check/lint clean, checklist==methods 1:1 source order, verbatim Note diff OK,
    no receiver-chain mutators in new code; 9b stamp DEFERRED to batch pass)
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
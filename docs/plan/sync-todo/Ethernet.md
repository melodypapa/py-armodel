# Sync todo: Fibex4Ethernet ethernet-related class cluster (SystemTemplate / SoftwareComponentTemplate)

Input scope: 17 ethernet-related classes in `M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet`,
selected by user from `docs/examples/method_deviation_by_class.md` (all without a `# Spec verified:`
stamp). Generated: 2026-08-23. Queue updated 2026-08-24: the previously "Skip (placeholder)" member
types are now PROMOTED into the queue as class rows and MUST be synced before their dependents per
Rule 0016.5 (member-type-first ordering). Queue re-audited 2026-08-24 against markdown: XSD-only
atpVariation `...RefConditional` / `...Conditional` wrappers, the obsolete SoAd enum classes, and the
ad-hoc technology enum classes were REMOVED from the queue (markdown is authoritative — Rule 0002 /
user decision); rows retargeted to the real markdown-documented classes.
**2026-08-26 — Rule 0007 (package location) audit + fix applied:** module layout now matches the spec
`Package` rows. `ApplicationEndpoint`, `Ipv6Configuration`, `InfrastructureServices` and the former
`NetworkEndpoint.py` classes moved into `EthernetTopology.py`; `SocketConnection`,
`SocketConnectionIpduIdentifier`, `SocketConnectionBundle`, `SoAdRoutingGroup` moved into the new
`ObsoleteModel.py` (Tables F.115/F.116); `CanControllerConfiguration` + `CanXlProps` moved into
`Fibex4Can/CanTopology.py`. `NetworkEndpoint.py` and `EthernetCommunication.py` deleted. Row notes
below carry per-class `MOVED ... per Rule 0007` markers. **Correction:** `SocketConnection` is NOT an
XSD-only class — Table F.116 exists in the R23-11 obsolete-model appendix (package ObsoleteModel).
**2026-08-26 — Ipv6Configuration member-type fix (user-reported):** `ipAddressKeepBehavior` was typed
ARLiteral but the spec (Table 6.138) says `IpAddressKeepEnum`; `ipv6AddressSource` was typed ARLiteral
but the spec (Table 6.140) says `Ipv6AddressSourceEnum`. Both AREnum classes implemented in
`EthernetTopology.py`, members retyped, parser constructs the enums; the two placeholder deviation
rows removed. `Ipv4Configuration.ipAddressKeepBehavior`/`ipv4AddressSource` have the SAME latent
mismatch (Ipv4AddressSourceEnum Table 6.137) — Ipv4Configuration is legacy/not queued, not yet retyped.
**2026-08-26 — member-type audit across the whole queue:** applied the Ipv6Configuration check to every
queued class. 15 missing member types found (placeholder ARLiteral/ARObject where real spec classes exist)
and ADDED as queue rows with 9-step sub-checklists below ("Member types — ADDED 2026-08-26"): 9 enums
(EventGroupControlTypeEnum 6.162, TcpRoleEnum F.135, EthernetConnectionNegotiationEnum 3.55,
CouplingPortRoleEnum F.38, EthernetMacLayerTypeEnum 3.56, EthernetPhysicalLayerTypeEnum 3.57,
EthernetSwitchVlanIngressTagEnum 3.58, TimeSyncTechnologyEnum 6.149, DoIpEntityRoleEnum 6.151) + 6 classes
(MacSecProps 3.118/SecureCommunication, PlcaProps 3.117, CouplingPortConnection 3.60,
GlobalTimeCouplingPortProps 9.18, CouplingPortAbstractShaper XSD-only, OrderedMaster 6.148).
These must sync BEFORE their consumers per Rule 0016.5 and resolve the placeholder deviation rows below.
Ref-target classes stored as RefType (SoConIPduIdentifier 6.163, EthernetWakeupSleepOnDatalineConfig 3.115/Set 3.116,
PncMappingIdent F.95) are NOT placeholder mismatches and are NOT queued.
**Policy (2026-08-26) — unstamped while a member type is missing:** a class whose member type is missing
is UNSTAMPED — the `# Spec verified:` marker (Rule 0012.1) is blocked until the member type is synced and
the placeholder deviation row is removed. The consumer rows marked `UNSTAMPED` below are excluded from the
batch 9b stamping until their queued member types land (Rule 0016.5 member-type-first).
**2026-08-28 — status synced to feature branch commits:** the member-type rows landed, including
`MacSecProps` (3.118, commit a150ffd2). `ApplicationEndpoint` was stamped in commit 4164139d and its
queue record is now complete. Consumers whose Step 9 was previously blocked by member types remain
marked STAMP DEFERRED pending batch 9b confirmation. `SocketConnection` remains unstamped because
`SoAdConnectorType`/`SoAdProtocolType` are XSD-only placeholders per Rule 0002. Most `# Spec verified:`
markers remain deferred pending the batch confirmation pass.
(resume = first class row still `[ ]`; all class rows `[x]` = sync finished)

**2026-08-29 — queue status: ALL 60 class rows `[x]` — SYNC FINISHED.** Final sessions: the
SocketConnection R4.3.1 resync family (EthernetCommunication.py), then the missing member-type
closure classes IPv6ExtHeaderFilterList (Table 6.129, parser/writer N/A — XSD-absent in both
releases) and TcpOptionFilterList (Table 6.131, parser/writer wired via the new TcpOptionFilterSet
Table 6.130 per user request), plus completion of the SocketConnectionIpduIdentifier /
SocketConnectionBundle wiring per the R4.3.1 XSD groups. All `# Spec verified:` markers remain
WITHHELD pending the batch 9b confirmation pass (standing queue policy). One open spec question for
a future pass: R4.3.1 markdown Table 6.120 lists only 2 SocketConnection attributes while the
R4.3.1 XSD SOCKET-CONNECTION group carries the full member set (incl. ALLOWED-I-PV-6-EXT-HEADERS-REF
/ ALLOWED-TCP-OPTIONS-REF) — the markdown conversion dropped the continuation rows of the
figure-split table; the model currently follows the markdown table (Rule 0015).

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

- [x] SomeipSdClientServiceInstanceConfig (ARElement value type · Table F.117 · p.2059 · used by ConsumedServiceInstance.sdClientTimerConfig · source ServiceInstances.py · adds initialFindBehavior aggr InitialSdDelayConfig, priority attr, serviceFindTimeToLive attr) — STAMPED R23-11 <!-- commit: fa198376 -->
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - [x] Step 9 — Verify (9a) + confirm (9b)
- [x] SomeipSdClientEventGroupTimingConfig (ARElement value type · Table 6.173 · p.1162 · used by ConsumedEventGroup.sdClientTimerConfig · source ServiceInstances.py · adds requestResponseDelay aggr RequestResponseDelay, subscribeEventgroupRetryDelay attr TimeValue, subscribeEventgroupRetryMax attr, timeToLive attr) · steps complete commit 0e472ca8 — STAMPED R23-11 — commit bae4ecae
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - [x] Step 9 — Verify (9a) + confirm (9b)
- [x] SomeipSdServerEventGroupTimingConfig (ARElement value type · Table 6.172 · p.1162 · used by EventHandler.sdServerEgTimingConfig · source ServiceInstances.py · adds requestResponseDelay aggr RequestResponseDelay) · steps complete commit 601f7bd5 — STAMPED R23-11 — commit 412c6eb5
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - [x] Step 9 — Verify (9a) + confirm (9b)
- [x] SomeipServiceVersion (ARObject value type · Table F.118 · used by ConsumedServiceInstance.blacklistedVersion · source ServiceInstances.py · adds majorVersion, minorVersion) · steps complete commit 152f3113 — STAMPED R23-11 — commit 98f6f205
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - [x] Step 9 — Verify (9a) + confirm (9b)
- [x] DhcpServerConfiguration (value type · Table 3.79 · used by InfrastructureServices.dhcpServerConfiguration, VlanMembership.dhcpAddressAssignment) · steps complete commit ecfa6c40 — STAMPED R23-11 — commit 026d9fb4
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - [x] Step 9 — Verify (9a) + confirm (9b)
- [x] CouplingPortTrafficClassAssignment (value type · Table 3.75 · used by CouplingPortDetails.ethernetTrafficClassAssignments) · steps complete commit 30c86e62 — STAMPED R23-11
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - [x] Step 9 — Verify (9a) + confirm (9b)
- [x] CanXlProps (value type · existing Fibex4Can/CanTopology.py — MOVED from EthernetCommunication.py per Rule 0007: no CP table, CAN-XL domain, aggregated by CanControllerConfiguration · used by EthernetCommunicationConnector.canXlPropsRefs / apApplicationEndpoint) · steps complete commit 4169b432 — XSD verified (AUTOSAR_00052.xsd, Rule 0002 exclusion — no CP marker) — commit 112b2fac
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - [x] Step 9 — Verify (9a) + confirm (9b)
- [x] TagWithOptionalValue (value type · Table 6.159 (CP) / 4.76 (FO) · used by SdClientConfig.capabilityRecord, AbstractServiceInstance.capabilityRecords) · steps complete commit 5241d431 — STAMPED R23-11
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

- [x] Ipv4DhcpServerConfiguration (value type · Table 3.80 · p.132 · used by DhcpServerConfiguration.ipv4DhcpServerConfiguration · source EthernetTopology.py · resolves DhcpServerConfiguration stub deviation; attrs addressRangeLowerBound, addressRangeUpperBound, defaultGateway, defaultLeaseTime, dnsServerAddresses *, networkMask) — STAMPED R23-11
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
- [x] Ipv6DhcpServerConfiguration (value type · Table 3.81 · p.132 · used by DhcpServerConfiguration.ipv6DhcpServerConfiguration · source EthernetTopology.py · resolves DhcpServerConfiguration stub deviation; same attr set as Ipv4 variant with Ip6AddressString types) — STAMPED R23-11
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
- [x] AnyServiceInstanceId (primitive · FO_TPS_GenericStructureTemplate Table E.6 · p.423 · used by ConsumedServiceInstance.instanceIdentifier · resolves String placeholder) — STAMPED R23-11 — confirmed by user 2026-08-28
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
- [x] AnyVersionString (primitive · FO_TPS_GenericStructureTemplate Table E.7 · p.423 · used by ConsumedServiceInstance.minorVersion · resolves String placeholder) — STAMPED R23-11 — confirmed by user 2026-08-28
  - [x] Step 1 — Sync members & description from spec
    (Table E.7 in markdown AUTOSAR_FO_TPS_GenericStructureTemplate.md:11463–11468 + PDF p.423;
    Primitive in GeneralTemplateClasses::PrimitiveTypes; Note cell is Tags-only — docstring carries the Tags block verbatim)
  - [x] Step 2 — Write model class unit test (Red)
    (TestAnyVersionString in test_PrimitiveTypes.py; Red confirmed — ImportError at collection)
  - [x] Step 3 — Implement model class (Green)
    (ARLiteral subclass mirroring PrimitiveIdentifier/CategoryString conventions)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
    (fresh implementation: no Note prose in spec — Tags block verbatim only)
  - [x] Step 5 — Write reader/writer round-trip test (N/A — standalone primitive, no own XML element;
    round-tripped via consuming class ConsumedServiceInstance.minorVersion in its RE-FIX row)
  - [x] Step 6 — Update parser & writer (N/A — same reason as Step 5)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
    (none; ConsumedServiceInstance minorVersion placeholder row resolved by the RE-FIX row)
  - [x] Step 9 — Verify (9a) + confirm (9b)
    (9a automated verification only — pytest 7286 passed, black/black-check/lint clean; 9b stamp DEFERRED to batch pass)
- [x] ServiceVersionAcceptanceKindEnum (enum · Table F.113 · p.2057 · used by ConsumedServiceInstance.versionDrivenFindBehavior · resolves ARLiteral placeholder · Steps 5/6 N/A if standalone enum) — STAMPED R23-11 — confirmed by user 2026-08-28
  - [x] Step 1 — Sync members & description from spec
    (Table F.113 page-split: exactOrAnyMinorVersion before caption markdown AUTOSAR_CP_TPS_SystemTemplate.md,
    minimumMinorVersion after; PDF pp.2056–2057, caption p.2057 per pypdf — pdf_page.py regex cannot match "F.113";
    Package ServiceInstances; Note verbatim incl. spec typo "Defined the possible acceptance kinds")
  - [x] Step 2 — Write model class unit test (Red)
    (TestServiceVersionAcceptanceKindEnum in test_ServiceInstances.py; Red confirmed — ImportError at collection;
    fixed test to AREnum convention: members are plain string constants + getEnumValues order)
  - [x] Step 3 — Implement model class (Green)
    (AREnum subclass, first enum in Fibex4Ethernet/ServiceInstances.py; literals EXACT_OR_ANY_MINOR_VERSION/MINIMUM_MINOR_VERSION
    with verbatim Descriptions as member comments)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
    (fresh implementation: class Note verbatim; literal comments verbatim incl. Tags tails per AREnum convention)
  - [x] Step 5 — Write reader/writer round-trip test (N/A — standalone enum, no own XML element;
    round-tripped via consuming class ConsumedServiceInstance.versionDrivenFindBehavior in its RE-FIX row)
  - [x] Step 6 — Update parser & writer (N/A — same reason as Step 5)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
    (none; ConsumedServiceInstance versionDrivenFindBehavior placeholder row resolved by the RE-FIX row)
  - [x] Step 9 — Verify (9a) + confirm (9b)
    (9a automated verification only — pytest 7288 passed, black/black-check/lint clean; 9b stamp DEFERRED to batch pass)
- [x] PduActivationRoutingGroup (Table 6.161 · p.489 · used by ConsumedEventGroup.pduActivationRoutingGroups AND AbstractServiceInstance.methodActivationRoutingGroup · Identifiable child → createXxx(short_name)) — STAMPED R23-11 <!-- commit: b0f50f6f -->
  - [x] Step 1 — Sync members & description from spec
    (Table 6.161 page-split in markdown AUTOSAR_CP_TPS_SystemTemplate.md:12976–13000 + PDF p.489;
    Base → Identifiable; 3 attr rows: eventGroupControlType attr, iPduIdentifierTcp/Udp * refs)
  - [x] Step 2 — Write model class unit test (Red)
    (TestPduActivationRoutingGroup in test_ServiceInstances.py; Red confirmed — ImportError at collection)
  - [x] Step 3 — Implement model class (Green)
    (Identifiable with (parent, short_name); typed List fields for both ref lists, guarded setters/adders)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
    (fresh implementation: class Note + per-attribute Notes verbatim)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
    (tests/test_armodel/writer/test_pdu_activation_routing_group.py; Red confirmed — 4 failed)
  - [x] Step 6 — Update parser & writer (Green)
    (writer setPduActivationRoutingGroup: writeIdentifiable + EVENT-GROUP-CONTROL-TYPE + both wrapper ref lists;
    parser getPduActivationRoutingGroup: getShortName + readIdentifiable + mutators)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
    (tracker: eventGroupControlType ARLiteral placeholder — EventGroupControlTypeEnum Table 6.162 queued 2026-08-26 (see Member types ADDED);
     iPduIdentifierTcp/Udp singular→plural convention noted; consumer wiring pending RE-FIX rows)
  - [x] Step 9 — Verify (9a) + confirm (9b)
    (9a automated verification only — pytest 7406 passed, black/black-check/lint clean; 9b stamp DEFERRED to batch pass; placeholder resolved once EventGroupControlTypeEnum landed — reader/writer now construct the enum)
- [x] StaticSocketConnection (Table 6.201 · p.544 · used by SocketAddress.staticSocketConnections · resolves ARObject placeholder) — STAMPED R23-11 <!-- commit: 2501d6ed -->
  - [x] Step 1 — Sync members & description from spec
    (Table 6.201 page-split in markdown AUTOSAR_CP_TPS_SystemTemplate.md:14280–14310 + PDF p.544;
    Base → Identifiable; 4 attr rows: iPduIdentifier * ref, remoteAddress 0..1 ref, tcpConnectTimeout attr, tcpRole attr;
    XSD serialization uses atpVariation conditional wrappers)
  - [x] Step 2 — Write model class unit test (Red)
    (TestStaticSocketConnection in test_ServiceInstances.py; Red confirmed — ImportError at collection)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
    (fresh implementation: class Note + per-attribute Notes verbatim, Stereotypes/Tags tails stripped per Rule 0012)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
    (tests/test_armodel/writer/test_static_socket_connection.py; Red confirmed — 4 failed)
  - [x] Step 6 — Update parser & writer (Green)
    (writer setStaticSocketConnection incl. conditional wrappers; parser getStaticSocketConnection via mutators;
     consumer wiring into SocketAddress pending its RE-FIX row)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
    (tracker: tcpRole ARLiteral placeholder — TcpRoleEnum Table F.135 queued 2026-08-26 (see Member types ADDED);
     iPduIdentifier/remoteAddress singular→plural/ref naming noted; SocketAddress placeholder row resolved by RE-FIX)
  - [x] Step 9 — Verify (9a) + confirm (9b)
    (9a automated verification only — pytest 7406 passed, black/black-check/lint clean; 9b stamp DEFERRED to batch pass; tcpRole placeholder resolved once TcpRoleEnum landed)
- [x] UdpChecksumCalculationEnum (enum · Table 6.119 · p.454 · used by SocketAddress.udpChecksumHandling · resolves ARLiteral placeholder · Steps 5/6 N/A if standalone enum) — STAMPED R23-11 <!-- commit: f8d50c9e -->
  - [x] Step 1 — Sync members & description from spec
    (Table 6.119 in markdown AUTOSAR_CP_TPS_SystemTemplate.md:11988–11997 + PDF p.454;
    Package ServiceInstances; literals udpChecksumEnabled idx0 / udpChecksumDisabled idx1 — display order differs from index order,
    enum member list follows EnumerationLiteralIndex)
  - [x] Step 2 — Write model class unit test (Red)
    (TestUdpChecksumCalculationEnum in test_ServiceInstances.py; Red confirmed — ImportError at collection)
  - [x] Step 3 — Implement model class (Green)
    (AREnum subclass next to ServiceVersionAcceptanceKindEnum)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
    (fresh implementation: class Note verbatim; literal comments verbatim incl. Tags tails per AREnum convention)
  - [x] Step 5 — Write reader/writer round-trip test (N/A — standalone enum, no own XML element;
    round-tripped via consuming class SocketAddress.udpChecksumHandling in its RE-FIX row)
  - [x] Step 6 — Update parser & writer (N/A — same reason as Step 5)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
    (none; SocketAddress udpChecksumHandling placeholder row resolved by the RE-FIX row)
  - [x] Step 9 — Verify (9a) + confirm (9b)
    (9a automated verification only — pytest 7306 passed, black/black-check/lint clean; 9b stamp DEFERRED to batch pass)

### Member types — ADDED 2026-08-26 after Ipv6Configuration member-type audit (user-reported placeholder mismatch) — Rule 0016.4/0016.5: sync BEFORE their consumers

Same issue as Ipv6Configuration (ARLiteral/ARObject placeholder where a real spec class exists). Each row
resolves the placeholders recorded in its consumers' Step 8 deviation notes below and MUST sync before that
consumer is stamped. (Ref targets stored as RefType — SoConIPduIdentifier 6.163, EthernetWakeupSleepOnDatalineConfig
3.115/Set 3.116, PncMappingIdent F.95 — are NOT placeholder mismatches and are NOT queued; noted for completeness.
Retype-only gaps with no missing class are NOT queued: EthernetCommunicationController.macUnicastAddress uses
ARLiteral but MacAddressString exists in PrimitiveTypes.py; legacy Ipv4Configuration.ipv4AddressSource/
ipAddressKeepBehavior (Ipv4AddressSourceEnum 6.137 / IpAddressKeepEnum 6.138) — class not queued.)

- [x] EventGroupControlTypeEnum (enum · Table 6.162 · p.489 · used by PduActivationRoutingGroup.eventGroupControlType AND SoAdRoutingGroup.eventGroupControlType (EthernetCommunication.py, untyped `# type:` comment) · source ServiceInstances.py · resolves both ARLiteral placeholders · Steps 5/6 N/A if standalone enum) — STAMPED R23-11 <!-- commit: 27220004 -->
  - [x] Step 1 — Sync members & description from spec
    (Table 6.162 markdown AUTOSAR_CP_TPS_SystemTemplate.md:13005 + PDF p.489; Package ServiceInstances; 4 literals)
  - [x] Step 2 — Write model class unit test (Red)
    (TestEventGroupControlTypeEnum in test_ServiceInstances.py; Red confirmed — ImportError at collection)
  - [x] Step 3 — Implement model class (Green)
    (AREnum in ServiceInstances.py; literals ACTIVATION_AND_TRIGGER_UNICAST/ACTIVATION_MULTICAST/ACTIVATION_UNICAST/TRIGGER_UNICAST with verbatim Descriptions)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
    (class Note verbatim; literal comments verbatim incl. Tags tails per AREnum convention)
  - [x] Step 5 — Write reader/writer round-trip test (N/A — standalone enum, no own XML element; round-tripped via consuming classes)
  - [x] Step 6 — Update parser & writer (N/A — same reason as Step 5)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
    (none; PduActivationRoutingGroup + SoAdRoutingGroup placeholder rows resolved)
  - [x] Step 9 — Verify (9a) + confirm (9b)
    (9a automated verification only — pytest 7406 passed, black/black-check/lint clean; 9b stamp DEFERRED to batch pass)
- [x] TcpRoleEnum (enum · Table F.135 · p.2074 (obsolete appendix) · used by StaticSocketConnection.tcpRole · source ServiceInstances.py · resolves ARLiteral placeholder · Steps 5/6 N/A if standalone enum) — STAMPED R23-11 <!-- commit: ffe91a62 -->
  - [x] Step 1 — Sync members & description from spec
    (Table F.135 markdown AUTOSAR_CP_TPS_SystemTemplate.md:76140; obsolete appendix; 2 literals)
  - [x] Step 2 — Write model class unit test (Red)
    (TestTcpRoleEnum in test_ServiceInstances.py; Red confirmed)
  - [x] Step 3 — Implement model class (Green)
    (AREnum in ServiceInstances.py; literals CONNECT/LISTEN with verbatim Descriptions)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
    (class Note verbatim; literal comments verbatim incl. Tags tails per AREnum convention)
  - [x] Step 5 — Write reader/writer round-trip test (N/A — standalone enum, no own XML element; round-tripped via consuming class)
  - [x] Step 6 — Update parser & writer (N/A — same reason as Step 5)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
    (none; StaticSocketConnection tcpRole placeholder row resolved)
  - [x] Step 9 — Verify (9a) + confirm (9b)
    (9a automated verification only — pytest 7406 passed, black/black-check/lint clean; 9b stamp DEFERRED to batch pass)
- [x] EthernetConnectionNegotiationEnum (enum · Table 3.55 · p.110 · used by CouplingPort.connectionNegotiationBehavior · source EthernetTopology.py · resolves ARLiteral placeholder · Steps 5/6 N/A if standalone enum) — STAMPED R23-11 <!-- commit: 2324ea15 -->
  - [x] Step 1 — Sync members & description from spec
    (Table 3.55 markdown AUTOSAR_CP_TPS_SystemTemplate.md:2826 + PDF p.110)
  - [x] Step 2 — Write model class unit test (Red)
    (TestEthernetConnectionNegotiationEnum in test_EthernetTopology.py; Red confirmed)
  - [x] Step 3 — Implement model class (Green)
    (AREnum in EthernetTopology.py)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
    (class Note verbatim; literal comments verbatim incl. Tags tails per AREnum convention)
  - [x] Step 5 — Write reader/writer round-trip test (N/A — standalone enum, no own XML element; round-tripped via consuming class)
  - [x] Step 6 — Update parser & writer (N/A — same reason as Step 5)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
    (none; CouplingPort connectionNegotiationBehavior placeholder row resolved)
  - [x] Step 9 — Verify (9a) + confirm (9b)
    (9a automated verification only — pytest 7406 passed, black/black-check/lint clean; 9b stamp DEFERRED to batch pass)
- [x] CouplingPortRoleEnum (enum · Table F.38 · p.2013 (obsolete appendix) · used by CouplingPort.couplingPortRole · source EthernetTopology.py · resolves ARLiteral placeholder · Steps 5/6 N/A if standalone enum) — STAMPED R23-11 <!-- commit: 2112c650 -->
   - [x] Step 1 — Sync members & description from spec
     (Table F.38 markdown AUTOSAR_CP_TPS_SystemTemplate.md:74377; PDF p.2013; obsolete appendix; literal index order verified)
  - [x] Step 2 — Write model class unit test (Red)
    (TestCouplingPortRoleEnum in test_EthernetTopology.py; Red confirmed)
  - [x] Step 3 — Implement model class (Green)
    (AREnum in EthernetTopology.py)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
    (class Note verbatim; literal comments verbatim incl. Tags tails per AREnum convention)
  - [x] Step 5 — Write reader/writer round-trip test (N/A — standalone enum, no own XML element; round-tripped via consuming class)
  - [x] Step 6 — Update parser & writer (N/A — same reason as Step 5)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
    (none; CouplingPort couplingPortRole placeholder row resolved)
   - [x] Step 9 — Verify (9a) + confirm (9b)
     (full 9-step audit: page corrected to p.2013 and literal order corrected to EnumerationLiteralIndex; targeted verification pending after fix; 9b stamp DEFERRED pending user confirmation)
- [x] EthernetMacLayerTypeEnum (enum · Table 3.56 · p.110 · used by CouplingPort.macLayerType AND EthernetCommunicationController.macLayerType · source EthernetTopology.py · resolves both ARLiteral placeholders · Steps 5/6 N/A if standalone enum) — STAMPED R23-11 <!-- commit: 76fd3ca3 -->
  - [x] Step 1 — Sync members & description from spec
     (Table 3.56 markdown AUTOSAR_CP_TPS_SystemTemplate.md:2838 + PDF p.110; literal order corrected to EnumerationLiteralIndex: X-MII, XG-MII, XXG-MII)
  - [x] Step 2 — Write model class unit test (Red)
    (TestEthernetMacLayerTypeEnum in test_EthernetTopology.py; Red confirmed)
  - [x] Step 3 — Implement model class (Green)
    (AREnum in EthernetTopology.py)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
    (class Note verbatim; literal comments verbatim incl. Tags tails per AREnum convention)
  - [x] Step 5 — Write reader/writer round-trip test (N/A — standalone enum, no own XML element; round-tripped via consuming classes)
  - [x] Step 6 — Update parser & writer (N/A — same reason as Step 5)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
    (none; CouplingPort + EthernetCommunicationController macLayerType placeholder rows resolved)
  - [x] Step 9 — Verify (9a) + confirm (9b)
    (9a automated verification only — pytest 7406 passed, black/black-check/lint clean; 9b stamp DEFERRED to batch pass)
- [x] EthernetPhysicalLayerTypeEnum (enum · Table 3.57 · p.111 · used by CouplingPort.physicalLayerType · source EthernetTopology.py · resolves ARLiteral placeholder · Steps 5/6 N/A if standalone enum) — STAMPED R23-11 — confirmed by user 2026-08-28 <!-- commit: c7f99ac3 -->
  - [x] Step 1 — Sync members & description from spec
    (Table 3.57 markdown AUTOSAR_CP_TPS_SystemTemplate.md:2865 + PDF p.111)
  - [x] Step 2 — Write model class unit test (Red)
    (TestEthernetPhysicalLayerTypeEnum in test_EthernetTopology.py; Red confirmed)
  - [x] Step 3 — Implement model class (Green)
    (AREnum in EthernetTopology.py)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
    (class Note verbatim; literal comments verbatim incl. Tags tails per AREnum convention)
  - [x] Step 5 — Write reader/writer round-trip test (N/A for the enum itself — standalone, no own XML element; round-trip coverage asserted on the consuming class CouplingPort in test_coupling_port.py, added during 9b)
  - [x] Step 6 — Update parser & writer (N/A — same reason as Step 5)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
    (none; CouplingPort physicalLayerType placeholder row resolved)
  - [x] Step 9 — Verify (9a) + confirm (9b)
    (9a re-run 2026-08-28: pytest 8129 passed / 0 failed incl. integration round-trip, lint clean, black clean on all touched files; 9b confirmed by user 2026-08-28 — marker written)
    **9b findings resolved 2026-08-28:** (1) BLOCKER — `writeCouplingPort` never emitted `PHYSICAL-LAYER-TYPE` while `readCouplingPort` read it (silent round-trip drop). Fixed TDD-style: failing assertions added to `tests/test_armodel/writer/test_coupling_port.py` (write_all + round_trip), then `arxml_writer.py:9190` wired at the XSD sequence position. **Drift note (Rule 0012.3): the fix lands on CouplingPort, which is already stamped — not re-stamped here.** Pre-existing, NOT fixed: `writeCouplingPort` emits PLCA-PROPS before MAC-SEC-PROPS but the XSD order is MAC-SEC-PROPS → PHYSICAL-LAYER-TYPE → PLCA-PROPS. (2) `# Columns:` line added to the checklist block. (3) Literal comments restored to the full spec row verbatim (xml.name tails on all 6 literals + atp.Status=draft on _10BASE_T1S), matching the stamped EthernetMacLayerTypeEnum form; verified by diff against Table 3.57.
- [x] EthernetSwitchVlanIngressTagEnum (enum · Table 3.58 · p.111 · used by CouplingPort.receiveActivity · source EthernetTopology.py · resolves ARLiteral placeholder · Steps 5/6 N/A if standalone enum) — STAMPED R23-11 — confirmed by user 2026-08-28 <!-- commit: 92ab380a -->
  - [x] Step 1 — Sync members & description from spec
    (Table 3.58 markdown AUTOSAR_CP_TPS_SystemTemplate.md:2876 + PDF p.111)
  - [x] Step 2 — Write model class unit test (Red)
    (TestEthernetSwitchVlanIngressTagEnum in test_EthernetTopology.py; Red confirmed)
  - [x] Step 3 — Implement model class (Green)
    (AREnum in EthernetTopology.py)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
    (class Note verbatim; literal comments verbatim incl. Tags tails per AREnum convention)
  - [x] Step 5 — Write reader/writer round-trip test (N/A — standalone enum, no own XML element; round-tripped via consuming class)
  - [x] Step 6 — Update parser & writer (N/A — same reason as Step 5)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
    (none; CouplingPort receiveActivity placeholder row resolved)
  - [x] Step 9 — Verify (9a) + confirm (9b)
    (9a re-run 2026-08-28: pytest 8130 passed / 0 failed incl. integration round-trip, lint clean, black clean on all touched files; 9b confirmed by user 2026-08-28 — marker written)
    **9b findings resolved 2026-08-28:** (1) Member order — user decision: KEEP the existing `atp.EnumerationLiteralIndex` order (forwardAsIs=0, dropUntagged=1), matching EthernetMacLayerTypeEnum; the spec displays dropUntagged first and Rule 0011 mandates neither, and this file is split (CouplingPortRoleEnum uses display order). (2) `# Columns:` line added to the checklist block.
    **CouplingPort drift fixed here (Rule 0012.3, CouplingPort not re-stamped):** `writeCouplingPort` emitted its children out of XSD sequence. TDD: new `test_write_child_element_order_matches_xsd` in tests/test_armodel/writer/test_coupling_port.py failed first, then the writer was reordered to the AUTOSAR_00052.xsd group COUPLING-PORT sequence — this also moves PHYSICAL-LAYER-TYPE (added in the 3.57 session, where it was placed at the wrong slot) to its true XSD position. COUPLING-PORT-SPEED stays unmodelled: atp.Status=removed in the XSD (Rule 0015).
    **Open observation (not acted on):** Table 3.54 lists 13 attributes but the model also carries `wakeUpSleepOnDatalineConfigRef` (in the XSD, not in the R23-11 table). Also the queue note above claiming Table 3.54 "adds couplingPortSpeed" is stale — couplingPortSpeed is not in Table 3.54.
- [x] MacSecProps (class · Table 3.118 · p.173 · used by CouplingPort.macSecProps (List) · source SystemTemplate/SecureCommunication · **Phase 0 closure resolved 2026-08-27** — its member-type cluster was synced dependency-first in `docs/plan/sync-todo/MacSecProps.md` and landed in commit a150ffd2. Markdown Table 3.118 is GARBLED (mislabels MacSecLocalKayProps content); the PDF (pp.173–177) is authoritative.) — STAMPED R23-11
- [x] PlcaProps (class · Table 3.117 · p.169 · used by CouplingPort.plcaProps · source EthernetTopology.py · resolves ARObject placeholder; attrs plcaLocalNodeId, plcaMaxBurstCount, plcaMaxBurstTimer) · steps complete commit a264fe14 — STAMPED R23-11 — confirmed by user 2026-08-28 <!-- commit: 992fb55f -->
  - [x] Step 1 — Sync members & description from spec
    (Table 3.117 markdown AUTOSAR_CP_TPS_SystemTemplate.md:4580 + PDF p.169; Base ARObject; 3 attr rows)
  - [x] Step 2 — Write model class unit test (Red)
    (TestPlcaProps added; Red confirmed — AttributeError)
  - [x] Step 3 — Implement model class (Green)
    (ARObject with typed Optional[PositiveInteger] fields + guarded setters)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
    (class Note verbatim + per-attribute Notes verbatim; None-no-op sentences appended)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
    (tests/test_armodel/writer/test_plca_props.py; Red confirmed)
  - [x] Step 6 — Update parser & writer (Green)
    (parser getPlcaProps/setPlcaProps wired into CouplingPort; writer matched)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
    (none; CouplingPort plcaProps placeholder row resolved)
  - [x] Step 9 — Verify (9a) + confirm (9b)
    (9a 2026-08-28: pytest 8130 passed / 0 failed incl. integration round-trip, lint clean, black clean, parity script CLASSES untested=0; 9b confirmed by user 2026-08-28 — marker written)
    **Full 9-step re-sync (class had no marker, so steps 1–8 were re-verified rather than trusted):** implementation already matched Table 3.117 — Base ARObject, 3 PEP 526 members in spec/XSD order, guarded setters returning self, all docstrings verbatim. Only two real changes were needed: (1) extended `TestPlcaProps.test_none_no_op` to cover setPlcaMaxBurstCount/setPlcaMaxBurstTimer — previously removing those None guards passed silently; proven load-bearing by mutation (Red then Green). (2) Resolved the `plcaProps` placeholder row in docs/examples/method_deviation_by_class_v2.md (Rule 0014). Reader/writer round-trip coverage verified load-bearing by mutation: dropping either the writer or reader PLCA-MAX-BURST-* line fails tests/test_armodel/writer/test_plca_props.py.
    **Deviation tracker cleanup (user decision, same commit):** six further stale rows in the tracker's `CouplingPort` section claimed referenced types were "not yet implemented; carried as ARLiteral/ARObject" but the source already used the real classes — connectionNegotiationBehavior, couplingPortRole, macLayerType (x2: also the EthernetCommunicationController section), macSecProps, physicalLayerType, receiveActivity. All retyped with Deviation = '-'. CouplingPort itself is NOT re-stamped.
- [x] CouplingPortConnection (class · Table 3.60 · p.113 · used by EthernetCluster.couplingPortConnections (List) · source EthernetTopology.py · Base ARObject; attrs firstPort 0..1 ref CouplingPort, nodePort * ref CouplingPort, plcaLocalNodeCount, plcaTransmitOpportunityTimer, secondPort 0..1 ref CouplingPort · resolves ARObject placeholder) · steps complete commit a264fe14 — STAMPED R23-11 — confirmed by user 2026-08-28 <!-- commit: fda9fba6 -->
  - [x] Step 1 — Sync members & description from spec
    (Table 3.60 markdown AUTOSAR_CP_TPS_SystemTemplate.md:2920 + PDF p.113; Base ARObject; 5 attr rows)
  - [x] Step 2 — Write model class unit test (Red)
    (TestCouplingPortConnection in test_EthernetTopology.py; Red confirmed)
  - [x] Step 3 — Implement model class (Green)
    (typed Optional/List fields, guarded setters/adders)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
    (class Note verbatim + per-attribute Notes verbatim; None-no-op sentences appended)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
    (tests/test_armodel/writer/test_coupling_port_connection.py; Red confirmed)
  - [x] Step 6 — Update parser & writer (Green)
    (read/writeEthernetClusterCouplingPortConnections wired)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
    (none; EthernetCluster couplingPortConnections placeholder row resolved)
  - [x] Step 9 — Verify (9a) + confirm (9b)
    (9a 2026-08-28: pytest 8132 passed / 0 failed incl. integration round-trip, lint clean, black clean on all touched files, parity script CLASSES untested=0; 9b confirmed by user 2026-08-28 — marker written)
    **Spec source caveat:** markdown Table 3.60 is GARBLED — it is missing the Package/Note/Base/Aggregated-by rows and the whole `firstPort` attribute row. The table was taken from the PDF (pp.112–113); the 4 rows the markdown does carry match the PDF exactly, so only `firstPort`'s text is PDF-sourced (Rule 0015).
    **Full 9-step re-sync (no marker, so steps 1–8 re-verified, not trusted). Two real defects fixed:** (1) Rule 0001.5 naming — the three `ref` members lacked the Kind suffix. Renamed to `firstPortRef`, `nodePortRefs`/`addNodePortRef`, `secondPortRef` (XSD elements FIRST-PORT-REF / NODE-PORTS / SECOND-PORT-REF confirm; sibling CouplingPort already used the convention). **BREAKING public API change** — getFirstPort, setFirstPort, getNodePorts, addNodePort, getSecondPort, setSecondPort all renamed with the Ref/Refs suffix; no consumers outside src/ and tests/. Applied across model, parser, writer and both test files (Rule 0014: fix, do not record and leave). (2) The class docstring was TRUNCATED — it dropped "or between a collection of Ports that are all referenced by the portCollection reference." (Rule 0001.4/0012).
    **Tests strengthened, both proven Red-then-Green:** model test now covers None no-op on all four setters (previously only addNodePort was covered, so deleting the other guards passed silently); writer test asserts node-port ref values instead of `len(...) == 2` and adds an empty-NODE-PORTS write case.
    **Deviation tracker:** the `couplingPortConnections` row in the EthernetCluster section was stale (`List[ARObject]`, "not yet implemented"); the field is `List[CouplingPortConnection]` with reader/writer — row retyped, keeping only the genuine `couplingPorts` mislabel note.
- [x] GlobalTimeCouplingPortProps (class · Table 9.18 · p.875 · used by CouplingPortDetails.globalTimeProps · source EthernetTopology.py · Base ARObject; attr propagationDelay TimeValue · resolves ARObject placeholder) · steps complete commit a264fe14 — STAMPED R23-11 — confirmed by user 2026-08-28 <!-- commit: baba7996 -->
  - [x] Step 1 — Sync members & description from spec
    (Table 9.18 markdown AUTOSAR_CP_TPS_SystemTemplate.md:22524 + PDF p.875; Base ARObject)
  - [x] Step 2 — Write model class unit test (Red)
    (TestGlobalTimeCouplingPortProps in test_EthernetTopology.py; Red confirmed)
  - [x] Step 3 — Implement model class (Green)
    (typed Optional[TimeValue] field + guarded setter)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
    (class Note verbatim + attribute Note verbatim; None-no-op sentence appended)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
    (tests/test_armodel/writer/test_global_time_coupling_port_props.py; Red confirmed)
  - [x] Step 6 — Update parser & writer (Green)
    (get/setGlobalTimeCouplingPortProps wired into CouplingPortDetails)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
    (none; CouplingPortDetails globalTimeProps placeholder row resolved)
  - [x] Step 9 — Verify (9a) + confirm (9b)
    (9a 2026-08-28: pytest 8132 passed / 0 failed incl. integration round-trip, lint clean, parity script CLASSES untested=0; 9b confirmed by user 2026-08-28 — marker written)
    **Full 9-step re-sync (no marker, so steps 1–8 re-verified, not trusted):** implementation, docstrings, checklist and tests were already spec-correct for Table 9.18 — Base ARObject, single attr propagationDelay (TimeValue, 0..1), PEP 526, guarded setter, all texts verbatim, reader/writer cover PROPAGATION-DELAY (the only XSD child) and are wired into CouplingPortDetails both sides. No source change. Load-bearing proof by mutation: removing the None guard fails TestGlobalTimeCouplingPortProps.test_none_no_op; removing the writer PROPAGATION-DELAY line fails test_write_all_fields; removing the reader line fails the round-trip test — all 3 failed under mutation, pass restored.
    **Deviation tracker:** the `globalTimeProps` row in the CouplingPortDetails section was stale (`Optional[ARObject]`, "not yet implemented"); retyped to `Optional[GlobalTimeCouplingPortProps]` with Deviation = '-' (Rule 0014).
- [x] CouplingPortAbstractShaper (abstract class · no own table (abstract; XSD-derived per Rule 0002, no marker) · used by CouplingPortFifo.shaper · source EthernetTopology.py · resolves ARObject placeholder; subclasses CouplingPortFifo/CouplingPortScheduler-style shapers reference it in Base) · steps complete commit 042e9a8c — STAMP DEFERRED (batch 9b pending; no marker applicable per Rule 0002)
  - [x] Step 1 — Sync members & description from spec
    (XSD-derived abstract base per Rule 0002; no PDF table)
  - [x] Step 2 — Write model class unit test (Red)
    (TestCouplingPortAbstractShaper via concrete subclass; Red confirmed)
  - [x] Step 3 — Implement model class (Green)
    (abstract base in EthernetTopology.py; CouplingPortFifo.shaper retyped)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
    (tests/test_armodel/writer/test_coupling_port_abstract_shaper.py; Red confirmed)
  - [x] Step 6 — Update parser & writer (Green)
    (shaper dispatch wired in read/writeCouplingPortFifo)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
    (none; CouplingPortFifo shaper placeholder row resolved)
  - [x] Step 9 — Verify (9a) + confirm (9b)
    (9a automated verification only — pytest 7406 passed, black/black-check/lint clean; 9b stamp DEFERRED to batch pass)
- [x] OrderedMaster (class · Table 6.148 · p.470 · used by TimeSyncClientConfiguration.orderedMasters (untyped `[]` placeholder) — member of the InfrastructureServices.timeSynchronization chain · source EthernetTopology.py · resolves placeholder; consumer class NOT queued (framework), but InfrastructureServices is UNSTAMPED until this lands) · steps complete commit 96d42032 — STAMP DEFERRED (batch 9b pending)
  - [x] Step 1 — Sync members & description from spec
    (Table 6.148 markdown AUTOSAR_CP_TPS_SystemTemplate.md:12552 + PDF p.470)
  - [x] Step 2 — Write model class unit test (Red)
    (tests/test_armodel/models/.../test_ordered_master_model.py; Red confirmed)
  - [x] Step 3 — Implement model class (Green)
    (ARObject in EthernetTopology.py; TimeSyncClientConfiguration.orderedMasters retyped)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
    (tests/test_armodel/writer/test_ordered_master.py; Red confirmed)
  - [x] Step 6 — Update parser & writer (Green)
    (read/writeOrderedMaster wired into TimeSyncClientConfiguration)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
    (none; TimeSyncClientConfiguration orderedMasters placeholder resolved)
  - [x] Step 9 — Verify (9a) + confirm (9b)
    (9a automated verification only — pytest 7406 passed, black/black-check/lint clean; 9b stamp DEFERRED to batch pass)
- [x] TimeSyncTechnologyEnum (enum · Table 6.149 · p.471 · used by TimeSyncClientConfiguration.timeSyncTechnology AND TimeSyncServerConfiguration.timeSyncTechnology (`# type:` placeholders) — member of the InfrastructureServices.timeSynchronization chain · source EthernetTopology.py · Steps 5/6 N/A if standalone enum) · steps complete commit 7fd728a6 — STAMP DEFERRED (batch 9b pending)
  - [x] Step 1 — Sync members & description from spec
    (Table 6.149 markdown AUTOSAR_CP_TPS_SystemTemplate.md:12567 + PDF p.471)
  - [x] Step 2 — Write model class unit test (Red)
    (TestTimeSyncTechnologyEnum in test_EthernetTopology.py; Red confirmed)
  - [x] Step 3 — Implement model class (Green)
    (AREnum in EthernetTopology.py; consumers retyped PEP 526)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
    (class Note verbatim; literal comments verbatim incl. Tags tails per AREnum convention)
  - [x] Step 5 — Write reader/writer round-trip test (N/A — standalone enum, no own XML element; round-tripped via consuming classes)
  - [x] Step 6 — Update parser & writer (N/A — same reason as Step 5)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
    (none; TimeSyncClient/ServerConfiguration timeSyncTechnology `# type:` placeholders resolved)
  - [x] Step 9 — Verify (9a) + confirm (9b)
    (9a automated verification only — pytest 7406 passed, black/black-check/lint clean; 9b stamp DEFERRED to batch pass)
- [x] DoIpEntityRoleEnum (enum · Table 6.151 · p.471 · used by DoIpEntity.doIpEntityRole (`# type:` placeholder) — member of the InfrastructureServices.doIpEntity chain · source EthernetTopology.py · Steps 5/6 N/A if standalone enum) · steps complete commit 70387e1b — STAMP DEFERRED (batch 9b pending)
  - [x] Step 1 — Sync members & description from spec
    (Table 6.151 markdown AUTOSAR_CP_TPS_SystemTemplate.md:12589 + PDF p.471)
  - [x] Step 2 — Write model class unit test (Red)
    (TestDoIpEntityRoleEnum in test_EthernetTopology.py; Red confirmed)
  - [x] Step 3 — Implement model class (Green)
    (AREnum in EthernetTopology.py; DoIpEntity.doIpEntityRole retyped PEP 526)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
    (class Note verbatim; literal comments verbatim incl. Tags tails per AREnum convention)
  - [x] Step 5 — Write reader/writer round-trip test (N/A — standalone enum, no own XML element; round-tripped via consuming class)
  - [x] Step 6 — Update parser & writer (N/A — same reason as Step 5)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
    (none; DoIpEntity doIpEntityRole `# type:` placeholder resolved)
  - [x] Step 9 — Verify (9a) + confirm (9b)
    (9a automated verification only — pytest 7406 passed, black/black-check/lint clean; 9b stamp DEFERRED to batch pass)

## RE-FIX rows (user review docs/plan/check.md 2026-08-25 — consumers of the member types above; re-run after their member classes land)

- [x] DhcpServerConfiguration RE-FIX (class docstring partial + member docstrings incorrect per user; full verbatim Notes incl. Tables 3.80/3.81 aggregation roles once Ipv4/Ipv6 subclasses are real) — STAMP DEFERRED (batch 9b pending)
  - [x] Step 1 — Sync members & description from spec
    (Table 3.79 re-verified: Note "Defines the configuration of DHCP servers that are running on the network
    endpoint. It is possible that an Ipv4DhcpServer and an Ipv6DhcpServer run on the same Ecu."; Base row = ARObject only;
    XSD complexType confirms AR-OBJECT group without DESCRIBABLE)
  - [x] Step 2/3 — Model behavior unchanged (docstring/base sync; existing get/set tests still green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
    (class docstring → full verbatim Note; member comments/getter/setter docstrings → verbatim Attribute-row Notes
    "Configuration of a IPv4/IPv6 DHCP server that runs on the network endpoint.")
  - [x] Step 5/6 — Reader/writer unchanged (no XML contract change)
  - [x] Step 7 — Update checklist comment (unchanged, p.131 verified)
  - [x] Step 8 — Deviations
    (tracker updated: base corrected Describable→ARObject per Table 3.79 + XSD; aggr rows now cite verbatim Notes)
  - [x] Step 9 — Verify (9a) + confirm (9b)
    (9a automated verification only — pytest 7306 passed, black/black-check/lint clean; 9b stamp DEFERRED to batch pass)
- [x] ConsumedServiceInstance RE-FIX (member types incorrect per user: retype instanceIdentifier → AnyServiceInstanceId, minorVersion → AnyVersionString, versionDrivenFindBehavior → ServiceVersionAcceptanceKindEnum once those classes land; remove resolved deviation rows) — STAMP DEFERRED (batch 9b pending)
  - [x] Step 1 — Spec re-check (Table 6.167 unchanged; member types now real)
  - [x] Step 2 — Retype round-trip assertions (Red)
    (test_consumed_service_instance.py: isinstance asserts for the three retyped members; Red confirmed —
    reader returned generic ARLiteral for instanceIdentifier)
  - [x] Step 3/4 — Model retyped: instanceIdentifier → Optional[AnyServiceInstanceId],
    minorVersion → Optional[AnyVersionString], versionDrivenFindBehavior → Optional[ServiceVersionAcceptanceKindEnum]
    (+ getter/setter hints); docstrings already verbatim from Table 6.167 sync
  - [x] Step 5/6 — Reader/writer updated
    (parser constructs AnyServiceInstanceId/AnyVersionString/ServiceVersionAcceptanceKindEnum from element values;
    writer switched INSTANCE-IDENTIFIER/MINOR-VERSION to literal helpers; ProvidedServiceInstance side untouched —
    stamped R23-11, out of scope)
  - [x] Step 7 — Checklist comment (method set unchanged)
  - [x] Step 8 — Deviations
    (tracker: three placeholder rows resolved and annotated; no open deviations left for this class)
  - [x] Step 9 — Verify (9a) + confirm (9b)
    (9a automated verification only — pytest 7306 passed, black/black-check/lint clean; 9b stamp DEFERRED to batch pass)
- [x] ConsumedEventGroup RE-FIX (missing member class per user: type pduActivationRoutingGroups → List[PduActivationRoutingGroup] with reader/writer coverage once it lands; remove resolved deviation row) — STAMP DEFERRED (batch 9b pending)
  - [x] Step 1 — Spec re-check (Table 6.168 unchanged; PduActivationRoutingGroup landed)
  - [x] Step 2 — Reader/writer coverage tests (Red)
    (test_consumed_event_group.py: write + round-trip of PDU-ACTIVATION-ROUTING-GROUPS wrapper;
     test_abstract_service_instance.py: METHOD-ACTIVATION-ROUTING-GROUPS on consumed AND provided sides;
     Red confirmed — 3 failed)
  - [x] Step 3/4 — Model retyped
    (ConsumedEventGroup.pduActivationRoutingGroups → List[PduActivationRoutingGroup]; AbstractServiceInstance.
    methodActivationRoutingGroup → Optional[PduActivationRoutingGroup]; placeholder docstrings replaced by verbatim
    spec Notes; forward refs quoted for py3.8 eager-annotation compatibility; checklists reader/writer flipped)
  - [x] Step 5/6 — Parser & writer wired
    (parser: readAbstractServiceInstanceMethodActivationRoutingGroups called from both readConsumedServiceInstance
    and readProvidedServiceInstance; readConsumedEventGroup loops the wrapper. writer:
    writeAbstractServiceInstanceMethodActivationRoutingGroups after MAJOR-VERSION per XSD group order;
    CONSUMED-EVENT-GROUP writes wrapper between EVENT-MULTICAST-ADDRESSS and PRIORITY)
  - [x] Step 7 — Checklist comments updated
  - [x] Step 8 — Deviations
    (tracker: both placeholder rows resolved and annotated; XSD unbounded-vs-PDF 0..1 note recorded on
    methodActivationRoutingGroup row, Rule 0015 table-wins)
  - [x] Step 9 — Verify (9a) + confirm (9b)
    (9a automated verification only — pytest 7313 passed, black/black-check/lint clean; 9b stamp DEFERRED to batch pass)
- [x] SocketAddress RE-FIX (type staticSocketConnections → List[StaticSocketConnection], udpChecksumHandling → UdpChecksumCalculationEnum once they land; remove resolved deviation rows) — STAMPED R23-11 <!-- commit: 2abee405 -->
  - [x] Step 1 — Spec re-check (Tables 6.118/6.119/6.201 unchanged; member classes landed)
  - [x] Step 2 — Retype round-trip tests (Red)
    (test_socket_address.py: fixture switched to enum, isinstance asserts, new TestSocketAddressStaticSocketConnections
    write + tmp_path round-trip + empty-reader cases; Red confirmed — 3 failed incl. old literal text assertion,
    updated to spec value udpChecksumEnabled)
  - [x] Step 3/4 — Model retyped (staticSocketConnections → List[StaticSocketConnection],
    udpChecksumHandling → Optional[UdpChecksumCalculationEnum]; placeholder docstring lines removed;
    checklist reader/writer columns flipped)
  - [x] Step 5/6 — Parser & writer wired
    (parser readSocketAddress: STATIC-SOCKET-CONNECTIONS loop via getStaticSocketConnection + enum construction for
     UDP-CHECKSUM-HANDLING; writer writeSocketAddress: STATIC-SOCKET-CONNECTIONS wrapper before UDP-CHECKSUM-HANDLING
     per XSD group order)
  - [x] Step 7 — Checklist comment updated
  - [x] Step 8 — Deviations
    (tracker: both placeholder rows resolved and annotated; SocketAddress now has zero open deviations)
  - [x] Step 9 — Verify (9a) + confirm (9b)
    (9a automated verification only — pytest 7316 passed, black/black-check/lint clean; 9b stamp DEFERRED to batch pass)
- [x] CanXlProps NOT CONFIRMED by user (RESOLVED 2026-08-28: confirmed XSD verified per row 135 — source CanTopology.py:1084 carries `# XSD verified: AUTOSAR_00052.xsd`; canConfig is typed Optional[CanControllerConfiguration], a real class, not a placeholder, so no clarification needed)

### Input ethernet classes — sync AFTER their member types (Rule 0016.5)

- [x] ConsumedEventGroup (markdown SoftwareComponentTemplate · Table 6.168 · p.978 · source Fibex4Ethernet/ServiceInstances.py · depends on SomeipSdClientEventGroupTimingConfig above; sdClientTimerConfig is a ref to it; adds instanceIdentifier) · steps complete commit d17132bf — STAMP DEFERRED (batch 9b pending); RE-FIX queued: type pduActivationRoutingGroups → List[PduActivationRoutingGroup]
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
- [x] ConsumedServiceInstance (markdown SoftwareComponentTemplate · Table 6.167 · p.980 · source Fibex4Ethernet/ServiceInstances.py · base AbstractServiceInstance below; depends on SomeipSdClientServiceInstanceConfig / SomeipServiceVersion above; adds blacklistedVersion, eventMulticastSubscriptionAddress, sdClientTimerConfig refs) · steps complete commit 7f27fb60 — STAMP DEFERRED (batch 9b pending)
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
- [x] AbstractServiceInstance (markdown SystemTemplate · Table 6.158 · p.477 · source Fibex4Ethernet/ServiceInstances.py · base of ConsumedServiceInstance / ProvidedServiceInstance; depends on TagWithOptionalValue above; fixes methodActivationRoutingGroup & routingGroupRefs member types) · steps complete commit 9b0023ed — STAMPED R23-11 <!-- commit: 2feb31c6 -->
  NOTE: Table 6.158 verified in AUTOSAR_CP_TPS_SystemTemplate.md:12736–12752 + PDF p.477 (pdf_page.py
  authoritative). No explicit Base row in the table — XSD group ABSTRACT-SERVICE-INSTANCE is
  incorporated into IDENTIFIABLE-extending subclasses; Python base stays (Identifiable, ABC). No
  class-level Note row; post-table prose paragraph used as class docstring. 4 Attribute rows: capabilityRecord (* aggr
  TagWithOptionalValue), majorVersion (0..1 attr PositiveInteger), methodActivationRoutingGroup (0..1
  aggr PduActivationRoutingGroup — resolved 2026-08-25 via the ConsumedEventGroup RE-FIX: typed
  Optional[PduActivationRoutingGroup], reader/writer wired; NOTE below was stale),
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
- [x] ApplicationEndpoint (markdown SystemTemplate · Table 6.124 · p.458 · source Fibex4Ethernet/EthernetTopology.py — MOVED from ServiceInstances.py per Rule 0007: Table 6.124 Package row = Fibex4Ethernet::EthernetTopology · technology members are XSD-removed and intentionally not modeled per Rule 0015) · steps complete commit 92517479 — STAMPED R23-11 — commit 4164139d
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
    (9a automated verification — pytest 3869 passed, lint passed; black-check has one unrelated
    pre-existing failure in test_parser_tdevents_sllet.py; checklist==methods 1:1 source order,
    verbatim Note diff OK, no receiver-chain mutators in new code; 9b confirmed by user)
- [x] SocketAddress (markdown SystemTemplate · Table 6.118 · p.453 · source Fibex4Ethernet/ServiceInstances.py · fixes applicationEndpoint type; adds ipAddress) · steps complete commit 1d699cf8 — STAMPED R23-11 <!-- commit: 2abee405 -->
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
- [x] SoAdConfig (markdown SystemTemplate · Table 6.117 · p.452 · source Fibex4Ethernet/ServiceInstances.py) — STAMPED R23-11; SYNCED AFTER SocketConnection (reorder per Rule 0016.5) <!-- commit: ecc58745 -->
  - [x] Step 1 — Sync members & description from spec
    (Table 6.117 page-split in markdown AUTOSAR_CP_TPS_SystemTemplate.md:11920–11937 + PDF p.452;
    Base ARObject; 3 attr rows: connection * aggr obsolete, connectionBundle * aggr obsolete, socketAddress * aggr;
    queue note "adds logicAddress ref" is STALE — no logicAddress row in the R23-11 table, XSD-only LOGIC-ADDRESSS
    wrapper NOT modeled per Rule 0015)
  - [x] Step 2 — Model test rewritten to spec shape (Red — createSocketConnection/addConnection missing,
    legacy bulk setters asserted)
  - [x] Step 3 — Implement model class (Green)
    (addConnection/getConnections; createSocketConnectionBundle/getConnectionBundles;
    createSocketAddress/getSocketAddresses; bulk setters removed as non-spec-shaped)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
    (class Note verbatim "SoAd Configuration for one specific Physical Channel."; member Notes verbatim
    incl. obsolete wording)
  - [x] Step 5/6 — Reader/writer round-trip test + wiring
    (tests/test_armodel/writer/test_so_ad_config.py: CONNECTIONS/BUNDLES/SOCKET-ADDRESSS round trip with new
     SocketConnection members; parser readSoAdConfigConnections + writer writeSoAdConfigConnections added in XSD order)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
    (tracker updated: naming deviations resolved to convention notes; stale logicAddress resolution recorded)
  - [x] Step 9 — Verify (9a) + confirm (9b)
    (9a automated verification only — pytest 7318 passed, black/black-check/lint clean; 9b stamp DEFERRED to batch pass)
- [x] EventHandler (markdown SystemTemplate · Table 6.166 · p.492 · source Fibex4Ethernet/ServiceInstances.py · depends on SomeipSdServerEventGroupTimingConfig above; adds eventGroupIdentifier, eventMulticastAddress, pduActivationRoutingGroup, sdServerEgTimingConfig) — STAMPED R23-11 <!-- commit: 0bd80500 -->
  - [x] Step 1 — Sync members & description from spec
    (Table 6.166 page-split in markdown AUTOSAR_CP_TPS_SystemTemplate.md:13081–13105 + PDF p.492;
    Base → Identifiable; 8 attr rows; applicationEndpoint is atp.Status=removed since 4.4.0 and ABSENT from the
    table → field/accessors/reader/writer removed per Rule 0015/the-table-wins)
  - [x] Step 2 — Model tests (Red)
    (TestEventHandler added: new members + applicationEndpointRef-removed assertion; legacy test_EventHandler
    rewritten to synced API; Red confirmed — 6 failed)
  - [x] Step 3 — Implement model class (Green)
    (adds eventGroupIdentifier, eventMulticastAddressRef, pduActivationRoutingGroups List[PduActivationRoutingGroup],
    sdServerEgTimingConfigRef; removes applicationEndpointRef)
  - [x] Step 4 — Sync docstrings (wipe + rewrite) (class Note + all Attribute Notes verbatim, Stereotypes/Tags stripped)
  - [x] Step 5/6 — Reader/writer round-trip test + wiring
    (tests/test_armodel/writer/test_event_handler.py: write_all_fields incl. conditional wrappers, removed-member
     omission case, tmp_path round trip, empty reader; readEventHandler/writeEventHandler fully rewired in XSD order;
     stale consumer test_writer_frame_channel updated off the removed API)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
    (tracker: four former missing rows resolved and annotated; applicationEndpoint removal recorded per Rule 0015)
  - [x] Step 9 — Verify (9a) + confirm (9b)
    (9a automated verification only — pytest 7328 passed, black/black-check/lint clean; 9b stamp DEFERRED to batch pass)
- [x] Ipv6Configuration (markdown SystemTemplate · Table 6.139 · p.466 · source Fibex4Ethernet/EthernetTopology.py — MOVED from NetworkEndpoint.py per Rule 0007: Table 6.139 Package row = Fibex4Ethernet::EthernetTopology · fixes dnsServerAddresses naming → dnsServerAddress) — STAMPED R23-11 <!-- commit: 762937dc -->
  - [x] Step 1 — Sync members & description from spec
    (Table 6.139 page-split in markdown AUTOSAR_CP_TPS_SystemTemplate.md:12392–12410 + PDF p.466;
    Base ARObject+NetworkEndpointAddress → NetworkEndpointAddress; 9 attr rows; "naming fix" resolved as
    convention alignment: bulk setDnsServerAddresses → addDnsServerAddress/getDnsServerAddresses per Rule 0001.5)
  - [x] Step 2 — Model test rewritten to spec shape (Red — addDnsServerAddress + None no-ops missing)
  - [x] Step 3 — Implement model class (Green)
    (typed annotations incl. ipAddressKeepBehavior → IpAddressKeepEnum Table 6.138 / ipv6AddressSource →
     Ipv6AddressSourceEnum Table 6.140 — both REAL AREnum classes implemented in EthernetTopology.py on
     2026-08-26 (user-reported member-type mismatch); ARLiteral placeholders removed; guarded setters)
  - [x] Step 4 — Sync docstrings (wipe + rewrite) (class Note + all nine Attribute Notes verbatim)
  - [x] Step 5/6 — Reader/writer round-trip test + wiring
    (tests/test_armodel/writer/test_ipv6_configuration.py: write_all/empty + round trip + empty reader;
     DNS-SERVER-ADDRESSES wrapper and IP-ADDRESS-KEEP-BEHAVIOR wired both sides in XSD order;
     reader now constructs IpAddressKeepEnum/Ipv6AddressSourceEnum from the element values;
     stale frame_channel ipv6 writer tests still green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
    (tracker: former dnsServerAddress missing row resolved and annotated; the two enum placeholder rows
     REMOVED — IpAddressKeepEnum/Ipv6AddressSourceEnum implemented, Rule 0011, member types retyped)
  - [x] Step 9 — Verify (9a) + confirm (9b)
    (9a automated verification only — pytest 7332 passed, black/black-check/lint clean; 9b stamp DEFERRED to batch pass)
- [x] InfrastructureServices (markdown SystemTemplate · Table 6.144 · p.469 · source Fibex4Ethernet/EthernetTopology.py — MOVED from NetworkEndpoint.py per Rule 0007: Table 6.144 Package row = Fibex4Ethernet::EthernetTopology · depends on DhcpServerConfiguration above; adds dhcpServerConfiguration) — STAMP DEFERRED (batch 9b pending); OrderedMaster 6.148 / TimeSyncTechnologyEnum 6.149 / DoIpEntityRoleEnum 6.151 landed 2026-08-26, Step 9 unblocked
  - [x] Step 1 — Sync members & description from spec
    (Table 6.144 in markdown AUTOSAR_CP_TPS_SystemTemplate.md:12480–12490 + PDF p.469;
    Base ARObject; only 2 attr rows: doIpEntity aggr, timeSynchronization aggr;
    queue note "adds dhcpServerConfiguration" is STALE — atp.Status=removed since 4.3.1, absent from the
    R23-11 table → field/accessors/reader-writer wiring REMOVED per Rule 0015/the-table-wins)
  - [x] Step 2 — Model test updated to spec shape (Red — removed-member assertion + missing TIME-SYNC coverage)
  - [x] Step 3 — Implement model class (Green) — verbatim Notes, typed Optional fields, guarded setters
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5/6 — Reader/writer round-trip test + wiring
    (tests/test_armodel/writer/test_infrastructure_services.py: presence round trip incl. TIME-SYNCHRONIZATION
     with TIME-SYNC-SERVER identity via writeReferrable/readReferrable; removed DHCP-SERVER-CONFIGURATION no longer
     written on this path; inner TimeSyncClient/ServerConfiguration members deferred — deviation recorded)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
    (tracker: new InfrastructureServices section; dhcpServerConfiguration removal per Rule 0015;
     timeSynchronization/doIpEntity inner-members deferral RESOLVED 2026-08-26 — OrderedMaster 6.148,
     TimeSyncTechnologyEnum 6.149, DoIpEntityRoleEnum 6.151 landed; placeholder deviation rows removed)
  - [x] Step 9 — Verify (9a) + confirm (9b)
    (9a automated verification only — pytest 7406 passed, black/black-check/lint clean; 9b stamp DEFERRED to batch pass; inner-member placeholders resolved once the member types landed)
- [x] CouplingPortFifo (markdown SystemTemplate · Table 3.68 · p.124 · source Fibex4Ethernet/EthernetTopology.py · fixes assignedTrafficClass type) — STAMPED R23-11 — confirmed by user 2026-08-28 <!-- commit: 0ff430d4 -->
  - [x] Step 1 — Sync members & description from spec
    (Table 3.68 page-split in markdown AUTOSAR_CP_TPS_SystemTemplate.md:3300–3312 + PDF p.124;
    Base → CouplingPortStructuralElement; 3 attr rows: assignedTrafficClass 0..8, minimumFifoLength, shaper candidate;
    trafficClassPreemptionSupport absent from table+XSD → REMOVED per Rule 0015)
  - [x] Step 2 — Model tests rewritten to spec shape (Red)
  - [x] Step 3 — Implement model class (Green) — verbatim Notes, typed fields, guarded setters
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5/6 — Reader/writer round-trip test + wiring
    (tests/test_armodel/writer/test_coupling_port_fifo.py; ASSIGNED-TRAFFIC-CLASSS wrapper + MINIMUM-FIFO-LENGTH
     wired both sides in XSD order; SHAPER element deferred with the placeholder class)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
    (tracker: shaper ARObject placeholder — CouplingPortAbstractShaper queued 2026-08-26 (see Member types ADDED);
     trafficClassPreemptionSupport removal recorded per Rule 0015)
  - [x] Step 9 — Verify (9a) + confirm (9b)
    (9a re-verified 2026-08-28 — targeted model+writer tests green, mutation Red proof passed; 9b confirmed by user — # Spec verified: R23-11 applied, commit 0ff430d4)
- [x] CouplingPortDetails (markdown SystemTemplate · Table 3.63 · p.122 · source Fibex4Ethernet/EthernetTopology.py · depends on CouplingPortTrafficClassAssignment above; fixes ethernetPriorityRegeneration / ethernetTrafficClassAssignment member types) — **NOT STAMPED** — ratePolicy member gap (see Step 8/9 notes); GlobalTimeCouplingPortProps (Table 9.18) landed 2026-08-26, but 9b failed re-check 2026-08-29
  - [x] Step 1 — Sync members & description from spec
    (Table 3.63 page-split in markdown AUTOSAR_CP_TPS_SystemTemplate.md:3231–3248 + PDF p.122;
    Base ARObject; 5 attr rows; defaultTrafficClass/framePreemptionSupport/ratePolicies/vlanTranslationTables
    absent from table → REMOVED per Rule 0015; globalTimeProps placeholder — GlobalTimeCouplingPortProps not implemented)
  - [x] Step 2 — Model tests rewritten to spec shape (Red)
  - [x] Step 3 — Implement model class (Green) — verbatim Notes, typed fields, guarded setters,
    bulk setters replaced with addEthernetTrafficClassAssignment mutator
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5/6 — Reader/writer round-trip test + wiring
    (tests/test_armodel/writer/test_coupling_port_details.py: structural elements incl. fifo+scheduler dispatch,
     priority regenerations, traffic class assignments, lastEgressSchedulerRef round trip;
     parser bulk-setter call replaced with mutator loop per Rule 0013)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
    (tracker: globalTimeProps ARObject placeholder — GlobalTimeCouplingPortProps Table 9.18 queued 2026-08-26 (see Member types ADDED);
     four removed members documented per Rule 0015;
     **NEW 2026-08-29 re-check: ratePolicy member MISSING** — Table 3.63 + PDF p.122 + XSD RATE-POLICYS
     (AUTOSAR_00052.xsd:23706) define ratePolicy → CouplingPortRatePolicy (*, aggr); earlier sync dropped
     ratePolicies (plural) as "absent from table" but never re-added ratePolicy (singular); type classes
     CouplingPortRatePolicy (Table 3.69) + CouplingPortRatePolicyActionEnum (Table 3.70) absent from codebase —
     queued to Member types ADDED, consumer kept unstamped per user 2026-08-29)
  - [x] Step 9 — Verify (9a) + confirm (9b)
    (9a automated verification only — pytest 7406 passed, black/black-check/lint clean; 9b RE-CHECK 2026-08-29
     FAILED — spec deviation ratePolicy found; NOT stamped; user chose "skip it and check next" — class deferred,
     next class is OrderedMaster (Table 6.148))
- [x] CouplingPort (markdown SystemTemplate · Table 3.54 · p.110 · source Fibex4Ethernet/EthernetTopology.py · member of EthernetCluster.couplingPorts & EthernetCommunicationController.couplingPorts; adds couplingPortSpeed, vlanModifierRef → EthernetPhysicalChannel Ref) — **STAMPED R23-11** — commit 2482fa9b: 6 of 7 member types landed 2026-08-26 (EthernetConnectionNegotiationEnum 3.55, CouplingPortRoleEnum F.38, EthernetMacLayerTypeEnum 3.56, EthernetPhysicalLayerTypeEnum 3.57, EthernetSwitchVlanIngressTagEnum 3.58, PlcaProps 3.117); MacSecProps (3.118) landed 2026-08-28 in its own sub-queue (a150ffd2) — # Spec verified: applied
  - [x] Step 1 — Sync members & description from spec
    (Table 3.54 page-split in markdown AUTOSAR_CP_TPS_SystemTemplate.md:2795–2825 + PDF p.110;
    Base → Identifiable; 14 attr rows incl. wakeupSleepOnDatalineConfig after caption;
    queue note "adds couplingPortSpeed" is STALE — XSD has COUPLING-PORT-SPEED but NO table row → NOT modeled per Rule 0015;
    vlanModifierRef ✓ added; macAddressVlanAssignments absent from table+XSD → REMOVED)
  - [x] Step 2 — Model test rewritten to spec shape (Red — vlanModifierRef missing, bulk setters removed)
  - [x] Step 3 — Implement model class (Green) — verbatim Notes, typed fields, guarded setters,
    enum-typed attrs carried as ARLiteral placeholders (Rule 0001.10), macSecProps/plcaProps ARObject placeholders
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5/6 — Reader/writer round-trip test + wiring
    (tests/test_armodel/writer/test_coupling_port.py: full-field write + tmp_path round trip + empty reader;
     readCouplingPort/writeCouplingPort cover all 14 members in XSD order)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
    (tracker: six enum placeholders (EthernetConnectionNegotiationEnum 3.55, CouplingPortRoleEnum F.38, EthernetMacLayerTypeEnum 3.56,
     EthernetPhysicalLayerTypeEnum 3.57, EthernetSwitchVlanIngressTagEnum 3.58, EthernetWakeupSleepOnDatalineConfig 3.115 ref) +
     plcaProps placeholder — ALL RESOLVED 2026-08-26 (see Member types ADDED);
     macSecProps ARObject placeholder RESOLVED 2026-08-28 — MacSecProps (3.118) stamped R23-11 in its own sub-queue (commit a150ffd2);
     stale couplingPortSpeed note resolved; macAddressVlanAssignments removal recorded per Rule 0015)
  - [x] Step 9 — Verify (9a) + confirm (9b)
    (9a re-verified after MacSecProps landed 2026-08-28 — 60 targeted, 7863 unit, 1 integration, lint, black-check all pass; # Spec verified: R23-11 applied on 9b confirmation — commit 2482fa9b)
- [x] EthernetCluster (markdown SystemTemplate · Table 3.47 · p.103 · source Fibex4Ethernet/EthernetTopology.py · adds couplingPorts to EthernetCluster; closes open items) — STAMPED R23-11 — confirmed by user 2026-08-28 <!-- commit: 0ff430d4 -->
  - [x] Step 1 — Sync members & description from spec
    (Table 3.47 in markdown AUTOSAR_CP_TPS_SystemTemplate.md:2599–2620 + PDF p.103;
    Base chain → CommunicationCluster; 4 attr rows: couplingPortConnection * aggr, two TimeValue attrs, macMulticastGroup * aggr;
    queue note "adds couplingPorts" resolved: spec role is couplingPortConnection (CouplingPortConnection objects),
    CouplingPorts themselves aggregate via CouplingElement/EthernetCommunicationController — mislabelled
    `couplingPorts` list renamed to `couplingPortConnections`)
  - [x] Step 2 — Model test rewritten to spec shape (Red)
  - [x] Step 3 — Implement model class (Green) — verbatim Notes, typed fields, guarded setters
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5/6 — Reader/writer round-trip test + wiring
    (tests/test_armodel/writer/test_ethernet_cluster.py; COUPLING-PORT-STARTUP-ACTIVE-TIME/SWITCHOFF-DELAY wired
     both sides inside ETHERNET-CLUSTER-CONDITIONAL per XSD order)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
    (tracker: couplingPortConnections ARObject placeholder — CouplingPortConnection Table 3.60 landed 2026-08-26 (see Member types ADDED), placeholder row removed)
  - [x] Step 9 — Verify (9a) + confirm (9b)
    (9a re-verified 2026-08-28 — targeted model+writer tests green, mutation Red proof passed; 9b confirmed by user — # Spec verified: R23-11 applied, commit 0ff430d4)
- [x] EthernetCommunicationController (markdown SystemTemplate · Table 3.61 · p.116 · source Fibex4Ethernet/EthernetTopology.py · closes open items) — STAMP DEFERRED (batch 9b pending); EthernetMacLayerTypeEnum (Table 3.56) landed 2026-08-26, Step 9 unblocked
  - [x] Step 1 — Sync members & description from spec
    (Table 3.61 page-split in markdown AUTOSAR_CP_TPS_SystemTemplate.md:2974–3011 + PDF p.116;
    Base → CommunicationController; 8 attr rows incl. slaveQualifiedUnexpectedLinkDownTime after caption;
    all members already present in model)
  - [x] Step 2 — Round-trip tests (Red) — writer/parser only wired COUPLING-PORTS before
  - [x] Step 3/4 — Docstrings wiped + rewritten (class Note verbatim, per-attribute Notes verbatim,
    PEP 526 annotations replacing # type: comments)
  - [x] Step 5/6 — Reader/writer wiring
    (readEthernetCommunicationController/writeEthernetCommunicationController now cover CAN-XL-CONFIG-REF,
     MAC-LAYER-TYPE, MAC-UNICAST-ADDRESS, MAXIMUM-{RECEIVE,TRANSMIT}-BUFFER-LENGTH,
     SLAVE-ACT-AS-PASSIVE-COMMUNICATION-SLAVE + coupling ports, in XSD order)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
    (tracker: new section, macLayerType ARLiteral placeholder — EthernetMacLayerTypeEnum Table 3.56 landed 2026-08-26 (see Member types ADDED), placeholder row removed)
  - [x] Step 9 — Verify (9a) + confirm (9b)
    (9a automated verification only — pytest 7406 passed, black/black-check/lint clean; 9b stamp DEFERRED to batch pass; macLayerType placeholder resolved once EthernetMacLayerTypeEnum landed)
- [x] EthernetCommunicationConnector (markdown SystemTemplate · Table 3.62 · p.117 · source Fibex4Ethernet/EthernetTopology.py · depends on CanXlProps above; adds apApplicationEndpoint, canXlPropsRefs, ipV6PathMtuEnabled, ipV6PathMtuTimeout, pncFilterDataMask, unicastNetworkEndpointRefs → NetworkEndpoint Ref) — STAMPED R23-11 <!-- commit: ccfd3365 -->
  - [x] Step 1 — Sync members & description from spec
    (Table 3.62 page-split in markdown AUTOSAR_CP_TPS_SystemTemplate.md:3020–3040 + PDF p.117;
    Base → CommunicationConnector; only 5 attr rows: ethIpProps ref, maximumTransmissionUnit, neighborCacheSize,
    pathMtuEnabled, pathMtuTimeout;
    queue-note members NOT modelled per Rule 0015: apApplicationEndpoint (XSD-only, class not queued),
    canXlPropsRefs (XSD-only, CanXlProps unconfirmed), ipV6PathMtuEnabled/Timeout (atp.Status=removed),
    pncFilterDataMask (absent); networkEndpointRefs (atp.Status=removed since 4.3.1) REMOVED)
  - [x] Step 2 — Model tests rewritten to spec shape (Red — removed-member assertion + missing reader/writer coverage)
  - [x] Step 3 — Implement model class (Green) — verbatim Notes, typed fields, guarded setters
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5/6 — Reader/writer round-trip test + wiring
    (tests/test_armodel/writer/test_ethernet_communication_connector.py: write_all/empty + tmp_path round trip +
     empty reader; readEthernetCommunicationConnector/writeEthernetCommunicationConnector cover all 5 members
     in XSD order; NETWORK-ENDPOINT-REFS helpers removed both sides; stale parser test replaced with
     NEIGHBOR-CACHE-SIZE case)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
    (tracker: networkEndpointRefs removal + all queue-note non-modelled members documented per Rule 0015)
  - [x] Step 9 — Verify (9a) + confirm (9b)
    (9a automated verification only — pytest 7356 passed, black/black-check/lint clean; 9b stamp DEFERRED to batch pass)
- [x] SdClientConfig (no PDF table · p.870 source EthernetTopology.py · depends on TagWithOptionalValue above; fixes capabilityRecord type) — XSD VERIFIED: AUTOSAR_00052.xsd <!-- commit: 1799b461 -->
  - [x] Step 1 — Derive members from XSD SD-CLIENT-CONFIG group; Base ARObject; 6 members;
    "fixes capabilityRecord type" resolved: single TagWithOptionalValue field → List[TagWithOptionalValue]
    with addCapabilityRecord/getCapabilityRecords per Rule 0001.5
  - [x] Step 2 — Model test rewritten to spec shape (Red)
  - [x] Step 3 — Implement model class (Green) — verbatim XSD Notes, typed fields, guarded setters
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5/6 — Reader/writer round-trip test + wiring
    (tests/test_armodel/writer/test_sd_client_config.py; CAPABILITY-RECORDS wired via
     getTagWithOptionalValues/setTagWithOptionalValues in both reader and writer)
  - [x] Step 7 — Checklist comment (XSD-only form, all rows checked, no marker)
  - [x] Step 8 — Deviations
    (tracker: new SdClientConfig section, zero open deviations)
  - [x] Step 9 — Verify (9a) + confirm (9b)
    (9a automated verification only — pytest 7360 passed, black/black-check/lint clean; marker N/A per Rule 0002)
- [x] IPv6ExtHeaderFilterList (class · Table 6.129 · p.325 · **R4.3.1** · source Fibex4Ethernet/EthernetCommunication.py — R4.3.1 package = M2::...::Fibex4Ethernet::Ethernet Communication; 1 attribute: allowedIPv6ExtHeader (PositiveInteger, 1..*); Base Identifiable — most-derived of the table chain ARObject/Identifiable/MultilanguageReferrable/Referrable) — queued as missing class (closure of SocketConnection resync, 2026-08-29); NOTE: R23-11 has a same-named headerless Table 6.121 fragment tied to the SocketAddress cluster; the queue targets the R4.3.1 table per the 2026-08-29 family decision; # Spec verified: withheld (pending batch 9b pass) <!-- commit: dec0081e -->
  - [x] Step 1 — Derive member from R4.3.1 Table 6.129 (p.325): allowedIPv6ExtHeader (PositiveInteger, 1..*); Base Identifiable (most-derived of the table's chain)
  - [x] Step 2 — Model test (Red → Green)
  - [x] Step 3 — Implement model class (Green): allowedIPv6ExtHeaders list, guarded add, verbatim Note
  - [x] Step 4 — Sync docstrings (verbatim R4.3.1 Note)
  - [x] Step 5/6 — N/A (class absent from BOTH the R4.3.1 and R23-11 XSDs — markdown-only class, no element names exist to wire without fabrication; documented 2026-08-29)
  - [x] Step 7 — Checklist comment
  - [x] Step 8 — Deviations: none
  - [x] Step 9 — Verify (9a) + confirm (9b): pytest 8126 passed + 2 integration, lint+black clean; 9b user-confirmed; # Spec verified: withheld (pending batch 9b pass)
- [x] TcpOptionFilterList (class · Table 6.131 · p.326 · **R4.3.1** · source Fibex4Ethernet/EthernetCommunication.py — R4.3.1 package = M2::...::Fibex4Ethernet::Ethernet Communication; 1 attribute: allowedTcpOption (PositiveInteger, 1..*); Base Identifiable — most-derived of the table chain ARObject/Identifiable/MultilanguageReferrable/Referrable) — missing class (closure of SocketConnection resync, 2026-08-29); parser/writer wired 2026-08-29 per user request (TCP-OPTION-FILTER-LIST inside TcpOptionFilterSet, names per R4.3.1 AUTOSAR_00044.xsd); # Spec verified: withheld (pending batch 9b pass) <!-- commit: 6ba017a4 -->
  - [x] Step 1 — Derive member from R4.3.1 Table 6.131 (p.326): allowedTcpOption (PositiveInteger, 1..*); Base Identifiable
  - [x] Step 2 — Model test (Red → Green)
  - [x] Step 3 — Implement model class (Green): allowedTcpOptions list, guarded add, verbatim Note
  - [x] Step 4 — Sync docstrings (verbatim R4.3.1 Note)
  - [x] Step 5/6 — Reader/writer wired 2026-08-29 (was N/A): TCP-OPTION-FILTER-LIST serialized within TcpOptionFilterSet; ALLOWED-TCP-OPTIONS/ALLOWED-TCP-OPTION per XSD; round-trip tests assert field values (tests/test_armodel/writer/test_tcp_option_filter_set.py)
  - [x] Step 7 — Checklist comment
  - [x] Step 8 — Deviations: none
  - [x] Step 9 — Verify (9a) + confirm (9b): pytest 8131 passed + 2 integration, lint+black clean; 9b user-confirmed (incl. wiring delta); # Spec verified: withheld (pending batch 9b pass)
- [x] TcpOptionFilterSet (class · Table 6.130 · p.326 · **R4.3.1** · source Fibex4Ethernet/EthernetCommunication.py — R4.3.1 package = M2::...::Fibex4Ethernet::Ethernet Communication; 1 attribute: tcpOptionFilterList (TcpOptionFilterList, *, aggr, "Collection of white lists for the filtering of TCP options."); Base ARElement — most-derived of the table chain incl. CollectableElement/PackageableElement) — created 2026-08-29 per user request to host TcpOptionFilterList serialization (atp.recommendedPackage=TcpOptionFilterSets; element names per R4.3.1 AUTOSAR_00044.xsd); # Spec verified: withheld (pending batch 9b pass) <!-- commit: ee6ddaa3 -->
  - [x] Step 1 — Derive member from R4.3.1 Table 6.130 (p.326): tcpOptionFilterList (TcpOptionFilterList, *, aggr); Base ARElement
  - [x] Step 2 — Model test (Red → Green): createTcpOptionFilterList appends, duplicate returns existing
  - [x] Step 3 — Implement model class (Green): ARElement subclass, dedicated typed list, registry-based create
  - [x] Step 4 — Sync docstrings (verbatim R4.3.1 Note)
  - [x] Step 5/6 — Reader/writer: package-level TCP-OPTION-FILTER-SET dispatch (readARPackageElements/writeARPackageElement); round-trip full + empty-wrapper cases
  - [x] Step 7 — Checklist comment
  - [x] Step 8 — Deviations: none
  - [x] Step 9 — Verify (9a) + confirm (9b): pytest 8131 passed + 2 integration, lint+black clean; 9b user-confirmed; # Spec verified: withheld (pending batch 9b pass)
- [x] SocketConnection (obsolete · Table 6.120 · p.319 · **R4.3.1** · source Fibex4Ethernet/EthernetCommunication.py — R4.3.1 package = M2::...::Fibex4Ethernet::Ethernet Communication (relocated from ObsoleteModel.py per Rule 0007, 2026-08-29); 2 members: runtimePortConfiguration → RuntimeAddressConfigurationEnum (Table 6.121), shortLabel → Identifier) — RESYNCED to R4.3.1 per user decision (2026-08-29); the prior 19-member XSD-derived shape (incl. SoAdConnectorType/SoAdProtocolType ARLiteral placeholders) was dropped per Rule 0015 (PDF/markdown table wins, no fabrication); # Spec verified: withheld (not yet confirmed/spec-verified)
  - [x] Step 1 — Derive members from R4.3.1 Table 6.120 (p.319): runtimePortConfiguration (RuntimeAddressConfigurationEnum, Table 6.121), shortLabel (Identifier); Base Describable
  - [x] Step 2 — Model test rewritten to R4.3.1 shape (Red → Green)
  - [x] Step 3 — Implement model class (Green): 2 members, guarded None-no-op setters, verbatim Notes
  - [x] Step 4 — Sync docstrings (verbatim R4.3.1 Notes)
  - [x] Step 5/6 — Reader/writer reduced to RUNTIME-PORT-CONFIGURATION + SHORT-LABEL (setSocketConnection/getSocketConnection)
  - [x] Step 7 — Checklist comment (R4.3.1 Table 6.120 p.319, all rows checked)
  - [x] Step 8 — Deviations: tracker updated; obsolete XSD-only members (SoAdConnectorType/SoAdProtocolType et al.) removed per Rule 0015
  - [x] Step 9 — Verify (9a) + confirm (9b): pytest (EthernetCommunication/so_ad_config/frame_channel) passed, lint+black clean, integration round-trip passed; # Spec verified: withheld (not yet confirmed/spec-verified)
- [x] RuntimeAddressConfigurationEnum (enum · Table 6.121 · p.320 · **R4.3.1** · source Fibex4Ethernet/EthernetCommunication.py — R4.3.1 package = M2::...::Fibex4Ethernet::Ethernet Communication (created this pass per Rule 0007, 2026-08-29); 2 literals: NONE="none" (atp.EnumerationValue=0), SD="sd" (atp.EnumerationValue=1); used by SocketConnection.runtimePortConfiguration) — created to support the SocketConnection R4.3.1 resync; # Spec verified: withheld (not yet confirmed/spec-verified)
  - [x] Step 1 — Derive literals from R4.3.1 Table 6.121 (p.320): NONE (atp.EnumerationValue=0), SD (atp.EnumerationValue=1)
  - [x] Step 2 — Enum unit test (Red → Green)
  - [x] Step 3 — Implement enum (Green): AREnum subclass, literals NONE="none"/SD="sd", verbatim literal Descriptions
  - [x] Step 4 — Sync docstrings (verbatim R4.3.1 Note + literal Descriptions)
  - [x] Step 5/6 — N/A: standalone enum, no own XML element; round-tripped via SocketConnection.runtimePortConfiguration
  - [x] Step 7 — Checklist comment (R4.3.1 Table 6.121 p.320, all rows checked)
  - [x] Step 8 — Deviations: none
  - [x] Step 9 — Verify (9a) + confirm (9b): pytest (EthernetCommunication) passed, lint+black clean; # Spec verified: withheld (not yet confirmed/spec-verified)
- [x] SocketConnectionIpduIdentifier (class · Table 6.122 · p.321 · **R4.3.1** · source Fibex4Ethernet/EthernetCommunication.py — R4.3.1 package = M2::...::Fibex4Ethernet::Ethernet Communication (relocated from ObsoleteModel.py per Rule 0007, 2026-08-29); 7 members: headerId (PositiveInteger), pduCollectionPduTimeout (TimeValue), pduCollectionSemantics, pduCollectionTrigger, pduRef (RefType), pduTriggeringRef (RefType), routingGroupRefs (List[RefType]); Base ARObject) — pre-existing EXIST type, relocated with the SocketConnection family; # Spec verified: withheld (not yet confirmed/spec-verified)
  - [x] Step 1 — Derive members from R4.3.1 Table 6.122 (p.321); Base ARObject
  - [x] Step 2 — Model test (Red → Green)
  - [x] Step 3 — Implement model class (Green): 7 members, typed Optional/List fields, guarded setters
  - [x] Step 4 — Sync docstrings
  - [x] Step 5/6 — Reader/writer: getSocketConnectionPdus/setSocketConnectionPdus (used by SocketConnectionBundle.pdus); wiring completed 2026-08-29: PDU-COLLECTION-PDU-TIMEOUT + ROUTING-GROUP-REFS/ROUTING-GROUP-REF (names per R4.3.1 AUTOSAR_00044.xsd)
  - [x] Step 7 — Checklist comment
  - [x] Step 8 — Deviations: none (pre-existing)
  - [x] Step 9 — Verify (9a) + confirm (9b): pytest (frame_channel) passed, lint+black clean; # Spec verified: withheld (not yet confirmed/spec-verified)
- [x] SocketConnectionBundle (class · Table 6.118 · p.316 · **R4.3.1** · source Fibex4Ethernet/EthernetCommunication.py — R4.3.1 package = M2::...::Fibex4Ethernet::Ethernet Communication (relocated from ObsoleteModel.py per Rule 0007, 2026-08-29); 7 members: bundledConnections (List[SocketConnection]), differentiatedServiceField (PositiveInteger), flowLabel (PositiveInteger), pathMtuDiscoveryEnabled (Boolean), pdus (List[SocketConnectionIpduIdentifier]), serverPortRef (RefType), udpChecksumHandling (UdpChecksumCalculationEnum); Base Referrable) — pre-existing EXIST type, relocated with the SocketConnection family; # Spec verified: withheld (not yet confirmed/spec-verified)
  - [x] Step 1 — Derive members from R4.3.1 Table 6.118 (p.316); Base Referrable
  - [x] Step 2 — Model test (Red → Green)
  - [x] Step 3 — Implement model class (Green): 7 members, typed Optional/List fields, guarded setters/adders
  - [x] Step 4 — Sync docstrings
  - [x] Step 5/6 — Reader/writer: writeSocketConnectionBundleConnections / writeSocketConnectionBundle / readSocketConnectionBundleConnections + pdus; wiring completed 2026-08-29: DIFFERENTIATED-SERVICE-FIELD, FLOW-LABEL, PATH-MTU-DISCOVERY-ENABLED, PDUS, UDP-CHECKSUM-HANDLING (names per R4.3.1 AUTOSAR_00044.xsd); round-trip asserts field values (test_so_ad_config.py)
  - [x] Step 7 — Checklist comment
  - [x] Step 8 — Deviations: none (pre-existing)
  - [x] Step 9 — Verify (9a) + confirm (9b): pytest (frame_channel) passed, lint+black clean; # Spec verified: withheld (not yet confirmed/spec-verified)
- [x] SoAdRoutingGroup (class · Table 6.125 · p.323 · **R4.3.1** · source Fibex4Ethernet/EthernetCommunication.py — R4.3.1 package = M2::...::Fibex4Ethernet::Ethernet Communication (relocated from ObsoleteModel.py per Rule 0007, 2026-08-29); 1 member: eventGroupControlType (EventGroupControlTypeEnum); Base FibexElement) — pre-existing EXIST type, relocated with the SocketConnection family; # Spec verified: withheld (not yet confirmed/spec-verified)
  - [x] Step 1 — Derive members from R4.3.1 Table 6.125 (p.323); Base FibexElement
  - [x] Step 2 — Model test (Red → Green)
  - [x] Step 3 — Implement model class (Green): 1 member eventGroupControlType (EventGroupControlTypeEnum), guarded None-no-op setter
  - [x] Step 4 — Sync docstrings
  - [x] Step 5/6 — Reader/writer: used by SoAdConfig / ServiceInstances routing-group refs
  - [x] Step 7 — Checklist comment
  - [x] Step 8 — Deviations: none (pre-existing)
  - [x] Step 9 — Verify (9a) + confirm (9b): pytest (ARPackage/frame_channel) passed, lint+black clean; # Spec verified: withheld (not yet confirmed/spec-verified)

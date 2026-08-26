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
- [x] SomeipSdClientEventGroupTimingConfig (ARElement value type · Table 6.173 · p.1162 · used by ConsumedEventGroup.sdClientTimerConfig · source ServiceInstances.py · adds requestResponseDelay aggr RequestResponseDelay, subscribeEventgroupRetryDelay attr TimeValue, subscribeEventgroupRetryMax attr, timeToLive attr) · steps complete commit 0e472ca8 — STAMP DEFERRED (batch 9b pending)
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - [x] Step 9 — Verify (9a) + confirm (9b)
- [x] SomeipSdServerEventGroupTimingConfig (ARElement value type · Table 6.172 · p.1162 · used by EventHandler.sdServerEgTimingConfig · source ServiceInstances.py · adds requestResponseDelay aggr RequestResponseDelay) · steps complete commit 601f7bd5 — STAMP DEFERRED (batch 9b pending)
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - [x] Step 9 — Verify (9a) + confirm (9b)
- [x] SomeipServiceVersion (ARObject value type · Table F.118 · used by ConsumedServiceInstance.blacklistedVersion · source ServiceInstances.py · adds majorVersion, minorVersion) · steps complete commit 152f3113 — STAMP DEFERRED (batch 9b pending)
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - [x] Step 9 — Verify (9a) + confirm (9b)
- [x] DhcpServerConfiguration (value type · Table 3.79 · used by InfrastructureServices.dhcpServerConfiguration, VlanMembership.dhcpAddressAssignment) · steps complete commit ecfa6c40 — STAMP DEFERRED (batch 9b pending)
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - [x] Step 9 — Verify (9a) + confirm (9b)
- [x] CouplingPortTrafficClassAssignment (value type · Table 3.75 · used by CouplingPortDetails.ethernetTrafficClassAssignments) · steps complete commit 30c86e62 — STAMP DEFERRED (batch 9b pending)
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - [x] Step 9 — Verify (9a) + confirm (9b)
- [ ] CanXlProps (value type · existing Fibex4Can/CanTopology.py — MOVED from EthernetCommunication.py per Rule 0007: no CP table, CAN-XL domain, aggregated by CanControllerConfiguration · used by EthernetCommunicationConnector.canXlPropsRefs / apApplicationEndpoint) · steps complete commit 4169b432 — STAMP DEFERRED (batch 9b pending)
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
  - [x] Step 9 — Verify (9a) + confirm (9b)
- [x] TagWithOptionalValue (value type · Table 6.159 (CP) / 4.76 (FO) · used by SdClientConfig.capabilityRecord, AbstractServiceInstance.capabilityRecords) · steps complete commit 5241d431 — STAMP DEFERRED (batch 9b pending)
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

- [x] Ipv4DhcpServerConfiguration (value type · Table 3.80 · p.132 · used by DhcpServerConfiguration.ipv4DhcpServerConfiguration · source EthernetTopology.py · resolves DhcpServerConfiguration stub deviation; attrs addressRangeLowerBound, addressRangeUpperBound, defaultGateway, defaultLeaseTime, dnsServerAddresses *, networkMask) — STAMP DEFERRED (batch 9b pending)
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
- [x] Ipv6DhcpServerConfiguration (value type · Table 3.81 · p.132 · used by DhcpServerConfiguration.ipv6DhcpServerConfiguration · source EthernetTopology.py · resolves DhcpServerConfiguration stub deviation; same attr set as Ipv4 variant with Ip6AddressString types) — STAMP DEFERRED (batch 9b pending)
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
- [x] AnyServiceInstanceId (primitive · FO_TPS_GenericStructureTemplate Table E.6 · p.423 · used by ConsumedServiceInstance.instanceIdentifier · resolves String placeholder) — STAMP DEFERRED (batch 9b pending)
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
- [x] AnyVersionString (primitive · FO_TPS_GenericStructureTemplate Table E.7 · p.423 · used by ConsumedServiceInstance.minorVersion · resolves String placeholder) — STAMP DEFERRED (batch 9b pending)
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
- [x] ServiceVersionAcceptanceKindEnum (enum · Table F.113 · p.2057 · used by ConsumedServiceInstance.versionDrivenFindBehavior · resolves ARLiteral placeholder · Steps 5/6 N/A if standalone enum) — STAMP DEFERRED (batch 9b pending)
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
- [ ] PduActivationRoutingGroup (Table 6.161 · p.489 · used by ConsumedEventGroup.pduActivationRoutingGroups AND AbstractServiceInstance.methodActivationRoutingGroup · Identifiable child → createXxx(short_name)) — STAMP DEFERRED (batch 9b pending)
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
    (tracker: eventGroupControlType ARLiteral placeholder — EventGroupControlTypeEnum Table F.114 not queued/not implemented,
     Rule 0001.10; iPduIdentifierTcp/Udp singular→plural convention noted; consumer wiring pending RE-FIX rows)
  - [x] Step 9 — Verify (9a) + confirm (9b)
    (9a automated verification only — pytest 7295 passed, black/black-check/lint clean; 9b stamp DEFERRED to batch pass)
- [ ] StaticSocketConnection (Table 6.201 · p.544 · used by SocketAddress.staticSocketConnections · resolves ARObject placeholder) — STAMP DEFERRED (batch 9b pending)
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
    (tracker: tcpRole ARLiteral placeholder — TcpRoleEnum not queued/not implemented, Rule 0001.10;
     iPduIdentifier/remoteAddress singular→plural/ref naming noted; SocketAddress placeholder row resolved by RE-FIX)
  - [x] Step 9 — Verify (9a) + confirm (9b)
    (9a automated verification only — pytest 7304 passed, black/black-check/lint clean; 9b stamp DEFERRED to batch pass)
- [x] UdpChecksumCalculationEnum (enum · Table 6.119 · p.454 · used by SocketAddress.udpChecksumHandling · resolves ARLiteral placeholder · Steps 5/6 N/A if standalone enum) — STAMP DEFERRED (batch 9b pending)
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
- [ ] SocketAddress RE-FIX (type staticSocketConnections → List[StaticSocketConnection], udpChecksumHandling → UdpChecksumCalculationEnum once they land; remove resolved deviation rows) — STAMP DEFERRED (batch 9b pending)
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
- [ ] CanXlProps NOT CONFIRMED by user (reason pending clarification; canConfig placeholder may resolve via CanControllerConfiguration Table 3.14)

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
- [ ] ApplicationEndpoint (markdown SystemTemplate · Table 6.124 · p.458 · source Fibex4Ethernet/EthernetTopology.py — MOVED from ServiceInstances.py per Rule 0007: Table 6.124 Package row = Fibex4Ethernet::EthernetTopology · adds discoveryTechnology, remotingTechnology, serializationTechnologyRef; these tech member types are XSD/ad-hoc — handle inside this sync) · steps complete commit 92517479 — STAMP DEFERRED (batch 9b pending)
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
- [ ] SoAdConfig (markdown SystemTemplate · Table 6.117 · p.452 · source Fibex4Ethernet/ServiceInstances.py) — STAMP DEFERRED (batch 9b pending); SYNCED AFTER SocketConnection (reorder per Rule 0016.5)
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
- [ ] EventHandler (markdown SystemTemplate · Table 6.166 · p.492 · source Fibex4Ethernet/ServiceInstances.py · depends on SomeipSdServerEventGroupTimingConfig above; adds eventGroupIdentifier, eventMulticastAddress, pduActivationRoutingGroup, sdServerEgTimingConfig) — STAMP DEFERRED (batch 9b pending)
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
- [ ] Ipv6Configuration (markdown SystemTemplate · Table 6.139 · p.466 · source Fibex4Ethernet/EthernetTopology.py — MOVED from NetworkEndpoint.py per Rule 0007: Table 6.139 Package row = Fibex4Ethernet::EthernetTopology · fixes dnsServerAddresses naming → dnsServerAddress) — STAMP DEFERRED (batch 9b pending)
  - [x] Step 1 — Sync members & description from spec
    (Table 6.139 page-split in markdown AUTOSAR_CP_TPS_SystemTemplate.md:12392–12410 + PDF p.466;
    Base ARObject+NetworkEndpointAddress → NetworkEndpointAddress; 9 attr rows; "naming fix" resolved as
    convention alignment: bulk setDnsServerAddresses → addDnsServerAddress/getDnsServerAddresses per Rule 0001.5)
  - [x] Step 2 — Model test rewritten to spec shape (Red — addDnsServerAddress + None no-ops missing)
  - [x] Step 3 — Implement model class (Green)
    (typed annotations incl. ipAddressKeepBehavior/ipv6AddressSource as ARLiteral placeholders —
     IpAddressKeepEnum Table 6.138 / Ipv6AddressSourceEnum not implemented, Rule 0001.10; guarded setters)
  - [x] Step 4 — Sync docstrings (wipe + rewrite) (class Note + all nine Attribute Notes verbatim)
  - [x] Step 5/6 — Reader/writer round-trip test + wiring
    (tests/test_armodel/writer/test_ipv6_configuration.py: write_all/empty + round trip + empty reader;
     DNS-SERVER-ADDRESSES wrapper and IP-ADDRESS-KEEP-BEHAVIOR wired both sides in XSD order;
     stale frame_channel ipv6 writer tests still green)
  - [x] Step 7 — Update checklist comment
  - [x] Step 8 — Deviations
    (tracker: former dnsServerAddress missing row resolved and annotated; two enum placeholders recorded)
  - [x] Step 9 — Verify (9a) + confirm (9b)
    (9a automated verification only — pytest 7332 passed, black/black-check/lint clean; 9b stamp DEFERRED to batch pass)
- [ ] InfrastructureServices (markdown SystemTemplate · Table 6.144 · p.469 · source Fibex4Ethernet/EthernetTopology.py — MOVED from NetworkEndpoint.py per Rule 0007: Table 6.144 Package row = Fibex4Ethernet::EthernetTopology · depends on DhcpServerConfiguration above; adds dhcpServerConfiguration) — STAMP DEFERRED (batch 9b pending)
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
     timeSynchronization inner-members deferral recorded per Rule 0001.10)
  - [x] Step 9 — Verify (9a) + confirm (9b)
    (9a automated verification only — pytest 7336 passed, black/black-check/lint clean; 9b stamp DEFERRED to batch pass)
- [ ] CouplingPortFifo (markdown SystemTemplate · Table 3.68 · p.124 · source Fibex4Ethernet/EthernetTopology.py · fixes assignedTrafficClass type) — STAMP DEFERRED (batch 9b pending)
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
    (tracker: shaper ARObject placeholder — CouplingPortAbstractShaper not implemented, Rule 0001.10;
     trafficClassPreemptionSupport removal recorded per Rule 0015)
  - [x] Step 9 — Verify (9a) + confirm (9b)
    (9a automated verification only — pytest 7341 passed, black/black-check/lint clean; 9b stamp DEFERRED to batch pass)
- [ ] CouplingPortDetails (markdown SystemTemplate · Table 3.63 · p.122 · source Fibex4Ethernet/EthernetTopology.py · depends on CouplingPortTrafficClassAssignment above; fixes ethernetPriorityRegeneration / ethernetTrafficClassAssignment member types) — STAMP DEFERRED (batch 9b pending)
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
    (tracker: globalTimeProps ARObject placeholder recorded; four removed members documented per Rule 0015)
  - [x] Step 9 — Verify (9a) + confirm (9b)
    (9a automated verification only — pytest 7344 passed, black/black-check/lint clean; 9b stamp DEFERRED to batch pass)
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] CouplingPort (markdown SystemTemplate · Table 3.54 · p.110 · source Fibex4Ethernet/EthernetTopology.py · member of EthernetCluster.couplingPorts & EthernetCommunicationController.couplingPorts; adds couplingPortSpeed, vlanModifierRef → EthernetPhysicalChannel Ref) — STAMP DEFERRED (batch 9b pending)
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
    (tracker: six enum placeholders, macSecProps/plcaProps placeholders, stale couplingPortSpeed note resolved;
     macAddressVlanAssignments removal recorded per Rule 0015)
  - [x] Step 9 — Verify (9a) + confirm (9b)
    (9a automated verification only — pytest 7347 passed, black/black-check/lint clean; 9b stamp DEFERRED to batch pass)
- [ ] EthernetCluster (markdown SystemTemplate · Table 3.47 · p.103 · source Fibex4Ethernet/EthernetTopology.py · adds couplingPorts to EthernetCluster; closes open items) — STAMP DEFERRED (batch 9b pending)
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
    (tracker: couplingPortConnections ARObject placeholder — CouplingPortConnection not implemented, Rule 0001.10)
  - [x] Step 9 — Verify (9a) + confirm (9b)
    (9a automated verification only — pytest 7350 passed, black/black-check/lint clean; 9b stamp DEFERRED to batch pass)
- [ ] EthernetCommunicationController (markdown SystemTemplate · Table 3.61 · p.116 · source Fibex4Ethernet/EthernetTopology.py · closes open items) — STAMP DEFERRED (batch 9b pending)
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
    (tracker: new section, macLayerType ARLiteral placeholder for EthernetMacLayerTypeEnum, Rule 0001.10)
  - [x] Step 9 — Verify (9a) + confirm (9b)
    (9a automated verification only — pytest 7353 passed, black/black-check/lint clean; 9b stamp DEFERRED to batch pass)
- [ ] EthernetCommunicationConnector (markdown SystemTemplate · Table 3.62 · p.117 · source Fibex4Ethernet/EthernetTopology.py · depends on CanXlProps above; adds apApplicationEndpoint, canXlPropsRefs, ipV6PathMtuEnabled, ipV6PathMtuTimeout, pncFilterDataMask, unicastNetworkEndpointRefs → NetworkEndpoint Ref) — STAMP DEFERRED (batch 9b pending)
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
- [ ] SdClientConfig (no PDF table · p.870 source EthernetTopology.py · depends on TagWithOptionalValue above; fixes capabilityRecord type) — STAMP DEFERRED (batch 9b pending); XSD-ONLY CLASS (obsolete, no R23-11 table) — Rule 0002 exclusion, no # Spec line/marker applicable
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
- [ ] SocketConnection (obsolete · Table F.116 · p.2057 · source Fibex4Ethernet/ObsoleteModel.py — MOVED from EthernetCommunication.py per Rule 0007: Table F.116 Package row = M2::...::Fibex4Ethernet::ObsoleteModel · adds autosarConnector, doIpSourceAddressRef/doIpTargetAddressRef, ident → TpConnectionIdent, localPortRef/remotePortRef → SocketAddress Ref, nPduRef, socketProtocol) — SYNCED AHEAD OF SoAdConfig (dependency-first, Rule 0016.5); CORRECTION (2026-08-26, Rule 0007 audit): a table DOES exist — Table F.116 in the R23-11 obsolete-model appendix — so this is NOT an XSD-only/Rel-4.4.0 class; the Rule 0002 XSD-exclusion note was stale and has been removed; the checklist keeps the XSD-derived rows for members the F-table lacks (Rule 0015)
  - [x] Step 1 — Derive members from XSD SOCKET-CONNECTION group (AUTOSAR_00052.xsd); Base ARObject+DESCRIBABLE → stays Describable; 19 elements incl. 8 newly modelled
  - [x] Step 2 — Model test rewritten to XSD shape (Red — new accessors missing)
  - [x] Step 3 — Implement model class (Green)
    (adds autosarConnector, doIpSource/TargetAddressRef, ident→TpConnectionIdent, localPortRef, nPduRef,
    remotePortRef, socketProtocol; typed Optional/List fields, guarded setters, verbatim XSD Notes;
    removed non-XSD pduSocketConnectionIpdus duplicate)
  - [x] Step 4 — Sync docstrings (wipe + rewrite)
  - [x] Step 5/6 — Reader/writer extended
    (setSocketConnection/getSocketConnection cover all XSD children in group order incl. IDENT via writeReferrable/
     readReferrable; SoAdConfig CONNECTIONS wrapper wired both sides)
  - [x] Step 7 — Checklist comment (XSD-only form, all rows checked, no marker)
  - [x] Step 8 — Deviations
    (tracker section added; SoAdConnectorType/SoAdProtocolType enums carried as ARLiteral placeholders, Rule 0001.10)
  - [x] Step 9 — Verify (9a) + confirm (9b)
    (9a automated verification only — pytest 7318 passed, black/black-check/lint clean; marker N/A per Rule 0002)
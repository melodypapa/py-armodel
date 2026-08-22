# Sync todo: ProvidedServiceInstance

Input class: ProvidedServiceInstance
Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.160, p.486
Release target: R23-11
Worktree: .worktrees/feature-sync-providedserviceinstance (branch feature/sync-providedserviceinstance-r23-11)

## Closure (confirmed with user)
- input: ProvidedServiceInstance (M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::ServiceInstances)
- base: AbstractServiceInstance (exists, conforms to Table 6.158) — NOT re-queued
- member types:
  - EventHandler (aggr, *) — exists
  - ApplicationEndpoint (ref) — exists
  - SdServerConfig (aggr) — exists
  - PositiveInteger (attr/primitive) — exists
  - SomeipSdServerServiceInstanceConfig (ref target for sdServerTimerConfig) — ref-only, stored as RefType, NOT modeled as a class

## Resolution decisions
- SomeipSdServerServiceInstanceConfig: ref-only dependency (RefType). No class modeled.

## Queue (dependency-first)
- [ ] ProvidedServiceInstance  — add missing attrs: loadBalancingPriority, loadBalancingWeight, localUnicastAddressRefs (0..2), minorVersion, remoteMulticastSubscriptionAddressRefs (*), remoteUnicastAddressRefs (*), sdServerTimerConfigRef (0..1). Verify base AbstractServiceInstance. Commit: <hash>

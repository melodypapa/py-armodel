# Group 4 Sync Report — BSW behavior policies, ServiceNeeds & related classes

Branch: `feature/sync-group4` · Generated: 2026-09-18 · Methodology: `docs/plan/sync-todo/Group4.md` (queue) + `.agents/skills/sync-autosar-class/` (9-step TDD workflow, Rules 0001–0020)

## 1. Scope and outcome

The Group 4 sync queue ("BSW behavior policies & ServiceNeeds A") is **fully synced**: all 29
class rows carry completed 9-step sub-checklists, and every class source carries a
`# Spec:` checklist in the 6-column format (impl / docstring / test / reader / writer / release).

| Category | Classes | Status |
|---|---|---|
| NEW XSD-derived dependency classes (Rule 0016.4, derive-from-XSD) | BswPerInstanceMemoryPolicy, BswClientPolicy, BswInternalTriggeringPointPolicy, BswParameterPolicy, BswReleasedTriggerPolicy, BswDataSendPolicy | **Verified** — `# XSD verified: AUTOSAR_00052.xsd` (R23-11) |
| Tracker inputs with own R23-11 table | BswInternalBehavior, ServiceNeeds, DiagEventDebounceAlgorithm, DiagEventDebounceMonitorInternal, EcuStateMgrUserNeeds, DltUserNeeds, DiagnosticComponentNeeds | **Verified** — `# Spec verified: R23-11` |
| Tracker inputs synced in batch mode | DiagnosticUploadDownloadNeeds, DiagnosticsCommunicationSecurityNeeds, FunctionInhibitionNeeds, GlobalSupervisionNeeds, HardwareTestNeeds, SupervisedEntityCheckpointNeeds, SyncTimeBaseMgrUserNeeds, BswMgrNeeds, CryptoKeyManagementNeeds, CryptoServiceJobNeeds, DiagnosticControlNeeds, DiagnosticEventManagerNeeds, DiagnosticRequestFileTransferNeeds, DoIpActivationLineNeeds, DoIpGidNeeds, DoIpGidSynchronizationNeeds | **Synced & committed — `# Spec verified:` stamps HELD** pending batch-review decision (see §5) |

The batch was executed in autonomous mode with a user-mandated modification: each class was
committed **without** its marker first, so the `# Spec verified:` stamp could be applied in one
reviewed batch. During the run, 5 classes were individually user-confirmed and stamped
mid-batch; the remaining 16 passed the full automated gate (9a) but their stamps are held.

## 2. Verification results (9a, run before push)

| Gate | Result |
|---|---|
| Unit suite (`python scripts/run_tests.py --unit`) | **9,330 passed / 0 failed** |
| Integration round-trip (29-file ARXML corpus, parse→write→re-parse→compare) | 2/2 PASS |
| `npm run lint` (flake8 E9/F63/F7/F82 + ruff E/F/W/I) | clean |
| `npm run black-check` (200-char) | clean |
| `scripts/check_model_test_parity.py` (set-based file-presence + class coverage) | OK |
| Per-class touched-file pytest runs | all Green, Red observed before each Green |

## 3. Per-class summary (batch-synced classes)

All 16 held classes share one profile: concrete `Class` (XSD `abstract="false"`),
**zero own attributes** (inheritance-only marker classes — the Attribute section of each spec
table is empty), class docstring = spec `Note` copied verbatim (markdown-primary, cross-checked
against sibling TPS copies and the XSD group documentation), `__init__` docless, single
`__init__` checklist row with `[—] reader [—] writer`, no deviations, release R23-11.

| Class | Spec table (page) | Most-derived base | Sync commit | In-pass fixes |
|---|---|---|---|---|
| DiagnosticUploadDownloadNeeds | BSW TPS 12.29 (p.252) | DiagnosticCapabilityElement (fixed) | fe8a0a1a | base correction + 5-place dispatch |
| DiagnosticsCommunicationSecurityNeeds | BSW TPS 12.27 (p.248) | DiagnosticCapabilityElement (fixed) | d24a6663 | base correction + 5-place dispatch |
| FunctionInhibitionNeeds | BSW TPS 12.19 (p.237) | ServiceNeeds | 757041c3 | 5-place dispatch |
| GlobalSupervisionNeeds | Swc TPS 13.4 (p.709) | ServiceNeeds | 75f98f45 | 5-place dispatch |
| HardwareTestNeeds | BSW TPS 12.40 (p.264) | ServiceNeeds | 414b28bf | 5-place dispatch |
| SupervisedEntityCheckpointNeeds | BSW TPS 12.30 (p.254) | ServiceNeeds | 67640c80 | 5-place dispatch |
| SyncTimeBaseMgrUserNeeds | BSW TPS 12.17 (p.236) | ServiceNeeds | 609f148a | 5-place dispatch |
| BswMgrNeeds | Swc TPS 13.8 (p.716) | ServiceNeeds | 628464ed | none — BSW dispatch pre-existed; XSD has no Swc-side element entry |
| CryptoKeyManagementNeeds | Swc TPS 13.11 (p.745) | ServiceNeeds | dc49a716 | 5-place dispatch |
| CryptoServiceJobNeeds | Swc TPS 13.10 (p.733) | ServiceNeeds | 2ec47467 | 5-place dispatch |
| DiagnosticControlNeeds | Swc TPS 13.63 (p.812) | DiagnosticCapabilityElement (fixed) | d0a1134e | base correction + 5-place dispatch |
| DiagnosticEventManagerNeeds | Swc TPS 13.14 (p.753) | DiagnosticCapabilityElement (fixed) | dc347744 | base correction + 5-place dispatch |
| DiagnosticRequestFileTransferNeeds | Swc TPS 13.43 (p.795) | DiagnosticCapabilityElement (fixed) | f084c432 | base correction + 5-place dispatch |
| DoIpActivationLineNeeds | Swc TPS 13.60 (p.807) | DoIpServiceNeeds (fixed) | bf846cce | base correction + 5-place dispatch + class relocation |
| DoIpGidNeeds | Swc TPS 13.55 (p.805) | DoIpServiceNeeds (fixed) | 6c31e005 | base correction + 5-place dispatch |
| DoIpGidSynchronizationNeeds | Swc TPS 13.56 (p.806) | DoIpServiceNeeds (fixed) | c64cb631 | base correction + 5-place dispatch |

Mid-batch stamped classes: DiagEventDebounceAlgorithm (63deeb9b), DiagEventDebounceMonitorInternal
(c34a2602), EcuStateMgrUserNeeds (e8405c18), DltUserNeeds (234eb675), DiagnosticComponentNeeds
(394cd617) — all pure marker/abstract classes with zero own attributes; DiagEventDebounceAlgorithm
is abstract with Identifiable base; DiagnosticComponentNeeds had its base corrected to
DiagnosticCapabilityElement and received new reader/writer dispatch.

Earlier rows (previous sessions, same branch): ServiceNeeds (5fd6271d) — pure abstract marker,
Base = Identifiable, class Note taken from the sibling Swc TPS Table 7.52 copy; BswInternalBehavior
(89a72317) — 22 own aggregations, 7 missing BSW wrappers added; the six BSW policy classes above
were created new from `AUTOSAR_00052.xsd` with `# XSD verified:` markers.

## 4. Recurring findings and how they were handled

1. **Wrong most-derived base (Rule 0001.2) — 7 classes fixed in-pass.** The affected classes
   derived from `ServiceNeeds` in src while their spec `Base` rows name `DiagnosticCapabilityElement`
   (4 classes) or `DoIpServiceNeeds` (3 classes). Corrected; verified against the XSD group-ref
   chains. `DoIpServiceNeeds` is itself stamped (Table 13.54, p.805).
2. **Missing concrete-element reader/writer dispatch (Rule 0001.7).** For 14 classes the
   `SERVICE-NEEDS` dispatch had no branch. Added the five-place pattern: parser import + BSW-side
   branch in `readBswServiceDependencyServiceNeeds` + Swc-side branch in
   `readSwcServiceDependencyServiceNeeds` (via `create<Xxx>Needs` factory on `SwcServiceDependency`),
   writer import + isinstance branches in both `writeBsw/SwcServiceDependencyServiceNeeds` chains,
   and `read<Xxx>Needs`/`write<Xxx>Needs` helpers. Branch order follows the XSD `sequenceOffset`
   (alphabetical) element order of the two `SERVICE-NEEDS` choice groups.
3. **Markdown render artifacts.** Several BSW/Swc TPS table bodies render *before* their captions
   (or the Note row is dropped, as in BSW Table 12.6). Resolved per class by matching table bodies
   to captions and cross-checking Notes against sibling copies and the XSD documentation;
   the markdown (not the XSD doc wording) is primary per Rule 0015.
4. **Class relocation.** The three DoIp classes were physically moved after `DoIpServiceNeeds`'s
   definition (they previously preceded their base, which is a forward-reference `NameError` once
   the base changed).
5. **Test coverage added.** One mirrored model test file per class (initialization/wiring,
   verbatim-Note docstring assertion, `__init__`-docless assertion) plus parser/writer dispatch
   tests (minimal read, standalone write, collective all-needs dispatch).

## 5. Open items

- **16 held stamps.** The batched 9b confirmation for the classes in §3 returned "hold". The
  classes are spec-synced and committed, but their sources intentionally carry **no**
  `# Spec verified:` marker and their todo rows remain `[ ]` until the review decision is made.
- **`DiagnosticCapabilityElement` is an unstamped stub** (Rule 0001.10). It now carries three
  newly-stamped-candidate subclasses plus previously-stamped ones; it needs its own 9-step sync
  pass (Swc TPS Table 13.15 area) — its accessors are untyped, docstrings paraphrased, checklist
  is the legacy 4-column format.
- **Legacy deviation tracker staleness.** `docs/examples/method_deviation_by_class_v2.md` still
  carries stale `missing` rows and wrong table ids for classes synced in this group (e.g.
  FunctionInhibitionNeeds → 12.20, DiagnosticsCommunicationSecurityNeeds → 12.28,
  GlobalSupervisionNeeds, HardwareTestNeeds). Untouched in this branch; needs a cleanup pass.
- **Fellow unstamped classes in ServiceNeeds.py** remain outside Group 4 scope (e.g.
  NvBlockNeeds, ComMgrUserNeeds, ErrorTracerNeeds, IdsMgrNeeds, IndicatorStatusNeeds,
  SecureOnBoardCommunicationNeeds, DoIpPowerModeStatusNeeds, Obd*Needs, V2x*Needs,
  VendorSpecificServiceNeeds, RoleBasedDataAssignment, plus the DiagEventDebounce*
  subclass attribute tables) — queue rows exist only for the Group 4 list.

## 6. Branch commits (42 total, `main..feature/sync-group4`)

Per-class `feat: <ClassName> synced.` commits with paired `chore:` hash-recording commits; the 5
mid-batch stamps are `chore: stamp <ClassName> Spec verified R23-11 (batch 9b)`; this report is
committed as `docs: Group 4 sync report`.

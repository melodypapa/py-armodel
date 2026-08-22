# Sync Queue: CAN Topology (CanCluster / CanCommunicationController / CanControllerFdConfiguration)

Input classes: `CanCluster`, `CanCommunicationController`, `CanControllerFdConfiguration` (+ bases per user)
Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf — Fibex CAN chapter
Created: 2026-08-22

## Closure (confirmed)
| Class | Role | Spec | Notes |
|-------|------|------|-------|
| CanCluster | input | Table 3.9, p.62 | marker class; 0 own attributes; base AbstractCanCluster |
| CanCommunicationController | input | Table 3.11, p.63 | marker class; 0 own attributes; base AbstractCanCommunicationController |
| CanControllerFdConfiguration | input | Table 3.16, p.66 | 7 attr: paddingValue, propSeg, sspOffset, syncJumpWidth, timeSeg1, timeSeg2, txBitRateSwitch; base ARObject |
| AbstractCanCluster | base | Table 3.8 | included per user; attrs busOffRecovery(CanClusterBusOffRecovery), canFdBaudrate, canXlBaudrate; member type exists |
| AbstractCanCommunicationController | base | Table 3.12 | included per user; attr canControllerAttributes(AbstractCanCommunicationControllerAttributes); member type exists |

Member-type classes (CanClusterBusOffRecovery, AbstractCanCommunicationControllerAttributes) exist as model classes — referenced, not synced this pass.

## Queue (dependency-first)
- [x] AbstractCanCluster (feat: 2853390c)
- [x] CanCluster (feat: 79861080)
- [x] AbstractCanCommunicationController (feat: 963f579c)
- [ ] CanCommunicationController
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
- [ ] CanControllerFdConfiguration
  - [ ] Step 1 — Sync members & description from spec
  - [ ] Step 2 — Write model class unit test (Red)
  - [ ] Step 3 — Implement model class (Green)
  - [ ] Step 4 — Sync docstrings (wipe + rewrite)
  - [ ] Step 5 — Write reader/writer round-trip test (Red)
  - [ ] Step 6 — Update parser & writer (Green)
  - [ ] Step 7 — Update checklist comment
  - [ ] Step 8 — Deviations
  - [ ] Step 9 — Verify (9a) + confirm (9b)
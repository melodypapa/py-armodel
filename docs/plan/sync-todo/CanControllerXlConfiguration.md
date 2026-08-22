# Sync Queue: CanControllerXlConfiguration / CanControllerXlConfigurationRequirements / AbstractCanCommunicationControllerAttributes

Input classes: `CanControllerXlConfiguration`, `CanControllerXlConfigurationRequirements` (+ `AbstractCanCommunicationControllerAttributes` added per user)
Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf — Fibex CAN chapter (Tables 3.18, 3.19, 3.13)
Release target: R23-11
Created: 2026-08-22

## Closure (confirmed)
| Class | Role | Base | Spec | Notes |
|-------|------|------|------|-------|
| CanControllerXlConfiguration | input | ARObject | Table 3.18, p.71 | 10 attr (all 0..1 attr): errorSignalingEnabled, propSeg, pwmL, pwmO, pwmS, sspOffset, syncJumpWidth, timeSeg1, timeSeg2, trcvPwmModeEnabled. EXISTING fields are fabricated/wrong (arbitrationPhaseSeg1, dataPhaseSeg1, timeSeg1Arbitration, xlBitRateSwitch, ...) → full resync. |
| CanControllerXlConfigurationRequirements | input | ARObject | Table 3.19, p.72 | 16 attr (all 0..1 attr): errorSignalingEnabled, maxNumberOfTimeQuantaPerBit, maxPwmL, maxPwmO, maxPwmS, maxSamplePoint, maxSyncJumpWidth, maxTrcvDelayCompensationOffset, minNumberOfTimeQuantaPerBit, minPwmL, minPwmO, minPwmS, minSamplePoint, minSyncJumpWidth, minTrcvDelayCompensationOffset, trcvPwmModeEnabled. EXISTING fields fabricated/wrong → full resync. |
| AbstractCanCommunicationControllerAttributes | added (consumer) | ARObject (abstract) | Table 3.13, p.64 | 4 aggr (0..1): canControllerFdAttributes, canControllerFdRequirements, canControllerXlAttributes, canControllerXlRequirements. Getter/setter exist; reader/writer coverage missing ([ ]). |

Member types referenced (all already exist in PrimitiveTypes / same module, referenced not re-synced this pass):
- Primitives: Boolean, PositiveInteger, Float, Integer, TimeValue (GenericStructure.GeneralTemplateClasses.PrimitiveTypes)
- CanControllerFdConfiguration, CanControllerFdConfigurationRequirements (same module — already implemented, referenced by AbstractCanCommunicationControllerAttributes)

## Queue (dependency-first — XL config classes before the abstract class that aggregates them)
- [x] CanControllerXlConfiguration (commit d8b47de7)
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite verbatim)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment (# Spec: line + rows; marker deferred to 9b)
  - [x] Step 8 — Deviations (none expected)
  - [x] Step 9 — Verify (9a) + confirm (9b) ⇒ write # Spec verified: R23-11
- [x] CanControllerXlConfigurationRequirements (commit 5fcfd96f)
  - [x] Step 1 — Sync members & description from spec
  - [x] Step 2 — Write model class unit test (Red)
  - [x] Step 3 — Implement model class (Green)
  - [x] Step 4 — Sync docstrings (wipe + rewrite verbatim)
  - [x] Step 5 — Write reader/writer round-trip test (Red)
  - [x] Step 6 — Update parser & writer (Green)
  - [x] Step 7 — Update checklist comment (# Spec: line + rows; marker deferred to 9b)
  - [x] Step 8 — Deviations (none expected)
  - [x] Step 9 — Verify (9a) + confirm (9b) ⇒ write # Spec verified: R23-11
- [x] AbstractCanCommunicationControllerAttributes (commit d501d4ec)
   - [x] Step 1 — Sync members & description from spec
   - [x] Step 2 — Write model class unit test (Red)
   - [x] Step 3 — Implement model class (Green)
   - [x] Step 4 — Sync docstrings (wipe + rewrite verbatim)
   - [x] Step 5 — Write reader/writer round-trip test (Red)
   - [x] Step 6 — Update parser & writer (Green)
   - [x] Step 7 — Update checklist comment (# Spec: line + rows; marker deferred to 9b)
   - [x] Step 8 — Deviations (none expected)
   - [x] Step 9 — Verify (9a) + confirm (9b) ⇒ write # Spec verified: R23-11

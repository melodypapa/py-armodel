# ServiceNeeds Class Sync Report (R23-11)

Date: 2026-08-20

Scope: sync of 7 input ServiceNeeds classes against the AUTOSAR CP R23-11
SoftwareComponentTemplate spec, plus 4 dependency classes required to stamp them
(per the `sync-autosar-class` Phase 0 closure). All classes live in
`src/armodel/models/M2/AUTOSARTemplates/CommonStructure/ServiceNeeds.py`.

## Summary

| # | Class | Spec table | p. | Base | Attributes / literals |
|---|---|---|---|---|---|
| 1 | DoIpServiceNeeds | 13.54 | 805 | ServiceNeeds, ABC (abstract) | — (base only) |
| 2 | ObdRatioConnectionKindEnum | 13.46 | 796 | AREnum | `apiUse`, `observer` |
| 3 | DiagnosticDenominatorConditionEnum | 13.52 | 803 | AREnum | `_500miles`, `coldstart`, `csers`, `evap`, `evappurgeflow`, `individual`, `obd` |
| 4 | VerificationStatusIndicationModeEnum | 13.69 | 824 | AREnum | `failureAndSuccess`, `failureOnly` |
| 5 | ObdRatioServiceNeeds | 13.44 | 795 | DiagnosticCapabilityElement | `connectionType`, `rateBasedMonitoredEventRef`, `usedFidRef` |
| 6 | ObdRatioDenominatorNeeds | 13.51 | 803 | ServiceNeeds | `denominatorCondition` |
| 7 | DoIpRoutingActivationAuthenticationNeeds | 13.58 | 806 | DoIpServiceNeeds | `dataLengthRequest`, `dataLengthResponse`, `routingActivationType` |
| 8 | DoIpRoutingActivationConfirmationNeeds | 13.59 | 807 | DoIpServiceNeeds | `dataLengthRequest`, `dataLengthResponse`, `routingActivationType` |
| 9 | SecureOnBoardCommunicationNeeds | 13.68 | 824 | ServiceNeeds | `verificationStatusIndicationMode` |
| 10 | IdsMgrNeeds | 13.81 | 842 | ServiceNeeds | `useSmartSensorApi` |

Additionally, the previously-stamped `DiagnosticOperationCycleNeeds` (13.24, p.761)
and its member enum `OperationCycleTypeEnum` (13.25) were re-verified against the
spec and confirmed unchanged.

## Work performed

- **Model** — all 10 classes rewritten/created following the sync rules:
  PEP 526 annotated members (`Optional[T] = None`), `setXxx` guarded setters
  (None no-op, return `self`), most-derived base from the spec `Base` chain,
  fields in displayed spec-row order, and per-literal spec descriptions as inline
  comments on every enum value.
- **Docstrings** — class docstrings, inline `__init__` member comments, and
  getter/setter docstrings copied verbatim from the spec `Note` text (diff-checked).
- **Reader/writer** — dispatch branches added in both the BSW and SWC
  `ServiceNeeds` aggregators (`read/writeBswServiceDependencyServiceNeeds`,
  `read/writeSwcServiceDependencyServiceNeeds`), 6 `readXxx` parser helpers, 6
  `writeXxx` writer helpers, and 6 `createXxx` factory methods on
  `SwcServiceDependency` (`ServiceMapping.py`).
- **Tests** — 21 new tests in
  `tests/test_armodel/models/M2/AUTOSARTemplates/CommonStructure/test_ServiceNeeds.py`:
  initialization, get/set round-trip + None no-op per attribute, enum values, and
  lossless BSW and SWC round-trips (asserting field values).
- **Tooling** — new `.agents/skills/sync-autosar-class/pdf_page.py` script that
  locates the spec table page (`p.NN`) in `autosar/pdf/*.pdf` with a cached
  per-PDF index; `SKILL.md` updated to reference it in Steps 1/4.

## Verification

- Full test suite: 6599 passed.
- `flake8` (E9/F63/F7/F82), `ruff check`, `black-check`: clean.
- Set-based checklist-vs-methods script: `checklist == methods` and full test
  coverage for every synced class.
- Verbatim-Note diff: every class/attribute `Note` appears character-for-character
  in the model source.
- Integration round-trip (parse → write → re-parse) green.

## Disclosures / deviations

1. **ObdRatioDenominatorNeeds** has no class `Note` in the markdown/PDF table
   (only Class + Aggregated by + Attribute). The class docstring uses the XSD
   `documentation` text verbatim ("...performance ration denominator" — the spec's
   own spelling is preserved).
2. **SecureOnBoardCommunicationNeeds** class `Note` states "This class currently
   contains no attributes" while table 13.68 lists
   `verificationStatusIndicationMode`. The stale `Note` was copied verbatim per the
   verbatim-docstring rule.
3. **FunctionInhibitionNeeds** (ref target of `ObdRatioServiceNeeds.usedFid`)
   remains an unstamped stub — out of scope (`ref` attributes use `RefType`, which
   does not require the target class to be synced).
4. **`ObdRatioServiceNeeds.usedSecondaryFid`** exists in the XSD but is absent from
   the PDF table 13.44; per Rule 0015 (PDF/markdown wins) it is not modeled.
5. Enum member values are the spec **literal names** (e.g. `_500miles`,
   `apiUse`); `xml.name` overrides (e.g. `-500-MILES`) are serialization details not
   represented in the model, consistent with existing synced enums.

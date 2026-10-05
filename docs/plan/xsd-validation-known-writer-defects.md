# XSD Validation — Known Writer/Model Defects

The `ARXMLWriter.save()` XSD validation gate (R23-11, `AUTOSAR_00052.xsd`) surfaced a set of pre-existing
writer/model defects: the generated XML is genuinely schema-invalid for the affected paths. The unit tests
covering those paths currently construct `ARXMLWriter(options={"validate": False})` /
`ARXMLParser(options={"validate": False})` (each marked with a `# known writer defect: ...` comment) so they
still verify round-trip fidelity while validation is suppressed. Fixing a defect means fixing the product
(writer/parser/model, never the gate) and then removing the `validate: False` marker from the listed tests.

Burn-down is per root cause: one row group per shared cause.

| Test | Root cause (one line) | Schema error (short) |
| --- | --- | --- |
| `tests/test_armodel/writer/test_writer_diagnostic_data_identifier.py::TestWriteDiagnosticDataIdentifier::test_round_trip` | PIV-VP group (cause C1): writer nests the attribute value in a `POSITIVE-INTEGER-VALUE-VARIATION-POINT` child element the schema does not allow | `POSITIVE-INTEGER-VALUE-VARIATION-POINT: This element is not expected.` |
| `tests/test_armodel/writer/test_writer_diagnostic_dynamic_data_identifier.py::TestWriteDiagnosticDynamicDataIdentifier::test_round_trip` | PIV-VP group (cause C1) | `POSITIVE-INTEGER-VALUE-VARIATION-POINT: This element is not expected.` |
| `tests/test_armodel/writer/test_writer_diagnostic_freeze_frame.py::TestWriteDiagnosticFreezeFrame::test_round_trip_preserves_field_values` | PIV-VP group (cause C1) | `POSITIVE-INTEGER-VALUE-VARIATION-POINT: This element is not expected.` |
| `tests/test_armodel/writer/test_writer_diagnostic_protocol.py::TestWriteDiagnosticProtocol::test_round_trip` | PIV-VP group (cause C1), also the `BOOLEAN-VALUE-VARIATION-POINT` variant | `POSITIVE-INTEGER-VALUE-VARIATION-POINT` / `BOOLEAN-VALUE-VARIATION-POINT: This element is not expected.` |
| `tests/test_armodel/writer/test_writer_diagnostic_routine.py::TestWriteDiagnosticRoutine::test_round_trip_preserves_field_values` | PIV-VP group (cause C1) | `POSITIVE-INTEGER-VALUE-VARIATION-POINT: This element is not expected.` |
| `tests/test_armodel/writer/test_writer_diagnostic_trouble_code_group.py::TestWriteDiagnosticTroubleCodeGroup::test_round_trip_preserves_field_values` | PIV-VP group (cause C1) | `POSITIVE-INTEGER-VALUE-VARIATION-POINT: This element is not expected.` |
| `tests/test_armodel/writer/test_writer_diagnostic_event.py::TestWriteDiagnosticEvent::test_round_trip_preserves_field_values` | PIV-VP group (cause C1) plus a second defect: `DIAGNOSTIC-CONNECTED-INDICATOR` written without its required `SHORT-NAME` | `POSITIVE-INTEGER-VALUE-VARIATION-POINT: This element is not expected.`; `INDICATOR-REF: This element is not expected. Expected is (SHORT-NAME).` |
| `tests/test_armodel/writer/test_writer_diagnostic_memory_destination_primary.py::TestWriteDiagnosticMemoryDestinationPrimary::test_round_trip_preserves_field_values` | Writer's `DIAGNOSTIC_TYPE_OF_DTC_SUPPORTED_XML_MAP` emits single-dash tokens where the XSD enumeration requires double-dash (`ISO-14229--1`) | `TYPE-OF-DTC-SUPPORTED: value 'ISO-14229-1' is not an element of {'ISO-11992--4', 'ISO-14229--1', 'ISO-15031--6', 'SAE-J-1939--73', 'SAE-J-2012--DA'}` |
| `tests/test_armodel/writer/test_bsw_behavior.py::TestBswExclusiveAreaPolicy::test_round_trip_full` | Model's `ApiPrincipleEnum` serializes `COMMON` as lowercase `common` where the XSD requires `COMMON` | `API-PRINCIPLE: value 'common' is not an element of {'COMMON', 'PER-EXECUTABLE'}` |
| `tests/test_armodel/writer/test_writer_bsw_module.py::TestWriterBswInternalBehaviorFullSync::test_round_trip_full_sync_wrappers` | Writer writes `VARIATION-POINT-PROXYS` in the wrong position within `BSW-INTERNAL-BEHAVIOR` | `VARIATION-POINT-PROXYS: This element is not expected. Expected is one of (SCHEDULER-NAME-PREFIXS, RECEPTION-POLICYS, DISTINGUISHED-PARTITIONS).` |
| `tests/test_armodel/writer/test_writer_diagnostic_trouble_code.py::TestWriteDiagnosticTroubleCode::test_round_trip_preserves_short_name` | DIAGNOSTIC-TROUBLE-CODE-position group (cause C2): writer writes `DIAGNOSTIC-TROUBLE-CODE` as an AR-PACKAGE element where R23-11 does not allow it (not a packageable element position) | `DIAGNOSTIC-TROUBLE-CODE: This element is not expected.` |
| `tests/test_armodel/writer/test_writer_diagnostic_trouble_code.py::TestWriteDiagnosticTroubleCode::test_round_trip_empty` | DIAGNOSTIC-TROUBLE-CODE-position group (cause C2) | `DIAGNOSTIC-TROUBLE-CODE: This element is not expected.` |
| `tests/test_armodel/writer/test_writer_documentation.py::TestDocumentationRoundTrip::test_round_trip` | BASE-REF-position group (cause C3): writer writes `BASE-REF` inside `FEATURE-IREF` (`ANY-INSTANCE-REF`), which the R23-11 `ANY-INSTANCE-REF` group does not allow | `BASE-REF: This element is not expected. Expected is one of (CONTEXT-ELEMENT-REF, TARGET-REF, VARIATION-POINT).` |
| `tests/test_armodel/writer/test_writer_ecuc_def.py::TestWriterEcucStringParamDef::test_round_trip_all_attrs` | SHORT-NAME-position group (cause C4): writer writes `SHORT-NAME` in the wrong position within the ECUC def element | `SHORT-NAME: This element is not expected. Expected is one of (DEFAULT-VALUE, MAX-LENGTH, MIN-LENGTH, REGULAR-EXPRESSION, VARIATION-POINT).` |
| `tests/test_armodel/writer/test_writer_ecuc_def.py::TestWriterEcucFunctionNameDef::test_round_trip_function_name_default_value` | SHORT-NAME-position group (cause C4) | same as above |
| `tests/test_armodel/writer/test_writer_ecuc_def.py::TestWriterEcucMultilineStringParamDef::test_round_trip_multiline_default_value` | SHORT-NAME-position group (cause C4) | same as above |
| `tests/test_armodel/writer/test_writer_ecuc_def.py::TestWriterEcucLinkerSymbolDef::test_round_trip` | SHORT-NAME-position group (cause C4) | same as above |
| `tests/test_armodel/writer/test_writer_signal_service_translation.py::TestSignalServiceTranslationWriter::test_round_trip_full` | Writer writes `SIGNAL-SERVICE-TRANSLATION-PROPS` in the wrong position (outside the `SIGNAL-SERVICE-TRANSLATION-PROPSS` wrapper) | `SIGNAL-SERVICE-TRANSLATION-PROPS: This element is not expected.` |
| `tests/test_armodel/writer/test_writer_signal_service_translation.py::TestSignalServiceTranslationWriter::test_no_wrapper_when_empty` | same as above | same as above |
| `tests/test_armodel/writer/test_writer_sw_component.py::TestSwComponentTypeDocumentationRoundTrip::test_round_trip_with_documentation` | Writer writes `SW-COMPONENT-DOCUMENTATION` in the wrong position within the SW component type | `SW-COMPONENT-DOCUMENTATION: This element is not expected.` |
| `tests/test_armodel/writer/test_writer_sw_component.py::TestSwComponentTypeDocumentationRoundTrip::test_round_trip_with_msr_query_members` | same as above | same as above |
| `tests/test_armodel/writer/test_writer_sw_component.py::TestSwComponentTypeDocumentationRoundTrip::test_round_trip_with_topic_content_or_msr_query` | same as above | same as above |
| `tests/test_armodel/writer/test_writer_controllers_ecu.py::TestWriterEcuInstance::test_ecu_instance_full_round_trip` | Writer writes `CONSUMED-PROVIDED-SERVICE-INSTANCE-GROUP-REF-CONDITIONAL` as text + `DEST` attribute instead of a nested `CONSUMED-PROVIDED-SERVICE-INSTANCE-GROUP-REF` child | `CONSUMED-PROVIDED-SERVICE-INSTANCE-GROUP-REF-CONDITIONAL: attribute 'DEST' is not allowed; character content not allowed (element-only content type)` |

Shared root causes:

- **C1 — PIV-VP group (7 tests):** the writer emits an attribute value wrapped in a
  `POSITIVE-INTEGER-VALUE-VARIATION-POINT` (resp. `BOOLEAN-VALUE-VARIATION-POINT`) child element; the R23-11
  XSD models these attributes as being *of* type `POSITIVE-INTEGER-VALUE-VARIATION-POINT` (mixed text
  content), so the wrapper element itself is never valid.
- **C2 — DIAGNOSTIC-TROUBLE-CODE position (2 tests):** the writer emits `DIAGNOSTIC-TROUBLE-CODE` where an
  AR-PACKAGE element is expected; R23-11 does not define it as a packageable element.
- **C3 — BASE-REF position (1 test):** the writer emits `BASE-REF` inside `ANY-INSTANCE-REF` instance refs;
  the R23-11 `ATP-INSTANCE-REF` group is empty, so `BASE-REF` is not allowed there.
- **C4 — SHORT-NAME position (4 tests):** the writer emits `SHORT-NAME` in the ECUC def's own element group
  position instead of (only) the Identifiable header position.

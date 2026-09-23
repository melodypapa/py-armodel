"""Model tests for DiagnosticServiceTable (Table 4.16, p.59)."""

import inspect

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics import DiagnosticCommonElement
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticContribution import DiagnosticServiceTable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import NameToken, RefType

NOTE = "This meta-class represents a model of a diagnostic service table, i.e. the UDS services applicable for a given ECU. Tags: atp.recommendedPackage=DiagnosticServiceTables"
DIAGNOSTIC_CONNECTION_NOTE = (
    "This represents the DiagnosticConnection that is taken for handling the data transmission for the enclosing DiagnosticServiceTable. "
    "It is possible to refer to more than one diagnostic Connections in order to support more than one diagnostic tester. "
    "Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=diagnosticConnection.diagnosticConnection, diagnosticConnection.variationPoint.shortLabel vh.latestBindingTime=postBuild"
)
ECU_INSTANCE_NOTE = "This represents the applicable EcuInstance for this DiagnosticServiceTable. Stereotypes: atpSplitable Tags: atp.Splitkey=ecuInstance"
PROTOCOL_KIND_NOTE = "This identifies the applicable protocol."
SERVICE_INSTANCE_NOTE = (
    "This represents the collection of DiagnosticService Instances to be considered in the scope of this Diagnostic ServiceTable, " "Stereotypes: atpSplitable Tags: atp.Splitkey=serviceInstance"
)


def _ref(dest, value):
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


def _table():
    parent = AUTOSAR.getInstance()
    ar_root = parent.createARPackage("DiagPkg")
    return DiagnosticServiceTable(ar_root, "TestDiagnosticTable")


class TestDiagnosticServiceTable:
    """Test cases for DiagnosticServiceTable class (Table 4.16, p.59)."""

    def test_is_diagnostic_common_element_subclass(self):
        assert issubclass(DiagnosticServiceTable, DiagnosticCommonElement)
        assert issubclass(DiagnosticServiceTable, Identifiable)

    def test_class_docstring_is_spec_note_verbatim(self):
        assert DiagnosticServiceTable.__doc__ == NOTE

    def test_init_has_no_docstring(self):
        assert DiagnosticServiceTable.__init__.__doc__ is None

    def test_defaults_in_spec_displayed_order(self):
        table = _table()
        assert list(table.__dict__)[-4:] == ["diagnosticConnectionRefs", "ecuInstanceRef", "protocolKind", "serviceInstanceRefs"]
        assert table.getDiagnosticConnectionRefs() == []
        assert table.getEcuInstanceRef() is None
        assert table.getProtocolKind() is None
        assert table.getServiceInstanceRefs() == []

    def test_member_comments_are_spec_notes_verbatim(self):
        source = inspect.getsource(DiagnosticServiceTable.__init__)
        assert "# " + DIAGNOSTIC_CONNECTION_NOTE in source
        assert "# " + ECU_INSTANCE_NOTE in source
        assert "# " + PROTOCOL_KIND_NOTE in source
        assert "# " + SERVICE_INSTANCE_NOTE in source

    def test_add_diagnostic_connection_ref_appends_none_no_op_returns_self(self):
        table = _table()
        ref1 = _ref("DIAGNOSTIC-CONNECTION", "/Diag/Conns/Dc1")
        ref2 = _ref("DIAGNOSTIC-CONNECTION", "/Diag/Conns/Dc2")
        assert table.addDiagnosticConnectionRef(ref1) is table
        table.addDiagnosticConnectionRef(ref2)
        assert table.getDiagnosticConnectionRefs() == [ref1, ref2]
        assert table.addDiagnosticConnectionRef(None) is table
        assert table.getDiagnosticConnectionRefs() == [ref1, ref2]

    def test_ecu_instance_ref_round_trip(self):
        table = _table()
        ref = _ref("ECU-INSTANCE", "/System/EcuInstances/EcuInst1")
        assert table.setEcuInstanceRef(ref) is table
        assert table.getEcuInstanceRef() is ref

    def test_ecu_instance_ref_setter_none_is_no_op(self):
        table = _table()
        ref = _ref("ECU-INSTANCE", "/System/EcuInstances/EcuInst1")
        table.setEcuInstanceRef(ref)
        assert table.setEcuInstanceRef(None) is table
        assert table.getEcuInstanceRef() is ref

    def test_protocol_kind_round_trip(self):
        table = _table()
        kind = NameToken().setValue("UDS")
        assert table.setProtocolKind(kind) is table
        assert table.getProtocolKind() is kind

    def test_protocol_kind_setter_none_is_no_op(self):
        table = _table()
        kind = NameToken().setValue("UDS")
        table.setProtocolKind(kind)
        assert table.setProtocolKind(None) is table
        assert table.getProtocolKind() is kind

    def test_add_service_instance_ref_appends_none_no_op_returns_self(self):
        table = _table()
        ref1 = _ref("DIAGNOSTIC-ECU-RESET", "/Diag/Instances/Der1")
        ref2 = _ref("DIAGNOSTIC-SESSION-CONTROL", "/Diag/Instances/Dsc1")
        assert table.addServiceInstanceRef(ref1) is table
        table.addServiceInstanceRef(ref2)
        assert table.getServiceInstanceRefs() == [ref1, ref2]
        assert table.addServiceInstanceRef(None) is table
        assert table.getServiceInstanceRefs() == [ref1, ref2]

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        import inspect

        assert inspect.cleandoc(DiagnosticServiceTable.getDiagnosticConnectionRefs.__doc__) == DIAGNOSTIC_CONNECTION_NOTE
        assert inspect.cleandoc(DiagnosticServiceTable.addDiagnosticConnectionRef.__doc__) == (DIAGNOSTIC_CONNECTION_NOTE + "\n\nA None value does not extend the diagnosticConnectionRefs list.")
        assert inspect.cleandoc(DiagnosticServiceTable.getEcuInstanceRef.__doc__) == ECU_INSTANCE_NOTE
        assert inspect.cleandoc(DiagnosticServiceTable.setEcuInstanceRef.__doc__) == (ECU_INSTANCE_NOTE + "\n\nA None value is a no-op and does not overwrite an existing ecuInstanceRef.")
        assert inspect.cleandoc(DiagnosticServiceTable.getProtocolKind.__doc__) == PROTOCOL_KIND_NOTE
        assert inspect.cleandoc(DiagnosticServiceTable.setProtocolKind.__doc__) == (PROTOCOL_KIND_NOTE + "\n\nA None value is a no-op and does not overwrite an existing protocolKind.")
        assert inspect.cleandoc(DiagnosticServiceTable.getServiceInstanceRefs.__doc__) == SERVICE_INSTANCE_NOTE
        assert inspect.cleandoc(DiagnosticServiceTable.addServiceInstanceRef.__doc__) == (SERVICE_INSTANCE_NOTE + "\n\nA None value does not extend the serviceInstanceRefs list.")

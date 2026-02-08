"""
This module contains comprehensive tests for the DiagnosticContribution.py file
in the AUTOSAR DiagnosticExtract module.
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticContribution import (
    DiagnosticServiceTable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
    RefType,
)


class TestDiagnosticServiceTable:
    """
    Test class for DiagnosticServiceTable functionality.
    """

    def test_initialization(self):
        """
        Test DiagnosticServiceTable initialization with parent and short name.
        """
        # Create parent AUTOSAR structure
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        # Create DiagnosticServiceTable instance
        diagnostic_table = DiagnosticServiceTable(ar_root, "TestDiagnosticTable")

        # Verify basic properties
        assert diagnostic_table is not None
        assert diagnostic_table.getShortName() == "TestDiagnosticTable"

        # Verify default values for attributes
        assert diagnostic_table.getDiagnosticConnectionRefs() == []
        assert diagnostic_table.getDiagnosticServiceInstanceRefs() == []
        assert diagnostic_table.getEcuInstanceRef() is None
        assert diagnostic_table.getProtocolKind() is None

    def test_get_diagnostic_connection_refs(self):
        """
        Test getDiagnosticConnectionRefs method returns empty list by default.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        diagnostic_table = DiagnosticServiceTable(ar_root, "TestDiagnosticTable")

        # Verify initial state
        connection_refs = diagnostic_table.getDiagnosticConnectionRefs()
        assert connection_refs == []
        assert isinstance(connection_refs, list)

    def test_add_diagnostic_connection_ref(self):
        """
        Test addDiagnosticConnectionRef method adds references correctly.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        diagnostic_table = DiagnosticServiceTable(ar_root, "TestDiagnosticTable")

        # Create mock RefType instances
        ref1 = RefType().setValue("Connection1")
        ref2 = RefType().setValue("Connection2")

        # Add first reference
        result = diagnostic_table.addDiagnosticConnectionRef(ref1)
        assert result is diagnostic_table  # Verify method chaining
        assert diagnostic_table.getDiagnosticConnectionRefs() == [ref1]

        # Add second reference
        diagnostic_table.addDiagnosticConnectionRef(ref2)
        assert diagnostic_table.getDiagnosticConnectionRefs() == [ref1, ref2]

    def test_add_diagnostic_connection_ref_none(self):
        """
        Test addDiagnosticConnectionRef method handles None value correctly.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        diagnostic_table = DiagnosticServiceTable(ar_root, "TestDiagnosticTable")

        # Add None value - should not add to list
        result = diagnostic_table.addDiagnosticConnectionRef(None)
        assert result is diagnostic_table  # Verify method chaining
        assert diagnostic_table.getDiagnosticConnectionRefs() == []

    def test_get_diagnostic_service_instance_refs(self):
        """
        Test getDiagnosticServiceInstanceRefs method returns empty list by default.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        diagnostic_table = DiagnosticServiceTable(ar_root, "TestDiagnosticTable")

        # Verify initial state
        service_refs = diagnostic_table.getDiagnosticServiceInstanceRefs()
        assert service_refs == []
        assert isinstance(service_refs, list)

    def test_add_diagnostic_service_instance_ref(self):
        """
        Test addDiagnosticServiceInstanceRef method adds references correctly.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        diagnostic_table = DiagnosticServiceTable(ar_root, "TestDiagnosticTable")

        # Create mock RefType instances
        ref1 = RefType().setValue("ServiceInstance1")
        ref2 = RefType().setValue("ServiceInstance2")

        # Add first reference
        result = diagnostic_table.addDiagnosticServiceInstanceRef(ref1)
        assert result is diagnostic_table  # Verify method chaining
        assert diagnostic_table.getDiagnosticServiceInstanceRefs() == [ref1]

        # Add second reference
        diagnostic_table.addDiagnosticServiceInstanceRef(ref2)
        assert diagnostic_table.getDiagnosticServiceInstanceRefs() == [ref1, ref2]

    def test_add_diagnostic_service_instance_ref_none(self):
        """
        Test addDiagnosticServiceInstanceRef method handles None value correctly.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        diagnostic_table = DiagnosticServiceTable(ar_root, "TestDiagnosticTable")

        # Add None value - should not add to list
        result = diagnostic_table.addDiagnosticServiceInstanceRef(None)
        assert result is diagnostic_table  # Verify method chaining
        assert diagnostic_table.getDiagnosticServiceInstanceRefs() == []

    def test_get_ecu_instance_ref(self):
        """
        Test getEcuInstanceRef method returns None by default.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        diagnostic_table = DiagnosticServiceTable(ar_root, "TestDiagnosticTable")

        # Verify initial state
        ecu_ref = diagnostic_table.getEcuInstanceRef()
        assert ecu_ref is None

    def test_set_ecu_instance_ref(self):
        """
        Test setEcuInstanceRef method sets the reference correctly.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        diagnostic_table = DiagnosticServiceTable(ar_root, "TestDiagnosticTable")

        # Create mock RefType instance
        ecu_ref = RefType().setValue("ECU1")

        # Set the reference
        result = diagnostic_table.setEcuInstanceRef(ecu_ref)
        assert result is diagnostic_table  # Verify method chaining
        assert diagnostic_table.getEcuInstanceRef() == ecu_ref

    def test_set_ecu_instance_ref_none(self):
        """
        Test setEcuInstanceRef method handles None value correctly.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        diagnostic_table = DiagnosticServiceTable(ar_root, "TestDiagnosticTable")

        # Set initial value
        initial_ref = RefType().setValue("ECU1")
        diagnostic_table.setEcuInstanceRef(initial_ref)
        assert diagnostic_table.getEcuInstanceRef() == initial_ref

        # Set to None - should not change the value (per implementation logic)
        result = diagnostic_table.setEcuInstanceRef(None)
        assert result is diagnostic_table  # Verify method chaining
        # Value should remain unchanged due to "if value is not None" check
        assert diagnostic_table.getEcuInstanceRef() == initial_ref

    def test_get_protocol_kind(self):
        """
        Test getProtocolKind method returns None by default.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        diagnostic_table = DiagnosticServiceTable(ar_root, "TestDiagnosticTable")

        # Verify initial state
        protocol_kind = diagnostic_table.getProtocolKind()
        assert protocol_kind is None

    def test_set_protocol_kind(self):
        """
        Test setProtocolKind method sets the protocol kind correctly.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        diagnostic_table = DiagnosticServiceTable(ar_root, "TestDiagnosticTable")

        # Create mock NameToken instance
        protocol_kind = NameToken().setValue("UDS")

        # Set the protocol kind
        result = diagnostic_table.setProtocolKind(protocol_kind)
        assert result is diagnostic_table  # Verify method chaining
        assert diagnostic_table.getProtocolKind() == protocol_kind

    def test_set_protocol_kind_none(self):
        """
        Test setProtocolKind method handles None value correctly.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        diagnostic_table = DiagnosticServiceTable(ar_root, "TestDiagnosticTable")

        # Set initial value
        initial_protocol = NameToken().setValue("UDS")
        diagnostic_table.setProtocolKind(initial_protocol)
        assert diagnostic_table.getProtocolKind() == initial_protocol

        # Set to None - should not change the value (per implementation logic)
        result = diagnostic_table.setProtocolKind(None)
        assert result is diagnostic_table  # Verify method chaining
        # Value should remain unchanged due to "if value is not None" check
        assert diagnostic_table.getProtocolKind() == initial_protocol

    def test_multiple_operations(self):
        """
        Test multiple operations on the same DiagnosticServiceTable instance.
        """
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        diagnostic_table = DiagnosticServiceTable(ar_root, "TestDiagnosticTable")

        # Add multiple connection and service instance references
        conn_ref1 = RefType().setValue("Connection1")
        conn_ref2 = RefType().setValue("Connection2")
        service_ref1 = RefType().setValue("Service1")
        service_ref2 = RefType().setValue("Service2")
        ecu_ref = RefType().setValue("ECU1")
        protocol_kind = NameToken().setValue("UDS")

        # Perform multiple operations
        diagnostic_table.addDiagnosticConnectionRef(conn_ref1)
        diagnostic_table.addDiagnosticConnectionRef(conn_ref2)
        diagnostic_table.addDiagnosticServiceInstanceRef(service_ref1)
        diagnostic_table.addDiagnosticServiceInstanceRef(service_ref2)
        diagnostic_table.setEcuInstanceRef(ecu_ref)
        diagnostic_table.setProtocolKind(protocol_kind)

        # Verify all values are set correctly
        assert diagnostic_table.getDiagnosticConnectionRefs() == [conn_ref1, conn_ref2]
        assert diagnostic_table.getDiagnosticServiceInstanceRefs() == [service_ref1, service_ref2]
        assert diagnostic_table.getEcuInstanceRef() == ecu_ref
        assert diagnostic_table.getProtocolKind() == protocol_kind

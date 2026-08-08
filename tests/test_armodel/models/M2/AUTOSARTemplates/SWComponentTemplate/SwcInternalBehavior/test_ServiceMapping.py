"""
This module contains comprehensive tests for the ServiceMapping module in SWComponentTemplate.SwcInternalBehavior.
Tests cover all classes and methods in the ServiceMapping.py file to achieve 100% test coverage.
"""

import os
import tempfile

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ServiceMapping import RoleBasedPortAssignment, SwcServiceDependency
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    DiagnosticEnableConditionNeeds,
    DiagnosticIndicatorTypeEnum,
    DiagnosticOperationCycleNeeds,
    DiagnosticStorageConditionNeeds,
    EventAcceptanceStatusEnum,
    FunctionInhibitionAvailabilityNeeds,
    IndicatorStatusNeeds,
    OperationCycleTypeEnum,
    StorageConditionStatusEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


class TestRoleBasedPortAssignment:
    """Test class for RoleBasedPortAssignment class."""

    def test_role_based_port_assignment_initialization(self):
        """Test RoleBasedPortAssignment initialization and methods."""
        port_assignment = RoleBasedPortAssignment()

        assert port_assignment.portPrototypeRef is None
        assert port_assignment.role is None

        # Test portPrototypeRef methods
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

        port_ref = RefType()
        port_ref.setValue("/Port/Ref")
        port_assignment.setPortPrototypeRef(port_ref)
        assert port_assignment.getPortPrototypeRef() == port_ref

        # Test role methods
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Identifier

        role = Identifier()
        role.setValue("test_role")
        port_assignment.setRole(role)
        assert port_assignment.getRole() == role


class TestSwcServiceDependency:
    """Test class for SwcServiceDependency class."""

    def test_swc_service_dependency_initialization(self):
        """Test SwcServiceDependency initialization and methods."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        service_dep = SwcServiceDependency(ar_root, "TestSwcServiceDependency")

        assert service_dep.parent == ar_root
        assert service_dep.short_name == "TestSwcServiceDependency"
        assert service_dep._assigned_data == []
        assert service_dep._assigned_ports == []

        # Test assigned data methods
        from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import RoleBasedDataAssignment

        data_assignment = RoleBasedDataAssignment()
        service_dep.AddAssignedData(data_assignment)
        assert data_assignment in service_dep.getAssignedData()

        # Test assigned ports methods
        port_assignment = RoleBasedPortAssignment()
        service_dep.AddAssignedPort(port_assignment)
        assert port_assignment in service_dep.getAssignedPorts()

        # Test service needs creation methods
        nv_block_needs = service_dep.createNvBlockNeeds("TestNvBlockNeeds")
        assert nv_block_needs is not None
        assert nv_block_needs.short_name == "TestNvBlockNeeds"
        assert nv_block_needs in service_dep.getNvBlockNeeds()

        diag_comm_needs = service_dep.createDiagnosticCommunicationManagerNeeds("TestDiagCommNeeds")
        assert diag_comm_needs is not None
        assert diag_comm_needs.short_name == "TestDiagCommNeeds"
        assert diag_comm_needs in service_dep.getDiagnosticCommunicationManagerNeeds()

        diag_routine_needs = service_dep.createDiagnosticRoutineNeeds("TestDiagRoutineNeeds")
        assert diag_routine_needs is not None
        assert diag_routine_needs.short_name == "TestDiagRoutineNeeds"
        assert diag_routine_needs in service_dep.getDiagnosticRoutineNeeds()

        diag_value_needs = service_dep.createDiagnosticValueNeeds("TestDiagValueNeeds")
        assert diag_value_needs is not None
        assert diag_value_needs.short_name == "TestDiagValueNeeds"
        assert diag_value_needs in service_dep.getDiagnosticValueNeeds()

        diag_event_needs = service_dep.createDiagnosticEventNeeds("TestDiagEventNeeds")
        assert diag_event_needs is not None
        assert diag_event_needs.short_name == "TestDiagEventNeeds"
        assert diag_event_needs in service_dep.getDiagnosticEventNeeds()

        diag_event_info_needs = service_dep.createDiagnosticEventInfoNeeds("TestDiagEventInfoNeeds")
        assert diag_event_info_needs is not None
        assert diag_event_info_needs.short_name == "TestDiagEventInfoNeeds"
        assert diag_event_info_needs in service_dep.getDiagnosticEventInfoNeeds()

        io_control_needs = service_dep.createDiagnosticIoControlNeeds("TestIoControlNeeds")
        assert io_control_needs is not None
        assert io_control_needs.short_name == "TestIoControlNeeds"
        assert io_control_needs in service_dep.getDiagnosticIoControlNeeds()

        crypto_needs = service_dep.createCryptoServiceNeeds("TestCryptoNeeds")
        assert crypto_needs is not None
        assert crypto_needs.short_name == "TestCryptoNeeds"
        assert crypto_needs in service_dep.getCryptoServiceNeeds()

        ecu_state_needs = service_dep.createEcuStateMgrUserNeeds("TestEcuStateNeeds")
        assert ecu_state_needs is not None
        assert ecu_state_needs.short_name == "TestEcuStateNeeds"
        assert ecu_state_needs in service_dep.getEcuStateMgrUserNeeds()

        dtc_needs = service_dep.createDtcStatusChangeNotificationNeeds("TestDtcNeeds")
        assert dtc_needs is not None
        assert dtc_needs.short_name == "TestDtcNeeds"
        assert dtc_needs in service_dep.getDtcStatusChangeNotificationNeeds()

        dlt_needs = service_dep.createDltUserNeeds("TestDltNeeds")
        assert dlt_needs is not None
        assert dlt_needs.short_name == "TestDltNeeds"
        assert dlt_needs in service_dep.getDltUserNeeds()

        com_needs = service_dep.createComMgrUserNeeds("TestComNeeds")
        assert com_needs is not None
        assert com_needs.short_name == "TestComNeeds"
        assert com_needs in service_dep.getComMgrUserNeeds()

        enable_condition_needs = service_dep.createDiagnosticEnableConditionNeeds("TestEnableConditionNeeds")
        assert enable_condition_needs is not None
        assert enable_condition_needs.short_name == "TestEnableConditionNeeds"
        assert enable_condition_needs in service_dep.getServiceNeeds()

        operation_cycle_needs = service_dep.createDiagnosticOperationCycleNeeds("TestOperationCycleNeeds")
        assert operation_cycle_needs is not None
        assert operation_cycle_needs.short_name == "TestOperationCycleNeeds"
        assert operation_cycle_needs in service_dep.getServiceNeeds()

        storage_condition_needs = service_dep.createDiagnosticStorageConditionNeeds("TestStorageConditionNeeds")
        assert storage_condition_needs is not None
        assert storage_condition_needs.short_name == "TestStorageConditionNeeds"
        assert storage_condition_needs in service_dep.getServiceNeeds()

        indicator_status_needs = service_dep.createIndicatorStatusNeeds("TestIndicatorStatusNeeds")
        assert indicator_status_needs is not None
        assert indicator_status_needs.short_name == "TestIndicatorStatusNeeds"
        assert indicator_status_needs in service_dep.getServiceNeeds()

        fim_availability_needs = service_dep.createFunctionInhibitionAvailabilityNeeds("TestFimAvailabilityNeeds")
        assert fim_availability_needs is not None
        assert fim_availability_needs.short_name == "TestFimAvailabilityNeeds"
        assert fim_availability_needs in service_dep.getServiceNeeds()

        # Test getting all service needs
        all_service_needs = service_dep.getServiceNeeds()
        assert len(all_service_needs) == 17  # All the ones we created above


class TestSwcServiceDependencyRoundTrip:
    """Test full parse -> write -> re-parse for the 5 new ServiceNeeds via SWC route."""

    def test_swc_service_needs_round_trip(self):
        """Verify all 5 new needs survive an SWC round-trip."""
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        ar_root = document.createARPackage("AUTOSAR")
        swc = ar_root.createApplicationSwComponentType("MySwc")
        behavior = swc.createSwcInternalBehavior("Beh")
        dependency = behavior.createSwcServiceDependency("Dep")

        enable = dependency.createDiagnosticEnableConditionNeeds("EnableNeeds")
        enable.setInitialStatus(EventAcceptanceStatusEnum().setValue(EventAcceptanceStatusEnum.EVENT_ACCEPTANCE_ENABLED))

        cycle = dependency.createDiagnosticOperationCycleNeeds("CycleNeeds")
        cycle.setOperationCycle(OperationCycleTypeEnum().setValue(OperationCycleTypeEnum.WARMUP))

        storage = dependency.createDiagnosticStorageConditionNeeds("StorageNeeds")
        storage.setInitialStatus(StorageConditionStatusEnum().setValue(StorageConditionStatusEnum.EVENT_STORAGE_ENABLE))

        indicator = dependency.createIndicatorStatusNeeds("IndicatorNeeds")
        indicator.setType(DiagnosticIndicatorTypeEnum().setValue(DiagnosticIndicatorTypeEnum.MALFUNCTION))

        fim = dependency.createFunctionInhibitionAvailabilityNeeds("FimNeeds")
        fim_ref = RefType()
        fim_ref.setValue("/Fim/Ref")
        fim.setControlledFidRef(fim_ref)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)

            swc_2 = document_2.getARPackages()[0].getSwComponentTypes()[0]
            behavior_2 = swc_2.getInternalBehavior()
            dependency_2 = behavior_2.getSwcServiceDependencies()[0]
            needs_2 = {n.getShortName(): n for n in dependency_2.getServiceNeeds()}

            assert needs_2["EnableNeeds"].getInitialStatus().getValue() == "eventAcceptanceEnabled"
            assert needs_2["CycleNeeds"].getOperationCycle().getValue() == "warmup"
            assert needs_2["StorageNeeds"].getInitialStatus().getValue() == "eventStorageEnabled"
            assert needs_2["IndicatorNeeds"].getType().getValue() == "malfunction"
            assert needs_2["FimNeeds"].getControlledFidRef().getValue() == "/Fim/Ref"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

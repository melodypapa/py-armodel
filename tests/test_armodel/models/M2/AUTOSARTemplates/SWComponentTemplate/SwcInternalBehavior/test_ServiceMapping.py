"""
This module contains comprehensive tests for the ServiceMapping module in SWComponentTemplate.SwcInternalBehavior.
Tests cover all classes and methods in the ServiceMapping.py file to achieve 100% test coverage.
"""

import pytest
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ServiceMapping import (
    RoleBasedPortAssignment, SwcServiceDependency
)
from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR


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
        
        # Test getting all service needs
        all_service_needs = service_dep.getServiceNeeds()
        assert len(all_service_needs) == 10  # All the ones we created above
"""
This module contains comprehensive tests for the ServiceNeeds.py file
in the AUTOSAR CommonStructure module.
"""

import os
import tempfile

import pytest

from armodel.models import ApplicationSwComponentType
from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior import BswServiceDependency
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    ComMgrUserNeeds,
    CryptoServiceNeeds,
    DevelopmentError,
    DiagEventDebounceAlgorithm,
    DiagEventDebounceCounterBased,
    DiagEventDebounceMonitorInternal,
    DiagEventDebounceTimeBased,
    DiagnosticAudienceEnum,
    DiagnosticCapabilityElement,
    DiagnosticClearDtcNotificationEnum,
    DiagnosticCommunicationManagerNeeds,
    DiagnosticDenominatorConditionEnum,
    DiagnosticEnableConditionNeeds,
    DiagnosticEventInfoNeeds,
    DiagnosticEventNeeds,
    DiagnosticIndicatorTypeEnum,
    DiagnosticIoControlNeeds,
    DiagnosticMonitorUpdateKindEnum,
    DiagnosticOperationCycleNeeds,
    DiagnosticProcessingStyleEnum,
    DiagnosticRoutineNeeds,
    DiagnosticRoutineTypeEnum,
    DiagnosticServiceRequestCallbackTypeEnum,
    DiagnosticStorageConditionNeeds,
    DiagnosticValueAccessEnum,
    DiagnosticValueNeeds,
    DltUserNeeds,
    DoIpRoutingActivationAuthenticationNeeds,
    DoIpRoutingActivationConfirmationNeeds,
    DoIpServiceNeeds,
    DtcFormatTypeEnum,
    DtcKindEnum,
    DtcStatusChangeNotificationNeeds,
    EcuStateMgrUserNeeds,
    ErrorTracerNeeds,
    EventAcceptanceStatusEnum,
    FunctionInhibitionAvailabilityNeeds,
    IdsMgrNeeds,
    IndicatorStatusNeeds,
    MaxCommModeEnum,
    NvBlockNeeds,
    NvBlockNeedsReliabilityEnum,
    NvBlockNeedsWritingPriorityEnum,
    ObdControlServiceNeeds,
    ObdInfoServiceNeeds,
    ObdMonitorServiceNeeds,
    ObdPidServiceNeeds,
    ObdRatioConnectionKindEnum,
    ObdRatioDenominatorNeeds,
    ObdRatioServiceNeeds,
    OperationCycleTypeEnum,
    PossibleErrorReaction,
    RamBlockStatusControlEnum,
    RoleBasedDataAssignment,
    RoleBasedDataTypeAssignment,
    RuntimeError,
    SecureOnBoardCommunicationNeeds,
    ServiceDependency,
    ServiceDiagnosticRelevanceEnum,
    ServiceNeeds,
    ServiceProviderEnum,
    StorageConditionStatusEnum,
    SupervisedEntityNeeds,
    TracedFailure,
    TransientFault,
    VerificationStatusIndicationModeEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, NameToken, PositiveInteger, RefType, TimeValue
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


class TestRoleBasedDataAssignment:
    def test_initialization(self):
        """Test RoleBasedDataAssignment initialization"""
        assignment = RoleBasedDataAssignment()

        assert assignment is not None
        assert assignment.role is None
        assert assignment.usedDataElement is None
        assert assignment.usedParameterElement is None
        assert assignment.usedPimRef is None

    def test_get_set_role(self):
        """Test getRole and setRole methods"""
        assignment = RoleBasedDataAssignment()

        assert assignment.getRole() is None

        assignment.setRole("TestRole")
        assert assignment.getRole() == "TestRole"

    def test_get_set_used_data_element(self):
        """Test getUsedDataElement and setUsedDataElement methods"""
        assignment = RoleBasedDataAssignment()

        assert assignment.getUsedDataElement() is None

        class MockVariableRef:
            pass

        var_ref = MockVariableRef()
        assignment.setUsedDataElement(var_ref)
        assert assignment.getUsedDataElement() == var_ref

    def test_get_set_used_parameter_element(self):
        """Test getUsedParameterElement and setUsedParameterElement methods"""
        assignment = RoleBasedDataAssignment()

        assert assignment.getUsedParameterElement() is None

        class MockParameterRef:
            pass

        param_ref = MockParameterRef()
        assignment.setUsedParameterElement(param_ref)
        assert assignment.getUsedParameterElement() == param_ref

    def test_get_set_used_pim_ref(self):
        """Test getUsedPimRef and setUsedPimRef methods"""
        assignment = RoleBasedDataAssignment()

        assert assignment.getUsedPimRef() is None

        class MockRefType:
            pass

        ref_type = MockRefType()
        assignment.setUsedPimRef(ref_type)
        assert assignment.getUsedPimRef() == ref_type


class TestServiceNeeds:
    def test_abstract_initialization(self):
        """Test that ServiceNeeds cannot be instantiated directly"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        with pytest.raises(TypeError):
            ServiceNeeds(ar_root, "TestServiceNeeds")


class TestRamBlockStatusControlEnum:
    def test_initialization(self):
        """Test RamBlockStatusControlEnum initialization"""
        enum = RamBlockStatusControlEnum()

        # Enum values are stored in enumValues attribute as a tuple
        assert enum.enumValues == ("api", "nvRamManager")

    def test_values(self):
        """Test enum values"""
        assert RamBlockStatusControlEnum.API == "api"
        assert RamBlockStatusControlEnum.NV_RAM_MANAGER == "nvRamManager"


class TestServiceProviderEnum:
    def test_initialization(self):
        """Test ServiceProviderEnum initialization matches the spec Literal rows in order"""
        enum = ServiceProviderEnum()
        assert enum.enumValues == (
            "anyStandardized",
            "basicSoftwareModeManager",
            "comManager",
            "cryptoKeyManagement",
            "cryptoServiceManager",
            "defaultErrorTracer",
            "diagnosticCommunicationManager",
            "diagnosticEventManager",
            "diagnosticLogAndTrace",
            "ecuManager",
            "errorTracer",
            "functionInhibitionManager",
            "hardwareTestManager",
            "intrusionDetectionSecurityManagement",
            "j1939Dcm",
            "j1939RequestManager",
            "nonVolatileRamManager",
            "operatingSystem",
            "secureOnBoardCommunication",
            "syncBaseTimeManager",
            "v2xFacilities",
            "v2xManagement",
            "vendorSpecific",
        )

    def test_values(self):
        """Test enum member values match the spec literals"""
        assert ServiceProviderEnum.ANY_STANDARDIZED == "anyStandardized"
        assert ServiceProviderEnum.BASIC_SOFTWARE_MODE_MANAGER == "basicSoftwareModeManager"
        assert ServiceProviderEnum.COM_MANAGER == "comManager"
        assert ServiceProviderEnum.CRYPTO_KEY_MANAGEMENT == "cryptoKeyManagement"
        assert ServiceProviderEnum.CRYPTO_SERVICE_MANAGER == "cryptoServiceManager"
        assert ServiceProviderEnum.DEFAULT_ERROR_TRACER == "defaultErrorTracer"
        assert ServiceProviderEnum.DIAGNOSTIC_COMMUNICATION_MANAGER == "diagnosticCommunicationManager"
        assert ServiceProviderEnum.DIAGNOSTIC_EVENT_MANAGER == "diagnosticEventManager"
        assert ServiceProviderEnum.DIAGNOSTIC_LOG_AND_TRACE == "diagnosticLogAndTrace"
        assert ServiceProviderEnum.ECU_MANAGER == "ecuManager"
        assert ServiceProviderEnum.ERROR_TRACER == "errorTracer"
        assert ServiceProviderEnum.FUNCTION_INHIBITION_MANAGER == "functionInhibitionManager"
        assert ServiceProviderEnum.HARDWARE_TEST_MANAGER == "hardwareTestManager"
        assert ServiceProviderEnum.INTRUSION_DETECTION_SECURITY_MANAGEMENT == "intrusionDetectionSecurityManagement"
        assert ServiceProviderEnum.J1939_DCM == "j1939Dcm"
        assert ServiceProviderEnum.J1939_REQUEST_MANAGER == "j1939RequestManager"
        assert ServiceProviderEnum.NON_VOLATILE_RAM_MANAGER == "nonVolatileRamManager"
        assert ServiceProviderEnum.OPERATING_SYSTEM == "operatingSystem"
        assert ServiceProviderEnum.SECURE_ON_BOARD_COMMUNICATION == "secureOnBoardCommunication"
        assert ServiceProviderEnum.SYNC_BASE_TIME_MANAGER == "syncBaseTimeManager"
        assert ServiceProviderEnum.V2X_FACILITIES == "v2xFacilities"
        assert ServiceProviderEnum.V2X_MANAGEMENT == "v2xManagement"
        assert ServiceProviderEnum.VENDOR_SPECIFIC == "vendorSpecific"

    def test_instantiation(self):
        """Test ServiceProviderEnum is instantiable and settable"""
        enum = ServiceProviderEnum().setValue(ServiceProviderEnum.COM_MANAGER)
        assert enum.getValue() == "comManager"


class TestNvBlockNeedsReliabilityEnum:
    def test_initialization(self):
        """Test NvBlockNeedsReliabilityEnum initialization"""
        enum = NvBlockNeedsReliabilityEnum()

        assert enum.enumValues == ("errorCorrection", "errorDetection", "noProtection")

    def test_values(self):
        """Test enum values"""
        assert NvBlockNeedsReliabilityEnum.ERROR_CORRECTION == "errorCorrection"
        assert NvBlockNeedsReliabilityEnum.ERROR_DETECTION == "errorDetection"
        assert NvBlockNeedsReliabilityEnum.NO_PROTECTION == "noProtection"


class TestNvBlockNeedsWritingPriorityEnum:
    def test_initialization(self):
        """Test NvBlockNeedsWritingPriorityEnum initialization"""
        enum = NvBlockNeedsWritingPriorityEnum()

        assert enum.enumValues == ("high", "low", "medium")

    def test_values(self):
        """Test enum values"""
        assert NvBlockNeedsWritingPriorityEnum.HIGH == "high"
        assert NvBlockNeedsWritingPriorityEnum.LOW == "low"
        assert NvBlockNeedsWritingPriorityEnum.MEDIUM == "medium"


class TestNvBlockNeeds:
    def test_initialization(self):
        """Test NvBlockNeeds initialization"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        nv_block = NvBlockNeeds(ar_root, "TestNvBlock")

        assert nv_block is not None
        assert nv_block.getShortName() == "TestNvBlock"
        assert nv_block.calcRamBlockCrc is None
        assert nv_block.checkStaticBlockId is None
        assert nv_block.cyclicWritingPeriod is None
        assert nv_block.nDataSets is None
        assert nv_block.nRomBlocks is None
        assert nv_block.ramBlockStatusControl is None
        assert nv_block.readonly is None
        assert nv_block.reliability is None
        assert nv_block.resistantToChangedSw is None
        assert nv_block.restoreAtStart is None
        assert nv_block.selectBlockForFirstInitAll is None
        assert nv_block.storeAtShutdown is None
        assert nv_block.storeCyclic is None
        assert nv_block.storeEmergency is None
        assert nv_block.storeImmediate is None
        assert nv_block.storeOnChange is None
        assert nv_block.useAutoValidationAtShutDown is None
        assert nv_block.useCRCCompMechanism is None
        assert nv_block.writeOnlyOnce is None
        assert nv_block.writeVerification is None
        assert nv_block.writingFrequency is None
        assert nv_block.writingPriority is None

    def test_get_set_calc_ram_block_crc(self):
        """Test getCalcRamBlockCrc and setCalcRamBlockCrc methods"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        nv_block = NvBlockNeeds(ar_root, "TestNvBlock")

        assert nv_block.getCalcRamBlockCrc() is None

        nv_block.setCalcRamBlockCrc(True)
        assert nv_block.getCalcRamBlockCrc() is True

    def test_get_set_check_static_block_id(self):
        """Test getCheckStaticBlockId and setCheckStaticBlockId methods"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        nv_block = NvBlockNeeds(ar_root, "TestNvBlock")

        assert nv_block.getCheckStaticBlockId() is None

        nv_block.setCheckStaticBlockId(True)
        assert nv_block.getCheckStaticBlockId() is True

    def test_get_set_cyclic_writing_period(self):
        """Test getCyclicWritingPeriod and setCyclicWritingPeriod methods"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        nv_block = NvBlockNeeds(ar_root, "TestNvBlock")

        assert nv_block.getCyclicWritingPeriod() is None

        class MockTimeValue:
            pass

        time_value = MockTimeValue()
        nv_block.setCyclicWritingPeriod(time_value)
        assert nv_block.getCyclicWritingPeriod() == time_value

    def test_get_set_n_data_sets(self):
        """Test getNDataSets and setNDataSets methods"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        nv_block = NvBlockNeeds(ar_root, "TestNvBlock")

        assert nv_block.getNDataSets() is None

        nv_block.setNDataSets(5)
        assert nv_block.getNDataSets() == 5

    def test_get_set_n_rom_blocks(self):
        """Test getNRomBlocks and setNRomBlocks methods"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        nv_block = NvBlockNeeds(ar_root, "TestNvBlock")

        assert nv_block.getNRomBlocks() is None

        nv_block.setNRomBlocks(3)
        assert nv_block.getNRomBlocks() == 3

    def test_get_set_ram_block_status_control(self):
        """Test getRamBlockStatusControl and setRamBlockStatusControl methods"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        nv_block = NvBlockNeeds(ar_root, "TestNvBlock")

        assert nv_block.getRamBlockStatusControl() is None

        enum_val = RamBlockStatusControlEnum.NV_RAM_MANAGER
        nv_block.setRamBlockStatusControl(enum_val)
        assert nv_block.getRamBlockStatusControl() == enum_val

    def test_get_set_readonly(self):
        """Test getReadonly and setReadonly methods"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        nv_block = NvBlockNeeds(ar_root, "TestNvBlock")

        assert nv_block.getReadonly() is None

        nv_block.setReadonly(True)
        assert nv_block.getReadonly() is True

    def test_get_set_reliability(self):
        """Test getReliability and setReliability methods"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        nv_block = NvBlockNeeds(ar_root, "TestNvBlock")

        assert nv_block.getReliability() is None

        enum_val = NvBlockNeedsReliabilityEnum.ERROR_DETECTION
        nv_block.setReliability(enum_val)
        assert nv_block.getReliability() == enum_val

    def test_get_set_resistant_to_changed_sw(self):
        """Test getResistantToChangedSw and setResistantToChangedSw methods"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        nv_block = NvBlockNeeds(ar_root, "TestNvBlock")

        assert nv_block.getResistantToChangedSw() is None

        nv_block.setResistantToChangedSw(True)
        assert nv_block.getResistantToChangedSw() is True

    def test_get_set_restore_at_start(self):
        """Test getRestoreAtStart and setRestoreAtStart methods"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        nv_block = NvBlockNeeds(ar_root, "TestNvBlock")

        assert nv_block.getRestoreAtStart() is None

        nv_block.setRestoreAtStart(True)
        assert nv_block.getRestoreAtStart() is True

    def test_get_set_select_block_for_first_init_all(self):
        """Test getSelectBlockForFirstInitAll and setSelectBlockForFirstInitAll methods"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        nv_block = NvBlockNeeds(ar_root, "TestNvBlock")

        assert nv_block.getSelectBlockForFirstInitAll() is None

        nv_block.setSelectBlockForFirstInitAll(True)
        assert nv_block.getSelectBlockForFirstInitAll() is True

    def test_get_set_store_at_shutdown(self):
        """Test getStoreAtShutdown and setStoreAtShutdown methods"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        nv_block = NvBlockNeeds(ar_root, "TestNvBlock")

        assert nv_block.getStoreAtShutdown() is None

        nv_block.setStoreAtShutdown(True)
        assert nv_block.getStoreAtShutdown() is True

    def test_get_set_store_cyclic(self):
        """Test getStoreCyclic and setStoreCyclic methods"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        nv_block = NvBlockNeeds(ar_root, "TestNvBlock")

        assert nv_block.getStoreCyclic() is None

        nv_block.setStoreCyclic(True)
        assert nv_block.getStoreCyclic() is True

    def test_get_set_store_emergency(self):
        """Test getStoreEmergency and setStoreEmergency methods"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        nv_block = NvBlockNeeds(ar_root, "TestNvBlock")

        assert nv_block.getStoreEmergency() is None

        nv_block.setStoreEmergency(True)
        assert nv_block.getStoreEmergency() is True

    def test_get_set_store_immediate(self):
        """Test getStoreImmediate and setStoreImmediate methods"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        nv_block = NvBlockNeeds(ar_root, "TestNvBlock")

        assert nv_block.getStoreImmediate() is None

        nv_block.setStoreImmediate(True)
        assert nv_block.getStoreImmediate() is True

    def test_get_set_store_on_change(self):
        """Test getStoreOnChange and setStoreOnChange methods"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        nv_block = NvBlockNeeds(ar_root, "TestNvBlock")

        assert nv_block.getStoreOnChange() is None

        nv_block.setStoreOnChange(True)
        assert nv_block.getStoreOnChange() is True

    def test_get_set_use_auto_validation_at_shut_down(self):
        """Test getUseAutoValidationAtShutDown and setUseAutoValidationAtShutDown methods"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        nv_block = NvBlockNeeds(ar_root, "TestNvBlock")

        assert nv_block.getUseAutoValidationAtShutDown() is None

        nv_block.setUseAutoValidationAtShutDown(True)
        assert nv_block.getUseAutoValidationAtShutDown() is True

    def test_get_set_use_crc_comp_mechanism(self):
        """Test getUseCRCCompMechanism and setUseCRCCompMechanism methods"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        nv_block = NvBlockNeeds(ar_root, "TestNvBlock")

        assert nv_block.getUseCRCCompMechanism() is None

        nv_block.setUseCRCCompMechanism(True)
        assert nv_block.getUseCRCCompMechanism() is True

    def test_get_set_write_only_once(self):
        """Test getWriteOnlyOnce and setWriteOnlyOnce methods"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        nv_block = NvBlockNeeds(ar_root, "TestNvBlock")

        assert nv_block.getWriteOnlyOnce() is None

        nv_block.setWriteOnlyOnce(True)
        assert nv_block.getWriteOnlyOnce() is True

    def test_get_set_write_verification(self):
        """Test getWriteVerification and setWriteVerification methods"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        nv_block = NvBlockNeeds(ar_root, "TestNvBlock")

        assert nv_block.getWriteVerification() is None

        nv_block.setWriteVerification(True)
        assert nv_block.getWriteVerification() is True

    def test_get_set_writing_frequency(self):
        """Test getWritingFrequency and setWritingFrequency methods"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        nv_block = NvBlockNeeds(ar_root, "TestNvBlock")

        assert nv_block.getWritingFrequency() is None

        nv_block.setWritingFrequency(10)
        assert nv_block.getWritingFrequency() == 10

    def test_get_set_writing_priority(self):
        """Test getWritingPriority and setWritingPriority methods"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        nv_block = NvBlockNeeds(ar_root, "TestNvBlock")

        assert nv_block.getWritingPriority() is None

        enum_val = NvBlockNeedsWritingPriorityEnum.HIGH
        nv_block.setWritingPriority(enum_val)
        assert nv_block.getWritingPriority() == enum_val


class TestRoleBasedDataTypeAssignment:
    def test_initialization(self):
        """Test RoleBasedDataTypeAssignment initialization"""
        assignment = RoleBasedDataTypeAssignment()

        assert assignment is not None
        assert assignment.role is None
        assert assignment.usedImplementationDataTypeRef is None

    def test_get_set_role(self):
        """Test getRole and setRole methods"""
        assignment = RoleBasedDataTypeAssignment()

        assert assignment.getRole() is None

        result = assignment.setRole("TestRole")
        assert result is assignment  # Method chaining
        assert assignment.getRole() == "TestRole"

        # None is a no-op
        assignment.setRole(None)
        assert assignment.getRole() == "TestRole"

    def test_get_set_used_implementation_data_type_ref(self):
        """Test getUsedImplementationDataTypeRef and setUsedImplementationDataTypeRef methods"""
        assignment = RoleBasedDataTypeAssignment()

        assert assignment.getUsedImplementationDataTypeRef() is None

        ref_type = RefType().setValue("/AutosarTypes/ImplDataType")
        result = assignment.setUsedImplementationDataTypeRef(ref_type)
        assert result is assignment  # Method chaining
        assert assignment.getUsedImplementationDataTypeRef() == ref_type

        # None is a no-op
        assignment.setUsedImplementationDataTypeRef(None)
        assert assignment.getUsedImplementationDataTypeRef() == ref_type


class TestServiceDiagnosticRelevanceEnum:
    def test_initialization(self):
        """Test ServiceDiagnosticRelevanceEnum initialization"""
        enum = ServiceDiagnosticRelevanceEnum()

        assert enum.enumValues == []


class TestServiceDependency:
    def test_abstract_class_cannot_be_instantiated(self):
        """Test that ServiceDependency abstract class cannot be instantiated directly"""
        with pytest.raises(TypeError, match="ServiceDependency is an abstract class"):
            ServiceDependency()

    def test_concrete_subclass_initialization(self):
        """Test that a concrete subclass of ServiceDependency can be instantiated"""
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ServiceMapping import SwcServiceDependency

        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        service_dep = SwcServiceDependency(ar_root, "TestServiceDependency")

        assert service_dep is not None
        assert service_dep.getShortName() == "TestServiceDependency"
        assert service_dep.assignedDataTypes == []
        assert service_dep.diagnosticRelevance is None
        assert service_dep.symbolicNameProps is None

    def test_get_assigned_data_types(self):
        """Test getAssignedDataTypes method"""
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ServiceMapping import SwcServiceDependency

        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        service_dep = SwcServiceDependency(ar_root, "TestServiceDependency")

        assert service_dep.getAssignedDataTypes() == []

    def test_add_assigned_data_type(self):
        """Test addAssignedDataType method"""
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ServiceMapping import SwcServiceDependency

        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        service_dep = SwcServiceDependency(ar_root, "TestServiceDependency")

        class MockDataTypeAssignment:
            pass

        data_type = MockDataTypeAssignment()

        result = service_dep.addAssignedDataType(data_type)
        assert result is service_dep
        assert service_dep.getAssignedDataTypes() == [data_type]

    def test_get_set_diagnostic_relevance(self):
        """Test getDiagnosticRelevance and setDiagnosticRelevance methods"""
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ServiceMapping import SwcServiceDependency

        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        service_dep = SwcServiceDependency(ar_root, "TestServiceDependency")

        assert service_dep.getDiagnosticRelevance() is None

        enum_val = ServiceDiagnosticRelevanceEnum()
        result = service_dep.setDiagnosticRelevance(enum_val)
        assert result is service_dep
        assert service_dep.getDiagnosticRelevance() == enum_val

    def test_get_set_symbolic_name_props(self):
        """Test getSymbolicNameProps and setSymbolicNameProps methods"""
        parent = AUTOSAR.getInstance()
        _ar_root = parent.createARPackage("AUTOSAR")

        # Create a concrete subclass for testing since ServiceDependency is abstract
        class ConcreteServiceDependency(ServiceDependency):
            def __init__(self):
                super().__init__()

        service_dep = ConcreteServiceDependency()

        assert service_dep.getSymbolicNameProps() is None

        class MockSymbolicNameProps:
            pass

        props = MockSymbolicNameProps()
        result = service_dep.setSymbolicNameProps(props)
        assert result is service_dep
        assert service_dep.getSymbolicNameProps() == props


class TestDiagnosticAudienceEnum:
    def test_initialization(self):
        """Test DiagnosticAudienceEnum initialization"""
        enum = DiagnosticAudienceEnum()

        assert enum.enumValues == ("aftermarket", "afterSales", "development", "manufacturing", "supplier")

    def test_values(self):
        """Test enum values"""
        assert DiagnosticAudienceEnum.AFTER_MARKET == "aftermarket"
        assert DiagnosticAudienceEnum.AFTER_SALES == "afterSales"
        assert DiagnosticAudienceEnum.DEVELOPMENT == "development"
        assert DiagnosticAudienceEnum.MANUFACTURING == "manufacturing"
        assert DiagnosticAudienceEnum.SUPPLIER == "supplier"


class TestDiagnosticServiceRequestCallbackTypeEnum:
    def test_initialization(self):
        """Test DiagnosticServiceRequestCallbackTypeEnum initialization"""
        enum = DiagnosticServiceRequestCallbackTypeEnum()

        assert enum.enumValues == ("requestCallbackTypeManufacturer", "requestCallbackTypeSupplier")

    def test_values(self):
        """Test enum values"""
        assert DiagnosticServiceRequestCallbackTypeEnum.REQUEST_CALLBACK_TYPE_MANUFACTURER == "requestCallbackTypeManufacturer"
        assert DiagnosticServiceRequestCallbackTypeEnum.REQUEST_CALLBACK_TYPE_SUPPLIER == "requestCallbackTypeSupplier"


class TestDiagnosticCapabilityElement:
    def test_abstract_initialization(self):
        """Test that DiagnosticCapabilityElement cannot be instantiated directly"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        with pytest.raises(TypeError):
            DiagnosticCapabilityElement(ar_root, "TestDiagnosticCapabilityElement")


class TestDiagnosticRoutineTypeEnum:
    def test_initialization(self):
        """Test DiagnosticRoutineTypeEnum initialization"""
        enum = DiagnosticRoutineTypeEnum()

        assert enum.enumValues == ("asynchronous", "synchronous")

    def test_values(self):
        """Test enum values"""
        assert DiagnosticRoutineTypeEnum.ASYNCHRONOUS == "asynchronous"
        assert DiagnosticRoutineTypeEnum.SYNCHRONOUS == "synchronous"


class TestDiagnosticCommunicationManagerNeeds:
    def test_initialization(self):
        """Test DiagnosticCommunicationManagerNeeds initialization"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        diag_comm = DiagnosticCommunicationManagerNeeds(ar_root, "TestDiagnosticCommunicationManagerNeeds")

        assert diag_comm is not None
        assert diag_comm.getShortName() == "TestDiagnosticCommunicationManagerNeeds"
        assert diag_comm.audiences == []
        assert diag_comm.diagRequirement is None
        assert diag_comm.securityAccessLevel is None
        assert diag_comm.serviceRequestCallbackType is None

    def test_get_set_service_request_callback_type(self):
        """Test getServiceRequestCallbackType and setServiceRequestCallbackType methods"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        diag_comm = DiagnosticCommunicationManagerNeeds(ar_root, "TestDiagnosticCommunicationManagerNeeds")

        assert diag_comm.getServiceRequestCallbackType() is None

        enum_val = DiagnosticServiceRequestCallbackTypeEnum.REQUEST_CALLBACK_TYPE_MANUFACTURER
        result = diag_comm.setServiceRequestCallbackType(enum_val)
        assert result is diag_comm
        assert diag_comm.getServiceRequestCallbackType() == enum_val

    def test_get_set_audiences(self):
        """Test getAudiences and addAudience methods"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        diag_comm = DiagnosticCommunicationManagerNeeds(ar_root, "TestDiagnosticCommunicationManagerNeeds")

        assert diag_comm.getAudiences() == []

        enum_val = DiagnosticAudienceEnum.DEVELOPMENT
        result = diag_comm.addAudience(enum_val)
        assert result is diag_comm
        assert diag_comm.getAudiences() == [enum_val]

    def test_get_set_diag_requirement(self):
        """Test getDiagRequirement and setDiagRequirement methods"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        diag_comm = DiagnosticCommunicationManagerNeeds(ar_root, "TestDiagnosticCommunicationManagerNeeds")

        assert diag_comm.getDiagRequirement() is None

        result = diag_comm.setDiagRequirement("REQ-001")
        assert result is diag_comm
        assert diag_comm.getDiagRequirement() == "REQ-001"

    def test_get_set_security_access_level(self):
        """Test getSecurityAccessLevel and setSecurityAccessLevel methods"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        diag_comm = DiagnosticCommunicationManagerNeeds(ar_root, "TestDiagnosticCommunicationManagerNeeds")

        assert diag_comm.getSecurityAccessLevel() is None

        result = diag_comm.setSecurityAccessLevel(2)
        assert result is diag_comm
        assert diag_comm.getSecurityAccessLevel() == 2


class TestDiagnosticRoutineNeeds:
    def test_initialization(self):
        """Test DiagnosticRoutineNeeds initialization"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        diag_routine = DiagnosticRoutineNeeds(ar_root, "TestDiagnosticRoutineNeeds")

        assert diag_routine is not None
        assert diag_routine.getShortName() == "TestDiagnosticRoutineNeeds"
        assert diag_routine.audiences == []
        assert diag_routine.diagRequirement is None
        assert diag_routine.securityAccessLevel is None
        assert diag_routine.diagRoutineType is None
        assert diag_routine.RidNumber is None

    def test_get_set_diag_routine_type(self):
        """Test getDiagRoutineType and setDiagRoutineType methods"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        diag_routine = DiagnosticRoutineNeeds(ar_root, "TestDiagnosticRoutineNeeds")

        assert diag_routine.getDiagRoutineType() is None

        enum_val = DiagnosticRoutineTypeEnum.ASYNCHRONOUS
        result = diag_routine.setDiagRoutineType(enum_val)
        assert result is diag_routine
        assert diag_routine.getDiagRoutineType() == enum_val

    def test_get_set_rid_number(self):
        """Test getRidNumber and setRidNumber methods"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        diag_routine = DiagnosticRoutineNeeds(ar_root, "TestDiagnosticRoutineNeeds")

        assert diag_routine.getRidNumber() is None

        result = diag_routine.setRidNumber(1234)
        assert result is diag_routine
        assert diag_routine.getRidNumber() == 1234

    def test_get_set_audiences(self):
        """Test getAudiences and addAudience methods"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        diag_routine = DiagnosticRoutineNeeds(ar_root, "TestDiagnosticRoutineNeeds")

        assert diag_routine.getAudiences() == []

        enum_val = DiagnosticAudienceEnum.AFTER_MARKET
        result = diag_routine.addAudience(enum_val)
        assert result is diag_routine
        assert diag_routine.getAudiences() == [enum_val]

    def test_get_set_diag_requirement(self):
        """Test getDiagRequirement and setDiagRequirement methods"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        diag_routine = DiagnosticRoutineNeeds(ar_root, "TestDiagnosticRoutineNeeds")

        assert diag_routine.getDiagRequirement() is None

        result = diag_routine.setDiagRequirement("REQ-002")
        assert result is diag_routine
        assert diag_routine.getDiagRequirement() == "REQ-002"

    def test_get_set_security_access_level(self):
        """Test getSecurityAccessLevel and setSecurityAccessLevel methods"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        diag_routine = DiagnosticRoutineNeeds(ar_root, "TestDiagnosticRoutineNeeds")

        assert diag_routine.getSecurityAccessLevel() is None

        result = diag_routine.setSecurityAccessLevel(3)
        assert result is diag_routine
        assert diag_routine.getSecurityAccessLevel() == 3


class TestDiagnosticValueAccessEnum:
    def test_initialization(self):
        """Test DiagnosticValueAccessEnum initialization"""
        enum = DiagnosticValueAccessEnum()

        assert enum.enumValues == ("readOnly", "readWrite", "writeOnly")

    def test_values(self):
        """Test enum values"""
        assert DiagnosticValueAccessEnum.READ_ONLY == "readOnly"
        assert DiagnosticValueAccessEnum.READ_WRITE == "readWrite"
        assert DiagnosticValueAccessEnum.WRITE_ONLY == "writeOnly"


class TestDiagnosticProcessingStyleEnum:
    def test_initialization(self):
        """Test DiagnosticProcessingStyleEnum initialization"""
        enum = DiagnosticProcessingStyleEnum()

        assert enum.enumValues == ("processingStyleAsynchronous", "processingStyleAsynchronousWithError", "processingStyleSynchronous")

    def test_values(self):
        """Test enum values"""
        assert DiagnosticProcessingStyleEnum.PROCESSING_STYLE_ASYNCHRONOUS == "processingStyleAsynchronous"
        assert DiagnosticProcessingStyleEnum.PROCESSING_STYLE_ASYNCHRONOUS_WITH_ERROR == "processingStyleAsynchronousWithError"
        assert DiagnosticProcessingStyleEnum.PROCESSING_STYLE_SYNCHRONOUS == "processingStyleSynchronous"


class TestDiagnosticValueNeeds:
    def test_initialization(self):
        """Test DiagnosticValueNeeds initialization"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        diag_value = DiagnosticValueNeeds(ar_root, "TestDiagnosticValueNeeds")

        assert diag_value is not None
        assert diag_value.getShortName() == "TestDiagnosticValueNeeds"
        assert diag_value.audiences == []
        assert diag_value.diagRequirement is None
        assert diag_value.securityAccessLevel is None
        assert diag_value.dataLength is None
        assert diag_value.diagnosticValueAccess is None
        assert diag_value.DidNumber is None
        assert diag_value.fixedLength is None
        assert diag_value.processingStyle is None

    def test_get_set_data_length(self):
        """Test getDataLength and setDataLength methods"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        diag_value = DiagnosticValueNeeds(ar_root, "TestDiagnosticValueNeeds")

        assert diag_value.getDataLength() is None

        result = diag_value.setDataLength(256)
        assert result is diag_value
        assert diag_value.getDataLength() == 256

    def test_get_set_diagnostic_value_access(self):
        """Test getDiagnosticValueAccess and setDiagnosticValueAccess methods"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        diag_value = DiagnosticValueNeeds(ar_root, "TestDiagnosticValueNeeds")

        assert diag_value.getDiagnosticValueAccess() is None

        enum_val = DiagnosticValueAccessEnum.READ_WRITE
        result = diag_value.setDiagnosticValueAccess(enum_val)
        assert result is diag_value
        assert diag_value.getDiagnosticValueAccess() == enum_val

    def test_get_set_did_number(self):
        """Test getDidNumber and setDidNumber methods"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        diag_value = DiagnosticValueNeeds(ar_root, "TestDiagnosticValueNeeds")

        assert diag_value.getDidNumber() is None

        result = diag_value.setDidNumber(12345)
        assert result is diag_value
        assert diag_value.getDidNumber() == 12345

    def test_get_set_fixed_length(self):
        """Test getFixedLength and setFixedLength methods"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        diag_value = DiagnosticValueNeeds(ar_root, "TestDiagnosticValueNeeds")

        assert diag_value.getFixedLength() is None

        result = diag_value.setFixedLength(True)
        assert result is diag_value
        assert diag_value.getFixedLength() is True

    def test_get_set_processing_style(self):
        """Test getProcessingStyle and setProcessingStyle methods"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        diag_value = DiagnosticValueNeeds(ar_root, "TestDiagnosticValueNeeds")

        assert diag_value.getProcessingStyle() is None

        enum_val = DiagnosticProcessingStyleEnum.PROCESSING_STYLE_SYNCHRONOUS
        result = diag_value.setProcessingStyle(enum_val)
        assert result is diag_value
        assert diag_value.getProcessingStyle() == enum_val

    def test_get_set_audiences(self):
        """Test getAudiences and addAudience methods"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        diag_value = DiagnosticValueNeeds(ar_root, "TestDiagnosticValueNeeds")

        assert diag_value.getAudiences() == []

        enum_val = DiagnosticAudienceEnum.SUPPLIER
        result = diag_value.addAudience(enum_val)
        assert result is diag_value
        assert diag_value.getAudiences() == [enum_val]

    def test_get_set_diag_requirement(self):
        """Test getDiagRequirement and setDiagRequirement methods"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        diag_value = DiagnosticValueNeeds(ar_root, "TestDiagnosticValueNeeds")

        assert diag_value.getDiagRequirement() is None

        result = diag_value.setDiagRequirement("REQ-003")
        assert result is diag_value
        assert diag_value.getDiagRequirement() == "REQ-003"

    def test_get_set_security_access_level(self):
        """Test getSecurityAccessLevel and setSecurityAccessLevel methods"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        diag_value = DiagnosticValueNeeds(ar_root, "TestDiagnosticValueNeeds")

        assert diag_value.getSecurityAccessLevel() is None

        result = diag_value.setSecurityAccessLevel(4)
        assert result is diag_value
        assert diag_value.getSecurityAccessLevel() == 4


class TestDiagnosticIoControlNeeds:
    def test_initialization(self):
        """Test DiagnosticIoControlNeeds initialization"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        needs = DiagnosticIoControlNeeds(ar_root, "TestDiagnosticIoControlNeeds")

        assert needs is not None
        assert needs.getShortName() == "TestDiagnosticIoControlNeeds"
        assert needs.audiences == []
        assert needs.diagRequirement is None
        assert needs.securityAccessLevel is None
        assert needs.currentValueRef is None
        assert needs.freezeCurrentStateSupported is None
        assert needs.resetToDefaultSupported is None
        assert needs.shortTermAdjustmentSupported is None

    def test_get_set_current_value_ref(self):
        """Test getCurrentValueRef/setCurrentValueRef (chaining, round-trip, None no-op)"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        needs = DiagnosticIoControlNeeds(ar_root, "TestDiagnosticIoControlNeeds")

        value = RefType().setValue("/Needs/CurrentValue")
        result = needs.setCurrentValueRef(value)
        assert result is needs  # Method chaining
        assert needs.getCurrentValueRef() == value

        needs.setCurrentValueRef(None)  # No-op
        assert needs.getCurrentValueRef() == value

    def test_get_set_freeze_current_state_supported(self):
        """Test getFreezeCurrentStateSupported/setFreezeCurrentStateSupported (chaining, round-trip, None no-op)"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        needs = DiagnosticIoControlNeeds(ar_root, "TestDiagnosticIoControlNeeds")

        value = Boolean().setValue(True)
        result = needs.setFreezeCurrentStateSupported(value)
        assert result is needs  # Method chaining
        assert needs.getFreezeCurrentStateSupported() == value

        needs.setFreezeCurrentStateSupported(None)  # No-op
        assert needs.getFreezeCurrentStateSupported() == value

    def test_get_set_reset_to_default_supported(self):
        """Test getResetToDefaultSupported/setResetToDefaultSupported (chaining, round-trip, None no-op)"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        needs = DiagnosticIoControlNeeds(ar_root, "TestDiagnosticIoControlNeeds")

        value = Boolean().setValue(False)
        result = needs.setResetToDefaultSupported(value)
        assert result is needs  # Method chaining
        assert needs.getResetToDefaultSupported() == value

        needs.setResetToDefaultSupported(None)  # No-op
        assert needs.getResetToDefaultSupported() == value

    def test_get_set_short_term_adjustment_supported(self):
        """Test getShortTermAdjustmentSupported/setShortTermAdjustmentSupported (chaining, round-trip, None no-op)"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        needs = DiagnosticIoControlNeeds(ar_root, "TestDiagnosticIoControlNeeds")

        value = Boolean().setValue(True)
        result = needs.setShortTermAdjustmentSupported(value)
        assert result is needs  # Method chaining
        assert needs.getShortTermAdjustmentSupported() == value

        needs.setShortTermAdjustmentSupported(None)  # No-op
        assert needs.getShortTermAdjustmentSupported() == value


class TestDiagnosticIoControlNeedsRoundTrip:
    def test_round_trip_attributes(self):
        """Test parse -> write -> re-parse preserves DiagnosticIoControlNeeds attributes."""
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        ar_root = document.createARPackage("AUTOSAR")
        desc = ar_root.createBswModuleDescription("BswMd")
        behavior = desc.createBswInternalBehavior("Beh")
        dependency = BswServiceDependency()
        needs = DiagnosticIoControlNeeds(dependency, "IoNeeds")
        needs.setCurrentValueRef(RefType().setValue("/Needs/Value"))
        needs.setFreezeCurrentStateSupported(Boolean().setValue(True))
        needs.setResetToDefaultSupported(Boolean().setValue(False))
        needs.setShortTermAdjustmentSupported(Boolean().setValue(True))
        dependency.setServiceNeeds(needs)
        behavior.addServiceDependency(dependency)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            behavior_2 = document_2.getARPackages()[0].getBswModuleDescriptions()[0].getInternalBehaviors()[0]
            needs_2 = behavior_2.getServiceDependencies()[0].getServiceNeeds()
            assert needs_2.getShortName() == "IoNeeds"
            assert needs_2.getCurrentValueRef().getValue() == "/Needs/Value"
            assert needs_2.getFreezeCurrentStateSupported().getValue() is True
            assert needs_2.getResetToDefaultSupported().getValue() is False
            assert needs_2.getShortTermAdjustmentSupported().getValue() is True
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)


class TestDiagEventDebounceAlgorithm:
    def test_abstract_initialization(self):
        """Test that DiagEventDebounceAlgorithm cannot be instantiated directly"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        with pytest.raises(TypeError):
            DiagEventDebounceAlgorithm(ar_root, "TestDiagEventDebounceAlgorithm")


class TestDiagEventDebounceCounterBased:
    def test_initialization(self):
        """Test DiagEventDebounceCounterBased initialization"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        debounce = DiagEventDebounceCounterBased(ar_root, "TestDiagEventDebounceCounterBased")

        assert debounce is not None
        assert debounce.getShortName() == "TestDiagEventDebounceCounterBased"
        assert debounce.counterBasedFdcThresholdStorageValue is None
        assert debounce.counterDecrementStepSize is None
        assert debounce.counterFailedThreshold is None
        assert debounce.counterIncrementStepSize is None
        assert debounce.counterJumpDown is None
        assert debounce.counterJumpDownValue is None
        assert debounce.counterJumpUp is None
        assert debounce.counterJumpUpValue is None
        assert debounce.counterPassedThreshold is None

    def test_get_set_counter_based_fdc_threshold_storage_value(self):
        """Test getCounterBasedFdcThresholdStorageValue and setCounterBasedFdcThresholdStorageValue methods"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        debounce = DiagEventDebounceCounterBased(ar_root, "TestDiagEventDebounceCounterBased")

        assert debounce.getCounterBasedFdcThresholdStorageValue() is None

        result = debounce.setCounterBasedFdcThresholdStorageValue(100)
        assert result is debounce
        assert debounce.getCounterBasedFdcThresholdStorageValue() == 100

    def test_get_set_counter_decrement_step_size(self):
        """Test getCounterDecrementStepSize and setCounterDecrementStepSize methods"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        debounce = DiagEventDebounceCounterBased(ar_root, "TestDiagEventDebounceCounterBased")

        assert debounce.getCounterDecrementStepSize() is None

        result = debounce.setCounterDecrementStepSize(5)
        assert result is debounce
        assert debounce.getCounterDecrementStepSize() == 5

    def test_get_set_counter_failed_threshold(self):
        """Test getCounterFailedThreshold and setCounterFailedThreshold methods"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        debounce = DiagEventDebounceCounterBased(ar_root, "TestDiagEventDebounceCounterBased")

        assert debounce.getCounterFailedThreshold() is None

        result = debounce.setCounterFailedThreshold(200)
        assert result is debounce
        assert debounce.getCounterFailedThreshold() == 200

    def test_get_set_counter_increment_step_size(self):
        """Test getCounterIncrementStepSize and setCounterIncrementStepSize methods"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        debounce = DiagEventDebounceCounterBased(ar_root, "TestDiagEventDebounceCounterBased")

        assert debounce.getCounterIncrementStepSize() is None

        result = debounce.setCounterIncrementStepSize(3)
        assert result is debounce
        assert debounce.getCounterIncrementStepSize() == 3

    def test_get_set_counter_jump_down(self):
        """Test getCounterJumpDown and setCounterJumpDown methods"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        debounce = DiagEventDebounceCounterBased(ar_root, "TestDiagEventDebounceCounterBased")

        assert debounce.getCounterJumpDown() is None

        result = debounce.setCounterJumpDown(150)
        assert result is debounce
        assert debounce.getCounterJumpDown() == 150

    def test_get_set_counter_jump_down_value(self):
        """Test getCounterJumpDownValue and setCounterJumpDownValue methods"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        debounce = DiagEventDebounceCounterBased(ar_root, "TestDiagEventDebounceCounterBased")

        assert debounce.getCounterJumpDownValue() is None

        result = debounce.setCounterJumpDownValue(50)
        assert result is debounce
        assert debounce.getCounterJumpDownValue() == 50

    def test_get_set_counter_jump_up(self):
        """Test getCounterJumpUp and setCounterJumpUp methods"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        debounce = DiagEventDebounceCounterBased(ar_root, "TestDiagEventDebounceCounterBased")

        assert debounce.getCounterJumpUp() is None

        result = debounce.setCounterJumpUp(250)
        assert result is debounce
        assert debounce.getCounterJumpUp() == 250

    def test_get_set_counter_jump_up_value(self):
        """Test getCounterJumpUpValue and setCounterJumpUpValue methods"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        debounce = DiagEventDebounceCounterBased(ar_root, "TestDiagEventDebounceCounterBased")

        assert debounce.getCounterJumpUpValue() is None

        result = debounce.setCounterJumpUpValue(75)
        assert result is debounce
        assert debounce.getCounterJumpUpValue() == 75

    def test_get_set_counter_passed_threshold(self):
        """Test getCounterPassedThreshold and setCounterPassedThreshold methods"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        debounce = DiagEventDebounceCounterBased(ar_root, "TestDiagEventDebounceCounterBased")

        assert debounce.getCounterPassedThreshold() is None

        result = debounce.setCounterPassedThreshold(180)
        assert result is debounce
        assert debounce.getCounterPassedThreshold() == 180


class TestDiagEventDebounceMonitorInternal:
    def test_initialization(self):
        """Test DiagEventDebounceMonitorInternal initialization"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        debounce = DiagEventDebounceMonitorInternal(ar_root, "TestDiagEventDebounceMonitorInternal")

        assert debounce is not None
        assert debounce.getShortName() == "TestDiagEventDebounceMonitorInternal"


class TestDiagEventDebounceTimeBased:
    def test_initialization(self):
        """Test DiagEventDebounceTimeBased initialization"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        debounce = DiagEventDebounceTimeBased(ar_root, "TestDiagEventDebounceTimeBased")

        assert debounce is not None
        assert debounce.getShortName() == "TestDiagEventDebounceTimeBased"
        assert debounce.timeBasedFdcThresholdStorageValue is None
        assert debounce.timeFailedThreshold is None
        assert debounce.timePassedThreshold is None

    def test_get_set_time_based_fdc_threshold_storage_value(self):
        """Test getTimeBasedFdcThresholdStorageValue and setTimeBasedFdcThresholdStorageValue methods"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        debounce = DiagEventDebounceTimeBased(ar_root, "TestDiagEventDebounceTimeBased")

        assert debounce.getTimeBasedFdcThresholdStorageValue() is None

        class MockTimeValue:
            pass

        time_value = MockTimeValue()
        result = debounce.setTimeBasedFdcThresholdStorageValue(time_value)
        assert result is debounce
        assert debounce.getTimeBasedFdcThresholdStorageValue() == time_value

    def test_get_set_time_failed_threshold(self):
        """Test getTimeFailedThreshold and setTimeFailedThreshold methods"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        debounce = DiagEventDebounceTimeBased(ar_root, "TestDiagEventDebounceTimeBased")

        assert debounce.getTimeFailedThreshold() is None

        class MockTimeValue:
            pass

        time_value = MockTimeValue()
        result = debounce.setTimeFailedThreshold(time_value)
        assert result is debounce
        assert debounce.getTimeFailedThreshold() == time_value

    def test_get_set_time_passed_threshold(self):
        """Test getTimePassedThreshold and setTimePassedThreshold methods"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        debounce = DiagEventDebounceTimeBased(ar_root, "TestDiagEventDebounceTimeBased")

        assert debounce.getTimePassedThreshold() is None

        class MockTimeValue:
            pass

        time_value = MockTimeValue()
        result = debounce.setTimePassedThreshold(time_value)
        assert result is debounce
        assert debounce.getTimePassedThreshold() == time_value


class TestDtcKindEnum:
    def test_initialization(self):
        """Test DtcKindEnum initialization"""
        enum = DtcKindEnum()

        assert enum.enumValues == []


class TestDiagnosticEventInfoNeeds:
    def test_initialization(self):
        """Test DiagnosticEventInfoNeeds initialization"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        diag_event_info = DiagnosticEventInfoNeeds(ar_root, "TestDiagnosticEventInfoNeeds")

        assert diag_event_info is not None
        assert diag_event_info.getShortName() == "TestDiagnosticEventInfoNeeds"
        assert diag_event_info.audiences == []
        assert diag_event_info.diagRequirement is None
        assert diag_event_info.securityAccessLevel is None
        assert diag_event_info.dtcKind is None
        assert diag_event_info.obdDtcNumber is None
        assert diag_event_info.udsDtcNumber is None

    def test_get_set_dtc_kind(self):
        """Test getDtcKind and setDtcKind methods"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        diag_event_info = DiagnosticEventInfoNeeds(ar_root, "TestDiagnosticEventInfoNeeds")

        assert diag_event_info.getDtcKind() is None

        enum_val = DtcKindEnum()
        result = diag_event_info.setDtcKind(enum_val)
        assert result is diag_event_info
        assert diag_event_info.getDtcKind() == enum_val

    def test_get_set_obd_dtc_number(self):
        """Test getObdDtcNumber and setObdDtcNumber methods"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        diag_event_info = DiagnosticEventInfoNeeds(ar_root, "TestDiagnosticEventInfoNeeds")

        assert diag_event_info.getObdDtcNumber() is None

        result = diag_event_info.setObdDtcNumber(500)
        assert result is diag_event_info
        assert diag_event_info.getObdDtcNumber() == 500

    def test_get_set_uds_dtc_number(self):
        """Test getUdsDtcNumber and setUdsDtcNumber methods"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        diag_event_info = DiagnosticEventInfoNeeds(ar_root, "TestDiagnosticEventInfoNeeds")

        assert diag_event_info.getUdsDtcNumber() is None

        result = diag_event_info.setUdsDtcNumber(600)
        assert result is diag_event_info
        assert diag_event_info.getUdsDtcNumber() == 600

    def test_get_set_audiences(self):
        """Test getAudiences and addAudience methods"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        diag_event_info = DiagnosticEventInfoNeeds(ar_root, "TestDiagnosticEventInfoNeeds")

        assert diag_event_info.getAudiences() == []

        enum_val = DiagnosticAudienceEnum.MANUFACTURING
        result = diag_event_info.addAudience(enum_val)
        assert result is diag_event_info
        assert diag_event_info.getAudiences() == [enum_val]

    def test_get_set_diag_requirement(self):
        """Test getDiagRequirement and setDiagRequirement methods"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        diag_event_info = DiagnosticEventInfoNeeds(ar_root, "TestDiagnosticEventInfoNeeds")

        assert diag_event_info.getDiagRequirement() is None

        result = diag_event_info.setDiagRequirement("REQ-004")
        assert result is diag_event_info
        assert diag_event_info.getDiagRequirement() == "REQ-004"

    def test_get_set_security_access_level(self):
        """Test getSecurityAccessLevel and setSecurityAccessLevel methods"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        diag_event_info = DiagnosticEventInfoNeeds(ar_root, "TestDiagnosticEventInfoNeeds")

        assert diag_event_info.getSecurityAccessLevel() is None

        result = diag_event_info.setSecurityAccessLevel(5)
        assert result is diag_event_info
        assert diag_event_info.getSecurityAccessLevel() == 5


class TestDiagnosticClearDtcNotificationEnum:
    def test_initialization(self):
        """Test DiagnosticClearDtcNotificationEnum initialization"""
        enum = DiagnosticClearDtcNotificationEnum()

        assert enum.enumValues == []


class TestDtcFormatTypeEnum:
    def test_initialization(self):
        """Test DtcFormatTypeEnum initialization"""
        enum = DtcFormatTypeEnum()

        assert enum.enumValues == []


class TestDtcStatusChangeNotificationNeeds:
    def test_initialization(self):
        """Test DtcStatusChangeNotificationNeeds initialization"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        notification = DtcStatusChangeNotificationNeeds(ar_root, "TestDtcStatusChangeNotificationNeeds")

        assert notification is not None
        assert notification.getShortName() == "TestDtcStatusChangeNotificationNeeds"
        assert notification.audiences == []
        assert notification.diagRequirement is None
        assert notification.securityAccessLevel is None
        assert notification.dtcFormatType is None
        assert notification.notificationTime is None

    def test_get_set_dtc_format_type(self):
        """Test getDtcFormatType and setDtcFormatType methods"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        notification = DtcStatusChangeNotificationNeeds(ar_root, "TestDtcStatusChangeNotificationNeeds")

        assert notification.getDtcFormatType() is None

        enum_val = DtcFormatTypeEnum()
        result = notification.setDtcFormatType(enum_val)
        assert result is notification
        assert notification.getDtcFormatType() == enum_val

    def test_get_set_notification_time(self):
        """Test getNotificationTime and setNotificationTime methods"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        notification = DtcStatusChangeNotificationNeeds(ar_root, "TestDtcStatusChangeNotificationNeeds")

        assert notification.getNotificationTime() is None

        enum_val = DiagnosticClearDtcNotificationEnum()
        result = notification.setNotificationTime(enum_val)
        assert result is notification
        assert notification.getNotificationTime() == enum_val

    def test_get_set_audiences(self):
        """Test getAudiences and addAudience methods"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        notification = DtcStatusChangeNotificationNeeds(ar_root, "TestDtcStatusChangeNotificationNeeds")

        assert notification.getAudiences() == []

        enum_val = DiagnosticAudienceEnum.DEVELOPMENT
        result = notification.addAudience(enum_val)
        assert result is notification
        assert notification.getAudiences() == [enum_val]

    def test_get_set_diag_requirement(self):
        """Test getDiagRequirement and setDiagRequirement methods"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        notification = DtcStatusChangeNotificationNeeds(ar_root, "TestDtcStatusChangeNotificationNeeds")

        assert notification.getDiagRequirement() is None

        result = notification.setDiagRequirement("REQ-005")
        assert result is notification
        assert notification.getDiagRequirement() == "REQ-005"

    def test_get_set_security_access_level(self):
        """Test getSecurityAccessLevel and setSecurityAccessLevel methods"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        notification = DtcStatusChangeNotificationNeeds(ar_root, "TestDtcStatusChangeNotificationNeeds")

        assert notification.getSecurityAccessLevel() is None

        result = notification.setSecurityAccessLevel(6)
        assert result is notification
        assert notification.getSecurityAccessLevel() == 6


class TestDiagnosticEventNeeds:
    def test_initialization(self):
        """Test DiagnosticEventNeeds initialization"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        diag_event = DiagnosticEventNeeds(ar_root, "TestDiagnosticEventNeeds")

        assert diag_event is not None
        assert diag_event.getShortName() == "TestDiagnosticEventNeeds"
        assert diag_event.audiences == []
        assert diag_event.diagRequirement is None
        assert diag_event.securityAccessLevel is None
        assert diag_event.deferringFidRefs == []
        assert diag_event.diagEventDebounceAlgorithm is None
        assert diag_event.inhibitingFidRef is None
        assert diag_event.inhibitingSecondaryFidRefs == []
        assert diag_event.prestoredFreezeframeStoredInNvm is None
        assert diag_event.usesMonitorData is None

    def test_get_deferring_fid_refs(self):
        """Test getDeferringFidRefs and addDeferringFidRef methods"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        diag_event = DiagnosticEventNeeds(ar_root, "TestDiagnosticEventNeeds")

        assert diag_event.getDeferringFidRefs() == []

        class MockRefType:
            pass

        ref = MockRefType()
        result = diag_event.addDeferringFidRef(ref)
        assert result is diag_event
        assert diag_event.getDeferringFidRefs() == [ref]

        diag_event.addDeferringFidRef(None)
        assert diag_event.getDeferringFidRefs() == [ref]

    def test_get_set_diag_event_debounce_algorithm(self):
        """Test getDiagEventDebounceAlgorithm method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        diag_event = DiagnosticEventNeeds(ar_root, "TestDiagnosticEventNeeds")

        assert diag_event.getDiagEventDebounceAlgorithm() is None

    def test_create_diag_event_debounce_counter_based(self):
        """Test createDiagEventDebounceCounterBased method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        diag_event = DiagnosticEventNeeds(ar_root, "TestDiagnosticEventNeeds")

        debounce_algo = diag_event.createDiagEventDebounceCounterBased("CounterBasedAlgo")
        assert debounce_algo is not None
        assert isinstance(debounce_algo, DiagEventDebounceCounterBased)

    def test_create_diag_event_debounce_monitor_internal(self):
        """Test createDiagEventDebounceMonitorInternal method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        diag_event = DiagnosticEventNeeds(ar_root, "TestDiagnosticEventNeeds")

        debounce_algo = diag_event.createDiagEventDebounceMonitorInternal("MonitorInternalAlgo")
        assert debounce_algo is not None
        assert isinstance(debounce_algo, DiagEventDebounceMonitorInternal)

    def test_create_diag_event_debounce_time_based(self):
        """Test createDiagEventDebounceTimeBased method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        diag_event = DiagnosticEventNeeds(ar_root, "TestDiagnosticEventNeeds")

        debounce_algo = diag_event.createDiagEventDebounceTimeBased("TimeBasedAlgo")
        assert debounce_algo is not None
        assert isinstance(debounce_algo, DiagEventDebounceTimeBased)

    def test_get_set_inhibiting_fid_ref(self):
        """Test getInhibitingFidRef and setInhibitingFidRef methods"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        diag_event = DiagnosticEventNeeds(ar_root, "TestDiagnosticEventNeeds")

        assert diag_event.getInhibitingFidRef() is None

        class MockRefType:
            pass

        ref = MockRefType()
        result = diag_event.setInhibitingFidRef(ref)
        assert result is diag_event
        assert diag_event.getInhibitingFidRef() == ref

        diag_event.setInhibitingFidRef(None)
        assert diag_event.getInhibitingFidRef() == ref

    def test_get_add_inhibiting_secondary_fid_refs(self):
        """Test getInhibitingSecondaryFidRefs and addInhibitingSecondaryFidRef methods"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        diag_event = DiagnosticEventNeeds(ar_root, "TestDiagnosticEventNeeds")

        assert diag_event.getInhibitingSecondaryFidRefs() == []

        class MockRefType:
            pass

        ref = MockRefType()
        result = diag_event.addInhibitingSecondaryFidRef(ref)
        assert result is diag_event
        assert diag_event.getInhibitingSecondaryFidRefs() == [ref]

        diag_event.addInhibitingSecondaryFidRef(None)
        assert diag_event.getInhibitingSecondaryFidRefs() == [ref]

    def test_get_set_prestored_freezeframe_stored_in_nvm(self):
        """Test getPrestoredFreezeframeStoredInNvm and setPrestoredFreezeframeStoredInNvm methods"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        diag_event = DiagnosticEventNeeds(ar_root, "TestDiagnosticEventNeeds")

        assert diag_event.getPrestoredFreezeframeStoredInNvm() is None

        result = diag_event.setPrestoredFreezeframeStoredInNvm(True)
        assert result is diag_event
        assert diag_event.getPrestoredFreezeframeStoredInNvm() is True

        diag_event.setPrestoredFreezeframeStoredInNvm(None)
        assert diag_event.getPrestoredFreezeframeStoredInNvm() is True

    def test_get_set_uses_monitor_data(self):
        """Test getUsesMonitorData and setUsesMonitorData methods"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        diag_event = DiagnosticEventNeeds(ar_root, "TestDiagnosticEventNeeds")

        assert diag_event.getUsesMonitorData() is None

        result = diag_event.setUsesMonitorData(True)
        assert result is diag_event
        assert diag_event.getUsesMonitorData() is True

        diag_event.setUsesMonitorData(None)
        assert diag_event.getUsesMonitorData() is True

    def test_roundtrip_diagnostic_event_needs(self):
        """Test parser/writer round trip for DiagnosticEventNeeds"""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        swc = ar_root.createApplicationSwComponentType("App")
        behavior = swc.createSwcInternalBehavior("Behavior")
        dependency = behavior.createSwcServiceDependency("Dep")
        needs = dependency.createDiagnosticEventNeeds("eventNeeds")

        ref1 = RefType()
        ref1.setValue("/Fim/Defer")
        ref1.setDest("FUNCTION-INHIBITION-NEEDS")
        needs.addDeferringFidRef(ref1)
        ref2 = RefType()
        ref2.setValue("/Fim/Inhibit")
        ref2.setDest("FUNCTION-INHIBITION-NEEDS")
        needs.setInhibitingFidRef(ref2)
        ref3 = RefType()
        ref3.setValue("/Fim/Secondary")
        ref3.setDest("FUNCTION-INHIBITION-NEEDS")
        needs.addInhibitingSecondaryFidRef(ref3)
        bool_nvm = Boolean()
        bool_nvm.setValue(True)
        needs.setPrestoredFreezeframeStoredInNvm(bool_nvm)
        bool_monitor = Boolean()
        bool_monitor.setValue(True)
        needs.setUsesMonitorData(bool_monitor)

        import os
        import tempfile

        writer = ARXMLWriter()
        with tempfile.NamedTemporaryFile(suffix=".arxml", delete=False) as f:
            writer.save(f.name, document)
            path = f.name
        try:
            parser = ARXMLParser()
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            parser.load(path, document_2)
            loaded = document_2.find("/AUTOSAR/App/Behavior/Dep/eventNeeds")
            assert loaded is not None
            assert len(loaded.getDeferringFidRefs()) == 1
            assert loaded.getDeferringFidRefs()[0].getValue() == "/Fim/Defer"
            assert loaded.getInhibitingFidRef().getValue() == "/Fim/Inhibit"
            assert len(loaded.getInhibitingSecondaryFidRefs()) == 1
            assert loaded.getInhibitingSecondaryFidRefs()[0].getValue() == "/Fim/Secondary"
            assert loaded.getPrestoredFreezeframeStoredInNvm().getValue() is True
            assert loaded.getUsesMonitorData().getValue() is True
        finally:
            os.unlink(path)

    def test_get_set_audiences(self):
        """Test getAudiences and addAudience methods"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        diag_event = DiagnosticEventNeeds(ar_root, "TestDiagnosticEventNeeds")

        assert diag_event.getAudiences() == []

        enum_val = DiagnosticAudienceEnum.AFTER_MARKET
        result = diag_event.addAudience(enum_val)
        assert result is diag_event
        assert diag_event.getAudiences() == [enum_val]

    def test_get_set_diag_requirement(self):
        """Test getDiagRequirement and setDiagRequirement methods"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        diag_event = DiagnosticEventNeeds(ar_root, "TestDiagnosticEventNeeds")

        assert diag_event.getDiagRequirement() is None

        result = diag_event.setDiagRequirement("REQ-006")
        assert result is diag_event
        assert diag_event.getDiagRequirement() == "REQ-006"

    def test_get_set_security_access_level(self):
        """Test getSecurityAccessLevel and setSecurityAccessLevel methods"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        diag_event = DiagnosticEventNeeds(ar_root, "TestDiagnosticEventNeeds")

        assert diag_event.getSecurityAccessLevel() is None

        result = diag_event.setSecurityAccessLevel(7)
        assert result is diag_event
        assert diag_event.getSecurityAccessLevel() == 7


class TestErrorTracerNeeds:
    def test_initialization(self):
        """Test ErrorTracerNeeds initialization"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        needs = ErrorTracerNeeds(ar_root, "TestErrorTracerNeeds")

        assert needs is not None
        assert needs.getShortName() == "TestErrorTracerNeeds"
        assert needs.getTracedFailures() == []

    def test_get_traced_failures(self):
        """Test getTracedFailures default value"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        needs = ErrorTracerNeeds(ar_root, "TestErrorTracerNeeds")
        assert needs.getTracedFailures() == []

    def test_create_development_error(self):
        """Test createDevelopmentError method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        needs = ErrorTracerNeeds(ar_root, "TestErrorTracerNeeds")

        failure = needs.createDevelopmentError("DevError")
        assert isinstance(failure, DevelopmentError)
        assert failure.getShortName() == "DevError"
        assert len(needs.getTracedFailures()) == 1

        same = needs.createDevelopmentError("DevError")
        assert same is failure
        assert len(needs.getTracedFailures()) == 1

    def test_create_runtime_error(self):
        """Test createRuntimeError method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        needs = ErrorTracerNeeds(ar_root, "TestErrorTracerNeeds")

        failure = needs.createRuntimeError("RunError")
        assert isinstance(failure, RuntimeError)
        assert failure.getShortName() == "RunError"
        assert len(needs.getTracedFailures()) == 1

    def test_create_transient_fault(self):
        """Test createTransientFault method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        needs = ErrorTracerNeeds(ar_root, "TestErrorTracerNeeds")

        failure = needs.createTransientFault("TransFault")
        assert isinstance(failure, TransientFault)
        assert failure.getShortName() == "TransFault"
        assert len(needs.getTracedFailures()) == 1

    def test_roundtrip_error_tracer_needs(self):
        """Test parser/writer round trip for ErrorTracerNeeds"""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        swc = ar_root.createApplicationSwComponentType("App")
        behavior = swc.createSwcInternalBehavior("Behavior")
        dependency = behavior.createSwcServiceDependency("Dep")
        needs = dependency.createErrorTracerNeeds("etn")

        dev = needs.createDevelopmentError("dev1")
        id_value = PositiveInteger()
        id_value.setValue("10")
        dev.setId(id_value)
        needs.createRuntimeError("rt1")
        tf = needs.createTransientFault("tf1")
        reaction = tf.createPossibleErrorReaction("reac1")
        reaction_code = PositiveInteger()
        reaction_code.setValue("99")
        reaction.setReactionCode(reaction_code)

        import os
        import tempfile

        writer = ARXMLWriter()
        with tempfile.NamedTemporaryFile(suffix=".arxml", delete=False) as f:
            writer.save(f.name, document)
            path = f.name
        try:
            parser = ARXMLParser()
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            parser.load(path, document_2)
            loaded = document_2.find("/AUTOSAR/App/Behavior/Dep/etn")
            assert loaded is not None
            failures = loaded.getTracedFailures()
            assert len(failures) == 3
            by_name = {f.getShortName(): f for f in failures}
            assert isinstance(by_name["dev1"], DevelopmentError)
            assert by_name["dev1"].getId().getValue() == 10
            assert isinstance(by_name["rt1"], RuntimeError)
            assert isinstance(by_name["tf1"], TransientFault)
            assert len(by_name["tf1"].getPossibleErrorReactions()) == 1
            assert by_name["tf1"].getPossibleErrorReactions()[0].getReactionCode().getValue() == 99
        finally:
            os.unlink(path)


class TestTracedFailure:
    def test_abstract_initialization(self):
        """Test that TracedFailure cannot be instantiated directly"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        with pytest.raises(TypeError):
            TracedFailure(ar_root, "TestTracedFailure")

    def test_concrete_subclass_initialization(self):
        """Test abstract TracedFailure __init__ defaults through a concrete subclass"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        failure = DevelopmentError(ar_root, "TestTracedFailure")

        assert failure.getShortName() == "TestTracedFailure"
        assert failure.getId() is None

    def test_get_set_id(self):
        """Test getId and setId methods through a concrete subclass"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        failure = DevelopmentError(ar_root, "TestTracedFailure")

        assert failure.getId() is None

        value = PositiveInteger()
        value.setValue("5")
        result = failure.setId(value)
        assert result is failure
        assert failure.getId() == value

        failure.setId(None)
        assert failure.getId() == value


class TestDevelopmentError:
    def test_initialization(self):
        """Test DevelopmentError initialization"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        failure = DevelopmentError(ar_root, "TestDevelopmentError")

        assert failure is not None
        assert failure.getShortName() == "TestDevelopmentError"
        assert failure.getId() is None


class TestRuntimeError:
    def test_initialization(self):
        """Test RuntimeError initialization"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        failure = RuntimeError(ar_root, "TestRuntimeError")

        assert failure is not None
        assert failure.getShortName() == "TestRuntimeError"
        assert failure.getId() is None


class TestTransientFault:
    def test_initialization(self):
        """Test TransientFault initialization"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        failure = TransientFault(ar_root, "TestTransientFault")

        assert failure is not None
        assert failure.getShortName() == "TestTransientFault"
        assert failure.getId() is None
        assert failure.getPossibleErrorReactions() == []

    def test_create_possible_error_reaction(self):
        """Test createPossibleErrorReaction and getPossibleErrorReactions methods"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        failure = TransientFault(ar_root, "TestTransientFault")

        reaction = failure.createPossibleErrorReaction("Reac")
        assert isinstance(reaction, PossibleErrorReaction)
        assert reaction.getShortName() == "Reac"
        assert len(failure.getPossibleErrorReactions()) == 1

        same = failure.createPossibleErrorReaction("Reac")
        assert same is reaction
        assert len(failure.getPossibleErrorReactions()) == 1


class TestPossibleErrorReaction:
    def test_initialization(self):
        """Test PossibleErrorReaction initialization"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        reaction = PossibleErrorReaction(ar_root, "TestPossibleErrorReaction")

        assert reaction is not None
        assert reaction.getShortName() == "TestPossibleErrorReaction"
        assert reaction.getReactionCode() is None

    def test_get_set_reaction_code(self):
        """Test getReactionCode and setReactionCode methods"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        reaction = PossibleErrorReaction(ar_root, "TestPossibleErrorReaction")

        assert reaction.getReactionCode() is None

        value = PositiveInteger()
        value.setValue("42")
        result = reaction.setReactionCode(value)
        assert result is reaction
        assert reaction.getReactionCode() == value

        reaction.setReactionCode(None)
        assert reaction.getReactionCode() == value


class TestCryptoServiceNeeds:
    def test_initialization(self):
        """Test CryptoServiceNeeds initialization"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        crypto_service = CryptoServiceNeeds(ar_root, "TestCryptoServiceNeeds")

        assert crypto_service is not None
        assert crypto_service.getShortName() == "TestCryptoServiceNeeds"
        assert crypto_service.algorithmFamily is None
        assert crypto_service.algorithmMode is None
        assert crypto_service.cryptoKeyDescription is None
        assert crypto_service.maximumKeyLength is None

    def test_get_set_algorithm_family(self):
        """Test getAlgorithmFamily and setAlgorithmFamily methods"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        crypto_service = CryptoServiceNeeds(ar_root, "TestCryptoServiceNeeds")

        assert crypto_service.getAlgorithmFamily() is None

        result = crypto_service.setAlgorithmFamily("AES")
        assert result is crypto_service
        assert crypto_service.getAlgorithmFamily() == "AES"

    def test_get_set_algorithm_mode(self):
        """Test getAlgorithmMode and setAlgorithmMode methods"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        crypto_service = CryptoServiceNeeds(ar_root, "TestCryptoServiceNeeds")

        assert crypto_service.getAlgorithmMode() is None

        result = crypto_service.setAlgorithmMode("CBC")
        assert result is crypto_service
        assert crypto_service.getAlgorithmMode() == "CBC"

    def test_get_set_crypto_key_description(self):
        """Test getCryptoKeyDescription and setCryptoKeyDescription methods"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        crypto_service = CryptoServiceNeeds(ar_root, "TestCryptoServiceNeeds")

        assert crypto_service.getCryptoKeyDescription() is None

        result = crypto_service.setCryptoKeyDescription("AES-256 key")
        assert result is crypto_service
        assert crypto_service.getCryptoKeyDescription() == "AES-256 key"

    def test_get_set_maximum_key_length(self):
        """Test getMaximumKeyLength and setMaximumKeyLength methods"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        crypto_service = CryptoServiceNeeds(ar_root, "TestCryptoServiceNeeds")

        assert crypto_service.getMaximumKeyLength() is None

        result = crypto_service.setMaximumKeyLength(256)
        assert result is crypto_service
        assert crypto_service.getMaximumKeyLength() == 256


class TestEcuStateMgrUserNeeds:
    def test_initialization(self):
        """Test EcuStateMgrUserNeeds initialization"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        ecu_state = EcuStateMgrUserNeeds(ar_root, "TestEcuStateMgrUserNeeds")

        assert ecu_state is not None
        assert ecu_state.getShortName() == "TestEcuStateMgrUserNeeds"


class TestDltUserNeeds:
    def test_initialization(self):
        """Test DltUserNeeds initialization"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        dlt_user = DltUserNeeds(ar_root, "TestDltUserNeeds")

        assert dlt_user is not None
        assert dlt_user.getShortName() == "TestDltUserNeeds"


class TestMaxCommModeEnum:
    def test_initialization(self):
        """Test MaxCommModeEnum initialization"""
        enum = MaxCommModeEnum()

        assert enum.enumValues == ("full", "none", "silent")

    def test_values(self):
        """Test enum values"""
        assert MaxCommModeEnum.FULL == "full"
        assert MaxCommModeEnum.NONE == "none"
        assert MaxCommModeEnum.SILENT == "silent"


class TestEventAcceptanceStatusEnum:
    def test_initialization(self):
        """Test EventAcceptanceStatusEnum initialization"""
        enum = EventAcceptanceStatusEnum()
        assert enum.enumValues == ("eventAcceptanceDisabled", "eventAcceptanceEnabled")

    def test_values(self):
        """Test enum values"""
        assert EventAcceptanceStatusEnum.EVENT_ACCEPTANCE_DISABLED == "eventAcceptanceDisabled"
        assert EventAcceptanceStatusEnum.EVENT_ACCEPTANCE_ENABLED == "eventAcceptanceEnabled"

    def test_get_value(self):
        """Test setValue/getValue round-trip"""
        enum = EventAcceptanceStatusEnum().setValue(EventAcceptanceStatusEnum.EVENT_ACCEPTANCE_ENABLED)
        assert enum.getValue() == "eventAcceptanceEnabled"


class TestOperationCycleTypeEnum:
    def test_initialization(self):
        """Test OperationCycleTypeEnum initialization"""
        enum = OperationCycleTypeEnum()
        assert enum.enumValues == ("ignition", "obdDcy", "other", "power", "time", "warmup")

    def test_values(self):
        """Test enum values"""
        assert OperationCycleTypeEnum.IGNITION == "ignition"
        assert OperationCycleTypeEnum.OBD_DCY == "obdDcy"
        assert OperationCycleTypeEnum.OTHER == "other"
        assert OperationCycleTypeEnum.POWER == "power"
        assert OperationCycleTypeEnum.TIME == "time"
        assert OperationCycleTypeEnum.WARMUP == "warmup"

    def test_get_value(self):
        """Test setValue/getValue round-trip"""
        enum = OperationCycleTypeEnum().setValue(OperationCycleTypeEnum.WARMUP)
        assert enum.getValue() == "warmup"


class TestStorageConditionStatusEnum:
    def test_initialization(self):
        """Test StorageConditionStatusEnum initialization"""
        enum = StorageConditionStatusEnum()
        assert enum.enumValues == ("eventStorageDisabled", "eventStorageEnabled")

    def test_values(self):
        """Test enum values"""
        assert StorageConditionStatusEnum.EVENT_STORAGE_DISABLE == "eventStorageDisabled"
        assert StorageConditionStatusEnum.EVENT_STORAGE_ENABLE == "eventStorageEnabled"

    def test_get_value(self):
        """Test setValue/getValue round-trip"""
        enum = StorageConditionStatusEnum().setValue(StorageConditionStatusEnum.EVENT_STORAGE_ENABLE)
        assert enum.getValue() == "eventStorageEnabled"


class TestDiagnosticIndicatorTypeEnum:
    def test_initialization(self):
        """Test DiagnosticIndicatorTypeEnum initialization"""
        enum = DiagnosticIndicatorTypeEnum()
        assert enum.enumValues == ("amberWarning", "malfunction", "protectLamp", "redStopLamp", "warning")

    def test_values(self):
        """Test enum values"""
        assert DiagnosticIndicatorTypeEnum.AMBER_WARNING == "amberWarning"
        assert DiagnosticIndicatorTypeEnum.MALFUNCTION == "malfunction"
        assert DiagnosticIndicatorTypeEnum.PROTECT_LAMP == "protectLamp"
        assert DiagnosticIndicatorTypeEnum.RED_STOP_LAMP == "redStopLamp"
        assert DiagnosticIndicatorTypeEnum.WARNING == "warning"

    def test_get_value(self):
        """Test setValue/getValue round-trip"""
        enum = DiagnosticIndicatorTypeEnum().setValue(DiagnosticIndicatorTypeEnum.MALFUNCTION)
        assert enum.getValue() == "malfunction"


class TestComMgrUserNeeds:
    def test_initialization(self):
        """Test ComMgrUserNeeds initialization"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        needs = ComMgrUserNeeds(ar_root, "TestComMgrUserNeeds")

        assert needs is not None
        assert needs.getShortName() == "TestComMgrUserNeeds"
        assert needs.maxCommMode is None

    def test_get_set_max_comm_mode(self):
        """Test getMaxCommMode/setMaxCommMode (chaining, round-trip, None no-op)"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        needs = ComMgrUserNeeds(ar_root, "TestComMgrUserNeeds")

        value = MaxCommModeEnum().setValue(MaxCommModeEnum.FULL)
        result = needs.setMaxCommMode(value)
        assert result is needs  # Method chaining
        assert needs.getMaxCommMode() == value

        needs.setMaxCommMode(None)  # No-op
        assert needs.getMaxCommMode() == value


class TestComMgrUserNeedsRoundTrip:
    def test_round_trip_max_comm_mode(self):
        """Test parse -> write -> re-parse preserves maxCommMode."""
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        ar_root = document.createARPackage("AUTOSAR")
        desc = ar_root.createBswModuleDescription("BswMd")
        behavior = desc.createBswInternalBehavior("Beh")
        dependency = BswServiceDependency()
        needs = ComMgrUserNeeds(dependency, "ComNeeds")
        needs.setMaxCommMode(MaxCommModeEnum().setValue(MaxCommModeEnum.FULL))
        dependency.setServiceNeeds(needs)
        behavior.addServiceDependency(dependency)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            behavior_2 = document_2.getARPackages()[0].getBswModuleDescriptions()[0].getInternalBehaviors()[0]
            needs_2 = behavior_2.getServiceDependencies()[0].getServiceNeeds()
            assert needs_2.getShortName() == "ComNeeds"
            assert needs_2.getMaxCommMode().getValue() == "full"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)


class TestDiagnosticEnableConditionNeeds:
    def test_initialization(self):
        """Test DiagnosticEnableConditionNeeds initialization"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        needs = DiagnosticEnableConditionNeeds(ar_root, "TestDiagnosticEnableConditionNeeds")

        assert needs is not None
        assert needs.getShortName() == "TestDiagnosticEnableConditionNeeds"
        assert needs.getInitialStatus() is None

    def test_get_set_initial_status(self):
        """Test getInitialStatus/setInitialStatus (chaining, round-trip, None no-op)"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        needs = DiagnosticEnableConditionNeeds(ar_root, "TestDiagnosticEnableConditionNeeds")

        value = EventAcceptanceStatusEnum().setValue(EventAcceptanceStatusEnum.EVENT_ACCEPTANCE_ENABLED)
        result = needs.setInitialStatus(value)
        assert result is needs  # Method chaining
        assert needs.getInitialStatus() == value

        needs.setInitialStatus(None)  # No-op
        assert needs.getInitialStatus() == value

    def test_round_trip_initial_status(self):
        """Test parse -> write -> re-parse preserves initialStatus."""
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        ar_root = document.createARPackage("AUTOSAR")
        desc = ar_root.createBswModuleDescription("BswMd")
        behavior = desc.createBswInternalBehavior("Beh")
        dependency = BswServiceDependency()
        needs = DiagnosticEnableConditionNeeds(dependency, "EnableNeeds")
        needs.setInitialStatus(EventAcceptanceStatusEnum().setValue(EventAcceptanceStatusEnum.EVENT_ACCEPTANCE_DISABLED))
        dependency.setServiceNeeds(needs)
        behavior.addServiceDependency(dependency)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            behavior_2 = document_2.getARPackages()[0].getBswModuleDescriptions()[0].getInternalBehaviors()[0]
            needs_2 = behavior_2.getServiceDependencies()[0].getServiceNeeds()
            assert needs_2.getShortName() == "EnableNeeds"
            assert needs_2.getInitialStatus().getValue() == "eventAcceptanceDisabled"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)


class TestDiagnosticOperationCycleNeeds:
    def test_initialization(self):
        """Test DiagnosticOperationCycleNeeds initialization"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        needs = DiagnosticOperationCycleNeeds(ar_root, "TestDiagnosticOperationCycleNeeds")

        assert needs is not None
        assert needs.getShortName() == "TestDiagnosticOperationCycleNeeds"
        assert needs.getOperationCycle() is None

    def test_get_set_operation_cycle(self):
        """Test getOperationCycle/setOperationCycle (chaining, round-trip, None no-op)"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        needs = DiagnosticOperationCycleNeeds(ar_root, "TestDiagnosticOperationCycleNeeds")

        value = OperationCycleTypeEnum().setValue(OperationCycleTypeEnum.WARMUP)
        result = needs.setOperationCycle(value)
        assert result is needs  # Method chaining
        assert needs.getOperationCycle() == value

        needs.setOperationCycle(None)  # No-op
        assert needs.getOperationCycle() == value

    def test_round_trip_operation_cycle(self):
        """Test parse -> write -> re-parse preserves operationCycle."""
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        ar_root = document.createARPackage("AUTOSAR")
        desc = ar_root.createBswModuleDescription("BswMd")
        behavior = desc.createBswInternalBehavior("Beh")
        dependency = BswServiceDependency()
        needs = DiagnosticOperationCycleNeeds(dependency, "CycleNeeds")
        needs.setOperationCycle(OperationCycleTypeEnum().setValue(OperationCycleTypeEnum.POWER))
        dependency.setServiceNeeds(needs)
        behavior.addServiceDependency(dependency)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            behavior_2 = document_2.getARPackages()[0].getBswModuleDescriptions()[0].getInternalBehaviors()[0]
            needs_2 = behavior_2.getServiceDependencies()[0].getServiceNeeds()
            assert needs_2.getShortName() == "CycleNeeds"
            assert needs_2.getOperationCycle().getValue() == "power"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)


class TestDiagnosticStorageConditionNeeds:
    def test_initialization(self):
        """Test DiagnosticStorageConditionNeeds initialization"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        needs = DiagnosticStorageConditionNeeds(ar_root, "TestDiagnosticStorageConditionNeeds")

        assert needs is not None
        assert needs.getShortName() == "TestDiagnosticStorageConditionNeeds"
        assert needs.getInitialStatus() is None

    def test_get_set_initial_status(self):
        """Test getInitialStatus/setInitialStatus (chaining, round-trip, None no-op)"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        needs = DiagnosticStorageConditionNeeds(ar_root, "TestDiagnosticStorageConditionNeeds")

        value = StorageConditionStatusEnum().setValue(StorageConditionStatusEnum.EVENT_STORAGE_ENABLE)
        result = needs.setInitialStatus(value)
        assert result is needs  # Method chaining
        assert needs.getInitialStatus() == value

        needs.setInitialStatus(None)  # No-op
        assert needs.getInitialStatus() == value

    def test_round_trip_initial_status(self):
        """Test parse -> write -> re-parse preserves initialStatus."""
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        ar_root = document.createARPackage("AUTOSAR")
        desc = ar_root.createBswModuleDescription("BswMd")
        behavior = desc.createBswInternalBehavior("Beh")
        dependency = BswServiceDependency()
        needs = DiagnosticStorageConditionNeeds(dependency, "StorageNeeds")
        needs.setInitialStatus(StorageConditionStatusEnum().setValue(StorageConditionStatusEnum.EVENT_STORAGE_DISABLE))
        dependency.setServiceNeeds(needs)
        behavior.addServiceDependency(dependency)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            behavior_2 = document_2.getARPackages()[0].getBswModuleDescriptions()[0].getInternalBehaviors()[0]
            needs_2 = behavior_2.getServiceDependencies()[0].getServiceNeeds()
            assert needs_2.getShortName() == "StorageNeeds"
            assert needs_2.getInitialStatus().getValue() == "eventStorageDisabled"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)


class TestIndicatorStatusNeeds:
    def test_initialization(self):
        """Test IndicatorStatusNeeds initialization"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        needs = IndicatorStatusNeeds(ar_root, "TestIndicatorStatusNeeds")

        assert needs is not None
        assert needs.getShortName() == "TestIndicatorStatusNeeds"
        assert needs.getType() is None

    def test_get_set_type(self):
        """Test getType/setType (chaining, round-trip, None no-op)"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        needs = IndicatorStatusNeeds(ar_root, "TestIndicatorStatusNeeds")

        value = DiagnosticIndicatorTypeEnum().setValue(DiagnosticIndicatorTypeEnum.MALFUNCTION)
        result = needs.setType(value)
        assert result is needs  # Method chaining
        assert needs.getType() == value

        needs.setType(None)  # No-op
        assert needs.getType() == value

    def test_round_trip_type(self):
        """Test parse -> write -> re-parse preserves type."""
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        ar_root = document.createARPackage("AUTOSAR")
        desc = ar_root.createBswModuleDescription("BswMd")
        behavior = desc.createBswInternalBehavior("Beh")
        dependency = BswServiceDependency()
        needs = IndicatorStatusNeeds(dependency, "IndNeeds")
        needs.setType(DiagnosticIndicatorTypeEnum().setValue(DiagnosticIndicatorTypeEnum.AMBER_WARNING))
        dependency.setServiceNeeds(needs)
        behavior.addServiceDependency(dependency)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            behavior_2 = document_2.getARPackages()[0].getBswModuleDescriptions()[0].getInternalBehaviors()[0]
            needs_2 = behavior_2.getServiceDependencies()[0].getServiceNeeds()
            assert needs_2.getShortName() == "IndNeeds"
            assert needs_2.getType().getValue() == "amberWarning"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)


class TestFunctionInhibitionAvailabilityNeeds:
    def test_initialization(self):
        """Test FunctionInhibitionAvailabilityNeeds initialization"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        needs = FunctionInhibitionAvailabilityNeeds(ar_root, "TestFunctionInhibitionAvailabilityNeeds")

        assert needs is not None
        assert needs.getShortName() == "TestFunctionInhibitionAvailabilityNeeds"
        assert needs.getControlledFidRef() is None

    def test_get_set_controlled_fid_ref(self):
        """Test getControlledFidRef/setControlledFidRef (chaining, round-trip, None no-op)"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        needs = FunctionInhibitionAvailabilityNeeds(ar_root, "TestFunctionInhibitionAvailabilityNeeds")

        value = RefType()
        value.setValue("/Fim/Controlled")
        value.setDest("FUNCTION-INHIBITION-NEEDS")
        result = needs.setControlledFidRef(value)
        assert result is needs  # Method chaining
        assert needs.getControlledFidRef() == value

        needs.setControlledFidRef(None)  # No-op
        assert needs.getControlledFidRef() == value

    def test_round_trip_controlled_fid_ref(self):
        """Test parse -> write -> re-parse preserves controlledFidRef."""
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        ar_root = document.createARPackage("AUTOSAR")
        desc = ar_root.createBswModuleDescription("BswMd")
        behavior = desc.createBswInternalBehavior("Beh")
        dependency = BswServiceDependency()
        needs = FunctionInhibitionAvailabilityNeeds(dependency, "FimNeeds")
        ref = RefType()
        ref.setValue("/Fim/Controlled")
        ref.setDest("FUNCTION-INHIBITION-NEEDS")
        needs.setControlledFidRef(ref)
        dependency.setServiceNeeds(needs)
        behavior.addServiceDependency(dependency)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            behavior_2 = document_2.getARPackages()[0].getBswModuleDescriptions()[0].getInternalBehaviors()[0]
            needs_2 = behavior_2.getServiceDependencies()[0].getServiceNeeds()
            assert needs_2.getShortName() == "FimNeeds"
            assert needs_2.getControlledFidRef().getValue() == "/Fim/Controlled"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)


class TestSupervisedEntityNeeds:
    def test_initialization(self):
        """Test SupervisedEntityNeeds initialization"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        needs = SupervisedEntityNeeds(ar_root, "TestSupervisedEntityNeeds")

        assert needs is not None
        assert needs.getShortName() == "TestSupervisedEntityNeeds"
        assert needs.activateAtStart is None
        assert needs.checkpointsRefs == []
        assert needs.enableDeactivation is None
        assert needs.expectedAliveCycle is None
        assert needs.maxAliveCycle is None
        assert needs.minAliveCycle is None
        assert needs.toleratedFailedCycles is None

    def test_get_set_activate_at_start(self):
        """Test getActivateAtStart/setActivateAtStart (chaining, round-trip, None no-op)"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        needs = SupervisedEntityNeeds(ar_root, "TestSupervisedEntityNeeds")

        value = Boolean().setValue(True)
        result = needs.setActivateAtStart(value)
        assert result is needs  # Method chaining
        assert needs.getActivateAtStart() == value

        needs.setActivateAtStart(None)  # No-op
        assert needs.getActivateAtStart() == value

    def test_add_get_checkpoints_refs(self):
        """Test addCheckpointsRef/getCheckpointsRefs (append, chaining, None no-op)"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        needs = SupervisedEntityNeeds(ar_root, "TestSupervisedEntityNeeds")

        ref = RefType().setValue("/Checkpoint")
        result = needs.addCheckpointsRef(ref)
        assert result is needs  # Method chaining
        assert needs.getCheckpointsRefs() == [ref]

        needs.addCheckpointsRef(None)  # No-op
        assert needs.getCheckpointsRefs() == [ref]

    def test_get_set_enable_deactivation(self):
        """Test getEnableDeactivation/setEnableDeactivation (chaining, round-trip, None no-op)"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        needs = SupervisedEntityNeeds(ar_root, "TestSupervisedEntityNeeds")

        value = Boolean().setValue(False)
        result = needs.setEnableDeactivation(value)
        assert result is needs  # Method chaining
        assert needs.getEnableDeactivation() == value

        needs.setEnableDeactivation(None)  # No-op
        assert needs.getEnableDeactivation() == value

    def test_get_set_expected_alive_cycle(self):
        """Test getExpectedAliveCycle/setExpectedAliveCycle (chaining, round-trip, None no-op)"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        needs = SupervisedEntityNeeds(ar_root, "TestSupervisedEntityNeeds")

        value = TimeValue().setValue(0.001)
        result = needs.setExpectedAliveCycle(value)
        assert result is needs  # Method chaining
        assert needs.getExpectedAliveCycle() == value

        needs.setExpectedAliveCycle(None)  # No-op
        assert needs.getExpectedAliveCycle() == value

    def test_get_set_max_alive_cycle(self):
        """Test getMaxAliveCycle/setMaxAliveCycle (chaining, round-trip, None no-op)"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        needs = SupervisedEntityNeeds(ar_root, "TestSupervisedEntityNeeds")

        value = TimeValue().setValue(0.01)
        result = needs.setMaxAliveCycle(value)
        assert result is needs  # Method chaining
        assert needs.getMaxAliveCycle() == value

        needs.setMaxAliveCycle(None)  # No-op
        assert needs.getMaxAliveCycle() == value

    def test_get_set_min_alive_cycle(self):
        """Test getMinAliveCycle/setMinAliveCycle (chaining, round-trip, None no-op)"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        needs = SupervisedEntityNeeds(ar_root, "TestSupervisedEntityNeeds")

        value = TimeValue().setValue(0.001)
        result = needs.setMinAliveCycle(value)
        assert result is needs  # Method chaining
        assert needs.getMinAliveCycle() == value

        needs.setMinAliveCycle(None)  # No-op
        assert needs.getMinAliveCycle() == value

    def test_get_set_tolerated_failed_cycles(self):
        """Test getToleratedFailedCycles/setToleratedFailedCycles (chaining, round-trip, None no-op)"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        needs = SupervisedEntityNeeds(ar_root, "TestSupervisedEntityNeeds")

        value = PositiveInteger().setValue("4")
        result = needs.setToleratedFailedCycles(value)
        assert result is needs  # Method chaining
        assert needs.getToleratedFailedCycles() == value

        needs.setToleratedFailedCycles(None)  # No-op
        assert needs.getToleratedFailedCycles() == value


class TestDiagnosticMonitorUpdateKindEnum:
    def test_enum_values(self):
        """Test DiagnosticMonitorUpdateKindEnum literal values and indices."""
        assert DiagnosticMonitorUpdateKindEnum.ALWAYS == "always"
        assert DiagnosticMonitorUpdateKindEnum.STEADY == "steady"
        enum = DiagnosticMonitorUpdateKindEnum()
        assert "always" in enum.getEnumValues()
        assert "steady" in enum.getEnumValues()

    def test_set_value(self):
        """Test setValue/getValue round-trip for the enum."""
        enum = DiagnosticMonitorUpdateKindEnum()
        result = enum.setValue(DiagnosticMonitorUpdateKindEnum.STEADY)
        assert result is enum  # Method chaining
        assert enum.getValue() == "steady"

        enum.setValue(DiagnosticMonitorUpdateKindEnum.ALWAYS)
        assert enum.getValue() == "always"

        enum.setValue(None)  # No-op
        assert enum.getValue() == "always"


class TestObdInfoServiceNeeds:
    def test_initialization(self):
        """Test ObdInfoServiceNeeds initialization defaults."""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        needs = ObdInfoServiceNeeds(ar_root, "TestObdInfoServiceNeeds")

        assert needs is not None
        assert needs.getShortName() == "TestObdInfoServiceNeeds"
        assert needs.audiences == []
        assert needs.diagRequirement is None
        assert needs.securityAccessLevel is None


class TestObdMonitorServiceNeeds:
    def test_initialization(self):
        """Test ObdMonitorServiceNeeds initialization defaults."""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        needs = ObdMonitorServiceNeeds(ar_root, "TestObdMonitorServiceNeeds")

        assert needs is not None
        assert needs.getShortName() == "TestObdMonitorServiceNeeds"
        assert needs.audiences == []
        assert needs.diagRequirement is None
        assert needs.securityAccessLevel is None
        assert needs.getApplicationDataTypeRef() is None
        assert needs.getEventNeedsRef() is None
        assert needs.getUnitAndScalingId() is None
        assert needs.getUpdateKind() is None

    def test_get_set_application_data_type_ref(self):
        """Test getApplicationDataTypeRef/setApplicationDataTypeRef (chaining, round-trip, None no-op)."""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        needs = ObdMonitorServiceNeeds(ar_root, "TestObdMonitorServiceNeeds")

        value = RefType().setValue("/Data/AppType")
        result = needs.setApplicationDataTypeRef(value)
        assert result is needs  # Method chaining
        assert needs.getApplicationDataTypeRef() == value

        needs.setApplicationDataTypeRef(None)  # No-op
        assert needs.getApplicationDataTypeRef() == value

    def test_get_set_event_needs_ref(self):
        """Test getEventNeedsRef/setEventNeedsRef (chaining, round-trip, None no-op)."""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        needs = ObdMonitorServiceNeeds(ar_root, "TestObdMonitorServiceNeeds")

        value = RefType().setValue("/Events/Evt")
        result = needs.setEventNeedsRef(value)
        assert result is needs  # Method chaining
        assert needs.getEventNeedsRef() == value

        needs.setEventNeedsRef(None)  # No-op
        assert needs.getEventNeedsRef() == value

    def test_get_set_unit_and_scaling_id(self):
        """Test getUnitAndScalingId/setUnitAndScalingId (chaining, round-trip, None no-op)."""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        needs = ObdMonitorServiceNeeds(ar_root, "TestObdMonitorServiceNeeds")

        value = PositiveInteger().setValue("2")
        result = needs.setUnitAndScalingId(value)
        assert result is needs  # Method chaining
        assert needs.getUnitAndScalingId() == value

        needs.setUnitAndScalingId(None)  # No-op
        assert needs.getUnitAndScalingId() == value

    def test_get_set_update_kind(self):
        """Test getUpdateKind/setUpdateKind (chaining, round-trip, None no-op)."""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        needs = ObdMonitorServiceNeeds(ar_root, "TestObdMonitorServiceNeeds")

        value = DiagnosticMonitorUpdateKindEnum().setValue(DiagnosticMonitorUpdateKindEnum.STEADY)
        result = needs.setUpdateKind(value)
        assert result is needs  # Method chaining
        assert needs.getUpdateKind() == value

        needs.setUpdateKind(None)  # No-op
        assert needs.getUpdateKind() == value


class TestObdPidServiceNeeds:
    def test_initialization(self):
        """Test ObdPidServiceNeeds initialization defaults."""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        needs = ObdPidServiceNeeds(ar_root, "TestObdPidServiceNeeds")

        assert needs is not None
        assert needs.getShortName() == "TestObdPidServiceNeeds"
        assert needs.audiences == []
        assert needs.diagRequirement is None
        assert needs.securityAccessLevel is None


class TestObdInfoServiceNeedsRoundTrip:
    def test_round_trip_attributes(self):
        """Test parse -> write -> re-parse preserves ObdInfoServiceNeeds (attribute-less)."""
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        ar_root = document.createARPackage("AUTOSAR")
        desc = ar_root.createBswModuleDescription("BswMd")
        behavior = desc.createBswInternalBehavior("Beh")
        dependency = BswServiceDependency()
        needs = ObdInfoServiceNeeds(dependency, "ObdInfoNeeds")
        dependency.setServiceNeeds(needs)
        behavior.addServiceDependency(dependency)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            behavior_2 = document_2.getARPackages()[0].getBswModuleDescriptions()[0].getInternalBehaviors()[0]
            needs_2 = behavior_2.getServiceDependencies()[0].getServiceNeeds()
            assert needs_2.getShortName() == "ObdInfoNeeds"
            assert isinstance(needs_2, ObdInfoServiceNeeds)
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)


class TestObdMonitorServiceNeedsRoundTrip:
    def test_round_trip_bsw_attributes(self):
        """Test parse -> write -> re-parse preserves ObdMonitorServiceNeeds attributes (BSW path)."""
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        ar_root = document.createARPackage("AUTOSAR")
        desc = ar_root.createBswModuleDescription("BswMd")
        behavior = desc.createBswInternalBehavior("Beh")
        dependency = BswServiceDependency()
        needs = ObdMonitorServiceNeeds(dependency, "ObdMonitorNeeds")
        app_ref = RefType()
        app_ref.setValue("/Data/AppType")
        app_ref.setDest("APPLICATION-DATA-TYPE--SUBTYPES-ENUM")
        needs.setApplicationDataTypeRef(app_ref)
        evt_ref = RefType()
        evt_ref.setValue("/Events/Evt")
        evt_ref.setDest("DIAGNOSTIC-EVENT-NEEDS--SUBTYPES-ENUM")
        needs.setEventNeedsRef(evt_ref)
        needs.setUnitAndScalingId(PositiveInteger().setValue("2"))
        needs.setUpdateKind(DiagnosticMonitorUpdateKindEnum().setValue(DiagnosticMonitorUpdateKindEnum.STEADY))
        dependency.setServiceNeeds(needs)
        behavior.addServiceDependency(dependency)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            behavior_2 = document_2.getARPackages()[0].getBswModuleDescriptions()[0].getInternalBehaviors()[0]
            needs_2 = behavior_2.getServiceDependencies()[0].getServiceNeeds()
            assert needs_2.getShortName() == "ObdMonitorNeeds"
            assert isinstance(needs_2, ObdMonitorServiceNeeds)
            assert needs_2.getApplicationDataTypeRef().getValue() == "/Data/AppType"
            assert needs_2.getApplicationDataTypeRef().getDest() == "APPLICATION-DATA-TYPE--SUBTYPES-ENUM"
            assert needs_2.getEventNeedsRef().getValue() == "/Events/Evt"
            assert needs_2.getEventNeedsRef().getDest() == "DIAGNOSTIC-EVENT-NEEDS--SUBTYPES-ENUM"
            assert needs_2.getUnitAndScalingId().getValue() == 2
            assert needs_2.getUpdateKind().getValue() == "steady"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_round_trip_swc_attributes(self):
        """Test parse -> write -> re-parse preserves ObdMonitorServiceNeeds attributes (SWC path)."""
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        ar_root = document.createARPackage("AUTOSAR")
        swc = ar_root.createApplicationSwComponentType("Swc")
        behavior = swc.createSwcInternalBehavior("Beh")
        dependency = behavior.createSwcServiceDependency("Dep")
        needs = dependency.createObdMonitorServiceNeeds("ObdMonitorNeeds")
        needs.setUpdateKind(DiagnosticMonitorUpdateKindEnum().setValue(DiagnosticMonitorUpdateKindEnum.ALWAYS))

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            behavior_2 = document_2.getARPackages()[0].getElement("Swc", ApplicationSwComponentType).getInternalBehavior()
            needs_2 = behavior_2.getSwcServiceDependencies()[0].getObdMonitorServiceNeeds()[0]
            assert needs_2.getShortName() == "ObdMonitorNeeds"
            assert isinstance(needs_2, ObdMonitorServiceNeeds)
            assert needs_2.getUpdateKind().getValue() == "always"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)


class TestObdPidServiceNeedsRoundTrip:
    def test_round_trip_attributes(self):
        """Test parse -> write -> re-parse preserves ObdPidServiceNeeds (attribute-less)."""
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        ar_root = document.createARPackage("AUTOSAR")
        desc = ar_root.createBswModuleDescription("BswMd")
        behavior = desc.createBswInternalBehavior("Beh")
        dependency = BswServiceDependency()
        needs = ObdPidServiceNeeds(dependency, "ObdPidNeeds")
        dependency.setServiceNeeds(needs)
        behavior.addServiceDependency(dependency)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            behavior_2 = document_2.getARPackages()[0].getBswModuleDescriptions()[0].getInternalBehaviors()[0]
            needs_2 = behavior_2.getServiceDependencies()[0].getServiceNeeds()
            assert needs_2.getShortName() == "ObdPidNeeds"
            assert isinstance(needs_2, ObdPidServiceNeeds)
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)


class TestObdControlServiceNeeds:
    def test_initialization(self):
        """Test ObdControlServiceNeeds initialization defaults."""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        needs = ObdControlServiceNeeds(ar_root, "TestObdControlServiceNeeds")

        assert needs is not None
        assert needs.getShortName() == "TestObdControlServiceNeeds"
        assert needs.audiences == []
        assert needs.diagRequirement is None
        assert needs.securityAccessLevel is None


class TestObdControlServiceNeedsRoundTrip:
    def test_round_trip_bsw_attributes(self):
        """Test parse -> write -> re-parse preserves ObdControlServiceNeeds (attribute-less, BSW path)."""
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        ar_root = document.createARPackage("AUTOSAR")
        desc = ar_root.createBswModuleDescription("BswMd")
        behavior = desc.createBswInternalBehavior("Beh")
        dependency = BswServiceDependency()
        needs = ObdControlServiceNeeds(dependency, "ObdControlNeeds")
        dependency.setServiceNeeds(needs)
        behavior.addServiceDependency(dependency)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            behavior_2 = document_2.getARPackages()[0].getBswModuleDescriptions()[0].getInternalBehaviors()[0]
            needs_2 = behavior_2.getServiceDependencies()[0].getServiceNeeds()
            assert needs_2.getShortName() == "ObdControlNeeds"
            assert isinstance(needs_2, ObdControlServiceNeeds)
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_round_trip_swc_attributes(self):
        """Test parse -> write -> re-parse preserves ObdControlServiceNeeds (attribute-less, SWC path)."""
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        ar_root = document.createARPackage("AUTOSAR")
        swc = ar_root.createApplicationSwComponentType("Swc")
        behavior = swc.createSwcInternalBehavior("Beh")
        dependency = behavior.createSwcServiceDependency("Dep")
        dependency.createObdControlServiceNeeds("ObdControlNeeds")

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            behavior_2 = document_2.getARPackages()[0].getElement("Swc", ApplicationSwComponentType).getInternalBehavior()
            needs_2 = behavior_2.getSwcServiceDependencies()[0].getObdControlServiceNeeds()[0]
            assert needs_2.getShortName() == "ObdControlNeeds"
            assert isinstance(needs_2, ObdControlServiceNeeds)
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)


class TestDoIpServiceNeeds:
    def test_abstract_initialization(self):
        """Test that DoIpServiceNeeds cannot be instantiated directly"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        with pytest.raises(TypeError):
            DoIpServiceNeeds(ar_root, "TestDoIpServiceNeeds")


class TestObdRatioConnectionKindEnum:
    def test_initialization(self):
        """Test ObdRatioConnectionKindEnum initialization"""
        enum = ObdRatioConnectionKindEnum()
        assert tuple(enum.enumValues) == ("apiUse", "observer")

    def test_values(self):
        """Test enum values"""
        assert ObdRatioConnectionKindEnum.API_USE == "apiUse"
        assert ObdRatioConnectionKindEnum.OBSERVER == "observer"

    def test_get_value(self):
        """Test setValue/getValue round-trip"""
        enum = ObdRatioConnectionKindEnum().setValue(ObdRatioConnectionKindEnum.OBSERVER)
        assert enum.getValue() == "observer"


class TestDiagnosticDenominatorConditionEnum:
    def test_initialization(self):
        """Test DiagnosticDenominatorConditionEnum initialization"""
        enum = DiagnosticDenominatorConditionEnum()
        assert tuple(enum.enumValues) == ("_500miles", "coldstart", "csers", "evap", "evappurgeflow", "individual", "obd")

    def test_values(self):
        """Test enum values"""
        assert DiagnosticDenominatorConditionEnum._500MILES == "_500miles"
        assert DiagnosticDenominatorConditionEnum.COLDSTART == "coldstart"
        assert DiagnosticDenominatorConditionEnum.CSERS == "csers"
        assert DiagnosticDenominatorConditionEnum.EVAP == "evap"
        assert DiagnosticDenominatorConditionEnum.EVAPPURGEFLOW == "evappurgeflow"
        assert DiagnosticDenominatorConditionEnum.INDIVIDUAL == "individual"
        assert DiagnosticDenominatorConditionEnum.OBD == "obd"

    def test_get_value(self):
        """Test setValue/getValue round-trip"""
        enum = DiagnosticDenominatorConditionEnum().setValue(DiagnosticDenominatorConditionEnum.EVAP)
        assert enum.getValue() == "evap"


class TestVerificationStatusIndicationModeEnum:
    def test_initialization(self):
        """Test VerificationStatusIndicationModeEnum initialization"""
        enum = VerificationStatusIndicationModeEnum()
        assert tuple(enum.enumValues) == ("failureAndSuccess", "failureOnly")

    def test_values(self):
        """Test enum values"""
        assert VerificationStatusIndicationModeEnum.FAILURE_AND_SUCCESS == "failureAndSuccess"
        assert VerificationStatusIndicationModeEnum.FAILURE_ONLY == "failureOnly"

    def test_get_value(self):
        """Test setValue/getValue round-trip"""
        enum = VerificationStatusIndicationModeEnum().setValue(VerificationStatusIndicationModeEnum.FAILURE_ONLY)
        assert enum.getValue() == "failureOnly"


class TestObdRatioServiceNeeds:
    def test_initialization(self):
        """Test ObdRatioServiceNeeds initialization"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        needs = ObdRatioServiceNeeds(ar_root, "TestObdRatioServiceNeeds")

        assert needs is not None
        assert needs.getShortName() == "TestObdRatioServiceNeeds"
        assert needs.getConnectionType() is None
        assert needs.getRateBasedMonitoredEventRef() is None
        assert needs.getUsedFidRef() is None

    def test_get_set_connection_type(self):
        """Test getConnectionType/setConnectionType (chaining, round-trip, None no-op)"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        needs = ObdRatioServiceNeeds(ar_root, "TestObdRatioServiceNeeds")

        value = ObdRatioConnectionKindEnum().setValue(ObdRatioConnectionKindEnum.OBSERVER)
        result = needs.setConnectionType(value)
        assert result is needs
        assert needs.getConnectionType() == value

        needs.setConnectionType(None)  # No-op
        assert needs.getConnectionType() == value

    def test_get_set_rate_based_monitored_event_ref(self):
        """Test getRateBasedMonitoredEventRef/setRateBasedMonitoredEventRef (chaining, round-trip, None no-op)"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        needs = ObdRatioServiceNeeds(ar_root, "TestObdRatioServiceNeeds")

        value = RefType().setValue("/Needs/RateBasedMonitoredEvent")
        result = needs.setRateBasedMonitoredEventRef(value)
        assert result is needs
        assert needs.getRateBasedMonitoredEventRef() == value

        needs.setRateBasedMonitoredEventRef(None)  # No-op
        assert needs.getRateBasedMonitoredEventRef() == value

    def test_get_set_used_fid_ref(self):
        """Test getUsedFidRef/setUsedFidRef (chaining, round-trip, None no-op)"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        needs = ObdRatioServiceNeeds(ar_root, "TestObdRatioServiceNeeds")

        value = RefType().setValue("/Needs/UsedFid")
        result = needs.setUsedFidRef(value)
        assert result is needs
        assert needs.getUsedFidRef() == value

        needs.setUsedFidRef(None)  # No-op
        assert needs.getUsedFidRef() == value

    def test_round_trip(self):
        """Test parse -> write -> re-parse preserves ObdRatioServiceNeeds fields."""
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        ar_root = document.createARPackage("AUTOSAR")
        desc = ar_root.createBswModuleDescription("BswMd")
        behavior = desc.createBswInternalBehavior("Beh")
        dependency = BswServiceDependency()
        needs = ObdRatioServiceNeeds(dependency, "RatioNeeds")
        needs.setConnectionType(ObdRatioConnectionKindEnum().setValue(ObdRatioConnectionKindEnum.OBSERVER))
        needs.setRateBasedMonitoredEventRef(RefType().setValue("/Ratio/MonitoredEvent"))
        needs.setUsedFidRef(RefType().setValue("/Ratio/UsedFid"))
        dependency.setServiceNeeds(needs)
        behavior.addServiceDependency(dependency)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            behavior_2 = document_2.getARPackages()[0].getBswModuleDescriptions()[0].getInternalBehaviors()[0]
            needs_2 = behavior_2.getServiceDependencies()[0].getServiceNeeds()
            assert needs_2.getShortName() == "RatioNeeds"
            assert isinstance(needs_2, ObdRatioServiceNeeds)
            assert needs_2.getConnectionType().getValue() == "observer"
            assert needs_2.getRateBasedMonitoredEventRef().getValue() == "/Ratio/MonitoredEvent"
            assert needs_2.getUsedFidRef().getValue() == "/Ratio/UsedFid"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)


class TestObdRatioDenominatorNeeds:
    def test_initialization(self):
        """Test ObdRatioDenominatorNeeds initialization"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        needs = ObdRatioDenominatorNeeds(ar_root, "TestObdRatioDenominatorNeeds")

        assert needs is not None
        assert needs.getShortName() == "TestObdRatioDenominatorNeeds"
        assert needs.getDenominatorCondition() is None

    def test_get_set_denominator_condition(self):
        """Test getDenominatorCondition/setDenominatorCondition (chaining, round-trip, None no-op)"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        needs = ObdRatioDenominatorNeeds(ar_root, "TestObdRatioDenominatorNeeds")

        value = DiagnosticDenominatorConditionEnum().setValue(DiagnosticDenominatorConditionEnum.EVAP)
        result = needs.setDenominatorCondition(value)
        assert result is needs
        assert needs.getDenominatorCondition() == value

        needs.setDenominatorCondition(None)  # No-op
        assert needs.getDenominatorCondition() == value

    def test_round_trip(self):
        """Test parse -> write -> re-parse preserves denominatorCondition."""
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        ar_root = document.createARPackage("AUTOSAR")
        desc = ar_root.createBswModuleDescription("BswMd")
        behavior = desc.createBswInternalBehavior("Beh")
        dependency = BswServiceDependency()
        needs = ObdRatioDenominatorNeeds(dependency, "DenomNeeds")
        needs.setDenominatorCondition(DiagnosticDenominatorConditionEnum().setValue(DiagnosticDenominatorConditionEnum.EVAP))
        dependency.setServiceNeeds(needs)
        behavior.addServiceDependency(dependency)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            behavior_2 = document_2.getARPackages()[0].getBswModuleDescriptions()[0].getInternalBehaviors()[0]
            needs_2 = behavior_2.getServiceDependencies()[0].getServiceNeeds()
            assert needs_2.getShortName() == "DenomNeeds"
            assert isinstance(needs_2, ObdRatioDenominatorNeeds)
            assert needs_2.getDenominatorCondition().getValue() == "evap"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)


class TestDoIpRoutingActivationAuthenticationNeeds:
    def test_initialization(self):
        """Test DoIpRoutingActivationAuthenticationNeeds initialization"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        needs = DoIpRoutingActivationAuthenticationNeeds(ar_root, "TestDoIpRoutingActivationAuthenticationNeeds")

        assert needs is not None
        assert needs.getShortName() == "TestDoIpRoutingActivationAuthenticationNeeds"
        assert needs.getDataLengthRequest() is None
        assert needs.getDataLengthResponse() is None
        assert needs.getRoutingActivationType() is None

    def test_get_set_data_length_request(self):
        """Test getDataLengthRequest/setDataLengthRequest (chaining, round-trip, None no-op)"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        needs = DoIpRoutingActivationAuthenticationNeeds(ar_root, "TestDoIpRoutingActivationAuthenticationNeeds")

        value = PositiveInteger().setValue("4")
        result = needs.setDataLengthRequest(value)
        assert result is needs
        assert needs.getDataLengthRequest() == value

        needs.setDataLengthRequest(None)  # No-op
        assert needs.getDataLengthRequest() == value

    def test_get_set_data_length_response(self):
        """Test getDataLengthResponse/setDataLengthResponse (chaining, round-trip, None no-op)"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        needs = DoIpRoutingActivationAuthenticationNeeds(ar_root, "TestDoIpRoutingActivationAuthenticationNeeds")

        value = PositiveInteger().setValue("8")
        result = needs.setDataLengthResponse(value)
        assert result is needs
        assert needs.getDataLengthResponse() == value

        needs.setDataLengthResponse(None)  # No-op
        assert needs.getDataLengthResponse() == value

    def test_get_set_routing_activation_type(self):
        """Test getRoutingActivationType/setRoutingActivationType (chaining, round-trip, None no-op)"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        needs = DoIpRoutingActivationAuthenticationNeeds(ar_root, "TestDoIpRoutingActivationAuthenticationNeeds")

        value = NameToken().setValue("RA_0xE1")
        result = needs.setRoutingActivationType(value)
        assert result is needs
        assert needs.getRoutingActivationType() == value

        needs.setRoutingActivationType(None)  # No-op
        assert needs.getRoutingActivationType() == value

    def test_round_trip(self):
        """Test parse -> write -> re-parse preserves DoIpRoutingActivationAuthenticationNeeds fields."""
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        ar_root = document.createARPackage("AUTOSAR")
        desc = ar_root.createBswModuleDescription("BswMd")
        behavior = desc.createBswInternalBehavior("Beh")
        dependency = BswServiceDependency()
        needs = DoIpRoutingActivationAuthenticationNeeds(dependency, "AuthNeeds")
        needs.setDataLengthRequest(PositiveInteger().setValue("4"))
        needs.setDataLengthResponse(PositiveInteger().setValue("8"))
        needs.setRoutingActivationType(NameToken().setValue("RA_0xE1"))
        dependency.setServiceNeeds(needs)
        behavior.addServiceDependency(dependency)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            behavior_2 = document_2.getARPackages()[0].getBswModuleDescriptions()[0].getInternalBehaviors()[0]
            needs_2 = behavior_2.getServiceDependencies()[0].getServiceNeeds()
            assert needs_2.getShortName() == "AuthNeeds"
            assert isinstance(needs_2, DoIpRoutingActivationAuthenticationNeeds)
            assert needs_2.getDataLengthRequest().getValue() == 4
            assert needs_2.getDataLengthResponse().getValue() == 8
            assert needs_2.getRoutingActivationType().getValue() == "RA_0xE1"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)


class TestDoIpRoutingActivationConfirmationNeeds:
    def test_initialization(self):
        """Test DoIpRoutingActivationConfirmationNeeds initialization"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        needs = DoIpRoutingActivationConfirmationNeeds(ar_root, "TestDoIpRoutingActivationConfirmationNeeds")

        assert needs is not None
        assert needs.getShortName() == "TestDoIpRoutingActivationConfirmationNeeds"
        assert needs.getDataLengthRequest() is None
        assert needs.getDataLengthResponse() is None
        assert needs.getRoutingActivationType() is None

    def test_get_set_data_length_request(self):
        """Test getDataLengthRequest/setDataLengthRequest (chaining, round-trip, None no-op)"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        needs = DoIpRoutingActivationConfirmationNeeds(ar_root, "TestDoIpRoutingActivationConfirmationNeeds")

        value = PositiveInteger().setValue("4")
        result = needs.setDataLengthRequest(value)
        assert result is needs
        assert needs.getDataLengthRequest() == value

        needs.setDataLengthRequest(None)  # No-op
        assert needs.getDataLengthRequest() == value

    def test_get_set_data_length_response(self):
        """Test getDataLengthResponse/setDataLengthResponse (chaining, round-trip, None no-op)"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        needs = DoIpRoutingActivationConfirmationNeeds(ar_root, "TestDoIpRoutingActivationConfirmationNeeds")

        value = PositiveInteger().setValue("8")
        result = needs.setDataLengthResponse(value)
        assert result is needs
        assert needs.getDataLengthResponse() == value

        needs.setDataLengthResponse(None)  # No-op
        assert needs.getDataLengthResponse() == value

    def test_get_set_routing_activation_type(self):
        """Test getRoutingActivationType/setRoutingActivationType (chaining, round-trip, None no-op)"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        needs = DoIpRoutingActivationConfirmationNeeds(ar_root, "TestDoIpRoutingActivationConfirmationNeeds")

        value = NameToken().setValue("RA_0xE1")
        result = needs.setRoutingActivationType(value)
        assert result is needs
        assert needs.getRoutingActivationType() == value

        needs.setRoutingActivationType(None)  # No-op
        assert needs.getRoutingActivationType() == value

    def test_round_trip(self):
        """Test parse -> write -> re-parse preserves DoIpRoutingActivationConfirmationNeeds fields."""
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        ar_root = document.createARPackage("AUTOSAR")
        desc = ar_root.createBswModuleDescription("BswMd")
        behavior = desc.createBswInternalBehavior("Beh")
        dependency = BswServiceDependency()
        needs = DoIpRoutingActivationConfirmationNeeds(dependency, "ConfNeeds")
        needs.setDataLengthRequest(PositiveInteger().setValue("4"))
        needs.setDataLengthResponse(PositiveInteger().setValue("8"))
        needs.setRoutingActivationType(NameToken().setValue("RA_0xE1"))
        dependency.setServiceNeeds(needs)
        behavior.addServiceDependency(dependency)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            behavior_2 = document_2.getARPackages()[0].getBswModuleDescriptions()[0].getInternalBehaviors()[0]
            needs_2 = behavior_2.getServiceDependencies()[0].getServiceNeeds()
            assert needs_2.getShortName() == "ConfNeeds"
            assert isinstance(needs_2, DoIpRoutingActivationConfirmationNeeds)
            assert needs_2.getDataLengthRequest().getValue() == 4
            assert needs_2.getDataLengthResponse().getValue() == 8
            assert needs_2.getRoutingActivationType().getValue() == "RA_0xE1"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)


class TestSecureOnBoardCommunicationNeeds:
    def test_initialization(self):
        """Test SecureOnBoardCommunicationNeeds initialization"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        needs = SecureOnBoardCommunicationNeeds(ar_root, "TestSecureOnBoardCommunicationNeeds")

        assert needs is not None
        assert needs.getShortName() == "TestSecureOnBoardCommunicationNeeds"
        assert needs.getVerificationStatusIndicationMode() is None

    def test_get_set_verification_status_indication_mode(self):
        """Test getVerificationStatusIndicationMode/setVerificationStatusIndicationMode (chaining, round-trip, None no-op)"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        needs = SecureOnBoardCommunicationNeeds(ar_root, "TestSecureOnBoardCommunicationNeeds")

        value = VerificationStatusIndicationModeEnum().setValue(VerificationStatusIndicationModeEnum.FAILURE_ONLY)
        result = needs.setVerificationStatusIndicationMode(value)
        assert result is needs
        assert needs.getVerificationStatusIndicationMode() == value

        needs.setVerificationStatusIndicationMode(None)  # No-op
        assert needs.getVerificationStatusIndicationMode() == value

    def test_round_trip(self):
        """Test parse -> write -> re-parse preserves verificationStatusIndicationMode."""
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        ar_root = document.createARPackage("AUTOSAR")
        desc = ar_root.createBswModuleDescription("BswMd")
        behavior = desc.createBswInternalBehavior("Beh")
        dependency = BswServiceDependency()
        needs = SecureOnBoardCommunicationNeeds(dependency, "SecOcNeeds")
        needs.setVerificationStatusIndicationMode(VerificationStatusIndicationModeEnum().setValue(VerificationStatusIndicationModeEnum.FAILURE_ONLY))
        dependency.setServiceNeeds(needs)
        behavior.addServiceDependency(dependency)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            behavior_2 = document_2.getARPackages()[0].getBswModuleDescriptions()[0].getInternalBehaviors()[0]
            needs_2 = behavior_2.getServiceDependencies()[0].getServiceNeeds()
            assert needs_2.getShortName() == "SecOcNeeds"
            assert isinstance(needs_2, SecureOnBoardCommunicationNeeds)
            assert needs_2.getVerificationStatusIndicationMode().getValue() == "failureOnly"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)


class TestIdsMgrNeeds:
    def test_initialization(self):
        """Test IdsMgrNeeds initialization"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        needs = IdsMgrNeeds(ar_root, "TestIdsMgrNeeds")

        assert needs is not None
        assert needs.getShortName() == "TestIdsMgrNeeds"
        assert needs.getUseSmartSensorApi() is None

    def test_get_set_use_smart_sensor_api(self):
        """Test getUseSmartSensorApi/setUseSmartSensorApi (chaining, round-trip, None no-op)"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        needs = IdsMgrNeeds(ar_root, "TestIdsMgrNeeds")

        value = Boolean().setValue(True)
        result = needs.setUseSmartSensorApi(value)
        assert result is needs
        assert needs.getUseSmartSensorApi() == value

        needs.setUseSmartSensorApi(None)  # No-op
        assert needs.getUseSmartSensorApi() == value

    def test_round_trip(self):
        """Test parse -> write -> re-parse preserves useSmartSensorApi."""
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        ar_root = document.createARPackage("AUTOSAR")
        desc = ar_root.createBswModuleDescription("BswMd")
        behavior = desc.createBswInternalBehavior("Beh")
        dependency = BswServiceDependency()
        needs = IdsMgrNeeds(dependency, "IdsNeeds")
        needs.setUseSmartSensorApi(Boolean().setValue(True))
        dependency.setServiceNeeds(needs)
        behavior.addServiceDependency(dependency)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            behavior_2 = document_2.getARPackages()[0].getBswModuleDescriptions()[0].getInternalBehaviors()[0]
            needs_2 = behavior_2.getServiceDependencies()[0].getServiceNeeds()
            assert needs_2.getShortName() == "IdsNeeds"
            assert isinstance(needs_2, IdsMgrNeeds)
            assert needs_2.getUseSmartSensorApi().getValue() is True
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)


class TestNewServiceNeedsSwcRoundTrip:
    """Round-trip the newly synced ServiceNeeds classes through the SWC aggregator."""

    def _round_trip(self, needs):
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        ar_root = document.createARPackage("AUTOSAR")
        swc = ar_root.createApplicationSwComponentType("Swc")
        behavior = swc.createSwcInternalBehavior("Beh")
        dependency = behavior.createSwcServiceDependency("Dep")
        if isinstance(needs, ObdRatioServiceNeeds):
            dependency.createObdRatioServiceNeeds(needs.getShortName())
        elif isinstance(needs, ObdRatioDenominatorNeeds):
            dependency.createObdRatioDenominatorNeeds(needs.getShortName())
        elif isinstance(needs, DoIpRoutingActivationAuthenticationNeeds):
            dependency.createDoIpRoutingActivationAuthenticationNeeds(needs.getShortName())
        elif isinstance(needs, DoIpRoutingActivationConfirmationNeeds):
            dependency.createDoIpRoutingActivationConfirmationNeeds(needs.getShortName())
        elif isinstance(needs, SecureOnBoardCommunicationNeeds):
            dependency.createSecureOnBoardCommunicationNeeds(needs.getShortName())
        elif isinstance(needs, IdsMgrNeeds):
            dependency.createIdsMgrNeeds(needs.getShortName())

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            behavior_2 = document_2.getARPackages()[0].getElement("Swc", ApplicationSwComponentType).getInternalBehavior()
            needs_2 = behavior_2.getSwcServiceDependencies()[0].getServiceNeeds()[0]
            return needs_2
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_round_trip_swc_obd_ratio_service(self):
        needs_2 = self._round_trip(ObdRatioServiceNeeds(None, "RatioSwcNeeds"))
        assert isinstance(needs_2, ObdRatioServiceNeeds)
        assert needs_2.getShortName() == "RatioSwcNeeds"

    def test_round_trip_swc_obd_ratio_denominator(self):
        needs_2 = self._round_trip(ObdRatioDenominatorNeeds(None, "DenomSwcNeeds"))
        assert isinstance(needs_2, ObdRatioDenominatorNeeds)
        assert needs_2.getShortName() == "DenomSwcNeeds"

    def test_round_trip_swc_doip_auth(self):
        needs_2 = self._round_trip(DoIpRoutingActivationAuthenticationNeeds(None, "AuthSwcNeeds"))
        assert isinstance(needs_2, DoIpRoutingActivationAuthenticationNeeds)
        assert needs_2.getShortName() == "AuthSwcNeeds"

    def test_round_trip_swc_doip_conf(self):
        needs_2 = self._round_trip(DoIpRoutingActivationConfirmationNeeds(None, "ConfSwcNeeds"))
        assert isinstance(needs_2, DoIpRoutingActivationConfirmationNeeds)
        assert needs_2.getShortName() == "ConfSwcNeeds"

    def test_round_trip_swc_secure_on_board(self):
        needs_2 = self._round_trip(SecureOnBoardCommunicationNeeds(None, "SecOcSwcNeeds"))
        assert isinstance(needs_2, SecureOnBoardCommunicationNeeds)
        assert needs_2.getShortName() == "SecOcSwcNeeds"

    def test_round_trip_swc_ids_mgr(self):
        needs_2 = self._round_trip(IdsMgrNeeds(None, "IdsSwcNeeds"))
        assert isinstance(needs_2, IdsMgrNeeds)
        assert needs_2.getShortName() == "IdsSwcNeeds"

"""
This module contains comprehensive tests for the ServiceMapping module in SWComponentTemplate.SwcInternalBehavior.
Tests cover all classes and methods in the ServiceMapping.py file to achieve 100% test coverage.
"""

import os
import tempfile
import typing

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    DiagnosticIndicatorTypeEnum,
    EventAcceptanceStatusEnum,
    OperationCycleTypeEnum,
    StorageConditionStatusEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Identifier, RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ServiceMapping import RoleBasedDataTypeAssignment, RoleBasedPortAssignment, SwcServiceDependency
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


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


CLASS_NOTE = (
    "This class specifies an assignment of a role to a particular service port (RPortPrototype or PPortPrototype) of an AtomicSwComponentType. "  # noqa E501
    "With this assignment, the role of the service port can be mapped to a specific ServiceNeeds element, so that a tool is able to create the correct connector."  # noqa E501
)

PORT_PROTOTYPE_NOTE = (
    "Service PortPrototype used in the assigned role. "  # noqa E501
    "This PortPrototype shall either belong to the same AtomicSwComponentType as the SwcInternalBehavior which owns the ServiceDependency "  # noqa E501
    "or to the same NvBlockSwComponentType as the NvBlockDescriptor."  # noqa E501
)

ROLE_NOTE = (
    "This is the role of the assigned Port in the given context. "  # noqa E501
    "The value shall be a shortName of the Blueprint of a PortInterface as standardized in the Software Specification of the related AUTOSAR Service."  # noqa E501
)


class TestRoleBasedPortAssignment:
    def test_spec_notes_are_verbatim(self):
        """Test that the class docstring and every accessor docstring is the spec Note verbatim (Table 7.54)"""
        assert RoleBasedPortAssignment.__doc__.strip() == CLASS_NOTE
        assert RoleBasedPortAssignment.getPortPrototypeRef.__doc__.strip() == PORT_PROTOTYPE_NOTE
        assert RoleBasedPortAssignment.setPortPrototypeRef.__doc__.strip() == (PORT_PROTOTYPE_NOTE + " A None value is a no-op and does not overwrite an existing portPrototypeRef.")
        assert RoleBasedPortAssignment.getRole.__doc__.strip() == ROLE_NOTE
        assert RoleBasedPortAssignment.setRole.__doc__.strip() == (ROLE_NOTE + " A None value is a no-op and does not overwrite an existing role.")

    def test_base_shape(self):
        """Test the base chain, no-arg __init__ and typed accessor signatures"""
        assert issubclass(RoleBasedPortAssignment, ARObject)
        assert issubclass(RoleBasedPortAssignment, VariationPointCapable)
        assignment = RoleBasedPortAssignment()
        assert assignment.portPrototypeRef is None
        assert assignment.role is None

        hints = typing.get_type_hints(RoleBasedPortAssignment.getPortPrototypeRef)
        assert hints["return"] == typing.Optional[RefType]
        hints = typing.get_type_hints(RoleBasedPortAssignment.setPortPrototypeRef)
        assert hints["value"] == typing.Optional[RefType]
        assert hints["return"] is RoleBasedPortAssignment
        hints = typing.get_type_hints(RoleBasedPortAssignment.getRole)
        assert hints["return"] == typing.Optional[Identifier]
        hints = typing.get_type_hints(RoleBasedPortAssignment.setRole)
        assert hints["value"] == typing.Optional[Identifier]
        assert hints["return"] is RoleBasedPortAssignment

    def test_initialization(self):
        """Test RoleBasedPortAssignment initialization"""
        assignment = RoleBasedPortAssignment()

        assert assignment is not None
        assert assignment.portPrototypeRef is None
        assert assignment.role is None

    def test_get_set_port_prototype_ref(self):
        """Test getPortPrototypeRef and setPortPrototypeRef methods"""
        assignment = RoleBasedPortAssignment()

        assert assignment.getPortPrototypeRef() is None
        port_ref = RefType()
        port_ref.setValue("/Swc/PortPrototype")
        assert assignment.setPortPrototypeRef(port_ref) is assignment
        assert assignment.getPortPrototypeRef() is port_ref
        assert isinstance(assignment.getPortPrototypeRef(), RefType)
        assert assignment.getPortPrototypeRef().getValue() == "/Swc/PortPrototype"
        assignment.setPortPrototypeRef(None)
        assert assignment.getPortPrototypeRef() is port_ref

    def test_get_set_role(self):
        """Test getRole and setRole methods"""
        assignment = RoleBasedPortAssignment()

        assert assignment.getRole() is None
        role = Identifier()
        role.setValue("NvMService")
        assert assignment.setRole(role) is assignment
        assert assignment.getRole() is role
        assert isinstance(assignment.getRole(), Identifier)
        assert assignment.getRole().getValue() == "NvMService"
        assignment.setRole(None)
        assert assignment.getRole() is role


class TestSwcServiceDependency:
    """Test class for SwcServiceDependency class (Table 7.56)."""

    def test_swc_service_dependency_initialization(self):
        """Test SwcServiceDependency initialization and field defaults."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        service_dep = SwcServiceDependency(ar_root, "TestSwcServiceDependency")

        assert service_dep.parent == ar_root
        assert service_dep.short_name == "TestSwcServiceDependency"
        assert service_dep.assignedData == []
        assert service_dep.assignedPort == []
        assert service_dep.representedPortGroupRef is None
        assert service_dep.serviceNeeds is None

    def test_base_shape(self):
        """Base arbitration: most-derived modeled classes of the two spec Base chains; no VP capability."""
        from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import ServiceDependency
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpStructureElement

        assert issubclass(SwcServiceDependency, AtpStructureElement)
        assert issubclass(SwcServiceDependency, ServiceDependency)
        assert issubclass(SwcServiceDependency, ARObject)
        assert not issubclass(SwcServiceDependency, VariationPointCapable)
        names = [cls.__name__ for cls in SwcServiceDependency.__mro__]
        assert "Identifiable" in names
        assert names.index("ServiceDependency") < names.index("ARObject")

    def test_add_assigned_data(self):
        """AddAssignedData: appending, chaining return, None no-op."""
        from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import RoleBasedDataAssignment

        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        service_dep = SwcServiceDependency(ar_root, "Dep")

        assert service_dep.getAssignedData() == []
        data_assignment = RoleBasedDataAssignment()
        assert service_dep.AddAssignedData(data_assignment) is service_dep
        assert service_dep.getAssignedData() == [data_assignment]

        service_dep.AddAssignedData(None)
        assert service_dep.getAssignedData() == [data_assignment]

    def test_add_assigned_port(self):
        """AddAssignedPort: appending, chaining return, None no-op."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        service_dep = SwcServiceDependency(ar_root, "Dep")

        assert service_dep.getAssignedPorts() == []
        port_assignment = RoleBasedPortAssignment()
        assert service_dep.AddAssignedPort(port_assignment) is service_dep
        assert service_dep.getAssignedPorts() == [port_assignment]

        service_dep.AddAssignedPort(None)
        assert service_dep.getAssignedPorts() == [port_assignment]

    def test_create_needs_factories_and_type_getters(self):
        """Every concrete ServiceNeeds subtype factory: create -> typed getter -> duplicate returns existing."""
        from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
            ComMgrUserNeeds,
            CryptoKeyManagementNeeds,
            CryptoServiceJobNeeds,
            CryptoServiceNeeds,
            DiagnosticCommunicationManagerNeeds,
            DiagnosticComponentNeeds,
            DiagnosticControlNeeds,
            DiagnosticEnableConditionNeeds,
            DiagnosticEventInfoNeeds,
            DiagnosticEventManagerNeeds,
            DiagnosticEventNeeds,
            DiagnosticIoControlNeeds,
            DiagnosticOperationCycleNeeds,
            DiagnosticRequestFileTransferNeeds,
            DiagnosticRoutineNeeds,
            DiagnosticsCommunicationSecurityNeeds,
            DiagnosticStorageConditionNeeds,
            DiagnosticUploadDownloadNeeds,
            DiagnosticValueNeeds,
            DltUserNeeds,
            DoIpActivationLineNeeds,
            DoIpGidNeeds,
            DoIpGidSynchronizationNeeds,
            DoIpPowerModeStatusNeeds,
            DoIpRoutingActivationAuthenticationNeeds,
            DoIpRoutingActivationConfirmationNeeds,
            DtcStatusChangeNotificationNeeds,
            EcuStateMgrUserNeeds,
            ErrorTracerNeeds,
            FunctionInhibitionAvailabilityNeeds,
            FunctionInhibitionNeeds,
            FurtherActionByteNeeds,
            GlobalSupervisionNeeds,
            HardwareTestNeeds,
            IdsMgrCustomTimestampNeeds,
            IdsMgrNeeds,
            IndicatorStatusNeeds,
            J1939DcmDm19Support,
            J1939RmIncomingRequestServiceNeeds,
            J1939RmOutgoingRequestServiceNeeds,
            NvBlockNeeds,
            ObdControlServiceNeeds,
            ObdInfoServiceNeeds,
            ObdMonitorServiceNeeds,
            ObdPidServiceNeeds,
            ObdRatioDenominatorNeeds,
            ObdRatioServiceNeeds,
            SecureOnBoardCommunicationNeeds,
            ServiceNeeds,
            SupervisedEntityCheckpointNeeds,
            SyncTimeBaseMgrUserNeeds,
            V2xDataManagerNeeds,
            V2xFacUserNeeds,
            V2xMUserNeeds,
            VendorSpecificServiceNeeds,
            WarningIndicatorRequestedBitNeeds,
        )

        factory_getter_type = [
            ("createNvBlockNeeds", "getNvBlockNeeds", NvBlockNeeds),
            ("createDiagnosticCommunicationManagerNeeds", "getDiagnosticCommunicationManagerNeeds", DiagnosticCommunicationManagerNeeds),
            ("createDiagnosticComponentNeeds", None, DiagnosticComponentNeeds),
            ("createDiagnosticControlNeeds", None, DiagnosticControlNeeds),
            ("createDiagnosticUploadDownloadNeeds", None, DiagnosticUploadDownloadNeeds),
            ("createDiagnosticsCommunicationSecurityNeeds", None, DiagnosticsCommunicationSecurityNeeds),
            ("createDiagnosticRoutineNeeds", "getDiagnosticRoutineNeeds", DiagnosticRoutineNeeds),
            ("createDiagnosticValueNeeds", "getDiagnosticValueNeeds", DiagnosticValueNeeds),
            ("createDiagnosticEventNeeds", "getDiagnosticEventNeeds", DiagnosticEventNeeds),
            ("createDiagnosticEventInfoNeeds", "getDiagnosticEventInfoNeeds", DiagnosticEventInfoNeeds),
            ("createCryptoKeyManagementNeeds", None, CryptoKeyManagementNeeds),
            ("createCryptoServiceJobNeeds", None, CryptoServiceJobNeeds),
            ("createCryptoServiceNeeds", "getCryptoServiceNeeds", CryptoServiceNeeds),
            ("createEcuStateMgrUserNeeds", "getEcuStateMgrUserNeeds", EcuStateMgrUserNeeds),
            ("createDtcStatusChangeNotificationNeeds", "getDtcStatusChangeNotificationNeeds", DtcStatusChangeNotificationNeeds),
            ("createDiagnosticIoControlNeeds", "getDiagnosticIoControlNeeds", DiagnosticIoControlNeeds),
            ("createDiagnosticEnableConditionNeeds", None, DiagnosticEnableConditionNeeds),
            ("createDiagnosticEventManagerNeeds", None, DiagnosticEventManagerNeeds),
            ("createDiagnosticOperationCycleNeeds", None, DiagnosticOperationCycleNeeds),
            ("createDiagnosticRequestFileTransferNeeds", None, DiagnosticRequestFileTransferNeeds),
            ("createDiagnosticStorageConditionNeeds", None, DiagnosticStorageConditionNeeds),
            ("createFunctionInhibitionAvailabilityNeeds", None, FunctionInhibitionAvailabilityNeeds),
            ("createFunctionInhibitionNeeds", None, FunctionInhibitionNeeds),
            ("createFurtherActionByteNeeds", None, FurtherActionByteNeeds),
            ("createGlobalSupervisionNeeds", None, GlobalSupervisionNeeds),
            ("createHardwareTestNeeds", None, HardwareTestNeeds),
            ("createIdsMgrCustomTimestampNeeds", None, IdsMgrCustomTimestampNeeds),
            ("createIndicatorStatusNeeds", None, IndicatorStatusNeeds),
            ("createJ1939DcmDm19Support", None, J1939DcmDm19Support),
            ("createJ1939RmIncomingRequestServiceNeeds", None, J1939RmIncomingRequestServiceNeeds),
            ("createJ1939RmOutgoingRequestServiceNeeds", None, J1939RmOutgoingRequestServiceNeeds),
            ("createDltUserNeeds", "getDltUserNeeds", DltUserNeeds),
            ("createComMgrUserNeeds", "getComMgrUserNeeds", ComMgrUserNeeds),
            ("createErrorTracerNeeds", "getErrorTracerNeeds", ErrorTracerNeeds),
            ("createObdInfoServiceNeeds", "getObdInfoServiceNeeds", ObdInfoServiceNeeds),
            ("createObdMonitorServiceNeeds", "getObdMonitorServiceNeeds", ObdMonitorServiceNeeds),
            ("createObdPidServiceNeeds", "getObdPidServiceNeeds", ObdPidServiceNeeds),
            ("createObdControlServiceNeeds", "getObdControlServiceNeeds", ObdControlServiceNeeds),
            ("createObdRatioServiceNeeds", None, ObdRatioServiceNeeds),
            ("createObdRatioDenominatorNeeds", None, ObdRatioDenominatorNeeds),
            ("createDoIpActivationLineNeeds", None, DoIpActivationLineNeeds),
            ("createDoIpGidNeeds", None, DoIpGidNeeds),
            ("createDoIpGidSynchronizationNeeds", None, DoIpGidSynchronizationNeeds),
            ("createDoIpPowerModeStatusNeeds", None, DoIpPowerModeStatusNeeds),
            ("createDoIpRoutingActivationAuthenticationNeeds", None, DoIpRoutingActivationAuthenticationNeeds),
            ("createDoIpRoutingActivationConfirmationNeeds", None, DoIpRoutingActivationConfirmationNeeds),
            ("createSecureOnBoardCommunicationNeeds", None, SecureOnBoardCommunicationNeeds),
            ("createSupervisedEntityCheckpointNeeds", None, SupervisedEntityCheckpointNeeds),
            ("createSyncTimeBaseMgrUserNeeds", None, SyncTimeBaseMgrUserNeeds),
            ("createV2xDataManagerNeeds", None, V2xDataManagerNeeds),
            ("createV2xFacUserNeeds", None, V2xFacUserNeeds),
            ("createV2xMUserNeeds", None, V2xMUserNeeds),
            ("createVendorSpecificServiceNeeds", None, VendorSpecificServiceNeeds),
            ("createWarningIndicatorRequestedBitNeeds", None, WarningIndicatorRequestedBitNeeds),
            ("createIdsMgrNeeds", None, IdsMgrNeeds),
        ]

        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        service_dep = SwcServiceDependency(ar_root, "Dep")

        first_needs = None
        last_needs = None
        for index, (factory, getter, needs_type) in enumerate(factory_getter_type):
            needs = getattr(service_dep, factory)("Needs%d" % index)
            assert isinstance(needs, needs_type)
            assert isinstance(needs, ServiceNeeds)
            assert needs.short_name == "Needs%d" % index
            assert needs.parent is service_dep
            if getter is not None:
                assert needs in getattr(service_dep, getter)()
            if index == 0:
                first_needs = needs
            last_needs = needs

        duplicate = service_dep.createNvBlockNeeds("Needs0")
        assert duplicate is first_needs
        assert service_dep.getServiceNeeds() is last_needs

    def test_service_needs_single_slot(self):
        """serviceNeeds is a 0..1 aggr: getServiceNeeds returns the field (Optional), last create wins."""
        from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import ServiceNeeds

        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        service_dep = SwcServiceDependency(ar_root, "Dep")

        assert service_dep.getServiceNeeds() is None

        nv = service_dep.createNvBlockNeeds("Nv")
        assert service_dep.getServiceNeeds() is nv
        dlt = service_dep.createDltUserNeeds("Dlt")
        assert service_dep.getServiceNeeds() is dlt

        hints = typing.get_type_hints(SwcServiceDependency.getServiceNeeds)
        assert hints["return"] == typing.Optional[ServiceNeeds]

    def test_get_set_represented_port_group(self):
        """Test representedPortGroup getter/setter round-trip with None no-op."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        service_dep = SwcServiceDependency(ar_root, "TestSwcServiceDependency")

        assert service_dep.getRepresentedPortGroupRef() is None

        port_group_ref = RefType()
        port_group_ref.setValue("/PortGroup/Ref")
        assert service_dep.setRepresentedPortGroupRef(port_group_ref) is service_dep
        assert service_dep.getRepresentedPortGroupRef().getValue() == "/PortGroup/Ref"

        # None is a no-op and must not overwrite an existing value
        service_dep.setRepresentedPortGroupRef(None)
        assert service_dep.getRepresentedPortGroupRef().getValue() == "/PortGroup/Ref"


class TestSwcServiceDependencyRoundTrip:
    """Test full parse -> write -> re-parse for ServiceNeeds via the SWC route (one needs per dependency, spec 0..1)."""

    def test_swc_service_needs_round_trip(self):
        """Verify representative needs survive an SWC round-trip (one ServiceNeeds per SwcServiceDependency)."""
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        ar_root = document.createARPackage("AUTOSAR")
        swc = ar_root.createApplicationSwComponentType("MySwc")
        behavior = swc.createSwcInternalBehavior("Beh")

        enable_dep = behavior.createSwcServiceDependency("EnableDep")
        enable = enable_dep.createDiagnosticEnableConditionNeeds("EnableNeeds")
        enable.setInitialStatus(EventAcceptanceStatusEnum().setValue(EventAcceptanceStatusEnum.EVENT_ACCEPTANCE_ENABLED))

        cycle_dep = behavior.createSwcServiceDependency("CycleDep")
        cycle = cycle_dep.createDiagnosticOperationCycleNeeds("CycleNeeds")
        cycle.setOperationCycle(OperationCycleTypeEnum().setValue(OperationCycleTypeEnum.WARMUP))

        storage_dep = behavior.createSwcServiceDependency("StorageDep")
        storage = storage_dep.createDiagnosticStorageConditionNeeds("StorageNeeds")
        storage.setInitialStatus(StorageConditionStatusEnum().setValue(StorageConditionStatusEnum.EVENT_STORAGE_ENABLE))

        indicator_dep = behavior.createSwcServiceDependency("IndicatorDep")
        indicator = indicator_dep.createIndicatorStatusNeeds("IndicatorNeeds")
        indicator.setType(DiagnosticIndicatorTypeEnum().setValue(DiagnosticIndicatorTypeEnum.MALFUNCTION))

        fim_dep = behavior.createSwcServiceDependency("FimDep")
        fim = fim_dep.createFunctionInhibitionAvailabilityNeeds("FimNeeds")
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
            deps_2 = {d.short_name: d for d in behavior_2.getSwcServiceDependencies()}

            enable_2 = deps_2["EnableDep"].getServiceNeeds()
            assert enable_2.getShortName() == "EnableNeeds"
            assert enable_2.getInitialStatus().getValue() == EventAcceptanceStatusEnum.EVENT_ACCEPTANCE_ENABLED

            cycle_2 = deps_2["CycleDep"].getServiceNeeds()
            assert cycle_2.getShortName() == "CycleNeeds"
            assert cycle_2.getOperationCycle().getValue() == "WARMUP"

            storage_2 = deps_2["StorageDep"].getServiceNeeds()
            assert storage_2.getShortName() == "StorageNeeds"
            assert storage_2.getInitialStatus().getValue() == StorageConditionStatusEnum.EVENT_STORAGE_ENABLE

            indicator_2 = deps_2["IndicatorDep"].getServiceNeeds()
            assert indicator_2.getShortName() == "IndicatorNeeds"
            assert indicator_2.getType().getValue() == DiagnosticIndicatorTypeEnum.MALFUNCTION

            fim_2 = deps_2["FimDep"].getServiceNeeds()
            assert fim_2.getShortName() == "FimNeeds"
            assert fim_2.getControlledFidRef().getValue() == "/Fim/Ref"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_swc_service_dependency_assigned_data_and_ports_round_trip(self):
        """Verify assignedData/assignedPort (the * aggrs) survive an SWC round-trip with field values."""
        from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import RoleBasedDataAssignment

        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        ar_root = document.createARPackage("AUTOSAR")
        swc = ar_root.createApplicationSwComponentType("MySwc")
        behavior = swc.createSwcInternalBehavior("Beh")
        dependency = behavior.createSwcServiceDependency("Dep")

        data_assignment = RoleBasedDataAssignment()
        data_ref = RefType()
        data_ref.setValue("/Data/Ref")
        role = Identifier()
        role.setValue("ramBlock")
        data_assignment.setRole(role)
        dependency.AddAssignedData(data_assignment)

        port_assignment = RoleBasedPortAssignment()
        port_ref = RefType()
        port_ref.setValue("/Port/Ref")
        port_role = Identifier()
        port_role.setValue("NvMService")
        port_assignment.setPortPrototypeRef(port_ref)
        port_assignment.setRole(port_role)
        dependency.AddAssignedPort(port_assignment)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)

            swc_2 = document_2.getARPackages()[0].getSwComponentTypes()[0]
            behavior_2 = swc_2.getInternalBehavior()
            dependency_2 = behavior_2.getSwcServiceDependencies()[0]

            assert len(dependency_2.getAssignedData()) == 1
            assert dependency_2.getAssignedData()[0].getRole().getValue() == "ramBlock"
            assert len(dependency_2.getAssignedPorts()) == 1
            assert dependency_2.getAssignedPorts()[0].getPortPrototypeRef().getValue() == "/Port/Ref"
            assert dependency_2.getAssignedPorts()[0].getRole().getValue() == "NvMService"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_swc_service_dependency_represented_port_group_round_trip(self):
        """Verify representedPortGroup (REPRESENTED-PORT-GROUP-REF) survives an SWC round-trip."""
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        ar_root = document.createARPackage("AUTOSAR")
        swc = ar_root.createApplicationSwComponentType("MySwc")
        behavior = swc.createSwcInternalBehavior("Beh")
        dependency = behavior.createSwcServiceDependency("Dep")

        port_group_ref = RefType()
        port_group_ref.setValue("/PortGroup/Ref")
        dependency.setRepresentedPortGroupRef(port_group_ref)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)

            swc_2 = document_2.getARPackages()[0].getSwComponentTypes()[0]
            behavior_2 = swc_2.getInternalBehavior()
            dependency_2 = behavior_2.getSwcServiceDependencies()[0]
            assert dependency_2.getRepresentedPortGroupRef().getValue() == "/PortGroup/Ref"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

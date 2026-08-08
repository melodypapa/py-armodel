from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport import RoleBasedMcDataAssignment
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptSupport import (
    RptAccessEnum,
    RptComponent,
    RptEnablerImplTypeEnum,
    RptExecutableEntity,
    RptExecutableEntityEvent,
    RptExecutionContext,
    RptExecutionControlEnum,
    RptPreparationEnum,
    RptServicePoint,
    RptSupportData,
    RptSwPrototypingAccess,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import CIdentifier, Identifier, PositiveInteger, RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.RPTScenario import RptExecutableEntityProperties, RptImplPolicy, RptServicePointEnum


class TestRptSupportDataInitialization:
    def test_initialization(self):
        """Test RptSupportData initialization defaults"""
        support_data = RptSupportData()
        assert support_data is not None
        assert support_data.executionContexts == []
        assert support_data.rptComponents == []
        assert support_data.rptServicePoints == []


class TestRptSupportDataChildren:
    def test_create_execution_context(self):
        """Test createExecutionContext creates and appends an execution context"""
        support_data = RptSupportData()
        context = support_data.createExecutionContext("TaskA")
        assert context is not None
        assert context.getShortName() == "TaskA"
        assert support_data.getExecutionContexts() == [context]

    def test_create_execution_context_duplicate(self):
        """Test createExecutionContext returns the existing context for a duplicate short name"""
        support_data = RptSupportData()
        context_1 = support_data.createExecutionContext("TaskA")
        context_2 = support_data.createExecutionContext("TaskA")
        assert context_1 is context_2
        assert len(support_data.getExecutionContexts()) == 1

    def test_create_rpt_component(self):
        """Test createRptComponent creates and appends a component"""
        support_data = RptSupportData()
        component = support_data.createRptComponent("Comp1")
        assert component is not None
        assert component.getShortName() == "Comp1"
        assert support_data.getRptComponents() == [component]

    def test_create_rpt_service_point(self):
        """Test createRptServicePoint creates and appends a service point"""
        support_data = RptSupportData()
        service_point = support_data.createRptServicePoint("SP1")
        assert service_point is not None
        assert service_point.getShortName() == "SP1"
        assert support_data.getRptServicePoints() == [service_point]


class TestRptComponent:
    def test_mc_data_assignment_add_get(self):
        """Test addMcDataAssignment appends and returns self"""
        component = RptComponent(AUTOSAR.getInstance(), "Comp1")
        assignment = RoleBasedMcDataAssignment()
        result = component.addMcDataAssignment(assignment)
        assert result is component
        assert component.getMcDataAssignments() == [assignment]

    def test_rp_impl_policy_setter_getter(self):
        """Test rpImplPolicy setter and getter"""
        component = RptComponent(AUTOSAR.getInstance(), "Comp1")
        policy = RptImplPolicy()
        result = component.setRpImplPolicy(policy)
        assert result is component
        assert component.getRpImplPolicy() == policy

    def test_create_rpt_executable_entity(self):
        """Test createRptExecutableEntity creates and appends an executable entity"""
        component = RptComponent(AUTOSAR.getInstance(), "Comp1")
        entity = component.createRptExecutableEntity("Run1")
        assert entity.getShortName() == "Run1"
        assert component.getRptExecutableEntities() == [entity]


class TestRptExecutableEntity:
    def test_create_rpt_executable_entity_event(self):
        """Test createRptExecutableEntityEvent creates and appends an event"""
        entity = RptExecutableEntity(AUTOSAR.getInstance(), "Run1")
        event = entity.createRptExecutableEntityEvent("TimingEvent1")
        assert event.getShortName() == "TimingEvent1"
        assert entity.getRptExecutableEntityEvents() == [event]

    def test_rpt_read_add_get(self):
        """Test addRptRead appends and returns self"""
        entity = RptExecutableEntity(AUTOSAR.getInstance(), "Run1")
        assignment = RoleBasedMcDataAssignment()
        result = entity.addRptRead(assignment)
        assert result is entity
        assert entity.getRptReads() == [assignment]

    def test_rpt_write_add_get(self):
        """Test addRptWrite appends and returns self"""
        entity = RptExecutableEntity(AUTOSAR.getInstance(), "Run1")
        assignment = RoleBasedMcDataAssignment()
        result = entity.addRptWrite(assignment)
        assert result is entity
        assert entity.getRptWrites() == [assignment]

    def test_symbol_setter_getter(self):
        """Test symbol setter and getter"""
        entity = RptExecutableEntity(AUTOSAR.getInstance(), "Run1")
        symbol = CIdentifier().setValue("Run1_func")
        result = entity.setSymbol(symbol)
        assert result is entity
        assert entity.getSymbol() == symbol


class TestRptExecutableEntityEvent:
    def test_execution_context_ref_add_get(self):
        """Test addExecutionContextRef appends and returns self"""
        event = RptExecutableEntityEvent(AUTOSAR.getInstance(), "TimingEvent1")
        ref = RefType()
        ref.setValue("/ctx")
        result = event.addExecutionContextRef(ref)
        assert result is event
        assert event.getExecutionContextRefs() == [ref]

    def test_mc_data_assignment_add_get(self):
        """Test addMcDataAssignment appends and returns self"""
        event = RptExecutableEntityEvent(AUTOSAR.getInstance(), "TimingEvent1")
        assignment = RoleBasedMcDataAssignment()
        result = event.addMcDataAssignment(assignment)
        assert result is event
        assert event.getMcDataAssignments() == [assignment]

    def test_rpt_event_id_setter_getter(self):
        """Test rptEventId setter and getter"""
        event = RptExecutableEntityEvent(AUTOSAR.getInstance(), "TimingEvent1")
        event_id = PositiveInteger().setValue("10")
        result = event.setRptEventId(event_id)
        assert result is event
        assert event.getRptEventId() == event_id

    def test_rpt_executable_entity_properties_setter_getter(self):
        """Test rptExecutableEntityProperties setter and getter"""
        event = RptExecutableEntityEvent(AUTOSAR.getInstance(), "TimingEvent1")
        properties = RptExecutableEntityProperties()
        result = event.setRptExecutableEntityProperties(properties)
        assert result is event
        assert event.getRptExecutableEntityProperties() == properties

    def test_rpt_impl_policy_setter_getter(self):
        """Test rptImplPolicy setter and getter"""
        event = RptExecutableEntityEvent(AUTOSAR.getInstance(), "TimingEvent1")
        policy = RptImplPolicy()
        result = event.setRptImplPolicy(policy)
        assert result is event
        assert event.getRptImplPolicy() == policy

    def test_rpt_service_point_post_ref_add_get(self):
        """Test addRptServicePointPostRef appends and returns self"""
        event = RptExecutableEntityEvent(AUTOSAR.getInstance(), "TimingEvent1")
        ref = RefType()
        ref.setValue("/sp/post")
        result = event.addRptServicePointPostRef(ref)
        assert result is event
        assert event.getRptServicePointPostRefs() == [ref]

    def test_rpt_service_point_pre_ref_add_get(self):
        """Test addRptServicePointPreRef appends and returns self"""
        event = RptExecutableEntityEvent(AUTOSAR.getInstance(), "TimingEvent1")
        ref = RefType()
        ref.setValue("/sp/pre")
        result = event.addRptServicePointPreRef(ref)
        assert result is event
        assert event.getRptServicePointPreRefs() == [ref]


class TestRptServicePoint:
    def test_initialization(self):
        """Test RptServicePoint initialization defaults"""
        service_point = RptServicePoint(AUTOSAR.getInstance(), "SP1")
        assert service_point.getShortName() == "SP1"
        assert service_point.serviceId is None
        assert service_point.symbol is None

    def test_service_id_setter_getter(self):
        """Test serviceId setter and getter"""
        service_point = RptServicePoint(AUTOSAR.getInstance(), "SP1")
        service_id = PositiveInteger().setValue("5")
        result = service_point.setServiceId(service_id)
        assert result is service_point
        assert service_point.getServiceId() == service_id

    def test_service_id_none_is_noop(self):
        """Test setting None serviceId is a no-op"""
        service_point = RptServicePoint(AUTOSAR.getInstance(), "SP1")
        service_id = PositiveInteger().setValue("5")
        service_point.setServiceId(service_id)
        service_point.setServiceId(None)
        assert service_point.getServiceId() == service_id


class TestRptSwPrototypingAccess:
    def test_initialization(self):
        """Test RptSwPrototypingAccess initialization defaults"""
        access = RptSwPrototypingAccess()
        assert access is not None
        assert access.rptHookAccess is None
        assert access.rptReadAccess is None
        assert access.rptWriteAccess is None

    def test_rpt_read_access_setter_getter(self):
        """Test rptReadAccess setter and getter"""
        access = RptSwPrototypingAccess()
        test_value = RptAccessEnum().setValue(RptAccessEnum.ENABLED)
        result = access.setRptReadAccess(test_value)
        assert result is access
        assert access.getRptReadAccess() == test_value

    def test_rpt_hook_access_setter_getter(self):
        """Test rptHookAccess setter and getter"""
        access = RptSwPrototypingAccess()
        test_value = RptAccessEnum().setValue(RptAccessEnum.PROTECTED)
        result = access.setRptHookAccess(test_value)
        assert result is access
        assert access.getRptHookAccess() == test_value

    def test_rpt_write_access_none_is_noop(self):
        """Test setting None rptWriteAccess is a no-op"""
        access = RptSwPrototypingAccess()
        test_value = RptAccessEnum().setValue(RptAccessEnum.NONE)
        access.setRptWriteAccess(test_value)
        access.setRptWriteAccess(None)
        assert access.getRptWriteAccess() == test_value


class TestRptExecutionContext:
    def test_initialization(self):
        """Test RptExecutionContext initialization defaults"""
        context = RptExecutionContext(AUTOSAR.getInstance(), "TaskA")
        assert context is not None
        assert context.getShortName() == "TaskA"


class TestRoleBasedMcDataAssignment:
    def test_initialization(self):
        """Test RoleBasedMcDataAssignment initialization defaults"""
        assignment = RoleBasedMcDataAssignment()
        assert assignment is not None
        assert assignment.executionContextRef is None
        assert assignment.mcDataInstanceRef is None
        assert assignment.role is None

    def test_mc_data_instance_ref_setter_getter(self):
        """Test mcDataInstanceRef setter and getter"""
        assignment = RoleBasedMcDataAssignment()
        ref = RefType()
        ref.setValue("/mc/instance")
        result = assignment.setMcDataInstanceRef(ref)
        assert result is assignment
        assert assignment.getMcDataInstanceRef() == ref

    def test_execution_context_ref_setter_getter(self):
        """Test executionContextRef setter and getter"""
        assignment = RoleBasedMcDataAssignment()
        ref = RefType()
        ref.setValue("/exec/context")
        result = assignment.setExecutionContextRef(ref)
        assert result is assignment
        assert assignment.getExecutionContextRef() == ref

    def test_role_setter_getter(self):
        """Test role setter and getter"""
        assignment = RoleBasedMcDataAssignment()
        role = Identifier().setValue("RpEnablerFlag")
        result = assignment.setRole(role)
        assert result is assignment
        assert assignment.getRole() == role


class TestRptEnums:
    def test_rpt_access_enum_members(self):
        """Test RptAccessEnum members match the spec literals"""
        assert RptAccessEnum.ENABLED == "enabled"
        assert RptAccessEnum.NONE == "none"
        assert RptAccessEnum.PROTECTED == "protected"

    def test_rpt_enabler_impl_type_enum_members(self):
        """Test RptEnablerImplTypeEnum members match the spec literals"""
        assert RptEnablerImplTypeEnum.NONE == "none"
        assert RptEnablerImplTypeEnum.RPT_ENABLER_RAM == "rptEnablerRam"
        assert RptEnablerImplTypeEnum.RPT_ENABLER_ROM == "rptEnablerRom"
        assert RptEnablerImplTypeEnum.RPT_ENABLER_RAM_AND_ROM == "rptEnablerRamAndRom"

    def test_rpt_execution_control_enum_members(self):
        """Test RptExecutionControlEnum members match the spec literals"""
        assert RptExecutionControlEnum.CONDITIONAL == "conditional"
        assert RptExecutionControlEnum.NONE == "none"

    def test_rpt_preparation_enum_members(self):
        """Test RptPreparationEnum members match the spec literals"""
        assert RptPreparationEnum.NONE == "none"
        assert RptPreparationEnum.RPT_LEVEL_1 == "rptLevel1"
        assert RptPreparationEnum.RPT_LEVEL_2 == "rptLevel2"
        assert RptPreparationEnum.RPT_LEVEL_3 == "rptLevel3"

    def test_rpt_service_point_enum_members(self):
        """Test RptServicePointEnum members match the spec literals"""
        assert RptServicePointEnum.ENABLED == "enabled"
        assert RptServicePointEnum.NONE == "none"

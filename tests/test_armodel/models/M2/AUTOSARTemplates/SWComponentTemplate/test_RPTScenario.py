from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptSupport import RptEnablerImplTypeEnum, RptExecutionControlEnum, RptPreparationEnum
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.RPTScenario import RptExecutableEntityProperties, RptImplPolicy, RptServicePointEnum


class TestRptImplPolicy:
    def test_initialization(self):
        """Test RptImplPolicy initialization defaults"""
        policy = RptImplPolicy()
        assert policy is not None
        assert policy.rptEnablerImplType is None
        assert policy.rptPreparationLevel is None

    def test_rpt_enabler_impl_type_setter_getter(self):
        """Test rptEnablerImplType setter and getter"""
        policy = RptImplPolicy()
        test_value = RptEnablerImplTypeEnum().setValue(RptEnablerImplTypeEnum.RPT_ENABLER_RAM)
        result = policy.setRptEnablerImplType(test_value)
        assert result is policy
        assert policy.getRptEnablerImplType() == test_value

    def test_rpt_enabler_impl_type_none_is_noop(self):
        """Test setting None rptEnablerImplType is a no-op"""
        policy = RptImplPolicy()
        test_value = RptEnablerImplTypeEnum().setValue(RptEnablerImplTypeEnum.RPT_ENABLER_ROM)
        policy.setRptEnablerImplType(test_value)
        policy.setRptEnablerImplType(None)
        assert policy.getRptEnablerImplType() == test_value

    def test_rpt_preparation_level_setter_getter(self):
        """Test rptPreparationLevel setter and getter"""
        policy = RptImplPolicy()
        test_value = RptPreparationEnum().setValue(RptPreparationEnum.RPT_LEVEL_2)
        result = policy.setRptPreparationLevel(test_value)
        assert result is policy
        assert policy.getRptPreparationLevel() == test_value


class TestRptExecutableEntityProperties:
    def test_initialization(self):
        """Test RptExecutableEntityProperties initialization defaults"""
        properties = RptExecutableEntityProperties()
        assert properties is not None
        assert properties.maxRptEventId is None
        assert properties.minRptEventId is None
        assert properties.rptExecutionControl is None
        assert properties.rptServicePoint is None

    def test_max_min_rpt_event_id_setter_getter(self):
        """Test maxRptEventId and minRptEventId setters and getters"""
        properties = RptExecutableEntityProperties()
        max_id = PositiveInteger().setValue("100")
        min_id = PositiveInteger().setValue("1")
        result = properties.setMaxRptEventId(max_id)
        assert result is properties
        assert properties.getMaxRptEventId() == max_id
        assert properties.setMinRptEventId(min_id) is properties
        assert properties.getMinRptEventId() == min_id

    def test_rpt_execution_control_setter_getter(self):
        """Test rptExecutionControl setter and getter"""
        properties = RptExecutableEntityProperties()
        test_value = RptExecutionControlEnum().setValue(RptExecutionControlEnum.CONDITIONAL)
        result = properties.setRptExecutionControl(test_value)
        assert result is properties
        assert properties.getRptExecutionControl() == test_value

    def test_rpt_service_point_setter_getter(self):
        """Test rptServicePoint setter and getter"""
        properties = RptExecutableEntityProperties()
        test_value = RptServicePointEnum().setValue(RptServicePointEnum.ENABLED)
        result = properties.setRptServicePoint(test_value)
        assert result is properties
        assert properties.getRptServicePoint() == test_value


class TestRptServicePointEnum:
    def test_members(self):
        """Test RptServicePointEnum members match the spec literals"""
        assert RptServicePointEnum.ENABLED == "enabled"
        assert RptServicePointEnum.NONE == "none"

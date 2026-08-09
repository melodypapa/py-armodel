import tempfile

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport import McSupportData, McSwEmulationMethodSupport, RoleBasedMcDataAssignment
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptSupport import (
    RptAccessEnum,
    RptEnablerImplTypeEnum,
    RptExecutionControlEnum,
    RptPreparationEnum,
    RptSupportData,
    RptSwPrototypingAccess,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import CIdentifier, Identifier, McdIdentifier, PositiveInteger, RefType, SymbolString
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.RPTScenario import RptExecutableEntityProperties, RptImplPolicy, RptServicePointEnum
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


class TestMcSupportDataInitialization:
    def test_initialization(self):
        """Test McSupportData initialization defaults"""
        support = McSupportData()
        assert support is not None
        assert support.emulationSupports == []
        assert support.mcParameterInstances == []
        assert support.mcVariableInstances == []
        assert support.measurableSystemConstantValuesRefs == []
        assert support.rptSupportData is None


class TestMcSupportDataEmulationSupport:
    def test_add_get_emulation_support(self):
        """Test addEmulationSupport appends and returns self for chaining"""
        support = McSupportData()
        emulation_support = McSwEmulationMethodSupport()
        result = support.addEmulationSupport(emulation_support)
        assert result is support
        assert support.getEmulationSupports() == [emulation_support]

    def test_add_emulation_support_none_is_noop(self):
        """Test adding a None emulation support is a no-op"""
        support = McSupportData()
        support.addEmulationSupport(None)
        assert support.getEmulationSupports() == []


class TestMcSupportDataMcParameterInstance:
    def test_create_get_mc_parameter_instance(self):
        """Test createMcParameterInstance creates and appends a calibration data instance"""
        support = McSupportData()
        instance = support.createMcParameterInstance("CalPrm1")
        assert instance is not None
        assert instance.getShortName() == "CalPrm1"
        assert support.getMcParameterInstances() == [instance]

    def test_create_mc_parameter_instance_duplicate_short_name(self):
        """Test createMcParameterInstance returns the existing instance for a duplicate short name"""
        support = McSupportData()
        instance_1 = support.createMcParameterInstance("CalPrm1")
        instance_2 = support.createMcParameterInstance("CalPrm1")
        assert instance_1 is instance_2
        assert len(support.getMcParameterInstances()) == 1


class TestMcSupportDataMcVariableInstance:
    def test_create_get_mc_variable_instance(self):
        """Test createMcVariableInstance creates and appends a measurement data instance"""
        support = McSupportData()
        instance = support.createMcVariableInstance("MeasVar1")
        assert instance is not None
        assert instance.getShortName() == "MeasVar1"
        assert support.getMcVariableInstances() == [instance]

    def test_create_mc_variable_instance_duplicate_short_name(self):
        """Test createMcVariableInstance returns the existing instance for a duplicate short name"""
        support = McSupportData()
        instance_1 = support.createMcVariableInstance("MeasVar1")
        instance_2 = support.createMcVariableInstance("MeasVar1")
        assert instance_1 is instance_2
        assert len(support.getMcVariableInstances()) == 1


class TestMcSupportDataMeasurableSystemConstantValues:
    def test_add_get_measurable_system_constant_values_ref(self):
        """Test addMeasurableSystemConstantValuesRef appends and returns self for chaining"""
        support = McSupportData()
        ref = RefType()
        ref.setValue("/sysconst")
        result = support.addMeasurableSystemConstantValuesRef(ref)
        assert result is support
        assert support.getMeasurableSystemConstantValuesRefs() == [ref]

    def test_add_measurable_system_constant_values_ref_none_is_noop(self):
        """Test adding a None system constant values ref is a no-op"""
        support = McSupportData()
        support.addMeasurableSystemConstantValuesRef(None)
        assert support.getMeasurableSystemConstantValuesRefs() == []


class TestMcSupportDataRptSupportData:
    def test_get_set_rpt_support_data(self):
        """Test setRptSupportData returns self and getRptSupportData round-trips"""
        support = McSupportData()
        rpt_support_data = RptSupportData()
        result = support.setRptSupportData(rpt_support_data)
        assert result is support
        assert support.getRptSupportData() == rpt_support_data

    def test_set_rpt_support_data_none_is_noop(self):
        """Test setting None rpt support data is a no-op"""
        support = McSupportData()
        rpt_support_data = RptSupportData()
        support.setRptSupportData(rpt_support_data)
        support.setRptSupportData(None)
        assert support.getRptSupportData() == rpt_support_data


class TestMcSupportDataRoundTrip:
    def test_round_trip_via_bsw_implementation(self):
        """Test full parse -> write -> re-parse round trip of McSupportData via a BswImplementation."""

        def make_ref(value):
            ref = RefType()
            ref.setValue(value)
            return ref

        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        ar_root = document.createARPackage("AUTOSAR")
        impl = ar_root.createBswImplementation("test_impl")
        support = McSupportData()
        impl.setMcSupport(support)

        support.addEmulationSupport(McSwEmulationMethodSupport())
        support.createMcParameterInstance("CalPrm1")
        support.createMcParameterInstance("CalPrm2")
        support.createMcVariableInstance("MeasVar1")
        support.addMeasurableSystemConstantValuesRef(make_ref("/sysconst"))
        support.setRptSupportData(RptSupportData())

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            support_2 = document_2.getARPackages()[0].getBswImplementations()[0].getMcSupport()

            assert support_2 is not None
            assert len(support_2.getEmulationSupports()) == 1
            assert len(support_2.getMcParameterInstances()) == 2
            assert [instance.getShortName() for instance in support_2.getMcParameterInstances()] == ["CalPrm1", "CalPrm2"]
            assert len(support_2.getMcVariableInstances()) == 1
            assert support_2.getMcVariableInstances()[0].getShortName() == "MeasVar1"
            assert len(support_2.getMeasurableSystemConstantValuesRefs()) == 1
            assert support_2.getMeasurableSystemConstantValuesRefs()[0].getValue() == "/sysconst"
            assert support_2.getRptSupportData() is not None
        finally:
            import os

            if os.path.exists(file_path):
                os.remove(file_path)

    def test_deep_round_trip_via_bsw_implementation(self):
        """Test parse -> write -> re-parse round trip of the full McSupportData subtree including RptSupportData and McDataInstance internals."""

        def make_ref(value):
            ref = RefType()
            ref.setValue(value)
            return ref

        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        ar_root = document.createARPackage("AUTOSAR")
        impl = ar_root.createBswImplementation("test_impl")
        support = McSupportData()
        impl.setMcSupport(support)

        instance = support.createMcParameterInstance("CalPrm1")
        instance.setArraySize(PositiveInteger().setValue("4")).setRole(Identifier().setValue("roleA")).setSymbol(SymbolString().setValue("sym"))
        instance.setFlatMapEntryRef(make_ref("/flatmap"))
        policy = RptImplPolicy()
        policy.setRptEnablerImplType(RptEnablerImplTypeEnum().setValue(RptEnablerImplTypeEnum.RPT_ENABLER_RAM)).setRptPreparationLevel(RptPreparationEnum().setValue(RptPreparationEnum.RPT_LEVEL_2))
        instance.setRptImplPolicy(policy)
        sub_element = instance.createSubElement("StructElem")
        sub_element.setSymbol(SymbolString().setValue("sub_sym"))
        assignment = RoleBasedMcDataAssignment()
        assignment.addMcDataInstanceRef(make_ref("/mc/inst")).setRole(Identifier().setValue("RpEnablerFlag"))
        instance.addMcDataAssignment(assignment)
        access = RptSwPrototypingAccess()
        access.setRptHookAccess(RptAccessEnum().setValue(RptAccessEnum.ENABLED)).setRptReadAccess(RptAccessEnum().setValue(RptAccessEnum.NONE))
        instance.setResultingRptSwPrototypingAccess(access)

        support.createMcVariableInstance("MeasVar1").setDisplayIdentifier(McdIdentifier().setValue("meas_1"))

        rpt_support_data = RptSupportData()
        support.setRptSupportData(rpt_support_data)
        rpt_support_data.createExecutionContext("TaskA")
        component = rpt_support_data.createRptComponent("Comp1")
        entity = component.createRptExecutableEntity("Run1")
        entity.setSymbol(CIdentifier().setValue("Run1_func"))
        event = entity.createRptExecutableEntityEvent("TimingEvent1")
        event.setRptEventId(PositiveInteger().setValue("7"))
        event.addExecutionContextRef(make_ref("/ctx"))
        event.addRptServicePointPostRef(make_ref("/sp/post"))
        event.addRptServicePointPreRef(make_ref("/sp/pre"))
        event_properties = RptExecutableEntityProperties()
        event_properties.setMaxRptEventId(PositiveInteger().setValue("100")).setMinRptEventId(PositiveInteger().setValue("1"))
        event_properties.setRptExecutionControl(RptExecutionControlEnum().setValue(RptExecutionControlEnum.CONDITIONAL)).setRptServicePoint(RptServicePointEnum().setValue(RptServicePointEnum.ENABLED))
        event.setRptExecutableEntityProperties(event_properties)
        entity.addRptRead(assignment)
        entity.addRptWrite(assignment)
        component.setRpImplPolicy(policy)
        service_point = rpt_support_data.createRptServicePoint("SP1")
        service_point.setServiceId(PositiveInteger().setValue("5")).setSymbol(CIdentifier().setValue("sp_func"))

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            support_2 = document_2.getARPackages()[0].getBswImplementations()[0].getMcSupport()

            assert support_2 is not None
            assert len(support_2.getMcParameterInstances()) == 1
            instance_2 = support_2.getMcParameterInstances()[0]
            assert instance_2.getShortName() == "CalPrm1"
            assert instance_2.getArraySize().getValue() == 4
            assert instance_2.getRole().getValue() == "roleA"
            assert instance_2.getSymbol().getValue() == "sym"
            assert instance_2.getFlatMapEntryRef().getValue() == "/flatmap"
            assert instance_2.getRptImplPolicy().getRptEnablerImplType().getValue() == "rptEnablerRam"
            assert instance_2.getRptImplPolicy().getRptPreparationLevel().getValue() == "rptLevel2"
            assert len(instance_2.getSubElements()) == 1
            assert instance_2.getSubElements()[0].getSymbol().getValue() == "sub_sym"
            assert instance_2.getMcDataAssignments()[0].getMcDataInstanceRefs()[0].getValue() == "/mc/inst"
            assert instance_2.getMcDataAssignments()[0].getRole().getValue() == "RpEnablerFlag"
            assert instance_2.getResultingRptSwPrototypingAccess().getRptHookAccess().getValue() == "enabled"
            assert support_2.getMcVariableInstances()[0].getDisplayIdentifier().getValue() == "meas_1"

            rpt_2 = support_2.getRptSupportData()
            assert rpt_2 is not None
            assert len(rpt_2.getExecutionContexts()) == 1
            assert rpt_2.getExecutionContexts()[0].getShortName() == "TaskA"
            component_2 = rpt_2.getRptComponents()[0]
            assert component_2.getShortName() == "Comp1"
            assert component_2.getRpImplPolicy().getRptEnablerImplType().getValue() == "rptEnablerRam"
            entity_2 = component_2.getRptExecutableEntities()[0]
            assert entity_2.getShortName() == "Run1"
            assert entity_2.getSymbol().getValue() == "Run1_func"
            assert len(entity_2.getRptReads()) == 1
            assert entity_2.getRptReads()[0].getMcDataInstanceRefs()[0].getValue() == "/mc/inst"
            assert len(entity_2.getRptWrites()) == 1
            event_2 = entity_2.getRptExecutableEntityEvents()[0]
            assert event_2.getShortName() == "TimingEvent1"
            assert event_2.getRptEventId().getValue() == 7
            assert event_2.getExecutionContextRefs()[0].getValue() == "/ctx"
            assert event_2.getRptServicePointPostRefs()[0].getValue() == "/sp/post"
            assert event_2.getRptServicePointPreRefs()[0].getValue() == "/sp/pre"
            assert event_2.getRptExecutableEntityProperties().getMaxRptEventId().getValue() == 100
            assert event_2.getRptExecutableEntityProperties().getMinRptEventId().getValue() == 1
            assert event_2.getRptExecutableEntityProperties().getRptExecutionControl().getValue() == "conditional"
            assert event_2.getRptExecutableEntityProperties().getRptServicePoint().getValue() == "enabled"
            service_point_2 = rpt_2.getRptServicePoints()[0]
            assert service_point_2.getShortName() == "SP1"
            assert service_point_2.getServiceId().getValue() == 5
            assert service_point_2.getSymbol().getValue() == "sp_func"
        finally:
            import os

            if os.path.exists(file_path):
                os.remove(file_path)

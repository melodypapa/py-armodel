from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport import ImplementationElementInParameterInstanceRef, McDataAccessDetails, McDataInstance, RoleBasedMcDataAssignment
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptSupport import RptSwPrototypingAccess
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Identifier, McdIdentifier, PositiveInteger, RefType, SymbolString
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.RPTScenario import RptImplPolicy
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps
import pytest


class TestMcDataInstanceInitialization:
    def test_initialization(self):
        """Test McDataInstance initialization defaults"""
        parent = AUTOSAR.getInstance()
        instance = McDataInstance(parent, "TestInstance")
        assert instance is not None
        assert instance.getShortName() == "TestInstance"
        assert instance.arraySize is None
        assert instance.displayIdentifier is None
        assert instance.flatMapEntryRef is None
        assert instance.instanceInMemory is None
        assert instance.mcDataAccessDetails is None
        assert instance.mcDataAssignments == []
        assert instance.resultingProperties is None
        assert instance.resultingRptSwPrototypingAccess is None
        assert instance.role is None
        assert instance.rptImplPolicy is None
        assert instance.subElements == []
        assert instance.symbol is None


class TestMcDataInstanceAccessors:
    def test_array_size_setter_getter(self):
        """Test arraySize setter and getter"""
        instance = McDataInstance(AUTOSAR.getInstance(), "TestInstance")
        test_value = PositiveInteger().setValue("4")
        result = instance.setArraySize(test_value)
        assert result is instance
        assert instance.getArraySize() == test_value

    def test_array_size_none_is_noop(self):
        """Test setting None arraySize is a no-op"""
        instance = McDataInstance(AUTOSAR.getInstance(), "TestInstance")
        test_value = PositiveInteger().setValue("4")
        instance.setArraySize(test_value)
        instance.setArraySize(None)
        assert instance.getArraySize() == test_value

    def test_display_identifier_setter_getter(self):
        """Test displayIdentifier setter and getter"""
        instance = McDataInstance(AUTOSAR.getInstance(), "TestInstance")
        test_value = McdIdentifier().setValue("meas_1")
        result = instance.setDisplayIdentifier(test_value)
        assert result is instance
        assert instance.getDisplayIdentifier() == test_value

    def test_flat_map_entry_ref_setter_getter(self):
        """Test flatMapEntryRef setter and getter"""
        instance = McDataInstance(AUTOSAR.getInstance(), "TestInstance")
        ref = RefType()
        ref.setValue("/flatmap/entry")
        result = instance.setFlatMapEntryRef(ref)
        assert result is instance
        assert instance.getFlatMapEntryRef() == ref

    def test_mc_data_assignment_add_get(self):
        """Test addMcDataAssignment appends and returns self"""
        instance = McDataInstance(AUTOSAR.getInstance(), "TestInstance")
        assignment = RoleBasedMcDataAssignment()
        result = instance.addMcDataAssignment(assignment)
        assert result is instance
        assert instance.getMcDataAssignments() == [assignment]

    def test_mc_data_assignment_none_is_noop(self):
        """Test adding None mc data assignment is a no-op"""
        instance = McDataInstance(AUTOSAR.getInstance(), "TestInstance")
        instance.addMcDataAssignment(None)
        assert instance.getMcDataAssignments() == []

    def test_mc_data_access_details_setter_getter(self):
        """Test mcDataAccessDetails setter and getter"""
        instance = McDataInstance(AUTOSAR.getInstance(), "TestInstance")
        details = McDataAccessDetails()
        result = instance.setMcDataAccessDetails(details)
        assert result is instance
        assert instance.getMcDataAccessDetails() == details

    def test_instance_in_memory_setter_getter(self):
        """Test instanceInMemory setter and getter"""
        instance = McDataInstance(AUTOSAR.getInstance(), "TestInstance")
        ref = ImplementationElementInParameterInstanceRef()
        ref.setContextRef(RefType().setValue("/mem/ctx"))
        ref.setTargetRef(RefType().setValue("/mem/inst"))
        result = instance.setInstanceInMemory(ref)
        assert result is instance
        assert instance.getInstanceInMemory() == ref

    def test_resulting_properties_setter_getter(self):
        """Test resultingProperties setter and getter"""
        instance = McDataInstance(AUTOSAR.getInstance(), "TestInstance")
        properties = SwDataDefProps()
        result = instance.setResultingProperties(properties)
        assert result is instance
        assert instance.getResultingProperties() == properties

    def test_resulting_rpt_sw_prototyping_access_setter_getter(self):
        """Test resultingRptSwPrototypingAccess setter and getter"""
        instance = McDataInstance(AUTOSAR.getInstance(), "TestInstance")
        access = RptSwPrototypingAccess()
        result = instance.setResultingRptSwPrototypingAccess(access)
        assert result is instance
        assert instance.getResultingRptSwPrototypingAccess() == access

    def test_role_setter_getter(self):
        """Test role setter and getter"""
        instance = McDataInstance(AUTOSAR.getInstance(), "TestInstance")
        test_value = Identifier().setValue("ImplicitBuffer")
        result = instance.setRole(test_value)
        assert result is instance
        assert instance.getRole() == test_value

    def test_rpt_impl_policy_setter_getter(self):
        """Test rptImplPolicy setter and getter"""
        instance = McDataInstance(AUTOSAR.getInstance(), "TestInstance")
        policy = RptImplPolicy()
        result = instance.setRptImplPolicy(policy)
        assert result is instance
        assert instance.getRptImplPolicy() == policy

    def test_symbol_setter_getter(self):
        """Test symbol setter and getter"""
        instance = McDataInstance(AUTOSAR.getInstance(), "TestInstance")
        test_value = SymbolString().setValue("sym_name")
        result = instance.setSymbol(test_value)
        assert result is instance
        assert instance.getSymbol() == test_value


class TestMcDataInstanceSubElement:
    def test_create_get_sub_element(self):
        """Test createSubElement creates and appends a sub element"""
        instance = McDataInstance(AUTOSAR.getInstance(), "Root")
        sub_element = instance.createSubElement("StructElem")
        assert sub_element is not None
        assert sub_element.getShortName() == "StructElem"
        assert instance.getSubElements() == [sub_element]

    def test_create_sub_element_duplicate_short_name(self):
        """Test createSubElement returns the existing sub element for a duplicate short name"""
        instance = McDataInstance(AUTOSAR.getInstance(), "Root")
        sub_element_1 = instance.createSubElement("StructElem")
        sub_element_2 = instance.createSubElement("StructElem")
        assert sub_element_1 is sub_element_2
        assert len(instance.getSubElements()) == 1

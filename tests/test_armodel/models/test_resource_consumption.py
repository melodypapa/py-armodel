from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.HeapUsage import HeapUsage
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.HardwareConfiguration import HardwareConfiguration
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.SoftwareContext import SoftwareContext
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.StackUsage import StackUsage, MeasuredStackUsage, RoughEstimateStackUsage, WorstCaseStackUsage
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.MemorySectionUsage import MemorySection
from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import String, ARLiteral, PositiveInteger, RefType
import pytest


class TestHeapUsage:
    def test_abstract_class_cannot_be_instantiated(self):
        """Test that HeapUsage abstract class cannot be instantiated directly"""
        with pytest.raises(NotImplementedError, match="HeapUsage is an abstract class."):
            HeapUsage(None, "TestHeap")


class TestHardwareConfiguration:
    def test_initialization(self):
        """Test HardwareConfiguration initialization"""
        hw_config = HardwareConfiguration()
        assert hw_config is not None
        assert hw_config.additionalInformation is None
        assert hw_config.processorMode is None
        assert hw_config.processorSpeed is None

    def test_additional_information_setter_getter(self):
        """Test additionalInformation setter and getter"""
        hw_config = HardwareConfiguration()
        test_value = String().setValue("Additional Info")
        result = hw_config.setAdditionalInformation(test_value)
        assert result is hw_config  # Method chaining
        assert hw_config.getAdditionalInformation() == test_value

    def test_processor_mode_setter_getter(self):
        """Test processorMode setter and getter"""
        hw_config = HardwareConfiguration()
        test_value = String().setValue("ARM Cortex-M4")
        result = hw_config.setProcessorMode(test_value)
        assert result is hw_config  # Method chaining
        assert hw_config.getProcessorMode() == test_value

    def test_processor_speed_setter_getter(self):
        """Test processorSpeed setter and getter"""
        hw_config = HardwareConfiguration()
        test_value = String().setValue("120 MHz")
        result = hw_config.setProcessorSpeed(test_value)
        assert result is hw_config  # Method chaining
        assert hw_config.getProcessorSpeed() == test_value

    def test_all_properties(self):
        """Test setting all properties"""
        hw_config = HardwareConfiguration()
        hw_config.setAdditionalInformation(String().setValue("Test Info"))
        hw_config.setProcessorMode(String().setValue("Test Mode"))
        hw_config.setProcessorSpeed(String().setValue("Test Speed"))
        
        assert hw_config.getAdditionalInformation().getValue() == "Test Info"
        assert hw_config.getProcessorMode().getValue() == "Test Mode"
        assert hw_config.getProcessorSpeed().getValue() == "Test Speed"


class TestSoftwareContext:
    def test_initialization(self):
        """Test SoftwareContext initialization"""
        sw_context = SoftwareContext()
        assert sw_context is not None
        assert sw_context.input is None
        assert sw_context.state is None

    def test_input_setter_getter(self):
        """Test input setter and getter"""
        sw_context = SoftwareContext()
        test_value = String().setValue("Test Input")
        result = sw_context.setInput(test_value)
        assert result is sw_context  # Method chaining
        assert sw_context.getInput() == test_value

    def test_state_setter_getter(self):
        """Test state setter and getter"""
        sw_context = SoftwareContext()
        test_value = String().setValue("Running")
        result = sw_context.setState(test_value)
        assert result is sw_context  # Method chaining
        assert sw_context.getState() == test_value

    def test_all_properties(self):
        """Test setting all properties"""
        sw_context = SoftwareContext()
        sw_context.setInput(String().setValue("Input Data"))
        sw_context.setState(String().setValue("Active"))
        
        assert sw_context.getInput().getValue() == "Input Data"
        assert sw_context.getState().getValue() == "Active"


class TestStackUsage:
    def test_abstract_class_cannot_be_instantiated(self):
        """Test that StackUsage abstract class cannot be instantiated directly"""
        parent = AUTOSAR.getInstance()
        with pytest.raises(NotImplementedError, match="StackUsage is an abstract class."):
            StackUsage(parent, "TestStack")

    def test_measured_stack_usage_initialization(self):
        """Test MeasuredStackUsage initialization"""
        parent = AUTOSAR.getInstance()
        stack_usage = MeasuredStackUsage(parent, "TestStack")
        assert stack_usage is not None
        assert stack_usage.getShortName() == "TestStack"

    def test_measured_stack_usage_properties(self):
        """Test MeasuredStackUsage specific properties"""
        parent = AUTOSAR.getInstance()
        stack_usage = MeasuredStackUsage(parent, "TestStack")
        
        # Test average memory consumption
        avg_value = PositiveInteger().setValue(1024)
        result = stack_usage.setAverageMemoryConsumption(avg_value)
        assert result is stack_usage
        assert stack_usage.getAverageMemoryConsumption() == avg_value
        
        # Test maximum memory consumption
        max_value = PositiveInteger().setValue(2048)
        result = stack_usage.setMaximumMemoryConsumption(max_value)
        assert result is stack_usage
        assert stack_usage.getMaximumMemoryConsumption() == max_value

    def test_rough_estimate_stack_usage_initialization(self):
        """Test RoughEstimateStackUsage initialization"""
        parent = AUTOSAR.getInstance()
        stack_usage = RoughEstimateStackUsage(parent, "TestStack")
        assert stack_usage is not None
        assert stack_usage.getShortName() == "TestStack"

    def test_rough_estimate_stack_usage_properties(self):
        """Test RoughEstimateStackUsage specific properties"""
        parent = AUTOSAR.getInstance()
        stack_usage = RoughEstimateStackUsage(parent, "TestStack")
        
        mem_value = PositiveInteger().setValue(512)
        result = stack_usage.setMemoryConsumption(mem_value)
        assert result is stack_usage
        assert stack_usage.getMemoryConsumption() == mem_value

    def test_worst_case_stack_usage_initialization(self):
        """Test WorstCaseStackUsage initialization"""
        parent = AUTOSAR.getInstance()
        stack_usage = WorstCaseStackUsage(parent, "TestStack")
        assert stack_usage is not None
        assert stack_usage.getShortName() == "TestStack"

    def test_worst_case_stack_usage_properties(self):
        """Test WorstCaseStackUsage specific properties"""
        parent = AUTOSAR.getInstance()
        stack_usage = WorstCaseStackUsage(parent, "TestStack")
        
        mem_value = PositiveInteger().setValue(4096)
        result = stack_usage.setMemoryConsumption(mem_value)
        assert result is stack_usage
        assert stack_usage.getMemoryConsumption() == mem_value

    def test_stack_usage_base_properties(self):
        """Test StackUsage base class properties"""
        parent = AUTOSAR.getInstance()
        stack_usage = MeasuredStackUsage(parent, "TestStack")
        
        # Test executable entity ref
        exec_ref = RefType().setValue("TestEntity")
        result = stack_usage.setExecutableEntityRef(exec_ref)
        assert result is stack_usage
        assert stack_usage.getExecutableEntityRef() == exec_ref
        
        # Test hardware configuration
        hw_config = HardwareConfiguration()
        result = stack_usage.setHardwareConfiguration(hw_config)
        assert result is stack_usage
        assert stack_usage.getHardwareConfiguration() == hw_config
        
        # Test hw element ref
        hw_ref = RefType().setValue("TestHwElement")
        result = stack_usage.setHwElementRef(hw_ref)
        assert result is stack_usage
        assert stack_usage.getHwElementRef() == hw_ref
        
        # Test software context
        sw_context = SoftwareContext()
        result = stack_usage.setSoftwareContext(sw_context)
        assert result is stack_usage
        assert stack_usage.getSoftwareContext() == sw_context


class TestMemorySection:
    def test_initialization(self):
        """Test MemorySection initialization"""
        parent = AUTOSAR.getInstance()
        mem_section = MemorySection(parent, "TestMemory")
        assert mem_section is not None
        assert mem_section.getShortName() == "TestMemory"
        assert mem_section.alignment is None
        assert mem_section.memClassSymbol is None
        assert mem_section.size is None
        assert mem_section.options == []
        assert mem_section.swAddrMethodRef is None
        assert mem_section.symbol is None

    def test_alignment_setter_getter(self):
        """Test alignment setter and getter"""
        parent = AUTOSAR.getInstance()
        mem_section = MemorySection(parent, "TestMemory")
        test_value = ARLiteral().setValue("8")
        result = mem_section.setAlignment(test_value)
        assert result is mem_section  # Method chaining
        assert mem_section.getAlignment() == test_value

    def test_alignment_property_setter(self):
        """Test alignment property setter"""
        parent = AUTOSAR.getInstance()
        mem_section = MemorySection(parent, "TestMemory")
        test_value = ARLiteral().setValue("16")
        mem_section.alignment = test_value
        assert mem_section.alignment == test_value

    def test_alignment_property_setter_none(self):
        """Test alignment property setter with None"""
        parent = AUTOSAR.getInstance()
        mem_section = MemorySection(parent, "TestMemory")
        mem_section.alignment = None
        assert mem_section.alignment is None

    def test_mem_class_symbol_setter_getter(self):
        """Test memClassSymbol setter and getter"""
        parent = AUTOSAR.getInstance()
        mem_section = MemorySection(parent, "TestMemory")
        test_value = ARLiteral().setValue("DATA")
        result = mem_section.setMemClassSymbol(test_value)
        assert result is mem_section  # Method chaining
        assert mem_section.getMemClassSymbol() == test_value

    def test_size_setter_getter(self):
        """Test size setter and getter"""
        parent = AUTOSAR.getInstance()
        mem_section = MemorySection(parent, "TestMemory")
        test_value = 1024
        result = mem_section.setSize(test_value)
        assert result is mem_section  # Method chaining
        assert mem_section.getSize() == test_value

    def test_sw_addr_method_ref_setter_getter(self):
        """Test swAddrMethodRef setter and getter"""
        parent = AUTOSAR.getInstance()
        mem_section = MemorySection(parent, "TestMemory")
        test_value = String().setValue("ADDR_METHOD")
        result = mem_section.setSwAddrMethodRef(test_value)
        assert result is mem_section  # Method chaining
        assert mem_section.getSwAddrMethodRef() == test_value

    def test_symbol_setter_getter(self):
        """Test symbol setter and getter"""
        parent = AUTOSAR.getInstance()
        mem_section = MemorySection(parent, "TestMemory")
        test_value = ARLiteral().setValue("_test_symbol")
        result = mem_section.setSymbol(test_value)
        assert result is mem_section  # Method chaining
        assert mem_section.getSymbol() == test_value

    def test_add_option(self):
        """Test adding options"""
        parent = AUTOSAR.getInstance()
        mem_section = MemorySection(parent, "TestMemory")
        option1 = ARLiteral().setValue("OPTION1")
        option2 = ARLiteral().setValue("OPTION2")
        
        mem_section.addOption(option1)
        mem_section.addOption(option2)
        
        options = mem_section.getOptions()
        assert len(options) == 2
        assert options[0] == option1
        assert options[1] == option2

    def test_get_options_empty(self):
        """Test getting options when empty"""
        parent = AUTOSAR.getInstance()
        mem_section = MemorySection(parent, "TestMemory")
        assert mem_section.getOptions() == []

    def test_all_properties(self):
        """Test setting all properties"""
        parent = AUTOSAR.getInstance()
        mem_section = MemorySection(parent, "TestMemory")
        
        mem_section.setAlignment(ARLiteral().setValue("8"))
        mem_section.setMemClassSymbol(ARLiteral().setValue("CODE"))
        mem_section.setSize(2048)
        mem_section.setSwAddrMethodRef(String().setValue("ABSOLUTE"))
        mem_section.setSymbol(ARLiteral().setValue("_code_section"))
        mem_section.addOption(ARLiteral().setValue("READONLY"))
        
        assert mem_section.getAlignment().getValue() == "8"
        assert mem_section.getMemClassSymbol().getValue() == "CODE"
        assert mem_section.getSize() == 2048
        assert mem_section.getSwAddrMethodRef().getValue() == "ABSOLUTE"
        assert mem_section.getSymbol().getValue() == "_code_section"
        assert len(mem_section.getOptions()) == 1
        assert mem_section.getOptions()[0].getValue() == "READONLY"
import os
import tempfile

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption import HardwareConfiguration, ResourceConsumption, SoftwareContext
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.ExecutionTime import (
    AnalyzedExecutionTime,
    ExecutionTime,
    MeasuredExecutionTime,
    MemorySectionLocation,
    RoughEstimateOfExecutionTime,
    SimulatedExecutionTime,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.HeapUsage import HeapUsage, MeasuredHeapUsage, RoughEstimateHeapUsage, WorstCaseHeapUsage
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.MemorySectionUsage import MemorySection, SectionNamePrefix
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.StackUsage import MeasuredStackUsage, RoughEstimateStackUsage, StackUsage, WorstCaseStackUsage
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime import MultidimensionalTime
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AlignmentType,
    ARLiteral,
    CIdentifier,
    CseCodeType,
    Identifier,
    Integer,
    NameToken,
    PositiveInteger,
    RefType,
    String,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount import AccessCount, AccessCountSet
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


class TestHeapUsage:
    def test_abstract_class_cannot_be_instantiated(self):
        """Test that HeapUsage abstract class cannot be instantiated directly"""
        with pytest.raises(TypeError, match="HeapUsage is an abstract class."):
            HeapUsage(None, "TestHeap")

    def test_concrete_subclass_can_be_instantiated(self):
        """Test that a concrete subclass of HeapUsage can be instantiated and the condition evaluates to False"""
        from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR

        # Create a concrete implementation to test the successful path
        class ConcreteHeapUsage(HeapUsage):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        parent = AUTOSAR.getInstance()
        # This should work because type(self) != HeapUsage for the subclass
        heap_usage = ConcreteHeapUsage(parent, "TestHeap")
        assert heap_usage is not None


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
        with pytest.raises(TypeError, match="StackUsage is an abstract class."):
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

    def test_stack_usage_base_properties_none_noop(self):
        """Test that setting None on StackUsage base properties is a no-op."""
        parent = AUTOSAR.getInstance()
        stack_usage = MeasuredStackUsage(parent, "TestStack")

        exec_ref = RefType().setValue("TestEntity")
        hw_config = HardwareConfiguration()
        hw_ref = RefType().setValue("TestHwElement")
        sw_context = SoftwareContext()
        stack_usage.setExecutableEntityRef(exec_ref)
        stack_usage.setHardwareConfiguration(hw_config)
        stack_usage.setHwElementRef(hw_ref)
        stack_usage.setSoftwareContext(sw_context)

        stack_usage.setExecutableEntityRef(None)
        stack_usage.setHardwareConfiguration(None)
        stack_usage.setHwElementRef(None)
        stack_usage.setSoftwareContext(None)

        assert stack_usage.getExecutableEntityRef() == exec_ref
        assert stack_usage.getHardwareConfiguration() == hw_config
        assert stack_usage.getHwElementRef() == hw_ref
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
        test_value = AlignmentType().setValue("8")
        result = mem_section.setAlignment(test_value)
        assert result is mem_section  # Method chaining
        assert mem_section.getAlignment() == test_value

    def test_alignment_setter_none_is_noop(self):
        """Test alignment setter with None is a no-op"""
        parent = AUTOSAR.getInstance()
        mem_section = MemorySection(parent, "TestMemory")
        mem_section.setAlignment(AlignmentType().setValue("16"))
        mem_section.setAlignment(None)
        assert mem_section.getAlignment().getValue() == "16"

    def test_alignment_default_value(self):
        """Test alignment defaults to None"""
        parent = AUTOSAR.getInstance()
        mem_section = MemorySection(parent, "TestMemory")
        assert mem_section.getAlignment() is None

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
        test_value = PositiveInteger().setValue("1024")
        result = mem_section.setSize(test_value)
        assert result is mem_section  # Method chaining
        assert mem_section.getSize() == test_value
        assert mem_section.getSize().getValue() == 1024

    def test_size_setter_none_is_noop(self):
        """Test size setter with None is a no-op"""
        parent = AUTOSAR.getInstance()
        mem_section = MemorySection(parent, "TestMemory")
        mem_section.setSize(PositiveInteger().setValue("512"))
        mem_section.setSize(None)
        assert mem_section.getSize().getValue() == 512

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
        test_value = Identifier().setValue("test_symbol")
        result = mem_section.setSymbol(test_value)
        assert result is mem_section  # Method chaining
        assert mem_section.getSymbol() == test_value

    def test_mem_class_symbol_none_noop(self):
        """Test memClassSymbol setter with None is a no-op."""
        parent = AUTOSAR.getInstance()
        mem_section = MemorySection(parent, "TestMemory")
        mem_section.setMemClassSymbol(CIdentifier().setValue("DATA"))
        mem_section.setMemClassSymbol(None)
        assert mem_section.getMemClassSymbol().getValue() == "DATA"

    def test_prefix_ref_none_noop(self):
        """Test prefixRef setter with None is a no-op."""
        parent = AUTOSAR.getInstance()
        mem_section = MemorySection(parent, "TestMemory")
        mem_section.setPrefixRef(RefType().setValue("/Prefix"))
        mem_section.setPrefixRef(None)
        assert mem_section.getPrefixRef().getValue() == "/Prefix"

    def test_sw_addr_method_ref_none_noop(self):
        """Test swAddrMethodRef setter with None is a no-op."""
        parent = AUTOSAR.getInstance()
        mem_section = MemorySection(parent, "TestMemory")
        mem_section.setSwAddrMethodRef(RefType().setValue("ADDR"))
        mem_section.setSwAddrMethodRef(None)
        assert mem_section.getSwAddrMethodRef().getValue() == "ADDR"

    def test_symbol_none_noop(self):
        """Test symbol setter with None is a no-op."""
        parent = AUTOSAR.getInstance()
        mem_section = MemorySection(parent, "TestMemory")
        mem_section.setSymbol(Identifier().setValue("sym"))
        mem_section.setSymbol(None)
        assert mem_section.getSymbol().getValue() == "sym"

    def test_add_option_none_noop(self):
        """Test addOption with None does not append."""
        parent = AUTOSAR.getInstance()
        mem_section = MemorySection(parent, "TestMemory")
        mem_section.addOption(None)
        assert mem_section.getOptions() == []

    def test_add_executable_entity_ref_none_noop(self):
        """Test addExecutableEntityRef with None does not append."""
        parent = AUTOSAR.getInstance()
        mem_section = MemorySection(parent, "TestMemory")
        mem_section.addExecutableEntityRef(None)
        assert mem_section.getExecutableEntityRefs() == []

    def test_add_option(self):
        """Test adding options"""
        parent = AUTOSAR.getInstance()
        mem_section = MemorySection(parent, "TestMemory")
        option1 = Identifier().setValue("OPTION1")
        option2 = Identifier().setValue("OPTION2")

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

        mem_section.setAlignment(AlignmentType().setValue("8"))
        mem_section.setMemClassSymbol(CIdentifier().setValue("CODE"))
        mem_section.setSize(PositiveInteger().setValue("2048"))
        mem_section.setSwAddrMethodRef(String().setValue("ABSOLUTE"))
        mem_section.setSymbol(Identifier().setValue("code_section"))
        mem_section.addOption(Identifier().setValue("READONLY"))

        assert mem_section.getAlignment().getValue() == "8"
        assert mem_section.getMemClassSymbol().getValue() == "CODE"
        assert mem_section.getSize().getValue() == 2048
        assert mem_section.getSwAddrMethodRef().getValue() == "ABSOLUTE"
        assert mem_section.getSymbol().getValue() == "code_section"
        assert len(mem_section.getOptions()) == 1
        assert mem_section.getOptions()[0].getValue() == "READONLY"


class TestResourceConsumption:
    def test_initialization(self):
        """Test ResourceConsumption initialization"""
        parent = AUTOSAR.getInstance()
        resource = ResourceConsumption(parent, "TestResource")
        assert resource is not None
        assert resource.getShortName() == "TestResource"
        assert resource.accessCountSets == []
        assert resource.executionTimes == []
        assert resource.heapUsages == []
        assert resource.memorySections == []
        assert resource.sectionNamePrefixes == []
        assert resource.stackUsages == []

    def test_create_memory_section(self):
        """Test creating a memory section"""
        parent = AUTOSAR.getInstance()
        resource = ResourceConsumption(parent, "TestResource")
        section = resource.createMemorySection("TestSection")
        assert isinstance(section, MemorySection)
        assert section.getShortName() == "TestSection"
        assert len(resource.memorySections) == 1
        assert resource.memorySections[0] == section

    def test_create_memory_section_duplicate(self):
        """Test creating a memory section with duplicate name"""
        parent = AUTOSAR.getInstance()
        resource = ResourceConsumption(parent, "TestResource")
        section1 = resource.createMemorySection("TestSection")
        section2 = resource.createMemorySection("TestSection")  # Should return the same instance
        assert section1 is section2

    def test_get_memory_sections(self):
        """Test getting all memory sections"""
        parent = AUTOSAR.getInstance()
        resource = ResourceConsumption(parent, "TestResource")
        resource.createMemorySection("Section2")
        resource.createMemorySection("Section1")  # Note: different name to test sorting
        sections = resource.getMemorySections()
        assert len(sections) == 2
        assert sections[0].getShortName() == "Section1"
        assert sections[1].getShortName() == "Section2"

    def test_get_memory_section(self):
        """Test getting a specific memory section by name"""
        parent = AUTOSAR.getInstance()
        resource = ResourceConsumption(parent, "TestResource")
        created_section = resource.createMemorySection("TestSection")
        found_section = resource.getMemorySection("TestSection")
        assert found_section is created_section

    def test_get_memory_section_not_found(self):
        """Test getting a memory section that doesn't exist"""
        parent = AUTOSAR.getInstance()
        resource = ResourceConsumption(parent, "TestResource")
        found_section = resource.getMemorySection("NonExistentSection")
        assert found_section is None

    def test_create_measured_stack_usage(self):
        """Test creating a measured stack usage"""
        parent = AUTOSAR.getInstance()
        resource = ResourceConsumption(parent, "TestResource")
        stack_usage = resource.createMeasuredStackUsage("TestStack")
        assert isinstance(stack_usage, MeasuredStackUsage)
        assert stack_usage.getShortName() == "TestStack"
        assert len(resource.stackUsages) == 1
        assert resource.stackUsages[0] == stack_usage

    def test_create_measured_stack_usage_duplicate(self):
        """Test creating a measured stack usage with duplicate name"""
        parent = AUTOSAR.getInstance()
        resource = ResourceConsumption(parent, "TestResource")
        stack1 = resource.createMeasuredStackUsage("TestStack")
        stack2 = resource.createMeasuredStackUsage("TestStack")  # Should return the same instance
        assert stack1 is stack2

    def test_create_rough_estimate_stack_usage(self):
        """Test creating a rough estimate stack usage"""
        parent = AUTOSAR.getInstance()
        resource = ResourceConsumption(parent, "TestResource")
        stack_usage = resource.createRoughEstimateStackUsage("TestStack")
        assert isinstance(stack_usage, RoughEstimateStackUsage)
        assert stack_usage.getShortName() == "TestStack"
        assert len(resource.stackUsages) == 1
        assert resource.stackUsages[0] == stack_usage

    def test_create_rough_estimate_stack_usage_duplicate(self):
        """Test creating a rough estimate stack usage with duplicate name"""
        parent = AUTOSAR.getInstance()
        resource = ResourceConsumption(parent, "TestResource")
        stack1 = resource.createRoughEstimateStackUsage("TestStack")
        stack2 = resource.createRoughEstimateStackUsage("TestStack")  # Should return the same instance
        assert stack1 is stack2

    def test_create_worst_case_stack_usage(self):
        """Test creating a worst case stack usage"""
        parent = AUTOSAR.getInstance()
        resource = ResourceConsumption(parent, "TestResource")
        stack_usage = resource.createWorstCaseStackUsage("TestStack")
        assert isinstance(stack_usage, WorstCaseStackUsage)
        assert stack_usage.getShortName() == "TestStack"
        assert len(resource.stackUsages) == 1
        assert resource.stackUsages[0] == stack_usage

    def test_create_worst_case_stack_usage_duplicate(self):
        """Test creating a worst case stack usage with duplicate name"""
        parent = AUTOSAR.getInstance()
        resource = ResourceConsumption(parent, "TestResource")
        stack1 = resource.createWorstCaseStackUsage("TestStack")
        stack2 = resource.createWorstCaseStackUsage("TestStack")  # Should return the same instance
        assert stack1 is stack2

    def test_get_stack_usages(self):
        """Test getting all stack usages"""
        parent = AUTOSAR.getInstance()
        resource = ResourceConsumption(parent, "TestResource")
        resource.createMeasuredStackUsage("Stack2")
        resource.createWorstCaseStackUsage("Stack1")  # Note: different name to test sorting
        usages = resource.getStackUsages()
        assert len(usages) == 2
        assert usages[0].getShortName() == "Stack1"
        assert usages[1].getShortName() == "Stack2"

    def test_all_stack_usages_functionality(self):
        """Test full functionality with all stack usage types"""
        parent = AUTOSAR.getInstance()
        resource = ResourceConsumption(parent, "TestResource")

        # Create different types of stack usages
        measured = resource.createMeasuredStackUsage("MeasuredStack")
        rough = resource.createRoughEstimateStackUsage("RoughStack")
        worst = resource.createWorstCaseStackUsage("WorstStack")

        # Verify they were created correctly
        assert isinstance(measured, MeasuredStackUsage)
        assert isinstance(rough, RoughEstimateStackUsage)
        assert isinstance(worst, WorstCaseStackUsage)
        assert len(resource.stackUsages) == 3

        # Test that getStackUsages returns all of them
        all_usages = resource.getStackUsages()
        assert len(all_usages) == 3


class TestMeasuredStackUsageExtended:
    def test_minimum_memory_consumption(self):
        """Test minimumMemoryConsumption setter and getter"""
        parent = AUTOSAR.getInstance()
        stack_usage = MeasuredStackUsage(parent, "TestStack")
        min_value = PositiveInteger().setValue(256)
        result = stack_usage.setMinimumMemoryConsumption(min_value)
        assert result is stack_usage
        assert stack_usage.getMinimumMemoryConsumption() == min_value

    def test_test_pattern(self):
        """Test testPattern setter and getter"""
        parent = AUTOSAR.getInstance()
        stack_usage = MeasuredStackUsage(parent, "TestStack")
        pattern = String().setValue("SPECIAL_CASE")
        result = stack_usage.setTestPattern(pattern)
        assert result is stack_usage
        assert stack_usage.getTestPattern() == pattern


class TestHeapUsageSubclasses:
    def test_measured_heap_usage_initialization(self):
        """Test MeasuredHeapUsage initialization"""
        parent = AUTOSAR.getInstance()
        heap = MeasuredHeapUsage(parent, "TestHeap")
        assert heap.getShortName() == "TestHeap"
        assert heap.getAverageMemoryConsumption() is None
        assert heap.getMaximumMemoryConsumption() is None
        assert heap.getMinimumMemoryConsumption() is None
        assert heap.getTestPattern() is None

    def test_measured_heap_usage_properties(self):
        """Test MeasuredHeapUsage specific properties"""
        parent = AUTOSAR.getInstance()
        heap = MeasuredHeapUsage(parent, "TestHeap")
        avg = PositiveInteger().setValue(10)
        mx = PositiveInteger().setValue(20)
        mn = PositiveInteger().setValue(5)
        pattern = String().setValue("test")
        result = heap.setAverageMemoryConsumption(avg).setMaximumMemoryConsumption(mx).setMinimumMemoryConsumption(mn).setTestPattern(pattern)
        assert result is heap
        assert heap.getAverageMemoryConsumption() == avg
        assert heap.getMaximumMemoryConsumption() == mx
        assert heap.getMinimumMemoryConsumption() == mn
        assert heap.getTestPattern() == pattern

    def test_rough_estimate_heap_usage(self):
        """Test RoughEstimateHeapUsage properties"""
        parent = AUTOSAR.getInstance()
        heap = RoughEstimateHeapUsage(parent, "TestHeap")
        value = PositiveInteger().setValue(100)
        result = heap.setMemoryConsumption(value)
        assert result is heap
        assert heap.getMemoryConsumption() == value

    def test_worst_case_heap_usage(self):
        """Test WorstCaseHeapUsage properties"""
        parent = AUTOSAR.getInstance()
        heap = WorstCaseHeapUsage(parent, "TestHeap")
        value = PositiveInteger().setValue(200)
        result = heap.setMemoryConsumption(value)
        assert result is heap
        assert heap.getMemoryConsumption() == value

    def test_heap_usage_base_properties(self):
        """Test HeapUsage base class properties"""
        parent = AUTOSAR.getInstance()
        heap = MeasuredHeapUsage(parent, "TestHeap")
        hw_config = HardwareConfiguration()
        hw_ref = RefType().setValue("Hw")
        sw_context = SoftwareContext()
        result = heap.setHardwareConfiguration(hw_config).setHwElementRef(hw_ref).setSoftwareContext(sw_context)
        assert result is heap
        assert heap.getHardwareConfiguration() == hw_config
        assert heap.getHwElementRef() == hw_ref
        assert heap.getSoftwareContext() == sw_context

    def test_heap_usage_base_properties_none_noop(self):
        """Test that setting None on HeapUsage base properties is a no-op."""
        parent = AUTOSAR.getInstance()
        heap = MeasuredHeapUsage(parent, "TestHeap")
        hw_config = HardwareConfiguration()
        hw_ref = RefType().setValue("Hw")
        sw_context = SoftwareContext()
        heap.setHardwareConfiguration(hw_config).setHwElementRef(hw_ref).setSoftwareContext(sw_context)

        heap.setHardwareConfiguration(None).setHwElementRef(None).setSoftwareContext(None)

        assert heap.getHardwareConfiguration() == hw_config
        assert heap.getHwElementRef() == hw_ref
        assert heap.getSoftwareContext() == sw_context


class TestMemorySectionExtended:
    def test_executable_entity_refs(self):
        """Test addExecutableEntityRef and getExecutableEntityRefs"""
        parent = AUTOSAR.getInstance()
        mem_section = MemorySection(parent, "TestMemory")
        ref1 = RefType().setValue("/Exec/1")
        ref2 = RefType().setValue("/Exec/2")
        mem_section.addExecutableEntityRef(ref1)
        mem_section.addExecutableEntityRef(ref2)
        refs = mem_section.getExecutableEntityRefs()
        assert len(refs) == 2
        assert refs[0] == ref1
        assert refs[1] == ref2

    def test_prefix_ref(self):
        """Test prefixRef setter and getter"""
        parent = AUTOSAR.getInstance()
        mem_section = MemorySection(parent, "TestMemory")
        ref = RefType().setValue("/Prefix")
        result = mem_section.setPrefixRef(ref)
        assert result is mem_section
        assert mem_section.getPrefixRef() == ref


class TestSectionNamePrefix:
    def test_initialization(self):
        """Test SectionNamePrefix initialization"""
        parent = AUTOSAR.getInstance()
        prefix = SectionNamePrefix(parent, "TestPrefix")
        assert prefix is not None
        assert prefix.getShortName() == "TestPrefix"
        assert prefix.getImplementedInRef() is None
        assert prefix.getSymbol() is None

    def test_implemented_in_ref(self):
        """Test implementedInRef setter and getter"""
        parent = AUTOSAR.getInstance()
        prefix = SectionNamePrefix(parent, "TestPrefix")
        ref = RefType().setValue("/Artifact")
        result = prefix.setImplementedInRef(ref)
        assert result is prefix
        assert prefix.getImplementedInRef() == ref

    def test_implemented_in_ref_none_noop(self):
        """Test implementedInRef setter with None is a no-op."""
        parent = AUTOSAR.getInstance()
        prefix = SectionNamePrefix(parent, "TestPrefix")
        prefix.setImplementedInRef(RefType().setValue("/Artifact"))
        prefix.setImplementedInRef(None)
        assert prefix.getImplementedInRef().getValue() == "/Artifact"

    def test_symbol_none_noop(self):
        """Test inherited ImplementationProps symbol setter with None is a no-op."""
        parent = AUTOSAR.getInstance()
        prefix = SectionNamePrefix(parent, "TestPrefix")
        prefix.setSymbol(ARLiteral().setValue("MY_PREFIX"))
        prefix.setSymbol(None)
        assert prefix.getSymbol().getValue() == "MY_PREFIX"
        parent = AUTOSAR.getInstance()
        prefix = SectionNamePrefix(parent, "TestPrefix")
        symbol = ARLiteral().setValue("MY_PREFIX")
        result = prefix.setSymbol(symbol)
        assert result is prefix
        assert prefix.getSymbol() == symbol


class TestExecutionTime:
    def test_abstract_class_cannot_be_instantiated(self):
        """Test that ExecutionTime abstract class cannot be instantiated directly"""
        with pytest.raises(TypeError, match="ExecutionTime is an abstract class."):
            ExecutionTime(None, "TestET")

    def test_analyzed_execution_time(self):
        """Test AnalyzedExecutionTime properties"""
        parent = AUTOSAR.getInstance()
        et = AnalyzedExecutionTime(parent, "TestET")
        best = MultidimensionalTime().setCseCode(CseCodeType().setValue("cse")).setCseCodeFactor(Integer().setValue(2))
        worst = MultidimensionalTime().setCseCode(CseCodeType().setValue("cse")).setCseCodeFactor(Integer().setValue(4))
        result = et.setBestCaseExecutionTime(best).setWorstCaseExecutionTime(worst)
        assert result is et
        assert et.getBestCaseExecutionTime() == best
        assert et.getWorstCaseExecutionTime() == worst

    def test_measured_execution_time(self):
        """Test MeasuredExecutionTime properties"""
        parent = AUTOSAR.getInstance()
        et = MeasuredExecutionTime(parent, "TestET")
        mx = MultidimensionalTime().setCseCode(CseCodeType().setValue("cse")).setCseCodeFactor(Integer().setValue(9))
        mn = MultidimensionalTime().setCseCode(CseCodeType().setValue("cse")).setCseCodeFactor(Integer().setValue(1))
        nom = MultidimensionalTime().setCseCode(CseCodeType().setValue("cse")).setCseCodeFactor(Integer().setValue(5))
        result = et.setMaximumExecutionTime(mx).setMinimumExecutionTime(mn).setNominalExecutionTime(nom)
        assert result is et
        assert et.getMaximumExecutionTime() == mx
        assert et.getMinimumExecutionTime() == mn
        assert et.getNominalExecutionTime() == nom

    def test_simulated_execution_time(self):
        """Test SimulatedExecutionTime properties"""
        parent = AUTOSAR.getInstance()
        et = SimulatedExecutionTime(parent, "TestET")
        mx = MultidimensionalTime().setCseCode(CseCodeType().setValue("cse")).setCseCodeFactor(Integer().setValue(9))
        result = et.setMaximumExecutionTime(mx)
        assert result is et
        assert et.getMaximumExecutionTime() == mx
        assert et.getMinimumExecutionTime() is None
        assert et.getNominalExecutionTime() is None

    def test_rough_estimate_of_execution_time(self):
        """Test RoughEstimateOfExecutionTime properties"""
        parent = AUTOSAR.getInstance()
        et = RoughEstimateOfExecutionTime(parent, "TestET")
        info = String().setValue("rough guess")
        est = MultidimensionalTime().setCseCode(CseCodeType().setValue("cse")).setCseCodeFactor(Integer().setValue(3))
        result = et.setAdditionalInformation(info).setEstimatedExecutionTime(est)
        assert result is et
        assert et.getAdditionalInformation() == info
        assert et.getEstimatedExecutionTime() == est

    def test_execution_time_base_properties(self):
        """Test ExecutionTime base class properties"""
        parent = AUTOSAR.getInstance()
        et = AnalyzedExecutionTime(parent, "TestET")
        exec_ref = RefType().setValue("/Exec")
        hw_ref = RefType().setValue("/Hw")
        lib_ref = RefType().setValue("/Lib")
        hw_config = HardwareConfiguration()
        sw_context = SoftwareContext()
        result = (
            et.setExecutableEntityRef(exec_ref).setHwElementRef(hw_ref).setExclusiveAreaRef(hw_ref).setHardwareConfiguration(hw_config).setSoftwareContext(sw_context).addIncludedLibraryRef(lib_ref)
        )
        assert result is et
        assert et.getExecutableEntityRef() == exec_ref
        assert et.getHwElementRef() == hw_ref
        assert et.getExclusiveAreaRef() == hw_ref
        assert et.getHardwareConfiguration() == hw_config
        assert et.getSoftwareContext() == sw_context
        assert et.getIncludedLibraryRefs() == [lib_ref]

    def test_execution_time_base_properties_none_noop(self):
        """Test that setting None on ExecutionTime base properties is a no-op."""
        parent = AUTOSAR.getInstance()
        et = AnalyzedExecutionTime(parent, "TestET")
        exec_ref = RefType().setValue("/Exec")
        hw_ref = RefType().setValue("/Hw")
        hw_config = HardwareConfiguration()
        sw_context = SoftwareContext()
        et.setExecutableEntityRef(exec_ref).setHwElementRef(hw_ref).setHardwareConfiguration(hw_config).setSoftwareContext(sw_context)

        et.setExecutableEntityRef(None).setHwElementRef(None).setHardwareConfiguration(None).setSoftwareContext(None)

        assert et.getExecutableEntityRef() == exec_ref
        assert et.getHwElementRef() == hw_ref
        assert et.getHardwareConfiguration() == hw_config
        assert et.getSoftwareContext() == sw_context

    def test_memory_section_location(self):
        """Test MemorySectionLocation properties and addMemorySectionLocation"""
        parent = AUTOSAR.getInstance()
        et = AnalyzedExecutionTime(parent, "TestET")
        location = MemorySectionLocation()
        result = et.addMemorySectionLocation(location)
        assert result is et  # Method chaining
        assert len(et.getMemorySectionLocations()) == 1
        assert isinstance(location, MemorySectionLocation)
        provided_ref = RefType().setValue("/Provided")
        sw_ref = RefType().setValue("/Section")
        result = location.setProvidedMemoryRef(provided_ref).setSoftwareMemorySectionRef(sw_ref)
        assert result is location
        assert location.getProvidedMemoryRef() == provided_ref
        assert location.getSoftwareMemorySectionRef() == sw_ref
        assert len(et.getMemorySectionLocations()) == 1


class TestResourceConsumptionExtended:
    def test_create_analyzed_execution_time(self):
        """Test creating an analyzed execution time"""
        parent = AUTOSAR.getInstance()
        resource = ResourceConsumption(parent, "TestResource")
        et = resource.createAnalyzedExecutionTime("TestET")
        assert isinstance(et, AnalyzedExecutionTime)
        assert et.getShortName() == "TestET"
        assert len(resource.executionTimes) == 1

    def test_create_measured_execution_time(self):
        """Test creating a measured execution time"""
        parent = AUTOSAR.getInstance()
        resource = ResourceConsumption(parent, "TestResource")
        et = resource.createMeasuredExecutionTime("TestET")
        assert isinstance(et, MeasuredExecutionTime)

    def test_create_rough_estimate_of_execution_time(self):
        """Test creating a rough estimate of execution time"""
        parent = AUTOSAR.getInstance()
        resource = ResourceConsumption(parent, "TestResource")
        et = resource.createRoughEstimateOfExecutionTime("TestET")
        assert isinstance(et, RoughEstimateOfExecutionTime)

    def test_create_simulated_execution_time(self):
        """Test creating a simulated execution time"""
        parent = AUTOSAR.getInstance()
        resource = ResourceConsumption(parent, "TestResource")
        et = resource.createSimulatedExecutionTime("TestET")
        assert isinstance(et, SimulatedExecutionTime)

    def test_get_execution_times(self):
        """Test getting all execution times"""
        parent = AUTOSAR.getInstance()
        resource = ResourceConsumption(parent, "TestResource")
        resource.createAnalyzedExecutionTime("ET2")
        resource.createMeasuredExecutionTime("ET1")
        ets = resource.getExecutionTimes()
        assert len(ets) == 2
        assert ets[0].getShortName() == "ET1"
        assert ets[1].getShortName() == "ET2"

    def test_create_measured_heap_usage(self):
        """Test creating a measured heap usage"""
        parent = AUTOSAR.getInstance()
        resource = ResourceConsumption(parent, "TestResource")
        heap = resource.createMeasuredHeapUsage("TestHeap")
        assert isinstance(heap, MeasuredHeapUsage)
        assert heap.getShortName() == "TestHeap"
        assert len(resource.heapUsages) == 1

    def test_create_rough_estimate_heap_usage(self):
        """Test creating a rough estimate heap usage"""
        parent = AUTOSAR.getInstance()
        resource = ResourceConsumption(parent, "TestResource")
        heap = resource.createRoughEstimateHeapUsage("TestHeap")
        assert isinstance(heap, RoughEstimateHeapUsage)

    def test_create_worst_case_heap_usage(self):
        """Test creating a worst case heap usage"""
        parent = AUTOSAR.getInstance()
        resource = ResourceConsumption(parent, "TestResource")
        heap = resource.createWorstCaseHeapUsage("TestHeap")
        assert isinstance(heap, WorstCaseHeapUsage)

    def test_get_heap_usages(self):
        """Test getting all heap usages"""
        parent = AUTOSAR.getInstance()
        resource = ResourceConsumption(parent, "TestResource")
        resource.createMeasuredHeapUsage("Heap2")
        resource.createWorstCaseHeapUsage("Heap1")
        heaps = resource.getHeapUsages()
        assert len(heaps) == 2
        assert heaps[0].getShortName() == "Heap1"
        assert heaps[1].getShortName() == "Heap2"

    def test_create_section_name_prefix(self):
        """Test creating a section name prefix"""
        parent = AUTOSAR.getInstance()
        resource = ResourceConsumption(parent, "TestResource")
        prefix = resource.createSectionNamePrefix("TestPrefix")
        assert isinstance(prefix, SectionNamePrefix)
        assert prefix.getShortName() == "TestPrefix"
        assert len(resource.sectionNamePrefixes) == 1

    def test_get_section_name_prefixes(self):
        """Test getting all section name prefixes"""
        parent = AUTOSAR.getInstance()
        resource = ResourceConsumption(parent, "TestResource")
        resource.createSectionNamePrefix("Prefix2")
        resource.createSectionNamePrefix("Prefix1")
        prefixes = resource.getSectionNamePrefixes()
        assert len(prefixes) == 2
        assert prefixes[0].getShortName() == "Prefix1"
        assert prefixes[1].getShortName() == "Prefix2"

    def test_add_access_count_set(self):
        """Test adding an access count set"""
        parent = AUTOSAR.getInstance()
        resource = ResourceConsumption(parent, "TestResource")
        acs = AccessCountSet()
        result = resource.addAccessCountSet(acs)
        assert result is resource  # Method chaining
        assert resource.getAccessCountSets() == [acs]

    def test_add_access_count_set_none_is_noop(self):
        """Test adding a None access count set is a no-op"""
        parent = AUTOSAR.getInstance()
        resource = ResourceConsumption(parent, "TestResource")
        resource.addAccessCountSet(None)
        assert resource.getAccessCountSets() == []


class TestResourceConsumptionRoundTrip:
    def test_round_trip_all_collections(self):
        """Test full parse -> write -> re-parse round trip of all ResourceConsumption collections."""

        def make_ref(value):
            ref = RefType()
            ref.setValue(value)
            return ref

        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        ar_root = document.createARPackage("AUTOSAR")
        impl = ar_root.createBswImplementation("test_impl")
        resource = impl.createResourceConsumption("RC")

        acs = AccessCountSet()
        resource.addAccessCountSet(acs)
        acs.setCountProfile(NameToken().setValue("PROFILE"))
        count = AccessCount()
        count.setAccessPointRef(make_ref("/ap")).setValue(PositiveInteger().setValue("3"))
        acs.addAccessCount(count)

        et = resource.createAnalyzedExecutionTime("ET")
        et.setExclusiveAreaRef(make_ref("/ea")).setExecutableEntityRef(make_ref("/ee")).setHwElementRef(make_ref("/hw"))
        et.setBestCaseExecutionTime(MultidimensionalTime().setCseCode(CseCodeType().setValue("cse")).setCseCodeFactor(Integer().setValue("1000")))
        location = MemorySectionLocation()
        location.setProvidedMemoryRef(make_ref("/pm")).setSoftwareMemorySectionRef(make_ref("/sm"))
        et.addMemorySectionLocation(location)
        et.addIncludedLibraryRef(make_ref("/lib"))

        heap = resource.createMeasuredHeapUsage("H")
        heap.setAverageMemoryConsumption(PositiveInteger().setValue("10")).setMaximumMemoryConsumption(PositiveInteger().setValue("20"))
        heap.setMinimumMemoryConsumption(PositiveInteger().setValue("5")).setTestPattern(String().setValue("p"))

        resource.createSectionNamePrefix("P").setImplementedInRef(make_ref("/art"))

        mem_section = resource.createMemorySection("MS")
        mem_section.setPrefixRef(make_ref("/pref")).addExecutableEntityRef(make_ref("/ex"))

        resource.createWorstCaseStackUsage("WS").setMemoryConsumption(PositiveInteger().setValue("50"))
        resource.createMeasuredStackUsage("MSU").setMinimumMemoryConsumption(PositiveInteger().setValue("1")).setTestPattern(String().setValue("t"))
        resource.createRoughEstimateOfExecutionTime("RT").setAdditionalInformation(String().setValue("info"))

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            resource_2 = document_2.getARPackages()[0].getBswImplementations()[0].getResourceConsumption()

            assert len(resource_2.getExecutionTimes()) == 2
            assert len(resource_2.getHeapUsages()) == 1
            assert len(resource_2.getStackUsages()) == 2
            assert len(resource_2.getAccessCountSets()) == 1
            assert len(resource_2.getSectionNamePrefixes()) == 1
            assert len(resource_2.getMemorySections()) == 1

            et_2 = resource_2.getExecutionTimes()[0]
            assert et_2.getShortName() == "ET"
            assert et_2.getExclusiveAreaRef().getValue() == "/ea"
            assert et_2.getExecutableEntityRef().getValue() == "/ee"
            assert et_2.getHwElementRef().getValue() == "/hw"
            assert et_2.getBestCaseExecutionTime().getCseCode().getValue() == "cse"
            assert et_2.getBestCaseExecutionTime().getCseCodeFactor().getValue() == 1000
            assert et_2.getMemorySectionLocations()[0].getProvidedMemoryRef().getValue() == "/pm"
            assert et_2.getMemorySectionLocations()[0].getSoftwareMemorySectionRef().getValue() == "/sm"
            assert et_2.getIncludedLibraryRefs()[0].getValue() == "/lib"

            heap_2 = resource_2.getHeapUsages()[0]
            assert heap_2.getShortName() == "H"
            assert heap_2.getAverageMemoryConsumption().getValue() == 10
            assert heap_2.getMaximumMemoryConsumption().getValue() == 20
            assert heap_2.getMinimumMemoryConsumption().getValue() == 5
            assert heap_2.getTestPattern().getValue() == "p"

            acs_2 = resource_2.getAccessCountSets()[0]
            assert acs_2.getCountProfile().getValue() == "PROFILE"
            assert acs_2.getAccessCounts()[0].getAccessPointRef().getValue() == "/ap"
            assert acs_2.getAccessCounts()[0].getValue().getValue() == 3

            prefix_2 = resource_2.getSectionNamePrefixes()[0]
            assert prefix_2.getShortName() == "P"
            assert prefix_2.getImplementedInRef().getValue() == "/art"

            mem_section_2 = resource_2.getMemorySections()[0]
            assert mem_section_2.getShortName() == "MS"
            assert mem_section_2.getPrefixRef().getValue() == "/pref"
            assert mem_section_2.getExecutableEntityRefs()[0].getValue() == "/ex"

            ws_2 = [s for s in resource_2.getStackUsages() if s.getShortName() == "WS"][0]
            assert ws_2.getMemoryConsumption().getValue() == 50
            msu_2 = [s for s in resource_2.getStackUsages() if s.getShortName() == "MSU"][0]
            assert msu_2.getMinimumMemoryConsumption().getValue() == 1
            assert msu_2.getTestPattern().getValue() == "t"

            rt_2 = resource_2.getExecutionTimes()[1]
            assert rt_2.getShortName() == "RT"
            assert rt_2.getAdditionalInformation().getValue() == "info"
        finally:
            os.remove(file_path)

"""
This module contains tests for the StackUsage family classes (StackUsage,
MeasuredStackUsage, RoughEstimateStackUsage, WorstCaseStackUsage) against the
AUTOSAR spec tables (AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate, Tables 8.9-8.12).
"""

import inspect
from typing import Optional, get_type_hints

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption import HardwareConfiguration, SoftwareContext
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.StackUsage import (
    MeasuredStackUsage,
    RoughEstimateStackUsage,
    StackUsage,
    WorstCaseStackUsage,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    RefType,
    String,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import (
    VariationPointCapable,
)

STACK_USAGE_NOTE = "Describes the stack memory usage of a software."

EXECUTABLE_ENTITY_REF_NOTE = "The executable entity for which this stack usage is described."

HARDWARE_CONFIGURATION_NOTE = "Contains information about the hardware context this stack usage is describing."

HW_ELEMENT_REF_NOTE = "Specifies for which hardware element (e.g. ECU) this stack usage is given."

SOFTWARE_CONTEXT_NOTE = "Contains details about the software context this stack usage is provided for."

MEASURED_STACK_USAGE_NOTE = "The stack usage has been measured."

AVERAGE_MEMORY_CONSUMPTION_NOTE = "The average stack usage measured. Unit: byte."

MAXIMUM_MEMORY_CONSUMPTION_NOTE = "The maximum stack usage measured. Unit: byte."

MINIMUM_MEMORY_CONSUMPTION_NOTE = "The minimum stack usage measured. Unit: byte."

TEST_PATTERN_NOTE = "Description of the test pattern used to acquire the measured values."

ROUGH_ESTIMATE_STACK_USAGE_NOTE = "Rough estimation of the stack usage."

ROUGH_MEMORY_CONSUMPTION_NOTE = "Rough estimate of the stack usage. Unit: byte."


def _setter_tail(name):
    return "A None value is a no-op and does not overwrite an existing %s." % name


def _doc(method):
    return inspect.cleandoc(method.__doc__)


def _make_ref(dest, value):
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _instantiate(cls, name):
    return cls(AUTOSAR.getInstance().createARPackage("Pkg_" + cls.__name__), name)


class TestStackUsage:
    """
    Test class for the abstract StackUsage base (Table 8.9), exercised through
    its concrete subclasses.
    """

    def test_abstract_instantiation_raises(self):
        with pytest.raises(TypeError):
            StackUsage(AUTOSAR.getInstance().createARPackage("Pkg_Abstract"), "SU")

    def test_base_chain(self):
        assert issubclass(StackUsage, Identifiable)
        assert issubclass(StackUsage, VariationPointCapable)
        assert issubclass(MeasuredStackUsage, StackUsage)
        assert issubclass(RoughEstimateStackUsage, StackUsage)
        assert issubclass(WorstCaseStackUsage, StackUsage)
        assert MeasuredStackUsage.__bases__ == (StackUsage,)
        assert RoughEstimateStackUsage.__bases__ == (StackUsage,)
        assert WorstCaseStackUsage.__bases__ == (StackUsage,)

    def test_class_docstring_verbatim(self):
        assert inspect.cleandoc(StackUsage.__doc__) == STACK_USAGE_NOTE

    def test_initialization_defaults(self):
        obj = _instantiate(MeasuredStackUsage, "SU")
        assert obj.getShortName() == "SU"
        assert obj.getExecutableEntityRef() is None
        assert obj.getHardwareConfiguration() is None
        assert obj.getHwElementRef() is None
        assert obj.getSoftwareContext() is None

    def test_annotations_match_spec_types(self):
        hints = get_type_hints(StackUsage.getExecutableEntityRef)
        assert hints["return"] == Optional[RefType]
        hints = get_type_hints(StackUsage.getHardwareConfiguration)
        assert hints["return"] == Optional[HardwareConfiguration]
        hints = get_type_hints(StackUsage.getHwElementRef)
        assert hints["return"] == Optional[RefType]
        hints = get_type_hints(StackUsage.getSoftwareContext)
        assert hints["return"] == Optional[SoftwareContext]

    def test_get_set_executable_entity_ref(self):
        obj = _instantiate(MeasuredStackUsage, "SU")
        assert obj.setExecutableEntityRef(_make_ref("EXECUTABLE-ENTITY", "/Pkg/EE")) is obj
        assert obj.getExecutableEntityRef().getValue() == "/Pkg/EE"
        assert obj.getExecutableEntityRef().getDest() == "EXECUTABLE-ENTITY"
        obj.setExecutableEntityRef(None)
        assert obj.getExecutableEntityRef().getValue() == "/Pkg/EE"

    def test_get_set_hw_element_ref(self):
        obj = _instantiate(MeasuredStackUsage, "SU")
        assert obj.setHwElementRef(_make_ref("HW-ELEMENT", "/Pkg/Hw")) is obj
        assert obj.getHwElementRef().getValue() == "/Pkg/Hw"
        assert obj.getHwElementRef().getDest() == "HW-ELEMENT"
        obj.setHwElementRef(None)
        assert obj.getHwElementRef().getValue() == "/Pkg/Hw"

    def test_get_set_hardware_configuration(self):
        obj = _instantiate(MeasuredStackUsage, "SU")
        config = HardwareConfiguration()
        config.setProcessorMode(String().setValue("NORMAL"))
        assert obj.setHardwareConfiguration(config) is obj
        assert obj.getHardwareConfiguration() is config
        assert obj.getHardwareConfiguration().getProcessorMode().getValue() == "NORMAL"
        obj.setHardwareConfiguration(None)
        assert obj.getHardwareConfiguration() is config

    def test_get_set_software_context(self):
        obj = _instantiate(MeasuredStackUsage, "SU")
        context = SoftwareContext()
        context.setState(String().setValue("RUN"))
        assert obj.setSoftwareContext(context) is obj
        assert obj.getSoftwareContext() is context
        assert obj.getSoftwareContext().getState().getValue() == "RUN"
        obj.setSoftwareContext(None)
        assert obj.getSoftwareContext() is context

    def test_init_has_no_docstring(self):
        assert StackUsage.__init__.__doc__ is None

    def test_docstrings_verbatim(self):
        assert _doc(StackUsage.getExecutableEntityRef) == EXECUTABLE_ENTITY_REF_NOTE
        assert _doc(StackUsage.setExecutableEntityRef) == EXECUTABLE_ENTITY_REF_NOTE + "\n" + _setter_tail("executableEntityRef")
        assert _doc(StackUsage.getHardwareConfiguration) == HARDWARE_CONFIGURATION_NOTE
        assert _doc(StackUsage.setHardwareConfiguration) == HARDWARE_CONFIGURATION_NOTE + "\n" + _setter_tail("hardwareConfiguration")
        assert _doc(StackUsage.getHwElementRef) == HW_ELEMENT_REF_NOTE
        assert _doc(StackUsage.setHwElementRef) == HW_ELEMENT_REF_NOTE + "\n" + _setter_tail("hwElementRef")
        assert _doc(StackUsage.getSoftwareContext) == SOFTWARE_CONTEXT_NOTE
        assert _doc(StackUsage.setSoftwareContext) == SOFTWARE_CONTEXT_NOTE + "\n" + _setter_tail("softwareContext")


class TestMeasuredStackUsage:
    """
    Test class for MeasuredStackUsage functionality (Table 8.11).
    """

    def test_base_chain(self):
        assert MeasuredStackUsage.__bases__ == (StackUsage,)

    def test_class_docstring_verbatim(self):
        assert inspect.cleandoc(MeasuredStackUsage.__doc__) == MEASURED_STACK_USAGE_NOTE

    def test_initialization(self):
        obj = _instantiate(MeasuredStackUsage, "MSU")
        assert obj.getShortName() == "MSU"
        assert obj.getAverageMemoryConsumption() is None
        assert obj.getMaximumMemoryConsumption() is None
        assert obj.getMinimumMemoryConsumption() is None
        assert obj.getTestPattern() is None

    def test_annotations_match_spec_types(self):
        hints = get_type_hints(MeasuredStackUsage.getAverageMemoryConsumption)
        assert hints["return"] == Optional[PositiveInteger]
        hints = get_type_hints(MeasuredStackUsage.getMaximumMemoryConsumption)
        assert hints["return"] == Optional[PositiveInteger]
        hints = get_type_hints(MeasuredStackUsage.getMinimumMemoryConsumption)
        assert hints["return"] == Optional[PositiveInteger]
        hints = get_type_hints(MeasuredStackUsage.getTestPattern)
        assert hints["return"] == Optional[String]

    def test_get_set_average_memory_consumption(self):
        obj = _instantiate(MeasuredStackUsage, "MSU")
        assert obj.setAverageMemoryConsumption(PositiveInteger().setValue("100")) is obj
        assert obj.getAverageMemoryConsumption().getValue() == 100
        obj.setAverageMemoryConsumption(None)
        assert obj.getAverageMemoryConsumption().getValue() == 100

    def test_get_set_maximum_memory_consumption(self):
        obj = _instantiate(MeasuredStackUsage, "MSU")
        assert obj.setMaximumMemoryConsumption(PositiveInteger().setValue("200")) is obj
        assert obj.getMaximumMemoryConsumption().getValue() == 200
        obj.setMaximumMemoryConsumption(None)
        assert obj.getMaximumMemoryConsumption().getValue() == 200

    def test_get_set_minimum_memory_consumption(self):
        obj = _instantiate(MeasuredStackUsage, "MSU")
        assert obj.setMinimumMemoryConsumption(PositiveInteger().setValue("50")) is obj
        assert obj.getMinimumMemoryConsumption().getValue() == 50
        obj.setMinimumMemoryConsumption(None)
        assert obj.getMinimumMemoryConsumption().getValue() == 50

    def test_get_set_test_pattern(self):
        obj = _instantiate(MeasuredStackUsage, "MSU")
        assert obj.setTestPattern(String().setValue("patternA")) is obj
        assert obj.getTestPattern().getValue() == "patternA"
        obj.setTestPattern(None)
        assert obj.getTestPattern().getValue() == "patternA"

    def test_init_has_no_docstring(self):
        assert MeasuredStackUsage.__init__.__doc__ is None

    def test_docstrings_verbatim(self):
        assert _doc(MeasuredStackUsage.getAverageMemoryConsumption) == AVERAGE_MEMORY_CONSUMPTION_NOTE
        assert _doc(MeasuredStackUsage.setAverageMemoryConsumption) == AVERAGE_MEMORY_CONSUMPTION_NOTE + "\n" + _setter_tail("averageMemoryConsumption")
        assert _doc(MeasuredStackUsage.getMaximumMemoryConsumption) == MAXIMUM_MEMORY_CONSUMPTION_NOTE
        assert _doc(MeasuredStackUsage.setMaximumMemoryConsumption) == MAXIMUM_MEMORY_CONSUMPTION_NOTE + "\n" + _setter_tail("maximumMemoryConsumption")
        assert _doc(MeasuredStackUsage.getMinimumMemoryConsumption) == MINIMUM_MEMORY_CONSUMPTION_NOTE
        assert _doc(MeasuredStackUsage.setMinimumMemoryConsumption) == MINIMUM_MEMORY_CONSUMPTION_NOTE + "\n" + _setter_tail("minimumMemoryConsumption")
        assert _doc(MeasuredStackUsage.getTestPattern) == TEST_PATTERN_NOTE
        assert _doc(MeasuredStackUsage.setTestPattern) == TEST_PATTERN_NOTE + "\n" + _setter_tail("testPattern")


class TestRoughEstimateStackUsage:
    """
    Test class for RoughEstimateStackUsage functionality (Table 8.12).
    """

    def test_base_chain(self):
        assert RoughEstimateStackUsage.__bases__ == (StackUsage,)

    def test_class_docstring_verbatim(self):
        assert inspect.cleandoc(RoughEstimateStackUsage.__doc__) == ROUGH_ESTIMATE_STACK_USAGE_NOTE

    def test_initialization(self):
        obj = _instantiate(RoughEstimateStackUsage, "RSU")
        assert obj.getShortName() == "RSU"
        assert obj.getMemoryConsumption() is None

    def test_annotations_match_spec_types(self):
        hints = get_type_hints(RoughEstimateStackUsage.getMemoryConsumption)
        assert hints["return"] == Optional[PositiveInteger]

    def test_get_set_memory_consumption(self):
        obj = _instantiate(RoughEstimateStackUsage, "RSU")
        assert obj.setMemoryConsumption(PositiveInteger().setValue("300")) is obj
        assert obj.getMemoryConsumption().getValue() == 300
        obj.setMemoryConsumption(None)
        assert obj.getMemoryConsumption().getValue() == 300

    def test_init_has_no_docstring(self):
        assert RoughEstimateStackUsage.__init__.__doc__ is None

    def test_docstrings_verbatim(self):
        assert _doc(RoughEstimateStackUsage.getMemoryConsumption) == ROUGH_MEMORY_CONSUMPTION_NOTE
        assert _doc(RoughEstimateStackUsage.setMemoryConsumption) == ROUGH_MEMORY_CONSUMPTION_NOTE + "\n" + _setter_tail("memoryConsumption")


class TestWorstCaseStackUsage:
    """
    Test class for WorstCaseStackUsage functionality.
    """

    def test_instantiation(self):
        obj = _instantiate(WorstCaseStackUsage, "WorstStack")
        assert obj.getShortName() == "WorstStack"

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
    Test class for MeasuredStackUsage functionality.
    """

    def test_instantiation(self):
        obj = _instantiate(MeasuredStackUsage, "MeasuredStack")
        assert obj.getShortName() == "MeasuredStack"


class TestRoughEstimateStackUsage:
    """
    Test class for RoughEstimateStackUsage functionality.
    """

    def test_instantiation(self):
        obj = _instantiate(RoughEstimateStackUsage, "RoughStack")
        assert obj.getShortName() == "RoughStack"


class TestWorstCaseStackUsage:
    """
    Test class for WorstCaseStackUsage functionality.
    """

    def test_instantiation(self):
        obj = _instantiate(WorstCaseStackUsage, "WorstStack")
        assert obj.getShortName() == "WorstStack"

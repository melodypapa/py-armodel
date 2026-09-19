"""
This module contains tests for the Ecuc* classes in the
AUTOSAR ECUCDescriptionTemplate module.
"""

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate import (
    EcucAbstractReferenceValue,
    EcucAddInfoParamValue,
    EcucContainerValue,
    EcucIndexableValue,
    EcucInstanceReferenceValue,
    EcucModuleConfigurationValues,
    EcucNumericalParamValue,
    EcucParameterValue,
    EcucReferenceValue,
    EcucTextualParamValue,
    EcucValueCollection,
    IntegerValue,
    ParameterValue,
)
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucConfigurationVariantEnum
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, RefType, RevisionLabelString, UnlimitedInteger
from armodel.models.M2.MSR.Documentation.Annotation import Annotation


def _instantiate(cls, name):
    return cls(AUTOSAR.getInstance().createARPackage("Pkg_" + cls.__name__), name)


class _R3ParameterValueStub(ParameterValue):
    """
    Minimal concrete subclass of the abstract R3.2.3 ParameterValue, used to
    exercise the inherited abstract-base behavior in unit tests.
    """


class TestEcucValueCollection:
    """
    Test class for EcucValueCollection functionality.
    """

    def test_instantiation(self):
        obj = _instantiate(EcucValueCollection, "EcucValueCollection")
        assert obj.getShortName() == "EcucValueCollection"


class TestEcucContainerValue:
    """
    Test class for EcucContainerValue functionality.
    """

    def test_instantiation(self):
        obj = _instantiate(EcucContainerValue, "EcucContainerValue")
        assert obj.getShortName() == "EcucContainerValue"


class TestEcucModuleConfigurationValues:
    """
    Test class for EcucModuleConfigurationValues functionality.
    """

    def test_instantiation(self):
        obj = _instantiate(EcucModuleConfigurationValues, "EcucModuleConfigurationValues")
        assert obj.getShortName() == "EcucModuleConfigurationValues"

    def test_initialization_defaults(self):
        obj = _instantiate(EcucModuleConfigurationValues, "EcucModuleConfigurationValues")
        assert obj.getContainers() == []
        assert obj.getDefinitionRef() is None
        assert obj.getEcucDefEdition() is None
        assert obj.getImplementationConfigVariant() is None
        assert obj.getModuleDescriptionRef() is None
        assert obj.getPostBuildVariantUsed() is None

    def test_set_definition_ref(self):
        obj = _instantiate(EcucModuleConfigurationValues, "EcucModuleConfigurationValues")
        ref = RefType().setValue("/Def")
        result = obj.setDefinitionRef(ref)
        assert result is obj
        assert obj.getDefinitionRef() == ref

    def test_set_ecuc_def_edition(self):
        obj = _instantiate(EcucModuleConfigurationValues, "EcucModuleConfigurationValues")
        edition = RevisionLabelString().setValue("1.0.0")
        result = obj.setEcucDefEdition(edition)
        assert result is obj
        assert obj.getEcucDefEdition() == edition

    def test_set_implementation_config_variant(self):
        obj = _instantiate(EcucModuleConfigurationValues, "EcucModuleConfigurationValues")
        variant = EcucConfigurationVariantEnum().setValue("VariantPreCompile")
        result = obj.setImplementationConfigVariant(variant)
        assert result is obj
        assert obj.getImplementationConfigVariant() == variant

    def test_set_module_description_ref(self):
        obj = _instantiate(EcucModuleConfigurationValues, "EcucModuleConfigurationValues")
        ref = RefType().setValue("/Desc")
        result = obj.setModuleDescriptionRef(ref)
        assert result is obj
        assert obj.getModuleDescriptionRef() == ref

    def test_set_post_build_variant_used(self):
        obj = _instantiate(EcucModuleConfigurationValues, "EcucModuleConfigurationValues")
        value = Boolean().setValue(True)
        result = obj.setPostBuildVariantUsed(value)
        assert result is obj
        assert obj.getPostBuildVariantUsed() == value

    def test_create_and_get_container(self):
        obj = _instantiate(EcucModuleConfigurationValues, "EcucModuleConfigurationValues")
        container = obj.createContainer("Container1")
        assert container is not None
        assert container.getShortName() == "Container1"
        assert obj.getContainers() == [container]

    def test_create_duplicate_container_returns_existing(self):
        obj = _instantiate(EcucModuleConfigurationValues, "EcucModuleConfigurationValues")
        first = obj.createContainer("Container1")
        second = obj.createContainer("Container1")
        assert first is second
        assert len(obj.getContainers()) == 1


class TestEcucAddInfoParamValue:
    """
    Test class for EcucAddInfoParamValue functionality.
    """

    def test_instantiation(self):
        assert isinstance(EcucAddInfoParamValue(), EcucAddInfoParamValue)


class TestEcucTextualParamValue:
    """
    Test class for EcucTextualParamValue functionality.
    """

    def test_instantiation(self):
        assert isinstance(EcucTextualParamValue(), EcucTextualParamValue)


class TestEcucNumericalParamValue:
    """
    Test class for EcucNumericalParamValue functionality.
    """

    def test_instantiation(self):
        assert isinstance(EcucNumericalParamValue(), EcucNumericalParamValue)


class TestEcucInstanceReferenceValue:
    """
    Test class for EcucInstanceReferenceValue functionality.
    """

    def test_instantiation(self):
        assert isinstance(EcucInstanceReferenceValue(), EcucInstanceReferenceValue)


class TestEcucReferenceValue:
    """
    Test class for EcucReferenceValue functionality.
    """

    def test_instantiation(self):
        assert isinstance(EcucReferenceValue(), EcucReferenceValue)


class TestEcucConfigurationVariantEnum:
    """
    Test class for EcucConfigurationVariantEnum functionality.
    """

    def test_instantiation(self):
        assert isinstance(EcucConfigurationVariantEnum(), EcucConfigurationVariantEnum)


class TestEcucIndexableValue:
    """
    Test class for EcucIndexableValue (abstract base) functionality.
    """

    def test_rejects_direct_instantiation(self):
        with pytest.raises(TypeError):
            EcucIndexableValue()


class TestEcucParameterValue:
    """
    Test class for EcucParameterValue (abstract base) functionality.
    """

    def test_rejects_direct_instantiation(self):
        with pytest.raises(TypeError):
            EcucParameterValue()

    def test_inheritance(self):
        assert issubclass(EcucAddInfoParamValue, EcucParameterValue)

    def test_initialization_defaults(self):
        obj = EcucTextualParamValue()
        assert obj.getAnnotations() == []
        assert obj.getDefinitionRef() is None
        assert obj.getIsAutoValue() is None

    def test_get_set_definition_ref(self):
        obj = EcucTextualParamValue()
        ref = RefType().setValue("/EcucDefs/Rte/Param")
        result = obj.setDefinitionRef(ref)
        assert result is obj
        assert obj.getDefinitionRef() == ref
        obj.setDefinitionRef(None)
        assert obj.getDefinitionRef() == ref

    def test_get_set_is_auto_value(self):
        obj = EcucTextualParamValue()
        value = Boolean().setValue(True)
        result = obj.setIsAutoValue(value)
        assert result is obj
        assert obj.getIsAutoValue() == value
        assert obj.getIsAutoValue().getValue() is True
        obj.setIsAutoValue(None)
        assert obj.getIsAutoValue() == value

    def test_add_annotation(self):
        obj = EcucTextualParamValue()
        annotation = Annotation()
        result = obj.addAnnotation(annotation)
        assert result is obj
        assert obj.getAnnotations() == [annotation]
        obj.addAnnotation(None)
        assert obj.getAnnotations() == [annotation]


class TestEcucAbstractReferenceValue:
    """
    Test class for EcucAbstractReferenceValue (abstract base) functionality.
    """

    def test_rejects_direct_instantiation(self):
        with pytest.raises(TypeError):
            EcucAbstractReferenceValue()

    def test_inheritance(self):
        assert issubclass(EcucInstanceReferenceValue, EcucAbstractReferenceValue)


class TestParameterValue:
    """
    Test class for ParameterValue (abstract base) functionality.

    Spec: R3.2.3/AUTOSAR_ECU_Configuration.pdf, Table 3.32, p.97 (R3.2 Rev 3)
    """

    def test_rejects_direct_instantiation(self):
        with pytest.raises(TypeError):
            ParameterValue()

    def test_initialization_defaults(self):
        obj = _R3ParameterValueStub()
        assert obj.getDefinitionRef() is None

    def test_get_set_definition_ref(self):
        obj = _R3ParameterValueStub()
        ref = RefType().setValue("/TS_T19D1M6I1R0_AS403/Os/Param")
        result = obj.setDefinitionRef(ref)
        assert result is obj
        assert obj.getDefinitionRef() == ref
        obj.setDefinitionRef(None)
        assert obj.getDefinitionRef() == ref


class TestIntegerValue:
    """
    Test class for IntegerValue functionality.

    Spec: R3.2.3/AUTOSAR_ECU_Configuration.pdf, Table 3.34, p.98 (R3.2 Rev 3)
    """

    def test_inheritance(self):
        assert issubclass(IntegerValue, ParameterValue)

    def test_initialization_defaults(self):
        obj = IntegerValue()
        assert obj.getDefinitionRef() is None
        assert obj.getValue() is None

    def test_get_set_value(self):
        obj = IntegerValue()
        value = UnlimitedInteger().setValue(5)
        result = obj.setValue(value)
        assert result is obj
        assert obj.getValue() == value
        assert obj.getValue().getValue() == 5
        obj.setValue(None)
        assert obj.getValue() == value

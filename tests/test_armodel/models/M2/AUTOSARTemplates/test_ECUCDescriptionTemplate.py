"""
This module contains tests for the Ecuc* classes in the
AUTOSAR ECUCDescriptionTemplate module.
"""

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate import (
    EcucAbstractReferenceValue,
    EcucAddInfoParamValue,
    EcucConfigurationVariantEnum,
    EcucContainerValue,
    EcucIndexableValue,
    EcucInstanceReferenceValue,
    EcucModuleConfigurationValues,
    EcucNumericalParamValue,
    EcucParameterValue,
    EcucReferenceValue,
    EcucTextualParamValue,
    EcucValueCollection,
)


def _instantiate(cls, name):
    return cls(AUTOSAR.getInstance().createARPackage("Pkg_" + cls.__name__), name)


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


class TestEcucAbstractReferenceValue:
    """
    Test class for EcucAbstractReferenceValue (abstract base) functionality.
    """

    def test_rejects_direct_instantiation(self):
        with pytest.raises(TypeError):
            EcucAbstractReferenceValue()

    def test_inheritance(self):
        assert issubclass(EcucInstanceReferenceValue, EcucAbstractReferenceValue)

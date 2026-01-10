import pytest

from src.armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from src.armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucChoiceContainerDef, EcucFloatParamDef, EcucParamConfContainerDef
from src.armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

# filepath: src/armodel/models/M2/AUTOSARTemplates/test_ECUCParameterDefTemplate.py


class TestEcucChoiceContainerDef:
    def test_initialization(self):
        document = AUTOSAR.getInstance()
        parent = document.createARPackage("AUTOSAR")
        short_name = "TestChoiceContainer"
        choice_container = EcucChoiceContainerDef(parent, short_name)

        assert choice_container.getShortName() == short_name
        assert choice_container.getChoices() == []

    def test_createEcucParamConfContainerDef(self):
        document = AUTOSAR.getInstance()
        parent = document.createARPackage("AUTOSAR")
        short_name = "TestChoiceContainer"
        choice_container = EcucChoiceContainerDef(parent, short_name)

        param_conf_container = choice_container.createEcucParamConfContainerDef("TestParamConfContainer")
        assert param_conf_container.getShortName() == "TestParamConfContainer"
        assert isinstance(param_conf_container, EcucParamConfContainerDef)
        assert param_conf_container in choice_container.getChoices()

    def test_createEcucParamConfContainerDef_duplicate(self):
        document = AUTOSAR.getInstance()
        parent = document.createARPackage("AUTOSAR")
        short_name = "TestChoiceContainer"
        choice_container = EcucChoiceContainerDef(parent, short_name)

        choice_container.createEcucParamConfContainerDef("TestParamConfContainer")
        param_conf_container_duplicate = choice_container.createEcucParamConfContainerDef("TestParamConfContainer")

        assert len(choice_container.getChoices()) == 1
        assert param_conf_container_duplicate.getShortName() == "TestParamConfContainer"

    def test_getChoices(self):
        document = AUTOSAR.getInstance()
        parent = document.createARPackage("AUTOSAR")
        short_name = "TestChoiceContainer"
        choice_container = EcucChoiceContainerDef(parent, short_name)

        choice_container.createEcucParamConfContainerDef("Choice1")
        choice_container.createEcucParamConfContainerDef("Choice2")

        choices = choice_container.getChoices()
        assert len(choices) == 2
        assert choices[0].getShortName() == "Choice1"
        assert choices[1].getShortName() == "Choice2"

        
class TestEcucFloatParamDef:
    def test_initialization(self):
        document = AUTOSAR.getInstance()
        parent = document.createARPackage("AUTOSAR")
        short_name = "TestFloatParam"
        float_param = EcucFloatParamDef(parent, short_name)

        assert float_param.getShortName() == short_name
        assert float_param.getDefaultValue() is None
        assert float_param.getMax() is None
        assert float_param.getMin() is None

    def test_set_and_get_default_value(self):
        document = AUTOSAR.getInstance()
        parent = document.createARPackage("AUTOSAR")
        float_param = EcucFloatParamDef(parent, "TestFloatParam")

        default_value = 3.14
        float_param.setDefaultValue(default_value)

        assert float_param.getDefaultValue() == default_value

    def test_set_and_get_max_value(self):
        document = AUTOSAR.getInstance()
        parent = document.createARPackage("AUTOSAR")
        float_param = EcucFloatParamDef(parent, "TestFloatParam")

        max_value = 100.0
        float_param.setMax(max_value)

        assert float_param.getMax() == max_value

    def test_set_and_get_min_value(self):
        document = AUTOSAR.getInstance()
        parent = document.createARPackage("AUTOSAR")
        float_param = EcucFloatParamDef(parent, "TestFloatParam")

        min_value = 0.0
        float_param.setMin(min_value)

        assert float_param.getMin() == min_value

    def test_set_max_to_none(self):
        document = AUTOSAR.getInstance()
        parent = document.createARPackage("AUTOSAR")
        float_param = EcucFloatParamDef(parent, "TestFloatParam")

        float_param.setMax(None)

        assert float_param.getMax() is None

    def test_set_min_to_none(self):
        document = AUTOSAR.getInstance()
        parent = document.createARPackage("AUTOSAR")
        float_param = EcucFloatParamDef(parent, "TestFloatParam")

        float_param.setMin(None)

        assert float_param.getMin() is None

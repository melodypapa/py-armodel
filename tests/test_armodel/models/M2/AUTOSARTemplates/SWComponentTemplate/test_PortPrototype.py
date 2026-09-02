import pytest

from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure import AtpBlueprintable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpPrototype
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import PPortComSpec, RPortComSpec
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import PortPrototype


class Test_PortPrototype:
    def test_PPortComSpec(self):
        with pytest.raises(TypeError) as err:
            PPortComSpec()
        assert str(err.value) == "PPortComSpec is an abstract class."

    def test_RPortComSpec(self):
        with pytest.raises(TypeError) as err:
            RPortComSpec()
        assert str(err.value) == "RPortComSpec is an abstract class."


class TestPortPrototypeHeritage:
    def test_abstract_initialization(self):
        with pytest.raises(TypeError) as err:
            PortPrototype(None, "pp")
        assert str(err.value) == "PortPrototype is an abstract class."

    def test_mro_reaches_atp_prototype_first(self):
        assert PortPrototype.__mro__[1] is AtpPrototype

    def test_mro_reaches_atp_blueprintable(self):
        # Table 3.2 Base closure names AtpBlueprintable; the compensating parallel
        # base restores it after AtpPrototype dropped AtpBlueprintable in favor of
        # AtpFeature. It must remain reachable in the MRO.
        assert AtpBlueprintable in PortPrototype.__mro__
        assert issubclass(PortPrototype, AtpBlueprintable)

    def test_concrete_subclass_initialization(self):
        class ConcretePort(PortPrototype):
            pass

        parent = object()
        pp = ConcretePort(parent, "myPort")
        assert pp.getShortName() == "myPort"
        assert pp.parent is parent
        assert isinstance(pp, AtpBlueprintable)
        assert isinstance(pp, AtpPrototype)

import pytest

from src.armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import PPortComSpec, RPortComSpec


class Test_PortPrototype:
    def test_PPortComSpec(self):
        with pytest.raises(NotImplementedError) as err:
            PPortComSpec()
        assert (str(err.value) == "PPortComSpec is an abstract class.")

    def test_RPortComSpec(self):
        with pytest.raises(NotImplementedError) as err:
            RPortComSpec()
        assert (str(err.value) == "RPortComSpec is an abstract class.")

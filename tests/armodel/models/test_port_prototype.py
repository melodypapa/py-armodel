import pytest

from armodel.models.port_prototype import PPortComSpec, RPortComSpec

class Test_PortProtype:
    def test_PPortComSpec(self):
        with pytest.raises(NotImplementedError) as err:
            PPortComSpec()
        assert(str(err.value) == "PPortComSpec is an abstract class.")

    def test_RPortComSpec(self):
        with pytest.raises(NotImplementedError) as err:
            RPortComSpec()
        assert(str(err.value) == "RPortComSpec is an abstract class.")

import pytest

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import BusspecificNmEcu, CanNmEcu


class Test_CanNmEcu:
    def test_instantiation(self):
        # concrete class per XSD (CAN-NM-ECU abstract="false") — no TypeError guard
        ecu = CanNmEcu()
        assert isinstance(ecu, BusspecificNmEcu)
        assert ecu.getChecksum() is None
        assert ecu.getTimestamp() is None

    def test_abstract_base_stays_abstract(self):
        with pytest.raises(TypeError):
            BusspecificNmEcu()

    def test_docstring_is_spec_note_verbatim(self):
        note = "CAN specific attributes."
        assert CanNmEcu.__doc__.strip() == note

import typing
from typing import Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Integer
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import VariationPoint
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import TpAddress


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


class Test_TpAddress:
    # Table 6.238, p.588 — attribute Note verbatim from the markdown
    NOTE_TP_ADDRESS = "An ECUs TP address on the referenced channel. This represents the diagnostic Address."
    CONSTRAINS = "[constr_9227] Existence of TpAddress.tpAddress: For each TpAddress, the attribute tpAddress" " shall exist at the time when the System Description is complete."

    def _make_address(self, parent=None):
        if parent is None:
            parent = MockParent()
        return TpAddress(parent, "TpAddr")

    def test_docstring_is_spec_note_verbatim(self):
        # Table 6.238, p.588 — class Note verbatim from the markdown + constr_9227 appended
        expected = self.NOTE_TP_ADDRESS + "\n\n" + self.CONSTRAINS
        assert TpAddress.__doc__.strip() == expected

    def test_init_has_no_docstring(self):
        assert TpAddress.__init__.__doc__ is None

    def test_heritage(self):
        address = self._make_address()
        assert isinstance(address, Identifiable)
        assert isinstance(address, ARObject)

    def test_initialization(self):
        address = self._make_address()
        assert address.getTpAddress() is None

    def test_get_set_tp_address(self):
        address = self._make_address()
        value = Integer().setValue("2047")
        assert address.setTpAddress(value) is address
        assert address.getTpAddress() is value
        address.setTpAddress(None)
        assert address.getTpAddress() is value

    def test_type_hints_pins(self):
        assert typing.get_type_hints(TpAddress.getTpAddress).get("return") == Optional[Integer]
        assert typing.get_type_hints(TpAddress.setTpAddress).get("value") == Optional[Integer]
        assert typing.get_type_hints(TpAddress.setTpAddress).get("return") is TpAddress

    def test_variation_point_capable(self):
        address = self._make_address()
        assert hasattr(address, "getVariationPoint")
        vp = VariationPoint()
        assert address.setVariationPoint(vp) is address
        assert address.getVariationPoint() is vp

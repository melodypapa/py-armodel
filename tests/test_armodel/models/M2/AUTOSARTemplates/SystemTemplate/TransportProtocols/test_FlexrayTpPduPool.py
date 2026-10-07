import typing
from inspect import cleandoc
from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import FlexrayTpPduPool


def _ref(value, dest):
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


def _pool(short_name: str) -> FlexrayTpPduPool:
    package = AUTOSAR.getInstance().createARPackage("TpConfigs")
    return FlexrayTpPduPool(package, short_name)


class Test_FlexrayTpPduPool:
    # Table 6.242, p.596 — class Note verbatim from the markdown; attribute note from the XSD
    # (the PDF table has no Note column)
    NOTE_N_PDU_REFS = "Reference to NPdus that are part of the PduPool."

    def test_docstring_is_spec_note_verbatim(self):
        assert cleandoc(FlexrayTpPduPool.__doc__) == "FlexrayTpPduPool is a set of N-PDUs which are defined for FrTp sending or receiving purpose."

    def test_init_has_no_docstring(self):
        assert FlexrayTpPduPool.__init__.__doc__ is None

    def test_heritage(self):
        pool = _pool("Pool1")
        assert isinstance(pool, Identifiable)

    def test_initialization(self):
        pool = _pool("Pool1")
        assert pool.getNPduRefs() == []

    def test_add_n_pdu_ref(self):
        pool = _pool("Pool1")
        ref1 = _ref("/NPdus/N1", "N-PDU")
        ref2 = _ref("/NPdus/N2", "N-PDU")
        assert pool.addNPduRef(ref1) is pool
        pool.addNPduRef(ref2)
        assert pool.getNPduRefs() == [ref1, ref2]
        pool.addNPduRef(None)
        assert pool.getNPduRefs() == [ref1, ref2]

    def test_type_hints_pins(self):
        assert typing.get_type_hints(FlexrayTpPduPool.getNPduRefs).get("return") == List[RefType]
        add_hints = typing.get_type_hints(FlexrayTpPduPool.addNPduRef)
        assert add_hints.get("value") == Optional[RefType]
        assert add_hints.get("return") is FlexrayTpPduPool

    def test_docstrings_are_spec_note_verbatim(self):
        assert cleandoc(FlexrayTpPduPool.addNPduRef.__doc__).split("\n")[0] == self.NOTE_N_PDU_REFS
        assert cleandoc(FlexrayTpPduPool.getNPduRefs.__doc__) == self.NOTE_N_PDU_REFS

    def test_variation_point_capable(self):
        pool = _pool("Pool1")
        assert pool.getVariationPoint() is None

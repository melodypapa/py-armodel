import typing
from inspect import cleandoc
from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection import TpConnection, TpConnectionIdent
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import EthTpConnection


def _ref(value, dest):
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


class Test_EthTpConnection:
    # Table 6.263, p.618 — attribute Note verbatim from the markdown
    NOTE_TP_SDUs = 'Reference to a PduTriggering that shall be transported using the "TP" semantics.'

    def test_docstring_is_spec_note_verbatim(self):
        # Table 6.263, p.618 — class Note verbatim from the markdown (no table constraints)
        assert cleandoc(EthTpConnection.__doc__) == 'A connection identifies which PduTriggerings shall be handled using the "TP" semantics.'

    def test_init_has_no_docstring(self):
        assert EthTpConnection.__init__.__doc__ is None

    def test_heritage(self):
        connection = EthTpConnection()
        assert isinstance(connection, TpConnection)
        assert connection.getIdent() is None

    def test_initialization(self):
        connection = EthTpConnection()
        assert connection.getTpSduRefs() == []

    def test_add_get_tp_sdu_refs(self):
        connection = EthTpConnection()
        ref1 = _ref("/PduTriggerings/Tp1", "PDU-TRIGGERING")
        ref2 = _ref("/PduTriggerings/Tp2", "PDU-TRIGGERING")
        assert connection.addTpSduRef(ref1) is connection
        assert connection.getTpSduRefs() == [ref1]
        connection.addTpSduRef(ref2)
        assert connection.getTpSduRefs() == [ref1, ref2]
        connection.addTpSduRef(None)
        assert connection.getTpSduRefs() == [ref1, ref2]

    def test_type_hints_pins(self):
        assert typing.get_type_hints(EthTpConnection.getTpSduRefs).get("return") == List[RefType]
        assert typing.get_type_hints(EthTpConnection.addTpSduRef).get("value") == Optional[RefType]
        assert typing.get_type_hints(EthTpConnection.addTpSduRef).get("return") is EthTpConnection

    def test_ident_factory(self):
        connection = EthTpConnection()
        ident = connection.createTpConnectionIdent("EthIdent")
        assert isinstance(ident, TpConnectionIdent)
        assert connection.getIdent() is ident
        assert connection.createTpConnectionIdent("other") is ident

    def test_not_variation_point_capable(self):
        # XSD group ETH-TP-CONNECTION carries no VARIATION-POINT element
        assert not hasattr(EthTpConnection, "getVariationPoint")

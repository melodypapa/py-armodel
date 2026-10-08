from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, Integer, RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import J1939TpPg


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


class TestJ1939TpPg:
    """Test class for J1939TpPg (R23-11, Table 6.269, p.626)."""

    def test_initialization(self):
        """
        Test J1939TpPg initialization and field defaults.
        """
        pg = J1939TpPg()

        assert pg is not None
        assert pg.getDirectPduRef() is None
        assert pg.getPgn() is None
        assert pg.getRequestable() is None
        assert pg.getSduRefs() == []

    def test_get_set_direct_pdu_ref(self):
        pg = J1939TpPg()
        ref = RefType()
        ref.setValue("/Pdus/DirectPdu")

        result = pg.setDirectPduRef(ref)
        assert result is pg
        assert pg.getDirectPduRef() is ref
        pg.setDirectPduRef(None)
        assert pg.getDirectPduRef() is ref

    def test_get_set_pgn(self):
        pg = J1939TpPg()
        value = Integer()
        value.setValue("61444")

        result = pg.setPgn(value)
        assert result is pg
        assert pg.getPgn() is value
        pg.setPgn(None)
        assert pg.getPgn() is value

    def test_get_set_requestable(self):
        pg = J1939TpPg()
        value = Boolean()
        value.setValue(True)

        result = pg.setRequestable(value)
        assert result is pg
        assert pg.getRequestable() is value
        pg.setRequestable(None)
        assert pg.getRequestable() is value

    def test_sdu_refs(self):
        pg = J1939TpPg()
        ref1 = RefType()
        ref1.setValue("/Pdus/Sdu1")
        ref2 = RefType()
        ref2.setValue("/Pdus/Sdu2")

        result = pg.addSduRef(ref1)
        assert result is pg
        assert ref1 in pg.getSduRefs()
        pg.addSduRef(ref2)
        assert len(pg.getSduRefs()) == 2

        pg.addSduRef(None)
        assert len(pg.getSduRefs()) == 2

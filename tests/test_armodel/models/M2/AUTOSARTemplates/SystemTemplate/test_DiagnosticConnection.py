import typing
from typing import Optional

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection import DiagnosticConnection, TpConnection, TpConnectionIdent

SPEC_NOTE = "DiagnosticConncection that is used to describe the relationship between several TP connections."


class _ConcreteTpConnection(TpConnection):
    pass


class TestTpConnection:
    # Table 6.272, p.633 — class Note verbatim from the markdown
    SPEC_NOTE_TP_CONNECTION = "TpConnection Base Class."
    IDENT_NOTE = "This adds the ability to become referrable to Tp Connection."

    def test_docstring_is_spec_note_verbatim(self):
        assert TpConnection.__doc__.strip() == self.SPEC_NOTE_TP_CONNECTION

    def test_init_has_no_docstring(self):
        assert TpConnection.__init__.__doc__ is None

    def test_abstract_instantiation_raises(self):
        with pytest.raises(TypeError):
            TpConnection()

    def test_initialization(self):
        connection = _ConcreteTpConnection()
        assert connection.getIdent() is None

    def test_ident_factory(self):
        connection = _ConcreteTpConnection()
        ident = connection.createTpConnectionIdent("connIdent")
        assert isinstance(ident, TpConnectionIdent)
        assert connection.getIdent() is ident
        assert connection.createTpConnectionIdent("other") is ident

    def test_accessors_docstring_is_spec_note_verbatim(self):
        assert TpConnection.getIdent.__doc__.strip() == self.IDENT_NOTE
        assert TpConnection.createTpConnectionIdent.__doc__.strip() == self.IDENT_NOTE

    def test_type_hints_pins(self):
        assert typing.get_type_hints(TpConnection.getIdent).get("return") == Optional[TpConnectionIdent]
        assert typing.get_type_hints(TpConnection.createTpConnectionIdent).get("short_name") is str
        assert typing.get_type_hints(TpConnection.createTpConnectionIdent).get("return") is TpConnectionIdent


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


class Test_DiagnosticConnection:
    """Test cases for DiagnosticConnection class."""

    def test_class_docstring_is_spec_note(self):
        """Test that the class docstring carries the spec Note verbatim (DEXT Table 4.17)"""
        assert DiagnosticConnection.__doc__.strip() == SPEC_NOTE

    def test_init_has_no_docstring(self):
        """Test that __init__ carries no docstring"""
        assert DiagnosticConnection.__init__.__doc__ is None

    def test_DiagnosticConnection(self):
        """Test DiagnosticConnection class functionality."""
        parent = MockParent()
        diag_conn = DiagnosticConnection(parent, "test_diag_conn")

        assert isinstance(diag_conn, ARElement)

        # Test default values
        assert diag_conn.getFunctionalRequestRefs() == []
        assert diag_conn.getPeriodicResponseUudtRefs() == []
        assert diag_conn.getPhysicalRequestRef() is None
        assert diag_conn.getResponseRef() is None
        assert diag_conn.getResponseOnEventRef() is None

        # Test adding functional request refs
        mock_ref1 = "ref1"
        mock_ref2 = "ref2"
        diag_conn.addFunctionalRequestRef(mock_ref1)
        diag_conn.addFunctionalRequestRef(mock_ref2)
        assert diag_conn.getFunctionalRequestRefs() == [mock_ref1, mock_ref2]

        # Test adding periodic response refs
        diag_conn.addPeriodicResponseUudtRef(mock_ref1)
        diag_conn.addPeriodicResponseUudtRef(mock_ref2)
        assert diag_conn.getPeriodicResponseUudtRefs() == [mock_ref1, mock_ref2]

        # Test setter methods
        diag_conn.setPhysicalRequestRef(mock_ref1)
        assert diag_conn.getPhysicalRequestRef() == mock_ref1

        diag_conn.setResponseRef(mock_ref2)
        assert diag_conn.getResponseRef() == mock_ref2

        diag_conn.setResponseOnEventRef(mock_ref1)
        assert diag_conn.getResponseOnEventRef() == mock_ref1

    def test_setters_none_is_noop(self):
        """Test that guarded setters ignore None (round-trip + None no-op)"""
        parent = MockParent()
        conn = DiagnosticConnection(parent, "conn")
        ref = RefType().setValue("/Tp/Conn")

        conn.setPhysicalRequestRef(ref)
        conn.setPhysicalRequestRef(None)
        assert conn.getPhysicalRequestRef() == ref

        conn.setResponseRef(ref)
        conn.setResponseRef(None)
        assert conn.getResponseRef() == ref

        conn.setResponseOnEventRef(ref)
        conn.setResponseOnEventRef(None)
        assert conn.getResponseOnEventRef() == ref

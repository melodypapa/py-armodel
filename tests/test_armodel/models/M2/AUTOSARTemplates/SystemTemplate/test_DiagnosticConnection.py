from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection import DiagnosticConnection

SPEC_NOTE = "DiagnosticConncection that is used to describe the relationship between several TP connections."


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

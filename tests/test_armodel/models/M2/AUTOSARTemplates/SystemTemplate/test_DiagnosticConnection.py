
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection import DiagnosticConnection
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import ARElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


class Test_DiagnosticConnection:
    """Test cases for DiagnosticConnection class."""
    
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
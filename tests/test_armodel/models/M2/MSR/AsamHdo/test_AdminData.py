"""
This module contains tests for the AdminData module in MSR.AsamHdo.
"""
from armodel.models.M2.MSR.AsamHdo.AdminData import *
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultiLanguageOverviewParagraph, MultiLanguagePlainText
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import LEnum
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DateTime, NameToken, RevisionLabelString, String


class TestModification:
    """Test class for Modification class."""
    
    def test_modification_initialization(self):
        """Test that a Modification object can be initialized with default values."""
        modification = Modification()
        assert modification.change is None
        assert modification.reason is None
    
    def test_modification_setters_and_getters(self):
        """Test the setters and getters for Modification class."""
        modification = Modification()
        
        # Create a test MultiLanguageOverviewParagraph object
        change_paragraph = MultiLanguageOverviewParagraph()
        reason_paragraph = MultiLanguageOverviewParagraph()
        
        # Test setChange and getChange
        result = modification.setChange(change_paragraph)
        assert modification.getChange() == change_paragraph
        assert result == modification  # Should return self for method chaining
        
        # Test setReason and getReason
        result = modification.setReason(reason_paragraph)
        assert modification.getReason() == reason_paragraph
        assert result == modification  # Should return self for method chaining


class TestDocRevision:
    """Test class for DocRevision class."""
    
    def test_doc_revision_initialization(self):
        """Test that a DocRevision object can be initialized with default values."""
        doc_revision = DocRevision()
        assert doc_revision.date is None
        assert doc_revision.issuedBy is None
        assert doc_revision.modifications == []
        assert doc_revision.revisionLabel is None
        assert doc_revision.revisionLabelP1 is None
        assert doc_revision.revisionLabelP2 is None
        assert doc_revision.state is None
    
    def test_doc_revision_setters_and_getters(self):
        """Test the setters and getters for DocRevision class."""
        doc_revision = DocRevision()
        
        # Create test objects
        date_obj = DateTime()
        issued_by_str = String()
        modification_obj = Modification()
        revision_label = RevisionLabelString()
        name_token = NameToken()
        
        # Test setDate and getDate
        result = doc_revision.setDate(date_obj)
        assert doc_revision.getDate() == date_obj
        assert result == doc_revision
        
        # Test setIssuedBy and getIssuedBy
        result = doc_revision.setIssuedBy(issued_by_str)
        assert doc_revision.getIssuedBy() == issued_by_str
        assert result == doc_revision
        
        # Test addModification and getModifications
        result = doc_revision.addModification(modification_obj)
        assert modification_obj in doc_revision.getModifications()
        assert result == doc_revision
        
        # Test setRevisionLabel and getRevisionLabel
        result = doc_revision.setRevisionLabel(revision_label)
        assert doc_revision.getRevisionLabel() == revision_label
        assert result == doc_revision
        
        # Test setRevisionLabelP1 and getRevisionLabelP1
        result = doc_revision.setRevisionLabelP1(revision_label)
        assert doc_revision.getRevisionLabelP1() == revision_label
        assert result == doc_revision
        
        # Test setRevisionLabelP2 and getRevisionLabelP2
        result = doc_revision.setRevisionLabelP2(revision_label)
        assert doc_revision.getRevisionLabelP2() == revision_label
        assert result == doc_revision
        
        # Test setState and getState
        result = doc_revision.setState(name_token)
        assert doc_revision.getState() == name_token
        assert result == doc_revision


class TestAdminData:
    """Test class for AdminData class."""
    
    def test_admin_data_initialization(self):
        """Test that an AdminData object can be initialized with default values."""
        admin_data = AdminData()
        assert admin_data.DocRevisions == []
        assert admin_data.language is None
        assert admin_data.sdgs == []
        assert admin_data.usedLanguages is None
    
    def test_admin_data_add_doc_revision(self):
        """Test adding document revisions to AdminData."""
        admin_data = AdminData()
        doc_revision = DocRevision()
        
        # Test addDocRevision and getDocRevisions
        result = admin_data.addDocRevision(doc_revision)
        assert doc_revision in admin_data.getDocRevisions()
        assert result == admin_data
    
    def test_admin_data_language_methods(self):
        """Test language-related methods in AdminData."""
        admin_data = AdminData()
        language = LEnum()
        
        # Test setLanguage and getLanguage
        result = admin_data.setLanguage(language)
        assert admin_data.getLanguage() == language
        assert result == admin_data
    
    def test_admin_data_sdgs_methods(self):
        """Test special data group (sdg) related methods in AdminData."""
        admin_data = AdminData()
        sdg_item = "test_sdg"
        
        # Test addSdg and getSdgs
        result = admin_data.addSdg(sdg_item)
        assert sdg_item in admin_data.getSdgs()
        assert result == admin_data
    
    def test_admin_data_used_languages_methods(self):
        """Test used languages methods in AdminData."""
        admin_data = AdminData()
        used_languages = MultiLanguagePlainText()
        
        # Test setUsedLanguages and getUsedLanguages
        result = admin_data.setUsedLanguages(used_languages)
        assert admin_data.getUsedLanguages() == used_languages
        assert result == admin_data
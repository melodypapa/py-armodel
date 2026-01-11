import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.Keyword import Keyword, KeywordSet
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import NameToken


class TestKeyword:
    def test_initialization(self):
        """Test Keyword initialization"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        keyword = Keyword(ar_root, "TestKeyword")
        
        assert keyword is not None
        assert keyword.getShortName() == "TestKeyword"
        assert keyword.abbrName is None
        assert keyword.classifications == []

    def test_get_abbr_name(self):
        """Test getAbbrName method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        keyword = Keyword(ar_root, "TestKeyword")
        assert keyword.getAbbrName() is None

    def test_set_abbr_name(self):
        """Test setAbbrName method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        keyword = Keyword(ar_root, "TestKeyword")
        test_value = NameToken().setValue("TEST")
        result = keyword.setAbbrName(test_value)
        assert result is keyword
        assert keyword.getAbbrName() == test_value

    def test_set_abbr_name_none(self):
        """Test setAbbrName with None value"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        keyword = Keyword(ar_root, "TestKeyword")
        result = keyword.setAbbrName(None)
        assert result is keyword
        assert keyword.getAbbrName() is None

    def test_get_classifications(self):
        """Test getClassifications method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        keyword = Keyword(ar_root, "TestKeyword")
        assert keyword.getClassifications() == []

    def test_add_classification(self):
        """Test addClassification method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        keyword = Keyword(ar_root, "TestKeyword")
        test_value = NameToken().setValue("Classification1")
        result = keyword.addClassification(test_value)
        assert result is keyword
        assert len(keyword.getClassifications()) == 1
        assert keyword.getClassifications()[0] == test_value

    def test_add_classification_none(self):
        """Test addClassification with None value"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        keyword = Keyword(ar_root, "TestKeyword")
        result = keyword.addClassification(None)
        assert result is keyword
        assert len(keyword.getClassifications()) == 0

    def test_all_properties(self):
        """Test setting all properties"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        keyword = Keyword(ar_root, "TestKeyword")
        
        abbr_value = NameToken().setValue("TEST")
        class_value = NameToken().setValue("Classification1")
        
        keyword.setAbbrName(abbr_value)
        keyword.addClassification(class_value)
        
        assert keyword.getAbbrName() == abbr_value
        assert len(keyword.getClassifications()) == 1
        assert keyword.getClassifications()[0] == class_value


class TestKeywordSet:
    def test_initialization(self):
        """Test KeywordSet initialization"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        keyword_set = KeywordSet(ar_root, "TestKeywordSet")
        
        assert keyword_set is not None
        assert keyword_set.getShortName() == "TestKeywordSet"
        assert keyword_set.keywords == []

    def test_get_keywords(self):
        """Test getKeywords method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        keyword_set = KeywordSet(ar_root, "TestKeywordSet")
        assert keyword_set.getKeywords() == []

    def test_create_keyword(self):
        """Test createKeyword method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        keyword_set = KeywordSet(ar_root, "TestKeywordSet")
        
        keyword = keyword_set.createKeyword("NewKeyword")
        assert keyword is not None
        assert keyword.getShortName() == "NewKeyword"
        assert keyword in keyword_set.getKeywords()
        assert len(keyword_set.getKeywords()) == 1

    def test_create_keyword_duplicate(self):
        """Test createKeyword with duplicate name"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        keyword_set = KeywordSet(ar_root, "TestKeywordSet")
        
        keyword1 = keyword_set.createKeyword("TestKeyword")
        keyword2 = keyword_set.createKeyword("TestKeyword")  # Should return same instance
        
        assert keyword1 is keyword2
        assert len(keyword_set.getKeywords()) == 1

    def test_keyword_properties(self):
        """Test properties of created Keyword through KeywordSet"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        keyword_set = KeywordSet(ar_root, "TestKeywordSet")
        
        keyword = keyword_set.createKeyword("TestKeyword")
        
        # Test keyword properties
        abbr_value = NameToken().setValue("TEST")
        keyword.setAbbrName(abbr_value)
        
        assert keyword.getAbbrName() == abbr_value
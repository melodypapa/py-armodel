"""
This module contains tests for the SpecialData module in MSR.AsamHdo.
"""
import pytest
from armodel.models.M2.MSR.AsamHdo.SpecialData import *
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultiLanguageOverviewParagraph
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARPackage


class TestSd:
    """Test class for Sd class."""
    
    def test_sd_initialization(self):
        """Test that an Sd object can be initialized with default values."""
        sd = Sd()
        assert sd.gid == ""
        assert sd.value == ""
    
    def test_sd_gid_methods(self):
        """Test the gid getter and setter."""
        sd = Sd()
        gid_value = "test_gid"
        
        result = sd.setGID(gid_value)
        assert sd.getGID() == gid_value
        assert result == sd
    
    def test_sd_value_methods(self):
        """Test the value getter and setter."""
        sd = Sd()
        value = "test_value"
        
        result = sd.setValue(value)
        assert sd.getValue() == value
        assert result == sd


class TestSdgCaption:
    """Test class for SdgCaption class."""
    
    def test_sdg_caption_initialization(self):
        """Test that an SdgCaption object can be initialized with default values."""
        parent_obj = ARPackage(None, "parent_test")  # Using ARPackage as a concrete ARObject subclass
        sdg_caption = SdgCaption(parent_obj, "test_name")
        assert sdg_caption.desc is None
    
    def test_sdg_caption_desc_methods(self):
        """Test the desc getter and setter."""
        parent_obj = ARPackage(None, "parent_test")  # Using ARPackage as a concrete ARObject subclass
        sdg_caption = SdgCaption(parent_obj, "test_name")
        desc = MultiLanguageOverviewParagraph()
        
        result = sdg_caption.setDesc(desc)
        assert sdg_caption.getDesc() == desc
        assert result == sdg_caption


class TestSdg:
    """Test class for Sdg class."""
    
    def test_sdg_initialization(self):
        """Test that an Sdg object can be initialized with default values."""
        sdg = Sdg()
        assert sdg.gid == ""
        assert sdg.sd == []
        assert sdg.sdgCaption is None
        assert sdg.sdgContentsTypes == []
        assert sdg.sdxRefs == []
    
    def test_sdg_gid_methods(self):
        """Test the gid getter and setter."""
        sdg = Sdg()
        gid_value = "test_gid"
        
        result = sdg.setGID(gid_value)
        assert sdg.getGID() == gid_value
        assert result == sdg
    
    def test_sdg_sd_methods(self):
        """Test adding and getting special data items."""
        sdg = Sdg()
        sd_item = Sd()
        
        result = sdg.addSd(sd_item)
        sds = sdg.getSds()
        assert sd_item in sds
        assert result == sdg
    
    def test_sdg_caption_methods(self):
        """Test the caption getter and creation."""
        sdg = Sdg()
        caption = sdg.createSdgCaption("test_caption")
        
        assert sdg.getSdgCaption() == caption
        assert caption.desc is None
        
        # Test that the caption is properly attached
        assert caption.parent == sdg
        assert caption.short_name == "test_caption"
    
    def test_sdg_contents_types_methods(self):
        """Test adding and getting special data group content types."""
        sdg = Sdg()
        sdg_content = Sdg()  # Create another Sdg instance
        
        sdg.addSdgContentsType(sdg_content)
        contents = sdg.getSdgContentsTypes()
        assert sdg_content in contents
    
    def test_sdg_refs_methods(self):
        """Test adding and getting special data extended references."""
        sdg = Sdg()
        ref = RefType()
        
        result = sdg.addSdxRef(ref)
        refs = sdg.getSdxRefs()
        assert ref in refs
        assert result == sdg
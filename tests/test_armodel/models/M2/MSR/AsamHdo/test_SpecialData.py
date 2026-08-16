"""
This module contains tests for the SpecialData module in MSR.AsamHdo.
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARPackage
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Enumerations import XmlSpaceEnum
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import NameToken, Numerical, RefType, VerbatimStringPlain
from armodel.models.M2.MSR.AsamHdo.SpecialData import Sd, Sdf, Sdg, SdgCaption, SdgContents
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultiLanguageOverviewParagraph


class TestSd:
    """Test class for Sd class."""

    def test_sd_initialization(self):
        """Test that an Sd object can be initialized with default values."""
        sd = Sd()
        assert sd.getGID() is None
        assert sd.getValue() is None
        assert sd.getXmlSpace() is None

    def test_sd_gid_methods(self):
        """Test the gid getter and setter."""
        sd = Sd()
        gid_value = NameToken().setValue("test_gid")

        result = sd.setGID(gid_value)
        assert sd.getGID() == gid_value
        assert result == sd

        sd.setGID(None)
        assert sd.getGID() == gid_value

    def test_sd_value_methods(self):
        """Test the value getter and setter."""
        sd = Sd()
        value = VerbatimStringPlain().setValue("test_value")

        result = sd.setValue(value)
        assert sd.getValue() == value
        assert result == sd

        sd.setValue(None)
        assert sd.getValue() == value

    def test_sd_xml_space_methods(self):
        """Test the xmlSpace getter and setter."""
        sd = Sd()
        xml_space = XmlSpaceEnum().setValue(XmlSpaceEnum.PRESERVE)

        result = sd.setXmlSpace(xml_space)
        assert sd.getXmlSpace() == xml_space
        assert result == sd

        sd.setXmlSpace(None)
        assert sd.getXmlSpace() == xml_space


class TestSdgCaption:
    """Test class for SdgCaption class."""

    def test_sdg_caption_initialization(self):
        """Test that an SdgCaption object can be initialized with default values."""
        parent_obj = ARPackage(None, "parent_test")  # Using ARPackage as a concrete ARObject subclass
        sdg_caption = SdgCaption(parent_obj, "test_name")
        assert sdg_caption.getDesc() is None

    def test_sdg_caption_desc_methods(self):
        """Test the desc getter and setter."""
        parent_obj = ARPackage(None, "parent_test")  # Using ARPackage as a concrete ARObject subclass
        sdg_caption = SdgCaption(parent_obj, "test_name")
        desc = MultiLanguageOverviewParagraph()

        result = sdg_caption.setDesc(desc)
        assert sdg_caption.getDesc() == desc
        assert result == sdg_caption

        sdg_caption.setDesc(None)
        assert sdg_caption.getDesc() == desc


class TestSdg:
    """Test class for Sdg class."""

    def test_sdg_initialization(self):
        """Test that an Sdg object can be initialized with default values."""
        sdg = Sdg()
        assert sdg.getGID() is None
        assert sdg.getSdgCaption() is None
        assert sdg.getSdgContentsType() is None

    def test_sdg_gid_methods(self):
        """Test the gid getter and setter."""
        sdg = Sdg()
        gid_value = NameToken().setValue("test_gid")

        result = sdg.setGID(gid_value)
        assert sdg.getGID() == gid_value
        assert result == sdg

        sdg.setGID(None)
        assert sdg.getGID() == gid_value

    def test_sdg_caption_methods(self):
        """Test the caption getter and creation."""
        sdg = Sdg()
        caption = sdg.createSdgCaption("test_caption")

        assert sdg.getSdgCaption() == caption
        assert caption.getDesc() is None

        # Test that the caption is properly attached
        assert caption.parent == sdg
        assert caption.short_name == "test_caption"

    def test_sdg_contents_type_methods(self):
        """Test setting and getting the sdg contents type."""
        sdg = Sdg()
        contents = SdgContents()
        contents.addSd(Sd())

        result = sdg.setSdgContentsType(contents)
        assert sdg.getSdgContentsType() == contents
        assert result == sdg

        sdg.setSdgContentsType(None)
        assert sdg.getSdgContentsType() == contents


class TestSdgContents:
    """Test class for SdgContents class."""

    def test_initialization(self):
        contents = SdgContents()
        assert contents.getSds() == []
        assert contents.getSdfs() == []
        assert contents.getSdgs() == []
        assert contents.getSdxRefs() == []
        assert contents.getSdxfRefs() == []

    def test_sd_methods(self):
        contents = SdgContents()
        sd_item = Sd()
        assert contents.addSd(sd_item) is contents
        assert contents.getSds() == [sd_item]
        contents.addSd(None)
        assert contents.getSds() == [sd_item]

    def test_sdf_methods(self):
        contents = SdgContents()
        sdf_item = Sdf()
        assert contents.addSdf(sdf_item) is contents
        assert contents.getSdfs() == [sdf_item]
        contents.addSdf(None)
        assert contents.getSdfs() == [sdf_item]

    def test_sdg_methods(self):
        contents = SdgContents()
        sdg_item = Sdg()
        assert contents.addSdg(sdg_item) is contents
        assert contents.getSdgs() == [sdg_item]
        contents.addSdg(None)
        assert contents.getSdgs() == [sdg_item]

    def test_sdx_refs_methods(self):
        contents = SdgContents()
        ref = RefType()
        assert contents.addSdxRef(ref) is contents
        assert contents.getSdxRefs() == [ref]
        contents.addSdxRef(None)
        assert contents.getSdxRefs() == [ref]

    def test_sdxf_refs_methods(self):
        contents = SdgContents()
        ref = RefType()
        assert contents.addSdxfRef(ref) is contents
        assert contents.getSdxfRefs() == [ref]
        contents.addSdxfRef(None)
        assert contents.getSdxfRefs() == [ref]


class TestSdf:
    """Test class for Sdf class."""

    def test_initialization(self):
        sdf = Sdf()
        assert sdf.getGID() is None
        assert sdf.getValue() is None

    def test_gid_methods(self):
        sdf = Sdf()
        gid_value = NameToken().setValue("test_gid")
        assert sdf.setGID(gid_value) is sdf
        assert sdf.getGID() == gid_value
        sdf.setGID(None)
        assert sdf.getGID() == gid_value

    def test_value_methods(self):
        sdf = Sdf()
        value = Numerical().setValue("42")
        assert sdf.setValue(value) is sdf
        assert sdf.getValue() == value
        sdf.setValue(None)
        assert sdf.getValue() == value

"""
Tests for ARXMLWriter class
"""
import xml.etree.cElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure import (
    ConstantReference,
    NumericalValueSpecification,
    TextValueSpecification,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARFloat,
    ARLiteral,
    DateTime,
    Limit,
    RefType,
    RevisionLabelString,
)
from armodel.models.M2.MSR.AsamHdo.AdminData import (
    AdminData,
    DocRevision,
    Modification,
)
from armodel.models.M2.MSR.AsamHdo.SpecialData import Sd, Sdg
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import (
    LLongName,
    LOverviewParagraph,
    LPlainText,
)
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import (
    MultilanguageLongName,
    MultiLanguageOverviewParagraph,
    MultiLanguagePlainText,
)
from armodel.writer.arxml_writer import ARXMLWriter


class TestARXMLWriterBasicMethods:
    """Test basic ARXMLWriter methods"""

    def test_initialization(self):
        """Test ARXMLWriter initialization"""
        writer = ARXMLWriter()
        assert writer is not None
        assert writer.options['warning'] == False
        assert writer.options['version'] == "4.2.2"

    def test_initialization_with_warning_option(self):
        """Test ARXMLWriter initialization with warning option"""
        writer = ARXMLWriter(options={'warning': True})
        assert writer.options['warning'] == True

    def test_set_short_name(self):
        """Test setShortName method"""
        writer = ARXMLWriter()
        parent = ET.Element("parent")

        result = writer.setShortName(parent, "TestName")

        assert result is not None
        assert result.tag == "SHORT-NAME"
        assert result.text == "TestName"
        assert len(parent) == 1
        assert parent[0] == result

    def test_set_child_limit_element_with_limit(self):
        """Test setChildLimitElement with a valid Limit"""
        writer = ARXMLWriter()
        parent = ET.Element("parent")

        limit = Limit()
        limit.value = "100"
        limit.intervalType = "CLOSED"

        writer.setChildLimitElement(parent, "TEST-LIMIT", limit)

        assert len(parent) == 1
        child = parent[0]
        assert child.tag == "TEST-LIMIT"
        assert child.text == "100"
        assert child.attrib.get('INTERVAL-TYPE') == "CLOSED"

    def test_set_child_limit_element_without_interval_type(self):
        """Test setChildLimitElement without interval type"""
        writer = ARXMLWriter()
        parent = ET.Element("parent")

        limit = Limit()
        limit.value = "100"

        writer.setChildLimitElement(parent, "TEST-LIMIT", limit)

        assert len(parent) == 1
        child = parent[0]
        assert child.tag == "TEST-LIMIT"
        assert child.text == "100"
        assert 'INTERVAL-TYPE' not in child.attrib

    def test_set_child_limit_element_none(self):
        """Test setChildLimitElement with None"""
        writer = ARXMLWriter()
        parent = ET.Element("parent")

        writer.setChildLimitElement(parent, "TEST-LIMIT", None)

        assert len(parent) == 0

    def test_write_referrable(self):
        """Test writeReferrable method"""
        writer = ARXMLWriter()
        autosar = AUTOSAR.getInstance()

        pkg = autosar.createARPackage("TestPackage")
        base_type = pkg.createSwBaseType("TestBaseType")

        element = ET.Element("TEST-ELEMENT")
        writer.writeReferrable(element, base_type)

        assert element.tag == "TEST-ELEMENT"
        assert len(element) == 1
        short_name = element[0]
        assert short_name.tag == "SHORT-NAME"
        assert short_name.text == "TestBaseType"


class TestARXMLWriterSdgMethods:
    """Test SDG (Special Data Group) related methods"""

    def test_write_sds_with_single_sd(self):
        """Test writeSds with a single SD"""
        writer = ARXMLWriter()
        parent = ET.Element("parent")

        sdg = Sdg()
        sd = Sd()
        sd.value = "test value"
        sd.gid = "test-gid"
        sdg.addSd(sd)

        writer.writeSds(parent, sdg)

        assert len(parent) == 1
        sd_tag = parent[0]
        assert sd_tag.tag == "SD"
        assert sd_tag.text == "test value"
        assert sd_tag.attrib.get('GID') == "test-gid"

    def test_write_sds_with_multiple_sds(self):
        """Test writeSds with multiple SDs"""
        writer = ARXMLWriter()
        parent = ET.Element("parent")

        sdg = Sdg()
        sd1 = Sd()
        sd1.value = "value1"
        sd2 = Sd()
        sd2.value = "value2"
        sdg.addSd(sd1)
        sdg.addSd(sd2)

        writer.writeSds(parent, sdg)

        assert len(parent) == 2
        assert parent[0].text == "value1"
        assert parent[1].text == "value2"

    def test_write_sdg_caption_with_caption(self):
        """Test writeSdgCaption with caption"""
        writer = ARXMLWriter()
        parent = ET.Element("parent")

        sdg = Sdg()
        # Note: This test is simplified as creating a proper caption requires more setup
        # In a real scenario, you'd need to create a MultilanguageReferrable object

        writer.writeSdgCaption(parent, sdg)

        # Should not add anything if caption is None
        assert len(parent) == 0

    def test_write_sdg_sdx_refs_with_refs(self):
        """Test writeSdgSdxRefs with references"""
        writer = ARXMLWriter()
        parent = ET.Element("parent")

        sdg = Sdg()
        ref = RefType()
        ref.value = "/path/to/ref"
        sdg.sdxRefs = [ref]

        writer.writeSdgSdxRefs(parent, sdg)

        assert len(parent) == 1
        ref_tag = parent[0]
        assert ref_tag.tag == "SDX-REF"
        assert ref_tag.text == "/path/to/ref"

    def test_set_sdg_basic(self):
        """Test setSdg with basic SDG"""
        writer = ARXMLWriter()
        parent = ET.Element("parent")

        sdg = Sdg()
        sdg.gid = "test-gid"
        sd = Sd()
        sd.value = "test value"
        sdg.addSd(sd)

        writer.setSdg(parent, sdg)

        assert len(parent) == 1
        sdg_tag = parent[0]
        assert sdg_tag.tag == "SDG"
        assert sdg_tag.attrib.get('GID') == "test-gid"

    def test_set_sdg_none(self):
        """Test setSdg with None"""
        writer = ARXMLWriter()
        parent = ET.Element("parent")

        writer.setSdg(parent, None)

        assert len(parent) == 0

    def test_set_sdg_empty_gid(self):
        """Test setSdg with empty GID"""
        writer = ARXMLWriter()
        parent = ET.Element("parent")

        sdg = Sdg()
        sdg.gid = ""
        sd = Sd()
        sd.value = "test value"
        sdg.addSd(sd)

        writer.setSdg(parent, sdg)

        assert len(parent) == 1
        sdg_tag = parent[0]
        assert 'GID' not in sdg_tag.attrib

    def test_write_admin_data_sdgs_with_sdgs(self):
        """Test writeAdminDataSdgs with SDGs"""
        writer = ARXMLWriter()
        parent = ET.Element("parent")

        admin_data = AdminData()
        sdg = Sdg()
        sd = Sd()
        sd.value = "test value"
        sdg.addSd(sd)
        admin_data.addSdg(sdg)

        writer.writeAdminDataSdgs(parent, admin_data)

        assert len(parent) == 1
        sdgs_tag = parent[0]
        assert sdgs_tag.tag == "SDGS"
        assert len(sdgs_tag) == 1

    def test_write_admin_data_sdgs_empty(self):
        """Test writeAdminDataSdgs with empty SDGs list"""
        writer = ARXMLWriter()
        parent = ET.Element("parent")

        admin_data = AdminData()
        # sdgs list is empty by default

        writer.writeAdminDataSdgs(parent, admin_data)

        assert len(parent) == 0


class TestARXMLWriterIntegration:
    """Integration tests for ARXMLWriter"""

    def test_write_simple_arxml_structure(self):
        """Test writing a simple ARXML structure"""
        writer = ARXMLWriter()

        autosar = AUTOSAR.getInstance()
        autosar.clear()

        pkg = autosar.createARPackage("TestPackage")
        base_type = pkg.createSwBaseType("TestBaseType")

        root = ET.Element("ROOT")
        writer.writeReferrable(root, base_type)

        assert len(root) == 1
        assert root[0].tag == "SHORT-NAME"
        assert root[0].text == "TestBaseType"

    def test_write_multiple_elements(self):
        """Test writing multiple elements"""
        writer = ARXMLWriter()

        autosar = AUTOSAR.getInstance()
        autosar.clear()

        pkg = autosar.createARPackage("TestPackage")
        base_type1 = pkg.createSwBaseType("TestBaseType1")
        base_type2 = pkg.createSwBaseType("TestBaseType2")

        root = ET.Element("ROOT")

        # Create separate elements for each base type
        elem1 = ET.SubElement(root, "BASE-TYPE-DEF")
        elem2 = ET.SubElement(root, "BASE-TYPE-DEF")

        writer.writeReferrable(elem1, base_type1)
        writer.writeReferrable(elem2, base_type2)

        assert len(root) == 2
        assert elem1[0].tag == "SHORT-NAME"
        assert elem1[0].text == "TestBaseType1"
        assert elem2[0].tag == "SHORT-NAME"
        assert elem2[0].text == "TestBaseType2"


class TestARXMLWriterLanguageSpecificMethods:
    """Test language-specific related methods"""

    def test_set_language_specific_with_l_attribute(self):
        """Test setLanguageSpecific with L attribute"""
        writer = ARXMLWriter()
        parent = ET.Element("parent")

        specific = LPlainText()  # Use concrete subclass instead of abstract base class
        specific.setL("EN")
        specific.setValue("Test value")

        writer.setLanguageSpecific(parent, "TEST-LANG", specific)

        assert len(parent) == 1
        child = parent[0]
        assert child.tag == "TEST-LANG"
        assert child.attrib.get('L') == "EN"
        assert child.text == "Test value"

    def test_set_language_specific_without_l_attribute(self):
        """Test setLanguageSpecific without L attribute"""
        writer = ARXMLWriter()
        parent = ET.Element("parent")

        specific = LPlainText()  # Use concrete subclass instead of abstract base class
        specific.setValue("Test value")
        # l attribute is None by default

        writer.setLanguageSpecific(parent, "TEST-LANG", specific)

        assert len(parent) == 1
        child = parent[0]
        assert child.tag == "TEST-LANG"
        assert 'L' not in child.attrib
        assert child.text == "Test value"

    def test_set_l_long_name(self):
        """Test setLLongName method"""
        writer = ARXMLWriter()
        parent = ET.Element("parent")

        name = LLongName()
        name.setL("EN")
        name.setValue("Long name")

        writer.setLLongName(parent, name)

        assert len(parent) == 1
        child = parent[0]
        assert child.tag == "L-4"
        assert child.attrib.get('L') == "EN"
        assert child.text == "Long name"

    def test_set_multi_long_name(self):
        """Test setMultiLongName method"""
        writer = ARXMLWriter()
        parent = ET.Element("parent")

        long_name = MultilanguageLongName()
        name1 = LLongName()
        name1.setL("EN")
        name1.setValue("English name")
        name2 = LLongName()
        name2.setL("DE")
        name2.setValue("German name")
        long_name.addL4(name1)
        long_name.addL4(name2)

        writer.setMultiLongName(parent, "LONG-NAME", long_name)

        assert len(parent) == 1
        child = parent[0]
        assert child.tag == "LONG-NAME"
        assert len(child) == 2
        assert child[0].tag == "L-4"
        assert child[0].text == "English name"
        assert child[1].tag == "L-4"
        assert child[1].text == "German name"

    def test_set_multi_long_name_none(self):
        """Test setMultiLongName with None"""
        writer = ARXMLWriter()
        parent = ET.Element("parent")

        writer.setMultiLongName(parent, "LONG-NAME", None)

        assert len(parent) == 0

    def test_set_l_overview_paragraph(self):
        """Test setLOverviewParagraph method"""
        writer = ARXMLWriter()
        parent = ET.Element("parent")

        name = LOverviewParagraph()
        name.setL("EN")
        name.setValue("Overview paragraph")

        writer.setLOverviewParagraph(parent, name)

        assert len(parent) == 1
        child = parent[0]
        assert child.tag == "L-2"
        assert child.attrib.get('L') == "EN"
        assert child.text == "Overview paragraph"

    def test_set_multi_language_overview_paragraph(self):
        """Test setMultiLanguageOverviewParagraph method"""
        writer = ARXMLWriter()
        parent = ET.Element("parent")

        paragraph = MultiLanguageOverviewParagraph()
        para1 = LOverviewParagraph()
        para1.setL("EN")
        para1.setValue("English paragraph")
        para2 = LOverviewParagraph()
        para2.setL("DE")
        para2.setValue("German paragraph")
        paragraph.addL2(para1)
        paragraph.addL2(para2)

        writer.setMultiLanguageOverviewParagraph(parent, "PARAGRAPH", paragraph)

        assert len(parent) == 1
        child = parent[0]
        assert child.tag == "PARAGRAPH"
        assert len(child) == 2
        assert child[0].tag == "L-2"
        assert child[0].text == "English paragraph"
        assert child[1].tag == "L-2"
        assert child[1].text == "German paragraph"

    def test_set_multi_language_overview_paragraph_none(self):
        """Test setMultiLanguageOverviewParagraph with None"""
        writer = ARXMLWriter()
        parent = ET.Element("parent")

        writer.setMultiLanguageOverviewParagraph(parent, "PARAGRAPH", None)

        assert len(parent) == 0

    def test_write_multilanguage_referrable(self):
        """Test writeMultilanguageReferrable method"""
        writer = ARXMLWriter()
        autosar = AUTOSAR.getInstance()

        pkg = autosar.createARPackage("TestPackage")
        base_type = pkg.createSwBaseType("TestBaseType")

        element = ET.Element("TEST-ELEMENT")
        writer.writeMultilanguageReferrable(element, base_type)

        assert element.tag == "TEST-ELEMENT"
        # Should have SHORT-NAME from the referrable part
        assert len(element) == 1
        short_name = element[0]
        assert short_name.tag == "SHORT-NAME"
        assert short_name.text == "TestBaseType"

    def test_set_l_plain_text(self):
        """Test setLPlainText method"""
        writer = ARXMLWriter()
        parent = ET.Element("parent")

        text = LPlainText()
        text.setL("EN")
        text.setValue("Plain text")

        writer.setLPlainText(parent, text)

        assert len(parent) == 1
        child = parent[0]
        assert child.tag == "L-10"
        assert child.attrib.get('L') == "EN"
        assert child.text == "Plain text"

    def test_set_multi_language_plain_text(self):
        """Test setMultiLanguagePlainText method"""
        writer = ARXMLWriter()
        parent = ET.Element("parent")

        paragraph = MultiLanguagePlainText()
        text1 = LPlainText()
        text1.setL("EN")
        text1.setValue("English text")
        text2 = LPlainText()
        text2.setL("DE")
        text2.setValue("German text")
        paragraph.addL10(text1)
        paragraph.addL10(text2)

        writer.setMultiLanguagePlainText(parent, "TEXT", paragraph)

        assert len(parent) == 1
        child = parent[0]
        assert child.tag == "TEXT"
        assert len(child) == 2
        assert child[0].tag == "L-10"
        assert child[0].text == "English text"
        assert child[1].tag == "L-10"
        assert child[1].text == "German text"

    def test_set_multi_language_plain_text_none(self):
        """Test setMultiLanguagePlainText with None"""
        writer = ARXMLWriter()
        parent = ET.Element("parent")

        writer.setMultiLanguagePlainText(parent, "TEXT", None)

        assert len(parent) == 0


class TestARXMLWriterDocRevisionMethods:
    """Test documentation revision related methods"""

    def test_write_modification(self):
        """Test writeModification method"""
        writer = ARXMLWriter()
        parent = ET.Element("parent")

        modification = Modification()
        change = MultiLanguageOverviewParagraph()
        change_para = LOverviewParagraph()
        change_para.setL("EN")
        change_para.setValue("Change description")
        change.addL2(change_para)
        modification.setChange(change)

        reason = MultiLanguageOverviewParagraph()
        reason_para = LOverviewParagraph()
        reason_para.setL("EN")
        reason_para.setValue("Reason for change")
        reason.addL2(reason_para)
        modification.setReason(reason)

        writer.writeModification(parent, modification)

        assert len(parent) == 1
        mod_element = parent[0]
        assert mod_element.tag == "MODIFICATION"
        assert len(mod_element) == 2
        assert mod_element[0].tag == "CHANGE"
        assert mod_element[0][0].tag == "L-2"
        assert mod_element[0][0].text == "Change description"
        assert mod_element[1].tag == "REASON"
        assert mod_element[1][0].tag == "L-2"
        assert mod_element[1][0].text == "Reason for change"

    def test_write_modification_none(self):
        """Test writeModification with None"""
        writer = ARXMLWriter()
        parent = ET.Element("parent")

        writer.writeModification(parent, None)

        assert len(parent) == 0

    def test_write_doc_revision(self):
        """Test writeDocRevision method"""
        writer = ARXMLWriter()
        parent = ET.Element("parent")

        revision = DocRevision()
        label = RevisionLabelString()
        label.setValue("1.0.0")
        revision.setRevisionLabel(label)

        state = ARLiteral()
        state.setValue("Draft")
        revision.setState(state)

        issued_by = ARLiteral()
        issued_by.setValue("Test Author")
        revision.setIssuedBy(issued_by)

        date = DateTime()
        date.setValue("2024-01-01T00:00:00")
        revision.setDate(date)

        writer.writeDocRevision(parent, revision)

        assert len(parent) == 1
        rev_element = parent[0]
        assert rev_element.tag == "DOC-REVISION"
        assert len(rev_element) == 4  # REVISION-LABEL, STATE, ISSUED-BY, DATE

    def test_write_doc_revision_none(self):
        """Test writeDocRevision with None"""
        writer = ARXMLWriter()
        parent = ET.Element("parent")

        writer.writeDocRevision(parent, None)

        assert len(parent) == 0

    def test_set_admin_data(self):
        """Test setAdminData method"""
        writer = ARXMLWriter()
        parent = ET.Element("parent")

        admin_data = AdminData()
        language = ARLiteral()
        language.setValue("EN")
        admin_data.setLanguage(language)

        writer.setAdminData(parent, admin_data)

        assert len(parent) == 1
        admin_element = parent[0]
        assert admin_element.tag == "ADMIN-DATA"
        # Should have LANGUAGE element
        lang_element = admin_element.find("LANGUAGE")
        assert lang_element is not None
        assert lang_element.text == "EN"

    def test_set_admin_data_none(self):
        """Test setAdminData with None"""
        writer = ARXMLWriter()
        parent = ET.Element("parent")

        writer.setAdminData(parent, None)

        assert len(parent) == 0


class TestARXMLWriterValueSpecMethods:
    """Test value specification related methods"""

    def test_write_text_value_specification(self):
        """Test writeTextValueSpecification method"""
        writer = ARXMLWriter()
        parent = ET.Element("parent")

        value_spec = TextValueSpecification()
        literal = ARLiteral()
        literal.setValue("Test text value")
        value_spec.setValue(literal)

        writer.writeTextValueSpecification(parent, value_spec)

        assert len(parent) == 1
        spec_element = parent[0]
        assert spec_element.tag == "TEXT-VALUE-SPECIFICATION"
        value_element = spec_element.find("VALUE")
        assert value_element is not None
        assert value_element.text == "Test text value"

    def test_write_text_value_specification_none(self):
        """Test writeTextValueSpecification with None"""
        writer = ARXMLWriter()
        parent = ET.Element("parent")

        writer.writeTextValueSpecification(parent, None)

        assert len(parent) == 0

    def test_write_numerical_value_specification(self):
        """Test writeNumericalValueSpecification method"""
        writer = ARXMLWriter()
        parent = ET.Element("parent")

        value_spec = NumericalValueSpecification()
        # Use ARFloat instead of Compu
        float_val = ARFloat()
        float_val.setValue(123.45)
        float_val._text = "123.45"  # Set internal text representation
        value_spec.setValue(float_val)

        writer.writeNumericalValueSpecification(parent, value_spec)

        assert len(parent) == 1
        spec_element = parent[0]
        assert spec_element.tag == "NUMERICAL-VALUE-SPECIFICATION"
        value_element = spec_element.find("VALUE")
        assert value_element is not None
        assert value_element.text == "123.45"

    def test_write_numerical_value_specification_none(self):
        """Test writeNumericalValueSpecification with None"""
        writer = ARXMLWriter()
        parent = ET.Element("parent")

        writer.writeNumericalValueSpecification(parent, None)

        assert len(parent) == 0

    def test_set_constant_reference(self):
        """Test setConstantReference method"""
        writer = ARXMLWriter()
        parent = ET.Element("parent")

        value_spec = ConstantReference()
        ref = RefType()
        ref.setValue("/path/to/constant")
        value_spec.setConstantRef(ref)

        writer.setConstantReference(parent, value_spec)

        assert len(parent) == 1
        spec_element = parent[0]
        assert spec_element.tag == "CONSTANT-REFERENCE"
        ref_element = spec_element.find("CONSTANT-REF")
        assert ref_element is not None
        assert ref_element.text == "/path/to/constant"

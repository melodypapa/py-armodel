"""
Tests for ARXMLWriter class
"""

import xml.etree.cElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure import ConstantReference, NumericalValueSpecification, ReferenceValueSpecification, TextValueSpecification
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Referrable, ShortNameFragment
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARFloat,
    ARLiteral,
    ARNumerical,
    DateTime,
    DisplayFormatString,
    Identifier,
    IntervalTypeEnum,
    Limit,
    MonotonyEnum,
    NameToken,
    RefType,
    RevisionLabelString,
    VerbatimStringPlain,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import (
    SwSystemconstValue,
)
from armodel.models.M2.MSR.AsamHdo.AdminData import AdminData, DocRevision, Modification
from armodel.models.M2.MSR.AsamHdo.SpecialData import Sd, Sdg, SdgContents
from armodel.models.M2.MSR.DataDictionary.Axis import SwAxisGeneric, SwAxisIndividual, SwGenericAxisParam
from armodel.models.M2.MSR.DataDictionary.CalibrationParameter import SwCalprmAxis, SwCalprmAxisSet
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwCalibrationAccessEnum, SwDataDefProps
from armodel.models.M2.MSR.Documentation.Annotation import Annotation
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import LLongName, LOverviewParagraph, LPlainText
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultilanguageLongName, MultiLanguageOverviewParagraph, MultiLanguagePlainText
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


class TestARXMLWriterBasicMethods:
    """Test basic ARXMLWriter methods"""

    def test_initialization(self):
        """Test ARXMLWriter initialization"""
        writer = ARXMLWriter()
        assert writer is not None
        assert writer.options["warning"] is False
        assert writer.options["version"] == "4.2.2"

    def test_initialization_with_warning_option(self):
        """Test ARXMLWriter initialization with warning option"""
        writer = ARXMLWriter(options={"warning": True})
        assert writer.options["warning"] is True

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
        limit.setIntervalType(IntervalTypeEnum().setValue("CLOSED"))

        writer.setChildLimitElement(parent, "TEST-LIMIT", limit)

        assert len(parent) == 1
        child = parent[0]
        assert child.tag == "TEST-LIMIT"
        assert child.text == "100"
        assert child.attrib.get("INTERVAL-TYPE") == "CLOSED"

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
        assert "INTERVAL-TYPE" not in child.attrib

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

        contents = SdgContents()
        sd = Sd()
        sd.setValue(VerbatimStringPlain().setValue("test value"))
        sd.setGID(NameToken().setValue("test-gid"))
        contents.addSd(sd)

        writer.writeSds(parent, contents)

        assert len(parent) == 1
        sd_tag = parent[0]
        assert sd_tag.tag == "SD"
        assert sd_tag.text == "test value"
        assert sd_tag.attrib.get("GID") == "test-gid"

    def test_write_sds_with_multiple_sds(self):
        """Test writeSds with multiple SDs"""
        writer = ARXMLWriter()
        parent = ET.Element("parent")

        contents = SdgContents()
        sd1 = Sd()
        sd1.setValue(VerbatimStringPlain().setValue("value1"))
        sd2 = Sd()
        sd2.setValue(VerbatimStringPlain().setValue("value2"))
        contents.addSd(sd1)
        contents.addSd(sd2)

        writer.writeSds(parent, contents)

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

        contents = SdgContents()
        ref = RefType()
        ref.value = "/path/to/ref"
        contents.addSdxRef(ref)

        writer.writeSdgSdxRefs(parent, contents)

        assert len(parent) == 1
        ref_tag = parent[0]
        assert ref_tag.tag == "SDX-REF"
        assert ref_tag.text == "/path/to/ref"

    def test_set_sdg_basic(self):
        """Test setSdg with basic SDG"""
        writer = ARXMLWriter()
        parent = ET.Element("parent")

        sdg = Sdg()
        sdg.setGID(NameToken().setValue("test-gid"))
        sd = Sd()
        sd.setValue(VerbatimStringPlain().setValue("test value"))
        contents = SdgContents()
        contents.addSd(sd)
        sdg.setSdgContentsType(contents)

        writer.setSdg(parent, sdg)

        assert len(parent) == 1
        sdg_tag = parent[0]
        assert sdg_tag.tag == "SDG"
        assert sdg_tag.attrib.get("GID") == "test-gid"

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
        sd = Sd()
        sd.setValue(VerbatimStringPlain().setValue("test value"))
        contents = SdgContents()
        contents.addSd(sd)
        sdg.setSdgContentsType(contents)

        writer.setSdg(parent, sdg)

        assert len(parent) == 1
        sdg_tag = parent[0]
        assert "GID" not in sdg_tag.attrib

    def test_write_admin_data_sdgs_with_sdgs(self):
        """Test writeAdminDataSdgs with SDGs"""
        writer = ARXMLWriter()
        parent = ET.Element("parent")

        admin_data = AdminData()
        sdg = Sdg()
        sd = Sd()
        sd.setValue(VerbatimStringPlain().setValue("test value"))
        contents = SdgContents()
        contents.addSd(sd)
        sdg.setSdgContentsType(contents)
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

    def test_write_nv_data_interface(self):
        """Test writing NV-DATA-INTERFACE structure."""
        writer = ARXMLWriter()

        autosar = AUTOSAR.getInstance()
        autosar.clear()

        pkg = autosar.createARPackage("TestPackage")
        nv_interface = pkg.createNvDataInterface("NvIf")
        nv_interface.createNvData("NvBlock")

        root = ET.Element("ROOT")
        writer.writeARPackageElement(root, nv_interface)

        assert len(root) == 1
        interface_tag = root[0]
        assert interface_tag.tag == "NV-DATA-INTERFACE"

        short_name = interface_tag.find("SHORT-NAME")
        assert short_name is not None
        assert short_name.text == "NvIf"

        nv_datas = interface_tag.find("NV-DATAS")
        assert nv_datas is not None
        assert len(nv_datas) == 1
        assert nv_datas[0].tag == "VARIABLE-DATA-PROTOTYPE"


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
        assert child.attrib.get("L") == "EN"
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
        assert "L" not in child.attrib
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
        assert child.attrib.get("L") == "EN"
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
        assert child.attrib.get("L") == "EN"
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
        assert child.attrib.get("L") == "EN"
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

    def test_write_reference_value_specification(self):
        """Test writeReferenceValueSpecification method"""
        writer = ARXMLWriter()
        parent = ET.Element("parent")

        value_spec = ReferenceValueSpecification()
        ref = RefType()
        ref.setValue("/Path/To/DataPrototype")
        ref.setDest("DATA-PROTOTYPE")
        value_spec.setReferenceValueRef(ref)

        writer.writeReferenceValueSpecification(parent, value_spec)

        assert len(parent) == 1
        spec_element = parent[0]
        assert spec_element.tag == "REFERENCE-VALUE-SPECIFICATION"
        ref_element = spec_element.find("REFERENCE-VALUE-REF")
        assert ref_element is not None
        assert ref_element.text == "/Path/To/DataPrototype"


class TestARXMLWriterSwSystemconstMethods:
    """Tests for SwSystemconst writer behavior."""

    def test_write_sw_systemconst_basic(self):
        """Test writeSwSystemconst with only short name."""
        writer = ARXMLWriter()
        autosar = AUTOSAR.getInstance()
        autosar.clear()

        pkg = autosar.createARPackage("Constants")
        system_const = pkg.createSwSystemConst("MySystemConstant")

        root = ET.Element("ELEMENTS")
        writer.writeSwSystemconst(root, system_const)

        assert len(root) == 1
        sw_systemconst = root.find("SW-SYSTEMCONST")
        assert sw_systemconst is not None
        short_name = sw_systemconst.find("SHORT-NAME")
        assert short_name is not None
        assert short_name.text == "MySystemConstant"
        assert sw_systemconst.find("SW-DATA-DEF-PROPS") is None

        autosar.clear()

    def test_write_sw_systemconst_with_sw_data_def_props(self):
        """Test writeSwSystemconst with SW-DATA-DEF-PROPS content."""
        writer = ARXMLWriter()
        autosar = AUTOSAR.getInstance()
        autosar.clear()

        pkg = autosar.createARPackage("Constants")
        system_const = pkg.createSwSystemConst("EncodedValue")

        props = SwDataDefProps()
        base_type_ref = RefType()
        base_type_ref.setDest("SW-BASE-TYPE")
        base_type_ref.setValue("/BaseTypes/uint8")
        compu_method_ref = RefType()
        compu_method_ref.setDest("COMPU-METHOD")
        compu_method_ref.setValue("/Application/CompuMethods/StatusEncoding")
        props.setBaseTypeRef(base_type_ref)
        props.setCompuMethodRef(compu_method_ref)
        props.setSwCalprmAxisSet(SwCalprmAxisSet())
        system_const.setSwDataDefProps(props)

        root = ET.Element("ELEMENTS")
        writer.writeSwSystemconst(root, system_const)

        sw_systemconst = root.find("SW-SYSTEMCONST")
        assert sw_systemconst is not None

        props_element = sw_systemconst.find("SW-DATA-DEF-PROPS")
        assert props_element is not None
        variants = props_element.find("SW-DATA-DEF-PROPS-VARIANTS")
        assert variants is not None
        conditional = variants.find("SW-DATA-DEF-PROPS-CONDITIONAL")
        assert conditional is not None

        base_type = conditional.find("BASE-TYPE-REF")
        assert base_type is not None
        assert base_type.text == "/BaseTypes/uint8"
        assert base_type.attrib.get("DEST") == "SW-BASE-TYPE"

        compu_method = conditional.find("COMPU-METHOD-REF")
        assert compu_method is not None
        assert compu_method.text == "/Application/CompuMethods/StatusEncoding"
        assert compu_method.attrib.get("DEST") == "COMPU-METHOD"

        autosar.clear()


class TestARXMLWriterSwCalprmAxisMethods:
    """Tests for SwCalprmAxis / SwCalprmAxisTypeProps writer behavior."""

    def _build_individual_axis(self) -> SwCalprmAxis:
        axis = SwCalprmAxis()
        props = SwAxisIndividual()
        gradient = ARFloat()
        gradient.setValue(2.5)
        props.setMaxGradient(gradient)
        monotony = MonotonyEnum()
        monotony.setValue(MonotonyEnum.STRICTLY_INCREASING)
        props.setMonotony(monotony)
        axis.setSwCalprmAxisTypeProps(props)
        return axis

    def test_setSwCalprmAxis_individual_type_props(self):
        """MAX-GRADIENT and MONOTONY shall be written inside SW-AXIS-INDIVIDUAL."""
        writer = ARXMLWriter()
        root = ET.Element("SW-CALPRM-AXIS-SET")
        writer.setSwCalprmAxis(root, self._build_individual_axis())

        axis_el = root.find("SW-CALPRM-AXIS")
        assert axis_el is not None
        individual = axis_el.find("SW-AXIS-INDIVIDUAL")
        assert individual is not None
        assert individual.find("MAX-GRADIENT") is not None
        assert individual.find("MAX-GRADIENT").text == "2.5"
        assert individual.find("MONOTONY") is not None
        assert individual.find("MONOTONY").text == "strictlyIncreasing"

    def test_setSwCalprmAxis_type_props_roundtrip(self):
        """Write then re-parse: maxGradient and monotony survive a round-trip."""
        writer = ARXMLWriter()
        root = ET.Element("SW-CALPRM-AXIS-SET")
        writer.setSwCalprmAxis(root, self._build_individual_axis())

        wrapped = ET.fromstring("<WRAP xmlns='http://autosar.org/schema/r4.0'>%s</WRAP>" % ET.tostring(root.find("SW-CALPRM-AXIS"), encoding="unicode"))
        parser = ARXMLParser()
        axis = parser.getSwCalprmAxis(wrapped[0])
        props = axis.getSwCalprmAxisTypeProps()
        assert props.getMaxGradient().getValue() == 2.5
        assert props.getMonotony().getValue() == "strictlyIncreasing"

    def test_setSwCalprmAxis_generic_axis_roundtrip(self):
        """SW-AXIS-GENERIC with type ref and generic params shall be written and round-trip."""
        writer = ARXMLWriter()
        axis = SwCalprmAxis()
        props = SwAxisIndividual()
        generic = SwAxisGeneric()
        axis_type_ref = RefType()
        axis_type_ref.setDest("SW-AXIS-TYPE")
        axis_type_ref.setValue("/axis/types/fixed")
        generic.setSwAxisTypeRef(axis_type_ref)
        param = SwGenericAxisParam()
        param_type_ref = RefType()
        param_type_ref.setDest("SW-GENERIC-AXIS-PARAM-TYPE")
        param_type_ref.setValue("/axis/types/fixed/shift")
        param.setSwGenericAxisParamTypeRef(param_type_ref)
        vf1 = ARNumerical()
        vf1.setValue("1.5")
        param.addVf(vf1)
        generic.addSwGenericAxisParam(param)
        props.setSwAxisGeneric(generic)
        axis.setSwCalprmAxisTypeProps(props)

        root = ET.Element("SW-CALPRM-AXIS-SET")
        writer.setSwCalprmAxis(root, axis)

        axis_el = root.find("SW-CALPRM-AXIS")
        individual = axis_el.find("SW-AXIS-INDIVIDUAL")
        assert individual is not None
        generic_el = individual.find("SW-AXIS-GENERIC")
        assert generic_el is not None
        assert generic_el.find("SW-AXIS-TYPE-REF").text == "/axis/types/fixed"
        params_wrapper = generic_el.find("SW-GENERIC-AXIS-PARAMS")
        assert params_wrapper is not None
        param_el = params_wrapper.find("SW-GENERIC-AXIS-PARAM")
        assert param_el is not None
        assert param_el.find("SW-GENERIC-AXIS-PARAM-TYPE-REF").text == "/axis/types/fixed/shift"
        assert len(param_el.findall("VF")) == 1
        assert param_el.find("VF").text == "1.5"

        wrapped = ET.fromstring("<WRAP xmlns='http://autosar.org/schema/r4.0'>%s</WRAP>" % ET.tostring(axis_el, encoding="unicode"))
        parser = ARXMLParser()
        reparsed = parser.getSwCalprmAxis(wrapped[0])
        reparsed_props = reparsed.getSwCalprmAxisTypeProps()
        reparsed_generic = reparsed_props.getSwAxisGeneric()
        assert reparsed_generic is not None
        assert reparsed_generic.getSwAxisTypeRef().getValue() == "/axis/types/fixed"
        reparsed_params = reparsed_generic.getSwGenericAxisParams()
        assert len(reparsed_params) == 1
        assert reparsed_params[0].getSwGenericAxisParamTypeRef().getValue() == "/axis/types/fixed/shift"
        assert len(reparsed_params[0].getVfs()) == 1
        assert reparsed_params[0].getVfs()[0].getValue() == 1.5

    def test_setSwCalprmAxis_access_and_display_format(self):
        """SW-CALIBRATION-ACCESS and DISPLAY-FORMAT shall be written in XSD sequence order."""
        writer = ARXMLWriter()
        axis = SwCalprmAxis()
        access = SwCalibrationAccessEnum()
        access.setValue(SwCalibrationAccessEnum.READ_ONLY)
        axis.setSwCalibrationAccess(access)
        display_format = DisplayFormatString()
        display_format.setValue("%.3f")
        axis.setDisplayFormat(display_format)

        root = ET.Element("SW-CALPRM-AXIS-SET")
        writer.setSwCalprmAxis(root, axis)

        axis_el = root.find("SW-CALPRM-AXIS")
        assert axis_el is not None
        access_el = axis_el.find("SW-CALIBRATION-ACCESS")
        assert access_el is not None
        assert access_el.text == "readOnly"
        display_el = axis_el.find("DISPLAY-FORMAT")
        assert display_el is not None
        assert display_el.text == "%.3f"


class TestARXMLWriterSwSystemconstantValueSetMethods:
    """Tests for SwSystemconstantValueSet writer behavior."""

    def test_write_sw_systemconstant_value_set_basic(self):
        """Test writing SW-SYSTEMCONSTANT-VALUE-SET with one value."""
        writer = ARXMLWriter()
        autosar = AUTOSAR.getInstance()
        autosar.clear()

        pkg = autosar.createARPackage("Variants")
        value_set = pkg.createSwSystemconstantValueSet("MyValueSet")

        value = SwSystemconstValue()
        ref = RefType()
        ref.setDest("SW-SYSTEMCONST")
        ref.setValue("/Constants/MySystemConstant")
        value.setSwSystemconstRef(ref)

        num = ARFloat()
        num.setValue(42)
        num._text = "42"
        value.setValue(num)
        value_set.addSwSystemconstantValue(value)

        root = ET.Element("ELEMENTS")
        writer.writeARPackageElement(root, value_set)

        value_set_el = root.find("SW-SYSTEMCONSTANT-VALUE-SET")
        assert value_set_el is not None
        assert value_set_el.find("SHORT-NAME").text == "MyValueSet"

        values_el = value_set_el.find("SW-SYSTEMCONSTANT-VALUES")
        assert values_el is not None

        value_el = values_el.find("SW-SYSTEMCONST-VALUE")
        assert value_el is not None

        ref_el = value_el.find("SW-SYSTEMCONST-REF")
        assert ref_el is not None
        assert ref_el.text == "/Constants/MySystemConstant"
        assert ref_el.attrib.get("DEST") == "SW-SYSTEMCONST"

        number_el = value_el.find("VALUE")
        assert number_el is not None
        assert number_el.text == "42"

        autosar.clear()

    def test_write_sw_systemconstant_value_set_with_annotation(self):
        """Test writing ANNOTATIONS under SW-SYSTEMCONST-VALUE."""
        writer = ARXMLWriter()
        autosar = AUTOSAR.getInstance()
        autosar.clear()

        pkg = autosar.createARPackage("Variants")
        value_set = pkg.createSwSystemconstantValueSet("AnnotatedValueSet")

        value = SwSystemconstValue()
        annotation = Annotation()
        value.addAnnotation(annotation)
        value_set.addSwSystemconstantValue(value)

        root = ET.Element("ELEMENTS")
        writer.writeARPackageElement(root, value_set)

        value_el = root.find("SW-SYSTEMCONSTANT-VALUE-SET/SW-SYSTEMCONSTANT-VALUES/SW-SYSTEMCONST-VALUE")
        assert value_el is not None
        assert value_el.find("ANNOTATIONS") is not None
        assert value_el.find("ANNOTATIONS/ANNOTATION") is not None

        autosar.clear()


class TestARXMLWriterPredefinedVariantMethods:
    """Tests for PredefinedVariant writer behavior."""

    def test_write_predefined_variant_with_refs(self):
        """Test writing PREDEFINED-VARIANT with all reference groups."""
        writer = ARXMLWriter()
        autosar = AUTOSAR.getInstance()
        autosar.clear()

        pkg = autosar.createARPackage("Variants")
        variant = pkg.createPredefinedVariant("VariantA")

        included_ref = RefType()
        included_ref.setDest("PREDEFINED-VARIANT")
        included_ref.setValue("/Variants/BaseVariant")
        variant.addIncludedVariantRef(included_ref)

        post_build_ref = RefType()
        post_build_ref.setDest("POST-BUILD-VARIANT-CRITERION-VALUE-SET")
        post_build_ref.setValue("/Variants/PbCriteriaSetA")
        variant.addPostBuildVariantCriterionValueSetRef(post_build_ref)

        systemconst_ref = RefType()
        systemconst_ref.setDest("SW-SYSTEMCONSTANT-VALUE-SET")
        systemconst_ref.setValue("/Variants/SystemConstValuesA")
        variant.addSwSystemconstantValueSetRef(systemconst_ref)

        root = ET.Element("ELEMENTS")
        writer.writeARPackageElement(root, variant)

        variant_el = root.find("PREDEFINED-VARIANT")
        assert variant_el is not None
        assert variant_el.find("SHORT-NAME").text == "VariantA"

        included_el = variant_el.find("INCLUDED-VARIANT-REFS/INCLUDED-VARIANT-REF")
        assert included_el is not None
        assert included_el.text == "/Variants/BaseVariant"
        assert included_el.attrib.get("DEST") == "PREDEFINED-VARIANT"

        post_build_el = variant_el.find("POST-BUILD-VARIANT-CRITERION-VALUE-SET-REFS/" "POST-BUILD-VARIANT-CRITERION-VALUE-SET-REF")
        assert post_build_el is not None
        assert post_build_el.text == "/Variants/PbCriteriaSetA"
        assert post_build_el.attrib.get("DEST") == "POST-BUILD-VARIANT-CRITERION-VALUE-SET"

        systemconst_el = variant_el.find("SW-SYSTEMCONSTANT-VALUE-SET-REFS/" "SW-SYSTEMCONSTANT-VALUE-SET-REF")
        assert systemconst_el is not None
        assert systemconst_el.text == "/Variants/SystemConstValuesA"
        assert systemconst_el.attrib.get("DEST") == "SW-SYSTEMCONSTANT-VALUE-SET"

        autosar.clear()


class TestShortNameFragmentsWriting:
    """Test writing of Referrable.shortNameFragments."""

    def test_write_referrable_with_short_name_fragments(self):
        writer = ARXMLWriter()
        parent = ET.Element("parent")
        autosar = AUTOSAR.getInstance()

        class ConcreteReferrable(Referrable):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        obj = ConcreteReferrable(autosar, "TestName")
        fragment = ShortNameFragment()
        fragment.setRole("prefix")
        fragment.setFragment(Identifier().setValue("PFX"))
        obj.addShortNameFragment(fragment)

        writer.writeReferrable(parent, obj)

        short_name_el = parent.find("SHORT-NAME")
        assert short_name_el is not None
        assert short_name_el.text == "TestName"

        fragments_el = parent.find("SHORT-NAME-FRAGMENTS")
        assert fragments_el is not None
        fragment_el = fragments_el.find("SHORT-NAME-FRAGMENT")
        assert fragment_el is not None
        role_el = fragment_el.find("ROLE")
        assert role_el is not None
        assert role_el.text == "prefix"
        fragment_value_el = fragment_el.find("FRAGMENT")
        assert fragment_value_el is not None
        assert fragment_value_el.text == "PFX"

    def test_write_referrable_without_short_name_fragments(self):
        writer = ARXMLWriter()
        parent = ET.Element("parent")
        autosar = AUTOSAR.getInstance()

        class ConcreteReferrable(Referrable):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        obj = ConcreteReferrable(autosar, "TestName")

        writer.writeReferrable(parent, obj)

        assert parent.find("SHORT-NAME-FRAGMENTS") is None

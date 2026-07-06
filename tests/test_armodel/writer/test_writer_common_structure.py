"""Tests for writer common structure and documentation handlers."""
import xml.etree.cElementTree as ET
import pytest
from armodel.writer.arxml_writer import ARXMLWriter
from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.MSR.AsamHdo.SpecialData import Sdg, Sd, SdgCaption
from armodel.models.M2.MSR.AsamHdo.AdminData import (
    AdminData, DocRevision, Modification,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (  # noqa: E501
    Limit, RefType, ARLiteral, RevisionLabelString, DateTime,
)
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import (
    LLongName, LPlainText, LOverviewParagraph,
)
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import (
    MultilanguageLongName, MultiLanguageOverviewParagraph,
    MultiLanguagePlainText, MultiLanguageParagraph,
)
from armodel.models.M2.MSR.Documentation.Annotation import Annotation
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import (
    DocumentationBlock,
)
from armodel.models.M2.MSR.Documentation.BlockElements.Figure import (
    MlFigure, Graphic, LGraphic,
)
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements.ListElements import (  # noqa: E501
    ARList,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ElementCollection import (  # noqa: E501
    Collection,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.Keyword import (  # noqa: E501
    Keyword, KeywordSet,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.BlueprintDedicated.PortPrototypeBlueprint import (  # noqa: E501
    PortPrototypeBlueprint,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import (
    ModeDeclarationMapping, ModeDeclarationMappingSet,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (  # noqa: E501
    Describable,
)


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    AUTOSAR.getInstance().new()
    return ARXMLWriter()


@pytest.fixture
def warning_writer():
    AUTOSAR.getInstance().new()
    return ARXMLWriter(options={'warning': True})


def _parent():
    return ET.Element("PARENT")


def _autosar():
    return AUTOSAR.getInstance()


class ConcreteDescribable(Describable):
    def __init__(self):
        super().__init__()


class TestSetShortName:
    def test_sets_short_name_element(self, writer):
        parent = _parent()
        result = writer.setShortName(parent, "TestName")
        assert result.tag == "SHORT-NAME"
        assert result.text == "TestName"
        assert parent[0] is result


class TestWriteSds:
    def test_single_sd_with_gid(self, writer):
        parent = _parent()
        sdg = Sdg()
        sd = Sd()
        sd.value = "val"
        sd.gid = "g1"
        sdg.addSd(sd)
        writer.writeSds(parent, sdg)
        assert len(parent) == 1
        assert parent[0].tag == "SD"
        assert parent[0].text == "val"
        assert parent[0].attrib['GID'] == "g1"

    def test_multiple_sds(self, writer):
        parent = _parent()
        sdg = Sdg()
        sd1 = Sd()
        sd1.value = "v1"
        sd2 = Sd()
        sd2.value = "v2"
        sdg.addSd(sd1).addSd(sd2)
        writer.writeSds(parent, sdg)
        assert len(parent) == 2
        assert parent[0].text == "v1"
        assert parent[1].text == "v2"

    def test_sd_without_gid(self, writer):
        parent = _parent()
        sdg = Sdg()
        sd = Sd()
        sd.value = "val"
        sd.gid = None
        sdg.addSd(sd)
        writer.writeSds(parent, sdg)
        assert 'GID' not in parent[0].attrib


class TestWriteSdgCaption:
    def test_with_caption(self, writer):
        parent = _parent()
        sdg = Sdg()
        sdg.createSdgCaption("CapName")
        writer.writeSdgCaption(parent, sdg)
        assert len(parent) == 1
        assert parent[0].tag == "SDG-CAPTION"
        sn = parent[0].find("SHORT-NAME")
        assert sn is not None
        assert sn.text == "CapName"

    def test_without_caption(self, writer):
        parent = _parent()
        sdg = Sdg()
        writer.writeSdgCaption(parent, sdg)
        assert len(parent) == 0


class TestWriteSdgSdxRefs:
    def test_with_refs(self, writer):
        parent = _parent()
        sdg = Sdg()
        ref = RefType()
        ref.value = "/path"
        ref.dest = "ELEMENT"
        sdg.addSdxRef(ref)
        writer.writeSdgSdxRefs(parent, sdg)
        assert len(parent) == 1
        assert parent[0].tag == "SDX-REF"
        assert parent[0].text == "/path"
        assert parent[0].attrib['DEST'] == "ELEMENT"

    def test_without_refs(self, writer):
        parent = _parent()
        sdg = Sdg()
        writer.writeSdgSdxRefs(parent, sdg)
        assert len(parent) == 0


class TestSetSdg:
    def test_basic_with_gid(self, writer):
        parent = _parent()
        sdg = Sdg()
        sdg.gid = "gid1"
        sd = Sd()
        sd.value = "v"
        sdg.addSd(sd)
        writer.setSdg(parent, sdg)
        assert parent[0].tag == "SDG"
        assert parent[0].attrib['GID'] == "gid1"
        sd_tag = parent[0].find("SD")
        assert sd_tag is not None
        assert sd_tag.text == "v"

    def test_none(self, writer):
        parent = _parent()
        writer.setSdg(parent, None)
        assert len(parent) == 0

    def test_empty_gid_not_written(self, writer):
        parent = _parent()
        sdg = Sdg()
        sdg.gid = ""
        writer.setSdg(parent, sdg)
        assert 'GID' not in parent[0].attrib

    def test_nested_sdg_contents(self, writer):
        parent = _parent()
        sdg = Sdg()
        sdg.gid = "outer"
        inner = Sdg()
        inner.gid = "inner"
        sdg.addSdgContentsType(inner)
        writer.setSdg(parent, sdg)
        outer = parent[0]
        assert outer.tag == "SDG"
        inner_tag = outer.find("SDG")
        assert inner_tag is not None
        assert inner_tag.attrib['GID'] == "inner"

    def test_sdg_with_caption_and_sdx(self, writer):
        parent = _parent()
        sdg = Sdg()
        sdg.gid = "g"
        sdg.createSdgCaption("Cap")
        ref = RefType()
        ref.value = "/r"
        sdg.addSdxRef(ref)
        writer.setSdg(parent, sdg)
        sdg_tag = parent[0]
        assert sdg_tag.find("SDG-CAPTION") is not None
        assert sdg_tag.find("SDX-REF") is not None


class TestWriteAdminDataSdgs:
    def test_with_sdgs(self, writer):
        parent = _parent()
        admin = AdminData()
        sdg = Sdg()
        sdg.gid = "g"
        admin.addSdg(sdg)
        writer.writeAdminDataSdgs(parent, admin)
        assert parent[0].tag == "SDGS"
        assert parent[0][0].tag == "SDG"

    def test_empty(self, writer):
        parent = _parent()
        admin = AdminData()
        writer.writeAdminDataSdgs(parent, admin)
        assert len(parent) == 0


class TestWriteReferrable:
    def test_writes_short_name(self, writer):
        parent = _parent()
        elem = Collection(_autosar(), "Coll")
        writer.writeReferrable(parent, elem)
        sn = parent.find("SHORT-NAME")
        assert sn is not None
        assert sn.text == "Coll"


class TestSetLanguageSpecific:
    def test_with_l_attribute(self, writer):
        parent = _parent()
        item = LLongName()
        item.l = "en"
        item.value = "Hello"
        writer.setLanguageSpecific(parent, "L-4", item)
        assert parent[0].tag == "L-4"
        assert parent[0].text == "Hello"
        assert parent[0].attrib['L'] == "en"

    def test_without_l_attribute(self, writer):
        parent = _parent()
        item = LLongName()
        item.l = None
        item.value = "Hi"
        writer.setLanguageSpecific(parent, "L-4", item)
        assert 'L' not in parent[0].attrib


class TestSetLLongName:
    def test_creates_l4_element(self, writer):
        parent = _parent()
        name = LLongName()
        name.l = "en"
        name.value = "Name"
        writer.setLLongName(parent, name)
        assert parent[0].tag == "L-4"
        assert parent[0].text == "Name"


class TestSetMultiLongName:
    def test_with_l4s(self, writer):
        parent = _parent()
        ln = MultilanguageLongName()
        l4 = LLongName()
        l4.l = "en"
        l4.value = "N"
        ln.addL4(l4)
        writer.setMultiLongName(parent, "LONG-NAME", ln)
        assert parent[0].tag == "LONG-NAME"
        assert parent[0][0].tag == "L-4"

    def test_none(self, writer):
        parent = _parent()
        writer.setMultiLongName(parent, "LONG-NAME", None)
        assert len(parent) == 0


class TestWriteMultilanguageReferrable:
    def test_with_long_name(self, writer):
        parent = _parent()
        cap = SdgCaption(_autosar(), "Cap")
        ln = MultilanguageLongName()
        l4 = LLongName()
        l4.l = "en"
        l4.value = "Long"
        ln.addL4(l4)
        cap.setLongName(ln)
        writer.writeMultilanguageReferrable(parent, cap)
        assert parent.find("SHORT-NAME").text == "Cap"
        assert parent.find("LONG-NAME") is not None

    def test_without_long_name(self, writer):
        parent = _parent()
        cap = SdgCaption(_autosar(), "Cap")
        writer.writeMultilanguageReferrable(parent, cap)
        assert parent.find("LONG-NAME") is None


class TestWriteModification:
    def test_with_change_and_reason(self, writer):
        parent = _parent()
        mod = Modification()
        change = MultiLanguageOverviewParagraph()
        l2 = LOverviewParagraph()
        l2.l = "en"
        l2.value = "Changed"
        change.addL2(l2)
        mod.setChange(change)
        reason = MultiLanguageOverviewParagraph()
        l2r = LOverviewParagraph()
        l2r.l = "en"
        l2r.value = "Because"
        reason.addL2(l2r)
        mod.setReason(reason)
        writer.writeModification(parent, mod)
        assert parent[0].tag == "MODIFICATION"
        assert parent[0].find("CHANGE") is not None
        assert parent[0].find("REASON") is not None

    def test_none(self, writer):
        parent = _parent()
        writer.writeModification(parent, None)
        assert len(parent) == 0


class TestWriteDocRevisionModifications:
    def test_with_modifications(self, writer):
        parent = _parent()
        rev = DocRevision()
        mod = Modification()
        rev.addModification(mod)
        writer.writeDocRevisionModifications(parent, rev)
        assert parent[0].tag == "MODIFICATIONS"
        assert parent[0][0].tag == "MODIFICATION"

    def test_empty(self, writer):
        parent = _parent()
        rev = DocRevision()
        writer.writeDocRevisionModifications(parent, rev)
        assert len(parent) == 0

    def test_unsupported_type(self, warning_writer):
        parent = _parent()
        rev = DocRevision()
        rev.modifications.append("not_a_modification")
        warning_writer.writeDocRevisionModifications(parent, rev)
        assert parent[0].tag == "MODIFICATIONS"


class TestWriteDocRevision:
    def test_with_fields(self, writer):
        parent = _parent()
        rev = DocRevision()
        rl = RevisionLabelString()
        rl.setValue("1.0.0")
        rev.setRevisionLabel(rl)
        state = ARLiteral()
        state.setValue("DRAFT")
        rev.setState(state)
        issued = ARLiteral()
        issued.setValue("Alice")
        rev.setIssuedBy(issued)
        dt = DateTime()
        dt.setValue("2024-01-01")
        rev.setDate(dt)
        mod = Modification()
        rev.addModification(mod)
        writer.writeDocRevision(parent, rev)
        assert parent[0].tag == "DOC-REVISION"
        assert parent[0].find("REVISION-LABEL").text == "1.0.0"
        assert parent[0].find("STATE").text == "DRAFT"
        assert parent[0].find("ISSUED-BY").text == "Alice"
        assert parent[0].find("DATE").text == "2024-01-01"
        assert parent[0].find("MODIFICATIONS") is not None

    def test_none(self, writer):
        parent = _parent()
        writer.writeDocRevision(parent, None)
        assert len(parent) == 0


class TestWriteAdminDataDocRevisions:
    def test_with_revisions(self, writer):
        parent = _parent()
        admin = AdminData()
        rev = DocRevision()
        admin.addDocRevision(rev)
        writer.writeAdminDataDocRevisions(parent, admin)
        assert parent[0].tag == "DOC-REVISIONS"
        assert parent[0][0].tag == "DOC-REVISION"

    def test_empty(self, writer):
        parent = _parent()
        admin = AdminData()
        writer.writeAdminDataDocRevisions(parent, admin)
        assert len(parent) == 0

    def test_unsupported_type(self, warning_writer):
        parent = _parent()
        admin = AdminData()
        admin.DocRevisions.append("not_a_revision")
        warning_writer.writeAdminDataDocRevisions(parent, admin)
        assert parent[0].tag == "DOC-REVISIONS"


class TestSetAdminData:
    def test_with_full_data(self, writer):
        parent = _parent()
        admin = AdminData()
        lang = ARLiteral()
        lang.setValue("en")
        admin.setLanguage(lang)
        ul = MultiLanguagePlainText()
        l10 = LPlainText()
        l10.l = "en"
        l10.value = "English"
        ul.addL10(l10)
        admin.setUsedLanguages(ul)
        admin.addSdg(Sdg())
        rev = DocRevision()
        admin.addDocRevision(rev)
        writer.setAdminData(parent, admin)
        assert parent[0].tag == "ADMIN-DATA"
        assert parent[0].find("LANGUAGE") is not None
        assert parent[0].find("USED-LANGUAGES") is not None
        assert parent[0].find("SDGS") is not None
        assert parent[0].find("DOC-REVISIONS") is not None

    def test_none(self, writer):
        parent = _parent()
        writer.setAdminData(parent, None)
        assert len(parent) == 0


class TestWriteIdentifiable:
    def test_writes_full_identifiable(self, writer):
        parent = _parent()
        coll = Collection(_autosar(), "Coll")
        cat = ARLiteral()
        cat.setValue("CAT")
        coll.setCategory(cat)
        desc = MultiLanguageOverviewParagraph()
        l2 = LOverviewParagraph()
        l2.l = "en"
        l2.value = "Desc"
        desc.addL2(l2)
        coll.setDesc(desc)
        admin = AdminData()
        coll.setAdminData(admin)
        ann = Annotation()
        coll.addAnnotation(ann)
        intro = DocumentationBlock()
        coll.setIntroduction(intro)
        writer.writeIdentifiable(parent, coll)
        assert parent.find("SHORT-NAME").text == "Coll"
        assert parent.find("DESC") is not None
        assert parent.find("CATEGORY").text == "CAT"
        assert parent.find("INTRODUCTION") is not None
        assert parent.find("ADMIN-DATA") is not None
        assert parent.find("ANNOTATIONS") is not None


class TestWriteARElement:
    def test_writes_ar_element(self, writer):
        parent = _parent()
        coll = Collection(_autosar(), "Coll")
        writer.writeARElement(parent, coll)
        assert parent.find("SHORT-NAME").text == "Coll"


class TestWriteLParagraphs:
    def test_with_l(self, writer):
        parent = _parent()
        para = MultiLanguageParagraph()
        l1 = LLongName()
        l1.l = "en"
        l1.value = "Text"
        para.addL1(l1)
        writer.writeLParagraphs(parent, para)
        assert parent[0].tag == "L-1"
        assert parent[0].attrib['L'] == "en"
        assert parent[0].text == "Text"

    def test_without_l(self, writer):
        parent = _parent()
        para = MultiLanguageParagraph()
        l1 = LLongName()
        l1.l = None
        l1.value = "Text"
        para.addL1(l1)
        writer.writeLParagraphs(parent, para)
        assert parent[0].tag == "L-1"
        assert 'L' not in parent[0].attrib

    def test_empty(self, writer):
        parent = _parent()
        para = MultiLanguageParagraph()
        writer.writeLParagraphs(parent, para)
        assert len(parent) == 0


class TestSetMultiLanguageParagraphs:
    def test_with_paragraphs(self, writer):
        parent = _parent()
        para = MultiLanguageParagraph()
        l1 = LLongName()
        l1.l = "en"
        l1.value = "P"
        para.addL1(l1)
        result = writer.setMultiLanguageParagraphs(parent, "P", [para])
        assert parent[0].tag == "P"
        assert parent[0][0].tag == "L-1"
        assert result == [para]

    def test_empty_list(self, writer):
        parent = _parent()
        writer.setMultiLanguageParagraphs(parent, "P", [])
        assert len(parent) == 0


class TestSetListElement:
    def test_with_type(self, writer):
        parent = _parent()
        lst = ARList()
        lst.setType("number")
        writer.setListElement(parent, "LIST", lst)
        assert parent[0].tag == "LIST"
        assert parent[0].attrib['TYPE'] == "number"

    def test_without_type(self, writer):
        parent = _parent()
        lst = ARList()
        writer.setListElement(parent, "LIST", lst)
        assert 'TYPE' not in parent[0].attrib

    def test_none(self, writer):
        parent = _parent()
        writer.setListElement(parent, "LIST", None)
        assert len(parent) == 0

    def test_with_documentation_block_item(self, writer):
        parent = _parent()
        lst = ARList()
        lst.setType("number")
        block = DocumentationBlock()
        para = MultiLanguageParagraph()
        l1 = LLongName()
        l1.l = "en"
        l1.value = "Item"
        para.addL1(l1)
        block.addP(para)
        lst.items.append(block)
        writer.setListElement(parent, "LIST", lst)
        assert parent[0].find("ITEM") is not None


class TestSetGraphic:
    def test_with_filename(self, writer):
        parent = _parent()
        g = Graphic()
        g.setFilename("img.png")
        writer.setGraphic(parent, "GRAPHIC", g)
        assert parent[0].tag == "GRAPHIC"
        assert parent[0].attrib['FILENAME'] == "img.png"

    def test_without_filename(self, writer):
        parent = _parent()
        g = Graphic()
        writer.setGraphic(parent, "GRAPHIC", g)
        assert 'FILENAME' not in parent[0].attrib

    def test_none(self, writer):
        parent = _parent()
        writer.setGraphic(parent, "GRAPHIC", None)
        assert len(parent) == 0


class TestWriteMlFigureLGraphics:
    def test_with_graphics(self, writer):
        parent = _parent()
        fig = MlFigure()
        lg = LGraphic()
        lg.setL("en")
        g = Graphic()
        g.setFilename("f.png")
        lg.setGraphic(g)
        fig.addLGraphics(lg)
        writer.writeMlFigureLGraphics(parent, fig)
        assert parent[0].tag == "L-GRAPHIC"
        assert parent[0].attrib['L'] == "en"
        assert parent[0][0].tag == "GRAPHIC"
        assert parent[0][0].attrib['FILENAME'] == "f.png"

    def test_without_l(self, writer):
        parent = _parent()
        fig = MlFigure()
        lg = LGraphic()
        lg.setL(None)
        fig.addLGraphics(lg)
        writer.writeMlFigureLGraphics(parent, fig)
        assert 'L' not in parent[0].attrib

    def test_empty(self, writer):
        parent = _parent()
        fig = MlFigure()
        writer.writeMlFigureLGraphics(parent, fig)
        assert len(parent) == 0


class TestWriteMlFigure:
    def test_writes_figure(self, writer):
        parent = _parent()
        fig = MlFigure()
        lg = LGraphic()
        lg.setL("en")
        fig.addLGraphics(lg)
        writer.writeMlFigure(parent, fig)
        assert parent[0].tag == "L-GRAPHIC"


class TestSetMlFigures:
    def test_with_figures(self, writer):
        parent = _parent()
        fig = MlFigure()
        lg = LGraphic()
        lg.setL("en")
        fig.addLGraphics(lg)
        writer.setMlFigures(parent, "FIGURE", [fig])
        assert parent[0].tag == "FIGURE"

    def test_empty(self, writer):
        parent = _parent()
        writer.setMlFigures(parent, "FIGURE", [])
        assert len(parent) == 0


class TestWriteDocumentationBlock:
    def test_full_block(self, writer):
        parent = _parent()
        block = DocumentationBlock()
        para = MultiLanguageParagraph()
        l1 = LLongName()
        l1.l = "en"
        l1.value = "P"
        para.addL1(l1)
        block.addP(para)
        lst = ARList()
        lst.setType("number")
        block.addList(lst)
        fig = MlFigure()
        lg = LGraphic()
        lg.setL("en")
        fig.addLGraphics(lg)
        block.addFigure(fig)
        writer.writeDocumentationBlock(parent, "DOC", block)
        assert parent[0].tag == "DOC"
        assert parent[0].find("P") is not None
        assert parent[0].find("LIST") is not None
        assert parent[0].find("FIGURE") is not None

    def test_none(self, writer):
        parent = _parent()
        writer.writeDocumentationBlock(parent, "DOC", None)
        assert len(parent) == 0


class TestWriteGeneralAnnotation:
    def test_full_annotation(self, writer):
        parent = _parent()
        ann = Annotation()
        ln = MultilanguageLongName()
        l4 = LLongName()
        l4.l = "en"
        l4.value = "Label"
        ln.addL4(l4)
        ann.setLabel(ln)
        origin = ARLiteral()
        origin.setValue("ORIG")
        ann.setAnnotationOrigin(origin)
        block = DocumentationBlock()
        ann.setAnnotationText(block)
        writer.writeGeneralAnnotation(parent, ann)
        assert parent.find("LABEL") is not None
        assert parent.find("ANNOTATION-ORIGIN").text == "ORIG"
        assert parent.find("ANNOTATION-TEXT") is not None


class TestSetAnnotations:
    def test_with_annotations(self, writer):
        parent = _parent()
        ann = Annotation()
        writer.setAnnotations(parent, [ann])
        assert parent[0].tag == "ANNOTATIONS"
        assert parent[0][0].tag == "ANNOTATION"

    def test_empty(self, writer):
        parent = _parent()
        writer.setAnnotations(parent, [])
        assert len(parent) == 0


class TestWriteCollectionElementRefs:
    def test_with_refs(self, writer):
        parent = _parent()
        coll = Collection(_autosar(), "C")
        ref = RefType()
        ref.value = "/r"
        ref.dest = "COLLECTION"
        coll.addElementRef(ref)
        writer.writeCollectionElementRefs(parent, coll)
        assert parent[0].tag == "ELEMENT-REFS"
        assert parent[0][0].tag == "ELEMENT-REF"

    def test_empty(self, writer):
        parent = _parent()
        coll = Collection(_autosar(), "C")
        writer.writeCollectionElementRefs(parent, coll)
        assert len(parent) == 0


class TestWriteCollectionSourceElementRefs:
    def test_with_refs(self, writer):
        parent = _parent()
        coll = Collection(_autosar(), "C")
        ref = RefType()
        ref.value = "/src"
        coll.addSourceElementRef(ref)
        writer.writeCollectionSourceElementRefs(parent, coll)
        assert parent[0].tag == "SOURCE-ELEMENT-REFS"
        assert parent[0][0].tag == "SOURCE-ELEMENT-REF"

    def test_empty(self, writer):
        parent = _parent()
        coll = Collection(_autosar(), "C")
        writer.writeCollectionSourceElementRefs(parent, coll)
        assert len(parent) == 0


class TestWriteCollection:
    def test_full_collection(self, writer):
        parent = _parent()
        coll = Collection(_autosar(), "Coll")
        ac = ARLiteral()
        ac.setValue("AUTO")
        coll.setAutoCollect(ac)
        role = ARLiteral()
        role.setValue("ROLE")
        coll.setElementRole(role)
        ref = RefType()
        ref.value = "/e"
        coll.addElementRef(ref)
        sref = RefType()
        sref.value = "/s"
        coll.addSourceElementRef(sref)
        writer.writeCollection(parent, coll)
        assert parent[0].tag == "COLLECTION"
        assert parent[0].find("SHORT-NAME").text == "Coll"
        assert parent[0].find("AUTO-COLLECT").text == "AUTO"
        assert parent[0].find("ELEMENT-ROLE").text == "ROLE"
        assert parent[0].find("ELEMENT-REFS") is not None
        assert parent[0].find("SOURCE-ELEMENT-REFS") is not None

    def test_none(self, writer):
        parent = _parent()
        writer.writeCollection(parent, None)
        assert len(parent) == 0


class TestWriteKeywordClassifications:
    def test_with_classifications(self, writer):
        parent = _parent()
        kw = Keyword(_autosar(), "Kw")
        c1 = ARLiteral()
        c1.setValue("C1")
        kw.addClassification(c1)
        writer.writeKeywordClassifications(parent, kw)
        assert parent[0].tag == "CLASSIFICATIONS"
        assert parent[0][0].tag == "CLASSIFICATION"
        assert parent[0][0].text == "C1"

    def test_empty(self, writer):
        parent = _parent()
        kw = Keyword(_autosar(), "Kw")
        writer.writeKeywordClassifications(parent, kw)
        assert len(parent) == 0


class TestWriteKeyword:
    def test_full_keyword(self, writer):
        parent = _parent()
        kw = Keyword(_autosar(), "Kw")
        abbr = ARLiteral()
        abbr.setValue("ABBR")
        kw.setAbbrName(abbr)
        c1 = ARLiteral()
        c1.setValue("CL")
        kw.addClassification(c1)
        writer.writeKeyword(parent, kw)
        assert parent[0].tag == "KEYWORD"
        assert parent[0].find("SHORT-NAME").text == "Kw"
        assert parent[0].find("ABBR-NAME").text == "ABBR"
        assert parent[0].find("CLASSIFICATIONS") is not None

    def test_none(self, writer):
        parent = _parent()
        writer.writeKeyword(parent, None)
        assert len(parent) == 0


class TestWriteKeywordSetKeywords:
    def test_with_keywords(self, writer):
        parent = _parent()
        ks = KeywordSet(_autosar(), "KS")
        kw = Keyword(_autosar(), "Kw")
        ks.keywords.append(kw)
        writer.writeKeywordSetKeywords(parent, ks)
        assert parent[0].tag == "KEYWORDS"
        assert parent[0][0].tag == "KEYWORD"

    def test_empty(self, writer):
        parent = _parent()
        ks = KeywordSet(_autosar(), "KS")
        writer.writeKeywordSetKeywords(parent, ks)
        assert len(parent) == 0

    def test_unsupported_type(self, warning_writer):
        parent = _parent()
        ks = KeywordSet(_autosar(), "KS")
        ks.keywords.append("not_a_keyword")
        warning_writer.writeKeywordSetKeywords(parent, ks)
        assert parent[0].tag == "KEYWORDS"


class TestWriteKeywordSet:
    def test_with_keywords(self, writer):
        parent = _parent()
        ks = KeywordSet(_autosar(), "KS")
        kw = Keyword(_autosar(), "Kw")
        ks.keywords.append(kw)
        writer.writeKeywordSet(parent, ks)
        assert parent[0].tag == "KEYWORD-SET"
        assert parent[0].find("SHORT-NAME").text == "KS"
        assert parent[0].find("KEYWORDS") is not None

    def test_none(self, writer):
        parent = _parent()
        writer.writeKeywordSet(parent, None)
        assert len(parent) == 0


class TestWritePortPrototypeBlueprint:
    def test_with_interface_ref(self, writer):
        parent = _parent()
        bp = PortPrototypeBlueprint(_autosar(), "BP")
        ref = RefType()
        ref.value = "/if"
        ref.dest = "PORT-INTERFACE"
        bp.setInterfaceRef(ref)
        writer.writePortPrototypeBlueprint(parent, bp)
        assert parent[0].tag == "PORT-PROTOTYPE-BLUEPRINT"
        assert parent[0].find("SHORT-NAME").text == "BP"
        assert parent[0].find("INTERFACE-REF") is not None

    def test_none(self, writer):
        parent = _parent()
        writer.writePortPrototypeBlueprint(parent, None)
        assert len(parent) == 0


class TestWriteModeDeclarationMappingFirstModeRefs:
    def test_with_refs(self, writer):
        parent = _parent()
        m = ModeDeclarationMapping(_autosar(), "M")
        ref = RefType()
        ref.value = "/first"
        m.addFirstModeRef(ref)
        writer.writeModeDeclarationMappingFirstModeRefs(parent, m)
        assert parent[0].tag == "FIRST-MODE-REFS"
        assert parent[0][0].tag == "FIRST-MODE-REF"

    def test_empty(self, writer):
        parent = _parent()
        m = ModeDeclarationMapping(_autosar(), "M")
        writer.writeModeDeclarationMappingFirstModeRefs(parent, m)
        assert len(parent) == 0


class TestWriteModeDeclarationMapping:
    def test_full_mapping(self, writer):
        parent = _parent()
        m = ModeDeclarationMapping(_autosar(), "Map")
        ref = RefType()
        ref.value = "/first"
        m.addFirstModeRef(ref)
        sref = RefType()
        sref.value = "/second"
        sref.dest = "MODE-DECLARATION"
        m.setSecondModeRef(sref)
        writer.writeModeDeclarationMapping(parent, m)
        assert parent[0].tag == "MODE-DECLARATION-MAPPING"
        assert parent[0].find("SHORT-NAME").text == "Map"
        assert parent[0].find("FIRST-MODE-REFS") is not None
        assert parent[0].find("SECOND-MODE-REF") is not None

    def test_none(self, writer):
        parent = _parent()
        writer.writeModeDeclarationMapping(parent, None)
        assert len(parent) == 0


class TestWriteModeDeclarationMappingSetMappings:
    def test_with_mappings(self, writer):
        parent = _parent()
        ms = ModeDeclarationMappingSet(_autosar(), "MS")
        m = ModeDeclarationMapping(_autosar(), "M")
        m.secondModeRef = None
        ms.modeDeclarationMappings.append(m)
        writer.writeModeDeclarationMappingSetModeDeclarationMappings(
            parent, ms)
        assert parent[0].tag == "MODE-DECLARATION-MAPPINGS"
        assert parent[0][0].tag == "MODE-DECLARATION-MAPPING"

    def test_empty(self, writer):
        parent = _parent()
        ms = ModeDeclarationMappingSet(_autosar(), "MS")
        writer.writeModeDeclarationMappingSetModeDeclarationMappings(
            parent, ms)
        assert len(parent) == 0

    def test_unsupported_type(self, warning_writer):
        parent = _parent()
        ms = ModeDeclarationMappingSet(_autosar(), "MS")
        ms.modeDeclarationMappings.append("not_a_mapping")
        warning_writer.writeModeDeclarationMappingSetModeDeclarationMappings(
            parent, ms)
        assert parent[0].tag == "MODE-DECLARATION-MAPPINGS"


class TestWriteModeDeclarationMappingSet:
    def test_with_mappings(self, writer):
        parent = _parent()
        ms = ModeDeclarationMappingSet(_autosar(), "MS")
        m = ModeDeclarationMapping(_autosar(), "M")
        m.secondModeRef = None
        ms.modeDeclarationMappings.append(m)
        writer.writeModeDeclarationMappingSet(parent, ms)
        assert parent[0].tag == "MODE-DECLARATION-MAPPING-SET"
        assert parent[0].find("SHORT-NAME").text == "MS"
        assert parent.find("MODE-DECLARATION-MAPPINGS") is not None

    def test_none(self, writer):
        parent = _parent()
        writer.writeModeDeclarationMappingSet(parent, None)
        assert len(parent) == 0


class TestWriteDescribable:
    def test_writes_attributes(self, writer):
        parent = _parent()
        desc = ConcreteDescribable()
        desc.timestamp = "2024-01-01T00:00:00"
        writer.writeDescribable(parent, desc)
        assert parent.attrib['T'] == "2024-01-01T00:00:00"

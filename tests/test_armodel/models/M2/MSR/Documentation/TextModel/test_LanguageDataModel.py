"""
This module contains tests for the LanguageDataModel module in MSR.Documentation.TextModel.
"""

from abc import ABC
from typing import Optional, get_type_hints

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Enumerations import XmlSpaceEnum
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import AtpMixedString
from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements import Br, EmphasisText, IndexEntry, Superscript, Tt, Xref, XrefTarget
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import (
    LanguageSpecific,
    LEnum,
    LLongName,
    LOverviewParagraph,
    LParagraph,
    LPlainText,
    LVerbatim,
    MixedContentForOverviewParagraph,
    MixedContentForParagraph,
    MixedContentForPlainText,
    MixedContentForVerbatim,
    SlParagraph,
    WhitespaceControlled,
)


class TestLEnum:
    """Test class for LEnum class."""

    def test_l_enum_members(self):
        """Test that LEnum has the expected members."""
        assert LEnum.AA == "aa"
        assert LEnum.EN == "en"
        assert LEnum.DE == "de"
        assert LEnum.FOR_ALL == "forAll"

    def test_l_enum_values(self):
        """Test that LEnum values are all valid."""
        l_enum = LEnum()
        assert l_enum.validateEnumValue("en")
        assert l_enum.validateEnumValue("de")
        assert not l_enum.validateEnumValue("xx")

    def test_l_enum_initialization(self):
        """Test that an LEnum object can be initialized."""
        l_enum = LEnum()
        assert l_enum is not None


class TestLanguageSpecific:
    """Test class for LanguageSpecific abstract class."""

    def test_language_specific_abstract_class(self):
        """Test that LanguageSpecific cannot be instantiated directly."""
        # This should raise NotImplementedError
        with pytest.raises(TypeError):
            LanguageSpecific()

    def test_language_specific_initialization(self):
        """Test that a concrete subclass can be initialized with default values."""

        # Create a concrete subclass for testing
        class ConcreteLanguageSpecific(LanguageSpecific):
            def __init__(self):
                super().__init__()

        concrete_lang_spec = ConcreteLanguageSpecific()
        assert concrete_lang_spec.l is None
        assert concrete_lang_spec.value == ""

    def test_language_specific_l_methods(self):
        """Test the l getter and setter."""

        class ConcreteLanguageSpecific(LanguageSpecific):
            def __init__(self):
                super().__init__()

        concrete_lang_spec = ConcreteLanguageSpecific()
        l_val = LEnum()

        result = concrete_lang_spec.setL(l_val)
        assert concrete_lang_spec.getL() == l_val
        assert result == concrete_lang_spec

        concrete_lang_spec.setL(None)
        assert concrete_lang_spec.getL() == l_val

    def test_language_specific_value_methods(self):
        """Test the value getter and setter."""

        class ConcreteLanguageSpecific(LanguageSpecific):
            def __init__(self):
                super().__init__()

        concrete_lang_spec = ConcreteLanguageSpecific()
        value = "test_value"

        result = concrete_lang_spec.setValue(value)
        assert concrete_lang_spec.getValue() == value
        assert result == concrete_lang_spec

        concrete_lang_spec.setValue(None)
        assert concrete_lang_spec.getValue() == value


class TestLOverviewParagraph:
    """Test class for LOverviewParagraph class."""

    def test_l_overview_paragraph_base_chain(self):
        """LOverviewParagraph must extend MixedContentForOverviewParagraph and LanguageSpecific per Table 9.91."""
        assert issubclass(LOverviewParagraph, MixedContentForOverviewParagraph)
        assert issubclass(LOverviewParagraph, LanguageSpecific)
        assert issubclass(LOverviewParagraph, ARObject)
        assert isinstance(LOverviewParagraph(), LOverviewParagraph)

    def test_l_overview_paragraph_inherits_mixed_content_accessors(self):
        """LOverviewParagraph inherits the mixed-content accessors from MixedContentForOverviewParagraph (Table 9.91 Base row)."""
        l_overview_paragraph = LOverviewParagraph()
        tt = Tt()
        assert l_overview_paragraph.setTt(tt) is l_overview_paragraph
        assert l_overview_paragraph.getTt() is tt
        assert l_overview_paragraph.setTt(None) is l_overview_paragraph
        assert l_overview_paragraph.getTt() is tt

    def test_l_overview_paragraph_initialization(self):
        """Test that an LOverviewParagraph object can be initialized."""
        l_overview_paragraph = LOverviewParagraph()
        assert l_overview_paragraph.l is None
        assert l_overview_paragraph.value == ""
        assert l_overview_paragraph.blueprintValue is None

    def test_l_overview_paragraph_docstring_verbatim(self):
        """Docstring must equal the spec Note from Table 9.91 verbatim."""
        import inspect

        expected = "MixedContentForOverviewParagraph in one particular language. " "The language is denoted in the attribute l."
        assert inspect.cleandoc(LOverviewParagraph.__doc__) == expected

    def test_l_overview_paragraph_blueprint_value_methods(self):
        """Test the blueprintValue getter and setter (Table 9.91 attribute row)."""
        l_overview_paragraph = LOverviewParagraph()
        value = "This is the overview text."

        result = l_overview_paragraph.setBlueprintValue(value)
        assert l_overview_paragraph.getBlueprintValue() == value
        assert result == l_overview_paragraph

        l_overview_paragraph.setBlueprintValue(None)
        assert l_overview_paragraph.getBlueprintValue() == value

    def test_l_overview_paragraph_blueprint_value_annotation_is_optional(self):
        """Accessors must carry Optional[str] hints per Rule 0003 and chain via LOverviewParagraph."""
        getter_hints = get_type_hints(LOverviewParagraph.getBlueprintValue)
        setter_hints = get_type_hints(LOverviewParagraph.setBlueprintValue)

        assert getter_hints["return"] == Optional[str]
        assert setter_hints["value"] == Optional[str]
        assert setter_hints["return"] == LOverviewParagraph


class TestLParagraph:
    """Test class for LParagraph class."""

    def test_l_paragraph_initialization(self):
        """Test that an LParagraph object can be initialized."""
        l_paragraph = LParagraph()
        assert l_paragraph.l is None
        assert l_paragraph.value == ""

    def test_l_paragraph_base_chain(self):
        """LParagraph must extend MixedContentForParagraph and LanguageSpecific per Table 9.92."""
        assert issubclass(LParagraph, MixedContentForParagraph)
        assert issubclass(LParagraph, LanguageSpecific)
        assert isinstance(LParagraph(), LParagraph)

    def test_l_paragraph_docstring_verbatim(self):
        """Docstring must equal the spec Note from Table 9.92 verbatim."""
        import inspect

        expected = "This is the text for a paragraph in one particular language. " "The language is denoted in the attribute l."
        assert inspect.cleandoc(LParagraph.__doc__) == expected

    def test_l_paragraph_inherits_mixed_content_accessors(self):
        """LParagraph inherits the mixed-content accessors from MixedContentForParagraph."""
        l_paragraph = LParagraph()
        tt = Tt()
        assert l_paragraph.setTt(tt) is l_paragraph
        assert l_paragraph.getTt() is tt
        assert l_paragraph.setTt(None) is l_paragraph
        assert l_paragraph.getTt() is tt


class TestSlParagraph:
    def test_initialization(self):
        paragraph = SlParagraph()

        assert paragraph.l is None
        assert paragraph.value == ""
        assert paragraph.br is None
        assert paragraph.xref is None

    def test_l_getter_and_setter(self):
        paragraph = SlParagraph()

        assert paragraph.getL() is None
        assert paragraph.setL("en") is paragraph
        assert paragraph.getL() == "en"
        assert paragraph.setL(None) is paragraph
        assert paragraph.getL() == "en"


class TestMixedContentForOverviewParagraph:
    def test_abstract_guard_and_defaults(self):
        with pytest.raises(TypeError):
            MixedContentForOverviewParagraph()

        class ConcreteMixedContent(MixedContentForOverviewParagraph):
            pass

        content = ConcreteMixedContent()
        assert content.br is None
        assert content.e is None
        assert content.ft is None
        assert content.ie is None
        assert content.sub is None
        assert content.sup is None
        assert content.traceRef is None
        assert content.tt is None
        assert content.xref is None
        assert content.xrefTarget is None
        assert content.getMixedString() is None

    def test_base_anchoring(self):
        """Most-derived base anchoring per Table 9.3 Base row ARObject + the <<atpMixedString>> mixin (hierarchy doc target shape)."""
        assert MixedContentForOverviewParagraph.__bases__ == (ARObject, AtpMixedString, ABC)

    def test_docstring_verbatim(self):
        """Docstring must equal the spec Note from Table 9.3 verbatim."""
        import inspect

        expected = "This is the text model of a restricted paragraph item within a documentation. " "Such restricted paragraphs are used mainly for overview items, e.g. desc."
        assert inspect.cleandoc(MixedContentForOverviewParagraph.__doc__) == expected

    def test_typed_getters_and_setters(self):
        class ConcreteMixedContent(MixedContentForOverviewParagraph):
            pass

        content = ConcreteMixedContent()
        values = {
            "Br": Br(),
            "E": EmphasisText(),
            "Ft": object(),
            "Ie": IndexEntry(),
            "Sub": Superscript(),
            "Sup": Superscript(),
            "TraceRef": object(),
            "Tt": Tt(),
            "Xref": Xref(),
            "XrefTarget": object(),
        }
        for name, value in values.items():
            setter = getattr(content, "set" + name)
            getter = getattr(content, "get" + name)
            assert setter(value) is content
            assert getter() is value
            assert setter(None) is content
            assert getter() is value

    def test_mixin_accessors(self):
        """getMixedString/setMixedString are stereotype-inherent (no spec rows) via the AtpMixedString mixin."""

        class ConcreteMixedContent(MixedContentForOverviewParagraph):
            pass

        content = ConcreteMixedContent()
        assert content.setMixedString("overview text") is content
        assert content.getMixedString() == "overview text"
        content.setMixedString(None)
        assert content.getMixedString() == "overview text"

    def test_annotation_hints(self):
        """PDF-typed accessors per Rule 0003; ft/traceRef carry forward references (SlOverviewParagraph queued, Traceable TYPE_CHECKING-only)."""
        expected_hints = {
            "Br": Optional[Br],
            "E": Optional[EmphasisText],
            "Ie": Optional[IndexEntry],
            "Sub": Optional[Superscript],
            "Sup": Optional[Superscript],
            "Tt": Optional[Tt],
            "Xref": Optional[Xref],
            "XrefTarget": Optional[XrefTarget],
        }
        for name, expected in expected_hints.items():
            getter_hints = get_type_hints(getattr(MixedContentForOverviewParagraph, "get" + name))
            setter_hints = get_type_hints(getattr(MixedContentForOverviewParagraph, "set" + name))
            assert getter_hints["return"] == expected, name
            assert setter_hints["value"] == expected, name

        assert MixedContentForOverviewParagraph.setFt.__annotations__["value"] == "Optional['SlOverviewParagraph']"
        assert MixedContentForOverviewParagraph.setTraceRef.__annotations__["value"] == "Optional[Traceable]"


class TestMixedContentForParagraph:
    def test_abstract_guard_and_defaults(self):
        with pytest.raises(TypeError):
            MixedContentForParagraph()

        class ConcreteMixedContent(MixedContentForParagraph):
            pass

        content = ConcreteMixedContent()
        assert content.br is None
        assert content.e is None
        assert content.ft is None
        assert content.ie is None
        assert content.std is None
        assert content.sub is None
        assert content.sup is None
        assert content.traceRef is None
        assert content.tt is None
        assert content.xdoc is None
        assert content.xfile is None
        assert content.xref is None
        assert content.xrefTarget is None

    def test_typed_getters_and_setters(self):
        class ConcreteMixedContent(MixedContentForParagraph):
            pass

        content = ConcreteMixedContent()
        values = {
            "Br": object(),
            "E": object(),
            "Ft": object(),
            "Ie": object(),
            "Std": object(),
            "Sub": object(),
            "Sup": object(),
            "TraceRef": object(),
            "Tt": object(),
            "Xdoc": object(),
            "Xfile": object(),
            "Xref": object(),
            "XrefTarget": object(),
        }
        for name, value in values.items():
            setter = getattr(content, "set" + name)
            getter = getattr(content, "get" + name)
            assert setter(value) is content
            assert getter() is value
            assert setter(None) is content
            assert getter() is value


class TestLLongName:
    """Test class for LLongName class."""

    def test_l_long_name_initialization(self):
        """Test that an LLongName object can be initialized."""
        l_long_name = LLongName()
        assert l_long_name.l is None
        assert l_long_name.value == ""
        assert l_long_name.e is None
        assert l_long_name.ie is None
        assert l_long_name.sub is None
        assert l_long_name.sup is None
        assert l_long_name.tt is None
        assert l_long_name.blueprintValue is None

    def test_l_long_name_e_methods(self):
        """Test the e getter and setter."""
        l_long_name = LLongName()
        e = EmphasisText()

        result = l_long_name.setE(e)
        assert l_long_name.getE() == e
        assert result == l_long_name

        l_long_name.setE(None)
        assert l_long_name.getE() == e

    def test_l_long_name_ie_methods(self):
        """Test the ie getter and setter."""
        l_long_name = LLongName()
        ie = IndexEntry()

        result = l_long_name.setIe(ie)
        assert l_long_name.getIe() == ie
        assert result == l_long_name

        l_long_name.setIe(None)
        assert l_long_name.getIe() == ie

    def test_l_long_name_sub_methods(self):
        """Test the sub getter and setter."""
        l_long_name = LLongName()
        sub = Superscript()

        result = l_long_name.setSub(sub)
        assert l_long_name.getSub() == sub
        assert result == l_long_name

        l_long_name.setSub(None)
        assert l_long_name.getSub() == sub

    def test_l_long_name_sup_methods(self):
        """Test the sup getter and setter."""
        l_long_name = LLongName()
        sup = Superscript()

        result = l_long_name.setSup(sup)
        assert l_long_name.getSup() == sup
        assert result == l_long_name

        l_long_name.setSup(None)
        assert l_long_name.getSup() == sup

    def test_l_long_name_tt_methods(self):
        """Test the tt getter and setter."""
        l_long_name = LLongName()
        tt = Tt()

        result = l_long_name.setTt(tt)
        assert l_long_name.getTt() == tt
        assert result == l_long_name

        l_long_name.setTt(None)
        assert l_long_name.getTt() == tt

    def test_l_long_name_blueprint_value_methods(self):
        """Test the blueprintValue getter and setter."""
        l_long_name = LLongName()
        value = "StringName"

        result = l_long_name.setBlueprintValue(value)
        assert l_long_name.getBlueprintValue() == value
        assert result == l_long_name

        l_long_name.setBlueprintValue(None)
        assert l_long_name.getBlueprintValue() == value


class TestWhitespaceControlled:
    """Spec-contract tests for WhitespaceControlled (Table 9.7)."""

    def test_abstract_guard_and_defaults(self):
        with pytest.raises(TypeError):
            WhitespaceControlled()

        class ConcreteWhitespace(WhitespaceControlled):
            pass

        whitespace = ConcreteWhitespace()
        assert whitespace.getXmlSpace() is None

    def test_base_anchoring(self):
        """Most-derived base anchoring per Table 9.7 Base row ARObject (no atpMixedString stereotype — XSD group appinfo is atpObject only)."""
        assert WhitespaceControlled.__bases__ == (ARObject, ABC)

    def test_docstring_verbatim(self):
        """Docstring must equal the spec Note from Table 9.7 verbatim."""
        import inspect

        expected = 'This meta-class represents the ability to control the white-space handling e.g. in xml serialization. This is implemented by adding the attribute "space".'
        assert inspect.cleandoc(WhitespaceControlled.__doc__) == expected

    def test_typed_getter_and_setter(self):
        """getXmlSpace/setXmlSpace round-trip the XmlSpaceEnum value (Table 9.7 single attribute row xmlSpace, Mult. 1, kind attr)."""

        class ConcreteWhitespace(WhitespaceControlled):
            pass

        whitespace = ConcreteWhitespace()
        value = XmlSpaceEnum().setValue(XmlSpaceEnum.PRESERVE)
        assert whitespace.setXmlSpace(value) is whitespace
        assert whitespace.getXmlSpace() is value
        assert whitespace.getXmlSpace().getValue() == "preserve"
        whitespace.setXmlSpace(None)
        assert whitespace.getXmlSpace() is value

    def test_has_exact_own_members(self):
        """Field-to-spec cross-check: Table 9.7 carries exactly one Attribute row (xmlSpace), so the class adds exactly that field beyond the ARObject anchor."""

        class _BareARObject(ARObject):
            pass

        class ConcreteWhitespace(WhitespaceControlled):
            pass

        assert set(vars(ConcreteWhitespace()).keys()) == set(vars(_BareARObject()).keys()) | {"xmlSpace"}


class TestMixedContentForPlainText:
    def test_abstract_guard_and_defaults(self):
        with pytest.raises(TypeError):
            MixedContentForPlainText()

        class ConcreteMixedContent(MixedContentForPlainText):
            pass

        content = ConcreteMixedContent()
        assert content.getMixedString() is None

    def test_base_anchoring(self):
        """Most-derived base anchoring per Table 9.94 Base row ARObject + the <<atpMixedString>> mixin (sibling MCFOP shape; the WhitespaceControlled re-parent belongs to that class's own queue row)."""
        assert MixedContentForPlainText.__bases__ == (ARObject, AtpMixedString, ABC)

    def test_docstring_verbatim(self):
        """Docstring must equal the spec Note from Table 9.94 verbatim."""
        import inspect

        expected = "This represents a plain text which conceptually is handled as mixed contents. " "It is modeled as such for symmetry reasons."
        assert inspect.cleandoc(MixedContentForPlainText.__doc__) == expected

    def test_mixin_accessors(self):
        """getMixedString/setMixedString are stereotype-inherent (no spec rows) via the AtpMixedString mixin."""

        class ConcreteMixedContent(MixedContentForPlainText):
            pass

        content = ConcreteMixedContent()
        assert content.setMixedString("plain text") is content
        assert content.getMixedString() == "plain text"
        content.setMixedString(None)
        assert content.getMixedString() == "plain text"

    def test_has_no_own_members(self):
        """Field-to-spec cross-check: Table 9.94 carries no Attribute rows, so MixedContentForPlainText adds no fields beyond the ARObject anchor."""

        class _BareARObject(ARObject):
            pass

        class ConcreteMixedContent(MixedContentForPlainText):
            pass

        assert set(vars(ConcreteMixedContent()).keys()) == set(vars(_BareARObject()).keys())


class TestLPlainText:
    """Test class for LPlainText class."""

    def test_l_plain_text_base_chain(self):
        """LPlainText must extend MixedContentForPlainText, LanguageSpecific and WhitespaceControlled per Table 9.96."""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

        assert issubclass(LPlainText, MixedContentForPlainText)
        assert issubclass(LPlainText, LanguageSpecific)
        assert issubclass(LPlainText, WhitespaceControlled)
        assert issubclass(LPlainText, ARObject)
        assert isinstance(LPlainText(), LPlainText)

    def test_l_plain_text_inherits_mixed_content_accessors(self):
        """LPlainText inherits the mixed-content accessors from MixedContentForPlainText (Table 9.96 Base row)."""
        l_plain_text = LPlainText()
        assert l_plain_text.setMixedString("plain text") is l_plain_text
        assert l_plain_text.getMixedString() == "plain text"
        assert l_plain_text.setMixedString(None) is l_plain_text
        assert l_plain_text.getMixedString() == "plain text"

    def test_l_plain_text_initialization(self):
        """Test that an LPlainText object can be initialized."""
        l_plain_text = LPlainText()
        assert l_plain_text.l is None
        assert l_plain_text.value == ""

    def test_l_plain_text_docstring_verbatim(self):
        """Docstring must equal the spec Note from Table 9.96 verbatim."""
        import inspect

        expected = "This represents plain string in one particular language. " "The language is denoted in the attribute l."
        assert inspect.cleandoc(LPlainText.__doc__) == expected

    def test_l_plain_text_inherited_accessors(self):
        """LPlainText inherits the l/value accessors from LanguageSpecific (Table 9.96 has no own Attribute rows)."""
        l_plain_text = LPlainText()

        result = l_plain_text.setL("DE")
        assert l_plain_text.getL() == "DE"
        assert result is l_plain_text

        result = l_plain_text.setValue("plain text")
        assert l_plain_text.getValue() == "plain text"
        assert result is l_plain_text

        l_plain_text.setL(None)
        assert l_plain_text.getL() == "DE"

        l_plain_text.setValue(None)
        assert l_plain_text.getValue() == "plain text"

    def test_l_plain_text_has_no_own_members(self):
        """Field-to-spec cross-check: Table 9.96 carries no own Attribute rows, so LPlainText adds no fields beyond its bases (LanguageSpecific l/value + the WhitespaceControlled xmlSpace)."""

        class _BareLanguageSpecific(LanguageSpecific):
            pass

        assert set(vars(LPlainText()).keys()) == set(vars(_BareLanguageSpecific()).keys()) | {"xmlSpace"}


class TestMixedContentForVerbatim:
    def test_abstract_guard_and_defaults(self):
        with pytest.raises(TypeError):
            MixedContentForVerbatim()

        class ConcreteMixedContent(MixedContentForVerbatim):
            pass

        content = ConcreteMixedContent()
        assert content.br is None
        assert content.e is None
        assert content.tt is None
        assert content.xref is None
        assert content.getMixedString() is None

    def test_base_anchoring(self):
        """Most-derived base anchoring per Table 9.6 Base row ARObject + the <<atpMixedString>> mixin (sibling MCFPT shape; the WhitespaceControlled re-parent belongs to that class's own queue row)."""
        assert MixedContentForVerbatim.__bases__ == (ARObject, AtpMixedString, ABC)

    def test_docstring_verbatim(self):
        """Docstring must equal the spec Note from Table 9.6 verbatim."""
        import inspect

        expected = "This is the text model for preformatted (verbatim) text. It mainly consists of attributes which do not change the length on rendering. This class represents multilingual verbatim. Verbatim, sometimes called preformatted text, means that white-space is maintained. When verbatim is rendered in PDF or Online media, it is rendered using a monospaced font while white-space is obeyed. Blanks are rendered as well as newline characters. Even if there are inline elements, the length of the data shall not be influenced by formatting."
        assert inspect.cleandoc(MixedContentForVerbatim.__doc__) == expected

    def test_typed_getters_and_setters(self):
        class ConcreteMixedContent(MixedContentForVerbatim):
            pass

        content = ConcreteMixedContent()
        values = {
            "Br": Br(),
            "E": EmphasisText(),
            "Tt": Tt(),
            "Xref": Xref(),
        }
        for name, value in values.items():
            setter = getattr(content, "set" + name)
            getter = getattr(content, "get" + name)
            assert setter(value) is content
            assert getter() is value
            assert setter(None) is content
            assert getter() is value

    def test_mixin_accessors(self):
        """getMixedString/setMixedString are stereotype-inherent (no spec rows) via the AtpMixedString mixin."""

        class ConcreteMixedContent(MixedContentForVerbatim):
            pass

        content = ConcreteMixedContent()
        assert content.setMixedString("verbatim text") is content
        assert content.getMixedString() == "verbatim text"
        content.setMixedString(None)
        assert content.getMixedString() == "verbatim text"

    def test_annotation_hints(self):
        """PDF-typed accessors per Rule 0003 (Table 9.6 rows br/e/tt/xref, all runtime-resolvable types)."""
        expected_hints = {
            "Br": Optional[Br],
            "E": Optional[EmphasisText],
            "Tt": Optional[Tt],
            "Xref": Optional[Xref],
        }
        for name, expected in expected_hints.items():
            getter_hints = get_type_hints(getattr(MixedContentForVerbatim, "get" + name))
            setter_hints = get_type_hints(getattr(MixedContentForVerbatim, "set" + name))
            assert getter_hints["return"] == expected, name
            assert setter_hints["value"] == expected, name


class TestLVerbatim:
    """Test class for LVerbatim class."""

    def test_l_verbatim_base_chain(self):
        """LVerbatim must extend MixedContentForVerbatim and LanguageSpecific per the Table 9.89 Base row (ARObject , LanguageSpecific , MixedContentForVerbatim , WhitespaceControlled)."""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

        assert issubclass(LVerbatim, MixedContentForVerbatim)
        assert issubclass(LVerbatim, LanguageSpecific)
        assert issubclass(LVerbatim, WhitespaceControlled)
        assert issubclass(LVerbatim, ARObject)
        assert isinstance(LVerbatim(), LVerbatim)

    def test_l_verbatim_inherits_mixed_content_accessors(self):
        """LVerbatim inherits the Table 9.6 mixed-content accessors from MixedContentForVerbatim (Table 9.89 Base row)."""
        l_verbatim = LVerbatim()
        tt = Tt()
        assert l_verbatim.setTt(tt) is l_verbatim
        assert l_verbatim.getTt() is tt
        assert l_verbatim.setTt(None) is l_verbatim
        assert l_verbatim.getTt() is tt

    def test_l_verbatim_initialization(self):
        """Test that an LVerbatim object can be initialized."""
        l_verbatim = LVerbatim()
        assert l_verbatim.l is None
        assert l_verbatim.value == ""

    def test_l_verbatim_docstring_verbatim(self):
        """Docstring must equal the spec Note from Table 9.89 verbatim."""
        import inspect

        expected = "MixedContentForVerbatim in one particular language. " "The language is denoted in the attribute l."
        assert inspect.cleandoc(LVerbatim.__doc__) == expected

    def test_l_verbatim_inherited_accessors(self):
        """LVerbatim inherits the l/value accessors from LanguageSpecific (Table 9.89 has no own Attribute rows)."""
        l_verbatim = LVerbatim()

        result = l_verbatim.setL("DE")
        assert l_verbatim.getL() == "DE"
        assert result is l_verbatim

        result = l_verbatim.setValue("verbatim text")
        assert l_verbatim.getValue() == "verbatim text"
        assert result is l_verbatim

        l_verbatim.setL(None)
        assert l_verbatim.getL() == "DE"

        l_verbatim.setValue(None)
        assert l_verbatim.getValue() == "verbatim text"

    def test_l_verbatim_has_no_own_members(self):
        """Field-to-spec cross-check: Table 9.89 carries no own Attribute rows, so LVerbatim adds no fields beyond its bases (LanguageSpecific l/value + the MixedContentForVerbatim Table 9.6 members + the WhitespaceControlled xmlSpace)."""

        class _ReferenceBases(MixedContentForVerbatim, LanguageSpecific, WhitespaceControlled):
            pass

        assert set(vars(LVerbatim()).keys()) == set(vars(_ReferenceBases()).keys())

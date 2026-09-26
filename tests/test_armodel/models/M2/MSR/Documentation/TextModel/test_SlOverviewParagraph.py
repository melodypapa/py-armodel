"""
This module contains tests for the SlOverviewParagraph class in MSR.Documentation.TextModel.
"""

import inspect

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import AtpMixedString
from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements import Br, Tt
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import MixedContentForOverviewParagraph
from armodel.models.M2.MSR.Documentation.TextModel.SingleLanguageData import SlOverviewParagraph


class TestSlOverviewParagraph:
    def test_initialization(self):
        """SlOverviewParagraph is concrete (Table E.70 header carries no "(abstract)"; XSD complexType L107517 abstract="false") — instantiable with all inherited defaults."""
        paragraph = SlOverviewParagraph()

        assert paragraph.l is None
        assert paragraph.br is None
        assert paragraph.e is None
        assert paragraph.ft is None
        assert paragraph.ie is None
        assert paragraph.sub is None
        assert paragraph.sup is None
        assert paragraph.traceRef is None
        assert paragraph.tt is None
        assert paragraph.xref is None
        assert paragraph.xrefTarget is None
        assert paragraph.getMixedString() is None

    def test_base_chain(self):
        """Base anchoring per Table E.70 Base row ARObject, MixedContentForOverviewParagraph — the XSD-only legacy L attribute is an own optional member (Rule 0019-style combine), NOT an inherited base."""
        assert SlOverviewParagraph.__bases__ == (MixedContentForOverviewParagraph,)
        assert issubclass(SlOverviewParagraph, ARObject)
        assert issubclass(SlOverviewParagraph, AtpMixedString)
        assert [cls.__name__ for cls in SlOverviewParagraph.__mro__] == [
            "SlOverviewParagraph",
            "MixedContentForOverviewParagraph",
            "ARObject",
            "AtpMixedString",
            "ABC",
            "object",
        ]

    def test_docstring_verbatim(self):
        """Docstring must equal the spec Note from Table E.70 verbatim."""
        expected = (
            "MixedContentForOverviewParagraph in one particular language. The language is defined by the context. " "The attribute l is there only for backwards compatibility and shall be ignored."
        )
        assert inspect.cleandoc(SlOverviewParagraph.__doc__) == expected

    def test_legacy_l_is_the_only_own_member(self):
        """Field-to-spec cross-check (Rule 0001.3): Table E.70 carries ZERO attribute rows (dash placeholder); the XSD-only legacy L attribute (attributeGroup SL-OVERVIEW-PARAGRAPH, atp.Status="removed") is merged as the single own optional member per Rule 0019."""

        class Reference(MixedContentForOverviewParagraph):
            pass

        assert set(vars(SlOverviewParagraph())) - set(vars(Reference())) == {"l"}

    def test_language_accessors(self):
        """The legacy l accessor semantics mirror the Table 9.97 LanguageSpecific.l row (None no-op)."""
        paragraph = SlOverviewParagraph()

        assert paragraph.getL() is None
        assert paragraph.setL("en") is paragraph
        assert paragraph.getL() == "en"
        assert paragraph.setL(None) is paragraph
        assert paragraph.getL() == "en"

    def test_mixed_string_accessor(self):
        """The mixed text rides the AtpMixedString mixin (mixedString) — no LanguageSpecific value member."""
        paragraph = SlOverviewParagraph()

        assert paragraph.setMixedString("overview text") is paragraph
        assert paragraph.getMixedString() == "overview text"
        paragraph.setMixedString(None)
        assert paragraph.getMixedString() == "overview text"
        assert not hasattr(paragraph, "value")

    def test_inherited_mixed_content_accessors(self):
        """The Table 9.3 mixed-content accessors are inherited from MixedContentForOverviewParagraph."""
        paragraph = SlOverviewParagraph()
        br = Br()
        tt = Tt()

        assert paragraph.setBr(br) is paragraph
        assert paragraph.getBr() is br
        assert paragraph.setBr(None) is paragraph
        assert paragraph.getBr() is br

        assert paragraph.setTt(tt) is paragraph
        assert paragraph.getTt() is tt
        assert paragraph.setTt(None) is paragraph
        assert paragraph.getTt() is tt

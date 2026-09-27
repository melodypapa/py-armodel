from typing import Optional

from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import (
    LEnum,
    MixedContentForLongName,
    MixedContentForOverviewParagraph,
)


class SingleLanguageLongName(MixedContentForLongName):
    """
    SingleLanguageLongName
    """

    # SingleLanguageLongName method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 4.7, p.62
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (zero own members — Table 4.7 has no attribute rows: e/ie/sub/sup/tt inherited from MixedContentForLongName;
    #  2026-09-27 unification: the mixed text rides the AtpMixedString mixin (mixedString) inherited from
    #  MixedContentForLongName — SlOverviewParagraph/LVerbatim shape; the concrete `value` member and
    #  getValue/setValue are removed; stereotype-inherent, no spec row)


class SlOverviewParagraph(MixedContentForOverviewParagraph):
    """
    MixedContentForOverviewParagraph in one particular language. The language is defined by the context. The attribute l is there only for backwards compatibility and shall be ignored.
    """

    # SlOverviewParagraph method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table E.70, p.464
    # Spec: R23-11/AUTOSAR_00052.xsd, attributeGroup SL-OVERVIEW-PARAGRAPH, L107508 (XSD-only; legacy l)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getL      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setL      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # (Table E.70 carries zero attribute rows: the legacy `L` XML attribute is atp.Status="removed" and
    #  removed attributes are excluded from the PDF attribute tables — the member is XSD-only, owned by
    #  SlOverviewParagraph itself (mmt.qualifiedName="SlOverviewParagraph.L", L-ENUM--SIMPLE, minOccurs 0,
    #  xml.attribute=true), docstring verbatim from its own attributeGroup documentation; NOT the required
    #  LanguageSpecific.l (Table 9.97, Mult. 1) — "the language is defined by the context" rules out the
    #  LanguageSpecific role. AR-version history: L introduced R4.2.2 on the ft class, SlOverviewParagraph
    #  created as the backwards-compatibility vehicle (FO GST footnote 5); already atp.Status="removed" with
    #  the same own-attribute shape in R4.3.1 (00044 L77362), R4.4.0 (00046 L83727) and R23-11 (00052 L107508).
    #  Rule 0019-style optional legacy member; the mixed text rides the AtpMixedString mixin (mixedString) via
    #  readMixedStringText/writeMixedStringText; Table 9.3 base members serialize on the consuming L-2
    #  element's FT child via readSlOverviewParagraph/writeSlOverviewParagraphContent)

    def __init__(self):
        super().__init__()

        # The attribute l is there only for backwards compatibility and shall be ignored.
        self.l: Optional[LEnum] = None

    def getL(self) -> Optional[LEnum]:
        """
        The attribute l is there only for backwards compatibility and shall be ignored.
        """
        return self.l

    def setL(self, value: Optional[LEnum]) -> "SlOverviewParagraph":
        """
        The attribute l is there only for backwards compatibility and shall be ignored. A None value is a no-op and does not overwrite an existing l.
        """
        if value is not None:
            self.l = value
        return self

from __future__ import annotations

from abc import ABC
from typing import TYPE_CHECKING, Optional
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import (
    AtpMixedString,
)
from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements import (
    Br,
    EmphasisText,
    IndexEntry,
    Superscript,
    Tt,
    Xref,
    XrefTarget,
)

if TYPE_CHECKING:
    from armodel.models.M2.MSR.Documentation.BlockElements.RequirementsTracing import Traceable
    from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements import Std, Xdoc, Xfile
    from armodel.models.M2.MSR.Documentation.TextModel.SlParagraph import SlParagraph


class LEnum(AREnum):
    """
    This denotes the possible language designators according to the two letter code of ISO 639.
    """

    # LEnum method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.97, p.350
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # (no methods) — enum value form serialized on LanguageSpecific.l / AdminData.language
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    # Afar Tags: atp.EnumerationLiteralIndex=0
    AA = "aa"
    # Abkhazian Tags: atp.EnumerationLiteralIndex=1
    AB = "ab"
    # Afrikaans Tags: atp.EnumerationLiteralIndex=2
    AF = "af"
    # Amharic Tags: atp.EnumerationLiteralIndex=3
    AM = "am"
    # Arabic Tags: atp.EnumerationLiteralIndex=4
    AR = "ar"
    # Assamese Tags: atp.EnumerationLiteralIndex=5
    AS = "as"
    # Aymara Tags: atp.EnumerationLiteralIndex=6
    AY = "ay"
    # Azerbaijani Tags: atp.EnumerationLiteralIndex=7
    AZ = "az"
    # Bashkir Tags: atp.EnumerationLiteralIndex=8
    BA = "ba"
    # Byelorussian Tags: atp.EnumerationLiteralIndex=9
    BE = "be"
    # Bulgarian Tags: atp.EnumerationLiteralIndex=10
    BG = "bg"
    # Bihari Tags: atp.EnumerationLiteralIndex=11
    BH = "bh"
    # Bislama Tags: atp.EnumerationLiteralIndex=12
    BI = "bi"
    # Bengali Tags: atp.EnumerationLiteralIndex=13
    BN = "bn"
    # Tibetian Tags: atp.EnumerationLiteralIndex=14
    BO = "bo"
    # Breton Tags: atp.EnumerationLiteralIndex=15
    BR = "br"
    # Catalan Tags: atp.EnumerationLiteralIndex=16
    CA = "ca"
    # Corsican Tags: atp.EnumerationLiteralIndex=17
    CO = "co"
    # Czech Tags: atp.EnumerationLiteralIndex=18
    CS = "cs"
    # Welsh Tags: atp.EnumerationLiteralIndex=19
    CY = "cy"
    # Danish Tags: atp.EnumerationLiteralIndex=20
    DA = "da"
    # German Tags: atp.EnumerationLiteralIndex=21
    DE = "de"
    # Bhutani Tags: atp.EnumerationLiteralIndex=22
    DZ = "dz"
    # Greek Tags: atp.EnumerationLiteralIndex=23
    EL = "el"
    # English Tags: atp.EnumerationLiteralIndex=24
    EN = "en"
    # Esperanto Tags: atp.EnumerationLiteralIndex=25
    EO = "eo"
    # Spanish Tags: atp.EnumerationLiteralIndex=26
    ES = "es"
    # Estonian Tags: atp.EnumerationLiteralIndex=27
    ET = "et"
    # Basque Tags: atp.EnumerationLiteralIndex=28
    EU = "eu"
    # Persian Tags: atp.EnumerationLiteralIndex=29
    FA = "fa"
    # Finnish Tags: atp.EnumerationLiteralIndex=30
    FI = "fi"
    # Fiji Tags: atp.EnumerationLiteralIndex=31
    FJ = "fj"
    # Faeroese Tags: atp.EnumerationLiteralIndex=32
    FO = "fo"
    # The content applies to all languages Tags: atp.EnumerationLiteralIndex=33
    FOR_ALL = "forAll"

    def __init__(self):
        super().__init__(
            (
                LEnum.AA,
                LEnum.AB,
                LEnum.AF,
                LEnum.AM,
                LEnum.AR,
                LEnum.AS,
                LEnum.AY,
                LEnum.AZ,
                LEnum.BA,
                LEnum.BE,
                LEnum.BG,
                LEnum.BH,
                LEnum.BI,
                LEnum.BN,
                LEnum.BO,
                LEnum.BR,
                LEnum.CA,
                LEnum.CO,
                LEnum.CS,
                LEnum.CY,
                LEnum.DA,
                LEnum.DE,
                LEnum.DZ,
                LEnum.EL,
                LEnum.EN,
                LEnum.EO,
                LEnum.ES,
                LEnum.ET,
                LEnum.EU,
                LEnum.FA,
                LEnum.FI,
                LEnum.FJ,
                LEnum.FO,
                LEnum.FOR_ALL,
            )
        )


class LanguageSpecific(ARObject, ABC):
    """
    This meta-class represents the ability to denote a particular language for which an object is applicable.
    """

    # LanguageSpecific method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.97, p.350
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getL         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setL         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getValue     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setValue     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        if type(self) is LanguageSpecific:
            raise TypeError("LanguageSpecific is an abstract class.")

        super().__init__()

        # This attribute denotes the language in which the language specific document entity is given. Note that "FOR-ALL" means, that the entity is applicable to all languages. It is language neutral. It follows ISO 639-1:2002 and is specified in upper case.
        self.l: Optional[LEnum] = None

        # The text content of the language specific entity.
        self.value: str = ""

    def getL(self) -> Optional[LEnum]:
        """
        This attribute denotes the language in which the language specific document entity is given. Note that "FOR-ALL" means, that the entity is applicable to all languages. It is language neutral. It follows ISO 639-1:2002 and is specified in upper case.
        """
        return self.l

    def setL(self, value: Optional[LEnum]) -> LanguageSpecific:
        """
        This attribute denotes the language in which the language specific document entity is given. Note that "FOR-ALL" means, that the entity is applicable to all languages. It is language neutral. It follows ISO 639-1:2002 and is specified in upper case. A None value is a no-op and does not overwrite an existing l.
        """
        if value is not None:
            self.l = value
        return self

    def getValue(self) -> str:
        """
        Gets the text content of the language specific entity.
        """
        return self.value

    def setValue(self, value: str) -> LanguageSpecific:
        """
        Sets the text content of the language specific entity. A None value is a no-op and does not overwrite an existing value.
        """
        if value is not None:
            self.value = value
        return self


class MixedContentForOverviewParagraph(ARObject, AtpMixedString, ABC):
    """
    This is the text model of a restricted paragraph item within a documentation. Such restricted paragraphs are used mainly for overview items, e.g. desc.
    """

    # MixedContentForOverviewParagraph method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.3, p.290
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element; members serialize on the consuming L-2 element via readMixedContentForOverviewParagraph/writeMixedContentForOverviewParagraph)
    # [x] __init__           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getBr              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setBr              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getE               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setE               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getFt              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setFt              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getIe              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setIe              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSub             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSub             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSup             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSup             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTraceRef        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTraceRef        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTt              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTt              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getXref            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setXref            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getXrefTarget      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setXrefTarget      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # (getMixedString/setMixedString inherited from the AtpMixedString mixin — stereotype-inherent, no spec rows)

    def __init__(self):
        if type(self) is MixedContentForOverviewParagraph:
            raise TypeError("MixedContentForOverviewParagraph is an abstract class.")

        super().__init__()

        # This element is the same as function here as in a HTML document i.e. it forces a line break.
        self.br: Optional[Br] = None

        # This is emphasis text. Tags: xml.sequenceOffset=60
        self.e: Optional[EmphasisText] = None

        # This is a foot note within a paragraph.
        self.ft: Optional["SlOverviewParagraph"] = None  # noqa: F821

        # This is an index entry. Tags: xml.sequenceOffset=100
        self.ie: Optional[IndexEntry] = None

        # This is superscript text. Tags: xml.sequenceOffset=90
        self.sub: Optional[Superscript] = None

        # This is subscript text. Tags: xml.sequenceOffset=80
        self.sup: Optional[Superscript] = None

        # This allows to place an arbitrary reference to a traceable object in documentation.
        self.traceRef: Optional[Traceable] = None

        # This is a technical term. Tags: xml.sequenceOffset=30
        self.tt: Optional[Tt] = None

        # This is a cross reference. Tags: xml.sequenceOffset=40
        self.xref: Optional[Xref] = None

        # This element specifies a reference target which can be scattered throughout the text. Tags: xml.sequenceOffset=50
        self.xrefTarget: Optional[XrefTarget] = None

    def getBr(self) -> Optional[Br]:
        """
        This element is the same as function here as in a HTML document i.e. it forces a line break.
        """
        return self.br

    def setBr(self, value: Optional[Br]) -> MixedContentForOverviewParagraph:
        """
        This element is the same as function here as in a HTML document i.e. it forces a line break. A None value is a no-op and does not overwrite an existing br.
        """
        if value is not None:
            self.br = value
        return self

    def getE(self) -> Optional[EmphasisText]:
        """
        This is emphasis text.
        """
        return self.e

    def setE(self, value: Optional[EmphasisText]) -> MixedContentForOverviewParagraph:
        """
        This is emphasis text. A None value is a no-op and does not overwrite an existing e.
        """
        if value is not None:
            self.e = value
        return self

    def getFt(self) -> Optional["SlOverviewParagraph"]:  # noqa: F821
        """
        This is a foot note within a paragraph.
        """
        return self.ft

    def setFt(self, value: Optional["SlOverviewParagraph"]) -> MixedContentForOverviewParagraph:  # noqa: F821
        """
        This is a foot note within a paragraph. A None value is a no-op and does not overwrite an existing ft.
        """
        if value is not None:
            self.ft = value
        return self

    def getIe(self) -> Optional[IndexEntry]:
        """
        This is an index entry.
        """
        return self.ie

    def setIe(self, value: Optional[IndexEntry]) -> MixedContentForOverviewParagraph:
        """
        This is an index entry. A None value is a no-op and does not overwrite an existing ie.
        """
        if value is not None:
            self.ie = value
        return self

    def getSub(self) -> Optional[Superscript]:
        """
        This is superscript text.
        """
        return self.sub

    def setSub(self, value: Optional[Superscript]) -> MixedContentForOverviewParagraph:
        """
        This is superscript text. A None value is a no-op and does not overwrite an existing sub.
        """
        if value is not None:
            self.sub = value
        return self

    def getSup(self) -> Optional[Superscript]:
        """
        This is subscript text.
        """
        return self.sup

    def setSup(self, value: Optional[Superscript]) -> MixedContentForOverviewParagraph:
        """
        This is subscript text. A None value is a no-op and does not overwrite an existing sup.
        """
        if value is not None:
            self.sup = value
        return self

    def getTraceRef(self) -> Optional[Traceable]:
        """
        This allows to place an arbitrary reference to a traceable object in documentation.
        """
        return self.traceRef

    def setTraceRef(self, value: Optional[Traceable]) -> MixedContentForOverviewParagraph:
        """
        This allows to place an arbitrary reference to a traceable object in documentation. A None value is a no-op and does not overwrite an existing traceRef.
        """
        if value is not None:
            self.traceRef = value
        return self

    def getTt(self) -> Optional[Tt]:
        """
        This is a technical term.
        """
        return self.tt

    def setTt(self, value: Optional[Tt]) -> MixedContentForOverviewParagraph:
        """
        This is a technical term. A None value is a no-op and does not overwrite an existing tt.
        """
        if value is not None:
            self.tt = value
        return self

    def getXref(self) -> Optional[Xref]:
        """
        This is a cross reference.
        """
        return self.xref

    def setXref(self, value: Optional[Xref]) -> MixedContentForOverviewParagraph:
        """
        This is a cross reference. A None value is a no-op and does not overwrite an existing xref.
        """
        if value is not None:
            self.xref = value
        return self

    def getXrefTarget(self) -> Optional[XrefTarget]:
        """
        This element specifies a reference target which can be scattered throughout the text.
        """
        return self.xrefTarget

    def setXrefTarget(self, value: Optional[XrefTarget]) -> MixedContentForOverviewParagraph:
        """
        This element specifies a reference target which can be scattered throughout the text. A None value is a no-op and does not overwrite an existing xrefTarget.
        """
        if value is not None:
            self.xrefTarget = value
        return self


class LOverviewParagraph(MixedContentForOverviewParagraph, LanguageSpecific):
    """
    MixedContentForOverviewParagraph in one particular language. The language is denoted in the attribute l.
    """

    # LOverviewParagraph method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.91, p.348
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__           [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getBlueprintValue  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setBlueprintValue  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # (inherited LanguageSpecific accessors are covered by their declaring class checklist;
    # blueprintValue is the BLUEPRINT-VALUE XML attribute on the L-2 role element — reader
    # readLOverviewParagraph/getLOverviewParagraphs, writer setLOverviewParagraph)

    def __init__(self):
        super().__init__()

        # This represents a description that documents how the value shall be defined when deriving objects from the blueprint. Tags: atp.Status=draft xml.attribute=true
        self.blueprintValue: Optional[str] = None

    def getBlueprintValue(self) -> Optional[str]:
        """
        This represents a description that documents how the value shall be defined when deriving objects from the blueprint. Tags: atp.Status=draft xml.attribute=true
        """
        return self.blueprintValue

    def setBlueprintValue(self, value: Optional[str]) -> LOverviewParagraph:
        """
        This represents a description that documents how the value shall be defined when deriving objects from the blueprint. Tags: atp.Status=draft xml.attribute=true

        A None value is a no-op and does not overwrite an existing blueprintValue.
        """
        if value is not None:
            self.blueprintValue = value
        return self


class MixedContentForLongName(ARObject, ABC):
    """
    This is the model for titles and long-names. It allows some emphasis and index entries but no reference target (which is provided by the identifiable in question). It is intended that the content model can also be rendered as plain text. The abstract class can be used for single language as well as for multi language elements.
    """

    # MixedContentForLongName method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 4.9, p.63
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getE         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setE         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getIe        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setIe        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSub       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSub       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSup       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSup       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTt        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTt        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        if type(self) is MixedContentForLongName:
            raise TypeError("MixedContentForLongName is an abstract class.")

        super().__init__()

        # This is emphasized text.
        self.e: Optional[EmphasisText] = None

        # This is an index entry.
        self.ie: Optional[IndexEntry] = None

        # This is subscript text.
        self.sub: Optional[Superscript] = None

        # This is superscript text.
        self.sup: Optional[Superscript] = None

        # This is a technical term.
        self.tt: Optional[Tt] = None

    def getE(self) -> Optional[EmphasisText]:
        """
        This is emphasized text.
        """
        return self.e

    def setE(self, value: Optional[EmphasisText]) -> MixedContentForLongName:
        """
        This is emphasized text. A None value is a no-op and does not overwrite an existing e.
        """
        if value is not None:
            self.e = value
        return self

    def getIe(self) -> Optional[IndexEntry]:
        """
        This is an index entry.
        """
        return self.ie

    def setIe(self, value: Optional[IndexEntry]) -> MixedContentForLongName:
        """
        This is an index entry. A None value is a no-op and does not overwrite an existing ie.
        """
        if value is not None:
            self.ie = value
        return self

    def getSub(self) -> Optional[Superscript]:
        """
        This is subscript text.
        """
        return self.sub

    def setSub(self, value: Optional[Superscript]) -> MixedContentForLongName:
        """
        This is subscript text. A None value is a no-op and does not overwrite an existing sub.
        """
        if value is not None:
            self.sub = value
        return self

    def getSup(self) -> Optional[Superscript]:
        """
        This is superscript text.
        """
        return self.sup

    def setSup(self, value: Optional[Superscript]) -> MixedContentForLongName:
        """
        This is superscript text. A None value is a no-op and does not overwrite an existing sup.
        """
        if value is not None:
            self.sup = value
        return self

    def getTt(self) -> Optional[Tt]:
        """
        This is a technical term.
        """
        return self.tt

    def setTt(self, value: Optional[Tt]) -> MixedContentForLongName:
        """
        This is a technical term. A None value is a no-op and does not overwrite an existing tt.
        """
        if value is not None:
            self.tt = value
        return self


class MixedContentForUnitNames(ARObject, ABC):
    """
    This is the text model for items with subscript and superscripts such as measurement unit designations. It is intended, that such models can easily be transcribed to a plain text model either by using appropriate characters or by transcribing like mˆ2.
    """

    # MixedContentForUnitNames method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table E.55, p.456
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element; SUB/SUP serialize as attributes on the consuming element)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getSub       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSub       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSup       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSup       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        if type(self) is MixedContentForUnitNames:
            raise TypeError("MixedContentForUnitNames is an abstract class.")

        super().__init__()

        # This is subscript text. Tags: xml.sequenceOffset=40
        self.sub: Optional[Superscript] = None

        # This is superscript text. Tags: xml.sequenceOffset=30
        self.sup: Optional[Superscript] = None

    def getSub(self) -> Optional[Superscript]:
        """
        This is subscript text.
        """
        return self.sub

    def setSub(self, value: Optional[Superscript]) -> MixedContentForUnitNames:
        """
        This is subscript text. A None value is a no-op and does not overwrite an existing sub.
        """
        if value is not None:
            self.sub = value
        return self

    def getSup(self) -> Optional[Superscript]:
        """
        This is superscript text.
        """
        return self.sup

    def setSup(self, value: Optional[Superscript]) -> MixedContentForUnitNames:
        """
        This is superscript text. A None value is a no-op and does not overwrite an existing sup.
        """
        if value is not None:
            self.sup = value
        return self


class MixedContentForParagraph(ARObject, ABC):
    """
    This mainly represents the text model of a full blown paragraph within a documentation.
    """

    # MixedContentForParagraph method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.2, p.289
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getBr  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setBr  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getE  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setE  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getFt  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setFt  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getIe  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setIe  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getStd  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setStd  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSub  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSub  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSup  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSup  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTraceRef  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTraceRef  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTt  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTt  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getXdoc  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setXdoc  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getXfile  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setXfile  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getXref  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setXref  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getXrefTarget  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setXrefTarget  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        if type(self) is MixedContentForParagraph:
            raise TypeError("MixedContentForParagraph is an abstract class.")

        super().__init__()

        # This element is the same as function here as in a HTML document i.e. it forces a line break.
        self.br: Optional[Br] = None

        # This is emphasized text.
        self.e: Optional[EmphasisText] = None

        # This is a foot note within a paragraph.
        self.ft: Optional[SlParagraph] = None

        # This is an index entry.
        self.ie: Optional[IndexEntry] = None

        # This is a refeernce to a standard.
        self.std: Optional[Std] = None

        # This is subscript text.
        self.sub: Optional[Superscript] = None

        # This is superscript text.
        self.sup: Optional[Superscript] = None

        # This allows to place an arbitrary reference to a traceable object in documentation.
        self.traceRef: Optional[Traceable] = None

        # This is a technical term.
        self.tt: Optional[Tt] = None

        # This is a reference to a printable external document.
        self.xdoc: Optional[Xdoc] = None

        # This represents a reference to an external file which usually cannot be printed.
        self.xfile: Optional[Xfile] = None

        # This is a cross reference.
        self.xref: Optional[Xref] = None

        # This element specifies a reference target which can be scattered throughout the text.
        self.xrefTarget: Optional[XrefTarget] = None

    def getBr(self) -> Optional[Br]:
        """
        This element is the same as function here as in a HTML document i.e. it forces a line break.
        """
        return self.br

    def setBr(self, value: Optional[Br]) -> MixedContentForParagraph:
        """
        This element is the same as function here as in a HTML document i.e. it forces a line break. A None value is a no-op and does not overwrite an existing br.
        """
        if value is not None:
            self.br = value
        return self

    def getE(self) -> Optional[EmphasisText]:
        """
        This is emphasized text.
        """
        return self.e

    def setE(self, value: Optional[EmphasisText]) -> MixedContentForParagraph:
        """
        This is emphasized text. A None value is a no-op and does not overwrite an existing e.
        """
        if value is not None:
            self.e = value
        return self

    def getFt(self) -> Optional[SlParagraph]:
        """
        This is a foot note within a paragraph.
        """
        return self.ft

    def setFt(self, value: Optional[SlParagraph]) -> MixedContentForParagraph:
        """
        This is a foot note within a paragraph. A None value is a no-op and does not overwrite an existing ft.
        """
        if value is not None:
            self.ft = value
        return self

    def getIe(self) -> Optional[IndexEntry]:
        """
        This is an index entry.
        """
        return self.ie

    def setIe(self, value: Optional[IndexEntry]) -> MixedContentForParagraph:
        """
        This is an index entry. A None value is a no-op and does not overwrite an existing ie.
        """
        if value is not None:
            self.ie = value
        return self

    def getStd(self) -> Optional[Std]:
        """
        This is a refeernce to a standard.
        """
        return self.std

    def setStd(self, value: Optional[Std]) -> MixedContentForParagraph:
        """
        This is a refeernce to a standard. A None value is a no-op and does not overwrite an existing std.
        """
        if value is not None:
            self.std = value
        return self

    def getSub(self) -> Optional[Superscript]:
        """
        This is subscript text.
        """
        return self.sub

    def setSub(self, value: Optional[Superscript]) -> MixedContentForParagraph:
        """
        This is subscript text. A None value is a no-op and does not overwrite an existing sub.
        """
        if value is not None:
            self.sub = value
        return self

    def getSup(self) -> Optional[Superscript]:
        """
        This is superscript text.
        """
        return self.sup

    def setSup(self, value: Optional[Superscript]) -> MixedContentForParagraph:
        """
        This is superscript text. A None value is a no-op and does not overwrite an existing sup.
        """
        if value is not None:
            self.sup = value
        return self

    def getTraceRef(self) -> Optional[Traceable]:
        """
        This allows to place an arbitrary reference to a traceable object in documentation.
        """
        return self.traceRef

    def setTraceRef(self, value: Optional[Traceable]) -> MixedContentForParagraph:
        """
        This allows to place an arbitrary reference to a traceable object in documentation. A None value is a no-op and does not overwrite an existing traceRef.
        """
        if value is not None:
            self.traceRef = value
        return self

    def getTt(self) -> Optional[Tt]:
        """
        This is a technical term.
        """
        return self.tt

    def setTt(self, value: Optional[Tt]) -> MixedContentForParagraph:
        """
        This is a technical term. A None value is a no-op and does not overwrite an existing tt.
        """
        if value is not None:
            self.tt = value
        return self

    def getXdoc(self) -> Optional[Xdoc]:
        """
        This is a reference to a printable external document.
        """
        return self.xdoc

    def setXdoc(self, value: Optional[Xdoc]) -> MixedContentForParagraph:
        """
        This is a reference to a printable external document. A None value is a no-op and does not overwrite an existing xdoc.
        """
        if value is not None:
            self.xdoc = value
        return self

    def getXfile(self) -> Optional[Xfile]:
        """
        This represents a reference to an external file which usually cannot be printed.
        """
        return self.xfile

    def setXfile(self, value: Optional[Xfile]) -> MixedContentForParagraph:
        """
        This represents a reference to an external file which usually cannot be printed. A None value is a no-op and does not overwrite an existing xfile.
        """
        if value is not None:
            self.xfile = value
        return self

    def getXref(self) -> Optional[Xref]:
        """
        This is a cross reference.
        """
        return self.xref

    def setXref(self, value: Optional[Xref]) -> MixedContentForParagraph:
        """
        This is a cross reference. A None value is a no-op and does not overwrite an existing xref.
        """
        if value is not None:
            self.xref = value
        return self

    def getXrefTarget(self) -> Optional[XrefTarget]:
        """
        This element specifies a reference target which can be scattered throughout the text.
        """
        return self.xrefTarget

    def setXrefTarget(self, value: Optional[XrefTarget]) -> MixedContentForParagraph:
        """
        This element specifies a reference target which can be scattered throughout the text. A None value is a no-op and does not overwrite an existing xrefTarget.
        """
        if value is not None:
            self.xrefTarget = value
        return self


class LParagraph(MixedContentForParagraph, LanguageSpecific):
    """
    This is the text for a paragraph in one particular language. The language is denoted in the attribute l.
    """

    # LParagraph method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.92, p.348
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # (inherited LanguageSpecific accessors and mixed-content members are covered by their declaring classes)

    def __init__(self):
        super().__init__()


class SlParagraph(MixedContentForParagraph, LanguageSpecific):
    """
    This is the text for a paragraph in one particular language. The language is defined by the context. The attribute l is there only for backwards compatibility and shall be ignored.
    """

    # SlParagraph method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table E.71, p.465
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # (inherited LanguageSpecific accessors and mixed-content members are covered by their declaring classes)

    def __init__(self):
        super().__init__()


class LLongName(MixedContentForLongName, LanguageSpecific):
    """
    MixedContentForLongNames in one particular language. The language is denoted in the attribute l.
    """

    # LLongName method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 4.7, p.62
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__             [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getBlueprintValue    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] setBlueprintValue    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self):
        super().__init__()

        # This represents a description that documents how the value shall be defined when deriving objects from the blueprint.
        self.blueprintValue: Optional[str] = None

    def getBlueprintValue(self) -> Optional[str]:
        """
        This represents a description that documents how the value shall be defined when deriving objects from the blueprint.
        """
        return self.blueprintValue

    def setBlueprintValue(self, value: Optional[str]) -> LLongName:
        """
        This represents a description that documents how the value shall be defined when deriving objects from the blueprint. A None value is a no-op and does not overwrite an existing blueprintValue.
        """
        if value is not None:
            self.blueprintValue = value
        return self


class LPlainText(LanguageSpecific):
    """
    This represents plain string in one particular language. The language is denoted in the attribute l.
    """

    # LPlainText method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.96, p.349
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # (no own attributes — Table 9.96 Attribute rows: none; inherited LanguageSpecific accessors
    #  getL/setL/getValue/setValue are covered by their declaring class checklist; the L-PLAIN-TEXT
    #  element serializes via the shared stamped setLanguageSpecific/readLanguageSpecific pair)

    def __init__(self):
        super().__init__()


class LVerbatim(LanguageSpecific):
    """
    MixedContentForVerbatim in one particular language. The language is denoted in the attribute l.
    """

    # LVerbatim method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.89, p.347
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # (no own attributes — Table 9.89 Attribute rows: none; inherited LanguageSpecific accessors
    #  getL/setL/getValue/setValue are covered by their declaring class checklist; the L-5
    #  element serializes via the shared stamped setLanguageSpecific/readLanguageSpecific pair)

    def __init__(self):
        super().__init__()

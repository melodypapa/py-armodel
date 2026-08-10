from abc import ABC
from typing import Optional
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements import (
    EmphasisText,
    IndexEntry,
    Superscript,
    Tt,
)


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

    def setL(self, value: Optional[LEnum]) -> "LanguageSpecific":
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

    def setValue(self, value: str) -> "LanguageSpecific":
        """
        Sets the text content of the language specific entity. A None value is a no-op and does not overwrite an existing value.
        """
        if value is not None:
            self.value = value
        return self


class LOverviewParagraph(LanguageSpecific):
    """
    Language-specific overview paragraph element.
    """

    # LOverviewParagraph method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()


class LParagraph(LanguageSpecific):
    """
    Language-specific paragraph element.
    """

    # LParagraph method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()


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

    def setE(self, value: Optional[EmphasisText]) -> "MixedContentForLongName":
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

    def setIe(self, value: Optional[IndexEntry]) -> "MixedContentForLongName":
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

    def setSub(self, value: Optional[Superscript]) -> "MixedContentForLongName":
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

    def setSup(self, value: Optional[Superscript]) -> "MixedContentForLongName":
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

    def setTt(self, value: Optional[Tt]) -> "MixedContentForLongName":
        """
        This is a technical term. A None value is a no-op and does not overwrite an existing tt.
        """
        if value is not None:
            self.tt = value
        return self


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

    def setBlueprintValue(self, value: Optional[str]) -> "LLongName":
        """
        This represents a description that documents how the value shall be defined when deriving objects from the blueprint. A None value is a no-op and does not overwrite an existing blueprintValue.
        """
        if value is not None:
            self.blueprintValue = value
        return self


class LPlainText(LanguageSpecific):
    """
    Language-specific plain text element.
    """

    # LPlainText method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()


class LVerbatim(LanguageSpecific):
    """
    Language-specific verbatim text element.
    """

    # LVerbatim method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

from __future__ import annotations

from abc import ABC
from typing import TYPE_CHECKING, Optional
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
    String,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Enumerations import (
    XmlSpaceEnum,
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
    from armodel.models.M2.MSR.Documentation.TextModel.SingleLanguageData import SlOverviewParagraph


class LEnum(AREnum):
    """
    This denotes the possible language designators according to the two letter code of ISO 639.
    """

    # LEnum method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.98, p.356
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods) — enum value form serialized on LanguageSpecific.l / AdminData.language
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # Afar Tags: atp.EnumerationLiteralIndex=0
    AA = "AA"
    # Abkhazian Tags: atp.EnumerationLiteralIndex=1
    AB = "AB"
    # Afrikaans Tags: atp.EnumerationLiteralIndex=2
    AF = "AF"
    # Amharic Tags: atp.EnumerationLiteralIndex=3
    AM = "AM"
    # Arabic Tags: atp.EnumerationLiteralIndex=4
    AR = "AR"
    # Assamese Tags: atp.EnumerationLiteralIndex=5
    AS = "AS"
    # Aymara Tags: atp.EnumerationLiteralIndex=6
    AY = "AY"
    # Azerbaijani Tags: atp.EnumerationLiteralIndex=7
    AZ = "AZ"
    # Bashkir Tags: atp.EnumerationLiteralIndex=8
    BA = "BA"
    # Byelorussian Tags: atp.EnumerationLiteralIndex=9
    BE = "BE"
    # Bulgarian Tags: atp.EnumerationLiteralIndex=10
    BG = "BG"
    # Bihari Tags: atp.EnumerationLiteralIndex=11
    BH = "BH"
    # Bislama Tags: atp.EnumerationLiteralIndex=12
    BI = "BI"
    # Bengali Tags: atp.EnumerationLiteralIndex=13
    BN = "BN"
    # Tibetian Tags: atp.EnumerationLiteralIndex=14
    BO = "BO"
    # Breton Tags: atp.EnumerationLiteralIndex=15
    BR = "BR"
    # Catalan Tags: atp.EnumerationLiteralIndex=16
    CA = "CA"
    # Corsican Tags: atp.EnumerationLiteralIndex=17
    CO = "CO"
    # Czech Tags: atp.EnumerationLiteralIndex=18
    CS = "CS"
    # Welsh Tags: atp.EnumerationLiteralIndex=19
    CY = "CY"
    # Danish Tags: atp.EnumerationLiteralIndex=20
    DA = "DA"
    # German Tags: atp.EnumerationLiteralIndex=21
    DE = "DE"
    # Bhutani Tags: atp.EnumerationLiteralIndex=22
    DZ = "DZ"
    # Greek Tags: atp.EnumerationLiteralIndex=23
    EL = "EL"
    # English Tags: atp.EnumerationLiteralIndex=24
    EN = "EN"
    # Esperanto Tags: atp.EnumerationLiteralIndex=25
    EO = "EO"
    # Spanish Tags: atp.EnumerationLiteralIndex=26
    ES = "ES"
    # Estonian Tags: atp.EnumerationLiteralIndex=27
    ET = "ET"
    # Basque Tags: atp.EnumerationLiteralIndex=28
    EU = "EU"
    # Persian Tags: atp.EnumerationLiteralIndex=29
    FA = "FA"
    # Finnish Tags: atp.EnumerationLiteralIndex=30
    FI = "FI"
    # Fiji Tags: atp.EnumerationLiteralIndex=31
    FJ = "FJ"
    # Faeroese Tags: atp.EnumerationLiteralIndex=32
    FO = "FO"
    # The content applies to all languages Tags: atp.EnumerationLiteralIndex=33
    FOR_ALL = "FOR-ALL"
    # French Tags: atp.EnumerationLiteralIndex=34
    FR = "FR"
    # Frisian Tags: atp.EnumerationLiteralIndex=35
    FY = "FY"
    # Irish Tags: atp.EnumerationLiteralIndex=36
    GA = "GA"
    # Scots Gaelic Tags: atp.EnumerationLiteralIndex=37
    GD = "GD"
    # Galician Tags: atp.EnumerationLiteralIndex=38
    GL = "GL"
    # Guarani Tags: atp.EnumerationLiteralIndex=39
    GN = "GN"
    # Gjarati Tags: atp.EnumerationLiteralIndex=40
    GU = "GU"
    # Hausa Tags: atp.EnumerationLiteralIndex=41
    HA = "HA"
    # Hindi Tags: atp.EnumerationLiteralIndex=42
    HI = "HI"
    # Croatian Tags: atp.EnumerationLiteralIndex=43
    HR = "HR"
    # Hungarian Tags: atp.EnumerationLiteralIndex=44
    HU = "HU"
    # Armenian Tags: atp.EnumerationLiteralIndex=45
    HY = "HY"
    # Interlingua Tags: atp.EnumerationLiteralIndex=46
    IA = "IA"
    # Interlingue Tags: atp.EnumerationLiteralIndex=47
    IE = "IE"
    # Inupiak Tags: atp.EnumerationLiteralIndex=48
    IK = "IK"
    # Indonesian Tags: atp.EnumerationLiteralIndex=49
    IN = "IN"
    # Icelandic Tags: atp.EnumerationLiteralIndex=50
    IS = "IS"
    # Italian Tags: atp.EnumerationLiteralIndex=51
    IT = "IT"
    # Hebrew Tags: atp.EnumerationLiteralIndex=52
    IW = "IW"
    # Japanese Tags: atp.EnumerationLiteralIndex=53
    JA = "JA"
    # Yiddish Tags: atp.EnumerationLiteralIndex=54
    JI = "JI"
    # Javanese Tags: atp.EnumerationLiteralIndex=55
    JW = "JW"
    # Georgian Tags: atp.EnumerationLiteralIndex=56
    KA = "KA"
    # Kazakh Tags: atp.EnumerationLiteralIndex=57
    KK = "KK"
    # Greenlandic Tags: atp.EnumerationLiteralIndex=58
    KL = "KL"
    # Cambodian Tags: atp.EnumerationLiteralIndex=59
    KM = "KM"
    # Kannada Tags: atp.EnumerationLiteralIndex=60
    KN = "KN"
    # Korean Tags: atp.EnumerationLiteralIndex=61
    KO = "KO"
    # Kashmiri Tags: atp.EnumerationLiteralIndex=62
    KS = "KS"
    # Kurdish Tags: atp.EnumerationLiteralIndex=63
    KU = "KU"
    # Kirghiz Tags: atp.EnumerationLiteralIndex=64
    KY = "KY"
    # Latin Tags: atp.EnumerationLiteralIndex=65
    LA = "LA"
    # Lingala Tags: atp.EnumerationLiteralIndex=66
    LN = "LN"
    # Laothian Tags: atp.EnumerationLiteralIndex=67
    LO = "LO"
    # Lithuanian Tags: atp.EnumerationLiteralIndex=68
    LT = "LT"
    # Lavian, Lettish Tags: atp.EnumerationLiteralIndex=69
    LV = "LV"
    # Malagasy Tags: atp.EnumerationLiteralIndex=70
    MG = "MG"
    # Maori Tags: atp.EnumerationLiteralIndex=71
    MI = "MI"
    # Macedonian Tags: atp.EnumerationLiteralIndex=72
    MK = "MK"
    # Malayalam Tags: atp.EnumerationLiteralIndex=73
    ML = "ML"
    # Mongolian Tags: atp.EnumerationLiteralIndex=74
    MN = "MN"
    # Moldavian Tags: atp.EnumerationLiteralIndex=75
    MO = "MO"
    # Marathi Tags: atp.EnumerationLiteralIndex=76
    MR = "MR"
    # Malay Tags: atp.EnumerationLiteralIndex=77
    MS = "MS"
    # Maltese Tags: atp.EnumerationLiteralIndex=78
    MT = "MT"
    # Burmese Tags: atp.EnumerationLiteralIndex=79
    MY = "MY"
    # Nauru Tags: atp.EnumerationLiteralIndex=80
    NA = "NA"
    # Nepali Tags: atp.EnumerationLiteralIndex=81
    NE = "NE"
    # Dutch Tags: atp.EnumerationLiteralIndex=82
    NL = "NL"
    # Norwegian Tags: atp.EnumerationLiteralIndex=83
    NO = "NO"
    # Occitan Tags: atp.EnumerationLiteralIndex=84
    OC = "OC"
    # (Afan) Oromo Tags: atp.EnumerationLiteralIndex=85
    OM = "OM"
    # Oriya Tags: atp.EnumerationLiteralIndex=86
    OR = "OR"
    # Punjabi Tags: atp.EnumerationLiteralIndex=87
    PA = "PA"
    # Polish Tags: atp.EnumerationLiteralIndex=88
    PL = "PL"
    # Pashto, Pushto Tags: atp.EnumerationLiteralIndex=89
    PS = "PS"
    # Portuguese Tags: atp.EnumerationLiteralIndex=90
    PT = "PT"
    # Quechua Tags: atp.EnumerationLiteralIndex=91
    QU = "QU"
    # Rhaeto-Romance Tags: atp.EnumerationLiteralIndex=92
    RM = "RM"
    # Kirundi Tags: atp.EnumerationLiteralIndex=93
    RN = "RN"
    # Romanian Tags: atp.EnumerationLiteralIndex=94
    RO = "RO"
    # Russian Tags: atp.EnumerationLiteralIndex=95
    RU = "RU"
    # Kinyarwanda Tags: atp.EnumerationLiteralIndex=96
    RW = "RW"
    # Sanskrit Tags: atp.EnumerationLiteralIndex=97
    SA = "SA"
    # Sindhi Tags: atp.EnumerationLiteralIndex=98
    SD = "SD"
    # Sangro Tags: atp.EnumerationLiteralIndex=99
    SG = "SG"
    # Serbo-Croatian Tags: atp.EnumerationLiteralIndex=100
    SH = "SH"
    # Singhalese Tags: atp.EnumerationLiteralIndex=101
    SI = "SI"
    # Slovak Tags: atp.EnumerationLiteralIndex=102
    SK = "SK"
    # Slovenian Tags: atp.EnumerationLiteralIndex=103
    SL = "SL"
    # Samoan Tags: atp.EnumerationLiteralIndex=104
    SM = "SM"
    # Shona Tags: atp.EnumerationLiteralIndex=105
    SN = "SN"
    # Somali Tags: atp.EnumerationLiteralIndex=106
    SO = "SO"
    # Albanian Tags: atp.EnumerationLiteralIndex=107
    SQ = "SQ"
    # Serbian Tags: atp.EnumerationLiteralIndex=108
    SR = "SR"
    # Siswati Tags: atp.EnumerationLiteralIndex=109
    SS = "SS"
    # Sesotho Tags: atp.EnumerationLiteralIndex=110
    ST = "ST"
    # Sundanese Tags: atp.EnumerationLiteralIndex=111
    SU = "SU"
    # Swedish Tags: atp.EnumerationLiteralIndex=112
    SV = "SV"
    # Swahili Tags: atp.EnumerationLiteralIndex=113
    SW = "SW"
    # Tamil Tags: atp.EnumerationLiteralIndex=114
    TA = "TA"
    # Tegulu Tags: atp.EnumerationLiteralIndex=115
    TE = "TE"
    # Tajik Tags: atp.EnumerationLiteralIndex=116
    TG = "TG"
    # Thai Tags: atp.EnumerationLiteralIndex=117
    TH = "TH"
    # Tigrinya Tags: atp.EnumerationLiteralIndex=118
    TI = "TI"
    # Turkmen Tags: atp.EnumerationLiteralIndex=119
    TK = "TK"
    # Tagalog Tags: atp.EnumerationLiteralIndex=120
    TL = "TL"
    # Setswana Tags: atp.EnumerationLiteralIndex=121
    TN = "TN"
    # Tonga Tags: atp.EnumerationLiteralIndex=122
    TO = "TO"
    # Turkish Tags: atp.EnumerationLiteralIndex=123
    TR = "TR"
    # Tsonga Tags: atp.EnumerationLiteralIndex=124
    TS = "TS"
    # Tatar Tags: atp.EnumerationLiteralIndex=125
    TT = "TT"
    # Twi Tags: atp.EnumerationLiteralIndex=126
    TW = "TW"
    # Ukrainian Tags: atp.EnumerationLiteralIndex=127
    UK = "UK"
    # Urdu Tags: atp.EnumerationLiteralIndex=128
    UR = "UR"
    # Uzbek Tags: atp.EnumerationLiteralIndex=129
    UZ = "UZ"
    # Vietnamese Tags: atp.EnumerationLiteralIndex=130
    VI = "VI"
    # Volapuk Tags: atp.EnumerationLiteralIndex=131
    VO = "VO"
    # Wolof Tags: atp.EnumerationLiteralIndex=132
    WO = "WO"
    # Xhosa Tags: atp.EnumerationLiteralIndex=133
    XH = "XH"
    # Yoruba Tags: atp.EnumerationLiteralIndex=134
    YO = "YO"
    # Chinese Tags: atp.EnumerationLiteralIndex=135
    ZH = "ZH"
    # Zulu Tags: atp.EnumerationLiteralIndex=136
    ZU = "ZU"

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
                LEnum.FR,
                LEnum.FY,
                LEnum.GA,
                LEnum.GD,
                LEnum.GL,
                LEnum.GN,
                LEnum.GU,
                LEnum.HA,
                LEnum.HI,
                LEnum.HR,
                LEnum.HU,
                LEnum.HY,
                LEnum.IA,
                LEnum.IE,
                LEnum.IK,
                LEnum.IN,
                LEnum.IS,
                LEnum.IT,
                LEnum.IW,
                LEnum.JA,
                LEnum.JI,
                LEnum.JW,
                LEnum.KA,
                LEnum.KK,
                LEnum.KL,
                LEnum.KM,
                LEnum.KN,
                LEnum.KO,
                LEnum.KS,
                LEnum.KU,
                LEnum.KY,
                LEnum.LA,
                LEnum.LN,
                LEnum.LO,
                LEnum.LT,
                LEnum.LV,
                LEnum.MG,
                LEnum.MI,
                LEnum.MK,
                LEnum.ML,
                LEnum.MN,
                LEnum.MO,
                LEnum.MR,
                LEnum.MS,
                LEnum.MT,
                LEnum.MY,
                LEnum.NA,
                LEnum.NE,
                LEnum.NL,
                LEnum.NO,
                LEnum.OC,
                LEnum.OM,
                LEnum.OR,
                LEnum.PA,
                LEnum.PL,
                LEnum.PS,
                LEnum.PT,
                LEnum.QU,
                LEnum.RM,
                LEnum.RN,
                LEnum.RO,
                LEnum.RU,
                LEnum.RW,
                LEnum.SA,
                LEnum.SD,
                LEnum.SG,
                LEnum.SH,
                LEnum.SI,
                LEnum.SK,
                LEnum.SL,
                LEnum.SM,
                LEnum.SN,
                LEnum.SO,
                LEnum.SQ,
                LEnum.SR,
                LEnum.SS,
                LEnum.ST,
                LEnum.SU,
                LEnum.SV,
                LEnum.SW,
                LEnum.TA,
                LEnum.TE,
                LEnum.TG,
                LEnum.TH,
                LEnum.TI,
                LEnum.TK,
                LEnum.TL,
                LEnum.TN,
                LEnum.TO,
                LEnum.TR,
                LEnum.TS,
                LEnum.TT,
                LEnum.TW,
                LEnum.UK,
                LEnum.UR,
                LEnum.UZ,
                LEnum.VI,
                LEnum.VO,
                LEnum.WO,
                LEnum.XH,
                LEnum.YO,
                LEnum.ZH,
                LEnum.ZU,
            )
        )


class LanguageSpecific(ARObject, ABC):
    """
    This meta-class represents the ability to denote a particular language for which an object is applicable.
    """

    # LanguageSpecific method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.97, p.350
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getL         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setL         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getValue     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setValue     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        if type(self) is LanguageSpecific:
            raise TypeError("LanguageSpecific is an abstract class.")

        super().__init__()

        # This attribute denotes the language in which the language specific document entity is given. Note that "FOR-ALL" means, that the entity is applicable to all languages. It is language neutral. It follows ISO 639-1:2002 and is specified in upper case. Tags: xml.attribute=true xml.enforceMinMultiplicity=true
        self.l: Optional[LEnum] = None

        # The text content of the language specific entity.
        self.value: str = ""

    def getL(self) -> Optional[LEnum]:
        """
        This attribute denotes the language in which the language specific document entity is given. Note that "FOR-ALL" means, that the entity is applicable to all languages. It is language neutral. It follows ISO 639-1:2002 and is specified in upper case. Tags: xml.attribute=true xml.enforceMinMultiplicity=true
        """
        return self.l

    def setL(self, value: Optional[LEnum]) -> LanguageSpecific:
        """
        This attribute denotes the language in which the language specific document entity is given. Note that "FOR-ALL" means, that the entity is applicable to all languages. It is language neutral. It follows ISO 639-1:2002 and is specified in upper case. Tags: xml.attribute=true xml.enforceMinMultiplicity=true. A None value is a no-op and does not overwrite an existing l.
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
    # Spec verified: R23-11
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
        self.ft: Optional[SlOverviewParagraph] = None

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

    def getFt(self) -> Optional[SlOverviewParagraph]:
        """
        This is a foot note within a paragraph.
        """
        return self.ft

    def setFt(self, value: Optional[SlOverviewParagraph]) -> MixedContentForOverviewParagraph:
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

    def setXrefTarget(self, value: Optional[XrefTarget]) -> MixedContentForOverviewParagraph:
        """
        This element specifies a reference target which can be scattered throughout the text. A None value is a no-op and does not overwrite an existing xrefTarget.
        """
        if value is not None:
            self.xrefTarget = value
        return self

    def getXrefTarget(self) -> Optional[XrefTarget]:
        """
        This element specifies a reference target which can be scattered throughout the text.
        """
        return self.xrefTarget

    def createXrefTarget(self, short_name: str) -> XrefTarget:
        """
        This element specifies a reference target which can be scattered throughout the text.

        Args:
            short_name: The short name of the XrefTarget

        Returns:
            The created (or existing) XrefTarget
        """
        if self.xrefTarget is not None and self.xrefTarget.getShortName() == short_name:
            return self.xrefTarget
        self.xrefTarget = XrefTarget(self, short_name)
        return self.xrefTarget


class LOverviewParagraph(MixedContentForOverviewParagraph, LanguageSpecific):
    """
    MixedContentForOverviewParagraph in one particular language. The language is denoted in the attribute l.
    """

    # LOverviewParagraph method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.91, p.348
    # Spec verified: R23-11 (2026-09-27, user 9b confirmation)
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
        self.blueprintValue: Optional[String] = None

    def getBlueprintValue(self) -> Optional[String]:
        """
        This represents a description that documents how the value shall be defined when deriving objects from the blueprint. Tags: atp.Status=draft xml.attribute=true
        """
        return self.blueprintValue

    def setBlueprintValue(self, value: Optional[String]) -> LOverviewParagraph:
        """
        This represents a description that documents how the value shall be defined when deriving objects from the blueprint. Tags: atp.Status=draft xml.attribute=true

        A None value is a no-op and does not overwrite an existing blueprintValue.
        """
        if value is not None:
            self.blueprintValue = value
        return self


class MixedContentForLongName(ARObject, AtpMixedString, ABC):
    """
    This is the model for titles and long-names. It allows some emphasis and index entries but no reference target (which is provided by the identifiable in question). It is intended that the content model can also be rendered as plain text. The abstract class can be used for single language as well as for multi language elements.
    """

    # MixedContentForLongName method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 4.9, p.63
    # Spec verified: R23-11 (2026-10-10, user 9b confirmation)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getE         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setE         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getIe        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setIe        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSub       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSub       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSup       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSup       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTt        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTt        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # (getMixedString/setMixedString inherited from the AtpMixedString mixin — stereotype-inherent, no spec rows;
    #  XSD group MIXED-CONTENT-FOR-LONG-NAME appinfo stereotypes "atpMixedString,atpObject" — 2026-09-27 unification)

    def __init__(self):
        if type(self) is MixedContentForLongName:
            raise TypeError("MixedContentForLongName is an abstract class.")

        super().__init__()

        # This is emphasized text Tags: xml.sequenceOffset=40
        self.e: Optional[EmphasisText] = None

        # This is an index entry. Tags: xml.sequenceOffset=70
        self.ie: Optional[IndexEntry] = None

        # This is subscript text. Tags: xml.sequenceOffset=60
        self.sub: Optional[Superscript] = None

        # This is superscript text. Tags: xml.sequenceOffset=50
        self.sup: Optional[Superscript] = None

        # This is a technical term. Tags: xml.sequenceOffset=30
        self.tt: Optional[Tt] = None

    def getE(self) -> Optional[EmphasisText]:
        """
        This is emphasized text Tags: xml.sequenceOffset=40
        """
        return self.e

    def setE(self, value: Optional[EmphasisText]) -> MixedContentForLongName:
        """
        This is emphasized text Tags: xml.sequenceOffset=40

        A None value is a no-op and does not overwrite an existing e.
        """
        if value is not None:
            self.e = value
        return self

    def getIe(self) -> Optional[IndexEntry]:
        """
        This is an index entry. Tags: xml.sequenceOffset=70
        """
        return self.ie

    def setIe(self, value: Optional[IndexEntry]) -> MixedContentForLongName:
        """
        This is an index entry. Tags: xml.sequenceOffset=70

        A None value is a no-op and does not overwrite an existing ie.
        """
        if value is not None:
            self.ie = value
        return self

    def getSub(self) -> Optional[Superscript]:
        """
        This is subscript text. Tags: xml.sequenceOffset=60
        """
        return self.sub

    def setSub(self, value: Optional[Superscript]) -> MixedContentForLongName:
        """
        This is subscript text. Tags: xml.sequenceOffset=60

        A None value is a no-op and does not overwrite an existing sub.
        """
        if value is not None:
            self.sub = value
        return self

    def getSup(self) -> Optional[Superscript]:
        """
        This is superscript text. Tags: xml.sequenceOffset=50
        """
        return self.sup

    def setSup(self, value: Optional[Superscript]) -> MixedContentForLongName:
        """
        This is superscript text. Tags: xml.sequenceOffset=50

        A None value is a no-op and does not overwrite an existing sup.
        """
        if value is not None:
            self.sup = value
        return self

    def getTt(self) -> Optional[Tt]:
        """
        This is a technical term. Tags: xml.sequenceOffset=30
        """
        return self.tt

    def setTt(self, value: Optional[Tt]) -> MixedContentForLongName:
        """
        This is a technical term. Tags: xml.sequenceOffset=30

        A None value is a no-op and does not overwrite an existing tt.
        """
        if value is not None:
            self.tt = value
        return self


class MixedContentForUnitNames(ARObject, AtpMixedString, ABC):
    """
    This is the text model for items with subscript and superscripts such as measurement unit designations. It is intended, that such models can easily be transcribed to a plain text model either by using appropriate characters or by transcribing like mˆ2.
    """

    # MixedContentForUnitNames method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table E.55, p.456 (trailing-caption render: table body above the caption line)
    # Spec verified: R23-11 (2026-09-27, user 9b confirmation)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element; SUP/SUB are xml.attribute=true on the consuming element)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getSub       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSub       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSup       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setSup       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # (getMixedString/setMixedString inherited from the AtpMixedString mixin — stereotype-inherent, no spec rows;
    #  XSD group MIXED-CONTENT-FOR-UNIT-NAMES appinfo stereotypes "atpMixedString,atpObject" — 2026-09-27 unification)

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

    def createStd(self, short_name: str) -> Std:
        """
        This is a refeernce to a standard.

        Args:
            short_name: The short name of the Std

        Returns:
            The created (or existing) Std
        """
        if self.std is not None and self.std.getShortName() == short_name:
            return self.std
        self.std = Std(self, short_name)
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

    def createXdoc(self, short_name: str) -> Xdoc:
        """
        This is a reference to a printable external document.

        Args:
            short_name: The short name of the Xdoc

        Returns:
            The created (or existing) Xdoc
        """
        if self.xdoc is not None and self.xdoc.getShortName() == short_name:
            return self.xdoc
        self.xdoc = Xdoc(self, short_name)
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

    def createXfile(self, short_name: str) -> Xfile:
        """
        This represents a reference to an external file which usually cannot be printed.

        Args:
            short_name: The short name of the Xfile

        Returns:
            The created (or existing) Xfile
        """
        if self.xfile is not None and self.xfile.getShortName() == short_name:
            return self.xfile
        self.xfile = Xfile(self, short_name)
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

    def setXrefTarget(self, value: Optional[XrefTarget]) -> MixedContentForParagraph:
        """
        This element specifies a reference target which can be scattered throughout the text. A None value is a no-op and does not overwrite an existing xrefTarget.
        """
        if value is not None:
            self.xrefTarget = value
        return self

    def getXrefTarget(self) -> Optional[XrefTarget]:
        """
        This element specifies a reference target which can be scattered throughout the text.
        """
        return self.xrefTarget

    def createXrefTarget(self, short_name: str) -> XrefTarget:
        """
        This element specifies a reference target which can be scattered throughout the text.

        Args:
            short_name: The short name of the XrefTarget

        Returns:
            The created (or existing) XrefTarget
        """
        if self.xrefTarget is not None and self.xrefTarget.getShortName() == short_name:
            return self.xrefTarget
        self.xrefTarget = XrefTarget(self, short_name)
        return self.xrefTarget


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
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 4.8, p.62
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__             [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getBlueprintValue    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setBlueprintValue    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # (blueprintValue is the BLUEPRINT-VALUE XML attribute on the L-4 element — reader readLLongName, writer setLLongName)

    def __init__(self):
        super().__init__()

        # This represents a description that documents how the value shall be defined when deriving objects from the blueprint. Tags: atp.Status=draft xml.attribute=true
        self.blueprintValue: Optional[String] = None

    def getBlueprintValue(self) -> Optional[String]:
        """
        This represents a description that documents how the value shall be defined when deriving objects from the blueprint. Tags: atp.Status=draft xml.attribute=true
        """
        return self.blueprintValue

    def setBlueprintValue(self, value: Optional[String]) -> LLongName:
        """
        This represents a description that documents how the value shall be defined when deriving objects from the blueprint. Tags: atp.Status=draft xml.attribute=true

        A None value is a no-op and does not overwrite an existing blueprintValue.
        """
        if value is not None:
            self.blueprintValue = value
        return self


class WhitespaceControlled(ARObject, ABC):
    """
    This meta-class represents the ability to control the white-space handling e.g. in xml serialization. This is implemented by adding the attribute "space".
    """

    # WhitespaceControlled method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.7, p.292
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no own XML element; xml:space serializes on the consuming L-10/L-5 elements via readWhitespaceControlled/writeWhitespaceControlled)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getXmlSpace  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setXmlSpace  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        if type(self) is WhitespaceControlled:
            raise TypeError("WhitespaceControlled is an abstract class.")

        super().__init__()

        # This attribute is used to signal an intention that in that element, white space should be preserved by applications. It is defined according to xml:space as declared by W3C. Tags: xml.attribute=true xml.attributeRef=true xml.enforceMinMultiplicity=true xml.name=space xml.nsPrefix=xml
        self.xmlSpace: Optional[XmlSpaceEnum] = None

    def getXmlSpace(self) -> Optional[XmlSpaceEnum]:
        """
        This attribute is used to signal an intention that in that element, white space should be preserved by applications. It is defined according to xml:space as declared by W3C.
        """
        return self.xmlSpace

    def setXmlSpace(self, value: Optional[XmlSpaceEnum]) -> WhitespaceControlled:
        """
        This attribute is used to signal an intention that in that element, white space should be preserved by applications. It is defined according to xml:space as declared by W3C. A None value is a no-op and does not overwrite an existing xmlSpace.
        """
        if value is not None:
            self.xmlSpace = value
        return self


class MixedContentForPlainText(WhitespaceControlled, AtpMixedString, ABC):
    """
    This represents a plain text which conceptually is handled as mixed contents. It is modeled as such for symmetry reasons.
    """

    # MixedContentForPlainText method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.94, p.349
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # (no own attributes — Table 9.94 Attribute rows: none; XSD group MIXED-CONTENT-FOR-PLAIN-TEXT
    #  (AUTOSAR_00052.xsd L81507) is an empty sequence, so the class serializes nothing itself —
    #  concrete subclasses (LPlainText) serialize via their own element helpers;
    #  getMixedString/setMixedString provided by the AtpMixedString base (mixin) — no spec row (stereotype-inherent);
    #  getXmlSpace/setXmlSpace inherited from the WhitespaceControlled base (Table 9.7) — tracked on that class's checklist)

    def __init__(self):
        if type(self) is MixedContentForPlainText:
            raise TypeError("MixedContentForPlainText is an abstract class.")

        super().__init__()


class LPlainText(MixedContentForPlainText, LanguageSpecific):
    """
    This represents plain string in one particular language. The language is denoted in the attribute l.
    """

    # LPlainText method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.96, p.349
    # Spec verified: R23-11 (2026-09-27, user 9b confirmation)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # (no own attributes — Table 9.96 Attribute rows: none; inherited LanguageSpecific accessors
    #  getL/setL/getValue/setValue are covered by their declaring class checklist; the L-PLAIN-TEXT
    #  element serializes via the shared stamped setLanguageSpecific/readLanguageSpecific pair)

    def __init__(self):
        super().__init__()


class MixedContentForVerbatim(WhitespaceControlled, AtpMixedString, ABC):
    """
    This is the text model for preformatted (verbatim) text. It mainly consists of attributes which do not change the length on rendering. This class represents multilingual verbatim. Verbatim, sometimes called preformatted text, means that white-space is maintained. When verbatim is rendered in PDF or Online media, it is rendered using a monospaced font while white-space is obeyed. Blanks are rendered as well as newline characters. Even if there are inline elements, the length of the data shall not be influenced by formatting.
    """

    # MixedContentForVerbatim method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.6, p.292
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element; members serialize on the consuming L-5 element via readMixedContentForVerbatim/writeMixedContentForVerbatim)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getBr     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setBr     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getE      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setE      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTt     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTt     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getXref   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setXref   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # (getMixedString/setMixedString inherited from the AtpMixedString mixin — stereotype-inherent, no spec rows;
    #  getXmlSpace/setXmlSpace inherited from the WhitespaceControlled base (Table 9.7) — tracked on that class's checklist)

    def __init__(self):
        if type(self) is MixedContentForVerbatim:
            raise TypeError("MixedContentForVerbatim is an abstract class.")

        super().__init__()

        # This element is the same as function here as in a HTML document i.e. it forces a line break. Tags: xml.sequenceOffset=50
        self.br: Optional[Br] = None

        # This is emphsized text. Note that in verbatim, the attribute font should not be considered since verbatim is always rendered as monospace font. Tags: xml.sequenceOffset=30
        self.e: Optional[EmphasisText] = None

        # This represents a technical term in verbatim. Note that it's the responibility of the user not to take a tt that would add additional character to the text (such as SgmlElement).
        self.tt: Optional[Tt] = None

        # This is a crossreference within a verbatim text. The attributes may disturb the arrangement of the text. It is subject to the author to keep this under control. Tags: xml.sequenceOffset=40
        self.xref: Optional[Xref] = None

    def getBr(self) -> Optional[Br]:
        """
        This element is the same as function here as in a HTML document i.e. it forces a line break.
        """
        return self.br

    def setBr(self, value: Optional[Br]) -> MixedContentForVerbatim:
        """
        This element is the same as function here as in a HTML document i.e. it forces a line break. A None value is a no-op and does not overwrite an existing br.
        """
        if value is not None:
            self.br = value
        return self

    def getE(self) -> Optional[EmphasisText]:
        """
        This is emphsized text. Note that in verbatim, the attribute font should not be considered since verbatim is always rendered as monospace font.
        """
        return self.e

    def setE(self, value: Optional[EmphasisText]) -> MixedContentForVerbatim:
        """
        This is emphsized text. Note that in verbatim, the attribute font should not be considered since verbatim is always rendered as monospace font. A None value is a no-op and does not overwrite an existing e.
        """
        if value is not None:
            self.e = value
        return self

    def getTt(self) -> Optional[Tt]:
        """
        This represents a technical term in verbatim. Note that it's the responibility of the user not to take a tt that would add additional character to the text (such as SgmlElement).
        """
        return self.tt

    def setTt(self, value: Optional[Tt]) -> MixedContentForVerbatim:
        """
        This represents a technical term in verbatim. Note that it's the responibility of the user not to take a tt that would add additional character to the text (such as SgmlElement). A None value is a no-op and does not overwrite an existing tt.
        """
        if value is not None:
            self.tt = value
        return self

    def getXref(self) -> Optional[Xref]:
        """
        This is a crossreference within a verbatim text. The attributes may disturb the arrangement of the text. It is subject to the author to keep this under control.
        """
        return self.xref

    def setXref(self, value: Optional[Xref]) -> MixedContentForVerbatim:
        """
        This is a crossreference within a verbatim text. The attributes may disturb the arrangement of the text. It is subject to the author to keep this under control. A None value is a no-op and does not overwrite an existing xref.
        """
        if value is not None:
            self.xref = value
        return self


class LVerbatim(MixedContentForVerbatim, LanguageSpecific):
    """
    MixedContentForVerbatim in one particular language. The language is denoted in the attribute l.
    """

    # LVerbatim method parity checklist:
    # Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 9.89, p.347
    # Spec verified: R23-11 (2026-09-27, user 9b confirmation)
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # (no own attributes — Table 9.89 Attribute rows: none; inherited LanguageSpecific accessors
    #  getL/setL/getValue/setValue are covered by their declaring class checklist; the Table 9.89
    #  Base row's MixedContentForVerbatim members (br/e/tt/xref) are covered by their declaring
    #  class checklist and serialize on this L-5 element via readMixedContentForVerbatim/
    #  writeMixedContentForVerbatim; the L-5 element also serializes via the shared stamped
    #  setLanguageSpecific/readLanguageSpecific pair)

    def __init__(self):
        super().__init__()

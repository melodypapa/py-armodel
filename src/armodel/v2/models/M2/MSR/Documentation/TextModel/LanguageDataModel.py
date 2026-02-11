"""
AUTOSAR Package - LanguageDataModel

Package: M2::MSR::Documentation::TextModel::LanguageDataModel
"""


from __future__ import annotations
from abc import ABC
from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
)


class LLongName(ARObject):
    """
    MixedContentForLongNames in one particular language. The language is denoted
    in the attribute l.
    
    Package: M2::MSR::Documentation::TextModel::LanguageDataModel::LLongName
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 179, Classic Platform
      R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 62, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents a description that documents how the be defined when deriving
        # objects from the.
        self._blueprintValue: Optional["String"] = None

    @property
    def blueprint_value(self) -> Optional["String"]:
        """Get blueprintValue (Pythonic accessor)."""
        return self._blueprintValue

    @blueprint_value.setter
    def blueprint_value(self, value: Optional["String"]) -> None:
        """
        Set blueprintValue with validation.
        
        Args:
            value: The blueprintValue to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._blueprintValue = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"blueprintValue must be String or str or None, got {type(value).__name__}"
            )
        self._blueprintValue = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBlueprintValue(self) -> "String":
        """
        AUTOSAR-compliant getter for blueprintValue.
        
        Returns:
            The blueprintValue value
        
        Note:
            Delegates to blueprint_value property (CODING_RULE_V2_00017)
        """
        return self.blueprint_value  # Delegates to property

    def setBlueprintValue(self, value: "String") -> LLongName:
        """
        AUTOSAR-compliant setter for blueprintValue with method chaining.
        
        Args:
            value: The blueprintValue to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to blueprint_value property setter (gets validation automatically)
        """
        self.blueprint_value = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_blueprint_value(self, value: Optional["String"]) -> LLongName:
        """
        Set blueprintValue and return self for chaining.
        
        Args:
            value: The blueprintValue to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_blueprint_value("value")
        """
        self.blueprint_value = value  # Use property setter (gets validation)
        return self



class WhitespaceControlled(ARObject, ABC):
    """
    This meta-class represents the ability to control the white-space handling
    e.g. in xml serialization. This is implemented by adding the attribute
    "space".
    
    Package: M2::MSR::Documentation::TextModel::LanguageDataModel::WhitespaceControlled
    
    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 292, Foundation
      R23-11)
    """
    def __init__(self):
        if type(self) is WhitespaceControlled:
            raise TypeError("WhitespaceControlled is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute is used to signal an intention that in that space should be
        # preserved by is defined according to xml:space as W3C.
        self._xmlSpace: "XmlSpaceEnum" = None

    @property
    def xml_space(self) -> "XmlSpaceEnum":
        """Get xmlSpace (Pythonic accessor)."""
        return self._xmlSpace

    @xml_space.setter
    def xml_space(self, value: "XmlSpaceEnum") -> None:
        """
        Set xmlSpace with validation.
        
        Args:
            value: The xmlSpace to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, XmlSpaceEnum):
            raise TypeError(
                f"xmlSpace must be XmlSpaceEnum, got {type(value).__name__}"
            )
        self._xmlSpace = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getXmlSpace(self) -> "XmlSpaceEnum":
        """
        AUTOSAR-compliant getter for xmlSpace.
        
        Returns:
            The xmlSpace value
        
        Note:
            Delegates to xml_space property (CODING_RULE_V2_00017)
        """
        return self.xml_space  # Delegates to property

    def setXmlSpace(self, value: "XmlSpaceEnum") -> WhitespaceControlled:
        """
        AUTOSAR-compliant setter for xmlSpace with method chaining.
        
        Args:
            value: The xmlSpace to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to xml_space property setter (gets validation automatically)
        """
        self.xml_space = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_xml_space(self, value: "XmlSpaceEnum") -> WhitespaceControlled:
        """
        Set xmlSpace and return self for chaining.
        
        Args:
            value: The xmlSpace to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_xml_space("value")
        """
        self.xml_space = value  # Use property setter (gets validation)
        return self



class LVerbatim(ARObject):
    """
    MixedContentForVerbatim in one particular language. The language is denoted
    in the attribute l.
    
    Package: M2::MSR::Documentation::TextModel::LanguageDataModel::LVerbatim
    
    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 347, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class LOverviewParagraph(ARObject):
    """
    MixedContentForOverviewParagraph in one particular language. The language is
    denoted in the attribute l.
    
    Package: M2::MSR::Documentation::TextModel::LanguageDataModel::LOverviewParagraph
    
    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 348, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents a description that documents how the be defined when deriving
        # objects from the.
        self._blueprintValue: Optional["String"] = None

    @property
    def blueprint_value(self) -> Optional["String"]:
        """Get blueprintValue (Pythonic accessor)."""
        return self._blueprintValue

    @blueprint_value.setter
    def blueprint_value(self, value: Optional["String"]) -> None:
        """
        Set blueprintValue with validation.
        
        Args:
            value: The blueprintValue to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._blueprintValue = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"blueprintValue must be String or str or None, got {type(value).__name__}"
            )
        self._blueprintValue = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBlueprintValue(self) -> "String":
        """
        AUTOSAR-compliant getter for blueprintValue.
        
        Returns:
            The blueprintValue value
        
        Note:
            Delegates to blueprint_value property (CODING_RULE_V2_00017)
        """
        return self.blueprint_value  # Delegates to property

    def setBlueprintValue(self, value: "String") -> LOverviewParagraph:
        """
        AUTOSAR-compliant setter for blueprintValue with method chaining.
        
        Args:
            value: The blueprintValue to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to blueprint_value property setter (gets validation automatically)
        """
        self.blueprint_value = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_blueprint_value(self, value: Optional["String"]) -> LOverviewParagraph:
        """
        Set blueprintValue and return self for chaining.
        
        Args:
            value: The blueprintValue to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_blueprint_value("value")
        """
        self.blueprint_value = value  # Use property setter (gets validation)
        return self



class LParagraph(ARObject):
    """
    This is the text for a paragraph in one particular language. The language is
    denoted in the attribute l.
    
    Package: M2::MSR::Documentation::TextModel::LanguageDataModel::LParagraph
    
    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 348, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class LPlainText(ARObject):
    """
    This represents plain string in one particular language. The language is
    denoted in the attribute l.
    
    Package: M2::MSR::Documentation::TextModel::LanguageDataModel::LPlainText
    
    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 349, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class LanguageSpecific(ARObject, ABC):
    """
    This meta-class represents the ability to denote a particular language for
    which an object is applicable.
    
    Package: M2::MSR::Documentation::TextModel::LanguageDataModel::LanguageSpecific
    
    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 350, Foundation
      R23-11)
    """
    def __init__(self):
        if type(self) is LanguageSpecific:
            raise TypeError("LanguageSpecific is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # ’This attribute denotes the language in which the document entity is given.
        # Note that that the entity is applicable to all is language neutral.
        # ISO 639-1:2002 and is specified in upper case.
        self._l: LEnum = None

    @property
    def l(self) -> LEnum:
        """Get l (Pythonic accessor)."""
        return self._l

    @l.setter
    def l(self, value: LEnum) -> None:
        """
        Set l with validation.
        
        Args:
            value: The l to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, LEnum):
            raise TypeError(
                f"l must be LEnum, got {type(value).__name__}"
            )
        self._l = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getL(self) -> LEnum:
        """
        AUTOSAR-compliant getter for l.
        
        Returns:
            The l value
        
        Note:
            Delegates to l property (CODING_RULE_V2_00017)
        """
        return self.l  # Delegates to property

    def setL(self, value: LEnum) -> LanguageSpecific:
        """
        AUTOSAR-compliant setter for l with method chaining.
        
        Args:
            value: The l to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to l property setter (gets validation automatically)
        """
        self.l = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_l(self, value: LEnum) -> LanguageSpecific:
        """
        Set l and return self for chaining.
        
        Args:
            value: The l to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_l("value")
        """
        self.l = value  # Use property setter (gets validation)
        return self


class LEnum(AREnum):
    """
    LEnum enumeration

This denotes the possible language designators according to the two letter code of ISO 639. Aggregated by AdminData.language, LanguageSpecific.l

Package: M2::MSR::Documentation::TextModel::LanguageDataModel
    """
    # Afar
    aa = "0"

    # Abkhazian
    ab = "1"

    # Afrikaans
    af = "2"

    # Amharic
    am = "3"

    # Arabic
    ar = "4"

    # Assamese
    assamese = "5"

    # Aymara
    ay = "6"

    # Azerbaijani
    az = "7"

    # Bashkir
    ba = "8"

    # Byelorussian
    be = "9"

    # Bulgarian
    bg = "10"

    # Bihari
    bh = "11"

    # Structure Template
    Generic = "None"

    # FO R23-11
    AUTOSARbi = "12"

    # Bengali
    bn = "13"

    # Tibetian
    bo = "14"

    # Breton
    br = "15"

    # Catalan
    ca = "16"

    # Corsican
    co = "17"

    # Czech
    cs = "18"

    # Welsh
    cy = "19"

    # Danish
    da = "20"

    # German
    de = "21"

    # Bhutani
    dz = "22"

    # Greek
    el = "23"

    # English
    en = "24"

    # Esperanto
    eo = "25"

    # Spanish
    es = "26"

    # Estonian
    et = "27"

    # Basque
    eu = "28"

    # Persian
    fa = "29"

    # Finnish
    fi = "30"

    # Fiji
    fj = "31"

    # Faeroese
    fo = "32"

    # Structure Template
    Generic = "None"

    # FO R23-11
    AUTOSAR = "None"

    # The content applies to all languages
    forAll = "33"

    # French
    fr = "34"

    # Frisian
    fy = "35"

    # Irish
    ga = "36"

    # Scots Gaelic
    gd = "37"

    # Galician
    gl = "38"

    # Guarani
    gn = "39"

    # Gjarati
    gu = "40"

    # Hausa
    ha = "41"

    # Hindi
    hi = "42"

    # Croatian
    hr = "43"

    # Hungarian
    hu = "44"

    # Armenian
    hy = "45"

    # Interlingua
    ia = "46"

    # Interlingue
    ie = "47"

    # Inupiak
    ik = "48"

    # Indonesian
    indonesian = "49"

    # Icelandic
    icelandic = "50"

    # Italian
    it = "51"

    # Hebrew
    iw = "52"

    # Japanese
    ja = "53"

    # Structure Template
    Generic = "None"

    # FO R23-11
    AUTOSARji = "54"

    # Javanese
    jw = "55"

    # Georgian
    ka = "56"

    # Kazakh
    kk = "57"

    # Greenlandic
    kl = "58"

    # Cambodian
    km = "59"

    # Kannada
    kn = "60"

    # Korean
    ko = "61"

    # Kashmiri
    ks = "62"

    # Kurdish
    ku = "63"

    # Kirghiz
    ky = "64"

    # Latin
    la = "65"

    # Lingala
    ln = "66"

    # Laothian
    lo = "67"

    # Lithuanian
    lt = "68"

    # Lavian, Lettish
    lv = "69"

    # Malagasy
    mg = "70"

    # Maori
    mi = "71"

    # Macedonian
    mk = "72"

    # Malayalam
    ml = "73"

    # Mongolian
    mn = "74"

    # Structure Template
    Generic = "None"

    # FO R23-11
    AUTOSARmo = "75"

    # Marathi
    mr = "76"

    # Malay
    ms = "77"

    # Maltese
    mt = "78"

    # Burmese
    my = "79"

    # Nauru
    na = "80"

    # Nepali
    ne = "81"

    # Dutch
    nl = "82"

    # Norwegian
    no = "83"

    # Occitan
    oc = "84"

    # (Afan) Oromo
    om = "85"

    # Oriya
    oriya = "86"

    # Punjabi
    pa = "87"

    # Polish
    pl = "88"

    # Pashto, Pushto
    ps = "89"

    # Portuguese
    pt = "90"

    # Quechua
    qu = "91"

    # Rhaeto-Romance
    rm = "92"

    # Kirundi
    rn = "93"

    # Romanian
    ro = "94"

    # Russian
    ru = "95"

    # Structure Template
    Generic = "None"

    # FO R23-11
    AUTOSARrw = "96"

    # Sanskrit
    sa = "97"

    # Sindhi
    sd = "98"

    # Sangro
    sg = "99"

    # Serbo-Croatian
    sh = "100"

    # Singhalese
    si = "101"

    # Slovak
    sk = "102"

    # Slovenian
    sl = "103"

    # Samoan
    sm = "104"

    # Shona
    sn = "105"

    # Somali
    so = "106"

    # Albanian
    sq = "107"

    # Serbian
    sr = "108"

    # Siswati
    ss = "109"

    # Sesotho
    st = "110"

    # Sundanese
    su = "111"

    # Swedish
    sv = "112"

    # Swahili
    sw = "113"

    # Tamil
    ta = "114"

    # Tegulu
    te = "115"

    # Tajik
    tg = "116"

    # Structure Template
    Generic = "None"

    # FO R23-11
    AUTOSARth = "117"

    # Tigrinya
    ti = "118"

    # Turkmen
    tk = "119"

    # Tagalog
    tl = "120"

    # Setswana
    tn = "121"

    # Tonga
    to = "122"

    # Turkish
    tr = "123"

    # Tsonga
    ts = "124"

    # Tatar
    tt = "125"

    # Twi
    tw = "126"

    # Ukrainian
    uk = "127"

    # Urdu
    ur = "128"

    # Uzbek
    uz = "129"

    # Vietnamese
    vi = "130"

    # Volapuk
    vo = "131"

    # Wolof
    wo = "132"

    # Xhosa
    xh = "133"

    # Yoruba
    yo = "134"

    # Chinese
    zh = "135"

    # Zulu
    zu = "136"

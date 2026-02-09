"""
AUTOSAR Package - SpecialData

Package: M2::MSR::AsamHdo::SpecialData
"""

from typing import Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
    RefType,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    MultilanguageReferrable,
)


class Sdg(ARObject):
    """
    Sdg (SpecialDataGroup) is a generic model which can be used to keep
    arbitrary information which is not explicitly modeled in the meta-model. Sdg
    can have various contents as defined by sdgContentsType. Special Data should
    only be used moderately since all elements should be defined in the
    meta-model. Thereby SDG should be considered as a temporary solution when no
    explicit model is available. If an sdg Caption is available, it is possible
    to establish a reference to the sdg structure.
    
    Package: M2::MSR::AsamHdo::SpecialData::Sdg
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 328, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 1004, Classic
      Platform R23-11)
      - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (Page 78, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 90, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attributes specifies an identifier.
        # Gid comes from the Identifier" which is the in XML.
        # The role of this attribute is the the name of an XML - element.
        self._gid: "NameToken" = None

    @property
    def gid(self) -> "NameToken":
        """Get gid (Pythonic accessor)."""
        return self._gid

    @gid.setter
    def gid(self, value: "NameToken") -> None:
        """
        Set gid with validation.
        
        Args:
            value: The gid to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, (NameToken, str)):
            raise TypeError(
                f"gid must be NameToken or str, got {type(value).__name__}"
            )
        self._gid = value
        # By this, a shortName etc.
        # can be the Sdg.
        self._sdgCaption: Optional["SdgCaption"] = None

    @property
    def sdg_caption(self) -> Optional["SdgCaption"]:
        """Get sdgCaption (Pythonic accessor)."""
        return self._sdgCaption

    @sdg_caption.setter
    def sdg_caption(self, value: Optional["SdgCaption"]) -> None:
        """
        Set sdgCaption with validation.
        
        Args:
            value: The sdgCaption to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sdgCaption = None
            return

        if not isinstance(value, SdgCaption):
            raise TypeError(
                f"sdgCaption must be SdgCaption or None, got {type(value).__name__}"
            )
        self._sdgCaption = value
        self._sdgContents: Optional["SdgContents"] = None

    @property
    def sdg_contents(self) -> Optional["SdgContents"]:
        """Get sdgContents (Pythonic accessor)."""
        return self._sdgContents

    @sdg_contents.setter
    def sdg_contents(self, value: Optional["SdgContents"]) -> None:
        """
        Set sdgContents with validation.
        
        Args:
            value: The sdgContents to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sdgContents = None
            return

        if not isinstance(value, SdgContents):
            raise TypeError(
                f"sdgContents must be SdgContents or None, got {type(value).__name__}"
            )
        self._sdgContents = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getGid(self) -> "NameToken":
        """
        AUTOSAR-compliant getter for gid.
        
        Returns:
            The gid value
        
        Note:
            Delegates to gid property (CODING_RULE_V2_00017)
        """
        return self.gid  # Delegates to property

    def setGid(self, value: "NameToken") -> "Sdg":
        """
        AUTOSAR-compliant setter for gid with method chaining.
        
        Args:
            value: The gid to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to gid property setter (gets validation automatically)
        """
        self.gid = value  # Delegates to property setter
        return self

    def getSdgCaption(self) -> "SdgCaption":
        """
        AUTOSAR-compliant getter for sdgCaption.
        
        Returns:
            The sdgCaption value
        
        Note:
            Delegates to sdg_caption property (CODING_RULE_V2_00017)
        """
        return self.sdg_caption  # Delegates to property

    def setSdgCaption(self, value: "SdgCaption") -> "Sdg":
        """
        AUTOSAR-compliant setter for sdgCaption with method chaining.
        
        Args:
            value: The sdgCaption to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to sdg_caption property setter (gets validation automatically)
        """
        self.sdg_caption = value  # Delegates to property setter
        return self

    def getSdgContents(self) -> "SdgContents":
        """
        AUTOSAR-compliant getter for sdgContents.
        
        Returns:
            The sdgContents value
        
        Note:
            Delegates to sdg_contents property (CODING_RULE_V2_00017)
        """
        return self.sdg_contents  # Delegates to property

    def setSdgContents(self, value: "SdgContents") -> "Sdg":
        """
        AUTOSAR-compliant setter for sdgContents with method chaining.
        
        Args:
            value: The sdgContents to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to sdg_contents property setter (gets validation automatically)
        """
        self.sdg_contents = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_gid(self, value: "NameToken") -> "Sdg":
        """
        Set gid and return self for chaining.
        
        Args:
            value: The gid to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_gid("value")
        """
        self.gid = value  # Use property setter (gets validation)
        return self

    def with_sdg_caption(self, value: Optional["SdgCaption"]) -> "Sdg":
        """
        Set sdgCaption and return self for chaining.
        
        Args:
            value: The sdgCaption to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_sdg_caption("value")
        """
        self.sdg_caption = value  # Use property setter (gets validation)
        return self

    def with_sdg_contents(self, value: Optional["SdgContents"]) -> "Sdg":
        """
        Set sdgContents and return self for chaining.
        
        Args:
            value: The sdgContents to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_sdg_contents("value")
        """
        self.sdg_contents = value  # Use property setter (gets validation)
        return self



class SdgContents(ARObject):
    """
    This meta-class represents the possible contents of a special data group. It
    can be an arbitrary mix of references, of primitive special data and nested
    special data groups.
    
    Package: M2::MSR::AsamHdo::SpecialData::SdgContents
    
    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 90, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is one particular special data element.
        self._sd: Optional["Sd"] = None

    @property
    def sd(self) -> Optional["Sd"]:
        """Get sd (Pythonic accessor)."""
        return self._sd

    @sd.setter
    def sd(self, value: Optional["Sd"]) -> None:
        """
        Set sd with validation.
        
        Args:
            value: The sd to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sd = None
            return

        if not isinstance(value, Sd):
            raise TypeError(
                f"sd must be Sd or None, got {type(value).__name__}"
            )
        self._sd = value
        self._sdf: Optional["Sdf"] = None

    @property
    def sdf(self) -> Optional["Sdf"]:
        """Get sdf (Pythonic accessor)."""
        return self._sdf

    @sdf.setter
    def sdf(self, value: Optional["Sdf"]) -> None:
        """
        Set sdf with validation.
        
        Args:
            value: The sdf to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sdf = None
            return

        if not isinstance(value, Sdf):
            raise TypeError(
                f"sdf must be Sdf or None, got {type(value).__name__}"
            )
        self._sdf = value
        # can be represented in atpVariation.
        self._sdg: Optional["Sdg"] = None

    @property
    def sdg(self) -> Optional["Sdg"]:
        """Get sdg (Pythonic accessor)."""
        return self._sdg

    @sdg.setter
    def sdg(self, value: Optional["Sdg"]) -> None:
        """
        Set sdg with validation.
        
        Args:
            value: The sdg to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sdg = None
            return

        if not isinstance(value, Sdg):
            raise TypeError(
                f"sdg must be Sdg or None, got {type(value).__name__}"
            )
        self._sdg = value
        # This allows to use to establish arbitrary relationships.
        # 535 Document ID 202: AUTOSAR_FO_TPS_GenericStructureTemplate Template R23-11.
        self._sdx: Optional["RefType"] = None

    @property
    def sdx(self) -> Optional["RefType"]:
        """Get sdx (Pythonic accessor)."""
        return self._sdx

    @sdx.setter
    def sdx(self, value: Optional["RefType"]) -> None:
        """
        Set sdx with validation.
        
        Args:
            value: The sdx to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sdx = None
            return

        self._sdx = value
        # atpVariation.
        self._sdxf: Optional["RefType"] = None

    @property
    def sdxf(self) -> Optional["RefType"]:
        """Get sdxf (Pythonic accessor)."""
        return self._sdxf

    @sdxf.setter
    def sdxf(self, value: Optional["RefType"]) -> None:
        """
        Set sdxf with validation.
        
        Args:
            value: The sdxf to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sdxf = None
            return

        self._sdxf = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSd(self) -> "Sd":
        """
        AUTOSAR-compliant getter for sd.
        
        Returns:
            The sd value
        
        Note:
            Delegates to sd property (CODING_RULE_V2_00017)
        """
        return self.sd  # Delegates to property

    def setSd(self, value: "Sd") -> "SdgContents":
        """
        AUTOSAR-compliant setter for sd with method chaining.
        
        Args:
            value: The sd to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to sd property setter (gets validation automatically)
        """
        self.sd = value  # Delegates to property setter
        return self

    def getSdf(self) -> "Sdf":
        """
        AUTOSAR-compliant getter for sdf.
        
        Returns:
            The sdf value
        
        Note:
            Delegates to sdf property (CODING_RULE_V2_00017)
        """
        return self.sdf  # Delegates to property

    def setSdf(self, value: "Sdf") -> "SdgContents":
        """
        AUTOSAR-compliant setter for sdf with method chaining.
        
        Args:
            value: The sdf to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to sdf property setter (gets validation automatically)
        """
        self.sdf = value  # Delegates to property setter
        return self

    def getSdg(self) -> "Sdg":
        """
        AUTOSAR-compliant getter for sdg.
        
        Returns:
            The sdg value
        
        Note:
            Delegates to sdg property (CODING_RULE_V2_00017)
        """
        return self.sdg  # Delegates to property

    def setSdg(self, value: "Sdg") -> "SdgContents":
        """
        AUTOSAR-compliant setter for sdg with method chaining.
        
        Args:
            value: The sdg to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to sdg property setter (gets validation automatically)
        """
        self.sdg = value  # Delegates to property setter
        return self

    def getSdx(self) -> "RefType":
        """
        AUTOSAR-compliant getter for sdx.
        
        Returns:
            The sdx value
        
        Note:
            Delegates to sdx property (CODING_RULE_V2_00017)
        """
        return self.sdx  # Delegates to property

    def setSdx(self, value: "RefType") -> "SdgContents":
        """
        AUTOSAR-compliant setter for sdx with method chaining.
        
        Args:
            value: The sdx to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to sdx property setter (gets validation automatically)
        """
        self.sdx = value  # Delegates to property setter
        return self

    def getSdxf(self) -> "RefType":
        """
        AUTOSAR-compliant getter for sdxf.
        
        Returns:
            The sdxf value
        
        Note:
            Delegates to sdxf property (CODING_RULE_V2_00017)
        """
        return self.sdxf  # Delegates to property

    def setSdxf(self, value: "RefType") -> "SdgContents":
        """
        AUTOSAR-compliant setter for sdxf with method chaining.
        
        Args:
            value: The sdxf to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to sdxf property setter (gets validation automatically)
        """
        self.sdxf = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_sd(self, value: Optional["Sd"]) -> "SdgContents":
        """
        Set sd and return self for chaining.
        
        Args:
            value: The sd to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_sd("value")
        """
        self.sd = value  # Use property setter (gets validation)
        return self

    def with_sdf(self, value: Optional["Sdf"]) -> "SdgContents":
        """
        Set sdf and return self for chaining.
        
        Args:
            value: The sdf to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_sdf("value")
        """
        self.sdf = value  # Use property setter (gets validation)
        return self

    def with_sdg(self, value: Optional["Sdg"]) -> "SdgContents":
        """
        Set sdg and return self for chaining.
        
        Args:
            value: The sdg to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_sdg("value")
        """
        self.sdg = value  # Use property setter (gets validation)
        return self

    def with_sdx(self, value: Optional[RefType]) -> "SdgContents":
        """
        Set sdx and return self for chaining.
        
        Args:
            value: The sdx to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_sdx("value")
        """
        self.sdx = value  # Use property setter (gets validation)
        return self

    def with_sdxf(self, value: Optional[RefType]) -> "SdgContents":
        """
        Set sdxf and return self for chaining.
        
        Args:
            value: The sdxf to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_sdxf("value")
        """
        self.sdxf = value  # Use property setter (gets validation)
        return self



class SdgCaption(MultilanguageReferrable):
    """
    This meta-class represents the caption of a special data group. This allows
    to have some parts of special data as identifiable.
    
    Package: M2::MSR::AsamHdo::SpecialData::SdgCaption
    
    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 91, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents a general but brief (one paragraph) what the special data in
                # question is about.
        # It is paragraph! Desc is intended to be collected into This property helps a
                # human reader to special data in question.
        self._desc: Optional["MultiLanguageOverview"] = None

    @property
    def desc(self) -> Optional["MultiLanguageOverview"]:
        """Get desc (Pythonic accessor)."""
        return self._desc

    @desc.setter
    def desc(self, value: Optional["MultiLanguageOverview"]) -> None:
        """
        Set desc with validation.
        
        Args:
            value: The desc to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._desc = None
            return

        if not isinstance(value, MultiLanguageOverview):
            raise TypeError(
                f"desc must be MultiLanguageOverview or None, got {type(value).__name__}"
            )
        self._desc = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDesc(self) -> "MultiLanguageOverview":
        """
        AUTOSAR-compliant getter for desc.
        
        Returns:
            The desc value
        
        Note:
            Delegates to desc property (CODING_RULE_V2_00017)
        """
        return self.desc  # Delegates to property

    def setDesc(self, value: "MultiLanguageOverview") -> "SdgCaption":
        """
        AUTOSAR-compliant setter for desc with method chaining.
        
        Args:
            value: The desc to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to desc property setter (gets validation automatically)
        """
        self.desc = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_desc(self, value: Optional["MultiLanguageOverview"]) -> "SdgCaption":
        """
        Set desc and return self for chaining.
        
        Args:
            value: The desc to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_desc("value")
        """
        self.desc = value  # Use property setter (gets validation)
        return self



class Sd(ARObject):
    """
    This class represents a primitive element in a special data group.
    
    Package: M2::MSR::AsamHdo::SpecialData::Sd
    
    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 91, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attributes specifies an identifier.
        # Gid comes from the Identifier" which is the in XML.
        # The role of this attribute is the the name of an XML - element.
        self._gid: "NameToken" = None

    @property
    def gid(self) -> "NameToken":
        """Get gid (Pythonic accessor)."""
        return self._gid

    @gid.setter
    def gid(self, value: "NameToken") -> None:
        """
        Set gid with validation.
        
        Args:
            value: The gid to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, (NameToken, str)):
            raise TypeError(
                f"gid must be NameToken or str, got {type(value).__name__}"
            )
        self._gid = value
        self._value: "VerbatimStringPlain" = None

    @property
    def value(self) -> "VerbatimStringPlain":
        """Get value (Pythonic accessor)."""
        return self._value

    @value.setter
    def value(self, value: "VerbatimStringPlain") -> None:
        """
        Set value with validation.
        
        Args:
            value: The value to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, VerbatimStringPlain):
            raise TypeError(
                f"value must be VerbatimStringPlain, got {type(value).__name__}"
            )
        self._value = value
        # preserved by is defined according to xml:space as W3C.
        self._xmlSpace: Optional["XmlSpaceEnum"] = None

    @property
    def xml_space(self) -> Optional["XmlSpaceEnum"]:
        """Get xmlSpace (Pythonic accessor)."""
        return self._xmlSpace

    @xml_space.setter
    def xml_space(self, value: Optional["XmlSpaceEnum"]) -> None:
        """
        Set xmlSpace with validation.
        
        Args:
            value: The xmlSpace to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._xmlSpace = None
            return

        if not isinstance(value, XmlSpaceEnum):
            raise TypeError(
                f"xmlSpace must be XmlSpaceEnum or None, got {type(value).__name__}"
            )
        self._xmlSpace = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getGid(self) -> "NameToken":
        """
        AUTOSAR-compliant getter for gid.
        
        Returns:
            The gid value
        
        Note:
            Delegates to gid property (CODING_RULE_V2_00017)
        """
        return self.gid  # Delegates to property

    def setGid(self, value: "NameToken") -> "Sd":
        """
        AUTOSAR-compliant setter for gid with method chaining.
        
        Args:
            value: The gid to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to gid property setter (gets validation automatically)
        """
        self.gid = value  # Delegates to property setter
        return self

    def getValue(self) -> "VerbatimStringPlain":
        """
        AUTOSAR-compliant getter for value.
        
        Returns:
            The value value
        
        Note:
            Delegates to value property (CODING_RULE_V2_00017)
        """
        return self.value  # Delegates to property

    def setValue(self, value: "VerbatimStringPlain") -> "Sd":
        """
        AUTOSAR-compliant setter for value with method chaining.
        
        Args:
            value: The value to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to value property setter (gets validation automatically)
        """
        self.value = value  # Delegates to property setter
        return self

    def getXmlSpace(self) -> "XmlSpaceEnum":
        """
        AUTOSAR-compliant getter for xmlSpace.
        
        Returns:
            The xmlSpace value
        
        Note:
            Delegates to xml_space property (CODING_RULE_V2_00017)
        """
        return self.xml_space  # Delegates to property

    def setXmlSpace(self, value: "XmlSpaceEnum") -> "Sd":
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

    def with_gid(self, value: "NameToken") -> "Sd":
        """
        Set gid and return self for chaining.
        
        Args:
            value: The gid to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_gid("value")
        """
        self.gid = value  # Use property setter (gets validation)
        return self

    def with_value(self, value: "VerbatimStringPlain") -> "Sd":
        """
        Set value and return self for chaining.
        
        Args:
            value: The value to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_value("value")
        """
        self.value = value  # Use property setter (gets validation)
        return self

    def with_xml_space(self, value: Optional["XmlSpaceEnum"]) -> "Sd":
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



class Sdf(ARObject):
    """
    This class represents a numerical value in a special data group which may be
    subject to variability.
    
    Package: M2::MSR::AsamHdo::SpecialData::Sdf
    
    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 92, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attributes specifies an identifier.
        # Gid comes from the Identifier" which is the in XML.
        # The role of this attribute is the the name of an XML - element.
        self._gid: "NameToken" = None

    @property
    def gid(self) -> "NameToken":
        """Get gid (Pythonic accessor)."""
        return self._gid

    @gid.setter
    def gid(self, value: "NameToken") -> None:
        """
        Set gid with validation.
        
        Args:
            value: The gid to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, (NameToken, str)):
            raise TypeError(
                f"gid must be NameToken or str, got {type(value).__name__}"
            )
        self._gid = value
        self._value: Optional["Numerical"] = None

    @property
    def value(self) -> Optional["Numerical"]:
        """Get value (Pythonic accessor)."""
        return self._value

    @value.setter
    def value(self, value: Optional["Numerical"]) -> None:
        """
        Set value with validation.
        
        Args:
            value: The value to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._value = None
            return

        if not isinstance(value, Numerical):
            raise TypeError(
                f"value must be Numerical or None, got {type(value).__name__}"
            )
        self._value = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getGid(self) -> "NameToken":
        """
        AUTOSAR-compliant getter for gid.
        
        Returns:
            The gid value
        
        Note:
            Delegates to gid property (CODING_RULE_V2_00017)
        """
        return self.gid  # Delegates to property

    def setGid(self, value: "NameToken") -> "Sdf":
        """
        AUTOSAR-compliant setter for gid with method chaining.
        
        Args:
            value: The gid to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to gid property setter (gets validation automatically)
        """
        self.gid = value  # Delegates to property setter
        return self

    def getValue(self) -> "Numerical":
        """
        AUTOSAR-compliant getter for value.
        
        Returns:
            The value value
        
        Note:
            Delegates to value property (CODING_RULE_V2_00017)
        """
        return self.value  # Delegates to property

    def setValue(self, value: "Numerical") -> "Sdf":
        """
        AUTOSAR-compliant setter for value with method chaining.
        
        Args:
            value: The value to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to value property setter (gets validation automatically)
        """
        self.value = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_gid(self, value: "NameToken") -> "Sdf":
        """
        Set gid and return self for chaining.
        
        Args:
            value: The gid to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_gid("value")
        """
        self.gid = value  # Use property setter (gets validation)
        return self

    def with_value(self, value: Optional["Numerical"]) -> "Sdf":
        """
        Set value and return self for chaining.
        
        Args:
            value: The value to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_value("value")
        """
        self.value = value  # Use property setter (gets validation)
        return self

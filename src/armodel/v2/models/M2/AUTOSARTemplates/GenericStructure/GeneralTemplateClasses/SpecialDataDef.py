"""
AUTOSAR Package - SpecialDataDef

Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::SpecialDataDef
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    NameToken,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)




class SdgDef(ARElement):
    """
    A SdgDef groups several SdgClasses which belong to the same extension. The
    concept of an SdgDef is similiar to an UML Profile.
    
    Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::SpecialDataDef::SdgDef
    
    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 99, Foundation R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 207, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The owned sdgClasses which define the structure of the.
        self._sdgClass: List["SdgClass"] = []

    @property
    def sdg_class(self) -> List["SdgClass"]:
        """Get sdgClass (Pythonic accessor)."""
        return self._sdgClass

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSdgClass(self) -> List["SdgClass"]:
        """
        AUTOSAR-compliant getter for sdgClass.
        
        Returns:
            The sdgClass value
        
        Note:
            Delegates to sdg_class property (CODING_RULE_V2_00017)
        """
        return self.sdg_class  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class SdgElementWithGid(ARObject, ABC):
    """
    A special data group element with gid is an abstract element that shall have
    a name (gid, "Generic Identifier").
    
    Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::SpecialDataDef::SdgElementWithGid
    
    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 99, Foundation R23-11)
    """
    def __init__(self):
        if type(self) is SdgElementWithGid:
            raise TypeError("SdgElementWithGid is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specifies the name that identifies the element.
        self._gid: Optional["NameToken"] = None

    @property
    def gid(self) -> Optional["NameToken"]:
        """Get gid (Pythonic accessor)."""
        return self._gid

    @gid.setter
    def gid(self, value: Optional["NameToken"]) -> None:
        """
        Set gid with validation.
        
        Args:
            value: The gid to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._gid = None
            return

        if not isinstance(value, (NameToken, str)):
            raise TypeError(
                f"gid must be NameToken or str or None, got {type(value).__name__}"
            )
        self._gid = value

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

    def setGid(self, value: "NameToken") -> "SdgElementWithGid":
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

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_gid(self, value: Optional["NameToken"]) -> "SdgElementWithGid":
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



class SdgAttribute(Identifiable, ABC):
    """
    Describes the attributes of an Sdg.
    
    Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::SpecialDataDef::SdgAttribute
    
    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 100, Foundation
      R23-11)
    """
    def __init__(self):
        if type(self) is SdgAttribute:
            raise TypeError("SdgAttribute is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class SdgClass(SdgElementWithGid):
    """
    An SdgClass specifies the name and structure of the SDG that may be used to
    store proprietary data in an AUTOSAR model. The SdgClass is similar to an
    UML stereotype.
    
    Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::SpecialDataDef::SdgClass
    
    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 99, Foundation R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 207, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defintion of the structure of the Sdg xml.
        # sequenceOffset=30.
        self._attribute: List["SdgAttribute"] = []

    @property
    def attribute(self) -> List["SdgAttribute"]:
        """Get attribute (Pythonic accessor)."""
        return self._attribute
        # Specifies if a caption is required.
        # Note: only Sdgs that caption can be referenced.
        self._caption: Optional["Boolean"] = None

    @property
    def caption(self) -> Optional["Boolean"]:
        """Get caption (Pythonic accessor)."""
        return self._caption

    @caption.setter
    def caption(self, value: Optional["Boolean"]) -> None:
        """
        Set caption with validation.
        
        Args:
            value: The caption to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._caption = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"caption must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._caption = value
        # The AUTOSAR Meta-Class that may be extended by this.
        self._extendsMeta: Optional["MetaClassName"] = None

    @property
    def extends_meta(self) -> Optional["MetaClassName"]:
        """Get extendsMeta (Pythonic accessor)."""
        return self._extendsMeta

    @extends_meta.setter
    def extends_meta(self, value: Optional["MetaClassName"]) -> None:
        """
        Set extendsMeta with validation.
        
        Args:
            value: The extendsMeta to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._extendsMeta = None
            return

        if not isinstance(value, MetaClassName):
            raise TypeError(
                f"extendsMeta must be MetaClassName or None, got {type(value).__name__}"
            )
        self._extendsMeta = value
        # Semantic constraints that restrict the structure of the group.
        self._sdgConstraint: List["TraceableText"] = []

    @property
    def sdg_constraint(self) -> List["TraceableText"]:
        """Get sdgConstraint (Pythonic accessor)."""
        return self._sdgConstraint

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAttribute(self) -> List["SdgAttribute"]:
        """
        AUTOSAR-compliant getter for attribute.
        
        Returns:
            The attribute value
        
        Note:
            Delegates to attribute property (CODING_RULE_V2_00017)
        """
        return self.attribute  # Delegates to property

    def getCaption(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for caption.
        
        Returns:
            The caption value
        
        Note:
            Delegates to caption property (CODING_RULE_V2_00017)
        """
        return self.caption  # Delegates to property

    def setCaption(self, value: "Boolean") -> "SdgClass":
        """
        AUTOSAR-compliant setter for caption with method chaining.
        
        Args:
            value: The caption to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to caption property setter (gets validation automatically)
        """
        self.caption = value  # Delegates to property setter
        return self

    def getExtendsMeta(self) -> "MetaClassName":
        """
        AUTOSAR-compliant getter for extendsMeta.
        
        Returns:
            The extendsMeta value
        
        Note:
            Delegates to extends_meta property (CODING_RULE_V2_00017)
        """
        return self.extends_meta  # Delegates to property

    def setExtendsMeta(self, value: "MetaClassName") -> "SdgClass":
        """
        AUTOSAR-compliant setter for extendsMeta with method chaining.
        
        Args:
            value: The extendsMeta to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to extends_meta property setter (gets validation automatically)
        """
        self.extends_meta = value  # Delegates to property setter
        return self

    def getSdgConstraint(self) -> List["TraceableText"]:
        """
        AUTOSAR-compliant getter for sdgConstraint.
        
        Returns:
            The sdgConstraint value
        
        Note:
            Delegates to sdg_constraint property (CODING_RULE_V2_00017)
        """
        return self.sdg_constraint  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_caption(self, value: Optional["Boolean"]) -> "SdgClass":
        """
        Set caption and return self for chaining.
        
        Args:
            value: The caption to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_caption("value")
        """
        self.caption = value  # Use property setter (gets validation)
        return self

    def with_extends_meta(self, value: Optional["MetaClassName"]) -> "SdgClass":
        """
        Set extendsMeta and return self for chaining.
        
        Args:
            value: The extendsMeta to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_extends_meta("value")
        """
        self.extends_meta = value  # Use property setter (gets validation)
        return self



class SdgAbstractPrimitiveAttribute(SdgElementWithGid, ABC):
    """
    Describes primitive attributes of a special data group.
    
    Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::SpecialDataDef::SdgAbstractPrimitiveAttribute
    
    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 100, Foundation
      R23-11)
    """
    def __init__(self):
        if type(self) is SdgAbstractPrimitiveAttribute:
            raise TypeError("SdgAbstractPrimitiveAttribute is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class SdgAggregationWithVariation(SdgElementWithGid):
    """
    Describes that the Sdg may contain another Sdg. The gid of the nested Sdg is
    defined by subSdg. Represents ’sdg’.
    
    Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::SpecialDataDef::SdgAggregationWithVariation
    
    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 101, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Supported sub Sdg Class.
        self._subSdg: Optional["SdgClass"] = None

    @property
    def sub_sdg(self) -> Optional["SdgClass"]:
        """Get subSdg (Pythonic accessor)."""
        return self._subSdg

    @sub_sdg.setter
    def sub_sdg(self, value: Optional["SdgClass"]) -> None:
        """
        Set subSdg with validation.
        
        Args:
            value: The subSdg to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._subSdg = None
            return

        if not isinstance(value, SdgClass):
            raise TypeError(
                f"subSdg must be SdgClass or None, got {type(value).__name__}"
            )
        self._subSdg = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSubSdg(self) -> "SdgClass":
        """
        AUTOSAR-compliant getter for subSdg.
        
        Returns:
            The subSdg value
        
        Note:
            Delegates to sub_sdg property (CODING_RULE_V2_00017)
        """
        return self.sub_sdg  # Delegates to property

    def setSubSdg(self, value: "SdgClass") -> "SdgAggregationWithVariation":
        """
        AUTOSAR-compliant setter for subSdg with method chaining.
        
        Args:
            value: The subSdg to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to sub_sdg property setter (gets validation automatically)
        """
        self.sub_sdg = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_sub_sdg(self, value: Optional["SdgClass"]) -> "SdgAggregationWithVariation":
        """
        Set subSdg and return self for chaining.
        
        Args:
            value: The subSdg to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_sub_sdg("value")
        """
        self.sub_sdg = value  # Use property setter (gets validation)
        return self



class SdgAbstractForeignReference(SdgElementWithGid, ABC):
    """
    An abstract reference that can point to any referrable object in an AUTOSAR
    Model.
    
    Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::SpecialDataDef::SdgAbstractForeignReference
    
    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 102, Foundation
      R23-11)
    """
    def __init__(self):
        if type(self) is SdgAbstractForeignReference:
            raise TypeError("SdgAbstractForeignReference is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # specifies the destination meta-class of the reference.
        self._destMetaClass: Optional["MetaClassName"] = None

    @property
    def dest_meta_class(self) -> Optional["MetaClassName"]:
        """Get destMetaClass (Pythonic accessor)."""
        return self._destMetaClass

    @dest_meta_class.setter
    def dest_meta_class(self, value: Optional["MetaClassName"]) -> None:
        """
        Set destMetaClass with validation.
        
        Args:
            value: The destMetaClass to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._destMetaClass = None
            return

        if not isinstance(value, MetaClassName):
            raise TypeError(
                f"destMetaClass must be MetaClassName or None, got {type(value).__name__}"
            )
        self._destMetaClass = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDestMetaClass(self) -> "MetaClassName":
        """
        AUTOSAR-compliant getter for destMetaClass.
        
        Returns:
            The destMetaClass value
        
        Note:
            Delegates to dest_meta_class property (CODING_RULE_V2_00017)
        """
        return self.dest_meta_class  # Delegates to property

    def setDestMetaClass(self, value: "MetaClassName") -> "SdgAbstractForeignReference":
        """
        AUTOSAR-compliant setter for destMetaClass with method chaining.
        
        Args:
            value: The destMetaClass to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to dest_meta_class property setter (gets validation automatically)
        """
        self.dest_meta_class = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_dest_meta_class(self, value: Optional["MetaClassName"]) -> "SdgAbstractForeignReference":
        """
        Set destMetaClass and return self for chaining.
        
        Args:
            value: The destMetaClass to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_dest_meta_class("value")
        """
        self.dest_meta_class = value  # Use property setter (gets validation)
        return self



class SdgReference(SdgAttribute):
    """
    Describes an attribute of a SdgClass which is used on the definition side to
    model a reference from one Sdg to another Sdg on the value side.
    
    Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::SpecialDataDef::SdgReference
    
    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 101, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Refers to a SdgClass which is used on the definition side the destination
                # type of the referenced Sdg.
        # On side the reference is realized by means of the defining an sdgx attribute
                # which refers to of the referenced Sdg.
        self._destSdg: Optional["SdgClass"] = None

    @property
    def dest_sdg(self) -> Optional["SdgClass"]:
        """Get destSdg (Pythonic accessor)."""
        return self._destSdg

    @dest_sdg.setter
    def dest_sdg(self, value: Optional["SdgClass"]) -> None:
        """
        Set destSdg with validation.
        
        Args:
            value: The destSdg to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._destSdg = None
            return

        if not isinstance(value, SdgClass):
            raise TypeError(
                f"destSdg must be SdgClass or None, got {type(value).__name__}"
            )
        self._destSdg = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDestSdg(self) -> "SdgClass":
        """
        AUTOSAR-compliant getter for destSdg.
        
        Returns:
            The destSdg value
        
        Note:
            Delegates to dest_sdg property (CODING_RULE_V2_00017)
        """
        return self.dest_sdg  # Delegates to property

    def setDestSdg(self, value: "SdgClass") -> "SdgReference":
        """
        AUTOSAR-compliant setter for destSdg with method chaining.
        
        Args:
            value: The destSdg to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to dest_sdg property setter (gets validation automatically)
        """
        self.dest_sdg = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_dest_sdg(self, value: Optional["SdgClass"]) -> "SdgReference":
        """
        Set destSdg and return self for chaining.
        
        Args:
            value: The destSdg to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_dest_sdg("value")
        """
        self.dest_sdg = value  # Use property setter (gets validation)
        return self



class SdgPrimitiveAttribute(SdgAbstractPrimitiveAttribute):
    """
    Describes primitive special data attributes without variation. This class
    accepts a special data "sd" attribute.
    
    Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::SpecialDataDef::SdgPrimitiveAttribute
    
    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 100, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class SdgPrimitiveAttributeWithVariation(SdgAbstractPrimitiveAttribute):
    """
    Describes a primitive numerical special data attribute with variation. This
    class accepts a special data "sdf" element.
    
    Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::SpecialDataDef::SdgPrimitiveAttributeWithVariation
    
    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 101, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class SdgForeignReference(SdgAbstractForeignReference):
    """
    A reference without variation support that can point to any referrable
    object in an AUTOSAR Model. This class accepts the special data "Sdx"
    reference.
    
    Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::SpecialDataDef::SdgForeignReference
    
    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 102, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class SdgForeignReferenceWithVariation(SdgAbstractForeignReference):
    """
    A reference with variation support that can point to any referrable object
    in an AUTOSAR Model. This class accepts the special data "Sdxf" reference.
    
    Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::SpecialDataDef::SdgForeignReferenceWithVariation
    
    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 102, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
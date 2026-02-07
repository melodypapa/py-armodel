from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

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

        if not isinstance(value, Boolean):
            raise TypeError(
                f"caption must be Boolean or None, got {type(value).__name__}"
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
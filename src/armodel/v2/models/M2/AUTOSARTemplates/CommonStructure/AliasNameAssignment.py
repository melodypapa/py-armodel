from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class AliasNameAssignment(ARObject):
    """
    that flatInstance and identifiable are mutually exclusive.
    
    Package: M2::AUTOSARTemplates::CommonStructure::FlatMap::AliasNameAssignment
    
    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 175, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 968, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Assignment of a unique name to a flat representation.
        self._flatInstance: Optional["FlatInstanceDescriptor"] = None

    @property
    def flat_instance(self) -> Optional["FlatInstanceDescriptor"]:
        """Get flatInstance (Pythonic accessor)."""
        return self._flatInstance

    @flat_instance.setter
    def flat_instance(self, value: Optional["FlatInstanceDescriptor"]) -> None:
        """
        Set flatInstance with validation.
        
        Args:
            value: The flatInstance to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._flatInstance = None
            return

        if not isinstance(value, FlatInstanceDescriptor):
            raise TypeError(
                f"flatInstance must be FlatInstanceDescriptor or None, got {type(value).__name__}"
            )
        self._flatInstance = value
        # Assignment of a unique name to an Identifiable.
        self._identifiable: Optional["Identifiable"] = None

    @property
    def identifiable(self) -> Optional["Identifiable"]:
        """Get identifiable (Pythonic accessor)."""
        return self._identifiable

    @identifiable.setter
    def identifiable(self, value: Optional["Identifiable"]) -> None:
        """
        Set identifiable with validation.
        
        Args:
            value: The identifiable to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._identifiable = None
            return

        if not isinstance(value, Identifiable):
            raise TypeError(
                f"identifiable must be Identifiable or None, got {type(value).__name__}"
            )
        self._identifiable = value
        # This represents an "Alias LongName".
        # xml.
        # sequenceOffset=20.
        self._label: Optional["MultilanguageLong"] = None

    @property
    def label(self) -> Optional["MultilanguageLong"]:
        """Get label (Pythonic accessor)."""
        return self._label

    @label.setter
    def label(self, value: Optional["MultilanguageLong"]) -> None:
        """
        Set label with validation.
        
        Args:
            value: The label to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._label = None
            return

        if not isinstance(value, MultilanguageLong):
            raise TypeError(
                f"label must be MultilanguageLong or None, got {type(value).__name__}"
            )
        self._label = value
        # This attribute represents the alias name.
        # It is modeled as the alias name is used outside of therefore no naming
                # conventions can be AUTOSAR.
        self._shortLabel: Optional["String"] = None

    @property
    def short_label(self) -> Optional["String"]:
        """Get shortLabel (Pythonic accessor)."""
        return self._shortLabel

    @short_label.setter
    def short_label(self, value: Optional["String"]) -> None:
        """
        Set shortLabel with validation.
        
        Args:
            value: The shortLabel to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._shortLabel = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"shortLabel must be String or None, got {type(value).__name__}"
            )
        self._shortLabel = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getFlatInstance(self) -> "FlatInstanceDescriptor":
        """
        AUTOSAR-compliant getter for flatInstance.
        
        Returns:
            The flatInstance value
        
        Note:
            Delegates to flat_instance property (CODING_RULE_V2_00017)
        """
        return self.flat_instance  # Delegates to property

    def setFlatInstance(self, value: "FlatInstanceDescriptor") -> "AliasNameAssignment":
        """
        AUTOSAR-compliant setter for flatInstance with method chaining.
        
        Args:
            value: The flatInstance to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to flat_instance property setter (gets validation automatically)
        """
        self.flat_instance = value  # Delegates to property setter
        return self

    def getIdentifiable(self) -> "Identifiable":
        """
        AUTOSAR-compliant getter for identifiable.
        
        Returns:
            The identifiable value
        
        Note:
            Delegates to identifiable property (CODING_RULE_V2_00017)
        """
        return self.identifiable  # Delegates to property

    def setIdentifiable(self, value: "Identifiable") -> "AliasNameAssignment":
        """
        AUTOSAR-compliant setter for identifiable with method chaining.
        
        Args:
            value: The identifiable to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to identifiable property setter (gets validation automatically)
        """
        self.identifiable = value  # Delegates to property setter
        return self

    def getLabel(self) -> "MultilanguageLong":
        """
        AUTOSAR-compliant getter for label.
        
        Returns:
            The label value
        
        Note:
            Delegates to label property (CODING_RULE_V2_00017)
        """
        return self.label  # Delegates to property

    def setLabel(self, value: "MultilanguageLong") -> "AliasNameAssignment":
        """
        AUTOSAR-compliant setter for label with method chaining.
        
        Args:
            value: The label to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to label property setter (gets validation automatically)
        """
        self.label = value  # Delegates to property setter
        return self

    def getShortLabel(self) -> "String":
        """
        AUTOSAR-compliant getter for shortLabel.
        
        Returns:
            The shortLabel value
        
        Note:
            Delegates to short_label property (CODING_RULE_V2_00017)
        """
        return self.short_label  # Delegates to property

    def setShortLabel(self, value: "String") -> "AliasNameAssignment":
        """
        AUTOSAR-compliant setter for shortLabel with method chaining.
        
        Args:
            value: The shortLabel to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to short_label property setter (gets validation automatically)
        """
        self.short_label = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_flat_instance(self, value: Optional["FlatInstanceDescriptor"]) -> "AliasNameAssignment":
        """
        Set flatInstance and return self for chaining.
        
        Args:
            value: The flatInstance to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_flat_instance("value")
        """
        self.flat_instance = value  # Use property setter (gets validation)
        return self

    def with_identifiable(self, value: Optional["Identifiable"]) -> "AliasNameAssignment":
        """
        Set identifiable and return self for chaining.
        
        Args:
            value: The identifiable to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_identifiable("value")
        """
        self.identifiable = value  # Use property setter (gets validation)
        return self

    def with_label(self, value: Optional["MultilanguageLong"]) -> "AliasNameAssignment":
        """
        Set label and return self for chaining.
        
        Args:
            value: The label to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_label("value")
        """
        self.label = value  # Use property setter (gets validation)
        return self

    def with_short_label(self, value: Optional["String"]) -> "AliasNameAssignment":
        """
        Set shortLabel and return self for chaining.
        
        Args:
            value: The shortLabel to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_short_label("value")
        """
        self.short_label = value  # Use property setter (gets validation)
        return self
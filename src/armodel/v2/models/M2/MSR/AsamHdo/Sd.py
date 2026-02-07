from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

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
        if not isinstance(value, NameToken):
            raise TypeError(
                f"gid must be NameToken, got {type(value).__name__}"
            )
        self._gid = value
        # This is the value of the special data.
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
        # This attribute is used to signal an intention that in that space should be
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
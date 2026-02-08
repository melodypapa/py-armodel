from abc import ABC

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class WhitespaceControlled(ARObject, ABC):
    """
    This meta-class represents the ability to control the white-space handling
    e.g. in xml serialization. This is implemented by adding the attribute
    "space".

    Package: M2::MSR::Documentation::TextModel::LanguageDataModel

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

    def setXmlSpace(self, value: "XmlSpaceEnum") -> "WhitespaceControlled":
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

    def with_xml_space(self, value: "XmlSpaceEnum") -> "WhitespaceControlled":
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

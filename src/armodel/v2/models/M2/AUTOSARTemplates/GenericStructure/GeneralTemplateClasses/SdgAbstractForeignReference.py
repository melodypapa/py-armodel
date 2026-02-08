from abc import ABC
from typing import Optional


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

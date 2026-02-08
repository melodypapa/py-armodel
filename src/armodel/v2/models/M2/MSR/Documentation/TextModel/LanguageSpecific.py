from abc import ABC

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class LanguageSpecific(ARObject, ABC):
    """
    This meta-class represents the ability to denote a particular language for
    which an object is applicable.

    Package: M2::MSR::Documentation::TextModel::LanguageDataModel

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
        self._l: "LEnum" = None

    @property
    def l(self) -> "LEnum":
        """Get l (Pythonic accessor)."""
        return self._l

    @l.setter
    def l(self, value: "LEnum") -> None:
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

    def getL(self) -> "LEnum":
        """
        AUTOSAR-compliant getter for l.

        Returns:
            The l value

        Note:
            Delegates to l property (CODING_RULE_V2_00017)
        """
        return self.l  # Delegates to property

    def setL(self, value: "LEnum") -> "LanguageSpecific":
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

    def with_l(self, value: "LEnum") -> "LanguageSpecific":
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

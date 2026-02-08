from abc import ABC
from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import SingleLanguageLong
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Referrable import (
    Referrable,
)


class SingleLanguageReferrable(Referrable, ABC):
    """
    Instances of this class can be referred to by their identifier (while
    adhering to namespace borders). They also may have a longName but in one
    language only. Specializations of this class only occur as inline elements
    in one particular language. Therefore they aggregate But they are not
    considered to contribute substantially to the overall structure of an
    AUTOSAR description. In particular it does not contain other Referrables.

    Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::Identifiable::SingleLanguageReferrable

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 64, Foundation R23-11)
    """
    def __init__(self):
        if type(self) is SingleLanguageReferrable:
            raise TypeError("SingleLanguageReferrable is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This specifies the long name of the object.
        # The role is for compatibiilty to ASAM FSX.
        self._longName1: Optional["SingleLanguageLong"] = None

    @property
    def long_name1(self) -> Optional["SingleLanguageLong"]:
        """Get longName1 (Pythonic accessor)."""
        return self._longName1

    @long_name1.setter
    def long_name1(self, value: Optional["SingleLanguageLong"]) -> None:
        """
        Set longName1 with validation.

        Args:
            value: The longName1 to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._longName1 = None
            return

        if not isinstance(value, SingleLanguageLong):
            raise TypeError(
                f"longName1 must be SingleLanguageLong or None, got {type(value).__name__}"
            )
        self._longName1 = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getLongName1(self) -> "SingleLanguageLong":
        """
        AUTOSAR-compliant getter for longName1.

        Returns:
            The longName1 value

        Note:
            Delegates to long_name1 property (CODING_RULE_V2_00017)
        """
        return self.long_name1  # Delegates to property

    def setLongName1(self, value: "SingleLanguageLong") -> "SingleLanguageReferrable":
        """
        AUTOSAR-compliant setter for longName1 with method chaining.

        Args:
            value: The longName1 to set

        Returns:
            self for method chaining

        Note:
            Delegates to long_name1 property setter (gets validation automatically)
        """
        self.long_name1 = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_long_name1(self, value: Optional["SingleLanguageLong"]) -> "SingleLanguageReferrable":
        """
        Set longName1 and return self for chaining.

        Args:
            value: The longName1 to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_long_name1("value")
        """
        self.long_name1 = value  # Use property setter (gets validation)
        return self

from abc import ABC
from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import MultilanguageLong
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Referrable import (
    Referrable,
)


class MultilanguageReferrable(Referrable, ABC):
    """
    Instances of this class can be referred to by their identifier (while
    adhering to namespace borders). They also may have a longName. But they are
    not considered to contribute substantially to the overall structure of an
    AUTOSAR description. In particular it does not contain other Referrables.

    Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::Identifiable::MultilanguageReferrable

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 179, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 301, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 1000, Classic
      Platform R23-11)
      - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (Page 48, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (Page 75, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 63, Foundation R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 197, Foundation R23-11)
    """
    def __init__(self):
        if type(self) is MultilanguageReferrable:
            raise TypeError("MultilanguageReferrable is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This specifies the long name of the object.
        # Long name is to human readers and acts like a headline.
        self._longName: Optional["MultilanguageLong"] = None

    @property
    def long_name(self) -> Optional["MultilanguageLong"]:
        """Get longName (Pythonic accessor)."""
        return self._longName

    @long_name.setter
    def long_name(self, value: Optional["MultilanguageLong"]) -> None:
        """
        Set longName with validation.

        Args:
            value: The longName to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._longName = None
            return

        if not isinstance(value, MultilanguageLong):
            raise TypeError(
                f"longName must be MultilanguageLong or None, got {type(value).__name__}"
            )
        self._longName = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getLongName(self) -> "MultilanguageLong":
        """
        AUTOSAR-compliant getter for longName.

        Returns:
            The longName value

        Note:
            Delegates to long_name property (CODING_RULE_V2_00017)
        """
        return self.long_name  # Delegates to property

    def setLongName(self, value: "MultilanguageLong") -> "MultilanguageReferrable":
        """
        AUTOSAR-compliant setter for longName with method chaining.

        Args:
            value: The longName to set

        Returns:
            self for method chaining

        Note:
            Delegates to long_name property setter (gets validation automatically)
        """
        self.long_name = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_long_name(self, value: Optional["MultilanguageLong"]) -> "MultilanguageReferrable":
        """
        Set longName and return self for chaining.

        Args:
            value: The longName to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_long_name("value")
        """
        self.long_name = value  # Use property setter (gets validation)
        return self

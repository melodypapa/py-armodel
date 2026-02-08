from abc import ABC
from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import SwSystemconst
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class SwSystemconstDependentFormula(ARObject, ABC):
    """
    This class represents an expression depending on system constants.

    Package: M2::AUTOSARTemplates::GenericStructure::VariantHandling::SwSystemconstDependentFormula

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 1006, Classic
      Platform R23-11)
      - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (Page 79, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 240, Foundation
      R23-11)
    """
    def __init__(self):
        if type(self) is SwSystemconstDependentFormula:
            raise TypeError("SwSystemconstDependentFormula is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This refers to a system constant.
        # The internal (coded) the system constant shall be used.
        self._sysc: Optional["SwSystemconst"] = None

    @property
    def sysc(self) -> Optional["SwSystemconst"]:
        """Get sysc (Pythonic accessor)."""
        return self._sysc

    @sysc.setter
    def sysc(self, value: Optional["SwSystemconst"]) -> None:
        """
        Set sysc with validation.

        Args:
            value: The sysc to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sysc = None
            return

        if not isinstance(value, SwSystemconst):
            raise TypeError(
                f"sysc must be SwSystemconst or None, got {type(value).__name__}"
            )
        self._sysc = value
        # syscString indicates that the referenced system constant evaluated as a
        # string according to.
        self._syscString: Optional["SwSystemconst"] = None

    @property
    def sysc_string(self) -> Optional["SwSystemconst"]:
        """Get syscString (Pythonic accessor)."""
        return self._syscString

    @sysc_string.setter
    def sysc_string(self, value: Optional["SwSystemconst"]) -> None:
        """
        Set syscString with validation.

        Args:
            value: The syscString to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._syscString = None
            return

        if not isinstance(value, SwSystemconst):
            raise TypeError(
                f"syscString must be SwSystemconst or None, got {type(value).__name__}"
            )
        self._syscString = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSysc(self) -> "SwSystemconst":
        """
        AUTOSAR-compliant getter for sysc.

        Returns:
            The sysc value

        Note:
            Delegates to sysc property (CODING_RULE_V2_00017)
        """
        return self.sysc  # Delegates to property

    def setSysc(self, value: "SwSystemconst") -> "SwSystemconstDependentFormula":
        """
        AUTOSAR-compliant setter for sysc with method chaining.

        Args:
            value: The sysc to set

        Returns:
            self for method chaining

        Note:
            Delegates to sysc property setter (gets validation automatically)
        """
        self.sysc = value  # Delegates to property setter
        return self

    def getSyscString(self) -> "SwSystemconst":
        """
        AUTOSAR-compliant getter for syscString.

        Returns:
            The syscString value

        Note:
            Delegates to sysc_string property (CODING_RULE_V2_00017)
        """
        return self.sysc_string  # Delegates to property

    def setSyscString(self, value: "SwSystemconst") -> "SwSystemconstDependentFormula":
        """
        AUTOSAR-compliant setter for syscString with method chaining.

        Args:
            value: The syscString to set

        Returns:
            self for method chaining

        Note:
            Delegates to sysc_string property setter (gets validation automatically)
        """
        self.sysc_string = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_sysc(self, value: Optional["SwSystemconst"]) -> "SwSystemconstDependentFormula":
        """
        Set sysc and return self for chaining.

        Args:
            value: The sysc to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sysc("value")
        """
        self.sysc = value  # Use property setter (gets validation)
        return self

    def with_sysc_string(self, value: Optional["SwSystemconst"]) -> "SwSystemconstDependentFormula":
        """
        Set syscString and return self for chaining.

        Args:
            value: The syscString to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sysc_string("value")
        """
        self.sysc_string = value  # Use property setter (gets validation)
        return self

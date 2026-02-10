"""
AUTOSAR Package - Common

Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::DataExchangePoint::Common
"""

from abc import ABC
from typing import Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    String,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class SpecElementReference(Identifiable, ABC):
    """
    This is a reference to a specification element in the Autosar standard.

    Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::DataExchangePoint::Common::SpecElementReference

    Sources:
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 82, Foundation R23-11)
    """
    def __init__(self):
        if type(self) is SpecElementReference:
            raise TypeError("SpecElementReference is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Alternative name of a specification element if its name fit into the
                # shortName.
        # E.
        # g.
        # because the name.
        self._alternative: Optional["String"] = None

    @property
    def alternative(self) -> Optional["String"]:
        """Get alternative (Pythonic accessor)."""
        return self._alternative

    @alternative.setter
    def alternative(self, value: Optional["String"]) -> None:
        """
        Set alternative with validation.

        Args:
            value: The alternative to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._alternative = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"alternative must be String or str or None, got {type(value).__name__}"
            )
        self._alternative = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAlternative(self) -> "String":
        """
        AUTOSAR-compliant getter for alternative.

        Returns:
            The alternative value

        Note:
            Delegates to alternative property (CODING_RULE_V2_00017)
        """
        return self.alternative  # Delegates to property

    def setAlternative(self, value: "String") -> "SpecElementReference":
        """
        AUTOSAR-compliant setter for alternative with method chaining.

        Args:
            value: The alternative to set

        Returns:
            self for method chaining

        Note:
            Delegates to alternative property setter (gets validation automatically)
        """
        self.alternative = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_alternative(self, value: Optional["String"]) -> "SpecElementReference":
        """
        Set alternative and return self for chaining.

        Args:
            value: The alternative to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_alternative("value")
        """
        self.alternative = value  # Use property setter (gets validation)
        return self



class RestrictionWithSeverity(ARObject, ABC):
    """
    A restriction that has a severity. The severity describes the severity level
    that is reported in case the restriction is violated.

    Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::DataExchangePoint::Common::RestrictionWithSeverity

    Sources:
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 86, Foundation R23-11)
    """
    def __init__(self):
        if type(self) is RestrictionWithSeverity:
            raise TypeError("RestrictionWithSeverity is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Severity level that is reported in case the restriction is.
        self._severity: "SeverityEnum" = None

    @property
    def severity(self) -> "SeverityEnum":
        """Get severity (Pythonic accessor)."""
        return self._severity

    @severity.setter
    def severity(self, value: "SeverityEnum") -> None:
        """
        Set severity with validation.

        Args:
            value: The severity to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, SeverityEnum):
            raise TypeError(
                f"severity must be SeverityEnum, got {type(value).__name__}"
            )
        self._severity = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSeverity(self) -> "SeverityEnum":
        """
        AUTOSAR-compliant getter for severity.

        Returns:
            The severity value

        Note:
            Delegates to severity property (CODING_RULE_V2_00017)
        """
        return self.severity  # Delegates to property

    def setSeverity(self, value: "SeverityEnum") -> "RestrictionWithSeverity":
        """
        AUTOSAR-compliant setter for severity with method chaining.

        Args:
            value: The severity to set

        Returns:
            self for method chaining

        Note:
            Delegates to severity property setter (gets validation automatically)
        """
        self.severity = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_severity(self, value: "SeverityEnum") -> "RestrictionWithSeverity":
        """
        Set severity and return self for chaining.

        Args:
            value: The severity to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_severity("value")
        """
        self.severity = value  # Use property setter (gets validation)
        return self



class SpecElementScope(SpecElementReference, ABC):
    """
    This class defines if a specification element is relevant within the context
    of this data exchange point.

    Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::DataExchangePoint::Common::SpecElementScope

    Sources:
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 84, Foundation R23-11)
    """
    def __init__(self):
        if type(self) is SpecElementScope:
            raise TypeError("SpecElementScope is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # indicates, if a specification element is relevant for this point.
        # It is relevant if inScope==true.
        # It is or don’t care if inScope=false.
        self._inScope: Optional["Boolean"] = None

    @property
    def in_scope(self) -> Optional["Boolean"]:
        """Get inScope (Pythonic accessor)."""
        return self._inScope

    @in_scope.setter
    def in_scope(self, value: Optional["Boolean"]) -> None:
        """
        Set inScope with validation.

        Args:
            value: The inScope to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._inScope = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"inScope must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._inScope = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getInScope(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for inScope.

        Returns:
            The inScope value

        Note:
            Delegates to in_scope property (CODING_RULE_V2_00017)
        """
        return self.in_scope  # Delegates to property

    def setInScope(self, value: "Boolean") -> "SpecElementScope":
        """
        AUTOSAR-compliant setter for inScope with method chaining.

        Args:
            value: The inScope to set

        Returns:
            self for method chaining

        Note:
            Delegates to in_scope property setter (gets validation automatically)
        """
        self.in_scope = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_in_scope(self, value: Optional["Boolean"]) -> "SpecElementScope":
        """
        Set inScope and return self for chaining.

        Args:
            value: The inScope to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_in_scope("value")
        """
        self.in_scope = value  # Use property setter (gets validation)
        return self



class DataFormatElementReference(SpecElementReference, ABC):
    """
    Superclass of all references to specification elements that have direct
    impact on the data exchange format (Meta-Classes, Meta-Attributes,
    constraints, SdgDefs)

    Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::DataExchangePoint::Common::DataFormatElementReference

    Sources:
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 91, Foundation R23-11)
    """
    def __init__(self):
        if type(self) is DataFormatElementReference:
            raise TypeError("DataFormatElementReference is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARElement,
)


class CryptoEllipticCurveProps(ARElement):
    """
    This meta-class provides attributes to specify the properties of elliptic
    curves.

    Package: M2::AUTOSARTemplates::SystemTemplate::SecureCommunication

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 564, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines the value of one specific NamedCurve Id.
        self._namedCurveId: Optional["PositiveInteger"] = None

    @property
    def named_curve_id(self) -> Optional["PositiveInteger"]:
        """Get namedCurveId (Pythonic accessor)."""
        return self._namedCurveId

    @named_curve_id.setter
    def named_curve_id(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set namedCurveId with validation.

        Args:
            value: The namedCurveId to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._namedCurveId = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"namedCurveId must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._namedCurveId = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getNamedCurveId(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for namedCurveId.

        Returns:
            The namedCurveId value

        Note:
            Delegates to named_curve_id property (CODING_RULE_V2_00017)
        """
        return self.named_curve_id  # Delegates to property

    def setNamedCurveId(self, value: "PositiveInteger") -> "CryptoEllipticCurveProps":
        """
        AUTOSAR-compliant setter for namedCurveId with method chaining.

        Args:
            value: The namedCurveId to set

        Returns:
            self for method chaining

        Note:
            Delegates to named_curve_id property setter (gets validation automatically)
        """
        self.named_curve_id = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_named_curve_id(self, value: Optional["PositiveInteger"]) -> "CryptoEllipticCurveProps":
        """
        Set namedCurveId and return self for chaining.

        Args:
            value: The namedCurveId to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_named_curve_id("value")
        """
        self.named_curve_id = value  # Use property setter (gets validation)
        return self

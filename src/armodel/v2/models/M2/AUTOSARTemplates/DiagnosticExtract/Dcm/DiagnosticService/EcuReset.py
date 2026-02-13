"""
AUTOSAR Package - EcuReset

Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::EcuReset
"""


from __future__ import annotations
from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.DiagnosticService.CommonService import (
    DiagnosticServiceClass,
    DiagnosticServiceInstance,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
)


class DiagnosticEcuReset(DiagnosticServiceInstance):
    """
    This represents an instance of the "ECU Reset" diagnostic service.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::EcuReset::DiagnosticEcuReset

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 102, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute shall be used to define a custom number if none of the
        # standardized values of shall be used.
        self._customSub: Optional[PositiveInteger] = None

    @property
    def custom_sub(self) -> Optional[PositiveInteger]:
        """Get customSub (Pythonic accessor)."""
        return self._customSub

    @custom_sub.setter
    def custom_sub(self, value: Optional[PositiveInteger]) -> None:
        """
        Set customSub with validation.

        Args:
            value: The customSub to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._customSub = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"customSub must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._customSub = value
        # represents the ability to access among all DiagnosticEcuReset in the.
        self._ecuResetClass: Optional[DiagnosticEcuReset] = None

    @property
    def ecu_reset_class(self) -> Optional[DiagnosticEcuReset]:
        """Get ecuResetClass (Pythonic accessor)."""
        return self._ecuResetClass

    @ecu_reset_class.setter
    def ecu_reset_class(self, value: Optional[DiagnosticEcuReset]) -> None:
        """
        Set ecuResetClass with validation.

        Args:
            value: The ecuResetClass to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ecuResetClass = None
            return

        if not isinstance(value, DiagnosticEcuReset):
            raise TypeError(
                f"ecuResetClass must be DiagnosticEcuReset or None, got {type(value).__name__}"
            )
        self._ecuResetClass = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCustomSub(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for customSub.

        Returns:
            The customSub value

        Note:
            Delegates to custom_sub property (CODING_RULE_V2_00017)
        """
        return self.custom_sub  # Delegates to property

    def setCustomSub(self, value: PositiveInteger) -> DiagnosticEcuReset:
        """
        AUTOSAR-compliant setter for customSub with method chaining.

        Args:
            value: The customSub to set

        Returns:
            self for method chaining

        Note:
            Delegates to custom_sub property setter (gets validation automatically)
        """
        self.custom_sub = value  # Delegates to property setter
        return self

    def getEcuResetClass(self) -> DiagnosticEcuReset:
        """
        AUTOSAR-compliant getter for ecuResetClass.

        Returns:
            The ecuResetClass value

        Note:
            Delegates to ecu_reset_class property (CODING_RULE_V2_00017)
        """
        return self.ecu_reset_class  # Delegates to property

    def setEcuResetClass(self, value: DiagnosticEcuReset) -> DiagnosticEcuReset:
        """
        AUTOSAR-compliant setter for ecuResetClass with method chaining.

        Args:
            value: The ecuResetClass to set

        Returns:
            self for method chaining

        Note:
            Delegates to ecu_reset_class property setter (gets validation automatically)
        """
        self.ecu_reset_class = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_custom_sub(self, value: Optional[PositiveInteger]) -> DiagnosticEcuReset:
        """
        Set customSub and return self for chaining.

        Args:
            value: The customSub to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_custom_sub("value")
        """
        self.custom_sub = value  # Use property setter (gets validation)
        return self

    def with_ecu_reset_class(self, value: Optional[DiagnosticEcuReset]) -> DiagnosticEcuReset:
        """
        Set ecuResetClass and return self for chaining.

        Args:
            value: The ecuResetClass to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ecu_reset_class("value")
        """
        self.ecu_reset_class = value  # Use property setter (gets validation)
        return self



class DiagnosticEcuResetClass(DiagnosticServiceClass):
    """
    This meta-class contains attributes shared by all instances of the "Ecu
    Reset" diagnostic service.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::EcuReset::DiagnosticEcuResetClass

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 102, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute defines whether the response to the Ecu Reset service shall be
        # transmitted before or after the.
        self._respondTo: Optional["DiagnosticResponseTo"] = None

    @property
    def respond_to(self) -> Optional["DiagnosticResponseTo"]:
        """Get respondTo (Pythonic accessor)."""
        return self._respondTo

    @respond_to.setter
    def respond_to(self, value: Optional["DiagnosticResponseTo"]) -> None:
        """
        Set respondTo with validation.

        Args:
            value: The respondTo to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._respondTo = None
            return

        if not isinstance(value, DiagnosticResponseTo):
            raise TypeError(
                f"respondTo must be DiagnosticResponseTo or None, got {type(value).__name__}"
            )
        self._respondTo = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getRespondTo(self) -> "DiagnosticResponseTo":
        """
        AUTOSAR-compliant getter for respondTo.

        Returns:
            The respondTo value

        Note:
            Delegates to respond_to property (CODING_RULE_V2_00017)
        """
        return self.respond_to  # Delegates to property

    def setRespondTo(self, value: "DiagnosticResponseTo") -> DiagnosticEcuResetClass:
        """
        AUTOSAR-compliant setter for respondTo with method chaining.

        Args:
            value: The respondTo to set

        Returns:
            self for method chaining

        Note:
            Delegates to respond_to property setter (gets validation automatically)
        """
        self.respond_to = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_respond_to(self, value: Optional["DiagnosticResponseTo"]) -> DiagnosticEcuResetClass:
        """
        Set respondTo and return self for chaining.

        Args:
            value: The respondTo to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_respond_to("value")
        """
        self.respond_to = value  # Use property setter (gets validation)
        return self


class DiagnosticResponseToEcuResetEnum(AREnum):
    """
    DiagnosticResponseToEcuResetEnum enumeration

This enumeration controls the point in time in which a response to the reception of an EcuReset service shall be generated. Aggregated by DiagnosticEcuResetClass.respondToReset

Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::EcuReset
    """
    # Answer to EcuReset service should come after the reset.
    respondAfterReset = "0"

    # Answer to EcuReset service should come before the reset.
    respondBeforeReset = "1"

from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class DiagnosticAuthTransmitCertificateEvaluation(Identifiable):
    """
    This meta-class represents the ability to configure a certificate evaluation
    in the context of a diagnostic authentication.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticService::Authentication::DiagnosticAuthTransmitCertificateEvaluation

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 101, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attributes represents the ID of the certificate.
        self._evaluationId: Optional["PositiveInteger"] = None

    @property
    def evaluation_id(self) -> Optional["PositiveInteger"]:
        """Get evaluationId (Pythonic accessor)."""
        return self._evaluationId

    @evaluation_id.setter
    def evaluation_id(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set evaluationId with validation.

        Args:
            value: The evaluationId to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._evaluationId = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"evaluationId must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._evaluationId = value
        # This attribute represents the description of the actual the corresponding
        # evaluation ID.
        self._function: Optional["String"] = None

    @property
    def function(self) -> Optional["String"]:
        """Get function (Pythonic accessor)."""
        return self._function

    @function.setter
    def function(self, value: Optional["String"]) -> None:
        """
        Set function with validation.

        Args:
            value: The function to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._function = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"function must be String or None, got {type(value).__name__}"
            )
        self._function = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEvaluationId(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for evaluationId.

        Returns:
            The evaluationId value

        Note:
            Delegates to evaluation_id property (CODING_RULE_V2_00017)
        """
        return self.evaluation_id  # Delegates to property

    def setEvaluationId(self, value: "PositiveInteger") -> "DiagnosticAuthTransmitCertificateEvaluation":
        """
        AUTOSAR-compliant setter for evaluationId with method chaining.

        Args:
            value: The evaluationId to set

        Returns:
            self for method chaining

        Note:
            Delegates to evaluation_id property setter (gets validation automatically)
        """
        self.evaluation_id = value  # Delegates to property setter
        return self

    def getFunction(self) -> "String":
        """
        AUTOSAR-compliant getter for function.

        Returns:
            The function value

        Note:
            Delegates to function property (CODING_RULE_V2_00017)
        """
        return self.function  # Delegates to property

    def setFunction(self, value: "String") -> "DiagnosticAuthTransmitCertificateEvaluation":
        """
        AUTOSAR-compliant setter for function with method chaining.

        Args:
            value: The function to set

        Returns:
            self for method chaining

        Note:
            Delegates to function property setter (gets validation automatically)
        """
        self.function = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_evaluation_id(self, value: Optional["PositiveInteger"]) -> "DiagnosticAuthTransmitCertificateEvaluation":
        """
        Set evaluationId and return self for chaining.

        Args:
            value: The evaluationId to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_evaluation_id("value")
        """
        self.evaluation_id = value  # Use property setter (gets validation)
        return self

    def with_function(self, value: Optional["String"]) -> "DiagnosticAuthTransmitCertificateEvaluation":
        """
        Set function and return self for chaining.

        Args:
            value: The function to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_function("value")
        """
        self.function = value  # Use property setter (gets validation)
        return self

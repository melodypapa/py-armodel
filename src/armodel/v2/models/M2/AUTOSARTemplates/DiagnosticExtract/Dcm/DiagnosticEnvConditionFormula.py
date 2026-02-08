from typing import Optional
from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dcm.EnvironmentalCondition import DiagnosticEnvConditionFormulaPart


class DiagnosticEnvConditionFormula(DiagnosticEnvConditionFormulaPart):
    """
    A DiagnosticEnvConditionFormula embodies the computation instruction that is
    to be evaluated at runtime to determine if the
    DiagnosticEnvironmentalCondition is currently present (i.e. the formula is
    evaluated to true) or not (otherwise). The formula itself consists of parts
    which are combined by the logical operations specified by
    DiagnosticEnvConditionFormula.op. If a diagnostic functionality cannot be
    executed because an environmental condition fails then the diagnostic stack
    shall send a negative response code (NRC) back to the client. The value of
    the NRC is directly related to the specific formula and is therefore
    formalized in the attribute DiagnosticEnvCondition Formula.nrcValue.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::EnvironmentalCondition::DiagnosticEnvConditionFormula

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 80, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute represents the concrete NRC value that returned if the
        # condition fails.
        self._nrcValue: Optional["PositiveInteger"] = None

    @property
    def nrc_value(self) -> Optional["PositiveInteger"]:
        """Get nrcValue (Pythonic accessor)."""
        return self._nrcValue

    @nrc_value.setter
    def nrc_value(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set nrcValue with validation.

        Args:
            value: The nrcValue to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nrcValue = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"nrcValue must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._nrcValue = value
        # This attribute represents the concrete operator operators: and, or) of the
                # condition formula.
        # DiagnosticEnvCondition * aggr This aggregation represents the collection of
                # formula that can be combined by logical operators.
        self._op: Optional["DiagnosticLogical"] = None

    @property
    def op(self) -> Optional["DiagnosticLogical"]:
        """Get op (Pythonic accessor)."""
        return self._op

    @op.setter
    def op(self, value: Optional["DiagnosticLogical"]) -> None:
        """
        Set op with validation.

        Args:
            value: The op to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._op = None
            return

        if not isinstance(value, DiagnosticLogical):
            raise TypeError(
                f"op must be DiagnosticLogical or None, got {type(value).__name__}"
            )
        self._op = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getNrcValue(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for nrcValue.

        Returns:
            The nrcValue value

        Note:
            Delegates to nrc_value property (CODING_RULE_V2_00017)
        """
        return self.nrc_value  # Delegates to property

    def setNrcValue(self, value: "PositiveInteger") -> "DiagnosticEnvConditionFormula":
        """
        AUTOSAR-compliant setter for nrcValue with method chaining.

        Args:
            value: The nrcValue to set

        Returns:
            self for method chaining

        Note:
            Delegates to nrc_value property setter (gets validation automatically)
        """
        self.nrc_value = value  # Delegates to property setter
        return self

    def getOp(self) -> "DiagnosticLogical":
        """
        AUTOSAR-compliant getter for op.

        Returns:
            The op value

        Note:
            Delegates to op property (CODING_RULE_V2_00017)
        """
        return self.op  # Delegates to property

    def setOp(self, value: "DiagnosticLogical") -> "DiagnosticEnvConditionFormula":
        """
        AUTOSAR-compliant setter for op with method chaining.

        Args:
            value: The op to set

        Returns:
            self for method chaining

        Note:
            Delegates to op property setter (gets validation automatically)
        """
        self.op = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_nrc_value(self, value: Optional["PositiveInteger"]) -> "DiagnosticEnvConditionFormula":
        """
        Set nrcValue and return self for chaining.

        Args:
            value: The nrcValue to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nrc_value("value")
        """
        self.nrc_value = value  # Use property setter (gets validation)
        return self

    def with_op(self, value: Optional["DiagnosticLogical"]) -> "DiagnosticEnvConditionFormula":
        """
        Set op and return self for chaining.

        Args:
            value: The op to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_op("value")
        """
        self.op = value  # Use property setter (gets validation)
        return self

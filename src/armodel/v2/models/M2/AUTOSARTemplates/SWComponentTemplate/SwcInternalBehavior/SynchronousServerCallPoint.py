from typing import Optional
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ServerCall import ServerCallPoint


class SynchronousServerCallPoint(ServerCallPoint):
    """
    This means that the RunnableEntity is supposed to perform a blocking wait
    for a response from the server.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::SwcInternalBehavior::ServerCall::SynchronousServerCallPoint

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 580, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2074, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This indicates that the call point is located at the deepest level inside one
        # or more ExclusiveAreas that are nested the given order.
        self._calledFrom: Optional["ExclusiveAreaNesting"] = None

    @property
    def called_from(self) -> Optional["ExclusiveAreaNesting"]:
        """Get calledFrom (Pythonic accessor)."""
        return self._calledFrom

    @called_from.setter
    def called_from(self, value: Optional["ExclusiveAreaNesting"]) -> None:
        """
        Set calledFrom with validation.

        Args:
            value: The calledFrom to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._calledFrom = None
            return

        if not isinstance(value, ExclusiveAreaNesting):
            raise TypeError(
                f"calledFrom must be ExclusiveAreaNesting or None, got {type(value).__name__}"
            )
        self._calledFrom = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCalledFrom(self) -> "ExclusiveAreaNesting":
        """
        AUTOSAR-compliant getter for calledFrom.

        Returns:
            The calledFrom value

        Note:
            Delegates to called_from property (CODING_RULE_V2_00017)
        """
        return self.called_from  # Delegates to property

    def setCalledFrom(self, value: "ExclusiveAreaNesting") -> "SynchronousServerCallPoint":
        """
        AUTOSAR-compliant setter for calledFrom with method chaining.

        Args:
            value: The calledFrom to set

        Returns:
            self for method chaining

        Note:
            Delegates to called_from property setter (gets validation automatically)
        """
        self.called_from = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_called_from(self, value: Optional["ExclusiveAreaNesting"]) -> "SynchronousServerCallPoint":
        """
        Set calledFrom and return self for chaining.

        Args:
            value: The calledFrom to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_called_from("value")
        """
        self.called_from = value  # Use property setter (gets validation)
        return self

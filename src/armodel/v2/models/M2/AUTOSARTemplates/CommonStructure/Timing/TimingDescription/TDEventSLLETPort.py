from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription import TDEventSLLET

    RefType,
)


class TDEventSLLETPort(TDEventSLLET):
    """
    Used to describe SL-LET timing events on the level of a SWC port.

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingDescription::TimingDescription

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 79, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The originating port of the timing event.
        self._port: RefType = None

    @property
    def port(self) -> RefType:
        """Get port (Pythonic accessor)."""
        return self._port

    @port.setter
    def port(self, value: RefType) -> None:
        """
        Set port with validation.

        Args:
            value: The port to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._port = None
            return

        self._port = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getPort(self) -> RefType:
        """
        AUTOSAR-compliant getter for port.

        Returns:
            The port value

        Note:
            Delegates to port property (CODING_RULE_V2_00017)
        """
        return self.port  # Delegates to property

    def setPort(self, value: RefType) -> "TDEventSLLETPort":
        """
        AUTOSAR-compliant setter for port with method chaining.

        Args:
            value: The port to set

        Returns:
            self for method chaining

        Note:
            Delegates to port property setter (gets validation automatically)
        """
        self.port = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_port(self, value: Optional[RefType]) -> "TDEventSLLETPort":
        """
        Set port and return self for chaining.

        Args:
            value: The port to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_port("value")
        """
        self.port = value  # Use property setter (gets validation)
        return self

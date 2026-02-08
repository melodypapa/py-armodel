from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class HwPortMapping(ARObject):
    """
    HWPortMapping specifies the hwCommunicationPort (defined in the ECU Resource
    Template) to realize the specified CommunicationConnector in a physical
    topology.

    Package: M2::AUTOSARTemplates::SystemTemplate::ECUResourceMapping

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 183, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to the CommunicationConnector in the System Template.
        self._communication: Optional["Communication"] = None

    @property
    def communication(self) -> Optional["Communication"]:
        """Get communication (Pythonic accessor)."""
        return self._communication

    @communication.setter
    def communication(self, value: Optional["Communication"]) -> None:
        """
        Set communication with validation.

        Args:
            value: The communication to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._communication = None
            return

        if not isinstance(value, Communication):
            raise TypeError(
                f"communication must be Communication or None, got {type(value).__name__}"
            )
        self._communication = value
        # Reference to the HwPinPortGroup of category The connection to the Hw is
        # described in the Ecu.
        self._hw: RefType = None

    @property
    def hw(self) -> RefType:
        """Get hw (Pythonic accessor)."""
        return self._hw

    @hw.setter
    def hw(self, value: RefType) -> None:
        """
        Set hw with validation.

        Args:
            value: The hw to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._hw = None
            return

        self._hw = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCommunication(self) -> "Communication":
        """
        AUTOSAR-compliant getter for communication.

        Returns:
            The communication value

        Note:
            Delegates to communication property (CODING_RULE_V2_00017)
        """
        return self.communication  # Delegates to property

    def setCommunication(self, value: "Communication") -> "HwPortMapping":
        """
        AUTOSAR-compliant setter for communication with method chaining.

        Args:
            value: The communication to set

        Returns:
            self for method chaining

        Note:
            Delegates to communication property setter (gets validation automatically)
        """
        self.communication = value  # Delegates to property setter
        return self

    def getHw(self) -> RefType:
        """
        AUTOSAR-compliant getter for hw.

        Returns:
            The hw value

        Note:
            Delegates to hw property (CODING_RULE_V2_00017)
        """
        return self.hw  # Delegates to property

    def setHw(self, value: RefType) -> "HwPortMapping":
        """
        AUTOSAR-compliant setter for hw with method chaining.

        Args:
            value: The hw to set

        Returns:
            self for method chaining

        Note:
            Delegates to hw property setter (gets validation automatically)
        """
        self.hw = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_communication(self, value: Optional["Communication"]) -> "HwPortMapping":
        """
        Set communication and return self for chaining.

        Args:
            value: The communication to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_communication("value")
        """
        self.communication = value  # Use property setter (gets validation)
        return self

    def with_hw(self, value: Optional[RefType]) -> "HwPortMapping":
        """
        Set hw and return self for chaining.

        Args:
            value: The hw to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_hw("value")
        """
        self.hw = value  # Use property setter (gets validation)
        return self

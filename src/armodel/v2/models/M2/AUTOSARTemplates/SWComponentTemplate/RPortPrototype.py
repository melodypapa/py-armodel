from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import (
    AbstractRequiredPortPrototype,
)


class RPortPrototype(AbstractRequiredPortPrototype):
    """
    Component port requiring a certain port interface.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::Components

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 68, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2047, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 237, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 460, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 202, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # If set to true, this attribute indicates that the enclosing may be left
        # unconnected and that this explicitly been considered in the.
        self._mayBe: Optional["Boolean"] = None

    @property
    def may_be(self) -> Optional["Boolean"]:
        """Get mayBe (Pythonic accessor)."""
        return self._mayBe

    @may_be.setter
    def may_be(self, value: Optional["Boolean"]) -> None:
        """
        Set mayBe with validation.

        Args:
            value: The mayBe to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._mayBe = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"mayBe must be Boolean or None, got {type(value).__name__}"
            )
        self._mayBe = value
        # isOfType.
        self._required: Optional["PortInterface"] = None

    @property
    def required(self) -> Optional["PortInterface"]:
        """Get required (Pythonic accessor)."""
        return self._required

    @required.setter
    def required(self, value: Optional["PortInterface"]) -> None:
        """
        Set required with validation.

        Args:
            value: The required to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._required = None
            return

        if not isinstance(value, PortInterface):
            raise TypeError(
                f"required must be PortInterface or None, got {type(value).__name__}"
            )
        self._required = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMayBe(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for mayBe.

        Returns:
            The mayBe value

        Note:
            Delegates to may_be property (CODING_RULE_V2_00017)
        """
        return self.may_be  # Delegates to property

    def setMayBe(self, value: "Boolean") -> "RPortPrototype":
        """
        AUTOSAR-compliant setter for mayBe with method chaining.

        Args:
            value: The mayBe to set

        Returns:
            self for method chaining

        Note:
            Delegates to may_be property setter (gets validation automatically)
        """
        self.may_be = value  # Delegates to property setter
        return self

    def getRequired(self) -> "PortInterface":
        """
        AUTOSAR-compliant getter for required.

        Returns:
            The required value

        Note:
            Delegates to required property (CODING_RULE_V2_00017)
        """
        return self.required  # Delegates to property

    def setRequired(self, value: "PortInterface") -> "RPortPrototype":
        """
        AUTOSAR-compliant setter for required with method chaining.

        Args:
            value: The required to set

        Returns:
            self for method chaining

        Note:
            Delegates to required property setter (gets validation automatically)
        """
        self.required = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_may_be(self, value: Optional["Boolean"]) -> "RPortPrototype":
        """
        Set mayBe and return self for chaining.

        Args:
            value: The mayBe to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_may_be("value")
        """
        self.may_be = value  # Use property setter (gets validation)
        return self

    def with_required(self, value: Optional["PortInterface"]) -> "RPortPrototype":
        """
        Set required and return self for chaining.

        Args:
            value: The required to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_required("value")
        """
        self.required = value  # Use property setter (gets validation)
        return self

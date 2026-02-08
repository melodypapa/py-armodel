from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class Compu(ARObject):
    """
    This meta-class represents the ability to express one particular
    computation.

    Package: M2::MSR::AsamHdo::ComputationMethod

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 386, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This specifies the details of the computation.
        self._compuContent: Optional["CompuContent"] = None

    @property
    def compu_content(self) -> Optional["CompuContent"]:
        """Get compuContent (Pythonic accessor)."""
        return self._compuContent

    @compu_content.setter
    def compu_content(self, value: Optional["CompuContent"]) -> None:
        """
        Set compuContent with validation.

        Args:
            value: The compuContent to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._compuContent = None
            return

        if not isinstance(value, CompuContent):
            raise TypeError(
                f"compuContent must be CompuContent or None, got {type(value).__name__}"
            )
        self._compuContent = value
        # This property can be used to specify an output value for a formula, if the
                # value to be converted lies plausibility limit.
        # Although this is possible for formulae, it is especially valid for variables
                # conversion formulae.
        self._compuDefault: Optional["CompuConst"] = None

    @property
    def compu_default(self) -> Optional["CompuConst"]:
        """Get compuDefault (Pythonic accessor)."""
        return self._compuDefault

    @compu_default.setter
    def compu_default(self, value: Optional["CompuConst"]) -> None:
        """
        Set compuDefault with validation.

        Args:
            value: The compuDefault to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._compuDefault = None
            return

        if not isinstance(value, CompuConst):
            raise TypeError(
                f"compuDefault must be CompuConst or None, got {type(value).__name__}"
            )
        self._compuDefault = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCompuContent(self) -> "CompuContent":
        """
        AUTOSAR-compliant getter for compuContent.

        Returns:
            The compuContent value

        Note:
            Delegates to compu_content property (CODING_RULE_V2_00017)
        """
        return self.compu_content  # Delegates to property

    def setCompuContent(self, value: "CompuContent") -> "Compu":
        """
        AUTOSAR-compliant setter for compuContent with method chaining.

        Args:
            value: The compuContent to set

        Returns:
            self for method chaining

        Note:
            Delegates to compu_content property setter (gets validation automatically)
        """
        self.compu_content = value  # Delegates to property setter
        return self

    def getCompuDefault(self) -> "CompuConst":
        """
        AUTOSAR-compliant getter for compuDefault.

        Returns:
            The compuDefault value

        Note:
            Delegates to compu_default property (CODING_RULE_V2_00017)
        """
        return self.compu_default  # Delegates to property

    def setCompuDefault(self, value: "CompuConst") -> "Compu":
        """
        AUTOSAR-compliant setter for compuDefault with method chaining.

        Args:
            value: The compuDefault to set

        Returns:
            self for method chaining

        Note:
            Delegates to compu_default property setter (gets validation automatically)
        """
        self.compu_default = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_compu_content(self, value: Optional["CompuContent"]) -> "Compu":
        """
        Set compuContent and return self for chaining.

        Args:
            value: The compuContent to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_compu_content("value")
        """
        self.compu_content = value  # Use property setter (gets validation)
        return self

    def with_compu_default(self, value: Optional["CompuConst"]) -> "Compu":
        """
        Set compuDefault and return self for chaining.

        Args:
            value: The compuDefault to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_compu_default("value")
        """
        self.compu_default = value  # Use property setter (gets validation)
        return self

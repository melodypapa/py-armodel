from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class ValueGroup(ARObject):
    """
    This element enables values to be grouped. It can be used to perform row and
    column-orientated groupings, so that these can be rendered properly e.g. as
    a table.

    Package: M2::MSR::CalibrationData::CalibrationValue

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 458, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This label allows to give the valueGroup a particular It can be used if the
        # Values are rendered as a.
        self._label: Optional["MultilanguageLong"] = None

    @property
    def label(self) -> Optional["MultilanguageLong"]:
        """Get label (Pythonic accessor)."""
        return self._label

    @label.setter
    def label(self, value: Optional["MultilanguageLong"]) -> None:
        """
        Set label with validation.

        Args:
            value: The label to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._label = None
            return

        if not isinstance(value, MultilanguageLong):
            raise TypeError(
                f"label must be MultilanguageLong or None, got {type(value).__name__}"
            )
        self._label = value
        # This represents the contents of the value group.
        self._vgContents: Optional["SwValues"] = None

    @property
    def vg_contents(self) -> Optional["SwValues"]:
        """Get vgContents (Pythonic accessor)."""
        return self._vgContents

    @vg_contents.setter
    def vg_contents(self, value: Optional["SwValues"]) -> None:
        """
        Set vgContents with validation.

        Args:
            value: The vgContents to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._vgContents = None
            return

        if not isinstance(value, SwValues):
            raise TypeError(
                f"vgContents must be SwValues or None, got {type(value).__name__}"
            )
        self._vgContents = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getLabel(self) -> "MultilanguageLong":
        """
        AUTOSAR-compliant getter for label.

        Returns:
            The label value

        Note:
            Delegates to label property (CODING_RULE_V2_00017)
        """
        return self.label  # Delegates to property

    def setLabel(self, value: "MultilanguageLong") -> "ValueGroup":
        """
        AUTOSAR-compliant setter for label with method chaining.

        Args:
            value: The label to set

        Returns:
            self for method chaining

        Note:
            Delegates to label property setter (gets validation automatically)
        """
        self.label = value  # Delegates to property setter
        return self

    def getVgContents(self) -> "SwValues":
        """
        AUTOSAR-compliant getter for vgContents.

        Returns:
            The vgContents value

        Note:
            Delegates to vg_contents property (CODING_RULE_V2_00017)
        """
        return self.vg_contents  # Delegates to property

    def setVgContents(self, value: "SwValues") -> "ValueGroup":
        """
        AUTOSAR-compliant setter for vgContents with method chaining.

        Args:
            value: The vgContents to set

        Returns:
            self for method chaining

        Note:
            Delegates to vg_contents property setter (gets validation automatically)
        """
        self.vg_contents = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_label(self, value: Optional["MultilanguageLong"]) -> "ValueGroup":
        """
        Set label and return self for chaining.

        Args:
            value: The label to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_label("value")
        """
        self.label = value  # Use property setter (gets validation)
        return self

    def with_vg_contents(self, value: Optional["SwValues"]) -> "ValueGroup":
        """
        Set vgContents and return self for chaining.

        Args:
            value: The vgContents to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_vg_contents("value")
        """
        self.vg_contents = value  # Use property setter (gets validation)
        return self

from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class Sdf(ARObject):
    """
    This class represents a numerical value in a special data group which may be
    subject to variability.

    Package: M2::MSR::AsamHdo::SpecialData

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 92, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attributes specifies an identifier.
        # Gid comes from the Identifier" which is the in XML.
        # The role of this attribute is the the name of an XML - element.
        self._gid: "NameToken" = None

    @property
    def gid(self) -> "NameToken":
        """Get gid (Pythonic accessor)."""
        return self._gid

    @gid.setter
    def gid(self, value: "NameToken") -> None:
        """
        Set gid with validation.

        Args:
            value: The gid to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, NameToken):
            raise TypeError(
                f"gid must be NameToken, got {type(value).__name__}"
            )
        self._gid = value
        # This is the value of the special data.
        self._value: Optional["Numerical"] = None

    @property
    def value(self) -> Optional["Numerical"]:
        """Get value (Pythonic accessor)."""
        return self._value

    @value.setter
    def value(self, value: Optional["Numerical"]) -> None:
        """
        Set value with validation.

        Args:
            value: The value to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._value = None
            return

        if not isinstance(value, Numerical):
            raise TypeError(
                f"value must be Numerical or None, got {type(value).__name__}"
            )
        self._value = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getGid(self) -> "NameToken":
        """
        AUTOSAR-compliant getter for gid.

        Returns:
            The gid value

        Note:
            Delegates to gid property (CODING_RULE_V2_00017)
        """
        return self.gid  # Delegates to property

    def setGid(self, value: "NameToken") -> "Sdf":
        """
        AUTOSAR-compliant setter for gid with method chaining.

        Args:
            value: The gid to set

        Returns:
            self for method chaining

        Note:
            Delegates to gid property setter (gets validation automatically)
        """
        self.gid = value  # Delegates to property setter
        return self

    def getValue(self) -> "Numerical":
        """
        AUTOSAR-compliant getter for value.

        Returns:
            The value value

        Note:
            Delegates to value property (CODING_RULE_V2_00017)
        """
        return self.value  # Delegates to property

    def setValue(self, value: "Numerical") -> "Sdf":
        """
        AUTOSAR-compliant setter for value with method chaining.

        Args:
            value: The value to set

        Returns:
            self for method chaining

        Note:
            Delegates to value property setter (gets validation automatically)
        """
        self.value = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_gid(self, value: "NameToken") -> "Sdf":
        """
        Set gid and return self for chaining.

        Args:
            value: The gid to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_gid("value")
        """
        self.gid = value  # Use property setter (gets validation)
        return self

    def with_value(self, value: Optional["Numerical"]) -> "Sdf":
        """
        Set value and return self for chaining.

        Args:
            value: The value to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_value("value")
        """
        self.value = value  # Use property setter (gets validation)
        return self

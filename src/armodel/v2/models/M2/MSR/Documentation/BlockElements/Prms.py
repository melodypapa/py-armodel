from typing import Optional


class Prms(Paginateable):
    """
    This metaclass represents the ability to specify a parameter table. It can
    be used e.g. to specify parameter tables in a data sheet.

    Package: M2::MSR::Documentation::BlockElements::GerneralParameters::Prms

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 338, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the caption of the parameter table.
        # xml.
        # sequenceOffset=20 topic1 is given to remain compatible with [22] 535 Document
                # ID 202: AUTOSAR_FO_TPS_GenericStructureTemplate Template R23-11.
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
        self._prm: "GeneralParameter" = None

    @property
    def prm(self) -> "GeneralParameter":
        """Get prm (Pythonic accessor)."""
        return self._prm

    @prm.setter
    def prm(self, value: "GeneralParameter") -> None:
        """
        Set prm with validation.

        Args:
            value: The prm to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, GeneralParameter):
            raise TypeError(
                f"prm must be GeneralParameter, got {type(value).__name__}"
            )
        self._prm = value

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

    def setLabel(self, value: "MultilanguageLong") -> "Prms":
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

    def getPrm(self) -> "GeneralParameter":
        """
        AUTOSAR-compliant getter for prm.

        Returns:
            The prm value

        Note:
            Delegates to prm property (CODING_RULE_V2_00017)
        """
        return self.prm  # Delegates to property

    def setPrm(self, value: "GeneralParameter") -> "Prms":
        """
        AUTOSAR-compliant setter for prm with method chaining.

        Args:
            value: The prm to set

        Returns:
            self for method chaining

        Note:
            Delegates to prm property setter (gets validation automatically)
        """
        self.prm = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_label(self, value: Optional["MultilanguageLong"]) -> "Prms":
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

    def with_prm(self, value: "GeneralParameter") -> "Prms":
        """
        Set prm and return self for chaining.

        Args:
            value: The prm to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_prm("value")
        """
        self.prm = value  # Use property setter (gets validation)
        return self

from typing import Optional


class DataExchangePoint(ARElement):
    """
    The Data Exchange Point describes the relationship between a work product
    and its intended use in the methodology with a tailoring of the AUTOSAR
    templates. An informal description is provided by the ’desc’ and
    ’introduction’ attributes of the DataExchangePoint. The informal description
    SHOULD include the subject that is described by this data exchange point.
    E.g. • producible data of tool A, version x • consumable data of tool B,
    version y • agreed profile between partner A and partner B in project xyz

    Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::DataExchangePoint::DataExchangePoint

    Sources:
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 78, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # tailoring to the Autosar Exchange Data Format The and tailoring of the
        # templates specifications Sdgs, Constraints, SpecItems).
        self._dataFormat: Optional["DataFormatTailoring"] = None

    @property
    def data_format(self) -> Optional["DataFormatTailoring"]:
        """Get dataFormat (Pythonic accessor)."""
        return self._dataFormat

    @data_format.setter
    def data_format(self, value: Optional["DataFormatTailoring"]) -> None:
        """
        Set dataFormat with validation.

        Args:
            value: The dataFormat to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dataFormat = None
            return

        if not isinstance(value, DataFormatTailoring):
            raise TypeError(
                f"dataFormat must be DataFormatTailoring or None, got {type(value).__name__}"
            )
        self._dataFormat = value
        # Specifies the kind of this DataExchangePoint.
        # It provides if this DataExchangePoint represents output of a tool that
                # produce data, input of a tool that consumes data or agreed profile.
        self._kind: "DataExchangePoint" = None

    @property
    def kind(self) -> "DataExchangePoint":
        """Get kind (Pythonic accessor)."""
        return self._kind

    @kind.setter
    def kind(self, value: "DataExchangePoint") -> None:
        """
        Set kind with validation.

        Args:
            value: The kind to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, DataExchangePoint):
            raise TypeError(
                f"kind must be DataExchangePoint, got {type(value).__name__}"
            )
        self._kind = value
        # The baseline of the AUTOSAR standard that is used as a within this Data
        # Exchange Point.
        self._referenced: "Baseline" = None

    @property
    def referenced(self) -> "Baseline":
        """Get referenced (Pythonic accessor)."""
        return self._referenced

    @referenced.setter
    def referenced(self, value: "Baseline") -> None:
        """
        Set referenced with validation.

        Args:
            value: The referenced to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, Baseline):
            raise TypeError(
                f"referenced must be Baseline, got {type(value).__name__}"
            )
        self._referenced = value
        # The speficication of the relevant subset of Autosar and custom
        # specifications.
        self._specification: Optional["SpecificationScope"] = None

    @property
    def specification(self) -> Optional["SpecificationScope"]:
        """Get specification (Pythonic accessor)."""
        return self._specification

    @specification.setter
    def specification(self, value: Optional["SpecificationScope"]) -> None:
        """
        Set specification with validation.

        Args:
            value: The specification to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._specification = None
            return

        if not isinstance(value, SpecificationScope):
            raise TypeError(
                f"specification must be SpecificationScope or None, got {type(value).__name__}"
            )
        self._specification = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDataFormat(self) -> "DataFormatTailoring":
        """
        AUTOSAR-compliant getter for dataFormat.

        Returns:
            The dataFormat value

        Note:
            Delegates to data_format property (CODING_RULE_V2_00017)
        """
        return self.data_format  # Delegates to property

    def setDataFormat(self, value: "DataFormatTailoring") -> "DataExchangePoint":
        """
        AUTOSAR-compliant setter for dataFormat with method chaining.

        Args:
            value: The dataFormat to set

        Returns:
            self for method chaining

        Note:
            Delegates to data_format property setter (gets validation automatically)
        """
        self.data_format = value  # Delegates to property setter
        return self

    def getKind(self) -> "DataExchangePoint":
        """
        AUTOSAR-compliant getter for kind.

        Returns:
            The kind value

        Note:
            Delegates to kind property (CODING_RULE_V2_00017)
        """
        return self.kind  # Delegates to property

    def setKind(self, value: "DataExchangePoint") -> "DataExchangePoint":
        """
        AUTOSAR-compliant setter for kind with method chaining.

        Args:
            value: The kind to set

        Returns:
            self for method chaining

        Note:
            Delegates to kind property setter (gets validation automatically)
        """
        self.kind = value  # Delegates to property setter
        return self

    def getReferenced(self) -> "Baseline":
        """
        AUTOSAR-compliant getter for referenced.

        Returns:
            The referenced value

        Note:
            Delegates to referenced property (CODING_RULE_V2_00017)
        """
        return self.referenced  # Delegates to property

    def setReferenced(self, value: "Baseline") -> "DataExchangePoint":
        """
        AUTOSAR-compliant setter for referenced with method chaining.

        Args:
            value: The referenced to set

        Returns:
            self for method chaining

        Note:
            Delegates to referenced property setter (gets validation automatically)
        """
        self.referenced = value  # Delegates to property setter
        return self

    def getSpecification(self) -> "SpecificationScope":
        """
        AUTOSAR-compliant getter for specification.

        Returns:
            The specification value

        Note:
            Delegates to specification property (CODING_RULE_V2_00017)
        """
        return self.specification  # Delegates to property

    def setSpecification(self, value: "SpecificationScope") -> "DataExchangePoint":
        """
        AUTOSAR-compliant setter for specification with method chaining.

        Args:
            value: The specification to set

        Returns:
            self for method chaining

        Note:
            Delegates to specification property setter (gets validation automatically)
        """
        self.specification = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_data_format(self, value: Optional["DataFormatTailoring"]) -> "DataExchangePoint":
        """
        Set dataFormat and return self for chaining.

        Args:
            value: The dataFormat to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_data_format("value")
        """
        self.data_format = value  # Use property setter (gets validation)
        return self

    def with_kind(self, value: "DataExchangePoint") -> "DataExchangePoint":
        """
        Set kind and return self for chaining.

        Args:
            value: The kind to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_kind("value")
        """
        self.kind = value  # Use property setter (gets validation)
        return self

    def with_referenced(self, value: "Baseline") -> "DataExchangePoint":
        """
        Set referenced and return self for chaining.

        Args:
            value: The referenced to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_referenced("value")
        """
        self.referenced = value  # Use property setter (gets validation)
        return self

    def with_specification(self, value: Optional["SpecificationScope"]) -> "DataExchangePoint":
        """
        Set specification and return self for chaining.

        Args:
            value: The specification to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_specification("value")
        """
        self.specification = value  # Use property setter (gets validation)
        return self

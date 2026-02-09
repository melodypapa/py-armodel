from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class DltArgument(Identifiable):
    """
    This element defines an Argument in a DltMessage.

    Package: M2::AUTOSARTemplates::LogAndTraceExtract

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 983, Classic Platform
      R23-11)
      - AUTOSAR_FO_TPS_LogAndTraceExtract.pdf (Page 13, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This aggregation is used to describe subElements of a Dlt that defines a
        # Structure.
        self._dltArgument: List["DltArgument"] = []

    @property
    def dlt_argument(self) -> List["DltArgument"]:
        """Get dltArgument (Pythonic accessor)."""
        return self._dltArgument
        # Describes the DltArgument length in case of Arrays and number of BaseTypes.
        self._length: Optional["PositiveInteger"] = None

    @property
    def length(self) -> Optional["PositiveInteger"]:
        """Get length (Pythonic accessor)."""
        return self._length

    @length.setter
    def length(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set length with validation.

        Args:
            value: The length to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._length = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"length must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._length = value
        # Definition of the networkRepresentation of the Dlt.
        self._network: Optional["SwDataDefProps"] = None

    @property
    def network(self) -> Optional["SwDataDefProps"]:
        """Get network (Pythonic accessor)."""
        return self._network

    @network.setter
    def network(self, value: Optional["SwDataDefProps"]) -> None:
        """
        Set network with validation.

        Args:
            value: The network to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._network = None
            return

        if not isinstance(value, SwDataDefProps):
            raise TypeError(
                f"network must be SwDataDefProps or None, got {type(value).__name__}"
            )
        self._network = value
        # This attribute defines whether the argument is optional or set to true, the
        # argument can be omitted from the a DLT message.
        self._optional: Optional["Boolean"] = None

    @property
    def optional(self) -> Optional["Boolean"]:
        """Get optional (Pythonic accessor)."""
        return self._optional

    @optional.setter
    def optional(self, value: Optional["Boolean"]) -> None:
        """
        Set optional with validation.

        Args:
            value: The optional to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._optional = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"optional must be Boolean or None, got {type(value).__name__}"
            )
        self._optional = value
        # This attribute defines whether the DltArgument is a Data).
        self._predefinedText: Optional["Boolean"] = None

    @property
    def predefined_text(self) -> Optional["Boolean"]:
        """Get predefinedText (Pythonic accessor)."""
        return self._predefinedText

    @predefined_text.setter
    def predefined_text(self, value: Optional["Boolean"]) -> None:
        """
        Set predefinedText with validation.

        Args:
            value: The predefinedText to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._predefinedText = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"predefinedText must be Boolean or None, got {type(value).__name__}"
            )
        self._predefinedText = value
        # This attribute defines whether the length of the Dlt variable (determined at
        # runtime) or not.
        self._variableLength: Optional["Boolean"] = None

    @property
    def variable_length(self) -> Optional["Boolean"]:
        """Get variableLength (Pythonic accessor)."""
        return self._variableLength

    @variable_length.setter
    def variable_length(self, value: Optional["Boolean"]) -> None:
        """
        Set variableLength with validation.

        Args:
            value: The variableLength to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._variableLength = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"variableLength must be Boolean or None, got {type(value).__name__}"
            )
        self._variableLength = value

    def with_dlt_argument(self, value):
        """
        Set dlt_argument and return self for chaining.

        Args:
            value: The dlt_argument to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_dlt_argument("value")
        """
        self.dlt_argument = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDltArgument(self) -> List["DltArgument"]:
        """
        AUTOSAR-compliant getter for dltArgument.

        Returns:
            The dltArgument value

        Note:
            Delegates to dlt_argument property (CODING_RULE_V2_00017)
        """
        return self.dlt_argument  # Delegates to property

    def getLength(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for length.

        Returns:
            The length value

        Note:
            Delegates to length property (CODING_RULE_V2_00017)
        """
        return self.length  # Delegates to property

    def setLength(self, value: "PositiveInteger") -> "DltArgument":
        """
        AUTOSAR-compliant setter for length with method chaining.

        Args:
            value: The length to set

        Returns:
            self for method chaining

        Note:
            Delegates to length property setter (gets validation automatically)
        """
        self.length = value  # Delegates to property setter
        return self

    def getNetwork(self) -> "SwDataDefProps":
        """
        AUTOSAR-compliant getter for network.

        Returns:
            The network value

        Note:
            Delegates to network property (CODING_RULE_V2_00017)
        """
        return self.network  # Delegates to property

    def setNetwork(self, value: "SwDataDefProps") -> "DltArgument":
        """
        AUTOSAR-compliant setter for network with method chaining.

        Args:
            value: The network to set

        Returns:
            self for method chaining

        Note:
            Delegates to network property setter (gets validation automatically)
        """
        self.network = value  # Delegates to property setter
        return self

    def getOptional(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for optional.

        Returns:
            The optional value

        Note:
            Delegates to optional property (CODING_RULE_V2_00017)
        """
        return self.optional  # Delegates to property

    def setOptional(self, value: "Boolean") -> "DltArgument":
        """
        AUTOSAR-compliant setter for optional with method chaining.

        Args:
            value: The optional to set

        Returns:
            self for method chaining

        Note:
            Delegates to optional property setter (gets validation automatically)
        """
        self.optional = value  # Delegates to property setter
        return self

    def getPredefinedText(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for predefinedText.

        Returns:
            The predefinedText value

        Note:
            Delegates to predefined_text property (CODING_RULE_V2_00017)
        """
        return self.predefined_text  # Delegates to property

    def setPredefinedText(self, value: "Boolean") -> "DltArgument":
        """
        AUTOSAR-compliant setter for predefinedText with method chaining.

        Args:
            value: The predefinedText to set

        Returns:
            self for method chaining

        Note:
            Delegates to predefined_text property setter (gets validation automatically)
        """
        self.predefined_text = value  # Delegates to property setter
        return self

    def getVariableLength(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for variableLength.

        Returns:
            The variableLength value

        Note:
            Delegates to variable_length property (CODING_RULE_V2_00017)
        """
        return self.variable_length  # Delegates to property

    def setVariableLength(self, value: "Boolean") -> "DltArgument":
        """
        AUTOSAR-compliant setter for variableLength with method chaining.

        Args:
            value: The variableLength to set

        Returns:
            self for method chaining

        Note:
            Delegates to variable_length property setter (gets validation automatically)
        """
        self.variable_length = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_length(self, value: Optional["PositiveInteger"]) -> "DltArgument":
        """
        Set length and return self for chaining.

        Args:
            value: The length to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_length("value")
        """
        self.length = value  # Use property setter (gets validation)
        return self

    def with_network(self, value: Optional["SwDataDefProps"]) -> "DltArgument":
        """
        Set network and return self for chaining.

        Args:
            value: The network to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_network("value")
        """
        self.network = value  # Use property setter (gets validation)
        return self

    def with_optional(self, value: Optional["Boolean"]) -> "DltArgument":
        """
        Set optional and return self for chaining.

        Args:
            value: The optional to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_optional("value")
        """
        self.optional = value  # Use property setter (gets validation)
        return self

    def with_predefined_text(self, value: Optional["Boolean"]) -> "DltArgument":
        """
        Set predefinedText and return self for chaining.

        Args:
            value: The predefinedText to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_predefined_text("value")
        """
        self.predefined_text = value  # Use property setter (gets validation)
        return self

    def with_variable_length(self, value: Optional["Boolean"]) -> "DltArgument":
        """
        Set variableLength and return self for chaining.

        Args:
            value: The variableLength to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_variable_length("value")
        """
        self.variable_length = value  # Use property setter (gets validation)
        return self

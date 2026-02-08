from typing import Optional


class Std(SingleLanguageReferrable):
    """
    This represents a reference to external standards.

    Package: M2::MSR::Documentation::TextModel::InlineTextElements

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 318, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This element specifies the release date of the external applicable.
        self._date: Optional["DateTime"] = None

    @property
    def date(self) -> Optional["DateTime"]:
        """Get date (Pythonic accessor)."""
        return self._date

    @date.setter
    def date(self, value: Optional["DateTime"]) -> None:
        """
        Set date with validation.

        Args:
            value: The date to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._date = None
            return

        if not isinstance(value, DateTime):
            raise TypeError(
                f"date must be DateTime or None, got {type(value).__name__}"
            )
        self._date = value
        # This represents the reference to the relevant positions of Kept as a string.
        self._position: Optional["String"] = None

    @property
    def position(self) -> Optional["String"]:
        """Get position (Pythonic accessor)."""
        return self._position

    @position.setter
    def position(self, value: Optional["String"]) -> None:
        """
        Set position with validation.

        Args:
            value: The position to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._position = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"position must be String or None, got {type(value).__name__}"
            )
        self._position = value
        # This represents version and state of a standard.
        # Kept as.
        self._state: Optional["String"] = None

    @property
    def state(self) -> Optional["String"]:
        """Get state (Pythonic accessor)."""
        return self._state

    @state.setter
    def state(self, value: Optional["String"]) -> None:
        """
        Set state with validation.

        Args:
            value: The state to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._state = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"state must be String or None, got {type(value).__name__}"
            )
        self._state = value
        # This represents the subtitle of the standard.
        self._subtitle: Optional["String"] = None

    @property
    def subtitle(self) -> Optional["String"]:
        """Get subtitle (Pythonic accessor)."""
        return self._subtitle

    @subtitle.setter
    def subtitle(self, value: Optional["String"]) -> None:
        """
        Set subtitle with validation.

        Args:
            value: The subtitle to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._subtitle = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"subtitle must be String or None, got {type(value).__name__}"
            )
        self._subtitle = value
        # This represents the URL of the standard.
        self._url: Optional["Url"] = None

    @property
    def url(self) -> Optional["Url"]:
        """Get url (Pythonic accessor)."""
        return self._url

    @url.setter
    def url(self, value: Optional["Url"]) -> None:
        """
        Set url with validation.

        Args:
            value: The url to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._url = None
            return

        if not isinstance(value, Url):
            raise TypeError(
                f"url must be Url or None, got {type(value).__name__}"
            )
        self._url = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDate(self) -> "DateTime":
        """
        AUTOSAR-compliant getter for date.

        Returns:
            The date value

        Note:
            Delegates to date property (CODING_RULE_V2_00017)
        """
        return self.date  # Delegates to property

    def setDate(self, value: "DateTime") -> "Std":
        """
        AUTOSAR-compliant setter for date with method chaining.

        Args:
            value: The date to set

        Returns:
            self for method chaining

        Note:
            Delegates to date property setter (gets validation automatically)
        """
        self.date = value  # Delegates to property setter
        return self

    def getPosition(self) -> "String":
        """
        AUTOSAR-compliant getter for position.

        Returns:
            The position value

        Note:
            Delegates to position property (CODING_RULE_V2_00017)
        """
        return self.position  # Delegates to property

    def setPosition(self, value: "String") -> "Std":
        """
        AUTOSAR-compliant setter for position with method chaining.

        Args:
            value: The position to set

        Returns:
            self for method chaining

        Note:
            Delegates to position property setter (gets validation automatically)
        """
        self.position = value  # Delegates to property setter
        return self

    def getState(self) -> "String":
        """
        AUTOSAR-compliant getter for state.

        Returns:
            The state value

        Note:
            Delegates to state property (CODING_RULE_V2_00017)
        """
        return self.state  # Delegates to property

    def setState(self, value: "String") -> "Std":
        """
        AUTOSAR-compliant setter for state with method chaining.

        Args:
            value: The state to set

        Returns:
            self for method chaining

        Note:
            Delegates to state property setter (gets validation automatically)
        """
        self.state = value  # Delegates to property setter
        return self

    def getSubtitle(self) -> "String":
        """
        AUTOSAR-compliant getter for subtitle.

        Returns:
            The subtitle value

        Note:
            Delegates to subtitle property (CODING_RULE_V2_00017)
        """
        return self.subtitle  # Delegates to property

    def setSubtitle(self, value: "String") -> "Std":
        """
        AUTOSAR-compliant setter for subtitle with method chaining.

        Args:
            value: The subtitle to set

        Returns:
            self for method chaining

        Note:
            Delegates to subtitle property setter (gets validation automatically)
        """
        self.subtitle = value  # Delegates to property setter
        return self

    def getUrl(self) -> "Url":
        """
        AUTOSAR-compliant getter for url.

        Returns:
            The url value

        Note:
            Delegates to url property (CODING_RULE_V2_00017)
        """
        return self.url  # Delegates to property

    def setUrl(self, value: "Url") -> "Std":
        """
        AUTOSAR-compliant setter for url with method chaining.

        Args:
            value: The url to set

        Returns:
            self for method chaining

        Note:
            Delegates to url property setter (gets validation automatically)
        """
        self.url = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_date(self, value: Optional["DateTime"]) -> "Std":
        """
        Set date and return self for chaining.

        Args:
            value: The date to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_date("value")
        """
        self.date = value  # Use property setter (gets validation)
        return self

    def with_position(self, value: Optional["String"]) -> "Std":
        """
        Set position and return self for chaining.

        Args:
            value: The position to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_position("value")
        """
        self.position = value  # Use property setter (gets validation)
        return self

    def with_state(self, value: Optional["String"]) -> "Std":
        """
        Set state and return self for chaining.

        Args:
            value: The state to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_state("value")
        """
        self.state = value  # Use property setter (gets validation)
        return self

    def with_subtitle(self, value: Optional["String"]) -> "Std":
        """
        Set subtitle and return self for chaining.

        Args:
            value: The subtitle to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_subtitle("value")
        """
        self.subtitle = value  # Use property setter (gets validation)
        return self

    def with_url(self, value: Optional["Url"]) -> "Std":
        """
        Set url and return self for chaining.

        Args:
            value: The url to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_url("value")
        """
        self.url = value  # Use property setter (gets validation)
        return self

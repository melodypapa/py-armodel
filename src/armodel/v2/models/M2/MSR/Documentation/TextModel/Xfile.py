from typing import Optional


class Xfile(SingleLanguageReferrable):
    """
    This represents to reference an external file within a documentation.

    Package: M2::MSR::Documentation::TextModel::InlineTextElements::Xfile

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 319, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This element describes the tool which was used to corresponding Xfile.
        # Kept as a string since syntax can be provided to denote a tool.
        self._tool: Optional["String"] = None

    @property
    def tool(self) -> Optional["String"]:
        """Get tool (Pythonic accessor)."""
        return self._tool

    @tool.setter
    def tool(self, value: Optional["String"]) -> None:
        """
        Set tool with validation.

        Args:
            value: The tool to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tool = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"tool must be String or None, got {type(value).__name__}"
            )
        self._tool = value
        # This element describes the tool version which was used the corresponding
                # xfile.
        # Kept as a string, specific syntax can be specified.
        self._toolVersion: Optional["String"] = None

    @property
    def tool_version(self) -> Optional["String"]:
        """Get toolVersion (Pythonic accessor)."""
        return self._toolVersion

    @tool_version.setter
    def tool_version(self, value: Optional["String"]) -> None:
        """
        Set toolVersion with validation.

        Args:
            value: The toolVersion to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._toolVersion = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"toolVersion must be String or None, got {type(value).__name__}"
            )
        self._toolVersion = value
        # This represents the URL of the external file.
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

    def getTool(self) -> "String":
        """
        AUTOSAR-compliant getter for tool.

        Returns:
            The tool value

        Note:
            Delegates to tool property (CODING_RULE_V2_00017)
        """
        return self.tool  # Delegates to property

    def setTool(self, value: "String") -> "Xfile":
        """
        AUTOSAR-compliant setter for tool with method chaining.

        Args:
            value: The tool to set

        Returns:
            self for method chaining

        Note:
            Delegates to tool property setter (gets validation automatically)
        """
        self.tool = value  # Delegates to property setter
        return self

    def getToolVersion(self) -> "String":
        """
        AUTOSAR-compliant getter for toolVersion.

        Returns:
            The toolVersion value

        Note:
            Delegates to tool_version property (CODING_RULE_V2_00017)
        """
        return self.tool_version  # Delegates to property

    def setToolVersion(self, value: "String") -> "Xfile":
        """
        AUTOSAR-compliant setter for toolVersion with method chaining.

        Args:
            value: The toolVersion to set

        Returns:
            self for method chaining

        Note:
            Delegates to tool_version property setter (gets validation automatically)
        """
        self.tool_version = value  # Delegates to property setter
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

    def setUrl(self, value: "Url") -> "Xfile":
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

    def with_tool(self, value: Optional["String"]) -> "Xfile":
        """
        Set tool and return self for chaining.

        Args:
            value: The tool to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tool("value")
        """
        self.tool = value  # Use property setter (gets validation)
        return self

    def with_tool_version(self, value: Optional["String"]) -> "Xfile":
        """
        Set toolVersion and return self for chaining.

        Args:
            value: The toolVersion to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tool_version("value")
        """
        self.tool_version = value  # Use property setter (gets validation)
        return self

    def with_url(self, value: Optional["Url"]) -> "Xfile":
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

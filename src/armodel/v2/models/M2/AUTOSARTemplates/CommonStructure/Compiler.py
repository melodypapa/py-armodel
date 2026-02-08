from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import String
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class Compiler(Identifiable):
    """
    Specifies the compiler attributes. In case of source code this specifies
    requirements how the compiler shall be invoked. In case of object code this
    documents the used compiler settings.

    Package: M2::AUTOSARTemplates::CommonStructure::Implementation::Compiler

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 133, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 621, Classic Platform
      R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 434, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Compiler name (like gcc).
        self._name: Optional["String"] = None

    @property
    def name(self) -> Optional["String"]:
        """Get name (Pythonic accessor)."""
        return self._name

    @name.setter
    def name(self, value: Optional["String"]) -> None:
        """
        Set name with validation.

        Args:
            value: The name to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._name = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"name must be String or None, got {type(value).__name__}"
            )
        self._name = value
        # Specifies the compiler options.
        self._options: Optional["String"] = None

    @property
    def options(self) -> Optional["String"]:
        """Get options (Pythonic accessor)."""
        return self._options

    @options.setter
    def options(self, value: Optional["String"]) -> None:
        """
        Set options with validation.

        Args:
            value: The options to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._options = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"options must be String or None, got {type(value).__name__}"
            )
        self._options = value
        # Vendor of compiler.
        self._vendor: Optional["String"] = None

    @property
    def vendor(self) -> Optional["String"]:
        """Get vendor (Pythonic accessor)."""
        return self._vendor

    @vendor.setter
    def vendor(self, value: Optional["String"]) -> None:
        """
        Set vendor with validation.

        Args:
            value: The vendor to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._vendor = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"vendor must be String or None, got {type(value).__name__}"
            )
        self._vendor = value
        # Exact version of compiler executable.
        self._version: Optional["String"] = None

    @property
    def version(self) -> Optional["String"]:
        """Get version (Pythonic accessor)."""
        return self._version

    @version.setter
    def version(self, value: Optional["String"]) -> None:
        """
        Set version with validation.

        Args:
            value: The version to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._version = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"version must be String or None, got {type(value).__name__}"
            )
        self._version = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getName(self) -> "String":
        """
        AUTOSAR-compliant getter for name.

        Returns:
            The name value

        Note:
            Delegates to name property (CODING_RULE_V2_00017)
        """
        return self.name  # Delegates to property

    def setName(self, value: "String") -> "Compiler":
        """
        AUTOSAR-compliant setter for name with method chaining.

        Args:
            value: The name to set

        Returns:
            self for method chaining

        Note:
            Delegates to name property setter (gets validation automatically)
        """
        self.name = value  # Delegates to property setter
        return self

    def getOptions(self) -> "String":
        """
        AUTOSAR-compliant getter for options.

        Returns:
            The options value

        Note:
            Delegates to options property (CODING_RULE_V2_00017)
        """
        return self.options  # Delegates to property

    def setOptions(self, value: "String") -> "Compiler":
        """
        AUTOSAR-compliant setter for options with method chaining.

        Args:
            value: The options to set

        Returns:
            self for method chaining

        Note:
            Delegates to options property setter (gets validation automatically)
        """
        self.options = value  # Delegates to property setter
        return self

    def getVendor(self) -> "String":
        """
        AUTOSAR-compliant getter for vendor.

        Returns:
            The vendor value

        Note:
            Delegates to vendor property (CODING_RULE_V2_00017)
        """
        return self.vendor  # Delegates to property

    def setVendor(self, value: "String") -> "Compiler":
        """
        AUTOSAR-compliant setter for vendor with method chaining.

        Args:
            value: The vendor to set

        Returns:
            self for method chaining

        Note:
            Delegates to vendor property setter (gets validation automatically)
        """
        self.vendor = value  # Delegates to property setter
        return self

    def getVersion(self) -> "String":
        """
        AUTOSAR-compliant getter for version.

        Returns:
            The version value

        Note:
            Delegates to version property (CODING_RULE_V2_00017)
        """
        return self.version  # Delegates to property

    def setVersion(self, value: "String") -> "Compiler":
        """
        AUTOSAR-compliant setter for version with method chaining.

        Args:
            value: The version to set

        Returns:
            self for method chaining

        Note:
            Delegates to version property setter (gets validation automatically)
        """
        self.version = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_name(self, value: Optional["String"]) -> "Compiler":
        """
        Set name and return self for chaining.

        Args:
            value: The name to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_name("value")
        """
        self.name = value  # Use property setter (gets validation)
        return self

    def with_options(self, value: Optional["String"]) -> "Compiler":
        """
        Set options and return self for chaining.

        Args:
            value: The options to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_options("value")
        """
        self.options = value  # Use property setter (gets validation)
        return self

    def with_vendor(self, value: Optional["String"]) -> "Compiler":
        """
        Set vendor and return self for chaining.

        Args:
            value: The vendor to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_vendor("value")
        """
        self.vendor = value  # Use property setter (gets validation)
        return self

    def with_version(self, value: Optional["String"]) -> "Compiler":
        """
        Set version and return self for chaining.

        Args:
            value: The version to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_version("value")
        """
        self.version = value  # Use property setter (gets validation)
        return self

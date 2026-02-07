from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class SomeipServiceVersion(ARObject):
    """
    This meta-class represents the ability to describe a version of a SOME/IP
    Service.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Ethernet::ServiceInstances::SomeipServiceVersion

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2059, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Major Version of the ServiceInterface.
        self._majorVersion: Optional["PositiveInteger"] = None

    @property
    def major_version(self) -> Optional["PositiveInteger"]:
        """Get majorVersion (Pythonic accessor)."""
        return self._majorVersion

    @major_version.setter
    def major_version(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set majorVersion with validation.

        Args:
            value: The majorVersion to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._majorVersion = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"majorVersion must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._majorVersion = value
        # Minor Version of the ServiceInterface.
        self._minorVersion: Optional["PositiveInteger"] = None

    @property
    def minor_version(self) -> Optional["PositiveInteger"]:
        """Get minorVersion (Pythonic accessor)."""
        return self._minorVersion

    @minor_version.setter
    def minor_version(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set minorVersion with validation.

        Args:
            value: The minorVersion to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._minorVersion = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"minorVersion must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._minorVersion = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMajorVersion(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for majorVersion.

        Returns:
            The majorVersion value

        Note:
            Delegates to major_version property (CODING_RULE_V2_00017)
        """
        return self.major_version  # Delegates to property

    def setMajorVersion(self, value: "PositiveInteger") -> "SomeipServiceVersion":
        """
        AUTOSAR-compliant setter for majorVersion with method chaining.

        Args:
            value: The majorVersion to set

        Returns:
            self for method chaining

        Note:
            Delegates to major_version property setter (gets validation automatically)
        """
        self.major_version = value  # Delegates to property setter
        return self

    def getMinorVersion(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for minorVersion.

        Returns:
            The minorVersion value

        Note:
            Delegates to minor_version property (CODING_RULE_V2_00017)
        """
        return self.minor_version  # Delegates to property

    def setMinorVersion(self, value: "PositiveInteger") -> "SomeipServiceVersion":
        """
        AUTOSAR-compliant setter for minorVersion with method chaining.

        Args:
            value: The minorVersion to set

        Returns:
            self for method chaining

        Note:
            Delegates to minor_version property setter (gets validation automatically)
        """
        self.minor_version = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_major_version(self, value: Optional["PositiveInteger"]) -> "SomeipServiceVersion":
        """
        Set majorVersion and return self for chaining.

        Args:
            value: The majorVersion to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_major_version("value")
        """
        self.major_version = value  # Use property setter (gets validation)
        return self

    def with_minor_version(self, value: Optional["PositiveInteger"]) -> "SomeipServiceVersion":
        """
        Set minorVersion and return self for chaining.

        Args:
            value: The minorVersion to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_minor_version("value")
        """
        self.minor_version = value  # Use property setter (gets validation)
        return self

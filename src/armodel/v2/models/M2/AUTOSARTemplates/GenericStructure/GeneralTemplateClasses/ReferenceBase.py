from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class ReferenceBase(ARObject):
    """
    This meta-class establishes a basis for relative references. Reference bases
    are identified by the short Label which shall be unique in the current
    package.

    Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::ARPackage

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 72, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute represents a meta-class for which the global is supported via
        # this reference base.
        self._globalElement: List[RefType] = []

    @property
    def global_element(self) -> List[RefType]:
        """Get globalElement (Pythonic accessor)."""
        return self._globalElement
        # This represents the ability to express that global elements in various
        # packages which do not have a common Packages mentioned by Reference used in
        # addition to the one in.
        self._globalIn: List["ARPackage"] = []

    @property
    def global_in(self) -> List["ARPackage"]:
        """Get globalIn (Pythonic accessor)."""
        return self._globalIn
        # This attribute denotes if the current ReferenceBase is the that there can
        # only be one default reference a package.
        self._isDefault: "Boolean" = None

    @property
    def is_default(self) -> "Boolean":
        """Get isDefault (Pythonic accessor)."""
        return self._isDefault

    @is_default.setter
    def is_default(self, value: "Boolean") -> None:
        """
        Set isDefault with validation.

        Args:
            value: The isDefault to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, Boolean):
            raise TypeError(
                f"isDefault must be Boolean, got {type(value).__name__}"
            )
        self._isDefault = value
        # shortLabel.
        self._package: Optional["ARPackage"] = None

    @property
    def package(self) -> Optional["ARPackage"]:
        """Get package (Pythonic accessor)."""
        return self._package

    @package.setter
    def package(self, value: Optional["ARPackage"]) -> None:
        """
        Set package with validation.

        Args:
            value: The package to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._package = None
            return

        if not isinstance(value, ARPackage):
            raise TypeError(
                f"package must be ARPackage or None, got {type(value).__name__}"
            )
        self._package = value
        # By this name, can denote the applicable base.
        self._shortLabel: "Identifier" = None

    @property
    def short_label(self) -> "Identifier":
        """Get shortLabel (Pythonic accessor)."""
        return self._shortLabel

    @short_label.setter
    def short_label(self, value: "Identifier") -> None:
        """
        Set shortLabel with validation.

        Args:
            value: The shortLabel to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, Identifier):
            raise TypeError(
                f"shortLabel must be Identifier, got {type(value).__name__}"
            )
        self._shortLabel = value

    def with_global_element(self, value):
        """
        Set global_element and return self for chaining.

        Args:
            value: The global_element to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_global_element("value")
        """
        self.global_element = value  # Use property setter (gets validation)
        return self

    def with_global_in(self, value):
        """
        Set global_in and return self for chaining.

        Args:
            value: The global_in to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_global_in("value")
        """
        self.global_in = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getGlobalElement(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for globalElement.

        Returns:
            The globalElement value

        Note:
            Delegates to global_element property (CODING_RULE_V2_00017)
        """
        return self.global_element  # Delegates to property

    def getGlobalIn(self) -> List["ARPackage"]:
        """
        AUTOSAR-compliant getter for globalIn.

        Returns:
            The globalIn value

        Note:
            Delegates to global_in property (CODING_RULE_V2_00017)
        """
        return self.global_in  # Delegates to property

    def getIsDefault(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for isDefault.

        Returns:
            The isDefault value

        Note:
            Delegates to is_default property (CODING_RULE_V2_00017)
        """
        return self.is_default  # Delegates to property

    def setIsDefault(self, value: "Boolean") -> "ReferenceBase":
        """
        AUTOSAR-compliant setter for isDefault with method chaining.

        Args:
            value: The isDefault to set

        Returns:
            self for method chaining

        Note:
            Delegates to is_default property setter (gets validation automatically)
        """
        self.is_default = value  # Delegates to property setter
        return self

    def getPackage(self) -> "ARPackage":
        """
        AUTOSAR-compliant getter for package.

        Returns:
            The package value

        Note:
            Delegates to package property (CODING_RULE_V2_00017)
        """
        return self.package  # Delegates to property

    def setPackage(self, value: "ARPackage") -> "ReferenceBase":
        """
        AUTOSAR-compliant setter for package with method chaining.

        Args:
            value: The package to set

        Returns:
            self for method chaining

        Note:
            Delegates to package property setter (gets validation automatically)
        """
        self.package = value  # Delegates to property setter
        return self

    def getShortLabel(self) -> "Identifier":
        """
        AUTOSAR-compliant getter for shortLabel.

        Returns:
            The shortLabel value

        Note:
            Delegates to short_label property (CODING_RULE_V2_00017)
        """
        return self.short_label  # Delegates to property

    def setShortLabel(self, value: "Identifier") -> "ReferenceBase":
        """
        AUTOSAR-compliant setter for shortLabel with method chaining.

        Args:
            value: The shortLabel to set

        Returns:
            self for method chaining

        Note:
            Delegates to short_label property setter (gets validation automatically)
        """
        self.short_label = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_is_default(self, value: "Boolean") -> "ReferenceBase":
        """
        Set isDefault and return self for chaining.

        Args:
            value: The isDefault to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_is_default("value")
        """
        self.is_default = value  # Use property setter (gets validation)
        return self

    def with_package(self, value: Optional["ARPackage"]) -> "ReferenceBase":
        """
        Set package and return self for chaining.

        Args:
            value: The package to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_package("value")
        """
        self.package = value  # Use property setter (gets validation)
        return self

    def with_short_label(self, value: "Identifier") -> "ReferenceBase":
        """
        Set shortLabel and return self for chaining.

        Args:
            value: The shortLabel to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_short_label("value")
        """
        self.short_label = value  # Use property setter (gets validation)
        return self

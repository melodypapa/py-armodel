from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class LifeCyclePeriod(ARObject):
    """
    This meta class represents the ability to specify a point of time within a
    specified period, e.g. the starting or end point, in which a specific life
    cycle state is valid/applies to.

    Package: M2::AUTOSARTemplates::GenericStructure::LifeCycles

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 392, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Version of the AUTOSAR Release the element referred to part of.
        # contains three levels (major, minor, are defined by AUTOSAR.
        self._arRelease: Optional["RevisionLabelString"] = None

    @property
    def ar_release(self) -> Optional["RevisionLabelString"]:
        """Get arRelease (Pythonic accessor)."""
        return self._arRelease

    @ar_release.setter
    def ar_release(self, value: Optional["RevisionLabelString"]) -> None:
        """
        Set arRelease with validation.

        Args:
            value: The arRelease to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._arRelease = None
            return

        if not isinstance(value, RevisionLabelString):
            raise TypeError(
                f"arRelease must be RevisionLabelString or None, got {type(value).__name__}"
            )
        self._arRelease = value
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
        self._productRelease: Optional["RevisionLabelString"] = None

    @property
    def product_release(self) -> Optional["RevisionLabelString"]:
        """Get productRelease (Pythonic accessor)."""
        return self._productRelease

    @product_release.setter
    def product_release(self, value: Optional["RevisionLabelString"]) -> None:
        """
        Set productRelease with validation.

        Args:
            value: The productRelease to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._productRelease = None
            return

        if not isinstance(value, RevisionLabelString):
            raise TypeError(
                f"productRelease must be RevisionLabelString or None, got {type(value).__name__}"
            )
        self._productRelease = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getArRelease(self) -> "RevisionLabelString":
        """
        AUTOSAR-compliant getter for arRelease.

        Returns:
            The arRelease value

        Note:
            Delegates to ar_release property (CODING_RULE_V2_00017)
        """
        return self.ar_release  # Delegates to property

    def setArRelease(self, value: "RevisionLabelString") -> "LifeCyclePeriod":
        """
        AUTOSAR-compliant setter for arRelease with method chaining.

        Args:
            value: The arRelease to set

        Returns:
            self for method chaining

        Note:
            Delegates to ar_release property setter (gets validation automatically)
        """
        self.ar_release = value  # Delegates to property setter
        return self

    def getDate(self) -> "DateTime":
        """
        AUTOSAR-compliant getter for date.

        Returns:
            The date value

        Note:
            Delegates to date property (CODING_RULE_V2_00017)
        """
        return self.date  # Delegates to property

    def setDate(self, value: "DateTime") -> "LifeCyclePeriod":
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

    def getProductRelease(self) -> "RevisionLabelString":
        """
        AUTOSAR-compliant getter for productRelease.

        Returns:
            The productRelease value

        Note:
            Delegates to product_release property (CODING_RULE_V2_00017)
        """
        return self.product_release  # Delegates to property

    def setProductRelease(self, value: "RevisionLabelString") -> "LifeCyclePeriod":
        """
        AUTOSAR-compliant setter for productRelease with method chaining.

        Args:
            value: The productRelease to set

        Returns:
            self for method chaining

        Note:
            Delegates to product_release property setter (gets validation automatically)
        """
        self.product_release = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_ar_release(self, value: Optional["RevisionLabelString"]) -> "LifeCyclePeriod":
        """
        Set arRelease and return self for chaining.

        Args:
            value: The arRelease to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ar_release("value")
        """
        self.ar_release = value  # Use property setter (gets validation)
        return self

    def with_date(self, value: Optional["DateTime"]) -> "LifeCyclePeriod":
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

    def with_product_release(self, value: Optional["RevisionLabelString"]) -> "LifeCyclePeriod":
        """
        Set productRelease and return self for chaining.

        Args:
            value: The productRelease to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_product_release("value")
        """
        self.product_release = value  # Use property setter (gets validation)
        return self

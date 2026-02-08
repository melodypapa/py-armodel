from abc import ABC
from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class DocumentViewSelectable(ARObject, ABC):
    """
    This meta-class represents the ability to be dedicated to a particular
    audience or document view.

    Package: M2::MSR::Documentation::BlockElements::PaginationAndView

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 340, Foundation
      R23-11)
    """
    def __init__(self):
        if type(self) is DocumentViewSelectable:
            raise TypeError("DocumentViewSelectable is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute allows to denote a semantic information used to identify
                # documentation objects to be customizable document views.
        # It shall be agreement between the involved parties.
        self._si: "NameTokens" = None

    @property
    def si(self) -> "NameTokens":
        """Get si (Pythonic accessor)."""
        return self._si

    @si.setter
    def si(self, value: "NameTokens") -> None:
        """
        Set si with validation.

        Args:
            value: The si to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, NameTokens):
            raise TypeError(
                f"si must be NameTokens, got {type(value).__name__}"
            )
        self._si = value
        # This attribute lists the document views in which the object If it is missing,
        # the object appears in all.
        self._view: Optional["ViewTokens"] = None

    @property
    def view(self) -> Optional["ViewTokens"]:
        """Get view (Pythonic accessor)."""
        return self._view

    @view.setter
    def view(self, value: Optional["ViewTokens"]) -> None:
        """
        Set view with validation.

        Args:
            value: The view to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._view = None
            return

        if not isinstance(value, ViewTokens):
            raise TypeError(
                f"view must be ViewTokens or None, got {type(value).__name__}"
            )
        self._view = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSi(self) -> "NameTokens":
        """
        AUTOSAR-compliant getter for si.

        Returns:
            The si value

        Note:
            Delegates to si property (CODING_RULE_V2_00017)
        """
        return self.si  # Delegates to property

    def setSi(self, value: "NameTokens") -> "DocumentViewSelectable":
        """
        AUTOSAR-compliant setter for si with method chaining.

        Args:
            value: The si to set

        Returns:
            self for method chaining

        Note:
            Delegates to si property setter (gets validation automatically)
        """
        self.si = value  # Delegates to property setter
        return self

    def getView(self) -> "ViewTokens":
        """
        AUTOSAR-compliant getter for view.

        Returns:
            The view value

        Note:
            Delegates to view property (CODING_RULE_V2_00017)
        """
        return self.view  # Delegates to property

    def setView(self, value: "ViewTokens") -> "DocumentViewSelectable":
        """
        AUTOSAR-compliant setter for view with method chaining.

        Args:
            value: The view to set

        Returns:
            self for method chaining

        Note:
            Delegates to view property setter (gets validation automatically)
        """
        self.view = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_si(self, value: "NameTokens") -> "DocumentViewSelectable":
        """
        Set si and return self for chaining.

        Args:
            value: The si to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_si("value")
        """
        self.si = value  # Use property setter (gets validation)
        return self

    def with_view(self, value: Optional["ViewTokens"]) -> "DocumentViewSelectable":
        """
        Set view and return self for chaining.

        Args:
            value: The view to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_view("value")
        """
        self.view = value  # Use property setter (gets validation)
        return self

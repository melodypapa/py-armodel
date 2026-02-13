"""
AUTOSAR Package - EngineeringObject

Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::EngineeringObject
"""


from __future__ import annotations

from abc import ABC
from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
    RevisionLabelString,
)


class EngineeringObject(ARObject, ABC):
    """
    This class specifies an engineering object. Usually such an object is
    represented by a file artifact. The properties of engineering object are
    such that the artifact can be found by querying an ASAM catalog file. The
    engineering object is uniquely identified by
    domain+category+shortLabel+revisionLabel.

    Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::EngineeringObject::EngineeringObject

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 132, Classic
      Platform R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 160, Foundation
      R23-11)
    """
    def __init__(self):
        if type(self) is EngineeringObject:
            raise TypeError("EngineeringObject is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This denotes the role of the engineering object in the Categories are such as
                # for source code for object code for a C-header file need to be defined via
                # Methodology.
        # 381 Document ID 89: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate Module
                # Description Template R23-11.
        self._category: "NameToken" = None

    @property
    def category(self) -> "NameToken":
        """Get category (Pythonic accessor)."""
        return self._category

    @category.setter
    def category(self, value: "NameToken") -> None:
        """
        Set category with validation.

        Args:
            value: The category to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, (NameToken, str)):
            raise TypeError(
                f"category must be NameToken or str, got {type(value).__name__}"
            )
        self._category = value
                # indicate various segments in the the engineering objects.
        # The domain companies, as well as automotive need to be defined by the
                # Methodology.
        # optional to support a default domain.
        self._domain: Optional["NameToken"] = None

    @property
    def domain(self) -> Optional["NameToken"]:
        """Get domain (Pythonic accessor)."""
        return self._domain

    @domain.setter
    def domain(self, value: Optional["NameToken"]) -> None:
        """
        Set domain with validation.

        Args:
            value: The domain to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._domain = None
            return

        if not isinstance(value, (NameToken, str)):
            raise TypeError(
                f"domain must be NameToken or str or None, got {type(value).__name__}"
            )
        self._domain = value
        self._revisionLabel: List[RevisionLabelString] = []

    @property
    def revision_label(self) -> List[RevisionLabelString]:
        """Get revisionLabel (Pythonic accessor)."""
        return self._revisionLabel
        # This is the short name of the engineering object.
        # Note is modeled as NameToken and not as Identifier ASAM-CC it is also a
                # NameToken.
        self._shortLabel: "NameToken" = None

    @property
    def short_label(self) -> "NameToken":
        """Get shortLabel (Pythonic accessor)."""
        return self._shortLabel

    @short_label.setter
    def short_label(self, value: "NameToken") -> None:
        """
        Set shortLabel with validation.

        Args:
            value: The shortLabel to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, (NameToken, str)):
            raise TypeError(
                f"shortLabel must be NameToken or str, got {type(value).__name__}"
            )
        self._shortLabel = value

    def with_revision_label(self, value):
        """
        Set revision_label and return self for chaining.

        Args:
            value: The revision_label to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_revision_label("value")
        """
        self.revision_label = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCategory(self) -> "NameToken":
        """
        AUTOSAR-compliant getter for category.

        Returns:
            The category value

        Note:
            Delegates to category property (CODING_RULE_V2_00017)
        """
        return self.category  # Delegates to property

    def setCategory(self, value: "NameToken") -> EngineeringObject:
        """
        AUTOSAR-compliant setter for category with method chaining.

        Args:
            value: The category to set

        Returns:
            self for method chaining

        Note:
            Delegates to category property setter (gets validation automatically)
        """
        self.category = value  # Delegates to property setter
        return self

    def getDomain(self) -> "NameToken":
        """
        AUTOSAR-compliant getter for domain.

        Returns:
            The domain value

        Note:
            Delegates to domain property (CODING_RULE_V2_00017)
        """
        return self.domain  # Delegates to property

    def setDomain(self, value: "NameToken") -> EngineeringObject:
        """
        AUTOSAR-compliant setter for domain with method chaining.

        Args:
            value: The domain to set

        Returns:
            self for method chaining

        Note:
            Delegates to domain property setter (gets validation automatically)
        """
        self.domain = value  # Delegates to property setter
        return self

    def getRevisionLabel(self) -> List["RevisionLabelString"]:
        """
        AUTOSAR-compliant getter for revisionLabel.

        Returns:
            The revisionLabel value

        Note:
            Delegates to revision_label property (CODING_RULE_V2_00017)
        """
        return self.revision_label  # Delegates to property

    def getShortLabel(self) -> "NameToken":
        """
        AUTOSAR-compliant getter for shortLabel.

        Returns:
            The shortLabel value

        Note:
            Delegates to short_label property (CODING_RULE_V2_00017)
        """
        return self.short_label  # Delegates to property

    def setShortLabel(self, value: "NameToken") -> EngineeringObject:
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

    def with_category(self, value: "NameToken") -> EngineeringObject:
        """
        Set category and return self for chaining.

        Args:
            value: The category to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_category("value")
        """
        self.category = value  # Use property setter (gets validation)
        return self

    def with_domain(self, value: Optional["NameToken"]) -> EngineeringObject:
        """
        Set domain and return self for chaining.

        Args:
            value: The domain to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_domain("value")
        """
        self.domain = value  # Use property setter (gets validation)
        return self

    def with_short_label(self, value: "NameToken") -> EngineeringObject:
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



class AutosarEngineeringObject(EngineeringObject):
    """
    This denotes an engineering object being part of the process. It is a
    specialization of the abstract class EngineeringObject for usage within
    AUTOSAR.

    Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::EngineeringObject::AutosarEngineeringObject

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 132, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 622, Classic Platform
      R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 161, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

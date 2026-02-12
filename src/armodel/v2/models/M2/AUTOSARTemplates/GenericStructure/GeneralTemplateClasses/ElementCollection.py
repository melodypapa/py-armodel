"""
AUTOSAR Package - ElementCollection

Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::ElementCollection

DEVATION NOTE: This file has a circular import with ARPackage.py.
Uses TYPE_CHECKING to resolve the circular dependency.
"""

from __future__ import annotations

from abc import ABC
from typing import TYPE_CHECKING, List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)

if TYPE_CHECKING:
    from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
        ARElement,
    )
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
    Identifier,
    NameToken,
)


class AutoCollectEnum(AREnum):
    """
    AutoCollectEnum enumeration

This enumerator defines the possible approaches to determine the final set of elements in a collection. Aggregated by Collection.autoCollect

Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::ElementCollection
    """
    # All objects being referenced (recursively) from the objects mentioned directly in the collection are also considered as part of the collection.
    refAll = "0"

    # This indicates that only those objects mentioned directly in the collection are part of the collection. No other objects are considered further.
    refNone = "1"

    # This indicates that non standard objects ([TPS_GST_00088]) referenced (recursively) by the objects mentioned directly in the collection are also considered to be part of the collection.
    refNonStandard = "2"

    def __init__(self):
        super().__init__([
            AutoCollectEnum.refAll,
            AutoCollectEnum.refNone,
            AutoCollectEnum.refNonStandard,
        ])

    def __eq__(self, other: object) -> bool:
        """
        Compare AutoCollectEnum with other objects.

        Args:
            other: The object to compare with

        Returns:
            True if the other object is an AutoCollectEnum with the same value or a string matching the value
        """
        if isinstance(other, AutoCollectEnum):
            return self.value == other.value
        elif isinstance(other, str):
            return self.value == other
        return False


class CollectableElement(Identifiable, ABC):
    """
    This meta-class specifies the ability to be part of a specific AUTOSAR
    collection of ARPackages or ARElements. The scope of collection has been
    extended beyond CollectableElement with Revision 4.0.3. For compatibility
    reasons the name of this meta Class was not changed.

    Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::ElementCollection::CollectableElement

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 399, Foundation
      R23-11)
    """
    def __init__(self):
        if type(self) is CollectableElement:
            raise TypeError("CollectableElement is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====


class Collection(CollectableElement):
    """
    This meta-class represents a collection of elements.

    Note that Collection is an ARElement. Therefore it is applicable e.g. for
    EvaluatedVariant, even if this is not obvious. Usually the category of a
    Collection is "SET". On the other hand, a Collection can also express an
    arbitrary relationship between elements. This is denoted by the category
    "RELATION" (see also [TPS_GST_00347]). In this case the collection represents
    an association from "sourceElement" to "targetElement" in the role "role".

    Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::ElementCollection

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2009, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 399, Foundation R23-11)

    DEVIATION: Does not inherit from ARElement due to circular import with ARPackage.py.
    ARElement inheritance is omitted to avoid circular dependency (see module docstring).
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute reflects how far the referenced objects are the collection.
        self._autoCollect: Optional[AutoCollectEnum] = None
        # Provides the ability to express the semantics of a depending on the intended use case.
        self._collection: Optional[NameToken] = None
        # ARElement properties added due to circular import deviation
        self._collected: List = []
        self._element: List = []
        self._elementRole: Optional[Identifier] = None
        self._sourceElement: List = []
        self._sourceInstance: List = []

    @property
    def auto_collect(self) -> Optional[AutoCollectEnum]:
        """Get autoCollect (Pythonic accessor)."""
        return self._autoCollect

    @auto_collect.setter
    def auto_collect(self, value: Optional[AutoCollectEnum]) -> None:
        """
        Set autoCollect with validation.

        Args:
            value: The autoCollect to set (AutoCollectEnum, valid str, or None)

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._autoCollect = None
            return

        # Accept AutoCollectEnum instances
        if isinstance(value, AutoCollectEnum):
            self._autoCollect = value
            return

        # Accept valid enum string values
        valid_values = [AutoCollectEnum.refAll, AutoCollectEnum.refNone, AutoCollectEnum.refNonStandard]
        if isinstance(value, str) and value in valid_values:
            self._autoCollect = value
            return

        raise TypeError(
            f"autoCollect must be AutoCollectEnum or None, got {type(value).__name__}"
        )

    @property
    def collection(self) -> Optional[NameToken]:
        """Get collection (Pythonic accessor)."""
        return self._collection

    @collection.setter
    def collection(self, value: Optional[NameToken]) -> None:
        """
        Set collection with validation.

        Args:
            value: The collection to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._collection = None
            return

        if not isinstance(value, (NameToken, str)):
            raise TypeError(
                f"collection must be NameToken or str or None, got {type(value).__name__}"
            )
        self._collection = value

    # Properties inherited from ARElement (added due to circular import deviation)
    @property
    def collected(self) -> List:
        """Get collected (Pythonic accessor)."""
        return self._collected

    @property
    def element(self) -> List:
        """Get element (Pythonic accessor)."""
        return self._element

    @property
    def element_role(self) -> Optional[Identifier]:
        """Get elementRole (Pythonic accessor)."""
        return self._elementRole

    @element_role.setter
    def element_role(self, value: Optional[Identifier]) -> None:
        """
        Set elementRole with validation.

        Args:
            value: The elementRole to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._elementRole = None
            return

        if not isinstance(value, (Identifier, str)):
            raise TypeError(
                f"elementRole must be Identifier or str or None, got {type(value).__name__}"
            )
        self._elementRole = value

    @property
    def source_element(self) -> List:
        """Get sourceElement (Pythonic accessor)."""
        return self._sourceElement

    @property
    def source_instance(self) -> List:
        """Get sourceInstance (Pythonic accessor)."""
        return self._sourceInstance

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAutoCollect(self) -> Optional[AutoCollectEnum]:
        """
        AUTOSAR-compliant getter for autoCollect.

        Returns:
            The autoCollect value

        Note:
            Delegates to auto_collect property (CODING_RULE_V2_00017)
        """
        return self.auto_collect  # Delegates to property

    def setAutoCollect(self, value: Optional[AutoCollectEnum]) -> Collection:
        """
        AUTOSAR-compliant setter for autoCollect with method chaining.

        Args:
            value: The autoCollect to set

        Returns:
            self for method chaining

        Note:
            Delegates to auto_collect property setter (gets validation automatically)
        """
        self.auto_collect = value  # Delegates to property setter
        return self

    def getCollection(self) -> Optional[NameToken]:
        """
        AUTOSAR-compliant getter for collection.

        Returns:
            The collection value

        Note:
            Delegates to collection property (CODING_RULE_V2_00017)
        """
        return self.collection  # Delegates to property

    def setCollection(self, value: Optional[NameToken]) -> Collection:
        """
        AUTOSAR-compliant setter for collection with method chaining.

        Args:
            value: The collection to set

        Returns:
            self for method chaining

        Note:
            Delegates to collection property setter (gets validation automatically)
        """
        self.collection = value  # Delegates to property setter
        return self

    # AUTOSAR-compatible methods for ARElement properties (added due to circular import deviation)
    def getCollected(self) -> List:
        """
        AUTOSAR-compliant getter for collected.

        Returns:
            The collected value

        Note:
            Delegates to collected property (CODING_RULE_V2_00017)
        """
        return self.collected  # Delegates to property

    def getElement(self) -> List:
        """
        AUTOSAR-compliant getter for element.

        Returns:
            The element value

        Note:
            Delegates to element property (CODING_RULE_V2_00017)
        """
        return self.element  # Delegates to property

    def getElementRole(self) -> Optional[Identifier]:
        """
        AUTOSAR-compliant getter for elementRole.

        Returns:
            The elementRole value

        Note:
            Delegates to element_role property (CODING_RULE_V2_00017)
        """
        return self.element_role  # Delegates to property

    def setElementRole(self, value: Optional[Identifier]) -> Collection:
        """
        AUTOSAR-compliant setter for elementRole with method chaining.

        Args:
            value: The elementRole to set

        Returns:
            self for method chaining

        Note:
            Delegates to element_role property setter (gets validation automatically)
        """
        self.element_role = value  # Delegates to property setter
        return self

    def getSourceElement(self) -> List:
        """
        AUTOSAR-compliant getter for sourceElement.

        Returns:
            The sourceElement value

        Note:
            Delegates to source_element property (CODING_RULE_V2_00017)
        """
        return self.source_element  # Delegates to property

    def getSourceInstance(self) -> List:
        """
        AUTOSAR-compliant getter for sourceInstance.

        Returns:
            The sourceInstance value

        Note:
            Delegates to source_instance property (CODING_RULE_V2_00017)
        """
        return self.source_instance  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_auto_collect(self, value: Optional[AutoCollectEnum]) -> Collection:
        """
        Set autoCollect and return self for chaining.

        Args:
            value: The autoCollect to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_auto_collect(AutoCollectEnum.refAll)
        """
        self.auto_collect = value  # Use property setter (gets validation)
        return self

    def with_collection(self, value: Optional[NameToken]) -> Collection:
        """
        Set collection and return self for chaining.

        Args:
            value: The collection to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_collection("SET")
        """
        self.collection = value  # Use property setter (gets validation)
        return self

    def with_element_role(self, value: Optional[Identifier]) -> Collection:
        """
        Set elementRole and return self for chaining.

        Args:
            value: The elementRole to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_element_role("TestRole")
        """
        self.element_role = value  # Use property setter (gets validation)
        return self

"""
AUTOSAR Package - ElementCollection

Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::ElementCollection
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
    NameToken,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
)


class AutoCollectEnum(AREnum):
    """
    AutoCollectEnum enumeration

This enumerator defines the possible approaches to determine the final set of elements in a collection. Aggregated by Collection.autoCollect

Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::ElementCollection
    """

    def __init__(self) -> None:
        super().__init__([
            AutoCollectEnum.REF_ALL,
            AutoCollectEnum.REF_NONE,
            AutoCollectEnum.REF_NON_STANDARD,
        ])

    # All objects being referenced (recursively) from the objects mentioned directly in the collection are also considered as part of the collection.
    REF_ALL = "0"

    # This indicates that only those objects mentioned directly in the collection are part of the collection. No other objects are considered further.
    REF_NONE = "1"

    # This indicates that non standard objects ([TPS_GST_00088]) referenced (recursively) by the objects mentioned directly in the collection are also considered to be part of the collection.
    REF_NON_STANDARD = "2"


class CollectableElement(Identifiable, ABC):
    """
    This meta-class specifies the ability to be part of a specific AUTOSAR
    collection of ARPackages or ARElements. The scope of collection has been
    extended beyond CollectableElement with Revision 4.0.3. For compatibility
    reasons the name of this meta Class was not changed.

    Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::ElementCollection

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 399, Foundation
      R23-11)
    """
    def __init__(self):
        if type(self) is CollectableElement:
            raise TypeError("CollectableElement is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute reflects how far the referenced objects are the collection.
        self._autoCollect: Optional["AutoCollectEnum"] = None

    @property
    def auto_collect(self) -> Optional["AutoCollectEnum"]:
        """Get autoCollect (Pythonic accessor)."""
        return self._autoCollect

    @auto_collect.setter
    def auto_collect(self, value: Optional["AutoCollectEnum"]) -> None:
        """
        Set autoCollect with validation.
        
        Args:
            value: The autoCollect to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._autoCollect = None
            return

        if not isinstance(value, AutoCollectEnum):
            raise TypeError(
                f"autoCollect must be AutoCollectEnum or None, got {type(value).__name__}"
            )
        self._autoCollect = value
        # is part of the collection.
        # by: AnyInstanceRef.
        self._collected: List["AtpFeature"] = []

    @property
    def collected(self) -> List["AtpFeature"]:
        """Get collected (Pythonic accessor)."""
        return self._collected
        # Provides the ability to express the semantics of a depending on the intended
                # use case.
        # The specified as a NameToken which agreed by all stakeholders.
        self._collection: Optional["NameToken"] = None

    @property
    def collection(self) -> Optional["NameToken"]:
        """Get collection (Pythonic accessor)."""
        return self._collection

    @collection.setter
    def collection(self, value: Optional["NameToken"]) -> None:
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
        # This is an element in the collection.
        # Note that Collection collectable.
        # Therefore collections can be nested.
        # of category="RELATION" this represents the of the relation.
        self._element: List["Identifiable"] = []

    @property
    def element(self) -> List["Identifiable"]:
        """Get element (Pythonic accessor)."""
        return self._element
        # This attribute allows to denote a particular role of the that the applicable
                # semantics shall be between the two parties.
        # it denotes the role of element in the context.
        self._elementRole: Optional["Identifier"] = None

    @property
    def element_role(self) -> Optional["Identifier"]:
        """Get elementRole (Pythonic accessor)."""
        return self._elementRole

    @element_role.setter
    def element_role(self, value: Optional["Identifier"]) -> None:
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
        # Only if Category = "RELATION".
        # This represents the a relation.
        self._sourceElement: List["Identifiable"] = []

    @property
    def source_element(self) -> List["Identifiable"]:
        """Get sourceElement (Pythonic accessor)."""
        return self._sourceElement
        # of a relation.
        # by: AnyInstanceRef.
        self._sourceInstance: List["AtpFeature"] = []

    @property
    def source_instance(self) -> List["AtpFeature"]:
        """Get sourceInstance (Pythonic accessor)."""
        return self._sourceInstance

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAutoCollect(self) -> "AutoCollectEnum":
        """
        AUTOSAR-compliant getter for autoCollect.
        
        Returns:
            The autoCollect value
        
        Note:
            Delegates to auto_collect property (CODING_RULE_V2_00017)
        """
        return self.auto_collect  # Delegates to property

    def setAutoCollect(self, value: "AutoCollectEnum") -> "Collection":
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

    def getCollected(self) -> List["AtpFeature"]:
        """
        AUTOSAR-compliant getter for collected.
        
        Returns:
            The collected value
        
        Note:
            Delegates to collected property (CODING_RULE_V2_00017)
        """
        return self.collected  # Delegates to property

    def getCollection(self) -> "NameToken":
        """
        AUTOSAR-compliant getter for collection.
        
        Returns:
            The collection value
        
        Note:
            Delegates to collection property (CODING_RULE_V2_00017)
        """
        return self.collection  # Delegates to property

    def setCollection(self, value: "NameToken") -> "Collection":
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

    def getElement(self) -> List["Identifiable"]:
        """
        AUTOSAR-compliant getter for element.
        
        Returns:
            The element value
        
        Note:
            Delegates to element property (CODING_RULE_V2_00017)
        """
        return self.element  # Delegates to property

    def getElementRole(self) -> "Identifier":
        """
        AUTOSAR-compliant getter for elementRole.
        
        Returns:
            The elementRole value
        
        Note:
            Delegates to element_role property (CODING_RULE_V2_00017)
        """
        return self.element_role  # Delegates to property

    def setElementRole(self, value: "Identifier") -> "Collection":
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

    def getSourceElement(self) -> List["Identifiable"]:
        """
        AUTOSAR-compliant getter for sourceElement.
        
        Returns:
            The sourceElement value
        
        Note:
            Delegates to source_element property (CODING_RULE_V2_00017)
        """
        return self.source_element  # Delegates to property

    def getSourceInstance(self) -> List["AtpFeature"]:
        """
        AUTOSAR-compliant getter for sourceInstance.
        
        Returns:
            The sourceInstance value
        
        Note:
            Delegates to source_instance property (CODING_RULE_V2_00017)
        """
        return self.source_instance  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_auto_collect(self, value: Optional["AutoCollectEnum"]) -> "Collection":
        """
        Set autoCollect and return self for chaining.
        
        Args:
            value: The autoCollect to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_auto_collect("value")
        """
        self.auto_collect = value  # Use property setter (gets validation)
        return self

    def with_collection(self, value: Optional["NameToken"]) -> "Collection":
        """
        Set collection and return self for chaining.
        
        Args:
            value: The collection to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_collection("value")
        """
        self.collection = value  # Use property setter (gets validation)
        return self

    def with_element_role(self, value: Optional["Identifier"]) -> "Collection":
        """
        Set elementRole and return self for chaining.
        
        Args:
            value: The elementRole to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_element_role("value")
        """
        self.element_role = value  # Use property setter (gets validation)
        return self



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

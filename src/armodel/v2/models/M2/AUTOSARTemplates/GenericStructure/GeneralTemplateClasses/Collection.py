from typing import (
    List,
    Optional,
    Union,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.AtpFeature import (
    AtpFeature,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARElement import (
    ARElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ElementCollection import (
    AutoCollectEnum,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
    NameToken,
)


class Collection(ARElement):
    """
    that Collection is an ARElement. Therefore it is applicable e.g. for
    EvaluatedVariant, even if this is not obvious. Usually the category of a
    Collection is "SET". On the other hand, a Collection can also express an
    arbitrary relationship between elements. This is denoted by the category
    "RELATION" (see also [TPS_GST_00347]). In this case the collection
    represents an association from "sourceElement" to "targetElement" in the
    role "role".

    Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::ElementCollection

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2009, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 398, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 175, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

        # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute reflects how far the referenced objects are the collection.
        self._autoCollect: Optional[AutoCollectEnum] = None
        # is part of the collection.
        # by: AnyInstanceRef.
        self._collected: List["AtpFeature"] = []
        # Provides the ability to express the semantics of a depending on the intended
        # use case.
        # The specified as a NameToken which agreed by all stakeholders.
        self._collection: Optional["NameToken"] = None
        # This is an element in the collection.
        # Note that Collection collectable.
        # Therefore collections can be nested.
        # of category="RELATION" this represents the of the relation.
        self._element: List["Identifiable"] = []
        # This attribute allows to denote a particular role of the that the applicable
        # semantics shall be between the two parties.
        # it denotes the role of element in the context.
        self._elementRole: Optional["Identifier"] = None
        # Only if Category = "RELATION".
        # This represents the a relation.
        self._sourceElement: List["Identifiable"] = []
        # of a relation.
        # by: AnyInstanceRef.
        self._sourceInstance: List["AtpFeature"] = []

    @property
    def auto_collect(self) -> Optional[AutoCollectEnum]:
        """Get autoCollect (Pythonic accessor)."""
        return self._autoCollect

    @auto_collect.setter
    def auto_collect(self, value: Optional[Union["AutoCollectEnum", str]]) -> None:
        """
        Set autoCollect with validation.

        Args:
            value: The autoCollect to set (AutoCollectEnum instance or string)

        Raises:
            TypeError: If value type is incorrect or string value is not a valid enum value
        """
        if value is None:
            self._autoCollect = None
            return

        # Accept both AutoCollectEnum instances and string values
        if isinstance(value, AutoCollectEnum):
            self._autoCollect = value
        elif isinstance(value, str):
            # Validate that the string is a valid enum value
            enum_instance = AutoCollectEnum()
            if not enum_instance.validateEnumValue(value):
                raise TypeError(
                    f"autoCollect must be AutoCollectEnum or None, got invalid string value '{value}'"
                )
            enum_instance.value = value
            self._autoCollect = enum_instance
        else:
            raise TypeError(
                f"autoCollect must be AutoCollectEnum or str or None, got {type(value).__name__}"
            )

    @property
    def collected(self) -> List["AtpFeature"]:
        """Get collected (Pythonic accessor)."""
        return self._collected

    @property
    def collection(self) -> Optional[NameToken]:
        """Get collection (Pythonic accessor)."""
        return self._collection

    @collection.setter
    def collection(self, value: Optional[Union[NameToken, str]]) -> None:
        """
        Set collection with validation.

        Args:
            value: The collection to set (NameToken instance or string)

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._collection = None
            return

        # Accept both NameToken instances and string values
        if isinstance(value, NameToken):
            self._collection = value
        elif isinstance(value, str):
            # Create a NameToken instance with the string value
            name_token = NameToken()
            name_token.value = value
            self._collection = name_token
        else:
            raise TypeError(
                f"collection must be NameToken or str or None, got {type(value).__name__}"
            )

    @property
    def element(self) -> List["Identifiable"]:
        """Get element (Pythonic accessor)."""
        return self._element

    @property
    def element_role(self) -> Optional[Identifier]:
        """Get elementRole (Pythonic accessor)."""
        return self._elementRole

    @element_role.setter
    def element_role(self, value: Optional[Union[Identifier, str]]) -> None:
        """
        Set elementRole with validation.

        Args:
            value: The elementRole to set (Identifier instance or string)

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._elementRole = None
            return

        # Accept both Identifier instances and string values
        if isinstance(value, Identifier):
            self._elementRole = value
        elif isinstance(value, str):
            # Create an Identifier instance with the string value
            identifier = Identifier()
            identifier.value = value
            self._elementRole = identifier
        else:
            raise TypeError(
                f"elementRole must be Identifier or str or None, got {type(value).__name__}"
            )

    @property
    def source_element(self) -> List["Identifiable"]:
        """Get sourceElement (Pythonic accessor)."""
        return self._sourceElement

    @property
    def source_instance(self) -> List["AtpFeature"]:
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

    def setAutoCollect(self, value: Union[AutoCollectEnum, str]) -> "Collection":
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

    def getCollection(self) -> Optional[NameToken]:
        """
        AUTOSAR-compliant getter for collection.

        Returns:
            The collection value

        Note:
            Delegates to collection property (CODING_RULE_V2_00017)
        """
        return self.collection  # Delegates to property

    def setCollection(self, value: Union[NameToken, str]) -> "Collection":
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

    def getElementRole(self) -> Optional[Identifier]:
        """
        AUTOSAR-compliant getter for elementRole.

        Returns:
            The elementRole value

        Note:
            Delegates to element_role property (CODING_RULE_V2_00017)
        """
        return self.element_role  # Delegates to property

    def setElementRole(self, value: Union[Identifier, str]) -> "Collection":
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

    def with_auto_collect(self, value: Optional[Union[AutoCollectEnum, str]]) -> "Collection":
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

    def with_collection(self, value: Optional[Union[NameToken, str]]) -> "Collection":
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

    def with_element_role(self, value: Optional[Union[Identifier, str]]) -> "Collection":
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

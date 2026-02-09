"""
AUTOSAR Package - ViewMapSet

Package: M2::AUTOSARTemplates::GenericStructure::ViewMapSet
"""

from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class ViewMap(Identifiable):
    """
    The ViewMap allows to relate any number of elements on the "first" side to
    any number of elements on the "second" side. Since the ViewMap does not
    address a specific mapping use-case the roles "first" and "second" shall
    imply this generality. This mapping allows to trace transformations of
    artifacts within the AUTOSAR environment. The references to the mapped
    elements can be plain references and/or InstanceRefs.
    
    Package: M2::AUTOSARTemplates::GenericStructure::ViewMapSet::ViewMap
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2079, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 401, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # xml.
        # sequenceOffset=50 by: AnyInstanceRef.
        self._firstElement: List["AtpFeature"] = []

    @property
    def first_element(self) -> List["AtpFeature"]:
        """Get firstElement (Pythonic accessor)."""
        return self._firstElement
        # This attribute is used to describe specific mapping the mappings:.
        self._role: Optional["Identifier"] = None

    @property
    def role(self) -> Optional["Identifier"]:
        """Get role (Pythonic accessor)."""
        return self._role

    @role.setter
    def role(self, value: Optional["Identifier"]) -> None:
        """
        Set role with validation.
        
        Args:
            value: The role to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._role = None
            return

        if not isinstance(value, (Identifier, str)):
            raise TypeError(
                f"role must be Identifier or str or None, got {type(value).__name__}"
            )
        self._role = value
        # xml.
        # sequenceOffset=60 by: AnyInstanceRef.
        self._secondElement: List["AtpFeature"] = []

    @property
    def second_element(self) -> List["AtpFeature"]:
        """Get secondElement (Pythonic accessor)."""
        return self._secondElement

    def with_first_element(self, value):
        """
        Set first_element and return self for chaining.

        Args:
            value: The first_element to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_first_element("value")
        """
        self.first_element = value  # Use property setter (gets validation)
        return self

    def with_second_element(self, value):
        """
        Set second_element and return self for chaining.

        Args:
            value: The second_element to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_second_element("value")
        """
        self.second_element = value  # Use property setter (gets validation)
        return self

    def with_view_map(self, value):
        """
        Set view_map and return self for chaining.

        Args:
            value: The view_map to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_view_map("value")
        """
        self.view_map = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getFirstElement(self) -> List["AtpFeature"]:
        """
        AUTOSAR-compliant getter for firstElement.
        
        Returns:
            The firstElement value
        
        Note:
            Delegates to first_element property (CODING_RULE_V2_00017)
        """
        return self.first_element  # Delegates to property

    def getRole(self) -> "Identifier":
        """
        AUTOSAR-compliant getter for role.
        
        Returns:
            The role value
        
        Note:
            Delegates to role property (CODING_RULE_V2_00017)
        """
        return self.role  # Delegates to property

    def setRole(self, value: "Identifier") -> "ViewMap":
        """
        AUTOSAR-compliant setter for role with method chaining.
        
        Args:
            value: The role to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to role property setter (gets validation automatically)
        """
        self.role = value  # Delegates to property setter
        return self

    def getSecondElement(self) -> List["AtpFeature"]:
        """
        AUTOSAR-compliant getter for secondElement.
        
        Returns:
            The secondElement value
        
        Note:
            Delegates to second_element property (CODING_RULE_V2_00017)
        """
        return self.second_element  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_role(self, value: Optional["Identifier"]) -> "ViewMap":
        """
        Set role and return self for chaining.
        
        Args:
            value: The role to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_role("value")
        """
        self.role = value  # Use property setter (gets validation)
        return self



class ViewMapSet(ARElement):
    """
    Collection of ViewMaps that are used to establish relationships between
    different AUTOSAR artifacts.
    
    Package: M2::AUTOSARTemplates::GenericStructure::ViewMapSet::ViewMapSet
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2079, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 401, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # ViewMaps that are collected by the ViewMapSet.
        self._viewMap: List["ViewMap"] = []

    @property
    def view_map(self) -> List["ViewMap"]:
        """Get viewMap (Pythonic accessor)."""
        return self._viewMap

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getViewMap(self) -> List["ViewMap"]:
        """
        AUTOSAR-compliant getter for viewMap.
        
        Returns:
            The viewMap value
        
        Note:
            Delegates to view_map property (CODING_RULE_V2_00017)
        """
        return self.view_map  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

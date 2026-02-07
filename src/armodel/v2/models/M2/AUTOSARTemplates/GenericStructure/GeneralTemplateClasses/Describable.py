from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class Describable(ARObject, ABC):
    """
    This meta-class represents the ability to add a descriptive documentation to
    non identifiable elements.
    
    Package: M2::AUTOSARTemplates::GenericStructure::GeneralTemplateClasses::Identifiable::Describable
    
    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 312, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 293, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_ECUResourceTemplate.pdf (Page 60, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 981, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2016, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 437, Foundation
      R23-11)
    """
    def __init__(self):
        if type(self) is Describable:
            raise TypeError("Describable is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the administrative data for the.
        self._adminData: Optional["AdminData"] = None

    @property
    def admin_data(self) -> Optional["AdminData"]:
        """Get adminData (Pythonic accessor)."""
        return self._adminData

    @admin_data.setter
    def admin_data(self, value: Optional["AdminData"]) -> None:
        """
        Set adminData with validation.
        
        Args:
            value: The adminData to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._adminData = None
            return

        if not isinstance(value, AdminData):
            raise TypeError(
                f"adminData must be AdminData or None, got {type(value).__name__}"
            )
        self._adminData = value
        # The category is a keyword that specializes the semantics Describable.
        # It affects the expected existence of the applicability of constraints.
        self._category: Optional["CategoryString"] = None

    @property
    def category(self) -> Optional["CategoryString"]:
        """Get category (Pythonic accessor)."""
        return self._category

    @category.setter
    def category(self, value: Optional["CategoryString"]) -> None:
        """
        Set category with validation.
        
        Args:
            value: The category to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._category = None
            return

        if not isinstance(value, CategoryString):
            raise TypeError(
                f"category must be CategoryString or None, got {type(value).__name__}"
            )
        self._category = value
        # This represents a general but brief (one paragraph) what the object in
                # question is about.
        # It is only Desc is intended to be collected into This property helps a human
                # reader to object in question.
        # documentation, (in particular how the built or used) should go to
                # "introduction".
        self._desc: Optional["MultiLanguageOverview"] = None

    @property
    def desc(self) -> Optional["MultiLanguageOverview"]:
        """Get desc (Pythonic accessor)."""
        return self._desc

    @desc.setter
    def desc(self, value: Optional["MultiLanguageOverview"]) -> None:
        """
        Set desc with validation.
        
        Args:
            value: The desc to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._desc = None
            return

        if not isinstance(value, MultiLanguageOverview):
            raise TypeError(
                f"desc must be MultiLanguageOverview or None, got {type(value).__name__}"
            )
        self._desc = value
        # This represents more information about how the object in built or is used.
        # Therefore it is a.
        self._introduction: Optional["DocumentationBlock"] = None

    @property
    def introduction(self) -> Optional["DocumentationBlock"]:
        """Get introduction (Pythonic accessor)."""
        return self._introduction

    @introduction.setter
    def introduction(self, value: Optional["DocumentationBlock"]) -> None:
        """
        Set introduction with validation.
        
        Args:
            value: The introduction to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._introduction = None
            return

        if not isinstance(value, DocumentationBlock):
            raise TypeError(
                f"introduction must be DocumentationBlock or None, got {type(value).__name__}"
            )
        self._introduction = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAdminData(self) -> "AdminData":
        """
        AUTOSAR-compliant getter for adminData.
        
        Returns:
            The adminData value
        
        Note:
            Delegates to admin_data property (CODING_RULE_V2_00017)
        """
        return self.admin_data  # Delegates to property

    def setAdminData(self, value: "AdminData") -> "Describable":
        """
        AUTOSAR-compliant setter for adminData with method chaining.
        
        Args:
            value: The adminData to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to admin_data property setter (gets validation automatically)
        """
        self.admin_data = value  # Delegates to property setter
        return self

    def getCategory(self) -> "CategoryString":
        """
        AUTOSAR-compliant getter for category.
        
        Returns:
            The category value
        
        Note:
            Delegates to category property (CODING_RULE_V2_00017)
        """
        return self.category  # Delegates to property

    def setCategory(self, value: "CategoryString") -> "Describable":
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

    def getDesc(self) -> "MultiLanguageOverview":
        """
        AUTOSAR-compliant getter for desc.
        
        Returns:
            The desc value
        
        Note:
            Delegates to desc property (CODING_RULE_V2_00017)
        """
        return self.desc  # Delegates to property

    def setDesc(self, value: "MultiLanguageOverview") -> "Describable":
        """
        AUTOSAR-compliant setter for desc with method chaining.
        
        Args:
            value: The desc to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to desc property setter (gets validation automatically)
        """
        self.desc = value  # Delegates to property setter
        return self

    def getIntroduction(self) -> "DocumentationBlock":
        """
        AUTOSAR-compliant getter for introduction.
        
        Returns:
            The introduction value
        
        Note:
            Delegates to introduction property (CODING_RULE_V2_00017)
        """
        return self.introduction  # Delegates to property

    def setIntroduction(self, value: "DocumentationBlock") -> "Describable":
        """
        AUTOSAR-compliant setter for introduction with method chaining.
        
        Args:
            value: The introduction to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to introduction property setter (gets validation automatically)
        """
        self.introduction = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_admin_data(self, value: Optional["AdminData"]) -> "Describable":
        """
        Set adminData and return self for chaining.
        
        Args:
            value: The adminData to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_admin_data("value")
        """
        self.admin_data = value  # Use property setter (gets validation)
        return self

    def with_category(self, value: Optional["CategoryString"]) -> "Describable":
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

    def with_desc(self, value: Optional["MultiLanguageOverview"]) -> "Describable":
        """
        Set desc and return self for chaining.
        
        Args:
            value: The desc to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_desc("value")
        """
        self.desc = value  # Use property setter (gets validation)
        return self

    def with_introduction(self, value: Optional["DocumentationBlock"]) -> "Describable":
        """
        Set introduction and return self for chaining.
        
        Args:
            value: The introduction to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_introduction("value")
        """
        self.introduction = value  # Use property setter (gets validation)
        return self
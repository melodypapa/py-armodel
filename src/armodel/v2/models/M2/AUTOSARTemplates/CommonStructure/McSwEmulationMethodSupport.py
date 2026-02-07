from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class McSwEmulationMethodSupport(ARObject):
    """
    This denotes the method used by the RTE to handle the calibration data. It
    is published by the RTE generator and can be used e.g. to generate the
    corresponding emulation method in a Complex Driver. According to the actual
    method given by the category attribute, not all attributes are always
    needed: • double pointered method: only baseReference is mandatory • single
    pointered method: only referenceTable is mandatory • initRam method: only
    elementGroup(s) are mandatory Note: For single/double pointered method the
    group locations are implicitly accessed via the reference table and their
    location can be found from the initial values in the M1 model of the
    respective pointers. Therefore, the description of elementGroups is not
    needed in these cases. Likewise, for double pointered method the reference
    table description can be accessed via the M1 model under baseReference.
    
    Package: M2::AUTOSARTemplates::CommonStructure::MeasurementCalibrationSupport::McSwEmulationMethodSupport
    
    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 180, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Refers to the base pointer in case of the double-pointered.
        self._baseReference: RefType = None

    @property
    def base_reference(self) -> RefType:
        """Get baseReference (Pythonic accessor)."""
        return self._baseReference

    @base_reference.setter
    def base_reference(self, value: RefType) -> None:
        """
        Set baseReference with validation.
        
        Args:
            value: The baseReference to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._baseReference = None
            return

        self._baseReference = value
        # Identifies the actual method.
        # The possible names shall the symbols of the ECU configuration the calibration
                # method of the RTE, and can specific methods.
        self._category: Optional["Identifier"] = None

    @property
    def category(self) -> Optional["Identifier"]:
        """Get category (Pythonic accessor)."""
        return self._category

    @category.setter
    def category(self, value: Optional["Identifier"]) -> None:
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

        if not isinstance(value, Identifier):
            raise TypeError(
                f"category must be Identifier or None, got {type(value).__name__}"
            )
        self._category = value
        # Denotes the grouping of calibration parameters in the RTE code.
        # Depending on the category, this required to set up the emulation code.
        self._elementGroup: List["McParameterElement"] = []

    @property
    def element_group(self) -> List["McParameterElement"]:
        """Get elementGroup (Pythonic accessor)."""
        return self._elementGroup
        # Refers to the pointer table in case of the single-pointered.
        self._referenceTable: RefType = None

    @property
    def reference_table(self) -> RefType:
        """Get referenceTable (Pythonic accessor)."""
        return self._referenceTable

    @reference_table.setter
    def reference_table(self, value: RefType) -> None:
        """
        Set referenceTable with validation.
        
        Args:
            value: The referenceTable to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._referenceTable = None
            return

        self._referenceTable = value
        # Assigns a name to this element.
        self._shortLabel: Optional["Identifier"] = None

    @property
    def short_label(self) -> Optional["Identifier"]:
        """Get shortLabel (Pythonic accessor)."""
        return self._shortLabel

    @short_label.setter
    def short_label(self, value: Optional["Identifier"]) -> None:
        """
        Set shortLabel with validation.
        
        Args:
            value: The shortLabel to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._shortLabel = None
            return

        if not isinstance(value, Identifier):
            raise TypeError(
                f"shortLabel must be Identifier or None, got {type(value).__name__}"
            )
        self._shortLabel = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBaseReference(self) -> RefType:
        """
        AUTOSAR-compliant getter for baseReference.
        
        Returns:
            The baseReference value
        
        Note:
            Delegates to base_reference property (CODING_RULE_V2_00017)
        """
        return self.base_reference  # Delegates to property

    def setBaseReference(self, value: RefType) -> "McSwEmulationMethodSupport":
        """
        AUTOSAR-compliant setter for baseReference with method chaining.
        
        Args:
            value: The baseReference to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to base_reference property setter (gets validation automatically)
        """
        self.base_reference = value  # Delegates to property setter
        return self

    def getCategory(self) -> "Identifier":
        """
        AUTOSAR-compliant getter for category.
        
        Returns:
            The category value
        
        Note:
            Delegates to category property (CODING_RULE_V2_00017)
        """
        return self.category  # Delegates to property

    def setCategory(self, value: "Identifier") -> "McSwEmulationMethodSupport":
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

    def getElementGroup(self) -> List["McParameterElement"]:
        """
        AUTOSAR-compliant getter for elementGroup.
        
        Returns:
            The elementGroup value
        
        Note:
            Delegates to element_group property (CODING_RULE_V2_00017)
        """
        return self.element_group  # Delegates to property

    def getReferenceTable(self) -> RefType:
        """
        AUTOSAR-compliant getter for referenceTable.
        
        Returns:
            The referenceTable value
        
        Note:
            Delegates to reference_table property (CODING_RULE_V2_00017)
        """
        return self.reference_table  # Delegates to property

    def setReferenceTable(self, value: RefType) -> "McSwEmulationMethodSupport":
        """
        AUTOSAR-compliant setter for referenceTable with method chaining.
        
        Args:
            value: The referenceTable to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to reference_table property setter (gets validation automatically)
        """
        self.reference_table = value  # Delegates to property setter
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

    def setShortLabel(self, value: "Identifier") -> "McSwEmulationMethodSupport":
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

    def with_base_reference(self, value: Optional[RefType]) -> "McSwEmulationMethodSupport":
        """
        Set baseReference and return self for chaining.
        
        Args:
            value: The baseReference to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_base_reference("value")
        """
        self.base_reference = value  # Use property setter (gets validation)
        return self

    def with_category(self, value: Optional["Identifier"]) -> "McSwEmulationMethodSupport":
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

    def with_reference_table(self, value: Optional[RefType]) -> "McSwEmulationMethodSupport":
        """
        Set referenceTable and return self for chaining.
        
        Args:
            value: The referenceTable to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_reference_table("value")
        """
        self.reference_table = value  # Use property setter (gets validation)
        return self

    def with_short_label(self, value: Optional["Identifier"]) -> "McSwEmulationMethodSupport":
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
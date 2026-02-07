from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

class McGroup(ARElement):
    """
    Represents a group element to be used as input to support measurement and
    calibration. It is used to provide selection lists (groups) of calibration
    parameters, measurement variables, and functions in a hierarchical manner
    (subGroups).
    
    Package: M2::AUTOSARTemplates::CommonStructure::McGroups::McGroup
    
    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 190, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2034, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # A McFunction that is seen as part of the enclosing group.
        self._mcFunction: List["McFunction"] = []

    @property
    def mc_function(self) -> List["McFunction"]:
        """Get mcFunction (Pythonic accessor)."""
        return self._mcFunction
        # Refers to the set of adjustable data (= calibration by this McGroup.
        # 381 Document ID 89: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate Module
                # Description Template R23-11.
        self._refCalprmSet: RefType = None

    @property
    def ref_calprm_set(self) -> RefType:
        """Get refCalprmSet (Pythonic accessor)."""
        return self._refCalprmSet

    @ref_calprm_set.setter
    def ref_calprm_set(self, value: RefType) -> None:
        """
        Set refCalprmSet with validation.
        
        Args:
            value: The refCalprmSet to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._refCalprmSet = None
            return

        self._refCalprmSet = value
        # Refers to the set of measurable belonging to this Mc atpSplitable.
        self._ref: RefType = None

    @property
    def ref(self) -> RefType:
        """Get ref (Pythonic accessor)."""
        return self._ref

    @ref.setter
    def ref(self, value: RefType) -> None:
        """
        Set ref with validation.
        
        Args:
            value: The ref to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ref = None
            return

        self._ref = value
        # A sub-group that is seen as part of the enclosing group.
        self._subGroup: List[RefType] = []

    @property
    def sub_group(self) -> List[RefType]:
        """Get subGroup (Pythonic accessor)."""
        return self._subGroup

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMcFunction(self) -> List["McFunction"]:
        """
        AUTOSAR-compliant getter for mcFunction.
        
        Returns:
            The mcFunction value
        
        Note:
            Delegates to mc_function property (CODING_RULE_V2_00017)
        """
        return self.mc_function  # Delegates to property

    def getRefCalprmSet(self) -> RefType:
        """
        AUTOSAR-compliant getter for refCalprmSet.
        
        Returns:
            The refCalprmSet value
        
        Note:
            Delegates to ref_calprm_set property (CODING_RULE_V2_00017)
        """
        return self.ref_calprm_set  # Delegates to property

    def setRefCalprmSet(self, value: RefType) -> "McGroup":
        """
        AUTOSAR-compliant setter for refCalprmSet with method chaining.
        
        Args:
            value: The refCalprmSet to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to ref_calprm_set property setter (gets validation automatically)
        """
        self.ref_calprm_set = value  # Delegates to property setter
        return self

    def getRef(self) -> RefType:
        """
        AUTOSAR-compliant getter for ref.
        
        Returns:
            The ref value
        
        Note:
            Delegates to ref property (CODING_RULE_V2_00017)
        """
        return self.ref  # Delegates to property

    def setRef(self, value: RefType) -> "McGroup":
        """
        AUTOSAR-compliant setter for ref with method chaining.
        
        Args:
            value: The ref to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to ref property setter (gets validation automatically)
        """
        self.ref = value  # Delegates to property setter
        return self

    def getSubGroup(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for subGroup.
        
        Returns:
            The subGroup value
        
        Note:
            Delegates to sub_group property (CODING_RULE_V2_00017)
        """
        return self.sub_group  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_ref_calprm_set(self, value: Optional[RefType]) -> "McGroup":
        """
        Set refCalprmSet and return self for chaining.
        
        Args:
            value: The refCalprmSet to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_ref_calprm_set("value")
        """
        self.ref_calprm_set = value  # Use property setter (gets validation)
        return self

    def with_ref(self, value: Optional[RefType]) -> "McGroup":
        """
        Set ref and return self for chaining.
        
        Args:
            value: The ref to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_ref("value")
        """
        self.ref = value  # Use property setter (gets validation)
        return self
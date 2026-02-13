"""
AUTOSAR Package - McGroups

Package: M2::AUTOSARTemplates::CommonStructure::McGroups
"""


from __future__ import annotations
from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARElement,
)


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
        self._refCalprmSet: Optional[RefType] = None

    @property
    def ref_calprm_set(self) -> Optional[RefType]:
        """Get refCalprmSet (Pythonic accessor)."""
        return self._refCalprmSet

    @ref_calprm_set.setter
    def ref_calprm_set(self, value: Optional[RefType]) -> None:
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
        self._ref: Optional[RefType] = None

    @property
    def ref(self) -> Optional[RefType]:
        """Get ref (Pythonic accessor)."""
        return self._ref

    @ref.setter
    def ref(self, value: Optional[RefType]) -> None:
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
        self._subGroup: List[RefType] = []

    @property
    def sub_group(self) -> List[RefType]:
        """Get subGroup (Pythonic accessor)."""
        return self._subGroup

    def with_mc_function(self, value):
        """
        Set mc_function and return self for chaining.

        Args:
            value: The mc_function to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mc_function("value")
        """
        self.mc_function = value  # Use property setter (gets validation)
        return self

    def with_sub_group(self, value):
        """
        Set sub_group and return self for chaining.

        Args:
            value: The sub_group to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sub_group("value")
        """
        self.sub_group = value  # Use property setter (gets validation)
        return self

    def with_flat_map_entry(self, value):
        """
        Set flat_map_entry and return self for chaining.

        Args:
            value: The flat_map_entry to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_flat_map_entry("value")
        """
        self.flat_map_entry = value  # Use property setter (gets validation)
        return self

    def with_mc_data_instance(self, value):
        """
        Set mc_data_instance and return self for chaining.

        Args:
            value: The mc_data_instance to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mc_data_instance("value")
        """
        self.mc_data_instance = value  # Use property setter (gets validation)
        return self

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

    def setRefCalprmSet(self, value: RefType) -> McGroup:
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

    def setRef(self, value: RefType) -> McGroup:
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

    def with_ref_calprm_set(self, value: Optional[RefType]) -> McGroup:
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

    def with_ref(self, value: Optional[RefType]) -> McGroup:
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



class McGroupDataRefSet(ARObject):
    """
    Refers to a set of data assigned to an McGroup in a particular role. The
    data are given • either by entries in a FlatMap • or by data instances that
    are part of MC support data. These two possibilities can be mixed within a
    given McGroupDataRefSet. Which one to use depends on the process and tool
    environment. The set is subject to variability because the same functional
    model may be used with various representation of the data. Tags:
    vh.latestBindingTime=preCompileTime

    Package: M2::AUTOSARTemplates::CommonStructure::McGroups::McGroupDataRefSet

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 191, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2035, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Refers to an entry in a FlatMap that is part of the set, for calibration
                # parameter or measured variable.
        # atpSplitable property has no atp.
        # Splitkey due (PropertySetPattern).
        self._flatMapEntry: List["FlatInstanceDescriptor"] = []

    @property
    def flat_map_entry(self) -> List["FlatInstanceDescriptor"]:
        """Get flatMapEntry (Pythonic accessor)."""
        return self._flatMapEntry
        # Refers to a data instance within MC support data that is the set, i.
        # e.
        # a calibration parameter or measured atpSplitable property has no atp.
        # Splitkey due (PropertySetPattern).
        self._mcDataInstance: List["McDataInstance"] = []

    @property
    def mc_data_instance(self) -> List["McDataInstance"]:
        """Get mcDataInstance (Pythonic accessor)."""
        return self._mcDataInstance

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getFlatMapEntry(self) -> List["FlatInstanceDescriptor"]:
        """
        AUTOSAR-compliant getter for flatMapEntry.

        Returns:
            The flatMapEntry value

        Note:
            Delegates to flat_map_entry property (CODING_RULE_V2_00017)
        """
        return self.flat_map_entry  # Delegates to property

    def getMcDataInstance(self) -> List["McDataInstance"]:
        """
        AUTOSAR-compliant getter for mcDataInstance.

        Returns:
            The mcDataInstance value

        Note:
            Delegates to mc_data_instance property (CODING_RULE_V2_00017)
        """
        return self.mc_data_instance  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

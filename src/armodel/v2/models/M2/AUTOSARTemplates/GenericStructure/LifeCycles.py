"""
AUTOSAR Package - LifeCycles

Package: M2::AUTOSARTemplates::GenericStructure::LifeCycles
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)




class LifeCycleStateDefinitionGroup(ARElement):
    """
    This meta class represents the ability to define the states and properties
    of one particular life cycle.
    
    Package: M2::AUTOSARTemplates::GenericStructure::LifeCycles::LifeCycleStateDefinitionGroup
    
    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 388, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 196, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Describes a single life cycle state of this life cycle state.
        self._lcState: List["LifeCycleState"] = []

    @property
    def lc_state(self) -> List["LifeCycleState"]:
        """Get lcState (Pythonic accessor)."""
        return self._lcState

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getLcState(self) -> List["LifeCycleState"]:
        """
        AUTOSAR-compliant getter for lcState.
        
        Returns:
            The lcState value
        
        Note:
            Delegates to lc_state property (CODING_RULE_V2_00017)
        """
        return self.lc_state  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class LifeCycleState(Identifiable):
    """
    This meta class represents one particular state in the LifeCycle.
    
    Package: M2::AUTOSARTemplates::GenericStructure::LifeCycles::LifeCycleState
    
    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 388, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 196, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class LifeCycleInfoSet(ARElement):
    """
    This meta class represents the ability to attach a life cycle information to
    a particular set of elements. The information can be defined for a
    particular period. This supports the definition of transition plans. If no
    period is specified, the life cycle state applies forever.
    
    Package: M2::AUTOSARTemplates::GenericStructure::LifeCycles::LifeCycleInfoSet
    
    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 391, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 195, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This denotes the default life cycle state.
        # To be used in all within the LifeCycleInfoSet if no state is stated there
                # explicitly.
        # I.
        # e.
        # the defaultLc be overwritten in LifeCycleInfo elements.
        self._defaultLcState: "LifeCycleState" = None

    @property
    def default_lc_state(self) -> "LifeCycleState":
        """Get defaultLcState (Pythonic accessor)."""
        return self._defaultLcState

    @default_lc_state.setter
    def default_lc_state(self, value: "LifeCycleState") -> None:
        """
        Set defaultLcState with validation.
        
        Args:
            value: The defaultLcState to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, LifeCycleState):
            raise TypeError(
                f"defaultLcState must be LifeCycleState, got {type(value).__name__}"
            )
        self._defaultLcState = value
        # Default expiry date, i.
        # e.
        # default end point of period for all specified lifeCycleInfo apply.
        # Note that the can be overridden for each lifeCycleInfo.
        self._defaultPeriod: Optional["LifeCyclePeriod"] = None

    @property
    def default_period(self) -> Optional["LifeCyclePeriod"]:
        """Get defaultPeriod (Pythonic accessor)."""
        return self._defaultPeriod

    @default_period.setter
    def default_period(self, value: Optional["LifeCyclePeriod"]) -> None:
        """
        Set defaultPeriod with validation.
        
        Args:
            value: The defaultPeriod to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._defaultPeriod = None
            return

        if not isinstance(value, LifeCyclePeriod):
            raise TypeError(
                f"defaultPeriod must be LifeCyclePeriod or None, got {type(value).__name__}"
            )
        self._defaultPeriod = value
        # This represents one particular life cycle information.
        self._lifeCycleInfo: List["LifeCycleInfo"] = []

    @property
    def life_cycle_info(self) -> List["LifeCycleInfo"]:
        """Get lifeCycleInfo (Pythonic accessor)."""
        return self._lifeCycleInfo
        # This denotes the life cycle states applicable to the current life cycle info
        # set.
        self._usedLifeCycle: "LifeCycleStateDefinition" = None

    @property
    def used_life_cycle(self) -> "LifeCycleStateDefinition":
        """Get usedLifeCycle (Pythonic accessor)."""
        return self._usedLifeCycle

    @used_life_cycle.setter
    def used_life_cycle(self, value: "LifeCycleStateDefinition") -> None:
        """
        Set usedLifeCycle with validation.
        
        Args:
            value: The usedLifeCycle to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, LifeCycleStateDefinition):
            raise TypeError(
                f"usedLifeCycle must be LifeCycleStateDefinition, got {type(value).__name__}"
            )
        self._usedLifeCycle = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDefaultLcState(self) -> "LifeCycleState":
        """
        AUTOSAR-compliant getter for defaultLcState.
        
        Returns:
            The defaultLcState value
        
        Note:
            Delegates to default_lc_state property (CODING_RULE_V2_00017)
        """
        return self.default_lc_state  # Delegates to property

    def setDefaultLcState(self, value: "LifeCycleState") -> "LifeCycleInfoSet":
        """
        AUTOSAR-compliant setter for defaultLcState with method chaining.
        
        Args:
            value: The defaultLcState to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to default_lc_state property setter (gets validation automatically)
        """
        self.default_lc_state = value  # Delegates to property setter
        return self

    def getDefaultPeriod(self) -> "LifeCyclePeriod":
        """
        AUTOSAR-compliant getter for defaultPeriod.
        
        Returns:
            The defaultPeriod value
        
        Note:
            Delegates to default_period property (CODING_RULE_V2_00017)
        """
        return self.default_period  # Delegates to property

    def setDefaultPeriod(self, value: "LifeCyclePeriod") -> "LifeCycleInfoSet":
        """
        AUTOSAR-compliant setter for defaultPeriod with method chaining.
        
        Args:
            value: The defaultPeriod to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to default_period property setter (gets validation automatically)
        """
        self.default_period = value  # Delegates to property setter
        return self

    def getLifeCycleInfo(self) -> List["LifeCycleInfo"]:
        """
        AUTOSAR-compliant getter for lifeCycleInfo.
        
        Returns:
            The lifeCycleInfo value
        
        Note:
            Delegates to life_cycle_info property (CODING_RULE_V2_00017)
        """
        return self.life_cycle_info  # Delegates to property

    def getUsedLifeCycle(self) -> "LifeCycleStateDefinition":
        """
        AUTOSAR-compliant getter for usedLifeCycle.
        
        Returns:
            The usedLifeCycle value
        
        Note:
            Delegates to used_life_cycle property (CODING_RULE_V2_00017)
        """
        return self.used_life_cycle  # Delegates to property

    def setUsedLifeCycle(self, value: "LifeCycleStateDefinition") -> "LifeCycleInfoSet":
        """
        AUTOSAR-compliant setter for usedLifeCycle with method chaining.
        
        Args:
            value: The usedLifeCycle to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to used_life_cycle property setter (gets validation automatically)
        """
        self.used_life_cycle = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_default_lc_state(self, value: "LifeCycleState") -> "LifeCycleInfoSet":
        """
        Set defaultLcState and return self for chaining.
        
        Args:
            value: The defaultLcState to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_default_lc_state("value")
        """
        self.default_lc_state = value  # Use property setter (gets validation)
        return self

    def with_default_period(self, value: Optional["LifeCyclePeriod"]) -> "LifeCycleInfoSet":
        """
        Set defaultPeriod and return self for chaining.
        
        Args:
            value: The defaultPeriod to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_default_period("value")
        """
        self.default_period = value  # Use property setter (gets validation)
        return self

    def with_used_life_cycle(self, value: "LifeCycleStateDefinition") -> "LifeCycleInfoSet":
        """
        Set usedLifeCycle and return self for chaining.
        
        Args:
            value: The usedLifeCycle to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_used_life_cycle("value")
        """
        self.used_life_cycle = value  # Use property setter (gets validation)
        return self



class LifeCyclePeriod(ARObject):
    """
    This meta class represents the ability to specify a point of time within a
    specified period, e.g. the starting or end point, in which a specific life
    cycle state is valid/applies to.
    
    Package: M2::AUTOSARTemplates::GenericStructure::LifeCycles::LifeCyclePeriod
    
    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 392, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Version of the AUTOSAR Release the element referred to part of.
        # contains three levels (major, minor, are defined by AUTOSAR.
        self._arRelease: Optional["RevisionLabelString"] = None

    @property
    def ar_release(self) -> Optional["RevisionLabelString"]:
        """Get arRelease (Pythonic accessor)."""
        return self._arRelease

    @ar_release.setter
    def ar_release(self, value: Optional["RevisionLabelString"]) -> None:
        """
        Set arRelease with validation.
        
        Args:
            value: The arRelease to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._arRelease = None
            return

        if not isinstance(value, RevisionLabelString):
            raise TypeError(
                f"arRelease must be RevisionLabelString or None, got {type(value).__name__}"
            )
        self._arRelease = value
        # Date within period.
        self._date: Optional["DateTime"] = None

    @property
    def date(self) -> Optional["DateTime"]:
        """Get date (Pythonic accessor)."""
        return self._date

    @date.setter
    def date(self, value: Optional["DateTime"]) -> None:
        """
        Set date with validation.
        
        Args:
            value: The date to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._date = None
            return

        if not isinstance(value, DateTime):
            raise TypeError(
                f"date must be DateTime or None, got {type(value).__name__}"
            )
        self._date = value
        # Version of the product within the period.
        self._productRelease: Optional["RevisionLabelString"] = None

    @property
    def product_release(self) -> Optional["RevisionLabelString"]:
        """Get productRelease (Pythonic accessor)."""
        return self._productRelease

    @product_release.setter
    def product_release(self, value: Optional["RevisionLabelString"]) -> None:
        """
        Set productRelease with validation.
        
        Args:
            value: The productRelease to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._productRelease = None
            return

        if not isinstance(value, RevisionLabelString):
            raise TypeError(
                f"productRelease must be RevisionLabelString or None, got {type(value).__name__}"
            )
        self._productRelease = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getArRelease(self) -> "RevisionLabelString":
        """
        AUTOSAR-compliant getter for arRelease.
        
        Returns:
            The arRelease value
        
        Note:
            Delegates to ar_release property (CODING_RULE_V2_00017)
        """
        return self.ar_release  # Delegates to property

    def setArRelease(self, value: "RevisionLabelString") -> "LifeCyclePeriod":
        """
        AUTOSAR-compliant setter for arRelease with method chaining.
        
        Args:
            value: The arRelease to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to ar_release property setter (gets validation automatically)
        """
        self.ar_release = value  # Delegates to property setter
        return self

    def getDate(self) -> "DateTime":
        """
        AUTOSAR-compliant getter for date.
        
        Returns:
            The date value
        
        Note:
            Delegates to date property (CODING_RULE_V2_00017)
        """
        return self.date  # Delegates to property

    def setDate(self, value: "DateTime") -> "LifeCyclePeriod":
        """
        AUTOSAR-compliant setter for date with method chaining.
        
        Args:
            value: The date to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to date property setter (gets validation automatically)
        """
        self.date = value  # Delegates to property setter
        return self

    def getProductRelease(self) -> "RevisionLabelString":
        """
        AUTOSAR-compliant getter for productRelease.
        
        Returns:
            The productRelease value
        
        Note:
            Delegates to product_release property (CODING_RULE_V2_00017)
        """
        return self.product_release  # Delegates to property

    def setProductRelease(self, value: "RevisionLabelString") -> "LifeCyclePeriod":
        """
        AUTOSAR-compliant setter for productRelease with method chaining.
        
        Args:
            value: The productRelease to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to product_release property setter (gets validation automatically)
        """
        self.product_release = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_ar_release(self, value: Optional["RevisionLabelString"]) -> "LifeCyclePeriod":
        """
        Set arRelease and return self for chaining.
        
        Args:
            value: The arRelease to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_ar_release("value")
        """
        self.ar_release = value  # Use property setter (gets validation)
        return self

    def with_date(self, value: Optional["DateTime"]) -> "LifeCyclePeriod":
        """
        Set date and return self for chaining.
        
        Args:
            value: The date to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_date("value")
        """
        self.date = value  # Use property setter (gets validation)
        return self

    def with_product_release(self, value: Optional["RevisionLabelString"]) -> "LifeCyclePeriod":
        """
        Set productRelease and return self for chaining.
        
        Args:
            value: The productRelease to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_product_release("value")
        """
        self.product_release = value  # Use property setter (gets validation)
        return self



class LifeCycleInfo(ARObject):
    """
    LifeCycleInfo describes the life cycle state of an element together with
    additional information like what to use instead
    
    Package: M2::AUTOSARTemplates::GenericStructure::LifeCycles::LifeCycleInfo
    
    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 392, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 195, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Element(s) have the life cycle as described in lcState.
        self._lcObject: "RefType" = None

    @property
    def lc_object(self) -> "RefType":
        """Get lcObject (Pythonic accessor)."""
        return self._lcObject

    @lc_object.setter
    def lc_object(self, value: "RefType") -> None:
        """
        Set lcObject with validation.
        
        Args:
            value: The lcObject to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        self._lcObject = value
        # This denotes the particular state assigned to the object.
        # If is given then the default life cycle state of Life assumed.
        self._lcState: Optional["LifeCycleState"] = None

    @property
    def lc_state(self) -> Optional["LifeCycleState"]:
        """Get lcState (Pythonic accessor)."""
        return self._lcState

    @lc_state.setter
    def lc_state(self, value: Optional["LifeCycleState"]) -> None:
        """
        Set lcState with validation.
        
        Args:
            value: The lcState to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._lcState = None
            return

        if not isinstance(value, LifeCycleState):
            raise TypeError(
                f"lcState must be LifeCycleState or None, got {type(value).__name__}"
            )
        self._lcState = value
        # Starting point of period in which the element has the cycle state lcState.
        # If no periodBegin is given default period begin of LifeCycleInfoSet is 535
                # Document ID 202: AUTOSAR_FO_TPS_GenericStructureTemplate Template R23-11.
        self._periodBegin: Optional["LifeCyclePeriod"] = None

    @property
    def period_begin(self) -> Optional["LifeCyclePeriod"]:
        """Get periodBegin (Pythonic accessor)."""
        return self._periodBegin

    @period_begin.setter
    def period_begin(self, value: Optional["LifeCyclePeriod"]) -> None:
        """
        Set periodBegin with validation.
        
        Args:
            value: The periodBegin to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._periodBegin = None
            return

        if not isinstance(value, LifeCyclePeriod):
            raise TypeError(
                f"periodBegin must be LifeCyclePeriod or None, got {type(value).__name__}"
            )
        self._periodBegin = value
        # Expiry date, i.
        # e.
        # end point of period the element does not denoted life cycle state lcState any
                # more.
        # If no given then the default period begin of Life assumed.
        self._periodEnd: Optional["LifeCyclePeriod"] = None

    @property
    def period_end(self) -> Optional["LifeCyclePeriod"]:
        """Get periodEnd (Pythonic accessor)."""
        return self._periodEnd

    @period_end.setter
    def period_end(self, value: Optional["LifeCyclePeriod"]) -> None:
        """
        Set periodEnd with validation.
        
        Args:
            value: The periodEnd to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._periodEnd = None
            return

        if not isinstance(value, LifeCyclePeriod):
            raise TypeError(
                f"periodEnd must be LifeCyclePeriod or None, got {type(value).__name__}"
            )
        self._periodEnd = value
        # Remark describing for example the element was given the specified life cycle
        # semantics of useInstead.
        self._remark: Optional["DocumentationBlock"] = None

    @property
    def remark(self) -> Optional["DocumentationBlock"]:
        """Get remark (Pythonic accessor)."""
        return self._remark

    @remark.setter
    def remark(self, value: Optional["DocumentationBlock"]) -> None:
        """
        Set remark with validation.
        
        Args:
            value: The remark to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._remark = None
            return

        if not isinstance(value, DocumentationBlock):
            raise TypeError(
                f"remark must be DocumentationBlock or None, got {type(value).__name__}"
            )
        self._remark = value
        # Element(s) that should be used instead of the one referrable.
        # in case of life cycle states lcState unlike case there are multiple
                # references the exact be individually described in the remark.
        self._useInstead: List["RefType"] = []

    @property
    def use_instead(self) -> List["RefType"]:
        """Get useInstead (Pythonic accessor)."""
        return self._useInstead

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getLcObject(self) -> "RefType":
        """
        AUTOSAR-compliant getter for lcObject.
        
        Returns:
            The lcObject value
        
        Note:
            Delegates to lc_object property (CODING_RULE_V2_00017)
        """
        return self.lc_object  # Delegates to property

    def setLcObject(self, value: "RefType") -> "LifeCycleInfo":
        """
        AUTOSAR-compliant setter for lcObject with method chaining.
        
        Args:
            value: The lcObject to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to lc_object property setter (gets validation automatically)
        """
        self.lc_object = value  # Delegates to property setter
        return self

    def getLcState(self) -> "LifeCycleState":
        """
        AUTOSAR-compliant getter for lcState.
        
        Returns:
            The lcState value
        
        Note:
            Delegates to lc_state property (CODING_RULE_V2_00017)
        """
        return self.lc_state  # Delegates to property

    def setLcState(self, value: "LifeCycleState") -> "LifeCycleInfo":
        """
        AUTOSAR-compliant setter for lcState with method chaining.
        
        Args:
            value: The lcState to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to lc_state property setter (gets validation automatically)
        """
        self.lc_state = value  # Delegates to property setter
        return self

    def getPeriodBegin(self) -> "LifeCyclePeriod":
        """
        AUTOSAR-compliant getter for periodBegin.
        
        Returns:
            The periodBegin value
        
        Note:
            Delegates to period_begin property (CODING_RULE_V2_00017)
        """
        return self.period_begin  # Delegates to property

    def setPeriodBegin(self, value: "LifeCyclePeriod") -> "LifeCycleInfo":
        """
        AUTOSAR-compliant setter for periodBegin with method chaining.
        
        Args:
            value: The periodBegin to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to period_begin property setter (gets validation automatically)
        """
        self.period_begin = value  # Delegates to property setter
        return self

    def getPeriodEnd(self) -> "LifeCyclePeriod":
        """
        AUTOSAR-compliant getter for periodEnd.
        
        Returns:
            The periodEnd value
        
        Note:
            Delegates to period_end property (CODING_RULE_V2_00017)
        """
        return self.period_end  # Delegates to property

    def setPeriodEnd(self, value: "LifeCyclePeriod") -> "LifeCycleInfo":
        """
        AUTOSAR-compliant setter for periodEnd with method chaining.
        
        Args:
            value: The periodEnd to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to period_end property setter (gets validation automatically)
        """
        self.period_end = value  # Delegates to property setter
        return self

    def getRemark(self) -> "DocumentationBlock":
        """
        AUTOSAR-compliant getter for remark.
        
        Returns:
            The remark value
        
        Note:
            Delegates to remark property (CODING_RULE_V2_00017)
        """
        return self.remark  # Delegates to property

    def setRemark(self, value: "DocumentationBlock") -> "LifeCycleInfo":
        """
        AUTOSAR-compliant setter for remark with method chaining.
        
        Args:
            value: The remark to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to remark property setter (gets validation automatically)
        """
        self.remark = value  # Delegates to property setter
        return self

    def getUseInstead(self) -> List["RefType"]:
        """
        AUTOSAR-compliant getter for useInstead.
        
        Returns:
            The useInstead value
        
        Note:
            Delegates to use_instead property (CODING_RULE_V2_00017)
        """
        return self.use_instead  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_lc_object(self, value: RefType) -> "LifeCycleInfo":
        """
        Set lcObject and return self for chaining.
        
        Args:
            value: The lcObject to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_lc_object("value")
        """
        self.lc_object = value  # Use property setter (gets validation)
        return self

    def with_lc_state(self, value: Optional["LifeCycleState"]) -> "LifeCycleInfo":
        """
        Set lcState and return self for chaining.
        
        Args:
            value: The lcState to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_lc_state("value")
        """
        self.lc_state = value  # Use property setter (gets validation)
        return self

    def with_period_begin(self, value: Optional["LifeCyclePeriod"]) -> "LifeCycleInfo":
        """
        Set periodBegin and return self for chaining.
        
        Args:
            value: The periodBegin to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_period_begin("value")
        """
        self.period_begin = value  # Use property setter (gets validation)
        return self

    def with_period_end(self, value: Optional["LifeCyclePeriod"]) -> "LifeCycleInfo":
        """
        Set periodEnd and return self for chaining.
        
        Args:
            value: The periodEnd to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_period_end("value")
        """
        self.period_end = value  # Use property setter (gets validation)
        return self

    def with_remark(self, value: Optional["DocumentationBlock"]) -> "LifeCycleInfo":
        """
        Set remark and return self for chaining.
        
        Args:
            value: The remark to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_remark("value")
        """
        self.remark = value  # Use property setter (gets validation)
        return self
"""
AUTOSAR Package - SwcBswMapping

Package: M2::AUTOSARTemplates::CommonStructure::SwcBswMapping
"""

from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARElement,
)


class SwcBswMapping(ARElement):
    """
    Maps an SwcInternalBehavior to an BswInternalBehavior. This is required to
    coordinate the API generation and the scheduling for AUTOSAR Service
    Components, ECU Abstraction Components and Complex Driver Components by the
    RTE and the BSW scheduling mechanisms.

    Package: M2::AUTOSARTemplates::CommonStructure::SwcBswMapping::SwcBswMapping

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 110, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 656, Classic Platform
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 217, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The mapped BswInternalBehavior.
        self._bswBehavior: Optional["BswInternalBehavior"] = None

    @property
    def bsw_behavior(self) -> Optional["BswInternalBehavior"]:
        """Get bswBehavior (Pythonic accessor)."""
        return self._bswBehavior

    @bsw_behavior.setter
    def bsw_behavior(self, value: Optional["BswInternalBehavior"]) -> None:
        """
        Set bswBehavior with validation.

        Args:
            value: The bswBehavior to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._bswBehavior = None
            return

        if not isinstance(value, BswInternalBehavior):
            raise TypeError(
                f"bswBehavior must be BswInternalBehavior or None, got {type(value).__name__}"
            )
        self._bswBehavior = value
        # Stereotypes: atpSplitable; atpVariation.
        self._runnable: List["SwcBswRunnable"] = []

    @property
    def runnable(self) -> List["SwcBswRunnable"]:
        """Get runnable (Pythonic accessor)."""
        return self._runnable
        # The mapped SwcInternalBehavior.
        self._swcBehavior: Optional["SwcInternalBehavior"] = None

    @property
    def swc_behavior(self) -> Optional["SwcInternalBehavior"]:
        """Get swcBehavior (Pythonic accessor)."""
        return self._swcBehavior

    @swc_behavior.setter
    def swc_behavior(self, value: Optional["SwcInternalBehavior"]) -> None:
        """
        Set swcBehavior with validation.

        Args:
            value: The swcBehavior to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swcBehavior = None
            return

        if not isinstance(value, SwcInternalBehavior):
            raise TypeError(
                f"swcBehavior must be SwcInternalBehavior or None, got {type(value).__name__}"
            )
        self._swcBehavior = value
        # atpVariation.
        self._synchronized: List["SwcBswSynchronized"] = []

    @property
    def synchronized(self) -> List["SwcBswSynchronized"]:
        """Get synchronized (Pythonic accessor)."""
        return self._synchronized

    def with_runnable(self, value):
        """
        Set runnable and return self for chaining.

        Args:
            value: The runnable to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_runnable("value")
        """
        self.runnable = value  # Use property setter (gets validation)
        return self

    def with_synchronized(self, value):
        """
        Set synchronized and return self for chaining.

        Args:
            value: The synchronized to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_synchronized("value")
        """
        self.synchronized = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBswBehavior(self) -> "BswInternalBehavior":
        """
        AUTOSAR-compliant getter for bswBehavior.

        Returns:
            The bswBehavior value

        Note:
            Delegates to bsw_behavior property (CODING_RULE_V2_00017)
        """
        return self.bsw_behavior  # Delegates to property

    def setBswBehavior(self, value: "BswInternalBehavior") -> "SwcBswMapping":
        """
        AUTOSAR-compliant setter for bswBehavior with method chaining.

        Args:
            value: The bswBehavior to set

        Returns:
            self for method chaining

        Note:
            Delegates to bsw_behavior property setter (gets validation automatically)
        """
        self.bsw_behavior = value  # Delegates to property setter
        return self

    def getRunnable(self) -> List["SwcBswRunnable"]:
        """
        AUTOSAR-compliant getter for runnable.

        Returns:
            The runnable value

        Note:
            Delegates to runnable property (CODING_RULE_V2_00017)
        """
        return self.runnable  # Delegates to property

    def getSwcBehavior(self) -> "SwcInternalBehavior":
        """
        AUTOSAR-compliant getter for swcBehavior.

        Returns:
            The swcBehavior value

        Note:
            Delegates to swc_behavior property (CODING_RULE_V2_00017)
        """
        return self.swc_behavior  # Delegates to property

    def setSwcBehavior(self, value: "SwcInternalBehavior") -> "SwcBswMapping":
        """
        AUTOSAR-compliant setter for swcBehavior with method chaining.

        Args:
            value: The swcBehavior to set

        Returns:
            self for method chaining

        Note:
            Delegates to swc_behavior property setter (gets validation automatically)
        """
        self.swc_behavior = value  # Delegates to property setter
        return self

    def getSynchronized(self) -> List["SwcBswSynchronized"]:
        """
        AUTOSAR-compliant getter for synchronized.

        Returns:
            The synchronized value

        Note:
            Delegates to synchronized property (CODING_RULE_V2_00017)
        """
        return self.synchronized  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_bsw_behavior(self, value: Optional["BswInternalBehavior"]) -> "SwcBswMapping":
        """
        Set bswBehavior and return self for chaining.

        Args:
            value: The bswBehavior to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_bsw_behavior("value")
        """
        self.bsw_behavior = value  # Use property setter (gets validation)
        return self

    def with_swc_behavior(self, value: Optional["SwcInternalBehavior"]) -> "SwcBswMapping":
        """
        Set swcBehavior and return self for chaining.

        Args:
            value: The swcBehavior to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_swc_behavior("value")
        """
        self.swc_behavior = value  # Use property setter (gets validation)
        return self



class SwcBswRunnableMapping(ARObject):
    """
    Maps a BswModuleEntity to a RunnableEntity if it is implemented as part of a
    BSW module (in the case of an AUTOSAR Service, a Complex Driver or an ECU
    Abstraction). The mapping can be used by a tool to find relevant information
    on the behavior, e.g. whether the bswEntity shall be running in interrupt
    context.

    Package: M2::AUTOSARTemplates::CommonStructure::SwcBswMapping::SwcBswRunnableMapping

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 110, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The mapped BswModuleEntity.
        self._bswEntity: Optional["BswModuleEntity"] = None

    @property
    def bsw_entity(self) -> Optional["BswModuleEntity"]:
        """Get bswEntity (Pythonic accessor)."""
        return self._bswEntity

    @bsw_entity.setter
    def bsw_entity(self, value: Optional["BswModuleEntity"]) -> None:
        """
        Set bswEntity with validation.

        Args:
            value: The bswEntity to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._bswEntity = None
            return

        if not isinstance(value, BswModuleEntity):
            raise TypeError(
                f"bswEntity must be BswModuleEntity or None, got {type(value).__name__}"
            )
        self._bswEntity = value
        self._swcRunnable: Optional["RunnableEntity"] = None

    @property
    def swc_runnable(self) -> Optional["RunnableEntity"]:
        """Get swcRunnable (Pythonic accessor)."""
        return self._swcRunnable

    @swc_runnable.setter
    def swc_runnable(self, value: Optional["RunnableEntity"]) -> None:
        """
        Set swcRunnable with validation.

        Args:
            value: The swcRunnable to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swcRunnable = None
            return

        if not isinstance(value, RunnableEntity):
            raise TypeError(
                f"swcRunnable must be RunnableEntity or None, got {type(value).__name__}"
            )
        self._swcRunnable = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBswEntity(self) -> "BswModuleEntity":
        """
        AUTOSAR-compliant getter for bswEntity.

        Returns:
            The bswEntity value

        Note:
            Delegates to bsw_entity property (CODING_RULE_V2_00017)
        """
        return self.bsw_entity  # Delegates to property

    def setBswEntity(self, value: "BswModuleEntity") -> "SwcBswRunnableMapping":
        """
        AUTOSAR-compliant setter for bswEntity with method chaining.

        Args:
            value: The bswEntity to set

        Returns:
            self for method chaining

        Note:
            Delegates to bsw_entity property setter (gets validation automatically)
        """
        self.bsw_entity = value  # Delegates to property setter
        return self

    def getSwcRunnable(self) -> "RunnableEntity":
        """
        AUTOSAR-compliant getter for swcRunnable.

        Returns:
            The swcRunnable value

        Note:
            Delegates to swc_runnable property (CODING_RULE_V2_00017)
        """
        return self.swc_runnable  # Delegates to property

    def setSwcRunnable(self, value: "RunnableEntity") -> "SwcBswRunnableMapping":
        """
        AUTOSAR-compliant setter for swcRunnable with method chaining.

        Args:
            value: The swcRunnable to set

        Returns:
            self for method chaining

        Note:
            Delegates to swc_runnable property setter (gets validation automatically)
        """
        self.swc_runnable = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_bsw_entity(self, value: Optional["BswModuleEntity"]) -> "SwcBswRunnableMapping":
        """
        Set bswEntity and return self for chaining.

        Args:
            value: The bswEntity to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_bsw_entity("value")
        """
        self.bsw_entity = value  # Use property setter (gets validation)
        return self

    def with_swc_runnable(self, value: Optional["RunnableEntity"]) -> "SwcBswRunnableMapping":
        """
        Set swcRunnable and return self for chaining.

        Args:
            value: The swcRunnable to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_swc_runnable("value")
        """
        self.swc_runnable = value  # Use property setter (gets validation)
        return self



class SwcBswSynchronizedModeGroupPrototype(ARObject):
    """
    Synchronizes a mode group provided by a component via a port with a mode
    group provided by a BSW module or cluster.

    Package: M2::AUTOSARTemplates::CommonStructure::SwcBswMapping::SwcBswSynchronizedModeGroupPrototype

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 111, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The BSW mode group prototype.
        self._bswModeGroupPrototype: Optional["RefType"] = None

    @property
    def bsw_mode_group_prototype(self) -> Optional["RefType"]:
        """Get bswModeGroupPrototype (Pythonic accessor)."""
        return self._bswModeGroupPrototype

    @bsw_mode_group_prototype.setter
    def bsw_mode_group_prototype(self, value: Optional["RefType"]) -> None:
        """
        Set bswModeGroupPrototype with validation.

        Args:
            value: The bswModeGroupPrototype to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._bswModeGroupPrototype = None
            return

        self._bswModeGroupPrototype = value
        self._swcModeGroupSwcInstanceRef: Optional["RefType"] = None

    @property
    def swc_mode_group_swc_instance_ref(self) -> Optional["RefType"]:
        """Get swcModeGroupSwcInstanceRef (Pythonic accessor)."""
        return self._swcModeGroupSwcInstanceRef

    @swc_mode_group_swc_instance_ref.setter
    def swc_mode_group_swc_instance_ref(self, value: Optional["RefType"]) -> None:
        """
        Set swcModeGroupSwcInstanceRef with validation.

        Args:
            value: The swcModeGroupSwcInstanceRef to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swcModeGroupSwcInstanceRef = None
            return

        self._swcModeGroupSwcInstanceRef = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBswModeGroupPrototype(self) -> "RefType":
        """
        AUTOSAR-compliant getter for bswModeGroupPrototype.

        Returns:
            The bswModeGroupPrototype value

        Note:
            Delegates to bsw_mode_group_prototype property (CODING_RULE_V2_00017)
        """
        return self.bsw_mode_group_prototype  # Delegates to property

    def setBswModeGroupPrototype(self, value: "RefType") -> "SwcBswSynchronizedModeGroupPrototype":
        """
        AUTOSAR-compliant setter for bswModeGroupPrototype with method chaining.

        Args:
            value: The bswModeGroupPrototype to set

        Returns:
            self for method chaining

        Note:
            Delegates to bsw_mode_group_prototype property setter (gets validation automatically)
        """
        self.bsw_mode_group_prototype = value  # Delegates to property setter
        return self

    def getSwcModeGroupSwcInstanceRef(self) -> "RefType":
        """
        AUTOSAR-compliant getter for swcModeGroupSwcInstanceRef.

        Returns:
            The swcModeGroupSwcInstanceRef value

        Note:
            Delegates to swc_mode_group_swc_instance_ref property (CODING_RULE_V2_00017)
        """
        return self.swc_mode_group_swc_instance_ref  # Delegates to property

    def setSwcModeGroupSwcInstanceRef(self, value: "RefType") -> "SwcBswSynchronizedModeGroupPrototype":
        """
        AUTOSAR-compliant setter for swcModeGroupSwcInstanceRef with method chaining.

        Args:
            value: The swcModeGroupSwcInstanceRef to set

        Returns:
            self for method chaining

        Note:
            Delegates to swc_mode_group_swc_instance_ref property setter (gets validation automatically)
        """
        self.swc_mode_group_swc_instance_ref = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_bsw_mode_group_prototype(self, value: Optional[RefType]) -> "SwcBswSynchronizedModeGroupPrototype":
        """
        Set bswModeGroupPrototype and return self for chaining.

        Args:
            value: The bswModeGroupPrototype to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_bsw_mode_group_prototype("value")
        """
        self.bsw_mode_group_prototype = value  # Use property setter (gets validation)
        return self

    def with_swc_mode_group_swc_instance_ref(self, value: Optional[RefType]) -> "SwcBswSynchronizedModeGroupPrototype":
        """
        Set swcModeGroupSwcInstanceRef and return self for chaining.

        Args:
            value: The swcModeGroupSwcInstanceRef to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_swc_mode_group_swc_instance_ref("value")
        """
        self.swc_mode_group_swc_instance_ref = value  # Use property setter (gets validation)
        return self



class SwcBswSynchronizedTrigger(ARObject):
    """
    Synchronizes a Trigger provided by a component via a port with a Trigger
    provided by a BSW module or cluster.

    Package: M2::AUTOSARTemplates::CommonStructure::SwcBswMapping::SwcBswSynchronizedTrigger

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 111, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The BSW Trigger.
        self._bswTrigger: Optional["RefType"] = None

    @property
    def bsw_trigger(self) -> Optional["RefType"]:
        """Get bswTrigger (Pythonic accessor)."""
        return self._bswTrigger

    @bsw_trigger.setter
    def bsw_trigger(self, value: Optional["RefType"]) -> None:
        """
        Set bswTrigger with validation.

        Args:
            value: The bswTrigger to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._bswTrigger = None
            return

        self._bswTrigger = value
        self._swcTriggerTypeInstanceRef: Optional["RefType"] = None

    @property
    def swc_trigger_type_instance_ref(self) -> Optional["RefType"]:
        """Get swcTriggerTypeInstanceRef (Pythonic accessor)."""
        return self._swcTriggerTypeInstanceRef

    @swc_trigger_type_instance_ref.setter
    def swc_trigger_type_instance_ref(self, value: Optional["RefType"]) -> None:
        """
        Set swcTriggerTypeInstanceRef with validation.

        Args:
            value: The swcTriggerTypeInstanceRef to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swcTriggerTypeInstanceRef = None
            return

        self._swcTriggerTypeInstanceRef = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBswTrigger(self) -> "RefType":
        """
        AUTOSAR-compliant getter for bswTrigger.

        Returns:
            The bswTrigger value

        Note:
            Delegates to bsw_trigger property (CODING_RULE_V2_00017)
        """
        return self.bsw_trigger  # Delegates to property

    def setBswTrigger(self, value: "RefType") -> "SwcBswSynchronizedTrigger":
        """
        AUTOSAR-compliant setter for bswTrigger with method chaining.

        Args:
            value: The bswTrigger to set

        Returns:
            self for method chaining

        Note:
            Delegates to bsw_trigger property setter (gets validation automatically)
        """
        self.bsw_trigger = value  # Delegates to property setter
        return self

    def getSwcTriggerTypeInstanceRef(self) -> "RefType":
        """
        AUTOSAR-compliant getter for swcTriggerTypeInstanceRef.

        Returns:
            The swcTriggerTypeInstanceRef value

        Note:
            Delegates to swc_trigger_type_instance_ref property (CODING_RULE_V2_00017)
        """
        return self.swc_trigger_type_instance_ref  # Delegates to property

    def setSwcTriggerTypeInstanceRef(self, value: "RefType") -> "SwcBswSynchronizedTrigger":
        """
        AUTOSAR-compliant setter for swcTriggerTypeInstanceRef with method chaining.

        Args:
            value: The swcTriggerTypeInstanceRef to set

        Returns:
            self for method chaining

        Note:
            Delegates to swc_trigger_type_instance_ref property setter (gets validation automatically)
        """
        self.swc_trigger_type_instance_ref = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_bsw_trigger(self, value: Optional[RefType]) -> "SwcBswSynchronizedTrigger":
        """
        Set bswTrigger and return self for chaining.

        Args:
            value: The bswTrigger to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_bsw_trigger("value")
        """
        self.bsw_trigger = value  # Use property setter (gets validation)
        return self

    def with_swc_trigger_type_instance_ref(self, value: Optional[RefType]) -> "SwcBswSynchronizedTrigger":
        """
        Set swcTriggerTypeInstanceRef and return self for chaining.

        Args:
            value: The swcTriggerTypeInstanceRef to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_swc_trigger_type_instance_ref("value")
        """
        self.swc_trigger_type_instance_ref = value  # Use property setter (gets validation)
        return self

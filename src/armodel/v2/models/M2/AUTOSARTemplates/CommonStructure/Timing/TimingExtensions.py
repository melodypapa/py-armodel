"""
AUTOSAR Package - TimingExtensions

Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingExtensions
"""


from __future__ import annotations

from abc import ABC
from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class TimingExtension(ARElement, ABC):
    """
    The abstract parent class of the different template specific timing
    extensions. Depending on the specific timing extension the timing
    descriptions and timing constraints, that can be used to specify the timing
    behavior, are restricted.

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingExtensions::TimingExtension

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 254, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is TimingExtension:
            raise TypeError("TimingExtension is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # A list of accuracies - which may be used to specify synchronizations from one
        # model clock to another model atpVariation.
        self._timingClock: List["TimingClockSync"] = []

    @property
    def timing_clock(self) -> List["TimingClockSync"]:
        """Get timingClock (Pythonic accessor)."""
        return self._timingClock
        # The timing condition specifies a specific condition.
        # atpVariation 277 Document ID 411: AUTOSAR_CP_TPS_TimingExtensions Timing
                # Extensions for Classic R23-11.
        self._timingCondition: List[TimingCondition] = []

    @property
    def timing_condition(self) -> List[TimingCondition]:
        """Get timingCondition (Pythonic accessor)."""
        return self._timingCondition
        # The timing constraints that belong to a specific timing in the role of a
                # timing requirement.
        # to support different timing constraint variants timing specification, the
                # aggregation is marked stereotype "atpVariation".
        # atpVariation.
        self._timing: List[TimingConstraint] = []

    @property
    def timing(self) -> List[TimingConstraint]:
        """Get timing (Pythonic accessor)."""
        return self._timing
        # The timing resource contains all instance references from within a timing
        # condition formula of a timing.
        self._timingResource: Optional[TimingExtension] = None

    @property
    def timing_resource(self) -> Optional[TimingExtension]:
        """Get timingResource (Pythonic accessor)."""
        return self._timingResource

    @timing_resource.setter
    def timing_resource(self, value: Optional[TimingExtension]) -> None:
        """
        Set timingResource with validation.

        Args:
            value: The timingResource to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timingResource = None
            return

        if not isinstance(value, TimingExtension):
            raise TypeError(
                f"timingResource must be TimingExtension or None, got {type(value).__name__}"
            )
        self._timingResource = value

    def with_timing_clock(self, value):
        """
        Set timing_clock and return self for chaining.

        Args:
            value: The timing_clock to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_timing_clock("value")
        """
        self.timing_clock = value  # Use property setter (gets validation)
        return self

    def with_timing_condition(self, value):
        """
        Set timing_condition and return self for chaining.

        Args:
            value: The timing_condition to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_timing_condition("value")
        """
        self.timing_condition = value  # Use property setter (gets validation)
        return self

    def with_timing(self, value):
        """
        Set timing and return self for chaining.

        Args:
            value: The timing to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_timing("value")
        """
        self.timing = value  # Use property setter (gets validation)
        return self

    def with_implementation(self, value):
        """
        Set implementation and return self for chaining.

        Args:
            value: The implementation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_implementation("value")
        """
        self.implementation = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTimingClock(self) -> List["TimingClockSync"]:
        """
        AUTOSAR-compliant getter for timingClock.

        Returns:
            The timingClock value

        Note:
            Delegates to timing_clock property (CODING_RULE_V2_00017)
        """
        return self.timing_clock  # Delegates to property

    def getTimingCondition(self) -> List[TimingCondition]:
        """
        AUTOSAR-compliant getter for timingCondition.

        Returns:
            The timingCondition value

        Note:
            Delegates to timing_condition property (CODING_RULE_V2_00017)
        """
        return self.timing_condition  # Delegates to property

    def getTiming(self) -> List[TimingConstraint]:
        """
        AUTOSAR-compliant getter for timing.

        Returns:
            The timing value

        Note:
            Delegates to timing property (CODING_RULE_V2_00017)
        """
        return self.timing  # Delegates to property

    def getTimingResource(self) -> TimingExtension:
        """
        AUTOSAR-compliant getter for timingResource.

        Returns:
            The timingResource value

        Note:
            Delegates to timing_resource property (CODING_RULE_V2_00017)
        """
        return self.timing_resource  # Delegates to property

    def setTimingResource(self, value: TimingExtension) -> TimingExtension:
        """
        AUTOSAR-compliant setter for timingResource with method chaining.

        Args:
            value: The timingResource to set

        Returns:
            self for method chaining

        Note:
            Delegates to timing_resource property setter (gets validation automatically)
        """
        self.timing_resource = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_timing_resource(self, value: Optional[TimingExtension]) -> TimingExtension:
        """
        Set timingResource and return self for chaining.

        Args:
            value: The timingResource to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_timing_resource("value")
        """
        self.timing_resource = value  # Use property setter (gets validation)
        return self



class VfbTiming(TimingExtension):
    """
    A model element used to define timing descriptions and constraints at VFB
    level. TimingDescriptions aggregated by VfbTiming are restricted to event
    chains referring to events which are derived from the class TDEventVfb.

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingExtensions::VfbTiming

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 24, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 223, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This defines the scope of a VfbTiming.
        # All corresponding and constraints shall be defined within.
        self._component: Optional["SwComponentType"] = None

    @property
    def component(self) -> Optional["SwComponentType"]:
        """Get component (Pythonic accessor)."""
        return self._component

    @component.setter
    def component(self, value: Optional["SwComponentType"]) -> None:
        """
        Set component with validation.

        Args:
            value: The component to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._component = None
            return

        if not isinstance(value, SwComponentType):
            raise TypeError(
                f"component must be SwComponentType or None, got {type(value).__name__}"
            )
        self._component = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getComponent(self) -> "SwComponentType":
        """
        AUTOSAR-compliant getter for component.

        Returns:
            The component value

        Note:
            Delegates to component property (CODING_RULE_V2_00017)
        """
        return self.component  # Delegates to property

    def setComponent(self, value: "SwComponentType") -> VfbTiming:
        """
        AUTOSAR-compliant setter for component with method chaining.

        Args:
            value: The component to set

        Returns:
            self for method chaining

        Note:
            Delegates to component property setter (gets validation automatically)
        """
        self.component = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_component(self, value: Optional["SwComponentType"]) -> VfbTiming:
        """
        Set component and return self for chaining.

        Args:
            value: The component to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_component("value")
        """
        self.component = value  # Use property setter (gets validation)
        return self



class SwcTiming(TimingExtension):
    """
    The SwcTiming is used to describe the timing of an atomic software
    component. TimingDescriptions aggregated by SwcTiming are restricted to
    event chains referring to events which are derived from the classes
    TDEventVfb and TDEventSwcInternalBehavior.

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingExtensions::SwcTiming

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 25, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This defines the scope of a SwcTiming.
        # All corresponding and constraints shall be defined within reason for the
                # cardinality of 0.
        # 1 is to ensure.
        self._behavior: Optional["SwcInternalBehavior"] = None

    @property
    def behavior(self) -> Optional["SwcInternalBehavior"]:
        """Get behavior (Pythonic accessor)."""
        return self._behavior

    @behavior.setter
    def behavior(self, value: Optional["SwcInternalBehavior"]) -> None:
        """
        Set behavior with validation.

        Args:
            value: The behavior to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._behavior = None
            return

        if not isinstance(value, SwcInternalBehavior):
            raise TypeError(
                f"behavior must be SwcInternalBehavior or None, got {type(value).__name__}"
            )
        self._behavior = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBehavior(self) -> "SwcInternalBehavior":
        """
        AUTOSAR-compliant getter for behavior.

        Returns:
            The behavior value

        Note:
            Delegates to behavior property (CODING_RULE_V2_00017)
        """
        return self.behavior  # Delegates to property

    def setBehavior(self, value: "SwcInternalBehavior") -> SwcTiming:
        """
        AUTOSAR-compliant setter for behavior with method chaining.

        Args:
            value: The behavior to set

        Returns:
            self for method chaining

        Note:
            Delegates to behavior property setter (gets validation automatically)
        """
        self.behavior = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_behavior(self, value: Optional["SwcInternalBehavior"]) -> SwcTiming:
        """
        Set behavior and return self for chaining.

        Args:
            value: The behavior to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_behavior("value")
        """
        self.behavior = value  # Use property setter (gets validation)
        return self



class SystemTiming(TimingExtension):
    """
    A model element used to refine timing descriptions and constraints (from a
    VfbTiming) at System level, utilizing information about topology, software
    deployment, and signal mapping described in the System Template.
    TimingDescriptions aggregated by SystemTiming are restricted to events which
    are derived from the class TDEventVfb, TDEventSwcInternalBehavior and
    TDEventCom.

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingExtensions::SystemTiming

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 26, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This defines the scope of a SystemTiming.
        # All descriptions and constraints shall within this scope.
        self._system: Optional["System"] = None

    @property
    def system(self) -> Optional["System"]:
        """Get system (Pythonic accessor)."""
        return self._system

    @system.setter
    def system(self, value: Optional["System"]) -> None:
        """
        Set system with validation.

        Args:
            value: The system to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._system = None
            return

        if not isinstance(value, System):
            raise TypeError(
                f"system must be System or None, got {type(value).__name__}"
            )
        self._system = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSystem(self) -> "System":
        """
        AUTOSAR-compliant getter for system.

        Returns:
            The system value

        Note:
            Delegates to system property (CODING_RULE_V2_00017)
        """
        return self.system  # Delegates to property

    def setSystem(self, value: "System") -> SystemTiming:
        """
        AUTOSAR-compliant setter for system with method chaining.

        Args:
            value: The system to set

        Returns:
            self for method chaining

        Note:
            Delegates to system property setter (gets validation automatically)
        """
        self.system = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_system(self, value: Optional["System"]) -> SystemTiming:
        """
        Set system and return self for chaining.

        Args:
            value: The system to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_system("value")
        """
        self.system = value  # Use property setter (gets validation)
        return self



class BswModuleTiming(TimingExtension):
    """
    A model element used to define timing descriptions and constraints for the
    BswInternalBehavior of one BSW Module. Thereby, for each BswInternalBehavior
    a separate timing can be specified. A constraint defined at this level holds
    true for all Implementations of that BswInternalBehavior. TimingDescriptions
    aggregated by BswModuleTiming are restricted to event chains referring to
    events which are derived from the class TDEventBswInternalBehavior.

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingExtensions::BswModuleTiming

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 28, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This defines the scope of a BswModuleTiming.
        # All descriptions and constraints shall within this scope.
        self._behavior: Optional["BswInternalBehavior"] = None

    @property
    def behavior(self) -> Optional["BswInternalBehavior"]:
        """Get behavior (Pythonic accessor)."""
        return self._behavior

    @behavior.setter
    def behavior(self, value: Optional["BswInternalBehavior"]) -> None:
        """
        Set behavior with validation.

        Args:
            value: The behavior to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._behavior = None
            return

        if not isinstance(value, BswInternalBehavior):
            raise TypeError(
                f"behavior must be BswInternalBehavior or None, got {type(value).__name__}"
            )
        self._behavior = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBehavior(self) -> "BswInternalBehavior":
        """
        AUTOSAR-compliant getter for behavior.

        Returns:
            The behavior value

        Note:
            Delegates to behavior property (CODING_RULE_V2_00017)
        """
        return self.behavior  # Delegates to property

    def setBehavior(self, value: "BswInternalBehavior") -> BswModuleTiming:
        """
        AUTOSAR-compliant setter for behavior with method chaining.

        Args:
            value: The behavior to set

        Returns:
            self for method chaining

        Note:
            Delegates to behavior property setter (gets validation automatically)
        """
        self.behavior = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_behavior(self, value: Optional["BswInternalBehavior"]) -> BswModuleTiming:
        """
        Set behavior and return self for chaining.

        Args:
            value: The behavior to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_behavior("value")
        """
        self.behavior = value  # Use property setter (gets validation)
        return self



class BswCompositionTiming(TimingExtension):
    """
    A model element used to define timing descriptions and constraints for a set
    of BswImplementations representing a BSW composition. A constraint defined
    at this level holds true for all referenced Bsw Implementations. Note, that
    multiple implementations of the same basic software module could be
    involved. TimingDescriptions aggregated by BswCompositionTiming are
    restricted to event chains referring to events which are derived from the
    class TDEventBswInternalBehavior and TDEventBsw. (cid:53) 28 of 277 Document
    ID 411: AUTOSAR_CP_TPS_TimingExtensions Specification of Timing Extensions
    for Classic Platform AUTOSAR CP R23-11 (cid:52)

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingExtensions::BswCompositionTiming

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 28, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This defines the scope of a BswCompositionTiming.
        # All descriptions and constraints shall within this scope.
        self._implementation: List[BswImplementation] = []

    @property
    def implementation(self) -> List[BswImplementation]:
        """Get implementation (Pythonic accessor)."""
        return self._implementation

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getImplementation(self) -> List[BswImplementation]:
        """
        AUTOSAR-compliant getter for implementation.

        Returns:
            The implementation value

        Note:
            Delegates to implementation property (CODING_RULE_V2_00017)
        """
        return self.implementation  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class EcuTiming(TimingExtension):
    """
    A model element used to define timing descriptions and constraints within
    the scope of one ECU configuration. TimingDescriptions aggregated by
    EcuTiming are allowed to use all events derived from the class Timing
    DescriptionEvent.

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingExtensions::EcuTiming

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 30, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This defines the scope of an EcuTiming.
        # All timing descriptions and constraints shall within this scope.
        self._ecu: Optional[RefType] = None

    @property
    def ecu(self) -> Optional[RefType]:
        """Get ecu (Pythonic accessor)."""
        return self._ecu

    @ecu.setter
    def ecu(self, value: Optional[RefType]) -> None:
        """
        Set ecu with validation.

        Args:
            value: The ecu to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ecu = None
            return

        self._ecu = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEcu(self) -> RefType:
        """
        AUTOSAR-compliant getter for ecu.

        Returns:
            The ecu value

        Note:
            Delegates to ecu property (CODING_RULE_V2_00017)
        """
        return self.ecu  # Delegates to property

    def setEcu(self, value: RefType) -> EcuTiming:
        """
        AUTOSAR-compliant setter for ecu with method chaining.

        Args:
            value: The ecu to set

        Returns:
            self for method chaining

        Note:
            Delegates to ecu property setter (gets validation automatically)
        """
        self.ecu = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_ecu(self, value: Optional[RefType]) -> EcuTiming:
        """
        Set ecu and return self for chaining.

        Args:
            value: The ecu to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ecu("value")
        """
        self.ecu = value  # Use property setter (gets validation)
        return self

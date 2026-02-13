"""
AUTOSAR Package - TimingDescription

Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingDescription::TimingDescription
"""


from __future__ import annotations
from abc import ABC
from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
    RefType,
)
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription import (
    TimingDescriptionEvent,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
)


class TDEventVfb(TimingDescriptionEvent, ABC):
    """
    This is the abstract parent class to describe timing events at Virtual
    Functional Bus (VFB) level.

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingDescription::TimingDescription::TDEventVfb

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 51, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is TDEventVfb:
            raise TypeError("TDEventVfb is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # implemented by: ComponentIn.
        self._componentCompositionInstanceRef: Optional[SwComponent] = None

    @property
    def component_composition_instance_ref(self) -> Optional[SwComponent]:
        """Get componentCompositionInstanceRef (Pythonic accessor)."""
        return self._componentCompositionInstanceRef

    @component_composition_instance_ref.setter
    def component_composition_instance_ref(self, value: Optional[SwComponent]) -> None:
        """
        Set componentCompositionInstanceRef with validation.

        Args:
            value: The componentCompositionInstanceRef to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._componentCompositionInstanceRef = None
            return

        if not isinstance(value, SwComponent):
            raise TypeError(
                f"componentCompositionInstanceRef must be SwComponent or None, got {type(value).__name__}"
            )
        self._componentCompositionInstanceRef = value

    def with_td_header_id_filter(self, value):
        """
        Set td_header_id_filter and return self for chaining.

        Args:
            value: The td_header_id_filter to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_td_header_id_filter("value")
        """
        self.td_header_id_filter = value  # Use property setter (gets validation)
        return self

    def with_td_pdu_triggering(self, value):
        """
        Set td_pdu_triggering and return self for chaining.

        Args:
            value: The td_pdu_triggering to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_td_pdu_triggering("value")
        """
        self.td_pdu_triggering = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getComponentCompositionInstanceRef(self) -> SwComponent:
        """
        AUTOSAR-compliant getter for componentCompositionInstanceRef.

        Returns:
            The componentCompositionInstanceRef value

        Note:
            Delegates to component_composition_instance_ref property (CODING_RULE_V2_00017)
        """
        return self.component_composition_instance_ref  # Delegates to property

    def setComponentCompositionInstanceRef(self, value: SwComponent) -> TDEventVfb:
        """
        AUTOSAR-compliant setter for componentCompositionInstanceRef with method chaining.

        Args:
            value: The componentCompositionInstanceRef to set

        Returns:
            self for method chaining

        Note:
            Delegates to component_composition_instance_ref property setter (gets validation automatically)
        """
        self.component_composition_instance_ref = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_component_composition_instance_ref(self, value: Optional[SwComponent]) -> TDEventVfb:
        """
        Set componentCompositionInstanceRef and return self for chaining.

        Args:
            value: The componentCompositionInstanceRef to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_component_composition_instance_ref("value")
        """
        self.component_composition_instance_ref = value  # Use property setter (gets validation)
        return self



class TDEventSwc(TimingDescriptionEvent, ABC):
    """
    This is the abstract parent class to describe timing events at Software
    Component (SW-C) level.

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingDescription::TimingDescription::TDEventSwc

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 60, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is TDEventSwc:
            raise TypeError("TDEventSwc is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # implemented by: ComponentIn.
        self._componentCompositionInstanceRef: Optional[SwComponent] = None

    @property
    def component_composition_instance_ref(self) -> Optional[SwComponent]:
        """Get componentCompositionInstanceRef (Pythonic accessor)."""
        return self._componentCompositionInstanceRef

    @component_composition_instance_ref.setter
    def component_composition_instance_ref(self, value: Optional[SwComponent]) -> None:
        """
        Set componentCompositionInstanceRef with validation.

        Args:
            value: The componentCompositionInstanceRef to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._componentCompositionInstanceRef = None
            return

        if not isinstance(value, SwComponent):
            raise TypeError(
                f"componentCompositionInstanceRef must be SwComponent or None, got {type(value).__name__}"
            )
        self._componentCompositionInstanceRef = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getComponentCompositionInstanceRef(self) -> SwComponent:
        """
        AUTOSAR-compliant getter for componentCompositionInstanceRef.

        Returns:
            The componentCompositionInstanceRef value

        Note:
            Delegates to component_composition_instance_ref property (CODING_RULE_V2_00017)
        """
        return self.component_composition_instance_ref  # Delegates to property

    def setComponentCompositionInstanceRef(self, value: SwComponent) -> TDEventSwc:
        """
        AUTOSAR-compliant setter for componentCompositionInstanceRef with method chaining.

        Args:
            value: The componentCompositionInstanceRef to set

        Returns:
            self for method chaining

        Note:
            Delegates to component_composition_instance_ref property setter (gets validation automatically)
        """
        self.component_composition_instance_ref = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_component_composition_instance_ref(self, value: Optional[SwComponent]) -> TDEventSwc:
        """
        Set componentCompositionInstanceRef and return self for chaining.

        Args:
            value: The componentCompositionInstanceRef to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_component_composition_instance_ref("value")
        """
        self.component_composition_instance_ref = value  # Use property setter (gets validation)
        return self



class TDEventCom(TimingDescriptionEvent, ABC):
    """
    This is the abstract parent class to describe timing events related to
    communication including the physical layer.

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingDescription::TimingDescription::TDEventCom

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 65, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is TDEventCom:
            raise TypeError("TDEventCom is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The ECU context for a particular timing event.
        # The link is the EcuInstance can not be defined for type TDEventCycleStart.
        self._ecuInstance: Optional[EcuInstance] = None

    @property
    def ecu_instance(self) -> Optional[EcuInstance]:
        """Get ecuInstance (Pythonic accessor)."""
        return self._ecuInstance

    @ecu_instance.setter
    def ecu_instance(self, value: Optional[EcuInstance]) -> None:
        """
        Set ecuInstance with validation.

        Args:
            value: The ecuInstance to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ecuInstance = None
            return

        if not isinstance(value, EcuInstance):
            raise TypeError(
                f"ecuInstance must be EcuInstance or None, got {type(value).__name__}"
            )
        self._ecuInstance = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEcuInstance(self) -> EcuInstance:
        """
        AUTOSAR-compliant getter for ecuInstance.

        Returns:
            The ecuInstance value

        Note:
            Delegates to ecu_instance property (CODING_RULE_V2_00017)
        """
        return self.ecu_instance  # Delegates to property

    def setEcuInstance(self, value: EcuInstance) -> TDEventCom:
        """
        AUTOSAR-compliant setter for ecuInstance with method chaining.

        Args:
            value: The ecuInstance to set

        Returns:
            self for method chaining

        Note:
            Delegates to ecu_instance property setter (gets validation automatically)
        """
        self.ecu_instance = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_ecu_instance(self, value: Optional[EcuInstance]) -> TDEventCom:
        """
        Set ecuInstance and return self for chaining.

        Args:
            value: The ecuInstance to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ecu_instance("value")
        """
        self.ecu_instance = value  # Use property setter (gets validation)
        return self



class TDHeaderIdRange(ARObject):
    """
    Specifies a range of PDU header identifiers. This range is specified by a
    minimum and maximum header identifier; and the maximum header identifier
    shall be greater than or equal the minimum header identifier.

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingDescription::TimingDescription::TDHeaderIdRange

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 70, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specifies the maximum PDU header identifier, in other upper bound of a range
        # of PDU header.
        self._maxHeaderId: Optional[Integer] = None

    @property
    def max_header_id(self) -> Optional[Integer]:
        """Get maxHeaderId (Pythonic accessor)."""
        return self._maxHeaderId

    @max_header_id.setter
    def max_header_id(self, value: Optional[Integer]) -> None:
        """
        Set maxHeaderId with validation.

        Args:
            value: The maxHeaderId to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxHeaderId = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"maxHeaderId must be Integer or int or None, got {type(value).__name__}"
            )
        self._maxHeaderId = value
        # of PDU header.
        self._minHeaderId: Optional[Integer] = None

    @property
    def min_header_id(self) -> Optional[Integer]:
        """Get minHeaderId (Pythonic accessor)."""
        return self._minHeaderId

    @min_header_id.setter
    def min_header_id(self, value: Optional[Integer]) -> None:
        """
        Set minHeaderId with validation.

        Args:
            value: The minHeaderId to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._minHeaderId = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"minHeaderId must be Integer or int or None, got {type(value).__name__}"
            )
        self._minHeaderId = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMaxHeaderId(self) -> Integer:
        """
        AUTOSAR-compliant getter for maxHeaderId.

        Returns:
            The maxHeaderId value

        Note:
            Delegates to max_header_id property (CODING_RULE_V2_00017)
        """
        return self.max_header_id  # Delegates to property

    def setMaxHeaderId(self, value: Integer) -> TDHeaderIdRange:
        """
        AUTOSAR-compliant setter for maxHeaderId with method chaining.

        Args:
            value: The maxHeaderId to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_header_id property setter (gets validation automatically)
        """
        self.max_header_id = value  # Delegates to property setter
        return self

    def getMinHeaderId(self) -> Integer:
        """
        AUTOSAR-compliant getter for minHeaderId.

        Returns:
            The minHeaderId value

        Note:
            Delegates to min_header_id property (CODING_RULE_V2_00017)
        """
        return self.min_header_id  # Delegates to property

    def setMinHeaderId(self, value: Integer) -> TDHeaderIdRange:
        """
        AUTOSAR-compliant setter for minHeaderId with method chaining.

        Args:
            value: The minHeaderId to set

        Returns:
            self for method chaining

        Note:
            Delegates to min_header_id property setter (gets validation automatically)
        """
        self.min_header_id = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_max_header_id(self, value: Optional[Integer]) -> TDHeaderIdRange:
        """
        Set maxHeaderId and return self for chaining.

        Args:
            value: The maxHeaderId to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_header_id("value")
        """
        self.max_header_id = value  # Use property setter (gets validation)
        return self

    def with_min_header_id(self, value: Optional[Integer]) -> TDHeaderIdRange:
        """
        Set minHeaderId and return self for chaining.

        Args:
            value: The minHeaderId to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_min_header_id("value")
        """
        self.min_header_id = value  # Use property setter (gets validation)
        return self



class TDEventBswInternalBehavior(TimingDescriptionEvent):
    """
    This is used to describe timing events related to the BswInternalBehavior of
    a BSW module.

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingDescription::TimingDescription::TDEventBswInternalBehavior

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 73, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The scope of this timing event.
        self._bswModuleEntity: Optional[BswModuleEntity] = None

    @property
    def bsw_module_entity(self) -> Optional[BswModuleEntity]:
        """Get bswModuleEntity (Pythonic accessor)."""
        return self._bswModuleEntity

    @bsw_module_entity.setter
    def bsw_module_entity(self, value: Optional[BswModuleEntity]) -> None:
        """
        Set bswModuleEntity with validation.

        Args:
            value: The bswModuleEntity to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._bswModuleEntity = None
            return

        if not isinstance(value, BswModuleEntity):
            raise TypeError(
                f"bswModuleEntity must be BswModuleEntity or None, got {type(value).__name__}"
            )
        self._bswModuleEntity = value
        self._tdEventBswBehaviorType: Optional["TDEventBswInternal"] = None

    @property
    def td_event_bsw_behavior_type(self) -> Optional["TDEventBswInternal"]:
        """Get tdEventBswBehaviorType (Pythonic accessor)."""
        return self._tdEventBswBehaviorType

    @td_event_bsw_behavior_type.setter
    def td_event_bsw_behavior_type(self, value: Optional["TDEventBswInternal"]) -> None:
        """
        Set tdEventBswBehaviorType with validation.

        Args:
            value: The tdEventBswBehaviorType to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tdEventBswBehaviorType = None
            return

        if not isinstance(value, TDEventBswInternal):
            raise TypeError(
                f"tdEventBswBehaviorType must be TDEventBswInternal or None, got {type(value).__name__}"
            )
        self._tdEventBswBehaviorType = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBswModuleEntity(self) -> BswModuleEntity:
        """
        AUTOSAR-compliant getter for bswModuleEntity.

        Returns:
            The bswModuleEntity value

        Note:
            Delegates to bsw_module_entity property (CODING_RULE_V2_00017)
        """
        return self.bsw_module_entity  # Delegates to property

    def setBswModuleEntity(self, value: BswModuleEntity) -> TDEventBswInternalBehavior:
        """
        AUTOSAR-compliant setter for bswModuleEntity with method chaining.

        Args:
            value: The bswModuleEntity to set

        Returns:
            self for method chaining

        Note:
            Delegates to bsw_module_entity property setter (gets validation automatically)
        """
        self.bsw_module_entity = value  # Delegates to property setter
        return self

    def getTdEventBswBehaviorType(self) -> "TDEventBswInternal":
        """
        AUTOSAR-compliant getter for tdEventBswBehaviorType.

        Returns:
            The tdEventBswBehaviorType value

        Note:
            Delegates to td_event_bsw_behavior_type property (CODING_RULE_V2_00017)
        """
        return self.td_event_bsw_behavior_type  # Delegates to property

    def setTdEventBswBehaviorType(self, value: "TDEventBswInternal") -> TDEventBswInternalBehavior:
        """
        AUTOSAR-compliant setter for tdEventBswBehaviorType with method chaining.

        Args:
            value: The tdEventBswBehaviorType to set

        Returns:
            self for method chaining

        Note:
            Delegates to td_event_bsw_behavior_type property setter (gets validation automatically)
        """
        self.td_event_bsw_behavior_type = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_bsw_module_entity(self, value: Optional[BswModuleEntity]) -> TDEventBswInternalBehavior:
        """
        Set bswModuleEntity and return self for chaining.

        Args:
            value: The bswModuleEntity to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_bsw_module_entity("value")
        """
        self.bsw_module_entity = value  # Use property setter (gets validation)
        return self

    def with_td_event_bsw_behavior_type(self, value: Optional["TDEventBswInternal"]) -> TDEventBswInternalBehavior:
        """
        Set tdEventBswBehaviorType and return self for chaining.

        Args:
            value: The tdEventBswBehaviorType to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_td_event_bsw_behavior_type("value")
        """
        self.td_event_bsw_behavior_type = value  # Use property setter (gets validation)
        return self



class TDEventComplex(TimingDescriptionEvent):
    """
    This is used to describe complex timing events. The context of a complex
    timing event either is described informally, e.g. using the documentation
    block, or is described formally by the associated
    TDEventOccurrenceExpression.

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingDescription::TimingDescription::TDEventComplex

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 78, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class TDEventOccurrenceExpression(ARObject):
    """
    This is used to specify a filter on the occurrences of
    TimingDescriptionEvents by means of a TDEventOccurrenceExpressionFormula.
    Filter criteria can be variable and argument values, i.e. the timing event
    only occurs for specific values, as well as the temporal characteristics of
    the occurrences of arbitrary timing events.

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingDescription::TimingDescription::TDEventOccurrenceExpression

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 84, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # An occurrence expression can reference an arbitrary of
        # OperationArgumentPrototypes in its association aggregates instance
        # OperationArgumentPrototypes which can in the expression.
        self._argument: List[AutosarOperation] = []

    @property
    def argument(self) -> List[AutosarOperation]:
        """Get argument (Pythonic accessor)."""
        return self._argument
        # This is the expression formula which is used to describe occurrence
        # expression.
        self._formula: Optional["TDEventOccurrence"] = None

    @property
    def formula(self) -> Optional["TDEventOccurrence"]:
        """Get formula (Pythonic accessor)."""
        return self._formula

    @formula.setter
    def formula(self, value: Optional["TDEventOccurrence"]) -> None:
        """
        Set formula with validation.

        Args:
            value: The formula to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._formula = None
            return

        if not isinstance(value, TDEventOccurrence):
            raise TypeError(
                f"formula must be TDEventOccurrence or None, got {type(value).__name__}"
            )
        self._formula = value
                # its expression.
        # This instance references to Mode can be referenced in the expression.
        self._mode: List["TimingModeInstance"] = []

    @property
    def mode(self) -> List["TimingModeInstance"]:
        """Get mode (Pythonic accessor)."""
        return self._mode
        # An occurrence expression can reference an arbitrary of VariableDataPrototypes
                # in its expression.
        # This instance references to Variable can be referenced in the.
        self._variable: List[AutosarVariable] = []

    @property
    def variable(self) -> List[AutosarVariable]:
        """Get variable (Pythonic accessor)."""
        return self._variable

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getArgument(self) -> List[AutosarOperation]:
        """
        AUTOSAR-compliant getter for argument.

        Returns:
            The argument value

        Note:
            Delegates to argument property (CODING_RULE_V2_00017)
        """
        return self.argument  # Delegates to property

    def getFormula(self) -> "TDEventOccurrence":
        """
        AUTOSAR-compliant getter for formula.

        Returns:
            The formula value

        Note:
            Delegates to formula property (CODING_RULE_V2_00017)
        """
        return self.formula  # Delegates to property

    def setFormula(self, value: "TDEventOccurrence") -> TDEventOccurrenceExpression:
        """
        AUTOSAR-compliant setter for formula with method chaining.

        Args:
            value: The formula to set

        Returns:
            self for method chaining

        Note:
            Delegates to formula property setter (gets validation automatically)
        """
        self.formula = value  # Delegates to property setter
        return self

    def getMode(self) -> List["TimingModeInstance"]:
        """
        AUTOSAR-compliant getter for mode.

        Returns:
            The mode value

        Note:
            Delegates to mode property (CODING_RULE_V2_00017)
        """
        return self.mode  # Delegates to property

    def getVariable(self) -> List[AutosarVariable]:
        """
        AUTOSAR-compliant getter for variable.

        Returns:
            The variable value

        Note:
            Delegates to variable property (CODING_RULE_V2_00017)
        """
        return self.variable  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_formula(self, value: Optional["TDEventOccurrence"]) -> TDEventOccurrenceExpression:
        """
        Set formula and return self for chaining.

        Args:
            value: The formula to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_formula("value")
        """
        self.formula = value  # Use property setter (gets validation)
        return self



class TDEventOccurrenceExpressionFormula(ARObject):
    """
    This is an extension of the FormulaExpression for the AUTOSAR Timing
    Extensions. A TDEventOccurrenceExpressionFormula provides the means to
    express the temporal characteristics of timing event occurrences in
    correlation with specific variable and argument values. The formal
    definition of the extended functions (ExtUnaryFunctions) is described in
    detail in the AUTOSAR Timing Extensions.

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingDescription::TimingDescription::TDEventOccurrenceExpressionFormula

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 84, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is one particular argument value used in the formula.
        self._argument: Optional[AutosarOperation] = None

    @property
    def argument(self) -> Optional[AutosarOperation]:
        """Get argument (Pythonic accessor)."""
        return self._argument

    @argument.setter
    def argument(self, value: Optional[AutosarOperation]) -> None:
        """
        Set argument with validation.

        Args:
            value: The argument to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._argument = None
            return

        if not isinstance(value, AutosarOperation):
            raise TypeError(
                f"argument must be AutosarOperation or None, got {type(value).__name__}"
            )
        self._argument = value
        self._event: Optional[TimingDescriptionEvent] = None

    @property
    def event(self) -> Optional[TimingDescriptionEvent]:
        """Get event (Pythonic accessor)."""
        return self._event

    @event.setter
    def event(self, value: Optional[TimingDescriptionEvent]) -> None:
        """
        Set event with validation.

        Args:
            value: The event to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._event = None
            return

        if not isinstance(value, TimingDescriptionEvent):
            raise TypeError(
                f"event must be TimingDescriptionEvent or None, got {type(value).__name__}"
            )
        self._event = value
        self._mode: Optional["TimingModeInstance"] = None

    @property
    def mode(self) -> Optional["TimingModeInstance"]:
        """Get mode (Pythonic accessor)."""
        return self._mode

    @mode.setter
    def mode(self, value: Optional["TimingModeInstance"]) -> None:
        """
        Set mode with validation.

        Args:
            value: The mode to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._mode = None
            return

        if not isinstance(value, TimingModeInstance):
            raise TypeError(
                f"mode must be TimingModeInstance or None, got {type(value).__name__}"
            )
        self._mode = value
        self._variable: Optional[AutosarVariable] = None

    @property
    def variable(self) -> Optional[AutosarVariable]:
        """Get variable (Pythonic accessor)."""
        return self._variable

    @variable.setter
    def variable(self, value: Optional[AutosarVariable]) -> None:
        """
        Set variable with validation.

        Args:
            value: The variable to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._variable = None
            return

        if not isinstance(value, AutosarVariable):
            raise TypeError(
                f"variable must be AutosarVariable or None, got {type(value).__name__}"
            )
        self._variable = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getArgument(self) -> AutosarOperation:
        """
        AUTOSAR-compliant getter for argument.

        Returns:
            The argument value

        Note:
            Delegates to argument property (CODING_RULE_V2_00017)
        """
        return self.argument  # Delegates to property

    def setArgument(self, value: AutosarOperation) -> TDEventOccurrenceExpressionFormula:
        """
        AUTOSAR-compliant setter for argument with method chaining.

        Args:
            value: The argument to set

        Returns:
            self for method chaining

        Note:
            Delegates to argument property setter (gets validation automatically)
        """
        self.argument = value  # Delegates to property setter
        return self

    def getEvent(self) -> TimingDescriptionEvent:
        """
        AUTOSAR-compliant getter for event.

        Returns:
            The event value

        Note:
            Delegates to event property (CODING_RULE_V2_00017)
        """
        return self.event  # Delegates to property

    def setEvent(self, value: TimingDescriptionEvent) -> TDEventOccurrenceExpressionFormula:
        """
        AUTOSAR-compliant setter for event with method chaining.

        Args:
            value: The event to set

        Returns:
            self for method chaining

        Note:
            Delegates to event property setter (gets validation automatically)
        """
        self.event = value  # Delegates to property setter
        return self

    def getMode(self) -> "TimingModeInstance":
        """
        AUTOSAR-compliant getter for mode.

        Returns:
            The mode value

        Note:
            Delegates to mode property (CODING_RULE_V2_00017)
        """
        return self.mode  # Delegates to property

    def setMode(self, value: "TimingModeInstance") -> TDEventOccurrenceExpressionFormula:
        """
        AUTOSAR-compliant setter for mode with method chaining.

        Args:
            value: The mode to set

        Returns:
            self for method chaining

        Note:
            Delegates to mode property setter (gets validation automatically)
        """
        self.mode = value  # Delegates to property setter
        return self

    def getVariable(self) -> AutosarVariable:
        """
        AUTOSAR-compliant getter for variable.

        Returns:
            The variable value

        Note:
            Delegates to variable property (CODING_RULE_V2_00017)
        """
        return self.variable  # Delegates to property

    def setVariable(self, value: AutosarVariable) -> TDEventOccurrenceExpressionFormula:
        """
        AUTOSAR-compliant setter for variable with method chaining.

        Args:
            value: The variable to set

        Returns:
            self for method chaining

        Note:
            Delegates to variable property setter (gets validation automatically)
        """
        self.variable = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_argument(self, value: Optional[AutosarOperation]) -> TDEventOccurrenceExpressionFormula:
        """
        Set argument and return self for chaining.

        Args:
            value: The argument to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_argument("value")
        """
        self.argument = value  # Use property setter (gets validation)
        return self

    def with_event(self, value: Optional[TimingDescriptionEvent]) -> TDEventOccurrenceExpressionFormula:
        """
        Set event and return self for chaining.

        Args:
            value: The event to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_event("value")
        """
        self.event = value  # Use property setter (gets validation)
        return self

    def with_mode(self, value: Optional["TimingModeInstance"]) -> TDEventOccurrenceExpressionFormula:
        """
        Set mode and return self for chaining.

        Args:
            value: The mode to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mode("value")
        """
        self.mode = value  # Use property setter (gets validation)
        return self

    def with_variable(self, value: Optional[AutosarVariable]) -> TDEventOccurrenceExpressionFormula:
        """
        Set variable and return self for chaining.

        Args:
            value: The variable to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_variable("value")
        """
        self.variable = value  # Use property setter (gets validation)
        return self



class AutosarVariableInstance(Identifiable):
    """
    This class represents a reference to a variable instance within AUTOSAR.
    This way it is possible to reference a variable instance in the occurrence
    expression formula. The variable instance can target to one of the following
    variables: • a variable provided via a PortPrototype as whole • an element
    inside of a composite variable provided via a PortPrototype

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingDescription::TimingDescription::AutosarVariableInstance

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 85, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # by: VariableInComponent.
        self._variableInstanceInstanceRef: Optional[RefType] = None

    @property
    def variable_instance_instance_ref(self) -> Optional[RefType]:
        """Get variableInstanceInstanceRef (Pythonic accessor)."""
        return self._variableInstanceInstanceRef

    @variable_instance_instance_ref.setter
    def variable_instance_instance_ref(self, value: Optional[RefType]) -> None:
        """
        Set variableInstanceInstanceRef with validation.

        Args:
            value: The variableInstanceInstanceRef to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._variableInstanceInstanceRef = None
            return

        self._variableInstanceInstanceRef = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getVariableInstanceInstanceRef(self) -> RefType:
        """
        AUTOSAR-compliant getter for variableInstanceInstanceRef.

        Returns:
            The variableInstanceInstanceRef value

        Note:
            Delegates to variable_instance_instance_ref property (CODING_RULE_V2_00017)
        """
        return self.variable_instance_instance_ref  # Delegates to property

    def setVariableInstanceInstanceRef(self, value: RefType) -> AutosarVariableInstance:
        """
        AUTOSAR-compliant setter for variableInstanceInstanceRef with method chaining.

        Args:
            value: The variableInstanceInstanceRef to set

        Returns:
            self for method chaining

        Note:
            Delegates to variable_instance_instance_ref property setter (gets validation automatically)
        """
        self.variable_instance_instance_ref = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_variable_instance_instance_ref(self, value: Optional[RefType]) -> AutosarVariableInstance:
        """
        Set variableInstanceInstanceRef and return self for chaining.

        Args:
            value: The variableInstanceInstanceRef to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_variable_instance_instance_ref("value")
        """
        self.variable_instance_instance_ref = value  # Use property setter (gets validation)
        return self



class AutosarOperationArgumentInstance(Identifiable):
    """
    This class represents a reference to an argument instance. This way it is
    possible to reference an argument instance in the occurrence expression
    formula. The argument instance can target to one of the following arguments:
    • a whole argument used in an operation of a PortPrototype with
    ClientServerInterface • an element inside of a composite argument used in an
    operation of a PortPrototype with ClientServer Interface

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingDescription::TimingDescription::AutosarOperationArgumentInstance

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 85, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # implemented by: OperationArgumentIn Instance ComponentInstanceRef.
        self._operation: Optional[RefType] = None

    @property
    def operation(self) -> Optional[RefType]:
        """Get operation (Pythonic accessor)."""
        return self._operation

    @operation.setter
    def operation(self, value: Optional[RefType]) -> None:
        """
        Set operation with validation.

        Args:
            value: The operation to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._operation = None
            return

        self._operation = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getOperation(self) -> RefType:
        """
        AUTOSAR-compliant getter for operation.

        Returns:
            The operation value

        Note:
            Delegates to operation property (CODING_RULE_V2_00017)
        """
        return self.operation  # Delegates to property

    def setOperation(self, value: RefType) -> AutosarOperationArgumentInstance:
        """
        AUTOSAR-compliant setter for operation with method chaining.

        Args:
            value: The operation to set

        Returns:
            self for method chaining

        Note:
            Delegates to operation property setter (gets validation automatically)
        """
        self.operation = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_operation(self, value: Optional[RefType]) -> AutosarOperationArgumentInstance:
        """
        Set operation and return self for chaining.

        Args:
            value: The operation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_operation("value")
        """
        self.operation = value  # Use property setter (gets validation)
        return self



class TDEventBsw(TimingDescriptionEvent, ABC):
    """
    This is used to describe timing events related to BSW modules.

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingDescription::TimingDescription::TDEventBsw

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 251, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is TDEventBsw:
            raise TypeError("TDEventBsw is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The scope of this timing event.
        self._bswModuleDescription: Optional[BswModuleDescription] = None

    @property
    def bsw_module_description(self) -> Optional[BswModuleDescription]:
        """Get bswModuleDescription (Pythonic accessor)."""
        return self._bswModuleDescription

    @bsw_module_description.setter
    def bsw_module_description(self, value: Optional[BswModuleDescription]) -> None:
        """
        Set bswModuleDescription with validation.

        Args:
            value: The bswModuleDescription to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._bswModuleDescription = None
            return

        if not isinstance(value, BswModuleDescription):
            raise TypeError(
                f"bswModuleDescription must be BswModuleDescription or None, got {type(value).__name__}"
            )
        self._bswModuleDescription = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBswModuleDescription(self) -> BswModuleDescription:
        """
        AUTOSAR-compliant getter for bswModuleDescription.

        Returns:
            The bswModuleDescription value

        Note:
            Delegates to bsw_module_description property (CODING_RULE_V2_00017)
        """
        return self.bsw_module_description  # Delegates to property

    def setBswModuleDescription(self, value: BswModuleDescription) -> TDEventBsw:
        """
        AUTOSAR-compliant setter for bswModuleDescription with method chaining.

        Args:
            value: The bswModuleDescription to set

        Returns:
            self for method chaining

        Note:
            Delegates to bsw_module_description property setter (gets validation automatically)
        """
        self.bsw_module_description = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_bsw_module_description(self, value: Optional[BswModuleDescription]) -> TDEventBsw:
        """
        Set bswModuleDescription and return self for chaining.

        Args:
            value: The bswModuleDescription to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_bsw_module_description("value")
        """
        self.bsw_module_description = value  # Use property setter (gets validation)
        return self



class TDEventSLLET(TimingDescriptionEvent, ABC):
    """
    Used to describe SL-LET (System-Level) timing events.

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingDescription::TimingDescription::TDEventSLLET

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 251, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is TDEventSLLET:
            raise TypeError("TDEventSLLET is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class TDEventVfbReference(TDEventVfb):
    """
    This is used to reference timing description events related to the Virtual
    Functional Bus (VFB) view which are specified in other timing views.

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingDescription::TimingDescription::TDEventVfbReference

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 52, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The referenced timing description event.
        self._referencedTDEventVfb: Optional[TDEventVfb] = None

    @property
    def referenced_td_event_vfb(self) -> Optional[TDEventVfb]:
        """Get referencedTDEventVfb (Pythonic accessor)."""
        return self._referencedTDEventVfb

    @referenced_td_event_vfb.setter
    def referenced_td_event_vfb(self, value: Optional[TDEventVfb]) -> None:
        """
        Set referencedTDEventVfb with validation.

        Args:
            value: The referencedTDEventVfb to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._referencedTDEventVfb = None
            return

        if not isinstance(value, TDEventVfb):
            raise TypeError(
                f"referencedTDEventVfb must be TDEventVfb or None, got {type(value).__name__}"
            )
        self._referencedTDEventVfb = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getReferencedTDEventVfb(self) -> TDEventVfb:
        """
        AUTOSAR-compliant getter for referencedTDEventVfb.

        Returns:
            The referencedTDEventVfb value

        Note:
            Delegates to referenced_td_event_vfb property (CODING_RULE_V2_00017)
        """
        return self.referenced_td_event_vfb  # Delegates to property

    def setReferencedTDEventVfb(self, value: TDEventVfb) -> TDEventVfbReference:
        """
        AUTOSAR-compliant setter for referencedTDEventVfb with method chaining.

        Args:
            value: The referencedTDEventVfb to set

        Returns:
            self for method chaining

        Note:
            Delegates to referenced_td_event_vfb property setter (gets validation automatically)
        """
        self.referenced_td_event_vfb = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_referenced_td_event_vfb(self, value: Optional[TDEventVfb]) -> TDEventVfbReference:
        """
        Set referencedTDEventVfb and return self for chaining.

        Args:
            value: The referencedTDEventVfb to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_referenced_td_event_vfb("value")
        """
        self.referenced_td_event_vfb = value  # Use property setter (gets validation)
        return self



class TDEventVfbPort(TDEventVfb, ABC):
    """
    This is the abstract parent class to describe specific timing event types at
    Virtual Functional Bus (VFB) level.

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingDescription::TimingDescription::TDEventVfbPort

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 52, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 221, Foundation R23-11)
    """
    def __init__(self):
        if type(self) is TDEventVfbPort:
            raise TypeError("TDEventVfbPort is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute is used to refer to external events that are hardware I/O,
        # like physical sensors and Virtual Functional Bus (VFB) level.
        self._isExternal: Optional[Boolean] = None

    @property
    def is_external(self) -> Optional[Boolean]:
        """Get isExternal (Pythonic accessor)."""
        return self._isExternal

    @is_external.setter
    def is_external(self, value: Optional[Boolean]) -> None:
        """
        Set isExternal with validation.

        Args:
            value: The isExternal to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._isExternal = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"isExternal must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._isExternal = value
        self._port: Optional[RefType] = None

    @property
    def port(self) -> Optional[RefType]:
        """Get port (Pythonic accessor)."""
        return self._port

    @port.setter
    def port(self, value: Optional[RefType]) -> None:
        """
        Set port with validation.

        Args:
            value: The port to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._port = None
            return

        self._port = value
        # blueprint).
        self._portPrototype: Optional[RefType] = None

    @property
    def port_prototype(self) -> Optional[RefType]:
        """Get portPrototype (Pythonic accessor)."""
        return self._portPrototype

    @port_prototype.setter
    def port_prototype(self, value: Optional[RefType]) -> None:
        """
        Set portPrototype with validation.

        Args:
            value: The portPrototype to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._portPrototype = None
            return

        self._portPrototype = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getIsExternal(self) -> Boolean:
        """
        AUTOSAR-compliant getter for isExternal.

        Returns:
            The isExternal value

        Note:
            Delegates to is_external property (CODING_RULE_V2_00017)
        """
        return self.is_external  # Delegates to property

    def setIsExternal(self, value: Boolean) -> TDEventVfbPort:
        """
        AUTOSAR-compliant setter for isExternal with method chaining.

        Args:
            value: The isExternal to set

        Returns:
            self for method chaining

        Note:
            Delegates to is_external property setter (gets validation automatically)
        """
        self.is_external = value  # Delegates to property setter
        return self

    def getPort(self) -> RefType:
        """
        AUTOSAR-compliant getter for port.

        Returns:
            The port value

        Note:
            Delegates to port property (CODING_RULE_V2_00017)
        """
        return self.port  # Delegates to property

    def setPort(self, value: RefType) -> TDEventVfbPort:
        """
        AUTOSAR-compliant setter for port with method chaining.

        Args:
            value: The port to set

        Returns:
            self for method chaining

        Note:
            Delegates to port property setter (gets validation automatically)
        """
        self.port = value  # Delegates to property setter
        return self

    def getPortPrototype(self) -> RefType:
        """
        AUTOSAR-compliant getter for portPrototype.

        Returns:
            The portPrototype value

        Note:
            Delegates to port_prototype property (CODING_RULE_V2_00017)
        """
        return self.port_prototype  # Delegates to property

    def setPortPrototype(self, value: RefType) -> TDEventVfbPort:
        """
        AUTOSAR-compliant setter for portPrototype with method chaining.

        Args:
            value: The portPrototype to set

        Returns:
            self for method chaining

        Note:
            Delegates to port_prototype property setter (gets validation automatically)
        """
        self.port_prototype = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_is_external(self, value: Optional[Boolean]) -> TDEventVfbPort:
        """
        Set isExternal and return self for chaining.

        Args:
            value: The isExternal to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_is_external("value")
        """
        self.is_external = value  # Use property setter (gets validation)
        return self

    def with_port(self, value: Optional[RefType]) -> TDEventVfbPort:
        """
        Set port and return self for chaining.

        Args:
            value: The port to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_port("value")
        """
        self.port = value  # Use property setter (gets validation)
        return self

    def with_port_prototype(self, value: Optional[RefType]) -> TDEventVfbPort:
        """
        Set portPrototype and return self for chaining.

        Args:
            value: The portPrototype to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_port_prototype("value")
        """
        self.port_prototype = value  # Use property setter (gets validation)
        return self



class TDEventSwcInternalBehavior(TDEventSwc):
    """
    This is used to describe timing events related to the SwcInternalBehavior of
    an AtomicSwComponent Type.

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingDescription::TimingDescription::TDEventSwcInternalBehavior

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 61, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The scope of this timing event.
        # 277 Document ID 411: AUTOSAR_CP_TPS_TimingExtensions Timing Extensions for
                # Classic R23-11.
        self._runnable: Optional[RunnableEntity] = None

    @property
    def runnable(self) -> Optional[RunnableEntity]:
        """Get runnable (Pythonic accessor)."""
        return self._runnable

    @runnable.setter
    def runnable(self, value: Optional[RunnableEntity]) -> None:
        """
        Set runnable with validation.

        Args:
            value: The runnable to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._runnable = None
            return

        if not isinstance(value, RunnableEntity):
            raise TypeError(
                f"runnable must be RunnableEntity or None, got {type(value).__name__}"
            )
        self._runnable = value
        self._tdEventSwcBehaviorType: Optional["TDEventSwcInternal"] = None

    @property
    def td_event_swc_behavior_type(self) -> Optional["TDEventSwcInternal"]:
        """Get tdEventSwcBehaviorType (Pythonic accessor)."""
        return self._tdEventSwcBehaviorType

    @td_event_swc_behavior_type.setter
    def td_event_swc_behavior_type(self, value: Optional["TDEventSwcInternal"]) -> None:
        """
        Set tdEventSwcBehaviorType with validation.

        Args:
            value: The tdEventSwcBehaviorType to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tdEventSwcBehaviorType = None
            return

        if not isinstance(value, TDEventSwcInternal):
            raise TypeError(
                f"tdEventSwcBehaviorType must be TDEventSwcInternal or None, got {type(value).__name__}"
            )
        self._tdEventSwcBehaviorType = value
        self._variableAccess: Optional["VariableAccess"] = None

    @property
    def variable_access(self) -> Optional["VariableAccess"]:
        """Get variableAccess (Pythonic accessor)."""
        return self._variableAccess

    @variable_access.setter
    def variable_access(self, value: Optional["VariableAccess"]) -> None:
        """
        Set variableAccess with validation.

        Args:
            value: The variableAccess to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._variableAccess = None
            return

        if not isinstance(value, VariableAccess):
            raise TypeError(
                f"variableAccess must be VariableAccess or None, got {type(value).__name__}"
            )
        self._variableAccess = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getRunnable(self) -> RunnableEntity:
        """
        AUTOSAR-compliant getter for runnable.

        Returns:
            The runnable value

        Note:
            Delegates to runnable property (CODING_RULE_V2_00017)
        """
        return self.runnable  # Delegates to property

    def setRunnable(self, value: RunnableEntity) -> TDEventSwcInternalBehavior:
        """
        AUTOSAR-compliant setter for runnable with method chaining.

        Args:
            value: The runnable to set

        Returns:
            self for method chaining

        Note:
            Delegates to runnable property setter (gets validation automatically)
        """
        self.runnable = value  # Delegates to property setter
        return self

    def getTdEventSwcBehaviorType(self) -> "TDEventSwcInternal":
        """
        AUTOSAR-compliant getter for tdEventSwcBehaviorType.

        Returns:
            The tdEventSwcBehaviorType value

        Note:
            Delegates to td_event_swc_behavior_type property (CODING_RULE_V2_00017)
        """
        return self.td_event_swc_behavior_type  # Delegates to property

    def setTdEventSwcBehaviorType(self, value: "TDEventSwcInternal") -> TDEventSwcInternalBehavior:
        """
        AUTOSAR-compliant setter for tdEventSwcBehaviorType with method chaining.

        Args:
            value: The tdEventSwcBehaviorType to set

        Returns:
            self for method chaining

        Note:
            Delegates to td_event_swc_behavior_type property setter (gets validation automatically)
        """
        self.td_event_swc_behavior_type = value  # Delegates to property setter
        return self

    def getVariableAccess(self) -> "VariableAccess":
        """
        AUTOSAR-compliant getter for variableAccess.

        Returns:
            The variableAccess value

        Note:
            Delegates to variable_access property (CODING_RULE_V2_00017)
        """
        return self.variable_access  # Delegates to property

    def setVariableAccess(self, value: "VariableAccess") -> TDEventSwcInternalBehavior:
        """
        AUTOSAR-compliant setter for variableAccess with method chaining.

        Args:
            value: The variableAccess to set

        Returns:
            self for method chaining

        Note:
            Delegates to variable_access property setter (gets validation automatically)
        """
        self.variable_access = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_runnable(self, value: Optional[RunnableEntity]) -> TDEventSwcInternalBehavior:
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

    def with_td_event_swc_behavior_type(self, value: Optional["TDEventSwcInternal"]) -> TDEventSwcInternalBehavior:
        """
        Set tdEventSwcBehaviorType and return self for chaining.

        Args:
            value: The tdEventSwcBehaviorType to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_td_event_swc_behavior_type("value")
        """
        self.td_event_swc_behavior_type = value  # Use property setter (gets validation)
        return self

    def with_variable_access(self, value: Optional["VariableAccess"]) -> TDEventSwcInternalBehavior:
        """
        Set variableAccess and return self for chaining.

        Args:
            value: The variableAccess to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_variable_access("value")
        """
        self.variable_access = value  # Use property setter (gets validation)
        return self



class TDEventSwcInternalBehaviorReference(TDEventSwc):
    """
    This is used to reference timing description events related to the Software
    Component (SW-C) view which are specified in other timing views.

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingDescription::TimingDescription::TDEventSwcInternalBehaviorReference

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 63, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The referenced timing description event.
        self._referencedTDEventSwc: Optional[TDEventSwc] = None

    @property
    def referenced_td_event_swc(self) -> Optional[TDEventSwc]:
        """Get referencedTDEventSwc (Pythonic accessor)."""
        return self._referencedTDEventSwc

    @referenced_td_event_swc.setter
    def referenced_td_event_swc(self, value: Optional[TDEventSwc]) -> None:
        """
        Set referencedTDEventSwc with validation.

        Args:
            value: The referencedTDEventSwc to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._referencedTDEventSwc = None
            return

        if not isinstance(value, TDEventSwc):
            raise TypeError(
                f"referencedTDEventSwc must be TDEventSwc or None, got {type(value).__name__}"
            )
        self._referencedTDEventSwc = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getReferencedTDEventSwc(self) -> TDEventSwc:
        """
        AUTOSAR-compliant getter for referencedTDEventSwc.

        Returns:
            The referencedTDEventSwc value

        Note:
            Delegates to referenced_td_event_swc property (CODING_RULE_V2_00017)
        """
        return self.referenced_td_event_swc  # Delegates to property

    def setReferencedTDEventSwc(self, value: TDEventSwc) -> TDEventSwcInternalBehaviorReference:
        """
        AUTOSAR-compliant setter for referencedTDEventSwc with method chaining.

        Args:
            value: The referencedTDEventSwc to set

        Returns:
            self for method chaining

        Note:
            Delegates to referenced_td_event_swc property setter (gets validation automatically)
        """
        self.referenced_td_event_swc = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_referenced_td_event_swc(self, value: Optional[TDEventSwc]) -> TDEventSwcInternalBehaviorReference:
        """
        Set referencedTDEventSwc and return self for chaining.

        Args:
            value: The referencedTDEventSwc to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_referenced_td_event_swc("value")
        """
        self.referenced_td_event_swc = value  # Use property setter (gets validation)
        return self



class TDEventISignal(TDEventCom):
    """
    This is used to describe timing events related to the exchange of I-Signals
    between COM and RTE.

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingDescription::TimingDescription::TDEventISignal

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 65, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The scope of this timing event.
        self._iSignal: Optional["ISignal"] = None

    @property
    def i_signal(self) -> Optional["ISignal"]:
        """Get iSignal (Pythonic accessor)."""
        return self._iSignal

    @i_signal.setter
    def i_signal(self, value: Optional["ISignal"]) -> None:
        """
        Set iSignal with validation.

        Args:
            value: The iSignal to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._iSignal = None
            return

        if not isinstance(value, ISignal):
            raise TypeError(
                f"iSignal must be ISignal or None, got {type(value).__name__}"
            )
        self._iSignal = value
        self._physical: Optional["PhysicalChannel"] = None

    @property
    def physical(self) -> Optional["PhysicalChannel"]:
        """Get physical (Pythonic accessor)."""
        return self._physical

    @physical.setter
    def physical(self, value: Optional["PhysicalChannel"]) -> None:
        """
        Set physical with validation.

        Args:
            value: The physical to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._physical = None
            return

        if not isinstance(value, PhysicalChannel):
            raise TypeError(
                f"physical must be PhysicalChannel or None, got {type(value).__name__}"
            )
        self._physical = value
        self._tdEventTypeEnum: Optional["TDEventISignalType"] = None

    @property
    def td_event_type_enum(self) -> Optional["TDEventISignalType"]:
        """Get tdEventTypeEnum (Pythonic accessor)."""
        return self._tdEventTypeEnum

    @td_event_type_enum.setter
    def td_event_type_enum(self, value: Optional["TDEventISignalType"]) -> None:
        """
        Set tdEventTypeEnum with validation.

        Args:
            value: The tdEventTypeEnum to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tdEventTypeEnum = None
            return

        if not isinstance(value, TDEventISignalType):
            raise TypeError(
                f"tdEventTypeEnum must be TDEventISignalType or None, got {type(value).__name__}"
            )
        self._tdEventTypeEnum = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getISignal(self) -> "ISignal":
        """
        AUTOSAR-compliant getter for iSignal.

        Returns:
            The iSignal value

        Note:
            Delegates to i_signal property (CODING_RULE_V2_00017)
        """
        return self.i_signal  # Delegates to property

    def setISignal(self, value: "ISignal") -> TDEventISignal:
        """
        AUTOSAR-compliant setter for iSignal with method chaining.

        Args:
            value: The iSignal to set

        Returns:
            self for method chaining

        Note:
            Delegates to i_signal property setter (gets validation automatically)
        """
        self.i_signal = value  # Delegates to property setter
        return self

    def getPhysical(self) -> "PhysicalChannel":
        """
        AUTOSAR-compliant getter for physical.

        Returns:
            The physical value

        Note:
            Delegates to physical property (CODING_RULE_V2_00017)
        """
        return self.physical  # Delegates to property

    def setPhysical(self, value: "PhysicalChannel") -> TDEventISignal:
        """
        AUTOSAR-compliant setter for physical with method chaining.

        Args:
            value: The physical to set

        Returns:
            self for method chaining

        Note:
            Delegates to physical property setter (gets validation automatically)
        """
        self.physical = value  # Delegates to property setter
        return self

    def getTdEventTypeEnum(self) -> "TDEventISignalType":
        """
        AUTOSAR-compliant getter for tdEventTypeEnum.

        Returns:
            The tdEventTypeEnum value

        Note:
            Delegates to td_event_type_enum property (CODING_RULE_V2_00017)
        """
        return self.td_event_type_enum  # Delegates to property

    def setTdEventTypeEnum(self, value: "TDEventISignalType") -> TDEventISignal:
        """
        AUTOSAR-compliant setter for tdEventTypeEnum with method chaining.

        Args:
            value: The tdEventTypeEnum to set

        Returns:
            self for method chaining

        Note:
            Delegates to td_event_type_enum property setter (gets validation automatically)
        """
        self.td_event_type_enum = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_i_signal(self, value: Optional["ISignal"]) -> TDEventISignal:
        """
        Set iSignal and return self for chaining.

        Args:
            value: The iSignal to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_i_signal("value")
        """
        self.i_signal = value  # Use property setter (gets validation)
        return self

    def with_physical(self, value: Optional["PhysicalChannel"]) -> TDEventISignal:
        """
        Set physical and return self for chaining.

        Args:
            value: The physical to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_physical("value")
        """
        self.physical = value  # Use property setter (gets validation)
        return self

    def with_td_event_type_enum(self, value: Optional["TDEventISignalType"]) -> TDEventISignal:
        """
        Set tdEventTypeEnum and return self for chaining.

        Args:
            value: The tdEventTypeEnum to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_td_event_type_enum("value")
        """
        self.td_event_type_enum = value  # Use property setter (gets validation)
        return self



class TDEventIPdu(TDEventCom):
    """
    This is used to describe timing events related to the exchange of I-PDUs
    between the bus specific (Flex Ray / CAN / LIN) Interface BSW module and
    COM.

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingDescription::TimingDescription::TDEventIPdu

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 66, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The scope of this timing event.
        self._iPdu: Optional["IPdu"] = None

    @property
    def i_pdu(self) -> Optional["IPdu"]:
        """Get iPdu (Pythonic accessor)."""
        return self._iPdu

    @i_pdu.setter
    def i_pdu(self, value: Optional["IPdu"]) -> None:
        """
        Set iPdu with validation.

        Args:
            value: The iPdu to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._iPdu = None
            return

        if not isinstance(value, IPdu):
            raise TypeError(
                f"iPdu must be IPdu or None, got {type(value).__name__}"
            )
        self._iPdu = value
        self._physical: Optional["PhysicalChannel"] = None

    @property
    def physical(self) -> Optional["PhysicalChannel"]:
        """Get physical (Pythonic accessor)."""
        return self._physical

    @physical.setter
    def physical(self, value: Optional["PhysicalChannel"]) -> None:
        """
        Set physical with validation.

        Args:
            value: The physical to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._physical = None
            return

        if not isinstance(value, PhysicalChannel):
            raise TypeError(
                f"physical must be PhysicalChannel or None, got {type(value).__name__}"
            )
        self._physical = value
        self._tdEventType: Optional[TDEventIPduTypeEnum] = None

    @property
    def td_event_type(self) -> Optional[TDEventIPduTypeEnum]:
        """Get tdEventType (Pythonic accessor)."""
        return self._tdEventType

    @td_event_type.setter
    def td_event_type(self, value: Optional[TDEventIPduTypeEnum]) -> None:
        """
        Set tdEventType with validation.

        Args:
            value: The tdEventType to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tdEventType = None
            return

        if not isinstance(value, TDEventIPduTypeEnum):
            raise TypeError(
                f"tdEventType must be TDEventIPduTypeEnum or None, got {type(value).__name__}"
            )
        self._tdEventType = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getIPdu(self) -> "IPdu":
        """
        AUTOSAR-compliant getter for iPdu.

        Returns:
            The iPdu value

        Note:
            Delegates to i_pdu property (CODING_RULE_V2_00017)
        """
        return self.i_pdu  # Delegates to property

    def setIPdu(self, value: "IPdu") -> TDEventIPdu:
        """
        AUTOSAR-compliant setter for iPdu with method chaining.

        Args:
            value: The iPdu to set

        Returns:
            self for method chaining

        Note:
            Delegates to i_pdu property setter (gets validation automatically)
        """
        self.i_pdu = value  # Delegates to property setter
        return self

    def getPhysical(self) -> "PhysicalChannel":
        """
        AUTOSAR-compliant getter for physical.

        Returns:
            The physical value

        Note:
            Delegates to physical property (CODING_RULE_V2_00017)
        """
        return self.physical  # Delegates to property

    def setPhysical(self, value: "PhysicalChannel") -> TDEventIPdu:
        """
        AUTOSAR-compliant setter for physical with method chaining.

        Args:
            value: The physical to set

        Returns:
            self for method chaining

        Note:
            Delegates to physical property setter (gets validation automatically)
        """
        self.physical = value  # Delegates to property setter
        return self

    def getTdEventType(self) -> TDEventIPduTypeEnum:
        """
        AUTOSAR-compliant getter for tdEventType.

        Returns:
            The tdEventType value

        Note:
            Delegates to td_event_type property (CODING_RULE_V2_00017)
        """
        return self.td_event_type  # Delegates to property

    def setTdEventType(self, value: TDEventIPduTypeEnum) -> TDEventIPdu:
        """
        AUTOSAR-compliant setter for tdEventType with method chaining.

        Args:
            value: The tdEventType to set

        Returns:
            self for method chaining

        Note:
            Delegates to td_event_type property setter (gets validation automatically)
        """
        self.td_event_type = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_i_pdu(self, value: Optional["IPdu"]) -> TDEventIPdu:
        """
        Set iPdu and return self for chaining.

        Args:
            value: The iPdu to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_i_pdu("value")
        """
        self.i_pdu = value  # Use property setter (gets validation)
        return self

    def with_physical(self, value: Optional["PhysicalChannel"]) -> TDEventIPdu:
        """
        Set physical and return self for chaining.

        Args:
            value: The physical to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_physical("value")
        """
        self.physical = value  # Use property setter (gets validation)
        return self

    def with_td_event_type(self, value: Optional[TDEventIPduTypeEnum]) -> TDEventIPdu:
        """
        Set tdEventType and return self for chaining.

        Args:
            value: The tdEventType to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_td_event_type("value")
        """
        self.td_event_type = value  # Use property setter (gets validation)
        return self



class TDEventFrame(TDEventCom):
    """
    This is used to describe timing events related to the exchange of frames
    between the communication controller and the bus specific (FlexRay / CAN /
    LIN) Interface BSW module.

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingDescription::TimingDescription::TDEventFrame

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 67, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The scope of this timing event.
        # 277 Document ID 411: AUTOSAR_CP_TPS_TimingExtensions Timing Extensions for
                # Classic R23-11.
        self._frame: Optional[Frame] = None

    @property
    def frame(self) -> Optional[Frame]:
        """Get frame (Pythonic accessor)."""
        return self._frame

    @frame.setter
    def frame(self, value: Optional[Frame]) -> None:
        """
        Set frame with validation.

        Args:
            value: The frame to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._frame = None
            return

        if not isinstance(value, Frame):
            raise TypeError(
                f"frame must be Frame or None, got {type(value).__name__}"
            )
        self._frame = value
        self._physical: Optional["PhysicalChannel"] = None

    @property
    def physical(self) -> Optional["PhysicalChannel"]:
        """Get physical (Pythonic accessor)."""
        return self._physical

    @physical.setter
    def physical(self, value: Optional["PhysicalChannel"]) -> None:
        """
        Set physical with validation.

        Args:
            value: The physical to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._physical = None
            return

        if not isinstance(value, PhysicalChannel):
            raise TypeError(
                f"physical must be PhysicalChannel or None, got {type(value).__name__}"
            )
        self._physical = value
        self._tdEventTypeEnum: Optional["TDEventFrameType"] = None

    @property
    def td_event_type_enum(self) -> Optional["TDEventFrameType"]:
        """Get tdEventTypeEnum (Pythonic accessor)."""
        return self._tdEventTypeEnum

    @td_event_type_enum.setter
    def td_event_type_enum(self, value: Optional["TDEventFrameType"]) -> None:
        """
        Set tdEventTypeEnum with validation.

        Args:
            value: The tdEventTypeEnum to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tdEventTypeEnum = None
            return

        if not isinstance(value, TDEventFrameType):
            raise TypeError(
                f"tdEventTypeEnum must be TDEventFrameType or None, got {type(value).__name__}"
            )
        self._tdEventTypeEnum = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getFrame(self) -> Frame:
        """
        AUTOSAR-compliant getter for frame.

        Returns:
            The frame value

        Note:
            Delegates to frame property (CODING_RULE_V2_00017)
        """
        return self.frame  # Delegates to property

    def setFrame(self, value: Frame) -> TDEventFrame:
        """
        AUTOSAR-compliant setter for frame with method chaining.

        Args:
            value: The frame to set

        Returns:
            self for method chaining

        Note:
            Delegates to frame property setter (gets validation automatically)
        """
        self.frame = value  # Delegates to property setter
        return self

    def getPhysical(self) -> "PhysicalChannel":
        """
        AUTOSAR-compliant getter for physical.

        Returns:
            The physical value

        Note:
            Delegates to physical property (CODING_RULE_V2_00017)
        """
        return self.physical  # Delegates to property

    def setPhysical(self, value: "PhysicalChannel") -> TDEventFrame:
        """
        AUTOSAR-compliant setter for physical with method chaining.

        Args:
            value: The physical to set

        Returns:
            self for method chaining

        Note:
            Delegates to physical property setter (gets validation automatically)
        """
        self.physical = value  # Delegates to property setter
        return self

    def getTdEventTypeEnum(self) -> "TDEventFrameType":
        """
        AUTOSAR-compliant getter for tdEventTypeEnum.

        Returns:
            The tdEventTypeEnum value

        Note:
            Delegates to td_event_type_enum property (CODING_RULE_V2_00017)
        """
        return self.td_event_type_enum  # Delegates to property

    def setTdEventTypeEnum(self, value: "TDEventFrameType") -> TDEventFrame:
        """
        AUTOSAR-compliant setter for tdEventTypeEnum with method chaining.

        Args:
            value: The tdEventTypeEnum to set

        Returns:
            self for method chaining

        Note:
            Delegates to td_event_type_enum property setter (gets validation automatically)
        """
        self.td_event_type_enum = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_frame(self, value: Optional[Frame]) -> TDEventFrame:
        """
        Set frame and return self for chaining.

        Args:
            value: The frame to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_frame("value")
        """
        self.frame = value  # Use property setter (gets validation)
        return self

    def with_physical(self, value: Optional["PhysicalChannel"]) -> TDEventFrame:
        """
        Set physical and return self for chaining.

        Args:
            value: The physical to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_physical("value")
        """
        self.physical = value  # Use property setter (gets validation)
        return self

    def with_td_event_type_enum(self, value: Optional["TDEventFrameType"]) -> TDEventFrame:
        """
        Set tdEventTypeEnum and return self for chaining.

        Args:
            value: The tdEventTypeEnum to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_td_event_type_enum("value")
        """
        self.td_event_type_enum = value  # Use property setter (gets validation)
        return self



class TDEventFrameEthernet(TDEventCom):
    """
    This is used to describe timing description events related to the exchange
    of Ethernet frames between an Ethernet communication controller and the BSW
    Ethernet interface and driver module.

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingDescription::TimingDescription::TDEventFrameEthernet

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 69, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specifies the SocketConnection by the means of which Data Units (PDU) are
        # transmitted or received Ethernet Frame.
        self._staticSocket: Optional["StaticSocketConnection"] = None

    @property
    def static_socket(self) -> Optional["StaticSocketConnection"]:
        """Get staticSocket (Pythonic accessor)."""
        return self._staticSocket

    @static_socket.setter
    def static_socket(self, value: Optional["StaticSocketConnection"]) -> None:
        """
        Set staticSocket with validation.

        Args:
            value: The staticSocket to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._staticSocket = None
            return

        if not isinstance(value, StaticSocketConnection):
            raise TypeError(
                f"staticSocket must be StaticSocketConnection or None, got {type(value).__name__}"
            )
        self._staticSocket = value
        self._tdEventType: Optional[TDEventFrameEthernet] = None

    @property
    def td_event_type(self) -> Optional[TDEventFrameEthernet]:
        """Get tdEventType (Pythonic accessor)."""
        return self._tdEventType

    @td_event_type.setter
    def td_event_type(self, value: Optional[TDEventFrameEthernet]) -> None:
        """
        Set tdEventType with validation.

        Args:
            value: The tdEventType to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tdEventType = None
            return

        if not isinstance(value, TDEventFrameEthernet):
            raise TypeError(
                f"tdEventType must be TDEventFrameEthernet or None, got {type(value).__name__}"
            )
        self._tdEventType = value
        # Ethernet frame let the.
        self._tdHeaderIdFilter: List[TDHeaderIdRange] = []

    @property
    def td_header_id_filter(self) -> List[TDHeaderIdRange]:
        """Get tdHeaderIdFilter (Pythonic accessor)."""
        return self._tdHeaderIdFilter
        # Specifies the PDU that if contained in the Ethernet frame the
        # TDEventFrameEthernet occur.
        self._tdPduTriggering: List[RefType] = []

    @property
    def td_pdu_triggering(self) -> List[RefType]:
        """Get tdPduTriggering (Pythonic accessor)."""
        return self._tdPduTriggering

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getStaticSocket(self) -> "StaticSocketConnection":
        """
        AUTOSAR-compliant getter for staticSocket.

        Returns:
            The staticSocket value

        Note:
            Delegates to static_socket property (CODING_RULE_V2_00017)
        """
        return self.static_socket  # Delegates to property

    def setStaticSocket(self, value: "StaticSocketConnection") -> TDEventFrameEthernet:
        """
        AUTOSAR-compliant setter for staticSocket with method chaining.

        Args:
            value: The staticSocket to set

        Returns:
            self for method chaining

        Note:
            Delegates to static_socket property setter (gets validation automatically)
        """
        self.static_socket = value  # Delegates to property setter
        return self

    def getTdEventType(self) -> TDEventFrameEthernet:
        """
        AUTOSAR-compliant getter for tdEventType.

        Returns:
            The tdEventType value

        Note:
            Delegates to td_event_type property (CODING_RULE_V2_00017)
        """
        return self.td_event_type  # Delegates to property

    def setTdEventType(self, value: TDEventFrameEthernet) -> TDEventFrameEthernet:
        """
        AUTOSAR-compliant setter for tdEventType with method chaining.

        Args:
            value: The tdEventType to set

        Returns:
            self for method chaining

        Note:
            Delegates to td_event_type property setter (gets validation automatically)
        """
        self.td_event_type = value  # Delegates to property setter
        return self

    def getTdHeaderIdFilter(self) -> List[TDHeaderIdRange]:
        """
        AUTOSAR-compliant getter for tdHeaderIdFilter.

        Returns:
            The tdHeaderIdFilter value

        Note:
            Delegates to td_header_id_filter property (CODING_RULE_V2_00017)
        """
        return self.td_header_id_filter  # Delegates to property

    def getTdPduTriggering(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for tdPduTriggering.

        Returns:
            The tdPduTriggering value

        Note:
            Delegates to td_pdu_triggering property (CODING_RULE_V2_00017)
        """
        return self.td_pdu_triggering  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_static_socket(self, value: Optional["StaticSocketConnection"]) -> TDEventFrameEthernet:
        """
        Set staticSocket and return self for chaining.

        Args:
            value: The staticSocket to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_static_socket("value")
        """
        self.static_socket = value  # Use property setter (gets validation)
        return self

    def with_td_event_type(self, value: Optional[TDEventFrameEthernet]) -> TDEventFrameEthernet:
        """
        Set tdEventType and return self for chaining.

        Args:
            value: The tdEventType to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_td_event_type("value")
        """
        self.td_event_type = value  # Use property setter (gets validation)
        return self



class TDEventCycleStart(TDEventCom, ABC):
    """
    This is the abstract parent class to describe timing events related to a
    point in time where a communication cycle starts. Via the attribute
    "cycleRepetition", a filtered view to the cycle start can be defined.

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingDescription::TimingDescription::TDEventCycleStart

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 71, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is TDEventCycleStart:
            raise TypeError("TDEventCycleStart is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The start of every <cycleRepetition> cycle is targeted by.
        self._cycleRepetition: Optional[Integer] = None

    @property
    def cycle_repetition(self) -> Optional[Integer]:
        """Get cycleRepetition (Pythonic accessor)."""
        return self._cycleRepetition

    @cycle_repetition.setter
    def cycle_repetition(self, value: Optional[Integer]) -> None:
        """
        Set cycleRepetition with validation.

        Args:
            value: The cycleRepetition to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._cycleRepetition = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"cycleRepetition must be Integer or int or None, got {type(value).__name__}"
            )
        self._cycleRepetition = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCycleRepetition(self) -> Integer:
        """
        AUTOSAR-compliant getter for cycleRepetition.

        Returns:
            The cycleRepetition value

        Note:
            Delegates to cycle_repetition property (CODING_RULE_V2_00017)
        """
        return self.cycle_repetition  # Delegates to property

    def setCycleRepetition(self, value: Integer) -> TDEventCycleStart:
        """
        AUTOSAR-compliant setter for cycleRepetition with method chaining.

        Args:
            value: The cycleRepetition to set

        Returns:
            self for method chaining

        Note:
            Delegates to cycle_repetition property setter (gets validation automatically)
        """
        self.cycle_repetition = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_cycle_repetition(self, value: Optional[Integer]) -> TDEventCycleStart:
        """
        Set cycleRepetition and return self for chaining.

        Args:
            value: The cycleRepetition to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_cycle_repetition("value")
        """
        self.cycle_repetition = value  # Use property setter (gets validation)
        return self



class TDEventBswModule(TDEventBsw):
    """
    This is used to describe timing events related to the interaction between
    BSW modules.

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingDescription::TimingDescription::TDEventBswModule

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 75, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The scope of this timing event.
        self._bswModuleEntry: Optional[BswModuleEntry] = None

    @property
    def bsw_module_entry(self) -> Optional[BswModuleEntry]:
        """Get bswModuleEntry (Pythonic accessor)."""
        return self._bswModuleEntry

    @bsw_module_entry.setter
    def bsw_module_entry(self, value: Optional[BswModuleEntry]) -> None:
        """
        Set bswModuleEntry with validation.

        Args:
            value: The bswModuleEntry to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._bswModuleEntry = None
            return

        if not isinstance(value, BswModuleEntry):
            raise TypeError(
                f"bswModuleEntry must be BswModuleEntry or None, got {type(value).__name__}"
            )
        self._bswModuleEntry = value
        self._tdEventBsw: Optional[TDEventBswModule] = None

    @property
    def td_event_bsw(self) -> Optional[TDEventBswModule]:
        """Get tdEventBsw (Pythonic accessor)."""
        return self._tdEventBsw

    @td_event_bsw.setter
    def td_event_bsw(self, value: Optional[TDEventBswModule]) -> None:
        """
        Set tdEventBsw with validation.

        Args:
            value: The tdEventBsw to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tdEventBsw = None
            return

        if not isinstance(value, TDEventBswModule):
            raise TypeError(
                f"tdEventBsw must be TDEventBswModule or None, got {type(value).__name__}"
            )
        self._tdEventBsw = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBswModuleEntry(self) -> BswModuleEntry:
        """
        AUTOSAR-compliant getter for bswModuleEntry.

        Returns:
            The bswModuleEntry value

        Note:
            Delegates to bsw_module_entry property (CODING_RULE_V2_00017)
        """
        return self.bsw_module_entry  # Delegates to property

    def setBswModuleEntry(self, value: BswModuleEntry) -> TDEventBswModule:
        """
        AUTOSAR-compliant setter for bswModuleEntry with method chaining.

        Args:
            value: The bswModuleEntry to set

        Returns:
            self for method chaining

        Note:
            Delegates to bsw_module_entry property setter (gets validation automatically)
        """
        self.bsw_module_entry = value  # Delegates to property setter
        return self

    def getTdEventBsw(self) -> TDEventBswModule:
        """
        AUTOSAR-compliant getter for tdEventBsw.

        Returns:
            The tdEventBsw value

        Note:
            Delegates to td_event_bsw property (CODING_RULE_V2_00017)
        """
        return self.td_event_bsw  # Delegates to property

    def setTdEventBsw(self, value: TDEventBswModule) -> TDEventBswModule:
        """
        AUTOSAR-compliant setter for tdEventBsw with method chaining.

        Args:
            value: The tdEventBsw to set

        Returns:
            self for method chaining

        Note:
            Delegates to td_event_bsw property setter (gets validation automatically)
        """
        self.td_event_bsw = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_bsw_module_entry(self, value: Optional[BswModuleEntry]) -> TDEventBswModule:
        """
        Set bswModuleEntry and return self for chaining.

        Args:
            value: The bswModuleEntry to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_bsw_module_entry("value")
        """
        self.bsw_module_entry = value  # Use property setter (gets validation)
        return self

    def with_td_event_bsw(self, value: Optional[TDEventBswModule]) -> TDEventBswModule:
        """
        Set tdEventBsw and return self for chaining.

        Args:
            value: The tdEventBsw to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_td_event_bsw("value")
        """
        self.td_event_bsw = value  # Use property setter (gets validation)
        return self



class TDEventBswModeDeclaration(TDEventBsw):
    """
    This is used to describe timing events related to the mode communication on
    BSW level.

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingDescription::TimingDescription::TDEventBswModeDeclaration

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 76, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Optional parameter which refines the scope of the If the parameter is set,
        # the only if the mode declaration group prototype enter into the referenced
        # ModeDeclaration.
        self._entryMode: Optional["ModeDeclaration"] = None

    @property
    def entry_mode(self) -> Optional["ModeDeclaration"]:
        """Get entryMode (Pythonic accessor)."""
        return self._entryMode

    @entry_mode.setter
    def entry_mode(self, value: Optional["ModeDeclaration"]) -> None:
        """
        Set entryMode with validation.

        Args:
            value: The entryMode to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._entryMode = None
            return

        if not isinstance(value, ModeDeclaration):
            raise TypeError(
                f"entryMode must be ModeDeclaration or None, got {type(value).__name__}"
            )
        self._entryMode = value
        # the only if the mode declaration group prototype exit from the referenced
        # ModeDeclaration.
        self._exitMode: Optional["ModeDeclaration"] = None

    @property
    def exit_mode(self) -> Optional["ModeDeclaration"]:
        """Get exitMode (Pythonic accessor)."""
        return self._exitMode

    @exit_mode.setter
    def exit_mode(self, value: Optional["ModeDeclaration"]) -> None:
        """
        Set exitMode with validation.

        Args:
            value: The exitMode to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._exitMode = None
            return

        if not isinstance(value, ModeDeclaration):
            raise TypeError(
                f"exitMode must be ModeDeclaration or None, got {type(value).__name__}"
            )
        self._exitMode = value
        # 277 Document ID 411: AUTOSAR_CP_TPS_TimingExtensions Timing Extensions for
                # Classic R23-11.
        self._mode: Optional[RefType] = None

    @property
    def mode(self) -> Optional[RefType]:
        """Get mode (Pythonic accessor)."""
        return self._mode

    @mode.setter
    def mode(self, value: Optional[RefType]) -> None:
        """
        Set mode with validation.

        Args:
            value: The mode to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._mode = None
            return

        self._mode = value
        self._tdEventBswDeclarationType: Optional["TDEventBswMode"] = None

    @property
    def td_event_bsw_declaration_type(self) -> Optional["TDEventBswMode"]:
        """Get tdEventBswDeclarationType (Pythonic accessor)."""
        return self._tdEventBswDeclarationType

    @td_event_bsw_declaration_type.setter
    def td_event_bsw_declaration_type(self, value: Optional["TDEventBswMode"]) -> None:
        """
        Set tdEventBswDeclarationType with validation.

        Args:
            value: The tdEventBswDeclarationType to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tdEventBswDeclarationType = None
            return

        if not isinstance(value, TDEventBswMode):
            raise TypeError(
                f"tdEventBswDeclarationType must be TDEventBswMode or None, got {type(value).__name__}"
            )
        self._tdEventBswDeclarationType = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEntryMode(self) -> "ModeDeclaration":
        """
        AUTOSAR-compliant getter for entryMode.

        Returns:
            The entryMode value

        Note:
            Delegates to entry_mode property (CODING_RULE_V2_00017)
        """
        return self.entry_mode  # Delegates to property

    def setEntryMode(self, value: "ModeDeclaration") -> TDEventBswModeDeclaration:
        """
        AUTOSAR-compliant setter for entryMode with method chaining.

        Args:
            value: The entryMode to set

        Returns:
            self for method chaining

        Note:
            Delegates to entry_mode property setter (gets validation automatically)
        """
        self.entry_mode = value  # Delegates to property setter
        return self

    def getExitMode(self) -> "ModeDeclaration":
        """
        AUTOSAR-compliant getter for exitMode.

        Returns:
            The exitMode value

        Note:
            Delegates to exit_mode property (CODING_RULE_V2_00017)
        """
        return self.exit_mode  # Delegates to property

    def setExitMode(self, value: "ModeDeclaration") -> TDEventBswModeDeclaration:
        """
        AUTOSAR-compliant setter for exitMode with method chaining.

        Args:
            value: The exitMode to set

        Returns:
            self for method chaining

        Note:
            Delegates to exit_mode property setter (gets validation automatically)
        """
        self.exit_mode = value  # Delegates to property setter
        return self

    def getMode(self) -> RefType:
        """
        AUTOSAR-compliant getter for mode.

        Returns:
            The mode value

        Note:
            Delegates to mode property (CODING_RULE_V2_00017)
        """
        return self.mode  # Delegates to property

    def setMode(self, value: RefType) -> TDEventBswModeDeclaration:
        """
        AUTOSAR-compliant setter for mode with method chaining.

        Args:
            value: The mode to set

        Returns:
            self for method chaining

        Note:
            Delegates to mode property setter (gets validation automatically)
        """
        self.mode = value  # Delegates to property setter
        return self

    def getTdEventBswDeclarationType(self) -> "TDEventBswMode":
        """
        AUTOSAR-compliant getter for tdEventBswDeclarationType.

        Returns:
            The tdEventBswDeclarationType value

        Note:
            Delegates to td_event_bsw_declaration_type property (CODING_RULE_V2_00017)
        """
        return self.td_event_bsw_declaration_type  # Delegates to property

    def setTdEventBswDeclarationType(self, value: "TDEventBswMode") -> TDEventBswModeDeclaration:
        """
        AUTOSAR-compliant setter for tdEventBswDeclarationType with method chaining.

        Args:
            value: The tdEventBswDeclarationType to set

        Returns:
            self for method chaining

        Note:
            Delegates to td_event_bsw_declaration_type property setter (gets validation automatically)
        """
        self.td_event_bsw_declaration_type = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_entry_mode(self, value: Optional["ModeDeclaration"]) -> TDEventBswModeDeclaration:
        """
        Set entryMode and return self for chaining.

        Args:
            value: The entryMode to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_entry_mode("value")
        """
        self.entry_mode = value  # Use property setter (gets validation)
        return self

    def with_exit_mode(self, value: Optional["ModeDeclaration"]) -> TDEventBswModeDeclaration:
        """
        Set exitMode and return self for chaining.

        Args:
            value: The exitMode to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_exit_mode("value")
        """
        self.exit_mode = value  # Use property setter (gets validation)
        return self

    def with_mode(self, value: Optional[RefType]) -> TDEventBswModeDeclaration:
        """
        Set mode and return self for chaining.

        Args:
            value: The mode to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mode("value")
        """
        self.mode = value  # Use property setter (gets validation)
        return self

    def with_td_event_bsw_declaration_type(self, value: Optional["TDEventBswMode"]) -> TDEventBswModeDeclaration:
        """
        Set tdEventBswDeclarationType and return self for chaining.

        Args:
            value: The tdEventBswDeclarationType to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_td_event_bsw_declaration_type("value")
        """
        self.td_event_bsw_declaration_type = value  # Use property setter (gets validation)
        return self



class TDEventSLLETPort(TDEventSLLET):
    """
    Used to describe SL-LET timing events on the level of a SWC port.

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingDescription::TimingDescription::TDEventSLLETPort

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 79, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The originating port of the timing event.
        self._port: Optional[RefType] = None

    @property
    def port(self) -> Optional[RefType]:
        """Get port (Pythonic accessor)."""
        return self._port

    @port.setter
    def port(self, value: Optional[RefType]) -> None:
        """
        Set port with validation.

        Args:
            value: The port to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._port = None
            return

        self._port = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getPort(self) -> RefType:
        """
        AUTOSAR-compliant getter for port.

        Returns:
            The port value

        Note:
            Delegates to port property (CODING_RULE_V2_00017)
        """
        return self.port  # Delegates to property

    def setPort(self, value: RefType) -> TDEventSLLETPort:
        """
        AUTOSAR-compliant setter for port with method chaining.

        Args:
            value: The port to set

        Returns:
            self for method chaining

        Note:
            Delegates to port property setter (gets validation automatically)
        """
        self.port = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_port(self, value: Optional[RefType]) -> TDEventSLLETPort:
        """
        Set port and return self for chaining.

        Args:
            value: The port to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_port("value")
        """
        self.port = value  # Use property setter (gets validation)
        return self



class TDEventVariableDataPrototype(TDEventVfbPort):
    """
    This is used to describe timing events related to sender-receiver
    communication at VFB level.

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingDescription::TimingDescription::TDEventVariableDataPrototype

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 53, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The referenced VariableDataPrototype.
        self._dataElement: Optional[RefType] = None

    @property
    def data_element(self) -> Optional[RefType]:
        """Get dataElement (Pythonic accessor)."""
        return self._dataElement

    @data_element.setter
    def data_element(self, value: Optional[RefType]) -> None:
        """
        Set dataElement with validation.

        Args:
            value: The dataElement to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dataElement = None
            return

        self._dataElement = value
        self._tdEventVariableType: Optional["TDEventVariableData"] = None

    @property
    def td_event_variable_type(self) -> Optional["TDEventVariableData"]:
        """Get tdEventVariableType (Pythonic accessor)."""
        return self._tdEventVariableType

    @td_event_variable_type.setter
    def td_event_variable_type(self, value: Optional["TDEventVariableData"]) -> None:
        """
        Set tdEventVariableType with validation.

        Args:
            value: The tdEventVariableType to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tdEventVariableType = None
            return

        if not isinstance(value, TDEventVariableData):
            raise TypeError(
                f"tdEventVariableType must be TDEventVariableData or None, got {type(value).__name__}"
            )
        self._tdEventVariableType = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDataElement(self) -> RefType:
        """
        AUTOSAR-compliant getter for dataElement.

        Returns:
            The dataElement value

        Note:
            Delegates to data_element property (CODING_RULE_V2_00017)
        """
        return self.data_element  # Delegates to property

    def setDataElement(self, value: RefType) -> TDEventVariableDataPrototype:
        """
        AUTOSAR-compliant setter for dataElement with method chaining.

        Args:
            value: The dataElement to set

        Returns:
            self for method chaining

        Note:
            Delegates to data_element property setter (gets validation automatically)
        """
        self.data_element = value  # Delegates to property setter
        return self

    def getTdEventVariableType(self) -> "TDEventVariableData":
        """
        AUTOSAR-compliant getter for tdEventVariableType.

        Returns:
            The tdEventVariableType value

        Note:
            Delegates to td_event_variable_type property (CODING_RULE_V2_00017)
        """
        return self.td_event_variable_type  # Delegates to property

    def setTdEventVariableType(self, value: "TDEventVariableData") -> TDEventVariableDataPrototype:
        """
        AUTOSAR-compliant setter for tdEventVariableType with method chaining.

        Args:
            value: The tdEventVariableType to set

        Returns:
            self for method chaining

        Note:
            Delegates to td_event_variable_type property setter (gets validation automatically)
        """
        self.td_event_variable_type = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_data_element(self, value: Optional[RefType]) -> TDEventVariableDataPrototype:
        """
        Set dataElement and return self for chaining.

        Args:
            value: The dataElement to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_data_element("value")
        """
        self.data_element = value  # Use property setter (gets validation)
        return self

    def with_td_event_variable_type(self, value: Optional["TDEventVariableData"]) -> TDEventVariableDataPrototype:
        """
        Set tdEventVariableType and return self for chaining.

        Args:
            value: The tdEventVariableType to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_td_event_variable_type("value")
        """
        self.td_event_variable_type = value  # Use property setter (gets validation)
        return self



class TDEventOperation(TDEventVfbPort):
    """
    This is used to describe timing events related to client-server
    communication at VFB level.

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingDescription::TimingDescription::TDEventOperation

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 55, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The referenced operation.
        self._operation: Optional[ClientServerOperation] = None

    @property
    def operation(self) -> Optional[ClientServerOperation]:
        """Get operation (Pythonic accessor)."""
        return self._operation

    @operation.setter
    def operation(self, value: Optional[ClientServerOperation]) -> None:
        """
        Set operation with validation.

        Args:
            value: The operation to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._operation = None
            return

        if not isinstance(value, ClientServerOperation):
            raise TypeError(
                f"operation must be ClientServerOperation or None, got {type(value).__name__}"
            )
        self._operation = value
        self._tdEvent: Optional["TDEventOperationType"] = None

    @property
    def td_event(self) -> Optional["TDEventOperationType"]:
        """Get tdEvent (Pythonic accessor)."""
        return self._tdEvent

    @td_event.setter
    def td_event(self, value: Optional["TDEventOperationType"]) -> None:
        """
        Set tdEvent with validation.

        Args:
            value: The tdEvent to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tdEvent = None
            return

        if not isinstance(value, TDEventOperationType):
            raise TypeError(
                f"tdEvent must be TDEventOperationType or None, got {type(value).__name__}"
            )
        self._tdEvent = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getOperation(self) -> ClientServerOperation:
        """
        AUTOSAR-compliant getter for operation.

        Returns:
            The operation value

        Note:
            Delegates to operation property (CODING_RULE_V2_00017)
        """
        return self.operation  # Delegates to property

    def setOperation(self, value: ClientServerOperation) -> TDEventOperation:
        """
        AUTOSAR-compliant setter for operation with method chaining.

        Args:
            value: The operation to set

        Returns:
            self for method chaining

        Note:
            Delegates to operation property setter (gets validation automatically)
        """
        self.operation = value  # Delegates to property setter
        return self

    def getTdEvent(self) -> "TDEventOperationType":
        """
        AUTOSAR-compliant getter for tdEvent.

        Returns:
            The tdEvent value

        Note:
            Delegates to td_event property (CODING_RULE_V2_00017)
        """
        return self.td_event  # Delegates to property

    def setTdEvent(self, value: "TDEventOperationType") -> TDEventOperation:
        """
        AUTOSAR-compliant setter for tdEvent with method chaining.

        Args:
            value: The tdEvent to set

        Returns:
            self for method chaining

        Note:
            Delegates to td_event property setter (gets validation automatically)
        """
        self.td_event = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_operation(self, value: Optional[ClientServerOperation]) -> TDEventOperation:
        """
        Set operation and return self for chaining.

        Args:
            value: The operation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_operation("value")
        """
        self.operation = value  # Use property setter (gets validation)
        return self

    def with_td_event(self, value: Optional["TDEventOperationType"]) -> TDEventOperation:
        """
        Set tdEvent and return self for chaining.

        Args:
            value: The tdEvent to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_td_event("value")
        """
        self.td_event = value  # Use property setter (gets validation)
        return self



class TDEventModeDeclaration(TDEventVfbPort):
    """
    This is used to describe timing events related to mode switch communication
    at VFB level.

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingDescription::TimingDescription::TDEventModeDeclaration

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 57, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Optional parameter which refines the scope of the If the parameter is set,
        # the only if the mode declaration group prototype enter into the referenced
        # ModeDeclaration.
        self._entryMode: Optional["ModeDeclaration"] = None

    @property
    def entry_mode(self) -> Optional["ModeDeclaration"]:
        """Get entryMode (Pythonic accessor)."""
        return self._entryMode

    @entry_mode.setter
    def entry_mode(self, value: Optional["ModeDeclaration"]) -> None:
        """
        Set entryMode with validation.

        Args:
            value: The entryMode to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._entryMode = None
            return

        if not isinstance(value, ModeDeclaration):
            raise TypeError(
                f"entryMode must be ModeDeclaration or None, got {type(value).__name__}"
            )
        self._entryMode = value
        # the only if the mode declaration group prototype exit from the referenced
        # ModeDeclaration.
        self._exitMode: Optional["ModeDeclaration"] = None

    @property
    def exit_mode(self) -> Optional["ModeDeclaration"]:
        """Get exitMode (Pythonic accessor)."""
        return self._exitMode

    @exit_mode.setter
    def exit_mode(self, value: Optional["ModeDeclaration"]) -> None:
        """
        Set exitMode with validation.

        Args:
            value: The exitMode to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._exitMode = None
            return

        if not isinstance(value, ModeDeclaration):
            raise TypeError(
                f"exitMode must be ModeDeclaration or None, got {type(value).__name__}"
            )
        self._exitMode = value
        self._mode: Optional[RefType] = None

    @property
    def mode(self) -> Optional[RefType]:
        """Get mode (Pythonic accessor)."""
        return self._mode

    @mode.setter
    def mode(self, value: Optional[RefType]) -> None:
        """
        Set mode with validation.

        Args:
            value: The mode to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._mode = None
            return

        self._mode = value
        self._tdEventMode: Optional["TDEventMode"] = None

    @property
    def td_event_mode(self) -> Optional["TDEventMode"]:
        """Get tdEventMode (Pythonic accessor)."""
        return self._tdEventMode

    @td_event_mode.setter
    def td_event_mode(self, value: Optional["TDEventMode"]) -> None:
        """
        Set tdEventMode with validation.

        Args:
            value: The tdEventMode to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tdEventMode = None
            return

        if not isinstance(value, TDEventMode):
            raise TypeError(
                f"tdEventMode must be TDEventMode or None, got {type(value).__name__}"
            )
        self._tdEventMode = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEntryMode(self) -> "ModeDeclaration":
        """
        AUTOSAR-compliant getter for entryMode.

        Returns:
            The entryMode value

        Note:
            Delegates to entry_mode property (CODING_RULE_V2_00017)
        """
        return self.entry_mode  # Delegates to property

    def setEntryMode(self, value: "ModeDeclaration") -> TDEventModeDeclaration:
        """
        AUTOSAR-compliant setter for entryMode with method chaining.

        Args:
            value: The entryMode to set

        Returns:
            self for method chaining

        Note:
            Delegates to entry_mode property setter (gets validation automatically)
        """
        self.entry_mode = value  # Delegates to property setter
        return self

    def getExitMode(self) -> "ModeDeclaration":
        """
        AUTOSAR-compliant getter for exitMode.

        Returns:
            The exitMode value

        Note:
            Delegates to exit_mode property (CODING_RULE_V2_00017)
        """
        return self.exit_mode  # Delegates to property

    def setExitMode(self, value: "ModeDeclaration") -> TDEventModeDeclaration:
        """
        AUTOSAR-compliant setter for exitMode with method chaining.

        Args:
            value: The exitMode to set

        Returns:
            self for method chaining

        Note:
            Delegates to exit_mode property setter (gets validation automatically)
        """
        self.exit_mode = value  # Delegates to property setter
        return self

    def getMode(self) -> RefType:
        """
        AUTOSAR-compliant getter for mode.

        Returns:
            The mode value

        Note:
            Delegates to mode property (CODING_RULE_V2_00017)
        """
        return self.mode  # Delegates to property

    def setMode(self, value: RefType) -> TDEventModeDeclaration:
        """
        AUTOSAR-compliant setter for mode with method chaining.

        Args:
            value: The mode to set

        Returns:
            self for method chaining

        Note:
            Delegates to mode property setter (gets validation automatically)
        """
        self.mode = value  # Delegates to property setter
        return self

    def getTdEventMode(self) -> "TDEventMode":
        """
        AUTOSAR-compliant getter for tdEventMode.

        Returns:
            The tdEventMode value

        Note:
            Delegates to td_event_mode property (CODING_RULE_V2_00017)
        """
        return self.td_event_mode  # Delegates to property

    def setTdEventMode(self, value: "TDEventMode") -> TDEventModeDeclaration:
        """
        AUTOSAR-compliant setter for tdEventMode with method chaining.

        Args:
            value: The tdEventMode to set

        Returns:
            self for method chaining

        Note:
            Delegates to td_event_mode property setter (gets validation automatically)
        """
        self.td_event_mode = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_entry_mode(self, value: Optional["ModeDeclaration"]) -> TDEventModeDeclaration:
        """
        Set entryMode and return self for chaining.

        Args:
            value: The entryMode to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_entry_mode("value")
        """
        self.entry_mode = value  # Use property setter (gets validation)
        return self

    def with_exit_mode(self, value: Optional["ModeDeclaration"]) -> TDEventModeDeclaration:
        """
        Set exitMode and return self for chaining.

        Args:
            value: The exitMode to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_exit_mode("value")
        """
        self.exit_mode = value  # Use property setter (gets validation)
        return self

    def with_mode(self, value: Optional[RefType]) -> TDEventModeDeclaration:
        """
        Set mode and return self for chaining.

        Args:
            value: The mode to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mode("value")
        """
        self.mode = value  # Use property setter (gets validation)
        return self

    def with_td_event_mode(self, value: Optional["TDEventMode"]) -> TDEventModeDeclaration:
        """
        Set tdEventMode and return self for chaining.

        Args:
            value: The tdEventMode to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_td_event_mode("value")
        """
        self.td_event_mode = value  # Use property setter (gets validation)
        return self



class TDEventTrigger(TDEventVfbPort):
    """
    This is used to describe timing events related to triggers at VFB level.

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingDescription::TimingDescription::TDEventTrigger

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 58, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The specific type of this timing event.
        self._tdEventTrigger: Optional[RefType] = None

    @property
    def td_event_trigger(self) -> Optional[RefType]:
        """Get tdEventTrigger (Pythonic accessor)."""
        return self._tdEventTrigger

    @td_event_trigger.setter
    def td_event_trigger(self, value: Optional[RefType]) -> None:
        """
        Set tdEventTrigger with validation.

        Args:
            value: The tdEventTrigger to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tdEventTrigger = None
            return

        self._tdEventTrigger = value
        self._trigger: Optional[RefType] = None

    @property
    def trigger(self) -> Optional[RefType]:
        """Get trigger (Pythonic accessor)."""
        return self._trigger

    @trigger.setter
    def trigger(self, value: Optional[RefType]) -> None:
        """
        Set trigger with validation.

        Args:
            value: The trigger to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._trigger = None
            return

        self._trigger = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTdEventTrigger(self) -> RefType:
        """
        AUTOSAR-compliant getter for tdEventTrigger.

        Returns:
            The tdEventTrigger value

        Note:
            Delegates to td_event_trigger property (CODING_RULE_V2_00017)
        """
        return self.td_event_trigger  # Delegates to property

    def setTdEventTrigger(self, value: RefType) -> TDEventTrigger:
        """
        AUTOSAR-compliant setter for tdEventTrigger with method chaining.

        Args:
            value: The tdEventTrigger to set

        Returns:
            self for method chaining

        Note:
            Delegates to td_event_trigger property setter (gets validation automatically)
        """
        self.td_event_trigger = value  # Delegates to property setter
        return self

    def getTrigger(self) -> RefType:
        """
        AUTOSAR-compliant getter for trigger.

        Returns:
            The trigger value

        Note:
            Delegates to trigger property (CODING_RULE_V2_00017)
        """
        return self.trigger  # Delegates to property

    def setTrigger(self, value: RefType) -> TDEventTrigger:
        """
        AUTOSAR-compliant setter for trigger with method chaining.

        Args:
            value: The trigger to set

        Returns:
            self for method chaining

        Note:
            Delegates to trigger property setter (gets validation automatically)
        """
        self.trigger = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_td_event_trigger(self, value: Optional[RefType]) -> TDEventTrigger:
        """
        Set tdEventTrigger and return self for chaining.

        Args:
            value: The tdEventTrigger to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_td_event_trigger("value")
        """
        self.td_event_trigger = value  # Use property setter (gets validation)
        return self

    def with_trigger(self, value: Optional[RefType]) -> TDEventTrigger:
        """
        Set trigger and return self for chaining.

        Args:
            value: The trigger to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_trigger("value")
        """
        self.trigger = value  # Use property setter (gets validation)
        return self



class TDEventFrClusterCycleStart(TDEventCycleStart):
    """
    This is used to describe the timing event related to a point in time where a
    communication cycle starts on a FlexRay cluster.

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingDescription::TimingDescription::TDEventFrClusterCycleStart

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 71, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The scope of this timing event.
        self._frCluster: Optional[FlexrayCluster] = None

    @property
    def fr_cluster(self) -> Optional[FlexrayCluster]:
        """Get frCluster (Pythonic accessor)."""
        return self._frCluster

    @fr_cluster.setter
    def fr_cluster(self, value: Optional[FlexrayCluster]) -> None:
        """
        Set frCluster with validation.

        Args:
            value: The frCluster to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._frCluster = None
            return

        if not isinstance(value, FlexrayCluster):
            raise TypeError(
                f"frCluster must be FlexrayCluster or None, got {type(value).__name__}"
            )
        self._frCluster = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getFrCluster(self) -> FlexrayCluster:
        """
        AUTOSAR-compliant getter for frCluster.

        Returns:
            The frCluster value

        Note:
            Delegates to fr_cluster property (CODING_RULE_V2_00017)
        """
        return self.fr_cluster  # Delegates to property

    def setFrCluster(self, value: FlexrayCluster) -> TDEventFrClusterCycleStart:
        """
        AUTOSAR-compliant setter for frCluster with method chaining.

        Args:
            value: The frCluster to set

        Returns:
            self for method chaining

        Note:
            Delegates to fr_cluster property setter (gets validation automatically)
        """
        self.fr_cluster = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_fr_cluster(self, value: Optional[FlexrayCluster]) -> TDEventFrClusterCycleStart:
        """
        Set frCluster and return self for chaining.

        Args:
            value: The frCluster to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_fr_cluster("value")
        """
        self.fr_cluster = value  # Use property setter (gets validation)
        return self



class TDEventTTCanCycleStart(TDEventCycleStart):
    """
    This is used to describe the timing event related to a point in time where a
    communication cycle starts on a TTCAN cluster.

    Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingDescription::TimingDescription::TDEventTTCanCycleStart

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 72, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The scope of this timing event.
        self._ttCanCluster: Optional[TtcanCluster] = None

    @property
    def tt_can_cluster(self) -> Optional[TtcanCluster]:
        """Get ttCanCluster (Pythonic accessor)."""
        return self._ttCanCluster

    @tt_can_cluster.setter
    def tt_can_cluster(self, value: Optional[TtcanCluster]) -> None:
        """
        Set ttCanCluster with validation.

        Args:
            value: The ttCanCluster to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ttCanCluster = None
            return

        if not isinstance(value, TtcanCluster):
            raise TypeError(
                f"ttCanCluster must be TtcanCluster or None, got {type(value).__name__}"
            )
        self._ttCanCluster = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTtCanCluster(self) -> TtcanCluster:
        """
        AUTOSAR-compliant getter for ttCanCluster.

        Returns:
            The ttCanCluster value

        Note:
            Delegates to tt_can_cluster property (CODING_RULE_V2_00017)
        """
        return self.tt_can_cluster  # Delegates to property

    def setTtCanCluster(self, value: TtcanCluster) -> TDEventTTCanCycleStart:
        """
        AUTOSAR-compliant setter for ttCanCluster with method chaining.

        Args:
            value: The ttCanCluster to set

        Returns:
            self for method chaining

        Note:
            Delegates to tt_can_cluster property setter (gets validation automatically)
        """
        self.tt_can_cluster = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_tt_can_cluster(self, value: Optional[TtcanCluster]) -> TDEventTTCanCycleStart:
        """
        Set ttCanCluster and return self for chaining.

        Args:
            value: The ttCanCluster to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tt_can_cluster("value")
        """
        self.tt_can_cluster = value  # Use property setter (gets validation)
        return self


class TDEventVariableDataPrototypeTypeEnum(AREnum):
    """
    TDEventVariableDataPrototypeTypeEnum enumeration

This is used to describe the specific event type of a TDEventVariableDataPrototype Aggregated by TDEventVariableDataPrototype.tdEventVariableDataPrototypeType

Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingDescription::TimingDescription
    """
    # A point in time where the referenced variable data prototype has been successfully transmitted and is PrototypeReceived available in the related communication buffer (of the RTE) for the receiving SWC.
    variableData = "0"

    # A point in time where the referenced variable data prototype has been successfully sent out by the PrototypeSent sending SWC, so that it is available in the related communication buffer (of the RTE) for transmission.
    variableData = "1"



class TDEventOperationTypeEnum(AREnum):
    """
    TDEventOperationTypeEnum enumeration

This is used to describe the specific event type of a TDEventOperation. Aggregated by TDEventOperation.tdEventOperationType

Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingDescription::TimingDescription
    """
    # A point in time where the referenced operation is called by the client SWC.
    operationCalled = "0"

    # A point in time where the call of the referenced operation is received by the server SWC.
    operationCallReceived = "1"

    # A point in time where the client SWC has received the response of the referenced operation call.
    operationCallResponseReceived = "2"

    # A point in time where the server SWC has terminated with the execution of the referenced operation, ResponseSent and has sent out a response.
    operationCall = "3"



class TDEventModeDeclarationTypeEnum(AREnum):
    """
    TDEventModeDeclarationTypeEnum enumeration

This is used to describe the specific event type of a TDEventModeDeclaration Aggregated by TDEventModeDeclaration.tdEventModeDeclarationType

Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingDescription::TimingDescription
    """
    # A point in time where the switch to the associated ModeDeclarationGroupPrototype has been SwitchCompleted completed.
    modeDeclaration = "0"

    # A point in time where the switch to the associated ModeDeclarationGroupPrototype has been SwitchInitiated initiated.
    modeDeclaration = "1"



class TDEventTriggerTypeEnum(AREnum):
    """
    TDEventTriggerTypeEnum enumeration

This is used to describe the specific event type of a TDEventTrigger. Aggregated by TDEventTrigger.tdEventTriggerType

Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingDescription::TimingDescription
    """
    # A point in time where the referenced trigger has been successfully released and is activating runnable entities of the receiving SW-C.
    triggerActivated = "0"

    # A point in time where the referenced trigger has been successfully released by the emitting SW-C.
    triggerReleased = "1"



class TDEventSwcInternalBehaviorTypeEnum(AREnum):
    """
    TDEventSwcInternalBehaviorTypeEnum enumeration

This is used to describe the specific event type of a TDEventSwcInternalBehavior. Aggregated by TDEventSwcInternalBehavior.tdEventSwcInternalBehaviorType

Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingDescription::TimingDescription
    """
    # A point in time where the associated RunnableEntity has been activated, which means that it has Activated entered the state "to be started".
    runnableEntity = "0"

    # A point in time where the associated RunnableEntity has entered the state "started" after its Started activation.
    runnableEntity = "1"

    # A point in time where the associated RunnableEntity has terminated and entered the state
    runnableEntityTerminated = "2"

    # A point in time where the associated variable is accessed.
    runnableEntityVariableAccess = "3"



class TDEventISignalTypeEnum(AREnum):
    """
    TDEventISignalTypeEnum enumeration

This is used to describe the specific event type of a TDEventISignal. Aggregated by TDEventISignal.tdEventType

Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingDescription::TimingDescription
    """
    # A point in time, where the COM module makes the contained signal / signal group available for the
    iSignalAvailableFor = "None"

    # RTE and the corresponding Rx Indication callout is generated (if configured).
    RTE = "0"

    # A point in time, where a transmission request call is issued by the RTE on a named COM signal / signal group and the new value is stored to the carrier COM I-PDU buffer.
    iSignalSentToCOM = "1"



class TDEventIPduTypeEnum(AREnum):
    """
    TDEventIPduTypeEnum enumeration

This is used to describe the specific event type of a TDEventIPdu. Aggregated by TDEventIPdu.tdEventType

Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingDescription::TimingDescription
    """
    # A point in time where the received frame is processed by the corresponding (FlexRay / CAN / LIN)
    iPduReceivedBy = "None"

    # Interface BSW module, routed through the PDUR and the contained PDUs are pushed to the COM
    COM = "0"

    # A point in time where the carrier COM I-PDU is routed through the PDUR and is pushed to the bus
    iPduSentToIfspecific = "1"



class TDEventFrameTypeEnum(AREnum):
    """
    TDEventFrameTypeEnum enumeration

This is used to describe the specific event type of a TDEventFrame. Aggregated by TDEventFrame.tdEventType

Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingDescription::TimingDescription
    """
    # A point in time where the frame containing the named signal / I-PDU is queued for transmission within Transmission the related Communication Driver.
    frameQueuedFor = "0"

    # A point in time where the frame is pushed from the subscriber’s communication controller to the
    frameReceivedByIfcorresponding = "1"

    # A point in time where the transmission of the frame completes successfully, and the subscriber’s OnBus communication controller receives the frame from the bus.
    frameTransmitted = "2"



class TDEventFrameEthernetTypeEnum(AREnum):
    """
    TDEventFrameEthernetTypeEnum enumeration

This is used to describe the specific event type of a TDEventFrameEthernet. Aggregated by TDEventFrameEthernet.tdEventType

Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingDescription::TimingDescription
    """
    # A point in time where the Ethernet frame containing the specified PDUs is queued for transmission QueuedFor within the corresponding Ethernet Communication Driver.
    frameEthernetTransmission = "0"

    # A point in time where the frame is pushed from the corresponding Ethernet communication controller ReceivedByIf to the BSW Ethernet communication interface.
    frameEthernet = "1"

    # A point in time where the receipt of the Ethernet frame/packet completes successfully on the ReceivedOnBus recipient’s Ethernet communication controller. In other words, the Ethernet frame/packet has entered the recipient’s Ethernet communication controller which means the last bit of the Ethernet frame/ packet has been received.
    frameEthernet = "2"

    # A point in time where the transmission of the Ethernet frame/packet completes successfully on the OnBus physical Ethernet communication network. In other words, the Ethernet frame/packet has left the packet has been sent.
    frameEthernetSent = "3"



class TDEventBswInternalBehaviorTypeEnum(AREnum):
    """
    TDEventBswInternalBehaviorTypeEnum enumeration

This is used to describe the specific event type of a TDEventBswInternalBehavior. Aggregated by TDEventBswInternalBehavior.tdEventBswInternalBehaviorType

Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingDescription::TimingDescription
    """
    # A point in time where the associated BswModuleEntity has been activated, which means that it has Activated entered the state "to be started".
    bswModuleEntity = "0"

    # A point in time where the associated BswModuleEntity has entered the state "started" after its Started activation.
    bswModuleEntity = "1"

    # A point in time where the associated BswModuleEntity has terminated and entered the state
    bswModuleEntityTerminated = "2"



class TDEventBswModuleTypeEnum(AREnum):
    """
    TDEventBswModuleTypeEnum enumeration

This is used to describe the specific event type of a TDEventBswModule. Aggregated by TDEventBswModule.tdEventBswModuleType

Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingDescription::TimingDescription
    """
    # A point in time where the associated BswModuleEntry has been called.
    bswMEntryCalled = "0"

    # A point in time where the call of the associated BswModuleEntry has returned.
    bswMEntryCallReturned = "1"



class TDEventBswModeDeclarationTypeEnum(AREnum):
    """
    TDEventBswModeDeclarationTypeEnum enumeration

This is used to describe the specific event type of a TDEventBswModeDeclaration. Aggregated by TDEventBswModeDeclaration.tdEventBswModeDeclarationType

Package: M2::AUTOSARTemplates::CommonStructure::Timing::TimingDescription::TimingDescription
    """
    # A point in time where the associated ModeDeclarationGroupPrototype has been requested.
    modeDeclarationRequested = "0"

    # A point in time where the switch to the associated ModeDeclarationGroupPrototype has been SwitchCompleted completed.
    modeDeclaration = "1"

    # A point in time where the switch to the associated ModeDeclarationGroupPrototype has been initiated SwitchInitiated by the BswM.
    modeDeclaration = "2"

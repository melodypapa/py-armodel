"""
AUTOSAR Package - RptSupport

Package: M2::AUTOSARTemplates::CommonStructure::MeasurementCalibrationSupport::RptSupport
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
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




class McFunctionDataRefSet(ARObject):
    """
    Refers to a set of data assigned to an McFunction in a particular role. The
    data are given • either by entries in a FlatMap • or by data instances that
    are part of MC support data. These two possibilities are exclusive within a
    given McFunctionDataRefSet. Which one to use depends on the process and tool
    environment. The set is subject to variability because the same functional
    model may be used with various representation of the data. Tags:
    vh.latestBindingTime=preCompileTime
    
    Package: M2::AUTOSARTemplates::CommonStructure::MeasurementCalibrationSupport::RptSupport::McFunctionDataRefSet
    
    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 187, Classic
      Platform R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 455, Foundation
      R23-11)
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



class RptSupportData(ARObject):
    """
    Root element for rapid prototyping support data related to one
    Implementation artifact on an ECU, in particular the RTE. The rapid
    prototyping support data may reference to elements provided for Mc
    SupportData.
    
    Package: M2::AUTOSARTemplates::CommonStructure::MeasurementCalibrationSupport::RptSupport::RptSupportData
    
    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 198, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines an environment for the execution of Executable.
        self._execution: List["RptExecutionContext"] = []

    @property
    def execution(self) -> List["RptExecutionContext"]:
        """Get execution (Pythonic accessor)."""
        return self._execution
        # Description of components for which rapid prototyping implemented.
        # atpVariation.
        self._rptComponent: List["RptComponent"] = []

    @property
    def rpt_component(self) -> List["RptComponent"]:
        """Get rptComponent (Pythonic accessor)."""
        return self._rptComponent
        # This aggregation represents the collection of service with the enclosing
        # RptSuportData atpVariation.
        self._rptServicePoint: List["RptServicePoint"] = []

    @property
    def rpt_service_point(self) -> List["RptServicePoint"]:
        """Get rptServicePoint (Pythonic accessor)."""
        return self._rptServicePoint

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getExecution(self) -> List["RptExecutionContext"]:
        """
        AUTOSAR-compliant getter for execution.
        
        Returns:
            The execution value
        
        Note:
            Delegates to execution property (CODING_RULE_V2_00017)
        """
        return self.execution  # Delegates to property

    def getRptComponent(self) -> List["RptComponent"]:
        """
        AUTOSAR-compliant getter for rptComponent.
        
        Returns:
            The rptComponent value
        
        Note:
            Delegates to rpt_component property (CODING_RULE_V2_00017)
        """
        return self.rpt_component  # Delegates to property

    def getRptServicePoint(self) -> List["RptServicePoint"]:
        """
        AUTOSAR-compliant getter for rptServicePoint.
        
        Returns:
            The rptServicePoint value
        
        Note:
            Delegates to rpt_service_point property (CODING_RULE_V2_00017)
        """
        return self.rpt_service_point  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class RptSwPrototypingAccess(ARObject):
    """
    Describes the accessibility of data and modes by the rapid prototyping
    tooling.
    
    Package: M2::AUTOSARTemplates::CommonStructure::MeasurementCalibrationSupport::RptSupport::RptSwPrototypingAccess
    
    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 199, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 856, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The related data element can be modified using a tool.
        # An ENABLED VariableData implicitly READABLE/WRITABLE.
        self._rptHookAccess: Optional["RptAccessEnum"] = None

    @property
    def rpt_hook_access(self) -> Optional["RptAccessEnum"]:
        """Get rptHookAccess (Pythonic accessor)."""
        return self._rptHookAccess

    @rpt_hook_access.setter
    def rpt_hook_access(self, value: Optional["RptAccessEnum"]) -> None:
        """
        Set rptHookAccess with validation.
        
        Args:
            value: The rptHookAccess to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rptHookAccess = None
            return

        if not isinstance(value, RptAccessEnum):
            raise TypeError(
                f"rptHookAccess must be RptAccessEnum or None, got {type(value).__name__}"
            )
        self._rptHookAccess = value
        # The related data element can be used as input for bypass RP tool.
        # If rptImplPolicy is not specified generation shall ensure at least suitable
                # MC are created.
        self._rptReadAccess: Optional["RptAccessEnum"] = None

    @property
    def rpt_read_access(self) -> Optional["RptAccessEnum"]:
        """Get rptReadAccess (Pythonic accessor)."""
        return self._rptReadAccess

    @rpt_read_access.setter
    def rpt_read_access(self, value: Optional["RptAccessEnum"]) -> None:
        """
        Set rptReadAccess with validation.
        
        Args:
            value: The rptReadAccess to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rptReadAccess = None
            return

        if not isinstance(value, RptAccessEnum):
            raise TypeError(
                f"rptReadAccess must be RptAccessEnum or None, got {type(value).__name__}"
            )
        self._rptReadAccess = value
        # The related data element can be used as output for by RP tool.
        # The data element shall to rptLevel2 and related write service points.
        self._rptWriteAccess: Optional["RptAccessEnum"] = None

    @property
    def rpt_write_access(self) -> Optional["RptAccessEnum"]:
        """Get rptWriteAccess (Pythonic accessor)."""
        return self._rptWriteAccess

    @rpt_write_access.setter
    def rpt_write_access(self, value: Optional["RptAccessEnum"]) -> None:
        """
        Set rptWriteAccess with validation.
        
        Args:
            value: The rptWriteAccess to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rptWriteAccess = None
            return

        if not isinstance(value, RptAccessEnum):
            raise TypeError(
                f"rptWriteAccess must be RptAccessEnum or None, got {type(value).__name__}"
            )
        self._rptWriteAccess = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getRptHookAccess(self) -> "RptAccessEnum":
        """
        AUTOSAR-compliant getter for rptHookAccess.
        
        Returns:
            The rptHookAccess value
        
        Note:
            Delegates to rpt_hook_access property (CODING_RULE_V2_00017)
        """
        return self.rpt_hook_access  # Delegates to property

    def setRptHookAccess(self, value: "RptAccessEnum") -> "RptSwPrototypingAccess":
        """
        AUTOSAR-compliant setter for rptHookAccess with method chaining.
        
        Args:
            value: The rptHookAccess to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to rpt_hook_access property setter (gets validation automatically)
        """
        self.rpt_hook_access = value  # Delegates to property setter
        return self

    def getRptReadAccess(self) -> "RptAccessEnum":
        """
        AUTOSAR-compliant getter for rptReadAccess.
        
        Returns:
            The rptReadAccess value
        
        Note:
            Delegates to rpt_read_access property (CODING_RULE_V2_00017)
        """
        return self.rpt_read_access  # Delegates to property

    def setRptReadAccess(self, value: "RptAccessEnum") -> "RptSwPrototypingAccess":
        """
        AUTOSAR-compliant setter for rptReadAccess with method chaining.
        
        Args:
            value: The rptReadAccess to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to rpt_read_access property setter (gets validation automatically)
        """
        self.rpt_read_access = value  # Delegates to property setter
        return self

    def getRptWriteAccess(self) -> "RptAccessEnum":
        """
        AUTOSAR-compliant getter for rptWriteAccess.
        
        Returns:
            The rptWriteAccess value
        
        Note:
            Delegates to rpt_write_access property (CODING_RULE_V2_00017)
        """
        return self.rpt_write_access  # Delegates to property

    def setRptWriteAccess(self, value: "RptAccessEnum") -> "RptSwPrototypingAccess":
        """
        AUTOSAR-compliant setter for rptWriteAccess with method chaining.
        
        Args:
            value: The rptWriteAccess to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to rpt_write_access property setter (gets validation automatically)
        """
        self.rpt_write_access = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_rpt_hook_access(self, value: Optional["RptAccessEnum"]) -> "RptSwPrototypingAccess":
        """
        Set rptHookAccess and return self for chaining.
        
        Args:
            value: The rptHookAccess to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_rpt_hook_access("value")
        """
        self.rpt_hook_access = value  # Use property setter (gets validation)
        return self

    def with_rpt_read_access(self, value: Optional["RptAccessEnum"]) -> "RptSwPrototypingAccess":
        """
        Set rptReadAccess and return self for chaining.
        
        Args:
            value: The rptReadAccess to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_rpt_read_access("value")
        """
        self.rpt_read_access = value  # Use property setter (gets validation)
        return self

    def with_rpt_write_access(self, value: Optional["RptAccessEnum"]) -> "RptSwPrototypingAccess":
        """
        Set rptWriteAccess and return self for chaining.
        
        Args:
            value: The rptWriteAccess to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_rpt_write_access("value")
        """
        self.rpt_write_access = value  # Use property setter (gets validation)
        return self



class RptComponent(Identifiable):
    """
    Description of component instance for which rapid prototyping support is
    implemented.
    
    Package: M2::AUTOSARTemplates::CommonStructure::MeasurementCalibrationSupport::RptSupport::RptComponent
    
    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 199, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to related McDataElement describing the implementation of "RP
        # global buffer", "RP global "RP enabler flag" and the "RP flag".
        self._mcData: List["RoleBasedMcData"] = []

    @property
    def mc_data(self) -> List["RoleBasedMcData"]:
        """Get mcData (Pythonic accessor)."""
        return self._mcData
        # Describes the implemented code preparation for rapid data accesses.
        self._rpImplPolicy: Optional["RptImplPolicy"] = None

    @property
    def rp_impl_policy(self) -> Optional["RptImplPolicy"]:
        """Get rpImplPolicy (Pythonic accessor)."""
        return self._rpImplPolicy

    @rp_impl_policy.setter
    def rp_impl_policy(self, value: Optional["RptImplPolicy"]) -> None:
        """
        Set rpImplPolicy with validation.
        
        Args:
            value: The rpImplPolicy to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rpImplPolicy = None
            return

        if not isinstance(value, RptImplPolicy):
            raise TypeError(
                f"rpImplPolicy must be RptImplPolicy or None, got {type(value).__name__}"
            )
        self._rpImplPolicy = value
        # ExecutableEntity instance which can be bypassed.
        # atpSplitable; atpVariation.
        self._rptExecutable: List["RptExecutableEntity"] = []

    @property
    def rpt_executable(self) -> List["RptExecutableEntity"]:
        """Get rptExecutable (Pythonic accessor)."""
        return self._rptExecutable

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMcData(self) -> List["RoleBasedMcData"]:
        """
        AUTOSAR-compliant getter for mcData.
        
        Returns:
            The mcData value
        
        Note:
            Delegates to mc_data property (CODING_RULE_V2_00017)
        """
        return self.mc_data  # Delegates to property

    def getRpImplPolicy(self) -> "RptImplPolicy":
        """
        AUTOSAR-compliant getter for rpImplPolicy.
        
        Returns:
            The rpImplPolicy value
        
        Note:
            Delegates to rp_impl_policy property (CODING_RULE_V2_00017)
        """
        return self.rp_impl_policy  # Delegates to property

    def setRpImplPolicy(self, value: "RptImplPolicy") -> "RptComponent":
        """
        AUTOSAR-compliant setter for rpImplPolicy with method chaining.
        
        Args:
            value: The rpImplPolicy to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to rp_impl_policy property setter (gets validation automatically)
        """
        self.rp_impl_policy = value  # Delegates to property setter
        return self

    def getRptExecutable(self) -> List["RptExecutableEntity"]:
        """
        AUTOSAR-compliant getter for rptExecutable.
        
        Returns:
            The rptExecutable value
        
        Note:
            Delegates to rpt_executable property (CODING_RULE_V2_00017)
        """
        return self.rpt_executable  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_rp_impl_policy(self, value: Optional["RptImplPolicy"]) -> "RptComponent":
        """
        Set rpImplPolicy and return self for chaining.
        
        Args:
            value: The rpImplPolicy to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_rp_impl_policy("value")
        """
        self.rp_impl_policy = value  # Use property setter (gets validation)
        return self



class RptExecutableEntity(Identifiable):
    """
    This describes a ExecutableEntity instance which can be bypassed.
    
    Package: M2::AUTOSARTemplates::CommonStructure::MeasurementCalibrationSupport::RptSupport::RptExecutableEntity
    
    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 200, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # ExecutableEntity event instance activation the owning Rpt ExecutableEntity.
        # atpVariation.
        self._rptExecutable: List["RptExecutableEntity"] = []

    @property
    def rpt_executable(self) -> List["RptExecutableEntity"]:
        """Get rptExecutable (Pythonic accessor)."""
        return self._rptExecutable
        # read access to a variable atpSplitable; atpVariation.
        self._rptRead: List["RoleBasedMcData"] = []

    @property
    def rpt_read(self) -> List["RoleBasedMcData"]:
        """Get rptRead (Pythonic accessor)."""
        return self._rptRead
        # write access to a variable atpSplitable; atpVariation.
        self._rptWrite: List["RoleBasedMcData"] = []

    @property
    def rpt_write(self) -> List["RoleBasedMcData"]:
        """Get rptWrite (Pythonic accessor)."""
        return self._rptWrite
        # The symbol describing this ExecutableEntity’s entry point.
        self._symbol: Optional["CIdentifier"] = None

    @property
    def symbol(self) -> Optional["CIdentifier"]:
        """Get symbol (Pythonic accessor)."""
        return self._symbol

    @symbol.setter
    def symbol(self, value: Optional["CIdentifier"]) -> None:
        """
        Set symbol with validation.
        
        Args:
            value: The symbol to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._symbol = None
            return

        if not isinstance(value, CIdentifier):
            raise TypeError(
                f"symbol must be CIdentifier or None, got {type(value).__name__}"
            )
        self._symbol = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getRptExecutable(self) -> List["RptExecutableEntity"]:
        """
        AUTOSAR-compliant getter for rptExecutable.
        
        Returns:
            The rptExecutable value
        
        Note:
            Delegates to rpt_executable property (CODING_RULE_V2_00017)
        """
        return self.rpt_executable  # Delegates to property

    def getRptRead(self) -> List["RoleBasedMcData"]:
        """
        AUTOSAR-compliant getter for rptRead.
        
        Returns:
            The rptRead value
        
        Note:
            Delegates to rpt_read property (CODING_RULE_V2_00017)
        """
        return self.rpt_read  # Delegates to property

    def getRptWrite(self) -> List["RoleBasedMcData"]:
        """
        AUTOSAR-compliant getter for rptWrite.
        
        Returns:
            The rptWrite value
        
        Note:
            Delegates to rpt_write property (CODING_RULE_V2_00017)
        """
        return self.rpt_write  # Delegates to property

    def getSymbol(self) -> "CIdentifier":
        """
        AUTOSAR-compliant getter for symbol.
        
        Returns:
            The symbol value
        
        Note:
            Delegates to symbol property (CODING_RULE_V2_00017)
        """
        return self.symbol  # Delegates to property

    def setSymbol(self, value: "CIdentifier") -> "RptExecutableEntity":
        """
        AUTOSAR-compliant setter for symbol with method chaining.
        
        Args:
            value: The symbol to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to symbol property setter (gets validation automatically)
        """
        self.symbol = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_symbol(self, value: Optional["CIdentifier"]) -> "RptExecutableEntity":
        """
        Set symbol and return self for chaining.
        
        Args:
            value: The symbol to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_symbol("value")
        """
        self.symbol = value  # Use property setter (gets validation)
        return self



class RptExecutableEntityEvent(Identifiable):
    """
    This describes an ExecutableEntity event instance which can be bypassed.
    
    Package: M2::AUTOSARTemplates::CommonStructure::MeasurementCalibrationSupport::RptSupport::RptExecutableEntityEvent
    
    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 201, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This describes the context in which the event of the entity is executed.
        self._execution: List["RptExecutionContext"] = []

    @property
    def execution(self) -> List["RptExecutionContext"]:
        """Get execution (Pythonic accessor)."""
        return self._execution
        # Reference to related McDataElements describing the implementation of "RP
        # runnable disabler flag" and flag" roles of the RoleBasedMcData are:.
        self._mcData: List["RoleBasedMcData"] = []

    @property
    def mc_data(self) -> List["RoleBasedMcData"]:
        """Get mcData (Pythonic accessor)."""
        return self._mcData
        # RPT event id used for service points call.
        self._rptEventId: Optional["PositiveInteger"] = None

    @property
    def rpt_event_id(self) -> Optional["PositiveInteger"]:
        """Get rptEventId (Pythonic accessor)."""
        return self._rptEventId

    @rpt_event_id.setter
    def rpt_event_id(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set rptEventId with validation.
        
        Args:
            value: The rptEventId to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rptEventId = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"rptEventId must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._rptEventId = value
        # Describes the implemented code preparation for rapid prototyping at
        # ExecutableEntity invocation.
        self._rptExecutable: Optional["RptExecutableEntity"] = None

    @property
    def rpt_executable(self) -> Optional["RptExecutableEntity"]:
        """Get rptExecutable (Pythonic accessor)."""
        return self._rptExecutable

    @rpt_executable.setter
    def rpt_executable(self, value: Optional["RptExecutableEntity"]) -> None:
        """
        Set rptExecutable with validation.
        
        Args:
            value: The rptExecutable to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rptExecutable = None
            return

        if not isinstance(value, RptExecutableEntity):
            raise TypeError(
                f"rptExecutable must be RptExecutableEntity or None, got {type(value).__name__}"
            )
        self._rptExecutable = value
        # Describes the RptImplPolicy of a RptExecutableEvent for bypassing.
        self._rptImplPolicy: Optional["RptImplPolicy"] = None

    @property
    def rpt_impl_policy(self) -> Optional["RptImplPolicy"]:
        """Get rptImplPolicy (Pythonic accessor)."""
        return self._rptImplPolicy

    @rpt_impl_policy.setter
    def rpt_impl_policy(self, value: Optional["RptImplPolicy"]) -> None:
        """
        Set rptImplPolicy with validation.
        
        Args:
            value: The rptImplPolicy to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rptImplPolicy = None
            return

        if not isinstance(value, RptImplPolicy):
            raise TypeError(
                f"rptImplPolicy must be RptImplPolicy or None, got {type(value).__name__}"
            )
        self._rptImplPolicy = value
        # This describes the applicable Pre Service Points for a / BswEvent of a
        # bypassed ExecutableEntity.
        self._rptServicePoint: List["RptServicePoint"] = []

    @property
    def rpt_service_point(self) -> List["RptServicePoint"]:
        """Get rptServicePoint (Pythonic accessor)."""
        return self._rptServicePoint

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getExecution(self) -> List["RptExecutionContext"]:
        """
        AUTOSAR-compliant getter for execution.
        
        Returns:
            The execution value
        
        Note:
            Delegates to execution property (CODING_RULE_V2_00017)
        """
        return self.execution  # Delegates to property

    def getMcData(self) -> List["RoleBasedMcData"]:
        """
        AUTOSAR-compliant getter for mcData.
        
        Returns:
            The mcData value
        
        Note:
            Delegates to mc_data property (CODING_RULE_V2_00017)
        """
        return self.mc_data  # Delegates to property

    def getRptEventId(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for rptEventId.
        
        Returns:
            The rptEventId value
        
        Note:
            Delegates to rpt_event_id property (CODING_RULE_V2_00017)
        """
        return self.rpt_event_id  # Delegates to property

    def setRptEventId(self, value: "PositiveInteger") -> "RptExecutableEntityEvent":
        """
        AUTOSAR-compliant setter for rptEventId with method chaining.
        
        Args:
            value: The rptEventId to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to rpt_event_id property setter (gets validation automatically)
        """
        self.rpt_event_id = value  # Delegates to property setter
        return self

    def getRptExecutable(self) -> "RptExecutableEntity":
        """
        AUTOSAR-compliant getter for rptExecutable.
        
        Returns:
            The rptExecutable value
        
        Note:
            Delegates to rpt_executable property (CODING_RULE_V2_00017)
        """
        return self.rpt_executable  # Delegates to property

    def setRptExecutable(self, value: "RptExecutableEntity") -> "RptExecutableEntityEvent":
        """
        AUTOSAR-compliant setter for rptExecutable with method chaining.
        
        Args:
            value: The rptExecutable to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to rpt_executable property setter (gets validation automatically)
        """
        self.rpt_executable = value  # Delegates to property setter
        return self

    def getRptImplPolicy(self) -> "RptImplPolicy":
        """
        AUTOSAR-compliant getter for rptImplPolicy.
        
        Returns:
            The rptImplPolicy value
        
        Note:
            Delegates to rpt_impl_policy property (CODING_RULE_V2_00017)
        """
        return self.rpt_impl_policy  # Delegates to property

    def setRptImplPolicy(self, value: "RptImplPolicy") -> "RptExecutableEntityEvent":
        """
        AUTOSAR-compliant setter for rptImplPolicy with method chaining.
        
        Args:
            value: The rptImplPolicy to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to rpt_impl_policy property setter (gets validation automatically)
        """
        self.rpt_impl_policy = value  # Delegates to property setter
        return self

    def getRptServicePoint(self) -> List["RptServicePoint"]:
        """
        AUTOSAR-compliant getter for rptServicePoint.
        
        Returns:
            The rptServicePoint value
        
        Note:
            Delegates to rpt_service_point property (CODING_RULE_V2_00017)
        """
        return self.rpt_service_point  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_rpt_event_id(self, value: Optional["PositiveInteger"]) -> "RptExecutableEntityEvent":
        """
        Set rptEventId and return self for chaining.
        
        Args:
            value: The rptEventId to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_rpt_event_id("value")
        """
        self.rpt_event_id = value  # Use property setter (gets validation)
        return self

    def with_rpt_executable(self, value: Optional["RptExecutableEntity"]) -> "RptExecutableEntityEvent":
        """
        Set rptExecutable and return self for chaining.
        
        Args:
            value: The rptExecutable to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_rpt_executable("value")
        """
        self.rpt_executable = value  # Use property setter (gets validation)
        return self

    def with_rpt_impl_policy(self, value: Optional["RptImplPolicy"]) -> "RptExecutableEntityEvent":
        """
        Set rptImplPolicy and return self for chaining.
        
        Args:
            value: The rptImplPolicy to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_rpt_impl_policy("value")
        """
        self.rpt_impl_policy = value  # Use property setter (gets validation)
        return self



class RptExecutionContext(Identifiable):
    """
    Defines an environment for the execution of ExecutableEntites which is
    qualified by • OSTask • communication buffer usage
    
    Package: M2::AUTOSARTemplates::CommonStructure::MeasurementCalibrationSupport::RptSupport::RptExecutionContext
    
    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 205, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class RptServicePoint(Identifiable):
    """
    Description of a Service Point implemented for rapid prototyping.
    
    Package: M2::AUTOSARTemplates::CommonStructure::MeasurementCalibrationSupport::RptSupport::RptServicePoint
    
    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 206, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Unique ID (Range: 0.
        # 65535) representing the service.
        self._serviceId: Optional["PositiveInteger"] = None

    @property
    def service_id(self) -> Optional["PositiveInteger"]:
        """Get serviceId (Pythonic accessor)."""
        return self._serviceId

    @service_id.setter
    def service_id(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set serviceId with validation.
        
        Args:
            value: The serviceId to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._serviceId = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"serviceId must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._serviceId = value
        # Complete symbol of the function implementing the This symbol is used for
        # post-build hooking.
        self._symbol: Optional["CIdentifier"] = None

    @property
    def symbol(self) -> Optional["CIdentifier"]:
        """Get symbol (Pythonic accessor)."""
        return self._symbol

    @symbol.setter
    def symbol(self, value: Optional["CIdentifier"]) -> None:
        """
        Set symbol with validation.
        
        Args:
            value: The symbol to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._symbol = None
            return

        if not isinstance(value, CIdentifier):
            raise TypeError(
                f"symbol must be CIdentifier or None, got {type(value).__name__}"
            )
        self._symbol = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getServiceId(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for serviceId.
        
        Returns:
            The serviceId value
        
        Note:
            Delegates to service_id property (CODING_RULE_V2_00017)
        """
        return self.service_id  # Delegates to property

    def setServiceId(self, value: "PositiveInteger") -> "RptServicePoint":
        """
        AUTOSAR-compliant setter for serviceId with method chaining.
        
        Args:
            value: The serviceId to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to service_id property setter (gets validation automatically)
        """
        self.service_id = value  # Delegates to property setter
        return self

    def getSymbol(self) -> "CIdentifier":
        """
        AUTOSAR-compliant getter for symbol.
        
        Returns:
            The symbol value
        
        Note:
            Delegates to symbol property (CODING_RULE_V2_00017)
        """
        return self.symbol  # Delegates to property

    def setSymbol(self, value: "CIdentifier") -> "RptServicePoint":
        """
        AUTOSAR-compliant setter for symbol with method chaining.
        
        Args:
            value: The symbol to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to symbol property setter (gets validation automatically)
        """
        self.symbol = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_service_id(self, value: Optional["PositiveInteger"]) -> "RptServicePoint":
        """
        Set serviceId and return self for chaining.
        
        Args:
            value: The serviceId to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_service_id("value")
        """
        self.service_id = value  # Use property setter (gets validation)
        return self

    def with_symbol(self, value: Optional["CIdentifier"]) -> "RptServicePoint":
        """
        Set symbol and return self for chaining.
        
        Args:
            value: The symbol to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_symbol("value")
        """
        self.symbol = value  # Use property setter (gets validation)
        return self


class RptEnablerImplTypeEnum(AREnum):
    """
    RptEnablerImplTypeEnum enumeration

Describes the required / implemented usage of enabler flags for data access in the code. Aggregated by RptImplPolicy.rptEnablerImplType, RptProfile.stimEnabler

Package: M2::AUTOSARTemplates::CommonStructure::MeasurementCalibrationSupport::RptSupport
    """
    # No "RP enabler" is implemented.
    none = "0"

    # "RP enabler" is implemented as a RAM variable
    rptEnablerRam = "1"

    # The RTE generator implements both the RAM and ROM "RP enabler".
    rptEnablerRamAndRom = "3"

    # "RP enabler" is implemented as a calibrateable ROM variable.
    rptEnablerRom = "2"



class RptPreparationEnum(AREnum):
    """
    RptPreparationEnum enumeration

Determines the RP preparation level for access to VariableDataPrototypes within the generated RTE implementation. Aggregated by RptImplPolicy.rptPreparationLevel

Package: M2::AUTOSARTemplates::CommonStructure::MeasurementCalibrationSupport::RptSupport
    """
    # No RP preparation for VariableDataPrototype.
    none = "0"

    # The RTE implementation uses an "RP global buffer" for measurement and post-build hooking
    rptLevel1 = "1"

    # As rpLevel1 but the RTE implementation also uses both "RP enabler flag" to permit RP overwrite at
    rptLevel2 = "2"

    # As rpLevel2 but the RTE implementation also uses "RP global measurement buffer" to record the
    rptLevel3 = "None"

    # ECU-generated value in addition to the RP value.
    original = "3"



class RptExecutionControlEnum(AREnum):
    """
    RptExecutionControlEnum enumeration

Determines rapid prototyping preparation of an ExecutableEntity. Aggregated by RptExecutableEntityProperties.rptExecutionControl

Package: M2::AUTOSARTemplates::CommonStructure::MeasurementCalibrationSupport::RptSupport
    """
    # The ExecutableEntity is only executed when the rapid prototyping disable flag is NOT set.
    conditional = "0"

    # The ExecutableEntity is executed without specific rapid prototyping condition.
    none = "1"



class RptAccessEnum(AREnum):
    """
    RptAccessEnum enumeration

Determines the access rights to a data object with respect to rapid prototyping. Aggregated by RptSwPrototypingAccess.rptHookAccess, RptSwPrototypingAccess.rptReadAccess, RptSw PrototypingAccess.rptWriteAccess

Package: M2::AUTOSARTemplates::CommonStructure::MeasurementCalibrationSupport::RptSupport
    """
    # The related data element is accessible by RP tool.
    enabled = "0"

    # The related data element is not accessible by RP tool.
    none = "1"

    # The data element is known to the RP tool however its usage for RP can be restricted. Use case: limitation based on access rights
    protected = "2"

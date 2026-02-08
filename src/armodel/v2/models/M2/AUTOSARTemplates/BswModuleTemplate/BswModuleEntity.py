from abc import ABC
from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior import ExecutableEntity

    RefType,
)


class BswModuleEntity(ExecutableEntity, ABC):
    """
    Specifies the smallest code fragment which can be described for a BSW module
    or cluster within AUTOSAR.

    Package: M2::AUTOSARTemplates::BswModuleTemplate::BswBehavior

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 70, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 215, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 429, Foundation
      R23-11)
    """
    def __init__(self):
        if type(self) is BswModuleEntity:
            raise TypeError("BswModuleEntity is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # A mode group which is accessed via API call by this entity.
        # It shall be a ModeDeclarationGroupPrototype this module or cluster.
        # atpVariation.
        self._accessedMode: List[RefType] = []

    @property
    def accessed_mode(self) -> List[RefType]:
        """Get accessedMode (Pythonic accessor)."""
        return self._accessedMode
        # Activation point used by the module entity to activate one more internal
                # triggers.
        # atpVariation.
        self._activationPoint: List[RefType] = []

    @property
    def activation_point(self) -> List[RefType]:
        """Get activationPoint (Pythonic accessor)."""
        return self._activationPoint
        # A call point used in the code of this entity.
        # of this association is especially targeted at It is possible to have one
                # variant calling AUTOSAR debug module and another one which atpVariation.
        self._callPoint: List["BswModuleCallPoint"] = []

    @property
    def call_point(self) -> List["BswModuleCallPoint"]:
        """Get callPoint (Pythonic accessor)."""
        return self._callPoint
        # The data is received via the BSW Scheduler.
        # atpSplitable; atpVariation.
        self._dataReceive: List["BswVariableAccess"] = []

    @property
    def data_receive(self) -> List["BswVariableAccess"]:
        """Get dataReceive (Pythonic accessor)."""
        return self._dataReceive
        # The data is sent via the BSW Scheduler.
        # atpVariation.
        self._dataSendPoint: List["BswVariableAccess"] = []

    @property
    def data_send_point(self) -> List["BswVariableAccess"]:
        """Get dataSendPoint (Pythonic accessor)."""
        return self._dataSendPoint
        # The entry which is implemented by this module entity.
        self._implemented: Optional["BswModuleEntry"] = None

    @property
    def implemented(self) -> Optional["BswModuleEntry"]:
        """Get implemented (Pythonic accessor)."""
        return self._implemented

    @implemented.setter
    def implemented(self, value: Optional["BswModuleEntry"]) -> None:
        """
        Set implemented with validation.

        Args:
            value: The implemented to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._implemented = None
            return

        if not isinstance(value, BswModuleEntry):
            raise TypeError(
                f"implemented must be BswModuleEntry or None, got {type(value).__name__}"
            )
        self._implemented = value
        # A trigger issued by this entity via BSW Scheduler API call.
        # be a BswTrigger released (i.
        # e.
        # owned) by this cluster.
        # atpVariation 381 Document ID 89: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate
                # Module Description Template R23-11.
        self._issuedTrigger: List[RefType] = []

    @property
    def issued_trigger(self) -> List[RefType]:
        """Get issuedTrigger (Pythonic accessor)."""
        return self._issuedTrigger
        # A mode group which is managed by this entity.
        # It shall be a ModeDeclarationGroupPrototype provided by this cluster.
        # atpVariation.
        self._managedMode: List[RefType] = []

    @property
    def managed_mode(self) -> List[RefType]:
        """Get managedMode (Pythonic accessor)."""
        return self._managedMode
        # A prefix to be used in generated names for the Bsw ModuleScheduler in the
                # context of this BswModuleEntity, entry point prototypes, macros for dealing
                # areas, header file names.
        # defined in the SWS RTE.
        # supersedes default rules for the prefix of those.
        self._schedulerName: Optional["BswSchedulerName"] = None

    @property
    def scheduler_name(self) -> Optional["BswSchedulerName"]:
        """Get schedulerName (Pythonic accessor)."""
        return self._schedulerName

    @scheduler_name.setter
    def scheduler_name(self, value: Optional["BswSchedulerName"]) -> None:
        """
        Set schedulerName with validation.

        Args:
            value: The schedulerName to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._schedulerName = None
            return

        if not isinstance(value, BswSchedulerName):
            raise TypeError(
                f"schedulerName must be BswSchedulerName or None, got {type(value).__name__}"
            )
        self._schedulerName = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAccessedMode(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for accessedMode.

        Returns:
            The accessedMode value

        Note:
            Delegates to accessed_mode property (CODING_RULE_V2_00017)
        """
        return self.accessed_mode  # Delegates to property

    def getActivationPoint(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for activationPoint.

        Returns:
            The activationPoint value

        Note:
            Delegates to activation_point property (CODING_RULE_V2_00017)
        """
        return self.activation_point  # Delegates to property

    def getCallPoint(self) -> List["BswModuleCallPoint"]:
        """
        AUTOSAR-compliant getter for callPoint.

        Returns:
            The callPoint value

        Note:
            Delegates to call_point property (CODING_RULE_V2_00017)
        """
        return self.call_point  # Delegates to property

    def getDataReceive(self) -> List["BswVariableAccess"]:
        """
        AUTOSAR-compliant getter for dataReceive.

        Returns:
            The dataReceive value

        Note:
            Delegates to data_receive property (CODING_RULE_V2_00017)
        """
        return self.data_receive  # Delegates to property

    def getDataSendPoint(self) -> List["BswVariableAccess"]:
        """
        AUTOSAR-compliant getter for dataSendPoint.

        Returns:
            The dataSendPoint value

        Note:
            Delegates to data_send_point property (CODING_RULE_V2_00017)
        """
        return self.data_send_point  # Delegates to property

    def getImplemented(self) -> "BswModuleEntry":
        """
        AUTOSAR-compliant getter for implemented.

        Returns:
            The implemented value

        Note:
            Delegates to implemented property (CODING_RULE_V2_00017)
        """
        return self.implemented  # Delegates to property

    def setImplemented(self, value: "BswModuleEntry") -> "BswModuleEntity":
        """
        AUTOSAR-compliant setter for implemented with method chaining.

        Args:
            value: The implemented to set

        Returns:
            self for method chaining

        Note:
            Delegates to implemented property setter (gets validation automatically)
        """
        self.implemented = value  # Delegates to property setter
        return self

    def getIssuedTrigger(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for issuedTrigger.

        Returns:
            The issuedTrigger value

        Note:
            Delegates to issued_trigger property (CODING_RULE_V2_00017)
        """
        return self.issued_trigger  # Delegates to property

    def getManagedMode(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for managedMode.

        Returns:
            The managedMode value

        Note:
            Delegates to managed_mode property (CODING_RULE_V2_00017)
        """
        return self.managed_mode  # Delegates to property

    def getSchedulerName(self) -> "BswSchedulerName":
        """
        AUTOSAR-compliant getter for schedulerName.

        Returns:
            The schedulerName value

        Note:
            Delegates to scheduler_name property (CODING_RULE_V2_00017)
        """
        return self.scheduler_name  # Delegates to property

    def setSchedulerName(self, value: "BswSchedulerName") -> "BswModuleEntity":
        """
        AUTOSAR-compliant setter for schedulerName with method chaining.

        Args:
            value: The schedulerName to set

        Returns:
            self for method chaining

        Note:
            Delegates to scheduler_name property setter (gets validation automatically)
        """
        self.scheduler_name = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_implemented(self, value: Optional["BswModuleEntry"]) -> "BswModuleEntity":
        """
        Set implemented and return self for chaining.

        Args:
            value: The implemented to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_implemented("value")
        """
        self.implemented = value  # Use property setter (gets validation)
        return self

    def with_scheduler_name(self, value: Optional["BswSchedulerName"]) -> "BswModuleEntity":
        """
        Set schedulerName and return self for chaining.

        Args:
            value: The schedulerName to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_scheduler_name("value")
        """
        self.scheduler_name = value  # Use property setter (gets validation)
        return self

"""
AUTOSAR Package - BswOverview

Package: M2::AUTOSARTemplates::BswModuleTemplate::BswOverview
"""


from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    RefType,
)


class BswModuleDescription(ARElement):
    """
    Root element for the description of a single BSW module or BSW cluster. In
    case it describes a BSW module, the short name of this element equals the
    name of the BSW module.

    Package: M2::AUTOSARTemplates::BswModuleTemplate::BswOverview::BswModuleDescription

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 26, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 303, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 973, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 212, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 426, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 168, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This adds a documentation to the BSW module.
        # Stereotypes: atpSplitable; atpVariation 381 Document ID 89:
                # AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate Module Description Template
                # R23-11.
        self._bswModule: Optional["SwComponent"] = None

    @property
    def bsw_module(self) -> Optional["SwComponent"]:
        """Get bswModule (Pythonic accessor)."""
        return self._bswModule

    @bsw_module.setter
    def bsw_module(self, value: Optional["SwComponent"]) -> None:
        """
        Set bswModule with validation.

        Args:
            value: The bswModule to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._bswModule = None
            return

        if not isinstance(value, SwComponent):
            raise TypeError(
                f"bswModule must be SwComponent or None, got {type(value).__name__}"
            )
        self._bswModule = value
        # Indicates an entry which is required by this module.
        # outgoingCallback / requiredEntry.
        # atpVariation.
        self._expectedEntry: List[BswModuleEntry] = []

    @property
    def expected_entry(self) -> List[BswModuleEntry]:
        """Get expectedEntry (Pythonic accessor)."""
        return self._expectedEntry
        # Specifies an entry provided by this module which can be by other modules.
        # This includes "main" functions, and callbacks.
        # Replacement of expectedCallback.
        # atpVariation.
        self._implemented: List[BswModuleEntry] = []

    @property
    def implemented(self) -> List[BswModuleEntry]:
        """Get implemented (Pythonic accessor)."""
        return self._implemented
        # The various BswInternalBehaviors associated with a Bsw be distributed over
        # several Therefore the aggregation is <<atp.
        self._internalBehavior: List[BswInternalBehavior] = []

    @property
    def internal_behavior(self) -> List[BswInternalBehavior]:
        """Get internalBehavior (Pythonic accessor)."""
        return self._internalBehavior
        # Refers to the BSW Module Identifier defined by the For non-standardized
        # modules, a can be optionally chosen.
        self._moduleId: Optional[PositiveInteger] = None

    @property
    def module_id(self) -> Optional[PositiveInteger]:
        """Get moduleId (Pythonic accessor)."""
        return self._moduleId

    @module_id.setter
    def module_id(self, value: Optional[PositiveInteger]) -> None:
        """
        Set moduleId with validation.

        Args:
            value: The moduleId to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._moduleId = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"moduleId must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._moduleId = value
        # Specifies that this module provides a client server entry which can be called
                # from another partition or core.
        # This declared locally to this context and will be the
                # requiredClientServerEntry of another or module via the configuration of the
                # BSW atpVariation.
        self._providedClient: List["BswModuleClientServer"] = []

    @property
    def provided_client(self) -> List["BswModuleClientServer"]:
        """Get providedClient (Pythonic accessor)."""
        return self._providedClient
        # Specifies a data prototype provided by this module in be read from another
                # partition or core.
        # The declared locally to this context and will be the requiredData of another
                # or the same the configuration of the BSW Scheduler.
        # atpVariation 381 Document ID 89: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate
                # Module Description Template R23-11.
        self._providedData: List[RefType] = []

    @property
    def provided_data(self) -> List[RefType]:
        """Get providedData (Pythonic accessor)."""
        return self._providedData
        # A set of modes which is owned and provided by this module or cluster.
        # It can be connected to the required other modules or clusters via the the
                # BswScheduler.
        # It can also be modes provided via ports by an EcuAbstraction
                # ComplexDeviceDriverSw atpVariation.
        self._providedMode: List[RefType] = []

    @property
    def provided_mode(self) -> List[RefType]:
        """Get providedMode (Pythonic accessor)."""
        return self._providedMode
        # A Trigger released by this module or cluster.
        # It can be the requiredTriggers of other modules or the configuration of the
                # BswScheduler.
        # It can synchronized with Triggers provided via ports by
                # ServiceSwComponentType, Ecu ComplexDeviceDriver atpVariation.
        self._releasedTrigger: List[RefType] = []

    @property
    def released_trigger(self) -> List[RefType]:
        """Get releasedTrigger (Pythonic accessor)."""
        return self._releasedTrigger
        # Specifies that this module requires a client server entry which can be
        # implemented on another partition or is declared locally to this context and
        # will to the providedClientServerEntry of another same module via the
        # configuration of the BSW atpVariation.
        self._requiredClient: List["BswModuleClientServer"] = []

    @property
    def required_client(self) -> List["BswModuleClientServer"]:
        """Get requiredClient (Pythonic accessor)."""
        return self._requiredClient
        # Specifies a data prototype required by this module in oder provided from
                # another partition or core.
        # The required declared locally to this context and will be the providedData of
                # another or the same the configuration of the BswScheduler.
        # atpVariation 381 Document ID 89: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate
                # Module Description Template R23-11.
        self._requiredData: List[RefType] = []

    @property
    def required_data(self) -> List[RefType]:
        """Get requiredData (Pythonic accessor)."""
        return self._requiredData
        # Specifies that this module or cluster depends on a certain mode group.
        # The requiredModeGroup is local to this will be connected to the
                # providedModeGroup module or cluster via the configuration of the
                # atpVariation.
        self._requiredMode: List[RefType] = []

    @property
    def required_mode(self) -> List[RefType]:
        """Get requiredMode (Pythonic accessor)."""
        return self._requiredMode
        # Specifies that this module or cluster reacts upon an requiredTrigger is
        # declared locally to and will be connected to the providedTrigger module or
        # cluster via the configuration of the atpVariation.
        self._requiredTrigger: List[RefType] = []

    @property
    def required_trigger(self) -> List[RefType]:
        """Get requiredTrigger (Pythonic accessor)."""
        return self._requiredTrigger

    def with_expected_entry(self, value):
        """
        Set expected_entry and return self for chaining.

        Args:
            value: The expected_entry to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_expected_entry("value")
        """
        self.expected_entry = value  # Use property setter (gets validation)
        return self

    def with_implemented(self, value):
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

    def with_internal_behavior(self, value):
        """
        Set internal_behavior and return self for chaining.

        Args:
            value: The internal_behavior to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_internal_behavior("value")
        """
        self.internal_behavior = value  # Use property setter (gets validation)
        return self

    def with_provided_client(self, value):
        """
        Set provided_client and return self for chaining.

        Args:
            value: The provided_client to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_provided_client("value")
        """
        self.provided_client = value  # Use property setter (gets validation)
        return self

    def with_provided_data(self, value):
        """
        Set provided_data and return self for chaining.

        Args:
            value: The provided_data to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_provided_data("value")
        """
        self.provided_data = value  # Use property setter (gets validation)
        return self

    def with_provided_mode(self, value):
        """
        Set provided_mode and return self for chaining.

        Args:
            value: The provided_mode to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_provided_mode("value")
        """
        self.provided_mode = value  # Use property setter (gets validation)
        return self

    def with_released_trigger(self, value):
        """
        Set released_trigger and return self for chaining.

        Args:
            value: The released_trigger to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_released_trigger("value")
        """
        self.released_trigger = value  # Use property setter (gets validation)
        return self

    def with_required_client(self, value):
        """
        Set required_client and return self for chaining.

        Args:
            value: The required_client to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_required_client("value")
        """
        self.required_client = value  # Use property setter (gets validation)
        return self

    def with_required_data(self, value):
        """
        Set required_data and return self for chaining.

        Args:
            value: The required_data to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_required_data("value")
        """
        self.required_data = value  # Use property setter (gets validation)
        return self

    def with_required_mode(self, value):
        """
        Set required_mode and return self for chaining.

        Args:
            value: The required_mode to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_required_mode("value")
        """
        self.required_mode = value  # Use property setter (gets validation)
        return self

    def with_required_trigger(self, value):
        """
        Set required_trigger and return self for chaining.

        Args:
            value: The required_trigger to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_required_trigger("value")
        """
        self.required_trigger = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBswModule(self) -> "SwComponent":
        """
        AUTOSAR-compliant getter for bswModule.

        Returns:
            The bswModule value

        Note:
            Delegates to bsw_module property (CODING_RULE_V2_00017)
        """
        return self.bsw_module  # Delegates to property

    def setBswModule(self, value: "SwComponent") -> BswModuleDescription:
        """
        AUTOSAR-compliant setter for bswModule with method chaining.

        Args:
            value: The bswModule to set

        Returns:
            self for method chaining

        Note:
            Delegates to bsw_module property setter (gets validation automatically)
        """
        self.bsw_module = value  # Delegates to property setter
        return self

    def getExpectedEntry(self) -> List[BswModuleEntry]:
        """
        AUTOSAR-compliant getter for expectedEntry.

        Returns:
            The expectedEntry value

        Note:
            Delegates to expected_entry property (CODING_RULE_V2_00017)
        """
        return self.expected_entry  # Delegates to property

    def getImplemented(self) -> List[BswModuleEntry]:
        """
        AUTOSAR-compliant getter for implemented.

        Returns:
            The implemented value

        Note:
            Delegates to implemented property (CODING_RULE_V2_00017)
        """
        return self.implemented  # Delegates to property

    def getInternalBehavior(self) -> List[BswInternalBehavior]:
        """
        AUTOSAR-compliant getter for internalBehavior.

        Returns:
            The internalBehavior value

        Note:
            Delegates to internal_behavior property (CODING_RULE_V2_00017)
        """
        return self.internal_behavior  # Delegates to property

    def getModuleId(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for moduleId.

        Returns:
            The moduleId value

        Note:
            Delegates to module_id property (CODING_RULE_V2_00017)
        """
        return self.module_id  # Delegates to property

    def setModuleId(self, value: PositiveInteger) -> BswModuleDescription:
        """
        AUTOSAR-compliant setter for moduleId with method chaining.

        Args:
            value: The moduleId to set

        Returns:
            self for method chaining

        Note:
            Delegates to module_id property setter (gets validation automatically)
        """
        self.module_id = value  # Delegates to property setter
        return self

    def getProvidedClient(self) -> List["BswModuleClientServer"]:
        """
        AUTOSAR-compliant getter for providedClient.

        Returns:
            The providedClient value

        Note:
            Delegates to provided_client property (CODING_RULE_V2_00017)
        """
        return self.provided_client  # Delegates to property

    def getProvidedData(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for providedData.

        Returns:
            The providedData value

        Note:
            Delegates to provided_data property (CODING_RULE_V2_00017)
        """
        return self.provided_data  # Delegates to property

    def getProvidedMode(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for providedMode.

        Returns:
            The providedMode value

        Note:
            Delegates to provided_mode property (CODING_RULE_V2_00017)
        """
        return self.provided_mode  # Delegates to property

    def getReleasedTrigger(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for releasedTrigger.

        Returns:
            The releasedTrigger value

        Note:
            Delegates to released_trigger property (CODING_RULE_V2_00017)
        """
        return self.released_trigger  # Delegates to property

    def getRequiredClient(self) -> List["BswModuleClientServer"]:
        """
        AUTOSAR-compliant getter for requiredClient.

        Returns:
            The requiredClient value

        Note:
            Delegates to required_client property (CODING_RULE_V2_00017)
        """
        return self.required_client  # Delegates to property

    def getRequiredData(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for requiredData.

        Returns:
            The requiredData value

        Note:
            Delegates to required_data property (CODING_RULE_V2_00017)
        """
        return self.required_data  # Delegates to property

    def getRequiredMode(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for requiredMode.

        Returns:
            The requiredMode value

        Note:
            Delegates to required_mode property (CODING_RULE_V2_00017)
        """
        return self.required_mode  # Delegates to property

    def getRequiredTrigger(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for requiredTrigger.

        Returns:
            The requiredTrigger value

        Note:
            Delegates to required_trigger property (CODING_RULE_V2_00017)
        """
        return self.required_trigger  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_bsw_module(self, value: Optional["SwComponent"]) -> BswModuleDescription:
        """
        Set bswModule and return self for chaining.

        Args:
            value: The bswModule to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_bsw_module("value")
        """
        self.bsw_module = value  # Use property setter (gets validation)
        return self

    def with_module_id(self, value: Optional[PositiveInteger]) -> BswModuleDescription:
        """
        Set moduleId and return self for chaining.

        Args:
            value: The moduleId to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_module_id("value")
        """
        self.module_id = value  # Use property setter (gets validation)
        return self


__all__ = [
    BswModuleDescription,
]

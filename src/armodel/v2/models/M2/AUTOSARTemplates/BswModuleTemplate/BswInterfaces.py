"""
AUTOSAR Package - BswInterfaces

Package: M2::AUTOSARTemplates::BswModuleTemplate::BswInterfaces
"""


from __future__ import annotations

from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
    Referrable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
    Boolean,
    Identifier,
    NameToken,
    PositiveInteger,
    SwServiceArg,
)


class BswModuleEntry(ARElement):
    """
    This class represents a single API entry (C-function prototype) into the BSW
    module or cluster. The name of the C-function is equal to the short name of
    this element with one exception: In case of multiple instances of a module
    on the same CPU, special rules for "infixes" apply, see description of class
    BswImplementation.

    Package: M2::AUTOSARTemplates::BswModuleTemplate::BswInterfaces::BswModuleEntry

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 32, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 976, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 216, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 431, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 171, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # An argument belonging to this BswModuleEntry.
        # atpSplitable; atpVariation.
        self._argument: List["SwServiceArg"] = []

    @property
    def argument(self) -> List["SwServiceArg"]:
        """Get argument (Pythonic accessor)."""
        return self._argument
        # This describes whether the entry is concrete or abstract.
        # attribute is missing the entry is considered as.
        self._bswEntryKind: Optional[BswEntryKindEnum] = None

    @property
    def bsw_entry_kind(self) -> Optional[BswEntryKindEnum]:
        """Get bswEntryKind (Pythonic accessor)."""
        return self._bswEntryKind

    @bsw_entry_kind.setter
    def bsw_entry_kind(self, value: Optional[BswEntryKindEnum]) -> None:
        """
        Set bswEntryKind with validation.

        Args:
            value: The bswEntryKind to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._bswEntryKind = None
            return

        if not isinstance(value, BswEntryKindEnum):
            raise TypeError(
                f"bswEntryKind must be BswEntryKindEnum or None, got {type(value).__name__}"
            )
        self._bswEntryKind = value
        self._callType: Optional[BswCallType] = None

    @property
    def call_type(self) -> Optional[BswCallType]:
        """Get callType (Pythonic accessor)."""
        return self._callType

    @call_type.setter
    def call_type(self, value: Optional[BswCallType]) -> None:
        """
        Set callType with validation.

        Args:
            value: The callType to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._callType = None
            return

        if not isinstance(value, BswCallType):
            raise TypeError(
                f"callType must be BswCallType or None, got {type(value).__name__}"
            )
        self._callType = value
        # module) or guaranteed (in case of from this module) for this service.
        self._execution: Optional[BswExecutionContext] = None

    @property
    def execution(self) -> Optional[BswExecutionContext]:
        """Get execution (Pythonic accessor)."""
        return self._execution

    @execution.setter
    def execution(self, value: Optional[BswExecutionContext]) -> None:
        """
        Set execution with validation.

        Args:
            value: The execution to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._execution = None
            return

        if not isinstance(value, BswExecutionContext):
            raise TypeError(
                f"execution must be BswExecutionContext or None, got {type(value).__name__}"
            )
        self._execution = value
        # the RTE generates the prototypes in the Module Interlink Header File.
        self._function: Optional["NameToken"] = None

    @property
    def function(self) -> Optional["NameToken"]:
        """Get function (Pythonic accessor)."""
        return self._function

    @function.setter
    def function(self, value: Optional["NameToken"]) -> None:
        """
        Set function with validation.

        Args:
            value: The function to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._function = None
            return

        if not isinstance(value, (NameToken, str)):
            raise TypeError(
                f"function must be NameToken or str or None, got {type(value).__name__}"
            )
        self._function = value
                # invoked again, before has finished.
        # It is prohibited to invoke the service again before finished.
        self._isReentrant: Optional[Boolean] = None

    @property
    def is_reentrant(self) -> Optional[Boolean]:
        """Get isReentrant (Pythonic accessor)."""
        return self._isReentrant

    @is_reentrant.setter
    def is_reentrant(self, value: Optional[Boolean]) -> None:
        """
        Set isReentrant with validation.

        Args:
            value: The isReentrant to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._isReentrant = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"isReentrant must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._isReentrant = value
                # synchronous service, i.
        # e.
        # the service when the call returns.
        # The service (on semantical level) may not be the call returns.
        self._isSynchronous: Optional[Boolean] = None

    @property
    def is_synchronous(self) -> Optional[Boolean]:
        """Get isSynchronous (Pythonic accessor)."""
        return self._isSynchronous

    @is_synchronous.setter
    def is_synchronous(self, value: Optional[Boolean]) -> None:
        """
        Set isSynchronous with validation.

        Args:
            value: The isSynchronous to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._isSynchronous = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"isSynchronous must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._isSynchronous = value
        # 381 Document ID 89: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate Module
                # Description Template R23-11.
        self._returnType: Optional["SwServiceArg"] = None

    @property
    def return_type(self) -> Optional["SwServiceArg"]:
        """Get returnType (Pythonic accessor)."""
        return self._returnType

    @return_type.setter
    def return_type(self, value: Optional["SwServiceArg"]) -> None:
        """
        Set returnType with validation.

        Args:
            value: The returnType to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._returnType = None
            return

        if not isinstance(value, SwServiceArg):
            raise TypeError(
                f"returnType must be SwServiceArg or None, got {type(value).__name__}"
            )
        self._returnType = value
        # It shall to the standardized name of the service call, cases where no
                # ServiceIdentifier is specified, callbacks.
        # Note that the ShortName is not always it maybe vendor specific (e.
        # g.
        # for can have more than one instance).
        self._role: Optional["Identifier"] = None

    @property
    def role(self) -> Optional["Identifier"]:
        """Get role (Pythonic accessor)."""
        return self._role

    @role.setter
    def role(self, value: Optional["Identifier"]) -> None:
        """
        Set role with validation.

        Args:
            value: The role to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._role = None
            return

        if not isinstance(value, (Identifier, str)):
            raise TypeError(
                f"role must be Identifier or str or None, got {type(value).__name__}"
            )
        self._role = value
        # For it can optionally be used for.
        self._serviceId: Optional[PositiveInteger] = None

    @property
    def service_id(self) -> Optional[PositiveInteger]:
        """Get serviceId (Pythonic accessor)."""
        return self._serviceId

    @service_id.setter
    def service_id(self, value: Optional[PositiveInteger]) -> None:
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
                # function or macro.
        # This has to be specified on because it determines the signature of the.
        self._swServiceImpl: Optional["SwServiceImplPolicy"] = None

    @property
    def sw_service_impl(self) -> Optional["SwServiceImplPolicy"]:
        """Get swServiceImpl (Pythonic accessor)."""
        return self._swServiceImpl

    @sw_service_impl.setter
    def sw_service_impl(self, value: Optional["SwServiceImplPolicy"]) -> None:
        """
        Set swServiceImpl with validation.

        Args:
            value: The swServiceImpl to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swServiceImpl = None
            return

        if not isinstance(value, SwServiceImplPolicy):
            raise TypeError(
                f"swServiceImpl must be SwServiceImplPolicy or None, got {type(value).__name__}"
            )
        self._swServiceImpl = value

    def with_argument(self, value):
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

    def with_bsw_entry_relationship(self, value):
        """
        Set bsw_entry_relationship and return self for chaining.

        Args:
            value: The bsw_entry_relationship to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_bsw_entry_relationship("value")
        """
        self.bsw_entry_relationship = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getArgument(self) -> List["SwServiceArg"]:
        """
        AUTOSAR-compliant getter for argument.

        Returns:
            The argument value

        Note:
            Delegates to argument property (CODING_RULE_V2_00017)
        """
        return self.argument  # Delegates to property

    def getBswEntryKind(self) -> BswEntryKindEnum:
        """
        AUTOSAR-compliant getter for bswEntryKind.

        Returns:
            The bswEntryKind value

        Note:
            Delegates to bsw_entry_kind property (CODING_RULE_V2_00017)
        """
        return self.bsw_entry_kind  # Delegates to property

    def setBswEntryKind(self, value: BswEntryKindEnum) -> BswModuleEntry:
        """
        AUTOSAR-compliant setter for bswEntryKind with method chaining.

        Args:
            value: The bswEntryKind to set

        Returns:
            self for method chaining

        Note:
            Delegates to bsw_entry_kind property setter (gets validation automatically)
        """
        self.bsw_entry_kind = value  # Delegates to property setter
        return self

    def getCallType(self) -> BswCallType:
        """
        AUTOSAR-compliant getter for callType.

        Returns:
            The callType value

        Note:
            Delegates to call_type property (CODING_RULE_V2_00017)
        """
        return self.call_type  # Delegates to property

    def setCallType(self, value: BswCallType) -> BswModuleEntry:
        """
        AUTOSAR-compliant setter for callType with method chaining.

        Args:
            value: The callType to set

        Returns:
            self for method chaining

        Note:
            Delegates to call_type property setter (gets validation automatically)
        """
        self.call_type = value  # Delegates to property setter
        return self

    def getExecution(self) -> BswExecutionContext:
        """
        AUTOSAR-compliant getter for execution.

        Returns:
            The execution value

        Note:
            Delegates to execution property (CODING_RULE_V2_00017)
        """
        return self.execution  # Delegates to property

    def setExecution(self, value: BswExecutionContext) -> BswModuleEntry:
        """
        AUTOSAR-compliant setter for execution with method chaining.

        Args:
            value: The execution to set

        Returns:
            self for method chaining

        Note:
            Delegates to execution property setter (gets validation automatically)
        """
        self.execution = value  # Delegates to property setter
        return self

    def getFunction(self) -> NameToken:
        """
        AUTOSAR-compliant getter for function.

        Returns:
            The function value

        Note:
            Delegates to function property (CODING_RULE_V2_00017)
        """
        return self.function  # Delegates to property

    def setFunction(self, value: NameToken) -> BswModuleEntry:
        """
        AUTOSAR-compliant setter for function with method chaining.

        Args:
            value: The function to set

        Returns:
            self for method chaining

        Note:
            Delegates to function property setter (gets validation automatically)
        """
        self.function = value  # Delegates to property setter
        return self

    def getIsReentrant(self) -> Boolean:
        """
        AUTOSAR-compliant getter for isReentrant.

        Returns:
            The isReentrant value

        Note:
            Delegates to is_reentrant property (CODING_RULE_V2_00017)
        """
        return self.is_reentrant  # Delegates to property

    def setIsReentrant(self, value: Boolean) -> BswModuleEntry:
        """
        AUTOSAR-compliant setter for isReentrant with method chaining.

        Args:
            value: The isReentrant to set

        Returns:
            self for method chaining

        Note:
            Delegates to is_reentrant property setter (gets validation automatically)
        """
        self.is_reentrant = value  # Delegates to property setter
        return self

    def getIsSynchronous(self) -> Boolean:
        """
        AUTOSAR-compliant getter for isSynchronous.

        Returns:
            The isSynchronous value

        Note:
            Delegates to is_synchronous property (CODING_RULE_V2_00017)
        """
        return self.is_synchronous  # Delegates to property

    def setIsSynchronous(self, value: Boolean) -> BswModuleEntry:
        """
        AUTOSAR-compliant setter for isSynchronous with method chaining.

        Args:
            value: The isSynchronous to set

        Returns:
            self for method chaining

        Note:
            Delegates to is_synchronous property setter (gets validation automatically)
        """
        self.is_synchronous = value  # Delegates to property setter
        return self

    def getReturnType(self) -> SwServiceArg:
        """
        AUTOSAR-compliant getter for returnType.

        Returns:
            The returnType value

        Note:
            Delegates to return_type property (CODING_RULE_V2_00017)
        """
        return self.return_type  # Delegates to property

    def setReturnType(self, value: SwServiceArg) -> BswModuleEntry:
        """
        AUTOSAR-compliant setter for returnType with method chaining.

        Args:
            value: The returnType to set

        Returns:
            self for method chaining

        Note:
            Delegates to return_type property setter (gets validation automatically)
        """
        self.return_type = value  # Delegates to property setter
        return self

    def getRole(self) -> Identifier:
        """
        AUTOSAR-compliant getter for role.

        Returns:
            The role value

        Note:
            Delegates to role property (CODING_RULE_V2_00017)
        """
        return self.role  # Delegates to property

    def setRole(self, value: Identifier) -> BswModuleEntry:
        """
        AUTOSAR-compliant setter for role with method chaining.

        Args:
            value: The role to set

        Returns:
            self for method chaining

        Note:
            Delegates to role property setter (gets validation automatically)
        """
        self.role = value  # Delegates to property setter
        return self

    def getServiceId(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for serviceId.

        Returns:
            The serviceId value

        Note:
            Delegates to service_id property (CODING_RULE_V2_00017)
        """
        return self.service_id  # Delegates to property

    def setServiceId(self, value: PositiveInteger) -> BswModuleEntry:
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

    def getSwServiceImpl(self) -> "SwServiceImplPolicy":
        """
        AUTOSAR-compliant getter for swServiceImpl.

        Returns:
            The swServiceImpl value

        Note:
            Delegates to sw_service_impl property (CODING_RULE_V2_00017)
        """
        return self.sw_service_impl  # Delegates to property

    def setSwServiceImpl(self, value: "SwServiceImplPolicy") -> BswModuleEntry:
        """
        AUTOSAR-compliant setter for swServiceImpl with method chaining.

        Args:
            value: The swServiceImpl to set

        Returns:
            self for method chaining

        Note:
            Delegates to sw_service_impl property setter (gets validation automatically)
        """
        self.sw_service_impl = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_bsw_entry_kind(self, value: Optional[BswEntryKindEnum]) -> BswModuleEntry:
        """
        Set bswEntryKind and return self for chaining.

        Args:
            value: The bswEntryKind to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_bsw_entry_kind("value")
        """
        self.bsw_entry_kind = value  # Use property setter (gets validation)
        return self

    def with_call_type(self, value: Optional[BswCallType]) -> BswModuleEntry:
        """
        Set callType and return self for chaining.

        Args:
            value: The callType to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_call_type("value")
        """
        self.call_type = value  # Use property setter (gets validation)
        return self

    def with_execution(self, value: Optional[BswExecutionContext]) -> BswModuleEntry:
        """
        Set execution and return self for chaining.

        Args:
            value: The execution to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_execution("value")
        """
        self.execution = value  # Use property setter (gets validation)
        return self

    def with_function(self, value: Optional["NameToken"]) -> BswModuleEntry:
        """
        Set function and return self for chaining.

        Args:
            value: The function to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_function("value")
        """
        self.function = value  # Use property setter (gets validation)
        return self

    def with_is_reentrant(self, value: Optional[Boolean]) -> BswModuleEntry:
        """
        Set isReentrant and return self for chaining.

        Args:
            value: The isReentrant to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_is_reentrant("value")
        """
        self.is_reentrant = value  # Use property setter (gets validation)
        return self

    def with_is_synchronous(self, value: Optional[Boolean]) -> BswModuleEntry:
        """
        Set isSynchronous and return self for chaining.

        Args:
            value: The isSynchronous to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_is_synchronous("value")
        """
        self.is_synchronous = value  # Use property setter (gets validation)
        return self

    def with_return_type(self, value: Optional["SwServiceArg"]) -> BswModuleEntry:
        """
        Set returnType and return self for chaining.

        Args:
            value: The returnType to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_return_type("value")
        """
        self.return_type = value  # Use property setter (gets validation)
        return self

    def with_role(self, value: Optional["Identifier"]) -> BswModuleEntry:
        """
        Set role and return self for chaining.

        Args:
            value: The role to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_role("value")
        """
        self.role = value  # Use property setter (gets validation)
        return self

    def with_service_id(self, value: Optional[PositiveInteger]) -> BswModuleEntry:
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

    def with_sw_service_impl(self, value: Optional["SwServiceImplPolicy"]) -> BswModuleEntry:
        """
        Set swServiceImpl and return self for chaining.

        Args:
            value: The swServiceImpl to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sw_service_impl("value")
        """
        self.sw_service_impl = value  # Use property setter (gets validation)
        return self



class BswModuleDependency(Identifiable):
    """
    This class collects the dependencies of a BSW module or cluster on a certain
    other BSW module.

    Package: M2::AUTOSARTemplates::BswModuleTemplate::BswInterfaces::BswModuleDependency

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 47, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # AUTOSAR identifier of the target module of which the defined.
        # is optional, because the target module be identified by targetModuleRef.
        # 381 Document ID 89: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate Module
                # Description Template R23-11.
        self._targetModuleId: Optional[PositiveInteger] = None

    @property
    def target_module_id(self) -> Optional[PositiveInteger]:
        """Get targetModuleId (Pythonic accessor)."""
        return self._targetModuleId

    @target_module_id.setter
    def target_module_id(self, value: Optional[PositiveInteger]) -> None:
        """
        Set targetModuleId with validation.

        Args:
            value: The targetModuleId to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._targetModuleId = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"targetModuleId must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._targetModuleId = value
        # It is an <<atpUriDef>> the reference shall be used to identify the target
                # actually needing the description of that atpUriDef; atpVariation.
        self._targetModule: Optional["BswModuleDescription"] = None

    @property
    def target_module(self) -> Optional["BswModuleDescription"]:
        """Get targetModule (Pythonic accessor)."""
        return self._targetModule

    @target_module.setter
    def target_module(self, value: Optional["BswModuleDescription"]) -> None:
        """
        Set targetModule with validation.

        Args:
            value: The targetModule to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._targetModule = None
            return

        if not isinstance(value, BswModuleDescription):
            raise TypeError(
                f"targetModule must be BswModuleDescription or None, got {type(value).__name__}"
            )
        self._targetModule = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTargetModuleId(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for targetModuleId.

        Returns:
            The targetModuleId value

        Note:
            Delegates to target_module_id property (CODING_RULE_V2_00017)
        """
        return self.target_module_id  # Delegates to property

    def setTargetModuleId(self, value: PositiveInteger) -> BswModuleDependency:
        """
        AUTOSAR-compliant setter for targetModuleId with method chaining.

        Args:
            value: The targetModuleId to set

        Returns:
            self for method chaining

        Note:
            Delegates to target_module_id property setter (gets validation automatically)
        """
        self.target_module_id = value  # Delegates to property setter
        return self

    def getTargetModule(self) -> "BswModuleDescription":
        """
        AUTOSAR-compliant getter for targetModule.

        Returns:
            The targetModule value

        Note:
            Delegates to target_module property (CODING_RULE_V2_00017)
        """
        return self.target_module  # Delegates to property

    def setTargetModule(self, value: "BswModuleDescription") -> BswModuleDependency:
        """
        AUTOSAR-compliant setter for targetModule with method chaining.

        Args:
            value: The targetModule to set

        Returns:
            self for method chaining

        Note:
            Delegates to target_module property setter (gets validation automatically)
        """
        self.target_module = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_target_module_id(self, value: Optional[PositiveInteger]) -> BswModuleDependency:
        """
        Set targetModuleId and return self for chaining.

        Args:
            value: The targetModuleId to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_target_module_id("value")
        """
        self.target_module_id = value  # Use property setter (gets validation)
        return self

    def with_target_module(self, value: Optional["BswModuleDescription"]) -> BswModuleDependency:
        """
        Set targetModule and return self for chaining.

        Args:
            value: The targetModule to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_target_module("value")
        """
        self.target_module = value  # Use property setter (gets validation)
        return self



class BswEntryRelationshipSet(ARElement):
    """
    Describes a set of relationships between two BswModuleEntrys.

    Package: M2::AUTOSARTemplates::BswModuleTemplate::BswInterfaces::BswEntryRelationshipSet

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 51, Classic
      Platform R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 51, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Relationship between two BswModuleEntrys.
        self._bswEntryRelationship: List[BswEntryRelationship] = []

    @property
    def bsw_entry_relationship(self) -> List[BswEntryRelationship]:
        """Get bswEntryRelationship (Pythonic accessor)."""
        return self._bswEntryRelationship

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBswEntryRelationship(self) -> List[BswEntryRelationship]:
        """
        AUTOSAR-compliant getter for bswEntryRelationship.

        Returns:
            The bswEntryRelationship value

        Note:
            Delegates to bsw_entry_relationship property (CODING_RULE_V2_00017)
        """
        return self.bsw_entry_relationship  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class BswEntryRelationship(ARObject):
    """
    Describes a relationship between two BswModuleEntrys and the type of
    relationship.

    Package: M2::AUTOSARTemplates::BswModuleTemplate::BswInterfaces::BswEntryRelationship

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 51, Classic
      Platform R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 52, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Denotes the type of the relationship.
        # Tags: xml.
        # sequenceOffset=5 Type.
        self._bswEntry: Optional[BswEntryRelationship] = None

    @property
    def bsw_entry(self) -> Optional[BswEntryRelationship]:
        """Get bswEntry (Pythonic accessor)."""
        return self._bswEntry

    @bsw_entry.setter
    def bsw_entry(self, value: Optional[BswEntryRelationship]) -> None:
        """
        Set bswEntry with validation.

        Args:
            value: The bswEntry to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._bswEntry = None
            return

        if not isinstance(value, BswEntryRelationship):
            raise TypeError(
                f"bswEntry must be BswEntryRelationship or None, got {type(value).__name__}"
            )
        self._bswEntry = value
        # this case the bswEntry be set to drivedFrom.
        self._from_module: Optional[BswModuleEntry] = None

    @property
    def from_module(self) -> Optional[BswModuleEntry]:
        """Get from_module (Pythonic accessor)."""
        return self._from_module

    @from_module.setter
    def from_module(self, value: Optional[BswModuleEntry]) -> None:
        """
        Set from_module with validation.

        Args:
            value: The from_module to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._from_module = None
            return

        if not isinstance(value, BswModuleEntry):
            raise TypeError(
                f"from_module must be BswModuleEntry or None, got {type(value).__name__}"
            )
        self._from_module = value
        self._to: Optional[BswModuleEntry] = None

    @property
    def to(self) -> Optional[BswModuleEntry]:
        """Get to (Pythonic accessor)."""
        return self._to

    @to.setter
    def to(self, value: Optional[BswModuleEntry]) -> None:
        """
        Set to with validation.

        Args:
            value: The to to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._to = None
            return

        if not isinstance(value, BswModuleEntry):
            raise TypeError(
                f"to must be BswModuleEntry or None, got {type(value).__name__}"
            )
        self._to = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBswEntry(self) -> BswEntryRelationship:
        """
        AUTOSAR-compliant getter for bswEntry.

        Returns:
            The bswEntry value

        Note:
            Delegates to bsw_entry property (CODING_RULE_V2_00017)
        """
        return self.bsw_entry  # Delegates to property

    def setBswEntry(self, value: BswEntryRelationship) -> BswEntryRelationship:
        """
        AUTOSAR-compliant setter for bswEntry with method chaining.

        Args:
            value: The bswEntry to set

        Returns:
            self for method chaining

        Note:
            Delegates to bsw_entry property setter (gets validation automatically)
        """
        self.bsw_entry = value  # Delegates to property setter
        return self

    def getFrom(self) -> BswModuleEntry:
        """
        AUTOSAR-compliant getter for from_module.

        Returns:
            The from_module value

        Note:
            Delegates to from_module property (CODING_RULE_V2_00017)
        """
        return self.from_module  # Delegates to property

    def setFrom(self, value: BswModuleEntry) -> BswEntryRelationship:
        """
        AUTOSAR-compliant setter for from_module with method chaining.

        Args:
            value: The from_module to set

        Returns:
            self for method chaining

        Note:
            Delegates to from_module property setter (gets validation automatically)
        """
        self.from_module = value  # Delegates to property setter
        return self

    def getTo(self) -> BswModuleEntry:
        """
        AUTOSAR-compliant getter for to.

        Returns:
            The to value

        Note:
            Delegates to to property (CODING_RULE_V2_00017)
        """
        return self.to  # Delegates to property

    def setTo(self, value: BswModuleEntry) -> BswEntryRelationship:
        """
        AUTOSAR-compliant setter for to with method chaining.

        Args:
            value: The to to set

        Returns:
            self for method chaining

        Note:
            Delegates to to property setter (gets validation automatically)
        """
        self.to = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_bsw_entry(self, value: Optional[BswEntryRelationship]) -> BswEntryRelationship:
        """
        Set bswEntry and return self for chaining.

        Args:
            value: The bswEntry to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_bsw_entry("value")
        """
        self.bsw_entry = value  # Use property setter (gets validation)
        return self

    def with_from_module(self, value: Optional[BswModuleEntry]) -> BswEntryRelationship:
        """
        Set from_module and return self for chaining.

        Args:
            value: The from_module to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_from_module("value")
        """
        self.from_module = value  # Use property setter (gets validation)
        return self

    def with_to(self, value: Optional[BswModuleEntry]) -> BswEntryRelationship:
        """
        Set to and return self for chaining.

        Args:
            value: The to to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_to("value")
        """
        self.to = value  # Use property setter (gets validation)
        return self



class BswModuleClientServerEntry(Referrable):
    """
    This meta-class represents a single API entry into the BSW module or cluster
    that has the ability to be called in client-server fashion via the BSW
    Scheduler. In this regard it is more special than BswModuleEntry and can be
    seen as a wrapper around the Bsw ModuleEntry to which it refers (property
    encapsulatedEntry).

    Package: M2::AUTOSARTemplates::BswModuleTemplate::BswInterfaces::BswModuleClientServerEntry

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 53, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The underlying BswModuleEntry.
        # xml.
        # sequenceOffset=5.
        self._encapsulated: Optional[BswModuleEntry] = None

    @property
    def encapsulated(self) -> Optional[BswModuleEntry]:
        """Get encapsulated (Pythonic accessor)."""
        return self._encapsulated

    @encapsulated.setter
    def encapsulated(self, value: Optional[BswModuleEntry]) -> None:
        """
        Set encapsulated with validation.

        Args:
            value: The encapsulated to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._encapsulated = None
            return

        if not isinstance(value, BswModuleEntry):
            raise TypeError(
                f"encapsulated must be BswModuleEntry or None, got {type(value).__name__}"
            )
        self._encapsulated = value
                # Enables the service to be invoked again, before has finished.
        # It is prohibited to invoke the service again before finished.
        # 381 Document ID 89: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate Module
                # Description Template R23-11.
        self._isReentrant: Optional[Boolean] = None

    @property
    def is_reentrant(self) -> Optional[Boolean]:
        """Get isReentrant (Pythonic accessor)."""
        return self._isReentrant

    @is_reentrant.setter
    def is_reentrant(self, value: Optional[Boolean]) -> None:
        """
        Set isReentrant with validation.

        Args:
            value: The isReentrant to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._isReentrant = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"isReentrant must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._isReentrant = value
                # This calls a synchronous service, i.
        # e.
        # the service when the call returns.
        # The service (on semantical level) may not be the call returns.
        self._isSynchronous: Optional[Boolean] = None

    @property
    def is_synchronous(self) -> Optional[Boolean]:
        """Get isSynchronous (Pythonic accessor)."""
        return self._isSynchronous

    @is_synchronous.setter
    def is_synchronous(self, value: Optional[Boolean]) -> None:
        """
        Set isSynchronous with validation.

        Args:
            value: The isSynchronous to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._isSynchronous = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"isSynchronous must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._isSynchronous = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEncapsulated(self) -> BswModuleEntry:
        """
        AUTOSAR-compliant getter for encapsulated.

        Returns:
            The encapsulated value

        Note:
            Delegates to encapsulated property (CODING_RULE_V2_00017)
        """
        return self.encapsulated  # Delegates to property

    def setEncapsulated(self, value: BswModuleEntry) -> BswModuleClientServerEntry:
        """
        AUTOSAR-compliant setter for encapsulated with method chaining.

        Args:
            value: The encapsulated to set

        Returns:
            self for method chaining

        Note:
            Delegates to encapsulated property setter (gets validation automatically)
        """
        self.encapsulated = value  # Delegates to property setter
        return self

    def getIsReentrant(self) -> Boolean:
        """
        AUTOSAR-compliant getter for isReentrant.

        Returns:
            The isReentrant value

        Note:
            Delegates to is_reentrant property (CODING_RULE_V2_00017)
        """
        return self.is_reentrant  # Delegates to property

    def setIsReentrant(self, value: Boolean) -> BswModuleClientServerEntry:
        """
        AUTOSAR-compliant setter for isReentrant with method chaining.

        Args:
            value: The isReentrant to set

        Returns:
            self for method chaining

        Note:
            Delegates to is_reentrant property setter (gets validation automatically)
        """
        self.is_reentrant = value  # Delegates to property setter
        return self

    def getIsSynchronous(self) -> Boolean:
        """
        AUTOSAR-compliant getter for isSynchronous.

        Returns:
            The isSynchronous value

        Note:
            Delegates to is_synchronous property (CODING_RULE_V2_00017)
        """
        return self.is_synchronous  # Delegates to property

    def setIsSynchronous(self, value: Boolean) -> BswModuleClientServerEntry:
        """
        AUTOSAR-compliant setter for isSynchronous with method chaining.

        Args:
            value: The isSynchronous to set

        Returns:
            self for method chaining

        Note:
            Delegates to is_synchronous property setter (gets validation automatically)
        """
        self.is_synchronous = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_encapsulated(self, value: Optional[BswModuleEntry]) -> BswModuleClientServerEntry:
        """
        Set encapsulated and return self for chaining.

        Args:
            value: The encapsulated to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_encapsulated("value")
        """
        self.encapsulated = value  # Use property setter (gets validation)
        return self

    def with_is_reentrant(self, value: Optional[Boolean]) -> BswModuleClientServerEntry:
        """
        Set isReentrant and return self for chaining.

        Args:
            value: The isReentrant to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_is_reentrant("value")
        """
        self.is_reentrant = value  # Use property setter (gets validation)
        return self

    def with_is_synchronous(self, value: Optional[Boolean]) -> BswModuleClientServerEntry:
        """
        Set isSynchronous and return self for chaining.

        Args:
            value: The isSynchronous to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_is_synchronous("value")
        """
        self.is_synchronous = value  # Use property setter (gets validation)
        return self


class BswEntryKindEnum(AREnum):
    """
    BswEntryKindEnum enumeration

Denotes the mechanism by which the entry into the Bsw module shall be called. Aggregated by BswModuleEntry.bswEntryKind

Package: M2::AUTOSARTemplates::BswModuleTemplate::BswInterfaces
    """
    # Software Module Description Template
    Basic = "None"

    # CP R23-11
    AUTOSAR = "None"

    # This BswModuleEntry specifies an abstract signature of C-functions. The signature needs to be implemented by concrete BswModuleEntrys
    abstract = "0"

    # This BswModuleEntry specifies a concrete C-function with its signature.
    concrete = "1"



class BswExecutionContext(AREnum):
    """
    BswExecutionContext enumeration

Specifies the execution context required or guaranteed for the call associated with this service. Aggregated by BswModuleEntry.executionContext

Package: M2::AUTOSARTemplates::BswModuleTemplate::BswInterfaces
    """
    # Context of an OS "hook" routine always
    hook = "0"

    # CAT1 interrupt context always
    interruptCat1 = "1"

    # CAT2 interrupt context always
    interruptCat2 = "2"

    # Task context always
    task = "3"

    # The execution context is not specified by the API
    unspecified = "4"



class BswCallType(AREnum):
    """
    BswCallType enumeration

Denotes the mechanism by which the entry into the Bsw module shall be called. Aggregated by BswModuleEntry.callType

Package: M2::AUTOSARTemplates::BswModuleTemplate::BswInterfaces
    """
    # Callback (i.e. the caller specifies the signature)
    callback = "0"

    # Callout - provide defined means to extend the functionality of an existing module. In this case caller specifies the signature.
    callout = "4"

    # Interrupt routine
    interrupt = "1"

    # Regular API call
    regular = "2"

    # Called by the scheduler
    scheduled = "3"



class BswEntryRelationshipEnum(AREnum):
    """
    BswEntryRelationshipEnum enumeration

Define the type of relationship between two BswModuleEntrys. Aggregated by BswEntryRelationship.bswEntryRelationshipType

Package: M2::AUTOSARTemplates::BswModuleTemplate::BswInterfaces
    """
    # Describes that the BswModuleEntry referenced as "to" needs to have the same signature as the
    derivedFrom = "0"

"""
AUTOSAR Package - ServiceNeeds

Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds
"""


from __future__ import annotations

from abc import ABC
from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.Implementation import (
    ImplementationProps,
)
from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticIndicator import (
    DiagnosticIndicatorTypeEnum,
)
from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping import (
    DiagEventDebounce,
    DiagnosticClearDtc,
    DiagnosticDenominator,
    DiagnosticMonitor,
    DiagnosticProcessing,
    DiagnosticService,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
    Boolean,
    DiagRequirementIdString,
    Identifier,
    Integer,
    NameToken,
    PositiveInteger,
    RefType,
    String,
    TimeValue,
)
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import (
    RamBlockStatusControlEnum,
)
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.PerInstanceMemory import (
    PerInstanceMemory,
)
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ServiceMapping import (
    RoleBasedDataTypeAssignment,
)

# Type aliases for backward compatibility with AUTOSAR naming conventions
RoleBasedDataType = RoleBasedDataTypeAssignment
DiagRequirementId = DiagRequirementIdString

# These enums will be defined later in this file, so we can't create aliases yet
# They will be available as actual classes when the file is fully loaded


class ServiceDependency(ARObject, ABC):
    """
    Collects all dependencies of a software module or component on an AUTOSAR
    Service related to a specific item (e.g. an NVRAM Block, a diagnostic event
    etc.). It defines the quality of service (Service Needs) of this item as
    well as (optionally) references to additional elements. This information is
    required for tools in order to generate the related basic software
    configuration and ServiceSwComponentTypes.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::ServiceDependency

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 225, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 609, Classic Platform
      R23-11)
    """
    def __init__(self):
        if type(self) is ServiceDependency:
            raise TypeError("ServiceDependency is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is the role of the assignment data type in the given context.
        # atpVariation.
        self._assignedData: Optional[RoleBasedDataType] = None

    @property
    def assigned_data(self) -> Optional[RoleBasedDataType]:
        """Get assignedData (Pythonic accessor)."""
        return self._assignedData

    @assigned_data.setter
    def assigned_data(self, value: Optional[RoleBasedDataType]) -> None:
        """
        Set assignedData with validation.

        Args:
            value: The assignedData to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._assignedData = None
            return

        if not isinstance(value, RoleBasedDataType):
            raise TypeError(
                f"assignedData must be RoleBasedDataType or None, got {type(value).__name__}"
            )
        self._assignedData = value
                # has a much easier time identifying the the configuration of the diagnostic
                # stack.
        # of mode conditions (e.
        # g.
        # application and BswM) relevant Dcm.
        self._diagnostic: Optional[ServiceDiagnosticRelevanceEnum] = None

    @property
    def diagnostic(self) -> Optional[ServiceDiagnosticRelevanceEnum]:
        """Get diagnostic (Pythonic accessor)."""
        return self._diagnostic

    @diagnostic.setter
    def diagnostic(self, value: Optional[ServiceDiagnosticRelevanceEnum]) -> None:
        """
        Set diagnostic with validation.

        Args:
            value: The diagnostic to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._diagnostic = None
            return

        if not isinstance(value, ServiceDiagnosticRelevanceEnum):
            raise TypeError(
                f"diagnostic must be ServiceDiagnosticRelevanceEnum or None, got {type(value).__name__}"
            )
        self._diagnostic = value
        self._symbolicName: Optional[SymbolicNameProps] = None

    @property
    def symbolic_name(self) -> Optional[SymbolicNameProps]:
        """Get symbolicName (Pythonic accessor)."""
        return self._symbolicName

    @symbolic_name.setter
    def symbolic_name(self, value: Optional[SymbolicNameProps]) -> None:
        """
        Set symbolicName with validation.

        Args:
            value: The symbolicName to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._symbolicName = None
            return

        if not isinstance(value, SymbolicNameProps):
            raise TypeError(
                f"symbolicName must be SymbolicNameProps or None, got {type(value).__name__}"
            )
        self._symbolicName = value

    def with_checkpoints(self, value):
        """
        Set checkpoints and return self for chaining.

        Args:
            value: The checkpoints to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_checkpoints("value")
        """
        self.checkpoints = value  # Use property setter (gets validation)
        return self

    def with_audience(self, value):
        """
        Set audience and return self for chaining.

        Args:
            value: The audience to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_audience("value")
        """
        self.audience = value  # Use property setter (gets validation)
        return self

    def with_traced_failure(self, value):
        """
        Set traced_failure and return self for chaining.

        Args:
            value: The traced_failure to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_traced_failure("value")
        """
        self.traced_failure = value  # Use property setter (gets validation)
        return self

    def with_possible_error(self, value):
        """
        Set possible_error and return self for chaining.

        Args:
            value: The possible_error to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_possible_error("value")
        """
        self.possible_error = value  # Use property setter (gets validation)
        return self

    def with_deferring_fid(self, value):
        """
        Set deferring_fid and return self for chaining.

        Args:
            value: The deferring_fid to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_deferring_fid("value")
        """
        self.deferring_fid = value  # Use property setter (gets validation)
        return self

    def with_inhibiting(self, value):
        """
        Set inhibiting and return self for chaining.

        Args:
            value: The inhibiting to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_inhibiting("value")
        """
        self.inhibiting = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAssignedData(self) -> RoleBasedDataType:
        """
        AUTOSAR-compliant getter for assignedData.

        Returns:
            The assignedData value

        Note:
            Delegates to assigned_data property (CODING_RULE_V2_00017)
        """
        return self.assigned_data  # Delegates to property

    def setAssignedData(self, value: RoleBasedDataType) -> ServiceDependency:
        """
        AUTOSAR-compliant setter for assignedData with method chaining.

        Args:
            value: The assignedData to set

        Returns:
            self for method chaining

        Note:
            Delegates to assigned_data property setter (gets validation automatically)
        """
        self.assigned_data = value  # Delegates to property setter
        return self

    def getDiagnostic(self) -> ServiceDiagnosticRelevanceEnum:
        """
        AUTOSAR-compliant getter for diagnostic.

        Returns:
            The diagnostic value

        Note:
            Delegates to diagnostic property (CODING_RULE_V2_00017)
        """
        return self.diagnostic  # Delegates to property

    def setDiagnostic(self, value: ServiceDiagnosticRelevanceEnum) -> ServiceDependency:
        """
        AUTOSAR-compliant setter for diagnostic with method chaining.

        Args:
            value: The diagnostic to set

        Returns:
            self for method chaining

        Note:
            Delegates to diagnostic property setter (gets validation automatically)
        """
        self.diagnostic = value  # Delegates to property setter
        return self

    def getSymbolicName(self) -> SymbolicNameProps:
        """
        AUTOSAR-compliant getter for symbolicName.

        Returns:
            The symbolicName value

        Note:
            Delegates to symbolic_name property (CODING_RULE_V2_00017)
        """
        return self.symbolic_name  # Delegates to property

    def setSymbolicName(self, value: SymbolicNameProps) -> ServiceDependency:
        """
        AUTOSAR-compliant setter for symbolicName with method chaining.

        Args:
            value: The symbolicName to set

        Returns:
            self for method chaining

        Note:
            Delegates to symbolic_name property setter (gets validation automatically)
        """
        self.symbolic_name = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_assigned_data(self, value: Optional[RoleBasedDataType]) -> ServiceDependency:
        """
        Set assignedData and return self for chaining.

        Args:
            value: The assignedData to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_assigned_data("value")
        """
        self.assigned_data = value  # Use property setter (gets validation)
        return self

    def with_diagnostic(self, value: Optional[ServiceDiagnosticRelevanceEnum]) -> ServiceDependency:
        """
        Set diagnostic and return self for chaining.

        Args:
            value: The diagnostic to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_diagnostic("value")
        """
        self.diagnostic = value  # Use property setter (gets validation)
        return self

    def with_symbolic_name(self, value: Optional[SymbolicNameProps]) -> ServiceDependency:
        """
        Set symbolicName and return self for chaining.

        Args:
            value: The symbolicName to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_symbolic_name("value")
        """
        self.symbolic_name = value  # Use property setter (gets validation)
        return self



class RoleBasedDataAssignment(ARObject):
    """
    This class specifies an assignment of a role to a particular data object in
    either • the SwcInternalBehavior of a software component (or in the
    BswInternalBehavior of a BSW module or BSW cluster) in the context of an
    AUTOSAR Service or • an NvBlockDescriptor to sort out the assignment of
    event-based writing strategies to data elements in a PortPrototype. With
    this assignment, the role of the data can be mapped to a DataPrototype that
    is used in the context of the definition of a specific ServiceNeeds or
    NvBlockDescriptor, so that a tool is able to create the correct access or
    writing strategy.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::RoleBasedDataAssignment

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 226, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 607, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is the role of the assigned data in the given context.
        # need to be specified on M1 level.
        # TPS Software Component Template list of applicable roles for various service
                # service use cases in chapter 13 and Service Use Cases" (e.
        # g.
        # , case of the needs for a permanent RAM.
        self._role: Optional[Identifier] = None

    @property
    def role(self) -> Optional[Identifier]:
        """Get role (Pythonic accessor)."""
        return self._role

    @role.setter
    def role(self, value: Optional[Identifier]) -> None:
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
        # g.
        # Permanent RAM Block of an NVRAM Block which shall the same
                # SwcInternalBehavior or Bsw the role signalBasedDiagnostics it has to refer to
                # a a SenderReceiverInterface or.
        self._usedData: Optional[RefType] = None

    @property
    def used_data(self) -> Optional[RefType]:
        """Get usedData (Pythonic accessor)."""
        return self._usedData

    @used_data.setter
    def used_data(self, value: Optional[RefType]) -> None:
        """
        Set usedData with validation.

        Args:
            value: The usedData to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._usedData = None
            return

        self._usedData = value
        # g.
        # ROM Block of an NVRAM Block.
        # It shall belong to the or BswInternalbehavior.
        # the role signalBasedDiagnostics it has to refer to a a ParameterInterface.
        self._usedParameter: Optional[RefType] = None

    @property
    def used_parameter(self) -> Optional[RefType]:
        """Get usedParameter (Pythonic accessor)."""
        return self._usedParameter

    @used_parameter.setter
    def used_parameter(self, value: Optional[RefType]) -> None:
        """
        Set usedParameter with validation.

        Args:
            value: The usedParameter to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._usedParameter = None
            return

        self._usedParameter = value
        # g.
        # Permanent RAM Block for an NVRAM Block).
        self._usedPim: Optional[PerInstanceMemory] = None

    @property
    def used_pim(self) -> Optional[PerInstanceMemory]:
        """Get usedPim (Pythonic accessor)."""
        return self._usedPim

    @used_pim.setter
    def used_pim(self, value: Optional[PerInstanceMemory]) -> None:
        """
        Set usedPim with validation.

        Args:
            value: The usedPim to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._usedPim = None
            return

        if not isinstance(value, PerInstanceMemory):
            raise TypeError(
                f"usedPim must be PerInstanceMemory or None, got {type(value).__name__}"
            )
        self._usedPim = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getRole(self) -> "Identifier":
        """
        AUTOSAR-compliant getter for role.

        Returns:
            The role value

        Note:
            Delegates to role property (CODING_RULE_V2_00017)
        """
        return self.role  # Delegates to property

    def setRole(self, value: Identifier) -> RoleBasedDataAssignment:
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

    def getUsedData(self) -> RefType:
        """
        AUTOSAR-compliant getter for usedData.

        Returns:
            The usedData value

        Note:
            Delegates to used_data property (CODING_RULE_V2_00017)
        """
        return self.used_data  # Delegates to property

    def setUsedData(self, value: RefType) -> RoleBasedDataAssignment:
        """
        AUTOSAR-compliant setter for usedData with method chaining.

        Args:
            value: The usedData to set

        Returns:
            self for method chaining

        Note:
            Delegates to used_data property setter (gets validation automatically)
        """
        self.used_data = value  # Delegates to property setter
        return self

    def getUsedParameter(self) -> RefType:
        """
        AUTOSAR-compliant getter for usedParameter.

        Returns:
            The usedParameter value

        Note:
            Delegates to used_parameter property (CODING_RULE_V2_00017)
        """
        return self.used_parameter  # Delegates to property

    def setUsedParameter(self, value: RefType) -> RoleBasedDataAssignment:
        """
        AUTOSAR-compliant setter for usedParameter with method chaining.

        Args:
            value: The usedParameter to set

        Returns:
            self for method chaining

        Note:
            Delegates to used_parameter property setter (gets validation automatically)
        """
        self.used_parameter = value  # Delegates to property setter
        return self

    def getUsedPim(self) -> PerInstanceMemory:
        """
        AUTOSAR-compliant getter for usedPim.

        Returns:
            The usedPim value

        Note:
            Delegates to used_pim property (CODING_RULE_V2_00017)
        """
        return self.used_pim  # Delegates to property

    def setUsedPim(self, value: PerInstanceMemory) -> RoleBasedDataAssignment:
        """
        AUTOSAR-compliant setter for usedPim with method chaining.

        Args:
            value: The usedPim to set

        Returns:
            self for method chaining

        Note:
            Delegates to used_pim property setter (gets validation automatically)
        """
        self.used_pim = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_role(self, value: Optional[Identifier]) -> RoleBasedDataAssignment:
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

    def with_used_data(self, value: Optional[RefType]) -> RoleBasedDataAssignment:
        """
        Set usedData and return self for chaining.

        Args:
            value: The usedData to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_used_data("value")
        """
        self.used_data = value  # Use property setter (gets validation)
        return self

    def with_used_parameter(self, value: Optional[RefType]) -> RoleBasedDataAssignment:
        """
        Set usedParameter and return self for chaining.

        Args:
            value: The usedParameter to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_used_parameter("value")
        """
        self.used_parameter = value  # Use property setter (gets validation)
        return self

    def with_used_pim(self, value: Optional[PerInstanceMemory]) -> RoleBasedDataAssignment:
        """
        Set usedPim and return self for chaining.

        Args:
            value: The usedPim to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_used_pim("value")
        """
        self.used_pim = value  # Use property setter (gets validation)
        return self



class ServiceNeeds(Identifiable, ABC):
    """
    This expresses the abstract needs that a Software Component or Basic
    Software Module has on the configuration of an AUTOSAR Service to which it
    will be connected. "Abstract needs" means that the model abstracts from the
    Configuration Parameters of the underlying Basic Software. (cid:53) 227 of
    381 Document ID 89: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate Basic
    Software Module Description Template AUTOSAR CP R23-11 (cid:52)

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::ServiceNeeds

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 227, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 329, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 306, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 603, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2055, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is ServiceNeeds:
            raise TypeError("ServiceNeeds is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class DiagEventDebounceAlgorithm(Identifiable, ABC):
    """
    This class represents the ability to specify the pre-debounce algorithm
    which is selected and/or required by the particular monitor. This class
    inherits from Identifiable in order to allow further documentation of the
    expected or implemented debouncing and to use the category for the
    identification of the expected / implemented debouncing.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::DiagEventDebounceAlgorithm

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 259, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 196, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 756, Classic Platform
      R23-11)
    """
    def __init__(self):
        if type(self) is DiagEventDebounceAlgorithm:
            raise TypeError("DiagEventDebounceAlgorithm is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class TracedFailure(Identifiable, ABC):
    """
    Specifies the ability to report a specific failure to the error tracer. The
    short name specifies the literal applicable for the Default Error Tracer.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::TracedFailure

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 263, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 832, Classic Platform
      R23-11)
    """
    def __init__(self):
        if type(self) is TracedFailure:
            raise TypeError("TracedFailure is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # ID of detected failure used in reporting API as error or.
        self._id: Optional[PositiveInteger] = None

    @property
    def id(self) -> Optional[PositiveInteger]:
        """Get id (Pythonic accessor)."""
        return self._id

    @id.setter
    def id(self, value: Optional[PositiveInteger]) -> None:
        """
        Set id with validation.

        Args:
            value: The id to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._id = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"id must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._id = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getId(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for id.

        Returns:
            The id value

        Note:
            Delegates to id property (CODING_RULE_V2_00017)
        """
        return self.id  # Delegates to property

    def setId(self, value: PositiveInteger) -> TracedFailure:
        """
        AUTOSAR-compliant setter for id with method chaining.

        Args:
            value: The id to set

        Returns:
            self for method chaining

        Note:
            Delegates to id property setter (gets validation automatically)
        """
        self.id = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_id(self, value: Optional[PositiveInteger]) -> TracedFailure:
        """
        Set id and return self for chaining.

        Args:
            value: The id to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_id("value")
        """
        self.id = value  # Use property setter (gets validation)
        return self



class SymbolicNameProps(ImplementationProps):
    """
    This meta-class can be taken to contribute to the creation of symbolic name
    values.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::SymbolicNameProps

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 610, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class NvBlockNeeds(ServiceNeeds):
    """
    Specifies the abstract needs on the configuration of a single NVRAM Block.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::NvBlockNeeds

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 231, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 679, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines if CRC (re)calculation for the permanent RAM is required.
        self._calcRamBlock: Optional[Boolean] = None

    @property
    def calc_ram_block(self) -> Optional[Boolean]:
        """Get calcRamBlock (Pythonic accessor)."""
        return self._calcRamBlock

    @calc_ram_block.setter
    def calc_ram_block(self, value: Optional[Boolean]) -> None:
        """
        Set calcRamBlock with validation.

        Args:
            value: The calcRamBlock to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._calcRamBlock = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"calcRamBlock must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._calcRamBlock = value
        self._checkStatic: Optional[Boolean] = None

    @property
    def check_static(self) -> Optional[Boolean]:
        """Get checkStatic (Pythonic accessor)."""
        return self._checkStatic

    @check_static.setter
    def check_static(self, value: Optional[Boolean]) -> None:
        """
        Set checkStatic with validation.

        Args:
            value: The checkStatic to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._checkStatic = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"checkStatic must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._checkStatic = value
        # Block.
        self._cyclicWriting: Optional[TimeValue] = None

    @property
    def cyclic_writing(self) -> Optional[TimeValue]:
        """Get cyclicWriting (Pythonic accessor)."""
        return self._cyclicWriting

    @cyclic_writing.setter
    def cyclic_writing(self, value: Optional[TimeValue]) -> None:
        """
        Set cyclicWriting with validation.

        Args:
            value: The cyclicWriting to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._cyclicWriting = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"cyclicWriting must be TimeValue or None, got {type(value).__name__}"
            )
        self._cyclicWriting = value
        # This is the total number of ROM RAM Blocks.
        self._nDataSets: Optional[PositiveInteger] = None

    @property
    def n_data_sets(self) -> Optional[PositiveInteger]:
        """Get nDataSets (Pythonic accessor)."""
        return self._nDataSets

    @n_data_sets.setter
    def n_data_sets(self, value: Optional[PositiveInteger]) -> None:
        """
        Set nDataSets with validation.

        Args:
            value: The nDataSets to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nDataSets = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"nDataSets must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._nDataSets = value
        # Please note that these multiple are given in a contiguous area.
        self._nRomBlocks: Optional[PositiveInteger] = None

    @property
    def n_rom_blocks(self) -> Optional[PositiveInteger]:
        """Get nRomBlocks (Pythonic accessor)."""
        return self._nRomBlocks

    @n_rom_blocks.setter
    def n_rom_blocks(self, value: Optional[PositiveInteger]) -> None:
        """
        Set nRomBlocks with validation.

        Args:
            value: The nRomBlocks to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nRomBlocks = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"nRomBlocks must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._nRomBlocks = value
        # controlled.
        self._ramBlockStatus: Optional[RamBlockStatusControlEnum] = None

    @property
    def ram_block_status(self) -> Optional[RamBlockStatusControlEnum]:
        """Get ramBlockStatus (Pythonic accessor)."""
        return self._ramBlockStatus

    @ram_block_status.setter
    def ram_block_status(self, value: Optional[RamBlockStatusControlEnum]) -> None:
        """
        Set ramBlockStatus with validation.

        Args:
            value: The ramBlockStatus to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ramBlockStatus = None
            return

        if not isinstance(value, RamBlockStatusControlEnum):
            raise TypeError(
                f"ramBlockStatus must be RamBlockStatusControlEnum or None, got {type(value).__name__}"
            )
        self._ramBlockStatus = value
        # disabled) restriction 381 Document ID 89:
        # AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate Module Description Template
        # R23-11.
        self._readonly: Optional[Boolean] = None

    @property
    def readonly(self) -> Optional[Boolean]:
        """Get readonly (Pythonic accessor)."""
        return self._readonly

    @readonly.setter
    def readonly(self, value: Optional[Boolean]) -> None:
        """
        Set readonly with validation.

        Args:
            value: The readonly to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._readonly = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"readonly must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._readonly = value
        self._reliability: Optional[NvBlockNeeds] = None

    @property
    def reliability(self) -> Optional[NvBlockNeeds]:
        """Get reliability (Pythonic accessor)."""
        return self._reliability

    @reliability.setter
    def reliability(self, value: Optional[NvBlockNeeds]) -> None:
        """
        Set reliability with validation.

        Args:
            value: The reliability to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._reliability = None
            return

        if not isinstance(value, NvBlockNeeds):
            raise TypeError(
                f"reliability must be NvBlockNeeds or None, got {type(value).__name__}"
            )
        self._reliability = value
                # (true) or not (false).
        # For to handle initialization in the latter case, to the NVRAM specification.
        self._resistantTo: Optional[Boolean] = None

    @property
    def resistant_to(self) -> Optional[Boolean]:
        """Get resistantTo (Pythonic accessor)."""
        return self._resistantTo

    @resistant_to.setter
    def resistant_to(self, value: Optional[Boolean]) -> None:
        """
        Set resistantTo with validation.

        Args:
            value: The resistantTo to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._resistantTo = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"resistantTo must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._resistantTo = value
        # software.
        self._restoreAtStart: Optional[Boolean] = None

    @property
    def restore_at_start(self) -> Optional[Boolean]:
        """Get restoreAtStart (Pythonic accessor)."""
        return self._restoreAtStart

    @restore_at_start.setter
    def restore_at_start(self, value: Optional[Boolean]) -> None:
        """
        Set restoreAtStart with validation.

        Args:
            value: The restoreAtStart to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._restoreAtStart = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"restoreAtStart must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._restoreAtStart = value
        # NvM_FirstInitAll() function.
        self._selectBlockFor: Optional[Boolean] = None

    @property
    def select_block_for(self) -> Optional[Boolean]:
        """Get selectBlockFor (Pythonic accessor)."""
        return self._selectBlockFor

    @select_block_for.setter
    def select_block_for(self, value: Optional[Boolean]) -> None:
        """
        Set selectBlockFor with validation.

        Args:
            value: The selectBlockFor to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._selectBlockFor = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"selectBlockFor must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._selectBlockFor = value
        # shutdown by the basic software.
        self._storeAt: Optional[Boolean] = None

    @property
    def store_at(self) -> Optional[Boolean]:
        """Get storeAt (Pythonic accessor)."""
        return self._storeAt

    @store_at.setter
    def store_at(self, value: Optional[Boolean]) -> None:
        """
        Set storeAt with validation.

        Args:
            value: The storeAt to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._storeAt = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"storeAt must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._storeAt = value
        # the basic software.
        self._storeCyclic: Optional[Boolean] = None

    @property
    def store_cyclic(self) -> Optional[Boolean]:
        """Get storeCyclic (Pythonic accessor)."""
        return self._storeCyclic

    @store_cyclic.setter
    def store_cyclic(self, value: Optional[Boolean]) -> None:
        """
        Set storeCyclic with validation.

        Args:
            value: The storeCyclic to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._storeCyclic = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"storeCyclic must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._storeCyclic = value
                # case of ECU failure (e.
        # g.
        # loss of the basic software.
        # If the attribute store set to true the associated RAM Block shall to have
                # immediate priority.
        self._store: Optional[Boolean] = None

    @property
    def store(self) -> Optional[Boolean]:
        """Get store (Pythonic accessor)."""
        return self._store

    @store.setter
    def store(self, value: Optional[Boolean]) -> None:
        """
        Set store with validation.

        Args:
            value: The store to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._store = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"store must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._store = value
        # during or after execution according SW-C RunnableEntity by the basic.
        self._storeImmediate: Optional[Boolean] = None

    @property
    def store_immediate(self) -> Optional[Boolean]:
        """Get storeImmediate (Pythonic accessor)."""
        return self._storeImmediate

    @store_immediate.setter
    def store_immediate(self, value: Optional[Boolean]) -> None:
        """
        Set storeImmediate with validation.

        Args:
            value: The storeImmediate to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._storeImmediate = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"storeImmediate must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._storeImmediate = value
        # the written value is different value stored in the associated RAM Block(s)
        # during execution of the according SW-C RunnableEntity.
        self._storeOnChange: Optional[Boolean] = None

    @property
    def store_on_change(self) -> Optional[Boolean]:
        """Get storeOnChange (Pythonic accessor)."""
        return self._storeOnChange

    @store_on_change.setter
    def store_on_change(self, value: Optional[Boolean]) -> None:
        """
        Set storeOnChange with validation.

        Args:
            value: The storeOnChange to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._storeOnChange = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"storeOnChange must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._storeOnChange = value
        self._useAuto: Optional[Boolean] = None

    @property
    def use_auto(self) -> Optional[Boolean]:
        """Get useAuto (Pythonic accessor)."""
        return self._useAuto

    @use_auto.setter
    def use_auto(self, value: Optional[Boolean]) -> None:
        """
        Set useAuto with validation.

        Args:
            value: The useAuto to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._useAuto = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"useAuto must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._useAuto = value
        # CRC which was the last successful read or write job in skip unnecessary NVRAM
        # writings.
        self._useCRCComp: Optional[Boolean] = None

    @property
    def use_crc_comp(self) -> Optional[Boolean]:
        """Get useCRCComp (Pythonic accessor)."""
        return self._useCRCComp

    @use_crc_comp.setter
    def use_crc_comp(self, value: Optional[Boolean]) -> None:
        """
        Set useCRCComp with validation.

        Args:
            value: The useCRCComp to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._useCRCComp = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"useCRCComp must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._useCRCComp = value
                # changed/erased replaced with the default ROM data after first the
                # software-component.
        # such restriction.
        self._writeOnlyOnce: Optional[Boolean] = None

    @property
    def write_only_once(self) -> Optional[Boolean]:
        """Get writeOnlyOnce (Pythonic accessor)."""
        return self._writeOnlyOnce

    @write_only_once.setter
    def write_only_once(self, value: Optional[Boolean]) -> None:
        """
        Set writeOnlyOnce with validation.

        Args:
            value: The writeOnlyOnce to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._writeOnlyOnce = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"writeOnlyOnce must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._writeOnlyOnce = value
        self._writeVerification: Optional[Boolean] = None

    @property
    def write_verification(self) -> Optional[Boolean]:
        """Get writeVerification (Pythonic accessor)."""
        return self._writeVerification

    @write_verification.setter
    def write_verification(self, value: Optional[Boolean]) -> None:
        """
        Set writeVerification with validation.

        Args:
            value: The writeVerification to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._writeVerification = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"writeVerification must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._writeVerification = value
        # It has to be provided in "number access per year".
        self._writing: Optional[PositiveInteger] = None

    @property
    def writing(self) -> Optional[PositiveInteger]:
        """Get writing (Pythonic accessor)."""
        return self._writing

    @writing.setter
    def writing(self, value: Optional[PositiveInteger]) -> None:
        """
        Set writing with validation.

        Args:
            value: The writing to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._writing = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"writing must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._writing = value
        # other blocks.
        self._writingPriority: Optional[NvBlockNeedsWritingPriorityEnum] = None

    @property
    def writing_priority(self) -> Optional[NvBlockNeedsWritingPriorityEnum]:
        """Get writingPriority (Pythonic accessor)."""
        return self._writingPriority

    @writing_priority.setter
    def writing_priority(self, value: Optional[NvBlockNeedsWritingPriorityEnum]) -> None:
        """
        Set writingPriority with validation.

        Args:
            value: The writingPriority to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._writingPriority = None
            return

        if not isinstance(value, NvBlockNeedsWritingPriorityEnum):
            raise TypeError(
                f"writingPriority must be NvBlockNeedsWritingPriorityEnum or None, got {type(value).__name__}"
            )
        self._writingPriority = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCalcRamBlock(self) -> Boolean:
        """
        AUTOSAR-compliant getter for calcRamBlock.

        Returns:
            The calcRamBlock value

        Note:
            Delegates to calc_ram_block property (CODING_RULE_V2_00017)
        """
        return self.calc_ram_block  # Delegates to property

    def setCalcRamBlock(self, value: Boolean) -> NvBlockNeeds:
        """
        AUTOSAR-compliant setter for calcRamBlock with method chaining.

        Args:
            value: The calcRamBlock to set

        Returns:
            self for method chaining

        Note:
            Delegates to calc_ram_block property setter (gets validation automatically)
        """
        self.calc_ram_block = value  # Delegates to property setter
        return self

    def getCheckStatic(self) -> Boolean:
        """
        AUTOSAR-compliant getter for checkStatic.

        Returns:
            The checkStatic value

        Note:
            Delegates to check_static property (CODING_RULE_V2_00017)
        """
        return self.check_static  # Delegates to property

    def setCheckStatic(self, value: Boolean) -> NvBlockNeeds:
        """
        AUTOSAR-compliant setter for checkStatic with method chaining.

        Args:
            value: The checkStatic to set

        Returns:
            self for method chaining

        Note:
            Delegates to check_static property setter (gets validation automatically)
        """
        self.check_static = value  # Delegates to property setter
        return self

    def getCyclicWriting(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for cyclicWriting.

        Returns:
            The cyclicWriting value

        Note:
            Delegates to cyclic_writing property (CODING_RULE_V2_00017)
        """
        return self.cyclic_writing  # Delegates to property

    def setCyclicWriting(self, value: TimeValue) -> NvBlockNeeds:
        """
        AUTOSAR-compliant setter for cyclicWriting with method chaining.

        Args:
            value: The cyclicWriting to set

        Returns:
            self for method chaining

        Note:
            Delegates to cyclic_writing property setter (gets validation automatically)
        """
        self.cyclic_writing = value  # Delegates to property setter
        return self

    def getNDataSets(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for nDataSets.

        Returns:
            The nDataSets value

        Note:
            Delegates to n_data_sets property (CODING_RULE_V2_00017)
        """
        return self.n_data_sets  # Delegates to property

    def setNDataSets(self, value: PositiveInteger) -> NvBlockNeeds:
        """
        AUTOSAR-compliant setter for nDataSets with method chaining.

        Args:
            value: The nDataSets to set

        Returns:
            self for method chaining

        Note:
            Delegates to n_data_sets property setter (gets validation automatically)
        """
        self.n_data_sets = value  # Delegates to property setter
        return self

    def getNRomBlocks(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for nRomBlocks.

        Returns:
            The nRomBlocks value

        Note:
            Delegates to n_rom_blocks property (CODING_RULE_V2_00017)
        """
        return self.n_rom_blocks  # Delegates to property

    def setNRomBlocks(self, value: PositiveInteger) -> NvBlockNeeds:
        """
        AUTOSAR-compliant setter for nRomBlocks with method chaining.

        Args:
            value: The nRomBlocks to set

        Returns:
            self for method chaining

        Note:
            Delegates to n_rom_blocks property setter (gets validation automatically)
        """
        self.n_rom_blocks = value  # Delegates to property setter
        return self

    def getRamBlockStatus(self) -> RamBlockStatusControlEnum:
        """
        AUTOSAR-compliant getter for ramBlockStatus.

        Returns:
            The ramBlockStatus value

        Note:
            Delegates to ram_block_status property (CODING_RULE_V2_00017)
        """
        return self.ram_block_status  # Delegates to property

    def setRamBlockStatus(self, value: RamBlockStatusControlEnum) -> NvBlockNeeds:
        """
        AUTOSAR-compliant setter for ramBlockStatus with method chaining.

        Args:
            value: The ramBlockStatus to set

        Returns:
            self for method chaining

        Note:
            Delegates to ram_block_status property setter (gets validation automatically)
        """
        self.ram_block_status = value  # Delegates to property setter
        return self

    def getReadonly(self) -> Boolean:
        """
        AUTOSAR-compliant getter for readonly.

        Returns:
            The readonly value

        Note:
            Delegates to readonly property (CODING_RULE_V2_00017)
        """
        return self.readonly  # Delegates to property

    def setReadonly(self, value: Boolean) -> NvBlockNeeds:
        """
        AUTOSAR-compliant setter for readonly with method chaining.

        Args:
            value: The readonly to set

        Returns:
            self for method chaining

        Note:
            Delegates to readonly property setter (gets validation automatically)
        """
        self.readonly = value  # Delegates to property setter
        return self

    def getReliability(self) -> NvBlockNeeds:
        """
        AUTOSAR-compliant getter for reliability.

        Returns:
            The reliability value

        Note:
            Delegates to reliability property (CODING_RULE_V2_00017)
        """
        return self.reliability  # Delegates to property

    def setReliability(self, value: NvBlockNeeds) -> NvBlockNeeds:
        """
        AUTOSAR-compliant setter for reliability with method chaining.

        Args:
            value: The reliability to set

        Returns:
            self for method chaining

        Note:
            Delegates to reliability property setter (gets validation automatically)
        """
        self.reliability = value  # Delegates to property setter
        return self

    def getResistantTo(self) -> Boolean:
        """
        AUTOSAR-compliant getter for resistantTo.

        Returns:
            The resistantTo value

        Note:
            Delegates to resistant_to property (CODING_RULE_V2_00017)
        """
        return self.resistant_to  # Delegates to property

    def setResistantTo(self, value: Boolean) -> NvBlockNeeds:
        """
        AUTOSAR-compliant setter for resistantTo with method chaining.

        Args:
            value: The resistantTo to set

        Returns:
            self for method chaining

        Note:
            Delegates to resistant_to property setter (gets validation automatically)
        """
        self.resistant_to = value  # Delegates to property setter
        return self

    def getRestoreAtStart(self) -> Boolean:
        """
        AUTOSAR-compliant getter for restoreAtStart.

        Returns:
            The restoreAtStart value

        Note:
            Delegates to restore_at_start property (CODING_RULE_V2_00017)
        """
        return self.restore_at_start  # Delegates to property

    def setRestoreAtStart(self, value: Boolean) -> NvBlockNeeds:
        """
        AUTOSAR-compliant setter for restoreAtStart with method chaining.

        Args:
            value: The restoreAtStart to set

        Returns:
            self for method chaining

        Note:
            Delegates to restore_at_start property setter (gets validation automatically)
        """
        self.restore_at_start = value  # Delegates to property setter
        return self

    def getSelectBlockFor(self) -> Boolean:
        """
        AUTOSAR-compliant getter for selectBlockFor.

        Returns:
            The selectBlockFor value

        Note:
            Delegates to select_block_for property (CODING_RULE_V2_00017)
        """
        return self.select_block_for  # Delegates to property

    def setSelectBlockFor(self, value: Boolean) -> NvBlockNeeds:
        """
        AUTOSAR-compliant setter for selectBlockFor with method chaining.

        Args:
            value: The selectBlockFor to set

        Returns:
            self for method chaining

        Note:
            Delegates to select_block_for property setter (gets validation automatically)
        """
        self.select_block_for = value  # Delegates to property setter
        return self

    def getStoreAt(self) -> Boolean:
        """
        AUTOSAR-compliant getter for storeAt.

        Returns:
            The storeAt value

        Note:
            Delegates to store_at property (CODING_RULE_V2_00017)
        """
        return self.store_at  # Delegates to property

    def setStoreAt(self, value: Boolean) -> NvBlockNeeds:
        """
        AUTOSAR-compliant setter for storeAt with method chaining.

        Args:
            value: The storeAt to set

        Returns:
            self for method chaining

        Note:
            Delegates to store_at property setter (gets validation automatically)
        """
        self.store_at = value  # Delegates to property setter
        return self

    def getStoreCyclic(self) -> Boolean:
        """
        AUTOSAR-compliant getter for storeCyclic.

        Returns:
            The storeCyclic value

        Note:
            Delegates to store_cyclic property (CODING_RULE_V2_00017)
        """
        return self.store_cyclic  # Delegates to property

    def setStoreCyclic(self, value: Boolean) -> NvBlockNeeds:
        """
        AUTOSAR-compliant setter for storeCyclic with method chaining.

        Args:
            value: The storeCyclic to set

        Returns:
            self for method chaining

        Note:
            Delegates to store_cyclic property setter (gets validation automatically)
        """
        self.store_cyclic = value  # Delegates to property setter
        return self

    def getStore(self) -> Boolean:
        """
        AUTOSAR-compliant getter for store.

        Returns:
            The store value

        Note:
            Delegates to store property (CODING_RULE_V2_00017)
        """
        return self.store  # Delegates to property

    def setStore(self, value: Boolean) -> NvBlockNeeds:
        """
        AUTOSAR-compliant setter for store with method chaining.

        Args:
            value: The store to set

        Returns:
            self for method chaining

        Note:
            Delegates to store property setter (gets validation automatically)
        """
        self.store = value  # Delegates to property setter
        return self

    def getStoreImmediate(self) -> Boolean:
        """
        AUTOSAR-compliant getter for storeImmediate.

        Returns:
            The storeImmediate value

        Note:
            Delegates to store_immediate property (CODING_RULE_V2_00017)
        """
        return self.store_immediate  # Delegates to property

    def setStoreImmediate(self, value: Boolean) -> NvBlockNeeds:
        """
        AUTOSAR-compliant setter for storeImmediate with method chaining.

        Args:
            value: The storeImmediate to set

        Returns:
            self for method chaining

        Note:
            Delegates to store_immediate property setter (gets validation automatically)
        """
        self.store_immediate = value  # Delegates to property setter
        return self

    def getStoreOnChange(self) -> Boolean:
        """
        AUTOSAR-compliant getter for storeOnChange.

        Returns:
            The storeOnChange value

        Note:
            Delegates to store_on_change property (CODING_RULE_V2_00017)
        """
        return self.store_on_change  # Delegates to property

    def setStoreOnChange(self, value: Boolean) -> NvBlockNeeds:
        """
        AUTOSAR-compliant setter for storeOnChange with method chaining.

        Args:
            value: The storeOnChange to set

        Returns:
            self for method chaining

        Note:
            Delegates to store_on_change property setter (gets validation automatically)
        """
        self.store_on_change = value  # Delegates to property setter
        return self

    def getUseAuto(self) -> Boolean:
        """
        AUTOSAR-compliant getter for useAuto.

        Returns:
            The useAuto value

        Note:
            Delegates to use_auto property (CODING_RULE_V2_00017)
        """
        return self.use_auto  # Delegates to property

    def setUseAuto(self, value: Boolean) -> NvBlockNeeds:
        """
        AUTOSAR-compliant setter for useAuto with method chaining.

        Args:
            value: The useAuto to set

        Returns:
            self for method chaining

        Note:
            Delegates to use_auto property setter (gets validation automatically)
        """
        self.use_auto = value  # Delegates to property setter
        return self

    def getUseCRCComp(self) -> Boolean:
        """
        AUTOSAR-compliant getter for useCRCComp.

        Returns:
            The useCRCComp value

        Note:
            Delegates to use_crc_comp property (CODING_RULE_V2_00017)
        """
        return self.use_crc_comp  # Delegates to property

    def setUseCRCComp(self, value: Boolean) -> NvBlockNeeds:
        """
        AUTOSAR-compliant setter for useCRCComp with method chaining.

        Args:
            value: The useCRCComp to set

        Returns:
            self for method chaining

        Note:
            Delegates to use_crc_comp property setter (gets validation automatically)
        """
        self.use_crc_comp = value  # Delegates to property setter
        return self

    def getWriteOnlyOnce(self) -> Boolean:
        """
        AUTOSAR-compliant getter for writeOnlyOnce.

        Returns:
            The writeOnlyOnce value

        Note:
            Delegates to write_only_once property (CODING_RULE_V2_00017)
        """
        return self.write_only_once  # Delegates to property

    def setWriteOnlyOnce(self, value: Boolean) -> NvBlockNeeds:
        """
        AUTOSAR-compliant setter for writeOnlyOnce with method chaining.

        Args:
            value: The writeOnlyOnce to set

        Returns:
            self for method chaining

        Note:
            Delegates to write_only_once property setter (gets validation automatically)
        """
        self.write_only_once = value  # Delegates to property setter
        return self

    def getWriteVerification(self) -> Boolean:
        """
        AUTOSAR-compliant getter for writeVerification.

        Returns:
            The writeVerification value

        Note:
            Delegates to write_verification property (CODING_RULE_V2_00017)
        """
        return self.write_verification  # Delegates to property

    def setWriteVerification(self, value: Boolean) -> NvBlockNeeds:
        """
        AUTOSAR-compliant setter for writeVerification with method chaining.

        Args:
            value: The writeVerification to set

        Returns:
            self for method chaining

        Note:
            Delegates to write_verification property setter (gets validation automatically)
        """
        self.write_verification = value  # Delegates to property setter
        return self

    def getWriting(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for writing.

        Returns:
            The writing value

        Note:
            Delegates to writing property (CODING_RULE_V2_00017)
        """
        return self.writing  # Delegates to property

    def setWriting(self, value: PositiveInteger) -> NvBlockNeeds:
        """
        AUTOSAR-compliant setter for writing with method chaining.

        Args:
            value: The writing to set

        Returns:
            self for method chaining

        Note:
            Delegates to writing property setter (gets validation automatically)
        """
        self.writing = value  # Delegates to property setter
        return self

    def getWritingPriority(self) -> NvBlockNeedsWritingPriorityEnum:
        """
        AUTOSAR-compliant getter for writingPriority.

        Returns:
            The writingPriority value

        Note:
            Delegates to writing_priority property (CODING_RULE_V2_00017)
        """
        return self.writing_priority  # Delegates to property

    def setWritingPriority(self, value: NvBlockNeedsWritingPriorityEnum) -> NvBlockNeeds:
        """
        AUTOSAR-compliant setter for writingPriority with method chaining.

        Args:
            value: The writingPriority to set

        Returns:
            self for method chaining

        Note:
            Delegates to writing_priority property setter (gets validation automatically)
        """
        self.writing_priority = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_calc_ram_block(self, value: Optional[Boolean]) -> NvBlockNeeds:
        """
        Set calcRamBlock and return self for chaining.

        Args:
            value: The calcRamBlock to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_calc_ram_block("value")
        """
        self.calc_ram_block = value  # Use property setter (gets validation)
        return self

    def with_check_static(self, value: Optional[Boolean]) -> NvBlockNeeds:
        """
        Set checkStatic and return self for chaining.

        Args:
            value: The checkStatic to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_check_static("value")
        """
        self.check_static = value  # Use property setter (gets validation)
        return self

    def with_cyclic_writing(self, value: Optional[TimeValue]) -> NvBlockNeeds:
        """
        Set cyclicWriting and return self for chaining.

        Args:
            value: The cyclicWriting to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_cyclic_writing("value")
        """
        self.cyclic_writing = value  # Use property setter (gets validation)
        return self

    def with_n_data_sets(self, value: Optional[PositiveInteger]) -> NvBlockNeeds:
        """
        Set nDataSets and return self for chaining.

        Args:
            value: The nDataSets to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_n_data_sets("value")
        """
        self.n_data_sets = value  # Use property setter (gets validation)
        return self

    def with_n_rom_blocks(self, value: Optional[PositiveInteger]) -> NvBlockNeeds:
        """
        Set nRomBlocks and return self for chaining.

        Args:
            value: The nRomBlocks to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_n_rom_blocks("value")
        """
        self.n_rom_blocks = value  # Use property setter (gets validation)
        return self

    def with_ram_block_status(self, value: Optional[RamBlockStatusControlEnum]) -> NvBlockNeeds:
        """
        Set ramBlockStatus and return self for chaining.

        Args:
            value: The ramBlockStatus to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ram_block_status("value")
        """
        self.ram_block_status = value  # Use property setter (gets validation)
        return self

    def with_readonly(self, value: Optional[Boolean]) -> NvBlockNeeds:
        """
        Set readonly and return self for chaining.

        Args:
            value: The readonly to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_readonly("value")
        """
        self.readonly = value  # Use property setter (gets validation)
        return self

    def with_reliability(self, value: Optional[NvBlockNeeds]) -> NvBlockNeeds:
        """
        Set reliability and return self for chaining.

        Args:
            value: The reliability to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_reliability("value")
        """
        self.reliability = value  # Use property setter (gets validation)
        return self

    def with_resistant_to(self, value: Optional[Boolean]) -> NvBlockNeeds:
        """
        Set resistantTo and return self for chaining.

        Args:
            value: The resistantTo to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_resistant_to("value")
        """
        self.resistant_to = value  # Use property setter (gets validation)
        return self

    def with_restore_at_start(self, value: Optional[Boolean]) -> NvBlockNeeds:
        """
        Set restoreAtStart and return self for chaining.

        Args:
            value: The restoreAtStart to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_restore_at_start("value")
        """
        self.restore_at_start = value  # Use property setter (gets validation)
        return self

    def with_select_block_for(self, value: Optional[Boolean]) -> NvBlockNeeds:
        """
        Set selectBlockFor and return self for chaining.

        Args:
            value: The selectBlockFor to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_select_block_for("value")
        """
        self.select_block_for = value  # Use property setter (gets validation)
        return self

    def with_store_at(self, value: Optional[Boolean]) -> NvBlockNeeds:
        """
        Set storeAt and return self for chaining.

        Args:
            value: The storeAt to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_store_at("value")
        """
        self.store_at = value  # Use property setter (gets validation)
        return self

    def with_store_cyclic(self, value: Optional[Boolean]) -> NvBlockNeeds:
        """
        Set storeCyclic and return self for chaining.

        Args:
            value: The storeCyclic to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_store_cyclic("value")
        """
        self.store_cyclic = value  # Use property setter (gets validation)
        return self

    def with_store(self, value: Optional[Boolean]) -> NvBlockNeeds:
        """
        Set store and return self for chaining.

        Args:
            value: The store to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_store("value")
        """
        self.store = value  # Use property setter (gets validation)
        return self

    def with_store_immediate(self, value: Optional[Boolean]) -> NvBlockNeeds:
        """
        Set storeImmediate and return self for chaining.

        Args:
            value: The storeImmediate to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_store_immediate("value")
        """
        self.store_immediate = value  # Use property setter (gets validation)
        return self

    def with_store_on_change(self, value: Optional[Boolean]) -> NvBlockNeeds:
        """
        Set storeOnChange and return self for chaining.

        Args:
            value: The storeOnChange to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_store_on_change("value")
        """
        self.store_on_change = value  # Use property setter (gets validation)
        return self

    def with_use_auto(self, value: Optional[Boolean]) -> NvBlockNeeds:
        """
        Set useAuto and return self for chaining.

        Args:
            value: The useAuto to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_use_auto("value")
        """
        self.use_auto = value  # Use property setter (gets validation)
        return self

    def with_use_crc_comp(self, value: Optional[Boolean]) -> NvBlockNeeds:
        """
        Set useCRCComp and return self for chaining.

        Args:
            value: The useCRCComp to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_use_crc_comp("value")
        """
        self.use_crc_comp = value  # Use property setter (gets validation)
        return self

    def with_write_only_once(self, value: Optional[Boolean]) -> NvBlockNeeds:
        """
        Set writeOnlyOnce and return self for chaining.

        Args:
            value: The writeOnlyOnce to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_write_only_once("value")
        """
        self.write_only_once = value  # Use property setter (gets validation)
        return self

    def with_write_verification(self, value: Optional[Boolean]) -> NvBlockNeeds:
        """
        Set writeVerification and return self for chaining.

        Args:
            value: The writeVerification to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_write_verification("value")
        """
        self.write_verification = value  # Use property setter (gets validation)
        return self

    def with_writing(self, value: Optional[PositiveInteger]) -> NvBlockNeeds:
        """
        Set writing and return self for chaining.

        Args:
            value: The writing to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_writing("value")
        """
        self.writing = value  # Use property setter (gets validation)
        return self

    def with_writing_priority(self, value: Optional[NvBlockNeedsWritingPriorityEnum]) -> NvBlockNeeds:
        """
        Set writingPriority and return self for chaining.

        Args:
            value: The writingPriority to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_writing_priority("value")
        """
        self.writing_priority = value  # Use property setter (gets validation)
        return self



class SupervisedEntityNeeds(ServiceNeeds):
    """
    that this value has to be recalculated with respect to the WdgM’s own cycle
    time for ECU configuration. Table 12.12: SupervisedEntityNeeds 234 of 381
    Document ID 89: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate Basic Software
    Module Description Template AUTOSAR CP R23-11

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::SupervisedEntityNeeds

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 234, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 707, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # true/false: supervision activation status of Supervised be enabled/disabled
        # at start.
        self._activateAtStart: Optional[Boolean] = None

    @property
    def activate_at_start(self) -> Optional[Boolean]:
        """Get activateAtStart (Pythonic accessor)."""
        return self._activateAtStart

    @activate_at_start.setter
    def activate_at_start(self, value: Optional[Boolean]) -> None:
        """
        Set activateAtStart with validation.

        Args:
            value: The activateAtStart to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._activateAtStart = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"activateAtStart must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._activateAtStart = value
        # atpVariation.
        self._checkpoints: List["SupervisedEntity"] = []

    @property
    def checkpoints(self) -> List["SupervisedEntity"]:
        """Get checkpoints (Pythonic accessor)."""
        return self._checkpoints
        # true: software-component shall be allowed to deactivate of this
        # SupervisedEntity shall be not allowed to of this SupervisedEntity.
        self._enable: Optional[Boolean] = None

    @property
    def enable(self) -> Optional[Boolean]:
        """Get enable (Pythonic accessor)."""
        return self._enable

    @enable.setter
    def enable(self, value: Optional[Boolean]) -> None:
        """
        Set enable with validation.

        Args:
            value: The enable to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._enable = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"enable must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._enable = value
        self._expectedAlive: Optional[TimeValue] = None

    @property
    def expected_alive(self) -> Optional[TimeValue]:
        """Get expectedAlive (Pythonic accessor)."""
        return self._expectedAlive

    @expected_alive.setter
    def expected_alive(self, value: Optional[TimeValue]) -> None:
        """
        Set expectedAlive with validation.

        Args:
            value: The expectedAlive to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._expectedAlive = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"expectedAlive must be TimeValue or None, got {type(value).__name__}"
            )
        self._expectedAlive = value
        self._maxAliveCycle: Optional[TimeValue] = None

    @property
    def max_alive_cycle(self) -> Optional[TimeValue]:
        """Get maxAliveCycle (Pythonic accessor)."""
        return self._maxAliveCycle

    @max_alive_cycle.setter
    def max_alive_cycle(self, value: Optional[TimeValue]) -> None:
        """
        Set maxAliveCycle with validation.

        Args:
            value: The maxAliveCycle to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxAliveCycle = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"maxAliveCycle must be TimeValue or None, got {type(value).__name__}"
            )
        self._maxAliveCycle = value
        self._minAliveCycle: Optional[TimeValue] = None

    @property
    def min_alive_cycle(self) -> Optional[TimeValue]:
        """Get minAliveCycle (Pythonic accessor)."""
        return self._minAliveCycle

    @min_alive_cycle.setter
    def min_alive_cycle(self, value: Optional[TimeValue]) -> None:
        """
        Set minAliveCycle with validation.

        Args:
            value: The minAliveCycle to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._minAliveCycle = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"minAliveCycle must be TimeValue or None, got {type(value).__name__}"
            )
        self._minAliveCycle = value
        # until the of the SupervisedEntity is set to SWS WdgM for more.
        self._toleratedFailed: Optional[PositiveInteger] = None

    @property
    def tolerated_failed(self) -> Optional[PositiveInteger]:
        """Get toleratedFailed (Pythonic accessor)."""
        return self._toleratedFailed

    @tolerated_failed.setter
    def tolerated_failed(self, value: Optional[PositiveInteger]) -> None:
        """
        Set toleratedFailed with validation.

        Args:
            value: The toleratedFailed to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._toleratedFailed = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"toleratedFailed must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._toleratedFailed = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getActivateAtStart(self) -> Boolean:
        """
        AUTOSAR-compliant getter for activateAtStart.

        Returns:
            The activateAtStart value

        Note:
            Delegates to activate_at_start property (CODING_RULE_V2_00017)
        """
        return self.activate_at_start  # Delegates to property

    def setActivateAtStart(self, value: Boolean) -> SupervisedEntityNeeds:
        """
        AUTOSAR-compliant setter for activateAtStart with method chaining.

        Args:
            value: The activateAtStart to set

        Returns:
            self for method chaining

        Note:
            Delegates to activate_at_start property setter (gets validation automatically)
        """
        self.activate_at_start = value  # Delegates to property setter
        return self

    def getCheckpoints(self) -> List["SupervisedEntity"]:
        """
        AUTOSAR-compliant getter for checkpoints.

        Returns:
            The checkpoints value

        Note:
            Delegates to checkpoints property (CODING_RULE_V2_00017)
        """
        return self.checkpoints  # Delegates to property

    def getEnable(self) -> Boolean:
        """
        AUTOSAR-compliant getter for enable.

        Returns:
            The enable value

        Note:
            Delegates to enable property (CODING_RULE_V2_00017)
        """
        return self.enable  # Delegates to property

    def setEnable(self, value: Boolean) -> SupervisedEntityNeeds:
        """
        AUTOSAR-compliant setter for enable with method chaining.

        Args:
            value: The enable to set

        Returns:
            self for method chaining

        Note:
            Delegates to enable property setter (gets validation automatically)
        """
        self.enable = value  # Delegates to property setter
        return self

    def getExpectedAlive(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for expectedAlive.

        Returns:
            The expectedAlive value

        Note:
            Delegates to expected_alive property (CODING_RULE_V2_00017)
        """
        return self.expected_alive  # Delegates to property

    def setExpectedAlive(self, value: TimeValue) -> SupervisedEntityNeeds:
        """
        AUTOSAR-compliant setter for expectedAlive with method chaining.

        Args:
            value: The expectedAlive to set

        Returns:
            self for method chaining

        Note:
            Delegates to expected_alive property setter (gets validation automatically)
        """
        self.expected_alive = value  # Delegates to property setter
        return self

    def getMaxAliveCycle(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for maxAliveCycle.

        Returns:
            The maxAliveCycle value

        Note:
            Delegates to max_alive_cycle property (CODING_RULE_V2_00017)
        """
        return self.max_alive_cycle  # Delegates to property

    def setMaxAliveCycle(self, value: TimeValue) -> SupervisedEntityNeeds:
        """
        AUTOSAR-compliant setter for maxAliveCycle with method chaining.

        Args:
            value: The maxAliveCycle to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_alive_cycle property setter (gets validation automatically)
        """
        self.max_alive_cycle = value  # Delegates to property setter
        return self

    def getMinAliveCycle(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for minAliveCycle.

        Returns:
            The minAliveCycle value

        Note:
            Delegates to min_alive_cycle property (CODING_RULE_V2_00017)
        """
        return self.min_alive_cycle  # Delegates to property

    def setMinAliveCycle(self, value: TimeValue) -> SupervisedEntityNeeds:
        """
        AUTOSAR-compliant setter for minAliveCycle with method chaining.

        Args:
            value: The minAliveCycle to set

        Returns:
            self for method chaining

        Note:
            Delegates to min_alive_cycle property setter (gets validation automatically)
        """
        self.min_alive_cycle = value  # Delegates to property setter
        return self

    def getToleratedFailed(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for toleratedFailed.

        Returns:
            The toleratedFailed value

        Note:
            Delegates to tolerated_failed property (CODING_RULE_V2_00017)
        """
        return self.tolerated_failed  # Delegates to property

    def setToleratedFailed(self, value: PositiveInteger) -> SupervisedEntityNeeds:
        """
        AUTOSAR-compliant setter for toleratedFailed with method chaining.

        Args:
            value: The toleratedFailed to set

        Returns:
            self for method chaining

        Note:
            Delegates to tolerated_failed property setter (gets validation automatically)
        """
        self.tolerated_failed = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_activate_at_start(self, value: Optional[Boolean]) -> SupervisedEntityNeeds:
        """
        Set activateAtStart and return self for chaining.

        Args:
            value: The activateAtStart to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_activate_at_start("value")
        """
        self.activate_at_start = value  # Use property setter (gets validation)
        return self

    def with_enable(self, value: Optional[Boolean]) -> SupervisedEntityNeeds:
        """
        Set enable and return self for chaining.

        Args:
            value: The enable to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_enable("value")
        """
        self.enable = value  # Use property setter (gets validation)
        return self

    def with_expected_alive(self, value: Optional[TimeValue]) -> SupervisedEntityNeeds:
        """
        Set expectedAlive and return self for chaining.

        Args:
            value: The expectedAlive to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_expected_alive("value")
        """
        self.expected_alive = value  # Use property setter (gets validation)
        return self

    def with_max_alive_cycle(self, value: Optional[TimeValue]) -> SupervisedEntityNeeds:
        """
        Set maxAliveCycle and return self for chaining.

        Args:
            value: The maxAliveCycle to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_alive_cycle("value")
        """
        self.max_alive_cycle = value  # Use property setter (gets validation)
        return self

    def with_min_alive_cycle(self, value: Optional[TimeValue]) -> SupervisedEntityNeeds:
        """
        Set minAliveCycle and return self for chaining.

        Args:
            value: The minAliveCycle to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_min_alive_cycle("value")
        """
        self.min_alive_cycle = value  # Use property setter (gets validation)
        return self

    def with_tolerated_failed(self, value: Optional[PositiveInteger]) -> SupervisedEntityNeeds:
        """
        Set toleratedFailed and return self for chaining.

        Args:
            value: The toleratedFailed to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tolerated_failed("value")
        """
        self.tolerated_failed = value  # Use property setter (gets validation)
        return self



class ComMgrUserNeeds(ServiceNeeds):
    """
    Specifies the abstract needs on the configuration of the Communication
    Manager for one "user".

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::ComMgrUserNeeds

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 235, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 711, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Maximum communication mode requested by this ComM.
        self._maxComm: Optional[MaxCommModeEnum] = None

    @property
    def max_comm(self) -> Optional[MaxCommModeEnum]:
        """Get maxComm (Pythonic accessor)."""
        return self._maxComm

    @max_comm.setter
    def max_comm(self, value: Optional[MaxCommModeEnum]) -> None:
        """
        Set maxComm with validation.

        Args:
            value: The maxComm to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxComm = None
            return

        if not isinstance(value, MaxCommModeEnum):
            raise TypeError(
                f"maxComm must be MaxCommModeEnum or None, got {type(value).__name__}"
            )
        self._maxComm = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMaxComm(self) -> MaxCommModeEnum:
        """
        AUTOSAR-compliant getter for maxComm.

        Returns:
            The maxComm value

        Note:
            Delegates to max_comm property (CODING_RULE_V2_00017)
        """
        return self.max_comm  # Delegates to property

    def setMaxComm(self, value: MaxCommModeEnum) -> ComMgrUserNeeds:
        """
        AUTOSAR-compliant setter for maxComm with method chaining.

        Args:
            value: The maxComm to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_comm property setter (gets validation automatically)
        """
        self.max_comm = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_max_comm(self, value: Optional[MaxCommModeEnum]) -> ComMgrUserNeeds:
        """
        Set maxComm and return self for chaining.

        Args:
            value: The maxComm to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_comm("value")
        """
        self.max_comm = value  # Use property setter (gets validation)
        return self



class EcuStateMgrUserNeeds(ServiceNeeds):
    """
    Specifies the abstract needs on the configuration of the ECU State Manager
    for one "user". This class currently contains no attributes. Its name can be
    regarded as a symbol identifying the user from the viewpoint of the
    component or module which owns this class.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::EcuStateMgrUserNeeds

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 235, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 714, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class CryptoServiceNeeds(ServiceNeeds):
    """
    Specifies the needs on the configuration of the CryptoServiceManager for one
    ConfigID (see Specification AUTOSAR_SWS_CSM.doc). An instance of this class
    is used to find out which ports of a software-component belong to this
    ConfigID.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::CryptoServiceNeeds

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 235, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 733, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute represents a description of the family (e.
        # g.
        # crypto algorithm implemented by the crypto case.
        self._algorithmFamily: Optional[String] = None

    @property
    def algorithm_family(self) -> Optional[String]:
        """Get algorithmFamily (Pythonic accessor)."""
        return self._algorithmFamily

    @algorithm_family.setter
    def algorithm_family(self, value: Optional[String]) -> None:
        """
        Set algorithmFamily with validation.

        Args:
            value: The algorithmFamily to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._algorithmFamily = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"algorithmFamily must be String or str or None, got {type(value).__name__}"
            )
        self._algorithmFamily = value
        self._algorithmMode: Optional[String] = None

    @property
    def algorithm_mode(self) -> Optional[String]:
        """Get algorithmMode (Pythonic accessor)."""
        return self._algorithmMode

    @algorithm_mode.setter
    def algorithm_mode(self, value: Optional[String]) -> None:
        """
        Set algorithmMode with validation.

        Args:
            value: The algorithmMode to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._algorithmMode = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"algorithmMode must be String or str or None, got {type(value).__name__}"
            )
        self._algorithmMode = value
        # The goal is to pass a hint for about how to treat the corresponding case.
        self._cryptoKey: Optional[String] = None

    @property
    def crypto_key(self) -> Optional[String]:
        """Get cryptoKey (Pythonic accessor)."""
        return self._cryptoKey

    @crypto_key.setter
    def crypto_key(self, value: Optional[String]) -> None:
        """
        Set cryptoKey with validation.

        Args:
            value: The cryptoKey to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._cryptoKey = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"cryptoKey must be String or str or None, got {type(value).__name__}"
            )
        self._cryptoKey = value
        # software-component or module for this bit.
        self._maximumKey: Optional[PositiveInteger] = None

    @property
    def maximum_key(self) -> Optional[PositiveInteger]:
        """Get maximumKey (Pythonic accessor)."""
        return self._maximumKey

    @maximum_key.setter
    def maximum_key(self, value: Optional[PositiveInteger]) -> None:
        """
        Set maximumKey with validation.

        Args:
            value: The maximumKey to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maximumKey = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"maximumKey must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._maximumKey = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAlgorithmFamily(self) -> String:
        """
        AUTOSAR-compliant getter for algorithmFamily.

        Returns:
            The algorithmFamily value

        Note:
            Delegates to algorithm_family property (CODING_RULE_V2_00017)
        """
        return self.algorithm_family  # Delegates to property

    def setAlgorithmFamily(self, value: String) -> CryptoServiceNeeds:
        """
        AUTOSAR-compliant setter for algorithmFamily with method chaining.

        Args:
            value: The algorithmFamily to set

        Returns:
            self for method chaining

        Note:
            Delegates to algorithm_family property setter (gets validation automatically)
        """
        self.algorithm_family = value  # Delegates to property setter
        return self

    def getAlgorithmMode(self) -> String:
        """
        AUTOSAR-compliant getter for algorithmMode.

        Returns:
            The algorithmMode value

        Note:
            Delegates to algorithm_mode property (CODING_RULE_V2_00017)
        """
        return self.algorithm_mode  # Delegates to property

    def setAlgorithmMode(self, value: String) -> CryptoServiceNeeds:
        """
        AUTOSAR-compliant setter for algorithmMode with method chaining.

        Args:
            value: The algorithmMode to set

        Returns:
            self for method chaining

        Note:
            Delegates to algorithm_mode property setter (gets validation automatically)
        """
        self.algorithm_mode = value  # Delegates to property setter
        return self

    def getCryptoKey(self) -> String:
        """
        AUTOSAR-compliant getter for cryptoKey.

        Returns:
            The cryptoKey value

        Note:
            Delegates to crypto_key property (CODING_RULE_V2_00017)
        """
        return self.crypto_key  # Delegates to property

    def setCryptoKey(self, value: String) -> CryptoServiceNeeds:
        """
        AUTOSAR-compliant setter for cryptoKey with method chaining.

        Args:
            value: The cryptoKey to set

        Returns:
            self for method chaining

        Note:
            Delegates to crypto_key property setter (gets validation automatically)
        """
        self.crypto_key = value  # Delegates to property setter
        return self

    def getMaximumKey(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for maximumKey.

        Returns:
            The maximumKey value

        Note:
            Delegates to maximum_key property (CODING_RULE_V2_00017)
        """
        return self.maximum_key  # Delegates to property

    def setMaximumKey(self, value: PositiveInteger) -> CryptoServiceNeeds:
        """
        AUTOSAR-compliant setter for maximumKey with method chaining.

        Args:
            value: The maximumKey to set

        Returns:
            self for method chaining

        Note:
            Delegates to maximum_key property setter (gets validation automatically)
        """
        self.maximum_key = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_algorithm_family(self, value: Optional[String]) -> CryptoServiceNeeds:
        """
        Set algorithmFamily and return self for chaining.

        Args:
            value: The algorithmFamily to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_algorithm_family("value")
        """
        self.algorithm_family = value  # Use property setter (gets validation)
        return self

    def with_algorithm_mode(self, value: Optional[String]) -> CryptoServiceNeeds:
        """
        Set algorithmMode and return self for chaining.

        Args:
            value: The algorithmMode to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_algorithm_mode("value")
        """
        self.algorithm_mode = value  # Use property setter (gets validation)
        return self

    def with_crypto_key(self, value: Optional[String]) -> CryptoServiceNeeds:
        """
        Set cryptoKey and return self for chaining.

        Args:
            value: The cryptoKey to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_crypto_key("value")
        """
        self.crypto_key = value  # Use property setter (gets validation)
        return self

    def with_maximum_key(self, value: Optional[PositiveInteger]) -> CryptoServiceNeeds:
        """
        Set maximumKey and return self for chaining.

        Args:
            value: The maximumKey to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_maximum_key("value")
        """
        self.maximum_key = value  # Use property setter (gets validation)
        return self



class DltUserNeeds(ServiceNeeds):
    """
    This meta-class specifies the needs on the configuration of the Diagnostic
    Log and Trace module for one SessionId. This class currently contains no
    attributes. An instance of this class is used to find out which
    PortPrototypes of an AtomicSwComponentType belong to this SessionId in order
    to group the request and response PortPrototypes of the same SessionId. The
    actual SessionId value is stored in the PortDefinedArgumentValue of the
    respective PortPrototype specification.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::DltUserNeeds

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 236, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 817, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class SyncTimeBaseMgrUserNeeds(ServiceNeeds):
    """
    Specifies the needs on the configuration of the Synchronized Time-base
    Manager for one time-base. This class currently contains no attributes. An
    instance of this class is used to find out which ports of a
    software-component belong to this time-base in order to group the request
    and response ports of the same time-base. The actual time-base value is
    stored in the PortDefinedArgumentValue of the respective port specification.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::SyncTimeBaseMgrUserNeeds

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 236, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 818, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class DiagnosticCapabilityElement(ServiceNeeds, ABC):
    """
    that with the implementation of a generic tracing concept in AUTOSAR this
    attribute might become obsolete. (cid:53) 236 of 381 Document ID 89:
    AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate Basic Software Module
    Description Template AUTOSAR CP R23-11 (cid:52)

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::DiagnosticCapabilityElement

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 236, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 753, Classic Platform
      R23-11)
    """
    def __init__(self):
        if type(self) is DiagnosticCapabilityElement:
            raise TypeError("DiagnosticCapabilityElement is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This specifies the intended audience for the diagnostic Note that this is not
        # only for the documentation but audience specific implementation.
        self._audience: List[DiagnosticAudienceEnum] = []

    @property
    def audience(self) -> List[DiagnosticAudienceEnum]:
        """Get audience (Pythonic accessor)."""
        return self._audience
        # This denotes the requirement identifier to which the object can be linked to.
        self._diag: Optional[DiagRequirementId] = None

    @property
    def diag(self) -> Optional[DiagRequirementId]:
        """Get diag (Pythonic accessor)."""
        return self._diag

    @diag.setter
    def diag(self, value: Optional[DiagRequirementId]) -> None:
        """
        Set diag with validation.

        Args:
            value: The diag to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._diag = None
            return

        if not isinstance(value, DiagRequirementId):
            raise TypeError(
                f"diag must be DiagRequirementId or None, got {type(value).__name__}"
            )
        self._diag = value
                # object.
        # The higher the level the for the security exists.
        # shall be mapped to the security level in the.
        self._securityAccess: Optional[PositiveInteger] = None

    @property
    def security_access(self) -> Optional[PositiveInteger]:
        """Get securityAccess (Pythonic accessor)."""
        return self._securityAccess

    @security_access.setter
    def security_access(self, value: Optional[PositiveInteger]) -> None:
        """
        Set securityAccess with validation.

        Args:
            value: The securityAccess to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._securityAccess = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"securityAccess must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._securityAccess = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAudience(self) -> List[DiagnosticAudienceEnum]:
        """
        AUTOSAR-compliant getter for audience.

        Returns:
            The audience value

        Note:
            Delegates to audience property (CODING_RULE_V2_00017)
        """
        return self.audience  # Delegates to property

    def getDiag(self) -> DiagRequirementId:
        """
        AUTOSAR-compliant getter for diag.

        Returns:
            The diag value

        Note:
            Delegates to diag property (CODING_RULE_V2_00017)
        """
        return self.diag  # Delegates to property

    def setDiag(self, value: DiagRequirementId) -> DiagnosticCapabilityElement:
        """
        AUTOSAR-compliant setter for diag with method chaining.

        Args:
            value: The diag to set

        Returns:
            self for method chaining

        Note:
            Delegates to diag property setter (gets validation automatically)
        """
        self.diag = value  # Delegates to property setter
        return self

    def getSecurityAccess(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for securityAccess.

        Returns:
            The securityAccess value

        Note:
            Delegates to security_access property (CODING_RULE_V2_00017)
        """
        return self.security_access  # Delegates to property

    def setSecurityAccess(self, value: PositiveInteger) -> DiagnosticCapabilityElement:
        """
        AUTOSAR-compliant setter for securityAccess with method chaining.

        Args:
            value: The securityAccess to set

        Returns:
            self for method chaining

        Note:
            Delegates to security_access property setter (gets validation automatically)
        """
        self.security_access = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_diag(self, value: Optional[DiagRequirementId]) -> DiagnosticCapabilityElement:
        """
        Set diag and return self for chaining.

        Args:
            value: The diag to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_diag("value")
        """
        self.diag = value  # Use property setter (gets validation)
        return self

    def with_security_access(self, value: Optional[PositiveInteger]) -> DiagnosticCapabilityElement:
        """
        Set securityAccess and return self for chaining.

        Args:
            value: The securityAccess to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_security_access("value")
        """
        self.security_access = value  # Use property setter (gets validation)
        return self



class FunctionInhibitionNeeds(ServiceNeeds):
    """
    Specifies the abstract needs on the configuration of the Function Inhibition
    Manager for one Function Identifier (FID). This class currently contains no
    attributes. Its name can be regarded as a symbol identifying the FID from
    the viewpoint of the component or module which owns this class.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::FunctionInhibitionNeeds

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 237, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 265, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 750, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class DoIpServiceNeeds(ServiceNeeds, ABC):
    """
    This represents an abstract base class for ServiceNeeds related to DoIP.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::DoIpServiceNeeds

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 237, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 805, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2020, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is DoIpServiceNeeds:
            raise TypeError("DoIpServiceNeeds is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class SupervisedEntityCheckpointNeeds(ServiceNeeds):
    """
    Specifies the abstract needs on the configuration of the Watchdog Manager to
    support a Checkpoint for a Supervised Entity.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::SupervisedEntityCheckpointNeeds

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 254, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 708, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class ErrorTracerNeeds(ServiceNeeds):
    """
    Specifies the need to report failures to the error tracer.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::ErrorTracerNeeds

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 263, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 832, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # list of traced failures atpVariation.
        self._tracedFailure: List[TracedFailure] = []

    @property
    def traced_failure(self) -> List[TracedFailure]:
        """Get tracedFailure (Pythonic accessor)."""
        return self._tracedFailure

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTracedFailure(self) -> List[TracedFailure]:
        """
        AUTOSAR-compliant getter for tracedFailure.

        Returns:
            The tracedFailure value

        Note:
            Delegates to traced_failure property (CODING_RULE_V2_00017)
        """
        return self.traced_failure  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class HardwareTestNeeds(ServiceNeeds):
    """
    This meta-class represents the ability to indicate that a software-component
    is interested in the results of the hardware test and will establish a
    PortPrototype to query the hardware test manager.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::HardwareTestNeeds

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 264, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 841, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class FunctionInhibitionAvailabilityNeeds(ServiceNeeds):
    """
    Specifies the abstract needs on the configuration of the Function Inhibition
    Manager to provide the control function for one Function Identifier (FID).

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::FunctionInhibitionAvailabilityNeeds

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 318, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 751, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference represents the controlled FID.
        self._controlledFid: Optional[FunctionInhibitionNeeds] = None

    @property
    def controlled_fid(self) -> Optional[FunctionInhibitionNeeds]:
        """Get controlledFid (Pythonic accessor)."""
        return self._controlledFid

    @controlled_fid.setter
    def controlled_fid(self, value: Optional[FunctionInhibitionNeeds]) -> None:
        """
        Set controlledFid with validation.

        Args:
            value: The controlledFid to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._controlledFid = None
            return

        if not isinstance(value, FunctionInhibitionNeeds):
            raise TypeError(
                f"controlledFid must be FunctionInhibitionNeeds or None, got {type(value).__name__}"
            )
        self._controlledFid = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getControlledFid(self) -> FunctionInhibitionNeeds:
        """
        AUTOSAR-compliant getter for controlledFid.

        Returns:
            The controlledFid value

        Note:
            Delegates to controlled_fid property (CODING_RULE_V2_00017)
        """
        return self.controlled_fid  # Delegates to property

    def setControlledFid(self, value: FunctionInhibitionNeeds) -> FunctionInhibitionAvailabilityNeeds:
        """
        AUTOSAR-compliant setter for controlledFid with method chaining.

        Args:
            value: The controlledFid to set

        Returns:
            self for method chaining

        Note:
            Delegates to controlled_fid property setter (gets validation automatically)
        """
        self.controlled_fid = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_controlled_fid(self, value: Optional[FunctionInhibitionNeeds]) -> FunctionInhibitionAvailabilityNeeds:
        """
        Set controlledFid and return self for chaining.

        Args:
            value: The controlledFid to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_controlled_fid("value")
        """
        self.controlled_fid = value  # Use property setter (gets validation)
        return self



class GlobalSupervisionNeeds(ServiceNeeds):
    """
    Specifies the abstract needs on the configuration of the Watchdog Manager to
    get access on the Global Supervision control and status interface.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::GlobalSupervisionNeeds

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 318, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 709, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class VendorSpecificServiceNeeds(ServiceNeeds):
    """
    This represents the ability to define vendor-specific service needs.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::VendorSpecificServiceNeeds

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 603, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class BswMgrNeeds(ServiceNeeds):
    """
    Specifies the abstract needs on the configuration of the Basic Software
    Manager for one "user".

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::BswMgrNeeds

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 716, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class CryptoServiceJobNeeds(ServiceNeeds):
    """
    This meta-class shall be taken to indicate that the service use case modeled
    with this kind of Service Needs assumes the usage of the crypto job API.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::CryptoServiceJobNeeds

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 733, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class CryptoKeyManagementNeeds(ServiceNeeds):
    """
    This meta-class can be used to indicate a service use case for key
    management.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::CryptoKeyManagementNeeds

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 745, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class IndicatorStatusNeeds(ServiceNeeds):
    """
    This meta-class shall be taken to signal a service use case that affects the
    indicator status.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::IndicatorStatusNeeds

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 766, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines the type of the indicator.
        self._typeEnum: Optional[DiagnosticIndicatorTypeEnum] = None

    @property
    def type_enum(self) -> Optional[DiagnosticIndicatorTypeEnum]:
        """Get typeEnum (Pythonic accessor)."""
        return self._typeEnum

    @type_enum.setter
    def type_enum(self, value: Optional[DiagnosticIndicatorTypeEnum]) -> None:
        """
        Set typeEnum with validation.

        Args:
            value: The typeEnum to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._typeEnum = None
            return

        if not isinstance(value, DiagnosticIndicatorTypeEnum):
            raise TypeError(
                f"typeEnum must be DiagnosticIndicatorTypeEnum or None, got {type(value).__name__}"
            )
        self._typeEnum = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTypeEnum(self) -> DiagnosticIndicatorTypeEnum:
        """
        AUTOSAR-compliant getter for typeEnum.

        Returns:
            The typeEnum value

        Note:
            Delegates to type_enum property (CODING_RULE_V2_00017)
        """
        return self.type_enum  # Delegates to property

    def setTypeEnum(self, value: DiagnosticIndicatorTypeEnum) -> IndicatorStatusNeeds:
        """
        AUTOSAR-compliant setter for typeEnum with method chaining.

        Args:
            value: The typeEnum to set

        Returns:
            self for method chaining

        Note:
            Delegates to type_enum property setter (gets validation automatically)
        """
        self.type_enum = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_type_enum(self, value: Optional[DiagnosticIndicatorTypeEnum]) -> IndicatorStatusNeeds:
        """
        Set typeEnum and return self for chaining.

        Args:
            value: The typeEnum to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_type_enum("value")
        """
        self.type_enum = value  # Use property setter (gets validation)
        return self



class SecureOnBoardCommunicationNeeds(ServiceNeeds):
    """
    Specifies the need for the existence of the SecOc module on the respective
    ECU. This class currently contains no attributes. An instance of this class
    is used to find out which ports of a software-component deal with the
    administration of secure communication in order to group the request and
    response ports.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::SecureOnBoardCommunicationNeeds

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 824, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute provides the ability to control the mode in which the
        # application software is notified about the result authentication attempts.
        self._verification: Optional[VerificationStatusIndicationModeEnum] = None

    @property
    def verification(self) -> Optional[VerificationStatusIndicationModeEnum]:
        """Get verification (Pythonic accessor)."""
        return self._verification

    @verification.setter
    def verification(self, value: Optional[VerificationStatusIndicationModeEnum]) -> None:
        """
        Set verification with validation.

        Args:
            value: The verification to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._verification = None
            return

        if not isinstance(value, VerificationStatusIndicationModeEnum):
            raise TypeError(
                f"verification must be VerificationStatusIndicationModeEnum or None, got {type(value).__name__}"
            )
        self._verification = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getVerification(self) -> VerificationStatusIndicationModeEnum:
        """
        AUTOSAR-compliant getter for verification.

        Returns:
            The verification value

        Note:
            Delegates to verification property (CODING_RULE_V2_00017)
        """
        return self.verification  # Delegates to property

    def setVerification(self, value: VerificationStatusIndicationModeEnum) -> SecureOnBoardCommunicationNeeds:
        """
        AUTOSAR-compliant setter for verification with method chaining.

        Args:
            value: The verification to set

        Returns:
            self for method chaining

        Note:
            Delegates to verification property setter (gets validation automatically)
        """
        self.verification = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_verification(self, value: Optional[VerificationStatusIndicationModeEnum]) -> SecureOnBoardCommunicationNeeds:
        """
        Set verification and return self for chaining.

        Args:
            value: The verification to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_verification("value")
        """
        self.verification = value  # Use property setter (gets validation)
        return self



class J1939RmOutgoingRequestServiceNeeds(ServiceNeeds):
    """
    This meta-class shall be used to specify needs with respect to the
    configuration of the J1939Rm, in particular for the case where an
    ApplicationSwComponentType needs to send a request to another J1939 node.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::J1939RmOutgoingRequestServiceNeeds

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 829, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class J1939RmIncomingRequestServiceNeeds(ServiceNeeds):
    """
    "This meta-class shall be used to specify needs with respect to the
    configuration of the J1939Rm, in particular for the case where an
    ApplicationSwComponentType needs to accept a request from another J1939
    node.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::J1939RmIncomingRequestServiceNeeds

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 829, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class J1939DcmDm19Support(ServiceNeeds):
    """
    The software-component provides information about calibration verification
    numbers for inclusion in DM19

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::J1939DcmDm19Support

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 831, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class V2xFacUserNeeds(ServiceNeeds):
    """
    This meta-class represents the ability to define service needs for V2x
    facilities.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::V2xFacUserNeeds

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 834, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class V2xMUserNeeds(ServiceNeeds):
    """
    This meta-class represents the ability to express service needs for the V2x
    management.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::V2xMUserNeeds

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 835, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class V2xDataManagerNeeds(ServiceNeeds):
    """
    This meta-class represents the ability to define service needs for V2x Data
    Manager.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::V2xDataManagerNeeds

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 840, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class IdsMgrNeeds(ServiceNeeds):
    """
    This meta-class is used to indicate that the enclosing SwcServiceDependency
    represents a service use case for the Intrusion Detection System Manager.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::IdsMgrNeeds

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 842, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute controls whether the reporting of the event shall be done by
        # means of the smart.
        self._useSmart: Optional[Boolean] = None

    @property
    def use_smart(self) -> Optional[Boolean]:
        """Get useSmart (Pythonic accessor)."""
        return self._useSmart

    @use_smart.setter
    def use_smart(self, value: Optional[Boolean]) -> None:
        """
        Set useSmart with validation.

        Args:
            value: The useSmart to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._useSmart = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"useSmart must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._useSmart = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getUseSmart(self) -> Boolean:
        """
        AUTOSAR-compliant getter for useSmart.

        Returns:
            The useSmart value

        Note:
            Delegates to use_smart property (CODING_RULE_V2_00017)
        """
        return self.use_smart  # Delegates to property

    def setUseSmart(self, value: Boolean) -> IdsMgrNeeds:
        """
        AUTOSAR-compliant setter for useSmart with method chaining.

        Args:
            value: The useSmart to set

        Returns:
            self for method chaining

        Note:
            Delegates to use_smart property setter (gets validation automatically)
        """
        self.use_smart = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_use_smart(self, value: Optional[Boolean]) -> IdsMgrNeeds:
        """
        Set useSmart and return self for chaining.

        Args:
            value: The useSmart to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_use_smart("value")
        """
        self.use_smart = value  # Use property setter (gets validation)
        return self



class IdsMgrCustomTimestampNeeds(ServiceNeeds):
    """
    This meta-class is used to indicate that the enclosing SwcServiceDependency
    represents a service use case for the retrieval of a custom timestamp by the
    Intrusion Detection System Manager.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::IdsMgrCustomTimestampNeeds

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 842, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class DiagEventDebounceCounterBased(DiagEventDebounceAlgorithm):
    """
    This meta-class represents the ability to indicate that the counter-based
    debounce algorithm shall be used by the DEM for this diagnostic monitor.
    This is related to set the ECUC choice container DemDebounceAlgorithmClass
    to DemDebounce CounterBased.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::DiagEventDebounceCounterBased

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 259, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 196, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 757, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Threshold to allocate an event memory entry and to the Freeze Frame.
        self._counterBased: Optional[Integer] = None

    @property
    def counter_based(self) -> Optional[Integer]:
        """Get counterBased (Pythonic accessor)."""
        return self._counterBased

    @counter_based.setter
    def counter_based(self, value: Optional[Integer]) -> None:
        """
        Set counterBased with validation.

        Args:
            value: The counterBased to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._counterBased = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"counterBased must be Integer or int or None, got {type(value).__name__}"
            )
        self._counterBased = value
        # atpVariation.
        self._counter: Optional[Integer] = None

    @property
    def counter(self) -> Optional[Integer]:
        """Get counter (Pythonic accessor)."""
        return self._counter

    @counter.setter
    def counter(self, value: Optional[Integer]) -> None:
        """
        Set counter with validation.

        Args:
            value: The counter to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._counter = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"counter must be Integer or int or None, got {type(value).__name__}"
            )
        self._counter = value
        # status.
        self._counterFailed: Optional[Integer] = None

    @property
    def counter_failed(self) -> Optional[Integer]:
        """Get counterFailed (Pythonic accessor)."""
        return self._counterFailed

    @counter_failed.setter
    def counter_failed(self, value: Optional[Integer]) -> None:
        """
        Set counterFailed with validation.

        Args:
            value: The counterFailed to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._counterFailed = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"counterFailed must be Integer or int or None, got {type(value).__name__}"
            )
        self._counterFailed = value
                # counting direction changes from decrementing.
        # 381 Document ID 89: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate Module
                # Description Template R23-11.
        self._counterJump: Optional[Integer] = None

    @property
    def counter_jump(self) -> Optional[Integer]:
        """Get counterJump (Pythonic accessor)."""
        return self._counterJump

    @counter_jump.setter
    def counter_jump(self, value: Optional[Integer]) -> None:
        """
        Set counterJump with validation.

        Args:
            value: The counterJump to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._counterJump = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"counterJump must be Integer or int or None, got {type(value).__name__}"
            )
        self._counterJump = value
        # counting direction changes from incrementing.
        self._counterJumpUp: Optional[Integer] = None

    @property
    def counter_jump_up(self) -> Optional[Integer]:
        """Get counterJumpUp (Pythonic accessor)."""
        return self._counterJumpUp

    @counter_jump_up.setter
    def counter_jump_up(self, value: Optional[Integer]) -> None:
        """
        Set counterJumpUp with validation.

        Args:
            value: The counterJumpUp to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._counterJumpUp = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"counterJumpUp must be Integer or int or None, got {type(value).__name__}"
            )
        self._counterJumpUp = value
        # status.
        self._counterPassed: Optional[Integer] = None

    @property
    def counter_passed(self) -> Optional[Integer]:
        """Get counterPassed (Pythonic accessor)."""
        return self._counterPassed

    @counter_passed.setter
    def counter_passed(self, value: Optional[Integer]) -> None:
        """
        Set counterPassed with validation.

        Args:
            value: The counterPassed to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._counterPassed = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"counterPassed must be Integer or int or None, got {type(value).__name__}"
            )
        self._counterPassed = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCounterBased(self) -> Integer:
        """
        AUTOSAR-compliant getter for counterBased.

        Returns:
            The counterBased value

        Note:
            Delegates to counter_based property (CODING_RULE_V2_00017)
        """
        return self.counter_based  # Delegates to property

    def setCounterBased(self, value: Integer) -> DiagEventDebounceCounterBased:
        """
        AUTOSAR-compliant setter for counterBased with method chaining.

        Args:
            value: The counterBased to set

        Returns:
            self for method chaining

        Note:
            Delegates to counter_based property setter (gets validation automatically)
        """
        self.counter_based = value  # Delegates to property setter
        return self

    def getCounter(self) -> Integer:
        """
        AUTOSAR-compliant getter for counter.

        Returns:
            The counter value

        Note:
            Delegates to counter property (CODING_RULE_V2_00017)
        """
        return self.counter  # Delegates to property

    def setCounter(self, value: Integer) -> DiagEventDebounceCounterBased:
        """
        AUTOSAR-compliant setter for counter with method chaining.

        Args:
            value: The counter to set

        Returns:
            self for method chaining

        Note:
            Delegates to counter property setter (gets validation automatically)
        """
        self.counter = value  # Delegates to property setter
        return self

    def getCounterFailed(self) -> Integer:
        """
        AUTOSAR-compliant getter for counterFailed.

        Returns:
            The counterFailed value

        Note:
            Delegates to counter_failed property (CODING_RULE_V2_00017)
        """
        return self.counter_failed  # Delegates to property

    def setCounterFailed(self, value: Integer) -> DiagEventDebounceCounterBased:
        """
        AUTOSAR-compliant setter for counterFailed with method chaining.

        Args:
            value: The counterFailed to set

        Returns:
            self for method chaining

        Note:
            Delegates to counter_failed property setter (gets validation automatically)
        """
        self.counter_failed = value  # Delegates to property setter
        return self

    def getCounterJump(self) -> Integer:
        """
        AUTOSAR-compliant getter for counterJump.

        Returns:
            The counterJump value

        Note:
            Delegates to counter_jump property (CODING_RULE_V2_00017)
        """
        return self.counter_jump  # Delegates to property

    def setCounterJump(self, value: Integer) -> DiagEventDebounceCounterBased:
        """
        AUTOSAR-compliant setter for counterJump with method chaining.

        Args:
            value: The counterJump to set

        Returns:
            self for method chaining

        Note:
            Delegates to counter_jump property setter (gets validation automatically)
        """
        self.counter_jump = value  # Delegates to property setter
        return self

    def getCounterJumpUp(self) -> Integer:
        """
        AUTOSAR-compliant getter for counterJumpUp.

        Returns:
            The counterJumpUp value

        Note:
            Delegates to counter_jump_up property (CODING_RULE_V2_00017)
        """
        return self.counter_jump_up  # Delegates to property

    def setCounterJumpUp(self, value: Integer) -> DiagEventDebounceCounterBased:
        """
        AUTOSAR-compliant setter for counterJumpUp with method chaining.

        Args:
            value: The counterJumpUp to set

        Returns:
            self for method chaining

        Note:
            Delegates to counter_jump_up property setter (gets validation automatically)
        """
        self.counter_jump_up = value  # Delegates to property setter
        return self

    def getCounterPassed(self) -> Integer:
        """
        AUTOSAR-compliant getter for counterPassed.

        Returns:
            The counterPassed value

        Note:
            Delegates to counter_passed property (CODING_RULE_V2_00017)
        """
        return self.counter_passed  # Delegates to property

    def setCounterPassed(self, value: Integer) -> DiagEventDebounceCounterBased:
        """
        AUTOSAR-compliant setter for counterPassed with method chaining.

        Args:
            value: The counterPassed to set

        Returns:
            self for method chaining

        Note:
            Delegates to counter_passed property setter (gets validation automatically)
        """
        self.counter_passed = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_counter_based(self, value: Optional[Integer]) -> DiagEventDebounceCounterBased:
        """
        Set counterBased and return self for chaining.

        Args:
            value: The counterBased to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_counter_based("value")
        """
        self.counter_based = value  # Use property setter (gets validation)
        return self

    def with_counter(self, value: Optional[Integer]) -> DiagEventDebounceCounterBased:
        """
        Set counter and return self for chaining.

        Args:
            value: The counter to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_counter("value")
        """
        self.counter = value  # Use property setter (gets validation)
        return self

    def with_counter_failed(self, value: Optional[Integer]) -> DiagEventDebounceCounterBased:
        """
        Set counterFailed and return self for chaining.

        Args:
            value: The counterFailed to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_counter_failed("value")
        """
        self.counter_failed = value  # Use property setter (gets validation)
        return self

    def with_counter_jump(self, value: Optional[Integer]) -> DiagEventDebounceCounterBased:
        """
        Set counterJump and return self for chaining.

        Args:
            value: The counterJump to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_counter_jump("value")
        """
        self.counter_jump = value  # Use property setter (gets validation)
        return self

    def with_counter_jump_up(self, value: Optional[Integer]) -> DiagEventDebounceCounterBased:
        """
        Set counterJumpUp and return self for chaining.

        Args:
            value: The counterJumpUp to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_counter_jump_up("value")
        """
        self.counter_jump_up = value  # Use property setter (gets validation)
        return self

    def with_counter_passed(self, value: Optional[Integer]) -> DiagEventDebounceCounterBased:
        """
        Set counterPassed and return self for chaining.

        Args:
            value: The counterPassed to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_counter_passed("value")
        """
        self.counter_passed = value  # Use property setter (gets validation)
        return self



class DiagEventDebounceTimeBased(DiagEventDebounceAlgorithm):
    """
    This meta-class represents the ability to indicate that the time-based
    pre-debounce algorithm shall be used by the Dem for this diagnostic monitor.
    This is related to set the EcuC choice container DemDebounceAlgorithmClass
    to DemDebounceTime Base.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::DiagEventDebounceTimeBased

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 260, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 198, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 758, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Threshold to allocate an event memory entry and to the Freeze Frame.
        # atpVariation.
        self._timeBasedFdc: Optional[TimeValue] = None

    @property
    def time_based_fdc(self) -> Optional[TimeValue]:
        """Get timeBasedFdc (Pythonic accessor)."""
        return self._timeBasedFdc

    @time_based_fdc.setter
    def time_based_fdc(self, value: Optional[TimeValue]) -> None:
        """
        Set timeBasedFdc with validation.

        Args:
            value: The timeBasedFdc to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeBasedFdc = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"timeBasedFdc must be TimeValue or None, got {type(value).__name__}"
            )
        self._timeBasedFdc = value
        self._timeFailed: Optional[TimeValue] = None

    @property
    def time_failed(self) -> Optional[TimeValue]:
        """Get timeFailed (Pythonic accessor)."""
        return self._timeFailed

    @time_failed.setter
    def time_failed(self, value: Optional[TimeValue]) -> None:
        """
        Set timeFailed with validation.

        Args:
            value: The timeFailed to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeFailed = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"timeFailed must be TimeValue or None, got {type(value).__name__}"
            )
        self._timeFailed = value
        self._timePassed: Optional[TimeValue] = None

    @property
    def time_passed(self) -> Optional[TimeValue]:
        """Get timePassed (Pythonic accessor)."""
        return self._timePassed

    @time_passed.setter
    def time_passed(self, value: Optional[TimeValue]) -> None:
        """
        Set timePassed with validation.

        Args:
            value: The timePassed to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timePassed = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"timePassed must be TimeValue or None, got {type(value).__name__}"
            )
        self._timePassed = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTimeBasedFdc(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for timeBasedFdc.

        Returns:
            The timeBasedFdc value

        Note:
            Delegates to time_based_fdc property (CODING_RULE_V2_00017)
        """
        return self.time_based_fdc  # Delegates to property

    def setTimeBasedFdc(self, value: TimeValue) -> DiagEventDebounceTimeBased:
        """
        AUTOSAR-compliant setter for timeBasedFdc with method chaining.

        Args:
            value: The timeBasedFdc to set

        Returns:
            self for method chaining

        Note:
            Delegates to time_based_fdc property setter (gets validation automatically)
        """
        self.time_based_fdc = value  # Delegates to property setter
        return self

    def getTimeFailed(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for timeFailed.

        Returns:
            The timeFailed value

        Note:
            Delegates to time_failed property (CODING_RULE_V2_00017)
        """
        return self.time_failed  # Delegates to property

    def setTimeFailed(self, value: TimeValue) -> DiagEventDebounceTimeBased:
        """
        AUTOSAR-compliant setter for timeFailed with method chaining.

        Args:
            value: The timeFailed to set

        Returns:
            self for method chaining

        Note:
            Delegates to time_failed property setter (gets validation automatically)
        """
        self.time_failed = value  # Delegates to property setter
        return self

    def getTimePassed(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for timePassed.

        Returns:
            The timePassed value

        Note:
            Delegates to time_passed property (CODING_RULE_V2_00017)
        """
        return self.time_passed  # Delegates to property

    def setTimePassed(self, value: TimeValue) -> DiagEventDebounceTimeBased:
        """
        AUTOSAR-compliant setter for timePassed with method chaining.

        Args:
            value: The timePassed to set

        Returns:
            self for method chaining

        Note:
            Delegates to time_passed property setter (gets validation automatically)
        """
        self.time_passed = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_time_based_fdc(self, value: Optional[TimeValue]) -> DiagEventDebounceTimeBased:
        """
        Set timeBasedFdc and return self for chaining.

        Args:
            value: The timeBasedFdc to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_time_based_fdc("value")
        """
        self.time_based_fdc = value  # Use property setter (gets validation)
        return self

    def with_time_failed(self, value: Optional[TimeValue]) -> DiagEventDebounceTimeBased:
        """
        Set timeFailed and return self for chaining.

        Args:
            value: The timeFailed to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_time_failed("value")
        """
        self.time_failed = value  # Use property setter (gets validation)
        return self

    def with_time_passed(self, value: Optional[TimeValue]) -> DiagEventDebounceTimeBased:
        """
        Set timePassed and return self for chaining.

        Args:
            value: The timePassed to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_time_passed("value")
        """
        self.time_passed = value  # Use property setter (gets validation)
        return self



class DiagEventDebounceMonitorInternal(DiagEventDebounceAlgorithm):
    """
    This meta-class represents the ability to indicate that no Dem pre-debounce
    algorithm shall be used for this diagnostic monitor. The SWC might implement
    an internal debouncing algorithm and report qualified (debounced) results to
    the Dem/DM.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::DiagEventDebounceMonitorInternal

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 260, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 199, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 758, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class DevelopmentError(TracedFailure):
    """
    The reported failure is classified as development error.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::DevelopmentError

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 263, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 832, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class RuntimeError(TracedFailure):
    """
    The reported failure is classified as runtime error.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::RuntimeError

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 263, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 832, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class TransientFault(TracedFailure):
    """
    The reported failure is classified as runtime error.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::TransientFault

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 1009, Classic
      Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Describes a possible error reactions for the transient fault.
        self._possibleError: List["PossibleErrorReaction"] = []

    @property
    def possible_error(self) -> List["PossibleErrorReaction"]:
        """Get possibleError (Pythonic accessor)."""
        return self._possibleError

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getPossibleError(self) -> List["PossibleErrorReaction"]:
        """
        AUTOSAR-compliant getter for possibleError.

        Returns:
            The possibleError value

        Note:
            Delegates to possible_error property (CODING_RULE_V2_00017)
        """
        return self.possible_error  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class DiagnosticValueNeeds(DiagnosticCapabilityElement):
    """
    Specifies the general needs on the configuration of the Diagnostic
    Communication Manager (DCM) which are not related to a particular item (e.g.
    a PID). The main use case is the mapping of service ports to the DCM which
    are not related to a particular item. In the case of using a sender receiver
    communicated value, the related value shall be taken via assigned Data in
    the role "signalBasedDiagnostics". In case of using a client/server
    communicated value, the related value shall be communicated via the port
    referenced by assignedPort. The details of this communication (e.g.
    appropriate naming conventions) are specified in the related software
    specifications (SWS). (cid:53) 245 of 381 Document ID 89:
    AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate Basic Software Module
    Description Template AUTOSAR CP R23-11 (cid:52)

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::DiagnosticValueNeeds

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 245, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 114, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 782, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute is applicable only if the DiagnosticValue aggregated within a
                # BswModuleDependency.
        # represents the length of data (in bytes) this particular PID signal.
        self._dataLength: Optional[PositiveInteger] = None

    @property
    def data_length(self) -> Optional[PositiveInteger]:
        """Get dataLength (Pythonic accessor)."""
        return self._dataLength

    @data_length.setter
    def data_length(self, value: Optional[PositiveInteger]) -> None:
        """
        Set dataLength with validation.

        Args:
            value: The dataLength to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dataLength = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"dataLength must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._dataLength = value
                # within a BswModuleDependency.
        # controls whether the data can be read and whether it is to be handled
                # read-only.
        self._diagnosticValue: Optional[DiagnosticValueAccessEnum] = None

    @property
    def diagnostic_value(self) -> Optional[DiagnosticValueAccessEnum]:
        """Get diagnosticValue (Pythonic accessor)."""
        return self._diagnosticValue

    @diagnostic_value.setter
    def diagnostic_value(self, value: Optional[DiagnosticValueAccessEnum]) -> None:
        """
        Set diagnosticValue with validation.

        Args:
            value: The diagnosticValue to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._diagnosticValue = None
            return

        if not isinstance(value, DiagnosticValueAccessEnum):
            raise TypeError(
                f"diagnosticValue must be DiagnosticValueAccessEnum or None, got {type(value).__name__}"
            )
        self._diagnosticValue = value
                # BswModuleDependency.
        # controls whether the data length of the data.
        self._fixedLength: Optional[Boolean] = None

    @property
    def fixed_length(self) -> Optional[Boolean]:
        """Get fixedLength (Pythonic accessor)."""
        return self._fixedLength

    @fixed_length.setter
    def fixed_length(self, value: Optional[Boolean]) -> None:
        """
        Set fixedLength with validation.

        Args:
            value: The fixedLength to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._fixedLength = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"fixedLength must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._fixedLength = value
        # synchronously on a request it processes the request in background but still
        # has to issue the call again to eventually obtain of the request.
        self._processingStyle: Optional[DiagnosticProcessing] = None

    @property
    def processing_style(self) -> Optional[DiagnosticProcessing]:
        """Get processingStyle (Pythonic accessor)."""
        return self._processingStyle

    @processing_style.setter
    def processing_style(self, value: Optional[DiagnosticProcessing]) -> None:
        """
        Set processingStyle with validation.

        Args:
            value: The processingStyle to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._processingStyle = None
            return

        if not isinstance(value, DiagnosticProcessing):
            raise TypeError(
                f"processingStyle must be DiagnosticProcessing or None, got {type(value).__name__}"
            )
        self._processingStyle = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDataLength(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for dataLength.

        Returns:
            The dataLength value

        Note:
            Delegates to data_length property (CODING_RULE_V2_00017)
        """
        return self.data_length  # Delegates to property

    def setDataLength(self, value: PositiveInteger) -> DiagnosticValueNeeds:
        """
        AUTOSAR-compliant setter for dataLength with method chaining.

        Args:
            value: The dataLength to set

        Returns:
            self for method chaining

        Note:
            Delegates to data_length property setter (gets validation automatically)
        """
        self.data_length = value  # Delegates to property setter
        return self

    def getDiagnosticValue(self) -> DiagnosticValueAccessEnum:
        """
        AUTOSAR-compliant getter for diagnosticValue.

        Returns:
            The diagnosticValue value

        Note:
            Delegates to diagnostic_value property (CODING_RULE_V2_00017)
        """
        return self.diagnostic_value  # Delegates to property

    def setDiagnosticValue(self, value: DiagnosticValueAccessEnum) -> DiagnosticValueNeeds:
        """
        AUTOSAR-compliant setter for diagnosticValue with method chaining.

        Args:
            value: The diagnosticValue to set

        Returns:
            self for method chaining

        Note:
            Delegates to diagnostic_value property setter (gets validation automatically)
        """
        self.diagnostic_value = value  # Delegates to property setter
        return self

    def getFixedLength(self) -> Boolean:
        """
        AUTOSAR-compliant getter for fixedLength.

        Returns:
            The fixedLength value

        Note:
            Delegates to fixed_length property (CODING_RULE_V2_00017)
        """
        return self.fixed_length  # Delegates to property

    def setFixedLength(self, value: Boolean) -> DiagnosticValueNeeds:
        """
        AUTOSAR-compliant setter for fixedLength with method chaining.

        Args:
            value: The fixedLength to set

        Returns:
            self for method chaining

        Note:
            Delegates to fixed_length property setter (gets validation automatically)
        """
        self.fixed_length = value  # Delegates to property setter
        return self

    def getProcessingStyle(self) -> "DiagnosticProcessing":
        """
        AUTOSAR-compliant getter for processingStyle.

        Returns:
            The processingStyle value

        Note:
            Delegates to processing_style property (CODING_RULE_V2_00017)
        """
        return self.processing_style  # Delegates to property

    def setProcessingStyle(self, value: DiagnosticProcessing) -> DiagnosticValueNeeds:
        """
        AUTOSAR-compliant setter for processingStyle with method chaining.

        Args:
            value: The processingStyle to set

        Returns:
            self for method chaining

        Note:
            Delegates to processing_style property setter (gets validation automatically)
        """
        self.processing_style = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_data_length(self, value: Optional[PositiveInteger]) -> DiagnosticValueNeeds:
        """
        Set dataLength and return self for chaining.

        Args:
            value: The dataLength to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_data_length("value")
        """
        self.data_length = value  # Use property setter (gets validation)
        return self

    def with_diagnostic_value(self, value: Optional[DiagnosticValueAccessEnum]) -> DiagnosticValueNeeds:
        """
        Set diagnosticValue and return self for chaining.

        Args:
            value: The diagnosticValue to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_diagnostic_value("value")
        """
        self.diagnostic_value = value  # Use property setter (gets validation)
        return self

    def with_fixed_length(self, value: Optional[Boolean]) -> DiagnosticValueNeeds:
        """
        Set fixedLength and return self for chaining.

        Args:
            value: The fixedLength to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_fixed_length("value")
        """
        self.fixed_length = value  # Use property setter (gets validation)
        return self

    def with_processing_style(self, value: Optional[DiagnosticProcessing]) -> DiagnosticValueNeeds:
        """
        Set processingStyle and return self for chaining.

        Args:
            value: The processingStyle to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_processing_style("value")
        """
        self.processing_style = value  # Use property setter (gets validation)
        return self



class DiagnosticRoutineNeeds(DiagnosticCapabilityElement):
    """
    Specifies the general needs on the configuration of the Diagnostic
    Communication Manager (Dcm) which are not related to a particular item (e.g.
    a PID). The main use case is the mapping of service ports to the Dcm which
    are not related to a particular item.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::DiagnosticRoutineNeeds

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 247, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 126, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 780, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This denotes the type of diagnostic routine which is implemented by the
        # referenced server port.
        self._diagRoutine: Optional[DiagnosticRoutineTypeEnum] = None

    @property
    def diag_routine(self) -> Optional[DiagnosticRoutineTypeEnum]:
        """Get diagRoutine (Pythonic accessor)."""
        return self._diagRoutine

    @diag_routine.setter
    def diag_routine(self, value: Optional[DiagnosticRoutineTypeEnum]) -> None:
        """
        Set diagRoutine with validation.

        Args:
            value: The diagRoutine to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._diagRoutine = None
            return

        if not isinstance(value, DiagnosticRoutineTypeEnum):
            raise TypeError(
                f"diagRoutine must be DiagnosticRoutineTypeEnum or None, got {type(value).__name__}"
            )
        self._diagRoutine = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDiagRoutine(self) -> DiagnosticRoutineTypeEnum:
        """
        AUTOSAR-compliant getter for diagRoutine.

        Returns:
            The diagRoutine value

        Note:
            Delegates to diag_routine property (CODING_RULE_V2_00017)
        """
        return self.diag_routine  # Delegates to property

    def setDiagRoutine(self, value: DiagnosticRoutineTypeEnum) -> DiagnosticRoutineNeeds:
        """
        AUTOSAR-compliant setter for diagRoutine with method chaining.

        Args:
            value: The diagRoutine to set

        Returns:
            self for method chaining

        Note:
            Delegates to diag_routine property setter (gets validation automatically)
        """
        self.diag_routine = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_diag_routine(self, value: Optional[DiagnosticRoutineTypeEnum]) -> DiagnosticRoutineNeeds:
        """
        Set diagRoutine and return self for chaining.

        Args:
            value: The diagRoutine to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_diag_routine("value")
        """
        self.diag_routine = value  # Use property setter (gets validation)
        return self



class DiagnosticIoControlNeeds(DiagnosticCapabilityElement):
    """
    Specifies the general needs on the configuration of the Diagnostic
    Communication Manager (DCM) which are not related to a particular item (e.g.
    a PID). The main use case is the mapping of service ports to the Dcm which
    are not related to a particular item.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::DiagnosticIoControlNeeds

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 248, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 119, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 781, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to the DiagnosticValueNeeds indicating the the current value via
        # signalBasedDiagnostics.
        self._currentValue: Optional[DiagnosticValueNeeds] = None

    @property
    def current_value(self) -> Optional[DiagnosticValueNeeds]:
        """Get currentValue (Pythonic accessor)."""
        return self._currentValue

    @current_value.setter
    def current_value(self, value: Optional[DiagnosticValueNeeds]) -> None:
        """
        Set currentValue with validation.

        Args:
            value: The currentValue to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._currentValue = None
            return

        if not isinstance(value, DiagnosticValueNeeds):
            raise TypeError(
                f"currentValue must be DiagnosticValueNeeds or None, got {type(value).__name__}"
            )
        self._currentValue = value
                # value.
        # freeze is not supported if the enclosing aggregated by a Swc [constr_1364].
        self._freezeCurrent: Optional[Boolean] = None

    @property
    def freeze_current(self) -> Optional[Boolean]:
        """Get freezeCurrent (Pythonic accessor)."""
        return self._freezeCurrent

    @freeze_current.setter
    def freeze_current(self, value: Optional[Boolean]) -> None:
        """
        Set freezeCurrent with validation.

        Args:
            value: The freezeCurrent to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._freezeCurrent = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"freezeCurrent must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._freezeCurrent = value
        # service interface.
        self._resetToDefault: Optional[Boolean] = None

    @property
    def reset_to_default(self) -> Optional[Boolean]:
        """Get resetToDefault (Pythonic accessor)."""
        return self._resetToDefault

    @reset_to_default.setter
    def reset_to_default(self, value: Optional[Boolean]) -> None:
        """
        Set resetToDefault with validation.

        Args:
            value: The resetToDefault to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._resetToDefault = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"resetToDefault must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._resetToDefault = value
                # value to a specific value by the diagnostic tester.
        # term adjustment is not supported if the is aggregated by a [constr_1364].
        self._shortTerm: Optional[Boolean] = None

    @property
    def short_term(self) -> Optional[Boolean]:
        """Get shortTerm (Pythonic accessor)."""
        return self._shortTerm

    @short_term.setter
    def short_term(self, value: Optional[Boolean]) -> None:
        """
        Set shortTerm with validation.

        Args:
            value: The shortTerm to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._shortTerm = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"shortTerm must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._shortTerm = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCurrentValue(self) -> DiagnosticValueNeeds:
        """
        AUTOSAR-compliant getter for currentValue.

        Returns:
            The currentValue value

        Note:
            Delegates to current_value property (CODING_RULE_V2_00017)
        """
        return self.current_value  # Delegates to property

    def setCurrentValue(self, value: DiagnosticValueNeeds) -> DiagnosticIoControlNeeds:
        """
        AUTOSAR-compliant setter for currentValue with method chaining.

        Args:
            value: The currentValue to set

        Returns:
            self for method chaining

        Note:
            Delegates to current_value property setter (gets validation automatically)
        """
        self.current_value = value  # Delegates to property setter
        return self

    def getFreezeCurrent(self) -> Boolean:
        """
        AUTOSAR-compliant getter for freezeCurrent.

        Returns:
            The freezeCurrent value

        Note:
            Delegates to freeze_current property (CODING_RULE_V2_00017)
        """
        return self.freeze_current  # Delegates to property

    def setFreezeCurrent(self, value: Boolean) -> DiagnosticIoControlNeeds:
        """
        AUTOSAR-compliant setter for freezeCurrent with method chaining.

        Args:
            value: The freezeCurrent to set

        Returns:
            self for method chaining

        Note:
            Delegates to freeze_current property setter (gets validation automatically)
        """
        self.freeze_current = value  # Delegates to property setter
        return self

    def getResetToDefault(self) -> Boolean:
        """
        AUTOSAR-compliant getter for resetToDefault.

        Returns:
            The resetToDefault value

        Note:
            Delegates to reset_to_default property (CODING_RULE_V2_00017)
        """
        return self.reset_to_default  # Delegates to property

    def setResetToDefault(self, value: Boolean) -> DiagnosticIoControlNeeds:
        """
        AUTOSAR-compliant setter for resetToDefault with method chaining.

        Args:
            value: The resetToDefault to set

        Returns:
            self for method chaining

        Note:
            Delegates to reset_to_default property setter (gets validation automatically)
        """
        self.reset_to_default = value  # Delegates to property setter
        return self

    def getShortTerm(self) -> Boolean:
        """
        AUTOSAR-compliant getter for shortTerm.

        Returns:
            The shortTerm value

        Note:
            Delegates to short_term property (CODING_RULE_V2_00017)
        """
        return self.short_term  # Delegates to property

    def setShortTerm(self, value: Boolean) -> DiagnosticIoControlNeeds:
        """
        AUTOSAR-compliant setter for shortTerm with method chaining.

        Args:
            value: The shortTerm to set

        Returns:
            self for method chaining

        Note:
            Delegates to short_term property setter (gets validation automatically)
        """
        self.short_term = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_current_value(self, value: Optional[DiagnosticValueNeeds]) -> DiagnosticIoControlNeeds:
        """
        Set currentValue and return self for chaining.

        Args:
            value: The currentValue to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_current_value("value")
        """
        self.current_value = value  # Use property setter (gets validation)
        return self

    def with_freeze_current(self, value: Optional[Boolean]) -> DiagnosticIoControlNeeds:
        """
        Set freezeCurrent and return self for chaining.

        Args:
            value: The freezeCurrent to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_freeze_current("value")
        """
        self.freeze_current = value  # Use property setter (gets validation)
        return self

    def with_reset_to_default(self, value: Optional[Boolean]) -> DiagnosticIoControlNeeds:
        """
        Set resetToDefault and return self for chaining.

        Args:
            value: The resetToDefault to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_reset_to_default("value")
        """
        self.reset_to_default = value  # Use property setter (gets validation)
        return self

    def with_short_term(self, value: Optional[Boolean]) -> DiagnosticIoControlNeeds:
        """
        Set shortTerm and return self for chaining.

        Args:
            value: The shortTerm to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_short_term("value")
        """
        self.short_term = value  # Use property setter (gets validation)
        return self



class DiagnosticsCommunicationSecurityNeeds(DiagnosticCapabilityElement):
    """
    This meta-class represents the needs of a software-component to verify the
    access to security level via diagnostic services.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::DiagnosticsCommunicationSecurityNeeds

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 248, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 783, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class DiagnosticCommunicationManagerNeeds(DiagnosticCapabilityElement):
    """
    Specifies the general needs on the configuration of the Diagnostic
    Communication Manager (Dcm) which are not related to a particular item (e.g.
    a PID or DiagnosticRoutineNeeds). The main use case is the mapping of
    service ports to the Dcm which are not related to a particular item.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::DiagnosticCommunicationManagerNeeds

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 248, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 779, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the ability to define whether the usage of PortInterface
        # ServiceRequestNotification has the of being initiated by a manufacturer or by
        # a.
        self._serviceRequest: Optional[DiagnosticService] = None

    @property
    def service_request(self) -> Optional[DiagnosticService]:
        """Get serviceRequest (Pythonic accessor)."""
        return self._serviceRequest

    @service_request.setter
    def service_request(self, value: Optional[DiagnosticService]) -> None:
        """
        Set serviceRequest with validation.

        Args:
            value: The serviceRequest to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._serviceRequest = None
            return

        if not isinstance(value, DiagnosticService):
            raise TypeError(
                f"serviceRequest must be DiagnosticService or None, got {type(value).__name__}"
            )
        self._serviceRequest = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getServiceRequest(self) -> DiagnosticService:
        """
        AUTOSAR-compliant getter for serviceRequest.

        Returns:
            The serviceRequest value

        Note:
            Delegates to service_request property (CODING_RULE_V2_00017)
        """
        return self.service_request  # Delegates to property

    def setServiceRequest(self, value: DiagnosticService) -> DiagnosticCommunicationManagerNeeds:
        """
        AUTOSAR-compliant setter for serviceRequest with method chaining.

        Args:
            value: The serviceRequest to set

        Returns:
            self for method chaining

        Note:
            Delegates to service_request property setter (gets validation automatically)
        """
        self.service_request = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_service_request(self, value: Optional[DiagnosticService]) -> DiagnosticCommunicationManagerNeeds:
        """
        Set serviceRequest and return self for chaining.

        Args:
            value: The serviceRequest to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_service_request("value")
        """
        self.service_request = value  # Use property setter (gets validation)
        return self



class DiagnosticUploadDownloadNeeds(DiagnosticCapabilityElement):
    """
    This meta-class represents the ability to specify needs regarding upload and
    download by means of diagnostic services.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::DiagnosticUploadDownloadNeeds

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 252, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 816, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class DiagnosticEventNeeds(DiagnosticCapabilityElement):
    """
    Specifies the abstract needs on the configuration of the Diagnostic Event
    Manager for one diagnostic event. Its shortName can be regarded as a symbol
    identifying the diagnostic event from the viewpoint of the component or
    module which owns this element. In case the diagnostic event specifies a
    production error, the shortName shall be the name of the production error.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::DiagnosticEventNeeds

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 258, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 311, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 756, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference contains the link to a function identifier FiM which is used
        # by the monitor before result.
        self._deferringFid: List[FunctionInhibitionNeeds] = []

    @property
    def deferring_fid(self) -> List[FunctionInhibitionNeeds]:
        """Get deferringFid (Pythonic accessor)."""
        return self._deferringFid
        # Specifies the abstract need on the Debounce Algorithm applied by the
        # Diagnostic Event Manager.
        self._diagEvent: Optional[DiagEventDebounce] = None

    @property
    def diag_event(self) -> Optional[DiagEventDebounce]:
        """Get diagEvent (Pythonic accessor)."""
        return self._diagEvent

    @diag_event.setter
    def diag_event(self, value: Optional[DiagEventDebounce]) -> None:
        """
        Set diagEvent with validation.

        Args:
            value: The diagEvent to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._diagEvent = None
            return

        if not isinstance(value, DiagEventDebounce):
            raise TypeError(
                f"diagEvent must be DiagEventDebounce or None, got {type(value).__name__}"
            )
        self._diagEvent = value
                # diagnostic monitor.
        # The FID inhibit the monitoring of a symptom or the detected faults.
        self._inhibitingFid: Optional[FunctionInhibitionNeeds] = None

    @property
    def inhibiting_fid(self) -> Optional[FunctionInhibitionNeeds]:
        """Get inhibitingFid (Pythonic accessor)."""
        return self._inhibitingFid

    @inhibiting_fid.setter
    def inhibiting_fid(self, value: Optional[FunctionInhibitionNeeds]) -> None:
        """
        Set inhibitingFid with validation.

        Args:
            value: The inhibitingFid to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._inhibitingFid = None
            return

        if not isinstance(value, FunctionInhibitionNeeds):
            raise TypeError(
                f"inhibitingFid must be FunctionInhibitionNeeds or None, got {type(value).__name__}"
            )
        self._inhibitingFid = value
                # diagnostic monitor.
        # Any FID inhibitions leads to an inhibition of the a symptom or the reporting
                # of detected.
        self._inhibiting: List[FunctionInhibitionNeeds] = []

    @property
    def inhibiting(self) -> List[FunctionInhibitionNeeds]:
        """Get inhibiting (Pythonic accessor)."""
        return self._inhibiting
        # If the Event uses a prestored freeze-frame (using the PrestoreFreezeFrame and
                # ClearPrestored of the service interface DiagnosticMonitor) indicates if the
                # Event requires the data to be non-volatile memory.
        # TRUE = Dem shall store data in non-volatile memory, FALSE = Data lost at
                # shutdown (not stored in Nvm).
        self._prestored: Optional[Boolean] = None

    @property
    def prestored(self) -> Optional[Boolean]:
        """Get prestored (Pythonic accessor)."""
        return self._prestored

    @prestored.setter
    def prestored(self, value: Optional[Boolean]) -> None:
        """
        Set prestored with validation.

        Args:
            value: The prestored to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._prestored = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"prestored must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._prestored = value
        # reporting of events.
        self._usesMonitor: Optional[Boolean] = None

    @property
    def uses_monitor(self) -> Optional[Boolean]:
        """Get usesMonitor (Pythonic accessor)."""
        return self._usesMonitor

    @uses_monitor.setter
    def uses_monitor(self, value: Optional[Boolean]) -> None:
        """
        Set usesMonitor with validation.

        Args:
            value: The usesMonitor to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._usesMonitor = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"usesMonitor must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._usesMonitor = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDeferringFid(self) -> List[FunctionInhibitionNeeds]:
        """
        AUTOSAR-compliant getter for deferringFid.

        Returns:
            The deferringFid value

        Note:
            Delegates to deferring_fid property (CODING_RULE_V2_00017)
        """
        return self.deferring_fid  # Delegates to property

    def getDiagEvent(self) -> "DiagEventDebounce":
        """
        AUTOSAR-compliant getter for diagEvent.

        Returns:
            The diagEvent value

        Note:
            Delegates to diag_event property (CODING_RULE_V2_00017)
        """
        return self.diag_event  # Delegates to property

    def setDiagEvent(self, value: DiagEventDebounce) -> DiagnosticEventNeeds:
        """
        AUTOSAR-compliant setter for diagEvent with method chaining.

        Args:
            value: The diagEvent to set

        Returns:
            self for method chaining

        Note:
            Delegates to diag_event property setter (gets validation automatically)
        """
        self.diag_event = value  # Delegates to property setter
        return self

    def getInhibitingFid(self) -> FunctionInhibitionNeeds:
        """
        AUTOSAR-compliant getter for inhibitingFid.

        Returns:
            The inhibitingFid value

        Note:
            Delegates to inhibiting_fid property (CODING_RULE_V2_00017)
        """
        return self.inhibiting_fid  # Delegates to property

    def setInhibitingFid(self, value: FunctionInhibitionNeeds) -> DiagnosticEventNeeds:
        """
        AUTOSAR-compliant setter for inhibitingFid with method chaining.

        Args:
            value: The inhibitingFid to set

        Returns:
            self for method chaining

        Note:
            Delegates to inhibiting_fid property setter (gets validation automatically)
        """
        self.inhibiting_fid = value  # Delegates to property setter
        return self

    def getInhibiting(self) -> List[FunctionInhibitionNeeds]:
        """
        AUTOSAR-compliant getter for inhibiting.

        Returns:
            The inhibiting value

        Note:
            Delegates to inhibiting property (CODING_RULE_V2_00017)
        """
        return self.inhibiting  # Delegates to property

    def getPrestored(self) -> Boolean:
        """
        AUTOSAR-compliant getter for prestored.

        Returns:
            The prestored value

        Note:
            Delegates to prestored property (CODING_RULE_V2_00017)
        """
        return self.prestored  # Delegates to property

    def setPrestored(self, value: Boolean) -> DiagnosticEventNeeds:
        """
        AUTOSAR-compliant setter for prestored with method chaining.

        Args:
            value: The prestored to set

        Returns:
            self for method chaining

        Note:
            Delegates to prestored property setter (gets validation automatically)
        """
        self.prestored = value  # Delegates to property setter
        return self

    def getUsesMonitor(self) -> Boolean:
        """
        AUTOSAR-compliant getter for usesMonitor.

        Returns:
            The usesMonitor value

        Note:
            Delegates to uses_monitor property (CODING_RULE_V2_00017)
        """
        return self.uses_monitor  # Delegates to property

    def setUsesMonitor(self, value: Boolean) -> DiagnosticEventNeeds:
        """
        AUTOSAR-compliant setter for usesMonitor with method chaining.

        Args:
            value: The usesMonitor to set

        Returns:
            self for method chaining

        Note:
            Delegates to uses_monitor property setter (gets validation automatically)
        """
        self.uses_monitor = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_diag_event(self, value: Optional[DiagEventDebounce]) -> DiagnosticEventNeeds:
        """
        Set diagEvent and return self for chaining.

        Args:
            value: The diagEvent to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_diag_event("value")
        """
        self.diag_event = value  # Use property setter (gets validation)
        return self

    def with_inhibiting_fid(self, value: Optional[FunctionInhibitionNeeds]) -> DiagnosticEventNeeds:
        """
        Set inhibitingFid and return self for chaining.

        Args:
            value: The inhibitingFid to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_inhibiting_fid("value")
        """
        self.inhibiting_fid = value  # Use property setter (gets validation)
        return self

    def with_prestored(self, value: Optional[Boolean]) -> DiagnosticEventNeeds:
        """
        Set prestored and return self for chaining.

        Args:
            value: The prestored to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_prestored("value")
        """
        self.prestored = value  # Use property setter (gets validation)
        return self

    def with_uses_monitor(self, value: Optional[Boolean]) -> DiagnosticEventNeeds:
        """
        Set usesMonitor and return self for chaining.

        Args:
            value: The usesMonitor to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_uses_monitor("value")
        """
        self.uses_monitor = value  # Use property setter (gets validation)
        return self



class DiagnosticComponentNeeds(DiagnosticCapabilityElement):
    """
    This meta-class represents the ability to specify the service needs for the
    configuration of component events.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::DiagnosticComponentNeeds

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 312, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 816, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class DiagnosticEventInfoNeeds(DiagnosticCapabilityElement):
    """
    This meta-class represents the needs of a software-component interested to
    get information regarding specific DTCs.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::DiagnosticEventInfoNeeds

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 312, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 760, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents a reasonable Diagnostic Trouble Code.
        # to predefine the Diagnostic Trouble Code, e.
        # g.
        # function developer has received a particular the OEM or from a
                # standardization applies for the OBD diagnostics use case.
        self._obdDtcNumber: Optional[PositiveInteger] = None

    @property
    def obd_dtc_number(self) -> Optional[PositiveInteger]:
        """Get obdDtcNumber (Pythonic accessor)."""
        return self._obdDtcNumber

    @obd_dtc_number.setter
    def obd_dtc_number(self, value: Optional[PositiveInteger]) -> None:
        """
        Set obdDtcNumber with validation.

        Args:
            value: The obdDtcNumber to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._obdDtcNumber = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"obdDtcNumber must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._obdDtcNumber = value
        # to predefine the Diagnostic Trouble Code, e.
        # g.
        # function developer has received a particular the OEM or from a
                # standardization applies for the UDS diagnostics use case.
        self._udsDtcNumber: Optional[PositiveInteger] = None

    @property
    def uds_dtc_number(self) -> Optional[PositiveInteger]:
        """Get udsDtcNumber (Pythonic accessor)."""
        return self._udsDtcNumber

    @uds_dtc_number.setter
    def uds_dtc_number(self, value: Optional[PositiveInteger]) -> None:
        """
        Set udsDtcNumber with validation.

        Args:
            value: The udsDtcNumber to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._udsDtcNumber = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"udsDtcNumber must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._udsDtcNumber = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getObdDtcNumber(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for obdDtcNumber.

        Returns:
            The obdDtcNumber value

        Note:
            Delegates to obd_dtc_number property (CODING_RULE_V2_00017)
        """
        return self.obd_dtc_number  # Delegates to property

    def setObdDtcNumber(self, value: PositiveInteger) -> DiagnosticEventInfoNeeds:
        """
        AUTOSAR-compliant setter for obdDtcNumber with method chaining.

        Args:
            value: The obdDtcNumber to set

        Returns:
            self for method chaining

        Note:
            Delegates to obd_dtc_number property setter (gets validation automatically)
        """
        self.obd_dtc_number = value  # Delegates to property setter
        return self

    def getUdsDtcNumber(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for udsDtcNumber.

        Returns:
            The udsDtcNumber value

        Note:
            Delegates to uds_dtc_number property (CODING_RULE_V2_00017)
        """
        return self.uds_dtc_number  # Delegates to property

    def setUdsDtcNumber(self, value: PositiveInteger) -> DiagnosticEventInfoNeeds:
        """
        AUTOSAR-compliant setter for udsDtcNumber with method chaining.

        Args:
            value: The udsDtcNumber to set

        Returns:
            self for method chaining

        Note:
            Delegates to uds_dtc_number property setter (gets validation automatically)
        """
        self.uds_dtc_number = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_obd_dtc_number(self, value: Optional[PositiveInteger]) -> DiagnosticEventInfoNeeds:
        """
        Set obdDtcNumber and return self for chaining.

        Args:
            value: The obdDtcNumber to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_obd_dtc_number("value")
        """
        self.obd_dtc_number = value  # Use property setter (gets validation)
        return self

    def with_uds_dtc_number(self, value: Optional[PositiveInteger]) -> DiagnosticEventInfoNeeds:
        """
        Set udsDtcNumber and return self for chaining.

        Args:
            value: The udsDtcNumber to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_uds_dtc_number("value")
        """
        self.uds_dtc_number = value  # Use property setter (gets validation)
        return self



class ObdInfoServiceNeeds(DiagnosticCapabilityElement):
    """
    Specifies the abstract needs of a component or module on the configuration
    of OBD Services in relation to a given InfoType (OBD Service 09) which is
    supported by this component or module.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::ObdInfoServiceNeeds

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 324, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 233, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 797, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class ObdPidServiceNeeds(DiagnosticCapabilityElement):
    """
    Specifies the abstract needs of a component or module on the configuration
    of OBD Services in relation to a particular PID (parameter identifier) which
    is supported by this component or module. In case of using a client/server
    communicated value, the related value shall be communicated via the port
    referenced by assignedPort. The details of this communication (e.g.
    appropriate naming conventions) are specified in the related software
    specifications (SWS).

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::ObdPidServiceNeeds

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 325, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 233, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 797, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class ObdControlServiceNeeds(DiagnosticCapabilityElement):
    """
    Specifies the abstract needs of a component or module on the configuration
    of OBD Service 08 (request control of on-board system) in relation to a
    particular test-Identifier (TID) supported by this component or module.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::ObdControlServiceNeeds

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 233, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 796, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class ObdMonitorServiceNeeds(DiagnosticCapabilityElement):
    """
    Specifies the abstract needs of a component or module on the configuration
    of OBD Services in relation to a particular on-board monitoring test
    supported by this component or module. (OBD Service 06).

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::ObdMonitorServiceNeeds

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 324, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 797, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # reference to an ApplicationDataType that describes the of the data reported
        # by the software-component to.
        self._applicationData: Optional["ApplicationDataType"] = None

    @property
    def application_data(self) -> Optional["ApplicationDataType"]:
        """Get applicationData (Pythonic accessor)."""
        return self._applicationData

    @application_data.setter
    def application_data(self, value: Optional["ApplicationDataType"]) -> None:
        """
        Set applicationData with validation.

        Args:
            value: The applicationData to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._applicationData = None
            return

        if not isinstance(value, ApplicationDataType):
            raise TypeError(
                f"applicationData must be ApplicationDataType or None, got {type(value).__name__}"
            )
        self._applicationData = value
        self._eventNeeds: Optional[DiagnosticEventNeeds] = None

    @property
    def event_needs(self) -> Optional[DiagnosticEventNeeds]:
        """Get eventNeeds (Pythonic accessor)."""
        return self._eventNeeds

    @event_needs.setter
    def event_needs(self, value: Optional[DiagnosticEventNeeds]) -> None:
        """
        Set eventNeeds with validation.

        Args:
            value: The eventNeeds to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._eventNeeds = None
            return

        if not isinstance(value, DiagnosticEventNeeds):
            raise TypeError(
                f"eventNeeds must be DiagnosticEventNeeds or None, got {type(value).__name__}"
            )
        self._eventNeeds = value
        self._unitAndScalingId: Optional[PositiveInteger] = None

    @property
    def unit_and_scaling_id(self) -> Optional[PositiveInteger]:
        """Get unitAndScalingId (Pythonic accessor)."""
        return self._unitAndScalingId

    @unit_and_scaling_id.setter
    def unit_and_scaling_id(self, value: Optional[PositiveInteger]) -> None:
        """
        Set unitAndScalingId with validation.

        Args:
            value: The unitAndScalingId to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._unitAndScalingId = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"unitAndScalingId must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._unitAndScalingId = value
        self._updateKind: Optional[DiagnosticMonitor] = None

    @property
    def update_kind(self) -> Optional[DiagnosticMonitor]:
        """Get updateKind (Pythonic accessor)."""
        return self._updateKind

    @update_kind.setter
    def update_kind(self, value: Optional[DiagnosticMonitor]) -> None:
        """
        Set updateKind with validation.

        Args:
            value: The updateKind to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._updateKind = None
            return

        if not isinstance(value, DiagnosticMonitor):
            raise TypeError(
                f"updateKind must be DiagnosticMonitor or None, got {type(value).__name__}"
            )
        self._updateKind = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getApplicationData(self) -> "ApplicationDataType":
        """
        AUTOSAR-compliant getter for applicationData.

        Returns:
            The applicationData value

        Note:
            Delegates to application_data property (CODING_RULE_V2_00017)
        """
        return self.application_data  # Delegates to property

    def setApplicationData(self, value: "ApplicationDataType") -> ObdMonitorServiceNeeds:
        """
        AUTOSAR-compliant setter for applicationData with method chaining.

        Args:
            value: The applicationData to set

        Returns:
            self for method chaining

        Note:
            Delegates to application_data property setter (gets validation automatically)
        """
        self.application_data = value  # Delegates to property setter
        return self

    def getEventNeeds(self) -> DiagnosticEventNeeds:
        """
        AUTOSAR-compliant getter for eventNeeds.

        Returns:
            The eventNeeds value

        Note:
            Delegates to event_needs property (CODING_RULE_V2_00017)
        """
        return self.event_needs  # Delegates to property

    def setEventNeeds(self, value: DiagnosticEventNeeds) -> ObdMonitorServiceNeeds:
        """
        AUTOSAR-compliant setter for eventNeeds with method chaining.

        Args:
            value: The eventNeeds to set

        Returns:
            self for method chaining

        Note:
            Delegates to event_needs property setter (gets validation automatically)
        """
        self.event_needs = value  # Delegates to property setter
        return self

    def getUnitAndScalingId(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for unitAndScalingId.

        Returns:
            The unitAndScalingId value

        Note:
            Delegates to unit_and_scaling_id property (CODING_RULE_V2_00017)
        """
        return self.unit_and_scaling_id  # Delegates to property

    def setUnitAndScalingId(self, value: PositiveInteger) -> ObdMonitorServiceNeeds:
        """
        AUTOSAR-compliant setter for unitAndScalingId with method chaining.

        Args:
            value: The unitAndScalingId to set

        Returns:
            self for method chaining

        Note:
            Delegates to unit_and_scaling_id property setter (gets validation automatically)
        """
        self.unit_and_scaling_id = value  # Delegates to property setter
        return self

    def getUpdateKind(self) -> "DiagnosticMonitor":
        """
        AUTOSAR-compliant getter for updateKind.

        Returns:
            The updateKind value

        Note:
            Delegates to update_kind property (CODING_RULE_V2_00017)
        """
        return self.update_kind  # Delegates to property

    def setUpdateKind(self, value: DiagnosticMonitor) -> ObdMonitorServiceNeeds:
        """
        AUTOSAR-compliant setter for updateKind with method chaining.

        Args:
            value: The updateKind to set

        Returns:
            self for method chaining

        Note:
            Delegates to update_kind property setter (gets validation automatically)
        """
        self.update_kind = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_application_data(self, value: Optional["ApplicationDataType"]) -> ObdMonitorServiceNeeds:
        """
        Set applicationData and return self for chaining.

        Args:
            value: The applicationData to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_application_data("value")
        """
        self.application_data = value  # Use property setter (gets validation)
        return self

    def with_event_needs(self, value: Optional[DiagnosticEventNeeds]) -> ObdMonitorServiceNeeds:
        """
        Set eventNeeds and return self for chaining.

        Args:
            value: The eventNeeds to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_event_needs("value")
        """
        self.event_needs = value  # Use property setter (gets validation)
        return self

    def with_unit_and_scaling_id(self, value: Optional[PositiveInteger]) -> ObdMonitorServiceNeeds:
        """
        Set unitAndScalingId and return self for chaining.

        Args:
            value: The unitAndScalingId to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_unit_and_scaling_id("value")
        """
        self.unit_and_scaling_id = value  # Use property setter (gets validation)
        return self

    def with_update_kind(self, value: Optional[DiagnosticMonitor]) -> ObdMonitorServiceNeeds:
        """
        Set updateKind and return self for chaining.

        Args:
            value: The updateKind to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_update_kind("value")
        """
        self.update_kind = value  # Use property setter (gets validation)
        return self



class DiagnosticEventManagerNeeds(DiagnosticCapabilityElement):
    """
    Specifies the general needs on the configuration of the Diagnostic Event
    Manager (Dem) which are not related to a particular item.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::DiagnosticEventManagerNeeds

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 753, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class DiagnosticOperationCycleNeeds(DiagnosticCapabilityElement):
    """
    This meta-class represents the needs of a software-component to provide
    information regarding the operation cycle management to the Dem module.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::DiagnosticOperationCycleNeeds

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 761, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Operation cycles types for the Dem to be supported by APIs.
        self._operationCycle: Optional[OperationCycleTypeEnum] = None

    @property
    def operation_cycle(self) -> Optional[OperationCycleTypeEnum]:
        """Get operationCycle (Pythonic accessor)."""
        return self._operationCycle

    @operation_cycle.setter
    def operation_cycle(self, value: Optional[OperationCycleTypeEnum]) -> None:
        """
        Set operationCycle with validation.

        Args:
            value: The operationCycle to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._operationCycle = None
            return

        if not isinstance(value, OperationCycleTypeEnum):
            raise TypeError(
                f"operationCycle must be OperationCycleTypeEnum or None, got {type(value).__name__}"
            )
        self._operationCycle = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getOperationCycle(self) -> OperationCycleTypeEnum:
        """
        AUTOSAR-compliant getter for operationCycle.

        Returns:
            The operationCycle value

        Note:
            Delegates to operation_cycle property (CODING_RULE_V2_00017)
        """
        return self.operation_cycle  # Delegates to property

    def setOperationCycle(self, value: OperationCycleTypeEnum) -> DiagnosticOperationCycleNeeds:
        """
        AUTOSAR-compliant setter for operationCycle with method chaining.

        Args:
            value: The operationCycle to set

        Returns:
            self for method chaining

        Note:
            Delegates to operation_cycle property setter (gets validation automatically)
        """
        self.operation_cycle = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_operation_cycle(self, value: Optional[OperationCycleTypeEnum]) -> DiagnosticOperationCycleNeeds:
        """
        Set operationCycle and return self for chaining.

        Args:
            value: The operationCycle to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_operation_cycle("value")
        """
        self.operation_cycle = value  # Use property setter (gets validation)
        return self



class DiagnosticEnableConditionNeeds(DiagnosticCapabilityElement):
    """
    This meta-class represents the needs of a software-component to provide the
    capability to set an enable condition.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::DiagnosticEnableConditionNeeds

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 762, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines the initial status for enable or disable of of event reports of a
        # diagnostic event.
        self._initialStatus: Optional[EventAcceptanceStatusEnum] = None

    @property
    def initial_status(self) -> Optional[EventAcceptanceStatusEnum]:
        """Get initialStatus (Pythonic accessor)."""
        return self._initialStatus

    @initial_status.setter
    def initial_status(self, value: Optional[EventAcceptanceStatusEnum]) -> None:
        """
        Set initialStatus with validation.

        Args:
            value: The initialStatus to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._initialStatus = None
            return

        if not isinstance(value, EventAcceptanceStatusEnum):
            raise TypeError(
                f"initialStatus must be EventAcceptanceStatusEnum or None, got {type(value).__name__}"
            )
        self._initialStatus = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getInitialStatus(self) -> EventAcceptanceStatusEnum:
        """
        AUTOSAR-compliant getter for initialStatus.

        Returns:
            The initialStatus value

        Note:
            Delegates to initial_status property (CODING_RULE_V2_00017)
        """
        return self.initial_status  # Delegates to property

    def setInitialStatus(self, value: EventAcceptanceStatusEnum) -> DiagnosticEnableConditionNeeds:
        """
        AUTOSAR-compliant setter for initialStatus with method chaining.

        Args:
            value: The initialStatus to set

        Returns:
            self for method chaining

        Note:
            Delegates to initial_status property setter (gets validation automatically)
        """
        self.initial_status = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_initial_status(self, value: Optional[EventAcceptanceStatusEnum]) -> DiagnosticEnableConditionNeeds:
        """
        Set initialStatus and return self for chaining.

        Args:
            value: The initialStatus to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_initial_status("value")
        """
        self.initial_status = value  # Use property setter (gets validation)
        return self



class DiagnosticStorageConditionNeeds(DiagnosticCapabilityElement):
    """
    This meta-class represents the needs of a software-component to provide the
    capability to set a storage condition.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::DiagnosticStorageConditionNeeds

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 762, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines the initial status for enable or disable of storage a diagnostic
        # event.
        self._initialStatus: Optional[StorageConditionStatusEnum] = None

    @property
    def initial_status(self) -> Optional[StorageConditionStatusEnum]:
        """Get initialStatus (Pythonic accessor)."""
        return self._initialStatus

    @initial_status.setter
    def initial_status(self, value: Optional[StorageConditionStatusEnum]) -> None:
        """
        Set initialStatus with validation.

        Args:
            value: The initialStatus to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._initialStatus = None
            return

        if not isinstance(value, StorageConditionStatusEnum):
            raise TypeError(
                f"initialStatus must be StorageConditionStatusEnum or None, got {type(value).__name__}"
            )
        self._initialStatus = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getInitialStatus(self) -> StorageConditionStatusEnum:
        """
        AUTOSAR-compliant getter for initialStatus.

        Returns:
            The initialStatus value

        Note:
            Delegates to initial_status property (CODING_RULE_V2_00017)
        """
        return self.initial_status  # Delegates to property

    def setInitialStatus(self, value: StorageConditionStatusEnum) -> DiagnosticStorageConditionNeeds:
        """
        AUTOSAR-compliant setter for initialStatus with method chaining.

        Args:
            value: The initialStatus to set

        Returns:
            self for method chaining

        Note:
            Delegates to initial_status property setter (gets validation automatically)
        """
        self.initial_status = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_initial_status(self, value: Optional[StorageConditionStatusEnum]) -> DiagnosticStorageConditionNeeds:
        """
        Set initialStatus and return self for chaining.

        Args:
            value: The initialStatus to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_initial_status("value")
        """
        self.initial_status = value  # Use property setter (gets validation)
        return self



class DtcStatusChangeNotificationNeeds(DiagnosticCapabilityElement):
    """
    This meta-class represents the needs of a software-component interested to
    get information regarding any DTC status change.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::DtcStatusChangeNotificationNeeds

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 776, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute determines the time when the notification the DTC operation
                # shall be executed.
        # This attribute relevant for the configuration of the ClearDtc.
        self._notificationTime: Optional[DiagnosticClearDtc] = None

    @property
    def notification_time(self) -> Optional[DiagnosticClearDtc]:
        """Get notificationTime (Pythonic accessor)."""
        return self._notificationTime

    @notification_time.setter
    def notification_time(self, value: Optional[DiagnosticClearDtc]) -> None:
        """
        Set notificationTime with validation.

        Args:
            value: The notificationTime to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._notificationTime = None
            return

        if not isinstance(value, DiagnosticClearDtc):
            raise TypeError(
                f"notificationTime must be DiagnosticClearDtc or None, got {type(value).__name__}"
            )
        self._notificationTime = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getNotificationTime(self) -> "DiagnosticClearDtc":
        """
        AUTOSAR-compliant getter for notificationTime.

        Returns:
            The notificationTime value

        Note:
            Delegates to notification_time property (CODING_RULE_V2_00017)
        """
        return self.notification_time  # Delegates to property

    def setNotificationTime(self, value: DiagnosticClearDtc) -> DtcStatusChangeNotificationNeeds:
        """
        AUTOSAR-compliant setter for notificationTime with method chaining.

        Args:
            value: The notificationTime to set

        Returns:
            self for method chaining

        Note:
            Delegates to notification_time property setter (gets validation automatically)
        """
        self.notification_time = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_notification_time(self, value: Optional[DiagnosticClearDtc]) -> DtcStatusChangeNotificationNeeds:
        """
        Set notificationTime and return self for chaining.

        Args:
            value: The notificationTime to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_notification_time("value")
        """
        self.notification_time = value  # Use property setter (gets validation)
        return self



class DiagnosticRequestFileTransferNeeds(DiagnosticCapabilityElement):
    """
    This meta-class indicates the existence of a service use case that involves
    UDS service 0x38, Request File Transfer.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::DiagnosticRequestFileTransferNeeds

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 795, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class ObdRatioServiceNeeds(DiagnosticCapabilityElement):
    """
    Specifies the abstract needs of a component or module on the configuration
    of OBD Services in relation to a particular "ratio monitoring" which is
    supported by this component or module.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::ObdRatioServiceNeeds

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 795, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines how the DEM is connected to the component or to perform the IUMPR (In
        # use monitor service.
        self._connectionType: Optional[ObdRatioConnectionKindEnum] = None

    @property
    def connection_type(self) -> Optional[ObdRatioConnectionKindEnum]:
        """Get connectionType (Pythonic accessor)."""
        return self._connectionType

    @connection_type.setter
    def connection_type(self, value: Optional[ObdRatioConnectionKindEnum]) -> None:
        """
        Set connectionType with validation.

        Args:
            value: The connectionType to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._connectionType = None
            return

        if not isinstance(value, ObdRatioConnectionKindEnum):
            raise TypeError(
                f"connectionType must be ObdRatioConnectionKindEnum or None, got {type(value).__name__}"
            )
        self._connectionType = value
        self._rateBasedMonitoredEvent: Optional[DiagnosticEventNeeds] = None

    @property
    def rate_based_monitored_event(self) -> Optional[DiagnosticEventNeeds]:
        """Get rateBasedMonitoredEvent (Pythonic accessor)."""
        return self._rateBasedMonitoredEvent

    @rate_based_monitored_event.setter
    def rate_based_monitored_event(self, value: Optional[DiagnosticEventNeeds]) -> None:
        """
        Set rateBasedMonitoredEvent with validation.

        Args:
            value: The rateBasedMonitoredEvent to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rateBasedMonitoredEvent = None
            return

        if not isinstance(value, DiagnosticEventNeeds):
            raise TypeError(
                f"rateBasedMonitoredEvent must be DiagnosticEventNeeds or None, got {type(value).__name__}"
            )
        self._rateBasedMonitoredEvent = value
                # monitor.
        # This is an optional.
        self._usedFid: Optional[FunctionInhibitionNeeds] = None

    @property
    def used_fid(self) -> Optional[FunctionInhibitionNeeds]:
        """Get usedFid (Pythonic accessor)."""
        return self._usedFid

    @used_fid.setter
    def used_fid(self, value: Optional[FunctionInhibitionNeeds]) -> None:
        """
        Set usedFid with validation.

        Args:
            value: The usedFid to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._usedFid = None
            return

        if not isinstance(value, FunctionInhibitionNeeds):
            raise TypeError(
                f"usedFid must be FunctionInhibitionNeeds or None, got {type(value).__name__}"
            )
        self._usedFid = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getConnectionType(self) -> ObdRatioConnectionKindEnum:
        """
        AUTOSAR-compliant getter for connectionType.

        Returns:
            The connectionType value

        Note:
            Delegates to connection_type property (CODING_RULE_V2_00017)
        """
        return self.connection_type  # Delegates to property

    def setConnectionType(self, value: ObdRatioConnectionKindEnum) -> ObdRatioServiceNeeds:
        """
        AUTOSAR-compliant setter for connectionType with method chaining.

        Args:
            value: The connectionType to set

        Returns:
            self for method chaining

        Note:
            Delegates to connection_type property setter (gets validation automatically)
        """
        self.connection_type = value  # Delegates to property setter
        return self

    def getRateBasedMonitoredEvent(self) -> DiagnosticEventNeeds:
        """
        AUTOSAR-compliant getter for rateBasedMonitoredEvent.

        Returns:
            The rateBasedMonitoredEvent value

        Note:
            Delegates to rate_based_monitored_event property (CODING_RULE_V2_00017)
        """
        return self.rate_based_monitored_event  # Delegates to property

    def setRateBasedMonitoredEvent(self, value: DiagnosticEventNeeds) -> ObdRatioServiceNeeds:
        """
        AUTOSAR-compliant setter for rateBasedMonitoredEvent with method chaining.

        Args:
            value: The rateBasedMonitoredEvent to set

        Returns:
            self for method chaining

        Note:
            Delegates to rate_based_monitored_event property setter (gets validation automatically)
        """
        self.rate_based_monitored_event = value  # Delegates to property setter
        return self

    def getUsedFid(self) -> FunctionInhibitionNeeds:
        """
        AUTOSAR-compliant getter for usedFid.

        Returns:
            The usedFid value

        Note:
            Delegates to used_fid property (CODING_RULE_V2_00017)
        """
        return self.used_fid  # Delegates to property

    def setUsedFid(self, value: FunctionInhibitionNeeds) -> ObdRatioServiceNeeds:
        """
        AUTOSAR-compliant setter for usedFid with method chaining.

        Args:
            value: The usedFid to set

        Returns:
            self for method chaining

        Note:
            Delegates to used_fid property setter (gets validation automatically)
        """
        self.used_fid = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_connection_type(self, value: Optional[ObdRatioConnectionKindEnum]) -> ObdRatioServiceNeeds:
        """
        Set connectionType and return self for chaining.

        Args:
            value: The connectionType to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_connection_type("value")
        """
        self.connection_type = value  # Use property setter (gets validation)
        return self

    def with_rate_based_monitored_event(self, value: Optional[DiagnosticEventNeeds]) -> ObdRatioServiceNeeds:
        """
        Set rateBasedMonitoredEvent and return self for chaining.

        Args:
            value: The rateBasedMonitoredEvent to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_rate_based_monitored_event("value")
        """
        self.rate_based_monitored_event = value  # Use property setter (gets validation)
        return self

    def with_used_fid(self, value: Optional[FunctionInhibitionNeeds]) -> ObdRatioServiceNeeds:
        """
        Set usedFid and return self for chaining.

        Args:
            value: The usedFid to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_used_fid("value")
        """
        self.used_fid = value  # Use property setter (gets validation)
        return self



class ObdRatioDenominatorNeeds(DiagnosticCapabilityElement):
    """
    This meta-class shall be used to indicate that a software-component wants to
    access the in-use-monitoring performance ration denominator.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::ObdRatioDenominatorNeeds

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 802, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute indicates the applicable denominator condition.
        self._denominator: Optional[DiagnosticDenominator] = None

    @property
    def denominator(self) -> Optional[DiagnosticDenominator]:
        """Get denominator (Pythonic accessor)."""
        return self._denominator

    @denominator.setter
    def denominator(self, value: Optional[DiagnosticDenominator]) -> None:
        """
        Set denominator with validation.

        Args:
            value: The denominator to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._denominator = None
            return

        if not isinstance(value, DiagnosticDenominator):
            raise TypeError(
                f"denominator must be DiagnosticDenominator or None, got {type(value).__name__}"
            )
        self._denominator = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDenominator(self) -> "DiagnosticDenominator":
        """
        AUTOSAR-compliant getter for denominator.

        Returns:
            The denominator value

        Note:
            Delegates to denominator property (CODING_RULE_V2_00017)
        """
        return self.denominator  # Delegates to property

    def setDenominator(self, value: DiagnosticDenominator) -> ObdRatioDenominatorNeeds:
        """
        AUTOSAR-compliant setter for denominator with method chaining.

        Args:
            value: The denominator to set

        Returns:
            self for method chaining

        Note:
            Delegates to denominator property setter (gets validation automatically)
        """
        self.denominator = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_denominator(self, value: Optional[DiagnosticDenominator]) -> ObdRatioDenominatorNeeds:
        """
        Set denominator and return self for chaining.

        Args:
            value: The denominator to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_denominator("value")
        """
        self.denominator = value  # Use property setter (gets validation)
        return self



class WarningIndicatorRequestedBitNeeds(DiagnosticCapabilityElement):
    """
    This meta-class represents the ability to explicitly request the existence
    of the WarningIndicator RequestedBit.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::WarningIndicatorRequestedBitNeeds

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 811, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class DiagnosticControlNeeds(DiagnosticCapabilityElement):
    """
    This meta-class indicates a service use-case for reporting the controlled
    status by diagnostic services.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::DiagnosticControlNeeds

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 812, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class DoIpGidNeeds(DoIpServiceNeeds):
    """
    The DoIpGidNeeds indicates that the software-component owning this
    ServiceNeeds is providing the GID number either after a GID Synchronisation
    or by other means like e.g. flashed EEPROM parameter. This need can be used
    independent from DoIpGidSynchronizationNeeds and is necessary if the GID can
    not be provided out of the DoIP configuration options.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::DoIpGidNeeds

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 805, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2019, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class DoIpGidSynchronizationNeeds(DoIpServiceNeeds):
    """
    The DoIpGidSynchronizationNeeds indicates that the software-component owning
    this ServiceNeeds is triggered by the DoIP entity to start a synchronization
    of the GID (Group Identification) on the DoIP service 0x0001, 0x0002, 0x0003
    or before announcement via service 0x0004 according to ISO 13400-2:2012 if
    necessary. Note that this need is only relevant for DoIP synchronization
    masters.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::DoIpGidSynchronizationNeeds

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 805, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2019, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class DoIpPowerModeStatusNeeds(DoIpServiceNeeds):
    """
    The DoIpPowerModeStatusNeeds indicates that the software-component owning
    this ServiceNeeds is providing the PowerModeStatus for the DoIP service
    0x4003 according to ISO 13400-2:2012.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::DoIpPowerModeStatusNeeds

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 806, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2019, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class DoIpRoutingActivationAuthenticationNeeds(DoIpServiceNeeds):
    """
    DoIPRoutingActivationAuthenticationNeeds indicates that the
    software-component owning this Service Needs will have an authentication
    required for a DoIP routing activation service (0x0005) according to ISO
    13400-2:2012.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::DoIpRoutingActivationAuthenticationNeeds

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 806, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Describes the length in byte of the additional information RA authentication
                # that is provided by the software the software entity is a software-component
                # the not need to exist as the information is the length of the uint8 Array
                # type.
        # Otherwise software entity is a Complex Driver) this attribute be filled in if
                # additional information is provided.
        self._dataLength: Optional[PositiveInteger] = None

    @property
    def data_length(self) -> Optional[PositiveInteger]:
        """Get dataLength (Pythonic accessor)."""
        return self._dataLength

    @data_length.setter
    def data_length(self, value: Optional[PositiveInteger]) -> None:
        """
        Set dataLength with validation.

        Args:
            value: The dataLength to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dataLength = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"dataLength must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._dataLength = value
                # received via DoIP 0x00 is DEFAULT, 0x01 is WWH-OBD.
        # If the specified values (0x00 or 0x01) is needed shall contain RA_ + hex
                # value representation of value shall be used (i.
        # e: RA_0xE1).
        self._routing: Optional[NameToken] = None

    @property
    def routing(self) -> Optional[NameToken]:
        """Get routing (Pythonic accessor)."""
        return self._routing

    @routing.setter
    def routing(self, value: Optional[NameToken]) -> None:
        """
        Set routing with validation.

        Args:
            value: The routing to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._routing = None
            return

        if not isinstance(value, (NameToken, str)):
            raise TypeError(
                f"routing must be NameToken or str or None, got {type(value).__name__}"
            )
        self._routing = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDataLength(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for dataLength.

        Returns:
            The dataLength value

        Note:
            Delegates to data_length property (CODING_RULE_V2_00017)
        """
        return self.data_length  # Delegates to property

    def setDataLength(self, value: PositiveInteger) -> DoIpRoutingActivationAuthenticationNeeds:
        """
        AUTOSAR-compliant setter for dataLength with method chaining.

        Args:
            value: The dataLength to set

        Returns:
            self for method chaining

        Note:
            Delegates to data_length property setter (gets validation automatically)
        """
        self.data_length = value  # Delegates to property setter
        return self

    def getRouting(self) -> "NameToken":
        """
        AUTOSAR-compliant getter for routing.

        Returns:
            The routing value

        Note:
            Delegates to routing property (CODING_RULE_V2_00017)
        """
        return self.routing  # Delegates to property

    def setRouting(self, value: NameToken) -> DoIpRoutingActivationAuthenticationNeeds:
        """
        AUTOSAR-compliant setter for routing with method chaining.

        Args:
            value: The routing to set

        Returns:
            self for method chaining

        Note:
            Delegates to routing property setter (gets validation automatically)
        """
        self.routing = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_data_length(self, value: Optional[PositiveInteger]) -> DoIpRoutingActivationAuthenticationNeeds:
        """
        Set dataLength and return self for chaining.

        Args:
            value: The dataLength to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_data_length("value")
        """
        self.data_length = value  # Use property setter (gets validation)
        return self

    def with_routing(self, value: Optional[NameToken]) -> DoIpRoutingActivationAuthenticationNeeds:
        """
        Set routing and return self for chaining.

        Args:
            value: The routing to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_routing("value")
        """
        self.routing = value  # Use property setter (gets validation)
        return self



class DoIpRoutingActivationConfirmationNeeds(DoIpServiceNeeds):
    """
    DoIpRoutingActivationConfirmationNeeds indicates that the software-component
    that owns this Service Needs will have a confirmation required for a DoIP
    routing activation service (0x0005) according to ISO 13400-2:2012.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::DoIpRoutingActivationConfirmationNeeds

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 807, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Describes the length in byte of the additional information RA confirmation
                # that is provided by the software entity.
        # software entity is a software-component the not need to exist as the
                # information is the length of the uint8 Array type.
        # Otherwise software entity is a Complex Driver) this attribute be filled out
                # if additional information is provided.
        self._dataLength: Optional[PositiveInteger] = None

    @property
    def data_length(self) -> Optional[PositiveInteger]:
        """Get dataLength (Pythonic accessor)."""
        return self._dataLength

    @data_length.setter
    def data_length(self, value: Optional[PositiveInteger]) -> None:
        """
        Set dataLength with validation.

        Args:
            value: The dataLength to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dataLength = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"dataLength must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._dataLength = value
                # received via DoIP 0x00 is DEFAULT, 0x01 is WWH-OBD.
        # If the specified values (0x00 or 0x01) is needed shall contain RA_ + hex
                # value representation of value shall be used (i.
        # e: RA_0xE1).
        self._routing: Optional[NameToken] = None

    @property
    def routing(self) -> Optional[NameToken]:
        """Get routing (Pythonic accessor)."""
        return self._routing

    @routing.setter
    def routing(self, value: Optional[NameToken]) -> None:
        """
        Set routing with validation.

        Args:
            value: The routing to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._routing = None
            return

        if not isinstance(value, (NameToken, str)):
            raise TypeError(
                f"routing must be NameToken or str or None, got {type(value).__name__}"
            )
        self._routing = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDataLength(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for dataLength.

        Returns:
            The dataLength value

        Note:
            Delegates to data_length property (CODING_RULE_V2_00017)
        """
        return self.data_length  # Delegates to property

    def setDataLength(self, value: PositiveInteger) -> DoIpRoutingActivationConfirmationNeeds:
        """
        AUTOSAR-compliant setter for dataLength with method chaining.

        Args:
            value: The dataLength to set

        Returns:
            self for method chaining

        Note:
            Delegates to data_length property setter (gets validation automatically)
        """
        self.data_length = value  # Delegates to property setter
        return self

    def getRouting(self) -> "NameToken":
        """
        AUTOSAR-compliant getter for routing.

        Returns:
            The routing value

        Note:
            Delegates to routing property (CODING_RULE_V2_00017)
        """
        return self.routing  # Delegates to property

    def setRouting(self, value: NameToken) -> DoIpRoutingActivationConfirmationNeeds:
        """
        AUTOSAR-compliant setter for routing with method chaining.

        Args:
            value: The routing to set

        Returns:
            self for method chaining

        Note:
            Delegates to routing property setter (gets validation automatically)
        """
        self.routing = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_data_length(self, value: Optional[PositiveInteger]) -> DoIpRoutingActivationConfirmationNeeds:
        """
        Set dataLength and return self for chaining.

        Args:
            value: The dataLength to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_data_length("value")
        """
        self.data_length = value  # Use property setter (gets validation)
        return self

    def with_routing(self, value: Optional[NameToken]) -> DoIpRoutingActivationConfirmationNeeds:
        """
        Set routing and return self for chaining.

        Args:
            value: The routing to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_routing("value")
        """
        self.routing = value  # Use property setter (gets validation)
        return self



class DoIpActivationLineNeeds(DoIpServiceNeeds):
    """
    A DoIP entity needs to be informed when an external tester is attached or
    activated. The DoIpActivation ServiceNeeds specifies the trigger for such an
    event. Examples would be a Pdu via a regular communication bus, a PWM
    signal, or an I/O. For details please refer to the ISO 13400.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::DoIpActivationLineNeeds

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 807, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2019, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class FurtherActionByteNeeds(DoIpServiceNeeds):
    """
    The FurtherActionByteNeeds indicates that the software-component is able to
    provide the "further action byte" to the DoIp Service Component.

    Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds::FurtherActionByteNeeds

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 812, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====


class NvBlockNeedsReliabilityEnum(AREnum):
    """
    NvBlockNeedsReliabilityEnum enumeration

Reliability against data loss on the non-volatile medium. These requirements give only a relative indication, for example on the required degree of redundancy for storage. They do, however, not specify by which means (e.g. software or hardware) the reliability is actually achieved. Aggregated by NvBlockNeeds.reliability

Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds
    """
    # Errors shall be corrected
    errorCorrection = "0"

    # Errors shall be detected
    errorDetection = "1"

    # Data need not to be handled with protection
    noProtection = "2"



class NvBlockNeedsWritingPriorityEnum(AREnum):
    """
    NvBlockNeedsWritingPriorityEnum enumeration

Specifies the priority of writing this block in case of concurrent requests to write other blocks. Aggregated by NvBlockNeeds.writingPriority

Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds
    """
    # Writing priority is high.
    high = "0"

    # Writing priority is low.
    low = "1"

    # Writing priority is medium.
    medium = "2"



class MaxCommModeEnum(AREnum):
    """
    MaxCommModeEnum enumeration

Maximum bus communication mode required by a user of the Communication Manager Service. Aggregated by ComMgrUserNeeds.maxCommMode (cid:53) 233 of 381 Document ID 89: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate Basic Software Module Description Template AUTOSAR CP R23-11 (cid:52)

Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds
    """
    # Full communication is requested.
    full = "0"

    # No communication is requested.
    none = "1"

    # Silent communication is requested: Only listening but not "talking".
    silent = "2"



class DiagnosticValueAccessEnum(AREnum):
    """
    DiagnosticValueAccessEnum enumeration

Defines the access of the configured diagnostic current values which will be used by the Dem or Dcm module. Aggregated by DiagnosticValueNeeds.diagnosticValueAccess

Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds
    """
    # The access to the data element is limited to read-only. This is typically used to read-out diagnostic
    readOnlyinformation = "0"

    # The value of the diagnostic data element is classified as configurable (read and write access is
    readWrite = "1"

    # The access to the data element is limited to write-only. This supports the use case where the Dcm just writes data to the application software without the intention to read it back,
    writeOnly = "2"



class DiagnosticProcessingStyleEnum(AREnum):
    """
    DiagnosticProcessingStyleEnum enumeration

This meta-class represents the ability to define the processing style of diagnostic requests. Aggregated by DiagnosticValueNeeds.processingStyle

Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds
    """
    # Software Module Description Template
    Basic = "None"

    # CP R23-11
    AUTOSAR = "None"

    # The software-component processes the request in background but still the Dcm has to issue the call Asynchronous again to eventually obtain the result of the request.
    processingStyle = "0"

    # The software-component processes the request in background but still the Dcm has to issue the call AsynchronousWith again to eventually obtain the result of the request or handle error code.
    processingStyleError = "1"

    # The software-component is supposed to react synchronously on the request.
    processingStyleSynchronous = "2"



class DiagnosticRoutineTypeEnum(AREnum):
    """
    DiagnosticRoutineTypeEnum enumeration

This enumerator specifies the different types of diagnostic routines. Aggregated by DiagnosticRoutineNeeds.diagRoutineType

Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds
    """
    # This indicates that the diagnostic server is not blocked while the diagnostic routine is running.
    asynchronous = "0"

    # This indicates that the diagnostic routine blocks the diagnostic server in the ECU while the routine is
    synchronous = "1"



class ServiceProviderEnum(AREnum):
    """
    ServiceProviderEnum enumeration

This represents a list of possible service providers Aggregated by PortInterface.serviceKind

Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds
    """
    # This value means that the specific nature is either unknown or it is not important for the given
    anyStandardized = "0"

    # The service relates to the Basic Software Mode Manager (BswM)
    basicSoftwareModeManager = "1"

    # The service relates to the COM Manager (ComM).
    comManager = "2"

    # The service relates to the Key Manager (KeyM).
    cryptoKeyManagement = "23"

    # The service relates to the Crypto Service Manager (CsM).
    cryptoServiceManager = "3"

    # The service relates to the Default Error Tracer (DET)
    defaultErrorTracer = "4"

    # The service relates to the Diagnostic Communication Manager (DCM).
    diagnosticCommunication = "6"

    # The service relates to the Diagnostic Event Manager (DEM).
    diagnosticEventManager = "7"

    # The service relates to the Diagnostic Log and Trace (DLT).
    diagnosticLogAndTrace = "8"

    # The service relates to the ECU Manager (EcuM).
    ecuManager = "9"

    # This service relates to the error tracer.
    errorTracer = "18"

    # The service relates to the Function Inhibition Manager (FIM).
    functionInhibitionManager = "10"

    # This service relates to the hardware test manager.
    hardwareTestManager = "19"

    # The service relates to the intrusion detection security management (IdsM).
    intrusionDetectionSecurity = "24"

    # This service relates to the J1939 Dcm.
    j1939Dcm = "22"

    # The service relates to the J1939Rm.
    j1939RequestManager = "11"

    # Component Template
    Software = "None"

    # CP R23-11
    AUTOSAR = "None"

    # The service relates to the Non-Volatile RAM Manager (NvM).
    nonVolatileRamManager = "12"

    # The service relates to the Operating System (OS).
    operatingSystem = "13"

    # The service relates to the SecOc module.
    secureOnBoardCommunication = "14"

    # The service relates to the Sync Time Base Manager (StbM).
    syncBaseTimeManager = "15"

    # This service relates to the Vehicle to X facilities.
    v2xFacilities = "20"

    # This service relates to the Vehicle to X management.
    v2xManagement = "21"

    # This value denotes a vendor-specific service.
    vendorSpecific = "16"

    # The service relates to the Watchdog Manager (WdgM).
    watchDogManager = "17"



class ServiceDiagnosticRelevanceEnum(AREnum):
    """
    ServiceDiagnosticRelevanceEnum enumeration

This enumeration provides values to describe the diagnostic relevance of a SwcServiceDependency (specifically if the aggregated ServiceNeeds itself does not indicate a relevance for diagnostics). Aggregated by ServiceDependency.diagnosticRelevance

Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds
    """
    # This value indicates that a relevance for diagnostics does not exist.
    isNotRelevant = "0"

    # This value indicates a relevance for diagnostics.
    isRelevant = "1"



class DiagnosticAudienceEnum(AREnum):
    """
    DiagnosticAudienceEnum enumeration

The possible values of the intended audience for a diagnostic object. Aggregated by DiagnosticCapabilityElement.audience

Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds
    """
    # The object is for free aftermarket service organizations.
    aftermarket = "1"

    # The object is relevant for the OEM after-sales organization.
    afterSales = "2"

    # The object is relevant for engineering only.
    development = "3"

    # The object is relevant for manufacturing.
    manufacturing = "4"

    # The object is relevant for the ECU-supplier aftermarket organization.
    supplier = "5"



class OperationCycleTypeEnum(AREnum):
    """
    OperationCycleTypeEnum enumeration

The possible values of the operation cycles types for the Dem. Aggregated by DiagnosticOperationCycleNeeds.operationCycle

Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds
    """
    # Ignition ON / OFF cycle.
    ignition = "0"

    # OBD Driving cycle.
    obdDcy = "1"

    # Further operation cycle.
    other = "2"

    # Power ON / OFF cycle.
    power = "3"

    # Time based operation cycle.
    time = "4"

    # OBD Warm up cycle.
    warmup = "5"



class EventAcceptanceStatusEnum(AREnum):
    """
    EventAcceptanceStatusEnum enumeration

This enumerator specifies the initial status for enable or disable of acceptance of event reports of a diagnostic event. Aggregated by DiagnosticEnableConditionNeeds.initialStatus

Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds
    """
    # Acceptance of a diagnostic event is disabled.
    eventAcceptanceDisabled = "0"

    # Acceptance of a diagnostic event is enabled.
    eventAcceptanceEnabled = "1"



class StorageConditionStatusEnum(AREnum):
    """
    StorageConditionStatusEnum enumeration

This enumeration specifies the initial status for enable or disable of storage of a diagnostic event. Aggregated by DiagnosticStorageConditionNeeds.initialStatus

Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds
    """
    # Storage of a diagnostic event is disabled.
    eventStorageDisabled = "0"

    # Storage of a diagnostic event is enabled.
    eventStorageEnabled = "1"



class DiagnosticClearDtcNotificationEnum(AREnum):
    """
    DiagnosticClearDtcNotificationEnum enumeration

This enumeration supports the specification of the time when the ClearDtcNotification callback is supposed to be executed. Aggregated by DtcStatusChangeNotificationNeeds.notificationTime

Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds
    """
    # The ClearDtcCallback shall be executed when the DTC operation finishes.
    finish = "1"

    # The ClearDtcCallback shall be executed when the DTC operation starts.
    start = "0"



class DiagnosticServiceRequestCallbackTypeEnum(AREnum):
    """
    DiagnosticServiceRequestCallbackTypeEnum enumeration

This represents the ability to define whether a Service Request Notification was used in the role of a manufacturer or a supplier. Aggregated by DiagnosticCommunicationManagerNeeds.serviceRequestCallbackType

Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds
    """
    # Component Template
    Software = "None"

    # CP R23-11
    AUTOSAR = "None"

    # This represents the case that the usage of PortInterface ServiceRequestNotification has the TypeManufacturer characteristics of being used by a manufacturer.
    requestCallback = "0"

    # This represents the case that the usage of PortInterface ServiceRequestNotification has the TypeSupplier characteristics of being used by a supplier.
    requestCallback = "1"



class ObdRatioConnectionKindEnum(AREnum):
    """
    ObdRatioConnectionKindEnum enumeration

Defines the way how the IUMPR service connection between the Dem and the client component or module is handled (for details see the DEM Specification). Aggregated by ObdRatioServiceNeeds.connectionType

Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds
    """
    # The IUMPR service (of the DEM) uses an explicit API to connect to the component or module.
    apiUse = "0"

    # The IUMPR service (of the Dem) uses no API but "observes" the associated diagnostic event.
    observer = "1"



class DiagnosticMonitorUpdateKindEnum(AREnum):
    """
    DiagnosticMonitorUpdateKindEnum enumeration

This enumeration indicates the acceptance criteria for a diagnostic monitor. Aggregated by ObdMonitorServiceNeeds.updateKind

Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds
    """
    # The value ’always’ configures Dem to accept the call to SetDTR() regardless of the state of the
    always = "0"

    # The value ’steady’ configures Dem to accept it only when debouncing is at the limit.
    steady = "1"



class DiagnosticDenominatorConditionEnum(AREnum):
    """
    DiagnosticDenominatorConditionEnum enumeration

This enumeration contains valid denominator types. Aggregated by ObdRatioDenominatorNeeds.denominatorCondition

Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds
    """
    # Condition based on definition of 500miles conditions as defined for OBD2.
    _500miles = "2"

    # Condition based on definition of "cold start" as defined for EU5+
    coldstart = "0"

    # Conditions based on the "Cold start emission reduction strategy" denominator
    csers = "5"

    # Condition based on definition of "EVAP" conditions as defined for OBD2.
    evap = "1"

    # Conditions based on the "EVAP purge flow" denominator. individual condition based on definition of individual requirements.
    evappurgeflow = "3"

    # Condition based on definition of OBD requirements.
    obd = "4"



class VerificationStatusIndicationModeEnum(AREnum):
    """
    VerificationStatusIndicationModeEnum enumeration

This enumeration provides options for setting the mode of a verification status indication. Aggregated by SecureOnBoardCommunicationNeeds.verificationStatusIndicationMode

Package: M2::AUTOSARTemplates::CommonStructure::ServiceNeeds
    """
    # Verification attempts that came out "false" or "true" shall be forwarded to the application software.
    failureAndSuccess = "1"

    # Only verification attempts that came out "false" shall be forwarded to the application software.
    failureOnly = "0"

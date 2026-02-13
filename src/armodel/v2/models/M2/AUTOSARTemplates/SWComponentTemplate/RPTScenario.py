"""
AUTOSAR Package - RPTScenario

Package: M2::AUTOSARTemplates::SWComponentTemplate::RPTScenario
"""


from __future__ import annotations
from abc import ABC
from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
    PositiveInteger,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
)


class RptImplPolicy(ARObject):
    """
    Describes the code preparation for rapid prototyping at data accesses.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::RPTScenario::RptImplPolicy

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 202, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 854, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # For Level 2 or Level3 this property determines how the RTE implements the
        # additional "RP enabler" flag.
        self._rptEnablerImpl: Optional["RptEnablerImplType"] = None

    @property
    def rpt_enabler_impl(self) -> Optional["RptEnablerImplType"]:
        """Get rptEnablerImpl (Pythonic accessor)."""
        return self._rptEnablerImpl

    @rpt_enabler_impl.setter
    def rpt_enabler_impl(self, value: Optional["RptEnablerImplType"]) -> None:
        """
        Set rptEnablerImpl with validation.

        Args:
            value: The rptEnablerImpl to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rptEnablerImpl = None
            return

        if not isinstance(value, RptEnablerImplType):
            raise TypeError(
                f"rptEnablerImpl must be RptEnablerImplType or None, got {type(value).__name__}"
            )
        self._rptEnablerImpl = value
        # implementation.
        self._rptPreparation: Optional["RptPreparationEnum"] = None

    @property
    def rpt_preparation(self) -> Optional["RptPreparationEnum"]:
        """Get rptPreparation (Pythonic accessor)."""
        return self._rptPreparation

    @rpt_preparation.setter
    def rpt_preparation(self, value: Optional["RptPreparationEnum"]) -> None:
        """
        Set rptPreparation with validation.

        Args:
            value: The rptPreparation to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rptPreparation = None
            return

        if not isinstance(value, RptPreparationEnum):
            raise TypeError(
                f"rptPreparation must be RptPreparationEnum or None, got {type(value).__name__}"
            )
        self._rptPreparation = value

    def with_rpt_container(self, value):
        """
        Set rpt_container and return self for chaining.

        Args:
            value: The rpt_container to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_rpt_container("value")
        """
        self.rpt_container = value  # Use property setter (gets validation)
        return self

    def with_rpt_profile(self, value):
        """
        Set rpt_profile and return self for chaining.

        Args:
            value: The rpt_profile to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_rpt_profile("value")
        """
        self.rpt_profile = value  # Use property setter (gets validation)
        return self

    def with_by_pass_point(self, value):
        """
        Set by_pass_point and return self for chaining.

        Args:
            value: The by_pass_point to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_by_pass_point("value")
        """
        self.by_pass_point = value  # Use property setter (gets validation)
        return self

    def with_explicit_rpt(self, value):
        """
        Set explicit_rpt and return self for chaining.

        Args:
            value: The explicit_rpt to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_explicit_rpt("value")
        """
        self.explicit_rpt = value  # Use property setter (gets validation)
        return self

    def with_rpt_container(self, value):
        """
        Set rpt_container and return self for chaining.

        Args:
            value: The rpt_container to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_rpt_container("value")
        """
        self.rpt_container = value  # Use property setter (gets validation)
        return self

    def with_sdg(self, value):
        """
        Set sdg and return self for chaining.

        Args:
            value: The sdg to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sdg("value")
        """
        self.sdg = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getRptEnablerImpl(self) -> "RptEnablerImplType":
        """
        AUTOSAR-compliant getter for rptEnablerImpl.

        Returns:
            The rptEnablerImpl value

        Note:
            Delegates to rpt_enabler_impl property (CODING_RULE_V2_00017)
        """
        return self.rpt_enabler_impl  # Delegates to property

    def setRptEnablerImpl(self, value: "RptEnablerImplType") -> RptImplPolicy:
        """
        AUTOSAR-compliant setter for rptEnablerImpl with method chaining.

        Args:
            value: The rptEnablerImpl to set

        Returns:
            self for method chaining

        Note:
            Delegates to rpt_enabler_impl property setter (gets validation automatically)
        """
        self.rpt_enabler_impl = value  # Delegates to property setter
        return self

    def getRptPreparation(self) -> "RptPreparationEnum":
        """
        AUTOSAR-compliant getter for rptPreparation.

        Returns:
            The rptPreparation value

        Note:
            Delegates to rpt_preparation property (CODING_RULE_V2_00017)
        """
        return self.rpt_preparation  # Delegates to property

    def setRptPreparation(self, value: "RptPreparationEnum") -> RptImplPolicy:
        """
        AUTOSAR-compliant setter for rptPreparation with method chaining.

        Args:
            value: The rptPreparation to set

        Returns:
            self for method chaining

        Note:
            Delegates to rpt_preparation property setter (gets validation automatically)
        """
        self.rpt_preparation = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_rpt_enabler_impl(self, value: Optional["RptEnablerImplType"]) -> RptImplPolicy:
        """
        Set rptEnablerImpl and return self for chaining.

        Args:
            value: The rptEnablerImpl to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_rpt_enabler_impl("value")
        """
        self.rpt_enabler_impl = value  # Use property setter (gets validation)
        return self

    def with_rpt_preparation(self, value: Optional["RptPreparationEnum"]) -> RptImplPolicy:
        """
        Set rptPreparation and return self for chaining.

        Args:
            value: The rptPreparation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_rpt_preparation("value")
        """
        self.rpt_preparation = value  # Use property setter (gets validation)
        return self



class RptExecutableEntityProperties(ARObject):
    """
    Describes the code preparation for rapid prototyping at ExecutableEntity
    invocation.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::RPTScenario::RptExecutableEntityProperties

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 203, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 859, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Highest RPT event id usable for RTE generated service attribute is relevant,
        # if dedicated id range applied to the ExecutableEntitys of a software specific
        # ExecutableEntitys.
        self._maxRptEventId: Optional[PositiveInteger] = None

    @property
    def max_rpt_event_id(self) -> Optional[PositiveInteger]:
        """Get maxRptEventId (Pythonic accessor)."""
        return self._maxRptEventId

    @max_rpt_event_id.setter
    def max_rpt_event_id(self, value: Optional[PositiveInteger]) -> None:
        """
        Set maxRptEventId with validation.

        Args:
            value: The maxRptEventId to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxRptEventId = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"maxRptEventId must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._maxRptEventId = value
        # if dedicated id range applied to the ExecutableEntitys of a software specific
        # ExecutableEntitys.
        self._minRptEventId: Optional[PositiveInteger] = None

    @property
    def min_rpt_event_id(self) -> Optional[PositiveInteger]:
        """Get minRptEventId (Pythonic accessor)."""
        return self._minRptEventId

    @min_rpt_event_id.setter
    def min_rpt_event_id(self, value: Optional[PositiveInteger]) -> None:
        """
        Set minRptEventId with validation.

        Args:
            value: The minRptEventId to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._minRptEventId = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"minRptEventId must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._minRptEventId = value
        self._rptExecution: Optional["RptExecutionControl"] = None

    @property
    def rpt_execution(self) -> Optional["RptExecutionControl"]:
        """Get rptExecution (Pythonic accessor)."""
        return self._rptExecution

    @rpt_execution.setter
    def rpt_execution(self, value: Optional["RptExecutionControl"]) -> None:
        """
        Set rptExecution with validation.

        Args:
            value: The rptExecution to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rptExecution = None
            return

        if not isinstance(value, RptExecutionControl):
            raise TypeError(
                f"rptExecution must be RptExecutionControl or None, got {type(value).__name__}"
            )
        self._rptExecution = value
        self._rptServicePoint: Optional[RptServicePointEnum] = None

    @property
    def rpt_service_point(self) -> Optional[RptServicePointEnum]:
        """Get rptServicePoint (Pythonic accessor)."""
        return self._rptServicePoint

    @rpt_service_point.setter
    def rpt_service_point(self, value: Optional[RptServicePointEnum]) -> None:
        """
        Set rptServicePoint with validation.

        Args:
            value: The rptServicePoint to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rptServicePoint = None
            return

        if not isinstance(value, RptServicePointEnum):
            raise TypeError(
                f"rptServicePoint must be RptServicePointEnum or None, got {type(value).__name__}"
            )
        self._rptServicePoint = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMaxRptEventId(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for maxRptEventId.

        Returns:
            The maxRptEventId value

        Note:
            Delegates to max_rpt_event_id property (CODING_RULE_V2_00017)
        """
        return self.max_rpt_event_id  # Delegates to property

    def setMaxRptEventId(self, value: PositiveInteger) -> RptExecutableEntityProperties:
        """
        AUTOSAR-compliant setter for maxRptEventId with method chaining.

        Args:
            value: The maxRptEventId to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_rpt_event_id property setter (gets validation automatically)
        """
        self.max_rpt_event_id = value  # Delegates to property setter
        return self

    def getMinRptEventId(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for minRptEventId.

        Returns:
            The minRptEventId value

        Note:
            Delegates to min_rpt_event_id property (CODING_RULE_V2_00017)
        """
        return self.min_rpt_event_id  # Delegates to property

    def setMinRptEventId(self, value: PositiveInteger) -> RptExecutableEntityProperties:
        """
        AUTOSAR-compliant setter for minRptEventId with method chaining.

        Args:
            value: The minRptEventId to set

        Returns:
            self for method chaining

        Note:
            Delegates to min_rpt_event_id property setter (gets validation automatically)
        """
        self.min_rpt_event_id = value  # Delegates to property setter
        return self

    def getRptExecution(self) -> "RptExecutionControl":
        """
        AUTOSAR-compliant getter for rptExecution.

        Returns:
            The rptExecution value

        Note:
            Delegates to rpt_execution property (CODING_RULE_V2_00017)
        """
        return self.rpt_execution  # Delegates to property

    def setRptExecution(self, value: "RptExecutionControl") -> RptExecutableEntityProperties:
        """
        AUTOSAR-compliant setter for rptExecution with method chaining.

        Args:
            value: The rptExecution to set

        Returns:
            self for method chaining

        Note:
            Delegates to rpt_execution property setter (gets validation automatically)
        """
        self.rpt_execution = value  # Delegates to property setter
        return self

    def getRptServicePoint(self) -> RptServicePointEnum:
        """
        AUTOSAR-compliant getter for rptServicePoint.

        Returns:
            The rptServicePoint value

        Note:
            Delegates to rpt_service_point property (CODING_RULE_V2_00017)
        """
        return self.rpt_service_point  # Delegates to property

    def setRptServicePoint(self, value: RptServicePointEnum) -> RptExecutableEntityProperties:
        """
        AUTOSAR-compliant setter for rptServicePoint with method chaining.

        Args:
            value: The rptServicePoint to set

        Returns:
            self for method chaining

        Note:
            Delegates to rpt_service_point property setter (gets validation automatically)
        """
        self.rpt_service_point = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_max_rpt_event_id(self, value: Optional[PositiveInteger]) -> RptExecutableEntityProperties:
        """
        Set maxRptEventId and return self for chaining.

        Args:
            value: The maxRptEventId to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_rpt_event_id("value")
        """
        self.max_rpt_event_id = value  # Use property setter (gets validation)
        return self

    def with_min_rpt_event_id(self, value: Optional[PositiveInteger]) -> RptExecutableEntityProperties:
        """
        Set minRptEventId and return self for chaining.

        Args:
            value: The minRptEventId to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_min_rpt_event_id("value")
        """
        self.min_rpt_event_id = value  # Use property setter (gets validation)
        return self

    def with_rpt_execution(self, value: Optional["RptExecutionControl"]) -> RptExecutableEntityProperties:
        """
        Set rptExecution and return self for chaining.

        Args:
            value: The rptExecution to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_rpt_execution("value")
        """
        self.rpt_execution = value  # Use property setter (gets validation)
        return self

    def with_rpt_service_point(self, value: Optional[RptServicePointEnum]) -> RptExecutableEntityProperties:
        """
        Set rptServicePoint and return self for chaining.

        Args:
            value: The rptServicePoint to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_rpt_service_point("value")
        """
        self.rpt_service_point = value  # Use property setter (gets validation)
        return self



class RapidPrototypingScenario(ARElement):
    """
    This meta-class provides the ability to describe a Rapid Prototyping
    Scenario. Such a Rapid Prototyping Scenario consist out of two main aspects,
    the description of the byPassPoints and the relation to an rpt Hook.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::RPTScenario::RapidPrototypingScenario

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 327, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 846, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # System which describes the software components of the.
        self._hostSystem: Optional["System"] = None

    @property
    def host_system(self) -> Optional["System"]:
        """Get hostSystem (Pythonic accessor)."""
        return self._hostSystem

    @host_system.setter
    def host_system(self, value: Optional["System"]) -> None:
        """
        Set hostSystem with validation.

        Args:
            value: The hostSystem to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._hostSystem = None
            return

        if not isinstance(value, System):
            raise TypeError(
                f"hostSystem must be System or None, got {type(value).__name__}"
            )
        self._hostSystem = value
        self._rptContainer: List[RptContainer] = []

    @property
    def rpt_container(self) -> List[RptContainer]:
        """Get rptContainer (Pythonic accessor)."""
        return self._rptContainer
        # Defiens the applicable Rapid Prototyping profils which are the smbol of the
                # service functions and id range.
        # The order of the RptProfiles determines of the service function invocation by
                # RTE.
        self._rptProfile: List[RptProfile] = []

    @property
    def rpt_profile(self) -> List[RptProfile]:
        """Get rptProfile (Pythonic accessor)."""
        return self._rptProfile
        # System which describes the rapid prototyping algorithm in of AUTOSAR Software
        # Components.
        self._rptSystem: Optional["System"] = None

    @property
    def rpt_system(self) -> Optional["System"]:
        """Get rptSystem (Pythonic accessor)."""
        return self._rptSystem

    @rpt_system.setter
    def rpt_system(self, value: Optional["System"]) -> None:
        """
        Set rptSystem with validation.

        Args:
            value: The rptSystem to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rptSystem = None
            return

        if not isinstance(value, System):
            raise TypeError(
                f"rptSystem must be System or None, got {type(value).__name__}"
            )
        self._rptSystem = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getHostSystem(self) -> "System":
        """
        AUTOSAR-compliant getter for hostSystem.

        Returns:
            The hostSystem value

        Note:
            Delegates to host_system property (CODING_RULE_V2_00017)
        """
        return self.host_system  # Delegates to property

    def setHostSystem(self, value: "System") -> RapidPrototypingScenario:
        """
        AUTOSAR-compliant setter for hostSystem with method chaining.

        Args:
            value: The hostSystem to set

        Returns:
            self for method chaining

        Note:
            Delegates to host_system property setter (gets validation automatically)
        """
        self.host_system = value  # Delegates to property setter
        return self

    def getRptContainer(self) -> List[RptContainer]:
        """
        AUTOSAR-compliant getter for rptContainer.

        Returns:
            The rptContainer value

        Note:
            Delegates to rpt_container property (CODING_RULE_V2_00017)
        """
        return self.rpt_container  # Delegates to property

    def getRptProfile(self) -> List[RptProfile]:
        """
        AUTOSAR-compliant getter for rptProfile.

        Returns:
            The rptProfile value

        Note:
            Delegates to rpt_profile property (CODING_RULE_V2_00017)
        """
        return self.rpt_profile  # Delegates to property

    def getRptSystem(self) -> "System":
        """
        AUTOSAR-compliant getter for rptSystem.

        Returns:
            The rptSystem value

        Note:
            Delegates to rpt_system property (CODING_RULE_V2_00017)
        """
        return self.rpt_system  # Delegates to property

    def setRptSystem(self, value: "System") -> RapidPrototypingScenario:
        """
        AUTOSAR-compliant setter for rptSystem with method chaining.

        Args:
            value: The rptSystem to set

        Returns:
            self for method chaining

        Note:
            Delegates to rpt_system property setter (gets validation automatically)
        """
        self.rpt_system = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_host_system(self, value: Optional["System"]) -> RapidPrototypingScenario:
        """
        Set hostSystem and return self for chaining.

        Args:
            value: The hostSystem to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_host_system("value")
        """
        self.host_system = value  # Use property setter (gets validation)
        return self

    def with_rpt_system(self, value: Optional["System"]) -> RapidPrototypingScenario:
        """
        Set rptSystem and return self for chaining.

        Args:
            value: The rptSystem to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_rpt_system("value")
        """
        self.rpt_system = value  # Use property setter (gets validation)
        return self



class IdentCaption(Identifiable, ABC):
    """
    This meta-class represents the caption. This allows having some meta-classes
    optionally identifiable.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::RPTScenario::IdentCaption

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 317, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 851, Classic Platform
      R23-11)
    """
    def __init__(self):
        if type(self) is IdentCaption:
            raise TypeError("IdentCaption is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class RptContainer(Identifiable):
    """
    This meta-class defines a byPassPoint and the relation to a rptHook.
    Additionally it may contain further rptContainers if the byPassPoint is not
    atomic. For example a byPass Point referencing to a RunnableEntity may
    contain rptContainers referring to the data access points of the
    RunnableEntity. The RptContainer structure on M1 shall follow the M1
    structure of the Software Component Descriptions. The category attribute
    denotes which level of the Software Component Description is annotated.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::RPTScenario::RptContainer

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 847, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # At a byPassPoint the host ECU shall be communicate with a RPT System in order
                # to execution of the rapid prototyping algorithms original data calculated by
                # the host system and to results of the host system by the the rapid
                # prototyping algorithm.
        # atpVariation by: AnyInstanceRef.
        self._byPassPoint: List[AtpFeature] = []

    @property
    def by_pass_point(self) -> List[AtpFeature]:
        """Get byPassPoint (Pythonic accessor)."""
        return self._byPassPoint
        # This attribute defines the applicable RptProfiles for the RptContainer.
        # If not any references to a specific defined, all RptProfiles defined in the
                # Rapid applicable.
        self._explicitRpt: List[RptProfile] = []

    @property
    def explicit_rpt(self) -> List[RptProfile]:
        """Get explicitRpt (Pythonic accessor)."""
        return self._explicitRpt
        # Sub-level rptContainer definitions of this specific rapid atpVariation.
        self._rptContainer: List[RptContainer] = []

    @property
    def rpt_container(self) -> List[RptContainer]:
        """Get rptContainer (Pythonic accessor)."""
        return self._rptContainer
        # Describes the required code preparation for rapid prototyping at
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
                # algorithm.
        # atpVariation.
        self._rptHook: Optional[RptHook] = None

    @property
    def rpt_hook(self) -> Optional[RptHook]:
        """Get rptHook (Pythonic accessor)."""
        return self._rptHook

    @rpt_hook.setter
    def rpt_hook(self, value: Optional[RptHook]) -> None:
        """
        Set rptHook with validation.

        Args:
            value: The rptHook to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rptHook = None
            return

        if not isinstance(value, RptHook):
            raise TypeError(
                f"rptHook must be RptHook or None, got {type(value).__name__}"
            )
        self._rptHook = value
        self._rptImplPolicy: Optional[RptImplPolicy] = None

    @property
    def rpt_impl_policy(self) -> Optional[RptImplPolicy]:
        """Get rptImplPolicy (Pythonic accessor)."""
        return self._rptImplPolicy

    @rpt_impl_policy.setter
    def rpt_impl_policy(self, value: Optional[RptImplPolicy]) -> None:
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
        # prototyping tooling.
        self._rptSw: Optional["RptSwPrototyping"] = None

    @property
    def rpt_sw(self) -> Optional["RptSwPrototyping"]:
        """Get rptSw (Pythonic accessor)."""
        return self._rptSw

    @rpt_sw.setter
    def rpt_sw(self, value: Optional["RptSwPrototyping"]) -> None:
        """
        Set rptSw with validation.

        Args:
            value: The rptSw to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rptSw = None
            return

        if not isinstance(value, RptSwPrototyping):
            raise TypeError(
                f"rptSw must be RptSwPrototyping or None, got {type(value).__name__}"
            )
        self._rptSw = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getByPassPoint(self) -> List[AtpFeature]:
        """
        AUTOSAR-compliant getter for byPassPoint.

        Returns:
            The byPassPoint value

        Note:
            Delegates to by_pass_point property (CODING_RULE_V2_00017)
        """
        return self.by_pass_point  # Delegates to property

    def getExplicitRpt(self) -> List[RptProfile]:
        """
        AUTOSAR-compliant getter for explicitRpt.

        Returns:
            The explicitRpt value

        Note:
            Delegates to explicit_rpt property (CODING_RULE_V2_00017)
        """
        return self.explicit_rpt  # Delegates to property

    def getRptContainer(self) -> List[RptContainer]:
        """
        AUTOSAR-compliant getter for rptContainer.

        Returns:
            The rptContainer value

        Note:
            Delegates to rpt_container property (CODING_RULE_V2_00017)
        """
        return self.rpt_container  # Delegates to property

    def getRptExecutable(self) -> "RptExecutableEntity":
        """
        AUTOSAR-compliant getter for rptExecutable.

        Returns:
            The rptExecutable value

        Note:
            Delegates to rpt_executable property (CODING_RULE_V2_00017)
        """
        return self.rpt_executable  # Delegates to property

    def setRptExecutable(self, value: "RptExecutableEntity") -> RptContainer:
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

    def getRptHook(self) -> RptHook:
        """
        AUTOSAR-compliant getter for rptHook.

        Returns:
            The rptHook value

        Note:
            Delegates to rpt_hook property (CODING_RULE_V2_00017)
        """
        return self.rpt_hook  # Delegates to property

    def setRptHook(self, value: RptHook) -> RptContainer:
        """
        AUTOSAR-compliant setter for rptHook with method chaining.

        Args:
            value: The rptHook to set

        Returns:
            self for method chaining

        Note:
            Delegates to rpt_hook property setter (gets validation automatically)
        """
        self.rpt_hook = value  # Delegates to property setter
        return self

    def getRptImplPolicy(self) -> RptImplPolicy:
        """
        AUTOSAR-compliant getter for rptImplPolicy.

        Returns:
            The rptImplPolicy value

        Note:
            Delegates to rpt_impl_policy property (CODING_RULE_V2_00017)
        """
        return self.rpt_impl_policy  # Delegates to property

    def setRptImplPolicy(self, value: RptImplPolicy) -> RptContainer:
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

    def getRptSw(self) -> "RptSwPrototyping":
        """
        AUTOSAR-compliant getter for rptSw.

        Returns:
            The rptSw value

        Note:
            Delegates to rpt_sw property (CODING_RULE_V2_00017)
        """
        return self.rpt_sw  # Delegates to property

    def setRptSw(self, value: "RptSwPrototyping") -> RptContainer:
        """
        AUTOSAR-compliant setter for rptSw with method chaining.

        Args:
            value: The rptSw to set

        Returns:
            self for method chaining

        Note:
            Delegates to rpt_sw property setter (gets validation automatically)
        """
        self.rpt_sw = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_rpt_executable(self, value: Optional["RptExecutableEntity"]) -> RptContainer:
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

    def with_rpt_hook(self, value: Optional[RptHook]) -> RptContainer:
        """
        Set rptHook and return self for chaining.

        Args:
            value: The rptHook to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_rpt_hook("value")
        """
        self.rpt_hook = value  # Use property setter (gets validation)
        return self

    def with_rpt_impl_policy(self, value: Optional[RptImplPolicy]) -> RptContainer:
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

    def with_rpt_sw(self, value: Optional["RptSwPrototyping"]) -> RptContainer:
        """
        Set rptSw and return self for chaining.

        Args:
            value: The rptSw to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_rpt_sw("value")
        """
        self.rpt_sw = value  # Use property setter (gets validation)
        return self



class RptHook(ARObject):
    """
    This meta-class provide the ability to describe a rapid prototyping hook.
    This can either be described by an other AUTOSAR system with the category
    RPT_SYSTEM or as a non AUTOSAR software.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::RPTScenario::RptHook

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 848, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute provides a code label which is used in the the hook.
        # For example this can be an C or the name of data definition.
        self._codeLabel: Optional[CIdentifier] = None

    @property
    def code_label(self) -> Optional[CIdentifier]:
        """Get codeLabel (Pythonic accessor)."""
        return self._codeLabel

    @code_label.setter
    def code_label(self, value: Optional[CIdentifier]) -> None:
        """
        Set codeLabel with validation.

        Args:
            value: The codeLabel to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._codeLabel = None
            return

        if not isinstance(value, CIdentifier):
            raise TypeError(
                f"codeLabel must be CIdentifier or None, got {type(value).__name__}"
            )
        self._codeLabel = value
        # display the Rpt Hook.
        self._mcdIdentifier: Optional["NameToken"] = None

    @property
    def mcd_identifier(self) -> Optional["NameToken"]:
        """Get mcdIdentifier (Pythonic accessor)."""
        return self._mcdIdentifier

    @mcd_identifier.setter
    def mcd_identifier(self, value: Optional["NameToken"]) -> None:
        """
        Set mcdIdentifier with validation.

        Args:
            value: The mcdIdentifier to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._mcdIdentifier = None
            return

        if not isinstance(value, (NameToken, str)):
            raise TypeError(
                f"mcdIdentifier must be NameToken or str or None, got {type(value).__name__}"
            )
        self._mcdIdentifier = value
        self._rptArHook: Optional[AtpFeature] = None

    @property
    def rpt_ar_hook(self) -> Optional[AtpFeature]:
        """Get rptArHook (Pythonic accessor)."""
        return self._rptArHook

    @rpt_ar_hook.setter
    def rpt_ar_hook(self, value: Optional[AtpFeature]) -> None:
        """
        Set rptArHook with validation.

        Args:
            value: The rptArHook to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rptArHook = None
            return

        if not isinstance(value, AtpFeature):
            raise TypeError(
                f"rptArHook must be AtpFeature or None, got {type(value).__name__}"
            )
        self._rptArHook = value
        # It can be utilized to tool specific data.
        self._sdg: List["Sdg"] = []

    @property
    def sdg(self) -> List["Sdg"]:
        """Get sdg (Pythonic accessor)."""
        return self._sdg

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCodeLabel(self) -> CIdentifier:
        """
        AUTOSAR-compliant getter for codeLabel.

        Returns:
            The codeLabel value

        Note:
            Delegates to code_label property (CODING_RULE_V2_00017)
        """
        return self.code_label  # Delegates to property

    def setCodeLabel(self, value: CIdentifier) -> RptHook:
        """
        AUTOSAR-compliant setter for codeLabel with method chaining.

        Args:
            value: The codeLabel to set

        Returns:
            self for method chaining

        Note:
            Delegates to code_label property setter (gets validation automatically)
        """
        self.code_label = value  # Delegates to property setter
        return self

    def getMcdIdentifier(self) -> "NameToken":
        """
        AUTOSAR-compliant getter for mcdIdentifier.

        Returns:
            The mcdIdentifier value

        Note:
            Delegates to mcd_identifier property (CODING_RULE_V2_00017)
        """
        return self.mcd_identifier  # Delegates to property

    def setMcdIdentifier(self, value: "NameToken") -> RptHook:
        """
        AUTOSAR-compliant setter for mcdIdentifier with method chaining.

        Args:
            value: The mcdIdentifier to set

        Returns:
            self for method chaining

        Note:
            Delegates to mcd_identifier property setter (gets validation automatically)
        """
        self.mcd_identifier = value  # Delegates to property setter
        return self

    def getRptArHook(self) -> AtpFeature:
        """
        AUTOSAR-compliant getter for rptArHook.

        Returns:
            The rptArHook value

        Note:
            Delegates to rpt_ar_hook property (CODING_RULE_V2_00017)
        """
        return self.rpt_ar_hook  # Delegates to property

    def setRptArHook(self, value: AtpFeature) -> RptHook:
        """
        AUTOSAR-compliant setter for rptArHook with method chaining.

        Args:
            value: The rptArHook to set

        Returns:
            self for method chaining

        Note:
            Delegates to rpt_ar_hook property setter (gets validation automatically)
        """
        self.rpt_ar_hook = value  # Delegates to property setter
        return self

    def getSdg(self) -> List["Sdg"]:
        """
        AUTOSAR-compliant getter for sdg.

        Returns:
            The sdg value

        Note:
            Delegates to sdg property (CODING_RULE_V2_00017)
        """
        return self.sdg  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_code_label(self, value: Optional[CIdentifier]) -> RptHook:
        """
        Set codeLabel and return self for chaining.

        Args:
            value: The codeLabel to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_code_label("value")
        """
        self.code_label = value  # Use property setter (gets validation)
        return self

    def with_mcd_identifier(self, value: Optional["NameToken"]) -> RptHook:
        """
        Set mcdIdentifier and return self for chaining.

        Args:
            value: The mcdIdentifier to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_mcd_identifier("value")
        """
        self.mcd_identifier = value  # Use property setter (gets validation)
        return self

    def with_rpt_ar_hook(self, value: Optional[AtpFeature]) -> RptHook:
        """
        Set rptArHook and return self for chaining.

        Args:
            value: The rptArHook to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_rpt_ar_hook("value")
        """
        self.rpt_ar_hook = value  # Use property setter (gets validation)
        return self



class RptProfile(Identifiable):
    """
    The RptProfile describes the common properties of a Rapid Prototyping
    method.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::RPTScenario::RptProfile

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 853, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Highest service point id useable for RTE generated points.
        self._maxService: Optional[PositiveInteger] = None

    @property
    def max_service(self) -> Optional[PositiveInteger]:
        """Get maxService (Pythonic accessor)."""
        return self._maxService

    @max_service.setter
    def max_service(self, value: Optional[PositiveInteger]) -> None:
        """
        Set maxService with validation.

        Args:
            value: The maxService to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxService = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"maxService must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._maxService = value
        self._minServicePoint: Optional[PositiveInteger] = None

    @property
    def min_service_point(self) -> Optional[PositiveInteger]:
        """Get minServicePoint (Pythonic accessor)."""
        return self._minServicePoint

    @min_service_point.setter
    def min_service_point(self, value: Optional[PositiveInteger]) -> None:
        """
        Set minServicePoint with validation.

        Args:
            value: The minServicePoint to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._minServicePoint = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"minServicePoint must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._minServicePoint = value
        # This symbol is used for post-build hooking 1228 Document ID 62:
                # AUTOSAR_CP_TPS_SoftwareComponentTemplate Template R23-11.
        self._servicePoint: Optional[CIdentifier] = None

    @property
    def service_point(self) -> Optional[CIdentifier]:
        """Get servicePoint (Pythonic accessor)."""
        return self._servicePoint

    @service_point.setter
    def service_point(self, value: Optional[CIdentifier]) -> None:
        """
        Set servicePoint with validation.

        Args:
            value: The servicePoint to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._servicePoint = None
            return

        if not isinstance(value, CIdentifier):
            raise TypeError(
                f"servicePoint must be CIdentifier or None, got {type(value).__name__}"
            )
        self._servicePoint = value
        # stimEnabler is "none" then no is passed to the service function.
        # stimulation enabler will be passed as a.
        self._stimEnabler: Optional["RptEnablerImplType"] = None

    @property
    def stim_enabler(self) -> Optional["RptEnablerImplType"]:
        """Get stimEnabler (Pythonic accessor)."""
        return self._stimEnabler

    @stim_enabler.setter
    def stim_enabler(self, value: Optional["RptEnablerImplType"]) -> None:
        """
        Set stimEnabler with validation.

        Args:
            value: The stimEnabler to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._stimEnabler = None
            return

        if not isinstance(value, RptEnablerImplType):
            raise TypeError(
                f"stimEnabler must be RptEnablerImplType or None, got {type(value).__name__}"
            )
        self._stimEnabler = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMaxService(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for maxService.

        Returns:
            The maxService value

        Note:
            Delegates to max_service property (CODING_RULE_V2_00017)
        """
        return self.max_service  # Delegates to property

    def setMaxService(self, value: PositiveInteger) -> RptProfile:
        """
        AUTOSAR-compliant setter for maxService with method chaining.

        Args:
            value: The maxService to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_service property setter (gets validation automatically)
        """
        self.max_service = value  # Delegates to property setter
        return self

    def getMinServicePoint(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for minServicePoint.

        Returns:
            The minServicePoint value

        Note:
            Delegates to min_service_point property (CODING_RULE_V2_00017)
        """
        return self.min_service_point  # Delegates to property

    def setMinServicePoint(self, value: PositiveInteger) -> RptProfile:
        """
        AUTOSAR-compliant setter for minServicePoint with method chaining.

        Args:
            value: The minServicePoint to set

        Returns:
            self for method chaining

        Note:
            Delegates to min_service_point property setter (gets validation automatically)
        """
        self.min_service_point = value  # Delegates to property setter
        return self

    def getServicePoint(self) -> CIdentifier:
        """
        AUTOSAR-compliant getter for servicePoint.

        Returns:
            The servicePoint value

        Note:
            Delegates to service_point property (CODING_RULE_V2_00017)
        """
        return self.service_point  # Delegates to property

    def setServicePoint(self, value: CIdentifier) -> RptProfile:
        """
        AUTOSAR-compliant setter for servicePoint with method chaining.

        Args:
            value: The servicePoint to set

        Returns:
            self for method chaining

        Note:
            Delegates to service_point property setter (gets validation automatically)
        """
        self.service_point = value  # Delegates to property setter
        return self

    def getStimEnabler(self) -> "RptEnablerImplType":
        """
        AUTOSAR-compliant getter for stimEnabler.

        Returns:
            The stimEnabler value

        Note:
            Delegates to stim_enabler property (CODING_RULE_V2_00017)
        """
        return self.stim_enabler  # Delegates to property

    def setStimEnabler(self, value: "RptEnablerImplType") -> RptProfile:
        """
        AUTOSAR-compliant setter for stimEnabler with method chaining.

        Args:
            value: The stimEnabler to set

        Returns:
            self for method chaining

        Note:
            Delegates to stim_enabler property setter (gets validation automatically)
        """
        self.stim_enabler = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_max_service(self, value: Optional[PositiveInteger]) -> RptProfile:
        """
        Set maxService and return self for chaining.

        Args:
            value: The maxService to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_service("value")
        """
        self.max_service = value  # Use property setter (gets validation)
        return self

    def with_min_service_point(self, value: Optional[PositiveInteger]) -> RptProfile:
        """
        Set minServicePoint and return self for chaining.

        Args:
            value: The minServicePoint to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_min_service_point("value")
        """
        self.min_service_point = value  # Use property setter (gets validation)
        return self

    def with_service_point(self, value: Optional[CIdentifier]) -> RptProfile:
        """
        Set servicePoint and return self for chaining.

        Args:
            value: The servicePoint to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_service_point("value")
        """
        self.service_point = value  # Use property setter (gets validation)
        return self

    def with_stim_enabler(self, value: Optional["RptEnablerImplType"]) -> RptProfile:
        """
        Set stimEnabler and return self for chaining.

        Args:
            value: The stimEnabler to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_stim_enabler("value")
        """
        self.stim_enabler = value  # Use property setter (gets validation)
        return self



class ModeAccessPointIdent(IdentCaption):
    """
    This meta-class has been created to introduce the ability to become
    referenced into the meta-class Mode AccessPoint without breaking backwards
    compatibility.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::RPTScenario::ModeAccessPointIdent

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 852, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class ExternalTriggeringPointIdent(IdentCaption):
    """
    This meta-class has been created to introduce the ability to become
    referenced into the meta-class ExternalTriggeringPoint without breaking
    backwards compatibility.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::RPTScenario::ExternalTriggeringPointIdent

    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 852, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====


class RptServicePointEnum(AREnum):
    """
    RptServicePointEnum enumeration

Specifies whether the invocation of ExecutableEntitys due to activation of specific RteEvents/Bsw Events requires the insertion of Service Points. Aggregated by RptExecutableEntityProperties.rptServicePoint

Package: M2::AUTOSARTemplates::SWComponentTemplate::RPTScenario
    """
    # Enables generation of service points by the RTE generator.
    enabled = "0"

    # No Service Points are requested.
    none = "1"

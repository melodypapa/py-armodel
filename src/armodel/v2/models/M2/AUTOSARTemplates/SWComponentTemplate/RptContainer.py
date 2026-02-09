from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class RptContainer(Identifiable):
    """
    This meta-class defines a byPassPoint and the relation to a rptHook.
    Additionally it may contain further rptContainers if the byPassPoint is not
    atomic. For example a byPass Point referencing to a RunnableEntity may
    contain rptContainers referring to the data access points of the
    RunnableEntity. The RptContainer structure on M1 shall follow the M1
    structure of the Software Component Descriptions. The category attribute
    denotes which level of the Software Component Description is annotated.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::RPTScenario

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
        self._byPassPoint: List["AtpFeature"] = []

    @property
    def by_pass_point(self) -> List["AtpFeature"]:
        """Get byPassPoint (Pythonic accessor)."""
        return self._byPassPoint
        # This attribute defines the applicable RptProfiles for the RptContainer.
        # If not any references to a specific defined, all RptProfiles defined in the
                # Rapid applicable.
        self._explicitRpt: List["RptProfile"] = []

    @property
    def explicit_rpt(self) -> List["RptProfile"]:
        """Get explicitRpt (Pythonic accessor)."""
        return self._explicitRpt
        # Sub-level rptContainer definitions of this specific rapid atpVariation.
        self._rptContainer: List["RptContainer"] = []

    @property
    def rpt_container(self) -> List["RptContainer"]:
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
        # The rptHook describes the link between a byPassPoint rapid prototyping
                # algorithm.
        # atpVariation.
        self._rptHook: Optional["RptHook"] = None

    @property
    def rpt_hook(self) -> Optional["RptHook"]:
        """Get rptHook (Pythonic accessor)."""
        return self._rptHook

    @rpt_hook.setter
    def rpt_hook(self, value: Optional["RptHook"]) -> None:
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
        # Describes the required code preparation for rapid data accesses.
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
        # Describes the required accessibility of data and modes by the rapid
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

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getByPassPoint(self) -> List["AtpFeature"]:
        """
        AUTOSAR-compliant getter for byPassPoint.

        Returns:
            The byPassPoint value

        Note:
            Delegates to by_pass_point property (CODING_RULE_V2_00017)
        """
        return self.by_pass_point  # Delegates to property

    def getExplicitRpt(self) -> List["RptProfile"]:
        """
        AUTOSAR-compliant getter for explicitRpt.

        Returns:
            The explicitRpt value

        Note:
            Delegates to explicit_rpt property (CODING_RULE_V2_00017)
        """
        return self.explicit_rpt  # Delegates to property

    def getRptContainer(self) -> List["RptContainer"]:
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

    def setRptExecutable(self, value: "RptExecutableEntity") -> "RptContainer":
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

    def getRptHook(self) -> "RptHook":
        """
        AUTOSAR-compliant getter for rptHook.

        Returns:
            The rptHook value

        Note:
            Delegates to rpt_hook property (CODING_RULE_V2_00017)
        """
        return self.rpt_hook  # Delegates to property

    def setRptHook(self, value: "RptHook") -> "RptContainer":
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

    def getRptImplPolicy(self) -> "RptImplPolicy":
        """
        AUTOSAR-compliant getter for rptImplPolicy.

        Returns:
            The rptImplPolicy value

        Note:
            Delegates to rpt_impl_policy property (CODING_RULE_V2_00017)
        """
        return self.rpt_impl_policy  # Delegates to property

    def setRptImplPolicy(self, value: "RptImplPolicy") -> "RptContainer":
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

    def setRptSw(self, value: "RptSwPrototyping") -> "RptContainer":
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

    def with_rpt_executable(self, value: Optional["RptExecutableEntity"]) -> "RptContainer":
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

    def with_rpt_hook(self, value: Optional["RptHook"]) -> "RptContainer":
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

    def with_rpt_impl_policy(self, value: Optional["RptImplPolicy"]) -> "RptContainer":
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

    def with_rpt_sw(self, value: Optional["RptSwPrototyping"]) -> "RptContainer":
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

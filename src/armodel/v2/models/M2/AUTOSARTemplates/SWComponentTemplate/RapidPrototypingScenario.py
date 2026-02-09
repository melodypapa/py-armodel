from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARElement,
)


class RapidPrototypingScenario(ARElement):
    """
    This meta-class provides the ability to describe a Rapid Prototyping
    Scenario. Such a Rapid Prototyping Scenario consist out of two main aspects,
    the description of the byPassPoints and the relation to an rpt Hook.

    Package: M2::AUTOSARTemplates::SWComponentTemplate::RPTScenario

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
        self._rptContainer: List["RptContainer"] = []

    @property
    def rpt_container(self) -> List["RptContainer"]:
        """Get rptContainer (Pythonic accessor)."""
        return self._rptContainer
        # Defiens the applicable Rapid Prototyping profils which are the smbol of the
                # service functions and id range.
        # The order of the RptProfiles determines of the service function invocation by
                # RTE.
        self._rptProfile: List["RptProfile"] = []

    @property
    def rpt_profile(self) -> List["RptProfile"]:
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

    def setHostSystem(self, value: "System") -> "RapidPrototypingScenario":
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

    def getRptContainer(self) -> List["RptContainer"]:
        """
        AUTOSAR-compliant getter for rptContainer.

        Returns:
            The rptContainer value

        Note:
            Delegates to rpt_container property (CODING_RULE_V2_00017)
        """
        return self.rpt_container  # Delegates to property

    def getRptProfile(self) -> List["RptProfile"]:
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

    def setRptSystem(self, value: "System") -> "RapidPrototypingScenario":
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

    def with_host_system(self, value: Optional["System"]) -> "RapidPrototypingScenario":
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

    def with_rpt_system(self, value: Optional["System"]) -> "RapidPrototypingScenario":
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

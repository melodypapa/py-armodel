from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class EcuResourceEstimation(ARObject):
    """
    Resource estimations for RTE and BSW of a single ECU instance.

    Package: M2::AUTOSARTemplates::SystemTemplate::SWmapping

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 260, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Estimation for the resource consumption of the basic.
        self._bswResource: Optional["ResourceConsumption"] = None

    @property
    def bsw_resource(self) -> Optional["ResourceConsumption"]:
        """Get bswResource (Pythonic accessor)."""
        return self._bswResource

    @bsw_resource.setter
    def bsw_resource(self, value: Optional["ResourceConsumption"]) -> None:
        """
        Set bswResource with validation.

        Args:
            value: The bswResource to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._bswResource = None
            return

        if not isinstance(value, ResourceConsumption):
            raise TypeError(
                f"bswResource must be ResourceConsumption or None, got {type(value).__name__}"
            )
        self._bswResource = value
        # Reference to the ECU this estimation is done for.
        self._ecuInstance: Optional["EcuInstance"] = None

    @property
    def ecu_instance(self) -> Optional["EcuInstance"]:
        """Get ecuInstance (Pythonic accessor)."""
        return self._ecuInstance

    @ecu_instance.setter
    def ecu_instance(self, value: Optional["EcuInstance"]) -> None:
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
        # This represents introductory documentation about the ecu.
        self._introduction: Optional["DocumentationBlock"] = None

    @property
    def introduction(self) -> Optional["DocumentationBlock"]:
        """Get introduction (Pythonic accessor)."""
        return self._introduction

    @introduction.setter
    def introduction(self, value: Optional["DocumentationBlock"]) -> None:
        """
        Set introduction with validation.

        Args:
            value: The introduction to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._introduction = None
            return

        if not isinstance(value, DocumentationBlock):
            raise TypeError(
                f"introduction must be DocumentationBlock or None, got {type(value).__name__}"
            )
        self._introduction = value
        # Estimation for the resource consumption of the run time.
        self._rteResource: Optional["ResourceConsumption"] = None

    @property
    def rte_resource(self) -> Optional["ResourceConsumption"]:
        """Get rteResource (Pythonic accessor)."""
        return self._rteResource

    @rte_resource.setter
    def rte_resource(self, value: Optional["ResourceConsumption"]) -> None:
        """
        Set rteResource with validation.

        Args:
            value: The rteResource to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rteResource = None
            return

        if not isinstance(value, ResourceConsumption):
            raise TypeError(
                f"rteResource must be ResourceConsumption or None, got {type(value).__name__}"
            )
        self._rteResource = value
        # References to SwcToEcuMappings that have been taken account for the resource
                # estimations.
        # This way it is define dfferent EcuResourceEstimations with e.
        # g.
        # before and after mapping an component.
        self._swCompToEcu: List[RefType] = []

    @property
    def sw_comp_to_ecu(self) -> List[RefType]:
        """Get swCompToEcu (Pythonic accessor)."""
        return self._swCompToEcu

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBswResource(self) -> "ResourceConsumption":
        """
        AUTOSAR-compliant getter for bswResource.

        Returns:
            The bswResource value

        Note:
            Delegates to bsw_resource property (CODING_RULE_V2_00017)
        """
        return self.bsw_resource  # Delegates to property

    def setBswResource(self, value: "ResourceConsumption") -> "EcuResourceEstimation":
        """
        AUTOSAR-compliant setter for bswResource with method chaining.

        Args:
            value: The bswResource to set

        Returns:
            self for method chaining

        Note:
            Delegates to bsw_resource property setter (gets validation automatically)
        """
        self.bsw_resource = value  # Delegates to property setter
        return self

    def getEcuInstance(self) -> "EcuInstance":
        """
        AUTOSAR-compliant getter for ecuInstance.

        Returns:
            The ecuInstance value

        Note:
            Delegates to ecu_instance property (CODING_RULE_V2_00017)
        """
        return self.ecu_instance  # Delegates to property

    def setEcuInstance(self, value: "EcuInstance") -> "EcuResourceEstimation":
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

    def getIntroduction(self) -> "DocumentationBlock":
        """
        AUTOSAR-compliant getter for introduction.

        Returns:
            The introduction value

        Note:
            Delegates to introduction property (CODING_RULE_V2_00017)
        """
        return self.introduction  # Delegates to property

    def setIntroduction(self, value: "DocumentationBlock") -> "EcuResourceEstimation":
        """
        AUTOSAR-compliant setter for introduction with method chaining.

        Args:
            value: The introduction to set

        Returns:
            self for method chaining

        Note:
            Delegates to introduction property setter (gets validation automatically)
        """
        self.introduction = value  # Delegates to property setter
        return self

    def getRteResource(self) -> "ResourceConsumption":
        """
        AUTOSAR-compliant getter for rteResource.

        Returns:
            The rteResource value

        Note:
            Delegates to rte_resource property (CODING_RULE_V2_00017)
        """
        return self.rte_resource  # Delegates to property

    def setRteResource(self, value: "ResourceConsumption") -> "EcuResourceEstimation":
        """
        AUTOSAR-compliant setter for rteResource with method chaining.

        Args:
            value: The rteResource to set

        Returns:
            self for method chaining

        Note:
            Delegates to rte_resource property setter (gets validation automatically)
        """
        self.rte_resource = value  # Delegates to property setter
        return self

    def getSwCompToEcu(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for swCompToEcu.

        Returns:
            The swCompToEcu value

        Note:
            Delegates to sw_comp_to_ecu property (CODING_RULE_V2_00017)
        """
        return self.sw_comp_to_ecu  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_bsw_resource(self, value: Optional["ResourceConsumption"]) -> "EcuResourceEstimation":
        """
        Set bswResource and return self for chaining.

        Args:
            value: The bswResource to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_bsw_resource("value")
        """
        self.bsw_resource = value  # Use property setter (gets validation)
        return self

    def with_ecu_instance(self, value: Optional["EcuInstance"]) -> "EcuResourceEstimation":
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

    def with_introduction(self, value: Optional["DocumentationBlock"]) -> "EcuResourceEstimation":
        """
        Set introduction and return self for chaining.

        Args:
            value: The introduction to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_introduction("value")
        """
        self.introduction = value  # Use property setter (gets validation)
        return self

    def with_rte_resource(self, value: Optional["ResourceConsumption"]) -> "EcuResourceEstimation":
        """
        Set rteResource and return self for chaining.

        Args:
            value: The rteResource to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_rte_resource("value")
        """
        self.rte_resource = value  # Use property setter (gets validation)
        return self

from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class DoIpConfig(ARObject):
    """
    This element defines the DoIp configuration for a specific Ecu.

    Package: M2::AUTOSARTemplates::SystemTemplate::DoIP

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 551, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # DoIP node consists of one or several DoIPInterfaces over ECU is able to
        # communicate via DoIP DoIP functionalities on each IP isolated from each
        # other.
        self._doipInterface: List["DoIpInterface"] = []

    @property
    def doip_interface(self) -> List["DoIpInterface"]:
        """Get doipInterface (Pythonic accessor)."""
        return self._doipInterface
        # Describes the logical address of the DoIP entity, i.
        # e.
        # the that will route diagnostic requests to the the DoIP entity.
        self._logicAddress: Optional["DoIpLogicAddress"] = None

    @property
    def logic_address(self) -> Optional["DoIpLogicAddress"]:
        """Get logicAddress (Pythonic accessor)."""
        return self._logicAddress

    @logic_address.setter
    def logic_address(self, value: Optional["DoIpLogicAddress"]) -> None:
        """
        Set logicAddress with validation.

        Args:
            value: The logicAddress to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._logicAddress = None
            return

        if not isinstance(value, DoIpLogicAddress):
            raise TypeError(
                f"logicAddress must be DoIpLogicAddress or None, got {type(value).__name__}"
            )
        self._logicAddress = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDoipInterface(self) -> List["DoIpInterface"]:
        """
        AUTOSAR-compliant getter for doipInterface.

        Returns:
            The doipInterface value

        Note:
            Delegates to doip_interface property (CODING_RULE_V2_00017)
        """
        return self.doip_interface  # Delegates to property

    def getLogicAddress(self) -> "DoIpLogicAddress":
        """
        AUTOSAR-compliant getter for logicAddress.

        Returns:
            The logicAddress value

        Note:
            Delegates to logic_address property (CODING_RULE_V2_00017)
        """
        return self.logic_address  # Delegates to property

    def setLogicAddress(self, value: "DoIpLogicAddress") -> "DoIpConfig":
        """
        AUTOSAR-compliant setter for logicAddress with method chaining.

        Args:
            value: The logicAddress to set

        Returns:
            self for method chaining

        Note:
            Delegates to logic_address property setter (gets validation automatically)
        """
        self.logic_address = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_logic_address(self, value: Optional["DoIpLogicAddress"]) -> "DoIpConfig":
        """
        Set logicAddress and return self for chaining.

        Args:
            value: The logicAddress to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_logic_address("value")
        """
        self.logic_address = value  # Use property setter (gets validation)
        return self

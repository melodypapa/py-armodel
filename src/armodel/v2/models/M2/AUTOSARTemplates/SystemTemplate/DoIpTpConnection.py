from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection import TpConnection

    RefType,
)


class DoIpTpConnection(TpConnection):
    """
    A connection identifies the sender and the receiver of this particular
    communication. The DoIp module routes a tpSdu through this connection.

    Package: M2::AUTOSARTemplates::SystemTemplate::DiagnosticConnection::DoIpTpConnection

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 555, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to the address of the sender of the tpSdu.
        self._doIpSource: Optional["DoIpLogicAddress"] = None

    @property
    def do_ip_source(self) -> Optional["DoIpLogicAddress"]:
        """Get doIpSource (Pythonic accessor)."""
        return self._doIpSource

    @do_ip_source.setter
    def do_ip_source(self, value: Optional["DoIpLogicAddress"]) -> None:
        """
        Set doIpSource with validation.

        Args:
            value: The doIpSource to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._doIpSource = None
            return

        if not isinstance(value, DoIpLogicAddress):
            raise TypeError(
                f"doIpSource must be DoIpLogicAddress or None, got {type(value).__name__}"
            )
        self._doIpSource = value
        # Reference to the address of the receiver of the tpSdu.
        self._doIpTarget: Optional["DoIpLogicAddress"] = None

    @property
    def do_ip_target(self) -> Optional["DoIpLogicAddress"]:
        """Get doIpTarget (Pythonic accessor)."""
        return self._doIpTarget

    @do_ip_target.setter
    def do_ip_target(self, value: Optional["DoIpLogicAddress"]) -> None:
        """
        Set doIpTarget with validation.

        Args:
            value: The doIpTarget to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._doIpTarget = None
            return

        if not isinstance(value, DoIpLogicAddress):
            raise TypeError(
                f"doIpTarget must be DoIpLogicAddress or None, got {type(value).__name__}"
            )
        self._doIpTarget = value
        # This reference is used to describe the data exchange and the PduR.
        self._tpSdu: RefType = None

    @property
    def tp_sdu(self) -> RefType:
        """Get tpSdu (Pythonic accessor)."""
        return self._tpSdu

    @tp_sdu.setter
    def tp_sdu(self, value: RefType) -> None:
        """
        Set tpSdu with validation.

        Args:
            value: The tpSdu to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tpSdu = None
            return

        self._tpSdu = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDoIpSource(self) -> "DoIpLogicAddress":
        """
        AUTOSAR-compliant getter for doIpSource.

        Returns:
            The doIpSource value

        Note:
            Delegates to do_ip_source property (CODING_RULE_V2_00017)
        """
        return self.do_ip_source  # Delegates to property

    def setDoIpSource(self, value: "DoIpLogicAddress") -> "DoIpTpConnection":
        """
        AUTOSAR-compliant setter for doIpSource with method chaining.

        Args:
            value: The doIpSource to set

        Returns:
            self for method chaining

        Note:
            Delegates to do_ip_source property setter (gets validation automatically)
        """
        self.do_ip_source = value  # Delegates to property setter
        return self

    def getDoIpTarget(self) -> "DoIpLogicAddress":
        """
        AUTOSAR-compliant getter for doIpTarget.

        Returns:
            The doIpTarget value

        Note:
            Delegates to do_ip_target property (CODING_RULE_V2_00017)
        """
        return self.do_ip_target  # Delegates to property

    def setDoIpTarget(self, value: "DoIpLogicAddress") -> "DoIpTpConnection":
        """
        AUTOSAR-compliant setter for doIpTarget with method chaining.

        Args:
            value: The doIpTarget to set

        Returns:
            self for method chaining

        Note:
            Delegates to do_ip_target property setter (gets validation automatically)
        """
        self.do_ip_target = value  # Delegates to property setter
        return self

    def getTpSdu(self) -> RefType:
        """
        AUTOSAR-compliant getter for tpSdu.

        Returns:
            The tpSdu value

        Note:
            Delegates to tp_sdu property (CODING_RULE_V2_00017)
        """
        return self.tp_sdu  # Delegates to property

    def setTpSdu(self, value: RefType) -> "DoIpTpConnection":
        """
        AUTOSAR-compliant setter for tpSdu with method chaining.

        Args:
            value: The tpSdu to set

        Returns:
            self for method chaining

        Note:
            Delegates to tp_sdu property setter (gets validation automatically)
        """
        self.tp_sdu = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_do_ip_source(self, value: Optional["DoIpLogicAddress"]) -> "DoIpTpConnection":
        """
        Set doIpSource and return self for chaining.

        Args:
            value: The doIpSource to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_do_ip_source("value")
        """
        self.do_ip_source = value  # Use property setter (gets validation)
        return self

    def with_do_ip_target(self, value: Optional["DoIpLogicAddress"]) -> "DoIpTpConnection":
        """
        Set doIpTarget and return self for chaining.

        Args:
            value: The doIpTarget to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_do_ip_target("value")
        """
        self.do_ip_target = value  # Use property setter (gets validation)
        return self

    def with_tp_sdu(self, value: Optional[RefType]) -> "DoIpTpConnection":
        """
        Set tpSdu and return self for chaining.

        Args:
            value: The tpSdu to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tp_sdu("value")
        """
        self.tp_sdu = value  # Use property setter (gets validation)
        return self

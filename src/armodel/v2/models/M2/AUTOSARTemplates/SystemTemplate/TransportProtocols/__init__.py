"""
AUTOSAR Package - TransportProtocols

Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols
"""


from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
    Boolean,
    Integer,
    PositiveInteger,
    RefType,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection import (
    TpConnection,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.__init__ import (
    FibexElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.__init__ import (
    TpConfig,
)


class DoIpLogicAddress(Identifiable):
    """
    The logical DoIP address.

    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::DoIpLogicAddress

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 555, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The logical DoIP address.
        self._address: Optional[Integer] = None

    @property
    def address(self) -> Optional[Integer]:
        """Get address (Pythonic accessor)."""
        return self._address

    @address.setter
    def address(self, value: Optional[Integer]) -> None:
        """
        Set address with validation.

        Args:
            value: The address to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._address = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"address must be Integer or int or None, got {type(value).__name__}"
            )
        self._address = value
        # Collection of additional LogicAddress properties.
        self._doIpLogic: Optional[AbstractDoIpLogic] = None

    @property
    def do_ip_logic(self) -> Optional[AbstractDoIpLogic]:
        """Get doIpLogic (Pythonic accessor)."""
        return self._doIpLogic

    @do_ip_logic.setter
    def do_ip_logic(self, value: Optional[AbstractDoIpLogic]) -> None:
        """
        Set doIpLogic with validation.

        Args:
            value: The doIpLogic to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._doIpLogic = None
            return

        if not isinstance(value, AbstractDoIpLogic):
            raise TypeError(
                f"doIpLogic must be AbstractDoIpLogic or None, got {type(value).__name__}"
            )
        self._doIpLogic = value

    def with_receiver(self, value):
        """
        Set receiver and return self for chaining.

        Args:
            value: The receiver to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_receiver("value")
        """
        self.receiver = value  # Use property setter (gets validation)
        return self

    def with_n_pdu(self, value):
        """
        Set n_pdu and return self for chaining.

        Args:
            value: The n_pdu to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_n_pdu("value")
        """
        self.n_pdu = value  # Use property setter (gets validation)
        return self

    def with_n_pdu(self, value):
        """
        Set n_pdu and return self for chaining.

        Args:
            value: The n_pdu to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_n_pdu("value")
        """
        self.n_pdu = value  # Use property setter (gets validation)
        return self

    def with_target(self, value):
        """
        Set target and return self for chaining.

        Args:
            value: The target to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_target("value")
        """
        self.target = value  # Use property setter (gets validation)
        return self

    def with_receiver(self, value):
        """
        Set receiver and return self for chaining.

        Args:
            value: The receiver to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_receiver("value")
        """
        self.receiver = value  # Use property setter (gets validation)
        return self

    def with_receiver(self, value):
        """
        Set receiver and return self for chaining.

        Args:
            value: The receiver to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_receiver("value")
        """
        self.receiver = value  # Use property setter (gets validation)
        return self

    def with_receiver(self, value):
        """
        Set receiver and return self for chaining.

        Args:
            value: The receiver to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_receiver("value")
        """
        self.receiver = value  # Use property setter (gets validation)
        return self

    def with_tp_pg(self, value):
        """
        Set tp_pg and return self for chaining.

        Args:
            value: The tp_pg to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tp_pg("value")
        """
        self.tp_pg = value  # Use property setter (gets validation)
        return self

    def with_sdu(self, value):
        """
        Set sdu and return self for chaining.

        Args:
            value: The sdu to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sdu("value")
        """
        self.sdu = value  # Use property setter (gets validation)
        return self

    def with_do_ip_logic_address(self, value):
        """
        Set do_ip_logic_address and return self for chaining.

        Args:
            value: The do_ip_logic_address to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_do_ip_logic_address("value")
        """
        self.do_ip_logic_address = value  # Use property setter (gets validation)
        return self

    def with_pdu_pool(self, value):
        """
        Set pdu_pool and return self for chaining.

        Args:
            value: The pdu_pool to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_pdu_pool("value")
        """
        self.pdu_pool = value  # Use property setter (gets validation)
        return self

    def with_tp_ecu(self, value):
        """
        Set tp_ecu and return self for chaining.

        Args:
            value: The tp_ecu to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tp_ecu("value")
        """
        self.tp_ecu = value  # Use property setter (gets validation)
        return self

    def with_tp_node(self, value):
        """
        Set tp_node and return self for chaining.

        Args:
            value: The tp_node to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tp_node("value")
        """
        self.tp_node = value  # Use property setter (gets validation)
        return self

    def with_tp_node(self, value):
        """
        Set tp_node and return self for chaining.

        Args:
            value: The tp_node to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tp_node("value")
        """
        self.tp_node = value  # Use property setter (gets validation)
        return self

    def with_tp_ecu(self, value):
        """
        Set tp_ecu and return self for chaining.

        Args:
            value: The tp_ecu to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tp_ecu("value")
        """
        self.tp_ecu = value  # Use property setter (gets validation)
        return self

    def with_tp_node(self, value):
        """
        Set tp_node and return self for chaining.

        Args:
            value: The tp_node to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tp_node("value")
        """
        self.tp_node = value  # Use property setter (gets validation)
        return self

    def with_tp_node(self, value):
        """
        Set tp_node and return self for chaining.

        Args:
            value: The tp_node to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tp_node("value")
        """
        self.tp_node = value  # Use property setter (gets validation)
        return self

    def with_tp_node(self, value):
        """
        Set tp_node and return self for chaining.

        Args:
            value: The tp_node to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tp_node("value")
        """
        self.tp_node = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAddress(self) -> Integer:
        """
        AUTOSAR-compliant getter for address.

        Returns:
            The address value

        Note:
            Delegates to address property (CODING_RULE_V2_00017)
        """
        return self.address  # Delegates to property

    def setAddress(self, value: Integer) -> DoIpLogicAddress:
        """
        AUTOSAR-compliant setter for address with method chaining.

        Args:
            value: The address to set

        Returns:
            self for method chaining

        Note:
            Delegates to address property setter (gets validation automatically)
        """
        self.address = value  # Delegates to property setter
        return self

    def getDoIpLogic(self) -> AbstractDoIpLogic:
        """
        AUTOSAR-compliant getter for doIpLogic.

        Returns:
            The doIpLogic value

        Note:
            Delegates to do_ip_logic property (CODING_RULE_V2_00017)
        """
        return self.do_ip_logic  # Delegates to property

    def setDoIpLogic(self, value: AbstractDoIpLogic) -> DoIpLogicAddress:
        """
        AUTOSAR-compliant setter for doIpLogic with method chaining.

        Args:
            value: The doIpLogic to set

        Returns:
            self for method chaining

        Note:
            Delegates to do_ip_logic property setter (gets validation automatically)
        """
        self.do_ip_logic = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_address(self, value: Optional[Integer]) -> DoIpLogicAddress:
        """
        Set address and return self for chaining.

        Args:
            value: The address to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_address("value")
        """
        self.address = value  # Use property setter (gets validation)
        return self

    def with_do_ip_logic(self, value: Optional[AbstractDoIpLogic]) -> DoIpLogicAddress:
        """
        Set doIpLogic and return self for chaining.

        Args:
            value: The doIpLogic to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_do_ip_logic("value")
        """
        self.do_ip_logic = value  # Use property setter (gets validation)
        return self



class TpConfig(FibexElement, ABC):
    """
    Contains all configuration elements for AUTOSAR TP.

    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::TpConfig

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 587, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is TpConfig:
            raise TypeError("TpConfig is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # A TpConfig is existing always in the context of exactly one.
        self._communication: Optional["CommunicationCluster"] = None

    @property
    def communication(self) -> Optional["CommunicationCluster"]:
        """Get communication (Pythonic accessor)."""
        return self._communication

    @communication.setter
    def communication(self, value: Optional["CommunicationCluster"]) -> None:
        """
        Set communication with validation.

        Args:
            value: The communication to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._communication = None
            return

        if not isinstance(value, CommunicationCluster):
            raise TypeError(
                f"communication must be CommunicationCluster or None, got {type(value).__name__}"
            )
        self._communication = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCommunication(self) -> "CommunicationCluster":
        """
        AUTOSAR-compliant getter for communication.

        Returns:
            The communication value

        Note:
            Delegates to communication property (CODING_RULE_V2_00017)
        """
        return self.communication  # Delegates to property

    def setCommunication(self, value: "CommunicationCluster") -> TpConfig:
        """
        AUTOSAR-compliant setter for communication with method chaining.

        Args:
            value: The communication to set

        Returns:
            self for method chaining

        Note:
            Delegates to communication property setter (gets validation automatically)
        """
        self.communication = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_communication(self, value: Optional["CommunicationCluster"]) -> TpConfig:
        """
        Set communication and return self for chaining.

        Args:
            value: The communication to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_communication("value")
        """
        self.communication = value  # Use property setter (gets validation)
        return self



class TpAddress(Identifiable):
    """
    An ECUs TP address on the referenced channel. This represents the diagnostic
    Address.

    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::TpAddress

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 588, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # An ECUs TP address on the referenced channel.
        # This diagnostic Address.
        self._tpAddress: Optional[Integer] = None

    @property
    def tp_address(self) -> Optional[Integer]:
        """Get tpAddress (Pythonic accessor)."""
        return self._tpAddress

    @tp_address.setter
    def tp_address(self, value: Optional[Integer]) -> None:
        """
        Set tpAddress with validation.

        Args:
            value: The tpAddress to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tpAddress = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"tpAddress must be Integer or int or None, got {type(value).__name__}"
            )
        self._tpAddress = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTpAddress(self) -> Integer:
        """
        AUTOSAR-compliant getter for tpAddress.

        Returns:
            The tpAddress value

        Note:
            Delegates to tp_address property (CODING_RULE_V2_00017)
        """
        return self.tp_address  # Delegates to property

    def setTpAddress(self, value: Integer) -> TpAddress:
        """
        AUTOSAR-compliant setter for tpAddress with method chaining.

        Args:
            value: The tpAddress to set

        Returns:
            self for method chaining

        Note:
            Delegates to tp_address property setter (gets validation automatically)
        """
        self.tp_address = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_tp_address(self, value: Optional[Integer]) -> TpAddress:
        """
        Set tpAddress and return self for chaining.

        Args:
            value: The tpAddress to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tp_address("value")
        """
        self.tp_address = value  # Use property setter (gets validation)
        return self



class FlexrayTpConnectionControl(Identifiable):
    """
    Configuration parameters to control a FlexRay TP connection.

    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::FlexrayTpConnectionControl

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 593, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This parameter defines the type of acknowledgement used for the specific
        # channel.
        self._ackType: Optional["TpAckType"] = None

    @property
    def ack_type(self) -> Optional["TpAckType"]:
        """Get ackType (Pythonic accessor)."""
        return self._ackType

    @ack_type.setter
    def ack_type(self, value: Optional["TpAckType"]) -> None:
        """
        Set ackType with validation.

        Args:
            value: The ackType to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ackType = None
            return

        if not isinstance(value, TpAckType):
            raise TypeError(
                f"ackType must be TpAckType or None, got {type(value).__name__}"
            )
        self._ackType = value
        # This attribute defines the maximum number of Flow with FlowState "WAIT".
        self._maxFcWait: Optional[Integer] = None

    @property
    def max_fc_wait(self) -> Optional[Integer]:
        """Get maxFcWait (Pythonic accessor)."""
        return self._maxFcWait

    @max_fc_wait.setter
    def max_fc_wait(self, value: Optional[Integer]) -> None:
        """
        Set maxFcWait with validation.

        Args:
            value: The maxFcWait to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxFcWait = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"maxFcWait must be Integer or int or None, got {type(value).__name__}"
            )
        self._maxFcWait = value
        # This parameter limits the number of N-Pdus the sender is to transmit within a
        # FlexRay cycle.
        self._maxNumberOf: Optional[Integer] = None

    @property
    def max_number_of(self) -> Optional[Integer]:
        """Get maxNumberOf (Pythonic accessor)."""
        return self._maxNumberOf

    @max_number_of.setter
    def max_number_of(self, value: Optional[Integer]) -> None:
        """
        Set maxNumberOf with validation.

        Args:
            value: The maxNumberOf to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxNumberOf = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"maxNumberOf must be Integer or int or None, got {type(value).__name__}"
            )
        self._maxNumberOf = value
        # This parameter defines the maximum number of retries (if configured for the
        # particular channel).
        self._maxRetries: Optional[Integer] = None

    @property
    def max_retries(self) -> Optional[Integer]:
        """Get maxRetries (Pythonic accessor)."""
        return self._maxRetries

    @max_retries.setter
    def max_retries(self, value: Optional[Integer]) -> None:
        """
        Set maxRetries with validation.

        Args:
            value: The maxRetries to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxRetries = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"maxRetries must be Integer or int or None, got {type(value).__name__}"
            )
        self._maxRetries = value
        # Exponent to calculate the minimum number of Cycles" the sender has to wait
        # for the next an FrTp N-Pdu.
        self._separationCycle: Optional[Integer] = None

    @property
    def separation_cycle(self) -> Optional[Integer]:
        """Get separationCycle (Pythonic accessor)."""
        return self._separationCycle

    @separation_cycle.setter
    def separation_cycle(self, value: Optional[Integer]) -> None:
        """
        Set separationCycle with validation.

        Args:
            value: The separationCycle to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._separationCycle = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"separationCycle must be Integer or int or None, got {type(value).__name__}"
            )
        self._separationCycle = value
        # Time (in seconds) until transmission of the next Flow.
        self._timeBr: Optional[TimeValue] = None

    @property
    def time_br(self) -> Optional[TimeValue]:
        """Get timeBr (Pythonic accessor)."""
        return self._timeBr

    @time_br.setter
    def time_br(self, value: Optional[TimeValue]) -> None:
        """
        Set timeBr with validation.

        Args:
            value: The timeBr to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeBr = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"timeBr must be TimeValue or None, got {type(value).__name__}"
            )
        self._timeBr = value
        # This parameter defines the time of waiting for the next try a Tx or Rx
                # buffer.
        # is equivalent to the temporal distance FC.
        # WT N-Pdus in case the buffer request seconds.
        self._timeBuffer: Optional[TimeValue] = None

    @property
    def time_buffer(self) -> Optional[TimeValue]:
        """Get timeBuffer (Pythonic accessor)."""
        return self._timeBuffer

    @time_buffer.setter
    def time_buffer(self, value: Optional[TimeValue]) -> None:
        """
        Set timeBuffer with validation.

        Args:
            value: The timeBuffer to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeBuffer = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"timeBuffer must be TimeValue or None, got {type(value).__name__}"
            )
        self._timeBuffer = value
        # Time (in seconds) until transmission of the next / LastFrame NPdu.
        self._timeCs: Optional[TimeValue] = None

    @property
    def time_cs(self) -> Optional[TimeValue]:
        """Get timeCs (Pythonic accessor)."""
        return self._timeCs

    @time_cs.setter
    def time_cs(self, value: Optional[TimeValue]) -> None:
        """
        Set timeCs with validation.

        Args:
            value: The timeCs to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeCs = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"timeCs must be TimeValue or None, got {type(value).__name__}"
            )
        self._timeCs = value
        # This parameter states the timeout between the PDU of the Transport Layer to
                # the FlexRay the corresponding confirmation of the Flex on the receiver side
                # (for FC or AF).
        # seconds.
        self._timeoutAr: Optional[TimeValue] = None

    @property
    def timeout_ar(self) -> Optional[TimeValue]:
        """Get timeoutAr (Pythonic accessor)."""
        return self._timeoutAr

    @timeout_ar.setter
    def timeout_ar(self, value: Optional[TimeValue]) -> None:
        """
        Set timeoutAr with validation.

        Args:
            value: The timeoutAr to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeoutAr = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"timeoutAr must be TimeValue or None, got {type(value).__name__}"
            )
        self._timeoutAr = value
        # This attribute states the timeout between the PDU for the first PDU of the
                # group used in the of the Transport Layer to the FlexRay the corresponding
                # confirmation of the Flex (when having sent the last PDU of the in this
                # connection) on the sender side (SF-x, or FC (in case of Transmit
                # Cancellation)).
        # seconds.
        self._timeoutAs: Optional[TimeValue] = None

    @property
    def timeout_as(self) -> Optional[TimeValue]:
        """Get timeoutAs (Pythonic accessor)."""
        return self._timeoutAs

    @timeout_as.setter
    def timeout_as(self, value: Optional[TimeValue]) -> None:
        """
        Set timeoutAs with validation.

        Args:
            value: The timeoutAs to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeoutAs = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"timeoutAs must be TimeValue or None, got {type(value).__name__}"
            )
        self._timeoutAs = value
        # This parameter defines the timeout in seconds for waiting FC or AF on the
        # sender side in a 1:1 connection.
        self._timeoutBs: Optional[TimeValue] = None

    @property
    def timeout_bs(self) -> Optional[TimeValue]:
        """Get timeoutBs (Pythonic accessor)."""
        return self._timeoutBs

    @timeout_bs.setter
    def timeout_bs(self, value: Optional[TimeValue]) -> None:
        """
        Set timeoutBs with validation.

        Args:
            value: The timeoutBs to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeoutBs = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"timeoutBs must be TimeValue or None, got {type(value).__name__}"
            )
        self._timeoutBs = value
        # This parameter defines the timeout value in seconds for a CF or FF-x (in case
        # of retry) after receiving CF or after sending an FC or AF on the receiver in
        # seconds.
        self._timeoutCr: Optional[TimeValue] = None

    @property
    def timeout_cr(self) -> Optional[TimeValue]:
        """Get timeoutCr (Pythonic accessor)."""
        return self._timeoutCr

    @timeout_cr.setter
    def timeout_cr(self, value: Optional[TimeValue]) -> None:
        """
        Set timeoutCr with validation.

        Args:
            value: The timeoutCr to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeoutCr = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"timeoutCr must be TimeValue or None, got {type(value).__name__}"
            )
        self._timeoutCr = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAckType(self) -> "TpAckType":
        """
        AUTOSAR-compliant getter for ackType.

        Returns:
            The ackType value

        Note:
            Delegates to ack_type property (CODING_RULE_V2_00017)
        """
        return self.ack_type  # Delegates to property

    def setAckType(self, value: "TpAckType") -> FlexrayTpConnectionControl:
        """
        AUTOSAR-compliant setter for ackType with method chaining.

        Args:
            value: The ackType to set

        Returns:
            self for method chaining

        Note:
            Delegates to ack_type property setter (gets validation automatically)
        """
        self.ack_type = value  # Delegates to property setter
        return self

    def getMaxFcWait(self) -> Integer:
        """
        AUTOSAR-compliant getter for maxFcWait.

        Returns:
            The maxFcWait value

        Note:
            Delegates to max_fc_wait property (CODING_RULE_V2_00017)
        """
        return self.max_fc_wait  # Delegates to property

    def setMaxFcWait(self, value: Integer) -> FlexrayTpConnectionControl:
        """
        AUTOSAR-compliant setter for maxFcWait with method chaining.

        Args:
            value: The maxFcWait to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_fc_wait property setter (gets validation automatically)
        """
        self.max_fc_wait = value  # Delegates to property setter
        return self

    def getMaxNumberOf(self) -> Integer:
        """
        AUTOSAR-compliant getter for maxNumberOf.

        Returns:
            The maxNumberOf value

        Note:
            Delegates to max_number_of property (CODING_RULE_V2_00017)
        """
        return self.max_number_of  # Delegates to property

    def setMaxNumberOf(self, value: Integer) -> FlexrayTpConnectionControl:
        """
        AUTOSAR-compliant setter for maxNumberOf with method chaining.

        Args:
            value: The maxNumberOf to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_number_of property setter (gets validation automatically)
        """
        self.max_number_of = value  # Delegates to property setter
        return self

    def getMaxRetries(self) -> Integer:
        """
        AUTOSAR-compliant getter for maxRetries.

        Returns:
            The maxRetries value

        Note:
            Delegates to max_retries property (CODING_RULE_V2_00017)
        """
        return self.max_retries  # Delegates to property

    def setMaxRetries(self, value: Integer) -> FlexrayTpConnectionControl:
        """
        AUTOSAR-compliant setter for maxRetries with method chaining.

        Args:
            value: The maxRetries to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_retries property setter (gets validation automatically)
        """
        self.max_retries = value  # Delegates to property setter
        return self

    def getSeparationCycle(self) -> Integer:
        """
        AUTOSAR-compliant getter for separationCycle.

        Returns:
            The separationCycle value

        Note:
            Delegates to separation_cycle property (CODING_RULE_V2_00017)
        """
        return self.separation_cycle  # Delegates to property

    def setSeparationCycle(self, value: Integer) -> FlexrayTpConnectionControl:
        """
        AUTOSAR-compliant setter for separationCycle with method chaining.

        Args:
            value: The separationCycle to set

        Returns:
            self for method chaining

        Note:
            Delegates to separation_cycle property setter (gets validation automatically)
        """
        self.separation_cycle = value  # Delegates to property setter
        return self

    def getTimeBr(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for timeBr.

        Returns:
            The timeBr value

        Note:
            Delegates to time_br property (CODING_RULE_V2_00017)
        """
        return self.time_br  # Delegates to property

    def setTimeBr(self, value: TimeValue) -> FlexrayTpConnectionControl:
        """
        AUTOSAR-compliant setter for timeBr with method chaining.

        Args:
            value: The timeBr to set

        Returns:
            self for method chaining

        Note:
            Delegates to time_br property setter (gets validation automatically)
        """
        self.time_br = value  # Delegates to property setter
        return self

    def getTimeBuffer(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for timeBuffer.

        Returns:
            The timeBuffer value

        Note:
            Delegates to time_buffer property (CODING_RULE_V2_00017)
        """
        return self.time_buffer  # Delegates to property

    def setTimeBuffer(self, value: TimeValue) -> FlexrayTpConnectionControl:
        """
        AUTOSAR-compliant setter for timeBuffer with method chaining.

        Args:
            value: The timeBuffer to set

        Returns:
            self for method chaining

        Note:
            Delegates to time_buffer property setter (gets validation automatically)
        """
        self.time_buffer = value  # Delegates to property setter
        return self

    def getTimeCs(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for timeCs.

        Returns:
            The timeCs value

        Note:
            Delegates to time_cs property (CODING_RULE_V2_00017)
        """
        return self.time_cs  # Delegates to property

    def setTimeCs(self, value: TimeValue) -> FlexrayTpConnectionControl:
        """
        AUTOSAR-compliant setter for timeCs with method chaining.

        Args:
            value: The timeCs to set

        Returns:
            self for method chaining

        Note:
            Delegates to time_cs property setter (gets validation automatically)
        """
        self.time_cs = value  # Delegates to property setter
        return self

    def getTimeoutAr(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for timeoutAr.

        Returns:
            The timeoutAr value

        Note:
            Delegates to timeout_ar property (CODING_RULE_V2_00017)
        """
        return self.timeout_ar  # Delegates to property

    def setTimeoutAr(self, value: TimeValue) -> FlexrayTpConnectionControl:
        """
        AUTOSAR-compliant setter for timeoutAr with method chaining.

        Args:
            value: The timeoutAr to set

        Returns:
            self for method chaining

        Note:
            Delegates to timeout_ar property setter (gets validation automatically)
        """
        self.timeout_ar = value  # Delegates to property setter
        return self

    def getTimeoutAs(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for timeoutAs.

        Returns:
            The timeoutAs value

        Note:
            Delegates to timeout_as property (CODING_RULE_V2_00017)
        """
        return self.timeout_as  # Delegates to property

    def setTimeoutAs(self, value: TimeValue) -> FlexrayTpConnectionControl:
        """
        AUTOSAR-compliant setter for timeoutAs with method chaining.

        Args:
            value: The timeoutAs to set

        Returns:
            self for method chaining

        Note:
            Delegates to timeout_as property setter (gets validation automatically)
        """
        self.timeout_as = value  # Delegates to property setter
        return self

    def getTimeoutBs(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for timeoutBs.

        Returns:
            The timeoutBs value

        Note:
            Delegates to timeout_bs property (CODING_RULE_V2_00017)
        """
        return self.timeout_bs  # Delegates to property

    def setTimeoutBs(self, value: TimeValue) -> FlexrayTpConnectionControl:
        """
        AUTOSAR-compliant setter for timeoutBs with method chaining.

        Args:
            value: The timeoutBs to set

        Returns:
            self for method chaining

        Note:
            Delegates to timeout_bs property setter (gets validation automatically)
        """
        self.timeout_bs = value  # Delegates to property setter
        return self

    def getTimeoutCr(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for timeoutCr.

        Returns:
            The timeoutCr value

        Note:
            Delegates to timeout_cr property (CODING_RULE_V2_00017)
        """
        return self.timeout_cr  # Delegates to property

    def setTimeoutCr(self, value: TimeValue) -> FlexrayTpConnectionControl:
        """
        AUTOSAR-compliant setter for timeoutCr with method chaining.

        Args:
            value: The timeoutCr to set

        Returns:
            self for method chaining

        Note:
            Delegates to timeout_cr property setter (gets validation automatically)
        """
        self.timeout_cr = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_ack_type(self, value: Optional["TpAckType"]) -> FlexrayTpConnectionControl:
        """
        Set ackType and return self for chaining.

        Args:
            value: The ackType to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ack_type("value")
        """
        self.ack_type = value  # Use property setter (gets validation)
        return self

    def with_max_fc_wait(self, value: Optional[Integer]) -> FlexrayTpConnectionControl:
        """
        Set maxFcWait and return self for chaining.

        Args:
            value: The maxFcWait to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_fc_wait("value")
        """
        self.max_fc_wait = value  # Use property setter (gets validation)
        return self

    def with_max_number_of(self, value: Optional[Integer]) -> FlexrayTpConnectionControl:
        """
        Set maxNumberOf and return self for chaining.

        Args:
            value: The maxNumberOf to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_number_of("value")
        """
        self.max_number_of = value  # Use property setter (gets validation)
        return self

    def with_max_retries(self, value: Optional[Integer]) -> FlexrayTpConnectionControl:
        """
        Set maxRetries and return self for chaining.

        Args:
            value: The maxRetries to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_retries("value")
        """
        self.max_retries = value  # Use property setter (gets validation)
        return self

    def with_separation_cycle(self, value: Optional[Integer]) -> FlexrayTpConnectionControl:
        """
        Set separationCycle and return self for chaining.

        Args:
            value: The separationCycle to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_separation_cycle("value")
        """
        self.separation_cycle = value  # Use property setter (gets validation)
        return self

    def with_time_br(self, value: Optional[TimeValue]) -> FlexrayTpConnectionControl:
        """
        Set timeBr and return self for chaining.

        Args:
            value: The timeBr to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_time_br("value")
        """
        self.time_br = value  # Use property setter (gets validation)
        return self

    def with_time_buffer(self, value: Optional[TimeValue]) -> FlexrayTpConnectionControl:
        """
        Set timeBuffer and return self for chaining.

        Args:
            value: The timeBuffer to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_time_buffer("value")
        """
        self.time_buffer = value  # Use property setter (gets validation)
        return self

    def with_time_cs(self, value: Optional[TimeValue]) -> FlexrayTpConnectionControl:
        """
        Set timeCs and return self for chaining.

        Args:
            value: The timeCs to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_time_cs("value")
        """
        self.time_cs = value  # Use property setter (gets validation)
        return self

    def with_timeout_ar(self, value: Optional[TimeValue]) -> FlexrayTpConnectionControl:
        """
        Set timeoutAr and return self for chaining.

        Args:
            value: The timeoutAr to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_timeout_ar("value")
        """
        self.timeout_ar = value  # Use property setter (gets validation)
        return self

    def with_timeout_as(self, value: Optional[TimeValue]) -> FlexrayTpConnectionControl:
        """
        Set timeoutAs and return self for chaining.

        Args:
            value: The timeoutAs to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_timeout_as("value")
        """
        self.timeout_as = value  # Use property setter (gets validation)
        return self

    def with_timeout_bs(self, value: Optional[TimeValue]) -> FlexrayTpConnectionControl:
        """
        Set timeoutBs and return self for chaining.

        Args:
            value: The timeoutBs to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_timeout_bs("value")
        """
        self.timeout_bs = value  # Use property setter (gets validation)
        return self

    def with_timeout_cr(self, value: Optional[TimeValue]) -> FlexrayTpConnectionControl:
        """
        Set timeoutCr and return self for chaining.

        Args:
            value: The timeoutCr to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_timeout_cr("value")
        """
        self.timeout_cr = value  # Use property setter (gets validation)
        return self



class FlexrayTpConnection(TpConnection):
    """
    A connection identifies the sender and the receiver of this particular
    communication. The FlexRayTp module routes a Pdu through this connection. In
    a System Description the references to the PduPools are mandatory. In an ECU
    Extract these references can be optional: On unicast connections these
    references are always mandatory. On multicast the txPduPool is mandatory on
    the sender side. The rxPduPool is mandatory on the receiver side. On Gateway
    ECUs both references are mandatory.

    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::FlexrayTpConnection

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 594, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specifies whether the connection requires a bandwidth or not.
        self._bandwidth: Optional[Boolean] = None

    @property
    def bandwidth(self) -> Optional[Boolean]:
        """Get bandwidth (Pythonic accessor)."""
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, value: Optional[Boolean]) -> None:
        """
        Set bandwidth with validation.

        Args:
            value: The bandwidth to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._bandwidth = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"bandwidth must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._bandwidth = value
        # Reference to the IPdu that is segmented by the Transport.
        self._directTpSdu: Optional[IPdu] = None

    @property
    def direct_tp_sdu(self) -> Optional[IPdu]:
        """Get directTpSdu (Pythonic accessor)."""
        return self._directTpSdu

    @direct_tp_sdu.setter
    def direct_tp_sdu(self, value: Optional[IPdu]) -> None:
        """
        Set directTpSdu with validation.

        Args:
            value: The directTpSdu to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._directTpSdu = None
            return

        if not isinstance(value, IPdu):
            raise TypeError(
                f"directTpSdu must be IPdu or None, got {type(value).__name__}"
            )
        self._directTpSdu = value
        # TP address for 1:n connections.
        self._multicast: Optional[TpAddress] = None

    @property
    def multicast(self) -> Optional[TpAddress]:
        """Get multicast (Pythonic accessor)."""
        return self._multicast

    @multicast.setter
    def multicast(self, value: Optional[TpAddress]) -> None:
        """
        Set multicast with validation.

        Args:
            value: The multicast to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._multicast = None
            return

        if not isinstance(value, TpAddress):
            raise TypeError(
                f"multicast must be TpAddress or None, got {type(value).__name__}"
            )
        self._multicast = value
        # The target of the TP connection.
        self._receiver: List[FlexrayTpNode] = []

    @property
    def receiver(self) -> List[FlexrayTpNode]:
        """Get receiver (Pythonic accessor)."""
        return self._receiver
        # Reference to the IPdu that is segmented by the Transport support of both
        # sending and receiving is used, references the IPdu used for the direction.
        self._reversedTpSdu: Optional[IPdu] = None

    @property
    def reversed_tp_sdu(self) -> Optional[IPdu]:
        """Get reversedTpSdu (Pythonic accessor)."""
        return self._reversedTpSdu

    @reversed_tp_sdu.setter
    def reversed_tp_sdu(self, value: Optional[IPdu]) -> None:
        """
        Set reversedTpSdu with validation.

        Args:
            value: The reversedTpSdu to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._reversedTpSdu = None
            return

        if not isinstance(value, IPdu):
            raise TypeError(
                f"reversedTpSdu must be IPdu or None, got {type(value).__name__}"
            )
        self._reversedTpSdu = value
        # A connection has a reference to a set of NPdus (FrTpRx are defined for
        # receiving data via this constraint is valid only for the System In case this
        # connection is applied to the rxPduPool holds the actually received case this
        # connection is applied to the receiver holds the actually sent NPdus.
        self._rxPduPool: Optional[FlexrayTpPduPool] = None

    @property
    def rx_pdu_pool(self) -> Optional[FlexrayTpPduPool]:
        """Get rxPduPool (Pythonic accessor)."""
        return self._rxPduPool

    @rx_pdu_pool.setter
    def rx_pdu_pool(self, value: Optional[FlexrayTpPduPool]) -> None:
        """
        Set rxPduPool with validation.

        Args:
            value: The rxPduPool to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rxPduPool = None
            return

        if not isinstance(value, FlexrayTpPduPool):
            raise TypeError(
                f"rxPduPool must be FlexrayTpPduPool or None, got {type(value).__name__}"
            )
        self._rxPduPool = value
        # Reference to the connection control.
        self._tpConnection: Optional[FlexrayTpConnection] = None

    @property
    def tp_connection(self) -> Optional[FlexrayTpConnection]:
        """Get tpConnection (Pythonic accessor)."""
        return self._tpConnection

    @tp_connection.setter
    def tp_connection(self, value: Optional[FlexrayTpConnection]) -> None:
        """
        Set tpConnection with validation.

        Args:
            value: The tpConnection to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tpConnection = None
            return

        if not isinstance(value, FlexrayTpConnection):
            raise TypeError(
                f"tpConnection must be FlexrayTpConnection or None, got {type(value).__name__}"
            )
        self._tpConnection = value
        # The source of the TP connection.
        self._transmitter: Optional[FlexrayTpNode] = None

    @property
    def transmitter(self) -> Optional[FlexrayTpNode]:
        """Get transmitter (Pythonic accessor)."""
        return self._transmitter

    @transmitter.setter
    def transmitter(self, value: Optional[FlexrayTpNode]) -> None:
        """
        Set transmitter with validation.

        Args:
            value: The transmitter to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._transmitter = None
            return

        if not isinstance(value, FlexrayTpNode):
            raise TypeError(
                f"transmitter must be FlexrayTpNode or None, got {type(value).__name__}"
            )
        self._transmitter = value
        # A connection has a reference to a set of NPdus (FrTpTx are defined for
        # sending data via this constraint is valid only for the System In case this
        # connection is applied to the txPduPool holds the actually sent case this
        # connection is applied to the receiver holds the actually received NPdus.
        self._txPduPool: Optional[FlexrayTpPduPool] = None

    @property
    def tx_pdu_pool(self) -> Optional[FlexrayTpPduPool]:
        """Get txPduPool (Pythonic accessor)."""
        return self._txPduPool

    @tx_pdu_pool.setter
    def tx_pdu_pool(self, value: Optional[FlexrayTpPduPool]) -> None:
        """
        Set txPduPool with validation.

        Args:
            value: The txPduPool to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._txPduPool = None
            return

        if not isinstance(value, FlexrayTpPduPool):
            raise TypeError(
                f"txPduPool must be FlexrayTpPduPool or None, got {type(value).__name__}"
            )
        self._txPduPool = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBandwidth(self) -> Boolean:
        """
        AUTOSAR-compliant getter for bandwidth.

        Returns:
            The bandwidth value

        Note:
            Delegates to bandwidth property (CODING_RULE_V2_00017)
        """
        return self.bandwidth  # Delegates to property

    def setBandwidth(self, value: Boolean) -> FlexrayTpConnection:
        """
        AUTOSAR-compliant setter for bandwidth with method chaining.

        Args:
            value: The bandwidth to set

        Returns:
            self for method chaining

        Note:
            Delegates to bandwidth property setter (gets validation automatically)
        """
        self.bandwidth = value  # Delegates to property setter
        return self

    def getDirectTpSdu(self) -> IPdu:
        """
        AUTOSAR-compliant getter for directTpSdu.

        Returns:
            The directTpSdu value

        Note:
            Delegates to direct_tp_sdu property (CODING_RULE_V2_00017)
        """
        return self.direct_tp_sdu  # Delegates to property

    def setDirectTpSdu(self, value: IPdu) -> FlexrayTpConnection:
        """
        AUTOSAR-compliant setter for directTpSdu with method chaining.

        Args:
            value: The directTpSdu to set

        Returns:
            self for method chaining

        Note:
            Delegates to direct_tp_sdu property setter (gets validation automatically)
        """
        self.direct_tp_sdu = value  # Delegates to property setter
        return self

    def getMulticast(self) -> TpAddress:
        """
        AUTOSAR-compliant getter for multicast.

        Returns:
            The multicast value

        Note:
            Delegates to multicast property (CODING_RULE_V2_00017)
        """
        return self.multicast  # Delegates to property

    def setMulticast(self, value: TpAddress) -> FlexrayTpConnection:
        """
        AUTOSAR-compliant setter for multicast with method chaining.

        Args:
            value: The multicast to set

        Returns:
            self for method chaining

        Note:
            Delegates to multicast property setter (gets validation automatically)
        """
        self.multicast = value  # Delegates to property setter
        return self

    def getReceiver(self) -> List[FlexrayTpNode]:
        """
        AUTOSAR-compliant getter for receiver.

        Returns:
            The receiver value

        Note:
            Delegates to receiver property (CODING_RULE_V2_00017)
        """
        return self.receiver  # Delegates to property

    def getReversedTpSdu(self) -> IPdu:
        """
        AUTOSAR-compliant getter for reversedTpSdu.

        Returns:
            The reversedTpSdu value

        Note:
            Delegates to reversed_tp_sdu property (CODING_RULE_V2_00017)
        """
        return self.reversed_tp_sdu  # Delegates to property

    def setReversedTpSdu(self, value: IPdu) -> FlexrayTpConnection:
        """
        AUTOSAR-compliant setter for reversedTpSdu with method chaining.

        Args:
            value: The reversedTpSdu to set

        Returns:
            self for method chaining

        Note:
            Delegates to reversed_tp_sdu property setter (gets validation automatically)
        """
        self.reversed_tp_sdu = value  # Delegates to property setter
        return self

    def getRxPduPool(self) -> FlexrayTpPduPool:
        """
        AUTOSAR-compliant getter for rxPduPool.

        Returns:
            The rxPduPool value

        Note:
            Delegates to rx_pdu_pool property (CODING_RULE_V2_00017)
        """
        return self.rx_pdu_pool  # Delegates to property

    def setRxPduPool(self, value: FlexrayTpPduPool) -> FlexrayTpConnection:
        """
        AUTOSAR-compliant setter for rxPduPool with method chaining.

        Args:
            value: The rxPduPool to set

        Returns:
            self for method chaining

        Note:
            Delegates to rx_pdu_pool property setter (gets validation automatically)
        """
        self.rx_pdu_pool = value  # Delegates to property setter
        return self

    def getTpConnection(self) -> FlexrayTpConnection:
        """
        AUTOSAR-compliant getter for tpConnection.

        Returns:
            The tpConnection value

        Note:
            Delegates to tp_connection property (CODING_RULE_V2_00017)
        """
        return self.tp_connection  # Delegates to property

    def setTpConnection(self, value: FlexrayTpConnection) -> FlexrayTpConnection:
        """
        AUTOSAR-compliant setter for tpConnection with method chaining.

        Args:
            value: The tpConnection to set

        Returns:
            self for method chaining

        Note:
            Delegates to tp_connection property setter (gets validation automatically)
        """
        self.tp_connection = value  # Delegates to property setter
        return self

    def getTransmitter(self) -> FlexrayTpNode:
        """
        AUTOSAR-compliant getter for transmitter.

        Returns:
            The transmitter value

        Note:
            Delegates to transmitter property (CODING_RULE_V2_00017)
        """
        return self.transmitter  # Delegates to property

    def setTransmitter(self, value: FlexrayTpNode) -> FlexrayTpConnection:
        """
        AUTOSAR-compliant setter for transmitter with method chaining.

        Args:
            value: The transmitter to set

        Returns:
            self for method chaining

        Note:
            Delegates to transmitter property setter (gets validation automatically)
        """
        self.transmitter = value  # Delegates to property setter
        return self

    def getTxPduPool(self) -> FlexrayTpPduPool:
        """
        AUTOSAR-compliant getter for txPduPool.

        Returns:
            The txPduPool value

        Note:
            Delegates to tx_pdu_pool property (CODING_RULE_V2_00017)
        """
        return self.tx_pdu_pool  # Delegates to property

    def setTxPduPool(self, value: FlexrayTpPduPool) -> FlexrayTpConnection:
        """
        AUTOSAR-compliant setter for txPduPool with method chaining.

        Args:
            value: The txPduPool to set

        Returns:
            self for method chaining

        Note:
            Delegates to tx_pdu_pool property setter (gets validation automatically)
        """
        self.tx_pdu_pool = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_bandwidth(self, value: Optional[Boolean]) -> FlexrayTpConnection:
        """
        Set bandwidth and return self for chaining.

        Args:
            value: The bandwidth to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_bandwidth("value")
        """
        self.bandwidth = value  # Use property setter (gets validation)
        return self

    def with_direct_tp_sdu(self, value: Optional[IPdu]) -> FlexrayTpConnection:
        """
        Set directTpSdu and return self for chaining.

        Args:
            value: The directTpSdu to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_direct_tp_sdu("value")
        """
        self.direct_tp_sdu = value  # Use property setter (gets validation)
        return self

    def with_multicast(self, value: Optional[TpAddress]) -> FlexrayTpConnection:
        """
        Set multicast and return self for chaining.

        Args:
            value: The multicast to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_multicast("value")
        """
        self.multicast = value  # Use property setter (gets validation)
        return self

    def with_reversed_tp_sdu(self, value: Optional[IPdu]) -> FlexrayTpConnection:
        """
        Set reversedTpSdu and return self for chaining.

        Args:
            value: The reversedTpSdu to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_reversed_tp_sdu("value")
        """
        self.reversed_tp_sdu = value  # Use property setter (gets validation)
        return self

    def with_rx_pdu_pool(self, value: Optional[FlexrayTpPduPool]) -> FlexrayTpConnection:
        """
        Set rxPduPool and return self for chaining.

        Args:
            value: The rxPduPool to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_rx_pdu_pool("value")
        """
        self.rx_pdu_pool = value  # Use property setter (gets validation)
        return self

    def with_tp_connection(self, value: Optional[FlexrayTpConnection]) -> FlexrayTpConnection:
        """
        Set tpConnection and return self for chaining.

        Args:
            value: The tpConnection to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tp_connection("value")
        """
        self.tp_connection = value  # Use property setter (gets validation)
        return self

    def with_transmitter(self, value: Optional[FlexrayTpNode]) -> FlexrayTpConnection:
        """
        Set transmitter and return self for chaining.

        Args:
            value: The transmitter to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_transmitter("value")
        """
        self.transmitter = value  # Use property setter (gets validation)
        return self

    def with_tx_pdu_pool(self, value: Optional[FlexrayTpPduPool]) -> FlexrayTpConnection:
        """
        Set txPduPool and return self for chaining.

        Args:
            value: The txPduPool to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tx_pdu_pool("value")
        """
        self.tx_pdu_pool = value  # Use property setter (gets validation)
        return self



class FlexrayTpPduPool(Identifiable):
    """
    FlexrayTpPduPool is a set of N-PDUs which are defined for FrTp sending or
    receiving purpose.

    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::FlexrayTpPduPool

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 596, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to NPdus that are part of the PduPool.
        self._nPdu: List["NPdu"] = []

    @property
    def n_pdu(self) -> List["NPdu"]:
        """Get nPdu (Pythonic accessor)."""
        return self._nPdu

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getNPdu(self) -> List["NPdu"]:
        """
        AUTOSAR-compliant getter for nPdu.

        Returns:
            The nPdu value

        Note:
            Delegates to n_pdu property (CODING_RULE_V2_00017)
        """
        return self.n_pdu  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class FlexrayTpNode(Identifiable):
    """
    TP Node (Sender or Receiver) provides the TP Address and the connection to
    the Topology description.

    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::FlexrayTpNode

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 596, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Association to one or more physical connectors (max of connectors for
                # FlexRay: 2).
        # System Description this reference is mandatory.
        # In Extract this reference is optional (references to are not part of the ECU
                # Extract shall be.
        self._connector: List[Communication] = []

    @property
    def connector(self) -> List[Communication]:
        """Get connector (Pythonic accessor)."""
        return self._connector
        # Reference to the TP Address that is used by the TpNode.
        # is optional in case that the multicast TP used (reference from TpConnection).
        self._tpAddress: Optional[TpAddress] = None

    @property
    def tp_address(self) -> Optional[TpAddress]:
        """Get tpAddress (Pythonic accessor)."""
        return self._tpAddress

    @tp_address.setter
    def tp_address(self, value: Optional[TpAddress]) -> None:
        """
        Set tpAddress with validation.

        Args:
            value: The tpAddress to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tpAddress = None
            return

        if not isinstance(value, TpAddress):
            raise TypeError(
                f"tpAddress must be TpAddress or None, got {type(value).__name__}"
            )
        self._tpAddress = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getConnector(self) -> List[Communication]:
        """
        AUTOSAR-compliant getter for connector.

        Returns:
            The connector value

        Note:
            Delegates to connector property (CODING_RULE_V2_00017)
        """
        return self.connector  # Delegates to property

    def getTpAddress(self) -> TpAddress:
        """
        AUTOSAR-compliant getter for tpAddress.

        Returns:
            The tpAddress value

        Note:
            Delegates to tp_address property (CODING_RULE_V2_00017)
        """
        return self.tp_address  # Delegates to property

    def setTpAddress(self, value: TpAddress) -> FlexrayTpNode:
        """
        AUTOSAR-compliant setter for tpAddress with method chaining.

        Args:
            value: The tpAddress to set

        Returns:
            self for method chaining

        Note:
            Delegates to tp_address property setter (gets validation automatically)
        """
        self.tp_address = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_tp_address(self, value: Optional[TpAddress]) -> FlexrayTpNode:
        """
        Set tpAddress and return self for chaining.

        Args:
            value: The tpAddress to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tp_address("value")
        """
        self.tp_address = value  # Use property setter (gets validation)
        return self



class FlexrayTpEcu(ARObject):
    """
    ECU specific TP configuration parameters. Each TpEcu element has a reference
    to exactly one ECUInstance in the topology.

    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::FlexrayTpEcu

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 596, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # With this switch Tx and Rx Cancellation can be turned on 2090 Document ID 63:
        # AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._cancellation: Optional[Boolean] = None

    @property
    def cancellation(self) -> Optional[Boolean]:
        """Get cancellation (Pythonic accessor)."""
        return self._cancellation

    @cancellation.setter
    def cancellation(self, value: Optional[Boolean]) -> None:
        """
        Set cancellation with validation.

        Args:
            value: The cancellation to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._cancellation = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"cancellation must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._cancellation = value
        # The period between successive calls to the Main Function the AUTOSAR TP.
        # Specified in seconds.
        self._cycleTimeMain: Optional[TimeValue] = None

    @property
    def cycle_time_main(self) -> Optional[TimeValue]:
        """Get cycleTimeMain (Pythonic accessor)."""
        return self._cycleTimeMain

    @cycle_time_main.setter
    def cycle_time_main(self, value: Optional[TimeValue]) -> None:
        """
        Set cycleTimeMain with validation.

        Args:
            value: The cycleTimeMain to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._cycleTimeMain = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"cycleTimeMain must be TimeValue or None, got {type(value).__name__}"
            )
        self._cycleTimeMain = value
        # Connection to the ECUInstance in the Topology.
        self._ecuInstance: Optional[EcuInstance] = None

    @property
    def ecu_instance(self) -> Optional[EcuInstance]:
        """Get ecuInstance (Pythonic accessor)."""
        return self._ecuInstance

    @ecu_instance.setter
    def ecu_instance(self, value: Optional[EcuInstance]) -> None:
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
        # The full duplex mechanisms is enabled if this attribute is to true.
        # Otherwise half duplex is enabled.
        self._fullDuplex: Optional[Boolean] = None

    @property
    def full_duplex(self) -> Optional[Boolean]:
        """Get fullDuplex (Pythonic accessor)."""
        return self._fullDuplex

    @full_duplex.setter
    def full_duplex(self, value: Optional[Boolean]) -> None:
        """
        Set fullDuplex with validation.

        Args:
            value: The fullDuplex to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._fullDuplex = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"fullDuplex must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._fullDuplex = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCancellation(self) -> Boolean:
        """
        AUTOSAR-compliant getter for cancellation.

        Returns:
            The cancellation value

        Note:
            Delegates to cancellation property (CODING_RULE_V2_00017)
        """
        return self.cancellation  # Delegates to property

    def setCancellation(self, value: Boolean) -> FlexrayTpEcu:
        """
        AUTOSAR-compliant setter for cancellation with method chaining.

        Args:
            value: The cancellation to set

        Returns:
            self for method chaining

        Note:
            Delegates to cancellation property setter (gets validation automatically)
        """
        self.cancellation = value  # Delegates to property setter
        return self

    def getCycleTimeMain(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for cycleTimeMain.

        Returns:
            The cycleTimeMain value

        Note:
            Delegates to cycle_time_main property (CODING_RULE_V2_00017)
        """
        return self.cycle_time_main  # Delegates to property

    def setCycleTimeMain(self, value: TimeValue) -> FlexrayTpEcu:
        """
        AUTOSAR-compliant setter for cycleTimeMain with method chaining.

        Args:
            value: The cycleTimeMain to set

        Returns:
            self for method chaining

        Note:
            Delegates to cycle_time_main property setter (gets validation automatically)
        """
        self.cycle_time_main = value  # Delegates to property setter
        return self

    def getEcuInstance(self) -> EcuInstance:
        """
        AUTOSAR-compliant getter for ecuInstance.

        Returns:
            The ecuInstance value

        Note:
            Delegates to ecu_instance property (CODING_RULE_V2_00017)
        """
        return self.ecu_instance  # Delegates to property

    def setEcuInstance(self, value: EcuInstance) -> FlexrayTpEcu:
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

    def getFullDuplex(self) -> Boolean:
        """
        AUTOSAR-compliant getter for fullDuplex.

        Returns:
            The fullDuplex value

        Note:
            Delegates to full_duplex property (CODING_RULE_V2_00017)
        """
        return self.full_duplex  # Delegates to property

    def setFullDuplex(self, value: Boolean) -> FlexrayTpEcu:
        """
        AUTOSAR-compliant setter for fullDuplex with method chaining.

        Args:
            value: The fullDuplex to set

        Returns:
            self for method chaining

        Note:
            Delegates to full_duplex property setter (gets validation automatically)
        """
        self.full_duplex = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_cancellation(self, value: Optional[Boolean]) -> FlexrayTpEcu:
        """
        Set cancellation and return self for chaining.

        Args:
            value: The cancellation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_cancellation("value")
        """
        self.cancellation = value  # Use property setter (gets validation)
        return self

    def with_cycle_time_main(self, value: Optional[TimeValue]) -> FlexrayTpEcu:
        """
        Set cycleTimeMain and return self for chaining.

        Args:
            value: The cycleTimeMain to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_cycle_time_main("value")
        """
        self.cycle_time_main = value  # Use property setter (gets validation)
        return self

    def with_ecu_instance(self, value: Optional[EcuInstance]) -> FlexrayTpEcu:
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

    def with_full_duplex(self, value: Optional[Boolean]) -> FlexrayTpEcu:
        """
        Set fullDuplex and return self for chaining.

        Args:
            value: The fullDuplex to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_full_duplex("value")
        """
        self.full_duplex = value  # Use property setter (gets validation)
        return self



class FlexrayArTpChannel(ARObject):
    """
    A channel is a group of connections sharing several properties. The FlexRay
    AutosarTransport Layer supports several channels. These channels can work
    concurrently, thus each of them requires its own state machine and
    management data structures and its own PDU-IDs.

    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::FlexrayArTpChannel

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 600, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Type of Acknowledgement.
        self._ackType: Optional[FrArTpAckType] = None

    @property
    def ack_type(self) -> Optional[FrArTpAckType]:
        """Get ackType (Pythonic accessor)."""
        return self._ackType

    @ack_type.setter
    def ack_type(self, value: Optional[FrArTpAckType]) -> None:
        """
        Set ackType with validation.

        Args:
            value: The ackType to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ackType = None
            return

        if not isinstance(value, FrArTpAckType):
            raise TypeError(
                f"ackType must be FrArTpAckType or None, got {type(value).__name__}"
            )
        self._ackType = value
        # With this switch Tx and Rx Cancellation can be turned on.
        self._cancellation: Optional[Boolean] = None

    @property
    def cancellation(self) -> Optional[Boolean]:
        """Get cancellation (Pythonic accessor)."""
        return self._cancellation

    @cancellation.setter
    def cancellation(self, value: Optional[Boolean]) -> None:
        """
        Set cancellation with validation.

        Args:
            value: The cancellation to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._cancellation = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"cancellation must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._cancellation = value
        # Adressing Type of this connection: Two Bytes Byte.
        self._extended: Optional[Boolean] = None

    @property
    def extended(self) -> Optional[Boolean]:
        """Get extended (Pythonic accessor)."""
        return self._extended

    @extended.setter
    def extended(self, value: Optional[Boolean]) -> None:
        """
        Set extended with validation.

        Args:
            value: The extended to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._extended = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"extended must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._extended = value
        # This attribute defines the maximum number of trying to frame when a TIMEOUT
        # AR occurs (depending retry is configured).
        self._maxAr: Optional[Integer] = None

    @property
    def max_ar(self) -> Optional[Integer]:
        """Get maxAr (Pythonic accessor)."""
        return self._maxAr

    @max_ar.setter
    def max_ar(self, value: Optional[Integer]) -> None:
        """
        Set maxAr with validation.

        Args:
            value: The maxAr to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxAr = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"maxAr must be Integer or int or None, got {type(value).__name__}"
            )
        self._maxAr = value
        # This attribute defines the maximum number of trying to frame when a TIMEOUT
        # AS occurs (depending on is configured).
        self._maxAs: Optional[Integer] = None

    @property
    def max_as(self) -> Optional[Integer]:
        """Get maxAs (Pythonic accessor)."""
        return self._maxAs

    @max_as.setter
    def max_as(self, value: Optional[Integer]) -> None:
        """
        Set maxAs with validation.

        Args:
            value: The maxAs to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxAs = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"maxAs must be Integer or int or None, got {type(value).__name__}"
            )
        self._maxAs = value
        # This attribute defines the number of consecutive CFs FCs (block size).
        # Valid values are 1.
        # 16 is activated, and 0.
        # 255 otherwise.
        self._maxBs: Optional[Integer] = None

    @property
    def max_bs(self) -> Optional[Integer]:
        """Get maxBs (Pythonic accessor)."""
        return self._maxBs

    @max_bs.setter
    def max_bs(self, value: Optional[Integer]) -> None:
        """
        Set maxBs with validation.

        Args:
            value: The maxBs to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxBs = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"maxBs must be Integer or int or None, got {type(value).__name__}"
            )
        self._maxBs = value
        # This attribute defines the maximal number of wait frames sent for a pending
                # connection.
        # Range is 0.
        # 255.
        self._maxFcWait: Optional[PositiveInteger] = None

    @property
    def max_fc_wait(self) -> Optional[PositiveInteger]:
        """Get maxFcWait (Pythonic accessor)."""
        return self._maxFcWait

    @max_fc_wait.setter
    def max_fc_wait(self, value: Optional[PositiveInteger]) -> None:
        """
        Set maxFcWait with validation.

        Args:
            value: The maxFcWait to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxFcWait = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"maxFcWait must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._maxFcWait = value
        # This specifies the maximum message length for the particular channel.
        self._maximum: Optional["MaximumMessage"] = None

    @property
    def maximum(self) -> Optional["MaximumMessage"]:
        """Get maximum (Pythonic accessor)."""
        return self._maximum

    @maximum.setter
    def maximum(self, value: Optional["MaximumMessage"]) -> None:
        """
        Set maximum with validation.

        Args:
            value: The maximum to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maximum = None
            return

        if not isinstance(value, MaximumMessage):
            raise TypeError(
                f"maximum must be MaximumMessage or None, got {type(value).__name__}"
            )
        self._maximum = value
        # This attribute defines the maximum number of retries (if configured for the
                # particular channel).
        # 2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._maxRetries: Optional[Integer] = None

    @property
    def max_retries(self) -> Optional[Integer]:
        """Get maxRetries (Pythonic accessor)."""
        return self._maxRetries

    @max_retries.setter
    def max_retries(self, value: Optional[Integer]) -> None:
        """
        Set maxRetries with validation.

        Args:
            value: The maxRetries to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxRetries = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"maxRetries must be Integer or int or None, got {type(value).__name__}"
            )
        self._maxRetries = value
        # This attribute defines the minimum amount of time two succeeding CFs of a 1:1
                # segmented seconds.
        # Valid values are 0, 100µs, 200µs 1ms, 2ms.
        # 127ms.
        # The value can be changed using the FrArTp_ChangeParameter interface.
        # shall be an integer multiple cycle length multiplied with the multiplexing
                # factor, = n * cycle * m, where n is >=0, cycle is FlexrayCluster.
        # cycle, and m is the of those cycles where PDUs of the PDU scheduled.
        # Due to the scheduling strategies of FrTp, only be kept to a degree the
                # maximum temporal distance of the PDUs PDU pool within one FlexRay cycle.
        # 0.
        # 127.
        self._minimum: Optional[TimeValue] = None

    @property
    def minimum(self) -> Optional[TimeValue]:
        """Get minimum (Pythonic accessor)."""
        return self._minimum

    @minimum.setter
    def minimum(self, value: Optional[TimeValue]) -> None:
        """
        Set minimum with validation.

        Args:
            value: The minimum to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._minimum = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"minimum must be TimeValue or None, got {type(value).__name__}"
            )
        self._minimum = value
        # This attribute defines whether segmentation within a 1:n is allowed or not.
        self._multicast: Optional[Boolean] = None

    @property
    def multicast(self) -> Optional[Boolean]:
        """Get multicast (Pythonic accessor)."""
        return self._multicast

    @multicast.setter
    def multicast(self, value: Optional[Boolean]) -> None:
        """
        Set multicast with validation.

        Args:
            value: The multicast to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._multicast = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"multicast must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._multicast = value
        # A FlexRayTpChannel references a set of NPdus.
        # These logically assembled into a pool of Rx NPdus pool of Tx NPdus.
        # It shall be ensured that a either references all NPdus of such a none.
        self._nPdu: List["NPdu"] = []

    @property
    def n_pdu(self) -> List["NPdu"]:
        """Get nPdu (Pythonic accessor)."""
        return self._nPdu
        # This attribute defines the time in seconds between last CF of a block or an
        # FF-x (or SF-x) and an FC or AF.
        self._timeBr: Optional[TimeValue] = None

    @property
    def time_br(self) -> Optional[TimeValue]:
        """Get timeBr (Pythonic accessor)."""
        return self._timeBr

    @time_br.setter
    def time_br(self, value: Optional[TimeValue]) -> None:
        """
        Set timeBr with validation.

        Args:
            value: The timeBr to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeBr = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"timeBr must be TimeValue or None, got {type(value).__name__}"
            )
        self._timeBr = value
        # This attribute defines the time in seconds between the two consecutive frames
        # or between a and a flow control (for Transmit between reception of an flow
        # control or and sending of the next or a flow control (for Transmit.
        self._timeCs: Optional[TimeValue] = None

    @property
    def time_cs(self) -> Optional[TimeValue]:
        """Get timeCs (Pythonic accessor)."""
        return self._timeCs

    @time_cs.setter
    def time_cs(self, value: Optional[TimeValue]) -> None:
        """
        Set timeCs with validation.

        Args:
            value: The timeCs to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeCs = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"timeCs must be TimeValue or None, got {type(value).__name__}"
            )
        self._timeCs = value
        # This attribute states the timeout in seconds between the request of the
                # Transport Layer to the Flex and the corresponding confirmation of the on the
                # receiver side (for FC or AF).
        # 2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._timeoutAr: Optional[TimeValue] = None

    @property
    def timeout_ar(self) -> Optional[TimeValue]:
        """Get timeoutAr (Pythonic accessor)."""
        return self._timeoutAr

    @timeout_ar.setter
    def timeout_ar(self, value: Optional[TimeValue]) -> None:
        """
        Set timeoutAr with validation.

        Args:
            value: The timeoutAr to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeoutAr = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"timeoutAr must be TimeValue or None, got {type(value).__name__}"
            )
        self._timeoutAr = value
        # This attribute states the timeout in seconds between the request for the
        # first PDU of the group used current connection of the Transport Layer to the
        # and the corresponding confirmation of Interface (when having sent the last
        # PDU of used in this connection) on the sender side CF).
        self._timeoutAs: Optional[TimeValue] = None

    @property
    def timeout_as(self) -> Optional[TimeValue]:
        """Get timeoutAs (Pythonic accessor)."""
        return self._timeoutAs

    @timeout_as.setter
    def timeout_as(self, value: Optional[TimeValue]) -> None:
        """
        Set timeoutAs with validation.

        Args:
            value: The timeoutAs to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeoutAs = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"timeoutAs must be TimeValue or None, got {type(value).__name__}"
            )
        self._timeoutAs = value
        # This attribute defines the timeout in seconds for waiting FC or AF on the
        # sender side in a 1:1 connection.
        self._timeoutBs: Optional[TimeValue] = None

    @property
    def timeout_bs(self) -> Optional[TimeValue]:
        """Get timeoutBs (Pythonic accessor)."""
        return self._timeoutBs

    @timeout_bs.setter
    def timeout_bs(self, value: Optional[TimeValue]) -> None:
        """
        Set timeoutBs with validation.

        Args:
            value: The timeoutBs to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeoutBs = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"timeoutBs must be TimeValue or None, got {type(value).__name__}"
            )
        self._timeoutBs = value
        # This attribute defines the timeout value in seconds for a CF or FF-x (in case
        # of retry) after receiving CF or after sending an FC or AF on the receiver.
        self._timeoutCr: Optional[TimeValue] = None

    @property
    def timeout_cr(self) -> Optional[TimeValue]:
        """Get timeoutCr (Pythonic accessor)."""
        return self._timeoutCr

    @timeout_cr.setter
    def timeout_cr(self, value: Optional[TimeValue]) -> None:
        """
        Set timeoutCr with validation.

        Args:
            value: The timeoutCr to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeoutCr = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"timeoutCr must be TimeValue or None, got {type(value).__name__}"
            )
        self._timeoutCr = value
        # Group of connections that can be used in this channel.
        self._tpConnection: List[FlexrayArTpConnection] = []

    @property
    def tp_connection(self) -> List[FlexrayArTpConnection]:
        """Get tpConnection (Pythonic accessor)."""
        return self._tpConnection

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAckType(self) -> FrArTpAckType:
        """
        AUTOSAR-compliant getter for ackType.

        Returns:
            The ackType value

        Note:
            Delegates to ack_type property (CODING_RULE_V2_00017)
        """
        return self.ack_type  # Delegates to property

    def setAckType(self, value: FrArTpAckType) -> FlexrayArTpChannel:
        """
        AUTOSAR-compliant setter for ackType with method chaining.

        Args:
            value: The ackType to set

        Returns:
            self for method chaining

        Note:
            Delegates to ack_type property setter (gets validation automatically)
        """
        self.ack_type = value  # Delegates to property setter
        return self

    def getCancellation(self) -> Boolean:
        """
        AUTOSAR-compliant getter for cancellation.

        Returns:
            The cancellation value

        Note:
            Delegates to cancellation property (CODING_RULE_V2_00017)
        """
        return self.cancellation  # Delegates to property

    def setCancellation(self, value: Boolean) -> FlexrayArTpChannel:
        """
        AUTOSAR-compliant setter for cancellation with method chaining.

        Args:
            value: The cancellation to set

        Returns:
            self for method chaining

        Note:
            Delegates to cancellation property setter (gets validation automatically)
        """
        self.cancellation = value  # Delegates to property setter
        return self

    def getExtended(self) -> Boolean:
        """
        AUTOSAR-compliant getter for extended.

        Returns:
            The extended value

        Note:
            Delegates to extended property (CODING_RULE_V2_00017)
        """
        return self.extended  # Delegates to property

    def setExtended(self, value: Boolean) -> FlexrayArTpChannel:
        """
        AUTOSAR-compliant setter for extended with method chaining.

        Args:
            value: The extended to set

        Returns:
            self for method chaining

        Note:
            Delegates to extended property setter (gets validation automatically)
        """
        self.extended = value  # Delegates to property setter
        return self

    def getMaxAr(self) -> Integer:
        """
        AUTOSAR-compliant getter for maxAr.

        Returns:
            The maxAr value

        Note:
            Delegates to max_ar property (CODING_RULE_V2_00017)
        """
        return self.max_ar  # Delegates to property

    def setMaxAr(self, value: Integer) -> FlexrayArTpChannel:
        """
        AUTOSAR-compliant setter for maxAr with method chaining.

        Args:
            value: The maxAr to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_ar property setter (gets validation automatically)
        """
        self.max_ar = value  # Delegates to property setter
        return self

    def getMaxAs(self) -> Integer:
        """
        AUTOSAR-compliant getter for maxAs.

        Returns:
            The maxAs value

        Note:
            Delegates to max_as property (CODING_RULE_V2_00017)
        """
        return self.max_as  # Delegates to property

    def setMaxAs(self, value: Integer) -> FlexrayArTpChannel:
        """
        AUTOSAR-compliant setter for maxAs with method chaining.

        Args:
            value: The maxAs to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_as property setter (gets validation automatically)
        """
        self.max_as = value  # Delegates to property setter
        return self

    def getMaxBs(self) -> Integer:
        """
        AUTOSAR-compliant getter for maxBs.

        Returns:
            The maxBs value

        Note:
            Delegates to max_bs property (CODING_RULE_V2_00017)
        """
        return self.max_bs  # Delegates to property

    def setMaxBs(self, value: Integer) -> FlexrayArTpChannel:
        """
        AUTOSAR-compliant setter for maxBs with method chaining.

        Args:
            value: The maxBs to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_bs property setter (gets validation automatically)
        """
        self.max_bs = value  # Delegates to property setter
        return self

    def getMaxFcWait(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for maxFcWait.

        Returns:
            The maxFcWait value

        Note:
            Delegates to max_fc_wait property (CODING_RULE_V2_00017)
        """
        return self.max_fc_wait  # Delegates to property

    def setMaxFcWait(self, value: PositiveInteger) -> FlexrayArTpChannel:
        """
        AUTOSAR-compliant setter for maxFcWait with method chaining.

        Args:
            value: The maxFcWait to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_fc_wait property setter (gets validation automatically)
        """
        self.max_fc_wait = value  # Delegates to property setter
        return self

    def getMaximum(self) -> "MaximumMessage":
        """
        AUTOSAR-compliant getter for maximum.

        Returns:
            The maximum value

        Note:
            Delegates to maximum property (CODING_RULE_V2_00017)
        """
        return self.maximum  # Delegates to property

    def setMaximum(self, value: "MaximumMessage") -> FlexrayArTpChannel:
        """
        AUTOSAR-compliant setter for maximum with method chaining.

        Args:
            value: The maximum to set

        Returns:
            self for method chaining

        Note:
            Delegates to maximum property setter (gets validation automatically)
        """
        self.maximum = value  # Delegates to property setter
        return self

    def getMaxRetries(self) -> Integer:
        """
        AUTOSAR-compliant getter for maxRetries.

        Returns:
            The maxRetries value

        Note:
            Delegates to max_retries property (CODING_RULE_V2_00017)
        """
        return self.max_retries  # Delegates to property

    def setMaxRetries(self, value: Integer) -> FlexrayArTpChannel:
        """
        AUTOSAR-compliant setter for maxRetries with method chaining.

        Args:
            value: The maxRetries to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_retries property setter (gets validation automatically)
        """
        self.max_retries = value  # Delegates to property setter
        return self

    def getMinimum(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for minimum.

        Returns:
            The minimum value

        Note:
            Delegates to minimum property (CODING_RULE_V2_00017)
        """
        return self.minimum  # Delegates to property

    def setMinimum(self, value: TimeValue) -> FlexrayArTpChannel:
        """
        AUTOSAR-compliant setter for minimum with method chaining.

        Args:
            value: The minimum to set

        Returns:
            self for method chaining

        Note:
            Delegates to minimum property setter (gets validation automatically)
        """
        self.minimum = value  # Delegates to property setter
        return self

    def getMulticast(self) -> Boolean:
        """
        AUTOSAR-compliant getter for multicast.

        Returns:
            The multicast value

        Note:
            Delegates to multicast property (CODING_RULE_V2_00017)
        """
        return self.multicast  # Delegates to property

    def setMulticast(self, value: Boolean) -> FlexrayArTpChannel:
        """
        AUTOSAR-compliant setter for multicast with method chaining.

        Args:
            value: The multicast to set

        Returns:
            self for method chaining

        Note:
            Delegates to multicast property setter (gets validation automatically)
        """
        self.multicast = value  # Delegates to property setter
        return self

    def getNPdu(self) -> List["NPdu"]:
        """
        AUTOSAR-compliant getter for nPdu.

        Returns:
            The nPdu value

        Note:
            Delegates to n_pdu property (CODING_RULE_V2_00017)
        """
        return self.n_pdu  # Delegates to property

    def getTimeBr(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for timeBr.

        Returns:
            The timeBr value

        Note:
            Delegates to time_br property (CODING_RULE_V2_00017)
        """
        return self.time_br  # Delegates to property

    def setTimeBr(self, value: TimeValue) -> FlexrayArTpChannel:
        """
        AUTOSAR-compliant setter for timeBr with method chaining.

        Args:
            value: The timeBr to set

        Returns:
            self for method chaining

        Note:
            Delegates to time_br property setter (gets validation automatically)
        """
        self.time_br = value  # Delegates to property setter
        return self

    def getTimeCs(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for timeCs.

        Returns:
            The timeCs value

        Note:
            Delegates to time_cs property (CODING_RULE_V2_00017)
        """
        return self.time_cs  # Delegates to property

    def setTimeCs(self, value: TimeValue) -> FlexrayArTpChannel:
        """
        AUTOSAR-compliant setter for timeCs with method chaining.

        Args:
            value: The timeCs to set

        Returns:
            self for method chaining

        Note:
            Delegates to time_cs property setter (gets validation automatically)
        """
        self.time_cs = value  # Delegates to property setter
        return self

    def getTimeoutAr(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for timeoutAr.

        Returns:
            The timeoutAr value

        Note:
            Delegates to timeout_ar property (CODING_RULE_V2_00017)
        """
        return self.timeout_ar  # Delegates to property

    def setTimeoutAr(self, value: TimeValue) -> FlexrayArTpChannel:
        """
        AUTOSAR-compliant setter for timeoutAr with method chaining.

        Args:
            value: The timeoutAr to set

        Returns:
            self for method chaining

        Note:
            Delegates to timeout_ar property setter (gets validation automatically)
        """
        self.timeout_ar = value  # Delegates to property setter
        return self

    def getTimeoutAs(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for timeoutAs.

        Returns:
            The timeoutAs value

        Note:
            Delegates to timeout_as property (CODING_RULE_V2_00017)
        """
        return self.timeout_as  # Delegates to property

    def setTimeoutAs(self, value: TimeValue) -> FlexrayArTpChannel:
        """
        AUTOSAR-compliant setter for timeoutAs with method chaining.

        Args:
            value: The timeoutAs to set

        Returns:
            self for method chaining

        Note:
            Delegates to timeout_as property setter (gets validation automatically)
        """
        self.timeout_as = value  # Delegates to property setter
        return self

    def getTimeoutBs(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for timeoutBs.

        Returns:
            The timeoutBs value

        Note:
            Delegates to timeout_bs property (CODING_RULE_V2_00017)
        """
        return self.timeout_bs  # Delegates to property

    def setTimeoutBs(self, value: TimeValue) -> FlexrayArTpChannel:
        """
        AUTOSAR-compliant setter for timeoutBs with method chaining.

        Args:
            value: The timeoutBs to set

        Returns:
            self for method chaining

        Note:
            Delegates to timeout_bs property setter (gets validation automatically)
        """
        self.timeout_bs = value  # Delegates to property setter
        return self

    def getTimeoutCr(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for timeoutCr.

        Returns:
            The timeoutCr value

        Note:
            Delegates to timeout_cr property (CODING_RULE_V2_00017)
        """
        return self.timeout_cr  # Delegates to property

    def setTimeoutCr(self, value: TimeValue) -> FlexrayArTpChannel:
        """
        AUTOSAR-compliant setter for timeoutCr with method chaining.

        Args:
            value: The timeoutCr to set

        Returns:
            self for method chaining

        Note:
            Delegates to timeout_cr property setter (gets validation automatically)
        """
        self.timeout_cr = value  # Delegates to property setter
        return self

    def getTpConnection(self) -> List[FlexrayArTpConnection]:
        """
        AUTOSAR-compliant getter for tpConnection.

        Returns:
            The tpConnection value

        Note:
            Delegates to tp_connection property (CODING_RULE_V2_00017)
        """
        return self.tp_connection  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_ack_type(self, value: Optional[FrArTpAckType]) -> FlexrayArTpChannel:
        """
        Set ackType and return self for chaining.

        Args:
            value: The ackType to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ack_type("value")
        """
        self.ack_type = value  # Use property setter (gets validation)
        return self

    def with_cancellation(self, value: Optional[Boolean]) -> FlexrayArTpChannel:
        """
        Set cancellation and return self for chaining.

        Args:
            value: The cancellation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_cancellation("value")
        """
        self.cancellation = value  # Use property setter (gets validation)
        return self

    def with_extended(self, value: Optional[Boolean]) -> FlexrayArTpChannel:
        """
        Set extended and return self for chaining.

        Args:
            value: The extended to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_extended("value")
        """
        self.extended = value  # Use property setter (gets validation)
        return self

    def with_max_ar(self, value: Optional[Integer]) -> FlexrayArTpChannel:
        """
        Set maxAr and return self for chaining.

        Args:
            value: The maxAr to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_ar("value")
        """
        self.max_ar = value  # Use property setter (gets validation)
        return self

    def with_max_as(self, value: Optional[Integer]) -> FlexrayArTpChannel:
        """
        Set maxAs and return self for chaining.

        Args:
            value: The maxAs to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_as("value")
        """
        self.max_as = value  # Use property setter (gets validation)
        return self

    def with_max_bs(self, value: Optional[Integer]) -> FlexrayArTpChannel:
        """
        Set maxBs and return self for chaining.

        Args:
            value: The maxBs to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_bs("value")
        """
        self.max_bs = value  # Use property setter (gets validation)
        return self

    def with_max_fc_wait(self, value: Optional[PositiveInteger]) -> FlexrayArTpChannel:
        """
        Set maxFcWait and return self for chaining.

        Args:
            value: The maxFcWait to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_fc_wait("value")
        """
        self.max_fc_wait = value  # Use property setter (gets validation)
        return self

    def with_maximum(self, value: Optional["MaximumMessage"]) -> FlexrayArTpChannel:
        """
        Set maximum and return self for chaining.

        Args:
            value: The maximum to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_maximum("value")
        """
        self.maximum = value  # Use property setter (gets validation)
        return self

    def with_max_retries(self, value: Optional[Integer]) -> FlexrayArTpChannel:
        """
        Set maxRetries and return self for chaining.

        Args:
            value: The maxRetries to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_retries("value")
        """
        self.max_retries = value  # Use property setter (gets validation)
        return self

    def with_minimum(self, value: Optional[TimeValue]) -> FlexrayArTpChannel:
        """
        Set minimum and return self for chaining.

        Args:
            value: The minimum to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_minimum("value")
        """
        self.minimum = value  # Use property setter (gets validation)
        return self

    def with_multicast(self, value: Optional[Boolean]) -> FlexrayArTpChannel:
        """
        Set multicast and return self for chaining.

        Args:
            value: The multicast to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_multicast("value")
        """
        self.multicast = value  # Use property setter (gets validation)
        return self

    def with_time_br(self, value: Optional[TimeValue]) -> FlexrayArTpChannel:
        """
        Set timeBr and return self for chaining.

        Args:
            value: The timeBr to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_time_br("value")
        """
        self.time_br = value  # Use property setter (gets validation)
        return self

    def with_time_cs(self, value: Optional[TimeValue]) -> FlexrayArTpChannel:
        """
        Set timeCs and return self for chaining.

        Args:
            value: The timeCs to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_time_cs("value")
        """
        self.time_cs = value  # Use property setter (gets validation)
        return self

    def with_timeout_ar(self, value: Optional[TimeValue]) -> FlexrayArTpChannel:
        """
        Set timeoutAr and return self for chaining.

        Args:
            value: The timeoutAr to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_timeout_ar("value")
        """
        self.timeout_ar = value  # Use property setter (gets validation)
        return self

    def with_timeout_as(self, value: Optional[TimeValue]) -> FlexrayArTpChannel:
        """
        Set timeoutAs and return self for chaining.

        Args:
            value: The timeoutAs to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_timeout_as("value")
        """
        self.timeout_as = value  # Use property setter (gets validation)
        return self

    def with_timeout_bs(self, value: Optional[TimeValue]) -> FlexrayArTpChannel:
        """
        Set timeoutBs and return self for chaining.

        Args:
            value: The timeoutBs to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_timeout_bs("value")
        """
        self.timeout_bs = value  # Use property setter (gets validation)
        return self

    def with_timeout_cr(self, value: Optional[TimeValue]) -> FlexrayArTpChannel:
        """
        Set timeoutCr and return self for chaining.

        Args:
            value: The timeoutCr to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_timeout_cr("value")
        """
        self.timeout_cr = value  # Use property setter (gets validation)
        return self



class FlexrayArTpNode(Identifiable):
    """
    TP Node (Sender or Receiver) provides the TP Address and the connection to
    the Topology description.

    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::FlexrayArTpNode

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 602, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Association to one or more physical connectors (max of connectors for
                # FlexRay: 2).
        # System Description this reference is mandatory.
        # In Extract this reference is optional (references to are not part of the ECU
                # Extract shall be.
        self._connector: List["FlexrayCommunication"] = []

    @property
    def connector(self) -> List["FlexrayCommunication"]:
        """Get connector (Pythonic accessor)."""
        return self._connector
        # Reference to the TP Address that is used by the TpNode.
        # is optional in case that the multicast TP used (reference from TpConnection).
        self._tpAddress: Optional[TpAddress] = None

    @property
    def tp_address(self) -> Optional[TpAddress]:
        """Get tpAddress (Pythonic accessor)."""
        return self._tpAddress

    @tp_address.setter
    def tp_address(self, value: Optional[TpAddress]) -> None:
        """
        Set tpAddress with validation.

        Args:
            value: The tpAddress to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tpAddress = None
            return

        if not isinstance(value, TpAddress):
            raise TypeError(
                f"tpAddress must be TpAddress or None, got {type(value).__name__}"
            )
        self._tpAddress = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getConnector(self) -> List["FlexrayCommunication"]:
        """
        AUTOSAR-compliant getter for connector.

        Returns:
            The connector value

        Note:
            Delegates to connector property (CODING_RULE_V2_00017)
        """
        return self.connector  # Delegates to property

    def getTpAddress(self) -> TpAddress:
        """
        AUTOSAR-compliant getter for tpAddress.

        Returns:
            The tpAddress value

        Note:
            Delegates to tp_address property (CODING_RULE_V2_00017)
        """
        return self.tp_address  # Delegates to property

    def setTpAddress(self, value: TpAddress) -> FlexrayArTpNode:
        """
        AUTOSAR-compliant setter for tpAddress with method chaining.

        Args:
            value: The tpAddress to set

        Returns:
            self for method chaining

        Note:
            Delegates to tp_address property setter (gets validation automatically)
        """
        self.tp_address = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_tp_address(self, value: Optional[TpAddress]) -> FlexrayArTpNode:
        """
        Set tpAddress and return self for chaining.

        Args:
            value: The tpAddress to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tp_address("value")
        """
        self.tp_address = value  # Use property setter (gets validation)
        return self



class FlexrayArTpConnection(TpConnection):
    """
    A connection within a channel identifies the sender and the receiver of this
    particular communication. The FlexRay Autosar Tp module routes a Pdu through
    this connection.

    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::FlexrayArTpConnection

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 603, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This parameter defines the number of PDUs that shall be for this connection
                # when it is active.
        # The range.
        self._connectionPrio: Optional[Integer] = None

    @property
    def connection_prio(self) -> Optional[Integer]:
        """Get connectionPrio (Pythonic accessor)."""
        return self._connectionPrio

    @connection_prio.setter
    def connection_prio(self, value: Optional[Integer]) -> None:
        """
        Set connectionPrio with validation.

        Args:
            value: The connectionPrio to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._connectionPrio = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"connectionPrio must be Integer or int or None, got {type(value).__name__}"
            )
        self._connectionPrio = value
        # Reference to the IPdu that is segmented by the Transport address of the
        # transmitted NPdu is the configured source Communication target address of the
        # transmitted NPdu is the configured target Communication.
        self._directTpSdu: Optional[IPdu] = None

    @property
    def direct_tp_sdu(self) -> Optional[IPdu]:
        """Get directTpSdu (Pythonic accessor)."""
        return self._directTpSdu

    @direct_tp_sdu.setter
    def direct_tp_sdu(self, value: Optional[IPdu]) -> None:
        """
        Set directTpSdu with validation.

        Args:
            value: The directTpSdu to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._directTpSdu = None
            return

        if not isinstance(value, IPdu):
            raise TypeError(
                f"directTpSdu must be IPdu or None, got {type(value).__name__}"
            )
        self._directTpSdu = value
        # TP address for 1:n connections.
        self._multicast: Optional[TpAddress] = None

    @property
    def multicast(self) -> Optional[TpAddress]:
        """Get multicast (Pythonic accessor)."""
        return self._multicast

    @multicast.setter
    def multicast(self, value: Optional[TpAddress]) -> None:
        """
        Set multicast with validation.

        Args:
            value: The multicast to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._multicast = None
            return

        if not isinstance(value, TpAddress):
            raise TypeError(
                f"multicast must be TpAddress or None, got {type(value).__name__}"
            )
        self._multicast = value
        # Reference to the IPdu that is segmented by the Transport support of both
                # sending and receiving is used, references the IPdu used for the direction.
        # address of the transmitted NPdu is the configured target Communication target
                # address of the transmitted NPdu is the configured source Communication.
        self._reversedTpSdu: Optional[IPdu] = None

    @property
    def reversed_tp_sdu(self) -> Optional[IPdu]:
        """Get reversedTpSdu (Pythonic accessor)."""
        return self._reversedTpSdu

    @reversed_tp_sdu.setter
    def reversed_tp_sdu(self, value: Optional[IPdu]) -> None:
        """
        Set reversedTpSdu with validation.

        Args:
            value: The reversedTpSdu to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._reversedTpSdu = None
            return

        if not isinstance(value, IPdu):
            raise TypeError(
                f"reversedTpSdu must be IPdu or None, got {type(value).__name__}"
            )
        self._reversedTpSdu = value
        # The source of the TP connection.
        self._source: Optional[FlexrayArTpNode] = None

    @property
    def source(self) -> Optional[FlexrayArTpNode]:
        """Get source (Pythonic accessor)."""
        return self._source

    @source.setter
    def source(self, value: Optional[FlexrayArTpNode]) -> None:
        """
        Set source with validation.

        Args:
            value: The source to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._source = None
            return

        if not isinstance(value, FlexrayArTpNode):
            raise TypeError(
                f"source must be FlexrayArTpNode or None, got {type(value).__name__}"
            )
        self._source = value
        # The target of the TP connection.
        self._target: List[FlexrayArTpNode] = []

    @property
    def target(self) -> List[FlexrayArTpNode]:
        """Get target (Pythonic accessor)."""
        return self._target

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getConnectionPrio(self) -> Integer:
        """
        AUTOSAR-compliant getter for connectionPrio.

        Returns:
            The connectionPrio value

        Note:
            Delegates to connection_prio property (CODING_RULE_V2_00017)
        """
        return self.connection_prio  # Delegates to property

    def setConnectionPrio(self, value: Integer) -> FlexrayArTpConnection:
        """
        AUTOSAR-compliant setter for connectionPrio with method chaining.

        Args:
            value: The connectionPrio to set

        Returns:
            self for method chaining

        Note:
            Delegates to connection_prio property setter (gets validation automatically)
        """
        self.connection_prio = value  # Delegates to property setter
        return self

    def getDirectTpSdu(self) -> IPdu:
        """
        AUTOSAR-compliant getter for directTpSdu.

        Returns:
            The directTpSdu value

        Note:
            Delegates to direct_tp_sdu property (CODING_RULE_V2_00017)
        """
        return self.direct_tp_sdu  # Delegates to property

    def setDirectTpSdu(self, value: IPdu) -> FlexrayArTpConnection:
        """
        AUTOSAR-compliant setter for directTpSdu with method chaining.

        Args:
            value: The directTpSdu to set

        Returns:
            self for method chaining

        Note:
            Delegates to direct_tp_sdu property setter (gets validation automatically)
        """
        self.direct_tp_sdu = value  # Delegates to property setter
        return self

    def getMulticast(self) -> TpAddress:
        """
        AUTOSAR-compliant getter for multicast.

        Returns:
            The multicast value

        Note:
            Delegates to multicast property (CODING_RULE_V2_00017)
        """
        return self.multicast  # Delegates to property

    def setMulticast(self, value: TpAddress) -> FlexrayArTpConnection:
        """
        AUTOSAR-compliant setter for multicast with method chaining.

        Args:
            value: The multicast to set

        Returns:
            self for method chaining

        Note:
            Delegates to multicast property setter (gets validation automatically)
        """
        self.multicast = value  # Delegates to property setter
        return self

    def getReversedTpSdu(self) -> IPdu:
        """
        AUTOSAR-compliant getter for reversedTpSdu.

        Returns:
            The reversedTpSdu value

        Note:
            Delegates to reversed_tp_sdu property (CODING_RULE_V2_00017)
        """
        return self.reversed_tp_sdu  # Delegates to property

    def setReversedTpSdu(self, value: IPdu) -> FlexrayArTpConnection:
        """
        AUTOSAR-compliant setter for reversedTpSdu with method chaining.

        Args:
            value: The reversedTpSdu to set

        Returns:
            self for method chaining

        Note:
            Delegates to reversed_tp_sdu property setter (gets validation automatically)
        """
        self.reversed_tp_sdu = value  # Delegates to property setter
        return self

    def getSource(self) -> FlexrayArTpNode:
        """
        AUTOSAR-compliant getter for source.

        Returns:
            The source value

        Note:
            Delegates to source property (CODING_RULE_V2_00017)
        """
        return self.source  # Delegates to property

    def setSource(self, value: FlexrayArTpNode) -> FlexrayArTpConnection:
        """
        AUTOSAR-compliant setter for source with method chaining.

        Args:
            value: The source to set

        Returns:
            self for method chaining

        Note:
            Delegates to source property setter (gets validation automatically)
        """
        self.source = value  # Delegates to property setter
        return self

    def getTarget(self) -> List[FlexrayArTpNode]:
        """
        AUTOSAR-compliant getter for target.

        Returns:
            The target value

        Note:
            Delegates to target property (CODING_RULE_V2_00017)
        """
        return self.target  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_connection_prio(self, value: Optional[Integer]) -> FlexrayArTpConnection:
        """
        Set connectionPrio and return self for chaining.

        Args:
            value: The connectionPrio to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_connection_prio("value")
        """
        self.connection_prio = value  # Use property setter (gets validation)
        return self

    def with_direct_tp_sdu(self, value: Optional[IPdu]) -> FlexrayArTpConnection:
        """
        Set directTpSdu and return self for chaining.

        Args:
            value: The directTpSdu to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_direct_tp_sdu("value")
        """
        self.direct_tp_sdu = value  # Use property setter (gets validation)
        return self

    def with_multicast(self, value: Optional[TpAddress]) -> FlexrayArTpConnection:
        """
        Set multicast and return self for chaining.

        Args:
            value: The multicast to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_multicast("value")
        """
        self.multicast = value  # Use property setter (gets validation)
        return self

    def with_reversed_tp_sdu(self, value: Optional[IPdu]) -> FlexrayArTpConnection:
        """
        Set reversedTpSdu and return self for chaining.

        Args:
            value: The reversedTpSdu to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_reversed_tp_sdu("value")
        """
        self.reversed_tp_sdu = value  # Use property setter (gets validation)
        return self

    def with_source(self, value: Optional[FlexrayArTpNode]) -> FlexrayArTpConnection:
        """
        Set source and return self for chaining.

        Args:
            value: The source to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_source("value")
        """
        self.source = value  # Use property setter (gets validation)
        return self



class CanTpChannel(Identifiable):
    """
    Configuration parameters of the CanTp channel.

    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::CanTpChannel

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 608, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The id of the channel.
        # The value shall be unique for each.
        self._channelId: Optional[PositiveInteger] = None

    @property
    def channel_id(self) -> Optional[PositiveInteger]:
        """Get channelId (Pythonic accessor)."""
        return self._channelId

    @channel_id.setter
    def channel_id(self, value: Optional[PositiveInteger]) -> None:
        """
        Set channelId with validation.

        Args:
            value: The channelId to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._channelId = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"channelId must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._channelId = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getChannelId(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for channelId.

        Returns:
            The channelId value

        Note:
            Delegates to channel_id property (CODING_RULE_V2_00017)
        """
        return self.channel_id  # Delegates to property

    def setChannelId(self, value: PositiveInteger) -> CanTpChannel:
        """
        AUTOSAR-compliant setter for channelId with method chaining.

        Args:
            value: The channelId to set

        Returns:
            self for method chaining

        Note:
            Delegates to channel_id property setter (gets validation automatically)
        """
        self.channel_id = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_channel_id(self, value: Optional[PositiveInteger]) -> CanTpChannel:
        """
        Set channelId and return self for chaining.

        Args:
            value: The channelId to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_channel_id("value")
        """
        self.channel_id = value  # Use property setter (gets validation)
        return self



class CanTpConnection(TpConnection):
    """
    A connection identifies the sender and the receiver of this particular
    communication. The CanTp module routes a Pdu through this connection.
    atpVariation: Derived, because TpNode can vary.

    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::CanTpConnection

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 608, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Declares which communication addressing mode is supported.
        self._addressing: Optional[CanTpAddressing] = None

    @property
    def addressing(self) -> Optional[CanTpAddressing]:
        """Get addressing (Pythonic accessor)."""
        return self._addressing

    @addressing.setter
    def addressing(self, value: Optional[CanTpAddressing]) -> None:
        """
        Set addressing with validation.

        Args:
            value: The addressing to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._addressing = None
            return

        if not isinstance(value, CanTpAddressing):
            raise TypeError(
                f"addressing must be CanTpAddressing or None, got {type(value).__name__}"
            )
        self._addressing = value
        # With this switch Tx Cancellation can be turned on or off.
        # that the Rx Cancellation is always enabled.
        self._cancellation: Optional[Boolean] = None

    @property
    def cancellation(self) -> Optional[Boolean]:
        """Get cancellation (Pythonic accessor)."""
        return self._cancellation

    @cancellation.setter
    def cancellation(self, value: Optional[Boolean]) -> None:
        """
        Set cancellation with validation.

        Args:
            value: The cancellation to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._cancellation = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"cancellation must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._cancellation = value
        # Reference to the CanTpChannel on which this CanTp realized.
        self._canTpChannel: Optional[CanTpChannel] = None

    @property
    def can_tp_channel(self) -> Optional[CanTpChannel]:
        """Get canTpChannel (Pythonic accessor)."""
        return self._canTpChannel

    @can_tp_channel.setter
    def can_tp_channel(self, value: Optional[CanTpChannel]) -> None:
        """
        Set canTpChannel with validation.

        Args:
            value: The canTpChannel to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._canTpChannel = None
            return

        if not isinstance(value, CanTpChannel):
            raise TypeError(
                f"canTpChannel must be CanTpChannel or None, got {type(value).__name__}"
            )
        self._canTpChannel = value
        # Reference to an Data NPdu.
        self._dataPdu: Optional["NPdu"] = None

    @property
    def data_pdu(self) -> Optional["NPdu"]:
        """Get dataPdu (Pythonic accessor)."""
        return self._dataPdu

    @data_pdu.setter
    def data_pdu(self, value: Optional["NPdu"]) -> None:
        """
        Set dataPdu with validation.

        Args:
            value: The dataPdu to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dataPdu = None
            return

        if not isinstance(value, NPdu):
            raise TypeError(
                f"dataPdu must be NPdu or None, got {type(value).__name__}"
            )
        self._dataPdu = value
        # Reference to the Flow Control NPdu.
        self._flowControlPdu: Optional["NPdu"] = None

    @property
    def flow_control_pdu(self) -> Optional["NPdu"]:
        """Get flowControlPdu (Pythonic accessor)."""
        return self._flowControlPdu

    @flow_control_pdu.setter
    def flow_control_pdu(self, value: Optional["NPdu"]) -> None:
        """
        Set flowControlPdu with validation.

        Args:
            value: The flowControlPdu to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._flowControlPdu = None
            return

        if not isinstance(value, NPdu):
            raise TypeError(
                f"flowControlPdu must be NPdu or None, got {type(value).__name__}"
            )
        self._flowControlPdu = value
        # The maximum number of N-PDUs the CanTp receiver sender to send, before
                # waiting for an continue transmission of the following further details on this
                # parameter value see specification.
        # reasons of buffer length, the CAN Transport adapt the BS value within the
                # limit of this.
        self._maxBlockSize: Optional[Integer] = None

    @property
    def max_block_size(self) -> Optional[Integer]:
        """Get maxBlockSize (Pythonic accessor)."""
        return self._maxBlockSize

    @max_block_size.setter
    def max_block_size(self, value: Optional[Integer]) -> None:
        """
        Set maxBlockSize with validation.

        Args:
            value: The maxBlockSize to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxBlockSize = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"maxBlockSize must be Integer or int or None, got {type(value).__name__}"
            )
        self._maxBlockSize = value
        # TP address for 1:n connections.
        self._multicast: Optional[CanTpAddress] = None

    @property
    def multicast(self) -> Optional[CanTpAddress]:
        """Get multicast (Pythonic accessor)."""
        return self._multicast

    @multicast.setter
    def multicast(self, value: Optional[CanTpAddress]) -> None:
        """
        Set multicast with validation.

        Args:
            value: The multicast to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._multicast = None
            return

        if not isinstance(value, CanTpAddress):
            raise TypeError(
                f"multicast must be CanTpAddress or None, got {type(value).__name__}"
            )
        self._multicast = value
        # This specifies whether or not Sfs, FCs and the last CF be padded to 8 bytes
                # length in case it contains less N-PDU received uses padding for SF, FC and
                # CF.
        # (N-PDU length is always 8 bytes) N-PDU received does not use padding for SF,
                # the last CF.
        # (N-PDU length is dynamic).
        self._padding: Optional[Boolean] = None

    @property
    def padding(self) -> Optional[Boolean]:
        """Get padding (Pythonic accessor)."""
        return self._padding

    @padding.setter
    def padding(self, value: Optional[Boolean]) -> None:
        """
        Set padding with validation.

        Args:
            value: The padding to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._padding = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"padding must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._padding = value
        # The target of the TP connection.
        self._receiver: List[CanTpNode] = []

    @property
    def receiver(self) -> List[CanTpNode]:
        """Get receiver (Pythonic accessor)."""
        return self._receiver
        # Network Target Address type.
        # 2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._taTypeType: Optional["NetworkTargetAddress"] = None

    @property
    def ta_type_type(self) -> Optional["NetworkTargetAddress"]:
        """Get taTypeType (Pythonic accessor)."""
        return self._taTypeType

    @ta_type_type.setter
    def ta_type_type(self, value: Optional["NetworkTargetAddress"]) -> None:
        """
        Set taTypeType with validation.

        Args:
            value: The taTypeType to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._taTypeType = None
            return

        if not isinstance(value, NetworkTargetAddress):
            raise TypeError(
                f"taTypeType must be NetworkTargetAddress or None, got {type(value).__name__}"
            )
        self._taTypeType = value
        # Value in seconds of the performance requirement for (N_ N_Ar).
        # N_Br is the elapsed time between the of a FF or CF or the transmit a FC,
                # until the transmit request of the next.
        self._timeoutBr: Optional[TimeValue] = None

    @property
    def timeout_br(self) -> Optional[TimeValue]:
        """Get timeoutBr (Pythonic accessor)."""
        return self._timeoutBr

    @timeout_br.setter
    def timeout_br(self, value: Optional[TimeValue]) -> None:
        """
        Set timeoutBr with validation.

        Args:
            value: The timeoutBr to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeoutBr = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"timeoutBr must be TimeValue or None, got {type(value).__name__}"
            )
        self._timeoutBr = value
        # This parameter defines the timeout for waiting for an FC on the sender side
                # in an 1:1 connection.
        # Specified.
        self._timeoutBs: Optional[TimeValue] = None

    @property
    def timeout_bs(self) -> Optional[TimeValue]:
        """Get timeoutBs (Pythonic accessor)."""
        return self._timeoutBs

    @timeout_bs.setter
    def timeout_bs(self, value: Optional[TimeValue]) -> None:
        """
        Set timeoutBs with validation.

        Args:
            value: The timeoutBs to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeoutBs = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"timeoutBs must be TimeValue or None, got {type(value).__name__}"
            )
        self._timeoutBs = value
        # This parameter defines the timeout value for waiting for a FF-x (in case of
                # retry) after receiving the last CF or an FC or AF on the receiver side.
        # Specified.
        self._timeoutCr: Optional[TimeValue] = None

    @property
    def timeout_cr(self) -> Optional[TimeValue]:
        """Get timeoutCr (Pythonic accessor)."""
        return self._timeoutCr

    @timeout_cr.setter
    def timeout_cr(self, value: Optional[TimeValue]) -> None:
        """
        Set timeoutCr with validation.

        Args:
            value: The timeoutCr to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeoutCr = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"timeoutCr must be TimeValue or None, got {type(value).__name__}"
            )
        self._timeoutCr = value
        # The attribute timeoutCs represents the time (in seconds) between the transmit
        # request of a CF the transmit request of the next CF N-PDU.
        self._timeoutCs: Optional[TimeValue] = None

    @property
    def timeout_cs(self) -> Optional[TimeValue]:
        """Get timeoutCs (Pythonic accessor)."""
        return self._timeoutCs

    @timeout_cs.setter
    def timeout_cs(self, value: Optional[TimeValue]) -> None:
        """
        Set timeoutCs with validation.

        Args:
            value: The timeoutCs to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeoutCs = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"timeoutCs must be TimeValue or None, got {type(value).__name__}"
            )
        self._timeoutCs = value
        # Reference to an IPdu that is segmented by the Transport.
        self._tpSdu: Optional[IPdu] = None

    @property
    def tp_sdu(self) -> Optional[IPdu]:
        """Get tpSdu (Pythonic accessor)."""
        return self._tpSdu

    @tp_sdu.setter
    def tp_sdu(self, value: Optional[IPdu]) -> None:
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

        if not isinstance(value, IPdu):
            raise TypeError(
                f"tpSdu must be IPdu or None, got {type(value).__name__}"
            )
        self._tpSdu = value
        # The source of the TP connection.
        self._transmitter: Optional[CanTpNode] = None

    @property
    def transmitter(self) -> Optional[CanTpNode]:
        """Get transmitter (Pythonic accessor)."""
        return self._transmitter

    @transmitter.setter
    def transmitter(self, value: Optional[CanTpNode]) -> None:
        """
        Set transmitter with validation.

        Args:
            value: The transmitter to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._transmitter = None
            return

        if not isinstance(value, CanTpNode):
            raise TypeError(
                f"transmitter must be CanTpNode or None, got {type(value).__name__}"
            )
        self._transmitter = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAddressing(self) -> CanTpAddressing:
        """
        AUTOSAR-compliant getter for addressing.

        Returns:
            The addressing value

        Note:
            Delegates to addressing property (CODING_RULE_V2_00017)
        """
        return self.addressing  # Delegates to property

    def setAddressing(self, value: CanTpAddressing) -> CanTpConnection:
        """
        AUTOSAR-compliant setter for addressing with method chaining.

        Args:
            value: The addressing to set

        Returns:
            self for method chaining

        Note:
            Delegates to addressing property setter (gets validation automatically)
        """
        self.addressing = value  # Delegates to property setter
        return self

    def getCancellation(self) -> Boolean:
        """
        AUTOSAR-compliant getter for cancellation.

        Returns:
            The cancellation value

        Note:
            Delegates to cancellation property (CODING_RULE_V2_00017)
        """
        return self.cancellation  # Delegates to property

    def setCancellation(self, value: Boolean) -> CanTpConnection:
        """
        AUTOSAR-compliant setter for cancellation with method chaining.

        Args:
            value: The cancellation to set

        Returns:
            self for method chaining

        Note:
            Delegates to cancellation property setter (gets validation automatically)
        """
        self.cancellation = value  # Delegates to property setter
        return self

    def getCanTpChannel(self) -> CanTpChannel:
        """
        AUTOSAR-compliant getter for canTpChannel.

        Returns:
            The canTpChannel value

        Note:
            Delegates to can_tp_channel property (CODING_RULE_V2_00017)
        """
        return self.can_tp_channel  # Delegates to property

    def setCanTpChannel(self, value: CanTpChannel) -> CanTpConnection:
        """
        AUTOSAR-compliant setter for canTpChannel with method chaining.

        Args:
            value: The canTpChannel to set

        Returns:
            self for method chaining

        Note:
            Delegates to can_tp_channel property setter (gets validation automatically)
        """
        self.can_tp_channel = value  # Delegates to property setter
        return self

    def getDataPdu(self) -> "NPdu":
        """
        AUTOSAR-compliant getter for dataPdu.

        Returns:
            The dataPdu value

        Note:
            Delegates to data_pdu property (CODING_RULE_V2_00017)
        """
        return self.data_pdu  # Delegates to property

    def setDataPdu(self, value: "NPdu") -> CanTpConnection:
        """
        AUTOSAR-compliant setter for dataPdu with method chaining.

        Args:
            value: The dataPdu to set

        Returns:
            self for method chaining

        Note:
            Delegates to data_pdu property setter (gets validation automatically)
        """
        self.data_pdu = value  # Delegates to property setter
        return self

    def getFlowControlPdu(self) -> "NPdu":
        """
        AUTOSAR-compliant getter for flowControlPdu.

        Returns:
            The flowControlPdu value

        Note:
            Delegates to flow_control_pdu property (CODING_RULE_V2_00017)
        """
        return self.flow_control_pdu  # Delegates to property

    def setFlowControlPdu(self, value: "NPdu") -> CanTpConnection:
        """
        AUTOSAR-compliant setter for flowControlPdu with method chaining.

        Args:
            value: The flowControlPdu to set

        Returns:
            self for method chaining

        Note:
            Delegates to flow_control_pdu property setter (gets validation automatically)
        """
        self.flow_control_pdu = value  # Delegates to property setter
        return self

    def getMaxBlockSize(self) -> Integer:
        """
        AUTOSAR-compliant getter for maxBlockSize.

        Returns:
            The maxBlockSize value

        Note:
            Delegates to max_block_size property (CODING_RULE_V2_00017)
        """
        return self.max_block_size  # Delegates to property

    def setMaxBlockSize(self, value: Integer) -> CanTpConnection:
        """
        AUTOSAR-compliant setter for maxBlockSize with method chaining.

        Args:
            value: The maxBlockSize to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_block_size property setter (gets validation automatically)
        """
        self.max_block_size = value  # Delegates to property setter
        return self

    def getMulticast(self) -> CanTpAddress:
        """
        AUTOSAR-compliant getter for multicast.

        Returns:
            The multicast value

        Note:
            Delegates to multicast property (CODING_RULE_V2_00017)
        """
        return self.multicast  # Delegates to property

    def setMulticast(self, value: CanTpAddress) -> CanTpConnection:
        """
        AUTOSAR-compliant setter for multicast with method chaining.

        Args:
            value: The multicast to set

        Returns:
            self for method chaining

        Note:
            Delegates to multicast property setter (gets validation automatically)
        """
        self.multicast = value  # Delegates to property setter
        return self

    def getPadding(self) -> Boolean:
        """
        AUTOSAR-compliant getter for padding.

        Returns:
            The padding value

        Note:
            Delegates to padding property (CODING_RULE_V2_00017)
        """
        return self.padding  # Delegates to property

    def setPadding(self, value: Boolean) -> CanTpConnection:
        """
        AUTOSAR-compliant setter for padding with method chaining.

        Args:
            value: The padding to set

        Returns:
            self for method chaining

        Note:
            Delegates to padding property setter (gets validation automatically)
        """
        self.padding = value  # Delegates to property setter
        return self

    def getReceiver(self) -> List[CanTpNode]:
        """
        AUTOSAR-compliant getter for receiver.

        Returns:
            The receiver value

        Note:
            Delegates to receiver property (CODING_RULE_V2_00017)
        """
        return self.receiver  # Delegates to property

    def getTaTypeType(self) -> "NetworkTargetAddress":
        """
        AUTOSAR-compliant getter for taTypeType.

        Returns:
            The taTypeType value

        Note:
            Delegates to ta_type_type property (CODING_RULE_V2_00017)
        """
        return self.ta_type_type  # Delegates to property

    def setTaTypeType(self, value: "NetworkTargetAddress") -> CanTpConnection:
        """
        AUTOSAR-compliant setter for taTypeType with method chaining.

        Args:
            value: The taTypeType to set

        Returns:
            self for method chaining

        Note:
            Delegates to ta_type_type property setter (gets validation automatically)
        """
        self.ta_type_type = value  # Delegates to property setter
        return self

    def getTimeoutBr(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for timeoutBr.

        Returns:
            The timeoutBr value

        Note:
            Delegates to timeout_br property (CODING_RULE_V2_00017)
        """
        return self.timeout_br  # Delegates to property

    def setTimeoutBr(self, value: TimeValue) -> CanTpConnection:
        """
        AUTOSAR-compliant setter for timeoutBr with method chaining.

        Args:
            value: The timeoutBr to set

        Returns:
            self for method chaining

        Note:
            Delegates to timeout_br property setter (gets validation automatically)
        """
        self.timeout_br = value  # Delegates to property setter
        return self

    def getTimeoutBs(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for timeoutBs.

        Returns:
            The timeoutBs value

        Note:
            Delegates to timeout_bs property (CODING_RULE_V2_00017)
        """
        return self.timeout_bs  # Delegates to property

    def setTimeoutBs(self, value: TimeValue) -> CanTpConnection:
        """
        AUTOSAR-compliant setter for timeoutBs with method chaining.

        Args:
            value: The timeoutBs to set

        Returns:
            self for method chaining

        Note:
            Delegates to timeout_bs property setter (gets validation automatically)
        """
        self.timeout_bs = value  # Delegates to property setter
        return self

    def getTimeoutCr(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for timeoutCr.

        Returns:
            The timeoutCr value

        Note:
            Delegates to timeout_cr property (CODING_RULE_V2_00017)
        """
        return self.timeout_cr  # Delegates to property

    def setTimeoutCr(self, value: TimeValue) -> CanTpConnection:
        """
        AUTOSAR-compliant setter for timeoutCr with method chaining.

        Args:
            value: The timeoutCr to set

        Returns:
            self for method chaining

        Note:
            Delegates to timeout_cr property setter (gets validation automatically)
        """
        self.timeout_cr = value  # Delegates to property setter
        return self

    def getTimeoutCs(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for timeoutCs.

        Returns:
            The timeoutCs value

        Note:
            Delegates to timeout_cs property (CODING_RULE_V2_00017)
        """
        return self.timeout_cs  # Delegates to property

    def setTimeoutCs(self, value: TimeValue) -> CanTpConnection:
        """
        AUTOSAR-compliant setter for timeoutCs with method chaining.

        Args:
            value: The timeoutCs to set

        Returns:
            self for method chaining

        Note:
            Delegates to timeout_cs property setter (gets validation automatically)
        """
        self.timeout_cs = value  # Delegates to property setter
        return self

    def getTpSdu(self) -> IPdu:
        """
        AUTOSAR-compliant getter for tpSdu.

        Returns:
            The tpSdu value

        Note:
            Delegates to tp_sdu property (CODING_RULE_V2_00017)
        """
        return self.tp_sdu  # Delegates to property

    def setTpSdu(self, value: IPdu) -> CanTpConnection:
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

    def getTransmitter(self) -> CanTpNode:
        """
        AUTOSAR-compliant getter for transmitter.

        Returns:
            The transmitter value

        Note:
            Delegates to transmitter property (CODING_RULE_V2_00017)
        """
        return self.transmitter  # Delegates to property

    def setTransmitter(self, value: CanTpNode) -> CanTpConnection:
        """
        AUTOSAR-compliant setter for transmitter with method chaining.

        Args:
            value: The transmitter to set

        Returns:
            self for method chaining

        Note:
            Delegates to transmitter property setter (gets validation automatically)
        """
        self.transmitter = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_addressing(self, value: Optional[CanTpAddressing]) -> CanTpConnection:
        """
        Set addressing and return self for chaining.

        Args:
            value: The addressing to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_addressing("value")
        """
        self.addressing = value  # Use property setter (gets validation)
        return self

    def with_cancellation(self, value: Optional[Boolean]) -> CanTpConnection:
        """
        Set cancellation and return self for chaining.

        Args:
            value: The cancellation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_cancellation("value")
        """
        self.cancellation = value  # Use property setter (gets validation)
        return self

    def with_can_tp_channel(self, value: Optional[CanTpChannel]) -> CanTpConnection:
        """
        Set canTpChannel and return self for chaining.

        Args:
            value: The canTpChannel to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_can_tp_channel("value")
        """
        self.can_tp_channel = value  # Use property setter (gets validation)
        return self

    def with_data_pdu(self, value: Optional["NPdu"]) -> CanTpConnection:
        """
        Set dataPdu and return self for chaining.

        Args:
            value: The dataPdu to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_data_pdu("value")
        """
        self.data_pdu = value  # Use property setter (gets validation)
        return self

    def with_flow_control_pdu(self, value: Optional["NPdu"]) -> CanTpConnection:
        """
        Set flowControlPdu and return self for chaining.

        Args:
            value: The flowControlPdu to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_flow_control_pdu("value")
        """
        self.flow_control_pdu = value  # Use property setter (gets validation)
        return self

    def with_max_block_size(self, value: Optional[Integer]) -> CanTpConnection:
        """
        Set maxBlockSize and return self for chaining.

        Args:
            value: The maxBlockSize to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_block_size("value")
        """
        self.max_block_size = value  # Use property setter (gets validation)
        return self

    def with_multicast(self, value: Optional[CanTpAddress]) -> CanTpConnection:
        """
        Set multicast and return self for chaining.

        Args:
            value: The multicast to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_multicast("value")
        """
        self.multicast = value  # Use property setter (gets validation)
        return self

    def with_padding(self, value: Optional[Boolean]) -> CanTpConnection:
        """
        Set padding and return self for chaining.

        Args:
            value: The padding to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_padding("value")
        """
        self.padding = value  # Use property setter (gets validation)
        return self

    def with_ta_type_type(self, value: Optional["NetworkTargetAddress"]) -> CanTpConnection:
        """
        Set taTypeType and return self for chaining.

        Args:
            value: The taTypeType to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ta_type_type("value")
        """
        self.ta_type_type = value  # Use property setter (gets validation)
        return self

    def with_timeout_br(self, value: Optional[TimeValue]) -> CanTpConnection:
        """
        Set timeoutBr and return self for chaining.

        Args:
            value: The timeoutBr to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_timeout_br("value")
        """
        self.timeout_br = value  # Use property setter (gets validation)
        return self

    def with_timeout_bs(self, value: Optional[TimeValue]) -> CanTpConnection:
        """
        Set timeoutBs and return self for chaining.

        Args:
            value: The timeoutBs to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_timeout_bs("value")
        """
        self.timeout_bs = value  # Use property setter (gets validation)
        return self

    def with_timeout_cr(self, value: Optional[TimeValue]) -> CanTpConnection:
        """
        Set timeoutCr and return self for chaining.

        Args:
            value: The timeoutCr to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_timeout_cr("value")
        """
        self.timeout_cr = value  # Use property setter (gets validation)
        return self

    def with_timeout_cs(self, value: Optional[TimeValue]) -> CanTpConnection:
        """
        Set timeoutCs and return self for chaining.

        Args:
            value: The timeoutCs to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_timeout_cs("value")
        """
        self.timeout_cs = value  # Use property setter (gets validation)
        return self

    def with_tp_sdu(self, value: Optional[IPdu]) -> CanTpConnection:
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

    def with_transmitter(self, value: Optional[CanTpNode]) -> CanTpConnection:
        """
        Set transmitter and return self for chaining.

        Args:
            value: The transmitter to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_transmitter("value")
        """
        self.transmitter = value  # Use property setter (gets validation)
        return self



class CanTpAddress(Identifiable):
    """
    An ECUs TP address on the referenced channel. This represents the diagnostic
    Address.

    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::CanTpAddress

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 610, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # If the mixed addressing format is used, this parameter the transport protocol
        # address extension value.
        self._tpAddress: Optional[Integer] = None

    @property
    def tp_address(self) -> Optional[Integer]:
        """Get tpAddress (Pythonic accessor)."""
        return self._tpAddress

    @tp_address.setter
    def tp_address(self, value: Optional[Integer]) -> None:
        """
        Set tpAddress with validation.

        Args:
            value: The tpAddress to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tpAddress = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"tpAddress must be Integer or int or None, got {type(value).__name__}"
            )
        self._tpAddress = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTpAddress(self) -> Integer:
        """
        AUTOSAR-compliant getter for tpAddress.

        Returns:
            The tpAddress value

        Note:
            Delegates to tp_address property (CODING_RULE_V2_00017)
        """
        return self.tp_address  # Delegates to property

    def setTpAddress(self, value: Integer) -> CanTpAddress:
        """
        AUTOSAR-compliant setter for tpAddress with method chaining.

        Args:
            value: The tpAddress to set

        Returns:
            self for method chaining

        Note:
            Delegates to tp_address property setter (gets validation automatically)
        """
        self.tp_address = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_tp_address(self, value: Optional[Integer]) -> CanTpAddress:
        """
        Set tpAddress and return self for chaining.

        Args:
            value: The tpAddress to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tp_address("value")
        """
        self.tp_address = value  # Use property setter (gets validation)
        return self



class CanTpEcu(ARObject):
    """
    ECU specific TP configuration parameters. Each TpEcu element has a reference
    to exactly one ECUInstance in the topology.

    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::CanTpEcu

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 610, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The period between successive calls to the Main Function the AUTOSAR TP.
        # Specified in seconds.
        self._cycleTimeMain: Optional[TimeValue] = None

    @property
    def cycle_time_main(self) -> Optional[TimeValue]:
        """Get cycleTimeMain (Pythonic accessor)."""
        return self._cycleTimeMain

    @cycle_time_main.setter
    def cycle_time_main(self, value: Optional[TimeValue]) -> None:
        """
        Set cycleTimeMain with validation.

        Args:
            value: The cycleTimeMain to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._cycleTimeMain = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"cycleTimeMain must be TimeValue or None, got {type(value).__name__}"
            )
        self._cycleTimeMain = value
        # Connection to the ECUInstance in the Topology.
        self._ecuInstance: Optional[EcuInstance] = None

    @property
    def ecu_instance(self) -> Optional[EcuInstance]:
        """Get ecuInstance (Pythonic accessor)."""
        return self._ecuInstance

    @ecu_instance.setter
    def ecu_instance(self, value: Optional[EcuInstance]) -> None:
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

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCycleTimeMain(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for cycleTimeMain.

        Returns:
            The cycleTimeMain value

        Note:
            Delegates to cycle_time_main property (CODING_RULE_V2_00017)
        """
        return self.cycle_time_main  # Delegates to property

    def setCycleTimeMain(self, value: TimeValue) -> CanTpEcu:
        """
        AUTOSAR-compliant setter for cycleTimeMain with method chaining.

        Args:
            value: The cycleTimeMain to set

        Returns:
            self for method chaining

        Note:
            Delegates to cycle_time_main property setter (gets validation automatically)
        """
        self.cycle_time_main = value  # Delegates to property setter
        return self

    def getEcuInstance(self) -> EcuInstance:
        """
        AUTOSAR-compliant getter for ecuInstance.

        Returns:
            The ecuInstance value

        Note:
            Delegates to ecu_instance property (CODING_RULE_V2_00017)
        """
        return self.ecu_instance  # Delegates to property

    def setEcuInstance(self, value: EcuInstance) -> CanTpEcu:
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

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_cycle_time_main(self, value: Optional[TimeValue]) -> CanTpEcu:
        """
        Set cycleTimeMain and return self for chaining.

        Args:
            value: The cycleTimeMain to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_cycle_time_main("value")
        """
        self.cycle_time_main = value  # Use property setter (gets validation)
        return self

    def with_ecu_instance(self, value: Optional[EcuInstance]) -> CanTpEcu:
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



class CanTpNode(Identifiable):
    """
    TP Node (Sender or Receiver) provides the TP Address and the connection to
    the Topology description.

    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::CanTpNode

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 611, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Association to a CommunicationConnector in the description.
        # In a System Description this mandatory.
        # In an ECU Extract this reference (references to ECUs that are not part of the
                # shall be avoided).
        self._connector: Optional[Communication] = None

    @property
    def connector(self) -> Optional[Communication]:
        """Get connector (Pythonic accessor)."""
        return self._connector

    @connector.setter
    def connector(self, value: Optional[Communication]) -> None:
        """
        Set connector with validation.

        Args:
            value: The connector to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._connector = None
            return

        if not isinstance(value, Communication):
            raise TypeError(
                f"connector must be Communication or None, got {type(value).__name__}"
            )
        self._connector = value
        # This attribute defines the maximum number of flow control can be
        # consecutively be transmitted by a.
        self._maxFcWait: Optional[Integer] = None

    @property
    def max_fc_wait(self) -> Optional[Integer]:
        """Get maxFcWait (Pythonic accessor)."""
        return self._maxFcWait

    @max_fc_wait.setter
    def max_fc_wait(self, value: Optional[Integer]) -> None:
        """
        Set maxFcWait with validation.

        Args:
            value: The maxFcWait to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxFcWait = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"maxFcWait must be Integer or int or None, got {type(value).__name__}"
            )
        self._maxFcWait = value
        # Sets the duration of the minimum time the CanTp sender between the
        # transmissions of two CF N-PDUs.
        self._stMin: Optional[TimeValue] = None

    @property
    def st_min(self) -> Optional[TimeValue]:
        """Get stMin (Pythonic accessor)."""
        return self._stMin

    @st_min.setter
    def st_min(self, value: Optional[TimeValue]) -> None:
        """
        Set stMin with validation.

        Args:
            value: The stMin to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._stMin = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"stMin must be TimeValue or None, got {type(value).__name__}"
            )
        self._stMin = value
        # This attribute states the timeout between the PDU of the Transport Layer to
                # the Can the corresponding confirmation of the Can the receiver side (for FC
                # or AF).
        # Specified in.
        self._timeoutAr: Optional[TimeValue] = None

    @property
    def timeout_ar(self) -> Optional[TimeValue]:
        """Get timeoutAr (Pythonic accessor)."""
        return self._timeoutAr

    @timeout_ar.setter
    def timeout_ar(self, value: Optional[TimeValue]) -> None:
        """
        Set timeoutAr with validation.

        Args:
            value: The timeoutAr to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeoutAr = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"timeoutAr must be TimeValue or None, got {type(value).__name__}"
            )
        self._timeoutAr = value
        # This attribute states the timeout between the PDU for the first PDU of the
                # group used in the of the Transport Layer to the Can the corresponding
                # confirmation of the Can having sent the last PDU of the group this
                # connection) on the sender side (SF-x, FF-x, FC (in case of Transmit
                # Cancellation)).
        # Specified in.
        self._timeoutAs: Optional[TimeValue] = None

    @property
    def timeout_as(self) -> Optional[TimeValue]:
        """Get timeoutAs (Pythonic accessor)."""
        return self._timeoutAs

    @timeout_as.setter
    def timeout_as(self, value: Optional[TimeValue]) -> None:
        """
        Set timeoutAs with validation.

        Args:
            value: The timeoutAs to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeoutAs = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"timeoutAs must be TimeValue or None, got {type(value).__name__}"
            )
        self._timeoutAs = value
        # Reference to the TP Address that is used by the TpNode.
        # is optional in case that the multicast TP used (reference from TpConnection).
        self._tpAddress: Optional[CanTpAddress] = None

    @property
    def tp_address(self) -> Optional[CanTpAddress]:
        """Get tpAddress (Pythonic accessor)."""
        return self._tpAddress

    @tp_address.setter
    def tp_address(self, value: Optional[CanTpAddress]) -> None:
        """
        Set tpAddress with validation.

        Args:
            value: The tpAddress to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tpAddress = None
            return

        if not isinstance(value, CanTpAddress):
            raise TypeError(
                f"tpAddress must be CanTpAddress or None, got {type(value).__name__}"
            )
        self._tpAddress = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getConnector(self) -> Communication:
        """
        AUTOSAR-compliant getter for connector.

        Returns:
            The connector value

        Note:
            Delegates to connector property (CODING_RULE_V2_00017)
        """
        return self.connector  # Delegates to property

    def setConnector(self, value: Communication) -> CanTpNode:
        """
        AUTOSAR-compliant setter for connector with method chaining.

        Args:
            value: The connector to set

        Returns:
            self for method chaining

        Note:
            Delegates to connector property setter (gets validation automatically)
        """
        self.connector = value  # Delegates to property setter
        return self

    def getMaxFcWait(self) -> Integer:
        """
        AUTOSAR-compliant getter for maxFcWait.

        Returns:
            The maxFcWait value

        Note:
            Delegates to max_fc_wait property (CODING_RULE_V2_00017)
        """
        return self.max_fc_wait  # Delegates to property

    def setMaxFcWait(self, value: Integer) -> CanTpNode:
        """
        AUTOSAR-compliant setter for maxFcWait with method chaining.

        Args:
            value: The maxFcWait to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_fc_wait property setter (gets validation automatically)
        """
        self.max_fc_wait = value  # Delegates to property setter
        return self

    def getStMin(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for stMin.

        Returns:
            The stMin value

        Note:
            Delegates to st_min property (CODING_RULE_V2_00017)
        """
        return self.st_min  # Delegates to property

    def setStMin(self, value: TimeValue) -> CanTpNode:
        """
        AUTOSAR-compliant setter for stMin with method chaining.

        Args:
            value: The stMin to set

        Returns:
            self for method chaining

        Note:
            Delegates to st_min property setter (gets validation automatically)
        """
        self.st_min = value  # Delegates to property setter
        return self

    def getTimeoutAr(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for timeoutAr.

        Returns:
            The timeoutAr value

        Note:
            Delegates to timeout_ar property (CODING_RULE_V2_00017)
        """
        return self.timeout_ar  # Delegates to property

    def setTimeoutAr(self, value: TimeValue) -> CanTpNode:
        """
        AUTOSAR-compliant setter for timeoutAr with method chaining.

        Args:
            value: The timeoutAr to set

        Returns:
            self for method chaining

        Note:
            Delegates to timeout_ar property setter (gets validation automatically)
        """
        self.timeout_ar = value  # Delegates to property setter
        return self

    def getTimeoutAs(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for timeoutAs.

        Returns:
            The timeoutAs value

        Note:
            Delegates to timeout_as property (CODING_RULE_V2_00017)
        """
        return self.timeout_as  # Delegates to property

    def setTimeoutAs(self, value: TimeValue) -> CanTpNode:
        """
        AUTOSAR-compliant setter for timeoutAs with method chaining.

        Args:
            value: The timeoutAs to set

        Returns:
            self for method chaining

        Note:
            Delegates to timeout_as property setter (gets validation automatically)
        """
        self.timeout_as = value  # Delegates to property setter
        return self

    def getTpAddress(self) -> CanTpAddress:
        """
        AUTOSAR-compliant getter for tpAddress.

        Returns:
            The tpAddress value

        Note:
            Delegates to tp_address property (CODING_RULE_V2_00017)
        """
        return self.tp_address  # Delegates to property

    def setTpAddress(self, value: CanTpAddress) -> CanTpNode:
        """
        AUTOSAR-compliant setter for tpAddress with method chaining.

        Args:
            value: The tpAddress to set

        Returns:
            self for method chaining

        Note:
            Delegates to tp_address property setter (gets validation automatically)
        """
        self.tp_address = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_connector(self, value: Optional[Communication]) -> CanTpNode:
        """
        Set connector and return self for chaining.

        Args:
            value: The connector to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_connector("value")
        """
        self.connector = value  # Use property setter (gets validation)
        return self

    def with_max_fc_wait(self, value: Optional[Integer]) -> CanTpNode:
        """
        Set maxFcWait and return self for chaining.

        Args:
            value: The maxFcWait to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_fc_wait("value")
        """
        self.max_fc_wait = value  # Use property setter (gets validation)
        return self

    def with_st_min(self, value: Optional[TimeValue]) -> CanTpNode:
        """
        Set stMin and return self for chaining.

        Args:
            value: The stMin to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_st_min("value")
        """
        self.st_min = value  # Use property setter (gets validation)
        return self

    def with_timeout_ar(self, value: Optional[TimeValue]) -> CanTpNode:
        """
        Set timeoutAr and return self for chaining.

        Args:
            value: The timeoutAr to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_timeout_ar("value")
        """
        self.timeout_ar = value  # Use property setter (gets validation)
        return self

    def with_timeout_as(self, value: Optional[TimeValue]) -> CanTpNode:
        """
        Set timeoutAs and return self for chaining.

        Args:
            value: The timeoutAs to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_timeout_as("value")
        """
        self.timeout_as = value  # Use property setter (gets validation)
        return self

    def with_tp_address(self, value: Optional[CanTpAddress]) -> CanTpNode:
        """
        Set tpAddress and return self for chaining.

        Args:
            value: The tpAddress to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tp_address("value")
        """
        self.tp_address = value  # Use property setter (gets validation)
        return self



class LinTpNode(Identifiable):
    """
    TP Node (Sender or Receiver) provides the TP Address and the connection to
    the Topology description.

    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::LinTpNode

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 614, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Association to a CommunicationConnector in the description.
        # System Description this reference is mandatory.
        # In Extract this reference is optional (references to are not part of the ECU
                # Extract shall be.
        self._connector: Optional[Communication] = None

    @property
    def connector(self) -> Optional[Communication]:
        """Get connector (Pythonic accessor)."""
        return self._connector

    @connector.setter
    def connector(self, value: Optional[Communication]) -> None:
        """
        Set connector with validation.

        Args:
            value: The connector to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._connector = None
            return

        if not isinstance(value, Communication):
            raise TypeError(
                f"connector must be Communication or None, got {type(value).__name__}"
            )
        self._connector = value
        # Configures if TP Frames of not requested LIN-Slaves are or not.
        # 2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._dropNot: Optional[Boolean] = None

    @property
    def drop_not(self) -> Optional[Boolean]:
        """Get dropNot (Pythonic accessor)."""
        return self._dropNot

    @drop_not.setter
    def drop_not(self, value: Optional[Boolean]) -> None:
        """
        Set dropNot with validation.

        Args:
            value: The dropNot to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dropNot = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"dropNot must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._dropNot = value
        # Configures the maximum number of allowed response frames.
        self._maxNumberOf: Optional[Integer] = None

    @property
    def max_number_of(self) -> Optional[Integer]:
        """Get maxNumberOf (Pythonic accessor)."""
        return self._maxNumberOf

    @max_number_of.setter
    def max_number_of(self, value: Optional[Integer]) -> None:
        """
        Set maxNumberOf with validation.

        Args:
            value: The maxNumberOf to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxNumberOf = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"maxNumberOf must be Integer or int or None, got {type(value).__name__}"
            )
        self._maxNumberOf = value
        # After reception of a response pending frame the P2 is reloaded with the
        # timeout time P2max.
        self._p2Max: Optional[TimeValue] = None

    @property
    def p2_max(self) -> Optional[TimeValue]:
        """Get p2Max (Pythonic accessor)."""
        return self._p2Max

    @p2_max.setter
    def p2_max(self, value: Optional[TimeValue]) -> None:
        """
        Set p2Max with validation.

        Args:
            value: The p2Max to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._p2Max = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"p2Max must be TimeValue or None, got {type(value).__name__}"
            )
        self._p2Max = value
        # P2 timeout observation parameter.
        self._p2Timing: Optional[TimeValue] = None

    @property
    def p2_timing(self) -> Optional[TimeValue]:
        """Get p2Timing (Pythonic accessor)."""
        return self._p2Timing

    @p2_timing.setter
    def p2_timing(self, value: Optional[TimeValue]) -> None:
        """
        Set p2Timing with validation.

        Args:
            value: The p2Timing to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._p2Timing = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"p2Timing must be TimeValue or None, got {type(value).__name__}"
            )
        self._p2Timing = value
        # Reference to the TP Address that is used by the TpNode.
        # is optional in case that the multicast TP used (reference from TpConnection).
        self._tpAddress: Optional[TpAddress] = None

    @property
    def tp_address(self) -> Optional[TpAddress]:
        """Get tpAddress (Pythonic accessor)."""
        return self._tpAddress

    @tp_address.setter
    def tp_address(self, value: Optional[TpAddress]) -> None:
        """
        Set tpAddress with validation.

        Args:
            value: The tpAddress to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tpAddress = None
            return

        if not isinstance(value, TpAddress):
            raise TypeError(
                f"tpAddress must be TpAddress or None, got {type(value).__name__}"
            )
        self._tpAddress = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getConnector(self) -> Communication:
        """
        AUTOSAR-compliant getter for connector.

        Returns:
            The connector value

        Note:
            Delegates to connector property (CODING_RULE_V2_00017)
        """
        return self.connector  # Delegates to property

    def setConnector(self, value: Communication) -> LinTpNode:
        """
        AUTOSAR-compliant setter for connector with method chaining.

        Args:
            value: The connector to set

        Returns:
            self for method chaining

        Note:
            Delegates to connector property setter (gets validation automatically)
        """
        self.connector = value  # Delegates to property setter
        return self

    def getDropNot(self) -> Boolean:
        """
        AUTOSAR-compliant getter for dropNot.

        Returns:
            The dropNot value

        Note:
            Delegates to drop_not property (CODING_RULE_V2_00017)
        """
        return self.drop_not  # Delegates to property

    def setDropNot(self, value: Boolean) -> LinTpNode:
        """
        AUTOSAR-compliant setter for dropNot with method chaining.

        Args:
            value: The dropNot to set

        Returns:
            self for method chaining

        Note:
            Delegates to drop_not property setter (gets validation automatically)
        """
        self.drop_not = value  # Delegates to property setter
        return self

    def getMaxNumberOf(self) -> Integer:
        """
        AUTOSAR-compliant getter for maxNumberOf.

        Returns:
            The maxNumberOf value

        Note:
            Delegates to max_number_of property (CODING_RULE_V2_00017)
        """
        return self.max_number_of  # Delegates to property

    def setMaxNumberOf(self, value: Integer) -> LinTpNode:
        """
        AUTOSAR-compliant setter for maxNumberOf with method chaining.

        Args:
            value: The maxNumberOf to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_number_of property setter (gets validation automatically)
        """
        self.max_number_of = value  # Delegates to property setter
        return self

    def getP2Max(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for p2Max.

        Returns:
            The p2Max value

        Note:
            Delegates to p2_max property (CODING_RULE_V2_00017)
        """
        return self.p2_max  # Delegates to property

    def setP2Max(self, value: TimeValue) -> LinTpNode:
        """
        AUTOSAR-compliant setter for p2Max with method chaining.

        Args:
            value: The p2Max to set

        Returns:
            self for method chaining

        Note:
            Delegates to p2_max property setter (gets validation automatically)
        """
        self.p2_max = value  # Delegates to property setter
        return self

    def getP2Timing(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for p2Timing.

        Returns:
            The p2Timing value

        Note:
            Delegates to p2_timing property (CODING_RULE_V2_00017)
        """
        return self.p2_timing  # Delegates to property

    def setP2Timing(self, value: TimeValue) -> LinTpNode:
        """
        AUTOSAR-compliant setter for p2Timing with method chaining.

        Args:
            value: The p2Timing to set

        Returns:
            self for method chaining

        Note:
            Delegates to p2_timing property setter (gets validation automatically)
        """
        self.p2_timing = value  # Delegates to property setter
        return self

    def getTpAddress(self) -> TpAddress:
        """
        AUTOSAR-compliant getter for tpAddress.

        Returns:
            The tpAddress value

        Note:
            Delegates to tp_address property (CODING_RULE_V2_00017)
        """
        return self.tp_address  # Delegates to property

    def setTpAddress(self, value: TpAddress) -> LinTpNode:
        """
        AUTOSAR-compliant setter for tpAddress with method chaining.

        Args:
            value: The tpAddress to set

        Returns:
            self for method chaining

        Note:
            Delegates to tp_address property setter (gets validation automatically)
        """
        self.tp_address = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_connector(self, value: Optional[Communication]) -> LinTpNode:
        """
        Set connector and return self for chaining.

        Args:
            value: The connector to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_connector("value")
        """
        self.connector = value  # Use property setter (gets validation)
        return self

    def with_drop_not(self, value: Optional[Boolean]) -> LinTpNode:
        """
        Set dropNot and return self for chaining.

        Args:
            value: The dropNot to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_drop_not("value")
        """
        self.drop_not = value  # Use property setter (gets validation)
        return self

    def with_max_number_of(self, value: Optional[Integer]) -> LinTpNode:
        """
        Set maxNumberOf and return self for chaining.

        Args:
            value: The maxNumberOf to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_number_of("value")
        """
        self.max_number_of = value  # Use property setter (gets validation)
        return self

    def with_p2_max(self, value: Optional[TimeValue]) -> LinTpNode:
        """
        Set p2Max and return self for chaining.

        Args:
            value: The p2Max to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_p2_max("value")
        """
        self.p2_max = value  # Use property setter (gets validation)
        return self

    def with_p2_timing(self, value: Optional[TimeValue]) -> LinTpNode:
        """
        Set p2Timing and return self for chaining.

        Args:
            value: The p2Timing to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_p2_timing("value")
        """
        self.p2_timing = value  # Use property setter (gets validation)
        return self

    def with_tp_address(self, value: Optional[TpAddress]) -> LinTpNode:
        """
        Set tpAddress and return self for chaining.

        Args:
            value: The tpAddress to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tp_address("value")
        """
        self.tp_address = value  # Use property setter (gets validation)
        return self



class LinTpConnection(TpConnection):
    """
    A LinTP channel represents an internal path for the transmission or
    reception of a Pdu via LinTp and describes the sender and the receiver of
    this particular communication. LinTp supports (per Lin Cluster) the
    configuration of one Rx Tp-SDU and one Tx Tp-SDU per NAD the LinMaster uses
    to address one or more of its Lin Slaves. To support this an arbitrary
    number of LinTp Connections shall be described.

    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::LinTpConnection

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 615, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to an NPdu (Single Frame, First Frame or Frame network protocol
                # data unit (SF N_PDU) sent out by the sending network entity and can by one or
                # multiple receiving network entities.
        # Frame (SF N_PDU) shall be sent out to service data unit that can be
                # transferred via a request to the data link layer.
        # This network unit shall be sent to transfer unsegmented Frame network
                # protocol data unit (FF N_PDU) first network protocol data unit (N_PDU) of a
                # transmitted by a network sending received by a receiving network entity.
        # Frame network protocol data unit (CF segments (N_Data) of the service data
                # data (<MessageData>).
        # All network units (N_PDUs) transmitted by the sending the First Frame network
                # protocol data unit (FF be encoded as Consecutive Frames data units (CF
                # N_PDUs).
        # 2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._dataPdu: Optional["NPdu"] = None

    @property
    def data_pdu(self) -> Optional["NPdu"]:
        """Get dataPdu (Pythonic accessor)."""
        return self._dataPdu

    @data_pdu.setter
    def data_pdu(self, value: Optional["NPdu"]) -> None:
        """
        Set dataPdu with validation.

        Args:
            value: The dataPdu to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dataPdu = None
            return

        if not isinstance(value, NPdu):
            raise TypeError(
                f"dataPdu must be NPdu or None, got {type(value).__name__}"
            )
        self._dataPdu = value
        # Reference to the Flow Control NPdu.
        # Control network protocol data unit (FC N_PDU) by the Flow Control protocol
                # control N_PCI).
        # The Flow Control network unit (FC N_PDU) instructs a sending to start, stop
                # or resume transmission of CF Flow Control network protocol data unit sent by
                # the receiving network layer entity to the layer entity, when ready to receive
                # more correct reception of: Frame network protocol data unit (FF N_PDU) last
                # Consecutive Frame network protocol data unit of a block of Consecutive Frames
                # (CF N_ further Consecutive Frame network protocol data N_PDU) need(s) to be
                # sent.
        self._flowControl: Optional["NPdu"] = None

    @property
    def flow_control(self) -> Optional["NPdu"]:
        """Get flowControl (Pythonic accessor)."""
        return self._flowControl

    @flow_control.setter
    def flow_control(self, value: Optional["NPdu"]) -> None:
        """
        Set flowControl with validation.

        Args:
            value: The flowControl to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._flowControl = None
            return

        if not isinstance(value, NPdu):
            raise TypeError(
                f"flowControl must be NPdu or None, got {type(value).__name__}"
            )
        self._flowControl = value
        # Reference to the IPdu that is segmented by the Transport.
        self._linTpNSdu: Optional[IPdu] = None

    @property
    def lin_tp_n_sdu(self) -> Optional[IPdu]:
        """Get linTpNSdu (Pythonic accessor)."""
        return self._linTpNSdu

    @lin_tp_n_sdu.setter
    def lin_tp_n_sdu(self, value: Optional[IPdu]) -> None:
        """
        Set linTpNSdu with validation.

        Args:
            value: The linTpNSdu to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._linTpNSdu = None
            return

        if not isinstance(value, IPdu):
            raise TypeError(
                f"linTpNSdu must be IPdu or None, got {type(value).__name__}"
            )
        self._linTpNSdu = value
        # TP address for 1:n connections.
        self._multicast: Optional[TpAddress] = None

    @property
    def multicast(self) -> Optional[TpAddress]:
        """Get multicast (Pythonic accessor)."""
        return self._multicast

    @multicast.setter
    def multicast(self, value: Optional[TpAddress]) -> None:
        """
        Set multicast with validation.

        Args:
            value: The multicast to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._multicast = None
            return

        if not isinstance(value, TpAddress):
            raise TypeError(
                f"multicast must be TpAddress or None, got {type(value).__name__}"
            )
        self._multicast = value
        # The target of the TP connection.
        self._receiver: List[LinTpNode] = []

    @property
    def receiver(self) -> List[LinTpNode]:
        """Get receiver (Pythonic accessor)."""
        return self._receiver
        # Time for transmission of the LIN frame (any N-PDU) on side.
        # Specified in seconds.
        self._timeoutAs: Optional[TimeValue] = None

    @property
    def timeout_as(self) -> Optional[TimeValue]:
        """Get timeoutAs (Pythonic accessor)."""
        return self._timeoutAs

    @timeout_as.setter
    def timeout_as(self, value: Optional[TimeValue]) -> None:
        """
        Set timeoutAs with validation.

        Args:
            value: The timeoutAs to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeoutAs = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"timeoutAs must be TimeValue or None, got {type(value).__name__}"
            )
        self._timeoutAs = value
        # This attribute defines the timeout value for waiting for a FF-x (in case of
                # retry) after receiving the last CF or an FC or AF on the receiver side.
        # Specified.
        self._timeoutCr: Optional[TimeValue] = None

    @property
    def timeout_cr(self) -> Optional[TimeValue]:
        """Get timeoutCr (Pythonic accessor)."""
        return self._timeoutCr

    @timeout_cr.setter
    def timeout_cr(self, value: Optional[TimeValue]) -> None:
        """
        Set timeoutCr with validation.

        Args:
            value: The timeoutCr to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeoutCr = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"timeoutCr must be TimeValue or None, got {type(value).__name__}"
            )
        self._timeoutCr = value
        # The attribute timeoutCs represents the time (in seconds) between the transmit
        # request of a CF the transmit request of the next CF N-PDU.
        self._timeoutCs: Optional[TimeValue] = None

    @property
    def timeout_cs(self) -> Optional[TimeValue]:
        """Get timeoutCs (Pythonic accessor)."""
        return self._timeoutCs

    @timeout_cs.setter
    def timeout_cs(self, value: Optional[TimeValue]) -> None:
        """
        Set timeoutCs with validation.

        Args:
            value: The timeoutCs to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeoutCs = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"timeoutCs must be TimeValue or None, got {type(value).__name__}"
            )
        self._timeoutCs = value
        # The source of the TP connection.
        self._transmitter: Optional[LinTpNode] = None

    @property
    def transmitter(self) -> Optional[LinTpNode]:
        """Get transmitter (Pythonic accessor)."""
        return self._transmitter

    @transmitter.setter
    def transmitter(self, value: Optional[LinTpNode]) -> None:
        """
        Set transmitter with validation.

        Args:
            value: The transmitter to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._transmitter = None
            return

        if not isinstance(value, LinTpNode):
            raise TypeError(
                f"transmitter must be LinTpNode or None, got {type(value).__name__}"
            )
        self._transmitter = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDataPdu(self) -> "NPdu":
        """
        AUTOSAR-compliant getter for dataPdu.

        Returns:
            The dataPdu value

        Note:
            Delegates to data_pdu property (CODING_RULE_V2_00017)
        """
        return self.data_pdu  # Delegates to property

    def setDataPdu(self, value: "NPdu") -> LinTpConnection:
        """
        AUTOSAR-compliant setter for dataPdu with method chaining.

        Args:
            value: The dataPdu to set

        Returns:
            self for method chaining

        Note:
            Delegates to data_pdu property setter (gets validation automatically)
        """
        self.data_pdu = value  # Delegates to property setter
        return self

    def getFlowControl(self) -> "NPdu":
        """
        AUTOSAR-compliant getter for flowControl.

        Returns:
            The flowControl value

        Note:
            Delegates to flow_control property (CODING_RULE_V2_00017)
        """
        return self.flow_control  # Delegates to property

    def setFlowControl(self, value: "NPdu") -> LinTpConnection:
        """
        AUTOSAR-compliant setter for flowControl with method chaining.

        Args:
            value: The flowControl to set

        Returns:
            self for method chaining

        Note:
            Delegates to flow_control property setter (gets validation automatically)
        """
        self.flow_control = value  # Delegates to property setter
        return self

    def getLinTpNSdu(self) -> IPdu:
        """
        AUTOSAR-compliant getter for linTpNSdu.

        Returns:
            The linTpNSdu value

        Note:
            Delegates to lin_tp_n_sdu property (CODING_RULE_V2_00017)
        """
        return self.lin_tp_n_sdu  # Delegates to property

    def setLinTpNSdu(self, value: IPdu) -> LinTpConnection:
        """
        AUTOSAR-compliant setter for linTpNSdu with method chaining.

        Args:
            value: The linTpNSdu to set

        Returns:
            self for method chaining

        Note:
            Delegates to lin_tp_n_sdu property setter (gets validation automatically)
        """
        self.lin_tp_n_sdu = value  # Delegates to property setter
        return self

    def getMulticast(self) -> TpAddress:
        """
        AUTOSAR-compliant getter for multicast.

        Returns:
            The multicast value

        Note:
            Delegates to multicast property (CODING_RULE_V2_00017)
        """
        return self.multicast  # Delegates to property

    def setMulticast(self, value: TpAddress) -> LinTpConnection:
        """
        AUTOSAR-compliant setter for multicast with method chaining.

        Args:
            value: The multicast to set

        Returns:
            self for method chaining

        Note:
            Delegates to multicast property setter (gets validation automatically)
        """
        self.multicast = value  # Delegates to property setter
        return self

    def getReceiver(self) -> List[LinTpNode]:
        """
        AUTOSAR-compliant getter for receiver.

        Returns:
            The receiver value

        Note:
            Delegates to receiver property (CODING_RULE_V2_00017)
        """
        return self.receiver  # Delegates to property

    def getTimeoutAs(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for timeoutAs.

        Returns:
            The timeoutAs value

        Note:
            Delegates to timeout_as property (CODING_RULE_V2_00017)
        """
        return self.timeout_as  # Delegates to property

    def setTimeoutAs(self, value: TimeValue) -> LinTpConnection:
        """
        AUTOSAR-compliant setter for timeoutAs with method chaining.

        Args:
            value: The timeoutAs to set

        Returns:
            self for method chaining

        Note:
            Delegates to timeout_as property setter (gets validation automatically)
        """
        self.timeout_as = value  # Delegates to property setter
        return self

    def getTimeoutCr(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for timeoutCr.

        Returns:
            The timeoutCr value

        Note:
            Delegates to timeout_cr property (CODING_RULE_V2_00017)
        """
        return self.timeout_cr  # Delegates to property

    def setTimeoutCr(self, value: TimeValue) -> LinTpConnection:
        """
        AUTOSAR-compliant setter for timeoutCr with method chaining.

        Args:
            value: The timeoutCr to set

        Returns:
            self for method chaining

        Note:
            Delegates to timeout_cr property setter (gets validation automatically)
        """
        self.timeout_cr = value  # Delegates to property setter
        return self

    def getTimeoutCs(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for timeoutCs.

        Returns:
            The timeoutCs value

        Note:
            Delegates to timeout_cs property (CODING_RULE_V2_00017)
        """
        return self.timeout_cs  # Delegates to property

    def setTimeoutCs(self, value: TimeValue) -> LinTpConnection:
        """
        AUTOSAR-compliant setter for timeoutCs with method chaining.

        Args:
            value: The timeoutCs to set

        Returns:
            self for method chaining

        Note:
            Delegates to timeout_cs property setter (gets validation automatically)
        """
        self.timeout_cs = value  # Delegates to property setter
        return self

    def getTransmitter(self) -> LinTpNode:
        """
        AUTOSAR-compliant getter for transmitter.

        Returns:
            The transmitter value

        Note:
            Delegates to transmitter property (CODING_RULE_V2_00017)
        """
        return self.transmitter  # Delegates to property

    def setTransmitter(self, value: LinTpNode) -> LinTpConnection:
        """
        AUTOSAR-compliant setter for transmitter with method chaining.

        Args:
            value: The transmitter to set

        Returns:
            self for method chaining

        Note:
            Delegates to transmitter property setter (gets validation automatically)
        """
        self.transmitter = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_data_pdu(self, value: Optional["NPdu"]) -> LinTpConnection:
        """
        Set dataPdu and return self for chaining.

        Args:
            value: The dataPdu to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_data_pdu("value")
        """
        self.data_pdu = value  # Use property setter (gets validation)
        return self

    def with_flow_control(self, value: Optional["NPdu"]) -> LinTpConnection:
        """
        Set flowControl and return self for chaining.

        Args:
            value: The flowControl to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_flow_control("value")
        """
        self.flow_control = value  # Use property setter (gets validation)
        return self

    def with_lin_tp_n_sdu(self, value: Optional[IPdu]) -> LinTpConnection:
        """
        Set linTpNSdu and return self for chaining.

        Args:
            value: The linTpNSdu to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_lin_tp_n_sdu("value")
        """
        self.lin_tp_n_sdu = value  # Use property setter (gets validation)
        return self

    def with_multicast(self, value: Optional[TpAddress]) -> LinTpConnection:
        """
        Set multicast and return self for chaining.

        Args:
            value: The multicast to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_multicast("value")
        """
        self.multicast = value  # Use property setter (gets validation)
        return self

    def with_timeout_as(self, value: Optional[TimeValue]) -> LinTpConnection:
        """
        Set timeoutAs and return self for chaining.

        Args:
            value: The timeoutAs to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_timeout_as("value")
        """
        self.timeout_as = value  # Use property setter (gets validation)
        return self

    def with_timeout_cr(self, value: Optional[TimeValue]) -> LinTpConnection:
        """
        Set timeoutCr and return self for chaining.

        Args:
            value: The timeoutCr to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_timeout_cr("value")
        """
        self.timeout_cr = value  # Use property setter (gets validation)
        return self

    def with_timeout_cs(self, value: Optional[TimeValue]) -> LinTpConnection:
        """
        Set timeoutCs and return self for chaining.

        Args:
            value: The timeoutCs to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_timeout_cs("value")
        """
        self.timeout_cs = value  # Use property setter (gets validation)
        return self

    def with_transmitter(self, value: Optional[LinTpNode]) -> LinTpConnection:
        """
        Set transmitter and return self for chaining.

        Args:
            value: The transmitter to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_transmitter("value")
        """
        self.transmitter = value  # Use property setter (gets validation)
        return self



class EthTpConnection(TpConnection):
    """
    A connection identifies which PduTriggerings shall be handled using the "TP"
    semantics.

    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::EthTpConnection

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 618, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to a PduTriggering that shall be transported "TP" semantics.
        self._tpSdu: List[RefType] = []

    @property
    def tp_sdu(self) -> List[RefType]:
        """Get tpSdu (Pythonic accessor)."""
        return self._tpSdu

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTpSdu(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for tpSdu.

        Returns:
            The tpSdu value

        Note:
            Delegates to tp_sdu property (CODING_RULE_V2_00017)
        """
        return self.tp_sdu  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class SomeipTpConnection(ARObject):
    """
    A connection identifies the sender and the receiver of this particular
    communication. The SOME/IP TP module routes a Pdu through this connection.

    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::SomeipTpConnection

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 620, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Assignment of configuration properties valid for this.
        self._tpChannel: Optional[SomeipTpChannel] = None

    @property
    def tp_channel(self) -> Optional[SomeipTpChannel]:
        """Get tpChannel (Pythonic accessor)."""
        return self._tpChannel

    @tp_channel.setter
    def tp_channel(self, value: Optional[SomeipTpChannel]) -> None:
        """
        Set tpChannel with validation.

        Args:
            value: The tpChannel to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tpChannel = None
            return

        if not isinstance(value, SomeipTpChannel):
            raise TypeError(
                f"tpChannel must be SomeipTpChannel or None, got {type(value).__name__}"
            )
        self._tpChannel = value
        # Reference to an IPdu that is segmented by the Transport.
        self._tpSdu: Optional[RefType] = None

    @property
    def tp_sdu(self) -> Optional[RefType]:
        """Get tpSdu (Pythonic accessor)."""
        return self._tpSdu

    @tp_sdu.setter
    def tp_sdu(self, value: Optional[RefType]) -> None:
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
        # Reference to the segmented IPdu.
        self._transportPdu: Optional[RefType] = None

    @property
    def transport_pdu(self) -> Optional[RefType]:
        """Get transportPdu (Pythonic accessor)."""
        return self._transportPdu

    @transport_pdu.setter
    def transport_pdu(self, value: Optional[RefType]) -> None:
        """
        Set transportPdu with validation.

        Args:
            value: The transportPdu to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._transportPdu = None
            return

        self._transportPdu = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTpChannel(self) -> SomeipTpChannel:
        """
        AUTOSAR-compliant getter for tpChannel.

        Returns:
            The tpChannel value

        Note:
            Delegates to tp_channel property (CODING_RULE_V2_00017)
        """
        return self.tp_channel  # Delegates to property

    def setTpChannel(self, value: SomeipTpChannel) -> SomeipTpConnection:
        """
        AUTOSAR-compliant setter for tpChannel with method chaining.

        Args:
            value: The tpChannel to set

        Returns:
            self for method chaining

        Note:
            Delegates to tp_channel property setter (gets validation automatically)
        """
        self.tp_channel = value  # Delegates to property setter
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

    def setTpSdu(self, value: RefType) -> SomeipTpConnection:
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

    def getTransportPdu(self) -> RefType:
        """
        AUTOSAR-compliant getter for transportPdu.

        Returns:
            The transportPdu value

        Note:
            Delegates to transport_pdu property (CODING_RULE_V2_00017)
        """
        return self.transport_pdu  # Delegates to property

    def setTransportPdu(self, value: RefType) -> SomeipTpConnection:
        """
        AUTOSAR-compliant setter for transportPdu with method chaining.

        Args:
            value: The transportPdu to set

        Returns:
            self for method chaining

        Note:
            Delegates to transport_pdu property setter (gets validation automatically)
        """
        self.transport_pdu = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_tp_channel(self, value: Optional[SomeipTpChannel]) -> SomeipTpConnection:
        """
        Set tpChannel and return self for chaining.

        Args:
            value: The tpChannel to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tp_channel("value")
        """
        self.tp_channel = value  # Use property setter (gets validation)
        return self

    def with_tp_sdu(self, value: Optional[RefType]) -> SomeipTpConnection:
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

    def with_transport_pdu(self, value: Optional[RefType]) -> SomeipTpConnection:
        """
        Set transportPdu and return self for chaining.

        Args:
            value: The transportPdu to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_transport_pdu("value")
        """
        self.transport_pdu = value  # Use property setter (gets validation)
        return self



class SomeipTpChannel(Identifiable):
    """
    This element is used to assign properties to SomeipTpConnections that are
    referencing this SomeipTp Channel.

    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::SomeipTpChannel

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 620, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specifies the number of segments that shall be a burst ignoring
                # separationTime.
        # then only be applied between bursts.
        # configured, SeparationTime will be applied between.
        self._burstSize: Optional[PositiveInteger] = None

    @property
    def burst_size(self) -> Optional[PositiveInteger]:
        """Get burstSize (Pythonic accessor)."""
        return self._burstSize

    @burst_size.setter
    def burst_size(self, value: Optional[PositiveInteger]) -> None:
        """
        Set burstSize with validation.

        Args:
            value: The burstSize to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._burstSize = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"burstSize must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._burstSize = value
        # Timer to monitor the successful reception.
        # It is started first NPdu is received, restarted after reception NPdus, and is
                # stopped when the last been received.
        self._rxTimeoutTime: Optional[TimeValue] = None

    @property
    def rx_timeout_time(self) -> Optional[TimeValue]:
        """Get rxTimeoutTime (Pythonic accessor)."""
        return self._rxTimeoutTime

    @rx_timeout_time.setter
    def rx_timeout_time(self, value: Optional[TimeValue]) -> None:
        """
        Set rxTimeoutTime with validation.

        Args:
            value: The rxTimeoutTime to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rxTimeoutTime = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"rxTimeoutTime must be TimeValue or None, got {type(value).__name__}"
            )
        self._rxTimeoutTime = value
        # Sets the duration of the minimum time in seconds the module shall wait
        # between the NPdus.
        self._separationTime: Optional[TimeValue] = None

    @property
    def separation_time(self) -> Optional[TimeValue]:
        """Get separationTime (Pythonic accessor)."""
        return self._separationTime

    @separation_time.setter
    def separation_time(self, value: Optional[TimeValue]) -> None:
        """
        Set separationTime with validation.

        Args:
            value: The separationTime to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._separationTime = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"separationTime must be TimeValue or None, got {type(value).__name__}"
            )
        self._separationTime = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBurstSize(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for burstSize.

        Returns:
            The burstSize value

        Note:
            Delegates to burst_size property (CODING_RULE_V2_00017)
        """
        return self.burst_size  # Delegates to property

    def setBurstSize(self, value: PositiveInteger) -> SomeipTpChannel:
        """
        AUTOSAR-compliant setter for burstSize with method chaining.

        Args:
            value: The burstSize to set

        Returns:
            self for method chaining

        Note:
            Delegates to burst_size property setter (gets validation automatically)
        """
        self.burst_size = value  # Delegates to property setter
        return self

    def getRxTimeoutTime(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for rxTimeoutTime.

        Returns:
            The rxTimeoutTime value

        Note:
            Delegates to rx_timeout_time property (CODING_RULE_V2_00017)
        """
        return self.rx_timeout_time  # Delegates to property

    def setRxTimeoutTime(self, value: TimeValue) -> SomeipTpChannel:
        """
        AUTOSAR-compliant setter for rxTimeoutTime with method chaining.

        Args:
            value: The rxTimeoutTime to set

        Returns:
            self for method chaining

        Note:
            Delegates to rx_timeout_time property setter (gets validation automatically)
        """
        self.rx_timeout_time = value  # Delegates to property setter
        return self

    def getSeparationTime(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for separationTime.

        Returns:
            The separationTime value

        Note:
            Delegates to separation_time property (CODING_RULE_V2_00017)
        """
        return self.separation_time  # Delegates to property

    def setSeparationTime(self, value: TimeValue) -> SomeipTpChannel:
        """
        AUTOSAR-compliant setter for separationTime with method chaining.

        Args:
            value: The separationTime to set

        Returns:
            self for method chaining

        Note:
            Delegates to separation_time property setter (gets validation automatically)
        """
        self.separation_time = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_burst_size(self, value: Optional[PositiveInteger]) -> SomeipTpChannel:
        """
        Set burstSize and return self for chaining.

        Args:
            value: The burstSize to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_burst_size("value")
        """
        self.burst_size = value  # Use property setter (gets validation)
        return self

    def with_rx_timeout_time(self, value: Optional[TimeValue]) -> SomeipTpChannel:
        """
        Set rxTimeoutTime and return self for chaining.

        Args:
            value: The rxTimeoutTime to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_rx_timeout_time("value")
        """
        self.rx_timeout_time = value  # Use property setter (gets validation)
        return self

    def with_separation_time(self, value: Optional[TimeValue]) -> SomeipTpChannel:
        """
        Set separationTime and return self for chaining.

        Args:
            value: The separationTime to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_separation_time("value")
        """
        self.separation_time = value  # Use property setter (gets validation)
        return self



class J1939TpConnection(TpConnection):
    """
    A J1939TpConnection represents an internal path for the transmission or
    reception of a Pdu via J1939Tp and describes the sender and the receiver of
    this particular communication. The J1939Tp module routes a Pdu (J1939 PGN)
    through the connection.

    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::J1939TpConnection

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 624, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # BAM (Broadcast Announce Message) is a broadcast this attribute is set to true
                # broadcast is used.
        # FF is the only broadcast address, there’s to configure it.
        self._broadcast: Optional[Boolean] = None

    @property
    def broadcast(self) -> Optional[Boolean]:
        """Get broadcast (Pythonic accessor)."""
        return self._broadcast

    @broadcast.setter
    def broadcast(self, value: Optional[Boolean]) -> None:
        """
        Set broadcast with validation.

        Args:
            value: The broadcast to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._broadcast = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"broadcast must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._broadcast = value
        # Defines usage of available data for dynamic block size protocol retry is
                # enabled.
        # This attribute percent of available buffer that shall be used.
        self._bufferRatio: Optional[PositiveInteger] = None

    @property
    def buffer_ratio(self) -> Optional[PositiveInteger]:
        """Get bufferRatio (Pythonic accessor)."""
        return self._bufferRatio

    @buffer_ratio.setter
    def buffer_ratio(self, value: Optional[PositiveInteger]) -> None:
        """
        Set bufferRatio with validation.

        Args:
            value: The bufferRatio to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._bufferRatio = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"bufferRatio must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._bufferRatio = value
        # Enable support for Tx/Rx cancellation.
        self._cancellation: Optional[Boolean] = None

    @property
    def cancellation(self) -> Optional[Boolean]:
        """Get cancellation (Pythonic accessor)."""
        return self._cancellation

    @cancellation.setter
    def cancellation(self, value: Optional[Boolean]) -> None:
        """
        Set cancellation with validation.

        Args:
            value: The cancellation to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._cancellation = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"cancellation must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._cancellation = value
        # Data Message (TP.
        # DT) used by CMDT and BAM.
        # has a fixed length of 8 bytes.
        self._dataPdu: Optional["NPdu"] = None

    @property
    def data_pdu(self) -> Optional["NPdu"]:
        """Get dataPdu (Pythonic accessor)."""
        return self._dataPdu

    @data_pdu.setter
    def data_pdu(self, value: Optional["NPdu"]) -> None:
        """
        Set dataPdu with validation.

        Args:
            value: The dataPdu to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dataPdu = None
            return

        if not isinstance(value, NPdu):
            raise TypeError(
                f"dataPdu must be NPdu or None, got {type(value).__name__}"
            )
        self._dataPdu = value
        # Enable support for dynamic block size calculation.
        # 2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._dynamicBs: Optional[Boolean] = None

    @property
    def dynamic_bs(self) -> Optional[Boolean]:
        """Get dynamicBs (Pythonic accessor)."""
        return self._dynamicBs

    @dynamic_bs.setter
    def dynamic_bs(self, value: Optional[Boolean]) -> None:
        """
        Set dynamicBs with validation.

        Args:
            value: The dynamicBs to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dynamicBs = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"dynamicBs must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._dynamicBs = value
        # CMDT (Connection Mode Data Transfer) in both one TP.
        # CM (Transport Protocol Command).
        # has a fixed length of 8 bytes.
        # that the role name "flowControlIPdu" is is kept for backward compatibilty
                # reasons.
        self._flowControlPdu: "NPdu" = None

    @property
    def flow_control_pdu(self) -> "NPdu":
        """Get flowControlPdu (Pythonic accessor)."""
        return self._flowControlPdu

    @flow_control_pdu.setter
    def flow_control_pdu(self, value: "NPdu") -> None:
        """
        Set flowControlPdu with validation.

        Args:
            value: The flowControlPdu to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, NPdu):
            raise TypeError(
                f"flowControlPdu must be NPdu, got {type(value).__name__}"
            )
        self._flowControlPdu = value
        # Set maximum block size (number of packets in TP.
        # CM_.
        self._maxBs: Optional[PositiveInteger] = None

    @property
    def max_bs(self) -> Optional[PositiveInteger]:
        """Get maxBs (Pythonic accessor)."""
        return self._maxBs

    @max_bs.setter
    def max_bs(self, value: Optional[PositiveInteger]) -> None:
        """
        Set maxBs with validation.

        Args:
            value: The maxBs to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxBs = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"maxBs must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._maxBs = value
        # Set maximum for expected block size (maximum number in TP.
        # CM_RTS).
        self._maxExpBs: Optional[PositiveInteger] = None

    @property
    def max_exp_bs(self) -> Optional[PositiveInteger]:
        """Get maxExpBs (Pythonic accessor)."""
        return self._maxExpBs

    @max_exp_bs.setter
    def max_exp_bs(self, value: Optional[PositiveInteger]) -> None:
        """
        Set maxExpBs with validation.

        Args:
            value: The maxExpBs to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxExpBs = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"maxExpBs must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._maxExpBs = value
        # The target of the TP connection.
        self._receiver: List[J1939TpNode] = []

    @property
    def receiver(self) -> List[J1939TpNode]:
        """Get receiver (Pythonic accessor)."""
        return self._receiver
        # Enable support for protocol retry.
        self._retry: Optional[Boolean] = None

    @property
    def retry(self) -> Optional[Boolean]:
        """Get retry (Pythonic accessor)."""
        return self._retry

    @retry.setter
    def retry(self, value: Optional[Boolean]) -> None:
        """
        Set retry with validation.

        Args:
            value: The retry to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._retry = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"retry must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._retry = value
        # J1939 messages (parameter groups, PGs) that can be this connection.
        self._tpPg: List[J1939TpPg] = []

    @property
    def tp_pg(self) -> List[J1939TpPg]:
        """Get tpPg (Pythonic accessor)."""
        return self._tpPg
        # The source of the TP connection.
        self._transmitter: Optional[J1939TpNode] = None

    @property
    def transmitter(self) -> Optional[J1939TpNode]:
        """Get transmitter (Pythonic accessor)."""
        return self._transmitter

    @transmitter.setter
    def transmitter(self, value: Optional[J1939TpNode]) -> None:
        """
        Set transmitter with validation.

        Args:
            value: The transmitter to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._transmitter = None
            return

        if not isinstance(value, J1939TpNode):
            raise TypeError(
                f"transmitter must be J1939TpNode or None, got {type(value).__name__}"
            )
        self._transmitter = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBroadcast(self) -> Boolean:
        """
        AUTOSAR-compliant getter for broadcast.

        Returns:
            The broadcast value

        Note:
            Delegates to broadcast property (CODING_RULE_V2_00017)
        """
        return self.broadcast  # Delegates to property

    def setBroadcast(self, value: Boolean) -> J1939TpConnection:
        """
        AUTOSAR-compliant setter for broadcast with method chaining.

        Args:
            value: The broadcast to set

        Returns:
            self for method chaining

        Note:
            Delegates to broadcast property setter (gets validation automatically)
        """
        self.broadcast = value  # Delegates to property setter
        return self

    def getBufferRatio(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for bufferRatio.

        Returns:
            The bufferRatio value

        Note:
            Delegates to buffer_ratio property (CODING_RULE_V2_00017)
        """
        return self.buffer_ratio  # Delegates to property

    def setBufferRatio(self, value: PositiveInteger) -> J1939TpConnection:
        """
        AUTOSAR-compliant setter for bufferRatio with method chaining.

        Args:
            value: The bufferRatio to set

        Returns:
            self for method chaining

        Note:
            Delegates to buffer_ratio property setter (gets validation automatically)
        """
        self.buffer_ratio = value  # Delegates to property setter
        return self

    def getCancellation(self) -> Boolean:
        """
        AUTOSAR-compliant getter for cancellation.

        Returns:
            The cancellation value

        Note:
            Delegates to cancellation property (CODING_RULE_V2_00017)
        """
        return self.cancellation  # Delegates to property

    def setCancellation(self, value: Boolean) -> J1939TpConnection:
        """
        AUTOSAR-compliant setter for cancellation with method chaining.

        Args:
            value: The cancellation to set

        Returns:
            self for method chaining

        Note:
            Delegates to cancellation property setter (gets validation automatically)
        """
        self.cancellation = value  # Delegates to property setter
        return self

    def getDataPdu(self) -> "NPdu":
        """
        AUTOSAR-compliant getter for dataPdu.

        Returns:
            The dataPdu value

        Note:
            Delegates to data_pdu property (CODING_RULE_V2_00017)
        """
        return self.data_pdu  # Delegates to property

    def setDataPdu(self, value: "NPdu") -> J1939TpConnection:
        """
        AUTOSAR-compliant setter for dataPdu with method chaining.

        Args:
            value: The dataPdu to set

        Returns:
            self for method chaining

        Note:
            Delegates to data_pdu property setter (gets validation automatically)
        """
        self.data_pdu = value  # Delegates to property setter
        return self

    def getDynamicBs(self) -> Boolean:
        """
        AUTOSAR-compliant getter for dynamicBs.

        Returns:
            The dynamicBs value

        Note:
            Delegates to dynamic_bs property (CODING_RULE_V2_00017)
        """
        return self.dynamic_bs  # Delegates to property

    def setDynamicBs(self, value: Boolean) -> J1939TpConnection:
        """
        AUTOSAR-compliant setter for dynamicBs with method chaining.

        Args:
            value: The dynamicBs to set

        Returns:
            self for method chaining

        Note:
            Delegates to dynamic_bs property setter (gets validation automatically)
        """
        self.dynamic_bs = value  # Delegates to property setter
        return self

    def getFlowControlPdu(self) -> "NPdu":
        """
        AUTOSAR-compliant getter for flowControlPdu.

        Returns:
            The flowControlPdu value

        Note:
            Delegates to flow_control_pdu property (CODING_RULE_V2_00017)
        """
        return self.flow_control_pdu  # Delegates to property

    def setFlowControlPdu(self, value: "NPdu") -> J1939TpConnection:
        """
        AUTOSAR-compliant setter for flowControlPdu with method chaining.

        Args:
            value: The flowControlPdu to set

        Returns:
            self for method chaining

        Note:
            Delegates to flow_control_pdu property setter (gets validation automatically)
        """
        self.flow_control_pdu = value  # Delegates to property setter
        return self

    def getMaxBs(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for maxBs.

        Returns:
            The maxBs value

        Note:
            Delegates to max_bs property (CODING_RULE_V2_00017)
        """
        return self.max_bs  # Delegates to property

    def setMaxBs(self, value: PositiveInteger) -> J1939TpConnection:
        """
        AUTOSAR-compliant setter for maxBs with method chaining.

        Args:
            value: The maxBs to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_bs property setter (gets validation automatically)
        """
        self.max_bs = value  # Delegates to property setter
        return self

    def getMaxExpBs(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for maxExpBs.

        Returns:
            The maxExpBs value

        Note:
            Delegates to max_exp_bs property (CODING_RULE_V2_00017)
        """
        return self.max_exp_bs  # Delegates to property

    def setMaxExpBs(self, value: PositiveInteger) -> J1939TpConnection:
        """
        AUTOSAR-compliant setter for maxExpBs with method chaining.

        Args:
            value: The maxExpBs to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_exp_bs property setter (gets validation automatically)
        """
        self.max_exp_bs = value  # Delegates to property setter
        return self

    def getReceiver(self) -> List[J1939TpNode]:
        """
        AUTOSAR-compliant getter for receiver.

        Returns:
            The receiver value

        Note:
            Delegates to receiver property (CODING_RULE_V2_00017)
        """
        return self.receiver  # Delegates to property

    def getRetry(self) -> Boolean:
        """
        AUTOSAR-compliant getter for retry.

        Returns:
            The retry value

        Note:
            Delegates to retry property (CODING_RULE_V2_00017)
        """
        return self.retry  # Delegates to property

    def setRetry(self, value: Boolean) -> J1939TpConnection:
        """
        AUTOSAR-compliant setter for retry with method chaining.

        Args:
            value: The retry to set

        Returns:
            self for method chaining

        Note:
            Delegates to retry property setter (gets validation automatically)
        """
        self.retry = value  # Delegates to property setter
        return self

    def getTpPg(self) -> List[J1939TpPg]:
        """
        AUTOSAR-compliant getter for tpPg.

        Returns:
            The tpPg value

        Note:
            Delegates to tp_pg property (CODING_RULE_V2_00017)
        """
        return self.tp_pg  # Delegates to property

    def getTransmitter(self) -> J1939TpNode:
        """
        AUTOSAR-compliant getter for transmitter.

        Returns:
            The transmitter value

        Note:
            Delegates to transmitter property (CODING_RULE_V2_00017)
        """
        return self.transmitter  # Delegates to property

    def setTransmitter(self, value: J1939TpNode) -> J1939TpConnection:
        """
        AUTOSAR-compliant setter for transmitter with method chaining.

        Args:
            value: The transmitter to set

        Returns:
            self for method chaining

        Note:
            Delegates to transmitter property setter (gets validation automatically)
        """
        self.transmitter = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_broadcast(self, value: Optional[Boolean]) -> J1939TpConnection:
        """
        Set broadcast and return self for chaining.

        Args:
            value: The broadcast to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_broadcast("value")
        """
        self.broadcast = value  # Use property setter (gets validation)
        return self

    def with_buffer_ratio(self, value: Optional[PositiveInteger]) -> J1939TpConnection:
        """
        Set bufferRatio and return self for chaining.

        Args:
            value: The bufferRatio to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_buffer_ratio("value")
        """
        self.buffer_ratio = value  # Use property setter (gets validation)
        return self

    def with_cancellation(self, value: Optional[Boolean]) -> J1939TpConnection:
        """
        Set cancellation and return self for chaining.

        Args:
            value: The cancellation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_cancellation("value")
        """
        self.cancellation = value  # Use property setter (gets validation)
        return self

    def with_data_pdu(self, value: Optional["NPdu"]) -> J1939TpConnection:
        """
        Set dataPdu and return self for chaining.

        Args:
            value: The dataPdu to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_data_pdu("value")
        """
        self.data_pdu = value  # Use property setter (gets validation)
        return self

    def with_dynamic_bs(self, value: Optional[Boolean]) -> J1939TpConnection:
        """
        Set dynamicBs and return self for chaining.

        Args:
            value: The dynamicBs to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_dynamic_bs("value")
        """
        self.dynamic_bs = value  # Use property setter (gets validation)
        return self

    def with_flow_control_pdu(self, value: "NPdu") -> J1939TpConnection:
        """
        Set flowControlPdu and return self for chaining.

        Args:
            value: The flowControlPdu to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_flow_control_pdu("value")
        """
        self.flow_control_pdu = value  # Use property setter (gets validation)
        return self

    def with_max_bs(self, value: Optional[PositiveInteger]) -> J1939TpConnection:
        """
        Set maxBs and return self for chaining.

        Args:
            value: The maxBs to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_bs("value")
        """
        self.max_bs = value  # Use property setter (gets validation)
        return self

    def with_max_exp_bs(self, value: Optional[PositiveInteger]) -> J1939TpConnection:
        """
        Set maxExpBs and return self for chaining.

        Args:
            value: The maxExpBs to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_exp_bs("value")
        """
        self.max_exp_bs = value  # Use property setter (gets validation)
        return self

    def with_retry(self, value: Optional[Boolean]) -> J1939TpConnection:
        """
        Set retry and return self for chaining.

        Args:
            value: The retry to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_retry("value")
        """
        self.retry = value  # Use property setter (gets validation)
        return self

    def with_transmitter(self, value: Optional[J1939TpNode]) -> J1939TpConnection:
        """
        Set transmitter and return self for chaining.

        Args:
            value: The transmitter to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_transmitter("value")
        """
        self.transmitter = value  # Use property setter (gets validation)
        return self



class J1939TpPg(ARObject):
    """
    A J1939TpPg represents one J1939 message (parameter group, PG) identified by
    the PGN (parameter group number) that can be received or transmitted via
    J1939Tp.

    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::J1939TpPg

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 625, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # In case of variable length IPdus (with system signals of an additional NPdu
        # (with the PGN in the is used for messages with up to 8 bytes.
        self._directPdu: Optional["NPdu"] = None

    @property
    def direct_pdu(self) -> Optional["NPdu"]:
        """Get directPdu (Pythonic accessor)."""
        return self._directPdu

    @direct_pdu.setter
    def direct_pdu(self, value: Optional["NPdu"]) -> None:
        """
        Set directPdu with validation.

        Args:
            value: The directPdu to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._directPdu = None
            return

        if not isinstance(value, NPdu):
            raise TypeError(
                f"directPdu must be NPdu or None, got {type(value).__name__}"
            )
        self._directPdu = value
        # Parameter group number (PGN) of a J1939 message PG) that can be received or
                # J1939Tp.
        # The PGN may be omitted when directPdu is referenced and is mapped into a Can
                # an identifier.
        self._pgn: Optional[Integer] = None

    @property
    def pgn(self) -> Optional[Integer]:
        """Get pgn (Pythonic accessor)."""
        return self._pgn

    @pgn.setter
    def pgn(self, value: Optional[Integer]) -> None:
        """
        Set pgn with validation.

        Args:
            value: The pgn to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._pgn = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"pgn must be Integer or int or None, got {type(value).__name__}"
            )
        self._pgn = value
        # Parameter Group can be triggered by the J1939 request 2090 Document ID 63:
        # AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._requestable: Optional[Boolean] = None

    @property
    def requestable(self) -> Optional[Boolean]:
        """Get requestable (Pythonic accessor)."""
        return self._requestable

    @requestable.setter
    def requestable(self, value: Optional[Boolean]) -> None:
        """
        Set requestable with validation.

        Args:
            value: The requestable to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._requestable = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"requestable must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._requestable = value
        # Reference to IPdus that are segmented by the Transport more than one IPdu is
        # referenced, the IPdus when the same PGN is received in parallel via protocols
        # (BAM, CMDT, direct) on the.
        self._sdu: List[IPdu] = []

    @property
    def sdu(self) -> List[IPdu]:
        """Get sdu (Pythonic accessor)."""
        return self._sdu

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDirectPdu(self) -> "NPdu":
        """
        AUTOSAR-compliant getter for directPdu.

        Returns:
            The directPdu value

        Note:
            Delegates to direct_pdu property (CODING_RULE_V2_00017)
        """
        return self.direct_pdu  # Delegates to property

    def setDirectPdu(self, value: "NPdu") -> J1939TpPg:
        """
        AUTOSAR-compliant setter for directPdu with method chaining.

        Args:
            value: The directPdu to set

        Returns:
            self for method chaining

        Note:
            Delegates to direct_pdu property setter (gets validation automatically)
        """
        self.direct_pdu = value  # Delegates to property setter
        return self

    def getPgn(self) -> Integer:
        """
        AUTOSAR-compliant getter for pgn.

        Returns:
            The pgn value

        Note:
            Delegates to pgn property (CODING_RULE_V2_00017)
        """
        return self.pgn  # Delegates to property

    def setPgn(self, value: Integer) -> J1939TpPg:
        """
        AUTOSAR-compliant setter for pgn with method chaining.

        Args:
            value: The pgn to set

        Returns:
            self for method chaining

        Note:
            Delegates to pgn property setter (gets validation automatically)
        """
        self.pgn = value  # Delegates to property setter
        return self

    def getRequestable(self) -> Boolean:
        """
        AUTOSAR-compliant getter for requestable.

        Returns:
            The requestable value

        Note:
            Delegates to requestable property (CODING_RULE_V2_00017)
        """
        return self.requestable  # Delegates to property

    def setRequestable(self, value: Boolean) -> J1939TpPg:
        """
        AUTOSAR-compliant setter for requestable with method chaining.

        Args:
            value: The requestable to set

        Returns:
            self for method chaining

        Note:
            Delegates to requestable property setter (gets validation automatically)
        """
        self.requestable = value  # Delegates to property setter
        return self

    def getSdu(self) -> List[IPdu]:
        """
        AUTOSAR-compliant getter for sdu.

        Returns:
            The sdu value

        Note:
            Delegates to sdu property (CODING_RULE_V2_00017)
        """
        return self.sdu  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_direct_pdu(self, value: Optional["NPdu"]) -> J1939TpPg:
        """
        Set directPdu and return self for chaining.

        Args:
            value: The directPdu to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_direct_pdu("value")
        """
        self.direct_pdu = value  # Use property setter (gets validation)
        return self

    def with_pgn(self, value: Optional[Integer]) -> J1939TpPg:
        """
        Set pgn and return self for chaining.

        Args:
            value: The pgn to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_pgn("value")
        """
        self.pgn = value  # Use property setter (gets validation)
        return self

    def with_requestable(self, value: Optional[Boolean]) -> J1939TpPg:
        """
        Set requestable and return self for chaining.

        Args:
            value: The requestable to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_requestable("value")
        """
        self.requestable = value  # Use property setter (gets validation)
        return self



class J1939TpNode(Identifiable):
    """
    TP Node (Sender or Receiver) provides the TP Address and the connection to
    the Topology description.

    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::J1939TpNode

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 626, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Association to a CommunicationConnector in the description.
        # In a System Description this mandatory.
        # In an ECU Extract this reference (references to ECUs that are not part of the
                # shall be avoided).
        self._connector: Optional[Communication] = None

    @property
    def connector(self) -> Optional[Communication]:
        """Get connector (Pythonic accessor)."""
        return self._connector

    @connector.setter
    def connector(self, value: Optional[Communication]) -> None:
        """
        Set connector with validation.

        Args:
            value: The connector to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._connector = None
            return

        if not isinstance(value, Communication):
            raise TypeError(
                f"connector must be Communication or None, got {type(value).__name__}"
            )
        self._connector = value
        # Reference to the TP Address that is used by the TpNode.
        # is optional only when no TP is sent and is received.
        self._tpAddress: Optional[TpAddress] = None

    @property
    def tp_address(self) -> Optional[TpAddress]:
        """Get tpAddress (Pythonic accessor)."""
        return self._tpAddress

    @tp_address.setter
    def tp_address(self, value: Optional[TpAddress]) -> None:
        """
        Set tpAddress with validation.

        Args:
            value: The tpAddress to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tpAddress = None
            return

        if not isinstance(value, TpAddress):
            raise TypeError(
                f"tpAddress must be TpAddress or None, got {type(value).__name__}"
            )
        self._tpAddress = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getConnector(self) -> Communication:
        """
        AUTOSAR-compliant getter for connector.

        Returns:
            The connector value

        Note:
            Delegates to connector property (CODING_RULE_V2_00017)
        """
        return self.connector  # Delegates to property

    def setConnector(self, value: Communication) -> J1939TpNode:
        """
        AUTOSAR-compliant setter for connector with method chaining.

        Args:
            value: The connector to set

        Returns:
            self for method chaining

        Note:
            Delegates to connector property setter (gets validation automatically)
        """
        self.connector = value  # Delegates to property setter
        return self

    def getTpAddress(self) -> TpAddress:
        """
        AUTOSAR-compliant getter for tpAddress.

        Returns:
            The tpAddress value

        Note:
            Delegates to tp_address property (CODING_RULE_V2_00017)
        """
        return self.tp_address  # Delegates to property

    def setTpAddress(self, value: TpAddress) -> J1939TpNode:
        """
        AUTOSAR-compliant setter for tpAddress with method chaining.

        Args:
            value: The tpAddress to set

        Returns:
            self for method chaining

        Note:
            Delegates to tp_address property setter (gets validation automatically)
        """
        self.tp_address = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_connector(self, value: Optional[Communication]) -> J1939TpNode:
        """
        Set connector and return self for chaining.

        Args:
            value: The connector to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_connector("value")
        """
        self.connector = value  # Use property setter (gets validation)
        return self

    def with_tp_address(self, value: Optional[TpAddress]) -> J1939TpNode:
        """
        Set tpAddress and return self for chaining.

        Args:
            value: The tpAddress to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tp_address("value")
        """
        self.tp_address = value  # Use property setter (gets validation)
        return self



class DoIpTpConfig(TpConfig):
    """
    This element defines exactly one DoIpTp Configuration that is used to
    configure all DoIPChannels available in a DoIpInterface. Each DoIPChannel
    describes a connection between a doIpSourceAddress and a doIpTargetAddress
    and the exchange of DcmIPdus between the PduR and DoIP.

    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::DoIpTpConfig

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 555, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Collection of logical DoIP Addresses.
        self._doIpLogicAddress: List[DoIpLogicAddress] = []

    @property
    def do_ip_logic_address(self) -> List[DoIpLogicAddress]:
        """Get doIpLogicAddress (Pythonic accessor)."""
        return self._doIpLogicAddress
        # Collection of unidirectional connections between a source a target address.
        self._tpConnection: List["DoIpTpConnection"] = []

    @property
    def tp_connection(self) -> List["DoIpTpConnection"]:
        """Get tpConnection (Pythonic accessor)."""
        return self._tpConnection

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDoIpLogicAddress(self) -> List[DoIpLogicAddress]:
        """
        AUTOSAR-compliant getter for doIpLogicAddress.

        Returns:
            The doIpLogicAddress value

        Note:
            Delegates to do_ip_logic_address property (CODING_RULE_V2_00017)
        """
        return self.do_ip_logic_address  # Delegates to property

    def getTpConnection(self) -> List["DoIpTpConnection"]:
        """
        AUTOSAR-compliant getter for tpConnection.

        Returns:
            The tpConnection value

        Note:
            Delegates to tp_connection property (CODING_RULE_V2_00017)
        """
        return self.tp_connection  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class FlexrayTpConfig(TpConfig):
    """
    This element defines exactly one FlexRay ISO TP Configuration. One
    FlexRayTpConfig element shall be created for each FlexRay Network in the
    System that uses Flex Ray Iso Tp.

    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::FlexrayTpConfig

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 592, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Configuration of FlexRay TP Pdu Pools.
        # atpVariation.
        self._pduPool: List[FlexrayTpPduPool] = []

    @property
    def pdu_pool(self) -> List[FlexrayTpPduPool]:
        """Get pduPool (Pythonic accessor)."""
        return self._pduPool
        # Collection of TpAddresses.
        # because EcuInstance can vary.
        # atpVariation.
        self._tpAddress: List[TpAddress] = []

    @property
    def tp_address(self) -> List[TpAddress]:
        """Get tpAddress (Pythonic accessor)."""
        return self._tpAddress
        # Configuration of FlexRay TP Connection Controls.
        # Stereotypes: atpSplitable; atpVariation.
        self._tpConnection: List[FlexrayTpConnection] = []

    @property
    def tp_connection(self) -> List[FlexrayTpConnection]:
        """Get tpConnection (Pythonic accessor)."""
        return self._tpConnection
        # Collection of TP Ecus because EcuInstance can vary.
        # atpVariation.
        self._tpEcu: List[FlexrayTpEcu] = []

    @property
    def tp_ecu(self) -> List[FlexrayTpEcu]:
        """Get tpEcu (Pythonic accessor)."""
        return self._tpEcu
        # Senders and receivers of FlexRay TP messages.
        # because EcuInstance can vary.
        # atpVariation.
        self._tpNode: List[FlexrayTpNode] = []

    @property
    def tp_node(self) -> List[FlexrayTpNode]:
        """Get tpNode (Pythonic accessor)."""
        return self._tpNode

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getPduPool(self) -> List[FlexrayTpPduPool]:
        """
        AUTOSAR-compliant getter for pduPool.

        Returns:
            The pduPool value

        Note:
            Delegates to pdu_pool property (CODING_RULE_V2_00017)
        """
        return self.pdu_pool  # Delegates to property

    def getTpAddress(self) -> List[TpAddress]:
        """
        AUTOSAR-compliant getter for tpAddress.

        Returns:
            The tpAddress value

        Note:
            Delegates to tp_address property (CODING_RULE_V2_00017)
        """
        return self.tp_address  # Delegates to property

    def getTpConnection(self) -> List[FlexrayTpConnection]:
        """
        AUTOSAR-compliant getter for tpConnection.

        Returns:
            The tpConnection value

        Note:
            Delegates to tp_connection property (CODING_RULE_V2_00017)
        """
        return self.tp_connection  # Delegates to property

    def getTpEcu(self) -> List[FlexrayTpEcu]:
        """
        AUTOSAR-compliant getter for tpEcu.

        Returns:
            The tpEcu value

        Note:
            Delegates to tp_ecu property (CODING_RULE_V2_00017)
        """
        return self.tp_ecu  # Delegates to property

    def getTpNode(self) -> List[FlexrayTpNode]:
        """
        AUTOSAR-compliant getter for tpNode.

        Returns:
            The tpNode value

        Note:
            Delegates to tp_node property (CODING_RULE_V2_00017)
        """
        return self.tp_node  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class FlexrayArTpConfig(TpConfig):
    """
    This element defines exactly one FlexRay Autosar TP Configuration. One
    FlexrayArTpConfig element shall be created for each FlexRay Network in the
    System that uses Flex Ray Autosar TP.

    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::FlexrayArTpConfig

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 599, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Collection of TpAddresses.
        # atpVariation.
        self._tpAddress: List[TpAddress] = []

    @property
    def tp_address(self) -> List[TpAddress]:
        """Get tpAddress (Pythonic accessor)."""
        return self._tpAddress
        # Configuration of FlexRay Autosar Transport Protocol atpVariation.
        self._tpChannel: List[FlexrayArTpChannel] = []

    @property
    def tp_channel(self) -> List[FlexrayArTpChannel]:
        """Get tpChannel (Pythonic accessor)."""
        return self._tpChannel
        # Senders and receivers of TP messages.
        # atpVariation.
        self._tpNode: List[FlexrayArTpNode] = []

    @property
    def tp_node(self) -> List[FlexrayArTpNode]:
        """Get tpNode (Pythonic accessor)."""
        return self._tpNode

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTpAddress(self) -> List[TpAddress]:
        """
        AUTOSAR-compliant getter for tpAddress.

        Returns:
            The tpAddress value

        Note:
            Delegates to tp_address property (CODING_RULE_V2_00017)
        """
        return self.tp_address  # Delegates to property

    def getTpChannel(self) -> List[FlexrayArTpChannel]:
        """
        AUTOSAR-compliant getter for tpChannel.

        Returns:
            The tpChannel value

        Note:
            Delegates to tp_channel property (CODING_RULE_V2_00017)
        """
        return self.tp_channel  # Delegates to property

    def getTpNode(self) -> List[FlexrayArTpNode]:
        """
        AUTOSAR-compliant getter for tpNode.

        Returns:
            The tpNode value

        Note:
            Delegates to tp_node property (CODING_RULE_V2_00017)
        """
        return self.tp_node  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class CanTpConfig(TpConfig):
    """
    This element defines exactly one CAN TP Configuration. One CanTpConfig
    element shall be created for each CAN Network in the System.

    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::CanTpConfig

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 606, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Collection of TP Addresses.
        # because EcuInstance can vary.
        # atpVariation.
        self._tpAddress: List[CanTpAddress] = []

    @property
    def tp_address(self) -> List[CanTpAddress]:
        """Get tpAddress (Pythonic accessor)."""
        return self._tpAddress
        # Configuration of CAN TP channels.
        # atpVariation.
        self._tpChannel: List[CanTpChannel] = []

    @property
    def tp_channel(self) -> List[CanTpChannel]:
        """Get tpChannel (Pythonic accessor)."""
        return self._tpChannel
        # Senders and receivers of CAN TP messages.
        # because TpNode can vary.
        # atpVariation.
        self._tpConnection: List[CanTpConnection] = []

    @property
    def tp_connection(self) -> List[CanTpConnection]:
        """Get tpConnection (Pythonic accessor)."""
        return self._tpConnection
        # Collection of TP Ecus because EcuInstance can vary.
        # atpVariation.
        self._tpEcu: List[CanTpEcu] = []

    @property
    def tp_ecu(self) -> List[CanTpEcu]:
        """Get tpEcu (Pythonic accessor)."""
        return self._tpEcu
        # Senders and receivers of Can TP messages.
        # because EcuInstance can vary.
        # atpVariation.
        self._tpNode: List[CanTpNode] = []

    @property
    def tp_node(self) -> List[CanTpNode]:
        """Get tpNode (Pythonic accessor)."""
        return self._tpNode

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTpAddress(self) -> List[CanTpAddress]:
        """
        AUTOSAR-compliant getter for tpAddress.

        Returns:
            The tpAddress value

        Note:
            Delegates to tp_address property (CODING_RULE_V2_00017)
        """
        return self.tp_address  # Delegates to property

    def getTpChannel(self) -> List[CanTpChannel]:
        """
        AUTOSAR-compliant getter for tpChannel.

        Returns:
            The tpChannel value

        Note:
            Delegates to tp_channel property (CODING_RULE_V2_00017)
        """
        return self.tp_channel  # Delegates to property

    def getTpConnection(self) -> List[CanTpConnection]:
        """
        AUTOSAR-compliant getter for tpConnection.

        Returns:
            The tpConnection value

        Note:
            Delegates to tp_connection property (CODING_RULE_V2_00017)
        """
        return self.tp_connection  # Delegates to property

    def getTpEcu(self) -> List[CanTpEcu]:
        """
        AUTOSAR-compliant getter for tpEcu.

        Returns:
            The tpEcu value

        Note:
            Delegates to tp_ecu property (CODING_RULE_V2_00017)
        """
        return self.tp_ecu  # Delegates to property

    def getTpNode(self) -> List[CanTpNode]:
        """
        AUTOSAR-compliant getter for tpNode.

        Returns:
            The tpNode value

        Note:
            Delegates to tp_node property (CODING_RULE_V2_00017)
        """
        return self.tp_node  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class LinTpConfig(TpConfig):
    """
    This element defines exactly one Lin TP Configuration. One LinTpConfig
    element shall be created for each Lin Network in the System.

    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::LinTpConfig

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 614, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Collection of TpAddresses.
        # because EcuInstance can vary.
        # atpVariation.
        self._tpAddress: List[TpAddress] = []

    @property
    def tp_address(self) -> List[TpAddress]:
        """Get tpAddress (Pythonic accessor)."""
        return self._tpAddress
        # Configuration of LIN TP channels.
        # because TpNode can vary.
        # atpVariation.
        self._tpConnection: List[LinTpConnection] = []

    @property
    def tp_connection(self) -> List[LinTpConnection]:
        """Get tpConnection (Pythonic accessor)."""
        return self._tpConnection
        # Senders and receivers of LIN TP messages.
        # because EcuInstance can vary.
        # atpVariation.
        self._tpNode: List[LinTpNode] = []

    @property
    def tp_node(self) -> List[LinTpNode]:
        """Get tpNode (Pythonic accessor)."""
        return self._tpNode

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTpAddress(self) -> List[TpAddress]:
        """
        AUTOSAR-compliant getter for tpAddress.

        Returns:
            The tpAddress value

        Note:
            Delegates to tp_address property (CODING_RULE_V2_00017)
        """
        return self.tp_address  # Delegates to property

    def getTpConnection(self) -> List[LinTpConnection]:
        """
        AUTOSAR-compliant getter for tpConnection.

        Returns:
            The tpConnection value

        Note:
            Delegates to tp_connection property (CODING_RULE_V2_00017)
        """
        return self.tp_connection  # Delegates to property

    def getTpNode(self) -> List[LinTpNode]:
        """
        AUTOSAR-compliant getter for tpNode.

        Returns:
            The tpNode value

        Note:
            Delegates to tp_node property (CODING_RULE_V2_00017)
        """
        return self.tp_node  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class EthTpConfig(TpConfig):
    """
    This element defines which PduTriggerings shall be handled using "TP"
    semantics.

    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::EthTpConfig

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 617, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Senders and receivers of SOME/IP TP messages.
        self._tpConnection: List[EthTpConnection] = []

    @property
    def tp_connection(self) -> List[EthTpConnection]:
        """Get tpConnection (Pythonic accessor)."""
        return self._tpConnection

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTpConnection(self) -> List[EthTpConnection]:
        """
        AUTOSAR-compliant getter for tpConnection.

        Returns:
            The tpConnection value

        Note:
            Delegates to tp_connection property (CODING_RULE_V2_00017)
        """
        return self.tp_connection  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class SomeipTpConfig(TpConfig):
    """
    This element defines exactly one SOME/IP TP Configuration.

    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::SomeipTpConfig

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 619, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Definition of SomeipTpChannels that are collecting that are valid for a
        # collection of.
        self._tpChannel: List[SomeipTpChannel] = []

    @property
    def tp_channel(self) -> List[SomeipTpChannel]:
        """Get tpChannel (Pythonic accessor)."""
        return self._tpChannel
        # Senders and receivers of SOME/IP TP messages.
        self._tpConnection: List[SomeipTpConnection] = []

    @property
    def tp_connection(self) -> List[SomeipTpConnection]:
        """Get tpConnection (Pythonic accessor)."""
        return self._tpConnection

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTpChannel(self) -> List[SomeipTpChannel]:
        """
        AUTOSAR-compliant getter for tpChannel.

        Returns:
            The tpChannel value

        Note:
            Delegates to tp_channel property (CODING_RULE_V2_00017)
        """
        return self.tp_channel  # Delegates to property

    def getTpConnection(self) -> List[SomeipTpConnection]:
        """
        AUTOSAR-compliant getter for tpConnection.

        Returns:
            The tpConnection value

        Note:
            Delegates to tp_connection property (CODING_RULE_V2_00017)
        """
        return self.tp_connection  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class J1939TpConfig(TpConfig):
    """
    This element defines exactly one J1939 TP Configuration. One J1939TpConfig
    element shall be created for each J1939 Network in the System.

    Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols::J1939TpConfig

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 623, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Collection of TP Adresses.
        # because EcuInstance can vary.
        # atpVariation.
        self._tpAddress: List[TpAddress] = []

    @property
    def tp_address(self) -> List[TpAddress]:
        """Get tpAddress (Pythonic accessor)."""
        return self._tpAddress
        # Configuration of J1939 TP connections.
        # because TpNode can vary.
        # atpVariation 2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._tpConnection: List[J1939TpConnection] = []

    @property
    def tp_connection(self) -> List[J1939TpConnection]:
        """Get tpConnection (Pythonic accessor)."""
        return self._tpConnection
        # Senders and receivers of J1939 TP messages.
        # because EcuInstance can vary.
        # atpVariation.
        self._tpNode: List[J1939TpNode] = []

    @property
    def tp_node(self) -> List[J1939TpNode]:
        """Get tpNode (Pythonic accessor)."""
        return self._tpNode

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTpAddress(self) -> List[TpAddress]:
        """
        AUTOSAR-compliant getter for tpAddress.

        Returns:
            The tpAddress value

        Note:
            Delegates to tp_address property (CODING_RULE_V2_00017)
        """
        return self.tp_address  # Delegates to property

    def getTpConnection(self) -> List[J1939TpConnection]:
        """
        AUTOSAR-compliant getter for tpConnection.

        Returns:
            The tpConnection value

        Note:
            Delegates to tp_connection property (CODING_RULE_V2_00017)
        """
        return self.tp_connection  # Delegates to property

    def getTpNode(self) -> List[J1939TpNode]:
        """
        AUTOSAR-compliant getter for tpNode.

        Returns:
            The tpNode value

        Note:
            Delegates to tp_node property (CODING_RULE_V2_00017)
        """
        return self.tp_node  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====


class FrArTpAckType(AREnum):
    """
    FrArTpAckType enumeration

Type of Acknowledgement. Aggregated by FlexrayArTpChannel.ackType

Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols
    """
    # Acknowledgement without retry.
    ackWithoutRt = "0"

    # Acknowledgement with retry.
    ackWithRt = "1"

    # No acknowledgement.
    noAck = "2"



class MaximumMessageLengthType(AREnum):
    """
    MaximumMessageLengthType enumeration

Type of Acknowledgement. Aggregated by FlexrayArTpChannel.maximumMessageLength

Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols
    """
    # SF-E allowed (SF of arbitrary length depending on FrTpPduLength), up to (2**32)-1 byte message
    I4glength = "0"

    # Up to (2**12)-1 Byte message length (No FF-Ex or SF-E or AF shall be used and recognized).
    iso = "1"

    # As ISO, but the maximum payload length is limited to 6 byte (SF-I, FF-I, CF). This is necessary to
    iso6 = "None"

    # TP on CAN when using Extended Addressing or Mixed Addressing on CAN.
    route = "2"



class CanTpAddressingFormatType(AREnum):
    """
    CanTpAddressingFormatType enumeration

Declares which communication addressing mode is supported. Aggregated by CanTpConnection.addressingFormat

Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols
    """
    # To use extended addressing format.
    extended = "0"

    # Template
    System = "None"

    # CP R23-11
    AUTOSAR = "None"

    # To use mixed 11bit addressing format.
    mixed = "1"

    # To use mixed 29bit addressing format
    mixed29bit = "2"

    # To use normal fixed addressing format
    normalfixed = "3"

    # To use normal addressing format.
    standard = "4"



class NetworkTargetAddressType(AREnum):
    """
    NetworkTargetAddressType enumeration

Network Target Address type (see ISO 15765-2). Aggregated by CanTpConnection.taType

Package: M2::AUTOSARTemplates::SystemTemplate::TransportProtocols
    """
    # Functional request type
    functional = "0"

    # Physical request type
    physical = "2"


__all__ = [
    DoIpLogicAddress,
    TpConfig,
    TpAddress,
    FlexrayTpConnectionControl,
    FlexrayTpConnection,
    FlexrayTpPduPool,
    FlexrayTpNode,
    FlexrayTpEcu,
    FlexrayArTpChannel,
    FlexrayArTpNode,
    FlexrayArTpConnection,
    CanTpChannel,
    CanTpConnection,
    CanTpAddress,
    CanTpEcu,
    CanTpNode,
    LinTpNode,
    LinTpConnection,
    EthTpConnection,
    SomeipTpConnection,
    SomeipTpChannel,
    J1939TpConnection,
    J1939TpPg,
    J1939TpNode,
    DoIpTpConfig,
    FlexrayTpConfig,
    FlexrayArTpConfig,
    CanTpConfig,
    LinTpConfig,
    EthTpConfig,
    SomeipTpConfig,
    J1939TpConfig,
    FrArTpAckType,
    MaximumMessageLengthType,
    CanTpAddressingFormatType,
    NetworkTargetAddressType,
]

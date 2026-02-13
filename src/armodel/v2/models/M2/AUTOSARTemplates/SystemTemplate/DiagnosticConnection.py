"""
AUTOSAR Package - DiagnosticConnection

Package: M2::AUTOSARTemplates::SystemTemplate::DiagnosticConnection
"""


from __future__ import annotations

from abc import ABC
from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Referrable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class DiagnosticConnection(ARElement):
    """
    DiagnosticConncection that is used to describe the relationship between
    several TP connections.

    Package: M2::AUTOSARTemplates::SystemTemplate::DiagnosticConnection::DiagnosticConnection

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 60, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 632, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to functional request messages.
        # 719 Document ID 673: AUTOSAR_CP_TPS_DiagnosticExtractTemplate Template
                # R23-11.
        self._functionalRequest: List[TpConnectionIdent] = []

    @property
    def functional_request(self) -> List[TpConnectionIdent]:
        """Get functionalRequest (Pythonic accessor)."""
        return self._functionalRequest
        # Reference to UUDT responses.
        self._periodicResponseUudt: List[RefType] = []

    @property
    def periodic_response_uudt(self) -> List[RefType]:
        """Get periodicResponseUudt (Pythonic accessor)."""
        return self._periodicResponseUudt
        # Reference to a physical request message.
        self._physicalRequest: Optional[TpConnectionIdent] = None

    @property
    def physical_request(self) -> Optional[TpConnectionIdent]:
        """Get physicalRequest (Pythonic accessor)."""
        return self._physicalRequest

    @physical_request.setter
    def physical_request(self, value: Optional[TpConnectionIdent]) -> None:
        """
        Set physicalRequest with validation.

        Args:
            value: The physicalRequest to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._physicalRequest = None
            return

        if not isinstance(value, TpConnectionIdent):
            raise TypeError(
                f"physicalRequest must be TpConnectionIdent or None, got {type(value).__name__}"
            )
        self._physicalRequest = value
        # are also cases where providing the not possible and/or not allowed.
        self._response: Optional[TpConnectionIdent] = None

    @property
    def response(self) -> Optional[TpConnectionIdent]:
        """Get response (Pythonic accessor)."""
        return self._response

    @response.setter
    def response(self, value: Optional[TpConnectionIdent]) -> None:
        """
        Set response with validation.

        Args:
            value: The response to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._response = None
            return

        if not isinstance(value, TpConnectionIdent):
            raise TypeError(
                f"response must be TpConnectionIdent or None, got {type(value).__name__}"
            )
        self._response = value
        # atp.
        # Status=obsolete.
        self._responseOn: Optional[TpConnectionIdent] = None

    @property
    def response_on(self) -> Optional[TpConnectionIdent]:
        """Get responseOn (Pythonic accessor)."""
        return self._responseOn

    @response_on.setter
    def response_on(self, value: Optional[TpConnectionIdent]) -> None:
        """
        Set responseOn with validation.

        Args:
            value: The responseOn to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._responseOn = None
            return

        if not isinstance(value, TpConnectionIdent):
            raise TypeError(
                f"responseOn must be TpConnectionIdent or None, got {type(value).__name__}"
            )
        self._responseOn = value

    def with_functional_request(self, value):
        """
        Set functional_request and return self for chaining.

        Args:
            value: The functional_request to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_functional_request("value")
        """
        self.functional_request = value  # Use property setter (gets validation)
        return self

    def with_periodic_response_uudt(self, value):
        """
        Set periodic_response_uudt and return self for chaining.

        Args:
            value: The periodic_response_uudt to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_periodic_response_uudt("value")
        """
        self.periodic_response_uudt = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getFunctionalRequest(self) -> List[TpConnectionIdent]:
        """
        AUTOSAR-compliant getter for functionalRequest.

        Returns:
            The functionalRequest value

        Note:
            Delegates to functional_request property (CODING_RULE_V2_00017)
        """
        return self.functional_request  # Delegates to property

    def getPeriodicResponseUudt(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for periodicResponseUudt.

        Returns:
            The periodicResponseUudt value

        Note:
            Delegates to periodic_response_uudt property (CODING_RULE_V2_00017)
        """
        return self.periodic_response_uudt  # Delegates to property

    def getPhysicalRequest(self) -> TpConnectionIdent:
        """
        AUTOSAR-compliant getter for physicalRequest.

        Returns:
            The physicalRequest value

        Note:
            Delegates to physical_request property (CODING_RULE_V2_00017)
        """
        return self.physical_request  # Delegates to property

    def setPhysicalRequest(self, value: TpConnectionIdent) -> DiagnosticConnection:
        """
        AUTOSAR-compliant setter for physicalRequest with method chaining.

        Args:
            value: The physicalRequest to set

        Returns:
            self for method chaining

        Note:
            Delegates to physical_request property setter (gets validation automatically)
        """
        self.physical_request = value  # Delegates to property setter
        return self

    def getResponse(self) -> TpConnectionIdent:
        """
        AUTOSAR-compliant getter for response.

        Returns:
            The response value

        Note:
            Delegates to response property (CODING_RULE_V2_00017)
        """
        return self.response  # Delegates to property

    def setResponse(self, value: TpConnectionIdent) -> DiagnosticConnection:
        """
        AUTOSAR-compliant setter for response with method chaining.

        Args:
            value: The response to set

        Returns:
            self for method chaining

        Note:
            Delegates to response property setter (gets validation automatically)
        """
        self.response = value  # Delegates to property setter
        return self

    def getResponseOn(self) -> TpConnectionIdent:
        """
        AUTOSAR-compliant getter for responseOn.

        Returns:
            The responseOn value

        Note:
            Delegates to response_on property (CODING_RULE_V2_00017)
        """
        return self.response_on  # Delegates to property

    def setResponseOn(self, value: TpConnectionIdent) -> DiagnosticConnection:
        """
        AUTOSAR-compliant setter for responseOn with method chaining.

        Args:
            value: The responseOn to set

        Returns:
            self for method chaining

        Note:
            Delegates to response_on property setter (gets validation automatically)
        """
        self.response_on = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_physical_request(self, value: Optional[TpConnectionIdent]) -> DiagnosticConnection:
        """
        Set physicalRequest and return self for chaining.

        Args:
            value: The physicalRequest to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_physical_request("value")
        """
        self.physical_request = value  # Use property setter (gets validation)
        return self

    def with_response(self, value: Optional[TpConnectionIdent]) -> DiagnosticConnection:
        """
        Set response and return self for chaining.

        Args:
            value: The response to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_response("value")
        """
        self.response = value  # Use property setter (gets validation)
        return self

    def with_response_on(self, value: Optional[TpConnectionIdent]) -> DiagnosticConnection:
        """
        Set responseOn and return self for chaining.

        Args:
            value: The responseOn to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_response_on("value")
        """
        self.response_on = value  # Use property setter (gets validation)
        return self



class TpConnectionIdent(Referrable):
    """
    This meta-class is created to add the ability to become the target of a
    reference to the non-Referrable Tp Connection.

    Package: M2::AUTOSARTemplates::SystemTemplate::DiagnosticConnection::TpConnectionIdent

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 61, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 633, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class TpConnection(ARObject, ABC):
    """
    TpConnection Base Class.

    Package: M2::AUTOSARTemplates::SystemTemplate::DiagnosticConnection::TpConnection

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 633, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is TpConnection:
            raise TypeError("TpConnection is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This adds the ability to become referrable to Tp.
        self._ident: Optional[TpConnectionIdent] = None

    @property
    def ident(self) -> Optional[TpConnectionIdent]:
        """Get ident (Pythonic accessor)."""
        return self._ident

    @ident.setter
    def ident(self, value: Optional[TpConnectionIdent]) -> None:
        """
        Set ident with validation.

        Args:
            value: The ident to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ident = None
            return

        if not isinstance(value, TpConnectionIdent):
            raise TypeError(
                f"ident must be TpConnectionIdent or None, got {type(value).__name__}"
            )
        self._ident = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getIdent(self) -> TpConnectionIdent:
        """
        AUTOSAR-compliant getter for ident.

        Returns:
            The ident value

        Note:
            Delegates to ident property (CODING_RULE_V2_00017)
        """
        return self.ident  # Delegates to property

    def setIdent(self, value: TpConnectionIdent) -> TpConnection:
        """
        AUTOSAR-compliant setter for ident with method chaining.

        Args:
            value: The ident to set

        Returns:
            self for method chaining

        Note:
            Delegates to ident property setter (gets validation automatically)
        """
        self.ident = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_ident(self, value: Optional[TpConnectionIdent]) -> TpConnection:
        """
        Set ident and return self for chaining.

        Args:
            value: The ident to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ident("value")
        """
        self.ident = value  # Use property setter (gets validation)
        return self



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

    def setDoIpSource(self, value: "DoIpLogicAddress") -> DoIpTpConnection:
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

    def setDoIpTarget(self, value: "DoIpLogicAddress") -> DoIpTpConnection:
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

    def setTpSdu(self, value: RefType) -> DoIpTpConnection:
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

    def with_do_ip_source(self, value: Optional["DoIpLogicAddress"]) -> DoIpTpConnection:
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

    def with_do_ip_target(self, value: Optional["DoIpLogicAddress"]) -> DoIpTpConnection:
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

    def with_tp_sdu(self, value: Optional[RefType]) -> DoIpTpConnection:
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

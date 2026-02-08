from typing import Optional
from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics import DiagnosticCommonElement


class DiagnosticSession(DiagnosticCommonElement):
    """
    This meta-class represents the ability to define a diagnostic session.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticSession

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 73, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This is the numerical identifier used to identify the the scope of diagnostic
        # workflow.
        self._id: Optional["PositiveInteger"] = None

    @property
    def id(self) -> Optional["PositiveInteger"]:
        """Get id (Pythonic accessor)."""
        return self._id

    @id.setter
    def id(self, value: Optional["PositiveInteger"]) -> None:
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

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"id must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._id = value
        # This attribute represents the ability to define whether this diagnostic
                # session allows to jump to Bootloader (OEM System Supplier Bootloader).
        # diagnostic session doesn’t allow to jump to value JumpToBootLoaderEnum.
        # noBoot chosen.
        # 719 Document ID 673: AUTOSAR_CP_TPS_DiagnosticExtractTemplate Template
                # R23-11.
        self._jumpToBoot: Optional["DiagnosticJumpToBoot"] = None

    @property
    def jump_to_boot(self) -> Optional["DiagnosticJumpToBoot"]:
        """Get jumpToBoot (Pythonic accessor)."""
        return self._jumpToBoot

    @jump_to_boot.setter
    def jump_to_boot(self, value: Optional["DiagnosticJumpToBoot"]) -> None:
        """
        Set jumpToBoot with validation.

        Args:
            value: The jumpToBoot to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._jumpToBoot = None
            return

        if not isinstance(value, DiagnosticJumpToBoot):
            raise TypeError(
                f"jumpToBoot must be DiagnosticJumpToBoot or None, got {type(value).__name__}"
            )
        self._jumpToBoot = value
        # This is the session value for P2ServerMax in seconds Control).
        # configuration standard is to use SI units, parameter is defined as a float
                # value in seconds.
        self._p2ServerMax: Optional["TimeValue"] = None

    @property
    def p2_server_max(self) -> Optional["TimeValue"]:
        """Get p2ServerMax (Pythonic accessor)."""
        return self._p2ServerMax

    @p2_server_max.setter
    def p2_server_max(self, value: Optional["TimeValue"]) -> None:
        """
        Set p2ServerMax with validation.

        Args:
            value: The p2ServerMax to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._p2ServerMax = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"p2ServerMax must be TimeValue or None, got {type(value).__name__}"
            )
        self._p2ServerMax = value
        # This is the session value for P2*ServerMax in seconds Session Control).
        # configuration standard is to use SI units, parameter is defined as a float
                # value in seconds.
        self._p2StarServer: Optional["TimeValue"] = None

    @property
    def p2_star_server(self) -> Optional["TimeValue"]:
        """Get p2StarServer (Pythonic accessor)."""
        return self._p2StarServer

    @p2_star_server.setter
    def p2_star_server(self, value: Optional["TimeValue"]) -> None:
        """
        Set p2StarServer with validation.

        Args:
            value: The p2StarServer to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._p2StarServer = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"p2StarServer must be TimeValue or None, got {type(value).__name__}"
            )
        self._p2StarServer = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getId(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for id.

        Returns:
            The id value

        Note:
            Delegates to id property (CODING_RULE_V2_00017)
        """
        return self.id  # Delegates to property

    def setId(self, value: "PositiveInteger") -> "DiagnosticSession":
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

    def getJumpToBoot(self) -> "DiagnosticJumpToBoot":
        """
        AUTOSAR-compliant getter for jumpToBoot.

        Returns:
            The jumpToBoot value

        Note:
            Delegates to jump_to_boot property (CODING_RULE_V2_00017)
        """
        return self.jump_to_boot  # Delegates to property

    def setJumpToBoot(self, value: "DiagnosticJumpToBoot") -> "DiagnosticSession":
        """
        AUTOSAR-compliant setter for jumpToBoot with method chaining.

        Args:
            value: The jumpToBoot to set

        Returns:
            self for method chaining

        Note:
            Delegates to jump_to_boot property setter (gets validation automatically)
        """
        self.jump_to_boot = value  # Delegates to property setter
        return self

    def getP2ServerMax(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for p2ServerMax.

        Returns:
            The p2ServerMax value

        Note:
            Delegates to p2_server_max property (CODING_RULE_V2_00017)
        """
        return self.p2_server_max  # Delegates to property

    def setP2ServerMax(self, value: "TimeValue") -> "DiagnosticSession":
        """
        AUTOSAR-compliant setter for p2ServerMax with method chaining.

        Args:
            value: The p2ServerMax to set

        Returns:
            self for method chaining

        Note:
            Delegates to p2_server_max property setter (gets validation automatically)
        """
        self.p2_server_max = value  # Delegates to property setter
        return self

    def getP2StarServer(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for p2StarServer.

        Returns:
            The p2StarServer value

        Note:
            Delegates to p2_star_server property (CODING_RULE_V2_00017)
        """
        return self.p2_star_server  # Delegates to property

    def setP2StarServer(self, value: "TimeValue") -> "DiagnosticSession":
        """
        AUTOSAR-compliant setter for p2StarServer with method chaining.

        Args:
            value: The p2StarServer to set

        Returns:
            self for method chaining

        Note:
            Delegates to p2_star_server property setter (gets validation automatically)
        """
        self.p2_star_server = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_id(self, value: Optional["PositiveInteger"]) -> "DiagnosticSession":
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

    def with_jump_to_boot(self, value: Optional["DiagnosticJumpToBoot"]) -> "DiagnosticSession":
        """
        Set jumpToBoot and return self for chaining.

        Args:
            value: The jumpToBoot to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_jump_to_boot("value")
        """
        self.jump_to_boot = value  # Use property setter (gets validation)
        return self

    def with_p2_server_max(self, value: Optional["TimeValue"]) -> "DiagnosticSession":
        """
        Set p2ServerMax and return self for chaining.

        Args:
            value: The p2ServerMax to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_p2_server_max("value")
        """
        self.p2_server_max = value  # Use property setter (gets validation)
        return self

    def with_p2_star_server(self, value: Optional["TimeValue"]) -> "DiagnosticSession":
        """
        Set p2StarServer and return self for chaining.

        Args:
            value: The p2StarServer to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_p2_star_server("value")
        """
        self.p2_star_server = value  # Use property setter (gets validation)
        return self

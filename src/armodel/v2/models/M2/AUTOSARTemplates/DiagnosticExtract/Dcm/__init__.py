"""
AUTOSAR Package - Dcm

Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm
"""


from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel.v2.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics import (
    DiagnosticCommonElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
)


class DiagnosticAccessPermission(DiagnosticCommonElement):
    """
    This represents the specification of whether a given service can be accessed
    according to the existence of meta-classes referenced by a particular
    DiagnosticAccessPermission. In other words, this meta-class acts as a
    mapping element between several (otherwise unrelated) pieces of information
    that are put into context for the purpose of checking for access rights.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticAccessPermission

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 73, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The existence of this aggregation indicates that an authentication is
                # foreseen.
        # The details are clarified by the.
        self._authentication: Optional[DiagnosticAuthRole] = None

    @property
    def authentication(self) -> Optional[DiagnosticAuthRole]:
        """Get authentication (Pythonic accessor)."""
        return self._authentication

    @authentication.setter
    def authentication(self, value: Optional[DiagnosticAuthRole]) -> None:
        """
        Set authentication with validation.

        Args:
            value: The authentication to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._authentication = None
            return

        if not isinstance(value, DiagnosticAuthRole):
            raise TypeError(
                f"authentication must be DiagnosticAuthRole or None, got {type(value).__name__}"
            )
        self._authentication = value
        # This represents the associated DiagnosticSessions atpSplitable.
        self._diagnostic: List[DiagnosticSession] = []

    @property
    def diagnostic(self) -> List[DiagnosticSession]:
        """Get diagnostic (Pythonic accessor)."""
        return self._diagnostic
        # This represents the environmental conditions associated with the access
        # permission.
        self._environmental: Optional["Diagnostic"] = None

    @property
    def environmental(self) -> Optional["Diagnostic"]:
        """Get environmental (Pythonic accessor)."""
        return self._environmental

    @environmental.setter
    def environmental(self, value: Optional["Diagnostic"]) -> None:
        """
        Set environmental with validation.

        Args:
            value: The environmental to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._environmental = None
            return

        if not isinstance(value, Diagnostic):
            raise TypeError(
                f"environmental must be Diagnostic or None, got {type(value).__name__}"
            )
        self._environmental = value
        # This represents the associated DiagnosticSecurityLevels.
        self._securityLevel: List[DiagnosticSecurityLevel] = []

    @property
    def security_level(self) -> List[DiagnosticSecurityLevel]:
        """Get securityLevel (Pythonic accessor)."""
        return self._securityLevel

    def with_diagnostic(self, value):
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

    def with_security_level(self, value):
        """
        Set security_level and return self for chaining.

        Args:
            value: The security_level to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_security_level("value")
        """
        self.security_level = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAuthentication(self) -> DiagnosticAuthRole:
        """
        AUTOSAR-compliant getter for authentication.

        Returns:
            The authentication value

        Note:
            Delegates to authentication property (CODING_RULE_V2_00017)
        """
        return self.authentication  # Delegates to property

    def setAuthentication(self, value: DiagnosticAuthRole) -> DiagnosticAccessPermission:
        """
        AUTOSAR-compliant setter for authentication with method chaining.

        Args:
            value: The authentication to set

        Returns:
            self for method chaining

        Note:
            Delegates to authentication property setter (gets validation automatically)
        """
        self.authentication = value  # Delegates to property setter
        return self

    def getDiagnostic(self) -> List[DiagnosticSession]:
        """
        AUTOSAR-compliant getter for diagnostic.

        Returns:
            The diagnostic value

        Note:
            Delegates to diagnostic property (CODING_RULE_V2_00017)
        """
        return self.diagnostic  # Delegates to property

    def getEnvironmental(self) -> "Diagnostic":
        """
        AUTOSAR-compliant getter for environmental.

        Returns:
            The environmental value

        Note:
            Delegates to environmental property (CODING_RULE_V2_00017)
        """
        return self.environmental  # Delegates to property

    def setEnvironmental(self, value: "Diagnostic") -> DiagnosticAccessPermission:
        """
        AUTOSAR-compliant setter for environmental with method chaining.

        Args:
            value: The environmental to set

        Returns:
            self for method chaining

        Note:
            Delegates to environmental property setter (gets validation automatically)
        """
        self.environmental = value  # Delegates to property setter
        return self

    def getSecurityLevel(self) -> List[DiagnosticSecurityLevel]:
        """
        AUTOSAR-compliant getter for securityLevel.

        Returns:
            The securityLevel value

        Note:
            Delegates to security_level property (CODING_RULE_V2_00017)
        """
        return self.security_level  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_authentication(self, value: Optional[DiagnosticAuthRole]) -> DiagnosticAccessPermission:
        """
        Set authentication and return self for chaining.

        Args:
            value: The authentication to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_authentication("value")
        """
        self.authentication = value  # Use property setter (gets validation)
        return self

    def with_environmental(self, value: Optional["Diagnostic"]) -> DiagnosticAccessPermission:
        """
        Set environmental and return self for chaining.

        Args:
            value: The environmental to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_environmental("value")
        """
        self.environmental = value  # Use property setter (gets validation)
        return self



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
        self._p2ServerMax: Optional[TimeValue] = None

    @property
    def p2_server_max(self) -> Optional[TimeValue]:
        """Get p2ServerMax (Pythonic accessor)."""
        return self._p2ServerMax

    @p2_server_max.setter
    def p2_server_max(self, value: Optional[TimeValue]) -> None:
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
        self._p2StarServer: Optional[TimeValue] = None

    @property
    def p2_star_server(self) -> Optional[TimeValue]:
        """Get p2StarServer (Pythonic accessor)."""
        return self._p2StarServer

    @p2_star_server.setter
    def p2_star_server(self, value: Optional[TimeValue]) -> None:
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

    def getId(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for id.

        Returns:
            The id value

        Note:
            Delegates to id property (CODING_RULE_V2_00017)
        """
        return self.id  # Delegates to property

    def setId(self, value: PositiveInteger) -> DiagnosticSession:
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

    def setJumpToBoot(self, value: "DiagnosticJumpToBoot") -> DiagnosticSession:
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

    def getP2ServerMax(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for p2ServerMax.

        Returns:
            The p2ServerMax value

        Note:
            Delegates to p2_server_max property (CODING_RULE_V2_00017)
        """
        return self.p2_server_max  # Delegates to property

    def setP2ServerMax(self, value: TimeValue) -> DiagnosticSession:
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

    def getP2StarServer(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for p2StarServer.

        Returns:
            The p2StarServer value

        Note:
            Delegates to p2_star_server property (CODING_RULE_V2_00017)
        """
        return self.p2_star_server  # Delegates to property

    def setP2StarServer(self, value: TimeValue) -> DiagnosticSession:
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

    def with_id(self, value: Optional[PositiveInteger]) -> DiagnosticSession:
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

    def with_jump_to_boot(self, value: Optional["DiagnosticJumpToBoot"]) -> DiagnosticSession:
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

    def with_p2_server_max(self, value: Optional[TimeValue]) -> DiagnosticSession:
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

    def with_p2_star_server(self, value: Optional[TimeValue]) -> DiagnosticSession:
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



class DiagnosticSecurityLevel(DiagnosticCommonElement):
    """
    This meta-class represents the ability to define a security level considered
    for diagnostic purposes.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticSecurityLevel

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 75, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the size of the AccessDataRecord used GetSeed.
        # Unit:byte.
        self._accessData: Optional[PositiveInteger] = None

    @property
    def access_data(self) -> Optional[PositiveInteger]:
        """Get accessData (Pythonic accessor)."""
        return self._accessData

    @access_data.setter
    def access_data(self, value: Optional[PositiveInteger]) -> None:
        """
        Set accessData with validation.

        Args:
            value: The accessData to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._accessData = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"accessData must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._accessData = value
        # This represents the size of the security key.
        # Unit: byte.
        self._keySize: Optional[PositiveInteger] = None

    @property
    def key_size(self) -> Optional[PositiveInteger]:
        """Get keySize (Pythonic accessor)."""
        return self._keySize

    @key_size.setter
    def key_size(self, value: Optional[PositiveInteger]) -> None:
        """
        Set keySize with validation.

        Args:
            value: The keySize to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._keySize = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"keySize must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._keySize = value
        # This represents the number of failed security accesses which the delay time
        # is activated.
        self._numFailed: Optional[PositiveInteger] = None

    @property
    def num_failed(self) -> Optional[PositiveInteger]:
        """Get numFailed (Pythonic accessor)."""
        return self._numFailed

    @num_failed.setter
    def num_failed(self, value: Optional[PositiveInteger]) -> None:
        """
        Set numFailed with validation.

        Args:
            value: The numFailed to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._numFailed = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"numFailed must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._numFailed = value
        # This represents the delay time after a failed security Unit: second.
        self._securityDelay: Optional[TimeValue] = None

    @property
    def security_delay(self) -> Optional[TimeValue]:
        """Get securityDelay (Pythonic accessor)."""
        return self._securityDelay

    @security_delay.setter
    def security_delay(self, value: Optional[TimeValue]) -> None:
        """
        Set securityDelay with validation.

        Args:
            value: The securityDelay to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._securityDelay = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"securityDelay must be TimeValue or None, got {type(value).__name__}"
            )
        self._securityDelay = value
        # This represents the size of the security seed.
        # Unit: byte.
        self._seedSize: Optional[PositiveInteger] = None

    @property
    def seed_size(self) -> Optional[PositiveInteger]:
        """Get seedSize (Pythonic accessor)."""
        return self._seedSize

    @seed_size.setter
    def seed_size(self, value: Optional[PositiveInteger]) -> None:
        """
        Set seedSize with validation.

        Args:
            value: The seedSize to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._seedSize = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"seedSize must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._seedSize = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAccessData(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for accessData.

        Returns:
            The accessData value

        Note:
            Delegates to access_data property (CODING_RULE_V2_00017)
        """
        return self.access_data  # Delegates to property

    def setAccessData(self, value: PositiveInteger) -> DiagnosticSecurityLevel:
        """
        AUTOSAR-compliant setter for accessData with method chaining.

        Args:
            value: The accessData to set

        Returns:
            self for method chaining

        Note:
            Delegates to access_data property setter (gets validation automatically)
        """
        self.access_data = value  # Delegates to property setter
        return self

    def getKeySize(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for keySize.

        Returns:
            The keySize value

        Note:
            Delegates to key_size property (CODING_RULE_V2_00017)
        """
        return self.key_size  # Delegates to property

    def setKeySize(self, value: PositiveInteger) -> DiagnosticSecurityLevel:
        """
        AUTOSAR-compliant setter for keySize with method chaining.

        Args:
            value: The keySize to set

        Returns:
            self for method chaining

        Note:
            Delegates to key_size property setter (gets validation automatically)
        """
        self.key_size = value  # Delegates to property setter
        return self

    def getNumFailed(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for numFailed.

        Returns:
            The numFailed value

        Note:
            Delegates to num_failed property (CODING_RULE_V2_00017)
        """
        return self.num_failed  # Delegates to property

    def setNumFailed(self, value: PositiveInteger) -> DiagnosticSecurityLevel:
        """
        AUTOSAR-compliant setter for numFailed with method chaining.

        Args:
            value: The numFailed to set

        Returns:
            self for method chaining

        Note:
            Delegates to num_failed property setter (gets validation automatically)
        """
        self.num_failed = value  # Delegates to property setter
        return self

    def getSecurityDelay(self) -> TimeValue:
        """
        AUTOSAR-compliant getter for securityDelay.

        Returns:
            The securityDelay value

        Note:
            Delegates to security_delay property (CODING_RULE_V2_00017)
        """
        return self.security_delay  # Delegates to property

    def setSecurityDelay(self, value: TimeValue) -> DiagnosticSecurityLevel:
        """
        AUTOSAR-compliant setter for securityDelay with method chaining.

        Args:
            value: The securityDelay to set

        Returns:
            self for method chaining

        Note:
            Delegates to security_delay property setter (gets validation automatically)
        """
        self.security_delay = value  # Delegates to property setter
        return self

    def getSeedSize(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for seedSize.

        Returns:
            The seedSize value

        Note:
            Delegates to seed_size property (CODING_RULE_V2_00017)
        """
        return self.seed_size  # Delegates to property

    def setSeedSize(self, value: PositiveInteger) -> DiagnosticSecurityLevel:
        """
        AUTOSAR-compliant setter for seedSize with method chaining.

        Args:
            value: The seedSize to set

        Returns:
            self for method chaining

        Note:
            Delegates to seed_size property setter (gets validation automatically)
        """
        self.seed_size = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_access_data(self, value: Optional[PositiveInteger]) -> DiagnosticSecurityLevel:
        """
        Set accessData and return self for chaining.

        Args:
            value: The accessData to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_access_data("value")
        """
        self.access_data = value  # Use property setter (gets validation)
        return self

    def with_key_size(self, value: Optional[PositiveInteger]) -> DiagnosticSecurityLevel:
        """
        Set keySize and return self for chaining.

        Args:
            value: The keySize to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_key_size("value")
        """
        self.key_size = value  # Use property setter (gets validation)
        return self

    def with_num_failed(self, value: Optional[PositiveInteger]) -> DiagnosticSecurityLevel:
        """
        Set numFailed and return self for chaining.

        Args:
            value: The numFailed to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_num_failed("value")
        """
        self.num_failed = value  # Use property setter (gets validation)
        return self

    def with_security_delay(self, value: Optional[TimeValue]) -> DiagnosticSecurityLevel:
        """
        Set securityDelay and return self for chaining.

        Args:
            value: The securityDelay to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_security_delay("value")
        """
        self.security_delay = value  # Use property setter (gets validation)
        return self

    def with_seed_size(self, value: Optional[PositiveInteger]) -> DiagnosticSecurityLevel:
        """
        Set seedSize and return self for chaining.

        Args:
            value: The seedSize to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_seed_size("value")
        """
        self.seed_size = value  # Use property setter (gets validation)
        return self



class DiagnosticAuthRoleProxy(ARObject):
    """
    This meta-class indicates that an authentication is generally foreseen. The
    question whether the authentication is done in general or whether it is done
    role-specific depends on the existence of references to DiagAuthRole.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticAuthRoleProxy

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 76, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference identifies the authenticationRole applicable the enclosing
        # DiagnosticAccessPermission.
        self._authentication: List[DiagnosticAuthRole] = []

    @property
    def authentication(self) -> List[DiagnosticAuthRole]:
        """Get authentication (Pythonic accessor)."""
        return self._authentication

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAuthentication(self) -> List[DiagnosticAuthRole]:
        """
        AUTOSAR-compliant getter for authentication.

        Returns:
            The authentication value

        Note:
            Delegates to authentication property (CODING_RULE_V2_00017)
        """
        return self.authentication  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class DiagnosticAuthRole(DiagnosticCommonElement):
    """
    This meta-class represents the ability to specify an authentication role
    that can be used to deliver fine-grained access rights.

    Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm::DiagnosticAuthRole

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 77, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute allows for the specification of the position of role in a
        # bitfield of roles.
        self._bitPosition: Optional[PositiveInteger] = None

    @property
    def bit_position(self) -> Optional[PositiveInteger]:
        """Get bitPosition (Pythonic accessor)."""
        return self._bitPosition

    @bit_position.setter
    def bit_position(self, value: Optional[PositiveInteger]) -> None:
        """
        Set bitPosition with validation.

        Args:
            value: The bitPosition to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._bitPosition = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"bitPosition must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._bitPosition = value
        # This attribute indicates whether the enclosing role is default role.
        self._isDefault: Optional[Boolean] = None

    @property
    def is_default(self) -> Optional[Boolean]:
        """Get isDefault (Pythonic accessor)."""
        return self._isDefault

    @is_default.setter
    def is_default(self, value: Optional[Boolean]) -> None:
        """
        Set isDefault with validation.

        Args:
            value: The isDefault to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._isDefault = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"isDefault must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._isDefault = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBitPosition(self) -> PositiveInteger:
        """
        AUTOSAR-compliant getter for bitPosition.

        Returns:
            The bitPosition value

        Note:
            Delegates to bit_position property (CODING_RULE_V2_00017)
        """
        return self.bit_position  # Delegates to property

    def setBitPosition(self, value: PositiveInteger) -> DiagnosticAuthRole:
        """
        AUTOSAR-compliant setter for bitPosition with method chaining.

        Args:
            value: The bitPosition to set

        Returns:
            self for method chaining

        Note:
            Delegates to bit_position property setter (gets validation automatically)
        """
        self.bit_position = value  # Delegates to property setter
        return self

    def getIsDefault(self) -> Boolean:
        """
        AUTOSAR-compliant getter for isDefault.

        Returns:
            The isDefault value

        Note:
            Delegates to is_default property (CODING_RULE_V2_00017)
        """
        return self.is_default  # Delegates to property

    def setIsDefault(self, value: Boolean) -> DiagnosticAuthRole:
        """
        AUTOSAR-compliant setter for isDefault with method chaining.

        Args:
            value: The isDefault to set

        Returns:
            self for method chaining

        Note:
            Delegates to is_default property setter (gets validation automatically)
        """
        self.is_default = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_bit_position(self, value: Optional[PositiveInteger]) -> DiagnosticAuthRole:
        """
        Set bitPosition and return self for chaining.

        Args:
            value: The bitPosition to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_bit_position("value")
        """
        self.bit_position = value  # Use property setter (gets validation)
        return self

    def with_is_default(self, value: Optional[Boolean]) -> DiagnosticAuthRole:
        """
        Set isDefault and return self for chaining.

        Args:
            value: The isDefault to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_is_default("value")
        """
        self.is_default = value  # Use property setter (gets validation)
        return self


class DiagnosticJumpToBootLoaderEnum(AREnum):
    """
    DiagnosticJumpToBootLoaderEnum enumeration

This enumeration contains the options for jumping to a boot loader. Aggregated by DiagnosticSession.jumpToBootLoader

Package: M2::AUTOSARTemplates::DiagnosticExtract::Dcm
    """
    # This diagnostic session doesn’t allow to jump to Bootloader.
    noBoot = "0"

    # This diagnostic session allows to jump to OEM Bootloader. In this case the bootloader send the final
    oemBoot = "1"

    # This diagnostic session allows to jump to OEM Bootloader and application sends final response.
    oemBootRespApp = "3"

    # This diagnostic session allows to jump to System Supplier Bootloader. In this case the bootloader send the final response.
    systemSupplierBoot = "2"

    # This diagnostic session allows to jump to System Supplier Bootloader and application sends final RespApp response.
    systemSupplierBoot = "4"


__all__ = [
    DiagnosticAccessPermission,
    DiagnosticSession,
    DiagnosticSecurityLevel,
    DiagnosticAuthRoleProxy,
    DiagnosticAuthRole,
    DiagnosticJumpToBootLoaderEnum,
]

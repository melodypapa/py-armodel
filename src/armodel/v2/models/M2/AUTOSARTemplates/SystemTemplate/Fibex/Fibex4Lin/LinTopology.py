from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class LinCluster(ARObject):
    """
    LIN specific attributes

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Lin::LinTopology

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 93, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

from abc import ABC
from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class LinCommunicationController(ARObject, ABC):
    """
    LIN bus specific communication controller attributes.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Lin::LinTopology

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 93, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is LinCommunicationController:
            raise TypeError("LinCommunicationController is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Version specifier for a communication protocol.
        self._protocolVersion: Optional["String"] = None

    @property
    def protocol_version(self) -> Optional["String"]:
        """Get protocolVersion (Pythonic accessor)."""
        return self._protocolVersion

    @protocol_version.setter
    def protocol_version(self, value: Optional["String"]) -> None:
        """
        Set protocolVersion with validation.

        Args:
            value: The protocolVersion to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._protocolVersion = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"protocolVersion must be String or None, got {type(value).__name__}"
            )
        self._protocolVersion = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getProtocolVersion(self) -> "String":
        """
        AUTOSAR-compliant getter for protocolVersion.

        Returns:
            The protocolVersion value

        Note:
            Delegates to protocol_version property (CODING_RULE_V2_00017)
        """
        return self.protocol_version  # Delegates to property

    def setProtocolVersion(self, value: "String") -> "LinCommunicationController":
        """
        AUTOSAR-compliant setter for protocolVersion with method chaining.

        Args:
            value: The protocolVersion to set

        Returns:
            self for method chaining

        Note:
            Delegates to protocol_version property setter (gets validation automatically)
        """
        self.protocol_version = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_protocol_version(self, value: Optional["String"]) -> "LinCommunicationController":
        """
        Set protocolVersion and return self for chaining.

        Args:
            value: The protocolVersion to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_protocol_version("value")
        """
        self.protocol_version = value  # Use property setter (gets validation)
        return self

from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class LinMaster(ARObject):
    """
    Describing the properties of the refering ecu as a LIN master.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Lin::LinTopology

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 94, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # LinSlaves that are handled by the LinMaster.
        self._linSlave: List["LinSlaveConfig"] = []

    @property
    def lin_slave(self) -> List["LinSlaveConfig"]:
        """Get linSlave (Pythonic accessor)."""
        return self._linSlave
        # Time base is mandatory for the master.
        # It is not used for Spec states: "The time_base value specifies the base in
                # the master node to generate the frame transfer time.
        # " base shall be specified AUTOSAR conform in.
        self._timeBase: Optional["TimeValue"] = None

    @property
    def time_base(self) -> Optional["TimeValue"]:
        """Get timeBase (Pythonic accessor)."""
        return self._timeBase

    @time_base.setter
    def time_base(self, value: Optional["TimeValue"]) -> None:
        """
        Set timeBase with validation.

        Args:
            value: The timeBase to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeBase = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"timeBase must be TimeValue or None, got {type(value).__name__}"
            )
        self._timeBase = value
        # The attribute timeBaseJitter is a mandatory attribute for and not used for
                # slaves.
        # Spec states: "The jitter value specifies the the maximum and minimum delay
                # base start point to the frame header sending (falling edge of BREAK signal).
        # " shall be specified AUTOSAR conform in.
        self._timeBaseJitter: Optional["TimeValue"] = None

    @property
    def time_base_jitter(self) -> Optional["TimeValue"]:
        """Get timeBaseJitter (Pythonic accessor)."""
        return self._timeBaseJitter

    @time_base_jitter.setter
    def time_base_jitter(self, value: Optional["TimeValue"]) -> None:
        """
        Set timeBaseJitter with validation.

        Args:
            value: The timeBaseJitter to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeBaseJitter = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"timeBaseJitter must be TimeValue or None, got {type(value).__name__}"
            )
        self._timeBaseJitter = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getLinSlave(self) -> List["LinSlaveConfig"]:
        """
        AUTOSAR-compliant getter for linSlave.

        Returns:
            The linSlave value

        Note:
            Delegates to lin_slave property (CODING_RULE_V2_00017)
        """
        return self.lin_slave  # Delegates to property

    def getTimeBase(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for timeBase.

        Returns:
            The timeBase value

        Note:
            Delegates to time_base property (CODING_RULE_V2_00017)
        """
        return self.time_base  # Delegates to property

    def setTimeBase(self, value: "TimeValue") -> "LinMaster":
        """
        AUTOSAR-compliant setter for timeBase with method chaining.

        Args:
            value: The timeBase to set

        Returns:
            self for method chaining

        Note:
            Delegates to time_base property setter (gets validation automatically)
        """
        self.time_base = value  # Delegates to property setter
        return self

    def getTimeBaseJitter(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for timeBaseJitter.

        Returns:
            The timeBaseJitter value

        Note:
            Delegates to time_base_jitter property (CODING_RULE_V2_00017)
        """
        return self.time_base_jitter  # Delegates to property

    def setTimeBaseJitter(self, value: "TimeValue") -> "LinMaster":
        """
        AUTOSAR-compliant setter for timeBaseJitter with method chaining.

        Args:
            value: The timeBaseJitter to set

        Returns:
            self for method chaining

        Note:
            Delegates to time_base_jitter property setter (gets validation automatically)
        """
        self.time_base_jitter = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_time_base(self, value: Optional["TimeValue"]) -> "LinMaster":
        """
        Set timeBase and return self for chaining.

        Args:
            value: The timeBase to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_time_base("value")
        """
        self.time_base = value  # Use property setter (gets validation)
        return self

    def with_time_base_jitter(self, value: Optional["TimeValue"]) -> "LinMaster":
        """
        Set timeBaseJitter and return self for chaining.

        Args:
            value: The timeBaseJitter to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_time_base_jitter("value")
        """
        self.time_base_jitter = value  # Use property setter (gets validation)
        return self

from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class LinSlaveConfig(ARObject):
    """
    Node attributes of LIN slaves that are handled by the LinMaster. In the
    System Description LIN slaves may be described in the context of the Lin
    Master. In an ECU Extract of the LinMaster the LinSlave Ecus shall not be
    available. The information that is described here is necessary in the ECU
    Extract for the configuration of the Lin Master. The values of attributes of
    LinSlaveConfig and the corresponding LinSlave shall be identical (if both
    are defined in a System Description).

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Lin::LinTopology

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 94, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # To distinguish LIN slaves that are used twice or more same cluster.
        self._configuredNad: Optional["Integer"] = None

    @property
    def configured_nad(self) -> Optional["Integer"]:
        """Get configuredNad (Pythonic accessor)."""
        return self._configuredNad

    @configured_nad.setter
    def configured_nad(self, value: Optional["Integer"]) -> None:
        """
        Set configuredNad with validation.

        Args:
            value: The configuredNad to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._configuredNad = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"configuredNad must be Integer or None, got {type(value).__name__}"
            )
        self._configuredNad = value
        # LIN function ID.
        self._functionId: Optional["PositiveInteger"] = None

    @property
    def function_id(self) -> Optional["PositiveInteger"]:
        """Get functionId (Pythonic accessor)."""
        return self._functionId

    @function_id.setter
    def function_id(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set functionId with validation.

        Args:
            value: The functionId to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._functionId = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"functionId must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._functionId = value
        # This adds the ability to become referrable to LinSlave.
        self._ident: Optional["LinSlaveConfigIdent"] = None

    @property
    def ident(self) -> Optional["LinSlaveConfigIdent"]:
        """Get ident (Pythonic accessor)."""
        return self._ident

    @ident.setter
    def ident(self, value: Optional["LinSlaveConfigIdent"]) -> None:
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

        if not isinstance(value, LinSlaveConfigIdent):
            raise TypeError(
                f"ident must be LinSlaveConfigIdent or None, got {type(value).__name__}"
            )
        self._ident = value
        # Initial NAD of the LIN slave.
        self._initialNad: Optional["Integer"] = None

    @property
    def initial_nad(self) -> Optional["Integer"]:
        """Get initialNad (Pythonic accessor)."""
        return self._initialNad

    @initial_nad.setter
    def initial_nad(self, value: Optional["Integer"]) -> None:
        """
        Set initialNad with validation.

        Args:
            value: The initialNad to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._initialNad = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"initialNad must be Integer or None, got {type(value).__name__}"
            )
        self._initialNad = value
        # List of all frames that are processed by the slave node 2090 Document ID 63:
        # AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._linConfigurable: List["LinConfigurableFrame"] = []

    @property
    def lin_configurable(self) -> List["LinConfigurableFrame"]:
        """Get linConfigurable (Pythonic accessor)."""
        return self._linConfigurable
        # Each slave node shall publish one response error in one its transmitted
        # unconditional frames.
        self._linError: Optional["LinErrorResponse"] = None

    @property
    def lin_error(self) -> Optional["LinErrorResponse"]:
        """Get linError (Pythonic accessor)."""
        return self._linError

    @lin_error.setter
    def lin_error(self, value: Optional["LinErrorResponse"]) -> None:
        """
        Set linError with validation.

        Args:
            value: The linError to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._linError = None
            return

        if not isinstance(value, LinErrorResponse):
            raise TypeError(
                f"linError must be LinErrorResponse or None, got {type(value).__name__}"
            )
        self._linError = value
        # List of all frames (unconditional frames, event-triggered frames and sporadic
                # frames) processed by the slave This element is necessary for the LIN 2.
        # 1.
        self._linOrdered: List["LinOrderedConfigurable"] = []

    @property
    def lin_ordered(self) -> List["LinOrderedConfigurable"]:
        """Get linOrdered (Pythonic accessor)."""
        return self._linOrdered
        # Version specifier for a communication protocol.
        # Protocol the LinMaster and the LinSlaves may be.
        self._protocolVersion: Optional["String"] = None

    @property
    def protocol_version(self) -> Optional["String"]:
        """Get protocolVersion (Pythonic accessor)."""
        return self._protocolVersion

    @protocol_version.setter
    def protocol_version(self, value: Optional["String"]) -> None:
        """
        Set protocolVersion with validation.

        Args:
            value: The protocolVersion to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._protocolVersion = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"protocolVersion must be String or None, got {type(value).__name__}"
            )
        self._protocolVersion = value
        # LIN Supplier ID.
        self._supplierId: Optional["PositiveInteger"] = None

    @property
    def supplier_id(self) -> Optional["PositiveInteger"]:
        """Get supplierId (Pythonic accessor)."""
        return self._supplierId

    @supplier_id.setter
    def supplier_id(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set supplierId with validation.

        Args:
            value: The supplierId to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._supplierId = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"supplierId must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._supplierId = value
        # Specifies the Variant ID.
        self._variantId: Optional["PositiveInteger"] = None

    @property
    def variant_id(self) -> Optional["PositiveInteger"]:
        """Get variantId (Pythonic accessor)."""
        return self._variantId

    @variant_id.setter
    def variant_id(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set variantId with validation.

        Args:
            value: The variantId to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._variantId = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"variantId must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._variantId = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getConfiguredNad(self) -> "Integer":
        """
        AUTOSAR-compliant getter for configuredNad.

        Returns:
            The configuredNad value

        Note:
            Delegates to configured_nad property (CODING_RULE_V2_00017)
        """
        return self.configured_nad  # Delegates to property

    def setConfiguredNad(self, value: "Integer") -> "LinSlaveConfig":
        """
        AUTOSAR-compliant setter for configuredNad with method chaining.

        Args:
            value: The configuredNad to set

        Returns:
            self for method chaining

        Note:
            Delegates to configured_nad property setter (gets validation automatically)
        """
        self.configured_nad = value  # Delegates to property setter
        return self

    def getFunctionId(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for functionId.

        Returns:
            The functionId value

        Note:
            Delegates to function_id property (CODING_RULE_V2_00017)
        """
        return self.function_id  # Delegates to property

    def setFunctionId(self, value: "PositiveInteger") -> "LinSlaveConfig":
        """
        AUTOSAR-compliant setter for functionId with method chaining.

        Args:
            value: The functionId to set

        Returns:
            self for method chaining

        Note:
            Delegates to function_id property setter (gets validation automatically)
        """
        self.function_id = value  # Delegates to property setter
        return self

    def getIdent(self) -> "LinSlaveConfigIdent":
        """
        AUTOSAR-compliant getter for ident.

        Returns:
            The ident value

        Note:
            Delegates to ident property (CODING_RULE_V2_00017)
        """
        return self.ident  # Delegates to property

    def setIdent(self, value: "LinSlaveConfigIdent") -> "LinSlaveConfig":
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

    def getInitialNad(self) -> "Integer":
        """
        AUTOSAR-compliant getter for initialNad.

        Returns:
            The initialNad value

        Note:
            Delegates to initial_nad property (CODING_RULE_V2_00017)
        """
        return self.initial_nad  # Delegates to property

    def setInitialNad(self, value: "Integer") -> "LinSlaveConfig":
        """
        AUTOSAR-compliant setter for initialNad with method chaining.

        Args:
            value: The initialNad to set

        Returns:
            self for method chaining

        Note:
            Delegates to initial_nad property setter (gets validation automatically)
        """
        self.initial_nad = value  # Delegates to property setter
        return self

    def getLinConfigurable(self) -> List["LinConfigurableFrame"]:
        """
        AUTOSAR-compliant getter for linConfigurable.

        Returns:
            The linConfigurable value

        Note:
            Delegates to lin_configurable property (CODING_RULE_V2_00017)
        """
        return self.lin_configurable  # Delegates to property

    def getLinError(self) -> "LinErrorResponse":
        """
        AUTOSAR-compliant getter for linError.

        Returns:
            The linError value

        Note:
            Delegates to lin_error property (CODING_RULE_V2_00017)
        """
        return self.lin_error  # Delegates to property

    def setLinError(self, value: "LinErrorResponse") -> "LinSlaveConfig":
        """
        AUTOSAR-compliant setter for linError with method chaining.

        Args:
            value: The linError to set

        Returns:
            self for method chaining

        Note:
            Delegates to lin_error property setter (gets validation automatically)
        """
        self.lin_error = value  # Delegates to property setter
        return self

    def getLinOrdered(self) -> List["LinOrderedConfigurable"]:
        """
        AUTOSAR-compliant getter for linOrdered.

        Returns:
            The linOrdered value

        Note:
            Delegates to lin_ordered property (CODING_RULE_V2_00017)
        """
        return self.lin_ordered  # Delegates to property

    def getProtocolVersion(self) -> "String":
        """
        AUTOSAR-compliant getter for protocolVersion.

        Returns:
            The protocolVersion value

        Note:
            Delegates to protocol_version property (CODING_RULE_V2_00017)
        """
        return self.protocol_version  # Delegates to property

    def setProtocolVersion(self, value: "String") -> "LinSlaveConfig":
        """
        AUTOSAR-compliant setter for protocolVersion with method chaining.

        Args:
            value: The protocolVersion to set

        Returns:
            self for method chaining

        Note:
            Delegates to protocol_version property setter (gets validation automatically)
        """
        self.protocol_version = value  # Delegates to property setter
        return self

    def getSupplierId(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for supplierId.

        Returns:
            The supplierId value

        Note:
            Delegates to supplier_id property (CODING_RULE_V2_00017)
        """
        return self.supplier_id  # Delegates to property

    def setSupplierId(self, value: "PositiveInteger") -> "LinSlaveConfig":
        """
        AUTOSAR-compliant setter for supplierId with method chaining.

        Args:
            value: The supplierId to set

        Returns:
            self for method chaining

        Note:
            Delegates to supplier_id property setter (gets validation automatically)
        """
        self.supplier_id = value  # Delegates to property setter
        return self

    def getVariantId(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for variantId.

        Returns:
            The variantId value

        Note:
            Delegates to variant_id property (CODING_RULE_V2_00017)
        """
        return self.variant_id  # Delegates to property

    def setVariantId(self, value: "PositiveInteger") -> "LinSlaveConfig":
        """
        AUTOSAR-compliant setter for variantId with method chaining.

        Args:
            value: The variantId to set

        Returns:
            self for method chaining

        Note:
            Delegates to variant_id property setter (gets validation automatically)
        """
        self.variant_id = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_configured_nad(self, value: Optional["Integer"]) -> "LinSlaveConfig":
        """
        Set configuredNad and return self for chaining.

        Args:
            value: The configuredNad to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_configured_nad("value")
        """
        self.configured_nad = value  # Use property setter (gets validation)
        return self

    def with_function_id(self, value: Optional["PositiveInteger"]) -> "LinSlaveConfig":
        """
        Set functionId and return self for chaining.

        Args:
            value: The functionId to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_function_id("value")
        """
        self.function_id = value  # Use property setter (gets validation)
        return self

    def with_ident(self, value: Optional["LinSlaveConfigIdent"]) -> "LinSlaveConfig":
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

    def with_initial_nad(self, value: Optional["Integer"]) -> "LinSlaveConfig":
        """
        Set initialNad and return self for chaining.

        Args:
            value: The initialNad to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_initial_nad("value")
        """
        self.initial_nad = value  # Use property setter (gets validation)
        return self

    def with_lin_error(self, value: Optional["LinErrorResponse"]) -> "LinSlaveConfig":
        """
        Set linError and return self for chaining.

        Args:
            value: The linError to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_lin_error("value")
        """
        self.lin_error = value  # Use property setter (gets validation)
        return self

    def with_protocol_version(self, value: Optional["String"]) -> "LinSlaveConfig":
        """
        Set protocolVersion and return self for chaining.

        Args:
            value: The protocolVersion to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_protocol_version("value")
        """
        self.protocol_version = value  # Use property setter (gets validation)
        return self

    def with_supplier_id(self, value: Optional["PositiveInteger"]) -> "LinSlaveConfig":
        """
        Set supplierId and return self for chaining.

        Args:
            value: The supplierId to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_supplier_id("value")
        """
        self.supplier_id = value  # Use property setter (gets validation)
        return self

    def with_variant_id(self, value: Optional["PositiveInteger"]) -> "LinSlaveConfig":
        """
        Set variantId and return self for chaining.

        Args:
            value: The variantId to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_variant_id("value")
        """
        self.variant_id = value  # Use property setter (gets validation)
        return self

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Referrable import (
    Referrable,
)


class LinSlaveConfigIdent(Referrable):
    """
    This meta-class is created to add the ability to become the target of a
    reference to the non-Referrable Lin SlaveConfig.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Lin::LinTopology

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 95, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class LinSlave(ARObject):
    """
    Describing the properties of the referring ecu as a LIN slave.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Lin::LinTopology

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 97, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute has the ability to control whether the node ’Assign NAD’ is
        # supported.
        self._assignNad: Optional["Boolean"] = None

    @property
    def assign_nad(self) -> Optional["Boolean"]:
        """Get assignNad (Pythonic accessor)."""
        return self._assignNad

    @assign_nad.setter
    def assign_nad(self, value: Optional["Boolean"]) -> None:
        """
        Set assignNad with validation.

        Args:
            value: The assignNad to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._assignNad = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"assignNad must be Boolean or None, got {type(value).__name__}"
            )
        self._assignNad = value
        # To distinguish LIN slaves that are used twice or more same cluster.
        self._configuredNad: Optional["Integer"] = None

    @property
    def configured_nad(self) -> Optional["Integer"]:
        """Get configuredNad (Pythonic accessor)."""
        return self._configuredNad

    @configured_nad.setter
    def configured_nad(self, value: Optional["Integer"]) -> None:
        """
        Set configuredNad with validation.

        Args:
            value: The configuredNad to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._configuredNad = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"configuredNad must be Integer or None, got {type(value).__name__}"
            )
        self._configuredNad = value
        # LIN function ID.
        self._functionId: Optional["PositiveInteger"] = None

    @property
    def function_id(self) -> Optional["PositiveInteger"]:
        """Get functionId (Pythonic accessor)."""
        return self._functionId

    @function_id.setter
    def function_id(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set functionId with validation.

        Args:
            value: The functionId to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._functionId = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"functionId must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._functionId = value
        # This attribute represents the initial NAD.
        self._initialNad: Optional["Integer"] = None

    @property
    def initial_nad(self) -> Optional["Integer"]:
        """Get initialNad (Pythonic accessor)."""
        return self._initialNad

    @initial_nad.setter
    def initial_nad(self, value: Optional["Integer"]) -> None:
        """
        Set initialNad with validation.

        Args:
            value: The initialNad to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._initialNad = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"initialNad must be Integer or None, got {type(value).__name__}"
            )
        self._initialNad = value
        # Each slave node shall publish one response error in one its transmitted
        # unconditional frames.
        self._linError: Optional["LinErrorResponse"] = None

    @property
    def lin_error(self) -> Optional["LinErrorResponse"]:
        """Get linError (Pythonic accessor)."""
        return self._linError

    @lin_error.setter
    def lin_error(self, value: Optional["LinErrorResponse"]) -> None:
        """
        Set linError with validation.

        Args:
            value: The linError to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._linError = None
            return

        if not isinstance(value, LinErrorResponse):
            raise TypeError(
                f"linError must be LinErrorResponse or None, got {type(value).__name__}"
            )
        self._linError = value
        # Value of the N_AS timeout.
        # Unit: seconds.
        self._nasTimeout: Optional["TimeValue"] = None

    @property
    def nas_timeout(self) -> Optional["TimeValue"]:
        """Get nasTimeout (Pythonic accessor)."""
        return self._nasTimeout

    @nas_timeout.setter
    def nas_timeout(self, value: Optional["TimeValue"]) -> None:
        """
        Set nasTimeout with validation.

        Args:
            value: The nasTimeout to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nasTimeout = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"nasTimeout must be TimeValue or None, got {type(value).__name__}"
            )
        self._nasTimeout = value
        # LIN Supplier ID.
        self._supplierId: Optional["PositiveInteger"] = None

    @property
    def supplier_id(self) -> Optional["PositiveInteger"]:
        """Get supplierId (Pythonic accessor)."""
        return self._supplierId

    @supplier_id.setter
    def supplier_id(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set supplierId with validation.

        Args:
            value: The supplierId to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._supplierId = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"supplierId must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._supplierId = value
        # Specifies the Variant ID.
        self._variantId: Optional["PositiveInteger"] = None

    @property
    def variant_id(self) -> Optional["PositiveInteger"]:
        """Get variantId (Pythonic accessor)."""
        return self._variantId

    @variant_id.setter
    def variant_id(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set variantId with validation.

        Args:
            value: The variantId to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._variantId = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"variantId must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._variantId = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAssignNad(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for assignNad.

        Returns:
            The assignNad value

        Note:
            Delegates to assign_nad property (CODING_RULE_V2_00017)
        """
        return self.assign_nad  # Delegates to property

    def setAssignNad(self, value: "Boolean") -> "LinSlave":
        """
        AUTOSAR-compliant setter for assignNad with method chaining.

        Args:
            value: The assignNad to set

        Returns:
            self for method chaining

        Note:
            Delegates to assign_nad property setter (gets validation automatically)
        """
        self.assign_nad = value  # Delegates to property setter
        return self

    def getConfiguredNad(self) -> "Integer":
        """
        AUTOSAR-compliant getter for configuredNad.

        Returns:
            The configuredNad value

        Note:
            Delegates to configured_nad property (CODING_RULE_V2_00017)
        """
        return self.configured_nad  # Delegates to property

    def setConfiguredNad(self, value: "Integer") -> "LinSlave":
        """
        AUTOSAR-compliant setter for configuredNad with method chaining.

        Args:
            value: The configuredNad to set

        Returns:
            self for method chaining

        Note:
            Delegates to configured_nad property setter (gets validation automatically)
        """
        self.configured_nad = value  # Delegates to property setter
        return self

    def getFunctionId(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for functionId.

        Returns:
            The functionId value

        Note:
            Delegates to function_id property (CODING_RULE_V2_00017)
        """
        return self.function_id  # Delegates to property

    def setFunctionId(self, value: "PositiveInteger") -> "LinSlave":
        """
        AUTOSAR-compliant setter for functionId with method chaining.

        Args:
            value: The functionId to set

        Returns:
            self for method chaining

        Note:
            Delegates to function_id property setter (gets validation automatically)
        """
        self.function_id = value  # Delegates to property setter
        return self

    def getInitialNad(self) -> "Integer":
        """
        AUTOSAR-compliant getter for initialNad.

        Returns:
            The initialNad value

        Note:
            Delegates to initial_nad property (CODING_RULE_V2_00017)
        """
        return self.initial_nad  # Delegates to property

    def setInitialNad(self, value: "Integer") -> "LinSlave":
        """
        AUTOSAR-compliant setter for initialNad with method chaining.

        Args:
            value: The initialNad to set

        Returns:
            self for method chaining

        Note:
            Delegates to initial_nad property setter (gets validation automatically)
        """
        self.initial_nad = value  # Delegates to property setter
        return self

    def getLinError(self) -> "LinErrorResponse":
        """
        AUTOSAR-compliant getter for linError.

        Returns:
            The linError value

        Note:
            Delegates to lin_error property (CODING_RULE_V2_00017)
        """
        return self.lin_error  # Delegates to property

    def setLinError(self, value: "LinErrorResponse") -> "LinSlave":
        """
        AUTOSAR-compliant setter for linError with method chaining.

        Args:
            value: The linError to set

        Returns:
            self for method chaining

        Note:
            Delegates to lin_error property setter (gets validation automatically)
        """
        self.lin_error = value  # Delegates to property setter
        return self

    def getNasTimeout(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for nasTimeout.

        Returns:
            The nasTimeout value

        Note:
            Delegates to nas_timeout property (CODING_RULE_V2_00017)
        """
        return self.nas_timeout  # Delegates to property

    def setNasTimeout(self, value: "TimeValue") -> "LinSlave":
        """
        AUTOSAR-compliant setter for nasTimeout with method chaining.

        Args:
            value: The nasTimeout to set

        Returns:
            self for method chaining

        Note:
            Delegates to nas_timeout property setter (gets validation automatically)
        """
        self.nas_timeout = value  # Delegates to property setter
        return self

    def getSupplierId(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for supplierId.

        Returns:
            The supplierId value

        Note:
            Delegates to supplier_id property (CODING_RULE_V2_00017)
        """
        return self.supplier_id  # Delegates to property

    def setSupplierId(self, value: "PositiveInteger") -> "LinSlave":
        """
        AUTOSAR-compliant setter for supplierId with method chaining.

        Args:
            value: The supplierId to set

        Returns:
            self for method chaining

        Note:
            Delegates to supplier_id property setter (gets validation automatically)
        """
        self.supplier_id = value  # Delegates to property setter
        return self

    def getVariantId(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for variantId.

        Returns:
            The variantId value

        Note:
            Delegates to variant_id property (CODING_RULE_V2_00017)
        """
        return self.variant_id  # Delegates to property

    def setVariantId(self, value: "PositiveInteger") -> "LinSlave":
        """
        AUTOSAR-compliant setter for variantId with method chaining.

        Args:
            value: The variantId to set

        Returns:
            self for method chaining

        Note:
            Delegates to variant_id property setter (gets validation automatically)
        """
        self.variant_id = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_assign_nad(self, value: Optional["Boolean"]) -> "LinSlave":
        """
        Set assignNad and return self for chaining.

        Args:
            value: The assignNad to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_assign_nad("value")
        """
        self.assign_nad = value  # Use property setter (gets validation)
        return self

    def with_configured_nad(self, value: Optional["Integer"]) -> "LinSlave":
        """
        Set configuredNad and return self for chaining.

        Args:
            value: The configuredNad to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_configured_nad("value")
        """
        self.configured_nad = value  # Use property setter (gets validation)
        return self

    def with_function_id(self, value: Optional["PositiveInteger"]) -> "LinSlave":
        """
        Set functionId and return self for chaining.

        Args:
            value: The functionId to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_function_id("value")
        """
        self.function_id = value  # Use property setter (gets validation)
        return self

    def with_initial_nad(self, value: Optional["Integer"]) -> "LinSlave":
        """
        Set initialNad and return self for chaining.

        Args:
            value: The initialNad to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_initial_nad("value")
        """
        self.initial_nad = value  # Use property setter (gets validation)
        return self

    def with_lin_error(self, value: Optional["LinErrorResponse"]) -> "LinSlave":
        """
        Set linError and return self for chaining.

        Args:
            value: The linError to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_lin_error("value")
        """
        self.lin_error = value  # Use property setter (gets validation)
        return self

    def with_nas_timeout(self, value: Optional["TimeValue"]) -> "LinSlave":
        """
        Set nasTimeout and return self for chaining.

        Args:
            value: The nasTimeout to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nas_timeout("value")
        """
        self.nas_timeout = value  # Use property setter (gets validation)
        return self

    def with_supplier_id(self, value: Optional["PositiveInteger"]) -> "LinSlave":
        """
        Set supplierId and return self for chaining.

        Args:
            value: The supplierId to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_supplier_id("value")
        """
        self.supplier_id = value  # Use property setter (gets validation)
        return self

    def with_variant_id(self, value: Optional["PositiveInteger"]) -> "LinSlave":
        """
        Set variantId and return self for chaining.

        Args:
            value: The variantId to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_variant_id("value")
        """
        self.variant_id = value  # Use property setter (gets validation)
        return self

from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import (
    CommunicationConnector,
)


class LinCommunicationConnector(CommunicationConnector):
    """
    LIN bus specific communication connector attributes.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Lin::LinTopology

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 98, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Initial NAD of the LIN slave.
        self._initialNad: Optional["Integer"] = None

    @property
    def initial_nad(self) -> Optional["Integer"]:
        """Get initialNad (Pythonic accessor)."""
        return self._initialNad

    @initial_nad.setter
    def initial_nad(self, value: Optional["Integer"]) -> None:
        """
        Set initialNad with validation.

        Args:
            value: The initialNad to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._initialNad = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"initialNad must be Integer or None, got {type(value).__name__}"
            )
        self._initialNad = value
        # LinConfigurableFrames shall list all frames (unconditional event-triggered
                # frames and sporadic frames) the slave node.
        # This element is necessary LIN 2.
        # 0 Assign-Frame command.
        self._linConfigurable: List["LinConfigurableFrame"] = []

    @property
    def lin_configurable(self) -> List["LinConfigurableFrame"]:
        """Get linConfigurable (Pythonic accessor)."""
        return self._linConfigurable
        # LinOrderedConfigurableFrames shall list all frames (unconditional frames,
                # event-triggered frames and frames) processed by the slave node.
        # This necessary for the LIN 2.
        # 1.
        self._linOrdered: List["LinOrderedConfigurable"] = []

    @property
    def lin_ordered(self) -> List["LinOrderedConfigurable"]:
        """Get linOrdered (Pythonic accessor)."""
        return self._linOrdered
        # This attribute defines the point in time where a schedule switch is
                # performed.
        # If this attribute is set to false or present, the schedule table shall be
                # switched after the of the active schedule table is ended.
        # If this enabled, the schedule table shall be switched transmission or
                # reception within an entry completed, ensured by status checks for reception.
        self._schedule: Optional["Boolean"] = None

    @property
    def schedule(self) -> Optional["Boolean"]:
        """Get schedule (Pythonic accessor)."""
        return self._schedule

    @schedule.setter
    def schedule(self, value: Optional["Boolean"]) -> None:
        """
        Set schedule with validation.

        Args:
            value: The schedule to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._schedule = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"schedule must be Boolean or None, got {type(value).__name__}"
            )
        self._schedule = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getInitialNad(self) -> "Integer":
        """
        AUTOSAR-compliant getter for initialNad.

        Returns:
            The initialNad value

        Note:
            Delegates to initial_nad property (CODING_RULE_V2_00017)
        """
        return self.initial_nad  # Delegates to property

    def setInitialNad(self, value: "Integer") -> "LinCommunicationConnector":
        """
        AUTOSAR-compliant setter for initialNad with method chaining.

        Args:
            value: The initialNad to set

        Returns:
            self for method chaining

        Note:
            Delegates to initial_nad property setter (gets validation automatically)
        """
        self.initial_nad = value  # Delegates to property setter
        return self

    def getLinConfigurable(self) -> List["LinConfigurableFrame"]:
        """
        AUTOSAR-compliant getter for linConfigurable.

        Returns:
            The linConfigurable value

        Note:
            Delegates to lin_configurable property (CODING_RULE_V2_00017)
        """
        return self.lin_configurable  # Delegates to property

    def getLinOrdered(self) -> List["LinOrderedConfigurable"]:
        """
        AUTOSAR-compliant getter for linOrdered.

        Returns:
            The linOrdered value

        Note:
            Delegates to lin_ordered property (CODING_RULE_V2_00017)
        """
        return self.lin_ordered  # Delegates to property

    def getSchedule(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for schedule.

        Returns:
            The schedule value

        Note:
            Delegates to schedule property (CODING_RULE_V2_00017)
        """
        return self.schedule  # Delegates to property

    def setSchedule(self, value: "Boolean") -> "LinCommunicationConnector":
        """
        AUTOSAR-compliant setter for schedule with method chaining.

        Args:
            value: The schedule to set

        Returns:
            self for method chaining

        Note:
            Delegates to schedule property setter (gets validation automatically)
        """
        self.schedule = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_initial_nad(self, value: Optional["Integer"]) -> "LinCommunicationConnector":
        """
        Set initialNad and return self for chaining.

        Args:
            value: The initialNad to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_initial_nad("value")
        """
        self.initial_nad = value  # Use property setter (gets validation)
        return self

    def with_schedule(self, value: Optional["Boolean"]) -> "LinCommunicationConnector":
        """
        Set schedule and return self for chaining.

        Args:
            value: The schedule to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_schedule("value")
        """
        self.schedule = value  # Use property setter (gets validation)
        return self

from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class LinConfigurableFrame(ARObject):
    """
    Assignment of messageIds to Frames. This element shall be used for the LIN
    2.0 Assign-Frame command.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Lin::LinTopology

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 99, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to a Frame that is processed by the slave.
        self._frame: Optional["LinFrame"] = None

    @property
    def frame(self) -> Optional["LinFrame"]:
        """Get frame (Pythonic accessor)."""
        return self._frame

    @frame.setter
    def frame(self, value: Optional["LinFrame"]) -> None:
        """
        Set frame with validation.

        Args:
            value: The frame to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._frame = None
            return

        if not isinstance(value, LinFrame):
            raise TypeError(
                f"frame must be LinFrame or None, got {type(value).__name__}"
            )
        self._frame = value
        # MessageId for the referenced frame.
        self._messageId: Optional["PositiveInteger"] = None

    @property
    def message_id(self) -> Optional["PositiveInteger"]:
        """Get messageId (Pythonic accessor)."""
        return self._messageId

    @message_id.setter
    def message_id(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set messageId with validation.

        Args:
            value: The messageId to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._messageId = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"messageId must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._messageId = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getFrame(self) -> "LinFrame":
        """
        AUTOSAR-compliant getter for frame.

        Returns:
            The frame value

        Note:
            Delegates to frame property (CODING_RULE_V2_00017)
        """
        return self.frame  # Delegates to property

    def setFrame(self, value: "LinFrame") -> "LinConfigurableFrame":
        """
        AUTOSAR-compliant setter for frame with method chaining.

        Args:
            value: The frame to set

        Returns:
            self for method chaining

        Note:
            Delegates to frame property setter (gets validation automatically)
        """
        self.frame = value  # Delegates to property setter
        return self

    def getMessageId(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for messageId.

        Returns:
            The messageId value

        Note:
            Delegates to message_id property (CODING_RULE_V2_00017)
        """
        return self.message_id  # Delegates to property

    def setMessageId(self, value: "PositiveInteger") -> "LinConfigurableFrame":
        """
        AUTOSAR-compliant setter for messageId with method chaining.

        Args:
            value: The messageId to set

        Returns:
            self for method chaining

        Note:
            Delegates to message_id property setter (gets validation automatically)
        """
        self.message_id = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_frame(self, value: Optional["LinFrame"]) -> "LinConfigurableFrame":
        """
        Set frame and return self for chaining.

        Args:
            value: The frame to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_frame("value")
        """
        self.frame = value  # Use property setter (gets validation)
        return self

    def with_message_id(self, value: Optional["PositiveInteger"]) -> "LinConfigurableFrame":
        """
        Set messageId and return self for chaining.

        Args:
            value: The messageId to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_message_id("value")
        """
        self.message_id = value  # Use property setter (gets validation)
        return self

from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
        ARObject,
    )


class LinOrderedConfigurableFrame(ARObject):
    """
    With the assignment of the index to a frame a mapping of Pids to Frames is
    possible. This element shall be used for the LIN 2.1 Assign-Frame-PID-Range
    command.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Lin::LinTopology

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 99, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to a Frame that is processed by the slave.
        self._frame: Optional["LinFrame"] = None

    @property
    def frame(self) -> Optional["LinFrame"]:
        """Get frame (Pythonic accessor)."""
        return self._frame

    @frame.setter
    def frame(self, value: Optional["LinFrame"]) -> None:
        """
        Set frame with validation.

        Args:
            value: The frame to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._frame = None
            return

        if not isinstance(value, LinFrame):
            raise TypeError(
                f"frame must be LinFrame or None, got {type(value).__name__}"
            )
        self._frame = value
        # This attribute is used to order the elements and allows an Pids to
        # ConfigurableFrames that are the slave.
        self._index: Optional["Integer"] = None

    @property
    def index(self) -> Optional["Integer"]:
        """Get index (Pythonic accessor)."""
        return self._index

    @index.setter
    def index(self, value: Optional["Integer"]) -> None:
        """
        Set index with validation.

        Args:
            value: The index to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._index = None
            return

        if not isinstance(value, Integer):
            raise TypeError(
                f"index must be Integer or None, got {type(value).__name__}"
            )
        self._index = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getFrame(self) -> "LinFrame":
        """
        AUTOSAR-compliant getter for frame.

        Returns:
            The frame value

        Note:
            Delegates to frame property (CODING_RULE_V2_00017)
        """
        return self.frame  # Delegates to property

    def setFrame(self, value: "LinFrame") -> "LinOrderedConfigurableFrame":
        """
        AUTOSAR-compliant setter for frame with method chaining.

        Args:
            value: The frame to set

        Returns:
            self for method chaining

        Note:
            Delegates to frame property setter (gets validation automatically)
        """
        self.frame = value  # Delegates to property setter
        return self

    def getIndex(self) -> "Integer":
        """
        AUTOSAR-compliant getter for index.

        Returns:
            The index value

        Note:
            Delegates to index property (CODING_RULE_V2_00017)
        """
        return self.index  # Delegates to property

    def setIndex(self, value: "Integer") -> "LinOrderedConfigurableFrame":
        """
        AUTOSAR-compliant setter for index with method chaining.

        Args:
            value: The index to set

        Returns:
            self for method chaining

        Note:
            Delegates to index property setter (gets validation automatically)
        """
        self.index = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_frame(self, value: Optional["LinFrame"]) -> "LinOrderedConfigurableFrame":
        """
        Set frame and return self for chaining.

        Args:
            value: The frame to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_frame("value")
        """
        self.frame = value  # Use property setter (gets validation)
        return self

    def with_index(self, value: Optional["Integer"]) -> "LinOrderedConfigurableFrame":
        """
        Set index and return self for chaining.

        Args:
            value: The index to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_index("value")
        """
        self.index = value  # Use property setter (gets validation)
        return self

from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import (
    PhysicalChannel,
)


class LinPhysicalChannel(PhysicalChannel):
    """
    LIN specific attributes to the physicalChannel

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::Fibex4Lin::LinTopology

    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 99, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute shall be used to set an idle timeout period the enclosing
                # LinPhysicalChannel.
        # 2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._busIdleTimeout: Optional["TimeValue"] = None

    @property
    def bus_idle_timeout(self) -> Optional["TimeValue"]:
        """Get busIdleTimeout (Pythonic accessor)."""
        return self._busIdleTimeout

    @bus_idle_timeout.setter
    def bus_idle_timeout(self, value: Optional["TimeValue"]) -> None:
        """
        Set busIdleTimeout with validation.

        Args:
            value: The busIdleTimeout to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._busIdleTimeout = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"busIdleTimeout must be TimeValue or None, got {type(value).__name__}"
            )
        self._busIdleTimeout = value
        # Schedule tables organize the timings of the frames for the transmitted frames
                # are variable, the shall be variable, too.
        # atpVariation.
        self._scheduleTable: List["LinScheduleTable"] = []

    @property
    def schedule_table(self) -> List["LinScheduleTable"]:
        """Get scheduleTable (Pythonic accessor)."""
        return self._scheduleTable

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBusIdleTimeout(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for busIdleTimeout.

        Returns:
            The busIdleTimeout value

        Note:
            Delegates to bus_idle_timeout property (CODING_RULE_V2_00017)
        """
        return self.bus_idle_timeout  # Delegates to property

    def setBusIdleTimeout(self, value: "TimeValue") -> "LinPhysicalChannel":
        """
        AUTOSAR-compliant setter for busIdleTimeout with method chaining.

        Args:
            value: The busIdleTimeout to set

        Returns:
            self for method chaining

        Note:
            Delegates to bus_idle_timeout property setter (gets validation automatically)
        """
        self.bus_idle_timeout = value  # Delegates to property setter
        return self

    def getScheduleTable(self) -> List["LinScheduleTable"]:
        """
        AUTOSAR-compliant getter for scheduleTable.

        Returns:
            The scheduleTable value

        Note:
            Delegates to schedule_table property (CODING_RULE_V2_00017)
        """
        return self.schedule_table  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_bus_idle_timeout(self, value: Optional["TimeValue"]) -> "LinPhysicalChannel":
        """
        Set busIdleTimeout and return self for chaining.

        Args:
            value: The busIdleTimeout to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_bus_idle_timeout("value")
        """
        self.bus_idle_timeout = value  # Use property setter (gets validation)
        return self

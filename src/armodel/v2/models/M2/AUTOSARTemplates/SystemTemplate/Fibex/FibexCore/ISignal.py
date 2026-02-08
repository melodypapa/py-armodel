from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    DataTransformation,
    DataTypePolicyEnum,
    FibexElement,
    ISignalProps,
    ISignalTypeEnum,
    SwDataDefProps,
    SystemSignal,
    TransformationISignal,
    UnlimitedInteger,
    ValueSpecification,
)


class ISignal(FibexElement):
    """
    Signal of the Interaction Layer. The RTE supports a "signal fan-out" where
    the same System Signal is sent in different SignalIPdus to multiple
    receivers. To support the RTE "signal fan-out" each SignalIPdu contains
    ISignals. If the same System Signal is to be mapped into several SignalIPdus
    there is one ISignal needed for each ISignalToIPduMapping. ISignals describe
    the Interface between the Precompile configured RTE and the potentially
    Postbuild configured Com Stack (see ECUC Parameter Mapping). In case of the
    SystemSignalGroup an ISignal shall be created for each SystemSignal
    contained in the SystemSignalGroup.

    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::ISignal

    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 315, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 992, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 320, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 227, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Optional reference to a DataTransformation which the transformer chain that
                # is used to transform that shall be placed inside this ISignal.
        # atpVariation.
        self._data: Optional["DataTransformation"] = None

    @property
    def data(self) -> Optional["DataTransformation"]:
        """Get data (Pythonic accessor)."""
        return self._data

    @data.setter
    def data(self, value: Optional["DataTransformation"]) -> None:
        """
        Set data with validation.

        Args:
            value: The data to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._data = None
            return

        if not isinstance(value, DataTransformation):
            raise TypeError(
                f"data must be DataTransformation or None, got {type(value).__name__}"
            )
        self._data = value
        # With the aggregation of SwDataDefProps an ISignal it is represented on the
                # network.
        # This a particular policy.
        # Note that this redundancy which is intended and can be support flexible
                # development methodology as well integrity checks.
        # policy "networkRepresentationFromComSpec" is network representation from the
                # ComSpec aggregated by the PortPrototype shall be used.
        # If policy is chosen the requirements specified PortInterface and in the
                # ComSpec are not fulfilled networkRepresentationProps.
        # In case the System use a complete Software Component View) the "legacy"
                # policy can be.
        self._dataTypePolicy: Optional["DataTypePolicyEnum"] = None

    @property
    def data_type_policy(self) -> Optional["DataTypePolicyEnum"]:
        """Get dataTypePolicy (Pythonic accessor)."""
        return self._dataTypePolicy

    @data_type_policy.setter
    def data_type_policy(self, value: Optional["DataTypePolicyEnum"]) -> None:
        """
        Set dataTypePolicy with validation.

        Args:
            value: The dataTypePolicy to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dataTypePolicy = None
            return

        if not isinstance(value, DataTypePolicyEnum):
            raise TypeError(
                f"dataTypePolicy must be DataTypePolicyEnum or None, got {type(value).__name__}"
            )
        self._dataTypePolicy = value
        # Optional definition of a ISignal’s initValue in case the doesn’t use a
                # complete Software (VFB View).
        # This supports the legacy system signals.
        # can be used to configure the Signal’s "Init full DataMapping exist for the
                # SystemSignal this be available from a configured Sender ReceiverComSpec.
        # In this case the SenderComSpec and/or ReceiverComSpec optional value
                # specification.
        # Further from the RTE specification.
        self._initValue: Optional["ValueSpecification"] = None

    @property
    def init_value(self) -> Optional["ValueSpecification"]:
        """Get initValue (Pythonic accessor)."""
        return self._initValue

    @init_value.setter
    def init_value(self, value: Optional["ValueSpecification"]) -> None:
        """
        Set initValue with validation.

        Args:
            value: The initValue to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._initValue = None
            return

        if not isinstance(value, ValueSpecification):
            raise TypeError(
                f"initValue must be ValueSpecification or None, got {type(value).__name__}"
            )
        self._initValue = value
        # Additional optional ISignal properties that may be stored files.
        self._iSignalProps: Optional["ISignalProps"] = None

    @property
    def i_signal_props(self) -> Optional["ISignalProps"]:
        """Get iSignalProps (Pythonic accessor)."""
        return self._iSignalProps

    @i_signal_props.setter
    def i_signal_props(self, value: Optional["ISignalProps"]) -> None:
        """
        Set iSignalProps with validation.

        Args:
            value: The iSignalProps to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._iSignalProps = None
            return

        if not isinstance(value, ISignalProps):
            raise TypeError(
                f"iSignalProps must be ISignalProps or None, got {type(value).__name__}"
            )
        self._iSignalProps = value
        # This attribute defines whether this iSignal is an array that a UINT8_N /
                # UINT8_DYN ComSignalType in the or a primitive type.
        # 719 Document ID 673: AUTOSAR_CP_TPS_DiagnosticExtractTemplate Template
                # R23-11.
        self._iSignalType: Optional["ISignalTypeEnum"] = None

    @property
    def i_signal_type(self) -> Optional["ISignalTypeEnum"]:
        """Get iSignalType (Pythonic accessor)."""
        return self._iSignalType

    @i_signal_type.setter
    def i_signal_type(self, value: Optional["ISignalTypeEnum"]) -> None:
        """
        Set iSignalType with validation.

        Args:
            value: The iSignalType to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._iSignalType = None
            return

        if not isinstance(value, ISignalTypeEnum):
            raise TypeError(
                f"iSignalType must be ISignalTypeEnum or None, got {type(value).__name__}"
            )
        self._iSignalType = value
        # Size of the signal in bits.
        # The size needs to be derived mapped VariableDataPrototype according to the
                # primitive DataTypes to BaseTypes as used in Indicates maximum size for
                # dynamic length length of zero bits is allowed.
        self._length: Optional["UnlimitedInteger"] = None

    @property
    def length(self) -> Optional["UnlimitedInteger"]:
        """Get length (Pythonic accessor)."""
        return self._length

    @length.setter
    def length(self, value: Optional["UnlimitedInteger"]) -> None:
        """
        Set length with validation.

        Args:
            value: The length to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._length = None
            return

        if not isinstance(value, UnlimitedInteger):
            raise TypeError(
                f"length must be UnlimitedInteger or None, got {type(value).__name__}"
            )
        self._length = value
        # Specification of the actual network representation.
        # The of SwDataDefProps for this purpose is restricted to attributes
                # compuMethod and baseType.
        # The optional "memAllignment" and "byteOrder" be used.
        # "dataTypePolicy" in the SystemTemplate whether this network representation
                # shall and the information shall be taken over from representation of the
                # ComSpec.
        # is chosen by the system integrator the can violate against the in the
                # PortInterface and in the of the ComSpec.
        # that the System Description doesn’t use a Component Description (VFB View) is
                # used to configure "ComSignalDataInvalid the Data Semantics.
        self._network: Optional["SwDataDefProps"] = None

    @property
    def network(self) -> Optional["SwDataDefProps"]:
        """Get network (Pythonic accessor)."""
        return self._network

    @network.setter
    def network(self, value: Optional["SwDataDefProps"]) -> None:
        """
        Set network with validation.

        Args:
            value: The network to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._network = None
            return

        if not isinstance(value, SwDataDefProps):
            raise TypeError(
                f"network must be SwDataDefProps or None, got {type(value).__name__}"
            )
        self._network = value
        # Reference to the System Signal that is supposed to be the ISignal.
        self._systemSignal: Optional["SystemSignal"] = None

    @property
    def system_signal(self) -> Optional["SystemSignal"]:
        """Get systemSignal (Pythonic accessor)."""
        return self._systemSignal

    @system_signal.setter
    def system_signal(self, value: Optional["SystemSignal"]) -> None:
        """
        Set systemSignal with validation.

        Args:
            value: The systemSignal to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._systemSignal = None
            return

        if not isinstance(value, SystemSignal):
            raise TypeError(
                f"systemSignal must be SystemSignal or None, got {type(value).__name__}"
            )
        self._systemSignal = value
        # Defines and enables the ComTimeoutSubstituition for this.
        self._timeout: Optional["ValueSpecification"] = None

    @property
    def timeout(self) -> Optional["ValueSpecification"]:
        """Get timeout (Pythonic accessor)."""
        return self._timeout

    @timeout.setter
    def timeout(self, value: Optional["ValueSpecification"]) -> None:
        """
        Set timeout with validation.

        Args:
            value: The timeout to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timeout = None
            return

        if not isinstance(value, ValueSpecification):
            raise TypeError(
                f"timeout must be ValueSpecification or None, got {type(value).__name__}"
            )
        self._timeout = value
        # A transformer chain consists of an ordered list of transformers.
        # The ISignal specific configuration each transformer are defined in the The
                # transformer that are common for all ISignals in the TransformationTechnology
                # class.
        self._transformation: List["TransformationISignal"] = []

    @property
    def transformation(self) -> List["TransformationISignal"]:
        """Get transformation (Pythonic accessor)."""
        return self._transformation

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getData(self) -> "DataTransformation":
        """
        AUTOSAR-compliant getter for data.

        Returns:
            The data value

        Note:
            Delegates to data property (CODING_RULE_V2_00017)
        """
        return self.data  # Delegates to property

    def setData(self, value: "DataTransformation") -> "ISignal":
        """
        AUTOSAR-compliant setter for data with method chaining.

        Args:
            value: The data to set

        Returns:
            self for method chaining

        Note:
            Delegates to data property setter (gets validation automatically)
        """
        self.data = value  # Delegates to property setter
        return self

    def getDataTypePolicy(self) -> "DataTypePolicyEnum":
        """
        AUTOSAR-compliant getter for dataTypePolicy.

        Returns:
            The dataTypePolicy value

        Note:
            Delegates to data_type_policy property (CODING_RULE_V2_00017)
        """
        return self.data_type_policy  # Delegates to property

    def setDataTypePolicy(self, value: "DataTypePolicyEnum") -> "ISignal":
        """
        AUTOSAR-compliant setter for dataTypePolicy with method chaining.

        Args:
            value: The dataTypePolicy to set

        Returns:
            self for method chaining

        Note:
            Delegates to data_type_policy property setter (gets validation automatically)
        """
        self.data_type_policy = value  # Delegates to property setter
        return self

    def getInitValue(self) -> "ValueSpecification":
        """
        AUTOSAR-compliant getter for initValue.

        Returns:
            The initValue value

        Note:
            Delegates to init_value property (CODING_RULE_V2_00017)
        """
        return self.init_value  # Delegates to property

    def setInitValue(self, value: "ValueSpecification") -> "ISignal":
        """
        AUTOSAR-compliant setter for initValue with method chaining.

        Args:
            value: The initValue to set

        Returns:
            self for method chaining

        Note:
            Delegates to init_value property setter (gets validation automatically)
        """
        self.init_value = value  # Delegates to property setter
        return self

    def getISignalProps(self) -> "ISignalProps":
        """
        AUTOSAR-compliant getter for iSignalProps.

        Returns:
            The iSignalProps value

        Note:
            Delegates to i_signal_props property (CODING_RULE_V2_00017)
        """
        return self.i_signal_props  # Delegates to property

    def setISignalProps(self, value: "ISignalProps") -> "ISignal":
        """
        AUTOSAR-compliant setter for iSignalProps with method chaining.

        Args:
            value: The iSignalProps to set

        Returns:
            self for method chaining

        Note:
            Delegates to i_signal_props property setter (gets validation automatically)
        """
        self.i_signal_props = value  # Delegates to property setter
        return self

    def getISignalType(self) -> "ISignalTypeEnum":
        """
        AUTOSAR-compliant getter for iSignalType.

        Returns:
            The iSignalType value

        Note:
            Delegates to i_signal_type property (CODING_RULE_V2_00017)
        """
        return self.i_signal_type  # Delegates to property

    def setISignalType(self, value: "ISignalTypeEnum") -> "ISignal":
        """
        AUTOSAR-compliant setter for iSignalType with method chaining.

        Args:
            value: The iSignalType to set

        Returns:
            self for method chaining

        Note:
            Delegates to i_signal_type property setter (gets validation automatically)
        """
        self.i_signal_type = value  # Delegates to property setter
        return self

    def getLength(self) -> "UnlimitedInteger":
        """
        AUTOSAR-compliant getter for length.

        Returns:
            The length value

        Note:
            Delegates to length property (CODING_RULE_V2_00017)
        """
        return self.length  # Delegates to property

    def setLength(self, value: "UnlimitedInteger") -> "ISignal":
        """
        AUTOSAR-compliant setter for length with method chaining.

        Args:
            value: The length to set

        Returns:
            self for method chaining

        Note:
            Delegates to length property setter (gets validation automatically)
        """
        self.length = value  # Delegates to property setter
        return self

    def getNetwork(self) -> "SwDataDefProps":
        """
        AUTOSAR-compliant getter for network.

        Returns:
            The network value

        Note:
            Delegates to network property (CODING_RULE_V2_00017)
        """
        return self.network  # Delegates to property

    def setNetwork(self, value: "SwDataDefProps") -> "ISignal":
        """
        AUTOSAR-compliant setter for network with method chaining.

        Args:
            value: The network to set

        Returns:
            self for method chaining

        Note:
            Delegates to network property setter (gets validation automatically)
        """
        self.network = value  # Delegates to property setter
        return self

    def getSystemSignal(self) -> "SystemSignal":
        """
        AUTOSAR-compliant getter for systemSignal.

        Returns:
            The systemSignal value

        Note:
            Delegates to system_signal property (CODING_RULE_V2_00017)
        """
        return self.system_signal  # Delegates to property

    def setSystemSignal(self, value: "SystemSignal") -> "ISignal":
        """
        AUTOSAR-compliant setter for systemSignal with method chaining.

        Args:
            value: The systemSignal to set

        Returns:
            self for method chaining

        Note:
            Delegates to system_signal property setter (gets validation automatically)
        """
        self.system_signal = value  # Delegates to property setter
        return self

    def getTimeout(self) -> "ValueSpecification":
        """
        AUTOSAR-compliant getter for timeout.

        Returns:
            The timeout value

        Note:
            Delegates to timeout property (CODING_RULE_V2_00017)
        """
        return self.timeout  # Delegates to property

    def setTimeout(self, value: "ValueSpecification") -> "ISignal":
        """
        AUTOSAR-compliant setter for timeout with method chaining.

        Args:
            value: The timeout to set

        Returns:
            self for method chaining

        Note:
            Delegates to timeout property setter (gets validation automatically)
        """
        self.timeout = value  # Delegates to property setter
        return self

    def getTransformation(self) -> List["TransformationISignal"]:
        """
        AUTOSAR-compliant getter for transformation.

        Returns:
            The transformation value

        Note:
            Delegates to transformation property (CODING_RULE_V2_00017)
        """
        return self.transformation  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_data(self, value: Optional["DataTransformation"]) -> "ISignal":
        """
        Set data and return self for chaining.

        Args:
            value: The data to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_data("value")
        """
        self.data = value  # Use property setter (gets validation)
        return self

    def with_data_type_policy(self, value: Optional["DataTypePolicyEnum"]) -> "ISignal":
        """
        Set dataTypePolicy and return self for chaining.

        Args:
            value: The dataTypePolicy to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_data_type_policy("value")
        """
        self.data_type_policy = value  # Use property setter (gets validation)
        return self

    def with_init_value(self, value: Optional["ValueSpecification"]) -> "ISignal":
        """
        Set initValue and return self for chaining.

        Args:
            value: The initValue to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_init_value("value")
        """
        self.init_value = value  # Use property setter (gets validation)
        return self

    def with_i_signal_props(self, value: Optional["ISignalProps"]) -> "ISignal":
        """
        Set iSignalProps and return self for chaining.

        Args:
            value: The iSignalProps to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_i_signal_props("value")
        """
        self.i_signal_props = value  # Use property setter (gets validation)
        return self

    def with_i_signal_type(self, value: Optional["ISignalTypeEnum"]) -> "ISignal":
        """
        Set iSignalType and return self for chaining.

        Args:
            value: The iSignalType to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_i_signal_type("value")
        """
        self.i_signal_type = value  # Use property setter (gets validation)
        return self

    def with_length(self, value: Optional["UnlimitedInteger"]) -> "ISignal":
        """
        Set length and return self for chaining.

        Args:
            value: The length to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_length("value")
        """
        self.length = value  # Use property setter (gets validation)
        return self

    def with_network(self, value: Optional["SwDataDefProps"]) -> "ISignal":
        """
        Set network and return self for chaining.

        Args:
            value: The network to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_network("value")
        """
        self.network = value  # Use property setter (gets validation)
        return self

    def with_system_signal(self, value: Optional["SystemSignal"]) -> "ISignal":
        """
        Set systemSignal and return self for chaining.

        Args:
            value: The systemSignal to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_system_signal("value")
        """
        self.system_signal = value  # Use property setter (gets validation)
        return self

    def with_timeout(self, value: Optional["ValueSpecification"]) -> "ISignal":
        """
        Set timeout and return self for chaining.

        Args:
            value: The timeout to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_timeout("value")
        """
        self.timeout = value  # Use property setter (gets validation)
        return self

"""
AUTOSAR Package - CoreCommunication

Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication
"""


from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
    PositiveInteger,
    RefType,
    String,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Describable,
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.__init__ import (
    IPdu,
    MultiplexedPart,
    Pdu,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import (
    CommConnectorPort,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.__init__ import (
    FibexElement,
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
        self._iSignalProps: Optional[ISignalProps] = None

    @property
    def i_signal_props(self) -> Optional[ISignalProps]:
        """Get iSignalProps (Pythonic accessor)."""
        return self._iSignalProps

    @i_signal_props.setter
    def i_signal_props(self, value: Optional[ISignalProps]) -> None:
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
        self._iSignalType: Optional[ISignalTypeEnum] = None

    @property
    def i_signal_type(self) -> Optional[ISignalTypeEnum]:
        """Get iSignalType (Pythonic accessor)."""
        return self._iSignalType

    @i_signal_type.setter
    def i_signal_type(self, value: Optional[ISignalTypeEnum]) -> None:
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
        self._systemSignal: Optional[SystemSignal] = None

    @property
    def system_signal(self) -> Optional[SystemSignal]:
        """Get systemSignal (Pythonic accessor)."""
        return self._systemSignal

    @system_signal.setter
    def system_signal(self, value: Optional[SystemSignal]) -> None:
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

    def with_transformation(self, value):
        """
        Set transformation and return self for chaining.

        Args:
            value: The transformation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_transformation("value")
        """
        self.transformation = value  # Use property setter (gets validation)
        return self

    def with_contained(self, value):
        """
        Set contained and return self for chaining.

        Args:
            value: The contained to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_contained("value")
        """
        self.contained = value  # Use property setter (gets validation)
        return self

    def with_i_signal_i_pdu(self, value):
        """
        Set i_signal_i_pdu and return self for chaining.

        Args:
            value: The i_signal_i_pdu to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_i_signal_i_pdu("value")
        """
        self.i_signal_i_pdu = value  # Use property setter (gets validation)
        return self

    def with_nm_pdu(self, value):
        """
        Set nm_pdu and return self for chaining.

        Args:
            value: The nm_pdu to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_nm_pdu("value")
        """
        self.nm_pdu = value  # Use property setter (gets validation)
        return self

    def with_pdu_to_frame(self, value):
        """
        Set pdu_to_frame and return self for chaining.

        Args:
            value: The pdu_to_frame to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_pdu_to_frame("value")
        """
        self.pdu_to_frame = value  # Use property setter (gets validation)
        return self

    def with_frame_port(self, value):
        """
        Set frame_port and return self for chaining.

        Args:
            value: The frame_port to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_frame_port("value")
        """
        self.frame_port = value  # Use property setter (gets validation)
        return self

    def with_pdu_triggering(self, value):
        """
        Set pdu_triggering and return self for chaining.

        Args:
            value: The pdu_triggering to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_pdu_triggering("value")
        """
        self.pdu_triggering = value  # Use property setter (gets validation)
        return self

    def with_i_pdu_port(self, value):
        """
        Set i_pdu_port and return self for chaining.

        Args:
            value: The i_pdu_port to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_i_pdu_port("value")
        """
        self.i_pdu_port = value  # Use property setter (gets validation)
        return self

    def with_trigger_i_pdu_send(self, value):
        """
        Set trigger_i_pdu_send and return self for chaining.

        Args:
            value: The trigger_i_pdu_send to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_trigger_i_pdu_send("value")
        """
        self.trigger_i_pdu_send = value  # Use property setter (gets validation)
        return self

    def with_transformation(self, value):
        """
        Set transformation and return self for chaining.

        Args:
            value: The transformation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_transformation("value")
        """
        self.transformation = value  # Use property setter (gets validation)
        return self

    def with_i_signal_port(self, value):
        """
        Set i_signal_port and return self for chaining.

        Args:
            value: The i_signal_port to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_i_signal_port("value")
        """
        self.i_signal_port = value  # Use property setter (gets validation)
        return self

    def with_i_signal_to_i_pdu(self, value):
        """
        Set i_signal_to_i_pdu and return self for chaining.

        Args:
            value: The i_signal_to_i_pdu to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_i_signal_to_i_pdu("value")
        """
        self.i_signal_to_i_pdu = value  # Use property setter (gets validation)
        return self

    def with_i_signal_to_pdu(self, value):
        """
        Set i_signal_to_pdu and return self for chaining.

        Args:
            value: The i_signal_to_pdu to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_i_signal_to_pdu("value")
        """
        self.i_signal_to_pdu = value  # Use property setter (gets validation)
        return self

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

    def setData(self, value: "DataTransformation") -> ISignal:
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

    def setDataTypePolicy(self, value: "DataTypePolicyEnum") -> ISignal:
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

    def setInitValue(self, value: "ValueSpecification") -> ISignal:
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

    def getISignalProps(self) -> ISignalProps:
        """
        AUTOSAR-compliant getter for iSignalProps.
        
        Returns:
            The iSignalProps value
        
        Note:
            Delegates to i_signal_props property (CODING_RULE_V2_00017)
        """
        return self.i_signal_props  # Delegates to property

    def setISignalProps(self, value: ISignalProps) -> ISignal:
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

    def getISignalType(self) -> ISignalTypeEnum:
        """
        AUTOSAR-compliant getter for iSignalType.
        
        Returns:
            The iSignalType value
        
        Note:
            Delegates to i_signal_type property (CODING_RULE_V2_00017)
        """
        return self.i_signal_type  # Delegates to property

    def setISignalType(self, value: ISignalTypeEnum) -> ISignal:
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

    def setLength(self, value: "UnlimitedInteger") -> ISignal:
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

    def setNetwork(self, value: "SwDataDefProps") -> ISignal:
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

    def getSystemSignal(self) -> SystemSignal:
        """
        AUTOSAR-compliant getter for systemSignal.
        
        Returns:
            The systemSignal value
        
        Note:
            Delegates to system_signal property (CODING_RULE_V2_00017)
        """
        return self.system_signal  # Delegates to property

    def setSystemSignal(self, value: SystemSignal) -> ISignal:
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

    def setTimeout(self, value: "ValueSpecification") -> ISignal:
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

    def with_data(self, value: Optional["DataTransformation"]) -> ISignal:
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

    def with_data_type_policy(self, value: Optional["DataTypePolicyEnum"]) -> ISignal:
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

    def with_init_value(self, value: Optional["ValueSpecification"]) -> ISignal:
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

    def with_i_signal_props(self, value: Optional[ISignalProps]) -> ISignal:
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

    def with_i_signal_type(self, value: Optional[ISignalTypeEnum]) -> ISignal:
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

    def with_length(self, value: Optional["UnlimitedInteger"]) -> ISignal:
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

    def with_network(self, value: Optional["SwDataDefProps"]) -> ISignal:
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

    def with_system_signal(self, value: Optional[SystemSignal]) -> ISignal:
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

    def with_timeout(self, value: Optional["ValueSpecification"]) -> ISignal:
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



class ISignalIPduGroup(FibexElement):
    """
    The AUTOSAR COM Layer is able to start and to stop sending and receiving
    configurable groups of I-Pdus during runtime. An ISignalIPduGroup contains
    either ISignalIPdus or ISignalIPduGroups.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::ISignalIPduGroup
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 316, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 350, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute defines the use-case for this ISignalIPdu (e.
        # g.
        # diagnostic, debugging etc.
        # ).
        # For example, in a all IPdus - which are not involved in are disabled.
        # The use cases are not limited to enumeration and can be specified as a
                # string.
        self._communication: Optional["String"] = None

    @property
    def communication(self) -> Optional["String"]:
        """Get communication (Pythonic accessor)."""
        return self._communication

    @communication.setter
    def communication(self, value: Optional["String"]) -> None:
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

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"communication must be String or str or None, got {type(value).__name__}"
            )
        self._communication = value
        # An I-Pdu group can be included in other I-Pdu groups.
        # I-Pdu groups shall not be referenced by the.
        self._contained: List["RefType"] = []

    @property
    def contained(self) -> List["RefType"]:
        """Get contained (Pythonic accessor)."""
        return self._contained
        # Reference to a set of Signal I-Pdus, which are contained ISignal I-Pdu Group.
        # content of a ISignal I-Pdu group can modes).
        # atpVariation.
        self._iSignalIPdu: List[ISignalIPdu] = []

    @property
    def i_signal_i_pdu(self) -> List[ISignalIPdu]:
        """Get iSignalIPdu (Pythonic accessor)."""
        return self._iSignalIPdu
        # Reference to a set of NmPdus with NmUserData, which in the ISignalIPduGroup.
        # atpVariation.
        self._nmPdu: List[NmPdu] = []

    @property
    def nm_pdu(self) -> List[NmPdu]:
        """Get nmPdu (Pythonic accessor)."""
        return self._nmPdu

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCommunication(self) -> "String":
        """
        AUTOSAR-compliant getter for communication.
        
        Returns:
            The communication value
        
        Note:
            Delegates to communication property (CODING_RULE_V2_00017)
        """
        return self.communication  # Delegates to property

    def setCommunication(self, value: "String") -> ISignalIPduGroup:
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

    def getContained(self) -> List["RefType"]:
        """
        AUTOSAR-compliant getter for contained.
        
        Returns:
            The contained value
        
        Note:
            Delegates to contained property (CODING_RULE_V2_00017)
        """
        return self.contained  # Delegates to property

    def getISignalIPdu(self) -> List[ISignalIPdu]:
        """
        AUTOSAR-compliant getter for iSignalIPdu.
        
        Returns:
            The iSignalIPdu value
        
        Note:
            Delegates to i_signal_i_pdu property (CODING_RULE_V2_00017)
        """
        return self.i_signal_i_pdu  # Delegates to property

    def getNmPdu(self) -> List[NmPdu]:
        """
        AUTOSAR-compliant getter for nmPdu.
        
        Returns:
            The nmPdu value
        
        Note:
            Delegates to nm_pdu property (CODING_RULE_V2_00017)
        """
        return self.nm_pdu  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_communication(self, value: Optional["String"]) -> ISignalIPduGroup:
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



class SystemSignal(ARElement):
    """
    The system signal represents the communication system’s view of data
    exchanged between SW components which reside on different ECUs. The system
    signals allow to represent this communication in a flattened structure, with
    exactly one system signal defined for each data element prototype sent and
    received by connected SW component instances.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::SystemSignal
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 332, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 1009, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 218, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The length of dynamic length signals is variable in a maximum length of such
        # a signal is the configuration (attribute length in ISignal.
        self._dynamicLength: Optional["Boolean"] = None

    @property
    def dynamic_length(self) -> Optional["Boolean"]:
        """Get dynamicLength (Pythonic accessor)."""
        return self._dynamicLength

    @dynamic_length.setter
    def dynamic_length(self, value: Optional["Boolean"]) -> None:
        """
        Set dynamicLength with validation.
        
        Args:
            value: The dynamicLength to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dynamicLength = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"dynamicLength must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._dynamicLength = value
        # Specification of the physical representation.
        self._physicalProps: Optional["SwDataDefProps"] = None

    @property
    def physical_props(self) -> Optional["SwDataDefProps"]:
        """Get physicalProps (Pythonic accessor)."""
        return self._physicalProps

    @physical_props.setter
    def physical_props(self, value: Optional["SwDataDefProps"]) -> None:
        """
        Set physicalProps with validation.
        
        Args:
            value: The physicalProps to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._physicalProps = None
            return

        if not isinstance(value, SwDataDefProps):
            raise TypeError(
                f"physicalProps must be SwDataDefProps or None, got {type(value).__name__}"
            )
        self._physicalProps = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDynamicLength(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for dynamicLength.
        
        Returns:
            The dynamicLength value
        
        Note:
            Delegates to dynamic_length property (CODING_RULE_V2_00017)
        """
        return self.dynamic_length  # Delegates to property

    def setDynamicLength(self, value: "Boolean") -> SystemSignal:
        """
        AUTOSAR-compliant setter for dynamicLength with method chaining.
        
        Args:
            value: The dynamicLength to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to dynamic_length property setter (gets validation automatically)
        """
        self.dynamic_length = value  # Delegates to property setter
        return self

    def getPhysicalProps(self) -> "SwDataDefProps":
        """
        AUTOSAR-compliant getter for physicalProps.
        
        Returns:
            The physicalProps value
        
        Note:
            Delegates to physical_props property (CODING_RULE_V2_00017)
        """
        return self.physical_props  # Delegates to property

    def setPhysicalProps(self, value: "SwDataDefProps") -> SystemSignal:
        """
        AUTOSAR-compliant setter for physicalProps with method chaining.
        
        Args:
            value: The physicalProps to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to physical_props property setter (gets validation automatically)
        """
        self.physical_props = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_dynamic_length(self, value: Optional["Boolean"]) -> SystemSignal:
        """
        Set dynamicLength and return self for chaining.
        
        Args:
            value: The dynamicLength to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_dynamic_length("value")
        """
        self.dynamic_length = value  # Use property setter (gets validation)
        return self

    def with_physical_props(self, value: Optional["SwDataDefProps"]) -> SystemSignal:
        """
        Set physicalProps and return self for chaining.
        
        Args:
            value: The physicalProps to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_physical_props("value")
        """
        self.physical_props = value  # Use property setter (gets validation)
        return self



class Frame(FibexElement, ABC):
    """
    Data frame which is sent over a communication medium. This element describes
    the pure Layout of a frame sent on a channel.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::Frame
    
    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 295, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 418, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 224, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is Frame:
            raise TypeError("Frame is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The used length (in bytes) of the referencing frame.
        # be confused with a static byte length reserved frame by some platforms (e.
        # g.
        # FlexRay).
        # of zero bytes is allowed.
        # also TPS_SYST_02255.
        self._frameLength: Optional["Integer"] = None

    @property
    def frame_length(self) -> Optional["Integer"]:
        """Get frameLength (Pythonic accessor)."""
        return self._frameLength

    @frame_length.setter
    def frame_length(self, value: Optional["Integer"]) -> None:
        """
        Set frameLength with validation.
        
        Args:
            value: The frameLength to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._frameLength = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"frameLength must be Integer or int or None, got {type(value).__name__}"
            )
        self._frameLength = value
        # A frames layout as a sequence of Pdus.
        # The content of a frame can be variable.
        # atpVariation.
        self._pduToFrame: List["RefType"] = []

    @property
    def pdu_to_frame(self) -> List["RefType"]:
        """Get pduToFrame (Pythonic accessor)."""
        return self._pduToFrame

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getFrameLength(self) -> "Integer":
        """
        AUTOSAR-compliant getter for frameLength.
        
        Returns:
            The frameLength value
        
        Note:
            Delegates to frame_length property (CODING_RULE_V2_00017)
        """
        return self.frame_length  # Delegates to property

    def setFrameLength(self, value: "Integer") -> Frame:
        """
        AUTOSAR-compliant setter for frameLength with method chaining.
        
        Args:
            value: The frameLength to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to frame_length property setter (gets validation automatically)
        """
        self.frame_length = value  # Delegates to property setter
        return self

    def getPduToFrame(self) -> List["RefType"]:
        """
        AUTOSAR-compliant getter for pduToFrame.
        
        Returns:
            The pduToFrame value
        
        Note:
            Delegates to pdu_to_frame property (CODING_RULE_V2_00017)
        """
        return self.pdu_to_frame  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_frame_length(self, value: Optional["Integer"]) -> Frame:
        """
        Set frameLength and return self for chaining.
        
        Args:
            value: The frameLength to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_frame_length("value")
        """
        self.frame_length = value  # Use property setter (gets validation)
        return self



class FrameTriggering(Identifiable, ABC):
    """
    The FrameTriggering describes the instance of a frame sent on a channel and
    defines the manner of triggering (timing information) and identification of
    a frame on the channel, on which it is sent. For the same frame, if
    FrameTriggerings exist on more than one channel of the same cluster the
    fan-out/ in is handled by the Bus interface.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::FrameTriggering
    
    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 295, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 418, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 224, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is FrameTriggering:
            raise TypeError("FrameTriggering is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # One frame can be triggered several times, e.
        # g.
        # on If a frame has no frame triggering, it sent at all.
        # A frame triggering has assigned frame, which it triggers.
        self._frame: Optional[Frame] = None

    @property
    def frame(self) -> Optional[Frame]:
        """Get frame (Pythonic accessor)."""
        return self._frame

    @frame.setter
    def frame(self, value: Optional[Frame]) -> None:
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

        if not isinstance(value, Frame):
            raise TypeError(
                f"frame must be Frame or None, got {type(value).__name__}"
            )
        self._frame = value
        # References to the FramePort on every ECU of the system and/or receives the
                # frame.
        # both the sender and the receiver side included when the system is completely
                # defined.
        self._framePort: List[FramePort] = []

    @property
    def frame_port(self) -> List[FramePort]:
        """Get framePort (Pythonic accessor)."""
        return self._framePort
        # This reference provides the relationship to the Pdu are implemented by the
                # FrameTriggering.
        # is optional since no PduTriggering can be NmPdus and XCP Pdus.
        # atpVariation.
        self._pduTriggering: List["RefType"] = []

    @property
    def pdu_triggering(self) -> List["RefType"]:
        """Get pduTriggering (Pythonic accessor)."""
        return self._pduTriggering

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getFrame(self) -> Frame:
        """
        AUTOSAR-compliant getter for frame.
        
        Returns:
            The frame value
        
        Note:
            Delegates to frame property (CODING_RULE_V2_00017)
        """
        return self.frame  # Delegates to property

    def setFrame(self, value: Frame) -> FrameTriggering:
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

    def getFramePort(self) -> List[FramePort]:
        """
        AUTOSAR-compliant getter for framePort.
        
        Returns:
            The framePort value
        
        Note:
            Delegates to frame_port property (CODING_RULE_V2_00017)
        """
        return self.frame_port  # Delegates to property

    def getPduTriggering(self) -> List["RefType"]:
        """
        AUTOSAR-compliant getter for pduTriggering.
        
        Returns:
            The pduTriggering value
        
        Note:
            Delegates to pdu_triggering property (CODING_RULE_V2_00017)
        """
        return self.pdu_triggering  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_frame(self, value: Optional[Frame]) -> FrameTriggering:
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



class Pdu(FibexElement, ABC):
    """
    Collection of all Pdus that can be routed through a bus interface.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::Pdu
    
    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 303, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 340, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is Pdu:
            raise TypeError("Pdu is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute defines whether the Pdu has dynamic (true) or not (false).
        # Please note that the usage of is restricted by [constr_3448].
        self._hasDynamic: Optional["Boolean"] = None

    @property
    def has_dynamic(self) -> Optional["Boolean"]:
        """Get hasDynamic (Pythonic accessor)."""
        return self._hasDynamic

    @has_dynamic.setter
    def has_dynamic(self, value: Optional["Boolean"]) -> None:
        """
        Set hasDynamic with validation.
        
        Args:
            value: The hasDynamic to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._hasDynamic = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"hasDynamic must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._hasDynamic = value
        # Pdu length in bytes.
        # In case of dynamic length IPdus dynamical length signal), this value maximum
                # data length.
        # It should be noted former AUTOSAR releases (Rel 2.
        # 1, Rel 3.
        # 0, Rel 4.
        # 0 Rev.
        # 1) this parameter was defined in bits.
        # length of zero bytes is allowed.
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

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getHasDynamic(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for hasDynamic.
        
        Returns:
            The hasDynamic value
        
        Note:
            Delegates to has_dynamic property (CODING_RULE_V2_00017)
        """
        return self.has_dynamic  # Delegates to property

    def setHasDynamic(self, value: "Boolean") -> Pdu:
        """
        AUTOSAR-compliant setter for hasDynamic with method chaining.
        
        Args:
            value: The hasDynamic to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to has_dynamic property setter (gets validation automatically)
        """
        self.has_dynamic = value  # Delegates to property setter
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

    def setLength(self, value: "UnlimitedInteger") -> Pdu:
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

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_has_dynamic(self, value: Optional["Boolean"]) -> Pdu:
        """
        Set hasDynamic and return self for chaining.
        
        Args:
            value: The hasDynamic to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_has_dynamic("value")
        """
        self.has_dynamic = value  # Use property setter (gets validation)
        return self

    def with_length(self, value: Optional["UnlimitedInteger"]) -> Pdu:
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



class PduTriggering(Identifiable):
    """
    The PduTriggering describes on which channel the IPdu is transmitted. The
    Pdu routing by the PduR is only allowed for subclasses of IPdu. Depending on
    its relation to entities such channels and clusters it can be unambiguously
    deduced whether a fan-out is handled by the Pdu router or the Bus Interface.
    If the fan-out is specified between different clusters it shall be handled
    by the Pdu Router. If the fan-out is specified between different channels of
    the same cluster it shall be handled by the Bus Interface.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::PduTriggering
    
    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 303, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 348, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 234, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to the Pdu for which the PduTriggering is I-Pdu can be triggered on
                # different channels The Pdu routing by the PduR is only subclasses of IPdu.
        # the reference to the Pdu element the PduTriggering element is also used the
                # sending and receiving connections to Ecu.
        self._iPdu: Optional[Pdu] = None

    @property
    def i_pdu(self) -> Optional[Pdu]:
        """Get iPdu (Pythonic accessor)."""
        return self._iPdu

    @i_pdu.setter
    def i_pdu(self, value: Optional[Pdu]) -> None:
        """
        Set iPdu with validation.
        
        Args:
            value: The iPdu to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._iPdu = None
            return

        if not isinstance(value, Pdu):
            raise TypeError(
                f"iPdu must be Pdu or None, got {type(value).__name__}"
            )
        self._iPdu = value
        # References to the IPduPort on every ECU of the system and/or receives the
                # I-PDU.
        # both the sender and the receiver side included when the system is completely
                # defined.
        self._iPduPort: List[IPduPort] = []

    @property
    def i_pdu_port(self) -> List[IPduPort]:
        """Get iPduPort (Pythonic accessor)."""
        return self._iPduPort
        # This reference provides the relationship to the ISignal that are implemented
                # by the PduTriggering.
        # is optional since no ISignalTriggering can for DCM and Multiplexed Pdus.
        # atpVariation 318 Document ID 87: AUTOSAR_CP_TPS_ECUConfiguration ECU
                # Configuration R23-11.
        self._iSignal: List["RefType"] = []

    @property
    def i_signal(self) -> List["RefType"]:
        """Get iSignal (Pythonic accessor)."""
        return self._iSignal
        # This reference identifies the crypto profile applicable to the usage (send,
        # receive) of the also referenced Secured reference is only applicable if the
        # references a SecuredIPdu in the role i.
        self._secOcCrypto: Optional["SecOcCryptoService"] = None

    @property
    def sec_oc_crypto(self) -> Optional["SecOcCryptoService"]:
        """Get secOcCrypto (Pythonic accessor)."""
        return self._secOcCrypto

    @sec_oc_crypto.setter
    def sec_oc_crypto(self, value: Optional["SecOcCryptoService"]) -> None:
        """
        Set secOcCrypto with validation.
        
        Args:
            value: The secOcCrypto to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._secOcCrypto = None
            return

        if not isinstance(value, SecOcCryptoService):
            raise TypeError(
                f"secOcCrypto must be SecOcCryptoService or None, got {type(value).__name__}"
            )
        self._secOcCrypto = value
        # Defines the trigger for the Com_TriggerIPDUSend API call.
        # Only if all defined TriggerIPduSendConditions true (AND associated) the
                # Com_Trigger shall be called.
        self._triggerIPduSend: List["RefType"] = []

    @property
    def trigger_i_pdu_send(self) -> List["RefType"]:
        """Get triggerIPduSend (Pythonic accessor)."""
        return self._triggerIPduSend

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getIPdu(self) -> Pdu:
        """
        AUTOSAR-compliant getter for iPdu.
        
        Returns:
            The iPdu value
        
        Note:
            Delegates to i_pdu property (CODING_RULE_V2_00017)
        """
        return self.i_pdu  # Delegates to property

    def setIPdu(self, value: Pdu) -> PduTriggering:
        """
        AUTOSAR-compliant setter for iPdu with method chaining.
        
        Args:
            value: The iPdu to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to i_pdu property setter (gets validation automatically)
        """
        self.i_pdu = value  # Delegates to property setter
        return self

    def getIPduPort(self) -> List[IPduPort]:
        """
        AUTOSAR-compliant getter for iPduPort.
        
        Returns:
            The iPduPort value
        
        Note:
            Delegates to i_pdu_port property (CODING_RULE_V2_00017)
        """
        return self.i_pdu_port  # Delegates to property

    def getISignal(self) -> List["RefType"]:
        """
        AUTOSAR-compliant getter for iSignal.
        
        Returns:
            The iSignal value
        
        Note:
            Delegates to i_signal property (CODING_RULE_V2_00017)
        """
        return self.i_signal  # Delegates to property

    def getSecOcCrypto(self) -> "SecOcCryptoService":
        """
        AUTOSAR-compliant getter for secOcCrypto.
        
        Returns:
            The secOcCrypto value
        
        Note:
            Delegates to sec_oc_crypto property (CODING_RULE_V2_00017)
        """
        return self.sec_oc_crypto  # Delegates to property

    def setSecOcCrypto(self, value: "SecOcCryptoService") -> PduTriggering:
        """
        AUTOSAR-compliant setter for secOcCrypto with method chaining.
        
        Args:
            value: The secOcCrypto to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to sec_oc_crypto property setter (gets validation automatically)
        """
        self.sec_oc_crypto = value  # Delegates to property setter
        return self

    def getTriggerIPduSend(self) -> List["RefType"]:
        """
        AUTOSAR-compliant getter for triggerIPduSend.
        
        Returns:
            The triggerIPduSend value
        
        Note:
            Delegates to trigger_i_pdu_send property (CODING_RULE_V2_00017)
        """
        return self.trigger_i_pdu_send  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_i_pdu(self, value: Optional[Pdu]) -> PduTriggering:
        """
        Set iPdu and return self for chaining.
        
        Args:
            value: The iPdu to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_i_pdu("value")
        """
        self.i_pdu = value  # Use property setter (gets validation)
        return self

    def with_sec_oc_crypto(self, value: Optional["SecOcCryptoService"]) -> PduTriggering:
        """
        Set secOcCrypto and return self for chaining.
        
        Args:
            value: The secOcCrypto to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_sec_oc_crypto("value")
        """
        self.sec_oc_crypto = value  # Use property setter (gets validation)
        return self



class ISignalGroup(FibexElement):
    """
    SignalGroup of the Interaction Layer. The RTE supports a "signal fan-out"
    where the same System Signal Group is sent in different SignalIPdus to
    multiple receivers. An ISignalGroup refers to a set of ISignals that shall
    always be kept together. A ISignalGroup represents a COM Signal Group.
    Therefore it is recommended to put the ISignalGroup in the same Package as
    ISignals (see atp.recommendedPackage)
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::ISignalGroup
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 993, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 323, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Optional reference to a DataTransformation which the transformer chain that
                # is used to transform data that shall be placed inside this ISignalGroup the
                # COMBasedTransformer approach.
        # atpVariation.
        self._comBased: Optional["DataTransformation"] = None

    @property
    def com_based(self) -> Optional["DataTransformation"]:
        """Get comBased (Pythonic accessor)."""
        return self._comBased

    @com_based.setter
    def com_based(self, value: Optional["DataTransformation"]) -> None:
        """
        Set comBased with validation.
        
        Args:
            value: The comBased to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._comBased = None
            return

        if not isinstance(value, DataTransformation):
            raise TypeError(
                f"comBased must be DataTransformation or None, got {type(value).__name__}"
            )
        self._comBased = value
        # Reference to a set of ISignals that shall always be kept.
        self._iSignal: List[ISignal] = []

    @property
    def i_signal(self) -> List[ISignal]:
        """Get iSignal (Pythonic accessor)."""
        return self._iSignal
        # Reference to the SystemSignalGroup that is defined on level and that is
        # supposed to be transmitted in the.
        self._systemSignal: Optional["RefType"] = None

    @property
    def system_signal(self) -> Optional["RefType"]:
        """Get systemSignal (Pythonic accessor)."""
        return self._systemSignal

    @system_signal.setter
    def system_signal(self, value: Optional["RefType"]) -> None:
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

        self._systemSignal = value
        # A transformer chain consists of an ordered list of transformers.
        # The ISignalGroup specific configuration each transformer are defined in the
                # The transformer that are common for all ISignal described in the
                # TransformationTechnology.
        self._transformation: List["TransformationISignal"] = []

    @property
    def transformation(self) -> List["TransformationISignal"]:
        """Get transformation (Pythonic accessor)."""
        return self._transformation

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getComBased(self) -> "DataTransformation":
        """
        AUTOSAR-compliant getter for comBased.
        
        Returns:
            The comBased value
        
        Note:
            Delegates to com_based property (CODING_RULE_V2_00017)
        """
        return self.com_based  # Delegates to property

    def setComBased(self, value: "DataTransformation") -> ISignalGroup:
        """
        AUTOSAR-compliant setter for comBased with method chaining.
        
        Args:
            value: The comBased to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to com_based property setter (gets validation automatically)
        """
        self.com_based = value  # Delegates to property setter
        return self

    def getISignal(self) -> List[ISignal]:
        """
        AUTOSAR-compliant getter for iSignal.
        
        Returns:
            The iSignal value
        
        Note:
            Delegates to i_signal property (CODING_RULE_V2_00017)
        """
        return self.i_signal  # Delegates to property

    def getSystemSignal(self) -> "RefType":
        """
        AUTOSAR-compliant getter for systemSignal.
        
        Returns:
            The systemSignal value
        
        Note:
            Delegates to system_signal property (CODING_RULE_V2_00017)
        """
        return self.system_signal  # Delegates to property

    def setSystemSignal(self, value: "RefType") -> ISignalGroup:
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

    def with_com_based(self, value: Optional["DataTransformation"]) -> ISignalGroup:
        """
        Set comBased and return self for chaining.
        
        Args:
            value: The comBased to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_com_based("value")
        """
        self.com_based = value  # Use property setter (gets validation)
        return self

    def with_system_signal(self, value: Optional[RefType]) -> ISignalGroup:
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



class FramePort(CommConnectorPort):
    """
    Connectors reception or send port on the referenced channel referenced by a
    FrameTriggering.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::FramePort
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 304, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class IPduPort(CommConnectorPort):
    """
    Connectors reception or send port on the referenced channel referenced by a
    PduTriggering.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::IPduPort
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 304, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Definition of the two signal processing modes Immediate and Deferred for both
        # Tx and Rx IPdus.
        self._iPduSignal: Optional["IPduSignalProcessing"] = None

    @property
    def i_pdu_signal(self) -> Optional["IPduSignalProcessing"]:
        """Get iPduSignal (Pythonic accessor)."""
        return self._iPduSignal

    @i_pdu_signal.setter
    def i_pdu_signal(self, value: Optional["IPduSignalProcessing"]) -> None:
        """
        Set iPduSignal with validation.
        
        Args:
            value: The iPduSignal to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._iPduSignal = None
            return

        if not isinstance(value, IPduSignalProcessing):
            raise TypeError(
                f"iPduSignal must be IPduSignalProcessing or None, got {type(value).__name__}"
            )
        self._iPduSignal = value
        # This attribute defines the bypassing of signature or MAC verification in the
                # receiving ECU.
        # If or set to true the signature authentication or shall be performed for the
                # SecuredIPdu.
        # to false the signature authentication or MAC not be performed for the
                # SecuredIPdu.
        self._rxSecurity: Optional["Boolean"] = None

    @property
    def rx_security(self) -> Optional["Boolean"]:
        """Get rxSecurity (Pythonic accessor)."""
        return self._rxSecurity

    @rx_security.setter
    def rx_security(self, value: Optional["Boolean"]) -> None:
        """
        Set rxSecurity with validation.
        
        Args:
            value: The rxSecurity to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rxSecurity = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"rxSecurity must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._rxSecurity = value
        # This attribute is used to define the maximum allowed in seconds from the
                # expected timestamp for a SecuredIPdu is still deemed authentic.
        # Please this attribute is for documentation only to allow of required
                # freshness value manager upstream mapping is defined for it.
        self._timestampRx: Optional["TimeValue"] = None

    @property
    def timestamp_rx(self) -> Optional["TimeValue"]:
        """Get timestampRx (Pythonic accessor)."""
        return self._timestampRx

    @timestamp_rx.setter
    def timestamp_rx(self, value: Optional["TimeValue"]) -> None:
        """
        Set timestampRx with validation.
        
        Args:
            value: The timestampRx to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._timestampRx = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"timestampRx must be TimeValue or None, got {type(value).__name__}"
            )
        self._timestampRx = value
        # This attribute describes whether a part of AuthenticPdu in a SecuredIPdu
                # shall be passed on to the verifies and generates the Freshness.
        # The part Authentic-PDU is defined by the authData authDataFreshnessLength.
        self._useAuthData: Optional["Boolean"] = None

    @property
    def use_auth_data(self) -> Optional["Boolean"]:
        """Get useAuthData (Pythonic accessor)."""
        return self._useAuthData

    @use_auth_data.setter
    def use_auth_data(self, value: Optional["Boolean"]) -> None:
        """
        Set useAuthData with validation.
        
        Args:
            value: The useAuthData to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._useAuthData = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"useAuthData must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._useAuthData = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getIPduSignal(self) -> "IPduSignalProcessing":
        """
        AUTOSAR-compliant getter for iPduSignal.
        
        Returns:
            The iPduSignal value
        
        Note:
            Delegates to i_pdu_signal property (CODING_RULE_V2_00017)
        """
        return self.i_pdu_signal  # Delegates to property

    def setIPduSignal(self, value: "IPduSignalProcessing") -> IPduPort:
        """
        AUTOSAR-compliant setter for iPduSignal with method chaining.
        
        Args:
            value: The iPduSignal to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to i_pdu_signal property setter (gets validation automatically)
        """
        self.i_pdu_signal = value  # Delegates to property setter
        return self

    def getRxSecurity(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for rxSecurity.
        
        Returns:
            The rxSecurity value
        
        Note:
            Delegates to rx_security property (CODING_RULE_V2_00017)
        """
        return self.rx_security  # Delegates to property

    def setRxSecurity(self, value: "Boolean") -> IPduPort:
        """
        AUTOSAR-compliant setter for rxSecurity with method chaining.
        
        Args:
            value: The rxSecurity to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to rx_security property setter (gets validation automatically)
        """
        self.rx_security = value  # Delegates to property setter
        return self

    def getTimestampRx(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for timestampRx.
        
        Returns:
            The timestampRx value
        
        Note:
            Delegates to timestamp_rx property (CODING_RULE_V2_00017)
        """
        return self.timestamp_rx  # Delegates to property

    def setTimestampRx(self, value: "TimeValue") -> IPduPort:
        """
        AUTOSAR-compliant setter for timestampRx with method chaining.
        
        Args:
            value: The timestampRx to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to timestamp_rx property setter (gets validation automatically)
        """
        self.timestamp_rx = value  # Delegates to property setter
        return self

    def getUseAuthData(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for useAuthData.
        
        Returns:
            The useAuthData value
        
        Note:
            Delegates to use_auth_data property (CODING_RULE_V2_00017)
        """
        return self.use_auth_data  # Delegates to property

    def setUseAuthData(self, value: "Boolean") -> IPduPort:
        """
        AUTOSAR-compliant setter for useAuthData with method chaining.
        
        Args:
            value: The useAuthData to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to use_auth_data property setter (gets validation automatically)
        """
        self.use_auth_data = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_i_pdu_signal(self, value: Optional["IPduSignalProcessing"]) -> IPduPort:
        """
        Set iPduSignal and return self for chaining.
        
        Args:
            value: The iPduSignal to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_i_pdu_signal("value")
        """
        self.i_pdu_signal = value  # Use property setter (gets validation)
        return self

    def with_rx_security(self, value: Optional["Boolean"]) -> IPduPort:
        """
        Set rxSecurity and return self for chaining.
        
        Args:
            value: The rxSecurity to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_rx_security("value")
        """
        self.rx_security = value  # Use property setter (gets validation)
        return self

    def with_timestamp_rx(self, value: Optional["TimeValue"]) -> IPduPort:
        """
        Set timestampRx and return self for chaining.
        
        Args:
            value: The timestampRx to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_timestamp_rx("value")
        """
        self.timestamp_rx = value  # Use property setter (gets validation)
        return self

    def with_use_auth_data(self, value: Optional["Boolean"]) -> IPduPort:
        """
        Set useAuthData and return self for chaining.
        
        Args:
            value: The useAuthData to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_use_auth_data("value")
        """
        self.use_auth_data = value  # Use property setter (gets validation)
        return self



class ISignalPort(CommConnectorPort):
    """
    Connectors reception or send port on the referenced channel referenced by an
    ISignalTriggering. If different timeouts or DataFilters for ISignals need to
    be specified several ISignalPorts may be created.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::ISignalPort
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 305, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Optional specification of a signal COM filter at the in case that the System
        # Description doesn’t complete Software Component Description (VFB supports the
        # inclusion of legacy system a full DataMapping exist for the SystemSignal may
        # be available from a configured this case the ReceiverComSpec optional
        # specification.
        self._dataFilter: Optional["DataFilter"] = None

    @property
    def data_filter(self) -> Optional["DataFilter"]:
        """Get dataFilter (Pythonic accessor)."""
        return self._dataFilter

    @data_filter.setter
    def data_filter(self, value: Optional["DataFilter"]) -> None:
        """
        Set dataFilter with validation.
        
        Args:
            value: The dataFilter to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dataFilter = None
            return

        if not isinstance(value, DataFilter):
            raise TypeError(
                f"dataFilter must be DataFilter or None, got {type(value).__name__}"
            )
        self._dataFilter = value
        # Reference to the DDS Qos profile used for this ISignal.
        self._ddsQosProfile: Optional["DdsCpQosProfile"] = None

    @property
    def dds_qos_profile(self) -> Optional["DdsCpQosProfile"]:
        """Get ddsQosProfile (Pythonic accessor)."""
        return self._ddsQosProfile

    @dds_qos_profile.setter
    def dds_qos_profile(self, value: Optional["DdsCpQosProfile"]) -> None:
        """
        Set ddsQosProfile with validation.
        
        Args:
            value: The ddsQosProfile to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ddsQosProfile = None
            return

        if not isinstance(value, DdsCpQosProfile):
            raise TypeError(
                f"ddsQosProfile must be DdsCpQosProfile or None, got {type(value).__name__}"
            )
        self._ddsQosProfile = value
        # • ISignalPort with communicationDirection = in: timeout value in seconds for
        # the reception of with communicationDirection = out: timeout value in seconds
        # for transmission.
        self._firstTimeout: Optional["TimeValue"] = None

    @property
    def first_timeout(self) -> Optional["TimeValue"]:
        """Get firstTimeout (Pythonic accessor)."""
        return self._firstTimeout

    @first_timeout.setter
    def first_timeout(self, value: Optional["TimeValue"]) -> None:
        """
        Set firstTimeout with validation.
        
        Args:
            value: The firstTimeout to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._firstTimeout = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"firstTimeout must be TimeValue or None, got {type(value).__name__}"
            )
        self._firstTimeout = value
        # This attribute defines how invalidation is applied to the in the context of
                # this ISignalPort.
        # 2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._handleInvalid: Optional["HandleInvalidEnum"] = None

    @property
    def handle_invalid(self) -> Optional["HandleInvalidEnum"]:
        """Get handleInvalid (Pythonic accessor)."""
        return self._handleInvalid

    @handle_invalid.setter
    def handle_invalid(self, value: Optional["HandleInvalidEnum"]) -> None:
        """
        Set handleInvalid with validation.
        
        Args:
            value: The handleInvalid to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._handleInvalid = None
            return

        if not isinstance(value, HandleInvalidEnum):
            raise TypeError(
                f"handleInvalid must be HandleInvalidEnum or None, got {type(value).__name__}"
            )
        self._handleInvalid = value
        # • ISignalPort with communicationDirection = in: value in seconds for the
                # reception of the attribute value is used to configure the Com the COM module.
        # The RTE ignores this timeout can also be specified with the If a exists for
                # the SystemSignal and the available in the configured ReceiverComSpec, timeout
                # value in the ReceiverComSpec overrides timeout specification during the
                # creation of Ecu Configuration of the COM module.
        # with communicationDirection = out: value in seconds for the transmission of
                # The attribute value is used to configure the the COM module.
        # The RTE ignores this timeout can also be specified with the ender If
                # DataMapping exists for the SystemSignal and the available in the configured
                # SenderComSpec, then value in the SenderComSpec overrides this specification
                # during the creation of the can be used in the following cases: signal where
                # the System Description doesn’t complete Software Component Description (VFB
                # where the DataMapping is missing.
        # monitoring use cases in which the DataMapping is.
        self._timeout: Optional["TimeValue"] = None

    @property
    def timeout(self) -> Optional["TimeValue"]:
        """Get timeout (Pythonic accessor)."""
        return self._timeout

    @timeout.setter
    def timeout(self, value: Optional["TimeValue"]) -> None:
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

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"timeout must be TimeValue or None, got {type(value).__name__}"
            )
        self._timeout = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDataFilter(self) -> "DataFilter":
        """
        AUTOSAR-compliant getter for dataFilter.
        
        Returns:
            The dataFilter value
        
        Note:
            Delegates to data_filter property (CODING_RULE_V2_00017)
        """
        return self.data_filter  # Delegates to property

    def setDataFilter(self, value: "DataFilter") -> ISignalPort:
        """
        AUTOSAR-compliant setter for dataFilter with method chaining.
        
        Args:
            value: The dataFilter to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to data_filter property setter (gets validation automatically)
        """
        self.data_filter = value  # Delegates to property setter
        return self

    def getDdsQosProfile(self) -> "DdsCpQosProfile":
        """
        AUTOSAR-compliant getter for ddsQosProfile.
        
        Returns:
            The ddsQosProfile value
        
        Note:
            Delegates to dds_qos_profile property (CODING_RULE_V2_00017)
        """
        return self.dds_qos_profile  # Delegates to property

    def setDdsQosProfile(self, value: "DdsCpQosProfile") -> ISignalPort:
        """
        AUTOSAR-compliant setter for ddsQosProfile with method chaining.
        
        Args:
            value: The ddsQosProfile to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to dds_qos_profile property setter (gets validation automatically)
        """
        self.dds_qos_profile = value  # Delegates to property setter
        return self

    def getFirstTimeout(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for firstTimeout.
        
        Returns:
            The firstTimeout value
        
        Note:
            Delegates to first_timeout property (CODING_RULE_V2_00017)
        """
        return self.first_timeout  # Delegates to property

    def setFirstTimeout(self, value: "TimeValue") -> ISignalPort:
        """
        AUTOSAR-compliant setter for firstTimeout with method chaining.
        
        Args:
            value: The firstTimeout to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to first_timeout property setter (gets validation automatically)
        """
        self.first_timeout = value  # Delegates to property setter
        return self

    def getHandleInvalid(self) -> "HandleInvalidEnum":
        """
        AUTOSAR-compliant getter for handleInvalid.
        
        Returns:
            The handleInvalid value
        
        Note:
            Delegates to handle_invalid property (CODING_RULE_V2_00017)
        """
        return self.handle_invalid  # Delegates to property

    def setHandleInvalid(self, value: "HandleInvalidEnum") -> ISignalPort:
        """
        AUTOSAR-compliant setter for handleInvalid with method chaining.
        
        Args:
            value: The handleInvalid to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to handle_invalid property setter (gets validation automatically)
        """
        self.handle_invalid = value  # Delegates to property setter
        return self

    def getTimeout(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for timeout.
        
        Returns:
            The timeout value
        
        Note:
            Delegates to timeout property (CODING_RULE_V2_00017)
        """
        return self.timeout  # Delegates to property

    def setTimeout(self, value: "TimeValue") -> ISignalPort:
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

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_data_filter(self, value: Optional["DataFilter"]) -> ISignalPort:
        """
        Set dataFilter and return self for chaining.
        
        Args:
            value: The dataFilter to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_data_filter("value")
        """
        self.data_filter = value  # Use property setter (gets validation)
        return self

    def with_dds_qos_profile(self, value: Optional["DdsCpQosProfile"]) -> ISignalPort:
        """
        Set ddsQosProfile and return self for chaining.
        
        Args:
            value: The ddsQosProfile to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_dds_qos_profile("value")
        """
        self.dds_qos_profile = value  # Use property setter (gets validation)
        return self

    def with_first_timeout(self, value: Optional["TimeValue"]) -> ISignalPort:
        """
        Set firstTimeout and return self for chaining.
        
        Args:
            value: The firstTimeout to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_first_timeout("value")
        """
        self.first_timeout = value  # Use property setter (gets validation)
        return self

    def with_handle_invalid(self, value: Optional["HandleInvalidEnum"]) -> ISignalPort:
        """
        Set handleInvalid and return self for chaining.
        
        Args:
            value: The handleInvalid to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_handle_invalid("value")
        """
        self.handle_invalid = value  # Use property setter (gets validation)
        return self

    def with_timeout(self, value: Optional["TimeValue"]) -> ISignalPort:
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



class ISignalProps(ARObject):
    """
    Additional ISignal properties that may be stored in different files.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::ISignalProps
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 323, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute defines the outOfRangeHandling for received and sent signals.
        self._handleOutOf: Optional["HandleOutOfRange"] = None

    @property
    def handle_out_of(self) -> Optional["HandleOutOfRange"]:
        """Get handleOutOf (Pythonic accessor)."""
        return self._handleOutOf

    @handle_out_of.setter
    def handle_out_of(self, value: Optional["HandleOutOfRange"]) -> None:
        """
        Set handleOutOf with validation.
        
        Args:
            value: The handleOutOf to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._handleOutOf = None
            return

        if not isinstance(value, HandleOutOfRange):
            raise TypeError(
                f"handleOutOf must be HandleOutOfRange or None, got {type(value).__name__}"
            )
        self._handleOutOf = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getHandleOutOf(self) -> "HandleOutOfRange":
        """
        AUTOSAR-compliant getter for handleOutOf.
        
        Returns:
            The handleOutOf value
        
        Note:
            Delegates to handle_out_of property (CODING_RULE_V2_00017)
        """
        return self.handle_out_of  # Delegates to property

    def setHandleOutOf(self, value: "HandleOutOfRange") -> ISignalProps:
        """
        AUTOSAR-compliant setter for handleOutOf with method chaining.
        
        Args:
            value: The handleOutOf to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to handle_out_of property setter (gets validation automatically)
        """
        self.handle_out_of = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_handle_out_of(self, value: Optional["HandleOutOfRange"]) -> ISignalProps:
        """
        Set handleOutOf and return self for chaining.
        
        Args:
            value: The handleOutOf to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_handle_out_of("value")
        """
        self.handle_out_of = value  # Use property setter (gets validation)
        return self



class SystemSignalGroup(ARElement):
    """
    A signal group refers to a set of signals that shall always be kept
    together. A signal group is used to guarantee the atomic transfer of AUTOSAR
    composite data types. The SystemSignalGroup defines a signal grouping on VFB
    level. On cluster level the Signal grouping is described by the ISignalGroup
    element.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::SystemSignalGroup
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 324, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to a set of SystemSignals that shall always be.
        self._systemSignal: List[SystemSignal] = []

    @property
    def system_signal(self) -> List[SystemSignal]:
        """Get systemSignal (Pythonic accessor)."""
        return self._systemSignal
        # Optional reference to the SystemSignal which shall the transformed (linear)
        # data.
        self._transforming: Optional[SystemSignal] = None

    @property
    def transforming(self) -> Optional[SystemSignal]:
        """Get transforming (Pythonic accessor)."""
        return self._transforming

    @transforming.setter
    def transforming(self, value: Optional[SystemSignal]) -> None:
        """
        Set transforming with validation.
        
        Args:
            value: The transforming to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._transforming = None
            return

        if not isinstance(value, SystemSignal):
            raise TypeError(
                f"transforming must be SystemSignal or None, got {type(value).__name__}"
            )
        self._transforming = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSystemSignal(self) -> List[SystemSignal]:
        """
        AUTOSAR-compliant getter for systemSignal.
        
        Returns:
            The systemSignal value
        
        Note:
            Delegates to system_signal property (CODING_RULE_V2_00017)
        """
        return self.system_signal  # Delegates to property

    def getTransforming(self) -> SystemSignal:
        """
        AUTOSAR-compliant getter for transforming.
        
        Returns:
            The transforming value
        
        Note:
            Delegates to transforming property (CODING_RULE_V2_00017)
        """
        return self.transforming  # Delegates to property

    def setTransforming(self, value: SystemSignal) -> SystemSignalGroup:
        """
        AUTOSAR-compliant setter for transforming with method chaining.
        
        Args:
            value: The transforming to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to transforming property setter (gets validation automatically)
        """
        self.transforming = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_transforming(self, value: Optional[SystemSignal]) -> SystemSignalGroup:
        """
        Set transforming and return self for chaining.
        
        Args:
            value: The transforming to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_transforming("value")
        """
        self.transforming = value  # Use property setter (gets validation)
        return self



class ISignalToIPduMapping(Identifiable):
    """
    that the exact bit position of the updateIndicationBit Position is linked to
    the value of the attribute packingByte Order because the method of finding
    the bit position is different for the values mostSignificantByteFirst and
    most SignificantByteLast. This means that if the value of packingByteOrder
    is changed while the value of update IndicationBitPosition remains unchanged
    the exact bit position of updateIndicationBitPosition within the enclosing
    ISignalIPdu still undergoes a change. This attribute denotes the least
    significant bit for "Little Endian" and the most significant bit for "Big
    Endian" packed signals within the IPdu (see the description of the
    packingByteOrder attribute). In AUTOSAR the bit counting is always set to
    "sawtooth" and the bit order is set to "Decreasing". The bit counting in
    byte 0 starts with bit 0 (least significant bit). The most significant bit
    in byte 0 is bit 7. Table 6.14: ISignalToIPduMapping [constr_5322] Value
    range of ISignalToIPduMapping.startPosition (cid:100)The value of
    ISignalToIPduMapping.startPosition shall be in the range of 0..4294967295
    Bits.(cid:99)() Please note that the range of
    ISignalToIPduMapping.startPosition is resc- tricted by [constr_5322] to the
    max value of 4294967295 Bits because of the de- fined range of the
    ComBitPosition parameter that is defined in the COM Config- uration [21].
    [constr_5323] Value range of ISignalToIPduMapping.updateIndicationBit-
    Position (cid:100)The value of ISignalToIPduMapping.updateIndicationBitPosi-
    tion shall be in the range of 0..4294967295 Bits.(cid:99)() Please note that
    the range of ISignalToIPduMapping.updateIndicationBit- Position is
    resctricted by [constr_5323] to the max value of 4294967295 Bits be- cause
    of the defined range of the ComUpdateBitPosition parameter that is defined
    in the COM Configuration [21]. [constr_3514] No two ISignalToIPduMappings
    shall reference the identical ISignal (cid:100)No two ISignalToIPduMappings
    shall reference the identical ISignal in the role iSignal in the scope of
    one System.(cid:99)() 326 of 2090 Document ID 63:
    AUTOSAR_CP_TPS_SystemTemplate System Template AUTOSAR CP R23-11
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::ISignalToIPduMapping
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 325, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to a ISignal that is mapped into the ISignal contained in the
                # ISignalGroup shall be an IPdu by an own ISignalToIPduMapping.
        # to the ISignal and to the ISignalGroup in are mutually exclusive.
        self._iSignal: Optional[ISignal] = None

    @property
    def i_signal(self) -> Optional[ISignal]:
        """Get iSignal (Pythonic accessor)."""
        return self._iSignal

    @i_signal.setter
    def i_signal(self, value: Optional[ISignal]) -> None:
        """
        Set iSignal with validation.
        
        Args:
            value: The iSignal to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._iSignal = None
            return

        if not isinstance(value, ISignal):
            raise TypeError(
                f"iSignal must be ISignal or None, got {type(value).__name__}"
            )
        self._iSignal = value
        # Reference to an ISignalGroup that is mapped into the an ISignalToIPduMapping
                # for an ISignal defined, only the UpdateIndicationBitPosition transferProperty
                # is relevant.
        # The startPosition packingByteOrder shall be ignored.
        # contained in the ISignalGroup shall be an IPdu by an own
                # ISignalToIPduMapping.
        # to the ISignal and to the ISignalGroup in are mutually exclusive.
        self._iSignalGroup: Optional["RefType"] = None

    @property
    def i_signal_group(self) -> Optional["RefType"]:
        """Get iSignalGroup (Pythonic accessor)."""
        return self._iSignalGroup

    @i_signal_group.setter
    def i_signal_group(self, value: Optional["RefType"]) -> None:
        """
        Set iSignalGroup with validation.
        
        Args:
            value: The iSignalGroup to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._iSignalGroup = None
            return

        self._iSignalGroup = value
        # This parameter defines the order of the bytes of the signal the packing into
                # the SignalIPdu.
        # The byte ordering (MostSignificantByteLast), "Big Endian" "Opaque" can be
                # selected.
        # data endianness conversion shall be Opaque.
        # The value of this attribute impacts position of the signal into the
                # SignalIPdu startPosition attribute description).
        # ISignalGroup the packingByteOrder is irrelevant be ignored.
        self._packingByte: Optional["ByteOrderEnum"] = None

    @property
    def packing_byte(self) -> Optional["ByteOrderEnum"]:
        """Get packingByte (Pythonic accessor)."""
        return self._packingByte

    @packing_byte.setter
    def packing_byte(self, value: Optional["ByteOrderEnum"]) -> None:
        """
        Set packingByte with validation.
        
        Args:
            value: The packingByte to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._packingByte = None
            return

        if not isinstance(value, ByteOrderEnum):
            raise TypeError(
                f"packingByte must be ByteOrderEnum or None, got {type(value).__name__}"
            )
        self._packingByte = value
        # This parameter is necessary to describe the bitposition of within an
                # SignalIPdu.
        # It denotes the least for "Little Endian" and the most significant "Big
                # Endian" packed signals within the IPdu (see of the packingByteOrder
                # attribute).
        # In bit counting is always set to "sawtooth" bit order is set to "Decreasing".
        # The bit counting 0 starts with bit 0 (least significant bit).
        # The most in byte 0 is bit 7.
        # that the way the bytes will be actually sent on does not impact this
                # representation: they will seen by the software as a byte array.
        # mapping for the ISignalGroup is defined, this attribute and shall be ignored.
        self._startPosition: Optional["UnlimitedInteger"] = None

    @property
    def start_position(self) -> Optional["UnlimitedInteger"]:
        """Get startPosition (Pythonic accessor)."""
        return self._startPosition

    @start_position.setter
    def start_position(self, value: Optional["UnlimitedInteger"]) -> None:
        """
        Set startPosition with validation.
        
        Args:
            value: The startPosition to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._startPosition = None
            return

        if not isinstance(value, UnlimitedInteger):
            raise TypeError(
                f"startPosition must be UnlimitedInteger or None, got {type(value).__name__}"
            )
        self._startPosition = value
        # Defines how the referenced ISignal contributes to the of the ISignalIPdu.
        # 2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._transferProperty: Optional[TransferPropertyEnum] = None

    @property
    def transfer_property(self) -> Optional[TransferPropertyEnum]:
        """Get transferProperty (Pythonic accessor)."""
        return self._transferProperty

    @transfer_property.setter
    def transfer_property(self, value: Optional[TransferPropertyEnum]) -> None:
        """
        Set transferProperty with validation.
        
        Args:
            value: The transferProperty to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._transferProperty = None
            return

        if not isinstance(value, TransferPropertyEnum):
            raise TypeError(
                f"transferProperty must be TransferPropertyEnum or None, got {type(value).__name__}"
            )
        self._transferProperty = value
        # The UpdateIndicationBit indicates to the receivers that the (or the signal
                # group) was updated by the sender.
        # is always one bit.
        # The UpdateIndicationBitPosition the position of the update bit within the
                # Signals of a ISignalGroup this attribute is shall be ignored.
        self._update: Optional["UnlimitedInteger"] = None

    @property
    def update(self) -> Optional["UnlimitedInteger"]:
        """Get update (Pythonic accessor)."""
        return self._update

    @update.setter
    def update(self, value: Optional["UnlimitedInteger"]) -> None:
        """
        Set update with validation.
        
        Args:
            value: The update to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._update = None
            return

        if not isinstance(value, UnlimitedInteger):
            raise TypeError(
                f"update must be UnlimitedInteger or None, got {type(value).__name__}"
            )
        self._update = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getISignal(self) -> ISignal:
        """
        AUTOSAR-compliant getter for iSignal.
        
        Returns:
            The iSignal value
        
        Note:
            Delegates to i_signal property (CODING_RULE_V2_00017)
        """
        return self.i_signal  # Delegates to property

    def setISignal(self, value: ISignal) -> ISignalToIPduMapping:
        """
        AUTOSAR-compliant setter for iSignal with method chaining.
        
        Args:
            value: The iSignal to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to i_signal property setter (gets validation automatically)
        """
        self.i_signal = value  # Delegates to property setter
        return self

    def getISignalGroup(self) -> "RefType":
        """
        AUTOSAR-compliant getter for iSignalGroup.
        
        Returns:
            The iSignalGroup value
        
        Note:
            Delegates to i_signal_group property (CODING_RULE_V2_00017)
        """
        return self.i_signal_group  # Delegates to property

    def setISignalGroup(self, value: "RefType") -> ISignalToIPduMapping:
        """
        AUTOSAR-compliant setter for iSignalGroup with method chaining.
        
        Args:
            value: The iSignalGroup to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to i_signal_group property setter (gets validation automatically)
        """
        self.i_signal_group = value  # Delegates to property setter
        return self

    def getPackingByte(self) -> "ByteOrderEnum":
        """
        AUTOSAR-compliant getter for packingByte.
        
        Returns:
            The packingByte value
        
        Note:
            Delegates to packing_byte property (CODING_RULE_V2_00017)
        """
        return self.packing_byte  # Delegates to property

    def setPackingByte(self, value: "ByteOrderEnum") -> ISignalToIPduMapping:
        """
        AUTOSAR-compliant setter for packingByte with method chaining.
        
        Args:
            value: The packingByte to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to packing_byte property setter (gets validation automatically)
        """
        self.packing_byte = value  # Delegates to property setter
        return self

    def getStartPosition(self) -> "UnlimitedInteger":
        """
        AUTOSAR-compliant getter for startPosition.
        
        Returns:
            The startPosition value
        
        Note:
            Delegates to start_position property (CODING_RULE_V2_00017)
        """
        return self.start_position  # Delegates to property

    def setStartPosition(self, value: "UnlimitedInteger") -> ISignalToIPduMapping:
        """
        AUTOSAR-compliant setter for startPosition with method chaining.
        
        Args:
            value: The startPosition to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to start_position property setter (gets validation automatically)
        """
        self.start_position = value  # Delegates to property setter
        return self

    def getTransferProperty(self) -> TransferPropertyEnum:
        """
        AUTOSAR-compliant getter for transferProperty.
        
        Returns:
            The transferProperty value
        
        Note:
            Delegates to transfer_property property (CODING_RULE_V2_00017)
        """
        return self.transfer_property  # Delegates to property

    def setTransferProperty(self, value: TransferPropertyEnum) -> ISignalToIPduMapping:
        """
        AUTOSAR-compliant setter for transferProperty with method chaining.
        
        Args:
            value: The transferProperty to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to transfer_property property setter (gets validation automatically)
        """
        self.transfer_property = value  # Delegates to property setter
        return self

    def getUpdate(self) -> "UnlimitedInteger":
        """
        AUTOSAR-compliant getter for update.
        
        Returns:
            The update value
        
        Note:
            Delegates to update property (CODING_RULE_V2_00017)
        """
        return self.update  # Delegates to property

    def setUpdate(self, value: "UnlimitedInteger") -> ISignalToIPduMapping:
        """
        AUTOSAR-compliant setter for update with method chaining.
        
        Args:
            value: The update to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to update property setter (gets validation automatically)
        """
        self.update = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_i_signal(self, value: Optional[ISignal]) -> ISignalToIPduMapping:
        """
        Set iSignal and return self for chaining.
        
        Args:
            value: The iSignal to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_i_signal("value")
        """
        self.i_signal = value  # Use property setter (gets validation)
        return self

    def with_i_signal_group(self, value: Optional[RefType]) -> ISignalToIPduMapping:
        """
        Set iSignalGroup and return self for chaining.
        
        Args:
            value: The iSignalGroup to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_i_signal_group("value")
        """
        self.i_signal_group = value  # Use property setter (gets validation)
        return self

    def with_packing_byte(self, value: Optional["ByteOrderEnum"]) -> ISignalToIPduMapping:
        """
        Set packingByte and return self for chaining.
        
        Args:
            value: The packingByte to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_packing_byte("value")
        """
        self.packing_byte = value  # Use property setter (gets validation)
        return self

    def with_start_position(self, value: Optional["UnlimitedInteger"]) -> ISignalToIPduMapping:
        """
        Set startPosition and return self for chaining.
        
        Args:
            value: The startPosition to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_start_position("value")
        """
        self.start_position = value  # Use property setter (gets validation)
        return self

    def with_transfer_property(self, value: Optional[TransferPropertyEnum]) -> ISignalToIPduMapping:
        """
        Set transferProperty and return self for chaining.
        
        Args:
            value: The transferProperty to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_transfer_property("value")
        """
        self.transfer_property = value  # Use property setter (gets validation)
        return self

    def with_update(self, value: Optional["UnlimitedInteger"]) -> ISignalToIPduMapping:
        """
        Set update and return self for chaining.
        
        Args:
            value: The update to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_update("value")
        """
        self.update = value  # Use property setter (gets validation)
        return self



class ISignalTriggering(Identifiable):
    """
    A ISignalTriggering allows an assignment of ISignals to physical channels.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::ISignalTriggering
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 330, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 229, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This reference shall be used if an ISignal is transported PhysicalChannel.
        # This reference forms an XOR the ISignalTriggering-ISignalGroup.
        self._iSignal: Optional[ISignal] = None

    @property
    def i_signal(self) -> Optional[ISignal]:
        """Get iSignal (Pythonic accessor)."""
        return self._iSignal

    @i_signal.setter
    def i_signal(self, value: Optional[ISignal]) -> None:
        """
        Set iSignal with validation.
        
        Args:
            value: The iSignal to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._iSignal = None
            return

        if not isinstance(value, ISignal):
            raise TypeError(
                f"iSignal must be ISignal or None, got {type(value).__name__}"
            )
        self._iSignal = value
        # This reference shall be used if an ISignalGroup is the PhysicalChannel.
        # This reference XOR relationship with the ISignal.
        self._iSignalGroup: Optional["RefType"] = None

    @property
    def i_signal_group(self) -> Optional["RefType"]:
        """Get iSignalGroup (Pythonic accessor)."""
        return self._iSignalGroup

    @i_signal_group.setter
    def i_signal_group(self, value: Optional["RefType"]) -> None:
        """
        Set iSignalGroup with validation.
        
        Args:
            value: The iSignalGroup to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._iSignalGroup = None
            return

        self._iSignalGroup = value
        # References to the ISignalPort on every ECU of the sends and/or receives the
                # ISignal.
        # both the sender and the receiver side included when the system is completely
                # defined.
        self._iSignalPort: List[ISignalPort] = []

    @property
    def i_signal_port(self) -> List[ISignalPort]:
        """Get iSignalPort (Pythonic accessor)."""
        return self._iSignalPort

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getISignal(self) -> ISignal:
        """
        AUTOSAR-compliant getter for iSignal.
        
        Returns:
            The iSignal value
        
        Note:
            Delegates to i_signal property (CODING_RULE_V2_00017)
        """
        return self.i_signal  # Delegates to property

    def setISignal(self, value: ISignal) -> ISignalTriggering:
        """
        AUTOSAR-compliant setter for iSignal with method chaining.
        
        Args:
            value: The iSignal to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to i_signal property setter (gets validation automatically)
        """
        self.i_signal = value  # Delegates to property setter
        return self

    def getISignalGroup(self) -> "RefType":
        """
        AUTOSAR-compliant getter for iSignalGroup.
        
        Returns:
            The iSignalGroup value
        
        Note:
            Delegates to i_signal_group property (CODING_RULE_V2_00017)
        """
        return self.i_signal_group  # Delegates to property

    def setISignalGroup(self, value: "RefType") -> ISignalTriggering:
        """
        AUTOSAR-compliant setter for iSignalGroup with method chaining.
        
        Args:
            value: The iSignalGroup to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to i_signal_group property setter (gets validation automatically)
        """
        self.i_signal_group = value  # Delegates to property setter
        return self

    def getISignalPort(self) -> List[ISignalPort]:
        """
        AUTOSAR-compliant getter for iSignalPort.
        
        Returns:
            The iSignalPort value
        
        Note:
            Delegates to i_signal_port property (CODING_RULE_V2_00017)
        """
        return self.i_signal_port  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_i_signal(self, value: Optional[ISignal]) -> ISignalTriggering:
        """
        Set iSignal and return self for chaining.
        
        Args:
            value: The iSignal to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_i_signal("value")
        """
        self.i_signal = value  # Use property setter (gets validation)
        return self

    def with_i_signal_group(self, value: Optional[RefType]) -> ISignalTriggering:
        """
        Set iSignalGroup and return self for chaining.
        
        Args:
            value: The iSignalGroup to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_i_signal_group("value")
        """
        self.i_signal_group = value  # Use property setter (gets validation)
        return self



class PduToFrameMapping(ARObject):
    """
    that the exact bit position of the updateIndicationBit Position is linked to
    the value of the attribute packingByte Order because the method of finding
    the bit position is different for the values mostSignificantByteFirst and
    most SignificantByteLast. This means that if the value of packingByteOrder
    is changed while the value of update IndicationBitPosition remains unchanged
    the exact bit position of updateIndicationBitPosition within the enclosing
    Frame still undergoes a change. This attribute denotes the least significant
    bit for "Little Endian" and the most significant bit for "Big Endian"
    (cid:53) (cid:53) 346 of 2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate
    System Template AUTOSAR CP R23-11 (cid:52)
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::PduToFrameMapping
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 346, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute defines the order of the bytes of the Pdu the packing into the
                # Frame.
        # Please consider that [constr_3222] are restricting the usage attribute.
        self._packingByte: Optional["ByteOrderEnum"] = None

    @property
    def packing_byte(self) -> Optional["ByteOrderEnum"]:
        """Get packingByte (Pythonic accessor)."""
        return self._packingByte

    @packing_byte.setter
    def packing_byte(self, value: Optional["ByteOrderEnum"]) -> None:
        """
        Set packingByte with validation.
        
        Args:
            value: The packingByte to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._packingByte = None
            return

        if not isinstance(value, ByteOrderEnum):
            raise TypeError(
                f"packingByte must be ByteOrderEnum or None, got {type(value).__name__}"
            )
        self._packingByte = value
        # Reference to a I-Pdu, N-Pdu or NmPdu that is transmitted Frame.
        self._pdu: Optional[Pdu] = None

    @property
    def pdu(self) -> Optional[Pdu]:
        """Get pdu (Pythonic accessor)."""
        return self._pdu

    @pdu.setter
    def pdu(self, value: Optional[Pdu]) -> None:
        """
        Set pdu with validation.
        
        Args:
            value: The pdu to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._pdu = None
            return

        if not isinstance(value, Pdu):
            raise TypeError(
                f"pdu must be Pdu or None, got {type(value).__name__}"
            )
        self._pdu = value
        # This attribute describes the bitposition of a Pdu within a that the absolute
                # position of the Pdu in the determined by the definition of the packingByte If
                # Big Endian is specified, the start the bit position of the most significant
                # bit Frame.
        # If Little Endian is specified, the start position bit position of the least
                # significant bit in the bit counting in byte 0 starts with bit 0 (least The
                # most significant bit in byte 0 is bit 7.
        # are byte aligned in a Frame and only the values 16, 24,.
        # (for little endian) and 7, 15, 23,.
        # (for big allowed.
        self._startPosition: Optional["Integer"] = None

    @property
    def start_position(self) -> Optional["Integer"]:
        """Get startPosition (Pythonic accessor)."""
        return self._startPosition

    @start_position.setter
    def start_position(self, value: Optional["Integer"]) -> None:
        """
        Set startPosition with validation.
        
        Args:
            value: The startPosition to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._startPosition = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"startPosition must be Integer or int or None, got {type(value).__name__}"
            )
        self._startPosition = value
        # Indication to the receivers that the corresponding Pdu updated by the sender.
        # This attribute describes the of the update bit in the frame that aggregates
                # this is always one bit.
        # within the IPdu (see the description of the In AUTOSAR the bit always set to
                # "sawtooth" and the bit order is "Decreasing".
        # The bit counting in byte 0 starts with (least significant bit).
        # The most significant bit in byte bit 7.
        self._update: Optional["Integer"] = None

    @property
    def update(self) -> Optional["Integer"]:
        """Get update (Pythonic accessor)."""
        return self._update

    @update.setter
    def update(self, value: Optional["Integer"]) -> None:
        """
        Set update with validation.
        
        Args:
            value: The update to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._update = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"update must be Integer or int or None, got {type(value).__name__}"
            )
        self._update = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getPackingByte(self) -> "ByteOrderEnum":
        """
        AUTOSAR-compliant getter for packingByte.
        
        Returns:
            The packingByte value
        
        Note:
            Delegates to packing_byte property (CODING_RULE_V2_00017)
        """
        return self.packing_byte  # Delegates to property

    def setPackingByte(self, value: "ByteOrderEnum") -> PduToFrameMapping:
        """
        AUTOSAR-compliant setter for packingByte with method chaining.
        
        Args:
            value: The packingByte to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to packing_byte property setter (gets validation automatically)
        """
        self.packing_byte = value  # Delegates to property setter
        return self

    def getPdu(self) -> Pdu:
        """
        AUTOSAR-compliant getter for pdu.
        
        Returns:
            The pdu value
        
        Note:
            Delegates to pdu property (CODING_RULE_V2_00017)
        """
        return self.pdu  # Delegates to property

    def setPdu(self, value: Pdu) -> PduToFrameMapping:
        """
        AUTOSAR-compliant setter for pdu with method chaining.
        
        Args:
            value: The pdu to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to pdu property setter (gets validation automatically)
        """
        self.pdu = value  # Delegates to property setter
        return self

    def getStartPosition(self) -> "Integer":
        """
        AUTOSAR-compliant getter for startPosition.
        
        Returns:
            The startPosition value
        
        Note:
            Delegates to start_position property (CODING_RULE_V2_00017)
        """
        return self.start_position  # Delegates to property

    def setStartPosition(self, value: "Integer") -> PduToFrameMapping:
        """
        AUTOSAR-compliant setter for startPosition with method chaining.
        
        Args:
            value: The startPosition to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to start_position property setter (gets validation automatically)
        """
        self.start_position = value  # Delegates to property setter
        return self

    def getUpdate(self) -> "Integer":
        """
        AUTOSAR-compliant getter for update.
        
        Returns:
            The update value
        
        Note:
            Delegates to update property (CODING_RULE_V2_00017)
        """
        return self.update  # Delegates to property

    def setUpdate(self, value: "Integer") -> PduToFrameMapping:
        """
        AUTOSAR-compliant setter for update with method chaining.
        
        Args:
            value: The update to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to update property setter (gets validation automatically)
        """
        self.update = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_packing_byte(self, value: Optional["ByteOrderEnum"]) -> PduToFrameMapping:
        """
        Set packingByte and return self for chaining.
        
        Args:
            value: The packingByte to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_packing_byte("value")
        """
        self.packing_byte = value  # Use property setter (gets validation)
        return self

    def with_pdu(self, value: Optional[Pdu]) -> PduToFrameMapping:
        """
        Set pdu and return self for chaining.
        
        Args:
            value: The pdu to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_pdu("value")
        """
        self.pdu = value  # Use property setter (gets validation)
        return self

    def with_start_position(self, value: Optional["Integer"]) -> PduToFrameMapping:
        """
        Set startPosition and return self for chaining.
        
        Args:
            value: The startPosition to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_start_position("value")
        """
        self.start_position = value  # Use property setter (gets validation)
        return self

    def with_update(self, value: Optional["Integer"]) -> PduToFrameMapping:
        """
        Set update and return self for chaining.
        
        Args:
            value: The update to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_update("value")
        """
        self.update = value  # Use property setter (gets validation)
        return self



class IPduTiming(Describable):
    """
    AUTOSAR COM provides the possibility to define two different TRANSMISSION
    MODES for each IPdu. The Transmission Mode of an IPdu that is valid at a
    specific point in time is selected using the values of the signals that are
    mapped to this IPdu. For each IPdu a Transmission Mode Selector is defined.
    The Transmission Mode Selector is calculated by evaluating the conditions
    for a subset of signals (class TransmissionModeCondition in the System
    Template). The Transmission Mode Selector is defined to be true, if at least
    one Condition evaluates to true and is defined to be false, if all
    Conditions evaluate to false.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::IPduTiming
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 348, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Minimum Delay in seconds between successive this I-PDU, independent of the.
        self._minimumDelay: Optional["TimeValue"] = None

    @property
    def minimum_delay(self) -> Optional["TimeValue"]:
        """Get minimumDelay (Pythonic accessor)."""
        return self._minimumDelay

    @minimum_delay.setter
    def minimum_delay(self, value: Optional["TimeValue"]) -> None:
        """
        Set minimumDelay with validation.
        
        Args:
            value: The minimumDelay to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._minimumDelay = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"minimumDelay must be TimeValue or None, got {type(value).__name__}"
            )
        self._minimumDelay = value
        # AUTOSAR COM allows configuring statically two different transmission modes
                # for each I-PDU (True and False).
        # The Mode Selector evaluates the conditions for of signals and decides the
                # transmission mode.
        # It to switch between the transmission modes.
        self._transmission: Optional["TransmissionMode"] = None

    @property
    def transmission(self) -> Optional["TransmissionMode"]:
        """Get transmission (Pythonic accessor)."""
        return self._transmission

    @transmission.setter
    def transmission(self, value: Optional["TransmissionMode"]) -> None:
        """
        Set transmission with validation.
        
        Args:
            value: The transmission to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._transmission = None
            return

        if not isinstance(value, TransmissionMode):
            raise TypeError(
                f"transmission must be TransmissionMode or None, got {type(value).__name__}"
            )
        self._transmission = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMinimumDelay(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for minimumDelay.
        
        Returns:
            The minimumDelay value
        
        Note:
            Delegates to minimum_delay property (CODING_RULE_V2_00017)
        """
        return self.minimum_delay  # Delegates to property

    def setMinimumDelay(self, value: "TimeValue") -> IPduTiming:
        """
        AUTOSAR-compliant setter for minimumDelay with method chaining.
        
        Args:
            value: The minimumDelay to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to minimum_delay property setter (gets validation automatically)
        """
        self.minimum_delay = value  # Delegates to property setter
        return self

    def getTransmission(self) -> "TransmissionMode":
        """
        AUTOSAR-compliant getter for transmission.
        
        Returns:
            The transmission value
        
        Note:
            Delegates to transmission property (CODING_RULE_V2_00017)
        """
        return self.transmission  # Delegates to property

    def setTransmission(self, value: "TransmissionMode") -> IPduTiming:
        """
        AUTOSAR-compliant setter for transmission with method chaining.
        
        Args:
            value: The transmission to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to transmission property setter (gets validation automatically)
        """
        self.transmission = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_minimum_delay(self, value: Optional["TimeValue"]) -> IPduTiming:
        """
        Set minimumDelay and return self for chaining.
        
        Args:
            value: The minimumDelay to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_minimum_delay("value")
        """
        self.minimum_delay = value  # Use property setter (gets validation)
        return self

    def with_transmission(self, value: Optional["TransmissionMode"]) -> IPduTiming:
        """
        Set transmission and return self for chaining.
        
        Args:
            value: The transmission to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_transmission("value")
        """
        self.transmission = value  # Use property setter (gets validation)
        return self



class PdurIPduGroup(FibexElement):
    """
    The AUTOSAR PduR will enable and disable the sending of configurable groups
    of IPdus during runtime according to the AUTOSAR PduR specification.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::PdurIPduGroup
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 352, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute defines the use-case for this PduRIPdu For example, in a
                # diagnostic mode all IPdus - not involved in diagnostic - are disabled.
        # The are not limited to a fixed enumeration and can as a string.
        self._communication: Optional["String"] = None

    @property
    def communication(self) -> Optional["String"]:
        """Get communication (Pythonic accessor)."""
        return self._communication

    @communication.setter
    def communication(self, value: Optional["String"]) -> None:
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

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"communication must be String or str or None, got {type(value).__name__}"
            )
        self._communication = value
        # Reference to a set of IPdus, which are contained in the Group.
        # If an IPdu is routed by the PduR to (PduR fan-out) than an Pdu each
                # destination is created in the System enable/disable a specific destination
                # the to the PduTriggering.
        # content of a PduR I-Pdu group can vary atpVariation.
        self._iPdu: List["RefType"] = []

    @property
    def i_pdu(self) -> List["RefType"]:
        """Get iPdu (Pythonic accessor)."""
        return self._iPdu

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCommunication(self) -> "String":
        """
        AUTOSAR-compliant getter for communication.
        
        Returns:
            The communication value
        
        Note:
            Delegates to communication property (CODING_RULE_V2_00017)
        """
        return self.communication  # Delegates to property

    def setCommunication(self, value: "String") -> PdurIPduGroup:
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

    def getIPdu(self) -> List["RefType"]:
        """
        AUTOSAR-compliant getter for iPdu.
        
        Returns:
            The iPdu value
        
        Note:
            Delegates to i_pdu property (CODING_RULE_V2_00017)
        """
        return self.i_pdu  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_communication(self, value: Optional["String"]) -> PdurIPduGroup:
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



class ContainedIPduProps(ARObject):
    """
    Defines the aspects of an IPdu which can be collected inside a
    ContainerIPdu.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::ContainedIPduProps
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 355, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines whether this ContainedIPdu shall be collected using a last-is-best or
        # queued semantics.
        self._collection: Optional["ContainedIPdu"] = None

    @property
    def collection(self) -> Optional["ContainedIPdu"]:
        """Get collection (Pythonic accessor)."""
        return self._collection

    @collection.setter
    def collection(self, value: Optional["ContainedIPdu"]) -> None:
        """
        Set collection with validation.
        
        Args:
            value: The collection to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._collection = None
            return

        if not isinstance(value, ContainedIPdu):
            raise TypeError(
                f"collection must be ContainedIPdu or None, got {type(value).__name__}"
            )
        self._collection = value
        # Reference to Pdu for which the ContainedIPduProps are.
        self._containedPdu: Optional["RefType"] = None

    @property
    def contained_pdu(self) -> Optional["RefType"]:
        """Get containedPdu (Pythonic accessor)."""
        return self._containedPdu

    @contained_pdu.setter
    def contained_pdu(self, value: Optional["RefType"]) -> None:
        """
        Set containedPdu with validation.
        
        Args:
            value: The containedPdu to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._containedPdu = None
            return

        self._containedPdu = value
        # Defines the header id this IPdu shall have in case this is put inside a
        # ContainerIPdu with headerType = 2090 Document ID 63:
        # AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._headerIdLong: Optional["PositiveInteger"] = None

    @property
    def header_id_long(self) -> Optional["PositiveInteger"]:
        """Get headerIdLong (Pythonic accessor)."""
        return self._headerIdLong

    @header_id_long.setter
    def header_id_long(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set headerIdLong with validation.
        
        Args:
            value: The headerIdLong to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._headerIdLong = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"headerIdLong must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._headerIdLong = value
        # Defines the header id this IPdu shall have in case this is put inside a
        # ContainerIPdu with headerType =.
        self._headerIdShort: Optional["PositiveInteger"] = None

    @property
    def header_id_short(self) -> Optional["PositiveInteger"]:
        """Get headerIdShort (Pythonic accessor)."""
        return self._headerIdShort

    @header_id_short.setter
    def header_id_short(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set headerIdShort with validation.
        
        Args:
            value: The headerIdShort to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._headerIdShort = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"headerIdShort must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._headerIdShort = value
        # Byte offset that describes the location of the Contained the ContainerPdu if
        # no header is used.
        self._offset: Optional["PositiveInteger"] = None

    @property
    def offset(self) -> Optional["PositiveInteger"]:
        """Get offset (Pythonic accessor)."""
        return self._offset

    @offset.setter
    def offset(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set offset with validation.
        
        Args:
            value: The offset to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._offset = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"offset must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._offset = value
        # Defines a priority of a ContainedTxPdu.
        # 255 represents priority and 0 represent the highest priority.
        self._priority: Optional["PositiveInteger"] = None

    @property
    def priority(self) -> Optional["PositiveInteger"]:
        """Get priority (Pythonic accessor)."""
        return self._priority

    @priority.setter
    def priority(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set priority with validation.
        
        Args:
            value: The priority to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._priority = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"priority must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._priority = value
        # Defines a IPdu specific sender timeout which can reduce timer when this
                # containedIPdu is put ContainerIPdu.
        # This attribute is ignored on.
        self._timeout: Optional["TimeValue"] = None

    @property
    def timeout(self) -> Optional["TimeValue"]:
        """Get timeout (Pythonic accessor)."""
        return self._timeout

    @timeout.setter
    def timeout(self, value: Optional["TimeValue"]) -> None:
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

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"timeout must be TimeValue or None, got {type(value).__name__}"
            )
        self._timeout = value
        # Defines whether this IPdu does trigger the sending of the This attribute is
        # ignored on receiver side.
        self._trigger: Optional["RefType"] = None

    @property
    def trigger(self) -> Optional["RefType"]:
        """Get trigger (Pythonic accessor)."""
        return self._trigger

    @trigger.setter
    def trigger(self, value: Optional["RefType"]) -> None:
        """
        Set trigger with validation.
        
        Args:
            value: The trigger to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._trigger = None
            return

        self._trigger = value
        # The updateIndicationBit specifies the bit location of Update-Bit in the
                # Container PDU.
        # It to the receivers that the ContainedIPdu in the updated.
        self._update: Optional["PositiveInteger"] = None

    @property
    def update(self) -> Optional["PositiveInteger"]:
        """Get update (Pythonic accessor)."""
        return self._update

    @update.setter
    def update(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set update with validation.
        
        Args:
            value: The update to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._update = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"update must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._update = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCollection(self) -> "ContainedIPdu":
        """
        AUTOSAR-compliant getter for collection.
        
        Returns:
            The collection value
        
        Note:
            Delegates to collection property (CODING_RULE_V2_00017)
        """
        return self.collection  # Delegates to property

    def setCollection(self, value: "ContainedIPdu") -> ContainedIPduProps:
        """
        AUTOSAR-compliant setter for collection with method chaining.
        
        Args:
            value: The collection to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to collection property setter (gets validation automatically)
        """
        self.collection = value  # Delegates to property setter
        return self

    def getContainedPdu(self) -> "RefType":
        """
        AUTOSAR-compliant getter for containedPdu.
        
        Returns:
            The containedPdu value
        
        Note:
            Delegates to contained_pdu property (CODING_RULE_V2_00017)
        """
        return self.contained_pdu  # Delegates to property

    def setContainedPdu(self, value: "RefType") -> ContainedIPduProps:
        """
        AUTOSAR-compliant setter for containedPdu with method chaining.
        
        Args:
            value: The containedPdu to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to contained_pdu property setter (gets validation automatically)
        """
        self.contained_pdu = value  # Delegates to property setter
        return self

    def getHeaderIdLong(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for headerIdLong.
        
        Returns:
            The headerIdLong value
        
        Note:
            Delegates to header_id_long property (CODING_RULE_V2_00017)
        """
        return self.header_id_long  # Delegates to property

    def setHeaderIdLong(self, value: "PositiveInteger") -> ContainedIPduProps:
        """
        AUTOSAR-compliant setter for headerIdLong with method chaining.
        
        Args:
            value: The headerIdLong to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to header_id_long property setter (gets validation automatically)
        """
        self.header_id_long = value  # Delegates to property setter
        return self

    def getHeaderIdShort(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for headerIdShort.
        
        Returns:
            The headerIdShort value
        
        Note:
            Delegates to header_id_short property (CODING_RULE_V2_00017)
        """
        return self.header_id_short  # Delegates to property

    def setHeaderIdShort(self, value: "PositiveInteger") -> ContainedIPduProps:
        """
        AUTOSAR-compliant setter for headerIdShort with method chaining.
        
        Args:
            value: The headerIdShort to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to header_id_short property setter (gets validation automatically)
        """
        self.header_id_short = value  # Delegates to property setter
        return self

    def getOffset(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for offset.
        
        Returns:
            The offset value
        
        Note:
            Delegates to offset property (CODING_RULE_V2_00017)
        """
        return self.offset  # Delegates to property

    def setOffset(self, value: "PositiveInteger") -> ContainedIPduProps:
        """
        AUTOSAR-compliant setter for offset with method chaining.
        
        Args:
            value: The offset to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to offset property setter (gets validation automatically)
        """
        self.offset = value  # Delegates to property setter
        return self

    def getPriority(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for priority.
        
        Returns:
            The priority value
        
        Note:
            Delegates to priority property (CODING_RULE_V2_00017)
        """
        return self.priority  # Delegates to property

    def setPriority(self, value: "PositiveInteger") -> ContainedIPduProps:
        """
        AUTOSAR-compliant setter for priority with method chaining.
        
        Args:
            value: The priority to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to priority property setter (gets validation automatically)
        """
        self.priority = value  # Delegates to property setter
        return self

    def getTimeout(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for timeout.
        
        Returns:
            The timeout value
        
        Note:
            Delegates to timeout property (CODING_RULE_V2_00017)
        """
        return self.timeout  # Delegates to property

    def setTimeout(self, value: "TimeValue") -> ContainedIPduProps:
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

    def getTrigger(self) -> "RefType":
        """
        AUTOSAR-compliant getter for trigger.
        
        Returns:
            The trigger value
        
        Note:
            Delegates to trigger property (CODING_RULE_V2_00017)
        """
        return self.trigger  # Delegates to property

    def setTrigger(self, value: "RefType") -> ContainedIPduProps:
        """
        AUTOSAR-compliant setter for trigger with method chaining.
        
        Args:
            value: The trigger to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to trigger property setter (gets validation automatically)
        """
        self.trigger = value  # Delegates to property setter
        return self

    def getUpdate(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for update.
        
        Returns:
            The update value
        
        Note:
            Delegates to update property (CODING_RULE_V2_00017)
        """
        return self.update  # Delegates to property

    def setUpdate(self, value: "PositiveInteger") -> ContainedIPduProps:
        """
        AUTOSAR-compliant setter for update with method chaining.
        
        Args:
            value: The update to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to update property setter (gets validation automatically)
        """
        self.update = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_collection(self, value: Optional["ContainedIPdu"]) -> ContainedIPduProps:
        """
        Set collection and return self for chaining.
        
        Args:
            value: The collection to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_collection("value")
        """
        self.collection = value  # Use property setter (gets validation)
        return self

    def with_contained_pdu(self, value: Optional[RefType]) -> ContainedIPduProps:
        """
        Set containedPdu and return self for chaining.
        
        Args:
            value: The containedPdu to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_contained_pdu("value")
        """
        self.contained_pdu = value  # Use property setter (gets validation)
        return self

    def with_header_id_long(self, value: Optional["PositiveInteger"]) -> ContainedIPduProps:
        """
        Set headerIdLong and return self for chaining.
        
        Args:
            value: The headerIdLong to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_header_id_long("value")
        """
        self.header_id_long = value  # Use property setter (gets validation)
        return self

    def with_header_id_short(self, value: Optional["PositiveInteger"]) -> ContainedIPduProps:
        """
        Set headerIdShort and return self for chaining.
        
        Args:
            value: The headerIdShort to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_header_id_short("value")
        """
        self.header_id_short = value  # Use property setter (gets validation)
        return self

    def with_offset(self, value: Optional["PositiveInteger"]) -> ContainedIPduProps:
        """
        Set offset and return self for chaining.
        
        Args:
            value: The offset to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_offset("value")
        """
        self.offset = value  # Use property setter (gets validation)
        return self

    def with_priority(self, value: Optional["PositiveInteger"]) -> ContainedIPduProps:
        """
        Set priority and return self for chaining.
        
        Args:
            value: The priority to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_priority("value")
        """
        self.priority = value  # Use property setter (gets validation)
        return self

    def with_timeout(self, value: Optional["TimeValue"]) -> ContainedIPduProps:
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

    def with_trigger(self, value: Optional[RefType]) -> ContainedIPduProps:
        """
        Set trigger and return self for chaining.
        
        Args:
            value: The trigger to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_trigger("value")
        """
        self.trigger = value  # Use property setter (gets validation)
        return self

    def with_update(self, value: Optional["PositiveInteger"]) -> ContainedIPduProps:
        """
        Set update and return self for chaining.
        
        Args:
            value: The update to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_update("value")
        """
        self.update = value  # Use property setter (gets validation)
        return self



class SecureCommunicationProps(ARObject):
    """
    This meta-class contains configuration settings that are specific for an
    individual SecuredIPdu.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::SecureCommunicationProps
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 369, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This value determines the start position in bits of the PDU that shall be
                # passed on to the SWC that and generates the Freshness.
        # The bit counting is to TPS_SYST_01068.
        self._authData: Optional["PositiveInteger"] = None

    @property
    def auth_data(self) -> Optional["PositiveInteger"]:
        """Get authData (Pythonic accessor)."""
        return self._authData

    @auth_data.setter
    def auth_data(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set authData with validation.
        
        Args:
            value: The authData to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._authData = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"authData must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._authData = value
        # This attribute defines the additional number of attempts that are to be
                # carried out when of the authentication information failed for SecuredIPdu.
        # If zero is set than only one is done.
        self._authentication: Optional["PositiveInteger"] = None

    @property
    def authentication(self) -> Optional["PositiveInteger"]:
        """Get authentication (Pythonic accessor)."""
        return self._authentication

    @authentication.setter
    def authentication(self, value: Optional["PositiveInteger"]) -> None:
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

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"authentication must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._authentication = value
        # This attribute defines a numerical identifier for the.
        self._dataId: Optional["PositiveInteger"] = None

    @property
    def data_id(self) -> Optional["PositiveInteger"]:
        """Get dataId (Pythonic accessor)."""
        return self._dataId

    @data_id.setter
    def data_id(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set dataId with validation.
        
        Args:
            value: The dataId to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dataId = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"dataId must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._dataId = value
        # This attribute defines the Id of the Freshness Value.
        # The Value might be a normal counter or a time.
        self._freshnessValue: Optional["PositiveInteger"] = None

    @property
    def freshness_value(self) -> Optional["PositiveInteger"]:
        """Get freshnessValue (Pythonic accessor)."""
        return self._freshnessValue

    @freshness_value.setter
    def freshness_value(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set freshnessValue with validation.
        
        Args:
            value: The freshnessValue to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._freshnessValue = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"freshnessValue must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._freshnessValue = value
        # SecOC links an AuthenticIPdu and CryptographicIPdu by repeating a specific
                # part (Message Linker) of in the CryptographicIPdu.
        # This attribute startPosition in bits of the messageLinker.
        self._messageLink: Optional["PositiveInteger"] = None

    @property
    def message_link(self) -> Optional["PositiveInteger"]:
        """Get messageLink (Pythonic accessor)."""
        return self._messageLink

    @message_link.setter
    def message_link(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set messageLink with validation.
        
        Args:
            value: The messageLink to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._messageLink = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"messageLink must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._messageLink = value
        # This attribute defines the Id of the Secondary Freshness The Secondary
                # Freshness Value might be a counter or a time value.
        # Please note that this for documentation only to allow the required freshness
                # value manager and no is defined for it.
        self._secondary: Optional["PositiveInteger"] = None

    @property
    def secondary(self) -> Optional["PositiveInteger"]:
        """Get secondary (Pythonic accessor)."""
        return self._secondary

    @secondary.setter
    def secondary(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set secondary with validation.
        
        Args:
            value: The secondary to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._secondary = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"secondary must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._secondary = value
        # This attribute defines the start position (offset in byte) of area within the
        # payload Pdu which will be secured.
        self._securedArea: Optional["PositiveInteger"] = None

    @property
    def secured_area(self) -> Optional["PositiveInteger"]:
        """Get securedArea (Pythonic accessor)."""
        return self._securedArea

    @secured_area.setter
    def secured_area(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set securedArea with validation.
        
        Args:
            value: The securedArea to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._securedArea = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"securedArea must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._securedArea = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAuthData(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for authData.
        
        Returns:
            The authData value
        
        Note:
            Delegates to auth_data property (CODING_RULE_V2_00017)
        """
        return self.auth_data  # Delegates to property

    def setAuthData(self, value: "PositiveInteger") -> SecureCommunicationProps:
        """
        AUTOSAR-compliant setter for authData with method chaining.
        
        Args:
            value: The authData to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to auth_data property setter (gets validation automatically)
        """
        self.auth_data = value  # Delegates to property setter
        return self

    def getAuthentication(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for authentication.
        
        Returns:
            The authentication value
        
        Note:
            Delegates to authentication property (CODING_RULE_V2_00017)
        """
        return self.authentication  # Delegates to property

    def setAuthentication(self, value: "PositiveInteger") -> SecureCommunicationProps:
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

    def getDataId(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for dataId.
        
        Returns:
            The dataId value
        
        Note:
            Delegates to data_id property (CODING_RULE_V2_00017)
        """
        return self.data_id  # Delegates to property

    def setDataId(self, value: "PositiveInteger") -> SecureCommunicationProps:
        """
        AUTOSAR-compliant setter for dataId with method chaining.
        
        Args:
            value: The dataId to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to data_id property setter (gets validation automatically)
        """
        self.data_id = value  # Delegates to property setter
        return self

    def getFreshnessValue(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for freshnessValue.
        
        Returns:
            The freshnessValue value
        
        Note:
            Delegates to freshness_value property (CODING_RULE_V2_00017)
        """
        return self.freshness_value  # Delegates to property

    def setFreshnessValue(self, value: "PositiveInteger") -> SecureCommunicationProps:
        """
        AUTOSAR-compliant setter for freshnessValue with method chaining.
        
        Args:
            value: The freshnessValue to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to freshness_value property setter (gets validation automatically)
        """
        self.freshness_value = value  # Delegates to property setter
        return self

    def getMessageLink(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for messageLink.
        
        Returns:
            The messageLink value
        
        Note:
            Delegates to message_link property (CODING_RULE_V2_00017)
        """
        return self.message_link  # Delegates to property

    def setMessageLink(self, value: "PositiveInteger") -> SecureCommunicationProps:
        """
        AUTOSAR-compliant setter for messageLink with method chaining.
        
        Args:
            value: The messageLink to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to message_link property setter (gets validation automatically)
        """
        self.message_link = value  # Delegates to property setter
        return self

    def getSecondary(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for secondary.
        
        Returns:
            The secondary value
        
        Note:
            Delegates to secondary property (CODING_RULE_V2_00017)
        """
        return self.secondary  # Delegates to property

    def setSecondary(self, value: "PositiveInteger") -> SecureCommunicationProps:
        """
        AUTOSAR-compliant setter for secondary with method chaining.
        
        Args:
            value: The secondary to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to secondary property setter (gets validation automatically)
        """
        self.secondary = value  # Delegates to property setter
        return self

    def getSecuredArea(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for securedArea.
        
        Returns:
            The securedArea value
        
        Note:
            Delegates to secured_area property (CODING_RULE_V2_00017)
        """
        return self.secured_area  # Delegates to property

    def setSecuredArea(self, value: "PositiveInteger") -> SecureCommunicationProps:
        """
        AUTOSAR-compliant setter for securedArea with method chaining.
        
        Args:
            value: The securedArea to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to secured_area property setter (gets validation automatically)
        """
        self.secured_area = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_auth_data(self, value: Optional["PositiveInteger"]) -> SecureCommunicationProps:
        """
        Set authData and return self for chaining.
        
        Args:
            value: The authData to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_auth_data("value")
        """
        self.auth_data = value  # Use property setter (gets validation)
        return self

    def with_authentication(self, value: Optional["PositiveInteger"]) -> SecureCommunicationProps:
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

    def with_data_id(self, value: Optional["PositiveInteger"]) -> SecureCommunicationProps:
        """
        Set dataId and return self for chaining.
        
        Args:
            value: The dataId to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_data_id("value")
        """
        self.data_id = value  # Use property setter (gets validation)
        return self

    def with_freshness_value(self, value: Optional["PositiveInteger"]) -> SecureCommunicationProps:
        """
        Set freshnessValue and return self for chaining.
        
        Args:
            value: The freshnessValue to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_freshness_value("value")
        """
        self.freshness_value = value  # Use property setter (gets validation)
        return self

    def with_message_link(self, value: Optional["PositiveInteger"]) -> SecureCommunicationProps:
        """
        Set messageLink and return self for chaining.
        
        Args:
            value: The messageLink to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_message_link("value")
        """
        self.message_link = value  # Use property setter (gets validation)
        return self

    def with_secondary(self, value: Optional["PositiveInteger"]) -> SecureCommunicationProps:
        """
        Set secondary and return self for chaining.
        
        Args:
            value: The secondary to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_secondary("value")
        """
        self.secondary = value  # Use property setter (gets validation)
        return self

    def with_secured_area(self, value: Optional["PositiveInteger"]) -> SecureCommunicationProps:
        """
        Set securedArea and return self for chaining.
        
        Args:
            value: The securedArea to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_secured_area("value")
        """
        self.secured_area = value  # Use property setter (gets validation)
        return self



class SecureCommunicationPropsSet(FibexElement):
    """
    Collection of properties used to configure SecuredIPdus.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::SecureCommunicationPropsSet
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 370, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Authentication properties used to configure Secured IPdus.
        self._authentication: List["SecureCommunication"] = []

    @property
    def authentication(self) -> List["SecureCommunication"]:
        """Get authentication (Pythonic accessor)."""
        return self._authentication
        # Freshness properties used to configure SecuredIPdus.
        self._freshnessProps: List["SecureCommunication"] = []

    @property
    def freshness_props(self) -> List["SecureCommunication"]:
        """Get freshnessProps (Pythonic accessor)."""
        return self._freshnessProps

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAuthentication(self) -> List["SecureCommunication"]:
        """
        AUTOSAR-compliant getter for authentication.
        
        Returns:
            The authentication value
        
        Note:
            Delegates to authentication property (CODING_RULE_V2_00017)
        """
        return self.authentication  # Delegates to property

    def getFreshnessProps(self) -> List["SecureCommunication"]:
        """
        AUTOSAR-compliant getter for freshnessProps.
        
        Returns:
            The freshnessProps value
        
        Note:
            Delegates to freshness_props property (CODING_RULE_V2_00017)
        """
        return self.freshness_props  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class SecureCommunicationFreshnessProps(Identifiable):
    """
    Freshness properties used to configure SecuredIPdus.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::SecureCommunicationFreshnessProps
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 370, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute defines a factor that specifies the time for the Freshness
                # Timestamp.
        # It holds a factor that specifies the concrete meaning Freshness Timestamp
                # increment by one on basis of.
        self._freshness: Optional["PositiveInteger"] = None

    @property
    def freshness(self) -> Optional["PositiveInteger"]:
        """Get freshness (Pythonic accessor)."""
        return self._freshness

    @freshness.setter
    def freshness(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set freshness with validation.
        
        Args:
            value: The freshness to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._freshness = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"freshness must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._freshness = value
        # This attribute defines the length in bits of the Freshness to be included in
                # the payload of the Secured I-PDU.
        # is specific to the least significant bits of the Counter.
        # If the attribute is 0 no is included in the Secured I-PDU.
        # 2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._freshnessValue: Optional["PositiveInteger"] = None

    @property
    def freshness_value(self) -> Optional["PositiveInteger"]:
        """Get freshnessValue (Pythonic accessor)."""
        return self._freshnessValue

    @freshness_value.setter
    def freshness_value(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set freshnessValue with validation.
        
        Args:
            value: The freshnessValue to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._freshnessValue = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"freshnessValue must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._freshnessValue = value
        # This attribute specifies whether the Freshness Value is through individual
        # Freshness Counters or by a value is set to TRUE when Timestamps.
        self._useFreshness: Optional["Boolean"] = None

    @property
    def use_freshness(self) -> Optional["Boolean"]:
        """Get useFreshness (Pythonic accessor)."""
        return self._useFreshness

    @use_freshness.setter
    def use_freshness(self, value: Optional["Boolean"]) -> None:
        """
        Set useFreshness with validation.
        
        Args:
            value: The useFreshness to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._useFreshness = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"useFreshness must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._useFreshness = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getFreshness(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for freshness.
        
        Returns:
            The freshness value
        
        Note:
            Delegates to freshness property (CODING_RULE_V2_00017)
        """
        return self.freshness  # Delegates to property

    def setFreshness(self, value: "PositiveInteger") -> SecureCommunicationFreshnessProps:
        """
        AUTOSAR-compliant setter for freshness with method chaining.
        
        Args:
            value: The freshness to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to freshness property setter (gets validation automatically)
        """
        self.freshness = value  # Delegates to property setter
        return self

    def getFreshnessValue(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for freshnessValue.
        
        Returns:
            The freshnessValue value
        
        Note:
            Delegates to freshness_value property (CODING_RULE_V2_00017)
        """
        return self.freshness_value  # Delegates to property

    def setFreshnessValue(self, value: "PositiveInteger") -> SecureCommunicationFreshnessProps:
        """
        AUTOSAR-compliant setter for freshnessValue with method chaining.
        
        Args:
            value: The freshnessValue to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to freshness_value property setter (gets validation automatically)
        """
        self.freshness_value = value  # Delegates to property setter
        return self

    def getUseFreshness(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for useFreshness.
        
        Returns:
            The useFreshness value
        
        Note:
            Delegates to use_freshness property (CODING_RULE_V2_00017)
        """
        return self.use_freshness  # Delegates to property

    def setUseFreshness(self, value: "Boolean") -> SecureCommunicationFreshnessProps:
        """
        AUTOSAR-compliant setter for useFreshness with method chaining.
        
        Args:
            value: The useFreshness to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to use_freshness property setter (gets validation automatically)
        """
        self.use_freshness = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_freshness(self, value: Optional["PositiveInteger"]) -> SecureCommunicationFreshnessProps:
        """
        Set freshness and return self for chaining.
        
        Args:
            value: The freshness to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_freshness("value")
        """
        self.freshness = value  # Use property setter (gets validation)
        return self

    def with_freshness_value(self, value: Optional["PositiveInteger"]) -> SecureCommunicationFreshnessProps:
        """
        Set freshnessValue and return self for chaining.
        
        Args:
            value: The freshnessValue to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_freshness_value("value")
        """
        self.freshness_value = value  # Use property setter (gets validation)
        return self

    def with_use_freshness(self, value: Optional["Boolean"]) -> SecureCommunicationFreshnessProps:
        """
        Set useFreshness and return self for chaining.
        
        Args:
            value: The useFreshness to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_use_freshness("value")
        """
        self.use_freshness = value  # Use property setter (gets validation)
        return self



class SecureCommunicationAuthenticationProps(Identifiable):
    """
    Authentication properties used to configure SecuredIPdus.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::SecureCommunicationAuthenticationProps
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 371, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute defines the length in bits of the code to be included in the
        # payload of the.
        self._authInfoTx: Optional["PositiveInteger"] = None

    @property
    def auth_info_tx(self) -> Optional["PositiveInteger"]:
        """Get authInfoTx (Pythonic accessor)."""
        return self._authInfoTx

    @auth_info_tx.setter
    def auth_info_tx(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set authInfoTx with validation.
        
        Args:
            value: The authInfoTx to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._authInfoTx = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"authInfoTx must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._authInfoTx = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAuthInfoTx(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for authInfoTx.
        
        Returns:
            The authInfoTx value
        
        Note:
            Delegates to auth_info_tx property (CODING_RULE_V2_00017)
        """
        return self.auth_info_tx  # Delegates to property

    def setAuthInfoTx(self, value: "PositiveInteger") -> SecureCommunicationAuthenticationProps:
        """
        AUTOSAR-compliant setter for authInfoTx with method chaining.
        
        Args:
            value: The authInfoTx to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to auth_info_tx property setter (gets validation automatically)
        """
        self.auth_info_tx = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_auth_info_tx(self, value: Optional["PositiveInteger"]) -> SecureCommunicationAuthenticationProps:
        """
        Set authInfoTx and return self for chaining.
        
        Args:
            value: The authInfoTx to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_auth_info_tx("value")
        """
        self.auth_info_tx = value  # Use property setter (gets validation)
        return self



class DynamicPartAlternative(ARObject):
    """
    One of the Com IPdu alternatives that are transmitted in the Dynamic Part of
    the MultiplexedIPdu. The selectorFieldCode specifies which Com IPdu is
    contained in the DynamicPart within a certain transmission of a multiplexed
    PDU.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::DynamicPartAlternative
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 411, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Dynamic part that shall be used to initialize this IPdu.
        # one DynamicPartAlternative in a be the initialDynamicPart.
        self._initialDynamic: Optional["Boolean"] = None

    @property
    def initial_dynamic(self) -> Optional["Boolean"]:
        """Get initialDynamic (Pythonic accessor)."""
        return self._initialDynamic

    @initial_dynamic.setter
    def initial_dynamic(self, value: Optional["Boolean"]) -> None:
        """
        Set initialDynamic with validation.
        
        Args:
            value: The initialDynamic to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._initialDynamic = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"initialDynamic must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._initialDynamic = value
        # Reference to a Com IPdu which is routed to the IPduM is combined to a
        # multiplexedPdu.
        self._iPdu: Optional[ISignalIPdu] = None

    @property
    def i_pdu(self) -> Optional[ISignalIPdu]:
        """Get iPdu (Pythonic accessor)."""
        return self._iPdu

    @i_pdu.setter
    def i_pdu(self, value: Optional[ISignalIPdu]) -> None:
        """
        Set iPdu with validation.
        
        Args:
            value: The iPdu to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._iPdu = None
            return

        if not isinstance(value, ISignalIPdu):
            raise TypeError(
                f"iPdu must be ISignalIPdu or None, got {type(value).__name__}"
            )
        self._iPdu = value
        # The selector field is part of a multiplexed IPdu.
        # It consists contiguous bits.
        # The value of the selector field selects of the multiplexed part of the IPdu.
        self._selectorField: Optional["Integer"] = None

    @property
    def selector_field(self) -> Optional["Integer"]:
        """Get selectorField (Pythonic accessor)."""
        return self._selectorField

    @selector_field.setter
    def selector_field(self, value: Optional["Integer"]) -> None:
        """
        Set selectorField with validation.
        
        Args:
            value: The selectorField to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._selectorField = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"selectorField must be Integer or int or None, got {type(value).__name__}"
            )
        self._selectorField = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getInitialDynamic(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for initialDynamic.
        
        Returns:
            The initialDynamic value
        
        Note:
            Delegates to initial_dynamic property (CODING_RULE_V2_00017)
        """
        return self.initial_dynamic  # Delegates to property

    def setInitialDynamic(self, value: "Boolean") -> DynamicPartAlternative:
        """
        AUTOSAR-compliant setter for initialDynamic with method chaining.
        
        Args:
            value: The initialDynamic to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to initial_dynamic property setter (gets validation automatically)
        """
        self.initial_dynamic = value  # Delegates to property setter
        return self

    def getIPdu(self) -> ISignalIPdu:
        """
        AUTOSAR-compliant getter for iPdu.
        
        Returns:
            The iPdu value
        
        Note:
            Delegates to i_pdu property (CODING_RULE_V2_00017)
        """
        return self.i_pdu  # Delegates to property

    def setIPdu(self, value: ISignalIPdu) -> DynamicPartAlternative:
        """
        AUTOSAR-compliant setter for iPdu with method chaining.
        
        Args:
            value: The iPdu to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to i_pdu property setter (gets validation automatically)
        """
        self.i_pdu = value  # Delegates to property setter
        return self

    def getSelectorField(self) -> "Integer":
        """
        AUTOSAR-compliant getter for selectorField.
        
        Returns:
            The selectorField value
        
        Note:
            Delegates to selector_field property (CODING_RULE_V2_00017)
        """
        return self.selector_field  # Delegates to property

    def setSelectorField(self, value: "Integer") -> DynamicPartAlternative:
        """
        AUTOSAR-compliant setter for selectorField with method chaining.
        
        Args:
            value: The selectorField to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to selector_field property setter (gets validation automatically)
        """
        self.selector_field = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_initial_dynamic(self, value: Optional["Boolean"]) -> DynamicPartAlternative:
        """
        Set initialDynamic and return self for chaining.
        
        Args:
            value: The initialDynamic to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_initial_dynamic("value")
        """
        self.initial_dynamic = value  # Use property setter (gets validation)
        return self

    def with_i_pdu(self, value: Optional[ISignalIPdu]) -> DynamicPartAlternative:
        """
        Set iPdu and return self for chaining.
        
        Args:
            value: The iPdu to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_i_pdu("value")
        """
        self.i_pdu = value  # Use property setter (gets validation)
        return self

    def with_selector_field(self, value: Optional["Integer"]) -> DynamicPartAlternative:
        """
        Set selectorField and return self for chaining.
        
        Args:
            value: The selectorField to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_selector_field("value")
        """
        self.selector_field = value  # Use property setter (gets validation)
        return self



class MultiplexedPart(ARObject, ABC):
    """
    The StaticPart and the DynamicPart have common properties. Both can be
    separated in multiple segments within the multiplexed PDU.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::MultiplexedPart
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 411, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is MultiplexedPart:
            raise TypeError("MultiplexedPart is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The StaticPart and the DynamicPart can be separated in segments within the
                # multiplexed PDU.
        # Therefore and the DynamicPart can contain multiple.
        self._segment: List[SegmentPosition] = []

    @property
    def segment(self) -> List[SegmentPosition]:
        """Get segment (Pythonic accessor)."""
        return self._segment

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSegment(self) -> List[SegmentPosition]:
        """
        AUTOSAR-compliant getter for segment.
        
        Returns:
            The segment value
        
        Note:
            Delegates to segment property (CODING_RULE_V2_00017)
        """
        return self.segment  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class SegmentPosition(ARObject):
    """
    that the absolute position of the segment in the MultiplexedIPdu is
    determined by the definition of the segmentByteOrder attribute of the
    SegmentPosition. If Big Endian is specified, the start position indicates
    the bit position of the most significant bit in the IPdu. If Little Endian
    is specified, the start position indicates the bit position of the least
    significant bit in the IPdu. In AUTOSAR the bit counting is always set to
    "sawtooth" and the bit order is set to "Decreasing". The bit counting in
    byte 0 starts with bit 0 (least significant bit). The most significant bit
    in byte 0 is bit 7. Table 6.77: SegmentPosition [constr_9182] Existence of
    SegmentPosition.segmentByteOrder (cid:100)For each SegmentPosition, the
    attribute segmentByteOrder shall exist at the time when the System
    Description is complete.(cid:99)() [constr_9183] Existence of
    SegmentPosition.segmentLength (cid:100)For each Seg- mentPosition, the
    attribute segmentLength shall exist at the time when the System Description
    is complete.(cid:99)() [constr_9184] Existence of
    SegmentPosition.segmentPosition (cid:100)For each SegmentPosition, the
    attribute segmentPosition shall exist at the time when the System
    Description is complete.(cid:99)() [constr_3247] Byte order mix within a
    MultiplexedIPdu is not allowed (cid:100)The segmentByteOrder of all
    SegmentPositions and the selectorFieldByte- Order shall have the same value
    in the MultiplexedIPdu.(cid:99)() [constr_3223] No ByteOrderEnum.opaque
    allowed for MultiplexedIPdu.se- lectorFieldByteOrder (cid:100)The values of
    MultiplexedIPdu.selectorFieldBy- teOrder are restricted to
    ByteOrderEnum.mostSignificantByteFirst and
    ByteOrderEnum.mostSignificantByteLast. I.e. the value ByteOrderEnum. opaque
    is not allowed.(cid:99)() [constr_3224] No ByteOrderEnum.opaque allowed for
    SegmentPosition.seg- mentByteOrder. (cid:100)The values of
    SegmentPosition.segmentByteOrder are re- stricted to
    ByteOrderEnum.mostSignificantByteFirst and ByteOrderEnum. 412 of 2090
    Document ID 63: AUTOSAR_CP_TPS_SystemTemplate System Template AUTOSAR CP
    R23-11 mostSignificantByteLast. I.e. the value ByteOrderEnum.opaque is not
    al- lowed.(cid:99)() Figure 6.26 shows an example of an IPdu Multiplexer.
    The static part of the multiplexed IPdu contains ComIPduA. The value of the
    selector field in the dynamic part decides which content is transmitted.
    ComIPduB is transmitted if the selector field value is "0". ComIPduC is
    transmitted if the selector field value is "1". The static and the dynamic
    part can consist of more than one element. These sub parts of the static or
    dynamic parts are called segments. In Figure 6.26 the dynamic Part is
    segmented into two parts. More details can be found in [23]. MuxPdu:
    MultiplexedIPdu selectorFieldLength = 1 length = 64
    selectorFieldStartPosition = 0 staticSegment: SegmentPosition :StaticPart
    segmentLength = 16 segmentPosition = 32 :DynamicPart dynamicSegment1:
    SegmentPosition segmentLength = 31 segmentPosition = 1 PduA: ISignalIPdu
    dynamicSegment2: SegmentPosition segmentLength = 16 segmentPosition = 48
    PduC: ISignalIPdu alternative1: DynamicPartAlternative selectorFieldCode = 1
    PduB: ISignalIPdu alternative2: DynamicPartAlternative selectorFieldCode = 0
    Figure 6.26: I-Pdu Multiplexer Example Each of the following figures shows
    an example with an allowed IPduM configuration. Please note that the AUTOSAR
    IPduM module does not shift any part (static or dy- namic) IPdu and just
    merges the payload. ISignalIPdus that are referenced by the different
    DynamicPartAlternatives in one MultiplexedIPdu shall always have the same
    length. A configuration may be optimized with respect to unused data at end
    of a StaticPart ISignalIPdu. This is shown in figure 6.27 where the
    ISignalIPdu that is referenced by the StaticPart is shorter than the Multi-
    plexedIPdu. An optimization with respect to unused data at end of
    DynamicPar- tAlternative ISignalIPdus is shown in figure 6.28. 413 of 2090
    Document ID 63: AUTOSAR_CP_TPS_SystemTemplate System Template AUTOSAR CP
    R23-11 0 48 64 MultiplexedPdu: Switch DynamicPart StaticPart DynamicPart
    All(cid:2)dynamic part Referenced ISignalIPdus:(cid:2)(cid:2)
    alternatives(cid:2)have the 0 8 same(cid:2)size,(cid:2)even if
    alternatives(cid:2)contain DynamicPartAlternative: 1 Signal1 Signal2 unused
    areas. 0 8 DynamicPartAlternative: 2 Signal3 Signal4 Signal5 0 8
    DynamicPartAlternative: 3 Signal3 Signal4 Signal6 0 The(cid:2)static
    StaticPart: Signal6 part may be shorter Figure 6.27: Multiplexer
    configuration example optimized with respect to unused data at end of static
    part Pdu 0 48 64 MultiplexedPdu: Switch DynamicPart StaticPart Referenced
    ISignalIPdus:(cid:2)(cid:2) 0 8 DynamicPartAlternative: 1 Signal1 Signal2
    All(cid:2)dynamic part The(cid:2)dynamic alternatives(cid:2)have the parts
    may be same(cid:2)size,(cid:2)even if 0 8 alternatives(cid:2)contain shorter
    than the static part unused areas. DynamicPartAlternative: 2 Signal3 Signal4
    0 8 DynamicPartAlternative: 3 Signal3 Signal4 Signal5 0 48 StaticPart:
    Signal6 Figure 6.28: Multiplexer configuration example optimized with
    respect to unused data at end of dynamic part Pdus 414 of 2090 Document ID
    63: AUTOSAR_CP_TPS_SystemTemplate System Template AUTOSAR CP R23-11 6.5.1
    I-Pdu Multiplexer in System Extract/ECU Extract The processing in the ECU
    determines the description of MultiplexedIPdus in the System Extract/Ecu
    Extract. In case that a Gateway ECU only routes a Multi- plexedIPdu without
    being interested in the content leads to a reduced description in the System
    Extract/ECU Extract. The following items describe the different scenar- ios
    and the consequences for the System Extract/ECU Extract description. A
    complete System Description contains all information. [TPS_SYST_01080]
    Sending or receiving of a MultiplexedIPdu in System Ex- tract/ECU Extract
    (cid:100) • all attributes of the MultiplexedIPdu are mandatory • aggregated
    DynamicPart with associated ISignalIPdus is mandatory in case – of sending –
    of receiving if at least one DynamicPartAlternative is received by one Ecu
    of the Extract. • a PduTriggering shall be defined for the MultiplexedIPdu •
    a PduTriggering shall be defined for all included ISignalIPdus in the Dy-
    namicPart and StaticPart (cid:99)() The initial ECU Configuration Generator
    configures COM, PduR, IpduM and lower lay- ers with the information from the
    System Extract/ECU Extract. [TPS_SYST_01081] Gatewaying of a MultiplexedIPdu
    in System Extract/ECU Extract (cid:100) • StaticPart and DynamicPart
    definitions shall be omitted, thus no ISig- nalIPdu description shall be
    included • all attributes of the MultiplexedIPdu shall be omitted. • a
    PduTriggering shall be defined only for the gatewayed MultiplexedIPdu • an
    IPduMapping between the source and the target PduTriggerings shall be
    defined (cid:99)() The initial ECU Configuration Generator configures PduR
    and lower layers with the information from the System Extract/ECU Extract.
    [TPS_SYST_01082] Receiving and gatewaying of a MultiplexedIPdu in System
    Extract/ECU Extract (cid:100) • all attributes of the MultiplexedIPdu are
    mandatory 415 of 2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate System
    Template AUTOSAR CP R23-11 • aggregated DynamicPart with associated
    ISignalIPdus is mandatory in case at least one DynamicPartAlternative is
    received by one Ecu of the Extract. • a PduTriggering shall be defined for
    the MultiplexedIPdu • an IPduMapping between the source and the target
    PduTriggerings shall be defined • a PduTriggering shall be defined for all
    included ISignalIPdus in the Dy- namicPart and StaticPart (cid:99)() The
    initial ECU Configuration Generator configures Com, PduR, IpduM and lower
    lay- ers with the information from the System Extract/ECU Extract. 416 of
    2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate System Template AUTOSAR
    CP R23-11 6.6 Frames Identifiable PhysicalChannel Identifiable
    FrameTriggering FibexElement Frame + frameLength: Integer [0..1]
    Identifiable «atpPrototype» FibexElement PduToFrameMapping
    UploadableDesignElement Pdu + packingByteOrder: ByteOrderEnum [0..1] +
    startPosition: Integer [0..1] + hasDynamicLength: Boolean [0..1] +
    updateIndicationBitPosition: Integer [0..1] + length: UnlimitedInteger
    [0..1] (cid:1) (cid:16) (cid:4) (cid:23) (cid:14) (cid:2) (cid:17) (cid:8)
    (cid:24) (cid:3) (cid:4) (cid:18) (cid:19) (cid:14) (cid:23) (cid:5) (cid:2)
    (cid:3) (cid:3) (cid:21) (cid:3) (cid:18) (cid:29) (cid:20) (cid:26)
    (cid:30) (cid:2) (cid:25) (cid:6) (cid:7) (cid:2) (cid:14) (cid:3) (cid:21)
    (cid:7) (cid:19) (cid:22) (cid:14) (cid:20) (cid:1) (cid:16) (cid:4) (cid:3)
    (cid:7) (cid:3) (cid:6) (cid:2) (cid:17) (cid:8) (cid:7) (cid:8) (cid:9)
    (cid:7) (cid:27) (cid:3) (cid:4) (cid:18) (cid:19) (cid:14) (cid:9) (cid:22)
    (cid:3) (cid:2) (cid:3) (cid:7) (cid:12) (cid:5) (cid:3) (cid:21) (cid:10)
    (cid:9) (cid:20) (cid:8) (cid:2) (cid:25) (cid:12) (cid:13) (cid:28) (cid:6)
    (cid:7) (cid:14) (cid:3) (cid:7) (cid:19) (cid:2) (cid:12) (cid:3) (cid:2)
    (cid:21) (cid:22) (cid:13) (cid:7) (cid:23) (cid:2) (cid:9) (cid:3) (cid:7)
    (cid:8) (cid:7) (cid:9) (cid:14) (cid:15) (cid:20) (cid:22) (cid:9) (cid:22)
    (cid:2) (cid:10) (cid:7) (cid:9) (cid:24) (cid:6) (cid:22) (cid:12) (cid:13)
    (cid:2) (cid:12) (cid:13) (cid:7) (cid:23) (cid:14) (cid:15) (cid:20)
    (cid:24) +managedPhysicalChannel 0..* «atpVariation,atpSplitable»
    +frameTriggering 0..* +frame 0..1 «atpVariation,atpSplitable»
    +pduToFrameMapping 0..* +pdu 0..1 Figure 6.29: Frame Overview (FibexCore:
    FrameOverview) [TPS_SYST_01083] Frame (cid:100)A Frame represents a general
    design object that is used to describe the layout of the included Pdus as a
    reusable asset.(cid:99)() [TPS_SYST_01084] FrameTriggering (cid:100)The
    FrameTriggering implements the reusable definition of a Frame within a
    concrete context and thus defines a Frame’s send behavior and identification
    on a certain PhysicalChannel.(cid:99)() [TPS_SYST_02255] Frame.frameLength
    usage for FlexrayFrames and Can- Frames (cid:100)The frameLength for a
    FlexrayFrame shall be equal or larger than the combined length of all Pdus
    that are mapped to the frame. The frameLength for a CanFrame is used to
    describe the minimum length of a re- ceived L-PDU to be accepted by a data
    length check. Therefore, it is possible to configure a frameLength which is
    smaller than the mapped Pdu to this frame. If data length check is not
    needed the frameLength of a CanFrame may be left unde- fined. The reason for
    that is that if the CanFrame.frameLength is larger than the Pdu.length of
    the mapped Pdu and data length check is used, a received Pdu will always be
    discarded due to a failing minimum length check.(cid:99)() 417 of 2090
    Document ID 63: AUTOSAR_CP_TPS_SystemTemplate System Template AUTOSAR CP
    R23-11
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::SegmentPosition
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 412, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute defines the order of the bytes of the and the packing into the
                # MultiplexedIPdu.
        # that [constr_3247] and [constr_3224] are usage of this attribute.
        self._segmentByte: Optional["ByteOrderEnum"] = None

    @property
    def segment_byte(self) -> Optional["ByteOrderEnum"]:
        """Get segmentByte (Pythonic accessor)."""
        return self._segmentByte

    @segment_byte.setter
    def segment_byte(self, value: Optional["ByteOrderEnum"]) -> None:
        """
        Set segmentByte with validation.
        
        Args:
            value: The segmentByte to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._segmentByte = None
            return

        if not isinstance(value, ByteOrderEnum):
            raise TypeError(
                f"segmentByte must be ByteOrderEnum or None, got {type(value).__name__}"
            )
        self._segmentByte = value
        # Data Length of the segment in bits.
        self._segmentLength: Optional["Integer"] = None

    @property
    def segment_length(self) -> Optional["Integer"]:
        """Get segmentLength (Pythonic accessor)."""
        return self._segmentLength

    @segment_length.setter
    def segment_length(self, value: Optional["Integer"]) -> None:
        """
        Set segmentLength with validation.
        
        Args:
            value: The segmentLength to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._segmentLength = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"segmentLength must be Integer or int or None, got {type(value).__name__}"
            )
        self._segmentLength = value
        # Segments bit position relatively to the beginning of a IPdu.
        self._segment: Optional["Integer"] = None

    @property
    def segment(self) -> Optional["Integer"]:
        """Get segment (Pythonic accessor)."""
        return self._segment

    @segment.setter
    def segment(self, value: Optional["Integer"]) -> None:
        """
        Set segment with validation.
        
        Args:
            value: The segment to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._segment = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"segment must be Integer or int or None, got {type(value).__name__}"
            )
        self._segment = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSegmentByte(self) -> "ByteOrderEnum":
        """
        AUTOSAR-compliant getter for segmentByte.
        
        Returns:
            The segmentByte value
        
        Note:
            Delegates to segment_byte property (CODING_RULE_V2_00017)
        """
        return self.segment_byte  # Delegates to property

    def setSegmentByte(self, value: "ByteOrderEnum") -> SegmentPosition:
        """
        AUTOSAR-compliant setter for segmentByte with method chaining.
        
        Args:
            value: The segmentByte to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to segment_byte property setter (gets validation automatically)
        """
        self.segment_byte = value  # Delegates to property setter
        return self

    def getSegmentLength(self) -> "Integer":
        """
        AUTOSAR-compliant getter for segmentLength.
        
        Returns:
            The segmentLength value
        
        Note:
            Delegates to segment_length property (CODING_RULE_V2_00017)
        """
        return self.segment_length  # Delegates to property

    def setSegmentLength(self, value: "Integer") -> SegmentPosition:
        """
        AUTOSAR-compliant setter for segmentLength with method chaining.
        
        Args:
            value: The segmentLength to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to segment_length property setter (gets validation automatically)
        """
        self.segment_length = value  # Delegates to property setter
        return self

    def getSegment(self) -> "Integer":
        """
        AUTOSAR-compliant getter for segment.
        
        Returns:
            The segment value
        
        Note:
            Delegates to segment property (CODING_RULE_V2_00017)
        """
        return self.segment  # Delegates to property

    def setSegment(self, value: "Integer") -> SegmentPosition:
        """
        AUTOSAR-compliant setter for segment with method chaining.
        
        Args:
            value: The segment to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to segment property setter (gets validation automatically)
        """
        self.segment = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_segment_byte(self, value: Optional["ByteOrderEnum"]) -> SegmentPosition:
        """
        Set segmentByte and return self for chaining.
        
        Args:
            value: The segmentByte to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_segment_byte("value")
        """
        self.segment_byte = value  # Use property setter (gets validation)
        return self

    def with_segment_length(self, value: Optional["Integer"]) -> SegmentPosition:
        """
        Set segmentLength and return self for chaining.
        
        Args:
            value: The segmentLength to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_segment_length("value")
        """
        self.segment_length = value  # Use property setter (gets validation)
        return self

    def with_segment(self, value: Optional["Integer"]) -> SegmentPosition:
        """
        Set segment and return self for chaining.
        
        Args:
            value: The segment to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_segment("value")
        """
        self.segment = value  # Use property setter (gets validation)
        return self



class NmPdu(Pdu):
    """
    Network Management Pdu
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::NmPdu
    
    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 302, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 342, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This optional aggregation is used to describe NmUser that is transmitted in
                # the NmPdu.
        # The counting of starts at the beginning of the NmPdu Cbv or Nid are used.
        self._iSignalToIPdu: List["RefType"] = []

    @property
    def i_signal_to_i_pdu(self) -> List["RefType"]:
        """Get iSignalToIPdu (Pythonic accessor)."""
        return self._iSignalToIPdu
        # Defines if the Pdu contains NM Data.
        # If the NmPdu does aggregate any ISignalToIPduMappings it still may that is
                # set via Nm_SetUserData().
        # If the then the nmDataInformation be ignored.
        self._nmData: Optional["Boolean"] = None

    @property
    def nm_data(self) -> Optional["Boolean"]:
        """Get nmData (Pythonic accessor)."""
        return self._nmData

    @nm_data.setter
    def nm_data(self, value: Optional["Boolean"]) -> None:
        """
        Set nmData with validation.
        
        Args:
            value: The nmData to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nmData = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"nmData must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._nmData = value
        # Defines if the Pdu contains NM Vote information.
        self._nmVoteInformation: Optional["Boolean"] = None

    @property
    def nm_vote_information(self) -> Optional["Boolean"]:
        """Get nmVoteInformation (Pythonic accessor)."""
        return self._nmVoteInformation

    @nm_vote_information.setter
    def nm_vote_information(self, value: Optional["Boolean"]) -> None:
        """
        Set nmVoteInformation with validation.
        
        Args:
            value: The nmVoteInformation to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._nmVoteInformation = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"nmVoteInformation must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._nmVoteInformation = value
        # AUTOSAR COM is filling not used areas of an Pdu with bit-pattern.
        # This attribute can only be used if the nm is set to true.
        self._unusedBit: Optional["Integer"] = None

    @property
    def unused_bit(self) -> Optional["Integer"]:
        """Get unusedBit (Pythonic accessor)."""
        return self._unusedBit

    @unused_bit.setter
    def unused_bit(self, value: Optional["Integer"]) -> None:
        """
        Set unusedBit with validation.
        
        Args:
            value: The unusedBit to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._unusedBit = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"unusedBit must be Integer or int or None, got {type(value).__name__}"
            )
        self._unusedBit = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getISignalToIPdu(self) -> List["RefType"]:
        """
        AUTOSAR-compliant getter for iSignalToIPdu.
        
        Returns:
            The iSignalToIPdu value
        
        Note:
            Delegates to i_signal_to_i_pdu property (CODING_RULE_V2_00017)
        """
        return self.i_signal_to_i_pdu  # Delegates to property

    def getNmData(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for nmData.
        
        Returns:
            The nmData value
        
        Note:
            Delegates to nm_data property (CODING_RULE_V2_00017)
        """
        return self.nm_data  # Delegates to property

    def setNmData(self, value: "Boolean") -> NmPdu:
        """
        AUTOSAR-compliant setter for nmData with method chaining.
        
        Args:
            value: The nmData to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to nm_data property setter (gets validation automatically)
        """
        self.nm_data = value  # Delegates to property setter
        return self

    def getNmVoteInformation(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for nmVoteInformation.
        
        Returns:
            The nmVoteInformation value
        
        Note:
            Delegates to nm_vote_information property (CODING_RULE_V2_00017)
        """
        return self.nm_vote_information  # Delegates to property

    def setNmVoteInformation(self, value: "Boolean") -> NmPdu:
        """
        AUTOSAR-compliant setter for nmVoteInformation with method chaining.
        
        Args:
            value: The nmVoteInformation to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to nm_vote_information property setter (gets validation automatically)
        """
        self.nm_vote_information = value  # Delegates to property setter
        return self

    def getUnusedBit(self) -> "Integer":
        """
        AUTOSAR-compliant getter for unusedBit.
        
        Returns:
            The unusedBit value
        
        Note:
            Delegates to unused_bit property (CODING_RULE_V2_00017)
        """
        return self.unused_bit  # Delegates to property

    def setUnusedBit(self, value: "Integer") -> NmPdu:
        """
        AUTOSAR-compliant setter for unusedBit with method chaining.
        
        Args:
            value: The unusedBit to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to unused_bit property setter (gets validation automatically)
        """
        self.unused_bit = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_nm_data(self, value: Optional["Boolean"]) -> NmPdu:
        """
        Set nmData and return self for chaining.
        
        Args:
            value: The nmData to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_nm_data("value")
        """
        self.nm_data = value  # Use property setter (gets validation)
        return self

    def with_nm_vote_information(self, value: Optional["Boolean"]) -> NmPdu:
        """
        Set nmVoteInformation and return self for chaining.
        
        Args:
            value: The nmVoteInformation to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_nm_vote_information("value")
        """
        self.nm_vote_information = value  # Use property setter (gets validation)
        return self

    def with_unused_bit(self, value: Optional["Integer"]) -> NmPdu:
        """
        Set unusedBit and return self for chaining.
        
        Args:
            value: The unusedBit to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_unused_bit("value")
        """
        self.unused_bit = value  # Use property setter (gets validation)
        return self



class UserDefinedPdu(Pdu):
    """
    UserDefinedPdu allows to describe PDU-based communication over Complex
    Drivers. If a new BSW module is added above the BusIf (e.g. a new Nm module)
    then this Pdu element shall be used to describe the communication.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::UserDefinedPdu
    
    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 314, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 345, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute defines the CDD that transmits or receives If several CDDs are
        # defined this used to distinguish between them.
        self._cddType: Optional["String"] = None

    @property
    def cdd_type(self) -> Optional["String"]:
        """Get cddType (Pythonic accessor)."""
        return self._cddType

    @cdd_type.setter
    def cdd_type(self, value: Optional["String"]) -> None:
        """
        Set cddType with validation.
        
        Args:
            value: The cddType to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._cddType = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"cddType must be String or str or None, got {type(value).__name__}"
            )
        self._cddType = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCddType(self) -> "String":
        """
        AUTOSAR-compliant getter for cddType.
        
        Returns:
            The cddType value
        
        Note:
            Delegates to cdd_type property (CODING_RULE_V2_00017)
        """
        return self.cdd_type  # Delegates to property

    def setCddType(self, value: "String") -> UserDefinedPdu:
        """
        AUTOSAR-compliant setter for cddType with method chaining.
        
        Args:
            value: The cddType to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to cdd_type property setter (gets validation automatically)
        """
        self.cdd_type = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_cdd_type(self, value: Optional["String"]) -> UserDefinedPdu:
        """
        Set cddType and return self for chaining.
        
        Args:
            value: The cddType to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_cdd_type("value")
        """
        self.cdd_type = value  # Use property setter (gets validation)
        return self



class IPdu(Pdu, ABC):
    """
    The IPdu (Interaction Layer Protocol Data Unit) element is used to sum up
    all Pdus that are routed by the PduR.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::IPdu
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 341, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 226, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is IPdu:
            raise TypeError("IPdu is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines whether this IPdu may be collected inside a.
        self._containedIPdu: Optional[ContainedIPduProps] = None

    @property
    def contained_i_pdu(self) -> Optional[ContainedIPduProps]:
        """Get containedIPdu (Pythonic accessor)."""
        return self._containedIPdu

    @contained_i_pdu.setter
    def contained_i_pdu(self, value: Optional[ContainedIPduProps]) -> None:
        """
        Set containedIPdu with validation.
        
        Args:
            value: The containedIPdu to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._containedIPdu = None
            return

        if not isinstance(value, ContainedIPduProps):
            raise TypeError(
                f"containedIPdu must be ContainedIPduProps or None, got {type(value).__name__}"
            )
        self._containedIPdu = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getContainedIPdu(self) -> ContainedIPduProps:
        """
        AUTOSAR-compliant getter for containedIPdu.
        
        Returns:
            The containedIPdu value
        
        Note:
            Delegates to contained_i_pdu property (CODING_RULE_V2_00017)
        """
        return self.contained_i_pdu  # Delegates to property

    def setContainedIPdu(self, value: ContainedIPduProps) -> IPdu:
        """
        AUTOSAR-compliant setter for containedIPdu with method chaining.
        
        Args:
            value: The containedIPdu to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to contained_i_pdu property setter (gets validation automatically)
        """
        self.contained_i_pdu = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_contained_i_pdu(self, value: Optional[ContainedIPduProps]) -> IPdu:
        """
        Set containedIPdu and return self for chaining.
        
        Args:
            value: The containedIPdu to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_contained_i_pdu("value")
        """
        self.contained_i_pdu = value  # Use property setter (gets validation)
        return self



class GeneralPurposePdu(Pdu):
    """
    This element is used for AUTOSAR Pdus without additional attributes that are
    routed by a bus interface. Please note that the category name of such Pdus
    is standardized in the AUTOSAR System Template.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::GeneralPurposePdu
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 344, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class StaticPart(MultiplexedPart):
    """
    Some parts/signals of the I-PDU may be the same regardless of the selector
    field. Such a part is called static part. The static part is optional.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::StaticPart
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 410, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to a Com IPdu which is routed to the IPduM is combined to a
        # multiplexedPdu.
        self._iPdu: Optional[ISignalIPdu] = None

    @property
    def i_pdu(self) -> Optional[ISignalIPdu]:
        """Get iPdu (Pythonic accessor)."""
        return self._iPdu

    @i_pdu.setter
    def i_pdu(self, value: Optional[ISignalIPdu]) -> None:
        """
        Set iPdu with validation.
        
        Args:
            value: The iPdu to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._iPdu = None
            return

        if not isinstance(value, ISignalIPdu):
            raise TypeError(
                f"iPdu must be ISignalIPdu or None, got {type(value).__name__}"
            )
        self._iPdu = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getIPdu(self) -> ISignalIPdu:
        """
        AUTOSAR-compliant getter for iPdu.
        
        Returns:
            The iPdu value
        
        Note:
            Delegates to i_pdu property (CODING_RULE_V2_00017)
        """
        return self.i_pdu  # Delegates to property

    def setIPdu(self, value: ISignalIPdu) -> StaticPart:
        """
        AUTOSAR-compliant setter for iPdu with method chaining.
        
        Args:
            value: The iPdu to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to i_pdu property setter (gets validation automatically)
        """
        self.i_pdu = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_i_pdu(self, value: Optional[ISignalIPdu]) -> StaticPart:
        """
        Set iPdu and return self for chaining.
        
        Args:
            value: The iPdu to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_i_pdu("value")
        """
        self.i_pdu = value  # Use property setter (gets validation)
        return self



class DynamicPart(MultiplexedPart):
    """
    Dynamic part of a multiplexed I-Pdu. Reserved space which is used to
    transport varying SignalIPdus at the same position, controlled by the
    corresponding selectorFieldCode.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::DynamicPart
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 410, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Com IPdu alternatives that are transmitted in the Dynamic of the
        # MultiplexedIPdu.
        self._dynamicPart: List[DynamicPartAlternative] = []

    @property
    def dynamic_part(self) -> List[DynamicPartAlternative]:
        """Get dynamicPart (Pythonic accessor)."""
        return self._dynamicPart

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDynamicPart(self) -> List[DynamicPartAlternative]:
        """
        AUTOSAR-compliant getter for dynamicPart.
        
        Returns:
            The dynamicPart value
        
        Note:
            Delegates to dynamic_part property (CODING_RULE_V2_00017)
        """
        return self.dynamic_part  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class J1939DcmIPdu(IPdu):
    """
    Represents the IPdus handled by J1939Dcm.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::J1939DcmIPdu
    
    Sources:
      - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (Page 321, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 344, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute is used to identify the actual DMx message,.
        self._diagnostic: Optional["PositiveInteger"] = None

    @property
    def diagnostic(self) -> Optional["PositiveInteger"]:
        """Get diagnostic (Pythonic accessor)."""
        return self._diagnostic

    @diagnostic.setter
    def diagnostic(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set diagnostic with validation.
        
        Args:
            value: The diagnostic to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._diagnostic = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"diagnostic must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._diagnostic = value
        self._MessageType: "e.g" = None

    @property
    def message_type(self) -> "e.g":
        """Get MessageType (Pythonic accessor)."""
        return self._MessageType

    @message_type.setter
    def message_type(self, value: "e.g") -> None:
        """
        Set MessageType with validation.
        
        Args:
            value: The MessageType to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, e.g):
            raise TypeError(
                f"MessageType must be e.g, got {type(value).__name__}"
            )
        self._MessageType = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDiagnostic(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for diagnostic.
        
        Returns:
            The diagnostic value
        
        Note:
            Delegates to diagnostic property (CODING_RULE_V2_00017)
        """
        return self.diagnostic  # Delegates to property

    def setDiagnostic(self, value: "PositiveInteger") -> J1939DcmIPdu:
        """
        AUTOSAR-compliant setter for diagnostic with method chaining.
        
        Args:
            value: The diagnostic to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to diagnostic property setter (gets validation automatically)
        """
        self.diagnostic = value  # Delegates to property setter
        return self

    def getMessageType(self) -> "e.g":
        """
        AUTOSAR-compliant getter for MessageType.
        
        Returns:
            The MessageType value
        
        Note:
            Delegates to message_type property (CODING_RULE_V2_00017)
        """
        return self.message_type  # Delegates to property

    def setMessageType(self, value: "e.g") -> J1939DcmIPdu:
        """
        AUTOSAR-compliant setter for MessageType with method chaining.
        
        Args:
            value: The MessageType to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to message_type property setter (gets validation automatically)
        """
        self.message_type = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_diagnostic(self, value: Optional["PositiveInteger"]) -> J1939DcmIPdu:
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

    def with_message_type(self, value: "e.g") -> J1939DcmIPdu:
        """
        Set MessageType and return self for chaining.
        
        Args:
            value: The MessageType to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_message_type("value")
        """
        self.message_type = value  # Use property setter (gets validation)
        return self



class NPdu(IPdu):
    """
    This is a Pdu of the Transport Layer. The main purpose of the TP Layer is to
    segment and reassemble IPdus.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::NPdu
    
    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 301, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 343, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class ISignalIPdu(IPdu):
    """
    Represents the IPdus handled by Com. The ISignalIPdu assembled and
    disassembled in AUTOSAR COM consists of one or more signals. In case no
    multiplexing is performed this IPdu is routed to/from the Interface Layer. A
    maximum of one dynamic length signal per IPdu is allowed.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::ISignalIPdu
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 994, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 342, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Timing specification for Com IPdus (Transmission This information is
                # mandatory for the sender in a This information may be omitted on a System
                # Extract.
        # timing of a Pdu can vary.
        # atpVariation 1228 Document ID 62: AUTOSAR_CP_TPS_SoftwareComponentTemplate
                # Template R23-11.
        self._iPduTiming: Optional[IPduTiming] = None

    @property
    def i_pdu_timing(self) -> Optional[IPduTiming]:
        """Get iPduTiming (Pythonic accessor)."""
        return self._iPduTiming

    @i_pdu_timing.setter
    def i_pdu_timing(self, value: Optional[IPduTiming]) -> None:
        """
        Set iPduTiming with validation.
        
        Args:
            value: The iPduTiming to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._iPduTiming = None
            return

        if not isinstance(value, IPduTiming):
            raise TypeError(
                f"iPduTiming must be IPduTiming or None, got {type(value).__name__}"
            )
        self._iPduTiming = value
        # Definition of SignalToIPduMappings included in the Signal content of a PDU
                # can be variable.
        # atpVariation.
        self._iSignalToPdu: List["RefType"] = []

    @property
    def i_signal_to_pdu(self) -> List["RefType"]:
        """Get iSignalToPdu (Pythonic accessor)."""
        return self._iSignalToPdu
        # AUTOSAR COM and AUTOSAR IPDUM are filling not areas of an IPDU with this
                # bit-pattern.
        # This attribute to avoid undefined behavior.
        # This be repeated throughout the IPdu.
        self._unusedBit: Optional["Integer"] = None

    @property
    def unused_bit(self) -> Optional["Integer"]:
        """Get unusedBit (Pythonic accessor)."""
        return self._unusedBit

    @unused_bit.setter
    def unused_bit(self, value: Optional["Integer"]) -> None:
        """
        Set unusedBit with validation.
        
        Args:
            value: The unusedBit to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._unusedBit = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"unusedBit must be Integer or int or None, got {type(value).__name__}"
            )
        self._unusedBit = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getIPduTiming(self) -> IPduTiming:
        """
        AUTOSAR-compliant getter for iPduTiming.
        
        Returns:
            The iPduTiming value
        
        Note:
            Delegates to i_pdu_timing property (CODING_RULE_V2_00017)
        """
        return self.i_pdu_timing  # Delegates to property

    def setIPduTiming(self, value: IPduTiming) -> ISignalIPdu:
        """
        AUTOSAR-compliant setter for iPduTiming with method chaining.
        
        Args:
            value: The iPduTiming to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to i_pdu_timing property setter (gets validation automatically)
        """
        self.i_pdu_timing = value  # Delegates to property setter
        return self

    def getISignalToPdu(self) -> List["RefType"]:
        """
        AUTOSAR-compliant getter for iSignalToPdu.
        
        Returns:
            The iSignalToPdu value
        
        Note:
            Delegates to i_signal_to_pdu property (CODING_RULE_V2_00017)
        """
        return self.i_signal_to_pdu  # Delegates to property

    def getUnusedBit(self) -> "Integer":
        """
        AUTOSAR-compliant getter for unusedBit.
        
        Returns:
            The unusedBit value
        
        Note:
            Delegates to unused_bit property (CODING_RULE_V2_00017)
        """
        return self.unused_bit  # Delegates to property

    def setUnusedBit(self, value: "Integer") -> ISignalIPdu:
        """
        AUTOSAR-compliant setter for unusedBit with method chaining.
        
        Args:
            value: The unusedBit to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to unused_bit property setter (gets validation automatically)
        """
        self.unused_bit = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_i_pdu_timing(self, value: Optional[IPduTiming]) -> ISignalIPdu:
        """
        Set iPduTiming and return self for chaining.
        
        Args:
            value: The iPduTiming to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_i_pdu_timing("value")
        """
        self.i_pdu_timing = value  # Use property setter (gets validation)
        return self

    def with_unused_bit(self, value: Optional["Integer"]) -> ISignalIPdu:
        """
        Set unusedBit and return self for chaining.
        
        Args:
            value: The unusedBit to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_unused_bit("value")
        """
        self.unused_bit = value  # Use property setter (gets validation)
        return self



class DcmIPdu(IPdu):
    """
    Represents the IPdus handled by Dcm.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::DcmIPdu
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 343, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Attribute is used to distinguish a request from a response.
        self._diagPduType: Optional[DiagPduType] = None

    @property
    def diag_pdu_type(self) -> Optional[DiagPduType]:
        """Get diagPduType (Pythonic accessor)."""
        return self._diagPduType

    @diag_pdu_type.setter
    def diag_pdu_type(self, value: Optional[DiagPduType]) -> None:
        """
        Set diagPduType with validation.
        
        Args:
            value: The diagPduType to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._diagPduType = None
            return

        if not isinstance(value, DiagPduType):
            raise TypeError(
                f"diagPduType must be DiagPduType or None, got {type(value).__name__}"
            )
        self._diagPduType = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDiagPduType(self) -> DiagPduType:
        """
        AUTOSAR-compliant getter for diagPduType.
        
        Returns:
            The diagPduType value
        
        Note:
            Delegates to diag_pdu_type property (CODING_RULE_V2_00017)
        """
        return self.diag_pdu_type  # Delegates to property

    def setDiagPduType(self, value: DiagPduType) -> DcmIPdu:
        """
        AUTOSAR-compliant setter for diagPduType with method chaining.
        
        Args:
            value: The diagPduType to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to diag_pdu_type property setter (gets validation automatically)
        """
        self.diag_pdu_type = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_diag_pdu_type(self, value: Optional[DiagPduType]) -> DcmIPdu:
        """
        Set diagPduType and return self for chaining.
        
        Args:
            value: The diagPduType to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_diag_pdu_type("value")
        """
        self.diag_pdu_type = value  # Use property setter (gets validation)
        return self



class GeneralPurposeIPdu(IPdu):
    """
    This element is used for AUTOSAR Pdus without attributes that are routed by
    the PduR. Please note that the category name of such Pdus is standardized in
    the AUTOSAR System Template.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::GeneralPurposeIPdu
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 345, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (Page 60, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class UserDefinedIPdu(IPdu):
    """
    UserDefinedIPdu allows to describe PDU-based communication over Complex
    Drivers. If a new BSW module is added above the PduR (e.g. a Diagnostic
    Service ) then this IPdu element shall be used to describe the
    communication.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::UserDefinedIPdu
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 346, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute defines the CDD that transmits or receives If several CDDs are
        # defined this used to distinguish between them.
        self._cddType: Optional["String"] = None

    @property
    def cdd_type(self) -> Optional["String"]:
        """Get cddType (Pythonic accessor)."""
        return self._cddType

    @cdd_type.setter
    def cdd_type(self, value: Optional["String"]) -> None:
        """
        Set cddType with validation.
        
        Args:
            value: The cddType to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._cddType = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"cddType must be String or str or None, got {type(value).__name__}"
            )
        self._cddType = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCddType(self) -> "String":
        """
        AUTOSAR-compliant getter for cddType.
        
        Returns:
            The cddType value
        
        Note:
            Delegates to cdd_type property (CODING_RULE_V2_00017)
        """
        return self.cdd_type  # Delegates to property

    def setCddType(self, value: "String") -> UserDefinedIPdu:
        """
        AUTOSAR-compliant setter for cddType with method chaining.
        
        Args:
            value: The cddType to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to cdd_type property setter (gets validation automatically)
        """
        self.cdd_type = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_cdd_type(self, value: Optional["String"]) -> UserDefinedIPdu:
        """
        Set cddType and return self for chaining.
        
        Args:
            value: The cddType to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_cdd_type("value")
        """
        self.cdd_type = value  # Use property setter (gets validation)
        return self



class ContainerIPdu(IPdu):
    """
    Allows to collect several IPdus in one ContainerIPdu based on the
    headerType.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::ContainerIPdu
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 353, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines properties for an IPdu that is part of the.
        self._containedIPdu: List[ContainedIPduProps] = []

    @property
    def contained_i_pdu(self) -> List[ContainedIPduProps]:
        """Get containedIPdu (Pythonic accessor)."""
        return self._containedIPdu
        # This PduTriggering shall be collected inside the Container 2090 Document ID
        # 63: AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._containedPdu: List["RefType"] = []

    @property
    def contained_pdu(self) -> List["RefType"]:
        """Get containedPdu (Pythonic accessor)."""
        return self._containedPdu
        # When this timeout expires the ContainerIPdu is sent out.
        # respective timer is started when the first Ipdu is put ContainerIPdu.
        # This attribute is ignored on.
        self._container: Optional["TimeValue"] = None

    @property
    def container(self) -> Optional["TimeValue"]:
        """Get container (Pythonic accessor)."""
        return self._container

    @container.setter
    def container(self, value: Optional["TimeValue"]) -> None:
        """
        Set container with validation.
        
        Args:
            value: The container to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._container = None
            return

        if not isinstance(value, TimeValue):
            raise TypeError(
                f"container must be TimeValue or None, got {type(value).__name__}"
            )
        self._container = value
        # Defines if the transmission of the ContainerIPdu shall be right after the
        # first ContainedIPdu was put into attribute shall be ignored on receiver side.
        self._containerTrigger: Optional["RefType"] = None

    @property
    def container_trigger(self) -> Optional["RefType"]:
        """Get containerTrigger (Pythonic accessor)."""
        return self._containerTrigger

    @container_trigger.setter
    def container_trigger(self, value: Optional["RefType"]) -> None:
        """
        Set containerTrigger with validation.
        
        Args:
            value: The containerTrigger to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._containerTrigger = None
            return

        self._containerTrigger = value
        # Defines whether and which header type is used (header and length).
        self._headerType: Optional["ContainerIPduHeader"] = None

    @property
    def header_type(self) -> Optional["ContainerIPduHeader"]:
        """Get headerType (Pythonic accessor)."""
        return self._headerType

    @header_type.setter
    def header_type(self, value: Optional["ContainerIPduHeader"]) -> None:
        """
        Set headerType with validation.
        
        Args:
            value: The headerType to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._headerType = None
            return

        if not isinstance(value, ContainerIPduHeader):
            raise TypeError(
                f"headerType must be ContainerIPduHeader or None, got {type(value).__name__}"
            )
        self._headerType = value
        # This attribute defines the minimum queue size for containers.
        self._minimumRx: Optional["PositiveInteger"] = None

    @property
    def minimum_rx(self) -> Optional["PositiveInteger"]:
        """Get minimumRx (Pythonic accessor)."""
        return self._minimumRx

    @minimum_rx.setter
    def minimum_rx(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set minimumRx with validation.
        
        Args:
            value: The minimumRx to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._minimumRx = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"minimumRx must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._minimumRx = value
        # This attribute defines the minimum queue size for containers.
        self._minimumTx: Optional["PositiveInteger"] = None

    @property
    def minimum_tx(self) -> Optional["PositiveInteger"]:
        """Get minimumTx (Pythonic accessor)."""
        return self._minimumTx

    @minimum_tx.setter
    def minimum_tx(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set minimumTx with validation.
        
        Args:
            value: The minimumTx to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._minimumTx = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"minimumTx must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._minimumTx = value
        # Defines whether this ContainerIPdu has a fixed set of containedIPdus assigned
        # for reception.
        self._rxAccept: Optional["RxAcceptContainedI"] = None

    @property
    def rx_accept(self) -> Optional["RxAcceptContainedI"]:
        """Get rxAccept (Pythonic accessor)."""
        return self._rxAccept

    @rx_accept.setter
    def rx_accept(self, value: Optional["RxAcceptContainedI"]) -> None:
        """
        Set rxAccept with validation.
        
        Args:
            value: The rxAccept to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._rxAccept = None
            return

        if not isinstance(value, RxAcceptContainedI):
            raise TypeError(
                f"rxAccept must be RxAcceptContainedI or None, got {type(value).__name__}"
            )
        self._rxAccept = value
        # Defines the size threshold which, when exceeded, sending of the ContainerIPdu
                # although the size has not been reached yet.
        # Unit: byte.
        self._thresholdSize: Optional["PositiveInteger"] = None

    @property
    def threshold_size(self) -> Optional["PositiveInteger"]:
        """Get thresholdSize (Pythonic accessor)."""
        return self._thresholdSize

    @threshold_size.setter
    def threshold_size(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set thresholdSize with validation.
        
        Args:
            value: The thresholdSize to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._thresholdSize = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"thresholdSize must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._thresholdSize = value
        # IPduM fills not updated areas of the ContainerPdu with byte-pattern.
        self._unusedBit: Optional["PositiveInteger"] = None

    @property
    def unused_bit(self) -> Optional["PositiveInteger"]:
        """Get unusedBit (Pythonic accessor)."""
        return self._unusedBit

    @unused_bit.setter
    def unused_bit(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set unusedBit with validation.
        
        Args:
            value: The unusedBit to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._unusedBit = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"unusedBit must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._unusedBit = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getContainedIPdu(self) -> List[ContainedIPduProps]:
        """
        AUTOSAR-compliant getter for containedIPdu.
        
        Returns:
            The containedIPdu value
        
        Note:
            Delegates to contained_i_pdu property (CODING_RULE_V2_00017)
        """
        return self.contained_i_pdu  # Delegates to property

    def getContainedPdu(self) -> List["RefType"]:
        """
        AUTOSAR-compliant getter for containedPdu.
        
        Returns:
            The containedPdu value
        
        Note:
            Delegates to contained_pdu property (CODING_RULE_V2_00017)
        """
        return self.contained_pdu  # Delegates to property

    def getContainer(self) -> "TimeValue":
        """
        AUTOSAR-compliant getter for container.
        
        Returns:
            The container value
        
        Note:
            Delegates to container property (CODING_RULE_V2_00017)
        """
        return self.container  # Delegates to property

    def setContainer(self, value: "TimeValue") -> ContainerIPdu:
        """
        AUTOSAR-compliant setter for container with method chaining.
        
        Args:
            value: The container to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to container property setter (gets validation automatically)
        """
        self.container = value  # Delegates to property setter
        return self

    def getContainerTrigger(self) -> "RefType":
        """
        AUTOSAR-compliant getter for containerTrigger.
        
        Returns:
            The containerTrigger value
        
        Note:
            Delegates to container_trigger property (CODING_RULE_V2_00017)
        """
        return self.container_trigger  # Delegates to property

    def setContainerTrigger(self, value: "RefType") -> ContainerIPdu:
        """
        AUTOSAR-compliant setter for containerTrigger with method chaining.
        
        Args:
            value: The containerTrigger to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to container_trigger property setter (gets validation automatically)
        """
        self.container_trigger = value  # Delegates to property setter
        return self

    def getHeaderType(self) -> "ContainerIPduHeader":
        """
        AUTOSAR-compliant getter for headerType.
        
        Returns:
            The headerType value
        
        Note:
            Delegates to header_type property (CODING_RULE_V2_00017)
        """
        return self.header_type  # Delegates to property

    def setHeaderType(self, value: "ContainerIPduHeader") -> ContainerIPdu:
        """
        AUTOSAR-compliant setter for headerType with method chaining.
        
        Args:
            value: The headerType to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to header_type property setter (gets validation automatically)
        """
        self.header_type = value  # Delegates to property setter
        return self

    def getMinimumRx(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for minimumRx.
        
        Returns:
            The minimumRx value
        
        Note:
            Delegates to minimum_rx property (CODING_RULE_V2_00017)
        """
        return self.minimum_rx  # Delegates to property

    def setMinimumRx(self, value: "PositiveInteger") -> ContainerIPdu:
        """
        AUTOSAR-compliant setter for minimumRx with method chaining.
        
        Args:
            value: The minimumRx to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to minimum_rx property setter (gets validation automatically)
        """
        self.minimum_rx = value  # Delegates to property setter
        return self

    def getMinimumTx(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for minimumTx.
        
        Returns:
            The minimumTx value
        
        Note:
            Delegates to minimum_tx property (CODING_RULE_V2_00017)
        """
        return self.minimum_tx  # Delegates to property

    def setMinimumTx(self, value: "PositiveInteger") -> ContainerIPdu:
        """
        AUTOSAR-compliant setter for minimumTx with method chaining.
        
        Args:
            value: The minimumTx to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to minimum_tx property setter (gets validation automatically)
        """
        self.minimum_tx = value  # Delegates to property setter
        return self

    def getRxAccept(self) -> "RxAcceptContainedI":
        """
        AUTOSAR-compliant getter for rxAccept.
        
        Returns:
            The rxAccept value
        
        Note:
            Delegates to rx_accept property (CODING_RULE_V2_00017)
        """
        return self.rx_accept  # Delegates to property

    def setRxAccept(self, value: "RxAcceptContainedI") -> ContainerIPdu:
        """
        AUTOSAR-compliant setter for rxAccept with method chaining.
        
        Args:
            value: The rxAccept to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to rx_accept property setter (gets validation automatically)
        """
        self.rx_accept = value  # Delegates to property setter
        return self

    def getThresholdSize(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for thresholdSize.
        
        Returns:
            The thresholdSize value
        
        Note:
            Delegates to threshold_size property (CODING_RULE_V2_00017)
        """
        return self.threshold_size  # Delegates to property

    def setThresholdSize(self, value: "PositiveInteger") -> ContainerIPdu:
        """
        AUTOSAR-compliant setter for thresholdSize with method chaining.
        
        Args:
            value: The thresholdSize to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to threshold_size property setter (gets validation automatically)
        """
        self.threshold_size = value  # Delegates to property setter
        return self

    def getUnusedBit(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for unusedBit.
        
        Returns:
            The unusedBit value
        
        Note:
            Delegates to unused_bit property (CODING_RULE_V2_00017)
        """
        return self.unused_bit  # Delegates to property

    def setUnusedBit(self, value: "PositiveInteger") -> ContainerIPdu:
        """
        AUTOSAR-compliant setter for unusedBit with method chaining.
        
        Args:
            value: The unusedBit to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to unused_bit property setter (gets validation automatically)
        """
        self.unused_bit = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_container(self, value: Optional["TimeValue"]) -> ContainerIPdu:
        """
        Set container and return self for chaining.
        
        Args:
            value: The container to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_container("value")
        """
        self.container = value  # Use property setter (gets validation)
        return self

    def with_container_trigger(self, value: Optional[RefType]) -> ContainerIPdu:
        """
        Set containerTrigger and return self for chaining.
        
        Args:
            value: The containerTrigger to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_container_trigger("value")
        """
        self.container_trigger = value  # Use property setter (gets validation)
        return self

    def with_header_type(self, value: Optional["ContainerIPduHeader"]) -> ContainerIPdu:
        """
        Set headerType and return self for chaining.
        
        Args:
            value: The headerType to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_header_type("value")
        """
        self.header_type = value  # Use property setter (gets validation)
        return self

    def with_minimum_rx(self, value: Optional["PositiveInteger"]) -> ContainerIPdu:
        """
        Set minimumRx and return self for chaining.
        
        Args:
            value: The minimumRx to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_minimum_rx("value")
        """
        self.minimum_rx = value  # Use property setter (gets validation)
        return self

    def with_minimum_tx(self, value: Optional["PositiveInteger"]) -> ContainerIPdu:
        """
        Set minimumTx and return self for chaining.
        
        Args:
            value: The minimumTx to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_minimum_tx("value")
        """
        self.minimum_tx = value  # Use property setter (gets validation)
        return self

    def with_rx_accept(self, value: Optional["RxAcceptContainedI"]) -> ContainerIPdu:
        """
        Set rxAccept and return self for chaining.
        
        Args:
            value: The rxAccept to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_rx_accept("value")
        """
        self.rx_accept = value  # Use property setter (gets validation)
        return self

    def with_threshold_size(self, value: Optional["PositiveInteger"]) -> ContainerIPdu:
        """
        Set thresholdSize and return self for chaining.
        
        Args:
            value: The thresholdSize to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_threshold_size("value")
        """
        self.threshold_size = value  # Use property setter (gets validation)
        return self

    def with_unused_bit(self, value: Optional["PositiveInteger"]) -> ContainerIPdu:
        """
        Set unusedBit and return self for chaining.
        
        Args:
            value: The unusedBit to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_unused_bit("value")
        """
        self.unused_bit = value  # Use property setter (gets validation)
        return self



class SecuredIPdu(IPdu):
    """
    If useAsCryptographicPdu is not set or set to false this IPdu contains the
    payload of an Authentic IPdu supplemented by additional Authentication
    Information (Freshness Counter and an Authenticator). If
    useAsCryptographicPdu is set to true this IPdu contains the Authenticator
    for a payload that is transported in a separate message. The separate
    Authentic IPdu is described by the Pdu that is referenced with the payload
    reference from this SecuredIPdu.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::SecuredIPdu
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 367, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to authentication properties that are valid for this SecuredIPdu.
        self._authentication: Optional["SecureCommunication"] = None

    @property
    def authentication(self) -> Optional["SecureCommunication"]:
        """Get authentication (Pythonic accessor)."""
        return self._authentication

    @authentication.setter
    def authentication(self, value: Optional["SecureCommunication"]) -> None:
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

        if not isinstance(value, SecureCommunication):
            raise TypeError(
                f"authentication must be SecureCommunication or None, got {type(value).__name__}"
            )
        self._authentication = value
        # Defines whether the length information for handling this with SecuredIPdu.
        # useSecuredPdu is taken from the configuration or from provided length
                # information during runtime.
        # length information is taken from the length information during runtime.
        # length information is taken from the.
        self._dynamic: Optional["Boolean"] = None

    @property
    def dynamic(self) -> Optional["Boolean"]:
        """Get dynamic (Pythonic accessor)."""
        return self._dynamic

    @dynamic.setter
    def dynamic(self, value: Optional["Boolean"]) -> None:
        """
        Set dynamic with validation.
        
        Args:
            value: The dynamic to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dynamic = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"dynamic must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._dynamic = value
        # Reference to freshness properties that are valid for this.
        self._freshnessProps: Optional["SecureCommunication"] = None

    @property
    def freshness_props(self) -> Optional["SecureCommunication"]:
        """Get freshnessProps (Pythonic accessor)."""
        return self._freshnessProps

    @freshness_props.setter
    def freshness_props(self, value: Optional["SecureCommunication"]) -> None:
        """
        Set freshnessProps with validation.
        
        Args:
            value: The freshnessProps to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._freshnessProps = None
            return

        if not isinstance(value, SecureCommunication):
            raise TypeError(
                f"freshnessProps must be SecureCommunication or None, got {type(value).__name__}"
            )
        self._freshnessProps = value
        # Reference to a Pdu that will be protected against and replay attacks.
        self._payload: Optional["RefType"] = None

    @property
    def payload(self) -> Optional["RefType"]:
        """Get payload (Pythonic accessor)."""
        return self._payload

    @payload.setter
    def payload(self, value: Optional["RefType"]) -> None:
        """
        Set payload with validation.
        
        Args:
            value: The payload to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._payload = None
            return

        self._payload = value
        # Specific configuration properties for this SecuredIPdu.
        self._secure: Optional["SecureCommunication"] = None

    @property
    def secure(self) -> Optional["SecureCommunication"]:
        """Get secure (Pythonic accessor)."""
        return self._secure

    @secure.setter
    def secure(self, value: Optional["SecureCommunication"]) -> None:
        """
        Set secure with validation.
        
        Args:
            value: The secure to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._secure = None
            return

        if not isinstance(value, SecureCommunication):
            raise TypeError(
                f"secure must be SecureCommunication or None, got {type(value).__name__}"
            )
        self._secure = value
        # If this attribute is set to true the SecuredIPdu contains the Information for
                # an AuthenticIPdu that is in a separate message.
        # The AuthenticIPdu original payload, i.
        # e.
        # the secured data.
        # attribute is set to false this SecuredIPdu contains of an Authentic IPdu
                # supplemented by Information.
        self._useAs: Optional["Boolean"] = None

    @property
    def use_as(self) -> Optional["Boolean"]:
        """Get useAs (Pythonic accessor)."""
        return self._useAs

    @use_as.setter
    def use_as(self, value: Optional["Boolean"]) -> None:
        """
        Set useAs with validation.
        
        Args:
            value: The useAs to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._useAs = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"useAs must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._useAs = value
        # This attribute defines the size of the header which is inserted into the
                # SecuredIPdu.
        # If this attribute is set to noHeader, the SecuredIPdu contains the Header to
                # indicate the length of the AuthenticIPdu contains the original the secured
                # data.
        self._useSecuredPdu: Optional["SecuredPduHeader"] = None

    @property
    def use_secured_pdu(self) -> Optional["SecuredPduHeader"]:
        """Get useSecuredPdu (Pythonic accessor)."""
        return self._useSecuredPdu

    @use_secured_pdu.setter
    def use_secured_pdu(self, value: Optional["SecuredPduHeader"]) -> None:
        """
        Set useSecuredPdu with validation.
        
        Args:
            value: The useSecuredPdu to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._useSecuredPdu = None
            return

        if not isinstance(value, SecuredPduHeader):
            raise TypeError(
                f"useSecuredPdu must be SecuredPduHeader or None, got {type(value).__name__}"
            )
        self._useSecuredPdu = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAuthentication(self) -> "SecureCommunication":
        """
        AUTOSAR-compliant getter for authentication.
        
        Returns:
            The authentication value
        
        Note:
            Delegates to authentication property (CODING_RULE_V2_00017)
        """
        return self.authentication  # Delegates to property

    def setAuthentication(self, value: "SecureCommunication") -> SecuredIPdu:
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

    def getDynamic(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for dynamic.
        
        Returns:
            The dynamic value
        
        Note:
            Delegates to dynamic property (CODING_RULE_V2_00017)
        """
        return self.dynamic  # Delegates to property

    def setDynamic(self, value: "Boolean") -> SecuredIPdu:
        """
        AUTOSAR-compliant setter for dynamic with method chaining.
        
        Args:
            value: The dynamic to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to dynamic property setter (gets validation automatically)
        """
        self.dynamic = value  # Delegates to property setter
        return self

    def getFreshnessProps(self) -> "SecureCommunication":
        """
        AUTOSAR-compliant getter for freshnessProps.
        
        Returns:
            The freshnessProps value
        
        Note:
            Delegates to freshness_props property (CODING_RULE_V2_00017)
        """
        return self.freshness_props  # Delegates to property

    def setFreshnessProps(self, value: "SecureCommunication") -> SecuredIPdu:
        """
        AUTOSAR-compliant setter for freshnessProps with method chaining.
        
        Args:
            value: The freshnessProps to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to freshness_props property setter (gets validation automatically)
        """
        self.freshness_props = value  # Delegates to property setter
        return self

    def getPayload(self) -> "RefType":
        """
        AUTOSAR-compliant getter for payload.
        
        Returns:
            The payload value
        
        Note:
            Delegates to payload property (CODING_RULE_V2_00017)
        """
        return self.payload  # Delegates to property

    def setPayload(self, value: "RefType") -> SecuredIPdu:
        """
        AUTOSAR-compliant setter for payload with method chaining.
        
        Args:
            value: The payload to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to payload property setter (gets validation automatically)
        """
        self.payload = value  # Delegates to property setter
        return self

    def getSecure(self) -> "SecureCommunication":
        """
        AUTOSAR-compliant getter for secure.
        
        Returns:
            The secure value
        
        Note:
            Delegates to secure property (CODING_RULE_V2_00017)
        """
        return self.secure  # Delegates to property

    def setSecure(self, value: "SecureCommunication") -> SecuredIPdu:
        """
        AUTOSAR-compliant setter for secure with method chaining.
        
        Args:
            value: The secure to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to secure property setter (gets validation automatically)
        """
        self.secure = value  # Delegates to property setter
        return self

    def getUseAs(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for useAs.
        
        Returns:
            The useAs value
        
        Note:
            Delegates to use_as property (CODING_RULE_V2_00017)
        """
        return self.use_as  # Delegates to property

    def setUseAs(self, value: "Boolean") -> SecuredIPdu:
        """
        AUTOSAR-compliant setter for useAs with method chaining.
        
        Args:
            value: The useAs to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to use_as property setter (gets validation automatically)
        """
        self.use_as = value  # Delegates to property setter
        return self

    def getUseSecuredPdu(self) -> "SecuredPduHeader":
        """
        AUTOSAR-compliant getter for useSecuredPdu.
        
        Returns:
            The useSecuredPdu value
        
        Note:
            Delegates to use_secured_pdu property (CODING_RULE_V2_00017)
        """
        return self.use_secured_pdu  # Delegates to property

    def setUseSecuredPdu(self, value: "SecuredPduHeader") -> SecuredIPdu:
        """
        AUTOSAR-compliant setter for useSecuredPdu with method chaining.
        
        Args:
            value: The useSecuredPdu to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to use_secured_pdu property setter (gets validation automatically)
        """
        self.use_secured_pdu = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_authentication(self, value: Optional["SecureCommunication"]) -> SecuredIPdu:
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

    def with_dynamic(self, value: Optional["Boolean"]) -> SecuredIPdu:
        """
        Set dynamic and return self for chaining.
        
        Args:
            value: The dynamic to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_dynamic("value")
        """
        self.dynamic = value  # Use property setter (gets validation)
        return self

    def with_freshness_props(self, value: Optional["SecureCommunication"]) -> SecuredIPdu:
        """
        Set freshnessProps and return self for chaining.
        
        Args:
            value: The freshnessProps to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_freshness_props("value")
        """
        self.freshness_props = value  # Use property setter (gets validation)
        return self

    def with_payload(self, value: Optional[RefType]) -> SecuredIPdu:
        """
        Set payload and return self for chaining.
        
        Args:
            value: The payload to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_payload("value")
        """
        self.payload = value  # Use property setter (gets validation)
        return self

    def with_secure(self, value: Optional["SecureCommunication"]) -> SecuredIPdu:
        """
        Set secure and return self for chaining.
        
        Args:
            value: The secure to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_secure("value")
        """
        self.secure = value  # Use property setter (gets validation)
        return self

    def with_use_as(self, value: Optional["Boolean"]) -> SecuredIPdu:
        """
        Set useAs and return self for chaining.
        
        Args:
            value: The useAs to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_use_as("value")
        """
        self.use_as = value  # Use property setter (gets validation)
        return self

    def with_use_secured_pdu(self, value: Optional["SecuredPduHeader"]) -> SecuredIPdu:
        """
        Set useSecuredPdu and return self for chaining.
        
        Args:
            value: The useSecuredPdu to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_use_secured_pdu("value")
        """
        self.use_secured_pdu = value  # Use property setter (gets validation)
        return self



class MultiplexedIPdu(IPdu):
    """
    that the absolute position of the selectorField in the MultiplexedIPdu is
    determined by the definition of the selectorFieldByteOrder attribute of the
    Multiplexed Pdu. If Big Endian is specified, the start position indicates
    the bit position of the most significant bit in the IPdu. If Little Endian
    is specified, the start position indicates the bit position of the least
    significant bit in the IPdu. In AUTOSAR the bit counting is always set to
    "sawtooth" and the bit order is set to "Decreasing". The bit counting in
    byte 0 starts with bit 0 (least significant bit). The most significant bit
    in byte 0 is bit 7. In a complete System Description this attribute is
    mandatory. If a MultiplexedPdu is received by a Pdu Gateway and is not
    delivered to the IPduM but routed directly to a bus interface then the
    content of the MulitplexedPdu doesn’t need to be described in the System
    Extract/Ecu Extract. To support this use case the multiplicity is set to
    0..1. staticPart StaticPart 0..1 aggr The static part of the multiplexed
    IPdu is the same regardless of the selector field. The static part is
    optional. atpVariation: Content of a multiplexed PDU can vary. Stereotypes:
    atpSplitable; atpVariation , staticPart.variationPoint.short Label
    vh.latestBindingTime=postBuild triggerMode TriggerMode 0..1 attr IPduM can
    be configured to send a transmission request for the new multiplexed IPdu to
    the PDU-Router because of the trigger conditions/ modes that are described
    in the TriggerMode enumeration. In a complete System Description this
    attribute is mandatory. If a MultiplexedPdu is received by a Pdu Gateway and
    is not delivered to the IPduM but routed directly to a bus interface then
    the content of the MulitplexedPdu doesn’t need to be described in the System
    Extract/Ecu Extract. To support this use case the multiplicity is set to
    0..1. (cid:53) 409 of 2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate
    System Template AUTOSAR CP R23-11 (cid:52)
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication::MultiplexedIPdu
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 408, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # According to the value of the selector field some parts of have a different
                # layout.
        # In a complete System MultiplexedIPdu shall contain a Dynamic following use
                # cases support the multiplicity to a MultiplexedIPdu is received by a Pdu
                # Gateway and delivered to the IPduM but routed directly to a then the content
                # of the MulitplexedIPdu to be described in the System Extract/ a
                # MultiplexedIPdu is received by an ECU which is in the static part of the
                # MultiplexedIPdu dynamicPart does not need to be described in Extract/Ecu
                # Extract.
        # of a multiplexed PDU can vary.
        # atpVariation 2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._dynamicPart: Optional[DynamicPart] = None

    @property
    def dynamic_part(self) -> Optional[DynamicPart]:
        """Get dynamicPart (Pythonic accessor)."""
        return self._dynamicPart

    @dynamic_part.setter
    def dynamic_part(self, value: Optional[DynamicPart]) -> None:
        """
        Set dynamicPart with validation.
        
        Args:
            value: The dynamicPart to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dynamicPart = None
            return

        if not isinstance(value, DynamicPart):
            raise TypeError(
                f"dynamicPart must be DynamicPart or None, got {type(value).__name__}"
            )
        self._dynamicPart = value
        # This parameter is necessary to describe the position of selector field within
        # the IPdu.
        self._selectorField: Optional["Integer"] = None

    @property
    def selector_field(self) -> Optional["Integer"]:
        """Get selectorField (Pythonic accessor)."""
        return self._selectorField

    @selector_field.setter
    def selector_field(self, value: Optional["Integer"]) -> None:
        """
        Set selectorField with validation.
        
        Args:
            value: The selectorField to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._selectorField = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"selectorField must be Integer or int or None, got {type(value).__name__}"
            )
        self._selectorField = value
        # AUTOSAR COM and AUTOSAR IPDUM are filling not areas of an IPdu with this
                # bit-pattern.
        # This attribute to avoid undefined behavior.
        # This be repeated throughout the IPdu.
        # complete System Description this attribute is a MultiplexedPdu is received by
                # a Pdu is not delivered to the IPduM but routed a bus interface then the
                # content of the need to be described in the Extract.
        # To support this use case the set to 0.
        # 1.
        self._unusedBit: Optional["Integer"] = None

    @property
    def unused_bit(self) -> Optional["Integer"]:
        """Get unusedBit (Pythonic accessor)."""
        return self._unusedBit

    @unused_bit.setter
    def unused_bit(self, value: Optional["Integer"]) -> None:
        """
        Set unusedBit with validation.
        
        Args:
            value: The unusedBit to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._unusedBit = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"unusedBit must be Integer or int or None, got {type(value).__name__}"
            )
        self._unusedBit = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDynamicPart(self) -> DynamicPart:
        """
        AUTOSAR-compliant getter for dynamicPart.
        
        Returns:
            The dynamicPart value
        
        Note:
            Delegates to dynamic_part property (CODING_RULE_V2_00017)
        """
        return self.dynamic_part  # Delegates to property

    def setDynamicPart(self, value: DynamicPart) -> MultiplexedIPdu:
        """
        AUTOSAR-compliant setter for dynamicPart with method chaining.
        
        Args:
            value: The dynamicPart to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to dynamic_part property setter (gets validation automatically)
        """
        self.dynamic_part = value  # Delegates to property setter
        return self

    def getSelectorField(self) -> "Integer":
        """
        AUTOSAR-compliant getter for selectorField.
        
        Returns:
            The selectorField value
        
        Note:
            Delegates to selector_field property (CODING_RULE_V2_00017)
        """
        return self.selector_field  # Delegates to property

    def setSelectorField(self, value: "Integer") -> MultiplexedIPdu:
        """
        AUTOSAR-compliant setter for selectorField with method chaining.
        
        Args:
            value: The selectorField to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to selector_field property setter (gets validation automatically)
        """
        self.selector_field = value  # Delegates to property setter
        return self

    def getUnusedBit(self) -> "Integer":
        """
        AUTOSAR-compliant getter for unusedBit.
        
        Returns:
            The unusedBit value
        
        Note:
            Delegates to unused_bit property (CODING_RULE_V2_00017)
        """
        return self.unused_bit  # Delegates to property

    def setUnusedBit(self, value: "Integer") -> MultiplexedIPdu:
        """
        AUTOSAR-compliant setter for unusedBit with method chaining.
        
        Args:
            value: The unusedBit to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to unused_bit property setter (gets validation automatically)
        """
        self.unused_bit = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_dynamic_part(self, value: Optional[DynamicPart]) -> MultiplexedIPdu:
        """
        Set dynamicPart and return self for chaining.
        
        Args:
            value: The dynamicPart to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_dynamic_part("value")
        """
        self.dynamic_part = value  # Use property setter (gets validation)
        return self

    def with_selector_field(self, value: Optional["Integer"]) -> MultiplexedIPdu:
        """
        Set selectorField and return self for chaining.
        
        Args:
            value: The selectorField to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_selector_field("value")
        """
        self.selector_field = value  # Use property setter (gets validation)
        return self

    def with_unused_bit(self, value: Optional["Integer"]) -> MultiplexedIPdu:
        """
        Set unusedBit and return self for chaining.
        
        Args:
            value: The unusedBit to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_unused_bit("value")
        """
        self.unused_bit = value  # Use property setter (gets validation)
        return self


class IPduSignalProcessingEnum(AREnum):
    """
    IPduSignalProcessingEnum enumeration

Definition of signal processing modes. Aggregated by IPduPort.iPduSignalProcessing

Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication
    """
    # The signal indications / confirmations are deferred.
    deferred = "0"

    # The signal indications / confirmations are performed.
    immediate = "1"



class ISignalTypeEnum(AREnum):
    """
    ISignalTypeEnum enumeration

This enumeration defines ISignal types that are used for derivation of the ComSignalType in the COM configuration. Aggregated by ISignal.iSignalType

Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication
    """
    # ISignal shall be interpreted as an array (UINT8_N, UINT8_DYN)
    array = "0"

    # ISignal shall be interpreted as a primitive type (e.g. UINT_8, SINT_32)
    primitive = "1"



class TransferPropertyEnum(AREnum):
    """
    TransferPropertyEnum enumeration

Transfer Properties of a Signal. Aggregated by ISignalToIPduMapping.transferProperty

Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication
    """
    # If the signal has the TransferProperty pending, then the function Com_SendSignal shall not perform a transmission of the IPdu associated with the signal.
    pending = "0"

    # The signal in the assigned IPdu is updated and a request for the IPdu’s transmission is made.
    triggered = "1"

    # The signal in the assigned IPdu is updated and a request for the IPdus transmission is made only if the signal value is different from the already stored signal value.
    triggeredOnChange = "2"

    # The signal in the assigned IPdu is updated and a request for the IPdus transmission is made only if WithoutRepetition the signal value is different from the already stored signal value. In the DIRECT/N-TIMES or MIXED transmission mode (EventControlledTiming) the IPdu will be transmitted just once without a
    triggeredOnChange = "3"

    # The signal in the assigned IPdu is updated and a request for the IPdu’s transmission is made. In the
    triggeredWithout = "None"

    # DIRECT/N-TIMES or MIXED transmission mode (EventControlledTiming) the IPdu will be transmitted just once without a repetition, independent of the defined NumberOfRepeats.
    Repetition = "4"



class DiagPduType(AREnum):
    """
    DiagPduType enumeration

Used to distinguish a diagnostic request from a response. Aggregated by DcmIPdu.diagPduType

Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication
    """
    # Diagnostic Request
    diagRequest = "0"

    # Diagnostic Response
    diagResponse = "1"



class CommunicationDirectionType(AREnum):
    """
    CommunicationDirectionType enumeration

Describes the communication direction. Aggregated by CommConnectorPort.communicationDirection, IEEE1722TpConnection.communicationDirection, IP SecRule.direction, ISignalIPduGroup.communicationDirection

Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication
    """
    # Reception (Input)
    in = "0"

    # Transmission (Output)
    out = "1"



class ContainerIPduTriggerEnum(AREnum):
    """
    ContainerIPduTriggerEnum enumeration

Defines when the transmission of the ContainerIPdu shall be requested. Aggregated by ContainerIPdu.containerTrigger

Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication
    """
    # Defines that the transmission of the ContainerIPdu shall be requested when the default trigger conditions apply (e.g. timeout of threshold).
    defaultTrigger = "0"

    # Defines that the transmission of the ContainerIPdu shall be requested right after the first Contained
    firstContained = "None"

    # IPdu was put into the ContainerIPdu.
    Trigger = "1"



class ContainerIPduHeaderTypeEnum(AREnum):
    """
    ContainerIPduHeaderTypeEnum enumeration

Is used to define the header type and size of ContainerIPdus. The header size includes the header id and the length information. Aggregated by ContainerIPdu.headerType

Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication
    """
    # Header size is 64 bit:
    longHeader = "0"

    # No Header is used and the location of each containedPdu in the ContainerPdu is statically configured.
    noHeader = "2"

    # Header size is 32 bit:
    shortHeader = "1"



class RxAcceptContainedIPduEnum(AREnum):
    """
    RxAcceptContainedIPduEnum enumeration

Defines whether this ContainerIPdu has a fixed set of containedIPdus assigned for reception. Aggregated by ContainerIPdu.rxAcceptContainedIPdu

Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication
    """
    # No fixed set of containedIPdus is defined for reception, any known containedIPdu (based on header
    acceptAll = "0"

    # A fixed set of containedIPdus is defined for reception. Only these assigned containedIPdus (based on ContainerIPdu this containedIPdu is discarded.
    acceptConfigured = "1"



class ContainedIPduCollectionSemanticsEnum(AREnum):
    """
    ContainedIPduCollectionSemanticsEnum enumeration

Defines the collection semantics for ContainedIPdus. Aggregated by ContainedIPduProps.collectionSemantics

Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication
    """
    # The ContainedIPdu data will be fetched via TriggerTransmit just before the transmission executes.
    lastIsBest = "0"

    # The ContainedIPdu data will instantly be stored to the ContainerIPdu in the context of the Transmit
    queued = "1"



class SecuredPduHeaderEnum(AREnum):
    """
    SecuredPduHeaderEnum enumeration

Defines the header which will be inserted into the SecuredIPdu. Aggregated by SecuredIPdu.useSecuredPduHeader

Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication
    """
    # No header included in the SecuredPdu.
    noHeader = "0"

    # Template
    System = "None"

    # CP R23-11
    AUTOSARsecuredPduHeader08Bit = "1"

    # 16 Bit Secured I-PDU Header included in the Secured I-PDU.
    securedPduHeader16Bit = "2"

    # 32 Bit Secured I-PDU Header included in the Secured I-PDU.
    securedPduHeader32Bit = "3"



class TriggerMode(AREnum):
    """
    TriggerMode enumeration

IPduM can be configured to send a transmission request for the new multiplexed I-PDU to the PDU-Router because of conditions/ modes. Aggregated by MultiplexedIPdu.triggerMode

Package: M2::AUTOSARTemplates::SystemTemplate::Fibex::FibexCore::CoreCommunication
    """
    # IPduM sends a transmission request to the PduR if a dynamic part is received.
    dynamicPartTrigger = "0"

    # IPduM does not trigger transmission because of receiving anything of this IPdu in case of Trigger
    none = "1"

    # IPduM sends a transmission request to the PduR if a static or dynamic part is received.
    staticOrDynamicPartTrigger = "2"

    # IPduM sends a transmission request to the PduR if a static part is received.
    staticPartTrigger = "3"


__all__ = [
    ISignal,
    ISignalIPduGroup,
    SystemSignal,
    Frame,
    FrameTriggering,
    Pdu,
    PduTriggering,
    ISignalGroup,
    FramePort,
    IPduPort,
    ISignalPort,
    ISignalProps,
    SystemSignalGroup,
    ISignalToIPduMapping,
    ISignalTriggering,
    PduToFrameMapping,
    IPduTiming,
    PdurIPduGroup,
    ContainedIPduProps,
    SecureCommunicationProps,
    SecureCommunicationPropsSet,
    SecureCommunicationFreshnessProps,
    SecureCommunicationAuthenticationProps,
    DynamicPartAlternative,
    MultiplexedPart,
    SegmentPosition,
    NmPdu,
    UserDefinedPdu,
    IPdu,
    GeneralPurposePdu,
    StaticPart,
    DynamicPart,
    J1939DcmIPdu,
    NPdu,
    ISignalIPdu,
    DcmIPdu,
    GeneralPurposeIPdu,
    UserDefinedIPdu,
    ContainerIPdu,
    SecuredIPdu,
    MultiplexedIPdu,
    IPduSignalProcessingEnum,
    ISignalTypeEnum,
    TransferPropertyEnum,
    DiagPduType,
    CommunicationDirectionType,
    ContainerIPduTriggerEnum,
    ContainerIPduHeaderTypeEnum,
    RxAcceptContainedIPduEnum,
    ContainedIPduCollectionSemanticsEnum,
    SecuredPduHeaderEnum,
    TriggerMode,
]

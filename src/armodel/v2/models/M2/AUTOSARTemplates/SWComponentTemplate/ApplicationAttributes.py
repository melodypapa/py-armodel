"""
AUTOSAR Package - ApplicationAttributes

Package: M2::AUTOSARTemplates::SWComponentTemplate::ApplicationAttributes
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Float,
    RefType,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.GeneralAnnotation import (
    GeneralAnnotation,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
)




class SenderReceiverAnnotation(GeneralAnnotation, ABC):
    """
    Annotation of the data elements in a port that realizes a sender/receiver
    interface.
    
    Package: M2::AUTOSARTemplates::SWComponentTemplate::ApplicationAttributes::SenderReceiverAnnotation
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 152, Classic Platform
      R23-11)
    """
    def __init__(self):
        if type(self) is SenderReceiverAnnotation:
            raise TypeError("SenderReceiverAnnotation is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Flag whether this data element was not measured directly was calculated from
        # possibly several other calculated values.
        self._computed: Optional["Boolean"] = None

    @property
    def computed(self) -> Optional["Boolean"]:
        """Get computed (Pythonic accessor)."""
        return self._computed

    @computed.setter
    def computed(self, value: Optional["Boolean"]) -> None:
        """
        Set computed with validation.
        
        Args:
            value: The computed to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._computed = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"computed must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._computed = value
        # The instance of VariableDataPrototype annotated.
        self._dataElement: Optional["RefType"] = None

    @property
    def data_element(self) -> Optional["RefType"]:
        """Get dataElement (Pythonic accessor)."""
        return self._dataElement

    @data_element.setter
    def data_element(self, value: Optional["RefType"]) -> None:
        """
        Set dataElement with validation.
        
        Args:
            value: The dataElement to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dataElement = None
            return

        self._dataElement = value
        # This min or max has not to be mismatched with the min- for data-value in a
                # compu-method.
        # For example, shows when the result of the calculation a RunnableEntity owned
                # by one AtomicSw transmitted to another AtomicSw RunnableEntity will use this
                # value limit, e.
        # g.
        # the max.
        # power which can be used by that the current min.
        # slip.
        self._limitKind: Optional["DataLimitKindEnum"] = None

    @property
    def limit_kind(self) -> Optional["DataLimitKindEnum"]:
        """Get limitKind (Pythonic accessor)."""
        return self._limitKind

    @limit_kind.setter
    def limit_kind(self, value: Optional["DataLimitKindEnum"]) -> None:
        """
        Set limitKind with validation.
        
        Args:
            value: The limitKind to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._limitKind = None
            return

        if not isinstance(value, DataLimitKindEnum):
            raise TypeError(
                f"limitKind must be DataLimitKindEnum or None, got {type(value).__name__}"
            )
        self._limitKind = value
        # This attribute controls how data is processed according to values of
        # ProcessingKindEnum.
        self._processingKind: Optional["ProcessingKindEnum"] = None

    @property
    def processing_kind(self) -> Optional["ProcessingKindEnum"]:
        """Get processingKind (Pythonic accessor)."""
        return self._processingKind

    @processing_kind.setter
    def processing_kind(self, value: Optional["ProcessingKindEnum"]) -> None:
        """
        Set processingKind with validation.
        
        Args:
            value: The processingKind to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._processingKind = None
            return

        if not isinstance(value, ProcessingKindEnum):
            raise TypeError(
                f"processingKind must be ProcessingKindEnum or None, got {type(value).__name__}"
            )
        self._processingKind = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getComputed(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for computed.
        
        Returns:
            The computed value
        
        Note:
            Delegates to computed property (CODING_RULE_V2_00017)
        """
        return self.computed  # Delegates to property

    def setComputed(self, value: "Boolean") -> "SenderReceiverAnnotation":
        """
        AUTOSAR-compliant setter for computed with method chaining.
        
        Args:
            value: The computed to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to computed property setter (gets validation automatically)
        """
        self.computed = value  # Delegates to property setter
        return self

    def getDataElement(self) -> "RefType":
        """
        AUTOSAR-compliant getter for dataElement.
        
        Returns:
            The dataElement value
        
        Note:
            Delegates to data_element property (CODING_RULE_V2_00017)
        """
        return self.data_element  # Delegates to property

    def setDataElement(self, value: "RefType") -> "SenderReceiverAnnotation":
        """
        AUTOSAR-compliant setter for dataElement with method chaining.
        
        Args:
            value: The dataElement to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to data_element property setter (gets validation automatically)
        """
        self.data_element = value  # Delegates to property setter
        return self

    def getLimitKind(self) -> "DataLimitKindEnum":
        """
        AUTOSAR-compliant getter for limitKind.
        
        Returns:
            The limitKind value
        
        Note:
            Delegates to limit_kind property (CODING_RULE_V2_00017)
        """
        return self.limit_kind  # Delegates to property

    def setLimitKind(self, value: "DataLimitKindEnum") -> "SenderReceiverAnnotation":
        """
        AUTOSAR-compliant setter for limitKind with method chaining.
        
        Args:
            value: The limitKind to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to limit_kind property setter (gets validation automatically)
        """
        self.limit_kind = value  # Delegates to property setter
        return self

    def getProcessingKind(self) -> "ProcessingKindEnum":
        """
        AUTOSAR-compliant getter for processingKind.
        
        Returns:
            The processingKind value
        
        Note:
            Delegates to processing_kind property (CODING_RULE_V2_00017)
        """
        return self.processing_kind  # Delegates to property

    def setProcessingKind(self, value: "ProcessingKindEnum") -> "SenderReceiverAnnotation":
        """
        AUTOSAR-compliant setter for processingKind with method chaining.
        
        Args:
            value: The processingKind to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to processing_kind property setter (gets validation automatically)
        """
        self.processing_kind = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_computed(self, value: Optional["Boolean"]) -> "SenderReceiverAnnotation":
        """
        Set computed and return self for chaining.
        
        Args:
            value: The computed to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_computed("value")
        """
        self.computed = value  # Use property setter (gets validation)
        return self

    def with_data_element(self, value: Optional[RefType]) -> "SenderReceiverAnnotation":
        """
        Set dataElement and return self for chaining.
        
        Args:
            value: The dataElement to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_data_element("value")
        """
        self.data_element = value  # Use property setter (gets validation)
        return self

    def with_limit_kind(self, value: Optional["DataLimitKindEnum"]) -> "SenderReceiverAnnotation":
        """
        Set limitKind and return self for chaining.
        
        Args:
            value: The limitKind to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_limit_kind("value")
        """
        self.limit_kind = value  # Use property setter (gets validation)
        return self

    def with_processing_kind(self, value: Optional["ProcessingKindEnum"]) -> "SenderReceiverAnnotation":
        """
        Set processingKind and return self for chaining.
        
        Args:
            value: The processingKind to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_processing_kind("value")
        """
        self.processing_kind = value  # Use property setter (gets validation)
        return self



class ClientServerAnnotation(GeneralAnnotation):
    """
    Annotation to a port regarding a certain Operation.
    
    Package: M2::AUTOSARTemplates::SWComponentTemplate::ApplicationAttributes::ClientServerAnnotation
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 155, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the ClientServerOperation that the Client to.
        self._operation: Optional["ClientServerOperation"] = None

    @property
    def operation(self) -> Optional["ClientServerOperation"]:
        """Get operation (Pythonic accessor)."""
        return self._operation

    @operation.setter
    def operation(self, value: Optional["ClientServerOperation"]) -> None:
        """
        Set operation with validation.
        
        Args:
            value: The operation to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._operation = None
            return

        if not isinstance(value, ClientServerOperation):
            raise TypeError(
                f"operation must be ClientServerOperation or None, got {type(value).__name__}"
            )
        self._operation = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getOperation(self) -> "ClientServerOperation":
        """
        AUTOSAR-compliant getter for operation.
        
        Returns:
            The operation value
        
        Note:
            Delegates to operation property (CODING_RULE_V2_00017)
        """
        return self.operation  # Delegates to property

    def setOperation(self, value: "ClientServerOperation") -> "ClientServerAnnotation":
        """
        AUTOSAR-compliant setter for operation with method chaining.
        
        Args:
            value: The operation to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to operation property setter (gets validation automatically)
        """
        self.operation = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_operation(self, value: Optional["ClientServerOperation"]) -> "ClientServerAnnotation":
        """
        Set operation and return self for chaining.
        
        Args:
            value: The operation to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_operation("value")
        """
        self.operation = value  # Use property setter (gets validation)
        return self



class IoHwAbstractionServerAnnotation(GeneralAnnotation):
    """
    that the "server" in the name of this meta-class is not meant to restrict
    the usage to ClientServer Interfaces.
    
    Package: M2::AUTOSARTemplates::SWComponentTemplate::ApplicationAttributes::IoHwAbstractionServerAnnotation
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 156, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # In case of a SET operation, the age will be interpreted as in a GET operation
        # (input) it specifies the the signal within the IoHwAbstraction Layer.
        self._age: Optional["MultidimensionalTime"] = None

    @property
    def age(self) -> Optional["MultidimensionalTime"]:
        """Get age (Pythonic accessor)."""
        return self._age

    @age.setter
    def age(self, value: Optional["MultidimensionalTime"]) -> None:
        """
        Set age with validation.
        
        Args:
            value: The age to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._age = None
            return

        if not isinstance(value, MultidimensionalTime):
            raise TypeError(
                f"age must be MultidimensionalTime or None, got {type(value).__name__}"
            )
        self._age = value
        # Reference to the corresponding ArgumentDataPrototype.
        self._argument: Optional["RefType"] = None

    @property
    def argument(self) -> Optional["RefType"]:
        """Get argument (Pythonic accessor)."""
        return self._argument

    @argument.setter
    def argument(self, value: Optional["RefType"]) -> None:
        """
        Set argument with validation.
        
        Args:
            value: The argument to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._argument = None
            return

        self._argument = value
        # This value is determined by an appropriate combination range, the unit as
        # well as the data-elements type, (2ˆdatatypelength - 1).
        self._bswResolution: Optional["Float"] = None

    @property
    def bsw_resolution(self) -> Optional["Float"]:
        """Get bswResolution (Pythonic accessor)."""
        return self._bswResolution

    @bsw_resolution.setter
    def bsw_resolution(self, value: Optional["Float"]) -> None:
        """
        Set bswResolution with validation.
        
        Args:
            value: The bswResolution to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._bswResolution = None
            return

        if not isinstance(value, (Float, float)):
            raise TypeError(
                f"bswResolution must be Float or float or None, got {type(value).__name__}"
            )
        self._bswResolution = value
        # Reference to the corresponding VariableDataPrototype.
        self._dataElement: Optional["RefType"] = None

    @property
    def data_element(self) -> Optional["RefType"]:
        """Get dataElement (Pythonic accessor)."""
        return self._dataElement

    @data_element.setter
    def data_element(self, value: Optional["RefType"]) -> None:
        """
        Set dataElement with validation.
        
        Args:
            value: The dataElement to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dataElement = None
            return

        self._dataElement = value
        # This is only applicable in SET operations.
        # If it is enabled, IoHwAbstraction layer will monitor the result of the issue
                # an diagnostic signal.
        # This means an additional client-server port has to be can use this
                # information to cross-check each data-element in a SET operation with an
                # additional port is created port monitors a failure in the to be of the
                # IoHwAbstraction referenced port has to be another port of the or Sensor
                # Component.
        # 1228 Document ID 62: AUTOSAR_CP_TPS_SoftwareComponentTemplate Template
                # R23-11.
        self._failure: Optional["RefType"] = None

    @property
    def failure(self) -> Optional["RefType"]:
        """Get failure (Pythonic accessor)."""
        return self._failure

    @failure.setter
    def failure(self, value: Optional["RefType"]) -> None:
        """
        Set failure with validation.
        
        Args:
            value: The failure to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._failure = None
            return

        self._failure = value
        # This attribute is used to indicate what kind of filtering/ has been put to
        # the signal in the IoHw that no modification of the signal has This is the
        # default value debounceData the signal is a mean value waitTimeData the signal
        # is delivered by a GET operation certain amount of time.
        self._filtering: Optional["FilterDebouncingEnum"] = None

    @property
    def filtering(self) -> Optional["FilterDebouncingEnum"]:
        """Get filtering (Pythonic accessor)."""
        return self._filtering

    @filtering.setter
    def filtering(self, value: Optional["FilterDebouncingEnum"]) -> None:
        """
        Set filtering with validation.
        
        Args:
            value: The filtering to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._filtering = None
            return

        if not isinstance(value, FilterDebouncingEnum):
            raise TypeError(
                f"filtering must be FilterDebouncingEnum or None, got {type(value).__name__}"
            )
        self._filtering = value
        # This attribute indicates to the connected SensorActuator the
        # VariableDataPrototype used to generate pulse test sequences using the.
        self._pulseTest: Optional["PulseTestEnum"] = None

    @property
    def pulse_test(self) -> Optional["PulseTestEnum"]:
        """Get pulseTest (Pythonic accessor)."""
        return self._pulseTest

    @pulse_test.setter
    def pulse_test(self, value: Optional["PulseTestEnum"]) -> None:
        """
        Set pulseTest with validation.
        
        Args:
            value: The pulseTest to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._pulseTest = None
            return

        if not isinstance(value, PulseTestEnum):
            raise TypeError(
                f"pulseTest must be PulseTestEnum or None, got {type(value).__name__}"
            )
        self._pulseTest = value
        # Reference to the corresponding Trigger.
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

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAge(self) -> "MultidimensionalTime":
        """
        AUTOSAR-compliant getter for age.
        
        Returns:
            The age value
        
        Note:
            Delegates to age property (CODING_RULE_V2_00017)
        """
        return self.age  # Delegates to property

    def setAge(self, value: "MultidimensionalTime") -> "IoHwAbstractionServerAnnotation":
        """
        AUTOSAR-compliant setter for age with method chaining.
        
        Args:
            value: The age to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to age property setter (gets validation automatically)
        """
        self.age = value  # Delegates to property setter
        return self

    def getArgument(self) -> "RefType":
        """
        AUTOSAR-compliant getter for argument.
        
        Returns:
            The argument value
        
        Note:
            Delegates to argument property (CODING_RULE_V2_00017)
        """
        return self.argument  # Delegates to property

    def setArgument(self, value: "RefType") -> "IoHwAbstractionServerAnnotation":
        """
        AUTOSAR-compliant setter for argument with method chaining.
        
        Args:
            value: The argument to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to argument property setter (gets validation automatically)
        """
        self.argument = value  # Delegates to property setter
        return self

    def getBswResolution(self) -> "Float":
        """
        AUTOSAR-compliant getter for bswResolution.
        
        Returns:
            The bswResolution value
        
        Note:
            Delegates to bsw_resolution property (CODING_RULE_V2_00017)
        """
        return self.bsw_resolution  # Delegates to property

    def setBswResolution(self, value: "Float") -> "IoHwAbstractionServerAnnotation":
        """
        AUTOSAR-compliant setter for bswResolution with method chaining.
        
        Args:
            value: The bswResolution to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to bsw_resolution property setter (gets validation automatically)
        """
        self.bsw_resolution = value  # Delegates to property setter
        return self

    def getDataElement(self) -> "RefType":
        """
        AUTOSAR-compliant getter for dataElement.
        
        Returns:
            The dataElement value
        
        Note:
            Delegates to data_element property (CODING_RULE_V2_00017)
        """
        return self.data_element  # Delegates to property

    def setDataElement(self, value: "RefType") -> "IoHwAbstractionServerAnnotation":
        """
        AUTOSAR-compliant setter for dataElement with method chaining.
        
        Args:
            value: The dataElement to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to data_element property setter (gets validation automatically)
        """
        self.data_element = value  # Delegates to property setter
        return self

    def getFailure(self) -> "RefType":
        """
        AUTOSAR-compliant getter for failure.
        
        Returns:
            The failure value
        
        Note:
            Delegates to failure property (CODING_RULE_V2_00017)
        """
        return self.failure  # Delegates to property

    def setFailure(self, value: "RefType") -> "IoHwAbstractionServerAnnotation":
        """
        AUTOSAR-compliant setter for failure with method chaining.
        
        Args:
            value: The failure to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to failure property setter (gets validation automatically)
        """
        self.failure = value  # Delegates to property setter
        return self

    def getFiltering(self) -> "FilterDebouncingEnum":
        """
        AUTOSAR-compliant getter for filtering.
        
        Returns:
            The filtering value
        
        Note:
            Delegates to filtering property (CODING_RULE_V2_00017)
        """
        return self.filtering  # Delegates to property

    def setFiltering(self, value: "FilterDebouncingEnum") -> "IoHwAbstractionServerAnnotation":
        """
        AUTOSAR-compliant setter for filtering with method chaining.
        
        Args:
            value: The filtering to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to filtering property setter (gets validation automatically)
        """
        self.filtering = value  # Delegates to property setter
        return self

    def getPulseTest(self) -> "PulseTestEnum":
        """
        AUTOSAR-compliant getter for pulseTest.
        
        Returns:
            The pulseTest value
        
        Note:
            Delegates to pulse_test property (CODING_RULE_V2_00017)
        """
        return self.pulse_test  # Delegates to property

    def setPulseTest(self, value: "PulseTestEnum") -> "IoHwAbstractionServerAnnotation":
        """
        AUTOSAR-compliant setter for pulseTest with method chaining.
        
        Args:
            value: The pulseTest to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to pulse_test property setter (gets validation automatically)
        """
        self.pulse_test = value  # Delegates to property setter
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

    def setTrigger(self, value: "RefType") -> "IoHwAbstractionServerAnnotation":
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

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_age(self, value: Optional["MultidimensionalTime"]) -> "IoHwAbstractionServerAnnotation":
        """
        Set age and return self for chaining.
        
        Args:
            value: The age to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_age("value")
        """
        self.age = value  # Use property setter (gets validation)
        return self

    def with_argument(self, value: Optional[RefType]) -> "IoHwAbstractionServerAnnotation":
        """
        Set argument and return self for chaining.
        
        Args:
            value: The argument to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_argument("value")
        """
        self.argument = value  # Use property setter (gets validation)
        return self

    def with_bsw_resolution(self, value: Optional["Float"]) -> "IoHwAbstractionServerAnnotation":
        """
        Set bswResolution and return self for chaining.
        
        Args:
            value: The bswResolution to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_bsw_resolution("value")
        """
        self.bsw_resolution = value  # Use property setter (gets validation)
        return self

    def with_data_element(self, value: Optional[RefType]) -> "IoHwAbstractionServerAnnotation":
        """
        Set dataElement and return self for chaining.
        
        Args:
            value: The dataElement to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_data_element("value")
        """
        self.data_element = value  # Use property setter (gets validation)
        return self

    def with_failure(self, value: Optional[RefType]) -> "IoHwAbstractionServerAnnotation":
        """
        Set failure and return self for chaining.
        
        Args:
            value: The failure to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_failure("value")
        """
        self.failure = value  # Use property setter (gets validation)
        return self

    def with_filtering(self, value: Optional["FilterDebouncingEnum"]) -> "IoHwAbstractionServerAnnotation":
        """
        Set filtering and return self for chaining.
        
        Args:
            value: The filtering to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_filtering("value")
        """
        self.filtering = value  # Use property setter (gets validation)
        return self

    def with_pulse_test(self, value: Optional["PulseTestEnum"]) -> "IoHwAbstractionServerAnnotation":
        """
        Set pulseTest and return self for chaining.
        
        Args:
            value: The pulseTest to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_pulse_test("value")
        """
        self.pulse_test = value  # Use property setter (gets validation)
        return self

    def with_trigger(self, value: Optional[RefType]) -> "IoHwAbstractionServerAnnotation":
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



class ParameterPortAnnotation(GeneralAnnotation):
    """
    Annotation to a port used for calibration regarding a certain
    ParameterDataPrototype.
    
    Package: M2::AUTOSARTemplates::SWComponentTemplate::ApplicationAttributes::ParameterPortAnnotation
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 158, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The instance of annotated ParameterDataPrototype.
        self._parameterPrototype: Optional["ParameterData"] = None

    @property
    def parameter_prototype(self) -> Optional["ParameterData"]:
        """Get parameterPrototype (Pythonic accessor)."""
        return self._parameterPrototype

    @parameter_prototype.setter
    def parameter_prototype(self, value: Optional["ParameterData"]) -> None:
        """
        Set parameterPrototype with validation.
        
        Args:
            value: The parameterPrototype to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._parameterPrototype = None
            return

        if not isinstance(value, ParameterData):
            raise TypeError(
                f"parameterPrototype must be ParameterData or None, got {type(value).__name__}"
            )
        self._parameterPrototype = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getParameterPrototype(self) -> "ParameterData":
        """
        AUTOSAR-compliant getter for parameterPrototype.
        
        Returns:
            The parameterPrototype value
        
        Note:
            Delegates to parameter_prototype property (CODING_RULE_V2_00017)
        """
        return self.parameter_prototype  # Delegates to property

    def setParameterPrototype(self, value: "ParameterData") -> "ParameterPortAnnotation":
        """
        AUTOSAR-compliant setter for parameterPrototype with method chaining.
        
        Args:
            value: The parameterPrototype to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to parameter_prototype property setter (gets validation automatically)
        """
        self.parameter_prototype = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_parameter_prototype(self, value: Optional["ParameterData"]) -> "ParameterPortAnnotation":
        """
        Set parameterPrototype and return self for chaining.
        
        Args:
            value: The parameterPrototype to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_parameter_prototype("value")
        """
        self.parameter_prototype = value  # Use property setter (gets validation)
        return self



class ModePortAnnotation(GeneralAnnotation):
    """
    Annotation to a port used for calibration regarding a certain
    ModeDeclarationGroupPrototype.
    
    Package: M2::AUTOSARTemplates::SWComponentTemplate::ApplicationAttributes::ModePortAnnotation
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 159, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The instance of annotated ModeDeclarationGroup.
        self._modeGroup: Optional["RefType"] = None

    @property
    def mode_group(self) -> Optional["RefType"]:
        """Get modeGroup (Pythonic accessor)."""
        return self._modeGroup

    @mode_group.setter
    def mode_group(self, value: Optional["RefType"]) -> None:
        """
        Set modeGroup with validation.
        
        Args:
            value: The modeGroup to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._modeGroup = None
            return

        self._modeGroup = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getModeGroup(self) -> "RefType":
        """
        AUTOSAR-compliant getter for modeGroup.
        
        Returns:
            The modeGroup value
        
        Note:
            Delegates to mode_group property (CODING_RULE_V2_00017)
        """
        return self.mode_group  # Delegates to property

    def setModeGroup(self, value: "RefType") -> "ModePortAnnotation":
        """
        AUTOSAR-compliant setter for modeGroup with method chaining.
        
        Args:
            value: The modeGroup to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to mode_group property setter (gets validation automatically)
        """
        self.mode_group = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_mode_group(self, value: Optional[RefType]) -> "ModePortAnnotation":
        """
        Set modeGroup and return self for chaining.
        
        Args:
            value: The modeGroup to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_mode_group("value")
        """
        self.mode_group = value  # Use property setter (gets validation)
        return self



class TriggerPortAnnotation(GeneralAnnotation):
    """
    Annotation to a port used for calibration regarding a certain Trigger.
    
    Package: M2::AUTOSARTemplates::SWComponentTemplate::ApplicationAttributes::TriggerPortAnnotation
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 160, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The instance of annotated trigger.
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

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTrigger(self) -> "RefType":
        """
        AUTOSAR-compliant getter for trigger.
        
        Returns:
            The trigger value
        
        Note:
            Delegates to trigger property (CODING_RULE_V2_00017)
        """
        return self.trigger  # Delegates to property

    def setTrigger(self, value: "RefType") -> "TriggerPortAnnotation":
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

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_trigger(self, value: Optional[RefType]) -> "TriggerPortAnnotation":
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



class NvDataPortAnnotation(GeneralAnnotation):
    """
    Annotation to a port regarding a certain VariableDataPrototype.
    
    Package: M2::AUTOSARTemplates::SWComponentTemplate::ApplicationAttributes::NvDataPortAnnotation
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 160, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The instance of nv data annotated.
        self._variable: Optional["RefType"] = None

    @property
    def variable(self) -> Optional["RefType"]:
        """Get variable (Pythonic accessor)."""
        return self._variable

    @variable.setter
    def variable(self, value: Optional["RefType"]) -> None:
        """
        Set variable with validation.
        
        Args:
            value: The variable to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._variable = None
            return

        self._variable = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getVariable(self) -> "RefType":
        """
        AUTOSAR-compliant getter for variable.
        
        Returns:
            The variable value
        
        Note:
            Delegates to variable property (CODING_RULE_V2_00017)
        """
        return self.variable  # Delegates to property

    def setVariable(self, value: "RefType") -> "NvDataPortAnnotation":
        """
        AUTOSAR-compliant setter for variable with method chaining.
        
        Args:
            value: The variable to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to variable property setter (gets validation automatically)
        """
        self.variable = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_variable(self, value: Optional[RefType]) -> "NvDataPortAnnotation":
        """
        Set variable and return self for chaining.
        
        Args:
            value: The variable to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_variable("value")
        """
        self.variable = value  # Use property setter (gets validation)
        return self



class DelegatedPortAnnotation(GeneralAnnotation):
    """
    Annotation to a "delegated port" to specify the Signal Fan In or Signal Fan
    Out inside the CompositionSw ComponentType.
    
    Package: M2::AUTOSARTemplates::SWComponentTemplate::ApplicationAttributes::DelegatedPortAnnotation
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 162, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specifies the Signal Fan In or Signal Fan Out inside the.
        self._signalFan: Optional["SignalFanEnum"] = None

    @property
    def signal_fan(self) -> Optional["SignalFanEnum"]:
        """Get signalFan (Pythonic accessor)."""
        return self._signalFan

    @signal_fan.setter
    def signal_fan(self, value: Optional["SignalFanEnum"]) -> None:
        """
        Set signalFan with validation.
        
        Args:
            value: The signalFan to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._signalFan = None
            return

        if not isinstance(value, SignalFanEnum):
            raise TypeError(
                f"signalFan must be SignalFanEnum or None, got {type(value).__name__}"
            )
        self._signalFan = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSignalFan(self) -> "SignalFanEnum":
        """
        AUTOSAR-compliant getter for signalFan.
        
        Returns:
            The signalFan value
        
        Note:
            Delegates to signal_fan property (CODING_RULE_V2_00017)
        """
        return self.signal_fan  # Delegates to property

    def setSignalFan(self, value: "SignalFanEnum") -> "DelegatedPortAnnotation":
        """
        AUTOSAR-compliant setter for signalFan with method chaining.
        
        Args:
            value: The signalFan to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to signal_fan property setter (gets validation automatically)
        """
        self.signal_fan = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_signal_fan(self, value: Optional["SignalFanEnum"]) -> "DelegatedPortAnnotation":
        """
        Set signalFan and return self for chaining.
        
        Args:
            value: The signalFan to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_signal_fan("value")
        """
        self.signal_fan = value  # Use property setter (gets validation)
        return self



class SenderAnnotation(SenderReceiverAnnotation):
    """
    Annotation of a sender port, specifying properties of data elements that
    don’t affect communication or generation of the RTE.
    
    Package: M2::AUTOSARTemplates::SWComponentTemplate::ApplicationAttributes::SenderAnnotation
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 153, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class ReceiverAnnotation(SenderReceiverAnnotation):
    """
    Annotation of a receiver port, specifying properties of data elements that
    don’t affect communication or generation of the RTE. The given attributes
    are requirements on the required data.
    
    Package: M2::AUTOSARTemplates::SWComponentTemplate::ApplicationAttributes::ReceiverAnnotation
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 153, Classic Platform
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The maximum allowed age of the signal since it was by a sensor.
        # This is a requirement the receiver side.
        self._signalAge: Optional["MultidimensionalTime"] = None

    @property
    def signal_age(self) -> Optional["MultidimensionalTime"]:
        """Get signalAge (Pythonic accessor)."""
        return self._signalAge

    @signal_age.setter
    def signal_age(self, value: Optional["MultidimensionalTime"]) -> None:
        """
        Set signalAge with validation.
        
        Args:
            value: The signalAge to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._signalAge = None
            return

        if not isinstance(value, MultidimensionalTime):
            raise TypeError(
                f"signalAge must be MultidimensionalTime or None, got {type(value).__name__}"
            )
        self._signalAge = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSignalAge(self) -> "MultidimensionalTime":
        """
        AUTOSAR-compliant getter for signalAge.
        
        Returns:
            The signalAge value
        
        Note:
            Delegates to signal_age property (CODING_RULE_V2_00017)
        """
        return self.signal_age  # Delegates to property

    def setSignalAge(self, value: "MultidimensionalTime") -> "ReceiverAnnotation":
        """
        AUTOSAR-compliant setter for signalAge with method chaining.
        
        Args:
            value: The signalAge to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to signal_age property setter (gets validation automatically)
        """
        self.signal_age = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_signal_age(self, value: Optional["MultidimensionalTime"]) -> "ReceiverAnnotation":
        """
        Set signalAge and return self for chaining.
        
        Args:
            value: The signalAge to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_signal_age("value")
        """
        self.signal_age = value  # Use property setter (gets validation)
        return self


class ProcessingKindEnum(AREnum):
    """
    ProcessingKindEnum enumeration

Kind of processing which has been applied to a data element. Aggregated by SenderReceiverAnnotation.processingKind

Package: M2::AUTOSARTemplates::SWComponentTemplate::ApplicationAttributes
    """
    # Indicates that a raw signal has been manipulated by some application software components by using
    filtered = "0"

    # Indicates that none of the other option apply.
    none = "1"

    # Specifies that a signal is taken directly from the basic software modules, i.e. from the ECU abstraction
    raw = "2"



class DataLimitKindEnum(AREnum):
    """
    DataLimitKindEnum enumeration

Indicates whether the data element carries a minimum or maximum value, thereby limiting the current range of another value. Aggregated by SenderReceiverAnnotation.limitKind

Package: M2::AUTOSARTemplates::SWComponentTemplate::ApplicationAttributes
    """
    # Limitation to maximum value
    max = "0"

    # Component Template
    Software = "None"

    # CP R23-11
    AUTOSAR = "None"

    # Limitation to minimum value
    min = "1"

    # No limitation applicable
    none = "2"



class FilterDebouncingEnum(AREnum):
    """
    FilterDebouncingEnum enumeration

This enumeration defines possible values for the filter debouncing strategy. Aggregated by IoHwAbstractionServerAnnotation.filteringDebouncing

Package: M2::AUTOSARTemplates::SWComponentTemplate::ApplicationAttributes
    """
    # The signal is a mean value
    debounceData = "0"

    # Means that no modification of the signal has been applied. This is the default value
    rawData = "1"

    # The signal is delivered by a GET operation after a certain amount of time
    waitTimeDate = "2"



class PulseTestEnum(AREnum):
    """
    PulseTestEnum enumeration

This element indicates to the connected Actuator Software component whether the data-element can be used to generate pulse test sequences using the IoHwAbstraction layer Aggregated by IoHwAbstractionServerAnnotation.pulseTest

Package: M2::AUTOSARTemplates::SWComponentTemplate::ApplicationAttributes
    """
    # Disables the pulse test
    disable = "0"

    # Enables the pulse test
    enable = "1"



class SignalFanEnum(AREnum):
    """
    SignalFanEnum enumeration

Signal Fan inside the Composition Component Type. Aggregated by DelegatedPortAnnotation.signalFan

Package: M2::AUTOSARTemplates::SWComponentTemplate::ApplicationAttributes
    """
    # The connections internally in the CompositionSwComponentType via DelegationSwConnectors and AssemblySwConnectors are defined in a way that at least one data element present in the S/R interface or one ClientServerOperation in the C/S interface of the outer PortPrototype is involved in a
    nfold = "0"

    # The connections internally in the CompositionSwComponentType via DelegationSwConnectors and AssemblySwConnectors are defined in a way that each VariableDataPrototype present in the S/R interface or ClientServerOperation in the C/S interface of the outer PortPrototype is involved in a 1:1 communication pattern only.
    single = "1"

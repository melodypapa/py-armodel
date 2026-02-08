"""
AUTOSAR Package - Transformer

Package: M2::AUTOSARTemplates::SystemTemplate::Transformer
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
    NameToken,
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
from armodel.v2.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import (
    TransformationComSpecProps,
)
from armodel.v2.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.__init__ import (
    DataPrototypeReference,
    TransformationDescription,
    TransformationProps,
)




class DataTransformation(Identifiable):
    """
    A DataTransformation represents a transformer chain. It is an ordered list
    of transformers.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Transformer::DataTransformation
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 149, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 763, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute controls the kind of DataTransformation to be applied.
        self._data: Optional["DataTransformationKind"] = None

    @property
    def data(self) -> Optional["DataTransformationKind"]:
        """Get data (Pythonic accessor)."""
        return self._data

    @data.setter
    def data(self, value: Optional["DataTransformationKind"]) -> None:
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

        if not isinstance(value, DataTransformationKind):
            raise TypeError(
                f"data must be DataTransformationKind or None, got {type(value).__name__}"
            )
        self._data = value
        # Specifies whether the transformer chain is executed even no input data are
                # available.
        # 1228 Document ID 62: AUTOSAR_CP_TPS_SoftwareComponentTemplate Template
                # R23-11.
        self._executeDespite: Optional["Boolean"] = None

    @property
    def execute_despite(self) -> Optional["Boolean"]:
        """Get executeDespite (Pythonic accessor)."""
        return self._executeDespite

    @execute_despite.setter
    def execute_despite(self, value: Optional["Boolean"]) -> None:
        """
        Set executeDespite with validation.
        
        Args:
            value: The executeDespite to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._executeDespite = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"executeDespite must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._executeDespite = value
        # This attribute represents the definition of a chain of Technology
        # transformers that are supposed to be executed according order of being
        # referenced from DataTransformation.
        self._transformer: List["Transformation"] = []

    @property
    def transformer(self) -> List["Transformation"]:
        """Get transformer (Pythonic accessor)."""
        return self._transformer

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getData(self) -> "DataTransformationKind":
        """
        AUTOSAR-compliant getter for data.
        
        Returns:
            The data value
        
        Note:
            Delegates to data property (CODING_RULE_V2_00017)
        """
        return self.data  # Delegates to property

    def setData(self, value: "DataTransformationKind") -> "DataTransformation":
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

    def getExecuteDespite(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for executeDespite.
        
        Returns:
            The executeDespite value
        
        Note:
            Delegates to execute_despite property (CODING_RULE_V2_00017)
        """
        return self.execute_despite  # Delegates to property

    def setExecuteDespite(self, value: "Boolean") -> "DataTransformation":
        """
        AUTOSAR-compliant setter for executeDespite with method chaining.
        
        Args:
            value: The executeDespite to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to execute_despite property setter (gets validation automatically)
        """
        self.execute_despite = value  # Delegates to property setter
        return self

    def getTransformer(self) -> List["Transformation"]:
        """
        AUTOSAR-compliant getter for transformer.
        
        Returns:
            The transformer value
        
        Note:
            Delegates to transformer property (CODING_RULE_V2_00017)
        """
        return self.transformer  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_data(self, value: Optional["DataTransformationKind"]) -> "DataTransformation":
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

    def with_execute_despite(self, value: Optional["Boolean"]) -> "DataTransformation":
        """
        Set executeDespite and return self for chaining.
        
        Args:
            value: The executeDespite to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_execute_despite("value")
        """
        self.execute_despite = value  # Use property setter (gets validation)
        return self



class TransformationTechnology(Identifiable):
    """
    A TransformationTechnology is a transformer inside a transformer chain.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Transformer::TransformationTechnology
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 198, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 764, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Aggregation of the mandatory BufferProperties.
        # 1228 Document ID 62: AUTOSAR_CP_TPS_SoftwareComponentTemplate Template
                # R23-11.
        self._bufferProperties: Optional["BufferProperties"] = None

    @property
    def buffer_properties(self) -> Optional["BufferProperties"]:
        """Get bufferProperties (Pythonic accessor)."""
        return self._bufferProperties

    @buffer_properties.setter
    def buffer_properties(self, value: Optional["BufferProperties"]) -> None:
        """
        Set bufferProperties with validation.
        
        Args:
            value: The bufferProperties to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._bufferProperties = None
            return

        if not isinstance(value, BufferProperties):
            raise TypeError(
                f"bufferProperties must be BufferProperties or None, got {type(value).__name__}"
            )
        self._bufferProperties = value
        # This attribute defines whether the Transformer has an state or not.
        self._hasInternal: Optional["Boolean"] = None

    @property
    def has_internal(self) -> Optional["Boolean"]:
        """Get hasInternal (Pythonic accessor)."""
        return self._hasInternal

    @has_internal.setter
    def has_internal(self, value: Optional["Boolean"]) -> None:
        """
        Set hasInternal with validation.
        
        Args:
            value: The hasInternal to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._hasInternal = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"hasInternal must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._hasInternal = value
        # Specifies whether this transformer gets access to the original data.
        self._needsOriginal: Optional["Boolean"] = None

    @property
    def needs_original(self) -> Optional["Boolean"]:
        """Get needsOriginal (Pythonic accessor)."""
        return self._needsOriginal

    @needs_original.setter
    def needs_original(self, value: Optional["Boolean"]) -> None:
        """
        Set needsOriginal with validation.
        
        Args:
            value: The needsOriginal to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._needsOriginal = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"needsOriginal must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._needsOriginal = value
        # Specifies the protocol that is implemented by this.
        self._protocol: Optional["String"] = None

    @property
    def protocol(self) -> Optional["String"]:
        """Get protocol (Pythonic accessor)."""
        return self._protocol

    @protocol.setter
    def protocol(self, value: Optional["String"]) -> None:
        """
        Set protocol with validation.
        
        Args:
            value: The protocol to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._protocol = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"protocol must be String or str or None, got {type(value).__name__}"
            )
        self._protocol = value
        # A transformer can be configured with transformer specific parameters which
        # are represented by the Transformer atpVariation.
        self._transformation: Optional["Transformation"] = None

    @property
    def transformation(self) -> Optional["Transformation"]:
        """Get transformation (Pythonic accessor)."""
        return self._transformation

    @transformation.setter
    def transformation(self, value: Optional["Transformation"]) -> None:
        """
        Set transformation with validation.
        
        Args:
            value: The transformation to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._transformation = None
            return

        if not isinstance(value, Transformation):
            raise TypeError(
                f"transformation must be Transformation or None, got {type(value).__name__}"
            )
        self._transformation = value
        # Specifies to which transformer class this transformer.
        self._transformer: Optional["TransformerClassEnum"] = None

    @property
    def transformer(self) -> Optional["TransformerClassEnum"]:
        """Get transformer (Pythonic accessor)."""
        return self._transformer

    @transformer.setter
    def transformer(self, value: Optional["TransformerClassEnum"]) -> None:
        """
        Set transformer with validation.
        
        Args:
            value: The transformer to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._transformer = None
            return

        if not isinstance(value, TransformerClassEnum):
            raise TypeError(
                f"transformer must be TransformerClassEnum or None, got {type(value).__name__}"
            )
        self._transformer = value
        # Version of the implemented protocol.
        self._version: Optional["String"] = None

    @property
    def version(self) -> Optional["String"]:
        """Get version (Pythonic accessor)."""
        return self._version

    @version.setter
    def version(self, value: Optional["String"]) -> None:
        """
        Set version with validation.
        
        Args:
            value: The version to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._version = None
            return

        if not isinstance(value, (String, str)):
            raise TypeError(
                f"version must be String or str or None, got {type(value).__name__}"
            )
        self._version = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBufferProperties(self) -> "BufferProperties":
        """
        AUTOSAR-compliant getter for bufferProperties.
        
        Returns:
            The bufferProperties value
        
        Note:
            Delegates to buffer_properties property (CODING_RULE_V2_00017)
        """
        return self.buffer_properties  # Delegates to property

    def setBufferProperties(self, value: "BufferProperties") -> "TransformationTechnology":
        """
        AUTOSAR-compliant setter for bufferProperties with method chaining.
        
        Args:
            value: The bufferProperties to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to buffer_properties property setter (gets validation automatically)
        """
        self.buffer_properties = value  # Delegates to property setter
        return self

    def getHasInternal(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for hasInternal.
        
        Returns:
            The hasInternal value
        
        Note:
            Delegates to has_internal property (CODING_RULE_V2_00017)
        """
        return self.has_internal  # Delegates to property

    def setHasInternal(self, value: "Boolean") -> "TransformationTechnology":
        """
        AUTOSAR-compliant setter for hasInternal with method chaining.
        
        Args:
            value: The hasInternal to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to has_internal property setter (gets validation automatically)
        """
        self.has_internal = value  # Delegates to property setter
        return self

    def getNeedsOriginal(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for needsOriginal.
        
        Returns:
            The needsOriginal value
        
        Note:
            Delegates to needs_original property (CODING_RULE_V2_00017)
        """
        return self.needs_original  # Delegates to property

    def setNeedsOriginal(self, value: "Boolean") -> "TransformationTechnology":
        """
        AUTOSAR-compliant setter for needsOriginal with method chaining.
        
        Args:
            value: The needsOriginal to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to needs_original property setter (gets validation automatically)
        """
        self.needs_original = value  # Delegates to property setter
        return self

    def getProtocol(self) -> "String":
        """
        AUTOSAR-compliant getter for protocol.
        
        Returns:
            The protocol value
        
        Note:
            Delegates to protocol property (CODING_RULE_V2_00017)
        """
        return self.protocol  # Delegates to property

    def setProtocol(self, value: "String") -> "TransformationTechnology":
        """
        AUTOSAR-compliant setter for protocol with method chaining.
        
        Args:
            value: The protocol to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to protocol property setter (gets validation automatically)
        """
        self.protocol = value  # Delegates to property setter
        return self

    def getTransformation(self) -> "Transformation":
        """
        AUTOSAR-compliant getter for transformation.
        
        Returns:
            The transformation value
        
        Note:
            Delegates to transformation property (CODING_RULE_V2_00017)
        """
        return self.transformation  # Delegates to property

    def setTransformation(self, value: "Transformation") -> "TransformationTechnology":
        """
        AUTOSAR-compliant setter for transformation with method chaining.
        
        Args:
            value: The transformation to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to transformation property setter (gets validation automatically)
        """
        self.transformation = value  # Delegates to property setter
        return self

    def getTransformer(self) -> "TransformerClassEnum":
        """
        AUTOSAR-compliant getter for transformer.
        
        Returns:
            The transformer value
        
        Note:
            Delegates to transformer property (CODING_RULE_V2_00017)
        """
        return self.transformer  # Delegates to property

    def setTransformer(self, value: "TransformerClassEnum") -> "TransformationTechnology":
        """
        AUTOSAR-compliant setter for transformer with method chaining.
        
        Args:
            value: The transformer to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to transformer property setter (gets validation automatically)
        """
        self.transformer = value  # Delegates to property setter
        return self

    def getVersion(self) -> "String":
        """
        AUTOSAR-compliant getter for version.
        
        Returns:
            The version value
        
        Note:
            Delegates to version property (CODING_RULE_V2_00017)
        """
        return self.version  # Delegates to property

    def setVersion(self, value: "String") -> "TransformationTechnology":
        """
        AUTOSAR-compliant setter for version with method chaining.
        
        Args:
            value: The version to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to version property setter (gets validation automatically)
        """
        self.version = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_buffer_properties(self, value: Optional["BufferProperties"]) -> "TransformationTechnology":
        """
        Set bufferProperties and return self for chaining.
        
        Args:
            value: The bufferProperties to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_buffer_properties("value")
        """
        self.buffer_properties = value  # Use property setter (gets validation)
        return self

    def with_has_internal(self, value: Optional["Boolean"]) -> "TransformationTechnology":
        """
        Set hasInternal and return self for chaining.
        
        Args:
            value: The hasInternal to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_has_internal("value")
        """
        self.has_internal = value  # Use property setter (gets validation)
        return self

    def with_needs_original(self, value: Optional["Boolean"]) -> "TransformationTechnology":
        """
        Set needsOriginal and return self for chaining.
        
        Args:
            value: The needsOriginal to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_needs_original("value")
        """
        self.needs_original = value  # Use property setter (gets validation)
        return self

    def with_protocol(self, value: Optional["String"]) -> "TransformationTechnology":
        """
        Set protocol and return self for chaining.
        
        Args:
            value: The protocol to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_protocol("value")
        """
        self.protocol = value  # Use property setter (gets validation)
        return self

    def with_transformation(self, value: Optional["Transformation"]) -> "TransformationTechnology":
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

    def with_transformer(self, value: Optional["TransformerClassEnum"]) -> "TransformationTechnology":
        """
        Set transformer and return self for chaining.
        
        Args:
            value: The transformer to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_transformer("value")
        """
        self.transformer = value  # Use property setter (gets validation)
        return self

    def with_version(self, value: Optional["String"]) -> "TransformationTechnology":
        """
        Set version and return self for chaining.
        
        Args:
            value: The version to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_version("value")
        """
        self.version = value  # Use property setter (gets validation)
        return self



class BufferProperties(ARObject):
    """
    Configuration of the buffer properties the transformer needs to work.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Transformer::BufferProperties
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 199, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 767, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines the length of the header (in bits) this transformer in front of the
        # data.
        self._headerLength: Optional["Integer"] = None

    @property
    def header_length(self) -> Optional["Integer"]:
        """Get headerLength (Pythonic accessor)."""
        return self._headerLength

    @header_length.setter
    def header_length(self, value: Optional["Integer"]) -> None:
        """
        Set headerLength with validation.
        
        Args:
            value: The headerLength to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._headerLength = None
            return

        if not isinstance(value, (Integer, int)):
            raise TypeError(
                f"headerLength must be Integer or int or None, got {type(value).__name__}"
            )
        self._headerLength = value
        # If set, the transformer uses the input buffer as output.
        self._inPlace: Optional["Boolean"] = None

    @property
    def in_place(self) -> Optional["Boolean"]:
        """Get inPlace (Pythonic accessor)."""
        return self._inPlace

    @in_place.setter
    def in_place(self, value: Optional["Boolean"]) -> None:
        """
        Set inPlace with validation.
        
        Args:
            value: The inPlace to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._inPlace = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"inPlace must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._inPlace = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getHeaderLength(self) -> "Integer":
        """
        AUTOSAR-compliant getter for headerLength.
        
        Returns:
            The headerLength value
        
        Note:
            Delegates to header_length property (CODING_RULE_V2_00017)
        """
        return self.header_length  # Delegates to property

    def setHeaderLength(self, value: "Integer") -> "BufferProperties":
        """
        AUTOSAR-compliant setter for headerLength with method chaining.
        
        Args:
            value: The headerLength to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to header_length property setter (gets validation automatically)
        """
        self.header_length = value  # Delegates to property setter
        return self

    def getInPlace(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for inPlace.
        
        Returns:
            The inPlace value
        
        Note:
            Delegates to in_place property (CODING_RULE_V2_00017)
        """
        return self.in_place  # Delegates to property

    def setInPlace(self, value: "Boolean") -> "BufferProperties":
        """
        AUTOSAR-compliant setter for inPlace with method chaining.
        
        Args:
            value: The inPlace to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to in_place property setter (gets validation automatically)
        """
        self.in_place = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_header_length(self, value: Optional["Integer"]) -> "BufferProperties":
        """
        Set headerLength and return self for chaining.
        
        Args:
            value: The headerLength to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_header_length("value")
        """
        self.header_length = value  # Use property setter (gets validation)
        return self

    def with_in_place(self, value: Optional["Boolean"]) -> "BufferProperties":
        """
        Set inPlace and return self for chaining.
        
        Args:
            value: The inPlace to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_in_place("value")
        """
        self.in_place = value  # Use property setter (gets validation)
        return self



class TransformationDescription(Describable, ABC):
    """
    The TransformationDescription is the abstract class that can be used by
    specific transformers to add transformer specific properties.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Transformer::TransformationDescription
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 199, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 770, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is TransformationDescription:
            raise TypeError("TransformationDescription is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class EndToEndTransformationComSpecProps(TransformationComSpecProps):
    """
    The class EndToEndTransformationIComSpecProps specifies port specific
    configuration properties for EndToEnd transformer attributes.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Transformer::EndToEndTransformationComSpecProps
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 200, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2023, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Clear monitoring window on transition from state Valid to Invalid.
        self._clearFromValid: Optional["Boolean"] = None

    @property
    def clear_from_valid(self) -> Optional["Boolean"]:
        """Get clearFromValid (Pythonic accessor)."""
        return self._clearFromValid

    @clear_from_valid.setter
    def clear_from_valid(self, value: Optional["Boolean"]) -> None:
        """
        Set clearFromValid with validation.
        
        Args:
            value: The clearFromValid to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._clearFromValid = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"clearFromValid must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._clearFromValid = value
        # Disables the E2EStateMachine (only E2E check is performed).
        self._disableEndTo: Optional["Boolean"] = None

    @property
    def disable_end_to(self) -> Optional["Boolean"]:
        """Get disableEndTo (Pythonic accessor)."""
        return self._disableEndTo

    @disable_end_to.setter
    def disable_end_to(self, value: Optional["Boolean"]) -> None:
        """
        Set disableEndTo with validation.
        
        Args:
            value: The disableEndTo to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._disableEndTo = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"disableEndTo must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._disableEndTo = value
        # Reference to additional settings for the E2E state machine.
        self._e2eProfile: Optional["E2EProfileCompatibility"] = None

    @property
    def e2e_profile(self) -> Optional["E2EProfileCompatibility"]:
        """Get e2eProfile (Pythonic accessor)."""
        return self._e2eProfile

    @e2e_profile.setter
    def e2e_profile(self, value: Optional["E2EProfileCompatibility"]) -> None:
        """
        Set e2eProfile with validation.
        
        Args:
            value: The e2eProfile to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._e2eProfile = None
            return

        if not isinstance(value, E2EProfileCompatibility):
            raise TypeError(
                f"e2eProfile must be E2EProfileCompatibility or None, got {type(value).__name__}"
            )
        self._e2eProfile = value
        # Maximum allowed difference between two counter values two consecutively
                # received valid messages.
        # For the receiver gets data with counter 1 and Max 3, then at the next
                # reception the receiver Counters with values 2, 3 or 4.
        self._maxDelta: Optional["PositiveInteger"] = None

    @property
    def max_delta(self) -> Optional["PositiveInteger"]:
        """Get maxDelta (Pythonic accessor)."""
        return self._maxDelta

    @max_delta.setter
    def max_delta(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set maxDelta with validation.
        
        Args:
            value: The maxDelta to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxDelta = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"maxDelta must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._maxDelta = value
        # Maximal number of checks in which ProfileStatus equal to was determined,
                # within the last Window for the state E2E_SM_VALID.
        # value is 0.
        self._maxErrorState: Optional["PositiveInteger"] = None

    @property
    def max_error_state(self) -> Optional["PositiveInteger"]:
        """Get maxErrorState (Pythonic accessor)."""
        return self._maxErrorState

    @max_error_state.setter
    def max_error_state(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set maxErrorState with validation.
        
        Args:
            value: The maxErrorState to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxErrorState = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"maxErrorState must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._maxErrorState = value
        # EndToEndTransformationDescription holds these which are profile specific and
        # have the same all E2E transformers.
        self._maxNoNewOr: Optional["PositiveInteger"] = None

    @property
    def max_no_new_or(self) -> Optional["PositiveInteger"]:
        """Get maxNoNewOr (Pythonic accessor)."""
        return self._maxNoNewOr

    @max_no_new_or.setter
    def max_no_new_or(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set maxNoNewOr with validation.
        
        Args:
            value: The maxNoNewOr to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxNoNewOr = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"maxNoNewOr must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._maxNoNewOr = value
        # Minimal number of checks in which ProfileStatus equal to determined, within
                # the last WindowSize the state E2E_SM_INIT.
        # value is 1.
        self._minOkStateInit: Optional["PositiveInteger"] = None

    @property
    def min_ok_state_init(self) -> Optional["PositiveInteger"]:
        """Get minOkStateInit (Pythonic accessor)."""
        return self._minOkStateInit

    @min_ok_state_init.setter
    def min_ok_state_init(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set minOkStateInit with validation.
        
        Args:
            value: The minOkStateInit to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._minOkStateInit = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"minOkStateInit must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._minOkStateInit = value
        # Minimal number of checks in which ProfileStatus equal to was determined,
                # within the last WindowSize the state E2E_SM_VALID.
        # value is 1.
        self._minOkState: Optional["PositiveInteger"] = None

    @property
    def min_ok_state(self) -> Optional["PositiveInteger"]:
        """Get minOkState (Pythonic accessor)."""
        return self._minOkState

    @min_ok_state.setter
    def min_ok_state(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set minOkState with validation.
        
        Args:
            value: The minOkState to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._minOkState = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"minOkState must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._minOkState = value
        # EndToEndTransformationDescription holds these are profile specific and have
        # the same all E2E transformers.
        self._syncCounterInit: Optional["PositiveInteger"] = None

    @property
    def sync_counter_init(self) -> Optional["PositiveInteger"]:
        """Get syncCounterInit (Pythonic accessor)."""
        return self._syncCounterInit

    @sync_counter_init.setter
    def sync_counter_init(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set syncCounterInit with validation.
        
        Args:
            value: The syncCounterInit to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._syncCounterInit = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"syncCounterInit must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._syncCounterInit = value
        # Size of the monitoring window of state Init for the E2E.
        self._windowSizeInit: Optional["PositiveInteger"] = None

    @property
    def window_size_init(self) -> Optional["PositiveInteger"]:
        """Get windowSizeInit (Pythonic accessor)."""
        return self._windowSizeInit

    @window_size_init.setter
    def window_size_init(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set windowSizeInit with validation.
        
        Args:
            value: The windowSizeInit to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._windowSizeInit = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"windowSizeInit must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._windowSizeInit = value
        # Size of the monitoring window of state Valid for the E2E machine.
        self._windowSize: Optional["PositiveInteger"] = None

    @property
    def window_size(self) -> Optional["PositiveInteger"]:
        """Get windowSize (Pythonic accessor)."""
        return self._windowSize

    @window_size.setter
    def window_size(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set windowSize with validation.
        
        Args:
            value: The windowSize to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._windowSize = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"windowSize must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._windowSize = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getClearFromValid(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for clearFromValid.
        
        Returns:
            The clearFromValid value
        
        Note:
            Delegates to clear_from_valid property (CODING_RULE_V2_00017)
        """
        return self.clear_from_valid  # Delegates to property

    def setClearFromValid(self, value: "Boolean") -> "EndToEndTransformationComSpecProps":
        """
        AUTOSAR-compliant setter for clearFromValid with method chaining.
        
        Args:
            value: The clearFromValid to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to clear_from_valid property setter (gets validation automatically)
        """
        self.clear_from_valid = value  # Delegates to property setter
        return self

    def getDisableEndTo(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for disableEndTo.
        
        Returns:
            The disableEndTo value
        
        Note:
            Delegates to disable_end_to property (CODING_RULE_V2_00017)
        """
        return self.disable_end_to  # Delegates to property

    def setDisableEndTo(self, value: "Boolean") -> "EndToEndTransformationComSpecProps":
        """
        AUTOSAR-compliant setter for disableEndTo with method chaining.
        
        Args:
            value: The disableEndTo to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to disable_end_to property setter (gets validation automatically)
        """
        self.disable_end_to = value  # Delegates to property setter
        return self

    def getE2eProfile(self) -> "E2EProfileCompatibility":
        """
        AUTOSAR-compliant getter for e2eProfile.
        
        Returns:
            The e2eProfile value
        
        Note:
            Delegates to e2e_profile property (CODING_RULE_V2_00017)
        """
        return self.e2e_profile  # Delegates to property

    def setE2eProfile(self, value: "E2EProfileCompatibility") -> "EndToEndTransformationComSpecProps":
        """
        AUTOSAR-compliant setter for e2eProfile with method chaining.
        
        Args:
            value: The e2eProfile to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to e2e_profile property setter (gets validation automatically)
        """
        self.e2e_profile = value  # Delegates to property setter
        return self

    def getMaxDelta(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for maxDelta.
        
        Returns:
            The maxDelta value
        
        Note:
            Delegates to max_delta property (CODING_RULE_V2_00017)
        """
        return self.max_delta  # Delegates to property

    def setMaxDelta(self, value: "PositiveInteger") -> "EndToEndTransformationComSpecProps":
        """
        AUTOSAR-compliant setter for maxDelta with method chaining.
        
        Args:
            value: The maxDelta to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to max_delta property setter (gets validation automatically)
        """
        self.max_delta = value  # Delegates to property setter
        return self

    def getMaxErrorState(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for maxErrorState.
        
        Returns:
            The maxErrorState value
        
        Note:
            Delegates to max_error_state property (CODING_RULE_V2_00017)
        """
        return self.max_error_state  # Delegates to property

    def setMaxErrorState(self, value: "PositiveInteger") -> "EndToEndTransformationComSpecProps":
        """
        AUTOSAR-compliant setter for maxErrorState with method chaining.
        
        Args:
            value: The maxErrorState to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to max_error_state property setter (gets validation automatically)
        """
        self.max_error_state = value  # Delegates to property setter
        return self

    def getMaxNoNewOr(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for maxNoNewOr.
        
        Returns:
            The maxNoNewOr value
        
        Note:
            Delegates to max_no_new_or property (CODING_RULE_V2_00017)
        """
        return self.max_no_new_or  # Delegates to property

    def setMaxNoNewOr(self, value: "PositiveInteger") -> "EndToEndTransformationComSpecProps":
        """
        AUTOSAR-compliant setter for maxNoNewOr with method chaining.
        
        Args:
            value: The maxNoNewOr to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to max_no_new_or property setter (gets validation automatically)
        """
        self.max_no_new_or = value  # Delegates to property setter
        return self

    def getMinOkStateInit(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for minOkStateInit.
        
        Returns:
            The minOkStateInit value
        
        Note:
            Delegates to min_ok_state_init property (CODING_RULE_V2_00017)
        """
        return self.min_ok_state_init  # Delegates to property

    def setMinOkStateInit(self, value: "PositiveInteger") -> "EndToEndTransformationComSpecProps":
        """
        AUTOSAR-compliant setter for minOkStateInit with method chaining.
        
        Args:
            value: The minOkStateInit to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to min_ok_state_init property setter (gets validation automatically)
        """
        self.min_ok_state_init = value  # Delegates to property setter
        return self

    def getMinOkState(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for minOkState.
        
        Returns:
            The minOkState value
        
        Note:
            Delegates to min_ok_state property (CODING_RULE_V2_00017)
        """
        return self.min_ok_state  # Delegates to property

    def setMinOkState(self, value: "PositiveInteger") -> "EndToEndTransformationComSpecProps":
        """
        AUTOSAR-compliant setter for minOkState with method chaining.
        
        Args:
            value: The minOkState to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to min_ok_state property setter (gets validation automatically)
        """
        self.min_ok_state = value  # Delegates to property setter
        return self

    def getSyncCounterInit(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for syncCounterInit.
        
        Returns:
            The syncCounterInit value
        
        Note:
            Delegates to sync_counter_init property (CODING_RULE_V2_00017)
        """
        return self.sync_counter_init  # Delegates to property

    def setSyncCounterInit(self, value: "PositiveInteger") -> "EndToEndTransformationComSpecProps":
        """
        AUTOSAR-compliant setter for syncCounterInit with method chaining.
        
        Args:
            value: The syncCounterInit to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to sync_counter_init property setter (gets validation automatically)
        """
        self.sync_counter_init = value  # Delegates to property setter
        return self

    def getWindowSizeInit(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for windowSizeInit.
        
        Returns:
            The windowSizeInit value
        
        Note:
            Delegates to window_size_init property (CODING_RULE_V2_00017)
        """
        return self.window_size_init  # Delegates to property

    def setWindowSizeInit(self, value: "PositiveInteger") -> "EndToEndTransformationComSpecProps":
        """
        AUTOSAR-compliant setter for windowSizeInit with method chaining.
        
        Args:
            value: The windowSizeInit to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to window_size_init property setter (gets validation automatically)
        """
        self.window_size_init = value  # Delegates to property setter
        return self

    def getWindowSize(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for windowSize.
        
        Returns:
            The windowSize value
        
        Note:
            Delegates to window_size property (CODING_RULE_V2_00017)
        """
        return self.window_size  # Delegates to property

    def setWindowSize(self, value: "PositiveInteger") -> "EndToEndTransformationComSpecProps":
        """
        AUTOSAR-compliant setter for windowSize with method chaining.
        
        Args:
            value: The windowSize to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to window_size property setter (gets validation automatically)
        """
        self.window_size = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_clear_from_valid(self, value: Optional["Boolean"]) -> "EndToEndTransformationComSpecProps":
        """
        Set clearFromValid and return self for chaining.
        
        Args:
            value: The clearFromValid to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_clear_from_valid("value")
        """
        self.clear_from_valid = value  # Use property setter (gets validation)
        return self

    def with_disable_end_to(self, value: Optional["Boolean"]) -> "EndToEndTransformationComSpecProps":
        """
        Set disableEndTo and return self for chaining.
        
        Args:
            value: The disableEndTo to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_disable_end_to("value")
        """
        self.disable_end_to = value  # Use property setter (gets validation)
        return self

    def with_e2e_profile(self, value: Optional["E2EProfileCompatibility"]) -> "EndToEndTransformationComSpecProps":
        """
        Set e2eProfile and return self for chaining.
        
        Args:
            value: The e2eProfile to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_e2e_profile("value")
        """
        self.e2e_profile = value  # Use property setter (gets validation)
        return self

    def with_max_delta(self, value: Optional["PositiveInteger"]) -> "EndToEndTransformationComSpecProps":
        """
        Set maxDelta and return self for chaining.
        
        Args:
            value: The maxDelta to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_max_delta("value")
        """
        self.max_delta = value  # Use property setter (gets validation)
        return self

    def with_max_error_state(self, value: Optional["PositiveInteger"]) -> "EndToEndTransformationComSpecProps":
        """
        Set maxErrorState and return self for chaining.
        
        Args:
            value: The maxErrorState to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_max_error_state("value")
        """
        self.max_error_state = value  # Use property setter (gets validation)
        return self

    def with_max_no_new_or(self, value: Optional["PositiveInteger"]) -> "EndToEndTransformationComSpecProps":
        """
        Set maxNoNewOr and return self for chaining.
        
        Args:
            value: The maxNoNewOr to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_max_no_new_or("value")
        """
        self.max_no_new_or = value  # Use property setter (gets validation)
        return self

    def with_min_ok_state_init(self, value: Optional["PositiveInteger"]) -> "EndToEndTransformationComSpecProps":
        """
        Set minOkStateInit and return self for chaining.
        
        Args:
            value: The minOkStateInit to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_min_ok_state_init("value")
        """
        self.min_ok_state_init = value  # Use property setter (gets validation)
        return self

    def with_min_ok_state(self, value: Optional["PositiveInteger"]) -> "EndToEndTransformationComSpecProps":
        """
        Set minOkState and return self for chaining.
        
        Args:
            value: The minOkState to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_min_ok_state("value")
        """
        self.min_ok_state = value  # Use property setter (gets validation)
        return self

    def with_sync_counter_init(self, value: Optional["PositiveInteger"]) -> "EndToEndTransformationComSpecProps":
        """
        Set syncCounterInit and return self for chaining.
        
        Args:
            value: The syncCounterInit to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_sync_counter_init("value")
        """
        self.sync_counter_init = value  # Use property setter (gets validation)
        return self

    def with_window_size_init(self, value: Optional["PositiveInteger"]) -> "EndToEndTransformationComSpecProps":
        """
        Set windowSizeInit and return self for chaining.
        
        Args:
            value: The windowSizeInit to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_window_size_init("value")
        """
        self.window_size_init = value  # Use property setter (gets validation)
        return self

    def with_window_size(self, value: Optional["PositiveInteger"]) -> "EndToEndTransformationComSpecProps":
        """
        Set windowSize and return self for chaining.
        
        Args:
            value: The windowSize to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_window_size("value")
        """
        self.window_size = value  # Use property setter (gets validation)
        return self



class E2EProfileCompatibilityProps(ARElement):
    """
    This meta-class collects settings for configuration of the E2E state
    machine.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Transformer::E2EProfileCompatibilityProps
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 202, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 807, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # E2E State machine behavior concerning transition from to INVALID no direct
        # transition from NODATA to transition from INIT to INVALID due to (Autosar
        # R19-11 or former direct transition from NODATA to INVALID from INIT to
        # INVALID due to covered (state machine extended).
        self._transitToInvalid: Optional["Boolean"] = None

    @property
    def transit_to_invalid(self) -> Optional["Boolean"]:
        """Get transitToInvalid (Pythonic accessor)."""
        return self._transitToInvalid

    @transit_to_invalid.setter
    def transit_to_invalid(self, value: Optional["Boolean"]) -> None:
        """
        Set transitToInvalid with validation.
        
        Args:
            value: The transitToInvalid to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._transitToInvalid = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"transitToInvalid must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._transitToInvalid = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTransitToInvalid(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for transitToInvalid.
        
        Returns:
            The transitToInvalid value
        
        Note:
            Delegates to transit_to_invalid property (CODING_RULE_V2_00017)
        """
        return self.transit_to_invalid  # Delegates to property

    def setTransitToInvalid(self, value: "Boolean") -> "E2EProfileCompatibilityProps":
        """
        AUTOSAR-compliant setter for transitToInvalid with method chaining.
        
        Args:
            value: The transitToInvalid to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to transit_to_invalid property setter (gets validation automatically)
        """
        self.transit_to_invalid = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_transit_to_invalid(self, value: Optional["Boolean"]) -> "E2EProfileCompatibilityProps":
        """
        Set transitToInvalid and return self for chaining.
        
        Args:
            value: The transitToInvalid to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_transit_to_invalid("value")
        """
        self.transit_to_invalid = value  # Use property setter (gets validation)
        return self



class DataTransformationSet(ARElement):
    """
    This element is the system wide container of DataTransformations which
    represent transformer chains.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Transformer::DataTransformationSet
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 762, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This container consists of all transformer chains which be used for
                # transformation of data communication.
        # atpVariation.
        self._data: List["DataTransformation"] = []

    @property
    def data(self) -> List["DataTransformation"]:
        """Get data (Pythonic accessor)."""
        return self._data
        # Transformer that is used in a transformer chain for transformation of data
                # communication.
        # atpVariation.
        self._transformation: List["Transformation"] = []

    @property
    def transformation(self) -> List["Transformation"]:
        """Get transformation (Pythonic accessor)."""
        return self._transformation

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getData(self) -> List["DataTransformation"]:
        """
        AUTOSAR-compliant getter for data.
        
        Returns:
            The data value
        
        Note:
            Delegates to data property (CODING_RULE_V2_00017)
        """
        return self.data  # Delegates to property

    def getTransformation(self) -> List["Transformation"]:
        """
        AUTOSAR-compliant getter for transformation.
        
        Returns:
            The transformation value
        
        Note:
            Delegates to transformation property (CODING_RULE_V2_00017)
        """
        return self.transformation  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class TransformationISignalProps(ARObject, ABC):
    """
    TransformationISignalProps holds all the attributes for the different
    TransformationTechnologies that are ISignal specific. Tags:
    vh.latestBindingTime=postBuild
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Transformer::TransformationISignalProps
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 772, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is TransformationISignalProps:
            raise TypeError("TransformationISignalProps is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines whether the transformer chain of client/server coordinates an
        # autonomous error reaction the RTE or whether any error reaction is the the
        # application.
        self._csErrorReaction: Optional["CSTransformerError"] = None

    @property
    def cs_error_reaction(self) -> Optional["CSTransformerError"]:
        """Get csErrorReaction (Pythonic accessor)."""
        return self._csErrorReaction

    @cs_error_reaction.setter
    def cs_error_reaction(self, value: Optional["CSTransformerError"]) -> None:
        """
        Set csErrorReaction with validation.
        
        Args:
            value: The csErrorReaction to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._csErrorReaction = None
            return

        if not isinstance(value, CSTransformerError):
            raise TypeError(
                f"csErrorReaction must be CSTransformerError or None, got {type(value).__name__}"
            )
        self._csErrorReaction = value
        # Fine granular modeling of TransfromationProps on the level of DataPrototypes.
        # This atpSplitable property has no atp.
        # Splitkey due (PropertySetPattern).
        self._dataPrototype: List["RefType"] = []

    @property
    def data_prototype(self) -> List["RefType"]:
        """Get dataPrototype (Pythonic accessor)."""
        return self._dataPrototype
        # Reference to the TransformationTechnology description contains transformer
        # specific and ISignal properties.
        self._transformer: Optional["Transformation"] = None

    @property
    def transformer(self) -> Optional["Transformation"]:
        """Get transformer (Pythonic accessor)."""
        return self._transformer

    @transformer.setter
    def transformer(self, value: Optional["Transformation"]) -> None:
        """
        Set transformer with validation.
        
        Args:
            value: The transformer to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._transformer = None
            return

        if not isinstance(value, Transformation):
            raise TypeError(
                f"transformer must be Transformation or None, got {type(value).__name__}"
            )
        self._transformer = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCsErrorReaction(self) -> "CSTransformerError":
        """
        AUTOSAR-compliant getter for csErrorReaction.
        
        Returns:
            The csErrorReaction value
        
        Note:
            Delegates to cs_error_reaction property (CODING_RULE_V2_00017)
        """
        return self.cs_error_reaction  # Delegates to property

    def setCsErrorReaction(self, value: "CSTransformerError") -> "TransformationISignalProps":
        """
        AUTOSAR-compliant setter for csErrorReaction with method chaining.
        
        Args:
            value: The csErrorReaction to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to cs_error_reaction property setter (gets validation automatically)
        """
        self.cs_error_reaction = value  # Delegates to property setter
        return self

    def getDataPrototype(self) -> List["RefType"]:
        """
        AUTOSAR-compliant getter for dataPrototype.
        
        Returns:
            The dataPrototype value
        
        Note:
            Delegates to data_prototype property (CODING_RULE_V2_00017)
        """
        return self.data_prototype  # Delegates to property

    def getTransformer(self) -> "Transformation":
        """
        AUTOSAR-compliant getter for transformer.
        
        Returns:
            The transformer value
        
        Note:
            Delegates to transformer property (CODING_RULE_V2_00017)
        """
        return self.transformer  # Delegates to property

    def setTransformer(self, value: "Transformation") -> "TransformationISignalProps":
        """
        AUTOSAR-compliant setter for transformer with method chaining.
        
        Args:
            value: The transformer to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to transformer property setter (gets validation automatically)
        """
        self.transformer = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_cs_error_reaction(self, value: Optional["CSTransformerError"]) -> "TransformationISignalProps":
        """
        Set csErrorReaction and return self for chaining.
        
        Args:
            value: The csErrorReaction to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_cs_error_reaction("value")
        """
        self.cs_error_reaction = value  # Use property setter (gets validation)
        return self

    def with_transformer(self, value: Optional["Transformation"]) -> "TransformationISignalProps":
        """
        Set transformer and return self for chaining.
        
        Args:
            value: The transformer to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_transformer("value")
        """
        self.transformer = value  # Use property setter (gets validation)
        return self



class SOMEIPTransformationISignalProps(ARObject):
    """
    The class SOMEIPTransformationISignalProps specifies ISignal specific
    configuration properties for SOME/IP transformer attributes.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Transformer::SOMEIPTransformationISignalProps
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 778, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute indicates that Strings in the SOME/IP shall NOT be serialized
                # according to the SOME/ specification for Strings.
        # attribute is set to true, BOM and null-termination be added in the
                # serialization for Strings in the this attribute is set to false (or not set)
                # BOM shall be added in the serialization for the payload according to the
                # SOME/IP Strings.
        # attribute is not future safe, and will be an upcoming AUTOSAR release!".
        self._implements: Optional["Boolean"] = None

    @property
    def implements(self) -> Optional["Boolean"]:
        """Get implements (Pythonic accessor)."""
        return self._implements

    @implements.setter
    def implements(self, value: Optional["Boolean"]) -> None:
        """
        Set implements with validation.
        
        Args:
            value: The implements to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._implements = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"implements must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._implements = value
        # The interface version the SOME/IP transformer shall use.
        self._interfaceVersion: Optional["PositiveInteger"] = None

    @property
    def interface_version(self) -> Optional["PositiveInteger"]:
        """Get interfaceVersion (Pythonic accessor)."""
        return self._interfaceVersion

    @interface_version.setter
    def interface_version(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set interfaceVersion with validation.
        
        Args:
            value: The interfaceVersion to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._interfaceVersion = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"interfaceVersion must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._interfaceVersion = value
        # This attribute shall be used to determine the wire type in context of using
        # the TLV encoding.
        self._isDynamic: Optional["Boolean"] = None

    @property
    def is_dynamic(self) -> Optional["Boolean"]:
        """Get isDynamic (Pythonic accessor)."""
        return self._isDynamic

    @is_dynamic.setter
    def is_dynamic(self, value: Optional["Boolean"]) -> None:
        """
        Set isDynamic with validation.
        
        Args:
            value: The isDynamic to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._isDynamic = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"isDynamic must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._isDynamic = value
        # The Message Type which shall be placed into the SOME/ header.
        self._messageType: Optional["SOMEIPMessageType"] = None

    @property
    def message_type(self) -> Optional["SOMEIPMessageType"]:
        """Get messageType (Pythonic accessor)."""
        return self._messageType

    @message_type.setter
    def message_type(self, value: Optional["SOMEIPMessageType"]) -> None:
        """
        Set messageType with validation.
        
        Args:
            value: The messageType to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._messageType = None
            return

        if not isinstance(value, SOMEIPMessageType):
            raise TypeError(
                f"messageType must be SOMEIPMessageType or None, got {type(value).__name__}"
            )
        self._messageType = value
        # The size of all length fields (in Bytes) of fixed-size arrays dynamic size
                # arrays in the SOME/IP message.
        # This valid for all available occurrences of fixed-size dynamic size arrays in
                # the SOME/IP message.
        self._sizeOfArray: Optional["PositiveInteger"] = None

    @property
    def size_of_array(self) -> Optional["PositiveInteger"]:
        """Get sizeOfArray (Pythonic accessor)."""
        return self._sizeOfArray

    @size_of_array.setter
    def size_of_array(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set sizeOfArray with validation.
        
        Args:
            value: The sizeOfArray to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sizeOfArray = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"sizeOfArray must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._sizeOfArray = value
        # The size of all length fields (in Bytes) of dynamic length in the SOME/IP
                # message.
        # This attribute is valid for occurrences of strings in the SOME/IP.
        self._sizeOfString: Optional["PositiveInteger"] = None

    @property
    def size_of_string(self) -> Optional["PositiveInteger"]:
        """Get sizeOfString (Pythonic accessor)."""
        return self._sizeOfString

    @size_of_string.setter
    def size_of_string(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set sizeOfString with validation.
        
        Args:
            value: The sizeOfString to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sizeOfString = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"sizeOfString must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._sizeOfString = value
        # The size of all length fields (in Bytes) of structs in the message.
        # This attribute is valid for all available structures in the SOME/IP message.
        # For fine granular modeling on the level of Data
                # DataPrototypeTransformationProps shall.
        self._sizeOfStruct: Optional["PositiveInteger"] = None

    @property
    def size_of_struct(self) -> Optional["PositiveInteger"]:
        """Get sizeOfStruct (Pythonic accessor)."""
        return self._sizeOfStruct

    @size_of_struct.setter
    def size_of_struct(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set sizeOfStruct with validation.
        
        Args:
            value: The sizeOfStruct to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sizeOfStruct = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"sizeOfStruct must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._sizeOfStruct = value
        # The size of all length fields (in Bytes) of unions in the message.
        # This attribute is valid for all available Unions in the SOME/IP message.
        # For a granular modeling on the level of Data DataPrototypeTransformationProps
                # shall.
        self._sizeOfUnion: Optional["PositiveInteger"] = None

    @property
    def size_of_union(self) -> Optional["PositiveInteger"]:
        """Get sizeOfUnion (Pythonic accessor)."""
        return self._sizeOfUnion

    @size_of_union.setter
    def size_of_union(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set sizeOfUnion with validation.
        
        Args:
            value: The sizeOfUnion to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sizeOfUnion = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"sizeOfUnion must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._sizeOfUnion = value
        # This reference identifies the TlvDataIdDefinitions relevant the enclosing
        # SOMEIPTransformationISignalProps.
        self._tlvDataId: List["RefType"] = []

    @property
    def tlv_data_id(self) -> List["RefType"]:
        """Get tlvDataId (Pythonic accessor)."""
        return self._tlvDataId

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getImplements(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for implements.
        
        Returns:
            The implements value
        
        Note:
            Delegates to implements property (CODING_RULE_V2_00017)
        """
        return self.implements  # Delegates to property

    def setImplements(self, value: "Boolean") -> "SOMEIPTransformationISignalProps":
        """
        AUTOSAR-compliant setter for implements with method chaining.
        
        Args:
            value: The implements to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to implements property setter (gets validation automatically)
        """
        self.implements = value  # Delegates to property setter
        return self

    def getInterfaceVersion(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for interfaceVersion.
        
        Returns:
            The interfaceVersion value
        
        Note:
            Delegates to interface_version property (CODING_RULE_V2_00017)
        """
        return self.interface_version  # Delegates to property

    def setInterfaceVersion(self, value: "PositiveInteger") -> "SOMEIPTransformationISignalProps":
        """
        AUTOSAR-compliant setter for interfaceVersion with method chaining.
        
        Args:
            value: The interfaceVersion to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to interface_version property setter (gets validation automatically)
        """
        self.interface_version = value  # Delegates to property setter
        return self

    def getIsDynamic(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for isDynamic.
        
        Returns:
            The isDynamic value
        
        Note:
            Delegates to is_dynamic property (CODING_RULE_V2_00017)
        """
        return self.is_dynamic  # Delegates to property

    def setIsDynamic(self, value: "Boolean") -> "SOMEIPTransformationISignalProps":
        """
        AUTOSAR-compliant setter for isDynamic with method chaining.
        
        Args:
            value: The isDynamic to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to is_dynamic property setter (gets validation automatically)
        """
        self.is_dynamic = value  # Delegates to property setter
        return self

    def getMessageType(self) -> "SOMEIPMessageType":
        """
        AUTOSAR-compliant getter for messageType.
        
        Returns:
            The messageType value
        
        Note:
            Delegates to message_type property (CODING_RULE_V2_00017)
        """
        return self.message_type  # Delegates to property

    def setMessageType(self, value: "SOMEIPMessageType") -> "SOMEIPTransformationISignalProps":
        """
        AUTOSAR-compliant setter for messageType with method chaining.
        
        Args:
            value: The messageType to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to message_type property setter (gets validation automatically)
        """
        self.message_type = value  # Delegates to property setter
        return self

    def getSizeOfArray(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for sizeOfArray.
        
        Returns:
            The sizeOfArray value
        
        Note:
            Delegates to size_of_array property (CODING_RULE_V2_00017)
        """
        return self.size_of_array  # Delegates to property

    def setSizeOfArray(self, value: "PositiveInteger") -> "SOMEIPTransformationISignalProps":
        """
        AUTOSAR-compliant setter for sizeOfArray with method chaining.
        
        Args:
            value: The sizeOfArray to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to size_of_array property setter (gets validation automatically)
        """
        self.size_of_array = value  # Delegates to property setter
        return self

    def getSizeOfString(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for sizeOfString.
        
        Returns:
            The sizeOfString value
        
        Note:
            Delegates to size_of_string property (CODING_RULE_V2_00017)
        """
        return self.size_of_string  # Delegates to property

    def setSizeOfString(self, value: "PositiveInteger") -> "SOMEIPTransformationISignalProps":
        """
        AUTOSAR-compliant setter for sizeOfString with method chaining.
        
        Args:
            value: The sizeOfString to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to size_of_string property setter (gets validation automatically)
        """
        self.size_of_string = value  # Delegates to property setter
        return self

    def getSizeOfStruct(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for sizeOfStruct.
        
        Returns:
            The sizeOfStruct value
        
        Note:
            Delegates to size_of_struct property (CODING_RULE_V2_00017)
        """
        return self.size_of_struct  # Delegates to property

    def setSizeOfStruct(self, value: "PositiveInteger") -> "SOMEIPTransformationISignalProps":
        """
        AUTOSAR-compliant setter for sizeOfStruct with method chaining.
        
        Args:
            value: The sizeOfStruct to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to size_of_struct property setter (gets validation automatically)
        """
        self.size_of_struct = value  # Delegates to property setter
        return self

    def getSizeOfUnion(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for sizeOfUnion.
        
        Returns:
            The sizeOfUnion value
        
        Note:
            Delegates to size_of_union property (CODING_RULE_V2_00017)
        """
        return self.size_of_union  # Delegates to property

    def setSizeOfUnion(self, value: "PositiveInteger") -> "SOMEIPTransformationISignalProps":
        """
        AUTOSAR-compliant setter for sizeOfUnion with method chaining.
        
        Args:
            value: The sizeOfUnion to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to size_of_union property setter (gets validation automatically)
        """
        self.size_of_union = value  # Delegates to property setter
        return self

    def getTlvDataId(self) -> List["RefType"]:
        """
        AUTOSAR-compliant getter for tlvDataId.
        
        Returns:
            The tlvDataId value
        
        Note:
            Delegates to tlv_data_id property (CODING_RULE_V2_00017)
        """
        return self.tlv_data_id  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_implements(self, value: Optional["Boolean"]) -> "SOMEIPTransformationISignalProps":
        """
        Set implements and return self for chaining.
        
        Args:
            value: The implements to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_implements("value")
        """
        self.implements = value  # Use property setter (gets validation)
        return self

    def with_interface_version(self, value: Optional["PositiveInteger"]) -> "SOMEIPTransformationISignalProps":
        """
        Set interfaceVersion and return self for chaining.
        
        Args:
            value: The interfaceVersion to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_interface_version("value")
        """
        self.interface_version = value  # Use property setter (gets validation)
        return self

    def with_is_dynamic(self, value: Optional["Boolean"]) -> "SOMEIPTransformationISignalProps":
        """
        Set isDynamic and return self for chaining.
        
        Args:
            value: The isDynamic to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_is_dynamic("value")
        """
        self.is_dynamic = value  # Use property setter (gets validation)
        return self

    def with_message_type(self, value: Optional["SOMEIPMessageType"]) -> "SOMEIPTransformationISignalProps":
        """
        Set messageType and return self for chaining.
        
        Args:
            value: The messageType to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_message_type("value")
        """
        self.message_type = value  # Use property setter (gets validation)
        return self

    def with_size_of_array(self, value: Optional["PositiveInteger"]) -> "SOMEIPTransformationISignalProps":
        """
        Set sizeOfArray and return self for chaining.
        
        Args:
            value: The sizeOfArray to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_size_of_array("value")
        """
        self.size_of_array = value  # Use property setter (gets validation)
        return self

    def with_size_of_string(self, value: Optional["PositiveInteger"]) -> "SOMEIPTransformationISignalProps":
        """
        Set sizeOfString and return self for chaining.
        
        Args:
            value: The sizeOfString to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_size_of_string("value")
        """
        self.size_of_string = value  # Use property setter (gets validation)
        return self

    def with_size_of_struct(self, value: Optional["PositiveInteger"]) -> "SOMEIPTransformationISignalProps":
        """
        Set sizeOfStruct and return self for chaining.
        
        Args:
            value: The sizeOfStruct to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_size_of_struct("value")
        """
        self.size_of_struct = value  # Use property setter (gets validation)
        return self

    def with_size_of_union(self, value: Optional["PositiveInteger"]) -> "SOMEIPTransformationISignalProps":
        """
        Set sizeOfUnion and return self for chaining.
        
        Args:
            value: The sizeOfUnion to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_size_of_union("value")
        """
        self.size_of_union = value  # Use property setter (gets validation)
        return self



class TransformationPropsSet(ARElement):
    """
    Collection of TransformationProps.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Transformer::TransformationPropsSet
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 782, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Transformer specific configuration properties.
        self._transformationProps: List["TransformationProps"] = []

    @property
    def transformation_props(self) -> List["TransformationProps"]:
        """Get transformationProps (Pythonic accessor)."""
        return self._transformationProps

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTransformationProps(self) -> List["TransformationProps"]:
        """
        AUTOSAR-compliant getter for transformationProps.
        
        Returns:
            The transformationProps value
        
        Note:
            Delegates to transformation_props property (CODING_RULE_V2_00017)
        """
        return self.transformation_props  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class TransformationProps(Identifiable, ABC):
    """
    This meta-class represents a abstract base class for transformation
    settings.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Transformer::TransformationProps
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 782, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is TransformationProps:
            raise TypeError("TransformationProps is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class DataPrototypeTransformationProps(ARObject):
    """
    DataPrototypeTransformationProps allows to set the attributes for the
    different Transformation Technologies that are DataPrototype specific.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Transformer::DataPrototypeTransformationProps
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 787, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to a DataPrototype that is transported in the serialized ISignal.
        self._dataPrototypeIn: Optional["RefType"] = None

    @property
    def data_prototype_in(self) -> Optional["RefType"]:
        """Get dataPrototypeIn (Pythonic accessor)."""
        return self._dataPrototypeIn

    @data_prototype_in.setter
    def data_prototype_in(self, value: Optional["RefType"]) -> None:
        """
        Set dataPrototypeIn with validation.
        
        Args:
            value: The dataPrototypeIn to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dataPrototypeIn = None
            return

        self._dataPrototypeIn = value
        # Specification of the actual network representation for the primitive
                # DataPrototype.
        # If a network is provided then the baseType shall be the Transformer as input
                # for the serialization/.
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
        # Collection of AutosarDataPrototype related configuration for a transformer.
        self._transformation: Optional["TransformationProps"] = None

    @property
    def transformation(self) -> Optional["TransformationProps"]:
        """Get transformation (Pythonic accessor)."""
        return self._transformation

    @transformation.setter
    def transformation(self, value: Optional["TransformationProps"]) -> None:
        """
        Set transformation with validation.
        
        Args:
            value: The transformation to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._transformation = None
            return

        if not isinstance(value, TransformationProps):
            raise TypeError(
                f"transformation must be TransformationProps or None, got {type(value).__name__}"
            )
        self._transformation = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDataPrototypeIn(self) -> "RefType":
        """
        AUTOSAR-compliant getter for dataPrototypeIn.
        
        Returns:
            The dataPrototypeIn value
        
        Note:
            Delegates to data_prototype_in property (CODING_RULE_V2_00017)
        """
        return self.data_prototype_in  # Delegates to property

    def setDataPrototypeIn(self, value: "RefType") -> "DataPrototypeTransformationProps":
        """
        AUTOSAR-compliant setter for dataPrototypeIn with method chaining.
        
        Args:
            value: The dataPrototypeIn to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to data_prototype_in property setter (gets validation automatically)
        """
        self.data_prototype_in = value  # Delegates to property setter
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

    def setNetwork(self, value: "SwDataDefProps") -> "DataPrototypeTransformationProps":
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

    def getTransformation(self) -> "TransformationProps":
        """
        AUTOSAR-compliant getter for transformation.
        
        Returns:
            The transformation value
        
        Note:
            Delegates to transformation property (CODING_RULE_V2_00017)
        """
        return self.transformation  # Delegates to property

    def setTransformation(self, value: "TransformationProps") -> "DataPrototypeTransformationProps":
        """
        AUTOSAR-compliant setter for transformation with method chaining.
        
        Args:
            value: The transformation to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to transformation property setter (gets validation automatically)
        """
        self.transformation = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_data_prototype_in(self, value: Optional[RefType]) -> "DataPrototypeTransformationProps":
        """
        Set dataPrototypeIn and return self for chaining.
        
        Args:
            value: The dataPrototypeIn to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_data_prototype_in("value")
        """
        self.data_prototype_in = value  # Use property setter (gets validation)
        return self

    def with_network(self, value: Optional["SwDataDefProps"]) -> "DataPrototypeTransformationProps":
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

    def with_transformation(self, value: Optional["TransformationProps"]) -> "DataPrototypeTransformationProps":
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



class DataPrototypeReference(ARObject, ABC):
    """
    This meta-class provides the ability to reference a DataPrototype.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Transformer::DataPrototypeReference
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 787, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is DataPrototypeReference:
            raise TypeError("DataPrototypeReference is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute represents the ability to specify a tag-id for of a specific
        # DataPrototype in the context (potentially deeply-nested) composite data
        # structure.
        self._tagId: Optional["PositiveInteger"] = None

    @property
    def tag_id(self) -> Optional["PositiveInteger"]:
        """Get tagId (Pythonic accessor)."""
        return self._tagId

    @tag_id.setter
    def tag_id(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set tagId with validation.
        
        Args:
            value: The tagId to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tagId = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"tagId must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._tagId = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTagId(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for tagId.
        
        Returns:
            The tagId value
        
        Note:
            Delegates to tag_id property (CODING_RULE_V2_00017)
        """
        return self.tag_id  # Delegates to property

    def setTagId(self, value: "PositiveInteger") -> "DataPrototypeReference":
        """
        AUTOSAR-compliant setter for tagId with method chaining.
        
        Args:
            value: The tagId to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to tag_id property setter (gets validation automatically)
        """
        self.tag_id = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_tag_id(self, value: Optional["PositiveInteger"]) -> "DataPrototypeReference":
        """
        Set tagId and return self for chaining.
        
        Args:
            value: The tagId to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_tag_id("value")
        """
        self.tag_id = value  # Use property setter (gets validation)
        return self



class EndToEndTransformationISignalProps(ARObject):
    """
    Holds all the ISignal specific attributes for the EndToEndTransformer.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Transformer::EndToEndTransformationISignalProps
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 808, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Length of payload and E2E header in bits.
        self._dataLength: Optional["PositiveInteger"] = None

    @property
    def data_length(self) -> Optional["PositiveInteger"]:
        """Get dataLength (Pythonic accessor)."""
        return self._dataLength

    @data_length.setter
    def data_length(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set dataLength with validation.
        
        Args:
            value: The dataLength to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dataLength = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"dataLength must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._dataLength = value
        # Maximum length of payload and E2E header in bits.
        self._maxDataLength: Optional["PositiveInteger"] = None

    @property
    def max_data_length(self) -> Optional["PositiveInteger"]:
        """Get maxDataLength (Pythonic accessor)."""
        return self._maxDataLength

    @max_data_length.setter
    def max_data_length(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set maxDataLength with validation.
        
        Args:
            value: The maxDataLength to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxDataLength = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"maxDataLength must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._maxDataLength = value
        # Minimum length of payload and E2E header in bits.
        # 2090 Document ID 63: AUTOSAR_CP_TPS_SystemTemplate R23-11.
        self._minDataLength: Optional["PositiveInteger"] = None

    @property
    def min_data_length(self) -> Optional["PositiveInteger"]:
        """Get minDataLength (Pythonic accessor)."""
        return self._minDataLength

    @min_data_length.setter
    def min_data_length(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set minDataLength with validation.
        
        Args:
            value: The minDataLength to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._minDataLength = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"minDataLength must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._minDataLength = value
        # This attribute represents a unique numerical identifier source of a certain
                # transmission.
        # In case of this ID uniquely identifies the client.
        # is used for protection against masquerading.
        # concerning the maximum number of values is specific for each E2E profile)
                # this attribute are controlled by a semantic depends on the category of the
                # EndToEnd.
        self._sourceId: Optional["PositiveInteger"] = None

    @property
    def source_id(self) -> Optional["PositiveInteger"]:
        """Get sourceId (Pythonic accessor)."""
        return self._sourceId

    @source_id.setter
    def source_id(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set sourceId with validation.
        
        Args:
            value: The sourceId to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sourceId = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"sourceId must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._sourceId = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDataLength(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for dataLength.
        
        Returns:
            The dataLength value
        
        Note:
            Delegates to data_length property (CODING_RULE_V2_00017)
        """
        return self.data_length  # Delegates to property

    def setDataLength(self, value: "PositiveInteger") -> "EndToEndTransformationISignalProps":
        """
        AUTOSAR-compliant setter for dataLength with method chaining.
        
        Args:
            value: The dataLength to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to data_length property setter (gets validation automatically)
        """
        self.data_length = value  # Delegates to property setter
        return self

    def getMaxDataLength(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for maxDataLength.
        
        Returns:
            The maxDataLength value
        
        Note:
            Delegates to max_data_length property (CODING_RULE_V2_00017)
        """
        return self.max_data_length  # Delegates to property

    def setMaxDataLength(self, value: "PositiveInteger") -> "EndToEndTransformationISignalProps":
        """
        AUTOSAR-compliant setter for maxDataLength with method chaining.
        
        Args:
            value: The maxDataLength to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to max_data_length property setter (gets validation automatically)
        """
        self.max_data_length = value  # Delegates to property setter
        return self

    def getMinDataLength(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for minDataLength.
        
        Returns:
            The minDataLength value
        
        Note:
            Delegates to min_data_length property (CODING_RULE_V2_00017)
        """
        return self.min_data_length  # Delegates to property

    def setMinDataLength(self, value: "PositiveInteger") -> "EndToEndTransformationISignalProps":
        """
        AUTOSAR-compliant setter for minDataLength with method chaining.
        
        Args:
            value: The minDataLength to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to min_data_length property setter (gets validation automatically)
        """
        self.min_data_length = value  # Delegates to property setter
        return self

    def getSourceId(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for sourceId.
        
        Returns:
            The sourceId value
        
        Note:
            Delegates to source_id property (CODING_RULE_V2_00017)
        """
        return self.source_id  # Delegates to property

    def setSourceId(self, value: "PositiveInteger") -> "EndToEndTransformationISignalProps":
        """
        AUTOSAR-compliant setter for sourceId with method chaining.
        
        Args:
            value: The sourceId to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to source_id property setter (gets validation automatically)
        """
        self.source_id = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_data_length(self, value: Optional["PositiveInteger"]) -> "EndToEndTransformationISignalProps":
        """
        Set dataLength and return self for chaining.
        
        Args:
            value: The dataLength to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_data_length("value")
        """
        self.data_length = value  # Use property setter (gets validation)
        return self

    def with_max_data_length(self, value: Optional["PositiveInteger"]) -> "EndToEndTransformationISignalProps":
        """
        Set maxDataLength and return self for chaining.
        
        Args:
            value: The maxDataLength to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_max_data_length("value")
        """
        self.max_data_length = value  # Use property setter (gets validation)
        return self

    def with_min_data_length(self, value: Optional["PositiveInteger"]) -> "EndToEndTransformationISignalProps":
        """
        Set minDataLength and return self for chaining.
        
        Args:
            value: The minDataLength to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_min_data_length("value")
        """
        self.min_data_length = value  # Use property setter (gets validation)
        return self

    def with_source_id(self, value: Optional["PositiveInteger"]) -> "EndToEndTransformationISignalProps":
        """
        Set sourceId and return self for chaining.
        
        Args:
            value: The sourceId to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_source_id("value")
        """
        self.source_id = value  # Use property setter (gets validation)
        return self



class UserDefinedTransformationISignalProps(ARObject):
    """
    The UserDefinedTransformationISignalProps is used to specify ISignal
    specific configuration properties for custom transformers.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Transformer::UserDefinedTransformationISignalProps
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 828, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class TlvDataIdDefinitionSet(ARElement):
    """
    This meta-class acts as a container of TlvDataIdDefinitions to be used in a
    given context
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Transformer::TlvDataIdDefinitionSet
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 830, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This aggregation represents the collection of TlVDataTid aggregated by the
        # TlvDataIdDefinitionSet.
        self._tlvDataId: List["TlvDataIdDefinition"] = []

    @property
    def tlv_data_id(self) -> List["TlvDataIdDefinition"]:
        """Get tlvDataId (Pythonic accessor)."""
        return self._tlvDataId

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getTlvDataId(self) -> List["TlvDataIdDefinition"]:
        """
        AUTOSAR-compliant getter for tlvDataId.
        
        Returns:
            The tlvDataId value
        
        Note:
            Delegates to tlv_data_id property (CODING_RULE_V2_00017)
        """
        return self.tlv_data_id  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class TlvDataIdDefinition(ARObject):
    """
    This meta-class represents the ability to define the tlvDataId.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Transformer::TlvDataIdDefinition
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 830, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute represents the definition of the value of the.
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

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"id must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._id = value
        # This reference assigns a tlvDataId to a given argument of.
        self._tlvArgument: Optional["RefType"] = None

    @property
    def tlv_argument(self) -> Optional["RefType"]:
        """Get tlvArgument (Pythonic accessor)."""
        return self._tlvArgument

    @tlv_argument.setter
    def tlv_argument(self, value: Optional["RefType"]) -> None:
        """
        Set tlvArgument with validation.
        
        Args:
            value: The tlvArgument to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tlvArgument = None
            return

        self._tlvArgument = value
        # This reference associates the definition of a TLV data id with a given
        # AbstractImplementationDataTypeElement.
        self._tlv: Optional["AbstractImplementation"] = None

    @property
    def tlv(self) -> Optional["AbstractImplementation"]:
        """Get tlv (Pythonic accessor)."""
        return self._tlv

    @tlv.setter
    def tlv(self, value: Optional["AbstractImplementation"]) -> None:
        """
        Set tlv with validation.
        
        Args:
            value: The tlv to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tlv = None
            return

        if not isinstance(value, AbstractImplementation):
            raise TypeError(
                f"tlv must be AbstractImplementation or None, got {type(value).__name__}"
            )
        self._tlv = value
        # This reference associates the definition of a TLV data id with a given
        # ApplicationRecordElement.
        self._tlvRecord: Optional["ApplicationRecord"] = None

    @property
    def tlv_record(self) -> Optional["ApplicationRecord"]:
        """Get tlvRecord (Pythonic accessor)."""
        return self._tlvRecord

    @tlv_record.setter
    def tlv_record(self, value: Optional["ApplicationRecord"]) -> None:
        """
        Set tlvRecord with validation.
        
        Args:
            value: The tlvRecord to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._tlvRecord = None
            return

        if not isinstance(value, ApplicationRecord):
            raise TypeError(
                f"tlvRecord must be ApplicationRecord or None, got {type(value).__name__}"
            )
        self._tlvRecord = value

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

    def setId(self, value: "PositiveInteger") -> "TlvDataIdDefinition":
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

    def getTlvArgument(self) -> "RefType":
        """
        AUTOSAR-compliant getter for tlvArgument.
        
        Returns:
            The tlvArgument value
        
        Note:
            Delegates to tlv_argument property (CODING_RULE_V2_00017)
        """
        return self.tlv_argument  # Delegates to property

    def setTlvArgument(self, value: "RefType") -> "TlvDataIdDefinition":
        """
        AUTOSAR-compliant setter for tlvArgument with method chaining.
        
        Args:
            value: The tlvArgument to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to tlv_argument property setter (gets validation automatically)
        """
        self.tlv_argument = value  # Delegates to property setter
        return self

    def getTlv(self) -> "AbstractImplementation":
        """
        AUTOSAR-compliant getter for tlv.
        
        Returns:
            The tlv value
        
        Note:
            Delegates to tlv property (CODING_RULE_V2_00017)
        """
        return self.tlv  # Delegates to property

    def setTlv(self, value: "AbstractImplementation") -> "TlvDataIdDefinition":
        """
        AUTOSAR-compliant setter for tlv with method chaining.
        
        Args:
            value: The tlv to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to tlv property setter (gets validation automatically)
        """
        self.tlv = value  # Delegates to property setter
        return self

    def getTlvRecord(self) -> "ApplicationRecord":
        """
        AUTOSAR-compliant getter for tlvRecord.
        
        Returns:
            The tlvRecord value
        
        Note:
            Delegates to tlv_record property (CODING_RULE_V2_00017)
        """
        return self.tlv_record  # Delegates to property

    def setTlvRecord(self, value: "ApplicationRecord") -> "TlvDataIdDefinition":
        """
        AUTOSAR-compliant setter for tlvRecord with method chaining.
        
        Args:
            value: The tlvRecord to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to tlv_record property setter (gets validation automatically)
        """
        self.tlv_record = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_id(self, value: Optional["PositiveInteger"]) -> "TlvDataIdDefinition":
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

    def with_tlv_argument(self, value: Optional[RefType]) -> "TlvDataIdDefinition":
        """
        Set tlvArgument and return self for chaining.
        
        Args:
            value: The tlvArgument to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_tlv_argument("value")
        """
        self.tlv_argument = value  # Use property setter (gets validation)
        return self

    def with_tlv(self, value: Optional["AbstractImplementation"]) -> "TlvDataIdDefinition":
        """
        Set tlv and return self for chaining.
        
        Args:
            value: The tlv to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_tlv("value")
        """
        self.tlv = value  # Use property setter (gets validation)
        return self

    def with_tlv_record(self, value: Optional["ApplicationRecord"]) -> "TlvDataIdDefinition":
        """
        Set tlvRecord and return self for chaining.
        
        Args:
            value: The tlvRecord to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_tlv_record("value")
        """
        self.tlv_record = value  # Use property setter (gets validation)
        return self



class EndToEndTransformationDescription(TransformationDescription):
    """
    EndToEndTransformationDescription holds these attributes which are profile
    specific and have the same value for all E2E transformers.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Transformer::EndToEndTransformationDescription
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 987, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 806, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Clear monitoring window on transition from state Valid to Invalid.
        self._clearFromValid: Optional["Boolean"] = None

    @property
    def clear_from_valid(self) -> Optional["Boolean"]:
        """Get clearFromValid (Pythonic accessor)."""
        return self._clearFromValid

    @clear_from_valid.setter
    def clear_from_valid(self, value: Optional["Boolean"]) -> None:
        """
        Set clearFromValid with validation.
        
        Args:
            value: The clearFromValid to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._clearFromValid = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"clearFromValid must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._clearFromValid = value
        # Offset of the counter in the Data[] array in bits.
        self._counterOffset: Optional["PositiveInteger"] = None

    @property
    def counter_offset(self) -> Optional["PositiveInteger"]:
        """Get counterOffset (Pythonic accessor)."""
        return self._counterOffset

    @counter_offset.setter
    def counter_offset(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set counterOffset with validation.
        
        Args:
            value: The counterOffset to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._counterOffset = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"counterOffset must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._counterOffset = value
        # Offset of the CRC in the Data[] array in bits.
        self._crcOffset: Optional["PositiveInteger"] = None

    @property
    def crc_offset(self) -> Optional["PositiveInteger"]:
        """Get crcOffset (Pythonic accessor)."""
        return self._crcOffset

    @crc_offset.setter
    def crc_offset(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set crcOffset with validation.
        
        Args:
            value: The crcOffset to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._crcOffset = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"crcOffset must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._crcOffset = value
        # This attribute describes the inclusion mode that is used to implicit two-byte
        # Data ID in the one-byte CRC.
        self._dataIdMode: Optional["DataIdModeEnum"] = None

    @property
    def data_id_mode(self) -> Optional["DataIdModeEnum"]:
        """Get dataIdMode (Pythonic accessor)."""
        return self._dataIdMode

    @data_id_mode.setter
    def data_id_mode(self, value: Optional["DataIdModeEnum"]) -> None:
        """
        Set dataIdMode with validation.
        
        Args:
            value: The dataIdMode to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dataIdMode = None
            return

        if not isinstance(value, DataIdModeEnum):
            raise TypeError(
                f"dataIdMode must be DataIdModeEnum or None, got {type(value).__name__}"
            )
        self._dataIdMode = value
        # Offset of the Data ID nibble in the Data[] array in bits.
        # 1228 Document ID 62: AUTOSAR_CP_TPS_SoftwareComponentTemplate Template
                # R23-11.
        self._dataIdNibble: Optional["PositiveInteger"] = None

    @property
    def data_id_nibble(self) -> Optional["PositiveInteger"]:
        """Get dataIdNibble (Pythonic accessor)."""
        return self._dataIdNibble

    @data_id_nibble.setter
    def data_id_nibble(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set dataIdNibble with validation.
        
        Args:
            value: The dataIdNibble to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dataIdNibble = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"dataIdNibble must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._dataIdNibble = value
        # Reference to additional settings for the E2E state machine.
        self._e2eProfile: Optional["E2EProfileCompatibility"] = None

    @property
    def e2e_profile(self) -> Optional["E2EProfileCompatibility"]:
        """Get e2eProfile (Pythonic accessor)."""
        return self._e2eProfile

    @e2e_profile.setter
    def e2e_profile(self, value: Optional["E2EProfileCompatibility"]) -> None:
        """
        Set e2eProfile with validation.
        
        Args:
            value: The e2eProfile to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._e2eProfile = None
            return

        if not isinstance(value, E2EProfileCompatibility):
            raise TypeError(
                f"e2eProfile must be E2EProfileCompatibility or None, got {type(value).__name__}"
            )
        self._e2eProfile = value
        # Maximum allowed difference between two counter values two consecutively
                # received valid messages.
        # For the receiver gets data with counter 1 and Max 3, then at the next
                # reception the receiver Counters with values 2, 3 or 4.
        self._maxDelta: Optional["PositiveInteger"] = None

    @property
    def max_delta(self) -> Optional["PositiveInteger"]:
        """Get maxDelta (Pythonic accessor)."""
        return self._maxDelta

    @max_delta.setter
    def max_delta(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set maxDelta with validation.
        
        Args:
            value: The maxDelta to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxDelta = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"maxDelta must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._maxDelta = value
        # Maximal number of checks in which ProfileStatus equal to was determined,
        # within the last Window for the state E2E_SM_VALID.
        self._maxErrorState: Optional["PositiveInteger"] = None

    @property
    def max_error_state(self) -> Optional["PositiveInteger"]:
        """Get maxErrorState (Pythonic accessor)."""
        return self._maxErrorState

    @max_error_state.setter
    def max_error_state(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set maxErrorState with validation.
        
        Args:
            value: The maxErrorState to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxErrorState = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"maxErrorState must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._maxErrorState = value
        # The maximum allowed amount of consecutive failed checks.
        self._maxNoNewOr: Optional["PositiveInteger"] = None

    @property
    def max_no_new_or(self) -> Optional["PositiveInteger"]:
        """Get maxNoNewOr (Pythonic accessor)."""
        return self._maxNoNewOr

    @max_no_new_or.setter
    def max_no_new_or(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set maxNoNewOr with validation.
        
        Args:
            value: The maxNoNewOr to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxNoNewOr = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"maxNoNewOr must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._maxNoNewOr = value
        # Minimal number of checks in which ProfileStatus equal to determined, within
        # the last WindowSize the state E2E_SM_INIT.
        self._minOkStateInit: Optional["PositiveInteger"] = None

    @property
    def min_ok_state_init(self) -> Optional["PositiveInteger"]:
        """Get minOkStateInit (Pythonic accessor)."""
        return self._minOkStateInit

    @min_ok_state_init.setter
    def min_ok_state_init(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set minOkStateInit with validation.
        
        Args:
            value: The minOkStateInit to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._minOkStateInit = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"minOkStateInit must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._minOkStateInit = value
        # Minimal number of checks in which ProfileStatus equal to was determined,
        # within the last WindowSize the state E2E_SM_VALID.
        self._minOkState: Optional["PositiveInteger"] = None

    @property
    def min_ok_state(self) -> Optional["PositiveInteger"]:
        """Get minOkState (Pythonic accessor)."""
        return self._minOkState

    @min_ok_state.setter
    def min_ok_state(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set minOkState with validation.
        
        Args:
            value: The minOkState to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._minOkState = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"minOkState must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._minOkState = value
        # Offset of the E2E header in the Data[] array in bits.
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
        # Behavior of the check functionality.
        self._profileBehaviorBehaviorEnum: Optional["EndToEndProfile"] = None

    @property
    def profile_behavior_behavior_enum(self) -> Optional["EndToEndProfile"]:
        """Get profileBehaviorBehaviorEnum (Pythonic accessor)."""
        return self._profileBehaviorBehaviorEnum

    @profile_behavior_behavior_enum.setter
    def profile_behavior_behavior_enum(self, value: Optional["EndToEndProfile"]) -> None:
        """
        Set profileBehaviorBehaviorEnum with validation.
        
        Args:
            value: The profileBehaviorBehaviorEnum to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._profileBehaviorBehaviorEnum = None
            return

        if not isinstance(value, EndToEndProfile):
            raise TypeError(
                f"profileBehaviorBehaviorEnum must be EndToEndProfile or None, got {type(value).__name__}"
            )
        self._profileBehaviorBehaviorEnum = value
        # Definition of the E2E profile.
        self._profileName: Optional["NameToken"] = None

    @property
    def profile_name(self) -> Optional["NameToken"]:
        """Get profileName (Pythonic accessor)."""
        return self._profileName

    @profile_name.setter
    def profile_name(self, value: Optional["NameToken"]) -> None:
        """
        Set profileName with validation.
        
        Args:
            value: The profileName to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._profileName = None
            return

        if not isinstance(value, (NameToken, str)):
            raise TypeError(
                f"profileName must be NameToken or str or None, got {type(value).__name__}"
            )
        self._profileName = value
        # Number of checks required for validating the consistency counter that shall
        # be received with a valid counter within the allowed lock-in range) after the
        # an unexpected behavior of a received.
        self._syncCounterInit: Optional["PositiveInteger"] = None

    @property
    def sync_counter_init(self) -> Optional["PositiveInteger"]:
        """Get syncCounterInit (Pythonic accessor)."""
        return self._syncCounterInit

    @sync_counter_init.setter
    def sync_counter_init(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set syncCounterInit with validation.
        
        Args:
            value: The syncCounterInit to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._syncCounterInit = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"syncCounterInit must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._syncCounterInit = value
        # This attribute describes the number of upper-header bits be shifted.
        # 0 or not present: shift of upper header is NOT 0: the E2E Transformer on the
                # protect-side, takes upperHeaderBitsToShift bits from the upper buffer header
                # part generated by SOME/IP shifts them towards the lower bytes and the Data[]
                # for the length of the E2E header bytes in case of E2E Profile 4).
        # This means the is fixed - it depends on the E2E header size is configured
                # here is the number of bits that are to This option is defined because the
                # Some/IP by SOME/IP transformer shall be, due between non-protected and at the
                # same position, before E2E header.
        self._upperHeader: Optional["PositiveInteger"] = None

    @property
    def upper_header(self) -> Optional["PositiveInteger"]:
        """Get upperHeader (Pythonic accessor)."""
        return self._upperHeader

    @upper_header.setter
    def upper_header(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set upperHeader with validation.
        
        Args:
            value: The upperHeader to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._upperHeader = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"upperHeader must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._upperHeader = value
        # Size of the monitoring window of state Init for the E2E 1228 Document ID 62:
        # AUTOSAR_CP_TPS_SoftwareComponentTemplate Template R23-11.
        self._windowSizeInit: Optional["PositiveInteger"] = None

    @property
    def window_size_init(self) -> Optional["PositiveInteger"]:
        """Get windowSizeInit (Pythonic accessor)."""
        return self._windowSizeInit

    @window_size_init.setter
    def window_size_init(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set windowSizeInit with validation.
        
        Args:
            value: The windowSizeInit to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._windowSizeInit = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"windowSizeInit must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._windowSizeInit = value
        # Size of the monitoring window of state Valid for the E2E machine.
        self._windowSize: Optional["PositiveInteger"] = None

    @property
    def window_size(self) -> Optional["PositiveInteger"]:
        """Get windowSize (Pythonic accessor)."""
        return self._windowSize

    @window_size.setter
    def window_size(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set windowSize with validation.
        
        Args:
            value: The windowSize to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._windowSize = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"windowSize must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._windowSize = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getClearFromValid(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for clearFromValid.
        
        Returns:
            The clearFromValid value
        
        Note:
            Delegates to clear_from_valid property (CODING_RULE_V2_00017)
        """
        return self.clear_from_valid  # Delegates to property

    def setClearFromValid(self, value: "Boolean") -> "EndToEndTransformationDescription":
        """
        AUTOSAR-compliant setter for clearFromValid with method chaining.
        
        Args:
            value: The clearFromValid to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to clear_from_valid property setter (gets validation automatically)
        """
        self.clear_from_valid = value  # Delegates to property setter
        return self

    def getCounterOffset(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for counterOffset.
        
        Returns:
            The counterOffset value
        
        Note:
            Delegates to counter_offset property (CODING_RULE_V2_00017)
        """
        return self.counter_offset  # Delegates to property

    def setCounterOffset(self, value: "PositiveInteger") -> "EndToEndTransformationDescription":
        """
        AUTOSAR-compliant setter for counterOffset with method chaining.
        
        Args:
            value: The counterOffset to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to counter_offset property setter (gets validation automatically)
        """
        self.counter_offset = value  # Delegates to property setter
        return self

    def getCrcOffset(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for crcOffset.
        
        Returns:
            The crcOffset value
        
        Note:
            Delegates to crc_offset property (CODING_RULE_V2_00017)
        """
        return self.crc_offset  # Delegates to property

    def setCrcOffset(self, value: "PositiveInteger") -> "EndToEndTransformationDescription":
        """
        AUTOSAR-compliant setter for crcOffset with method chaining.
        
        Args:
            value: The crcOffset to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to crc_offset property setter (gets validation automatically)
        """
        self.crc_offset = value  # Delegates to property setter
        return self

    def getDataIdMode(self) -> "DataIdModeEnum":
        """
        AUTOSAR-compliant getter for dataIdMode.
        
        Returns:
            The dataIdMode value
        
        Note:
            Delegates to data_id_mode property (CODING_RULE_V2_00017)
        """
        return self.data_id_mode  # Delegates to property

    def setDataIdMode(self, value: "DataIdModeEnum") -> "EndToEndTransformationDescription":
        """
        AUTOSAR-compliant setter for dataIdMode with method chaining.
        
        Args:
            value: The dataIdMode to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to data_id_mode property setter (gets validation automatically)
        """
        self.data_id_mode = value  # Delegates to property setter
        return self

    def getDataIdNibble(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for dataIdNibble.
        
        Returns:
            The dataIdNibble value
        
        Note:
            Delegates to data_id_nibble property (CODING_RULE_V2_00017)
        """
        return self.data_id_nibble  # Delegates to property

    def setDataIdNibble(self, value: "PositiveInteger") -> "EndToEndTransformationDescription":
        """
        AUTOSAR-compliant setter for dataIdNibble with method chaining.
        
        Args:
            value: The dataIdNibble to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to data_id_nibble property setter (gets validation automatically)
        """
        self.data_id_nibble = value  # Delegates to property setter
        return self

    def getE2eProfile(self) -> "E2EProfileCompatibility":
        """
        AUTOSAR-compliant getter for e2eProfile.
        
        Returns:
            The e2eProfile value
        
        Note:
            Delegates to e2e_profile property (CODING_RULE_V2_00017)
        """
        return self.e2e_profile  # Delegates to property

    def setE2eProfile(self, value: "E2EProfileCompatibility") -> "EndToEndTransformationDescription":
        """
        AUTOSAR-compliant setter for e2eProfile with method chaining.
        
        Args:
            value: The e2eProfile to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to e2e_profile property setter (gets validation automatically)
        """
        self.e2e_profile = value  # Delegates to property setter
        return self

    def getMaxDelta(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for maxDelta.
        
        Returns:
            The maxDelta value
        
        Note:
            Delegates to max_delta property (CODING_RULE_V2_00017)
        """
        return self.max_delta  # Delegates to property

    def setMaxDelta(self, value: "PositiveInteger") -> "EndToEndTransformationDescription":
        """
        AUTOSAR-compliant setter for maxDelta with method chaining.
        
        Args:
            value: The maxDelta to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to max_delta property setter (gets validation automatically)
        """
        self.max_delta = value  # Delegates to property setter
        return self

    def getMaxErrorState(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for maxErrorState.
        
        Returns:
            The maxErrorState value
        
        Note:
            Delegates to max_error_state property (CODING_RULE_V2_00017)
        """
        return self.max_error_state  # Delegates to property

    def setMaxErrorState(self, value: "PositiveInteger") -> "EndToEndTransformationDescription":
        """
        AUTOSAR-compliant setter for maxErrorState with method chaining.
        
        Args:
            value: The maxErrorState to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to max_error_state property setter (gets validation automatically)
        """
        self.max_error_state = value  # Delegates to property setter
        return self

    def getMaxNoNewOr(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for maxNoNewOr.
        
        Returns:
            The maxNoNewOr value
        
        Note:
            Delegates to max_no_new_or property (CODING_RULE_V2_00017)
        """
        return self.max_no_new_or  # Delegates to property

    def setMaxNoNewOr(self, value: "PositiveInteger") -> "EndToEndTransformationDescription":
        """
        AUTOSAR-compliant setter for maxNoNewOr with method chaining.
        
        Args:
            value: The maxNoNewOr to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to max_no_new_or property setter (gets validation automatically)
        """
        self.max_no_new_or = value  # Delegates to property setter
        return self

    def getMinOkStateInit(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for minOkStateInit.
        
        Returns:
            The minOkStateInit value
        
        Note:
            Delegates to min_ok_state_init property (CODING_RULE_V2_00017)
        """
        return self.min_ok_state_init  # Delegates to property

    def setMinOkStateInit(self, value: "PositiveInteger") -> "EndToEndTransformationDescription":
        """
        AUTOSAR-compliant setter for minOkStateInit with method chaining.
        
        Args:
            value: The minOkStateInit to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to min_ok_state_init property setter (gets validation automatically)
        """
        self.min_ok_state_init = value  # Delegates to property setter
        return self

    def getMinOkState(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for minOkState.
        
        Returns:
            The minOkState value
        
        Note:
            Delegates to min_ok_state property (CODING_RULE_V2_00017)
        """
        return self.min_ok_state  # Delegates to property

    def setMinOkState(self, value: "PositiveInteger") -> "EndToEndTransformationDescription":
        """
        AUTOSAR-compliant setter for minOkState with method chaining.
        
        Args:
            value: The minOkState to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to min_ok_state property setter (gets validation automatically)
        """
        self.min_ok_state = value  # Delegates to property setter
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

    def setOffset(self, value: "PositiveInteger") -> "EndToEndTransformationDescription":
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

    def getProfileBehaviorBehaviorEnum(self) -> "EndToEndProfile":
        """
        AUTOSAR-compliant getter for profileBehaviorBehaviorEnum.
        
        Returns:
            The profileBehaviorBehaviorEnum value
        
        Note:
            Delegates to profile_behavior_behavior_enum property (CODING_RULE_V2_00017)
        """
        return self.profile_behavior_behavior_enum  # Delegates to property

    def setProfileBehaviorBehaviorEnum(self, value: "EndToEndProfile") -> "EndToEndTransformationDescription":
        """
        AUTOSAR-compliant setter for profileBehaviorBehaviorEnum with method chaining.
        
        Args:
            value: The profileBehaviorBehaviorEnum to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to profile_behavior_behavior_enum property setter (gets validation automatically)
        """
        self.profile_behavior_behavior_enum = value  # Delegates to property setter
        return self

    def getProfileName(self) -> "NameToken":
        """
        AUTOSAR-compliant getter for profileName.
        
        Returns:
            The profileName value
        
        Note:
            Delegates to profile_name property (CODING_RULE_V2_00017)
        """
        return self.profile_name  # Delegates to property

    def setProfileName(self, value: "NameToken") -> "EndToEndTransformationDescription":
        """
        AUTOSAR-compliant setter for profileName with method chaining.
        
        Args:
            value: The profileName to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to profile_name property setter (gets validation automatically)
        """
        self.profile_name = value  # Delegates to property setter
        return self

    def getSyncCounterInit(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for syncCounterInit.
        
        Returns:
            The syncCounterInit value
        
        Note:
            Delegates to sync_counter_init property (CODING_RULE_V2_00017)
        """
        return self.sync_counter_init  # Delegates to property

    def setSyncCounterInit(self, value: "PositiveInteger") -> "EndToEndTransformationDescription":
        """
        AUTOSAR-compliant setter for syncCounterInit with method chaining.
        
        Args:
            value: The syncCounterInit to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to sync_counter_init property setter (gets validation automatically)
        """
        self.sync_counter_init = value  # Delegates to property setter
        return self

    def getUpperHeader(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for upperHeader.
        
        Returns:
            The upperHeader value
        
        Note:
            Delegates to upper_header property (CODING_RULE_V2_00017)
        """
        return self.upper_header  # Delegates to property

    def setUpperHeader(self, value: "PositiveInteger") -> "EndToEndTransformationDescription":
        """
        AUTOSAR-compliant setter for upperHeader with method chaining.
        
        Args:
            value: The upperHeader to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to upper_header property setter (gets validation automatically)
        """
        self.upper_header = value  # Delegates to property setter
        return self

    def getWindowSizeInit(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for windowSizeInit.
        
        Returns:
            The windowSizeInit value
        
        Note:
            Delegates to window_size_init property (CODING_RULE_V2_00017)
        """
        return self.window_size_init  # Delegates to property

    def setWindowSizeInit(self, value: "PositiveInteger") -> "EndToEndTransformationDescription":
        """
        AUTOSAR-compliant setter for windowSizeInit with method chaining.
        
        Args:
            value: The windowSizeInit to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to window_size_init property setter (gets validation automatically)
        """
        self.window_size_init = value  # Delegates to property setter
        return self

    def getWindowSize(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for windowSize.
        
        Returns:
            The windowSize value
        
        Note:
            Delegates to window_size property (CODING_RULE_V2_00017)
        """
        return self.window_size  # Delegates to property

    def setWindowSize(self, value: "PositiveInteger") -> "EndToEndTransformationDescription":
        """
        AUTOSAR-compliant setter for windowSize with method chaining.
        
        Args:
            value: The windowSize to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to window_size property setter (gets validation automatically)
        """
        self.window_size = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_clear_from_valid(self, value: Optional["Boolean"]) -> "EndToEndTransformationDescription":
        """
        Set clearFromValid and return self for chaining.
        
        Args:
            value: The clearFromValid to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_clear_from_valid("value")
        """
        self.clear_from_valid = value  # Use property setter (gets validation)
        return self

    def with_counter_offset(self, value: Optional["PositiveInteger"]) -> "EndToEndTransformationDescription":
        """
        Set counterOffset and return self for chaining.
        
        Args:
            value: The counterOffset to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_counter_offset("value")
        """
        self.counter_offset = value  # Use property setter (gets validation)
        return self

    def with_crc_offset(self, value: Optional["PositiveInteger"]) -> "EndToEndTransformationDescription":
        """
        Set crcOffset and return self for chaining.
        
        Args:
            value: The crcOffset to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_crc_offset("value")
        """
        self.crc_offset = value  # Use property setter (gets validation)
        return self

    def with_data_id_mode(self, value: Optional["DataIdModeEnum"]) -> "EndToEndTransformationDescription":
        """
        Set dataIdMode and return self for chaining.
        
        Args:
            value: The dataIdMode to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_data_id_mode("value")
        """
        self.data_id_mode = value  # Use property setter (gets validation)
        return self

    def with_data_id_nibble(self, value: Optional["PositiveInteger"]) -> "EndToEndTransformationDescription":
        """
        Set dataIdNibble and return self for chaining.
        
        Args:
            value: The dataIdNibble to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_data_id_nibble("value")
        """
        self.data_id_nibble = value  # Use property setter (gets validation)
        return self

    def with_e2e_profile(self, value: Optional["E2EProfileCompatibility"]) -> "EndToEndTransformationDescription":
        """
        Set e2eProfile and return self for chaining.
        
        Args:
            value: The e2eProfile to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_e2e_profile("value")
        """
        self.e2e_profile = value  # Use property setter (gets validation)
        return self

    def with_max_delta(self, value: Optional["PositiveInteger"]) -> "EndToEndTransformationDescription":
        """
        Set maxDelta and return self for chaining.
        
        Args:
            value: The maxDelta to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_max_delta("value")
        """
        self.max_delta = value  # Use property setter (gets validation)
        return self

    def with_max_error_state(self, value: Optional["PositiveInteger"]) -> "EndToEndTransformationDescription":
        """
        Set maxErrorState and return self for chaining.
        
        Args:
            value: The maxErrorState to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_max_error_state("value")
        """
        self.max_error_state = value  # Use property setter (gets validation)
        return self

    def with_max_no_new_or(self, value: Optional["PositiveInteger"]) -> "EndToEndTransformationDescription":
        """
        Set maxNoNewOr and return self for chaining.
        
        Args:
            value: The maxNoNewOr to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_max_no_new_or("value")
        """
        self.max_no_new_or = value  # Use property setter (gets validation)
        return self

    def with_min_ok_state_init(self, value: Optional["PositiveInteger"]) -> "EndToEndTransformationDescription":
        """
        Set minOkStateInit and return self for chaining.
        
        Args:
            value: The minOkStateInit to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_min_ok_state_init("value")
        """
        self.min_ok_state_init = value  # Use property setter (gets validation)
        return self

    def with_min_ok_state(self, value: Optional["PositiveInteger"]) -> "EndToEndTransformationDescription":
        """
        Set minOkState and return self for chaining.
        
        Args:
            value: The minOkState to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_min_ok_state("value")
        """
        self.min_ok_state = value  # Use property setter (gets validation)
        return self

    def with_offset(self, value: Optional["PositiveInteger"]) -> "EndToEndTransformationDescription":
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

    def with_profile_behavior_behavior_enum(self, value: Optional["EndToEndProfile"]) -> "EndToEndTransformationDescription":
        """
        Set profileBehaviorBehaviorEnum and return self for chaining.
        
        Args:
            value: The profileBehaviorBehaviorEnum to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_profile_behavior_behavior_enum("value")
        """
        self.profile_behavior_behavior_enum = value  # Use property setter (gets validation)
        return self

    def with_profile_name(self, value: Optional["NameToken"]) -> "EndToEndTransformationDescription":
        """
        Set profileName and return self for chaining.
        
        Args:
            value: The profileName to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_profile_name("value")
        """
        self.profile_name = value  # Use property setter (gets validation)
        return self

    def with_sync_counter_init(self, value: Optional["PositiveInteger"]) -> "EndToEndTransformationDescription":
        """
        Set syncCounterInit and return self for chaining.
        
        Args:
            value: The syncCounterInit to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_sync_counter_init("value")
        """
        self.sync_counter_init = value  # Use property setter (gets validation)
        return self

    def with_upper_header(self, value: Optional["PositiveInteger"]) -> "EndToEndTransformationDescription":
        """
        Set upperHeader and return self for chaining.
        
        Args:
            value: The upperHeader to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_upper_header("value")
        """
        self.upper_header = value  # Use property setter (gets validation)
        return self

    def with_window_size_init(self, value: Optional["PositiveInteger"]) -> "EndToEndTransformationDescription":
        """
        Set windowSizeInit and return self for chaining.
        
        Args:
            value: The windowSizeInit to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_window_size_init("value")
        """
        self.window_size_init = value  # Use property setter (gets validation)
        return self

    def with_window_size(self, value: Optional["PositiveInteger"]) -> "EndToEndTransformationDescription":
        """
        Set windowSize and return self for chaining.
        
        Args:
            value: The windowSize to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_window_size("value")
        """
        self.window_size = value  # Use property setter (gets validation)
        return self



class UserDefinedTransformationDescription(TransformationDescription):
    """
    The UserDefinedTransformationDescription is used to specify details and
    documentation for custom transformers.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Transformer::UserDefinedTransformationDescription
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 771, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class SOMEIPTransformationDescription(TransformationDescription):
    """
    The SOMEIPTransformationDescription is used to specify SOME/IP transformer
    specific attributes.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Transformer::SOMEIPTransformationDescription
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 777, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines the padding for alignment purposes that will be the SOME/IP
                # transformer after the serialized the variable data length data element.
        # The be specified in Bits.
        self._alignment: Optional["PositiveInteger"] = None

    @property
    def alignment(self) -> Optional["PositiveInteger"]:
        """Get alignment (Pythonic accessor)."""
        return self._alignment

    @alignment.setter
    def alignment(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set alignment with validation.
        
        Args:
            value: The alignment to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._alignment = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"alignment must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._alignment = value
        # Defines which byte order shall be serialized by the.
        self._byteOrder: Optional["ByteOrderEnum"] = None

    @property
    def byte_order(self) -> Optional["ByteOrderEnum"]:
        """Get byteOrder (Pythonic accessor)."""
        return self._byteOrder

    @byte_order.setter
    def byte_order(self, value: Optional["ByteOrderEnum"]) -> None:
        """
        Set byteOrder with validation.
        
        Args:
            value: The byteOrder to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._byteOrder = None
            return

        if not isinstance(value, ByteOrderEnum):
            raise TypeError(
                f"byteOrder must be ByteOrderEnum or None, got {type(value).__name__}"
            )
        self._byteOrder = value
        # The interface version the SOME/IP transformer shall use.
        self._interfaceVersion: Optional["PositiveInteger"] = None

    @property
    def interface_version(self) -> Optional["PositiveInteger"]:
        """Get interfaceVersion (Pythonic accessor)."""
        return self._interfaceVersion

    @interface_version.setter
    def interface_version(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set interfaceVersion with validation.
        
        Args:
            value: The interfaceVersion to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._interfaceVersion = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"interfaceVersion must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._interfaceVersion = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAlignment(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for alignment.
        
        Returns:
            The alignment value
        
        Note:
            Delegates to alignment property (CODING_RULE_V2_00017)
        """
        return self.alignment  # Delegates to property

    def setAlignment(self, value: "PositiveInteger") -> "SOMEIPTransformationDescription":
        """
        AUTOSAR-compliant setter for alignment with method chaining.
        
        Args:
            value: The alignment to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to alignment property setter (gets validation automatically)
        """
        self.alignment = value  # Delegates to property setter
        return self

    def getByteOrder(self) -> "ByteOrderEnum":
        """
        AUTOSAR-compliant getter for byteOrder.
        
        Returns:
            The byteOrder value
        
        Note:
            Delegates to byte_order property (CODING_RULE_V2_00017)
        """
        return self.byte_order  # Delegates to property

    def setByteOrder(self, value: "ByteOrderEnum") -> "SOMEIPTransformationDescription":
        """
        AUTOSAR-compliant setter for byteOrder with method chaining.
        
        Args:
            value: The byteOrder to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to byte_order property setter (gets validation automatically)
        """
        self.byte_order = value  # Delegates to property setter
        return self

    def getInterfaceVersion(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for interfaceVersion.
        
        Returns:
            The interfaceVersion value
        
        Note:
            Delegates to interface_version property (CODING_RULE_V2_00017)
        """
        return self.interface_version  # Delegates to property

    def setInterfaceVersion(self, value: "PositiveInteger") -> "SOMEIPTransformationDescription":
        """
        AUTOSAR-compliant setter for interfaceVersion with method chaining.
        
        Args:
            value: The interfaceVersion to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to interface_version property setter (gets validation automatically)
        """
        self.interface_version = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_alignment(self, value: Optional["PositiveInteger"]) -> "SOMEIPTransformationDescription":
        """
        Set alignment and return self for chaining.
        
        Args:
            value: The alignment to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_alignment("value")
        """
        self.alignment = value  # Use property setter (gets validation)
        return self

    def with_byte_order(self, value: Optional["ByteOrderEnum"]) -> "SOMEIPTransformationDescription":
        """
        Set byteOrder and return self for chaining.
        
        Args:
            value: The byteOrder to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_byte_order("value")
        """
        self.byte_order = value  # Use property setter (gets validation)
        return self

    def with_interface_version(self, value: Optional["PositiveInteger"]) -> "SOMEIPTransformationDescription":
        """
        Set interfaceVersion and return self for chaining.
        
        Args:
            value: The interfaceVersion to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_interface_version("value")
        """
        self.interface_version = value  # Use property setter (gets validation)
        return self



class SOMEIPTransformationProps(TransformationProps):
    """
    The class SOMEIPTransformationProps specifies SOME/IP specific configuration
    properties.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Transformer::SOMEIPTransformationProps
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 783, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Defines the padding for alignment purposes that will be the SOME/IP
                # transformer after the serialized the variable data length data element.
        # The be specified in Bits.
        self._alignment: Optional["PositiveInteger"] = None

    @property
    def alignment(self) -> Optional["PositiveInteger"]:
        """Get alignment (Pythonic accessor)."""
        return self._alignment

    @alignment.setter
    def alignment(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set alignment with validation.
        
        Args:
            value: The alignment to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._alignment = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"alignment must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._alignment = value
        # This attribute describes the size of the length field (in that will be put in
        # front of the referenced Array in message.
        self._sizeOfArray: Optional["PositiveInteger"] = None

    @property
    def size_of_array(self) -> Optional["PositiveInteger"]:
        """Get sizeOfArray (Pythonic accessor)."""
        return self._sizeOfArray

    @size_of_array.setter
    def size_of_array(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set sizeOfArray with validation.
        
        Args:
            value: The sizeOfArray to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sizeOfArray = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"sizeOfArray must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._sizeOfArray = value
        # This attribute describes the size of the length field (in that will be put in
        # front of the referenced String in message.
        self._sizeOfString: Optional["PositiveInteger"] = None

    @property
    def size_of_string(self) -> Optional["PositiveInteger"]:
        """Get sizeOfString (Pythonic accessor)."""
        return self._sizeOfString

    @size_of_string.setter
    def size_of_string(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set sizeOfString with validation.
        
        Args:
            value: The sizeOfString to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sizeOfString = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"sizeOfString must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._sizeOfString = value
        # This attribute describes the size of the length field (in that will be put in
        # front of a Structure in the SOME/.
        self._sizeOfStruct: Optional["PositiveInteger"] = None

    @property
    def size_of_struct(self) -> Optional["PositiveInteger"]:
        """Get sizeOfStruct (Pythonic accessor)."""
        return self._sizeOfStruct

    @size_of_struct.setter
    def size_of_struct(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set sizeOfStruct with validation.
        
        Args:
            value: The sizeOfStruct to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sizeOfStruct = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"sizeOfStruct must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._sizeOfStruct = value
        # This attribute describes the size of the length field (in that will be put in
        # front of a Union in the SOME/IP.
        self._sizeOfUnion: Optional["PositiveInteger"] = None

    @property
    def size_of_union(self) -> Optional["PositiveInteger"]:
        """Get sizeOfUnion (Pythonic accessor)."""
        return self._sizeOfUnion

    @size_of_union.setter
    def size_of_union(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set sizeOfUnion with validation.
        
        Args:
            value: The sizeOfUnion to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._sizeOfUnion = None
            return

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"sizeOfUnion must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._sizeOfUnion = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAlignment(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for alignment.
        
        Returns:
            The alignment value
        
        Note:
            Delegates to alignment property (CODING_RULE_V2_00017)
        """
        return self.alignment  # Delegates to property

    def setAlignment(self, value: "PositiveInteger") -> "SOMEIPTransformationProps":
        """
        AUTOSAR-compliant setter for alignment with method chaining.
        
        Args:
            value: The alignment to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to alignment property setter (gets validation automatically)
        """
        self.alignment = value  # Delegates to property setter
        return self

    def getSizeOfArray(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for sizeOfArray.
        
        Returns:
            The sizeOfArray value
        
        Note:
            Delegates to size_of_array property (CODING_RULE_V2_00017)
        """
        return self.size_of_array  # Delegates to property

    def setSizeOfArray(self, value: "PositiveInteger") -> "SOMEIPTransformationProps":
        """
        AUTOSAR-compliant setter for sizeOfArray with method chaining.
        
        Args:
            value: The sizeOfArray to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to size_of_array property setter (gets validation automatically)
        """
        self.size_of_array = value  # Delegates to property setter
        return self

    def getSizeOfString(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for sizeOfString.
        
        Returns:
            The sizeOfString value
        
        Note:
            Delegates to size_of_string property (CODING_RULE_V2_00017)
        """
        return self.size_of_string  # Delegates to property

    def setSizeOfString(self, value: "PositiveInteger") -> "SOMEIPTransformationProps":
        """
        AUTOSAR-compliant setter for sizeOfString with method chaining.
        
        Args:
            value: The sizeOfString to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to size_of_string property setter (gets validation automatically)
        """
        self.size_of_string = value  # Delegates to property setter
        return self

    def getSizeOfStruct(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for sizeOfStruct.
        
        Returns:
            The sizeOfStruct value
        
        Note:
            Delegates to size_of_struct property (CODING_RULE_V2_00017)
        """
        return self.size_of_struct  # Delegates to property

    def setSizeOfStruct(self, value: "PositiveInteger") -> "SOMEIPTransformationProps":
        """
        AUTOSAR-compliant setter for sizeOfStruct with method chaining.
        
        Args:
            value: The sizeOfStruct to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to size_of_struct property setter (gets validation automatically)
        """
        self.size_of_struct = value  # Delegates to property setter
        return self

    def getSizeOfUnion(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for sizeOfUnion.
        
        Returns:
            The sizeOfUnion value
        
        Note:
            Delegates to size_of_union property (CODING_RULE_V2_00017)
        """
        return self.size_of_union  # Delegates to property

    def setSizeOfUnion(self, value: "PositiveInteger") -> "SOMEIPTransformationProps":
        """
        AUTOSAR-compliant setter for sizeOfUnion with method chaining.
        
        Args:
            value: The sizeOfUnion to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to size_of_union property setter (gets validation automatically)
        """
        self.size_of_union = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_alignment(self, value: Optional["PositiveInteger"]) -> "SOMEIPTransformationProps":
        """
        Set alignment and return self for chaining.
        
        Args:
            value: The alignment to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_alignment("value")
        """
        self.alignment = value  # Use property setter (gets validation)
        return self

    def with_size_of_array(self, value: Optional["PositiveInteger"]) -> "SOMEIPTransformationProps":
        """
        Set sizeOfArray and return self for chaining.
        
        Args:
            value: The sizeOfArray to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_size_of_array("value")
        """
        self.size_of_array = value  # Use property setter (gets validation)
        return self

    def with_size_of_string(self, value: Optional["PositiveInteger"]) -> "SOMEIPTransformationProps":
        """
        Set sizeOfString and return self for chaining.
        
        Args:
            value: The sizeOfString to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_size_of_string("value")
        """
        self.size_of_string = value  # Use property setter (gets validation)
        return self

    def with_size_of_struct(self, value: Optional["PositiveInteger"]) -> "SOMEIPTransformationProps":
        """
        Set sizeOfStruct and return self for chaining.
        
        Args:
            value: The sizeOfStruct to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_size_of_struct("value")
        """
        self.size_of_struct = value  # Use property setter (gets validation)
        return self

    def with_size_of_union(self, value: Optional["PositiveInteger"]) -> "SOMEIPTransformationProps":
        """
        Set sizeOfUnion and return self for chaining.
        
        Args:
            value: The sizeOfUnion to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_size_of_union("value")
        """
        self.size_of_union = value  # Use property setter (gets validation)
        return self



class UserDefinedTransformationProps(TransformationProps):
    """
    The class UserDefinedTransformationProps specifies specific configuration
    properties of a user defined serializer.
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Transformer::UserDefinedTransformationProps
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 829, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class DataPrototypeInPortInterfaceRef(DataPrototypeReference):
    """
    This class represents a RootDataPrototype that is typed by an
    ApplicationDataType or Implementation DataType or a DataTypeElement that is
    aggregated within a composite application data type (record or array).
    
    Package: M2::AUTOSARTemplates::SystemTemplate::Transformer::DataPrototypeInPortInterfaceRef
    
    Sources:
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 787, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # context of a SenderReceiverInterface.
        # implemented by: DataPrototypeInSender.
        self._dataPrototypeIn: Optional["RefType"] = None

    @property
    def data_prototype_in(self) -> Optional["RefType"]:
        """Get dataPrototypeIn (Pythonic accessor)."""
        return self._dataPrototypeIn

    @data_prototype_in.setter
    def data_prototype_in(self, value: Optional["RefType"]) -> None:
        """
        Set dataPrototypeIn with validation.
        
        Args:
            value: The dataPrototypeIn to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dataPrototypeIn = None
            return

        self._dataPrototypeIn = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDataPrototypeIn(self) -> "RefType":
        """
        AUTOSAR-compliant getter for dataPrototypeIn.
        
        Returns:
            The dataPrototypeIn value
        
        Note:
            Delegates to data_prototype_in property (CODING_RULE_V2_00017)
        """
        return self.data_prototype_in  # Delegates to property

    def setDataPrototypeIn(self, value: "RefType") -> "DataPrototypeInPortInterfaceRef":
        """
        AUTOSAR-compliant setter for dataPrototypeIn with method chaining.
        
        Args:
            value: The dataPrototypeIn to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to data_prototype_in property setter (gets validation automatically)
        """
        self.data_prototype_in = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_data_prototype_in(self, value: Optional[RefType]) -> "DataPrototypeInPortInterfaceRef":
        """
        Set dataPrototypeIn and return self for chaining.
        
        Args:
            value: The dataPrototypeIn to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_data_prototype_in("value")
        """
        self.data_prototype_in = value  # Use property setter (gets validation)
        return self


class DataTransformationKindEnum(AREnum):
    """
    DataTransformationKindEnum enumeration

This enumeration contributes to the definition of the scope of the DataTransformation. Aggregated by DataTransformation.dataTransformationKind

Package: M2::AUTOSARTemplates::SystemTemplate::Transformer
    """
    # The DataTransformation shall only be applied to the receiving end only, i.e. transform from byte array ByteArray to data type.
    asymmetricFrom = "0"

    # The DataTransformation shall be applied to the sending end only, i.e. from data type to byte array.
    asymmetricToByteArray = "1"

    # The DataTransformation shall be applied at both the sending and the receiving end of the
    symmetric = "2"



class TransformerClassEnum(AREnum):
    """
    TransformerClassEnum enumeration

Specifies the transformer class of a transformer. Aggregated by TransformationTechnology.transformerClass

Package: M2::AUTOSARTemplates::SystemTemplate::Transformer
    """
    # The transformer is a custom transformer.
    custom = "0"

    # The transformer is a safety transformer.
    safety = "1"

    # The transformer is a security transformer.
    security = "2"

    # The transformer is a serializing transformer.
    serializer = "3"



class CSTransformerErrorReactionEnum(AREnum):
    """
    CSTransformerErrorReactionEnum enumeration

Possible kinds of error reaction in case of a hard transformer error. Aggregated by TransformationISignalProps.csErrorReaction

Package: M2::AUTOSARTemplates::SystemTemplate::Transformer
    """
    # The application is responsible for any error reaction. No autonomous error reaction of RTE and
    applicationOnly = "0"

    # RTE and Transformer coordinate an autonomous error reaction on their own.
    autonomous = "1"



class SOMEIPMessageTypeEnum(AREnum):
    """
    SOMEIPMessageTypeEnum enumeration

Depending on the style of the communication different message types shall be set in the header of a SOME/IP message. Aggregated by SOMEIPTransformationISignalProps.messageType

Package: M2::AUTOSARTemplates::SystemTemplate::Transformer
    """
    # A request of a notification expecting no response.
    notification = "1"

    # A request expecting a response.
    request = "2"

    # A fire&forget request.
    requestNoReturn = "3"

    # The response message.
    response = "4"



class DataIdModeEnum(AREnum):
    """
    DataIdModeEnum enumeration

Supported inclusion modes to include the implicit two-byte Data ID in the one-byte CRC. Aggregated by E2EProfileConfiguration.dataIdMode, EndToEndTransformationDescription.dataIdMode

Package: M2::AUTOSARTemplates::SystemTemplate::Transformer
    """
    # Two bytes are included in the CRC (double ID configuration).
    all16Bit = "0"

    # One of the two bytes byte is included, alternating high and low byte, depending on parity of the high byte is included.
    alternating8Bitcounter = "1"

    # The low byte is included in the implicit CRC calculation, the low nibble of the high byte is transmitted along with the data (i.e. it is explicitly included), the high nibble of the high byte is not used. This is applicable for the IDs up to 12 bits.
    lower12Bit = "2"

    # Only low byte is included, high byte is never used. This is applicable if the IDs in a particular system
    lower8Bitare = "3"



class EndToEndProfileBehaviorEnum(AREnum):
    """
    EndToEndProfileBehaviorEnum enumeration

Behavior of the check functionality Aggregated by EndToEndTransformationDescription.profileBehavior

Package: M2::AUTOSARTemplates::SystemTemplate::Transformer
    """
    # Check has the legacy behavior, before AUTOSAR Release 4.2.
    PRE_R4_2 = "0"

    # Check behaves like new P4/P5/P6 profiles introduced in AUTOSAR Release 4.2.
    R4_2 = "1"

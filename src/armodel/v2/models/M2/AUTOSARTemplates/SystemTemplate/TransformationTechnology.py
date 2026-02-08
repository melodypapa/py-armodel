from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    BufferProperties,
    String,
    Transformation,
    TransformerClassEnum,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)


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

        if not isinstance(value, Boolean):
            raise TypeError(
                f"hasInternal must be Boolean or None, got {type(value).__name__}"
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

        if not isinstance(value, Boolean):
            raise TypeError(
                f"needsOriginal must be Boolean or None, got {type(value).__name__}"
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

        if not isinstance(value, String):
            raise TypeError(
                f"protocol must be String or None, got {type(value).__name__}"
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

        if not isinstance(value, String):
            raise TypeError(
                f"version must be String or None, got {type(value).__name__}"
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

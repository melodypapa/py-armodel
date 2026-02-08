from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


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
        self._dataPrototypeIn: RefType = None

    @property
    def data_prototype_in(self) -> RefType:
        """Get dataPrototypeIn (Pythonic accessor)."""
        return self._dataPrototypeIn

    @data_prototype_in.setter
    def data_prototype_in(self, value: RefType) -> None:
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

    def getDataPrototypeIn(self) -> RefType:
        """
        AUTOSAR-compliant getter for dataPrototypeIn.

        Returns:
            The dataPrototypeIn value

        Note:
            Delegates to data_prototype_in property (CODING_RULE_V2_00017)
        """
        return self.data_prototype_in  # Delegates to property

    def setDataPrototypeIn(self, value: RefType) -> "DataPrototypeTransformationProps":
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

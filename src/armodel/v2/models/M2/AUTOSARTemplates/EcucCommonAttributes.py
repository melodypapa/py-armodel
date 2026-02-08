from abc import ABC
from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import (
    EcucDefinitionElement,
)


class EcucCommonAttributes(EcucDefinitionElement, ABC):
    """
    Attributes used by Configuration Parameters as well as References.

    Package: M2::AUTOSARTemplates::ECUCParameterDefTemplate

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 48, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is EcucCommonAttributes:
            raise TypeError("EcucCommonAttributes is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specifies in which MultiplicityConfigurationClass this parameter or reference
        # is available in a particular aggregation is optional if the has the Category
        # the of the EcucModuleDef is set to this mandatory.
        self._multiplicity: List["EcucMultiplicity"] = []

    @property
    def multiplicity(self) -> List["EcucMultiplicity"]:
        """Get multiplicity (Pythonic accessor)."""
        return self._multiplicity
        # String specifying if this configuration parameter is an configuration
        # parameter or if the hardware- or vendor-specific.
        self._origin: Optional["String"] = None

    @property
    def origin(self) -> Optional["String"]:
        """Get origin (Pythonic accessor)."""
        return self._origin

    @origin.setter
    def origin(self, value: Optional["String"]) -> None:
        """
        Set origin with validation.

        Args:
            value: The origin to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._origin = None
            return

        if not isinstance(value, String):
            raise TypeError(
                f"origin must be String or None, got {type(value).__name__}"
            )
        self._origin = value
        # Indicates if a parameter or a reference may have different in different
                # post-build variants (previously known as configuration sets).
        # TRUE means means no.
        self._postBuildVariant: Optional["Boolean"] = None

    @property
    def post_build_variant(self) -> Optional["Boolean"]:
        """Get postBuildVariant (Pythonic accessor)."""
        return self._postBuildVariant

    @post_build_variant.setter
    def post_build_variant(self, value: Optional["Boolean"]) -> None:
        """
        Set postBuildVariant with validation.

        Args:
            value: The postBuildVariant to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._postBuildVariant = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"postBuildVariant must be Boolean or None, got {type(value).__name__}"
            )
        self._postBuildVariant = value
        # Used to define whether the value element for this be provided with an index.
        # 318 Document ID 87: AUTOSAR_CP_TPS_ECUConfiguration ECU Configuration R23-11.
        self._requiresIndex: Optional["Boolean"] = None

    @property
    def requires_index(self) -> Optional["Boolean"]:
        """Get requiresIndex (Pythonic accessor)."""
        return self._requiresIndex

    @requires_index.setter
    def requires_index(self, value: Optional["Boolean"]) -> None:
        """
        Set requiresIndex with validation.

        Args:
            value: The requiresIndex to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._requiresIndex = None
            return

        if not isinstance(value, Boolean):
            raise TypeError(
                f"requiresIndex must be Boolean or None, got {type(value).__name__}"
            )
        self._requiresIndex = value
        # Specifies in which ValueConfigurationClass this aggregation is optional if
        # the has the Category the of the EcucModuleDef is set to this mandatory.
        self._valueConfig: List["EcucValueConfiguration"] = []

    @property
    def value_config(self) -> List["EcucValueConfiguration"]:
        """Get valueConfig (Pythonic accessor)."""
        return self._valueConfig

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMultiplicity(self) -> List["EcucMultiplicity"]:
        """
        AUTOSAR-compliant getter for multiplicity.

        Returns:
            The multiplicity value

        Note:
            Delegates to multiplicity property (CODING_RULE_V2_00017)
        """
        return self.multiplicity  # Delegates to property

    def getOrigin(self) -> "String":
        """
        AUTOSAR-compliant getter for origin.

        Returns:
            The origin value

        Note:
            Delegates to origin property (CODING_RULE_V2_00017)
        """
        return self.origin  # Delegates to property

    def setOrigin(self, value: "String") -> "EcucCommonAttributes":
        """
        AUTOSAR-compliant setter for origin with method chaining.

        Args:
            value: The origin to set

        Returns:
            self for method chaining

        Note:
            Delegates to origin property setter (gets validation automatically)
        """
        self.origin = value  # Delegates to property setter
        return self

    def getPostBuildVariant(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for postBuildVariant.

        Returns:
            The postBuildVariant value

        Note:
            Delegates to post_build_variant property (CODING_RULE_V2_00017)
        """
        return self.post_build_variant  # Delegates to property

    def setPostBuildVariant(self, value: "Boolean") -> "EcucCommonAttributes":
        """
        AUTOSAR-compliant setter for postBuildVariant with method chaining.

        Args:
            value: The postBuildVariant to set

        Returns:
            self for method chaining

        Note:
            Delegates to post_build_variant property setter (gets validation automatically)
        """
        self.post_build_variant = value  # Delegates to property setter
        return self

    def getRequiresIndex(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for requiresIndex.

        Returns:
            The requiresIndex value

        Note:
            Delegates to requires_index property (CODING_RULE_V2_00017)
        """
        return self.requires_index  # Delegates to property

    def setRequiresIndex(self, value: "Boolean") -> "EcucCommonAttributes":
        """
        AUTOSAR-compliant setter for requiresIndex with method chaining.

        Args:
            value: The requiresIndex to set

        Returns:
            self for method chaining

        Note:
            Delegates to requires_index property setter (gets validation automatically)
        """
        self.requires_index = value  # Delegates to property setter
        return self

    def getValueConfig(self) -> List["EcucValueConfiguration"]:
        """
        AUTOSAR-compliant getter for valueConfig.

        Returns:
            The valueConfig value

        Note:
            Delegates to value_config property (CODING_RULE_V2_00017)
        """
        return self.value_config  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_origin(self, value: Optional["String"]) -> "EcucCommonAttributes":
        """
        Set origin and return self for chaining.

        Args:
            value: The origin to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_origin("value")
        """
        self.origin = value  # Use property setter (gets validation)
        return self

    def with_post_build_variant(self, value: Optional["Boolean"]) -> "EcucCommonAttributes":
        """
        Set postBuildVariant and return self for chaining.

        Args:
            value: The postBuildVariant to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_post_build_variant("value")
        """
        self.post_build_variant = value  # Use property setter (gets validation)
        return self

    def with_requires_index(self, value: Optional["Boolean"]) -> "EcucCommonAttributes":
        """
        Set requiresIndex and return self for chaining.

        Args:
            value: The requiresIndex to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_requires_index("value")
        """
        self.requires_index = value  # Use property setter (gets validation)
        return self

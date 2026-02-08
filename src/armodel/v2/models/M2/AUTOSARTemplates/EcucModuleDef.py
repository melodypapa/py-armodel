from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    CIdentifier,
    EcucConfiguration,
    EcucContainerDef,
    EcucDefinitionElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)


class EcucModuleDef(EcucDefinitionElement):
    """
    Used as the top-level element for configuration definition for Software
    Modules, including BSW and RTE as well as ECU Infrastructure.

    Package: M2::AUTOSARTemplates::ECUCParameterDefTemplate::EcucModuleDef

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 314, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 32, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 187, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # For modules where several instances of the VSMD can the apiServicePrefix
                # defines the API the derived instances, e.
        # g.
        # Cdd, Xfrm E2EXf).
        self._apiServicePrefix: Optional["CIdentifier"] = None

    @property
    def api_service_prefix(self) -> Optional["CIdentifier"]:
        """Get apiServicePrefix (Pythonic accessor)."""
        return self._apiServicePrefix

    @api_service_prefix.setter
    def api_service_prefix(self, value: Optional["CIdentifier"]) -> None:
        """
        Set apiServicePrefix with validation.

        Args:
            value: The apiServicePrefix to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._apiServicePrefix = None
            return

        if not isinstance(value, CIdentifier):
            raise TypeError(
                f"apiServicePrefix must be CIdentifier or None, got {type(value).__name__}"
            )
        self._apiServicePrefix = value
        # Aggregates the top-level container definitions of this definition.
        self._container: List["EcucContainerDef"] = []

    @property
    def container(self) -> List["EcucContainerDef"]:
        """Get container (Pythonic accessor)."""
        return self._container
        # Indicates if a module supports different post-build variants known as
        # post-build selectable configuration means yes, FALSE means no.
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
        # Optional reference from the Vendor Specific Module to the Standardized Module
                # Definition it refines.
        # this EcucModuleDef has the category reference be provided.
        # In case this EcucModuleDef has VENDOR_SPECIFIC_MODULE_ reference is
                # mandatory.
        self._refinedModule: Optional["EcucModuleDef"] = None

    @property
    def refined_module(self) -> Optional["EcucModuleDef"]:
        """Get refinedModule (Pythonic accessor)."""
        return self._refinedModule

    @refined_module.setter
    def refined_module(self, value: Optional["EcucModuleDef"]) -> None:
        """
        Set refinedModule with validation.

        Args:
            value: The refinedModule to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._refinedModule = None
            return

        if not isinstance(value, EcucModuleDef):
            raise TypeError(
                f"refinedModule must be EcucModuleDef or None, got {type(value).__name__}"
            )
        self._refinedModule = value
        # Specifies which ConfigurationVariants are supported by this software module.
        # This attribute is optional if the Ecuc the category STANDARDIZED_ the
                # category attribute of the set to VENDOR_SPECIFIC_ this attribute is
                # mandatory.
        self._supported: List["EcucConfiguration"] = []

    @property
    def supported(self) -> List["EcucConfiguration"]:
        """Get supported (Pythonic accessor)."""
        return self._supported

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getApiServicePrefix(self) -> "CIdentifier":
        """
        AUTOSAR-compliant getter for apiServicePrefix.

        Returns:
            The apiServicePrefix value

        Note:
            Delegates to api_service_prefix property (CODING_RULE_V2_00017)
        """
        return self.api_service_prefix  # Delegates to property

    def setApiServicePrefix(self, value: "CIdentifier") -> "EcucModuleDef":
        """
        AUTOSAR-compliant setter for apiServicePrefix with method chaining.

        Args:
            value: The apiServicePrefix to set

        Returns:
            self for method chaining

        Note:
            Delegates to api_service_prefix property setter (gets validation automatically)
        """
        self.api_service_prefix = value  # Delegates to property setter
        return self

    def getContainer(self) -> List["EcucContainerDef"]:
        """
        AUTOSAR-compliant getter for container.

        Returns:
            The container value

        Note:
            Delegates to container property (CODING_RULE_V2_00017)
        """
        return self.container  # Delegates to property

    def getPostBuildVariant(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for postBuildVariant.

        Returns:
            The postBuildVariant value

        Note:
            Delegates to post_build_variant property (CODING_RULE_V2_00017)
        """
        return self.post_build_variant  # Delegates to property

    def setPostBuildVariant(self, value: "Boolean") -> "EcucModuleDef":
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

    def getRefinedModule(self) -> "EcucModuleDef":
        """
        AUTOSAR-compliant getter for refinedModule.

        Returns:
            The refinedModule value

        Note:
            Delegates to refined_module property (CODING_RULE_V2_00017)
        """
        return self.refined_module  # Delegates to property

    def setRefinedModule(self, value: "EcucModuleDef") -> "EcucModuleDef":
        """
        AUTOSAR-compliant setter for refinedModule with method chaining.

        Args:
            value: The refinedModule to set

        Returns:
            self for method chaining

        Note:
            Delegates to refined_module property setter (gets validation automatically)
        """
        self.refined_module = value  # Delegates to property setter
        return self

    def getSupported(self) -> List["EcucConfiguration"]:
        """
        AUTOSAR-compliant getter for supported.

        Returns:
            The supported value

        Note:
            Delegates to supported property (CODING_RULE_V2_00017)
        """
        return self.supported  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_api_service_prefix(self, value: Optional["CIdentifier"]) -> "EcucModuleDef":
        """
        Set apiServicePrefix and return self for chaining.

        Args:
            value: The apiServicePrefix to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_api_service_prefix("value")
        """
        self.api_service_prefix = value  # Use property setter (gets validation)
        return self

    def with_post_build_variant(self, value: Optional["Boolean"]) -> "EcucModuleDef":
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

    def with_refined_module(self, value: Optional["EcucModuleDef"]) -> "EcucModuleDef":
        """
        Set refinedModule and return self for chaining.

        Args:
            value: The refinedModule to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_refined_module("value")
        """
        self.refined_module = value  # Use property setter (gets validation)
        return self

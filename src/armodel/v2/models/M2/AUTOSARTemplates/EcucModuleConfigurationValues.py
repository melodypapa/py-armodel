from typing import (
    List,
    Optional,
)

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARElement,
)


class EcucModuleConfigurationValues(ARElement):
    """
    Head of the configuration of one Module. A Module can be a BSW module as
    well as the RTE and ECU Infrastructure. As part of the BSW module
    description, the EcucModuleConfigurationValues element has two different
    roles: The recommendedConfiguration contains parameter values recommended by
    the BSW module vendor. The preconfiguredConfiguration contains values for
    those parameters which are fixed by the implementation and cannot be
    changed. These two EcucModuleConfigurationValues are used when the base
    EcucModuleConfigurationValues (as part of the base ECU configuration) is
    created to fill parameters with initial values.

    Package: M2::AUTOSARTemplates::ECUCDescriptionTemplate

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 313, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 110, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 441, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Aggregates all containers that belong to this module atpVariation.
        self._container: List["EcucContainerValue"] = []

    @property
    def container(self) -> List["EcucContainerValue"]:
        """Get container (Pythonic accessor)."""
        return self._container
        # Reference to the definition of this EcucModule Typically, this is a vendor
        # configuration.
        self._definition: Optional["EcucModuleDef"] = None

    @property
    def definition(self) -> Optional["EcucModuleDef"]:
        """Get definition (Pythonic accessor)."""
        return self._definition

    @definition.setter
    def definition(self, value: Optional["EcucModuleDef"]) -> None:
        """
        Set definition with validation.

        Args:
            value: The definition to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._definition = None
            return

        if not isinstance(value, EcucModuleDef):
            raise TypeError(
                f"definition must be EcucModuleDef or None, got {type(value).__name__}"
            )
        self._definition = value
        # to / are Definition of ModuleDef ECUC Parameters the be used to express the
        # semantic compatibility rules between the definition revision labels is up to
        # the module’s vendor.
        self._ecucDefEdition: Optional["RevisionLabelString"] = None

    @property
    def ecuc_def_edition(self) -> Optional["RevisionLabelString"]:
        """Get ecucDefEdition (Pythonic accessor)."""
        return self._ecucDefEdition

    @ecuc_def_edition.setter
    def ecuc_def_edition(self, value: Optional["RevisionLabelString"]) -> None:
        """
        Set ecucDefEdition with validation.

        Args:
            value: The ecucDefEdition to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ecucDefEdition = None
            return

        if not isinstance(value, RevisionLabelString):
            raise TypeError(
                f"ecucDefEdition must be RevisionLabelString or None, got {type(value).__name__}"
            )
        self._ecucDefEdition = value
                # provides.
        # If this element is in a particular role (e.
        # g.
        # preconfigured recommendedConfiguration) then the be one of VariantPreCompile,
                # VariantLink.
        self._implementation: Optional["EcucConfiguration"] = None

    @property
    def implementation(self) -> Optional["EcucConfiguration"]:
        """Get implementation (Pythonic accessor)."""
        return self._implementation

    @implementation.setter
    def implementation(self, value: Optional["EcucConfiguration"]) -> None:
        """
        Set implementation with validation.

        Args:
            value: The implementation to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._implementation = None
            return

        if not isinstance(value, EcucConfiguration):
            raise TypeError(
                f"implementation must be EcucConfiguration or None, got {type(value).__name__}"
            )
        self._implementation = value
        # optional because the EcucModuleConfiguration is also used to configure the
                # ECU map) or Application SW-Cs.
        # case the EcucModuleConfigurationValues are configure the module, the
                # reference is mandatory to fetch module specific "common" published.
        self._module: Optional["BswImplementation"] = None

    @property
    def module(self) -> Optional["BswImplementation"]:
        """Get module (Pythonic accessor)."""
        return self._module

    @module.setter
    def module(self, value: Optional["BswImplementation"]) -> None:
        """
        Set module with validation.

        Args:
            value: The module to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._module = None
            return

        if not isinstance(value, BswImplementation):
            raise TypeError(
                f"module must be BswImplementation or None, got {type(value).__name__}"
            )
        self._module = value
        # e.
        # , introduced at link or post-build time) new points.
        # TRUE means yes, FALSE If the attribute is not defined, FALSE be assumed.
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

    def with_container(self, value):
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

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getContainer(self) -> List["EcucContainerValue"]:
        """
        AUTOSAR-compliant getter for container.

        Returns:
            The container value

        Note:
            Delegates to container property (CODING_RULE_V2_00017)
        """
        return self.container  # Delegates to property

    def getDefinition(self) -> "EcucModuleDef":
        """
        AUTOSAR-compliant getter for definition.

        Returns:
            The definition value

        Note:
            Delegates to definition property (CODING_RULE_V2_00017)
        """
        return self.definition  # Delegates to property

    def setDefinition(self, value: "EcucModuleDef") -> "EcucModuleConfigurationValues":
        """
        AUTOSAR-compliant setter for definition with method chaining.

        Args:
            value: The definition to set

        Returns:
            self for method chaining

        Note:
            Delegates to definition property setter (gets validation automatically)
        """
        self.definition = value  # Delegates to property setter
        return self

    def getEcucDefEdition(self) -> "RevisionLabelString":
        """
        AUTOSAR-compliant getter for ecucDefEdition.

        Returns:
            The ecucDefEdition value

        Note:
            Delegates to ecuc_def_edition property (CODING_RULE_V2_00017)
        """
        return self.ecuc_def_edition  # Delegates to property

    def setEcucDefEdition(self, value: "RevisionLabelString") -> "EcucModuleConfigurationValues":
        """
        AUTOSAR-compliant setter for ecucDefEdition with method chaining.

        Args:
            value: The ecucDefEdition to set

        Returns:
            self for method chaining

        Note:
            Delegates to ecuc_def_edition property setter (gets validation automatically)
        """
        self.ecuc_def_edition = value  # Delegates to property setter
        return self

    def getImplementation(self) -> "EcucConfiguration":
        """
        AUTOSAR-compliant getter for implementation.

        Returns:
            The implementation value

        Note:
            Delegates to implementation property (CODING_RULE_V2_00017)
        """
        return self.implementation  # Delegates to property

    def setImplementation(self, value: "EcucConfiguration") -> "EcucModuleConfigurationValues":
        """
        AUTOSAR-compliant setter for implementation with method chaining.

        Args:
            value: The implementation to set

        Returns:
            self for method chaining

        Note:
            Delegates to implementation property setter (gets validation automatically)
        """
        self.implementation = value  # Delegates to property setter
        return self

    def getModule(self) -> "BswImplementation":
        """
        AUTOSAR-compliant getter for module.

        Returns:
            The module value

        Note:
            Delegates to module property (CODING_RULE_V2_00017)
        """
        return self.module  # Delegates to property

    def setModule(self, value: "BswImplementation") -> "EcucModuleConfigurationValues":
        """
        AUTOSAR-compliant setter for module with method chaining.

        Args:
            value: The module to set

        Returns:
            self for method chaining

        Note:
            Delegates to module property setter (gets validation automatically)
        """
        self.module = value  # Delegates to property setter
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

    def setPostBuildVariant(self, value: "Boolean") -> "EcucModuleConfigurationValues":
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

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_definition(self, value: Optional["EcucModuleDef"]) -> "EcucModuleConfigurationValues":
        """
        Set definition and return self for chaining.

        Args:
            value: The definition to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_definition("value")
        """
        self.definition = value  # Use property setter (gets validation)
        return self

    def with_ecuc_def_edition(self, value: Optional["RevisionLabelString"]) -> "EcucModuleConfigurationValues":
        """
        Set ecucDefEdition and return self for chaining.

        Args:
            value: The ecucDefEdition to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ecuc_def_edition("value")
        """
        self.ecuc_def_edition = value  # Use property setter (gets validation)
        return self

    def with_implementation(self, value: Optional["EcucConfiguration"]) -> "EcucModuleConfigurationValues":
        """
        Set implementation and return self for chaining.

        Args:
            value: The implementation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_implementation("value")
        """
        self.implementation = value  # Use property setter (gets validation)
        return self

    def with_module(self, value: Optional["BswImplementation"]) -> "EcucModuleConfigurationValues":
        """
        Set module and return self for chaining.

        Args:
            value: The module to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_module("value")
        """
        self.module = value  # Use property setter (gets validation)
        return self

    def with_post_build_variant(self, value: Optional["Boolean"]) -> "EcucModuleConfigurationValues":
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

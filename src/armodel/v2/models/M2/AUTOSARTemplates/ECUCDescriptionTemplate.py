"""
AUTOSAR Package - ECUCDescriptionTemplate

Package: M2::AUTOSARTemplates::ECUCDescriptionTemplate
"""

from abc import ABC
from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    RefType,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
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

    Package: M2::AUTOSARTemplates::ECUCDescriptionTemplate::EcucModuleConfigurationValues

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

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"postBuildVariant must be Boolean or bool or None, got {type(value).__name__}"
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

    def with_ecuc_value(self, value):
        """
        Set ecuc_value and return self for chaining.

        Args:
            value: The ecuc_value to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ecuc_value("value")
        """
        self.ecuc_value = value  # Use property setter (gets validation)
        return self

    def with_parameter_value(self, value):
        """
        Set parameter_value and return self for chaining.

        Args:
            value: The parameter_value to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_parameter_value("value")
        """
        self.parameter_value = value  # Use property setter (gets validation)
        return self

    def with_reference_value(self, value):
        """
        Set reference_value and return self for chaining.

        Args:
            value: The reference_value to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_reference_value("value")
        """
        self.reference_value = value  # Use property setter (gets validation)
        return self

    def with_sub_container(self, value):
        """
        Set sub_container and return self for chaining.

        Args:
            value: The sub_container to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sub_container("value")
        """
        self.sub_container = value  # Use property setter (gets validation)
        return self

    def with_annotation(self, value):
        """
        Set annotation and return self for chaining.

        Args:
            value: The annotation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_annotation("value")
        """
        self.annotation = value  # Use property setter (gets validation)
        return self

    def with_annotation(self, value):
        """
        Set annotation and return self for chaining.

        Args:
            value: The annotation to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_annotation("value")
        """
        self.annotation = value  # Use property setter (gets validation)
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



class EcucValueCollection(ARElement):
    """
    This represents the anchor point of the ECU configuration description.

    Package: M2::AUTOSARTemplates::ECUCDescriptionTemplate::EcucValueCollection

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 108, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2022, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 222, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # References to the configuration of individual software that are present on
                # this ECU.
        # atpVariation.
        self._ecucValue: List["EcucModule"] = []

    @property
    def ecuc_value(self) -> List["EcucModule"]:
        """Get ecucValue (Pythonic accessor)."""
        return self._ecucValue
        # Represents the extract of the System Configuration that is the ECU configured
        # with that ECU.
        self._ecuExtract: Optional["System"] = None

    @property
    def ecu_extract(self) -> Optional["System"]:
        """Get ecuExtract (Pythonic accessor)."""
        return self._ecuExtract

    @ecu_extract.setter
    def ecu_extract(self, value: Optional["System"]) -> None:
        """
        Set ecuExtract with validation.

        Args:
            value: The ecuExtract to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ecuExtract = None
            return

        if not isinstance(value, System):
            raise TypeError(
                f"ecuExtract must be System or None, got {type(value).__name__}"
            )
        self._ecuExtract = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getEcucValue(self) -> List["EcucModule"]:
        """
        AUTOSAR-compliant getter for ecucValue.

        Returns:
            The ecucValue value

        Note:
            Delegates to ecuc_value property (CODING_RULE_V2_00017)
        """
        return self.ecuc_value  # Delegates to property

    def getEcuExtract(self) -> "System":
        """
        AUTOSAR-compliant getter for ecuExtract.

        Returns:
            The ecuExtract value

        Note:
            Delegates to ecu_extract property (CODING_RULE_V2_00017)
        """
        return self.ecu_extract  # Delegates to property

    def setEcuExtract(self, value: "System") -> "EcucValueCollection":
        """
        AUTOSAR-compliant setter for ecuExtract with method chaining.

        Args:
            value: The ecuExtract to set

        Returns:
            self for method chaining

        Note:
            Delegates to ecu_extract property setter (gets validation automatically)
        """
        self.ecu_extract = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_ecu_extract(self, value: Optional["System"]) -> "EcucValueCollection":
        """
        Set ecuExtract and return self for chaining.

        Args:
            value: The ecuExtract to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_ecu_extract("value")
        """
        self.ecu_extract = value  # Use property setter (gets validation)
        return self



class EcucIndexableValue(ARObject, ABC):
    """
    Used to support the specification of ordering of parameter values.

    Package: M2::AUTOSARTemplates::ECUCDescriptionTemplate::EcucIndexableValue

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 110, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is EcucIndexableValue:
            raise TypeError("EcucIndexableValue is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Used to support the specification of ordering of parameter.
        self._index: Optional["PositiveInteger"] = None

    @property
    def index(self) -> Optional["PositiveInteger"]:
        """Get index (Pythonic accessor)."""
        return self._index

    @index.setter
    def index(self, value: Optional["PositiveInteger"]) -> None:
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

        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"index must be PositiveInteger or str or None, got {type(value).__name__}"
            )
        self._index = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getIndex(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for index.

        Returns:
            The index value

        Note:
            Delegates to index property (CODING_RULE_V2_00017)
        """
        return self.index  # Delegates to property

    def setIndex(self, value: "PositiveInteger") -> "EcucIndexableValue":
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

    def with_index(self, value: Optional["PositiveInteger"]) -> "EcucIndexableValue":
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



class EcucContainerValue(Identifiable):
    """
    Represents a Container definition in the ECU Configuration Description.

    Package: M2::AUTOSARTemplates::ECUCDescriptionTemplate::EcucContainerValue

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 119, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2021, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 439, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 185, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Reference to the definition of this Container in the ECU Definition.
        self._definition: Optional["EcucContainerDef"] = None

    @property
    def definition(self) -> Optional["EcucContainerDef"]:
        """Get definition (Pythonic accessor)."""
        return self._definition

    @definition.setter
    def definition(self, value: Optional["EcucContainerDef"]) -> None:
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

        if not isinstance(value, EcucContainerDef):
            raise TypeError(
                f"definition must be EcucContainerDef or None, got {type(value).__name__}"
            )
        self._definition = value
        self._parameterValue: List["EcucParameterValue"] = []

    @property
    def parameter_value(self) -> List["EcucParameterValue"]:
        """Get parameterValue (Pythonic accessor)."""
        return self._parameterValue
        # Aggregates all References with this container.
        # [RS_ECUC_00079] atpVariation.
        self._referenceValue: List["RefType"] = []

    @property
    def reference_value(self) -> List["RefType"]:
        """Get referenceValue (Pythonic accessor)."""
        return self._referenceValue
        # Aggregates all sub-containers within this container.
        # atpVariation.
        self._subContainer: List["EcucContainerValue"] = []

    @property
    def sub_container(self) -> List["EcucContainerValue"]:
        """Get subContainer (Pythonic accessor)."""
        return self._subContainer

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDefinition(self) -> "EcucContainerDef":
        """
        AUTOSAR-compliant getter for definition.

        Returns:
            The definition value

        Note:
            Delegates to definition property (CODING_RULE_V2_00017)
        """
        return self.definition  # Delegates to property

    def setDefinition(self, value: "EcucContainerDef") -> "EcucContainerValue":
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

    def getParameterValue(self) -> List["EcucParameterValue"]:
        """
        AUTOSAR-compliant getter for parameterValue.

        Returns:
            The parameterValue value

        Note:
            Delegates to parameter_value property (CODING_RULE_V2_00017)
        """
        return self.parameter_value  # Delegates to property

    def getReferenceValue(self) -> List["RefType"]:
        """
        AUTOSAR-compliant getter for referenceValue.

        Returns:
            The referenceValue value

        Note:
            Delegates to reference_value property (CODING_RULE_V2_00017)
        """
        return self.reference_value  # Delegates to property

    def getSubContainer(self) -> List["EcucContainerValue"]:
        """
        AUTOSAR-compliant getter for subContainer.

        Returns:
            The subContainer value

        Note:
            Delegates to sub_container property (CODING_RULE_V2_00017)
        """
        return self.sub_container  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_definition(self, value: Optional["EcucContainerDef"]) -> "EcucContainerValue":
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



class EcucParameterValue(EcucIndexableValue, ABC):
    """
    Common class to all types of configuration values.

    Package: M2::AUTOSARTemplates::ECUCDescriptionTemplate::EcucParameterValue

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 124, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 442, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 189, Foundation R23-11)
    """
    def __init__(self):
        if type(self) is EcucParameterValue:
            raise TypeError("EcucParameterValue is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Possibility to provide additional notes while defining the Parameter Values.
        # These are not documentation but are mere design notes.
        # its sub-classes 318 Document ID 87: AUTOSAR_CP_TPS_ECUConfiguration ECU
                # Configuration R23-11.
        self._annotation: List["Annotation"] = []

    @property
    def annotation(self) -> List["Annotation"]:
        """Get annotation (Pythonic accessor)."""
        return self._annotation
        # Reference to the definition of this EcucParameterValue the ECU Configuration
        # Parameter.
        self._definition: Optional["EcucParameterDef"] = None

    @property
    def definition(self) -> Optional["EcucParameterDef"]:
        """Get definition (Pythonic accessor)."""
        return self._definition

    @definition.setter
    def definition(self, value: Optional["EcucParameterDef"]) -> None:
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

        if not isinstance(value, EcucParameterDef):
            raise TypeError(
                f"definition must be EcucParameterDef or None, got {type(value).__name__}"
            )
        self._definition = value
                # "true".
        # If isAutoValue is set to actual value will not be considered during ECU will
                # be (re-)calculated by the code stored in the value attribute afterwards.
        # updated values might require a other modules which reference these is not
                # present the default is "false".
        self._isAutoValue: Optional["Boolean"] = None

    @property
    def is_auto_value(self) -> Optional["Boolean"]:
        """Get isAutoValue (Pythonic accessor)."""
        return self._isAutoValue

    @is_auto_value.setter
    def is_auto_value(self, value: Optional["Boolean"]) -> None:
        """
        Set isAutoValue with validation.

        Args:
            value: The isAutoValue to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._isAutoValue = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"isAutoValue must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._isAutoValue = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAnnotation(self) -> List["Annotation"]:
        """
        AUTOSAR-compliant getter for annotation.

        Returns:
            The annotation value

        Note:
            Delegates to annotation property (CODING_RULE_V2_00017)
        """
        return self.annotation  # Delegates to property

    def getDefinition(self) -> "EcucParameterDef":
        """
        AUTOSAR-compliant getter for definition.

        Returns:
            The definition value

        Note:
            Delegates to definition property (CODING_RULE_V2_00017)
        """
        return self.definition  # Delegates to property

    def setDefinition(self, value: "EcucParameterDef") -> "EcucParameterValue":
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

    def getIsAutoValue(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for isAutoValue.

        Returns:
            The isAutoValue value

        Note:
            Delegates to is_auto_value property (CODING_RULE_V2_00017)
        """
        return self.is_auto_value  # Delegates to property

    def setIsAutoValue(self, value: "Boolean") -> "EcucParameterValue":
        """
        AUTOSAR-compliant setter for isAutoValue with method chaining.

        Args:
            value: The isAutoValue to set

        Returns:
            self for method chaining

        Note:
            Delegates to is_auto_value property setter (gets validation automatically)
        """
        self.is_auto_value = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_definition(self, value: Optional["EcucParameterDef"]) -> "EcucParameterValue":
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

    def with_is_auto_value(self, value: Optional["Boolean"]) -> "EcucParameterValue":
        """
        Set isAutoValue and return self for chaining.

        Args:
            value: The isAutoValue to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_is_auto_value("value")
        """
        self.is_auto_value = value  # Use property setter (gets validation)
        return self



class EcucAbstractReferenceValue(EcucIndexableValue, ABC):
    """
    Abstract class to be used as common parent for all reference values in the
    ECU Configuration Description.

    Package: M2::AUTOSARTemplates::ECUCDescriptionTemplate::EcucAbstractReferenceValue

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 131, Classic Platform R23-11)
    """
    def __init__(self):
        if type(self) is EcucAbstractReferenceValue:
            raise TypeError("EcucAbstractReferenceValue is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Possibility to provide additional notes while defining a (e.
        # g.
        # the ECU Configuration Parameter are not intended as documentation but design
                # notes.
        self._annotation: List["Annotation"] = []

    @property
    def annotation(self) -> List["Annotation"]:
        """Get annotation (Pythonic accessor)."""
        return self._annotation
        # Reference to the definition of this EcucAbstractReference subclasses in the
        # ECU Configuration Parameter.
        self._definition: Optional["RefType"] = None

    @property
    def definition(self) -> Optional["RefType"]:
        """Get definition (Pythonic accessor)."""
        return self._definition

    @definition.setter
    def definition(self, value: Optional["RefType"]) -> None:
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

        self._definition = value
                # "true".
        # is set to "true" the actual value will not be ECU Configuration but will be
                # the code generator and stored in the afterwards.
        # These implicit updated values a re-generation of other modules which values.
        # is not present the default is "false".
        self._isAutoValue: Optional["Boolean"] = None

    @property
    def is_auto_value(self) -> Optional["Boolean"]:
        """Get isAutoValue (Pythonic accessor)."""
        return self._isAutoValue

    @is_auto_value.setter
    def is_auto_value(self, value: Optional["Boolean"]) -> None:
        """
        Set isAutoValue with validation.

        Args:
            value: The isAutoValue to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._isAutoValue = None
            return

        if not isinstance(value, (Boolean, bool)):
            raise TypeError(
                f"isAutoValue must be Boolean or bool or None, got {type(value).__name__}"
            )
        self._isAutoValue = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAnnotation(self) -> List["Annotation"]:
        """
        AUTOSAR-compliant getter for annotation.

        Returns:
            The annotation value

        Note:
            Delegates to annotation property (CODING_RULE_V2_00017)
        """
        return self.annotation  # Delegates to property

    def getDefinition(self) -> "RefType":
        """
        AUTOSAR-compliant getter for definition.

        Returns:
            The definition value

        Note:
            Delegates to definition property (CODING_RULE_V2_00017)
        """
        return self.definition  # Delegates to property

    def setDefinition(self, value: "RefType") -> "EcucAbstractReferenceValue":
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

    def getIsAutoValue(self) -> "Boolean":
        """
        AUTOSAR-compliant getter for isAutoValue.

        Returns:
            The isAutoValue value

        Note:
            Delegates to is_auto_value property (CODING_RULE_V2_00017)
        """
        return self.is_auto_value  # Delegates to property

    def setIsAutoValue(self, value: "Boolean") -> "EcucAbstractReferenceValue":
        """
        AUTOSAR-compliant setter for isAutoValue with method chaining.

        Args:
            value: The isAutoValue to set

        Returns:
            self for method chaining

        Note:
            Delegates to is_auto_value property setter (gets validation automatically)
        """
        self.is_auto_value = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_definition(self, value: Optional[RefType]) -> "EcucAbstractReferenceValue":
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

    def with_is_auto_value(self, value: Optional["Boolean"]) -> "EcucAbstractReferenceValue":
        """
        Set isAutoValue and return self for chaining.

        Args:
            value: The isAutoValue to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_is_auto_value("value")
        """
        self.is_auto_value = value  # Use property setter (gets validation)
        return self



class EcucTextualParamValue(EcucParameterValue):
    """
    Holding a value which is not subject to variation.

    Package: M2::AUTOSARTemplates::ECUCDescriptionTemplate::EcucTextualParamValue

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 127, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 443, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 190, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Value of the parameter, not subject to variant handling.
        self._value: Optional["VerbatimString"] = None

    @property
    def value(self) -> Optional["VerbatimString"]:
        """Get value (Pythonic accessor)."""
        return self._value

    @value.setter
    def value(self, value: Optional["VerbatimString"]) -> None:
        """
        Set value with validation.

        Args:
            value: The value to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._value = None
            return

        if not isinstance(value, VerbatimString):
            raise TypeError(
                f"value must be VerbatimString or None, got {type(value).__name__}"
            )
        self._value = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getValue(self) -> "VerbatimString":
        """
        AUTOSAR-compliant getter for value.

        Returns:
            The value value

        Note:
            Delegates to value property (CODING_RULE_V2_00017)
        """
        return self.value  # Delegates to property

    def setValue(self, value: "VerbatimString") -> "EcucTextualParamValue":
        """
        AUTOSAR-compliant setter for value with method chaining.

        Args:
            value: The value to set

        Returns:
            self for method chaining

        Note:
            Delegates to value property setter (gets validation automatically)
        """
        self.value = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_value(self, value: Optional["VerbatimString"]) -> "EcucTextualParamValue":
        """
        Set value and return self for chaining.

        Args:
            value: The value to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_value("value")
        """
        self.value = value  # Use property setter (gets validation)
        return self



class EcucNumericalParamValue(EcucParameterValue):
    """
    Holding the value which is subject to variant handling.

    Package: M2::AUTOSARTemplates::ECUCDescriptionTemplate::EcucNumericalParamValue

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 128, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 442, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 188, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Value which is subject to variant handling.
        self._value: Optional["Numerical"] = None

    @property
    def value(self) -> Optional["Numerical"]:
        """Get value (Pythonic accessor)."""
        return self._value

    @value.setter
    def value(self, value: Optional["Numerical"]) -> None:
        """
        Set value with validation.

        Args:
            value: The value to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._value = None
            return

        if not isinstance(value, Numerical):
            raise TypeError(
                f"value must be Numerical or None, got {type(value).__name__}"
            )
        self._value = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getValue(self) -> "Numerical":
        """
        AUTOSAR-compliant getter for value.

        Returns:
            The value value

        Note:
            Delegates to value property (CODING_RULE_V2_00017)
        """
        return self.value  # Delegates to property

    def setValue(self, value: "Numerical") -> "EcucNumericalParamValue":
        """
        AUTOSAR-compliant setter for value with method chaining.

        Args:
            value: The value to set

        Returns:
            self for method chaining

        Note:
            Delegates to value property setter (gets validation automatically)
        """
        self.value = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_value(self, value: Optional["Numerical"]) -> "EcucNumericalParamValue":
        """
        Set value and return self for chaining.

        Args:
            value: The value to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_value("value")
        """
        self.value = value  # Use property setter (gets validation)
        return self



class EcucAddInfoParamValue(EcucParameterValue):
    """
    This parameter corresponds to EcucAddInfoParamDef.

    Package: M2::AUTOSARTemplates::ECUCDescriptionTemplate::EcucAddInfoParamValue

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 129, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Holds the content of the formated text.
        self._value: Optional["DocumentationBlock"] = None

    @property
    def value(self) -> Optional["DocumentationBlock"]:
        """Get value (Pythonic accessor)."""
        return self._value

    @value.setter
    def value(self, value: Optional["DocumentationBlock"]) -> None:
        """
        Set value with validation.

        Args:
            value: The value to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._value = None
            return

        if not isinstance(value, DocumentationBlock):
            raise TypeError(
                f"value must be DocumentationBlock or None, got {type(value).__name__}"
            )
        self._value = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getValue(self) -> "DocumentationBlock":
        """
        AUTOSAR-compliant getter for value.

        Returns:
            The value value

        Note:
            Delegates to value property (CODING_RULE_V2_00017)
        """
        return self.value  # Delegates to property

    def setValue(self, value: "DocumentationBlock") -> "EcucAddInfoParamValue":
        """
        AUTOSAR-compliant setter for value with method chaining.

        Args:
            value: The value to set

        Returns:
            self for method chaining

        Note:
            Delegates to value property setter (gets validation automatically)
        """
        self.value = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_value(self, value: Optional["DocumentationBlock"]) -> "EcucAddInfoParamValue":
        """
        Set value and return self for chaining.

        Args:
            value: The value to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_value("value")
        """
        self.value = value  # Use property setter (gets validation)
        return self



class EcucReferenceValue(EcucAbstractReferenceValue):
    """
    Used to represent a configuration value that has a parameter definition of
    type EcucAbstractReference Def (used for all of its specializations
    excluding EcucInstanceReferenceDef).

    Package: M2::AUTOSARTemplates::ECUCDescriptionTemplate::EcucReferenceValue

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 132, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 443, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Specifies the destination of the reference.
        self._value: Optional["RefType"] = None

    @property
    def value(self) -> Optional["RefType"]:
        """Get value (Pythonic accessor)."""
        return self._value

    @value.setter
    def value(self, value: Optional["RefType"]) -> None:
        """
        Set value with validation.

        Args:
            value: The value to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._value = None
            return

        self._value = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getValue(self) -> "RefType":
        """
        AUTOSAR-compliant getter for value.

        Returns:
            The value value

        Note:
            Delegates to value property (CODING_RULE_V2_00017)
        """
        return self.value  # Delegates to property

    def setValue(self, value: "RefType") -> "EcucReferenceValue":
        """
        AUTOSAR-compliant setter for value with method chaining.

        Args:
            value: The value to set

        Returns:
            self for method chaining

        Note:
            Delegates to value property setter (gets validation automatically)
        """
        self.value = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_value(self, value: Optional[RefType]) -> "EcucReferenceValue":
        """
        Set value and return self for chaining.

        Args:
            value: The value to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_value("value")
        """
        self.value = value  # Use property setter (gets validation)
        return self



class EcucInstanceReferenceValue(EcucAbstractReferenceValue):
    """
    InstanceReference representation in the ECU Configuration.

    Package: M2::AUTOSARTemplates::ECUCDescriptionTemplate::EcucInstanceReferenceValue

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 134, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # by: AnyInstanceRef.
        self._value: Optional["AtpFeature"] = None

    @property
    def value(self) -> Optional["AtpFeature"]:
        """Get value (Pythonic accessor)."""
        return self._value

    @value.setter
    def value(self, value: Optional["AtpFeature"]) -> None:
        """
        Set value with validation.

        Args:
            value: The value to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._value = None
            return

        if not isinstance(value, AtpFeature):
            raise TypeError(
                f"value must be AtpFeature or None, got {type(value).__name__}"
            )
        self._value = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getValue(self) -> "AtpFeature":
        """
        AUTOSAR-compliant getter for value.

        Returns:
            The value value

        Note:
            Delegates to value property (CODING_RULE_V2_00017)
        """
        return self.value  # Delegates to property

    def setValue(self, value: "AtpFeature") -> "EcucInstanceReferenceValue":
        """
        AUTOSAR-compliant setter for value with method chaining.

        Args:
            value: The value to set

        Returns:
            self for method chaining

        Note:
            Delegates to value property setter (gets validation automatically)
        """
        self.value = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_value(self, value: Optional["AtpFeature"]) -> "EcucInstanceReferenceValue":
        """
        Set value and return self for chaining.

        Args:
            value: The value to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_value("value")
        """
        self.value = value  # Use property setter (gets validation)
        return self

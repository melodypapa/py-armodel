from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class PortPrototypeBlueprint(ARElement):
    """
    This meta-class represents the ability to express a blueprint of a
    PortPrototype by referring to a particular PortInterface. This blueprint can
    then be used as a guidance to create particular PortPrototypes which are
    defined according to this blueprint. By this it is possible to standardize
    application interfaces without the need to also standardize
    software-components with PortPrototypes typed by the standardized Port
    Interfaces.

    Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::BlueprintDedicated::Port::PortPrototypeBlueprint

    Sources:
      - AUTOSAR_CP_TPS_TimingExtensions.pdf (Page 237, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 459, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 60, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This specifies the init values for the dataElements in the
        # PortPrototypeBlueprint.
        self._initValue: List[RefType] = []

    @property
    def init_value(self) -> List[RefType]:
        """Get initValue (Pythonic accessor)."""
        return self._initValue
        # This is the interface for which the blueprint is defined.
        # It a blueprint itself or a standardized PortInterface.
        self._interface: "PortInterface" = None

    @property
    def interface(self) -> "PortInterface":
        """Get interface (Pythonic accessor)."""
        return self._interface

    @interface.setter
    def interface(self, value: "PortInterface") -> None:
        """
        Set interface with validation.

        Args:
            value: The interface to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, PortInterface):
            raise TypeError(
                f"interface must be PortInterface, got {type(value).__name__}"
            )
        self._interface = value
        # Provided communication attributes per interface element element or
        # operation).
        self._providedCom: List["PPortComSpec"] = []

    @property
    def provided_com(self) -> List["PPortComSpec"]:
        """Get providedCom (Pythonic accessor)."""
        return self._providedCom
        # Required communication attributes, one for each element.
        self._requiredCom: List["RPortComSpec"] = []

    @property
    def required_com(self) -> List["RPortComSpec"]:
        """Get requiredCom (Pythonic accessor)."""
        return self._requiredCom

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getInitValue(self) -> List[RefType]:
        """
        AUTOSAR-compliant getter for initValue.

        Returns:
            The initValue value

        Note:
            Delegates to init_value property (CODING_RULE_V2_00017)
        """
        return self.init_value  # Delegates to property

    def getInterface(self) -> "PortInterface":
        """
        AUTOSAR-compliant getter for interface.

        Returns:
            The interface value

        Note:
            Delegates to interface property (CODING_RULE_V2_00017)
        """
        return self.interface  # Delegates to property

    def setInterface(self, value: "PortInterface") -> "PortPrototypeBlueprint":
        """
        AUTOSAR-compliant setter for interface with method chaining.

        Args:
            value: The interface to set

        Returns:
            self for method chaining

        Note:
            Delegates to interface property setter (gets validation automatically)
        """
        self.interface = value  # Delegates to property setter
        return self

    def getProvidedCom(self) -> List["PPortComSpec"]:
        """
        AUTOSAR-compliant getter for providedCom.

        Returns:
            The providedCom value

        Note:
            Delegates to provided_com property (CODING_RULE_V2_00017)
        """
        return self.provided_com  # Delegates to property

    def getRequiredCom(self) -> List["RPortComSpec"]:
        """
        AUTOSAR-compliant getter for requiredCom.

        Returns:
            The requiredCom value

        Note:
            Delegates to required_com property (CODING_RULE_V2_00017)
        """
        return self.required_com  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_interface(self, value: "PortInterface") -> "PortPrototypeBlueprint":
        """
        Set interface and return self for chaining.

        Args:
            value: The interface to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_interface("value")
        """
        self.interface = value  # Use property setter (gets validation)
        return self

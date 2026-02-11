"""
AUTOSAR Package - AbstractBlueprintStructure

Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::AbstractBlueprintStructure
"""


from __future__ import annotations
from abc import ABC
from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    String,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class AtpBlueprint(Identifiable, ABC):
    """
    This meta-class represents the ability to act as a Blueprint. As this class
    is an abstract one, particular blueprint meta-classes inherit from this one.

    Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::AbstractBlueprintStructure::AtpBlueprint

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 305, Classic
      Platform R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 424, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 161, Foundation R23-11)
    """
    def __init__(self):
        if type(self) is AtpBlueprint:
            raise TypeError("AtpBlueprint is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This role indicates whether the blueprintable element will or not modifiable.
        self._blueprintPolicy: List[BlueprintPolicy] = []

    @property
    def blueprint_policy(self) -> List[BlueprintPolicy]:
        """Get blueprintPolicy (Pythonic accessor)."""
        return self._blueprintPolicy

    def with_blueprint_policy(self, value):
        """
        Set blueprint_policy and return self for chaining.

        Args:
            value: The blueprint_policy to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_blueprint_policy("value")
        """
        self.blueprint_policy = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBlueprintPolicy(self) -> List[BlueprintPolicy]:
        """
        AUTOSAR-compliant getter for blueprintPolicy.

        Returns:
            The blueprintPolicy value

        Note:
            Delegates to blueprint_policy property (CODING_RULE_V2_00017)
        """
        return self.blueprint_policy  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class AtpBlueprintable(Identifiable, ABC):
    """
    This meta-class represents the ability to be derived from a Blueprint. As
    this class is an abstract one, particular blueprintable meta-classes inherit
    from this one.

    Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::AbstractBlueprintStructure::AtpBlueprintable

    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 424, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 162, Foundation R23-11)
    """
    def __init__(self):
        if type(self) is AtpBlueprintable:
            raise TypeError("AtpBlueprintable is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class AtpBlueprintMapping(ARObject, ABC):
    """
    This meta-class represents the ability to express a particular mapping
    between a blueprint and an element derived from this blueprint. Particular
    mappings are defined by specializations of this meta-class.

    Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::AbstractBlueprintStructure::AtpBlueprintMapping

    Sources:
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 161, Foundation R23-11)
    """
    def __init__(self):
        if type(self) is AtpBlueprintMapping:
            raise TypeError("AtpBlueprintMapping is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the blueprint.
        # atpUriDef.
        self._atpBlueprint: AtpBlueprint = None

    @property
    def atp_blueprint(self) -> AtpBlueprint:
        """Get atpBlueprint (Pythonic accessor)."""
        return self._atpBlueprint

    @atp_blueprint.setter
    def atp_blueprint(self, value: AtpBlueprint) -> None:
        """
        Set atpBlueprint with validation.

        Args:
            value: The atpBlueprint to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, AtpBlueprint):
            raise TypeError(
                f"atpBlueprint must be AtpBlueprint, got {type(value).__name__}"
            )
        self._atpBlueprint = value
        self._atpBlueprinted: AtpBlueprintable = None

    @property
    def atp_blueprinted(self) -> AtpBlueprintable:
        """Get atpBlueprinted (Pythonic accessor)."""
        return self._atpBlueprinted

    @atp_blueprinted.setter
    def atp_blueprinted(self, value: AtpBlueprintable) -> None:
        """
        Set atpBlueprinted with validation.

        Args:
            value: The atpBlueprinted to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, AtpBlueprintable):
            raise TypeError(
                f"atpBlueprinted must be AtpBlueprintable, got {type(value).__name__}"
            )
        self._atpBlueprinted = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAtpBlueprint(self) -> AtpBlueprint:
        """
        AUTOSAR-compliant getter for atpBlueprint.

        Returns:
            The atpBlueprint value

        Note:
            Delegates to atp_blueprint property (CODING_RULE_V2_00017)
        """
        return self.atp_blueprint  # Delegates to property

    def setAtpBlueprint(self, value: AtpBlueprint) -> AtpBlueprintMapping:
        """
        AUTOSAR-compliant setter for atpBlueprint with method chaining.

        Args:
            value: The atpBlueprint to set

        Returns:
            self for method chaining

        Note:
            Delegates to atp_blueprint property setter (gets validation automatically)
        """
        self.atp_blueprint = value  # Delegates to property setter
        return self

    def getAtpBlueprinted(self) -> AtpBlueprintable:
        """
        AUTOSAR-compliant getter for atpBlueprinted.

        Returns:
            The atpBlueprinted value

        Note:
            Delegates to atp_blueprinted property (CODING_RULE_V2_00017)
        """
        return self.atp_blueprinted  # Delegates to property

    def setAtpBlueprinted(self, value: AtpBlueprintable) -> AtpBlueprintMapping:
        """
        AUTOSAR-compliant setter for atpBlueprinted with method chaining.

        Args:
            value: The atpBlueprinted to set

        Returns:
            self for method chaining

        Note:
            Delegates to atp_blueprinted property setter (gets validation automatically)
        """
        self.atp_blueprinted = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_atp_blueprint(self, value: AtpBlueprint) -> AtpBlueprintMapping:
        """
        Set atpBlueprint and return self for chaining.

        Args:
            value: The atpBlueprint to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_atp_blueprint("value")
        """
        self.atp_blueprint = value  # Use property setter (gets validation)
        return self

    def with_atp_blueprinted(self, value: AtpBlueprintable) -> AtpBlueprintMapping:
        """
        Set atpBlueprinted and return self for chaining.

        Args:
            value: The atpBlueprinted to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_atp_blueprinted("value")
        """
        self.atp_blueprinted = value  # Use property setter (gets validation)
        return self



class BlueprintPolicy(ARObject, ABC):
    """
    This meta-class represents the ability to indicate whether blueprintable
    elements will be modifiable or not modifiable. (cid:53) 163 of 238 Document
    ID 535: AUTOSAR_FO_TPS_StandardizationTemplate Standardization Template
    AUTOSAR FO R23-11 (cid:52)

    Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::AbstractBlueprintStructure::BlueprintPolicy

    Sources:
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 163, Foundation R23-11)
    """
    def __init__(self):
        if type(self) is BlueprintPolicy:
            raise TypeError("BlueprintPolicy is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This identifies the related attribute of a BlueprintPolicy.
        # over the model a subset of xpath used.
        self._attributeName: "String" = None

    @property
    def attribute_name(self) -> "String":
        """Get attributeName (Pythonic accessor)."""
        return self._attributeName

    @attribute_name.setter
    def attribute_name(self, value: "String") -> None:
        """
        Set attributeName with validation.

        Args:
            value: The attributeName to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, (String, str)):
            raise TypeError(
                f"attributeName must be String or str, got {type(value).__name__}"
            )
        self._attributeName = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAttributeName(self) -> "String":
        """
        AUTOSAR-compliant getter for attributeName.

        Returns:
            The attributeName value

        Note:
            Delegates to attribute_name property (CODING_RULE_V2_00017)
        """
        return self.attribute_name  # Delegates to property

    def setAttributeName(self, value: "String") -> BlueprintPolicy:
        """
        AUTOSAR-compliant setter for attributeName with method chaining.

        Args:
            value: The attributeName to set

        Returns:
            self for method chaining

        Note:
            Delegates to attribute_name property setter (gets validation automatically)
        """
        self.attribute_name = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_attribute_name(self, value: "String") -> BlueprintPolicy:
        """
        Set attributeName and return self for chaining.

        Args:
            value: The attributeName to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_attribute_name("value")
        """
        self.attribute_name = value  # Use property setter (gets validation)
        return self



class BlueprintPolicyList(BlueprintPolicy):
    """
    The class represents that the related attribute is modifiable during the
    blueprinting. It applies only to attribute with upper multiplicity greater
    than 1.

    Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::AbstractBlueprintStructure::BlueprintPolicyList

    Sources:
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 164, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Maximum number of elements in list.
        # If the maximum is not constraint it shall be set to "undefined".
        self._maxNumberOf: "PositiveInteger" = None

    @property
    def max_number_of(self) -> "PositiveInteger":
        """Get maxNumberOf (Pythonic accessor)."""
        return self._maxNumberOf

    @max_number_of.setter
    def max_number_of(self, value: "PositiveInteger") -> None:
        """
        Set maxNumberOf with validation.

        Args:
            value: The maxNumberOf to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"maxNumberOf must be PositiveInteger or str, got {type(value).__name__}"
            )
        self._maxNumberOf = value
        # If the minimum is not constraint it shall be set to "undefined".
        self._minNumberOf: "PositiveInteger" = None

    @property
    def min_number_of(self) -> "PositiveInteger":
        """Get minNumberOf (Pythonic accessor)."""
        return self._minNumberOf

    @min_number_of.setter
    def min_number_of(self, value: "PositiveInteger") -> None:
        """
        Set minNumberOf with validation.

        Args:
            value: The minNumberOf to set

        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, (PositiveInteger, str)):
            raise TypeError(
                f"minNumberOf must be PositiveInteger or str, got {type(value).__name__}"
            )
        self._minNumberOf = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getMaxNumberOf(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for maxNumberOf.

        Returns:
            The maxNumberOf value

        Note:
            Delegates to max_number_of property (CODING_RULE_V2_00017)
        """
        return self.max_number_of  # Delegates to property

    def setMaxNumberOf(self, value: "PositiveInteger") -> BlueprintPolicyList:
        """
        AUTOSAR-compliant setter for maxNumberOf with method chaining.

        Args:
            value: The maxNumberOf to set

        Returns:
            self for method chaining

        Note:
            Delegates to max_number_of property setter (gets validation automatically)
        """
        self.max_number_of = value  # Delegates to property setter
        return self

    def getMinNumberOf(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for minNumberOf.

        Returns:
            The minNumberOf value

        Note:
            Delegates to min_number_of property (CODING_RULE_V2_00017)
        """
        return self.min_number_of  # Delegates to property

    def setMinNumberOf(self, value: "PositiveInteger") -> BlueprintPolicyList:
        """
        AUTOSAR-compliant setter for minNumberOf with method chaining.

        Args:
            value: The minNumberOf to set

        Returns:
            self for method chaining

        Note:
            Delegates to min_number_of property setter (gets validation automatically)
        """
        self.min_number_of = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_max_number_of(self, value: "PositiveInteger") -> BlueprintPolicyList:
        """
        Set maxNumberOf and return self for chaining.

        Args:
            value: The maxNumberOf to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_max_number_of("value")
        """
        self.max_number_of = value  # Use property setter (gets validation)
        return self

    def with_min_number_of(self, value: "PositiveInteger") -> BlueprintPolicyList:
        """
        Set minNumberOf and return self for chaining.

        Args:
            value: The minNumberOf to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_min_number_of("value")
        """
        self.min_number_of = value  # Use property setter (gets validation)
        return self



class BlueprintPolicyNotModifiable(BlueprintPolicy):
    """
    The class represents that the related attribute is not modifiable during the
    blueprinting.

    Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::AbstractBlueprintStructure::BlueprintPolicyNotModifiable

    Sources:
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 164, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class BlueprintPolicySingle(BlueprintPolicy):
    """
    The class represents that the related attribute is modifiable during the
    blueprinting. It applies only to attribute with upper multiplicity equal 1.

    Package: M2::AUTOSARTemplates::CommonStructure::StandardizationTemplate::AbstractBlueprintStructure::BlueprintPolicySingle

    Sources:
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 164, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

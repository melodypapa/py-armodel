from typing import Optional

from armodel.v2.models.M2.AUTOSARTemplates import (
    ConditionByFormula,
    DocumentationBlock,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class VariationPoint(ARObject):
    """
    that variationPoints are not allowed within a formal BlueprintGenerator.
    postBuildVariant PostBuildVariant * aggr This is the set of post build
    variant conditions which all Condition Condition shall be fulfilled in order
    to (postbuild) bind the variation point. sdg Sdg 0..1 aggr An optional
    special data group is attached to every variation point. These data can be
    used by external software systems to attach application specific data. For
    example, a variant management system might add an identifier, an URL or a
    specific classifier. shortLabel Identifier 0..1 attr This provides a name to
    the particular variation point to support the RTE generator. It is necessary
    for supporting splitable aggregations and if binding time is later than
    codeGenerationTime, as well as some RTE conditions. It needs to be unique
    with in the enclosing Identifiables with the same ShortName. Stereotypes:
    atpIdentityContributor (cid:53) 315 of 318 Document ID 87:
    AUTOSAR_CP_TPS_ECUConfiguration Specification of ECU Configuration AUTOSAR
    CP R23-11 (cid:52)

    Package: M2::AUTOSARTemplates::GenericStructure::VariantHandling::VariationPoint

    Sources:
      - AUTOSAR_CP_TPS_ECUConfiguration.pdf (Page 315, Classic Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 1010, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 2078, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (Page 80, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 226, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 39, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents a description that documents how the point shall be resolved
        # when deriving objects blueprint.
        self._blueprint: Optional["DocumentationBlock"] = None

    @property
    def blueprint(self) -> Optional["DocumentationBlock"]:
        """Get blueprint (Pythonic accessor)."""
        return self._blueprint

    @blueprint.setter
    def blueprint(self, value: Optional["DocumentationBlock"]) -> None:
        """
        Set blueprint with validation.

        Args:
            value: The blueprint to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._blueprint = None
            return

        if not isinstance(value, DocumentationBlock):
            raise TypeError(
                f"blueprint must be DocumentationBlock or None, got {type(value).__name__}"
            )
        self._blueprint = value
        # This condition acts as Binding Function for the Variation that the
                # multiplicity is 0.
        # 1 in order to support variants.
        self._swSyscond: Optional["ConditionByFormula"] = None

    @property
    def sw_syscond(self) -> Optional["ConditionByFormula"]:
        """Get swSyscond (Pythonic accessor)."""
        return self._swSyscond

    @sw_syscond.setter
    def sw_syscond(self, value: Optional["ConditionByFormula"]) -> None:
        """
        Set swSyscond with validation.

        Args:
            value: The swSyscond to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swSyscond = None
            return

        if not isinstance(value, ConditionByFormula):
            raise TypeError(
                f"swSyscond must be ConditionByFormula or None, got {type(value).__name__}"
            )
        self._swSyscond = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBlueprint(self) -> "DocumentationBlock":
        """
        AUTOSAR-compliant getter for blueprint.

        Returns:
            The blueprint value

        Note:
            Delegates to blueprint property (CODING_RULE_V2_00017)
        """
        return self.blueprint  # Delegates to property

    def setBlueprint(self, value: "DocumentationBlock") -> "VariationPoint":
        """
        AUTOSAR-compliant setter for blueprint with method chaining.

        Args:
            value: The blueprint to set

        Returns:
            self for method chaining

        Note:
            Delegates to blueprint property setter (gets validation automatically)
        """
        self.blueprint = value  # Delegates to property setter
        return self

    def getSwSyscond(self) -> "ConditionByFormula":
        """
        AUTOSAR-compliant getter for swSyscond.

        Returns:
            The swSyscond value

        Note:
            Delegates to sw_syscond property (CODING_RULE_V2_00017)
        """
        return self.sw_syscond  # Delegates to property

    def setSwSyscond(self, value: "ConditionByFormula") -> "VariationPoint":
        """
        AUTOSAR-compliant setter for swSyscond with method chaining.

        Args:
            value: The swSyscond to set

        Returns:
            self for method chaining

        Note:
            Delegates to sw_syscond property setter (gets validation automatically)
        """
        self.sw_syscond = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_blueprint(self, value: Optional["DocumentationBlock"]) -> "VariationPoint":
        """
        Set blueprint and return self for chaining.

        Args:
            value: The blueprint to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_blueprint("value")
        """
        self.blueprint = value  # Use property setter (gets validation)
        return self

    def with_sw_syscond(self, value: Optional["ConditionByFormula"]) -> "VariationPoint":
        """
        Set swSyscond and return self for chaining.

        Args:
            value: The swSyscond to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sw_syscond("value")
        """
        self.sw_syscond = value  # Use property setter (gets validation)
        return self

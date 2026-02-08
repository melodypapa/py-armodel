from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class FMFeatureSelection(Identifiable):
    """
    that a FMFeatureSelection cannot include two FMAttributeValues that refer to
    the same FMAttributeDef in the role definition. feature FMFeature 0..1 ref
    The FMFeature whose state is defined by this FMFeature Selection. maximum
    BindingTimeEnum 0..1 attr Defines an upper bound for the binding time of the
    SelectedBinding variation points that are associated with the FMFeature,
    Time and refines its maximumIntendedBindingTime. This attribute is meant as
    a hint for the development process. minimum BindingTimeEnum 0..1 attr
    Defines a lower bound for the binding time of the variation SelectedBinding
    points that are associated with the FMFeature, and Time refines its
    minimumIntendedBindingTime. This attribute is meant as a hint for the
    development process. state FMFeatureSelection 0..1 attr Defines how the
    FMFeature that is described by this State FMFeatureSelection contributes to
    the FMFeature SelectionSet. A FMFeature may have the state selected,
    deselected or undecided. Table 5.2: FMFeatureSelection [constr_3661]
    Multiplicity of FMFeatureSelection.feature (cid:100)For each FMFea-
    tureSelection the reference in the role feature shall exist.(cid:99)()
    [constr_3662] Multiplicity of FMFeatureSelection.state (cid:100)For each
    FMFea- tureSelection the attribute state shall exist.(cid:99)() 40 of 92
    Document ID 606: AUTOSAR_FO_TPS_FeatureModelExchangeFormat AUTOSAR Feature
    Model Exchange Format AUTOSAR FO R23-11 5.2.1 Reference feature The
    reference feature points to the feature that is described by this
    FMFeatureSe- lection. 5.2.2 Attribute state FMFeatureSelection has an
    attribute state that defines how the feature referred to by feature
    contributes to the selection.

    Package: M2::AUTOSARTemplates::FeatureModelTemplate

    Sources:
      - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (Page 40, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This defines a value for the attribute that is referred to in definition.
        self._attributeValue: List["FMAttributeValue"] = []

    @property
    def attribute_value(self) -> List["FMAttributeValue"]:
        """Get attributeValue (Pythonic accessor)."""
        return self._attributeValue

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getAttributeValue(self) -> List["FMAttributeValue"]:
        """
        AUTOSAR-compliant getter for attributeValue.

        Returns:
            The attributeValue value

        Note:
            Delegates to attribute_value property (CODING_RULE_V2_00017)
        """
        return self.attribute_value  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

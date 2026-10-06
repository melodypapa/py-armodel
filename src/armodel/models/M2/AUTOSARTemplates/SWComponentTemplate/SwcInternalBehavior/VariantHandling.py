from __future__ import annotations
from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import ConditionByFormula, PostBuildVariantCondition
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling.AttributeValueVariationPoints import AttributeValueVariationPoint


class VariationPointProxy(Identifiable):
    """
    The VariationPointProxy represents variation points of the C/C++ implementation. In case of bindingTime = compileTime the RTE provides defines which can be used for Pre Processor directives to implement compileTime variability.
    """

    # VariationPointProxy method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 7.61, p.613
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                       [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getConditionAccess             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setConditionAccess             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getImplementationDataTypeRef   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setImplementationDataTypeRef   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPostBuildValueAccessRef     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setPostBuildValueAccessRef     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addPostBuildVariantCondition   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPostBuildVariantConditions  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getValueAccess                 [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setValueAccess                 [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This condition acts as Binding Function for the Variation Point.
        self.conditionAccess: Optional[ConditionByFormula] = None

        # This association to ImplementationDataType shall be taken as an implementation hint by the RTE generator.
        self.implementationDataTypeRef: Optional[RefType] = None

        # This represents the applicable PostBuildVariantCriterion in the context of a VariationPointProxy. Note that the technical details how to access the particular postBuildValueAccess are still considered internal to the RTE and are consequently not standardized.
        self.postBuildValueAccessRef: Optional[RefType] = None

        # This represents that applicable PostBuoldVariant Condition in the context of aVariationPointProxy.
        self.postBuildVariantConditions: List[PostBuildVariantCondition] = []

        # This value acts as Binding Function for the VariationPoint.
        self.valueAccess: Optional[AttributeValueVariationPoint] = None

    def getConditionAccess(self) -> Optional[ConditionByFormula]:
        """This condition acts as Binding Function for the Variation Point."""
        return self.conditionAccess

    def setConditionAccess(self, value: Optional[ConditionByFormula]) -> VariationPointProxy:
        """This condition acts as Binding Function for the Variation Point. A None value is a no-op and does not overwrite an existing conditionAccess."""
        if value is not None:
            self.conditionAccess = value
        return self

    def getImplementationDataTypeRef(self) -> Optional[RefType]:
        """This association to ImplementationDataType shall be taken as an implementation hint by the RTE generator."""
        return self.implementationDataTypeRef

    def setImplementationDataTypeRef(self, value: Optional[RefType]) -> VariationPointProxy:
        """This association to ImplementationDataType shall be taken as an implementation hint by the RTE generator. A None value is a no-op and does not overwrite an existing implementationDataTypeRef."""
        if value is not None:
            self.implementationDataTypeRef = value
        return self

    def getPostBuildValueAccessRef(self) -> Optional[RefType]:
        """This represents the applicable PostBuildVariantCriterion in the context of a VariationPointProxy. Note that the technical details how to access the particular postBuildValueAccess are still considered internal to the RTE and are consequently not standardized."""
        return self.postBuildValueAccessRef

    def setPostBuildValueAccessRef(self, value: Optional[RefType]) -> VariationPointProxy:
        """This represents the applicable PostBuildVariantCriterion in the context of a VariationPointProxy. Note that the technical details how to access the particular postBuildValueAccess are still considered internal to the RTE and are consequently not standardized. A None value is a no-op and does not overwrite an existing postBuildValueAccessRef."""
        if value is not None:
            self.postBuildValueAccessRef = value
        return self

    def addPostBuildVariantCondition(self, value: Optional[PostBuildVariantCondition]) -> VariationPointProxy:
        """This represents that applicable PostBuoldVariant Condition in the context of aVariationPointProxy. A None value is a no-op and does not append to postBuildVariantConditions."""
        if value is not None:
            self.postBuildVariantConditions.append(value)
        return self

    def getPostBuildVariantConditions(self) -> List[PostBuildVariantCondition]:
        """This represents that applicable PostBuoldVariant Condition in the context of aVariationPointProxy."""
        return self.postBuildVariantConditions

    def getValueAccess(self) -> Optional[AttributeValueVariationPoint]:
        """This value acts as Binding Function for the VariationPoint."""
        return self.valueAccess

    def setValueAccess(self, value: Optional[AttributeValueVariationPoint]) -> VariationPointProxy:
        """This value acts as Binding Function for the VariationPoint. A None value is a no-op and does not overwrite an existing valueAccess."""
        if value is not None:
            self.valueAccess = value
        return self

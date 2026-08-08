from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import ConditionByFormula, PostBuildVariantCondition


class VariationPointProxy(Identifiable):
    """
    The VariationPointProxy represents variation points of the C/C++
    implementation. In case of bindingTime = compileTime the RTE provides
    defines which can be used for Pre Processor directives to implement
    compileTime variability.
    """

    # VariationPointProxy method parity checklist:
    # [x] __init__                            [x] impl  [x] docstring  [x] test
    # [x] getConditionAccess                  [x] impl  [x] docstring  [x] test
    # [x] setConditionAccess                  [x] impl  [x] docstring  [x] test
    # [x] getImplementationDataTypeRef        [x] impl  [x] docstring  [x] test
    # [x] setImplementationDataTypeRef        [x] impl  [x] docstring  [x] test
    # [x] getPostBuildValueAccessRef          [x] impl  [x] docstring  [x] test
    # [x] setPostBuildValueAccessRef          [x] impl  [x] docstring  [x] test
    # [x] getPostBuildVariantConditions       [x] impl  [x] docstring  [x] test
    # [x] addPostBuildVariantCondition        [x] impl  [x] docstring  [x] test
    # [x] getValueAccess                      [x] impl  [x] docstring  [x] test
    # [x] setValueAccess                      [x] impl  [x] docstring  [x] test

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This condition acts as Binding Function for the Variation Point.
        self.conditionAccess: Optional[ConditionByFormula] = None

        # This association to ImplementationDataType shall be taken as an
        # implementation hint by the RTE generator.
        self.implementationDataTypeRef: Optional[RefType] = None

        # This represents the applicable PostBuildVariantCriterion in the
        # context of a VariationPointProxy.
        self.postBuildValueAccessRef: Optional[RefType] = None

        # This represents that applicable PostBuildVariantCondition in the
        # context of a VariationPointProxy.
        self.postBuildVariantConditions: List[PostBuildVariantCondition] = []

        # This value acts as Binding Function for the VariationPoint.
        # Spec type: AttributeValueVariationPoint (abstract, not yet
        # implemented); carried as ARObject placeholder. See deviation tracker
        # "class not yet implemented".
        self.valueAccess: Optional[ARObject] = None

    def getConditionAccess(self) -> Optional[ConditionByFormula]:
        """Gets the condition acting as Binding Function for the Variation Point."""
        return self.conditionAccess

    def setConditionAccess(self, value: Optional[ConditionByFormula]) -> "VariationPointProxy":
        """
        Sets the condition acting as Binding Function for the Variation Point.
        A None value is a no-op and does not overwrite an existing
        conditionAccess.
        """
        if value is not None:
            self.conditionAccess = value
        return self

    def getImplementationDataTypeRef(self) -> Optional[RefType]:
        """Gets the ImplementationDataType reference used as an implementation hint by the RTE generator."""
        return self.implementationDataTypeRef

    def setImplementationDataTypeRef(self, value: Optional[RefType]) -> "VariationPointProxy":
        """
        Sets the ImplementationDataType reference used as an implementation
        hint by the RTE generator. A None value is a no-op and does not
        overwrite an existing implementationDataTypeRef.
        """
        if value is not None:
            self.implementationDataTypeRef = value
        return self

    def getPostBuildValueAccessRef(self) -> Optional[RefType]:
        """Gets the applicable PostBuildVariantCriterion in the context of a VariationPointProxy."""
        return self.postBuildValueAccessRef

    def setPostBuildValueAccessRef(self, value: Optional[RefType]) -> "VariationPointProxy":
        """
        Sets the applicable PostBuildVariantCriterion in the context of a
        VariationPointProxy. A None value is a no-op and does not overwrite an
        existing postBuildValueAccessRef.
        """
        if value is not None:
            self.postBuildValueAccessRef = value
        return self

    def getPostBuildVariantConditions(self) -> List[PostBuildVariantCondition]:
        """Gets the applicable PostBuildVariantConditions in the context of a VariationPointProxy."""
        return self.postBuildVariantConditions

    def addPostBuildVariantCondition(self, value: Optional[PostBuildVariantCondition]) -> "VariationPointProxy":
        """
        Adds an applicable PostBuildVariantCondition in the context of a
        VariationPointProxy. A None value is a no-op and does not append to
        postBuildVariantConditions.
        """
        if value is not None:
            self.postBuildVariantConditions.append(value)
        return self

    def getValueAccess(self) -> Optional[ARObject]:
        """Gets the value acting as Binding Function for the VariationPoint."""
        return self.valueAccess

    def setValueAccess(self, value: Optional[ARObject]) -> "VariationPointProxy":
        """
        Sets the value acting as Binding Function for the VariationPoint.
        A None value is a no-op and does not overwrite an existing valueAccess.
        """
        if value is not None:
            self.valueAccess = value
        return self

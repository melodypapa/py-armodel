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
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                         [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getConditionAccess               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setConditionAccess               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getImplementationDataTypeRef     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setImplementationDataTypeRef     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getPostBuildValueAccessRef       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setPostBuildValueAccessRef       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getPostBuildVariantConditions    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addPostBuildVariantCondition     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getValueAccess                   [x] impl  [x] docstring  [x] test  [x] reader  [x] writer
    # [x] setValueAccess                   [x] impl  [x] docstring  [x] test  [x] reader  [x] writer

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
        """
        This condition acts as Binding Function for the Variation Point.

        Returns:
            Optional[ConditionByFormula]: The conditionAccess
        """
        return self.conditionAccess

    def setConditionAccess(self, value: Optional[ConditionByFormula]) -> "VariationPointProxy":
        """
        This condition acts as Binding Function for the Variation Point. A None value is a no-op and does not overwrite an existing conditionAccess.

        Args:
            value: The conditionAccess to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.conditionAccess = value
        return self

    def getImplementationDataTypeRef(self) -> Optional[RefType]:
        """
        This association to ImplementationDataType shall be taken as an implementation hint by the RTE generator.

        Returns:
            Optional[RefType]: The implementationDataTypeRef
        """
        return self.implementationDataTypeRef

    def setImplementationDataTypeRef(self, value: Optional[RefType]) -> "VariationPointProxy":
        """
        This association to ImplementationDataType shall be taken as an implementation hint by the RTE generator. A None value is a no-op and does not overwrite an existing implementationDataTypeRef.

        Args:
            value: The implementationDataTypeRef to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.implementationDataTypeRef = value
        return self

    def getPostBuildValueAccessRef(self) -> Optional[RefType]:
        """
        This represents the applicable PostBuildVariantCriterion in the context of a VariationPointProxy. Note that the technical details how to access the particular postBuildValueAccess are still considered internal to the RTE and are consequently not standardized.

        Returns:
            Optional[RefType]: The postBuildValueAccessRef
        """
        return self.postBuildValueAccessRef

    def setPostBuildValueAccessRef(self, value: Optional[RefType]) -> "VariationPointProxy":
        """
        This represents the applicable PostBuildVariantCriterion in the context of a VariationPointProxy. Note that the technical details how to access the particular postBuildValueAccess are still considered internal to the RTE and are consequently not standardized. A None value is a no-op and does not overwrite an existing postBuildValueAccessRef.

        Args:
            value: The postBuildValueAccessRef to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.postBuildValueAccessRef = value
        return self

    def getPostBuildVariantConditions(self) -> List[PostBuildVariantCondition]:
        """
        This represents that applicable PostBuoldVariant Condition in the context of aVariationPointProxy.

        Returns:
            List[PostBuildVariantCondition]: The postBuildVariantConditions
        """
        return self.postBuildVariantConditions

    def addPostBuildVariantCondition(self, value: Optional[PostBuildVariantCondition]) -> "VariationPointProxy":
        """
        This represents that applicable PostBuoldVariant Condition in the context of aVariationPointProxy. A None value is a no-op and does not append to postBuildVariantConditions.

        Args:
            value: The postBuildVariantCondition to add

        Returns:
            self for method chaining
        """
        if value is not None:
            self.postBuildVariantConditions.append(value)
        return self

    def getValueAccess(self) -> Optional[AttributeValueVariationPoint]:
        """
        This value acts as Binding Function for the VariationPoint.

        Returns:
            Optional[AttributeValueVariationPoint]: The valueAccess
        """
        return self.valueAccess

    def setValueAccess(self, value: Optional[AttributeValueVariationPoint]) -> "VariationPointProxy":
        """
        This value acts as Binding Function for the VariationPoint. A None value is a no-op and does not overwrite an existing valueAccess.

        Args:
            value: The valueAccess to set

        Returns:
            self for method chaining
        """
        if value is not None:
            self.valueAccess = value
        return self

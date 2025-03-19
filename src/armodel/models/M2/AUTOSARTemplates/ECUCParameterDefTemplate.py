from abc import ABCMeta
from typing import List

from ....models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum, Boolean, PositiveInteger, RefType
from ....models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from ....models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject


# class EcucConditionFormula(FormulaExpression)

class EcucConditionSpecification(ARObject):
    def __init__(self):
        super().__init__()

        # self.conditionFormula: EcucConditionFormula = None


class EcucValidationCondition(Identifiable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class EcucScopeEnum(AREnum):
    def __init__(self):
        super().__init__([])


class EcucDefinitionElement(Identifiable, metaclass=ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.ecucCond: EcucConditionSpecification = None
        self.ecucValidationConds: List[EcucValidationCondition] = []
        self.lowerMultiplicity: PositiveInteger = None
        self.relatedTraceItemRef: RefType = None
        self.scope: EcucScopeEnum = None
        self.upperMultiplicity: PositiveInteger = None
        self.upperMultiplicityInfinite: Boolean = None

    def getEcucCond(self) -> EcucConditionSpecification:
        return self.ecucCond

    def setEcucCond(self, value: EcucConditionSpecification):
        if value is not None:
            self.ecucCond = value
        return self

    def getEcucValidationConds(self) -> List[EcucValidationCondition]:
        return self.ecucValidationConds

    def addEcucValidationCond(self, value: EcucValidationCondition):
        if value is not None:
            self.ecucValidationConds.append(value)
        return self

    def getLowerMultiplicity(self) -> PositiveInteger:
        return self.lowerMultiplicity

    def setLowerMultiplicity(self, value: PositiveInteger):
        if value is not None:
            self.lowerMultiplicity = value
        return self

    def getRelatedTraceItemRef(self) -> RefType:
        return self.relatedTraceItemRef

    def setRelatedTraceItemRef(self, value: RefType):
        if value is not None:
            self.relatedTraceItemRef = value
        return self

    def getScope(self) -> EcucScopeEnum:
        return self.scope

    def setScope(self, value: EcucScopeEnum):
        if value is not None:
            self.scope = value
        return self

    def getUpperMultiplicity(self) -> PositiveInteger:
        return self.upperMultiplicity

    def setUpperMultiplicity(self, value: PositiveInteger):
        if value is not None:
            self.upperMultiplicity = value
        return self

    def getUpperMultiplicityInfinite(self) -> Boolean:
        return self.upperMultiplicityInfinite

    def setUpperMultiplicityInfinite(self, value: Boolean):
        if value is not None:
            self.upperMultiplicityInfinite = value
        return self
    

class EcucContainerDef(EcucDefinitionElement, metaclass=ABCMeta):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class EcucParamConfContainerDef(EcucContainerDef):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class EcucChoiceContainerDef(EcucContainerDef):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

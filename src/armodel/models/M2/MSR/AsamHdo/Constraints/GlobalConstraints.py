from typing import List
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure import AtpBlueprintable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARNumerical, Limit, RefType

class InternalConstrs(ARObject):
    """
    Represents internal constraints for data values.
    Base: ARObject
    """
    def __init__(self):
        super().__init__()

        self.lower_limit: Limit = None
        self.upper_limit: Limit = None


class PhysConstrs(ARObject):
    """
    Represents physical constraints for data values with unit reference.
    Base: ARObject
    """
    def __init__(self):
        super().__init__()

        self.lower_limit: Limit = None
        self.upper_limit: Limit = None
        self.unit_ref: RefType = None


class DataConstrRule(ARObject):
    """
    Represents a single data constraint rule with internal and physical constraints.
    Base: ARObject
    """
    def __init__(self):
        super().__init__()

        self.constrLevel: ARNumerical = None
        self.internalConstrs: InternalConstrs = None
        self.physConstrs: PhysConstrs = None


class DataConstr(AtpBlueprintable):
    """
    Represents data constraints with multiple rules.
    Base: AtpBlueprintable
    """
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.data_constr_rule: List[DataConstrRule] = []

    def addDataConstrRule(self, rule: DataConstrRule):
        self.data_constr_rule.append(rule)

    def getDataConstrRules(self) -> List[DataConstrRule]:
        return self.data_constr_rule
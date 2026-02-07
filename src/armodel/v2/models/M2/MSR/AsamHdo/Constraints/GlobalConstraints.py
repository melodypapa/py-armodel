from typing import List, Union

from armodel.v2.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure import (
    AtpBlueprintable,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARNumerical,
    Limit,
    RefType,
)


class InternalConstrs(ARObject):
    """
    Represents internal constraints for data values.
    Base: ARObject
    """

    def __init__(self) -> None:
        super().__init__()

        self.lower_limit: Union[Union[Limit, None] , None] = None
        self.upper_limit: Union[Union[Limit, None] , None] = None


class PhysConstrs(ARObject):
    """
    Represents physical constraints for data values with unit reference.
    Base: ARObject
    """

    def __init__(self) -> None:
        super().__init__()

        self.lower_limit: Union[Union[Limit, None] , None] = None
        self.upper_limit: Union[Union[Limit, None] , None] = None
        self.unit_ref: Union[Union[RefType, None] , None] = None


class DataConstrRule(ARObject):
    """
    Represents a single data constraint rule with internal and physical constraints.
    Base: ARObject
    """

    def __init__(self) -> None:
        super().__init__()

        self.constrLevel: Union[Union[ARNumerical, None] , None] = None
        self.internalConstrs: Union[Union[InternalConstrs, None] , None] = None
        self.physConstrs: Union[Union[PhysConstrs, None] , None] = None


class DataConstr(AtpBlueprintable):
    """
    Represents data constraints with multiple rules.
    Base: AtpBlueprintable
    """
    def __init__(self, parent: ARObject, short_name: str) -> None:
        super().__init__(parent, short_name)

        self.data_constr_rule: List[DataConstrRule] = []

    def addDataConstrRule(self, rule: DataConstrRule) -> None:
        self.data_constr_rule.append(rule)

    def getDataConstrRules(self) -> List[DataConstrRule]:
        return self.data_constr_rule

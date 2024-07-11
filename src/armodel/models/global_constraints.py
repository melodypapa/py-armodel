from .ar_ref import RefType
from .ar_object import ARObject
from .general_structure import Identifiable, Limit

from typing import List

class InternalConstrs(ARObject):
    def __init__(self):
        super().__init__()

        self.lower_limit = None         # type: Limit
        self.upper_limit = None         # type: Limit

class PhysConstrs(ARObject):
    def __init__(self):
        super().__init__()

        self.lower_limit = None         # type: Limit
        self.upper_limit = None         # type: Limit
        self.unit_ref = None            # type: RefType

class DataConstrRule(ARObject):
    def __init__(self):
        super().__init__()

        self.constr_level = None        # type: int
        self.internal_constrs = None    # type: InternalConstrs    
        self.phys_constrs = None        # type: PhysConstrs

class DataConstr(Identifiable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.data_constr_rule = []    #  type: List[DataConstrRule]

    def addDataConstrRule(self, rule: DataConstrRule):
        self.data_constr_rule.append(rule)

    def getDataConstrRules(self) -> List[DataConstrRule]:
        return self.data_constr_rule
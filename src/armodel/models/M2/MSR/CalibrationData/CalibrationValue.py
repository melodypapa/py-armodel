from typing import List
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARNumerical, RefType
from ....M2.MSR.DataDictionary.DataDefProperties import ValueList

class SwValues(ARObject):
    def __init__(self):
        super().__init__()

        self._v = []                    # type: List[ARNumerical]
        self.vt = None                  # type: float

    def addV(self, v: ARNumerical):
        self._v.append(v)

    def getVs(self) -> List[ARNumerical]:
        return self._v


class SwValueCont(ARObject):
    def __init__(self):
        super().__init__()

        self.sw_arraysize = None         # type: ValueList
        self.unit_ref = None             # type: RefType
        self.sw_values_phys = None        # type: SwValues
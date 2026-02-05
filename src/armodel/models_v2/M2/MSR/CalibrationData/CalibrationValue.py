from typing import List

from armodel.models_v2.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.models_v2.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARNumerical,
)


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

        self.swArraysize = None             # type: ValueList
        self.swValuesPhys = None            # type: SwValues
        self.unitRef = None                 # type: RefType
        self.unitDisplayName = None         # type: SingleLanguageUnitNames

    def getSwArraysize(self):
        return self.swArraysize

    def setSwArraysize(self, value):
        self.swArraysize = value
        return self

    def getSwValuesPhys(self):
        return self.swValuesPhys

    def setSwValuesPhys(self, value):
        self.swValuesPhys = value
        return self

    def getUnitRef(self):
        return self.unitRef

    def setUnitRef(self, value):
        self.unitRef = value
        return self

    def getUnitDisplayName(self):
        return self.unitDisplayName

    def setUnitDisplayName(self, value):
        self.unitDisplayName = value
        return self

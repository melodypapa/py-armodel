from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARNumerical,
)


class SwValues(ARObject):

    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    def __init__(self) -> None:
        super().__init__()

        self._v = []                    # type: List[ARNumerical]
        self.vt: Union[float, None] = None

    def addV(self, v: ARNumerical):
        self._v.append(v)

    def getVs(self) -> List[ARNumerical]:
        return self._v


class SwValueCont(ARObject):

    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    def __init__(self) -> None:
        super().__init__()

        self.swArraysize: Union[ValueList, None] = None
        self.swValuesPhys: Union[SwValues, None] = None
        self.unitRef: Union[RefType, None] = None
        self.unitDisplayName: Union[SingleLanguageUnitNames, None] = None

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

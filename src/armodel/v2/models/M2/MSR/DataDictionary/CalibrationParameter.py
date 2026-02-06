from abc import ABC
from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class SwCalprmAxisTypeProps(ARObject, ABC):
    def __init__(self) -> None:
        if type(self) is SwCalprmAxisTypeProps:
            raise TypeError("SwCalprmAxisTypeProps is an abstract class.")

        super().__init__()

        self.maxGradient = None         # type: ARFloat
        self.monotony = None            # type: MonotonyEnum


class SwCalprmAxis(ARObject):

    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    def __init__(self) -> None:
        super().__init__()

        self.category = None                        # type: CalprmAxisCategoryEnum
        self.displayFormat = None                   # type: DisplayFormatString
        self.sw_axis_index = None                   # type: AxisIndexType
        self.swCalibrationAccess = None             # type: SwCalibrationAccessEnum
        self.sw_calprm_axis_type_props = None       # type: SwCalprmAxisTypeProps

class SwCalprmAxisSet(ARObject):

    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    def __init__(self) -> None:
        super().__init__()

        self._swCalprmAxis = []          # type: List[SwCalprmAxis]

    def addSwCalprmAxis(self, axis: SwCalprmAxis):
        self._swCalprmAxis.append(axis)

    def getSwCalprmAxises(self) -> List[SwCalprmAxis]:
        return self._swCalprmAxis

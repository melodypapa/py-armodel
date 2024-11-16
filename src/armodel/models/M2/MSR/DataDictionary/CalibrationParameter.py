from typing import List
from ...AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from ...AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARFloat

from abc import ABCMeta
class SwCalprmAxisTypeProps(ARObject, metaclass = ABCMeta):
    def __init__(self):
        if type(self) == SwCalprmAxisTypeProps:
            raise NotImplementedError("SwCalprmAxisTypeProps is an abstract class.")

        super().__init__()

        self.maxGradient = None         # type: ARFloat
        self.monotony = None            # type: MonotonyEnum


class SwCalprmAxis(ARObject):
    def __init__(self):
        super().__init__()

        self.category = None                        # type: CalprmAxisCategoryEnum
        self.displayFormat = None                   # type: DisplayFormatString
        self.sw_axis_index = None                   # type: AxisIndexType   
        self.swCalibrationAccess = None             # type: SwCalibrationAccessEnum
        self.sw_calprm_axis_type_props = None       # type: SwCalprmAxisTypeProps

class SwCalprmAxisSet(ARObject):
    def __init__(self):
        super().__init__()

        self._swCalprmAxis = []          # type: List[SwCalprmAxis]

    def addSwCalprmAxis(self, axis: SwCalprmAxis):
        self._swCalprmAxis.append(axis)

    def getSwCalprmAxises(self) -> List[SwCalprmAxis]:
        return self._swCalprmAxis
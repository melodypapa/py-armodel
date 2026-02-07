from abc import ABC
from typing import List, Union

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AREnum,
    ARFloat,
    DisplayFormatString,
    MonotonyEnum,
)
from armodel.v2.models.M2.MSR.DataDictionary.DataDefProperties import (
    SwCalibrationAccessEnum,
)
from armodel.v2.models.M2.MSR.DataDictionary.RecordLayout import (
    AxisIndexType,
)


class CalprmAxisCategoryEnum(AREnum):
    """
    Enumeration of calibration parameter axis categories.

    This enum specifies the possible values of the category property
    within SwCalprmAxis.
    """
    SOFTWARE = 'Software'
    AUTOSAR = 'AUTOSAR'
    COM_AXIS = 'comAxis'
    FIX_AXIS = 'fixAXIS'
    RES_AXIS = 'resAxis'
    STD_AXIS = 'stdAxis'

    def __init__(self) -> None:
        super().__init__([
            CalprmAxisCategoryEnum.SOFTWARE,
            CalprmAxisCategoryEnum.AUTOSAR,
            CalprmAxisCategoryEnum.COM_AXIS,
            CalprmAxisCategoryEnum.FIX_AXIS,
            CalprmAxisCategoryEnum.RES_AXIS,
            CalprmAxisCategoryEnum.STD_AXIS,
        ])

class SwCalprmAxisTypeProps(ARObject, ABC):
    def __init__(self) -> None:
        if type(self) is SwCalprmAxisTypeProps:
            raise TypeError("SwCalprmAxisTypeProps is an abstract class.")

        super().__init__()

        self.maxGradient: Union[ARFloat, None] = None
        self.monotony: Union[MonotonyEnum, None] = None


class SwCalprmAxis(ARObject):

    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    def __init__(self) -> None:
        super().__init__()

        self.category: Union[CalprmAxisCategoryEnum, None] = None
        self.displayFormat: Union[DisplayFormatString, None] = None
        self.sw_axis_index: Union[AxisIndexType, None] = None
        self.swCalibrationAccess: Union[SwCalibrationAccessEnum, None] = None
        self.sw_calprm_axis_type_props: Union[SwCalprmAxisTypeProps, None] = None

class SwCalprmAxisSet(ARObject):

    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    def __init__(self) -> None:
        super().__init__()

        self._swCalprmAxis = []          # type: List[SwCalprmAxis]

    def addSwCalprmAxis(self, axis: SwCalprmAxis) -> None:
        self._swCalprmAxis.append(axis)

    def getSwCalprmAxises(self) -> List[SwCalprmAxis]:
        return self._swCalprmAxis

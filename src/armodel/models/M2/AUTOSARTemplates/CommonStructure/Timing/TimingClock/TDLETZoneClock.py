from typing import Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime import (
    MultidimensionalTime,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingClock.TimingClock import (
    TimingClock,
)


class TDLETZoneClock(TimingClock):
    """
    Describes a LET zone clock.
    """

    # TDLETZoneClock method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table D.58, p.252
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getAccuracyExt    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setAccuracyExt    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getAccuracyInt    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setAccuracyInt    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent, short_name: str):
        super().__init__(parent, short_name)

        # External synchronization accuracy within the LET Zone/ Zone Clock.
        self.accuracyExt: Optional[MultidimensionalTime] = None

        # Internal synchronization accuracy within the LET Zone/ Zone Clock.
        self.accuracyInt: Optional[MultidimensionalTime] = None

    def getAccuracyExt(self) -> Optional[MultidimensionalTime]:
        """External synchronization accuracy within the LET Zone/ Zone Clock."""
        return self.accuracyExt

    def setAccuracyExt(self, value: Optional[MultidimensionalTime]) -> "TDLETZoneClock":
        """External synchronization accuracy within the LET Zone/ Zone Clock. A None value is a no-op and does not overwrite an existing accuracyExt."""
        if value is not None:
            self.accuracyExt = value
        return self

    def getAccuracyInt(self) -> Optional[MultidimensionalTime]:
        """Internal synchronization accuracy within the LET Zone/ Zone Clock."""
        return self.accuracyInt

    def setAccuracyInt(self, value: Optional[MultidimensionalTime]) -> "TDLETZoneClock":
        """Internal synchronization accuracy within the LET Zone/ Zone Clock. A None value is a no-op and does not overwrite an existing accuracyInt."""
        if value is not None:
            self.accuracyInt = value
        return self

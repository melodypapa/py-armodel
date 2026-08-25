from typing import Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime import (
    MultidimensionalTime,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class TimingClockSyncAccuracy(Identifiable):
    """
    Describes the synchronization accuracy between exactly two TDClocks.
    """

    # TimingClockSyncAccuracy method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table D.60, p.252
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__       [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getAccuracy    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setAccuracy    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getLowerRef    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setLowerRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getUpperRef    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setUpperRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Synchronization accuracy, treated as zero if not given.
        self.accuracy: Optional[MultidimensionalTime] = None

        # References a target clock
        self.lowerRef: Optional[RefType] = None

        # References a source clock
        self.upperRef: Optional[RefType] = None

    def getAccuracy(self) -> Optional[MultidimensionalTime]:
        """Synchronization accuracy, treated as zero if not given."""
        return self.accuracy

    def setAccuracy(self, value: Optional[MultidimensionalTime]) -> "TimingClockSyncAccuracy":
        """Synchronization accuracy, treated as zero if not given. A None value is a no-op and does not overwrite an existing accuracy."""
        if value is not None:
            self.accuracy = value
        return self

    def getLowerRef(self) -> Optional[RefType]:
        """References a target clock"""
        return self.lowerRef

    def setLowerRef(self, value: Optional[RefType]) -> "TimingClockSyncAccuracy":
        """References a target clock. A None value is a no-op and does not overwrite an existing lowerRef."""
        if value is not None:
            self.lowerRef = value
        return self

    def getUpperRef(self) -> Optional[RefType]:
        """References a source clock"""
        return self.upperRef

    def setUpperRef(self, value: Optional[RefType]) -> "TimingClockSyncAccuracy":
        """References a source clock. A None value is a no-op and does not overwrite an existing upperRef."""
        if value is not None:
            self.upperRef = value
        return self

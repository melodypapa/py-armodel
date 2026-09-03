from abc import ABC
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.VariationPointCapable import VariationPointCapable
from typing import Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime import MultidimensionalTime
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType


class TimingClock(Identifiable, VariationPointCapable, ABC):
    """
    Describes an abstract clock.
    """

    # TimingClock method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table D.59, p.252
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                 [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getPlatformTimeBaseRef   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setPlatformTimeBaseRef   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is TimingClock:
            raise TypeError("TimingClock is an abstract class.")

        super().__init__(parent, short_name)

        # Refers to a physical time base reference on the respective platform level
        # Placeholder: GlobalTimeDomain not yet implemented (Rule 0001.10); typed RefType.
        self.platformTimeBaseRef: Optional[RefType] = None

    def getPlatformTimeBaseRef(self) -> Optional[RefType]:
        """Refers to a physical time base reference on the respective platform level."""
        return self.platformTimeBaseRef

    def setPlatformTimeBaseRef(self, value: Optional[RefType]) -> "TimingClock":
        """Refers to a physical time base reference on the respective platform level. A None value is a no-op and does not overwrite an existing platformTimeBaseRef."""
        if value is not None:
            self.platformTimeBaseRef = value
        return self


class TDLETZoneClock(TimingClock):
    """
    Describes a LET zone clock.
    """

    # TDLETZoneClock method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table D.58, p.252
    # Spec verified: R23-11
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


class TimingClockSyncAccuracy(Identifiable, VariationPointCapable):
    """
    Describes the synchronization accuracy between exactly two TDClocks.
    """

    # TimingClockSyncAccuracy method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table D.60, p.252
    # Spec verified: R23-11
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

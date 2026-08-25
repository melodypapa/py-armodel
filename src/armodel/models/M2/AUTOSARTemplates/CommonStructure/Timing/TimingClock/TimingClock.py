from abc import ABC
from typing import Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class TimingClock(Identifiable, ABC):
    """
    Describes an abstract clock.
    """

    # TimingClock method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table D.59, p.252
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

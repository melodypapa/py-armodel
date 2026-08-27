from abc import ABC
from typing import Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements.RequirementsTracing import (
    Traceable,
)


class TimingConstraint(Traceable, ABC):
    """
    The abstract parent class of different timing constraints supported by the Timing extension. A concrete timing constraint is used to bound the timing behavior of the model elements in its scope.
    """

    # TimingConstraint method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table D.61, p.253
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__               [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getTimingConditionRef  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTimingConditionRef  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is TimingConstraint:
            raise TypeError("TimingConstraint is an abstract class.")

        super().__init__(parent, short_name)

        # A timing condition the timing constraint depends on. In other words it specifies the condition the timing constraint holds.
        self.timingConditionRef: Optional[RefType] = None

    def getTimingConditionRef(self) -> Optional[RefType]:
        """A timing condition the timing constraint depends on. In other words it specifies the condition the timing constraint holds."""
        return self.timingConditionRef

    def setTimingConditionRef(self, value: Optional[RefType]) -> "TimingConstraint":
        """A timing condition the timing constraint depends on. In other words it specifies the condition the timing constraint holds. A None value is a no-op and does not overwrite an existing timingConditionRef."""
        if value is not None:
            self.timingConditionRef = value
        return self

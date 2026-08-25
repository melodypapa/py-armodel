from __future__ import annotations

from typing import Optional, TYPE_CHECKING

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition import TimingConditionFormula


class TimingCondition(Identifiable):
    """
    A TimingCondition describes a dependency on a specific condition. The element owns an expression which describes the timing condition dependency.
    """

    # TimingCondition method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 3.7, p.35
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                   [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getTimingConditionFormula  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTimingConditionFormula  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent, short_name: str):
        super().__init__(parent, short_name)

        # This is the expression describing the dependency on a specific condition.
        self.timingConditionFormula: Optional[TimingConditionFormula] = None

    def getTimingConditionFormula(self) -> Optional[TimingConditionFormula]:
        """This is the expression describing the dependency on a specific condition."""
        return self.timingConditionFormula

    def setTimingConditionFormula(self, value: Optional[TimingConditionFormula]) -> "TimingCondition":
        """This is the expression describing the dependency on a specific condition. A None value is a no-op and does not overwrite an existing formula."""
        if value is not None:
            self.timingConditionFormula = value
        return self

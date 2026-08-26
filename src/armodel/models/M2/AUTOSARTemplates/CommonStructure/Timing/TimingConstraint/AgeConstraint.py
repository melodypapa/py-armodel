"""
This module defines age constraints in AUTOSAR timing specifications.

Age constraints specify the maximum allowed age of data between its creation
and its consumption, ensuring data freshness requirements are met.

Classes:
    AgeConstraint: Specifies the maximum allowed age of data
"""

from typing import Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime import (
    MultidimensionalTime,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint import TimingConstraint
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class AgeConstraint(TimingConstraint):
    """
    Constrains the scope by a minimum and maximum time boundary.

    (scope -> TimingDescriptionEvent placeholder, Rule 0001.10)
    """

    # AgeConstraint method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 3.67, p.115
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__       [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getMaximum     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMaximum     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMinimum     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMinimum     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getScopeRef    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setScopeRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent, short_name: str):
        super().__init__(parent, short_name)

        # The received event referenced by scope should not exceed this upper bound.
        self.maximum: Optional[MultidimensionalTime] = None

        # The received event referenced by scope should not precede this lower bound.
        self.minimum: Optional[MultidimensionalTime] = None

        # TimingDescriptionEvent to be constrained. (TimingDescriptionEvent placeholder, Rule 0001.10)
        self.scopeRef: Optional[RefType] = None

    def getMaximum(self) -> Optional[MultidimensionalTime]:
        """The received event referenced by scope should not exceed this upper bound."""
        return self.maximum

    def setMaximum(self, value: Optional[MultidimensionalTime]) -> "AgeConstraint":
        """The received event referenced by scope should not exceed this upper bound. A None value is a no-op and does not overwrite an existing maximum."""
        if value is not None:
            self.maximum = value
        return self

    def getMinimum(self) -> Optional[MultidimensionalTime]:
        """The received event referenced by scope should not precede this lower bound."""
        return self.minimum

    def setMinimum(self, value: Optional[MultidimensionalTime]) -> "AgeConstraint":
        """The received event referenced by scope should not precede this lower bound. A None value is a no-op and does not overwrite an existing minimum."""
        if value is not None:
            self.minimum = value
        return self

    def getScopeRef(self) -> Optional[RefType]:
        """TimingDescriptionEvent to be constrained."""
        return self.scopeRef

    def setScopeRef(self, value: Optional[RefType]) -> "AgeConstraint":
        """TimingDescriptionEvent to be constrained. A None value is a no-op and does not overwrite an existing scope."""
        if value is not None:
            self.scopeRef = value
        return self

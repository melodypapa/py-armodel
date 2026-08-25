from typing import Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType


class TimingModeInstance(Identifiable):
    """
    This class specifies the mode declaration to be checked in a specific instance of a mode declaration group. This is used in a timing condition formula as an operand of the unary timing function TIMEX_modeActive to check whether the mode declaration is active at the point in time this expression is evaluated.
    """

    # TimingModeInstance method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 3.10, p.37
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getModeInstance         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setModeInstance         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        # This refers to a specific mode declaration in the given context.
        # Placeholder typed Optional[RefType]: the spec type ModeInSwcBswInstanceRef (abstract) is not yet implemented as a model class.
        self.modeInstance: Optional[RefType] = None

    def getModeInstance(self) -> Optional[RefType]:
        """This refers to a specific mode declaration in the given context."""
        return self.modeInstance

    def setModeInstance(self, value: Optional[RefType]) -> "TimingModeInstance":
        """This refers to a specific mode declaration in the given context. A None value is a no-op and does not overwrite an existing modeInstance."""
        if value is not None:
            self.modeInstance = value
        return self

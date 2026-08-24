from typing import Optional

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition.ModeInBswInstanceRef import ModeInBswInstanceRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition.ModeInSwcInstanceRef import ModeInSwcInstanceRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition.TimingCondition import TimingCondition
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition.TimingExtensionResource import TimingExtensionResource
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition.TimingModeInstance import TimingModeInstance
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Referrable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

__all__ = ["ModeInBswInstanceRef", "ModeInSwcInstanceRef", "TimingCondition", "TimingConditionFormula", "TimingExtensionResource", "TimingModeInstance"]


class TimingConditionFormula(Referrable):
    """
    A TimingConditionFormula describes a specific dependency. The expression shall be a boolean expression addressing modes, variables, arguments, and/or events.
    """

    # TimingConditionFormula method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 3.8, p.35
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                 [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getText                  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setText                  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTimingArgumentRef     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTimingArgumentRef     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTimingConditionRef    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTimingConditionRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTimingEventRef        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTimingEventRef        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTimingModeRef         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTimingModeRef         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTimingVariableRef     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setTimingVariableRef     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        # This refers to an argument of an operation call.
        self.timingArgumentRef: Optional[RefType] = None

        # This refers to a timing condition that is part of an expression describing the dependency on a specific condition.
        self.timingConditionRef: Optional[RefType] = None

        # This refers to a timing event.
        self.timingEventRef: Optional[RefType] = None

        # This refers to a mode declaration.
        self.timingModeRef: Optional[RefType] = None

        # This refers to a variable.
        self.timingVariableRef: Optional[RefType] = None

        self._text: Optional[str] = None

    def getText(self) -> Optional[str]:
        """Returns the mixed string content (the boolean expression) of this <<atpMixedString>> TimingConditionFormula."""
        return self._text

    def setText(self, value: Optional[str]) -> "TimingConditionFormula":
        """Sets the mixed string content (the boolean expression) of this <<atpMixedString>> TimingConditionFormula. A None value is a no-op and does not overwrite an existing value."""
        if value is not None:
            self._text = value
        return self

    def getTimingArgumentRef(self) -> Optional[RefType]:
        """This refers to an argument of an operation call."""
        return self.timingArgumentRef

    def setTimingArgumentRef(self, value: Optional[RefType]) -> "TimingConditionFormula":
        """This refers to an argument of an operation call. A None value is a no-op and does not overwrite an existing timingArgumentRef."""
        if value is not None:
            self.timingArgumentRef = value
        return self

    def getTimingConditionRef(self) -> Optional[RefType]:
        """This refers to a timing condition that is part of an expression describing the dependency on a specific condition."""
        return self.timingConditionRef

    def setTimingConditionRef(self, value: Optional[RefType]) -> "TimingConditionFormula":
        """This refers to a timing condition that is part of an expression describing the dependency on a specific condition. A None value is a no-op and does not overwrite an existing timingConditionRef."""
        if value is not None:
            self.timingConditionRef = value
        return self

    def getTimingEventRef(self) -> Optional[RefType]:
        """This refers to a timing event."""
        return self.timingEventRef

    def setTimingEventRef(self, value: Optional[RefType]) -> "TimingConditionFormula":
        """This refers to a timing event. A None value is a no-op and does not overwrite an existing timingEventRef."""
        if value is not None:
            self.timingEventRef = value
        return self

    def getTimingModeRef(self) -> Optional[RefType]:
        """This refers to a mode declaration."""
        return self.timingModeRef

    def setTimingModeRef(self, value: Optional[RefType]) -> "TimingConditionFormula":
        """This refers to a mode declaration. A None value is a no-op and does not overwrite an existing timingModeRef."""
        if value is not None:
            self.timingModeRef = value
        return self

    def getTimingVariableRef(self) -> Optional[RefType]:
        """This refers to a variable."""
        return self.timingVariableRef

    def setTimingVariableRef(self, value: Optional[RefType]) -> "TimingConditionFormula":
        """This refers to a variable. A None value is a no-op and does not overwrite an existing timingVariableRef."""
        if value is not None:
            self.timingVariableRef = value
        return self

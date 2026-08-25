from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCondition.TimingModeInstance import TimingModeInstance
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType


class TimingExtensionResource(Identifiable):
    """
    A TimingExtensionResource provides the capability to contain instance references referred from within a timing condition formula.
    """

    # TimingExtensionResource method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table 3.9, p.36
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                 [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] addTimingArgument        [x] impl  [x] docstring  [x] test  [ ] reader  [ ] writer
    # [x] getTimingArguments       [x] impl  [x] docstring  [x] test  [—] reader  [ ] writer
    # [x] createTimingMode         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getTimingModes           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addTimingVariable        [x] impl  [x] docstring  [x] test  [ ] reader  [ ] writer
    # [x] getTimingVariables       [x] impl  [x] docstring  [x] test  [—] reader  [ ] writer
    # The timingArgument and timingVariable rows stay [ ] (pending): the item classes
    # AutosarOperationArgumentInstance and AutosarVariableInstance are not yet implemented.

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        # This refers to an instance reference of an argument of an operation call.
        # Placeholder typed List[RefType]: the spec item type AutosarOperationArgumentInstance is not yet implemented as a model class.
        self.timingArguments: List[RefType] = []

        # This refers to an instance reference of a mode declaration.
        self.timingModes: List[TimingModeInstance] = []

        # This refers to an instance reference of a variable.
        # Placeholder typed List[RefType]: the spec item type AutosarVariableInstance is not yet implemented as a model class.
        self.timingVariables: List[RefType] = []

    def addTimingArgument(self, value: Optional[RefType]) -> "TimingExtensionResource":
        """This refers to an instance reference of an argument of an operation call. A None value is a no-op and does not append anything."""
        if value is not None:
            self.timingArguments.append(value)
        return self

    def getTimingArguments(self) -> List[RefType]:
        """This refers to an instance reference of an argument of an operation call."""
        return self.timingArguments

    def createTimingMode(self, short_name: str) -> TimingModeInstance:
        """This refers to an instance reference of a mode declaration."""
        if not self.IsElementExists(short_name):
            mode = TimingModeInstance(self, short_name)
            self.addElement(mode)
            self.timingModes.append(mode)
        return self.getElement(short_name, TimingModeInstance)

    def getTimingModes(self) -> List[TimingModeInstance]:
        """This refers to an instance reference of a mode declaration."""
        return self.timingModes

    def addTimingVariable(self, value: Optional[RefType]) -> "TimingExtensionResource":
        """This refers to an instance reference of a variable. A None value is a no-op and does not append anything."""
        if value is not None:
            self.timingVariables.append(value)
        return self

    def getTimingVariables(self) -> List[RefType]:
        """This refers to an instance reference of a variable."""
        return self.timingVariables

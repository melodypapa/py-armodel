from ......M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.ExecutionOrderConstraint import ExecutionOrderConstraint
from ......M2.AUTOSARTemplates.CommonStructure.Timing.TimingConstraint.TimingConstraint import TimingConstraint
from ......M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from ......M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from abc import ABCMeta
from typing import List


class TimingExtension(Identifiable):
    __metaclass__ = ABCMeta

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == TimingExtension:
            raise NotImplementedError("TimingExtension is an abstract class.")

        super().__init__(parent, short_name)

        self.timing_requirements = []           # Type: List[TimingConstraint]

    def createExecutionOrderConstraint(self, short_name: str)-> ExecutionOrderConstraint:
        if not self.IsElementExists(short_name):
            constraint = ExecutionOrderConstraint(self, short_name)
            self.addElement(constraint)
            self.timing_requirements.append(constraint)
        return self.getElement(short_name, ExecutionOrderConstraint)

    def getTimingRequirements(self) -> List[TimingConstraint]:
        return self.timing_requirements


class SwcTiming(TimingExtension):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)
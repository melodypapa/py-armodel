from ......M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from ......M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from ......M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from abc import ABCMeta


class TimingConstraint(Identifiable):
    __metaclass__ = ABCMeta

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == TimingConstraint:
            raise NotImplementedError("TimingExtension is an abstract class.")

        super().__init__(parent, short_name)

        self.timing_condition_ref = None                # type: RefType

    @property
    def timingConditionRef(self) -> RefType:
        return self.timing_condition_ref

    @timingConditionRef.setter
    def timingConditionRef(self, ref: RefType):
        self.timing_condition_ref = ref
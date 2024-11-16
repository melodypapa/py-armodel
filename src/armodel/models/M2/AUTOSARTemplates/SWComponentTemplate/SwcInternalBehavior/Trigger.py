
from .AccessCount import AbstractAccessPoint
from ...GenericStructure.GeneralTemplateClasses.ArObject import ARObject


class InternalTriggeringPoint(AbstractAccessPoint):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name) 

        self.sw_impl_policy = None
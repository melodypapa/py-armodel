from ..GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from ..GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from ..CommonStructure.Implementation import Implementation

class SwcImplementation(Implementation):
    def __init__(self, parent: ARObject, short_name: str) -> None:
        super().__init__(parent, short_name)

        self.behavior_ref = None                        # type: RefType
        self.per_instance_memory_size = None
        self.required_rte_vendor = ""
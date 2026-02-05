from armodel.models_v2.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models_v2.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models_v2.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum

class SwServiceArg(Identifiable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.direction = None                   # type: ArgumentDirectionEnum
        self.swArraysize = None                 # type: ValueList
        self.swDataDefProps = None              # type: SwDataDefProps

    def getDirection(self):
        return self.direction

    def setDirection(self, value):
        self.direction = value
        return self

    def getSwArraysize(self):
        return self.swArraysize

    def setSwArraysize(self, value):
        self.swArraysize = value
        return self

    def getSwDataDefProps(self):
        return self.swDataDefProps

    def setSwDataDefProps(self, value):
        self.swDataDefProps = value
        return self


class SwServiceImplPolicyEnum(AREnum):
    """
    Enumeration for SW Service Implementation Policy values.
    Defines how software service implementations should be generated in code.
    """
    # Implementation should be inlined
    INLINE = "INLINE"
    # Implementation should be inlined conditionally based on configuration
    INLINE_CONDITIONAL = "INLINE-CONDITIONAL"
    # Implementation should be generated as a macro
    MACRO = "MACRO"
    # Standard implementation (not inlined)
    STANDARD = "STANDARD"

    def __init__(self):
        super().__init__((
            SwServiceImplPolicyEnum.INLINE,
            SwServiceImplPolicyEnum.INLINE_CONDITIONAL,
            SwServiceImplPolicyEnum.MACRO,
            SwServiceImplPolicyEnum.STANDARD,
        ))

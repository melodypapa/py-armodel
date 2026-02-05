from armodel.models_v2.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class ModeInSwcInstanceRef(RefType):
    """
    Represents a reference to a mode in a SWC instance.
    Used for referencing modes within software component instances.
    """

    def __init__(self):
        """
        Initializes the ModeInSwcInstanceRef with default values.
        """
        super().__init__()

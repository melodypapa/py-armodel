from armodel.models_v2.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class ModeInBswInstanceRef(RefType):
    """
    Represents a reference to a mode in a BSW instance.
    Used for referencing modes within BSW module instances.
    """

    def __init__(self):
        """
        Initializes the ModeInBswInstanceRef with default values.
        """
        super().__init__()

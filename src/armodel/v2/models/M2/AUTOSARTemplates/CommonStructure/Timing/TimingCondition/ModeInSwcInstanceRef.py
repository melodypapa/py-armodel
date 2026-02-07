from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class ModeInSwcInstanceRef(RefType):

    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass    """
    Represents a reference to a mode in a SWC instance.
    Used for referencing modes within software component instances.
    """

    def __init__(self) -> None:
        """
        Initializes the ModeInSwcInstanceRef with default values.
        """
        super().__init__()

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    RefType,
)


class ImplementationElementInParameterInstanceRef(RefType):
    """
    Represents a reference to an implementation element in a parameter instance.
    Used for referencing implementation elements within parameter instances in AUTOSAR models.
    """

    def __init__(self) -> None:
        """
        Initializes the ImplementationElementInParameterInstanceRef with default values.
        """
        super().__init__()

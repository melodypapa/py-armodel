from armodel.models_v2.M2.AUTOSARTemplates.CommonStructure import (
    ValueSpecification,
)
from armodel.models_v2.M2.AUTOSARTemplates.GenericStructure.RolesAndRights.AtpDefinition import (
    AtpDefinition,
)


class SwSystemconst(AtpDefinition):
    """
    Represents a software system constant in the AUTOSAR model.

    This class is used to define system constants that are used throughout
    the software configuration.

    Attributes:
        value (ValueSpecification): The value of the system constant.
    """

    def __init__(self, parent, short_name: str):
        super().__init__(parent, short_name)

        self.value: ValueSpecification = None

    def getValue(self) -> ValueSpecification:
        return self.value

    def setValue(self, value: ValueSpecification):
        if value is not None:
            self.value = value
        return self

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure import ValueSpecification


class SwSystemconst(ARObject):
    """
    Represents a software system constant in the AUTOSAR model.

    This class is used to define system constants that are used throughout
    the software configuration.

    Attributes:
        value (ValueSpecification): The value of the system constant.
    """
    def __init__(self):
        super().__init__()

        self.value: ValueSpecification = None

    def getValue(self) -> ValueSpecification:
        return self.value

    def setValue(self, value: ValueSpecification):
        if value is not None:
            self.value = value
        return self
from abc import ABC
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class Traceable(Identifiable, ABC):
    """
    Abstract base class for traceable identifiable elements.
    """
    # Traceable method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent, short_name: str):
        if type(self) is Traceable:
            raise TypeError("Traceable is an abstract class.")
        super().__init__(parent, short_name)

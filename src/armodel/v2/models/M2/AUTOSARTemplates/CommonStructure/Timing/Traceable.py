from abc import ABC

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class Traceable(Identifiable, ABC):
    def __init__(self, parent, short_name: str):
        if type(self) is Traceable:
            raise TypeError("Traceable is an abstract class.")
        super().__init__(parent, short_name)

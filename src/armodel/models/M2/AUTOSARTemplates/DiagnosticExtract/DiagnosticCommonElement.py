from abc import ABC
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    ARElement,
)


class DiagnosticCommonElement(ARElement, ABC):
    """
    Abstract base class for common diagnostic elements in the diagnostic
    extract template.
    """
    # DiagnosticCommonElement method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test

    def __init__(self, parent, short_name: str):
        if type(self) is DiagnosticCommonElement:
            raise TypeError("DiagnosticCommonElement is an abstract class.")
        super().__init__(parent, short_name)

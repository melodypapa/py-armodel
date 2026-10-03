from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR


class AbstractTransformer:
    """
    Abstract base class for data transformers with lifecycle methods.
    """

    def __init__(self):
        pass

    def remove(self, root: "AUTOSAR") -> None:
        pass

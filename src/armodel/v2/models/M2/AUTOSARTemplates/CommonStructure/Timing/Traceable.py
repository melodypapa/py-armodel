from abc import ABC


def _get_identifiable_base():
    """Lazy import of Identifiable to avoid circular import."""
    from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
        Identifiable,
    )
    return Identifiable


class Traceable(ABC):
    def __init__(self, parent, short_name: str) -> None:
        if type(self) is Traceable:
            raise TypeError("Traceable is an abstract class.")
        # Lazy import to avoid circular import
        Identifiable = _get_identifiable_base()
        Identifiable.__init__(self, parent, short_name)

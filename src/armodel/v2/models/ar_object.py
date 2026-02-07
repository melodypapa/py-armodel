"""
Base ARObject class for V2 demo models.
"""
from abc import ABC, abstractmethod
from typing import Optional


class ARObject(ABC):
    """
    Abstract base class for all AUTOSAR objects.
    Pure data model - NO serialization methods.
    """

    @abstractmethod
    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass

    def __init__(self) -> None:
        if type(self) is ARObject:
            raise TypeError("ARObject is an abstract class.")
        self._validate_abstract()

        self.parent: Optional['ARObject'] = None
        self.uuid: Optional[str] = None

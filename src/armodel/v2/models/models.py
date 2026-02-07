"""
Demo model classes for V2 ARXML reader/writer.
"""
from typing import List, Optional
from .ar_object import ARObject


class AUTOSAR(ARObject):
    """
    AUTOSAR root element.
    """

    def _validate_abstract(self) -> None:
        pass

    def __init__(self) -> None:
        super().__init__()
        self.ar_packages: List[ARPackage] = []


class ARPackage(ARObject):
    """
    AUTOSAR AR Package.
    """

    def _validate_abstract(self) -> None:
        pass

    def __init__(self) -> None:
        super().__init__()
        self.short_name: Optional[str] = None
        self.ar_packages: List[ARPackage] = []
        self.elements: List[ARObject] = []


class SwComponentType(ARObject):
    """
    Software Component Type (simplified for demo).
    """

    def _validate_abstract(self) -> None:
        pass

    def __init__(self) -> None:
        super().__init__()
        self.short_name: Optional[str] = None
        self.category: Optional[str] = None

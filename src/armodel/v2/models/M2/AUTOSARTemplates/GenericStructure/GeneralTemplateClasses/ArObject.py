'''V2 base classes copied from ArObject.py'''

from abc import ABC
from typing import Optional, Dict


class ARObject(ABC):
    """
    Abstract base class for all AUTOSAR objects.
    This class provides the basic structure and functionality for all AUTOSAR objects.
    """

    def __init__(self):
        if type(self) is ARObject:
            raise TypeError("ARObject is an abstract class.")

        self.parent: Optional['ARObject'] = None
        self.checksum: Optional[str] = None

        self.timestamp: Optional[str] = None
        self.uuid: Optional[str] = None

    def getTagName(self, tag: str, nsmap: Dict) -> str:
        """
        Gets the tag name without namespace prefix.

        Args:
            tag: The full tag name with namespace prefix
            nsmap: The namespace map dictionary

        Returns:
            The tag name without namespace prefix
        """
        return tag.replace("{%s}" % nsmap["xmlns"], "")


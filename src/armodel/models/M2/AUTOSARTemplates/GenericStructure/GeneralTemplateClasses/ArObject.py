from abc import ABCMeta
from typing import Dict


class ARObject(metaclass=ABCMeta):
    def __init__(self):
        if type(self) is ARObject:
            raise TypeError("ARObject is an abstract class.")

        self.parent = None              # type: ARObject
        self.checksum = None            # type: str

        self.timestamp = None           # type: str
        self.uuid = None                # type: str

    def getTagName(self, tag: str, nsmap: Dict) -> str:
        return tag.replace("{%s}" % nsmap["xmlns"], "")

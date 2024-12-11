from .....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from .....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from .....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral, RefType
import re
from typing import List

class MemorySection(Identifiable):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self._alignment = None              # type: ARLiteral
        self.memClassSymbol = None          # type: ARLiteral
        self.size = None
        self.options = []                   # type: List[ARLiteral]
        self.swAddrMethodRef = None         # type: RefType
        self.symbol = None                  # type: ARLiteral

    def getAlignment(self):
        return self.alignment

    def setAlignment(self, value):
        self.alignment = value
        return self
    
    def getMemClassSymbol(self):
        return self.memClassSymbol

    def setMemClassSymbol(self, value):
        self.memClassSymbol = value
        return self

    def getSize(self):
        return self.size

    def setSize(self, value):
        self.size = value
        return self

    def getSwAddrMethodRef(self):
        return self.swAddrMethodRef

    def setSwAddrMethodRef(self, value):
        self.swAddrMethodRef = value
        return self

    def getSymbol(self):
        return self.symbol

    def setSymbol(self, value):
        self.symbol = value
        return self

    @property
    def alignment(self) -> ARLiteral:
        return self._alignment

    @alignment.setter
    def alignment(self, value: ARLiteral):
        if value is not None and value.getValue() != "":
            match = False
            if value.getValue() in ("UNKNOWN", "UNSPECIFIED", "BOOLEAN", "PTR"):
                self._alignment = value
                match = True
            else:
                m = re.match(r'^\d+', value.value)
                if m:
                    self._alignment = value
                    match = True

            if not match:
                raise ValueError("Invalid alignment <%s> of memory section <%s>" % (value, self.getShortName()))

    def addOption(self, option: ARLiteral):
        self.options.append(option)

    def getOptions(self) -> List[ARLiteral]:
        return self.options
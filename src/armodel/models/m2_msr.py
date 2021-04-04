from .general_structure import ARObject, ARElement, Limit
from abc import ABCMeta
from typing import List

class CompuContent(ARObject, metaclass=ABCMeta):
    def __init__(self):
        if type(self) == CompuContent:
            raise NotImplementedError("CompuContent is an abstract class.")
        super().__init__()

class Compu(ARObject):
    def __init__(self):
        super().__init__()

        '''required'''
        self.compu_content = None           # type: CompuContent

        '''optional'''
        self.compu_default_value = None     # type: CompuConst

class CompuConstContent(ARObject):
    def __init__(self):
        super().__init__()

class CompuConstTextContent(CompuConstContent):
    def __init__(self):
        super().__init__()

        self.vt = None

class CompuConstNumericContent(CompuConstContent):
    def __init__(self):
        super().__init__()

        self.v = None

class CompuConst(ARObject):
    def __init__(self):
        super().__init__()

        self.compu_const_content_type = None    # type: CompuConstContent

class CompuScale(Compu):
    def __init__(self):
        super().__init__()

        self.lower_limit = None             # type: Limit
        self.upper_limit = None             # type: Limit
        self.compu_inverse_value = None     # type: CompuConst
        self.compu_scale_contents = None    # type: CompuScaleContents

class CompuScales(CompuContent):
    def __init__(self):
        super().__init__()

        self.compu_scales = []              # type: List[CompuScale]

    def addCompuScale(self, compu_scale: CompuScale):
        self.compu_scales.append(compu_scale)

    def getCompuScales(self) -> List[CompuScale]:
        return self.compu_scales

class CompuMethod(ARElement):
    CATEGORY_TEXTTABLE = "TEXTTABLE"

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        self.compu_internal_to_phys = None  # type: Compu
        self.compu_phys_to_internal = None  # type: Compu
        self.display_format = None          # type: DisplayFormatString
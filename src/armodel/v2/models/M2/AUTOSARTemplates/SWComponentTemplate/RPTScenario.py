"""
This module contains classes for representing AUTOSAR Run-Time Protection (RPT) scenarios
and access point identification elements in software component templates.
"""

from abc import ABC

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import (
    AtpStructureElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class IdentCaption(AtpStructureElement, ABC):

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is IdentCaption:
            raise TypeError("IdentCaption is an abstract class.")

        super().__init__(parent, short_name)


class ModeAccessPointIdent(IdentCaption):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class ExternalTriggeringPointIdent(IdentCaption):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

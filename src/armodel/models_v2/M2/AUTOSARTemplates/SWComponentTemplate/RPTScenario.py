"""
This module contains classes for representing AUTOSAR Run-Time Protection (RPT) scenarios
and access point identification elements in software component templates.
"""

from armodel.models_v2.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpStructureElement
from armodel.models_v2.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models_v2.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from abc import ABC

class IdentCaption(AtpStructureElement, ABC):

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) == IdentCaption:
            raise TypeError("IdentCaption is an abstract class.")

        super().__init__(parent, short_name)


class ModeAccessPointIdent(IdentCaption):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class ExternalTriggeringPointIdent(IdentCaption):
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)
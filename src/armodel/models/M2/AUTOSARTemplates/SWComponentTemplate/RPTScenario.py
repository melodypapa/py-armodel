"""
This module contains classes for representing AUTOSAR Run-Time Protection (RPT) scenarios
and access point identification elements in software component templates.
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpStructureElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from abc import ABC


class IdentCaption(AtpStructureElement, ABC):
    """
    Abstract base class for identification captions used in access points.
    """

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is IdentCaption:
            raise TypeError("IdentCaption is an abstract class.")

        super().__init__(parent, short_name)


class ModeAccessPointIdent(IdentCaption):
    """
    Identification of a mode access point used to reference a specific
    access point within a runnable entity.
    """

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)
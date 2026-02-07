"""
This module contains classes for representing AUTOSAR per-instance memory elements
in software component internal behavior templates.
"""

from typing import Union

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import (
    AtpStructureElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARLiteral,
)
from armodel.v2.models.M2.MSR.DataDictionary.DataDefProperties import (
    SwDataDefProps,
)


class PerInstanceMemory(AtpStructureElement):

    def _validate_abstract(self) -> None:
        """Validate this is a concrete class."""
        pass    def __init__(self, parent: ARObject, short_name: str) -> None:
        super().__init__(parent, short_name)

        self.initValue: Union[Union[ARLiteral, None] , None] = None
        self.swDataDefProps: 'SwDataDefProps' = None
        self.type: Union[Union[ARLiteral, None] , None] = None
        self.typeDefinition: Union[Union[ARLiteral, None] , None] = None

    def getInitValue(self):
        return self.initValue

    def setInitValue(self, value):
        self.initValue = value
        return self

    def getSwDataDefProps(self):
        return self.swDataDefProps

    def setSwDataDefProps(self, value):
        self.swDataDefProps = value
        return self

    def getType(self):
        return self.type

    def setType(self, value):
        self.type = value
        return self

    def getTypeDefinition(self):
        return self.typeDefinition

    def setTypeDefinition(self, value):
        self.typeDefinition = value
        return self

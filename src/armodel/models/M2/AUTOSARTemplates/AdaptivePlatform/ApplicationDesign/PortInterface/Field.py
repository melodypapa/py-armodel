from typing import Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import (
    AutosarDataPrototype,
)


class Field(AutosarDataPrototype):
    """
    This meta-class represents the ability to define a piece of data that can be
    accessed with read and/or write semantics. It is also possible to generate a
    notification if the value of the data changes.

    Sources:
      - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (Page 45, Foundation
      R23-11)
    """
    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This attribute controls whether read access is foreseen to.
        self.hasGetter: Optional[Boolean] = None
        # This attribute controls whether a notification semantics is this field.
        self.hasNotifier: Optional[Boolean] = None
        # This attribute controls whether write access is foreseen to.
        self.hasSetter: Optional[Boolean] = None

    def getHasGetter(self) -> Boolean:
        return self.hasGetter


    def setHasGetter(self, value: Boolean) -> "Field":
        self.hasGetter = value
        return self


    def getHasNotifier(self) -> Boolean:
        return self.hasNotifier


    def setHasNotifier(self, value: Boolean) -> "Field":
        self.hasNotifier = value
        return self


    def getHasSetter(self) -> Boolean:
        return self.hasSetter


    def setHasSetter(self, value: Boolean) -> "Field":
        self.hasSetter = value
        return self



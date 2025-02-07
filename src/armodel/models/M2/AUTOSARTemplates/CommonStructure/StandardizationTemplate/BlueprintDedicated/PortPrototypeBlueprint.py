from typing import List

from ......M2.AUTOSARTemplates.CommonStructure import ValueSpecification
from ......M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from ......M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from ......M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import ARElement
from ......M2.AUTOSARTemplates.SWComponentTemplate.Communication import PPortComSpec


class PortPrototypeBlueprintInitValue(ARObject):
    def __init__(self):
        super().__init__()

        self.dataPrototypeRef = None                            # type: RefType
        self.value = None                                       # type: ValueSpecification

    def getDataPrototypeRef(self):
        return self.dataPrototypeRef

    def setDataPrototypeRef(self, value):
        if value is not None:
            self.dataPrototypeRef = value
        return self

    def getValue(self):
        return self.value

    def setValue(self, value):
        if value is not None:
            self.value = value
        return self


class PortPrototypeBlueprint(ARElement):
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.initValues = []                                    # type: List[PortPrototypeBlueprintInitValue]
        self.interfaceRef = None                                # type: RefType
        self.providedComSpecs = []                              # type: List[PPortComSpec]
        self.requiredComSpecs = []                              # type: List[RPortComSpec]

    def getInitValues(self):
        return self.initValues

    def setInitValues(self, value):
        if value is not None:
            self.initValues = value
        return self

    def getInterfaceRef(self):
        return self.interfaceRef

    def setInterfaceRef(self, value):
        if value is not None:
            self.interfaceRef = value
        return self

    def getProvidedComSpecs(self):
        return self.providedComSpecs

    def setProvidedComSpecs(self, value):
        if value is not None:
            self.providedComSpecs = value
        return self

    def getRequiredComSpecs(self):
        return self.requiredComSpecs

    def setRequiredComSpecs(self, value):
        if value is not None:
            self.requiredComSpecs = value
        return self

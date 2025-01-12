from typing import List

from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Integer, RefType, String
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import ARElement


class HwDescriptionEntity(ARElement):
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)
        
        self.hwAttributeValues = []                                 # type: List[HwAttributeValue]
        self.hwCategoryRefs = []                                    # type: List[RefType]
        self.hwTypeRef = None                                       # type: RefType

    def getHwAttributeValues(self):
        return self.hwAttributeValues

    def setHwAttributeValues(self, value):
        if value is not None:
            self.hwAttributeValues = value
        return self

    def getHwCategoryRefs(self):
        return self.hwCategoryRefs

    def addHwCategoryRef(self, value):
        if value is not None:
            self.hwCategoryRefs.append(value)
        return self

    def getHwTypeRef(self):
        return self.hwTypeRef

    def setHwTypeRef(self, value):
        if value is not None:
            self.hwTypeRef = value
        return self
    

class HwPin(HwDescriptionEntity):
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.functionName = None                                    # type: String
        self.packagingPinName = None                                # type: String
        self.pinNumber = None                                       # type: Integer

    def getFunctionName(self):
        return self.functionName

    def setFunctionName(self, value):
        if value is not None:
            self.functionName = value
        return self

    def getPackagingPinName(self):
        return self.packagingPinName

    def setPackagingPinName(self, value):
        if value is not None:
            self.packagingPinName = value
        return self

    def getPinNumber(self):
        return self.pinNumber

    def setPinNumber(self, value):
        if value is not None:
            self.pinNumber = value
        return self


class HwPinGroupContent(ARObject):
    def __init__(self):
        super().__init__()

        self.hwPin = None                                           # type: HwPin
        self.hwPinGroup = None                                      # type: HwPinGroup

    def getHwPin(self):
        return self.hwPin

    def createHwPin(self, short_name: str) -> HwPin:
        pin = HwPin(self, short_name)
        self.hwPin = pin
        return pin

    def getHwPinGroup(self):
        return self.hwPinGroup

    def setHwPinGroup(self, value):
        if value is not None:
            self.hwPinGroup = value
        return self


class HwPinGroup(HwDescriptionEntity):
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.hwPinGroupContent = None                               # type: HwPinGroupContent

    def getHwPinGroupContent(self):
        return self.hwPinGroupContent

    def setHwPinGroupContent(self, value):
        if value is not None:
            self.hwPinGroupContent = value
        return self


class HwElement(HwDescriptionEntity):
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.hwElementConnections = []                              # type: List[HwElementConnector]
        self.hwPinGroups = []                                       # type: List[HwPinGroup]
        self.nestedElementRefs = []                                 # type: List[RefType]

    def getHwElementConnections(self):
        return self.hwElementConnections

    def setHwElementConnections(self, value):
        if value is not None:
            self.hwElementConnections = value
        return self

    def getHwPinGroups(self):
        return self.hwPinGroups

    def createHwPinGroup(self, short_name: str) -> HwPinGroup:
        if (not self.IsElementExists(short_name)):
            pin_group = HwPinGroup(self, short_name)
            self.addElement(pin_group)
            self.hwPinGroups.append(pin_group)
        return self.getElement(short_name)

    def getNestedElementRefs(self):
        return self.nestedElementRefs

    def setNestedElementRefs(self, value):
        if value is not None:
            self.nestedElementRefs = value
        return self

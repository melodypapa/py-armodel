from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum, PositiveInteger, UnlimitedInteger
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject


class DataFilterTypeEnum(AREnum):

    maskedNewDiffersMaskedOld = "maskedNewDiffersMaskedOld"
    maskedNewDiffersX = "maskedNewDiffersX"
    maskedNewEqualsX = "maskedNewEqualsX"
    never = "never"
    newIsOutside = "newIsOutside"
    newIsWithin = "newIsWithin"
    oneEveryN = "oneEveryN"

    def __init__(self):
        super().__init__((
            self.maskedNewDiffersMaskedOld,
            self.maskedNewDiffersX,
            self.maskedNewEqualsX, 
            self.never,
            self.newIsOutside,
            self.newIsWithin,
            self.oneEveryN
        ))


class DataFilter(ARObject):
    def __init__(self):
        super().__init__()

        self.dataFilterType = None                  # type: DataFilterTypeEnum
        self.mask = None                            # type: UnlimitedInteger
        self.max = None                             # type: UnlimitedInteger
        self.min = None                             # type: UnlimitedInteger
        self.offset = None                          # type: PositiveInteger
        self.period = None                          # type: PositiveInteger
        self.x = None                               # type: UnlimitedInteger

    def getDataFilterType(self):
        return self.dataFilterType

    def setDataFilterType(self, value):
        self.dataFilterType = value
        return self

    def getMask(self):
        return self.mask

    def setMask(self, value):
        self.mask = value
        return self

    def getMax(self):
        return self.max

    def setMax(self, value):
        self.max = value
        return self

    def getMin(self):
        return self.min

    def setMin(self, value):
        self.min = value
        return self

    def getOffset(self):
        return self.offset

    def setOffset(self, value):
        self.offset = value
        return self

    def getPeriod(self):
        return self.period

    def setPeriod(self, value):
        self.period = value
        return self

    def getX(self):
        return self.x

    def setX(self, value):
        self.x = value
        return self

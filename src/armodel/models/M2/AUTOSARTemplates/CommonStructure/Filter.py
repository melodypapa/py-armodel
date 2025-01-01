from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum, PositiveInteger, UnlimitedInteger
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject


class DataFilterTypeEnum(AREnum):

    MASKED_NEW_DIFFERS_MASKED_OLD = "maskedNewDiffersMaskedOld"
    MASKED_NEW_DIFFERS_X = "maskedNewDiffersX"
    MASKED_NEW_EQUALS_X = "maskedNewEqualsX"
    NEVER = "never"
    NEW_IS_OUTSIDE = "newIsOutside"
    NEW_IS_WITHIN = "newIsWithin"
    ONE_EVERY_N = "oneEveryN"

    def __init__(self):
        super().__init__((
            DataFilterTypeEnum.MASKED_NEW_DIFFERS_MASKED_OLD,
            DataFilterTypeEnum.MASKED_NEW_DIFFERS_X,
            DataFilterTypeEnum.MASKED_NEW_EQUALS_X, 
            DataFilterTypeEnum.NEVER,
            DataFilterTypeEnum.NEW_IS_OUTSIDE,
            DataFilterTypeEnum.NEW_IS_WITHIN,
            DataFilterTypeEnum.ONE_EVERY_N
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
        if value is not None:
            self.dataFilterType = value
        return self

    def getMask(self):
        return self.mask

    def setMask(self, value):
        if value is not None:
            self.mask = value
        return self

    def getMax(self):
        return self.max

    def setMax(self, value):
        if value is not None:
            self.max = value
        return self

    def getMin(self):
        return self.min

    def setMin(self, value):
        if value is not None:
            self.min = value
        return self

    def getOffset(self):
        return self.offset

    def setOffset(self, value):
        if value is not None:
            self.offset = value
        return self

    def getPeriod(self):
        return self.period

    def setPeriod(self, value):
        if value is not None:
            self.period = value
        return self

    def getX(self):
        return self.x

    def setX(self, value):
        if value is not None:
            self.x = value
        return self


    

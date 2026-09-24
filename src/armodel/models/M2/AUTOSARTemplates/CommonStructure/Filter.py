"""
This module contains classes for representing AUTOSAR data filter configurations
in the CommonStructure module. Data filters are used to define conditions for
data processing, such as when to update values based on filters or limits.
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum, PositiveInteger, UnlimitedInteger
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject


class DataFilterTypeEnum(AREnum):
    """
    This enum specifies the supported DataFilterTypes.
    """

    # DataFilterTypeEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.76, p.183
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods) — enum value form serialized on DataFilter.dataFilterType (DATA-FILTER-TYPE child element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # No filtering is performed so that the message always passes. Tags: atp.EnumerationLiteralIndex=0
    ALWAYS = "ALWAYS"

    # Pass messages where the masked value has changed. (new_value&mask) !=(old_value&mask) new_value: current value of the message old_value: last value of the message (initialized with the initial value of the message, updated with new_value if the new message value is not filtered out) Tags: atp.EnumerationLiteralIndex=1
    MASKED_NEW_DIFFERS_MASKED_OLD = "MASKED-NEW-DIFFERS-MASKED-OLD"

    # Pass messages whose masked value is not equal to a specific value x (new_value&mask) != x new_value: current value of the message Tags: atp.EnumerationLiteralIndex=2
    MASKED_NEW_DIFFERS_X = "MASKED-NEW-DIFFERS-X"

    # Pass messages whose masked value is equal to a specific value x (new_value&mask) == x new_value: current value of the message Tags: atp.EnumerationLiteralIndex=3
    MASKED_NEW_EQUALS_X = "MASKED-NEW-EQUALS-X"

    # The filter removes all messages. Tags: atp.EnumerationLiteralIndex=4
    NEVER = "NEVER"

    # Pass a message if its value is outside a predefined boundary. (min > new_value) OR (new_value > max) Tags: atp.EnumerationLiteralIndex=5
    NEW_IS_OUTSIDE = "NEW-IS-OUTSIDE"

    # Pass a message if its value is within a predefined boundary. min <= new_value <= max Tags: atp.EnumerationLiteralIndex=6
    NEW_IS_WITHIN = "NEW-IS-WITHIN"

    # Pass a message once every N message occurrences. Algorithm: occurrence %period == offset Start: occurrence = 0. Each time the message is received or transmitted, occurrence is incremented by 1 after filtering. Length of occurrence is 8 bit (minimum). Tags: atp.EnumerationLiteralIndex=7
    ONE_EVERY_N = "ONE-EVERY-N"

    def __init__(self):
        super().__init__(
            (
                DataFilterTypeEnum.ALWAYS,
                DataFilterTypeEnum.MASKED_NEW_DIFFERS_MASKED_OLD,
                DataFilterTypeEnum.MASKED_NEW_DIFFERS_X,
                DataFilterTypeEnum.MASKED_NEW_EQUALS_X,
                DataFilterTypeEnum.NEVER,
                DataFilterTypeEnum.NEW_IS_OUTSIDE,
                DataFilterTypeEnum.NEW_IS_WITHIN,
                DataFilterTypeEnum.ONE_EVERY_N,
            )
        )


class DataFilter(ARObject):
    """
    Base class for data filters. The type of the filter is specified in attribute dataFilterType. Some of the filter types require additional arguments which are specified as attributes of this class.
    """

    # DataFilter method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 4.75, p.182
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getDataFilterType            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setDataFilterType            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMask                      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMask                      [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMax                       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMax                       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMin                       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMin                       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getOffset                    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setOffset                    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getPeriod                    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setPeriod                    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getX                         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setX                         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # This attribute specifies the type of the filter.
        self.dataFilterType: DataFilterTypeEnum = None

        # Mask for old and new value.
        self.mask: UnlimitedInteger = None

        # Value to specify the upper boundary
        self.max: UnlimitedInteger = None

        # Value to specify the lower boundary
        self.min: UnlimitedInteger = None

        # Specifies the initial number of messages to occur before the first message is passed
        self.offset: PositiveInteger = None

        # Specifies number of messages to occur before the message is passed again
        self.period: PositiveInteger = None

        # Value to compare with
        self.x: UnlimitedInteger = None

    def getDataFilterType(self):
        """
        This attribute specifies the type of the filter.
        """
        return self.dataFilterType

    def setDataFilterType(self, value):
        """
        This attribute specifies the type of the filter.
        A None value is a no-op and does not overwrite an existing dataFilterType.
        """
        if value is not None:
            self.dataFilterType = value
        return self

    def getMask(self):
        """
        Mask for old and new value.
        """
        return self.mask

    def setMask(self, value):
        """
        Mask for old and new value.
        A None value is a no-op and does not overwrite an existing mask.
        """
        if value is not None:
            self.mask = value
        return self

    def getMax(self):
        """
        Value to specify the upper boundary
        """
        return self.max

    def setMax(self, value):
        """
        Value to specify the upper boundary
        A None value is a no-op and does not overwrite an existing max.
        """
        if value is not None:
            self.max = value
        return self

    def getMin(self):
        """
        Value to specify the lower boundary
        """
        return self.min

    def setMin(self, value):
        """
        Value to specify the lower boundary
        A None value is a no-op and does not overwrite an existing min.
        """
        if value is not None:
            self.min = value
        return self

    def getOffset(self):
        """
        Specifies the initial number of messages to occur before the first message is passed
        """
        return self.offset

    def setOffset(self, value):
        """
        Specifies the initial number of messages to occur before the first message is passed
        A None value is a no-op and does not overwrite an existing offset.
        """
        if value is not None:
            self.offset = value
        return self

    def getPeriod(self):
        """
        Specifies number of messages to occur before the message is passed again
        """
        return self.period

    def setPeriod(self, value):
        """
        Specifies number of messages to occur before the message is passed again
        A None value is a no-op and does not overwrite an existing period.
        """
        if value is not None:
            self.period = value
        return self

    def getX(self):
        """
        Value to compare with
        """
        return self.x

    def setX(self, value):
        """
        Value to compare with
        A None value is a no-op and does not overwrite an existing x.
        """
        if value is not None:
            self.x = value
        return self

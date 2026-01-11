"""
This module contains classes for representing AUTOSAR data filter configurations
in the CommonStructure module. Data filters are used to define conditions for
data processing, such as when to update values based on filters or limits.
"""

from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum, PositiveInteger, UnlimitedInteger
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject


class DataFilterTypeEnum(AREnum):
    """
    Enumeration for data filter types in AUTOSAR models.
    Defines various filtering strategies for data processing in AUTOSAR systems.
    """

    # Filter condition: new value with mask differs from old value with mask
    MASKED_NEW_DIFFERS_MASKED_OLD = "maskedNewDiffersMaskedOld"
    # Filter condition: new value with mask differs from reference value X
    MASKED_NEW_DIFFERS_X = "maskedNewDiffersX"
    # Filter condition: new value with mask equals reference value X
    MASKED_NEW_EQUALS_X = "maskedNewEqualsX"
    # Filter condition: never update (no filtering)
    NEVER = "never"
    # Filter condition: new value is outside specified range
    NEW_IS_OUTSIDE = "newIsOutside"
    # Filter condition: new value is within specified range
    NEW_IS_WITHIN = "newIsWithin"
    # Filter condition: update every N occurrences
    ONE_EVERY_N = "oneEveryN"

    def __init__(self):
        """
        Initializes the DataFilterTypeEnum with all possible values.
        """
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
    """
    Represents a data filter configuration in AUTOSAR models.
    This class defines conditions and parameters for filtering data updates in AUTOSAR systems.
    """
    
    def __init__(self):
        """
        Initializes the DataFilter with default values.
        """
        super().__init__()

        # Type of data filtering to apply
        self.dataFilterType: DataFilterTypeEnum = None                  
        # Bit mask for masked filtering operations
        self.mask: UnlimitedInteger = None                            
        # Maximum threshold value for range-based filtering
        self.max: UnlimitedInteger = None                             
        # Minimum threshold value for range-based filtering
        self.min: UnlimitedInteger = None                             
        # Offset value for filtering calculations
        self.offset: PositiveInteger = None                          
        # Period for periodic filtering operations (e.g., oneEveryN)
        self.period: PositiveInteger = None                          
        # Reference value X used in comparison-based filtering
        self.x: UnlimitedInteger = None                               

    def getDataFilterType(self):
        """
        Gets the type of data filtering to apply.
        
        Returns:
            DataFilterTypeEnum: The data filter type
        """
        return self.dataFilterType

    def setDataFilterType(self, value):
        """
        Sets the type of data filtering to apply.
        Only sets the value if it is not None.
        
        Args:
            value: The data filter type to set
            
        Returns:
            self for method chaining
        """
        if value is not None:
            self.dataFilterType = value
        return self

    def getMask(self):
        """
        Gets the bit mask for masked filtering operations.
        
        Returns:
            UnlimitedInteger: The bit mask
        """
        return self.mask

    def setMask(self, value):
        """
        Sets the bit mask for masked filtering operations.
        Only sets the value if it is not None.
        
        Args:
            value: The bit mask to set
            
        Returns:
            self for method chaining
        """
        if value is not None:
            self.mask = value
        return self

    def getMax(self):
        """
        Gets the maximum threshold value for range-based filtering.
        
        Returns:
            UnlimitedInteger: The maximum threshold
        """
        return self.max

    def setMax(self, value):
        """
        Sets the maximum threshold value for range-based filtering.
        Only sets the value if it is not None.
        
        Args:
            value: The maximum threshold to set
            
        Returns:
            self for method chaining
        """
        if value is not None:
            self.max = value
        return self

    def getMin(self):
        """
        Gets the minimum threshold value for range-based filtering.
        
        Returns:
            UnlimitedInteger: The minimum threshold
        """
        return self.min

    def setMin(self, value):
        """
        Sets the minimum threshold value for range-based filtering.
        Only sets the value if it is not None.
        
        Args:
            value: The minimum threshold to set
            
        Returns:
            self for method chaining
        """
        if value is not None:
            self.min = value
        return self

    def getOffset(self):
        """
        Gets the offset value for filtering calculations.
        
        Returns:
            PositiveInteger: The offset value
        """
        return self.offset

    def setOffset(self, value):
        """
        Sets the offset value for filtering calculations.
        Only sets the value if it is not None.
        
        Args:
            value: The offset value to set
            
        Returns:
            self for method chaining
        """
        if value is not None:
            self.offset = value
        return self

    def getPeriod(self):
        """
        Gets the period for periodic filtering operations (e.g., oneEveryN).
        
        Returns:
            PositiveInteger: The period value
        """
        return self.period

    def setPeriod(self, value):
        """
        Sets the period for periodic filtering operations (e.g., oneEveryN).
        Only sets the value if it is not None.
        
        Args:
            value: The period value to set
            
        Returns:
            self for method chaining
        """
        if value is not None:
            self.period = value
        return self

    def getX(self):
        """
        Gets the reference value X used in comparison-based filtering.
        
        Returns:
            UnlimitedInteger: The reference value X
        """
        return self.x

    def setX(self, value):
        """
        Sets the reference value X used in comparison-based filtering.
        Only sets the value if it is not None.
        
        Args:
            value: The reference value X to set
            
        Returns:
            self for method chaining
        """
        if value is not None:
            self.x = value
        return self


    

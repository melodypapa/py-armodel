import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Filter import DataFilter, DataFilterTypeEnum
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import UnlimitedInteger, PositiveInteger


class TestDataFilterTypeEnum:
    def test_initialization(self):
        """Test DataFilterTypeEnum initialization"""
        enum_obj = DataFilterTypeEnum()
        assert enum_obj is not None

    def test_enum_values(self):
        """Test all enum values are properly defined"""
        assert DataFilterTypeEnum.MASKED_NEW_DIFFERS_MASKED_OLD == "maskedNewDiffersMaskedOld"
        assert DataFilterTypeEnum.MASKED_NEW_DIFFERS_X == "maskedNewDiffersX"
        assert DataFilterTypeEnum.MASKED_NEW_EQUALS_X == "maskedNewEqualsX"
        assert DataFilterTypeEnum.NEVER == "never"
        assert DataFilterTypeEnum.NEW_IS_OUTSIDE == "newIsOutside"
        assert DataFilterTypeEnum.NEW_IS_WITHIN == "newIsWithin"
        assert DataFilterTypeEnum.ONE_EVERY_N == "oneEveryN"

    def test_enum_values_list(self):
        """Test that all enum values are in the list"""
        enum_obj = DataFilterTypeEnum()
        values = enum_obj.getEnumValues()
        expected_values = [
            "maskedNewDiffersMaskedOld",
            "maskedNewDiffersX",
            "maskedNewEqualsX",
            "never",
            "newIsOutside",
            "newIsWithin",
            "oneEveryN"
        ]
        assert set(values) == set(expected_values)


class TestDataFilter:
    def test_initialization(self):
        """Test DataFilter initialization"""
        data_filter = DataFilter()
        assert data_filter is not None
        assert data_filter.dataFilterType is None
        assert data_filter.mask is None
        assert data_filter.max is None
        assert data_filter.min is None
        assert data_filter.offset is None
        assert data_filter.period is None
        assert data_filter.x is None

    def test_get_data_filter_type(self):
        """Test getDataFilterType method"""
        data_filter = DataFilter()
        assert data_filter.getDataFilterType() is None

    def test_set_data_filter_type(self):
        """Test setDataFilterType method"""
        data_filter = DataFilter()
        test_value = DataFilterTypeEnum()
        result = data_filter.setDataFilterType(test_value)
        assert result is data_filter  # Method chaining
        assert data_filter.getDataFilterType() == test_value

    def test_set_data_filter_type_none(self):
        """Test setDataFilterType with None value"""
        data_filter = DataFilter()
        result = data_filter.setDataFilterType(None)
        assert result is data_filter  # Method chaining
        assert data_filter.getDataFilterType() is None

    def test_get_mask(self):
        """Test getMask method"""
        data_filter = DataFilter()
        assert data_filter.getMask() is None

    def test_set_mask(self):
        """Test setMask method"""
        data_filter = DataFilter()
        test_value = UnlimitedInteger().setValue(8)
        result = data_filter.setMask(test_value)
        assert result is data_filter  # Method chaining
        assert data_filter.getMask() == test_value

    def test_set_mask_none(self):
        """Test setMask with None value"""
        data_filter = DataFilter()
        result = data_filter.setMask(None)
        assert result is data_filter  # Method chaining
        assert data_filter.getMask() is None

    def test_get_max(self):
        """Test getMax method"""
        data_filter = DataFilter()
        assert data_filter.getMax() is None

    def test_set_max(self):
        """Test setMax method"""
        data_filter = DataFilter()
        test_value = UnlimitedInteger().setValue(100)
        result = data_filter.setMax(test_value)
        assert result is data_filter  # Method chaining
        assert data_filter.getMax() == test_value

    def test_set_max_none(self):
        """Test setMax with None value"""
        data_filter = DataFilter()
        result = data_filter.setMax(None)
        assert result is data_filter  # Method chaining
        assert data_filter.getMax() is None

    def test_get_min(self):
        """Test getMin method"""
        data_filter = DataFilter()
        assert data_filter.getMin() is None

    def test_set_min(self):
        """Test setMin method"""
        data_filter = DataFilter()
        test_value = UnlimitedInteger().setValue(10)
        result = data_filter.setMin(test_value)
        assert result is data_filter  # Method chaining
        assert data_filter.getMin() == test_value

    def test_set_min_none(self):
        """Test setMin with None value"""
        data_filter = DataFilter()
        result = data_filter.setMin(None)
        assert result is data_filter  # Method chaining
        assert data_filter.getMin() is None

    def test_get_offset(self):
        """Test getOffset method"""
        data_filter = DataFilter()
        assert data_filter.getOffset() is None

    def test_set_offset(self):
        """Test setOffset method"""
        data_filter = DataFilter()
        test_value = PositiveInteger().setValue(5)
        result = data_filter.setOffset(test_value)
        assert result is data_filter  # Method chaining
        assert data_filter.getOffset() == test_value

    def test_set_offset_none(self):
        """Test setOffset with None value"""
        data_filter = DataFilter()
        result = data_filter.setOffset(None)
        assert result is data_filter  # Method chaining
        assert data_filter.getOffset() is None

    def test_get_period(self):
        """Test getPeriod method"""
        data_filter = DataFilter()
        assert data_filter.getPeriod() is None

    def test_set_period(self):
        """Test setPeriod method"""
        data_filter = DataFilter()
        test_value = PositiveInteger().setValue(10)
        result = data_filter.setPeriod(test_value)
        assert result is data_filter  # Method chaining
        assert data_filter.getPeriod() == test_value

    def test_set_period_none(self):
        """Test setPeriod with None value"""
        data_filter = DataFilter()
        result = data_filter.setPeriod(None)
        assert result is data_filter  # Method chaining
        assert data_filter.getPeriod() is None

    def test_get_x(self):
        """Test getX method"""
        data_filter = DataFilter()
        assert data_filter.getX() is None

    def test_set_x(self):
        """Test setX method"""
        data_filter = DataFilter()
        test_value = UnlimitedInteger().setValue(42)
        result = data_filter.setX(test_value)
        assert result is data_filter  # Method chaining
        assert data_filter.getX() == test_value

    def test_set_x_none(self):
        """Test setX with None value"""
        data_filter = DataFilter()
        result = data_filter.setX(None)
        assert result is data_filter  # Method chaining
        assert data_filter.getX() is None

    def test_all_properties(self):
        """Test setting all properties"""
        data_filter = DataFilter()
        
        # Create test values
        filter_type = DataFilterTypeEnum()
        mask = UnlimitedInteger().setValue(16)
        max_val = UnlimitedInteger().setValue(1000)
        min_val = UnlimitedInteger().setValue(0)
        offset = PositiveInteger().setValue(3)
        period = PositiveInteger().setValue(5)
        x_val = UnlimitedInteger().setValue(99)
        
        # Set all properties
        data_filter.setDataFilterType(filter_type)
        data_filter.setMask(mask)
        data_filter.setMax(max_val)
        data_filter.setMin(min_val)
        data_filter.setOffset(offset)
        data_filter.setPeriod(period)
        data_filter.setX(x_val)
        
        # Verify all properties
        assert data_filter.getDataFilterType() == filter_type
        assert data_filter.getMask() == mask
        assert data_filter.getMax() == max_val
        assert data_filter.getMin() == min_val
        assert data_filter.getOffset() == offset
        assert data_filter.getPeriod() == period
        assert data_filter.getX() == x_val
"""
This module contains tests for the ListElements module in MSR.Documentation.TextModel.BlockElements.
"""
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements.ListElements import *


class TestListEnum:
    """Test class for ListEnum class."""

    def test_list_enum_initialization(self):
        """Test that a ListEnum object can be initialized with expected values."""
        list_enum = ListEnum()
        # Check that enum has expected values
        assert hasattr(ListEnum, 'NUMBER')
        assert hasattr(ListEnum, 'UNNUMBER')
        assert ListEnum.NUMBER == 'number'
        assert ListEnum.UNNUMBER == 'unnumber'


class TestItem:
    """Test class for Item class."""

    def test_item_initialization(self):
        """Test that an Item object can be initialized with default values."""
        item = Item()
        assert item.itemContents is None

    def test_item_contents_methods(self):
        """Test the itemContents getter and setter."""
        item = Item()
        contents = "Test contents"

        result = item.setItemContents(contents)
        assert item.getItemContents() == contents
        assert result == item


class TestARList:
    """Test class for ARList class."""

    def test_ar_list_initialization(self):
        """Test that an ARList object can be initialized with default values."""
        ar_list = ARList()
        assert ar_list.items == []
        assert ar_list.type is None

    def test_ar_list_items_methods(self):
        """Test adding items to the list."""
        ar_list = ARList()
        item = Item()

        result = ar_list.addItem(item)
        items = ar_list.getItems()
        assert item in items
        assert result == ar_list

    def test_ar_list_type_methods(self):
        """Test the type getter and setter."""
        ar_list = ARList()
        list_type = ListEnum()

        result = ar_list.setType(list_type)
        assert ar_list.getType() == list_type
        assert result == ar_list

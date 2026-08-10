"""
This module contains tests for the ListElements module in MSR.Documentation.TextModel.BlockElements.
"""

from armodel.models.M2.MSR.Documentation.TextModel.BlockElements.ListElements import (
    ARList,
    DefItem,
    DefList,
    IndentSample,
    Item,
    ItemLabelPosEnum,
    LabeledItem,
    LabeledList,
    ListEnum,
)
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultiLanguageOverviewParagraph


class TestListEnum:
    """Test class for ListEnum class."""

    def test_list_enum_initialization(self):
        """Test that a ListEnum object can be initialized with expected values."""
        ListEnum()
        # Check that enum has expected values
        assert hasattr(ListEnum, "NUMBER")
        assert hasattr(ListEnum, "UNNUMBER")
        assert ListEnum.NUMBER == "number"
        assert ListEnum.UNNUMBER == "unnumber"


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


class TestItemLabelPosEnum:
    """Test class for ItemLabelPosEnum class."""

    def test_item_label_pos_enum_members(self):
        """Test that ItemLabelPosEnum has the expected members."""
        assert ItemLabelPosEnum.NEWLINE == "newline"
        assert ItemLabelPosEnum.NO_NEWLINE == "noNewline"

    def test_item_label_pos_enum_initialization(self):
        """Test that an ItemLabelPosEnum object can be initialized."""
        item_label_pos_enum = ItemLabelPosEnum()
        assert item_label_pos_enum.validateEnumValue("newline")
        assert not item_label_pos_enum.validateEnumValue("unknown")


class TestIndentSample:
    """Test class for IndentSample class."""

    def test_indent_sample_initialization(self):
        """Test that an IndentSample object can be initialized with default values."""
        indent_sample = IndentSample()
        assert indent_sample.itemLabelPos is None
        assert indent_sample.l2s == []

    def test_indent_sample_item_label_pos_methods(self):
        """Test the itemLabelPos getter and setter."""
        indent_sample = IndentSample()
        pos = ItemLabelPosEnum()

        result = indent_sample.setItemLabelPos(pos)
        assert indent_sample.getItemLabelPos() == pos
        assert result == indent_sample

        indent_sample.setItemLabelPos(None)
        assert indent_sample.getItemLabelPos() == pos

    def test_indent_sample_l2s_methods(self):
        """Test adding L2 entries."""
        from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import LOverviewParagraph

        indent_sample = IndentSample()
        l2 = LOverviewParagraph()

        result = indent_sample.addL2(l2)
        assert l2 in indent_sample.getL2s()
        assert result == indent_sample

        indent_sample.addL2(None)
        assert indent_sample.getL2s() == [l2]


class TestLabeledItem:
    """Test class for LabeledItem class."""

    def test_labeled_item_initialization(self):
        """Test that a LabeledItem object can be initialized with default values."""
        labeled_item = LabeledItem()
        assert labeled_item.helpEntry is None
        assert labeled_item.itemContents is None
        assert labeled_item.itemLabel is None

    def test_labeled_item_item_label_methods(self):
        """Test the itemLabel getter and setter."""
        labeled_item = LabeledItem()
        item_label = MultiLanguageOverviewParagraph()

        result = labeled_item.setItemLabel(item_label)
        assert labeled_item.getItemLabel() == item_label
        assert result == labeled_item

        labeled_item.setItemLabel(None)
        assert labeled_item.getItemLabel() == item_label

    def test_labeled_item_help_entry_methods(self):
        """Test the helpEntry getter and setter."""
        labeled_item = LabeledItem()
        help_entry = "help"

        result = labeled_item.setHelpEntry(help_entry)
        assert labeled_item.getHelpEntry() == help_entry
        assert result == labeled_item

        labeled_item.setHelpEntry(None)
        assert labeled_item.getHelpEntry() == help_entry

    def test_labeled_item_item_contents_methods(self):
        """Test the itemContents getter and setter."""
        from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock

        labeled_item = LabeledItem()
        contents = DocumentationBlock()

        result = labeled_item.setItemContents(contents)
        assert labeled_item.getItemContents() == contents
        assert result == labeled_item

        labeled_item.setItemContents(None)
        assert labeled_item.getItemContents() == contents


class TestLabeledList:
    """Test class for LabeledList class."""

    def test_labeled_list_initialization(self):
        """Test that a LabeledList object can be initialized with default values."""
        labeled_list = LabeledList()
        assert labeled_list.indentSample is None
        assert labeled_list.labeledItems == []

    def test_labeled_list_labeled_items_methods(self):
        """Test adding labeled items."""
        labeled_list = LabeledList()
        labeled_item = LabeledItem()

        result = labeled_list.addLabeledItem(labeled_item)
        assert labeled_item in labeled_list.getLabeledItems()
        assert result == labeled_list

        labeled_list.addLabeledItem(None)
        assert labeled_list.getLabeledItems() == [labeled_item]

    def test_labeled_list_indent_sample_methods(self):
        """Test the indentSample getter and setter."""
        labeled_list = LabeledList()
        indent_sample = IndentSample()

        result = labeled_list.setIndentSample(indent_sample)
        assert labeled_list.getIndentSample() == indent_sample
        assert result == labeled_list

        labeled_list.setIndentSample(None)
        assert labeled_list.getIndentSample() == indent_sample


class TestDefItem:
    """Test class for DefItem class."""

    def test_def_item_initialization(self):
        """Test that a DefItem object can be initialized with default values."""
        def_item = DefItem()
        assert def_item.def_doc is None
        assert def_item.helpEntry is None

    def test_def_item_def_methods(self):
        """Test the def getter and setter."""
        from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock

        def_item = DefItem()
        def_block = DocumentationBlock()

        result = def_item.setDef(def_block)
        assert def_item.getDef() == def_block
        assert result == def_item

        def_item.setDef(None)
        assert def_item.getDef() == def_block

    def test_def_item_help_entry_methods(self):
        """Test the helpEntry getter and setter."""
        def_item = DefItem()
        help_entry = "help"

        result = def_item.setHelpEntry(help_entry)
        assert def_item.getHelpEntry() == help_entry
        assert result == def_item

        def_item.setHelpEntry(None)
        assert def_item.getHelpEntry() == help_entry


class TestDefList:
    """Test class for DefList class."""

    def test_def_list_initialization(self):
        """Test that a DefList object can be initialized with default values."""
        def_list = DefList()
        assert def_list.defItems == []

    def test_def_list_def_items_methods(self):
        """Test adding def items."""
        def_list = DefList()
        def_item = DefItem()

        result = def_list.addDefItem(def_item)
        assert def_item in def_list.getDefItems()
        assert result == def_list

        def_list.addDefItem(None)
        assert def_list.getDefItems() == [def_item]

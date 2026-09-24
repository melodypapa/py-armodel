"""
This module contains tests for the ListElements module in MSR.Documentation.BlockElements.
"""

from inspect import cleandoc

from armodel.models.M2.MSR.Documentation.BlockElements.ListElements import (
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

    def test_list_enum_has_spec_note(self):
        """The class docstring carries the Table 9.10 Note verbatim."""
        assert cleandoc(ListEnum.__doc__) == "This meta-class represents the notation of the various types of lists."

    def test_list_enum_spec_literals(self):
        """ListEnum shall expose the 2 spec literals in Table 9.10 order."""
        enum_obj = ListEnum()
        assert ListEnum.NUMBER == "number"
        assert ListEnum.UNNUMBER == "unnumber"
        assert enum_obj.getEnumValues() == ["number", "unnumber"]

    def test_list_enum_validate_enum_value(self):
        """validateEnumValue accepts the model literal values and rejects non-wire forms.

        R23-11 AUTOSAR_00052.xsd LIST-ENUM--SIMPLE (L139836) carries no
        atp.Status="removed" literals, so no legacy forms are valid; the uppercase
        wire forms (NUMBER, UNNUMBER) live only in the consumer-side TYPE attribute
        handling and are not model values.
        """
        enum_obj = ListEnum()
        assert enum_obj.validateEnumValue("number") is True
        assert enum_obj.validateEnumValue("unnumber") is True
        assert enum_obj.validateEnumValue("NUMBER") is False
        assert enum_obj.validateEnumValue("UNNUMBER") is False
        assert enum_obj.validateEnumValue("unknown") is False

    def test_list_enum_set_value_with_member(self):
        """The enum is instantiable and its literal value can be set from a member constant."""
        enum_obj = ListEnum().setValue(ListEnum.UNNUMBER)
        assert enum_obj.getValue() == "unnumber"


class TestItem:
    """Test class for Item class (Table 9.9, AUTOSAR_FO_TPS_GenericStructureTemplate)."""

    def test_item_inheritance(self):
        """Item shall derive from Paginateable (Table 9.9 Base row, most-derived) and carry the VariationPointCapable mixin (XSD 00052 group ITEM carries the VARIATION-POINT element)."""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.VariationPointCapable import VariationPointCapable
        from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView import DocumentViewSelectable, Paginateable

        item = Item()
        assert isinstance(item, Paginateable)
        assert isinstance(item, DocumentViewSelectable)
        assert isinstance(item, VariationPointCapable)

    def test_item_has_spec_note(self):
        """The class docstring carries the Table 9.9 Note verbatim."""
        assert cleandoc(Item.__doc__) == "This meta-class represents one particular item in a list."

    def test_item_contents_annotation_is_optional(self):
        """getItemContents return and setItemContents value shall be Optional[DocumentationBlock] (Rule 0003).

        DocumentationBlock is imported at the BOTTOM of ListElements.py (runtime import,
        cycle-breaker against TextModel.BlockElements), so the name lives in the module's
        runtime globals and plain get_type_hints resolves it on every supported Python
        (3.8's get_type_hints ignores caller-supplied globalns for functions — bpo-39291 —
        which is why the import must be a real module global, not TYPE_CHECKING-only).
        """
        import typing

        from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock

        for cls in (Item, LabeledItem):
            getter_hints = typing.get_type_hints(cls.getItemContents)
            setter_hints = typing.get_type_hints(cls.setItemContents)
            assert getter_hints["return"] == typing.Optional[DocumentationBlock]
            assert setter_hints["value"] == typing.Optional[DocumentationBlock]

    def test_item_contents_round_trip(self):
        """setItemContents stores the DocumentationBlock and the setter chains."""
        from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock

        item = Item()
        contents = DocumentationBlock()

        result = item.setItemContents(contents)
        assert item.getItemContents() == contents
        assert result == item

    def test_set_item_contents_none_noop(self):
        """setItemContents(None) is a no-op and does not overwrite an existing itemContents."""
        from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock

        item = Item()
        contents = DocumentationBlock()

        item.setItemContents(contents)
        item.setItemContents(None)
        assert item.getItemContents() == contents

    def test_item_inherits_paginateable_accessors(self):
        """The Paginateable base accessors remain reachable on Item (Table 9.9 Base row)."""
        from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView import ChapterEnumBreak

        item = Item()
        item.setBreak(ChapterEnumBreak.BREAK)
        assert item.getBreak() == ChapterEnumBreak.BREAK


class TestARList:
    """Test class for ARList class (Table 9.8, AUTOSAR_FO_TPS_GenericStructureTemplate — spec class name List)."""

    def test_ar_list_inheritance(self):
        """ARList shall derive from Paginateable (Table 9.8 Base row, most-derived) and carry the VariationPointCapable mixin (XSD 00052 group LIST carries the VARIATION-POINT element, mmt.qualifiedName="List.variationPoint" — same convention as the Item sibling)."""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.VariationPointCapable import VariationPointCapable
        from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView import DocumentViewSelectable, Paginateable

        ar_list = ARList()
        assert isinstance(ar_list, Paginateable)
        assert isinstance(ar_list, DocumentViewSelectable)
        assert isinstance(ar_list, VariationPointCapable)

    def test_ar_list_has_spec_note(self):
        """The class docstring carries the Table 9.8 Note verbatim."""
        assert cleandoc(ARList.__doc__) == "This meta-class represents the ability to express a list. The kind of list is specified in the attribute."

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

    def test_ar_list_add_item_none_noop(self):
        """addItem(None) is a no-op and is not appended (stamped-sibling accessor convention)."""
        ar_list = ARList()
        item = Item()

        ar_list.addItem(item)
        ar_list.addItem(None)
        assert ar_list.getItems() == [item]

    def test_ar_list_items_annotation_is_typed_list(self):
        """getItems return and addItem value shall be List[Item] / Optional[Item] (Rule 0003)."""
        import typing

        getter_hints = typing.get_type_hints(ARList.getItems)
        adder_hints = typing.get_type_hints(ARList.addItem)
        assert getter_hints["return"] == typing.List[Item]
        assert adder_hints["value"] == typing.Optional[Item]

    def test_ar_list_type_methods(self):
        """Test the type getter and setter."""
        ar_list = ARList()
        list_type = ListEnum()

        result = ar_list.setType(list_type)
        assert ar_list.getType() == list_type
        assert result == ar_list

    def test_ar_list_set_type_none_noop(self):
        """setType(None) is a no-op and does not overwrite an existing type (stamped-sibling accessor convention)."""
        ar_list = ARList()
        list_type = ListEnum()

        ar_list.setType(list_type)
        ar_list.setType(None)
        assert ar_list.getType() == list_type

    def test_ar_list_type_annotation_is_optional_list_enum(self):
        """getType return and setType value shall be Optional[ListEnum] (Rule 0003)."""
        import typing

        getter_hints = typing.get_type_hints(ARList.getType)
        setter_hints = typing.get_type_hints(ARList.setType)
        assert getter_hints["return"] == typing.Optional[ListEnum]
        assert setter_hints["value"] == typing.Optional[ListEnum]

    def test_ar_list_member_order(self):
        """Field-to-spec cross-check: ARList adds exactly the 2 Table 9.8 attribute rows over its base, in displayed order (item, type)."""
        from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView import Paginateable

        class _ConcretePaginateable(Paginateable):
            pass

        base_fields = set(vars(_ConcretePaginateable()).keys())
        own_fields = [key for key in vars(ARList()).keys() if key not in base_fields]
        assert own_fields == ["items", "type"]


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

"""
This module contains tests for the ListElements module in MSR.Documentation.BlockElements.
"""

import inspect
from inspect import cleandoc

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import String
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
        assert ListEnum.NUMBER == "NUMBER"
        assert ListEnum.UNNUMBER == "UNNUMBER"

    def test_list_enum_has_spec_note(self):
        """The class docstring carries the Table 9.10 Note verbatim."""
        assert cleandoc(ListEnum.__doc__) == "This meta-class represents the notation of the various types of lists."

    def test_list_enum_spec_literals(self):
        """ListEnum shall expose the 2 spec literals in Table 9.10 order."""
        enum_obj = ListEnum()
        assert ListEnum.NUMBER == "NUMBER"
        assert ListEnum.UNNUMBER == "UNNUMBER"
        assert enum_obj.getEnumValues() == ["NUMBER", "UNNUMBER"]

    def test_list_enum_validate_enum_value(self):
        """validateEnumValue accepts the model literal values and rejects non-wire forms.

        R23-11 AUTOSAR_00052.xsd LIST-ENUM--SIMPLE (L139836) carries no
        atp.Status="removed" literals, so no legacy forms are valid; the uppercase
        wire forms (NUMBER, UNNUMBER) live only in the consumer-side TYPE attribute
        handling and are not model values.
        """
        enum_obj = ListEnum()
        assert enum_obj.validateEnumValue("NUMBER") is True
        assert enum_obj.validateEnumValue("UNNUMBER") is True
        assert enum_obj.validateEnumValue("number") is False
        assert enum_obj.validateEnumValue("unnumber") is False
        assert enum_obj.validateEnumValue("unknown") is False

    def test_list_enum_set_value_with_member(self):
        """The enum is instantiable and its literal value can be set from a member constant."""
        enum_obj = ListEnum().setValue(ListEnum.UNNUMBER)
        assert enum_obj.getValue() == ListEnum.UNNUMBER


class TestItem:
    """Test class for Item class (Table 9.9, AUTOSAR_FO_TPS_GenericStructureTemplate)."""

    def test_item_inheritance(self):
        """Item shall derive from Paginateable (Table 9.9 Base row, most-derived) and carry the VariationPointCapable mixin (XSD 00052 group ITEM carries the VARIATION-POINT element)."""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable
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
        cycle-breaker against BlockElements), so the name lives in the module's
        runtime globals and plain get_type_hints resolves it on every supported Python
        (3.8's get_type_hints ignores caller-supplied globalns for functions — bpo-39291 —
        which is why the import must be a real module global, not TYPE_CHECKING-only).
        """
        import typing

        from armodel.models.M2.MSR.Documentation.BlockElements import DocumentationBlock

        for cls in (Item, LabeledItem):
            getter_hints = typing.get_type_hints(cls.getItemContents)
            setter_hints = typing.get_type_hints(cls.setItemContents)
            assert getter_hints["return"] == typing.Optional[DocumentationBlock]
            assert setter_hints["value"] == typing.Optional[DocumentationBlock]

    def test_item_contents_round_trip(self):
        """setItemContents stores the DocumentationBlock and the setter chains."""
        from armodel.models.M2.MSR.Documentation.BlockElements import DocumentationBlock

        item = Item()
        contents = DocumentationBlock()

        result = item.setItemContents(contents)
        assert item.getItemContents() == contents
        assert result == item

    def test_set_item_contents_none_noop(self):
        """setItemContents(None) is a no-op and does not overwrite an existing itemContents."""
        from armodel.models.M2.MSR.Documentation.BlockElements import DocumentationBlock

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
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable
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

    def test_ar_list_accessor_order(self):
        """Accessor pairs in spec row order with the Rule 0001.11 pair shapes: the aggregated `item` pair is mutator-first (addItem/getItems), then the scalar `type` pair is getter-first (getType/setType)."""
        methods = [name for name in vars(ARList) if not name.startswith("_")]
        assert methods == ["addItem", "getItems", "getType", "setType"]


class TestItemLabelPosEnum:
    """Test class for ItemLabelPosEnum class (Table 9.14, AUTOSAR_FO_TPS_GenericStructureTemplate)."""

    SPEC_NOTE = "This enumerator specifies, how the label of a labeled list shall be rendered."

    def test_item_label_pos_enum_is_ar_enum(self):
        """The enumeration derives from AREnum and is instantiable (Rule 0010)."""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum

        assert issubclass(ItemLabelPosEnum, AREnum)
        assert isinstance(ItemLabelPosEnum(), ItemLabelPosEnum)

    def test_item_label_pos_enum_has_spec_note(self):
        """The class docstring carries the Table 9.14 Note verbatim."""
        assert cleandoc(ItemLabelPosEnum.__doc__) == self.SPEC_NOTE

    def test_item_label_pos_enum_init_has_no_docstring(self):
        """__init__ has no docstring (Rule 0012.2.4)."""
        assert ItemLabelPosEnum.__init__.__doc__ is None

    def test_item_label_pos_enum_spec_literals(self):
        """ItemLabelPosEnum shall expose the 3 Table 9.14 literals in displayed order with the XSD facet values."""
        expected = {
            ItemLabelPosEnum.NEWLINE: "NEWLINE",
            ItemLabelPosEnum.NEWLINE_IF_NECESSARY: "NEWLINE-IF-NECESSARY",
            ItemLabelPosEnum.NO_NEWLINE: "NO-NEWLINE",
        }
        for const, value in expected.items():
            assert const == value
        assert tuple(ItemLabelPosEnum().getEnumValues()) == ("NEWLINE", "NEWLINE-IF-NECESSARY", "NO-NEWLINE")

    def test_item_label_pos_enum_literal_notes_are_verbatim(self):
        """Each literal's inline comment is the Table 9.14 Description (incl. the Tags tail) verbatim."""
        source = inspect.getsource(ItemLabelPosEnum)
        for note in (
            "The label is renders in a new line. Tags: atp.EnumerationLiteralIndex=0",
            "The label is rendered in a new line if it is longer than the indentation. Tags: atp.EnumerationLiteralIndex=1",
            "The label is rendered in one line with the item even if it is longer than the indentation. Tags: atp.EnumerationLiteralIndex=2",
        ):
            assert note in source

    def test_item_label_pos_enum_validate_enum_value(self):
        """validateEnumValue accepts the XSD wire forms only (AUTOSAR_00052.xsd ITEM-LABEL-POS-ENUM--SIMPLE)."""
        item_label_pos_enum = ItemLabelPosEnum()
        assert item_label_pos_enum.validateEnumValue("NEWLINE") is True
        assert item_label_pos_enum.validateEnumValue("NEWLINE-IF-NECESSARY") is True
        assert item_label_pos_enum.validateEnumValue("NO-NEWLINE") is True
        assert item_label_pos_enum.validateEnumValue("NEWLINE_IF_NECESSARY") is False
        assert item_label_pos_enum.validateEnumValue("newlineIfNecessary") is False
        assert item_label_pos_enum.validateEnumValue("unknown") is False

    def test_item_label_pos_enum_set_value_with_member(self):
        """The enum value is set and read through members, never plain strings (Rule 0011)."""
        item_label_pos_enum = ItemLabelPosEnum().setValue(ItemLabelPosEnum.NEWLINE_IF_NECESSARY)
        assert item_label_pos_enum.getValue() == ItemLabelPosEnum.NEWLINE_IF_NECESSARY


class TestIndentSample:
    """Test class for IndentSample class (Table 9.13, AUTOSAR_FO_TPS_GenericStructureTemplate)."""

    ITEM_LABEL_POS_NOTE = 'The position of the label in case the label is too long. The default is "NO-NEWLINE" Tags: xml.attribute=true'
    L2_NOTE = (
        "This represents the indent sample in one particular language. "
        "Tags: xml.roleElement=true xml.roleWrapperElement=false xml.sequenceOffset=20 "
        "xml.typeElement=false xml.typeWrapperElement=false"
    )

    def test_indent_sample_inheritance(self):
        """IndentSample shall derive from ARObject (Table 9.13 Base row)."""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

        indent_sample = IndentSample()
        assert isinstance(indent_sample, ARObject)

    def test_indent_sample_has_spec_note(self):
        """The class docstring carries the Table 9.13 Note verbatim."""
        assert (
            cleandoc(IndentSample.__doc__)
            == "This represents the ability to specify indentation of a labeled list by providing a sample content. This content can be measured by the rendering system in order to determine the width of indentation."
        )

    def test_indent_sample_init_has_no_docstring(self):
        """__init__ has no docstring (spec Notes live in inline member comments)."""
        assert IndentSample.__init__.__doc__ is None

    def test_indent_sample_initialization(self):
        """Test that an IndentSample object can be initialized with default values."""
        indent_sample = IndentSample()
        assert indent_sample.itemLabelPos is None
        assert indent_sample.l2s == []

    def test_indent_sample_item_label_pos_methods(self):
        """Test the itemLabelPos getter and setter (None is a no-op)."""
        indent_sample = IndentSample()
        pos = ItemLabelPosEnum()

        result = indent_sample.setItemLabelPos(pos)
        assert indent_sample.getItemLabelPos() is pos
        assert result is indent_sample

        indent_sample.setItemLabelPos(None)
        assert indent_sample.getItemLabelPos() is pos

    def test_indent_sample_l2s_methods(self):
        """Test adding L2 entries (None is a no-op)."""
        from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import LOverviewParagraph

        indent_sample = IndentSample()
        l2 = LOverviewParagraph()

        result = indent_sample.addL2(l2)
        assert l2 in indent_sample.getL2s()
        assert result is indent_sample

        indent_sample.addL2(None)
        assert indent_sample.getL2s() == [l2]

    def test_item_label_pos_annotation_is_optional_item_label_pos_enum(self):
        """getItemLabelPos return and setItemLabelPos value shall be Optional[ItemLabelPosEnum] (Rule 0003, Table 9.13 Mult 0..1)."""
        import typing

        getter_hints = typing.get_type_hints(IndentSample.getItemLabelPos)
        setter_hints = typing.get_type_hints(IndentSample.setItemLabelPos)
        assert getter_hints["return"] == typing.Optional[ItemLabelPosEnum]
        assert setter_hints["value"] == typing.Optional[ItemLabelPosEnum]

    def test_l2s_annotation_is_typed_list(self):
        """getL2s return and addL2 value shall be List[LOverviewParagraph] / Optional[LOverviewParagraph] (Rule 0003, Table 9.13 Mult 1..*)."""
        import typing

        from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import LOverviewParagraph

        getter_hints = typing.get_type_hints(IndentSample.getL2s)
        adder_hints = typing.get_type_hints(IndentSample.addL2)
        assert getter_hints["return"] == typing.List[LOverviewParagraph]
        assert adder_hints["value"] == typing.Optional[LOverviewParagraph]

    def test_indent_sample_member_order(self):
        """Field-to-spec cross-check: IndentSample adds exactly the 2 Table 9.13 attribute rows over its base, in displayed order (itemLabelPos, l2s)."""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

        class _ConcreteARObject(ARObject):
            pass

        base_fields = set(vars(_ConcreteARObject()).keys())
        own_fields = [key for key in vars(IndentSample()).keys() if key not in base_fields]
        assert own_fields == ["itemLabelPos", "l2s"]

    def test_indent_sample_accessor_order(self):
        """Accessor pairs in spec row order with the Rule 0001.11 pair shapes: the scalar `itemLabelPos` pair is getter-first, the aggregated `l2` pair is mutator-first (addL2/getL2s)."""
        methods = [name for name in vars(IndentSample) if not name.startswith("_")]
        assert methods == ["getItemLabelPos", "setItemLabelPos", "addL2", "getL2s"]

    def test_item_label_pos_member_notes_verbatim(self):
        """The itemLabelPos Note is verbatim (incl. the Tags: tail, Rule 0012.2.5.3) on the __init__ comment and both accessors."""
        source = inspect.getsource(IndentSample.__init__)
        assert self.ITEM_LABEL_POS_NOTE in source

        assert IndentSample.getItemLabelPos.__doc__.strip() == self.ITEM_LABEL_POS_NOTE
        assert IndentSample.setItemLabelPos.__doc__.strip() == self.ITEM_LABEL_POS_NOTE + ". A None value is a no-op and does not overwrite an existing itemLabelPos."

    def test_l2_member_notes_verbatim(self):
        """The l2 Note is verbatim (incl. the Tags: tail, Rule 0012.2.5.3) on the __init__ comment and both accessors."""
        source = inspect.getsource(IndentSample.__init__)
        assert self.L2_NOTE in source

        assert IndentSample.getL2s.__doc__.strip() == self.L2_NOTE
        assert IndentSample.addL2.__doc__.strip() == self.L2_NOTE + ". A None value is a no-op and is not appended."


class TestLabeledItem:
    """Test class for LabeledItem class (Table 9.12, AUTOSAR_FO_TPS_GenericStructureTemplate)."""

    HELP_ENTRY_NOTE = (
        "This specifies an entry point in an online help system to be linked with the parent class. "
        "The syntax shall be defined by the applied help system respectively help system generator. "
        "Tags: xml.attribute=true"
    )
    ITEM_CONTENTS_NOTE = (
        "This represents the actual content of the item. It is composed of a DocumentationBlock. "
        "This way it is possible to use simple paragraphs to nested lists, formula, figures or notes. "
        "Tags: xml.roleElement=false xml.roleWrapperElement=false xml.sequenceOffset=30 "
        "xml.typeElement=false xml.typeWrapperElement=false"
    )
    ITEM_LABEL_NOTE = "This is the label of the item. Tags: xml.sequenceOffset=20"

    def test_labeled_item_inheritance(self):
        """LabeledItem shall derive from Paginateable (Table 9.12 Base row, most-derived) and carry the VariationPointCapable mixin (XSD 00052 group LABELED-ITEM carries the VARIATION-POINT element, mmt.qualifiedName="LabeledItem.variationPoint")."""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable
        from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView import DocumentViewSelectable, Paginateable

        labeled_item = LabeledItem()
        assert isinstance(labeled_item, Paginateable)
        assert isinstance(labeled_item, DocumentViewSelectable)
        assert isinstance(labeled_item, VariationPointCapable)

    def test_labeled_item_has_spec_note(self):
        """The class docstring carries the Table 9.12 Note verbatim."""
        assert cleandoc(LabeledItem.__doc__) == "this represents an item of a labeled list."

    def test_labeled_item_init_has_no_docstring(self):
        """__init__ has no docstring (spec Notes live in inline member comments)."""
        assert LabeledItem.__init__.__doc__ is None

    def test_labeled_item_initialization(self):
        """Test that a LabeledItem object can be initialized with default values."""
        labeled_item = LabeledItem()
        assert labeled_item.helpEntry is None
        assert labeled_item.itemContents is None
        assert labeled_item.itemLabel is None

    def test_labeled_item_help_entry_methods(self):
        """Test the helpEntry getter and setter (None is a no-op)."""
        labeled_item = LabeledItem()
        help_entry = String().setValue("help")

        result = labeled_item.setHelpEntry(help_entry)
        assert labeled_item.getHelpEntry() is help_entry
        assert result is labeled_item

        labeled_item.setHelpEntry(None)
        assert labeled_item.getHelpEntry() is help_entry

    def test_labeled_item_item_contents_methods(self):
        """Test the itemContents getter and setter (None is a no-op)."""
        from armodel.models.M2.MSR.Documentation.BlockElements import DocumentationBlock

        labeled_item = LabeledItem()
        contents = DocumentationBlock()

        result = labeled_item.setItemContents(contents)
        assert labeled_item.getItemContents() is contents
        assert result is labeled_item

        labeled_item.setItemContents(None)
        assert labeled_item.getItemContents() is contents

    def test_labeled_item_item_label_methods(self):
        """Test the itemLabel getter and setter (None is a no-op)."""
        labeled_item = LabeledItem()
        item_label = MultiLanguageOverviewParagraph()

        result = labeled_item.setItemLabel(item_label)
        assert labeled_item.getItemLabel() is item_label
        assert result is labeled_item

        labeled_item.setItemLabel(None)
        assert labeled_item.getItemLabel() is item_label

    def test_help_entry_annotation_is_optional_string(self):
        """getHelpEntry return and setHelpEntry value shall be Optional[String] (Rule 0003, Table 9.12 Type String, Mult 0..1)."""
        import typing

        getter_hints = typing.get_type_hints(LabeledItem.getHelpEntry)
        setter_hints = typing.get_type_hints(LabeledItem.setHelpEntry)
        assert getter_hints["return"] == typing.Optional[String]
        assert setter_hints["value"] == typing.Optional[String]

    def test_item_contents_annotation_is_optional_documentation_block(self):
        """getItemContents return and setItemContents value shall be Optional[DocumentationBlock] (Rule 0003, Table 9.12 Mult 0..1)."""
        import typing

        from armodel.models.M2.MSR.Documentation.BlockElements import DocumentationBlock

        getter_hints = typing.get_type_hints(LabeledItem.getItemContents)
        setter_hints = typing.get_type_hints(LabeledItem.setItemContents)
        assert getter_hints["return"] == typing.Optional[DocumentationBlock]
        assert setter_hints["value"] == typing.Optional[DocumentationBlock]

    def test_item_label_annotation_is_optional_multi_language_overview_paragraph(self):
        """getItemLabel return and setItemLabel value shall be Optional[MultiLanguageOverviewParagraph] (Rule 0003, Table 9.12)."""
        import typing

        getter_hints = typing.get_type_hints(LabeledItem.getItemLabel)
        setter_hints = typing.get_type_hints(LabeledItem.setItemLabel)
        assert getter_hints["return"] == typing.Optional[MultiLanguageOverviewParagraph]
        assert setter_hints["value"] == typing.Optional[MultiLanguageOverviewParagraph]

    def test_labeled_item_member_order(self):
        """Field-to-spec cross-check: LabeledItem adds exactly the 3 Table 9.12 attribute rows over its base, in displayed order (helpEntry, itemContents, itemLabel)."""
        from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView import Paginateable

        class _ConcretePaginateable(Paginateable):
            pass

        base_fields = set(vars(_ConcretePaginateable()).keys())
        own_fields = [key for key in vars(LabeledItem()).keys() if key not in base_fields]
        assert own_fields == ["helpEntry", "itemContents", "itemLabel"]

    def test_labeled_item_accessor_order(self):
        """Accessor pairs in spec row order, each single-valued pair getter-first (Rule 0001.11)."""
        methods = [name for name in vars(LabeledItem) if not name.startswith("_")]
        assert methods == ["getHelpEntry", "setHelpEntry", "getItemContents", "setItemContents", "getItemLabel", "setItemLabel"]

    def test_help_entry_member_notes_verbatim(self):
        """The helpEntry Note is verbatim (incl. the Tags: tail, Rule 0012.2.5.3) on the __init__ comment and both accessors."""
        source = inspect.getsource(LabeledItem.__init__)
        assert self.HELP_ENTRY_NOTE in source

        assert LabeledItem.getHelpEntry.__doc__.strip() == self.HELP_ENTRY_NOTE
        assert LabeledItem.setHelpEntry.__doc__.strip() == self.HELP_ENTRY_NOTE + ". A None value is a no-op and does not overwrite an existing helpEntry."

    def test_item_contents_member_notes_verbatim(self):
        """The itemContents Note is verbatim (incl. the Tags: tail, Rule 0012.2.5.3) on the __init__ comment and both accessors."""
        source = inspect.getsource(LabeledItem.__init__)
        assert self.ITEM_CONTENTS_NOTE in source

        assert LabeledItem.getItemContents.__doc__.strip() == self.ITEM_CONTENTS_NOTE
        assert LabeledItem.setItemContents.__doc__.strip() == self.ITEM_CONTENTS_NOTE + ". A None value is a no-op and does not overwrite an existing itemContents."

    def test_item_label_member_notes_verbatim(self):
        """The itemLabel Note is verbatim (incl. the Tags: tail, Rule 0012.2.5.3) on the __init__ comment and both accessors."""
        source = inspect.getsource(LabeledItem.__init__)
        assert self.ITEM_LABEL_NOTE in source

        assert LabeledItem.getItemLabel.__doc__.strip() == self.ITEM_LABEL_NOTE
        assert LabeledItem.setItemLabel.__doc__.strip() == self.ITEM_LABEL_NOTE + ". A None value is a no-op and does not overwrite an existing itemLabel."


class TestLabeledList:
    """Test class for LabeledList class (Table 9.11, AUTOSAR_FO_TPS_GenericStructureTemplate)."""

    INDENT_SAMPLE_NOTE = (
        "This is a sample item. This sample is used by a rendering system to measure out the width of indentation. "
        "Since this depends on the particular fontsize etc. the indentation cannot be specified e.g. in mm. "
        "Tags: xml.sequenceOffset=20"
    )
    LABELED_ITEM_NOTE = (
        "This represents one particular item in the labeled list. "
        "Stereotypes: atpSplitable; atpVariation "
        "Tags: atp.Splitkey=labeledItem, labeledItem.variationPoint.shortLabel vh.latestBindingTime=postBuild "
        "xml.roleElement=true xml.roleWrapperElement=false xml.sequenceOffset=30 "
        "xml.typeElement=false xml.typeWrapperElement=false"
    )

    def test_labeled_list_inheritance(self):
        """LabeledList shall derive from Paginateable (Table 9.11 Base row, most-derived) and carry the VariationPointCapable mixin (XSD 00052 group LABELED-LIST carries the VARIATION-POINT element, mmt.qualifiedName="LabeledList.variationPoint" — same convention as the Item/ARList siblings)."""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable
        from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView import DocumentViewSelectable, Paginateable

        labeled_list = LabeledList()
        assert isinstance(labeled_list, Paginateable)
        assert isinstance(labeled_list, DocumentViewSelectable)
        assert isinstance(labeled_list, VariationPointCapable)

    def test_labeled_list_has_spec_note(self):
        """The class docstring carries the Table 9.11 Note verbatim."""
        assert (
            cleandoc(LabeledList.__doc__)
            == "This meta-class represents a labeled list, in which items have a label and a content. The policy how to render such items is specified in the labeled list."
        )

    def test_init_has_no_docstring(self):
        """__init__ has no docstring (spec Notes live in inline member comments)."""
        assert LabeledList.__init__.__doc__ is None

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

    def test_labeled_items_annotation_is_typed_list(self):
        """getLabeledItems return and addLabeledItem value shall be List[LabeledItem] / Optional[LabeledItem] (Rule 0003)."""
        import typing

        getter_hints = typing.get_type_hints(LabeledList.getLabeledItems)
        adder_hints = typing.get_type_hints(LabeledList.addLabeledItem)
        assert getter_hints["return"] == typing.List[LabeledItem]
        assert adder_hints["value"] == typing.Optional[LabeledItem]

    def test_indent_sample_annotation_is_optional(self):
        """getIndentSample return and setIndentSample value shall be Optional[IndentSample] (Rule 0003, Table 9.11 Mult 0..1)."""
        import typing

        getter_hints = typing.get_type_hints(LabeledList.getIndentSample)
        setter_hints = typing.get_type_hints(LabeledList.setIndentSample)
        assert getter_hints["return"] == typing.Optional[IndentSample]
        assert setter_hints["value"] == typing.Optional[IndentSample]

    def test_labeled_list_member_order(self):
        """Field-to-spec cross-check: LabeledList adds exactly the 2 Table 9.11 attribute rows over its base, in displayed order (indentSample, labeledItem)."""
        from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView import Paginateable

        class _ConcretePaginateable(Paginateable):
            pass

        base_fields = set(vars(_ConcretePaginateable()).keys())
        own_fields = [key for key in vars(LabeledList()).keys() if key not in base_fields]
        assert own_fields == ["indentSample", "labeledItems"]

    def test_labeled_list_accessor_order(self):
        """Accessor pairs in spec row order with the Rule 0001.11 pair shapes: the scalar `indentSample` pair is getter-first (getIndentSample/setIndentSample), the aggregated `labeledItem` pair is mutator-first (addLabeledItem/getLabeledItems)."""
        methods = [name for name in vars(LabeledList) if not name.startswith("_")]
        assert methods == ["getIndentSample", "setIndentSample", "addLabeledItem", "getLabeledItems"]

    def test_indent_sample_member_notes_verbatim(self):
        """The indentSample Note is verbatim (incl. the Tags: tail, Rule 0012.2.5.3) on the __init__ comment and both accessors."""
        source = inspect.getsource(LabeledList.__init__)
        assert self.INDENT_SAMPLE_NOTE in source

        assert LabeledList.getIndentSample.__doc__.strip() == self.INDENT_SAMPLE_NOTE
        assert LabeledList.setIndentSample.__doc__.strip() == self.INDENT_SAMPLE_NOTE + ". A None value is a no-op and does not overwrite an existing indentSample."

    def test_labeled_item_member_notes_verbatim(self):
        """The labeledItem Note is verbatim (incl. the Stereotypes:/Tags: tail, Rule 0012.2.5.3; shortLabel per the XSD appinfo) on the __init__ comment and both accessors."""
        source = inspect.getsource(LabeledList.__init__)
        assert self.LABELED_ITEM_NOTE in source

        assert LabeledList.getLabeledItems.__doc__.strip() == self.LABELED_ITEM_NOTE
        assert LabeledList.addLabeledItem.__doc__.strip() == self.LABELED_ITEM_NOTE + ". A None value is a no-op and is not appended."


class TestDefItem:
    """Test class for DefItem class (Table 9.16, AUTOSAR_FO_TPS_GenericStructureTemplate)."""

    DEF_NOTE = "This represents the definition part of the DefItem. Tags: xml.sequenceOffset=20"
    HELP_ENTRY_NOTE = (
        "This specifies an entry point in an online help system to be linked with the parent class. "
        "The syntax shall be defined by the applied help system respectively help system generator. "
        "Tags: xml.attribute=true"
    )

    def test_def_item_inheritance(self):
        """DefItem shall derive from MultilanguageReferrable (Table 9.16 Base row, most-derived; covers Referrable/ARObject), Paginateable (covers DocumentViewSelectable) and carry the VariationPointCapable mixin (XSD 00052 group DEF-ITEM carries the VARIATION-POINT element, mmt.qualifiedName="DefItem.variationPoint")."""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import MultilanguageReferrable
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable
        from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView import DocumentViewSelectable, Paginateable

        def_item = DefItem(DefList(), "DefItem1")
        assert isinstance(def_item, MultilanguageReferrable)
        assert isinstance(def_item, DocumentViewSelectable)
        assert isinstance(def_item, Paginateable)
        assert isinstance(def_item, VariationPointCapable)

    def test_def_item_has_spec_note(self):
        """The class docstring carries the Table 9.16 Note verbatim."""
        assert cleandoc(DefItem.__doc__) == "This represents an entry in a definition list. The defined item is specified using shortName and longName."

    def test_def_item_init_has_no_docstring(self):
        """__init__ has no docstring (spec Notes live in inline member comments)."""
        assert DefItem.__init__.__doc__ is None

    def test_def_item_initialization(self):
        """Test that a DefItem object can be initialized with default values."""
        def_list = DefList()
        def_item = DefItem(def_list, "DefItem1")
        assert def_item.def_doc is None
        assert def_item.helpEntry is None
        assert def_item.getShortName() == "DefItem1"

    def test_def_item_def_methods(self):
        """Test the def getter and setter (None is a no-op)."""
        from armodel.models.M2.MSR.Documentation.BlockElements import DocumentationBlock

        def_list = DefList()
        def_item = DefItem(def_list, "DefItem1")
        def_block = DocumentationBlock()

        result = def_item.setDef(def_block)
        assert def_item.getDef() is def_block
        assert result is def_item

        def_item.setDef(None)
        assert def_item.getDef() is def_block

    def test_def_item_help_entry_methods(self):
        """Test the helpEntry getter and setter with the spec type String (None is a no-op)."""
        def_list = DefList()
        def_item = DefItem(def_list, "DefItem1")
        help_entry = String().setValue("help")

        result = def_item.setHelpEntry(help_entry)
        assert def_item.getHelpEntry() is help_entry
        assert def_item.getHelpEntry().getValue() == "help"
        assert result is def_item

        def_item.setHelpEntry(None)
        assert def_item.getHelpEntry() is help_entry

    def test_def_annotation_is_optional_documentation_block(self):
        """getDef return and setDef value shall be Optional[DocumentationBlock] (Rule 0003, Table 9.16 Type DocumentationBlock, Mult 1; the spec attribute name `def` is kept as def_doc — Python keyword)."""
        import typing

        from armodel.models.M2.MSR.Documentation.BlockElements import DocumentationBlock

        getter_hints = typing.get_type_hints(DefItem.getDef)
        setter_hints = typing.get_type_hints(DefItem.setDef)
        assert getter_hints["return"] == typing.Optional[DocumentationBlock]
        assert setter_hints["value"] == typing.Optional[DocumentationBlock]

    def test_help_entry_annotation_is_optional_string(self):
        """getHelpEntry return and setHelpEntry value shall be Optional[String] (Rule 0003, Table 9.16 Type String, Mult 0..1)."""
        import typing

        getter_hints = typing.get_type_hints(DefItem.getHelpEntry)
        setter_hints = typing.get_type_hints(DefItem.setHelpEntry)
        assert getter_hints["return"] == typing.Optional[String]
        assert setter_hints["value"] == typing.Optional[String]

    def test_def_item_member_order(self):
        """Field-to-spec cross-check: DefItem adds exactly the 2 Table 9.16 attribute rows over its base, in displayed order (def, helpEntry)."""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import MultilanguageReferrable
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable
        from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView import Paginateable

        class _ConcreteBaseTrio(MultilanguageReferrable, Paginateable, VariationPointCapable):
            pass

        base_fields = set(vars(_ConcreteBaseTrio(DefList(), "BaseTrio")).keys())
        own_fields = [key for key in vars(DefItem(DefList(), "DefItem1")).keys() if key not in base_fields]
        assert own_fields == ["def_doc", "helpEntry"]

    def test_def_item_accessor_order(self):
        """Accessor pairs in spec row order (def, helpEntry), each single-valued pair getter-first (Rule 0001.11)."""
        methods = [name for name in vars(DefItem) if not name.startswith("_")]
        assert methods == ["getDef", "setDef", "getHelpEntry", "setHelpEntry"]

    def test_def_member_notes_verbatim(self):
        """The def Note is verbatim (incl. the Tags: tail, Rule 0012.2.5.3) on the __init__ comment and both accessors."""
        source = inspect.getsource(DefItem.__init__)
        assert self.DEF_NOTE in source

        assert DefItem.getDef.__doc__.strip() == self.DEF_NOTE
        assert DefItem.setDef.__doc__.strip() == self.DEF_NOTE + ". A None value is a no-op and does not overwrite an existing def."

    def test_help_entry_member_notes_verbatim(self):
        """The helpEntry Note is verbatim (incl. the Tags: tail, Rule 0012.2.5.3) on the __init__ comment and both accessors."""
        source = inspect.getsource(DefItem.__init__)
        assert self.HELP_ENTRY_NOTE in source

        assert DefItem.getHelpEntry.__doc__.strip() == self.HELP_ENTRY_NOTE
        assert DefItem.setHelpEntry.__doc__.strip() == self.HELP_ENTRY_NOTE + ". A None value is a no-op and does not overwrite an existing helpEntry."


class TestDefList:
    """Test class for DefList class."""

    def test_def_list_initialization(self):
        """Test that a DefList object can be initialized with default values."""
        def_list = DefList()
        assert def_list.defItems == []

    def test_def_list_create_def_item(self):
        """createDefItem builds a DefItem owned by the list and reuses an existing short name."""
        def_list = DefList()

        def_item = def_list.createDefItem("DefItem1")
        assert isinstance(def_item, DefItem)
        assert def_item.getParent() == def_list
        assert def_list.getDefItems() == [def_item]

        assert def_list.createDefItem("DefItem1") is def_item
        assert len(def_list.getDefItems()) == 1

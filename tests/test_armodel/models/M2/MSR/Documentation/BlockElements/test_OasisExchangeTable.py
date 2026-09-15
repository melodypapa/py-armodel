"""Tests for the OasisExchangeTable enums (FloatEnum, PgwideEnum, FrameEnum)."""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral, Integer, NameToken, String
from armodel.models.M2.MSR.Documentation.BlockElements import Caption
from armodel.models.M2.MSR.Documentation.BlockElements.OasisExchangeTable import (
    AlignEnum,
    Colspec,
    Entry,
    FloatEnum,
    FrameEnum,
    OrientEnum,
    PgwideEnum,
    Row,
    Table,
    TableSeparatorString,
    Tbody,
    Tgroup,
    ValignEnum,
)
from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView import (
    ChapterEnumBreak,
    DocumentViewSelectable,
    KeepWithPreviousEnum,
    Paginateable,
)
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock


class TestFloatEnum:
    """Test class for FloatEnum class."""

    def test_float_enum_members(self):
        """Test that FloatEnum has the expected members."""
        assert FloatEnum.FLOAT == "float"
        assert FloatEnum.NO_FLOAT == "noFloat"

    def test_float_enum_initialization(self):
        """Test that a FloatEnum object can be initialized."""
        float_enum = FloatEnum()
        assert float_enum.validateEnumValue("float")
        assert float_enum.validateEnumValue("noFloat")
        assert not float_enum.validateEnumValue("unknown")


class TestPgwideEnum:
    """Test class for PgwideEnum class."""

    def test_pgwide_enum_members(self):
        """Test that PgwideEnum has the expected members."""
        assert PgwideEnum.NO_PGWIDE == "noPgwide"
        assert PgwideEnum.PGWIDE == "pgwide"

    def test_pgwide_enum_initialization(self):
        """Test that a PgwideEnum object can be initialized."""
        pgwide_enum = PgwideEnum()
        assert pgwide_enum.validateEnumValue("noPgwide")
        assert pgwide_enum.validateEnumValue("pgwide")
        assert not pgwide_enum.validateEnumValue("unknown")


class TestFrameEnum:
    """Test class for FrameEnum class."""

    def test_frame_enum_members(self):
        """Test that FrameEnum has the six XSD literals in index order."""
        assert FrameEnum.ALL == "ALL"
        assert FrameEnum.BOTTOM == "BOTTOM"
        assert FrameEnum.NONE == "NONE"
        assert FrameEnum.SIDES == "SIDES"
        assert FrameEnum.TOP == "TOP"
        assert FrameEnum.TOPBOT == "TOPBOT"

    def test_frame_enum_initialization(self):
        """Test that a FrameEnum object validates its literals."""
        frame_enum = FrameEnum()
        assert frame_enum.validateEnumValue("ALL")
        assert frame_enum.validateEnumValue("TOPBOT")
        assert not frame_enum.validateEnumValue("unknown")

    def test_frame_enum_set_get_value(self):
        """Test that the enum value round-trips via setValue/getValue."""
        frame_enum = FrameEnum()
        frame_enum.setValue(FrameEnum.SIDES)
        assert frame_enum.getValue() == "SIDES"


class TestAlignEnum:
    """Test class for AlignEnum class."""

    def test_align_enum_members(self):
        """Test that AlignEnum has the four XSD literals in index order."""
        assert AlignEnum.CENTER == "CENTER"
        assert AlignEnum.JUSTIFY == "JUSTIFY"
        assert AlignEnum.LEFT == "LEFT"
        assert AlignEnum.RIGHT == "RIGHT"

    def test_align_enum_initialization(self):
        """Test that an AlignEnum object validates its literals."""
        align_enum = AlignEnum()
        assert align_enum.validateEnumValue("CENTER")
        assert align_enum.validateEnumValue("RIGHT")
        assert not align_enum.validateEnumValue("unknown")

    def test_align_enum_set_get_value(self):
        """Test that the enum value round-trips via setValue/getValue."""
        align_enum = AlignEnum()
        align_enum.setValue(AlignEnum.JUSTIFY)
        assert align_enum.getValue() == "JUSTIFY"


class TestValignEnum:
    """Test class for ValignEnum class."""

    def test_valign_enum_members(self):
        """Test that ValignEnum has the three XSD literals in index order."""
        assert ValignEnum.BOTTOM == "BOTTOM"
        assert ValignEnum.MIDDLE == "MIDDLE"
        assert ValignEnum.TOP == "TOP"

    def test_valign_enum_initialization(self):
        """Test that a ValignEnum object validates its literals."""
        valign_enum = ValignEnum()
        assert valign_enum.validateEnumValue("BOTTOM")
        assert valign_enum.validateEnumValue("TOP")
        assert not valign_enum.validateEnumValue("unknown")

    def test_valign_enum_set_get_value(self):
        """Test that the enum value round-trips via setValue/getValue."""
        valign_enum = ValignEnum()
        valign_enum.setValue(ValignEnum.MIDDLE)
        assert valign_enum.getValue() == "MIDDLE"


class TestOrientEnum:
    """Test class for OrientEnum class."""

    def test_orient_enum_members(self):
        """Test that OrientEnum has the two XSD literals in index order."""
        assert OrientEnum.LAND == "LAND"
        assert OrientEnum.PORT == "PORT"

    def test_orient_enum_initialization(self):
        """Test that an OrientEnum object validates its literals."""
        orient_enum = OrientEnum()
        assert orient_enum.validateEnumValue("LAND")
        assert orient_enum.validateEnumValue("PORT")
        assert not orient_enum.validateEnumValue("unknown")

    def test_orient_enum_set_get_value(self):
        """Test that the enum value round-trips via setValue/getValue."""
        orient_enum = OrientEnum()
        orient_enum.setValue(OrientEnum.PORT)
        assert orient_enum.getValue() == "PORT"


class TestTableSeparatorString:
    """Test class for TableSeparatorString (Table 9.72, Primitive)."""

    def test_initialization(self):
        """Test that TableSeparatorString initializes as an ARLiteral with no value."""
        separator = TableSeparatorString()
        assert separator is not None
        assert isinstance(separator, ARLiteral)
        assert separator._value is None

    def test_set_get_value(self):
        """Test that the value round-trips via setValue and str()."""
        separator = TableSeparatorString()
        assert separator.setValue("1") is separator
        assert separator.value == "1"
        assert str(separator) == "1"


class TestColspec:
    """Test class for Colspec (Table E.21)."""

    def test_initialization_and_accessors(self):
        colspec = Colspec()
        assert colspec.getAlign() is None
        assert colspec.getColname() is None
        assert colspec.getColnum() is None
        assert colspec.getColsep() is None
        assert colspec.getColwidth() is None
        assert colspec.getRowsep() is None

        values = {
            "Align": AlignEnum().setValue(AlignEnum.CENTER),
            "Colname": String().setValue("name"),
            "Colnum": String().setValue("1"),
            "Colsep": TableSeparatorString().setValue("1"),
            "Colwidth": String().setValue("2*"),
            "Rowsep": TableSeparatorString().setValue("0"),
        }
        for name, value in values.items():
            assert getattr(colspec, "set" + name)(value) is colspec
            assert getattr(colspec, "get" + name)() is value
            assert getattr(colspec, "set" + name)(None) is colspec
            assert getattr(colspec, "get" + name)() is value


class TestEntry:
    """Test class for Entry (Table 9.71)."""

    def test_initialization_and_accessors(self):
        entry = Entry()
        assert entry.getAlign() is None
        assert entry.getBgcolor() is None
        assert entry.getColname() is None
        assert entry.getColsep() is None
        assert entry.getEntryContents() is None
        assert entry.getMorerows() is None
        assert entry.getNameend() is None
        assert entry.getNamest() is None
        assert entry.getRotate() is None
        assert entry.getRowsep() is None
        assert entry.getSpanname() is None
        assert entry.getValign() is None

        values = {
            "Align": AlignEnum().setValue(AlignEnum.CENTER),
            "Bgcolor": String().setValue("#FFFFFF"),
            "Colname": String().setValue("name"),
            "Colsep": TableSeparatorString().setValue("1"),
            "EntryContents": DocumentationBlock(),
            "Morerows": String().setValue("0"),
            "Nameend": String().setValue("c2"),
            "Namest": String().setValue("c1"),
            "Rotate": String().setValue("0"),
            "Rowsep": TableSeparatorString().setValue("0"),
            "Spanname": String().setValue("span"),
            "Valign": ValignEnum().setValue(ValignEnum.TOP),
        }
        for name, value in values.items():
            assert getattr(entry, "set" + name)(value) is entry
            assert getattr(entry, "get" + name)() is value
            assert getattr(entry, "set" + name)(None) is entry
            assert getattr(entry, "get" + name)() is value


class TestRow:
    """Test class for Row (Table 9.70)."""

    def test_initialization_and_bases(self):
        row = Row()

        assert isinstance(row, DocumentViewSelectable)
        assert isinstance(row, Paginateable)
        assert row.getEntries() == []
        assert row.getRowsep() is None
        assert row.getValign() is None

    def test_entry_aggregation_and_optional_attributes(self):
        row = Row()
        entry = Entry()
        row.addEntry(entry)

        assert row.getEntries() == [entry]
        assert row.setRowsep(TableSeparatorString().setValue("1")) is row
        assert row.getRowsep().getValue() == "1"
        assert row.setValign(ValignEnum().setValue(ValignEnum.MIDDLE)) is row
        assert row.getValign().getValue() == ValignEnum.MIDDLE

    def test_none_setters_are_no_ops(self):
        row = Row()
        row.setRowsep(TableSeparatorString().setValue("0"))
        row.setValign(ValignEnum().setValue(ValignEnum.TOP))

        assert row.setRowsep(None).getRowsep().getValue() == "0"
        assert row.setValign(None).getValign().getValue() == ValignEnum.TOP


class TestTbody:
    """Test class for Tbody (Table 9.68)."""

    def test_initialization_and_accessors(self):
        tbody = Tbody()
        assert tbody.getRows() == []
        assert tbody.getValign() is None

        row = Row()
        assert tbody.addRow(row) is tbody
        assert tbody.getRows() == [row]
        assert tbody.setValign(ValignEnum().setValue(ValignEnum.MIDDLE)) is tbody
        assert tbody.getValign().getValue() == ValignEnum.MIDDLE
        assert tbody.setValign(None).getValign().getValue() == ValignEnum.MIDDLE


class TestTgroup:
    """Test class for Tgroup (Table 9.66)."""

    def test_initialization_and_accessors(self):
        tgroup = Tgroup()
        assert tgroup.getColspecs() == []
        assert tgroup.getThead() is None
        assert tgroup.getTfoot() is None
        assert tgroup.getTbody() is None
        assert tgroup.getAlign() is None
        assert tgroup.getCols() is None
        assert tgroup.getColsep() is None
        assert tgroup.getRowsep() is None

        colspec = Colspec()
        tbody = Tbody()
        assert tgroup.addColspec(colspec) is tgroup
        assert tgroup.getColspecs() == [colspec]
        assert tgroup.setTbody(tbody) is tgroup
        assert tgroup.getTbody() is tbody
        assert tgroup.setAlign(AlignEnum().setValue(AlignEnum.CENTER)) is tgroup
        assert tgroup.setCols(Integer().setValue(2)) is tgroup
        assert tgroup.setColsep(TableSeparatorString().setValue("1")) is tgroup
        assert tgroup.setRowsep(TableSeparatorString().setValue("0")) is tgroup
        assert tgroup.getAlign().getValue() == AlignEnum.CENTER
        assert tgroup.getCols().getValue() == 2
        assert tgroup.getColsep().getValue() == "1"
        assert tgroup.getRowsep().getValue() == "0"


class TestTable:
    """Test class for Table (Table 9.63)."""

    def test_initialization_and_bases(self):
        table = Table()

        assert isinstance(table, DocumentViewSelectable)
        assert isinstance(table, Paginateable)
        assert table.getColsep() is None
        assert table.getFloat() is None
        assert table.getFrame() is None
        assert table.getHelpEntry() is None
        assert table.getOrient() is None
        assert table.getPgwide() is None
        assert table.getRowsep() is None
        assert table.getTableCaption() is None
        assert table.getTabstyle() is None
        assert table.getTgroups() == []

    def test_attribute_accessors_and_none_no_op(self):
        table = Table()
        values = {
            "Colsep": TableSeparatorString().setValue("1"),
            "Float": FloatEnum().setValue(FloatEnum.FLOAT),
            "Frame": FrameEnum().setValue(FrameEnum.ALL),
            "HelpEntry": String().setValue("help"),
            "Orient": OrientEnum().setValue(OrientEnum.LAND),
            "Pgwide": NameToken().setValue("pgwide"),
            "Rowsep": TableSeparatorString().setValue("0"),
            "Tabstyle": NameToken().setValue("style"),
        }
        for name, value in values.items():
            assert getattr(table, "set" + name)(value) is table
            assert getattr(table, "get" + name)() is value
            assert getattr(table, "set" + name)(None) is table
            assert getattr(table, "get" + name)() is value

    def test_tgroup_aggregation_and_table_caption(self):
        table = Table()
        tgroup = Tgroup()
        caption = Caption(None, "table_1")

        assert table.addTgroup(tgroup) is table
        assert table.getTgroups() == [tgroup]
        assert table.setTableCaption(caption) is table
        assert table.getTableCaption() is caption

    def test_inherited_pagination_accessors(self):
        table = Table()
        assert table.setBreak(ChapterEnumBreak().setValue(ChapterEnumBreak.BREAK)) is table
        assert table.getBreak().getValue() == ChapterEnumBreak.BREAK
        assert table.setKeepWithPrevious(KeepWithPreviousEnum().setValue(KeepWithPreviousEnum.KEEP)) is table
        assert table.getKeepWithPrevious().getValue() == KeepWithPreviousEnum.KEEP

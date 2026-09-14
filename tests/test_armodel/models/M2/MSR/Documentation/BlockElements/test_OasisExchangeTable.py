"""Tests for the OasisExchangeTable enums (FloatEnum, PgwideEnum, FrameEnum)."""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral, String
from armodel.models.M2.MSR.Documentation.BlockElements.OasisExchangeTable import AlignEnum, Colspec, FloatEnum, FrameEnum, OrientEnum, PgwideEnum, TableSeparatorString, ValignEnum


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

"""Tests for the OasisExchangeTable enums (FloatEnum, PgwideEnum, FrameEnum)."""

from armodel.models.M2.MSR.Documentation.BlockElements.OasisExchangeTable import AlignEnum, FloatEnum, FrameEnum, PgwideEnum, ValignEnum


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

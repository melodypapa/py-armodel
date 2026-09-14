"""Tests for the OasisExchangeTable enums (FloatEnum, PgwideEnum, FrameEnum)."""

from armodel.models.M2.MSR.Documentation.BlockElements.OasisExchangeTable import FloatEnum, FrameEnum, PgwideEnum


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

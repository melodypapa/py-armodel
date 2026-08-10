"""Tests for the OasisExchangeTable enums (FloatEnum, PgwideEnum)."""

from armodel.models.M2.MSR.Documentation.BlockElements.OasisExchangeTable import FloatEnum, PgwideEnum


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

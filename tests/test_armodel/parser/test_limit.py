"""Reader tests for Limit (Swc TPS Table 5.86, p.408).

Limit serializes on the consuming element (LOWER-LIMIT, UPPER-LIMIT, ...): the element
text is the limit value (LIMIT-VALUE pattern) and the INTERVAL-TYPE attribute carries
the UPPERCASE XSD wire token (AR:INTERVAL-TYPE-ENUM--SIMPLE: CLOSED|INFINITE|OPEN),
decoded to the camelCase IntervalTypeEnum member via INTERVAL_TYPE_XML_MAP.
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import IntervalTypeEnum, Limit
from tests.test_armodel.parser._helpers import _snip


class TestLimitReader:
    def test_read_field_values(self, parser):
        element = _snip(
            """
            <LOWER-LIMIT INTERVAL-TYPE="CLOSED">0</LOWER-LIMIT>
            """,
        )
        limit = parser.getChildLimitElement(element, "LOWER-LIMIT")
        assert limit is not None
        assert isinstance(limit, Limit)
        assert isinstance(limit.getIntervalType(), IntervalTypeEnum)
        assert limit.getIntervalType().getValue() == "closed"
        assert limit.getValue() == "0"

    def test_read_open_token_maps_to_member_value(self, parser):
        """The UPPERCASE XSD wire token maps to the camelCase IntervalTypeEnum member value."""
        element = _snip(
            """
            <UPPER-LIMIT INTERVAL-TYPE="OPEN">65535</UPPER-LIMIT>
            """,
        )
        limit = parser.getChildLimitElement(element, "UPPER-LIMIT")
        assert limit is not None
        assert isinstance(limit.getIntervalType(), IntervalTypeEnum)
        assert limit.getIntervalType().getValue() == "open"
        assert limit.getValue() == "65535"

    def test_read_without_interval_type_defaults_to_none(self, parser):
        """A missing INTERVAL-TYPE attribute leaves intervalType unset (spec default "CLOSED")."""
        element = _snip(
            """
            <UPPER-LIMIT>INF</UPPER-LIMIT>
            """,
        )
        limit = parser.getChildLimitElement(element, "UPPER-LIMIT")
        assert limit is not None
        assert limit.getIntervalType() is None
        assert limit.getValue() == "INF"

    def test_read_missing_element_returns_none(self, parser):
        element = _snip(
            """
            <MONOTONY>DECREASING</MONOTONY>
            """,
        )
        assert parser.getChildLimitElement(element, "LOWER-LIMIT") is None

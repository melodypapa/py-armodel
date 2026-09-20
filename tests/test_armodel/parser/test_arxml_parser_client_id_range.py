"""Tests for the readClientIdRange handler (R23-11 ClientIdRange, Table 3.2, p.52)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import ClientIdRange, EcuInstance
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test and pin the R23-11 release."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    """Fresh ARXMLParser instance running in strict mode."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    return ARXMLParser()


def _snip(inner: str, root_tag: str = "ROOT") -> ET.Element:
    """Wrap an inner XML fragment in a root element bound to the AUTOSAR NS."""
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


def _range() -> ClientIdRange:
    return ClientIdRange()


class TestReadClientIdRange:
    """Tests for readClientIdRange handler (R23-11 ClientIdRange, Table 3.2, p.52)."""

    def test_read_client_id_range_full(self, parser):
        element = _snip(
            """
                <LOWER-LIMIT INTERVAL-TYPE="CLOSED">0</LOWER-LIMIT>
                <UPPER-LIMIT INTERVAL-TYPE="OPEN">255</UPPER-LIMIT>
            """,
            root_tag="CLIENT-ID-RANGE",
        )
        id_range = _range()
        parser.readClientIdRange(element, id_range)
        assert id_range.getLowerLimit().getValue() == "0"
        assert id_range.getLowerLimit().getIntervalType().getValue() == "CLOSED"
        assert id_range.getUpperLimit().getValue() == "255"
        assert id_range.getUpperLimit().getIntervalType().getValue() == "OPEN"

    def test_read_client_id_range_empty(self, parser):
        element = _snip(
            """
            """,
            root_tag="CLIENT-ID-RANGE",
        )
        id_range = _range()
        parser.readClientIdRange(element, id_range)
        assert id_range.getLowerLimit() is None
        assert id_range.getUpperLimit() is None

    def test_read_ecu_instance_client_id_range(self, parser):
        element = _snip(
            """
                <SHORT-NAME>ecu</SHORT-NAME>
                <CLIENT-ID-RANGE>
                    <LOWER-LIMIT>1</LOWER-LIMIT>
                    <UPPER-LIMIT>65534</UPPER-LIMIT>
                </CLIENT-ID-RANGE>
            """,
            root_tag="ECU-INSTANCE",
        )
        instance = EcuInstance(parent=AUTOSAR.getInstance(), short_name="ecu")
        parser.readEcuInstance(element, instance)
        id_range = instance.getClientIdRange()
        assert id_range is not None
        assert id_range.getLowerLimit().getValue() == "1"
        assert id_range.getUpperLimit().getValue() == "65534"

"""Tests for the writeClientIdRange handler (R23-11 ClientIdRange, Table 3.2, p.52)."""

import xml.etree.cElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import IntervalTypeEnum, Limit
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import ClientIdRange, EcuInstance
from armodel.writer.arxml_writer import ARXMLWriter

XSD_CHILD_ORDER = [
    "LOWER-LIMIT",
    "UPPER-LIMIT",
]


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    return ARXMLWriter()


def _parent():
    return ET.Element("PARENT")


def _limit(value, interval_type=None):
    limit = Limit()
    limit.setValue(value)
    if interval_type is not None:
        limit.setIntervalType(IntervalTypeEnum().setValue(interval_type))
    return limit


def _fill_range(id_range):
    id_range.setLowerLimit(_limit("0", "CLOSED"))
    id_range.setUpperLimit(_limit("255", "OPEN"))
    return id_range


class TestWriteClientIdRange:
    """Tests for writeClientIdRange handler (R23-11 ClientIdRange, Table 3.2, p.52)."""

    def test_children_in_xsd_order(self, writer):
        id_range = _fill_range(ClientIdRange())

        parent = _parent()
        writer.writeClientIdRange(parent, id_range)
        child = parent.find("CLIENT-ID-RANGE")
        assert child is not None
        child_tags = [element.tag for element in child]
        assert child_tags == XSD_CHILD_ORDER
        lower_limit = child.find("LOWER-LIMIT")
        assert lower_limit.text == "0"
        assert lower_limit.get("INTERVAL-TYPE") == "CLOSED"
        upper_limit = child.find("UPPER-LIMIT")
        assert upper_limit.text == "255"
        assert upper_limit.get("INTERVAL-TYPE") == "OPEN"

    def test_empty_children_omitted(self, writer):
        id_range = ClientIdRange()
        parent = _parent()
        writer.writeClientIdRange(parent, id_range)
        child = parent.find("CLIENT-ID-RANGE")
        assert child is not None
        for tag in XSD_CHILD_ORDER:
            assert child.find(tag) is None

    def test_write_ecu_instance_client_id_range(self, writer):
        instance = EcuInstance(parent=AUTOSAR.getInstance(), short_name="ecu")
        instance.setClientIdRange(_fill_range(ClientIdRange()))

        parent = _parent()
        writer.writeEcuInstance(parent, instance)
        ecu = parent.find("ECU-INSTANCE")
        assert ecu is not None
        range_element = ecu.find("CLIENT-ID-RANGE")
        assert range_element is not None
        child_tags = [element.tag for element in range_element]
        assert child_tags == XSD_CHILD_ORDER
        assert range_element.find("LOWER-LIMIT").text == "0"
        assert range_element.find("UPPER-LIMIT").text == "255"

    def test_write_ecu_instance_without_client_id_range_omits_element(self, writer):
        instance = EcuInstance(parent=AUTOSAR.getInstance(), short_name="ecu")
        parent = _parent()
        writer.writeEcuInstance(parent, instance)
        ecu = parent.find("ECU-INSTANCE")
        assert ecu.find("CLIENT-ID-RANGE") is None

"""Tests for the writeFlexrayTpPduPool handler (R23-11 FlexrayTpPduPool, Table 6.242, p.596)."""

import xml.etree.cElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import FlexrayTpConfig, FlexrayTpPduPool
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


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


@pytest.fixture
def parser():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    return ARXMLParser()


def _parent():
    return ET.Element("PARENT")


def _ref(value, dest):
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


def _pool(short_name: str) -> FlexrayTpPduPool:
    package = AUTOSAR.getInstance().createARPackage("TpConfigs")
    return FlexrayTpPduPool(package, short_name)


class TestWriteFlexrayTpPduPool:
    """Tests for writeFlexrayTpPduPool (R23-11 FlexrayTpPduPool, Table 6.242, p.596)."""

    def test_write_refs_wrapper_in_xsd_order(self, writer):
        pool = _pool("Pool1")
        pool.addNPduRef(_ref("/NPdus/N1", "N-PDU"))
        pool.addNPduRef(_ref("/NPdus/N2", "N-PDU"))
        parent = _parent()
        writer.writeFlexrayTpPduPool(parent, pool)
        child = parent.find("FLEXRAY-TP-PDU-POOL")
        assert child is not None
        child_tags = [element.tag for element in child if element.tag != "SHORT-NAME"]
        assert child_tags == ["N-PDU-REFS"]
        refs = child.findall("N-PDU-REFS/N-PDU-REF")
        assert len(refs) == 2
        assert refs[0].text == "/NPdus/N1"
        assert refs[0].get("DEST") == "N-PDU"
        assert refs[1].text == "/NPdus/N2"

    def test_empty_pool_writes_no_wrapper(self, writer):
        pool = _pool("Pool1")
        parent = _parent()
        writer.writeFlexrayTpPduPool(parent, pool)
        child = parent.find("FLEXRAY-TP-PDU-POOL")
        assert child is not None
        child_tags = [element.tag for element in child if element.tag != "SHORT-NAME"]
        assert child_tags == []

    def test_round_trip_via_config(self, writer, parser):
        config = FlexrayTpConfig(AUTOSAR.getInstance().createARPackage("TpConfigs"), "Config1")
        pool = config.createFlexrayTpPduPool("Pool1")
        pool.addNPduRef(_ref("/NPdus/N1", "N-PDU"))
        pool.addNPduRef(_ref("/NPdus/N2", "N-PDU"))

        parent = _parent()
        writer.writeFlexrayTpConfig(parent, config)
        xml_text = ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1)
        assert "N-PDU-REFS" in xml_text

        reparsed = ET.fromstring(xml_text)[0]
        config2 = FlexrayTpConfig(AUTOSAR.getInstance().createARPackage("TpConfigs"), "Config1")
        parser.readFlexrayTpConfig(reparsed, config2)
        pools = config2.getPduPools()
        assert len(pools) == 1
        assert pools[0].getShortName() == "Pool1"
        refs = pools[0].getNPduRefs()
        assert len(refs) == 2
        assert refs[0].getValue() == "/NPdus/N1"
        assert refs[0].getDest() == "N-PDU"
        assert refs[1].getValue() == "/NPdus/N2"
        assert refs[1].getDest() == "N-PDU"

"""Tests for the readFlexrayTpPduPool handler (R23-11 FlexrayTpPduPool, Table 6.242, p.596)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import FlexrayTpConfig, FlexrayTpPduPool
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    return ARXMLParser()


def _snip(inner: str, root_tag: str = "ROOT") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadFlexrayTpPduPool:
    """Tests for readFlexrayTpPduPool (R23-11 FlexrayTpPduPool, Table 6.242, p.596)."""

    def test_read_full_pool(self, parser):
        element = _snip(
            """
                <SHORT-NAME>Pool1</SHORT-NAME>
                <N-PDU-REFS>
                    <N-PDU-REF DEST="N-PDU">/NPdus/N1</N-PDU-REF>
                    <N-PDU-REF DEST="N-PDU">/NPdus/N2</N-PDU-REF>
                </N-PDU-REFS>
            """,
            root_tag="FLEXRAY-TP-PDU-POOL",
        )
        package = AUTOSAR.getInstance().createARPackage("TpConfigs")
        pool = FlexrayTpPduPool(package, "Pool1")
        parser.readFlexrayTpPduPool(element, pool)
        refs = pool.getNPduRefs()
        assert len(refs) == 2
        assert refs[0].getValue() == "/NPdus/N1"
        assert refs[0].getDest() == "N-PDU"
        assert refs[1].getValue() == "/NPdus/N2"
        assert pool.getShortName() == "Pool1"

    def test_read_empty_pool(self, parser):
        element = _snip(
            """
                <SHORT-NAME>Pool1</SHORT-NAME>
            """,
            root_tag="FLEXRAY-TP-PDU-POOL",
        )
        package = AUTOSAR.getInstance().createARPackage("TpConfigs")
        pool = FlexrayTpPduPool(package, "Pool1")
        parser.readFlexrayTpPduPool(element, pool)
        assert pool.getNPduRefs() == []

    def test_read_via_config_dispatch(self, parser):
        element = _snip(
            """
                <SHORT-NAME>Config1</SHORT-NAME>
                <PDU-POOLS>
                    <FLEXRAY-TP-PDU-POOL>
                        <SHORT-NAME>Pool1</SHORT-NAME>
                        <N-PDU-REFS>
                            <N-PDU-REF DEST="N-PDU">/NPdus/N1</N-PDU-REF>
                        </N-PDU-REFS>
                    </FLEXRAY-TP-PDU-POOL>
                </PDU-POOLS>
            """,
            root_tag="FLEXRAY-TP-CONFIG",
        )
        package = AUTOSAR.getInstance().createARPackage("TpConfigs")
        config = FlexrayTpConfig(package, "Config1")
        parser.readFlexrayTpConfig(element, config)
        pools = config.getPduPools()
        assert len(pools) == 1
        assert pools[0].getShortName() == "Pool1"
        refs = pools[0].getNPduRefs()
        assert len(refs) == 1
        assert refs[0].getValue() == "/NPdus/N1"

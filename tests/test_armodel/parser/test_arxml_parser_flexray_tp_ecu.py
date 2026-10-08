"""Tests for the readFlexrayTpEcu handler (R23-11 FlexrayTpEcu, Table 6.244, p.597)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import FlexrayTpConfig, FlexrayTpEcu
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


class TestReadFlexrayTpEcu:
    """Tests for readFlexrayTpEcu (R23-11 FlexrayTpEcu, Table 6.244, p.597)."""

    def test_read_full_ecu(self, parser):
        element = _snip(
            """
                <CANCELLATION>true</CANCELLATION>
                <CYCLE-TIME-MAIN-FUNCTION>0.005</CYCLE-TIME-MAIN-FUNCTION>
                <ECU-INSTANCE-REF DEST="ECU-INSTANCE">/Topology/Ecu1</ECU-INSTANCE-REF>
                <FULL-DUPLEX-ENABLED>true</FULL-DUPLEX-ENABLED>
            """,
            root_tag="FLEXRAY-TP-ECU",
        )
        ecu = FlexrayTpEcu()
        parser.readFlexrayTpEcu(element, ecu)
        assert ecu.getCancellation() is not None
        assert ecu.getCancellation().getValue() is True
        assert ecu.getCycleTimeMainFunction().getValue() == 0.005
        assert ecu.getEcuInstanceRef().getValue() == "/Topology/Ecu1"
        assert ecu.getEcuInstanceRef().getDest() == "ECU-INSTANCE"
        assert ecu.getFullDuplexEnabled().getValue() is True

    def test_read_empty_ecu(self, parser):
        element = _snip("", root_tag="FLEXRAY-TP-ECU")
        ecu = FlexrayTpEcu()
        parser.readFlexrayTpEcu(element, ecu)
        assert ecu.getCancellation() is None
        assert ecu.getCycleTimeMainFunction() is None
        assert ecu.getEcuInstanceRef() is None
        assert ecu.getFullDuplexEnabled() is None

    def test_read_via_config_dispatch(self, parser):
        element = _snip(
            """
                <SHORT-NAME>Config1</SHORT-NAME>
                <TP-ECUS>
                    <FLEXRAY-TP-ECU>
                        <CANCELLATION>false</CANCELLATION>
                        <ECU-INSTANCE-REF DEST="ECU-INSTANCE">/Topology/Ecu1</ECU-INSTANCE-REF>
                        <FULL-DUPLEX-ENABLED>false</FULL-DUPLEX-ENABLED>
                    </FLEXRAY-TP-ECU>
                </TP-ECUS>
            """,
            root_tag="FLEXRAY-TP-CONFIG",
        )
        package = AUTOSAR.getInstance().createARPackage("TpConfigs")
        config = FlexrayTpConfig(package, "Config1")
        parser.readFlexrayTpConfig(element, config)
        ecus = config.getTpEcus()
        assert len(ecus) == 1
        assert ecus[0].getCancellation().getValue() is False
        assert ecus[0].getEcuInstanceRef().getValue() == "/Topology/Ecu1"
        assert ecus[0].getFullDuplexEnabled().getValue() is False

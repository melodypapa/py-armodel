"""Tests for the readFlexrayTpConnectionControl handler (R23-11 FlexrayTpConnectionControl, Table 6.240, p.593)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import FlexrayTpConfig, FlexrayTpConnectionControl, TpAckType
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


class TestReadFlexrayTpConnectionControl:
    """Tests for readFlexrayTpConnectionControl (R23-11 FlexrayTpConnectionControl, Table 6.240, p.593)."""

    def test_read_full_control(self, parser):
        element = _snip(
            """
                <SHORT-NAME>Control1</SHORT-NAME>
                <ACK-TYPE>ACK-WITH-RT</ACK-TYPE>
                <MAX-FC-WAIT>5</MAX-FC-WAIT>
                <MAX-NUMBER-OF-NPDU-PER-CYCLE>2</MAX-NUMBER-OF-NPDU-PER-CYCLE>
                <MAX-RETRIES>3</MAX-RETRIES>
                <SEPARATION-CYCLE-EXPONENT>1</SEPARATION-CYCLE-EXPONENT>
                <TIME-BR>0.01</TIME-BR>
                <TIME-BUFFER>0.02</TIME-BUFFER>
                <TIME-CS>0.03</TIME-CS>
                <TIMEOUT-AR>0.04</TIMEOUT-AR>
                <TIMEOUT-AS>0.05</TIMEOUT-AS>
                <TIMEOUT-BS>0.06</TIMEOUT-BS>
                <TIMEOUT-CR>0.07</TIMEOUT-CR>
            """,
            root_tag="FLEXRAY-TP-CONNECTION-CONTROL",
        )
        package = AUTOSAR.getInstance().createARPackage("TpConfigs")
        control = FlexrayTpConnectionControl(package, "Control1")
        parser.readFlexrayTpConnectionControl(element, control)
        assert control.getAckType() is not None
        assert isinstance(control.getAckType(), TpAckType)
        assert control.getAckType().getValue() == TpAckType.ENUM_ACK_WITH_RT
        assert control.getMaxFcWait().getValue() == 5
        assert control.getMaxNumberOfNpduPerCycle().getValue() == 2
        assert control.getMaxRetries().getValue() == 3
        assert control.getSeparationCycleExponent().getValue() == 1
        assert control.getTimeBr().getValue() == 0.01
        assert control.getTimeBuffer().getValue() == 0.02
        assert control.getTimeCs().getValue() == 0.03
        assert control.getTimeoutAr().getValue() == 0.04
        assert control.getTimeoutAs().getValue() == 0.05
        assert control.getTimeoutBs().getValue() == 0.06
        assert control.getTimeoutCr().getValue() == 0.07
        assert control.getShortName() == "Control1"

    def test_read_empty_control(self, parser):
        element = _snip(
            """
                <SHORT-NAME>Control1</SHORT-NAME>
            """,
            root_tag="FLEXRAY-TP-CONNECTION-CONTROL",
        )
        package = AUTOSAR.getInstance().createARPackage("TpConfigs")
        control = FlexrayTpConnectionControl(package, "Control1")
        parser.readFlexrayTpConnectionControl(element, control)
        assert control.getAckType() is None
        assert control.getMaxFcWait() is None
        assert control.getMaxNumberOfNpduPerCycle() is None
        assert control.getMaxRetries() is None
        assert control.getSeparationCycleExponent() is None
        assert control.getTimeBr() is None
        assert control.getTimeBuffer() is None
        assert control.getTimeCs() is None
        assert control.getTimeoutAr() is None
        assert control.getTimeoutAs() is None
        assert control.getTimeoutBs() is None
        assert control.getTimeoutCr() is None

    def test_read_via_config_dispatch(self, parser):
        element = _snip(
            """
                <SHORT-NAME>Config1</SHORT-NAME>
                <TP-CONNECTION-CONTROLS>
                    <FLEXRAY-TP-CONNECTION-CONTROL>
                        <SHORT-NAME>Control1</SHORT-NAME>
                        <MAX-RETRIES>4</MAX-RETRIES>
                        <TIMEOUT-AS>0.05</TIMEOUT-AS>
                    </FLEXRAY-TP-CONNECTION-CONTROL>
                </TP-CONNECTION-CONTROLS>
            """,
            root_tag="FLEXRAY-TP-CONFIG",
        )
        package = AUTOSAR.getInstance().createARPackage("TpConfigs")
        config = FlexrayTpConfig(package, "Config1")
        parser.readFlexrayTpConfig(element, config)
        controls = config.getTpConnectionControls()
        assert len(controls) == 1
        assert controls[0].getShortName() == "Control1"
        assert controls[0].getMaxRetries().getValue() == 4
        assert controls[0].getTimeoutAs().getValue() == 0.05

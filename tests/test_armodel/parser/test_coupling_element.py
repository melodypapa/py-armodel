"""
Tests for parsing COUPLING-ELEMENT elements (CouplingElement, Table 3.52, p.108).

Round-trip counterpart: tests/test_armodel/writer/test_coupling_element.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    CouplingElementAbstractDetails,
    CouplingElementSwitchDetails,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    CouplingElement,
    CouplingElementEnum,
    CouplingPort,
)
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    """Create ARXML parser instance."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    return ARXMLParser()


def _make_coupling_element() -> CouplingElement:
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    ar_root = AUTOSAR.getInstance().createARPackage("AUTOSAR")
    return ar_root.createCouplingElement("Switch")


class TestReadCouplingElement:
    """Test readCouplingElement (CouplingElement, Table 3.52)."""

    def test_read_all_members(self, parser):
        """Every COUPLING-ELEMENT group element populates its model field."""
        coupling_element = _make_coupling_element()
        element = ET.fromstring(
            f"""<COUPLING-ELEMENT xmlns='{NS}'>
                <SHORT-NAME>Switch</SHORT-NAME>
                <COMMUNICATION-CLUSTER-REF DEST="ETHERNET-CLUSTER">/AUTOSAR/EthernetClusters/Cluster</COMMUNICATION-CLUSTER-REF>
                <COUPLING-ELEMENT-DETAILS>
                    <COUPLING-ELEMENT-SWITCH-DETAILS>
                        <SHORT-NAME>SwitchDetails</SHORT-NAME>
                    </COUPLING-ELEMENT-SWITCH-DETAILS>
                </COUPLING-ELEMENT-DETAILS>
                <COUPLING-PORTS>
                    <COUPLING-PORT>
                        <SHORT-NAME>Cport1</SHORT-NAME>
                    </COUPLING-PORT>
                    <COUPLING-PORT>
                        <SHORT-NAME>Cport2</SHORT-NAME>
                    </COUPLING-PORT>
                </COUPLING-PORTS>
                <COUPLING-TYPE>SWITCH</COUPLING-TYPE>
                <ECU-INSTANCE-REF DEST="ECU-INSTANCE">/AUTOSAR/Ecus/Ecu1</ECU-INSTANCE-REF>
                <FIREWALL-RULE-REFS>
                    <FIREWALL-RULE-REF DEST="STATE-DEPENDENT-FIREWALL">/AUTOSAR/Firewalls/Rule1</FIREWALL-RULE-REF>
                    <FIREWALL-RULE-REF DEST="STATE-DEPENDENT-FIREWALL">/AUTOSAR/Firewalls/Rule2</FIREWALL-RULE-REF>
                </FIREWALL-RULE-REFS>
            </COUPLING-ELEMENT>"""
        )

        parser.readCouplingElement(element, coupling_element)

        assert coupling_element.getShortName() == "Switch"
        assert coupling_element.getCommunicationClusterRef() is not None
        assert coupling_element.getCommunicationClusterRef().getDest() == "ETHERNET-CLUSTER"
        assert coupling_element.getCommunicationClusterRef().getValue() == "/AUTOSAR/EthernetClusters/Cluster"

        details = coupling_element.getCouplingElementDetails()
        assert isinstance(details, CouplingElementSwitchDetails)
        assert isinstance(details, CouplingElementAbstractDetails)
        assert details.getShortName() == "SwitchDetails"

        ports = coupling_element.getCouplingPorts()
        assert len(ports) == 2
        assert isinstance(ports[0], CouplingPort)
        assert ports[0].getShortName() == "Cport1"
        assert ports[1].getShortName() == "Cport2"

        assert coupling_element.getCouplingType() is not None
        assert coupling_element.getCouplingType().getValue() == CouplingElementEnum.SWITCH

        assert coupling_element.getEcuInstanceRef() is not None
        assert coupling_element.getEcuInstanceRef().getDest() == "ECU-INSTANCE"
        assert coupling_element.getEcuInstanceRef().getValue() == "/AUTOSAR/Ecus/Ecu1"

        firewall_rule_refs = coupling_element.getFirewallRuleRefs()
        assert len(firewall_rule_refs) == 2
        assert firewall_rule_refs[0].getDest() == "STATE-DEPENDENT-FIREWALL"
        assert firewall_rule_refs[0].getValue() == "/AUTOSAR/Firewalls/Rule1"
        assert firewall_rule_refs[1].getValue() == "/AUTOSAR/Firewalls/Rule2"

    def test_read_absent_optional_members(self, parser):
        """Absent optional members leave the fields untouched (empty-wrapper case)."""
        coupling_element = _make_coupling_element()
        element = ET.fromstring(
            f"""<COUPLING-ELEMENT xmlns='{NS}'>
                <SHORT-NAME>Switch</SHORT-NAME>
            </COUPLING-ELEMENT>"""
        )

        parser.readCouplingElement(element, coupling_element)

        assert coupling_element.getCommunicationClusterRef() is None
        assert coupling_element.getCouplingElementDetails() is None
        assert coupling_element.getCouplingPorts() == []
        assert coupling_element.getCouplingType() is None
        assert coupling_element.getEcuInstanceRef() is None
        assert coupling_element.getFirewallRuleRefs() == []

    def test_load_via_ar_package(self, parser):
        """Test that the ARPackage ELEMENTS dispatch reads a COUPLING-ELEMENT."""
        content = f"""<?xml version="1.0" encoding="utf-8"?>
<AUTOSAR xmlns="{NS}" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="{NS} AUTOSAR_00052.xsd">
    <AR-PACKAGES>
        <AR-PACKAGE>
            <SHORT-NAME>AUTOSAR</SHORT-NAME>
            <ELEMENTS>
                <COUPLING-ELEMENT>
                    <SHORT-NAME>Router</SHORT-NAME>
                    <COMMUNICATION-CLUSTER-REF DEST="ETHERNET-CLUSTER">/AUTOSAR/Cluster</COMMUNICATION-CLUSTER-REF>
                    <COUPLING-TYPE>ROUTER</COUPLING-TYPE>
                    <ECU-INSTANCE-REF DEST="ECU-INSTANCE">/AUTOSAR/Ecu1</ECU-INSTANCE-REF>
                </COUPLING-ELEMENT>
            </ELEMENTS>
        </AR-PACKAGE>
    </AR-PACKAGES>
</AUTOSAR>"""
        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)

            document = AUTOSAR.getInstance()
            document.clear()
            parser.load(file_path, document)

            pkg = document.getARPackages()[0]
            coupling_elements = [e for e in pkg.getReferrableElements() if isinstance(e, CouplingElement)]
            assert len(coupling_elements) == 1
            assert coupling_elements[0].getShortName() == "Router"
            assert coupling_elements[0].getCommunicationClusterRef().getValue() == "/AUTOSAR/Cluster"
            assert coupling_elements[0].getCouplingType().getValue() == CouplingElementEnum.ROUTER
            assert coupling_elements[0].getEcuInstanceRef().getValue() == "/AUTOSAR/Ecu1"
            assert coupling_elements[0].getFirewallRuleRefs() == []
        finally:
            os.remove(file_path)

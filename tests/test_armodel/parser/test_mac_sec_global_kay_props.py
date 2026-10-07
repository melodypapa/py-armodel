"""
Reader tests for MacSecGlobalKayProps (CP_TPS_SystemTemplate Table 3.120, p.174, R23-11).

Covers the IDENTIFIABLE base level (SHORT-NAME/UUID round-trip plus the S/T attributes
carried by readIdentifiable's chain down to readARObjectAttributes), the two optional
wrappers BYPASS-ETHER-TYPES/BYPASS-VLANS (each holding maxOccurs=255 POSITIVE-INTEGER
items per AUTOSAR_00052.xsd group MAC-SEC-GLOBAL-KAY-PROPS), the partial and
absent-wrapper cases and the ARPackage ELEMENTS dispatch (aggregated by
ARPackage.element).

Round-trip counterpart: tests/test_armodel/writer/test_mac_sec_global_kay_props.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR as AutosarDocument
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication import MacSecGlobalKayProps
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str) -> ET.Element:
    return ET.fromstring(f"<MAC-SEC-GLOBAL-KAY-PROPS xmlns='{NS}'>{inner}</MAC-SEC-GLOBAL-KAY-PROPS>")


def _snip_with_attrs(attrs: str, inner: str) -> ET.Element:
    return ET.fromstring(f"<MAC-SEC-GLOBAL-KAY-PROPS xmlns='{NS}' {attrs}>{inner}</MAC-SEC-GLOBAL-KAY-PROPS>")


def _full_inner() -> str:
    return (
        "<SHORT-NAME>GKP1</SHORT-NAME>"
        "<BYPASS-ETHER-TYPES>"
        "<BYPASS-ETHER-TYPE>2048</BYPASS-ETHER-TYPE>"
        "<BYPASS-ETHER-TYPE>34825</BYPASS-ETHER-TYPE>"
        "</BYPASS-ETHER-TYPES>"
        "<BYPASS-VLANS>"
        "<BYPASS-VLAN>1</BYPASS-VLAN>"
        "<BYPASS-VLAN>0</BYPASS-VLAN>"
        "</BYPASS-VLANS>"
    )


class TestReadMacSecGlobalKayProps:
    def test_read_identifiable_base_level(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip_with_attrs(
            "UUID='5d3d3d0d-3c1f-4a2b-9d1a-65ab0bd89ab1' S='chk-1' T='2009-07-23T13:38:00Z'",
            "<SHORT-NAME>GKP1</SHORT-NAME>",
        )
        props = MacSecGlobalKayProps(AutosarDocument.getInstance(), "Initial")
        parser.readMacSecGlobalKayProps(element, props)

        assert props.getUuid().getValue() == "5d3d3d0d-3c1f-4a2b-9d1a-65ab0bd89ab1"
        assert props.getChecksum().getValue() == "chk-1"
        assert props.getTimestamp().getValue() == "2009-07-23T13:38:00Z"
        assert props.getBypassEtherTypes() == []
        assert props.getBypassVlans() == []

    def test_read_all_wrappers(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip(_full_inner())
        props = MacSecGlobalKayProps(AutosarDocument.getInstance(), "Initial")
        parser.readMacSecGlobalKayProps(element, props)

        assert [v.getValue() for v in props.getBypassEtherTypes()] == [2048, 34825]
        assert [v.getValue() for v in props.getBypassVlans()] == [1, 0]

    def test_read_partial_wrappers(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("<SHORT-NAME>GKP1</SHORT-NAME><BYPASS-VLANS><BYPASS-VLAN>42</BYPASS-VLAN></BYPASS-VLANS>")
        props = MacSecGlobalKayProps(AutosarDocument.getInstance(), "Initial")
        parser.readMacSecGlobalKayProps(element, props)

        assert props.getBypassEtherTypes() == []
        assert [v.getValue() for v in props.getBypassVlans()] == [42]

    def test_read_empty_wrappers(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip("<SHORT-NAME>GKP1</SHORT-NAME>" "<BYPASS-ETHER-TYPES></BYPASS-ETHER-TYPES>" "<BYPASS-VLANS></BYPASS-VLANS>")
        props = MacSecGlobalKayProps(AutosarDocument.getInstance(), "Initial")
        parser.readMacSecGlobalKayProps(element, props)

        assert props.getBypassEtherTypes() == []
        assert props.getBypassVlans() == []

    def test_load_via_ar_package(self):
        """The ARPackage ELEMENTS dispatch reads a MAC-SEC-GLOBAL-KAY-PROPS element."""
        content = f"""<?xml version="1.0" encoding="utf-8"?>
<AUTOSAR xmlns="{NS}" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="{NS} AUTOSAR_00052.xsd">
    <AR-PACKAGES>
        <AR-PACKAGE>
            <SHORT-NAME>AUTOSAR</SHORT-NAME>
            <ELEMENTS>
                <MAC-SEC-GLOBAL-KAY-PROPS>
                    <SHORT-NAME>GlobalKayProps</SHORT-NAME>
                    <BYPASS-ETHER-TYPES>
                        <BYPASS-ETHER-TYPE>2048</BYPASS-ETHER-TYPE>
                    </BYPASS-ETHER-TYPES>
                    <BYPASS-VLANS>
                        <BYPASS-VLAN>1</BYPASS-VLAN>
                        <BYPASS-VLAN>0</BYPASS-VLAN>
                    </BYPASS-VLANS>
                </MAC-SEC-GLOBAL-KAY-PROPS>
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
            parser = ARXMLParser(options={"warning": True})
            parser.load(file_path, document)

            pkg = document.getARPackages()[0]
            props_list = [e for e in pkg.getReferrableElements() if isinstance(e, MacSecGlobalKayProps)]
            assert len(props_list) == 1
            props = props_list[0]
            assert props.getShortName() == "GlobalKayProps"
            assert [v.getValue() for v in props.getBypassEtherTypes()] == [2048]
            assert [v.getValue() for v in props.getBypassVlans()] == [1, 0]
        finally:
            os.remove(file_path)

"""Parser tests for J1939NodeName (Table 6.321, p.692).

The NAME structure aggregates only under J1939NmNode.nodeName (NODE-NAME
element); coverage runs through the getJ1939NodeName entry point. The S/T
ARObject level (Rule 0025) round-trips through getJ1939NodeName.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


NODE_NAME_XML = (
    "<WRAP xmlns='%(ns)s'>"
    "<NODE-NAME S='42' T='2023-01-01T00:00:00+02:00'>"
    "<ARBITRARY-ADDRESS-CAPABLE>true</ARBITRARY-ADDRESS-CAPABLE>"
    "<ECU-INSTANCE>3</ECU-INSTANCE>"
    "<FUNCTION>170</FUNCTION>"
    "<FUNCTION-INSTANCE>1</FUNCTION-INSTANCE>"
    "<IDENTITIY-NUMBER>4660</IDENTITIY-NUMBER>"
    "<INDUSTRY-GROUP>4</INDUSTRY-GROUP>"
    "<MANUFACTURER-CODE>221</MANUFACTURER-CODE>"
    "<VEHICLE-SYSTEM>4</VEHICLE-SYSTEM>"
    "<VEHICLE-SYSTEM-INSTANCE>2</VEHICLE-SYSTEM-INSTANCE>"
    "</NODE-NAME>"
    "</WRAP>" % {"ns": NS}
)


class TestParseJ1939NodeName:
    def test_parse_field_values(self):
        root = ET.fromstring(NODE_NAME_XML)
        node_name = ARXMLParser().getJ1939NodeName(root, "NODE-NAME")
        assert node_name is not None
        assert node_name.getArbitraryAddressCapable().getValue() is True
        assert node_name.getEcuInstance().getValue() == 3
        assert node_name.getFunction().getValue() == 170
        assert node_name.getFunctionInstance().getValue() == 1
        assert node_name.getIdentitiyNumber().getValue() == 4660
        assert node_name.getIndustryGroup().getValue() == 4
        assert node_name.getManufacturerCode().getValue() == 221
        assert node_name.getVehicleSystem().getValue() == 4
        assert node_name.getVehicleSystemInstance().getValue() == 2

    def test_parse_s_t_attributes(self):
        root = ET.fromstring(NODE_NAME_XML)
        node_name = ARXMLParser().getJ1939NodeName(root, "NODE-NAME")
        assert node_name.getChecksum() is not None
        assert node_name.getChecksum().getValue() == "42"
        assert node_name.getTimestamp() is not None
        assert node_name.getTimestamp().getValue() == "2023-01-01T00:00:00+02:00"

    def test_parse_missing_element_returns_none(self):
        root = ET.fromstring("<OTHER xmlns='%s'/>" % NS)
        assert ARXMLParser().getJ1939NodeName(root, "NODE-NAME") is None

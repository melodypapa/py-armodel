"""Writer round-trip tests for J1939NodeName (Table 6.321, p.692).

The NAME structure is emitted by setJ1939NodeName under the owning NODE-NAME
key; the S/T ARObject level (Rule 0025) round-trip is pinned end-to-end.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, Integer, String
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import J1939NodeName
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _int(value):
    integer = Integer()
    integer.setValue(value)
    return integer


def _bool(value):
    boolean = Boolean()
    boolean.setValue(value)
    return boolean


def _new_node_name():
    node_name = J1939NodeName()
    checksum = String()
    checksum.setValue("42")
    node_name.setChecksum(checksum)
    node_name.setArbitraryAddressCapable(_bool(True))
    node_name.setEcuInstance(_int(3))
    node_name.setFunction(_int(170))
    node_name.setFunctionInstance(_int(1))
    node_name.setIdentitiyNumber(_int(4660))
    node_name.setIndustryGroup(_int(4))
    node_name.setManufacturerCode(_int(221))
    node_name.setVehicleSystem(_int(4))
    node_name.setVehicleSystemInstance(_int(2))
    return node_name


class TestWriteJ1939NodeName:
    def test_write_field_values(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().setJ1939NodeName(parent, "NODE-NAME", _new_node_name())
        node = parent.find("NODE-NAME")
        assert node is not None
        assert node.find("ARBITRARY-ADDRESS-CAPABLE").text == "true"
        assert node.find("ECU-INSTANCE").text == "3"
        assert node.find("FUNCTION").text == "170"
        assert node.find("FUNCTION-INSTANCE").text == "1"
        assert node.find("IDENTITIY-NUMBER").text == "4660"
        assert node.find("INDUSTRY-GROUP").text == "4"
        assert node.find("MANUFACTURER-CODE").text == "221"
        assert node.find("VEHICLE-SYSTEM").text == "4"
        assert node.find("VEHICLE-SYSTEM-INSTANCE").text == "2"

    def test_write_s_t_attributes(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().setJ1939NodeName(parent, "NODE-NAME", _new_node_name())
        node = parent.find("NODE-NAME")
        assert node.attrib["S"] == "42"

    def test_write_none_emits_nothing(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().setJ1939NodeName(parent, "NODE-NAME", None)
        assert parent.find("NODE-NAME") is None

    def test_round_trip_preserves_field_values_and_s_t(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().setJ1939NodeName(parent, "NODE-NAME", _new_node_name())
        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring("<AUTOSAR xmlns='%s'>%s</AUTOSAR>" % (NS, inner))

        parsed = ARXMLParser().getJ1939NodeName(root[0], "NODE-NAME")
        assert parsed is not None
        assert parsed.getChecksum().getValue() == "42"
        assert parsed.getArbitraryAddressCapable().getValue() is True
        assert parsed.getEcuInstance().getValue() == 3
        assert parsed.getFunction().getValue() == 170
        assert parsed.getFunctionInstance().getValue() == 1
        assert parsed.getIdentitiyNumber().getValue() == 4660
        assert parsed.getIndustryGroup().getValue() == 4
        assert parsed.getManufacturerCode().getValue() == 221
        assert parsed.getVehicleSystem().getValue() == 4
        assert parsed.getVehicleSystemInstance().getValue() == 2

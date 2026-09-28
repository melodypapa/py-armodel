"""Writer round-trip tests for FlexrayCommunicationConnector (Table 3.33, p.89).

XML element order per XSD group FLEXRAY-COMMUNICATION-CONNECTOR: NM-READY-SLEEP-TIME,
WAKE-UP-CHANNEL (PNC-FILTER-DATA-MASK carries atp.Status="removed" in R23-11 and is
not serialized). Coverage runs through the CONNECTORS dispatch on writeEcuInstanceConnectors.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, Float, RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import EcuInstance
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

XSD_ORDER = ["NM-READY-SLEEP-TIME", "WAKE-UP-CHANNEL"]


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _float(text):
    value = Float()
    value.setValue(text)
    return value


def _boolean(value):
    value_obj = Boolean()
    value_obj.setValue(value)
    return value_obj


def _new_instance_with_connector():
    pkg = AUTOSAR.getInstance().createARPackage("Pkg")
    instance = EcuInstance(pkg, "Ecu")
    connector = instance.createFlexrayCommunicationConnector("conn")
    connector.setCommControllerRef(RefType().setValue("/flexray/ctrl"))
    connector.setNmReadySleepTime(_float("10.5"))
    connector.setWakeUpChannel(_boolean(True))
    return instance


def _write_instance(instance):
    parent = ET.Element("ECU-INSTANCE")
    ARXMLWriter().writeEcuInstanceConnectors(parent, instance)
    return parent


class TestWriteFlexrayCommunicationConnector:
    def test_write_all_fields_in_xsd_order(self):
        parent = _write_instance(_new_instance_with_connector())
        connector_tag = parent.find("CONNECTORS/FLEXRAY-COMMUNICATION-CONNECTOR")
        assert connector_tag is not None
        tags = [child.tag for child in connector_tag]
        assert tags == ["SHORT-NAME", "COMM-CONTROLLER-REF"] + XSD_ORDER

    def test_write_field_values(self):
        parent = _write_instance(_new_instance_with_connector())
        connector_tag = parent.find("CONNECTORS/FLEXRAY-COMMUNICATION-CONNECTOR")
        assert connector_tag.find("COMM-CONTROLLER-REF").text == "/flexray/ctrl"
        assert connector_tag.find("NM-READY-SLEEP-TIME").text == "10.5"
        assert connector_tag.find("WAKE-UP-CHANNEL").text == "true"

    def test_write_connector_without_flexray_fields_omits_elements(self):
        pkg = AUTOSAR.getInstance().createARPackage("Pkg")
        instance = EcuInstance(pkg, "Ecu")
        instance.createFlexrayCommunicationConnector("conn")
        parent = _write_instance(instance)
        connector_tag = parent.find("CONNECTORS/FLEXRAY-COMMUNICATION-CONNECTOR")
        assert connector_tag is not None
        tags = [child.tag for child in connector_tag]
        for flexray_tag in XSD_ORDER:
            assert flexray_tag not in tags

    def test_round_trip_preserves_all_values(self):
        instance = _new_instance_with_connector()
        parent = _write_instance(instance)
        inner = ET.tostring(parent).decode("utf-8")
        root = ET.fromstring("<ROOT xmlns='%s'>%s</ROOT>" % (NS, inner))

        parsed_pkg = AUTOSAR.getInstance().createARPackage("Parsed")
        parsed_instance = EcuInstance(parsed_pkg, "Ecu")
        ARXMLParser().readEcuInstanceConnectors(root[0], parsed_instance)

        connector = parsed_instance.getConnectors()[0]
        assert connector.getShortName() == "conn"
        assert connector.getCommControllerRef().getValue() == "/flexray/ctrl"
        assert isinstance(connector.getNmReadySleepTime(), Float)
        assert connector.getNmReadySleepTime().getValue() == 10.5
        assert isinstance(connector.getWakeUpChannel(), Boolean)
        assert connector.getWakeUpChannel().getValue() is True

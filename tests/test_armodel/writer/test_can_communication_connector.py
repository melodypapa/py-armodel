"""Writer round-trip tests for CanCommunicationConnector (Table 3.23, p.74).

XML element order per XSD group CAN-COMMUNICATION-CONNECTOR: PNC-WAKEUP-CAN-ID,
PNC-WAKEUP-CAN-ID-EXTENDED, PNC-WAKEUP-CAN-ID-MASK, PNC-WAKEUP-DATA-MASK, PNC-WAKEUP-DLC.
Coverage runs through the CONNECTORS dispatch on writeEcuInstanceConnectors.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, PositiveInteger, PositiveUnlimitedInteger
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import EcuInstance
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

XSD_ORDER = ["PNC-WAKEUP-CAN-ID", "PNC-WAKEUP-CAN-ID-EXTENDED", "PNC-WAKEUP-CAN-ID-MASK", "PNC-WAKEUP-DATA-MASK", "PNC-WAKEUP-DLC"]


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _pos_int(text):
    value = PositiveInteger()
    value.setValue(text)
    return value


def _data_mask(text):
    value = PositiveUnlimitedInteger()
    value.setValue(text)
    return value


def _boolean(value):
    value_obj = Boolean()
    value_obj.setValue(value)
    return value_obj


def _new_instance_with_connector():
    pkg = AUTOSAR.getInstance().createARPackage("Pkg")
    instance = EcuInstance(pkg, "Ecu")
    connector = instance.createCanCommunicationConnector("conn")
    connector.setPncWakeupCanId(_pos_int("401"))
    connector.setPncWakeupCanIdExtended(_boolean(True))
    connector.setPncWakeupCanIdMask(_pos_int("255"))
    connector.setPncWakeupDataMask(_data_mask("65535"))
    connector.setPncWakeupDlc(_pos_int("8"))
    return instance


def _write_instance(instance):
    parent = ET.Element("ECU-INSTANCE")
    ARXMLWriter().writeEcuInstanceConnectors(parent, instance)
    return parent


class TestWriteCanCommunicationConnector:
    def test_write_all_five_fields_in_xsd_order(self):
        parent = _write_instance(_new_instance_with_connector())
        connector_tag = parent.find("CONNECTORS/CAN-COMMUNICATION-CONNECTOR")
        assert connector_tag is not None
        tags = [child.tag for child in connector_tag]
        assert tags == ["SHORT-NAME"] + XSD_ORDER

    def test_write_field_values(self):
        parent = _write_instance(_new_instance_with_connector())
        connector_tag = parent.find("CONNECTORS/CAN-COMMUNICATION-CONNECTOR")
        assert connector_tag.find("PNC-WAKEUP-CAN-ID").text == "401"
        assert connector_tag.find("PNC-WAKEUP-CAN-ID-EXTENDED").text == "true"
        assert connector_tag.find("PNC-WAKEUP-CAN-ID-MASK").text == "255"
        assert connector_tag.find("PNC-WAKEUP-DATA-MASK").text == "65535"
        assert connector_tag.find("PNC-WAKEUP-DLC").text == "8"

    def test_write_connector_without_pnc_fields_omits_elements(self):
        pkg = AUTOSAR.getInstance().createARPackage("Pkg")
        instance = EcuInstance(pkg, "Ecu")
        instance.createCanCommunicationConnector("conn")
        parent = _write_instance(instance)
        connector_tag = parent.find("CONNECTORS/CAN-COMMUNICATION-CONNECTOR")
        assert connector_tag is not None
        tags = [child.tag for child in connector_tag]
        for pnc_tag in XSD_ORDER:
            assert pnc_tag not in tags

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
        assert isinstance(connector.getPncWakeupCanId(), PositiveInteger)
        assert connector.getPncWakeupCanId().getValue() == 401
        assert isinstance(connector.getPncWakeupCanIdExtended(), Boolean)
        assert connector.getPncWakeupCanIdExtended().getValue() is True
        assert isinstance(connector.getPncWakeupCanIdMask(), PositiveInteger)
        assert connector.getPncWakeupCanIdMask().getValue() == 255
        assert isinstance(connector.getPncWakeupDataMask(), PositiveUnlimitedInteger)
        assert connector.getPncWakeupDataMask().getValue() == 65535
        assert isinstance(connector.getPncWakeupDlc(), PositiveInteger)
        assert connector.getPncWakeupDlc().getValue() == 8

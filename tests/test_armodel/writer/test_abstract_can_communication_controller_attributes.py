"""Writer round-trip tests for AbstractCanCommunicationControllerAttributes (Table 3.13, p.64).

XML element order per XSD group ABSTRACT-CAN-COMMUNICATION-CONTROLLER-ATTRIBUTES
(AUTOSAR_00052.xsd line 160): CAN-CONTROLLER-FD-ATTRIBUTES (line 169, type
CAN-CONTROLLER-FD-CONFIGURATION), CAN-CONTROLLER-FD-REQUIREMENTS (line 175, type
CAN-CONTROLLER-FD-CONFIGURATION-REQUIREMENTS), CAN-CONTROLLER-XL-ATTRIBUTES
(line 181, type CAN-CONTROLLER-XL-CONFIGURATION), CAN-CONTROLLER-XL-REQUIREMENTS
(line 187, type CAN-CONTROLLER-XL-CONFIGURATION-REQUIREMENTS). The class is a pure
XSD element group with no own element; round-trip coverage runs through the
CAN-CONTROLLER-CONFIGURATION consumer element (Rule 0001.7).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, DateTime, Integer, PositiveInteger, String
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import (
    CanControllerConfiguration,
    CanControllerConfigurationRequirements,
    CanControllerFdConfiguration,
    CanControllerFdConfigurationRequirements,
    CanControllerXlConfiguration,
    CanControllerXlConfigurationRequirements,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _parent():
    return ET.Element("PARENT")


def _pos_int(text):
    value = PositiveInteger()
    value.setValue(text)
    return value


def _int(text):
    value = Integer()
    value.setValue(text)
    return value


def _bool(value):
    b = Boolean()
    b.setValue(value)
    return b


def _new_group() -> CanControllerConfigurationRequirements:
    group = CanControllerConfigurationRequirements()
    group.setChecksum(String().setValue("1234"))
    group.setTimestamp(DateTime().setValue("2024-01-01T00:00:00Z"))

    fd = CanControllerFdConfiguration()
    fd.setPaddingValue(_pos_int("8"))
    fd.setPropSeg(_pos_int("4"))
    fd.setTxBitRateSwitch(_bool(True))
    group.setCanControllerFdAttributes(fd)

    fd_req = CanControllerFdConfigurationRequirements()
    fd_req.setMaxNumberOfTimeQuantaPerBit(_int("32"))
    fd_req.setMinNumberOfTimeQuantaPerBit(_int("16"))
    fd_req.setTxBitRateSwitch(_bool(False))
    group.setCanControllerFdRequirements(fd_req)

    xl = CanControllerXlConfiguration()
    xl.setErrorSignalingEnabled(_bool(True))
    xl.setPropSeg(_pos_int("6"))
    xl.setPwmL(_pos_int("2"))
    xl.setTrcvPwmModeEnabled(_bool(False))
    group.setCanControllerXlAttributes(xl)

    xl_req = CanControllerXlConfigurationRequirements()
    xl_req.setMaxPwmL(_pos_int("4"))
    xl_req.setMinPwmL(_pos_int("1"))
    group.setCanControllerXlRequirements(xl_req)
    return group


class TestWriteAbstractCanCommunicationControllerAttributes:
    def test_write_none_members_omits_children(self):
        parent = _parent()
        ARXMLWriter().writeAbstractCanCommunicationControllerAttributes(parent, CanControllerConfigurationRequirements())
        assert len(parent) == 0

    def test_write_all_four_children_in_xsd_order(self):
        parent = _parent()
        ARXMLWriter().writeAbstractCanCommunicationControllerAttributes(parent, _new_group())
        tags = [child.tag for child in parent]
        assert tags == [
            "CAN-CONTROLLER-FD-ATTRIBUTES",
            "CAN-CONTROLLER-FD-REQUIREMENTS",
            "CAN-CONTROLLER-XL-ATTRIBUTES",
            "CAN-CONTROLLER-XL-REQUIREMENTS",
        ]

    def test_write_field_values(self):
        parent = _parent()
        ARXMLWriter().writeAbstractCanCommunicationControllerAttributes(parent, _new_group())
        assert parent.get("S") == "1234"
        assert parent.get("T") == "2024-01-01T00:00:00Z"

        fd = parent.find("CAN-CONTROLLER-FD-ATTRIBUTES")
        assert fd.find("PADDING-VALUE").text == "8"
        assert fd.find("PROP-SEG").text == "4"
        assert fd.find("TX-BIT-RATE-SWITCH").text == "true"

        fd_req = parent.find("CAN-CONTROLLER-FD-REQUIREMENTS")
        assert fd_req.find("MAX-NUMBER-OF-TIME-QUANTA-PER-BIT").text == "32"
        assert fd_req.find("MIN-NUMBER-OF-TIME-QUANTA-PER-BIT").text == "16"
        assert fd_req.find("TX-BIT-RATE-SWITCH").text == "false"

        xl = parent.find("CAN-CONTROLLER-XL-ATTRIBUTES")
        assert xl.find("ERROR-SIGNALING-ENABLED").text == "true"
        assert xl.find("PROP-SEG").text == "6"
        assert xl.find("PWM-L").text == "2"
        assert xl.find("TRCV-PWM-MODE-ENABLED").text == "false"

        xl_req = parent.find("CAN-CONTROLLER-XL-REQUIREMENTS")
        assert xl_req.find("MAX-PWM-L").text == "4"
        assert xl_req.find("MIN-PWM-L").text == "1"


class TestAbstractCanCommunicationControllerAttributesRoundTrip:
    def test_round_trip_through_can_controller_configuration(self):
        config = CanControllerConfiguration()
        config.setChecksum(String().setValue("4321"))
        config.setTimestamp(DateTime().setValue("2024-06-01T12:00:00Z"))
        config.setPropSeg(_int("10"))
        config.setSyncJumpWidth(_int("1"))
        config.setCanControllerFdAttributes(_new_group().getCanControllerFdAttributes())
        config.setCanControllerXlRequirements(_new_group().getCanControllerXlRequirements())

        wrapper = ET.SubElement(_parent(), "CAN-CONTROLLER-CONFIGURATION")
        ARXMLWriter().writeCanControllerConfiguration(wrapper, config)
        root = ET.fromstring("<ROOT xmlns='%s'>%s</ROOT>" % (NS, ET.tostring(wrapper).decode("utf-8")))

        parsed = CanControllerConfiguration()
        ARXMLParser().readCanControllerConfiguration(root[0], parsed)

        assert parsed.getChecksum().getValue() == "4321"
        assert parsed.getTimestamp().getValue() == "2024-06-01T12:00:00Z"
        assert parsed.getPropSeg().getValue() == 10
        assert parsed.getSyncJumpWidth().getValue() == 1

        fd = parsed.getCanControllerFdAttributes()
        assert isinstance(fd, CanControllerFdConfiguration)
        assert fd.getPaddingValue().getValue() == 8
        assert fd.getPropSeg().getValue() == 4
        assert fd.getTxBitRateSwitch().getValue() is True

        xl_req = parsed.getCanControllerXlRequirements()
        assert isinstance(xl_req, CanControllerXlConfigurationRequirements)
        assert xl_req.getMaxPwmL().getValue() == 4
        assert xl_req.getMinPwmL().getValue() == 1

        assert parsed.getCanControllerFdRequirements() is None
        assert parsed.getCanControllerXlAttributes() is None

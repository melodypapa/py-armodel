"""Writer/reader round-trip tests for CanXlProps (AdaptivePlatform CAN-XL-PROPS).

CanXlProps is a standalone ARElement consumed by
EthernetCommunicationConnector.canXlPropsRefs / apApplicationEndpoint. It carries
the machine specific CAN XL attributes canBaudrate, canConfig, canFdBaudrate,
canFdConfig, canXlBaudrate, canXlConfig and canXlConfigReqs.
"""

import xml.etree.cElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Integer, PositiveInteger
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import (
    CanControllerConfiguration,
    CanControllerFdConfiguration,
    CanControllerXlConfiguration,
    CanControllerXlConfigurationRequirements,
    CanXlProps,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


def _serialize_and_wrap(element: ET.Element) -> ET.Element:
    inner = ET.tostring(element).decode("utf-8")
    root = ET.fromstring(f"<AUTOSAR xmlns='{NS}'>{inner}</AUTOSAR>")
    return root[0][0]


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    AUTOSAR.getInstance().new()
    return ARXMLWriter()


@pytest.fixture
def parser():
    AUTOSAR.getInstance().new()
    return ARXMLParser()


def _pos(value):
    v = PositiveInteger()
    v.setValue(str(value))
    return v


def _new_props(short_name="CanXlProps_1"):
    props = CanXlProps(None, short_name)
    props.setCanBaudrate(_pos(500000))
    props.setCanConfig(CanControllerConfiguration())
    props.setCanFdBaudrate(_pos(2000000))
    fd_config = CanControllerFdConfiguration()
    fd_config.setPropSeg(_pos(10))
    props.setCanFdConfig(fd_config)
    props.setCanXlBaudrate(_pos(10000000))
    xl_config = CanControllerXlConfiguration()
    xl_config.setPropSeg(_pos(20))
    props.setCanXlConfig(xl_config)
    xl_reqs = CanControllerXlConfigurationRequirements()
    max_tq = Integer()
    max_tq.setValue("50")
    xl_reqs.setMaxNumberOfTimeQuantaPerBit(max_tq)
    props.setCanXlConfigReqs(xl_reqs)
    return props


class TestWriteCanXlProps:
    def test_write_all_fields(self, writer):
        props = _new_props()
        parent = ET.Element("PARENT")
        writer.writeCanXlProps(parent, props)
        element = parent.find("CAN-XL-PROPS")
        assert element is not None
        assert element.find("SHORT-NAME").text == "CanXlProps_1"
        assert element.find("CAN-BAUDRATE").text == "500000"
        assert element.find("CAN-CONFIG") is not None
        assert element.find("CAN-FD-BAUDRATE").text == "2000000"
        assert element.find("CAN-FD-CONFIG") is not None
        assert element.find("CAN-FD-CONFIG/PROP-SEG").text == "10"
        assert element.find("CAN-XL-BAUDRATE").text == "10000000"
        assert element.find("CAN-XL-CONFIG") is not None
        assert element.find("CAN-XL-CONFIG/PROP-SEG").text == "20"
        assert element.find("CAN-XL-CONFIG-REQS") is not None
        assert element.find("CAN-XL-CONFIG-REQS/MAX-NUMBER-OF-TIME-QUANTA-PER-BIT").text == "50"

    def test_write_empty_omits_elements(self, writer):
        props = CanXlProps(None, "Empty")
        parent = ET.Element("PARENT")
        writer.writeCanXlProps(parent, props)
        element = parent.find("CAN-XL-PROPS")
        assert element is not None
        assert element.find("CAN-BAUDRATE") is None
        assert element.find("CAN-CONFIG") is None
        assert element.find("CAN-FD-BAUDRATE") is None
        assert element.find("CAN-FD-CONFIG") is None
        assert element.find("CAN-XL-BAUDRATE") is None
        assert element.find("CAN-XL-CONFIG") is None
        assert element.find("CAN-XL-CONFIG-REQS") is None


class TestCanXlPropsRoundTrip:
    def test_round_trip_preserves_all_values(self, writer, parser):
        props = _new_props()
        parent = ET.Element("PARENT")
        writer.writeCanXlProps(parent, props)
        element = _serialize_and_wrap(parent)
        parsed = CanXlProps(None, "dummy")
        parser.readCanXlProps(element, parsed)
        assert parsed.getCanBaudrate().getValue() == 500000
        assert isinstance(parsed.getCanConfig(), CanControllerConfiguration)
        assert parsed.getCanFdBaudrate().getValue() == 2000000
        assert parsed.getCanFdConfig().getPropSeg().getValue() == 10
        assert parsed.getCanXlBaudrate().getValue() == 10000000
        assert parsed.getCanXlConfig().getPropSeg().getValue() == 20
        assert parsed.getCanXlConfigReqs().getMaxNumberOfTimeQuantaPerBit().getValue() == 50

    def test_reader_empty_fields(self, parser):
        element = ET.fromstring("<CAN-XL-PROPS xmlns='%s'><SHORT-NAME>x</SHORT-NAME></CAN-XL-PROPS>" % NS)
        parsed = CanXlProps(None, "x")
        parser.readCanXlProps(element, parsed)
        assert parsed.getCanBaudrate() is None
        assert parsed.getCanConfig() is None
        assert parsed.getCanFdBaudrate() is None
        assert parsed.getCanFdConfig() is None
        assert parsed.getCanXlBaudrate() is None
        assert parsed.getCanXlConfig() is None
        assert parsed.getCanXlConfigReqs() is None

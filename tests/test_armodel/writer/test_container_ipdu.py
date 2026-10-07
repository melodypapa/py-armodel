"""Writer round-trip tests for ContainerIPdu (Table 6.35, p.354).

Serialized through the CONTAINER-I-PDU element (AUTOSAR_00052.xsd l.23024)
and the ARPackage ELEMENTS dispatch.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARPackage
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType, TimeValue
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    ContainedIPduProps,
    ContainerIPdu,
    ContainerIPduHeaderTypeEnum,
    ContainerIPduTriggerEnum,
    RxAcceptContainedIPduEnum,
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


def _with_ns(parent: ET.Element) -> ET.Element:
    return ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))


def _positive(value: int) -> PositiveInteger:
    num = PositiveInteger()
    num.setValue(str(value))
    return num


def _ref(value: str, dest: str) -> RefType:
    ref = RefType()
    ref.setValue(value)
    ref.setDest(dest)
    return ref


class TestWriteContainerIPdu:
    def test_empty(self):
        ipdu = ContainerIPdu(None, "CIP1")
        parent = ET.Element("PARENT")
        ARXMLWriter().writeContainerIPdu(parent, ipdu)

        node = parent.find("CONTAINER-I-PDU")
        assert node is not None
        assert node.find("CONTAINED-I-PDU-TRIGGERING-PROPSS") is None
        assert node.find("CONTAINED-PDU-TRIGGERING-REFS") is None
        assert node.find("CONTAINER-TIMEOUT") is None
        assert node.find("HEADER-TYPE") is None

    def test_full_element_order(self):
        ipdu = ContainerIPdu(None, "CIP1")
        props = ContainedIPduProps()
        ipdu.addContainedIPduTriggeringProps(props)
        ipdu.addContainedPduTriggeringRef(_ref("/Cluster/PT1", "PDU-TRIGGERING"))
        timeout = TimeValue()
        timeout.setValue("0.01")
        ipdu.setContainerTimeout(timeout)
        trigger = ContainerIPduTriggerEnum()
        trigger.setValue(ContainerIPduTriggerEnum.FIRST_CONTAINED_TRIGGER)
        ipdu.setContainerTrigger(trigger)
        header_type = ContainerIPduHeaderTypeEnum()
        header_type.setValue(ContainerIPduHeaderTypeEnum.SHORT_HEADER)
        ipdu.setHeaderType(header_type)
        ipdu.setMinimumRxContainerQueueSize(_positive(4))
        ipdu.setMinimumTxContainerQueueSize(_positive(8))
        rx_accept = RxAcceptContainedIPduEnum()
        rx_accept.setValue(RxAcceptContainedIPduEnum.ACCEPT_CONFIGURED)
        ipdu.setRxAcceptContainedIPdu(rx_accept)
        ipdu.setThresholdSize(_positive(100))
        ipdu.setUnusedBitPattern(_positive(255))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeContainerIPdu(parent, ipdu)

        node = parent.find("CONTAINER-I-PDU")
        tags = [child.tag for child in node]
        assert tags.index("CONTAINED-I-PDU-TRIGGERING-PROPSS") < tags.index("CONTAINED-PDU-TRIGGERING-REFS")
        assert tags.index("CONTAINED-PDU-TRIGGERING-REFS") < tags.index("CONTAINER-TIMEOUT")
        assert tags.index("CONTAINER-TIMEOUT") < tags.index("CONTAINER-TRIGGER")
        assert tags.index("CONTAINER-TRIGGER") < tags.index("HEADER-TYPE")
        assert tags.index("HEADER-TYPE") < tags.index("MINIMUM-RX-CONTAINER-QUEUE-SIZE")
        assert tags.index("MINIMUM-RX-CONTAINER-QUEUE-SIZE") < tags.index("MINIMUM-TX-CONTAINER-QUEUE-SIZE")
        assert tags.index("MINIMUM-TX-CONTAINER-QUEUE-SIZE") < tags.index("RX-ACCEPT-CONTAINED-I-PDU")
        assert tags.index("RX-ACCEPT-CONTAINED-I-PDU") < tags.index("THRESHOLD-SIZE")
        assert tags.index("THRESHOLD-SIZE") < tags.index("UNUSED-BIT-PATTERN")

        assert node.find("CONTAINED-PDU-TRIGGERING-REFS/CONTAINED-PDU-TRIGGERING-REF").text == "/Cluster/PT1"
        assert node.find("CONTAINED-PDU-TRIGGERING-REFS/CONTAINED-PDU-TRIGGERING-REF").get("DEST") == "PDU-TRIGGERING"
        assert node.find("CONTAINER-TRIGGER").text == "FIRST-CONTAINED-TRIGGER"
        assert node.find("HEADER-TYPE").text == "SHORT-HEADER"
        assert node.find("MINIMUM-RX-CONTAINER-QUEUE-SIZE").text == "4"
        assert node.find("RX-ACCEPT-CONTAINED-I-PDU").text == "ACCEPT-CONFIGURED"
        assert node.find("UNUSED-BIT-PATTERN").text == "255"

    def test_round_trip_full(self):
        ipdu = ContainerIPdu(None, "CIP1")
        props = ContainedIPduProps()
        ipdu.addContainedIPduTriggeringProps(props)
        ipdu.addContainedPduTriggeringRef(_ref("/Cluster/PT1", "PDU-TRIGGERING"))
        header_type = ContainerIPduHeaderTypeEnum()
        header_type.setValue(ContainerIPduHeaderTypeEnum.LONG_HEADER)
        ipdu.setHeaderType(header_type)
        ipdu.setThresholdSize(_positive(100))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeContainerIPdu(parent, ipdu)

        reloaded = ContainerIPdu(None, "CIP1")
        ARXMLParser().readContainerIPdu(_with_ns(parent)[0], reloaded)

        assert len(reloaded.getContainedIPduTriggeringProps()) == 1
        assert [ref.getValue() for ref in reloaded.getContainedPduTriggeringRefs()] == ["/Cluster/PT1"]
        assert reloaded.getHeaderType().getValue() == "LONG-HEADER"
        assert reloaded.getThresholdSize().getValue() == 100

    def test_round_trip_via_ar_package_dispatch(self):
        pkg = ARPackage(parent=None, short_name="Pkg")
        ipdu = pkg.createContainerIPdu("CIP1")
        ipdu.addContainedPduTriggeringRef(_ref("/Cluster/PT1", "PDU-TRIGGERING"))
        rx_accept = RxAcceptContainedIPduEnum()
        rx_accept.setValue(RxAcceptContainedIPduEnum.ACCEPT_ALL)
        ipdu.setRxAcceptContainedIPdu(rx_accept)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeARPackageElements(parent, pkg)

        node = parent.find("ELEMENTS/CONTAINER-I-PDU")
        assert node is not None

        reloaded_pkg = ARPackage(parent=None, short_name="Pkg")
        ARXMLParser().readARPackageElements(_with_ns(parent), reloaded_pkg)
        ipdus = reloaded_pkg.getContainerIPdus()
        assert len(ipdus) == 1
        assert ipdus[0].getShortName() == "CIP1"
        assert ipdus[0].getRxAcceptContainedIPdu().getValue() == "ACCEPT-ALL"
        assert [ref.getValue() for ref in ipdus[0].getContainedPduTriggeringRefs()] == ["/Cluster/PT1"]

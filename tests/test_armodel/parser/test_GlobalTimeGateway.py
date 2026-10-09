"""Reader tests for GlobalTimeGateway (Table 9.6, p.861)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import GlobalTimeGateway
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    from armodel.models import AUTOSAR

    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    return ARXMLParser()


class TestReadGlobalTimeGateway:
    def test_read_all_elements(self, parser):
        """
        All three GLOBAL-TIME-GATEWAY group elements plus the Identifiable level (SHORT-NAME, UUID)
        and the trailing VARIATION-POINT are read into the object.
        """
        element = ET.fromstring(
            "<GLOBAL-TIME-GATEWAY xmlns='%s' UUID='4d5e6f7a-8b9c-4abb-ccdd-3f4a5b6c7d8e'>"
            "<SHORT-NAME>gateway1</SHORT-NAME>"
            "<HOST-REF DEST='ECU-INSTANCE'>/ECUs/EcuInstance1</HOST-REF>"
            "<MASTER-REF DEST='GLOBAL-TIME-CAN-MASTER'>/TimeDomains/Domain1/Master</MASTER-REF>"
            "<SLAVE-REF DEST='GLOBAL-TIME-CAN-SLAVE'>/TimeDomains/Domain1/Slave</SLAVE-REF>"
            "<VARIATION-POINT><SHORT-LABEL>vpGateway</SHORT-LABEL></VARIATION-POINT>"
            "</GLOBAL-TIME-GATEWAY>" % NS
        )

        gateway = parser.readGlobalTimeGateway(element, GlobalTimeGateway(None, "gateway1"))

        assert gateway.getShortName() == "gateway1"
        assert gateway.getUuid().getValue() == "4d5e6f7a-8b9c-4abb-ccdd-3f4a5b6c7d8e"
        assert gateway.getHostRef().getValue() == "/ECUs/EcuInstance1"
        assert gateway.getHostRef().getDest() == "ECU-INSTANCE"
        assert gateway.getMasterRef().getValue() == "/TimeDomains/Domain1/Master"
        assert gateway.getMasterRef().getDest() == "GLOBAL-TIME-CAN-MASTER"
        assert gateway.getSlaveRef().getValue() == "/TimeDomains/Domain1/Slave"
        assert gateway.getSlaveRef().getDest() == "GLOBAL-TIME-CAN-SLAVE"
        assert gateway.getVariationPoint().getShortLabel().getValue() == "vpGateway"

    def test_read_empty_element(self, parser):
        """
        A GLOBAL-TIME-GATEWAY element without group content leaves the fields unset.
        """
        element = ET.fromstring("<GLOBAL-TIME-GATEWAY xmlns='%s'></GLOBAL-TIME-GATEWAY>" % NS)

        gateway = parser.readGlobalTimeGateway(element, GlobalTimeGateway(None, "gateway2"))

        assert gateway.getHostRef() is None
        assert gateway.getMasterRef() is None
        assert gateway.getSlaveRef() is None
        assert gateway.getVariationPoint() is None

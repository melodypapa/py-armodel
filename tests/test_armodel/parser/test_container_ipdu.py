"""Reader tests for ContainerIPdu (Table 6.35, p.354).

XML group CONTAINER-I-PDU (AUTOSAR_00052.xsd l.22935): CONTAINED-I-PDU-TRIGGERING-PROPSS
wrapper + CONTAINED-PDU-TRIGGERING-REFS wrapper + 8 optional attributes, after the
inherited I-PDU group. Dispatched from ARPackage ELEMENTS (CONTAINER-I-PDU).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARPackage
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    ContainedIPduProps,
    ContainerIPdu,
)
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _parse(xml: str) -> ET.Element:
    return ET.fromstring(xml)


FULL_XML = (
    """
<CONTAINER-I-PDU xmlns="%s">
    <SHORT-NAME>CIP1</SHORT-NAME>
    <LENGTH>16</LENGTH>
    <CONTAINED-I-PDU-TRIGGERING-PROPSS>
        <CONTAINED-I-PDU-PROPS>
            <COLLECTION-SEMANTICS>QUEUED</COLLECTION-SEMANTICS>
            <HEADER-ID-LONG-HEADER>305419896</HEADER-ID-LONG-HEADER>
        </CONTAINED-I-PDU-PROPS>
        <CONTAINED-I-PDU-PROPS>
            <COLLECTION-SEMANTICS>LAST-IS-BEST</COLLECTION-SEMANTICS>
        </CONTAINED-I-PDU-PROPS>
    </CONTAINED-I-PDU-TRIGGERING-PROPSS>
    <CONTAINED-PDU-TRIGGERING-REFS>
        <CONTAINED-PDU-TRIGGERING-REF DEST="PDU-TRIGGERING">/Cluster/PT1</CONTAINED-PDU-TRIGGERING-REF>
        <CONTAINED-PDU-TRIGGERING-REF DEST="PDU-TRIGGERING">/Cluster/PT2</CONTAINED-PDU-TRIGGERING-REF>
    </CONTAINED-PDU-TRIGGERING-REFS>
    <CONTAINER-TIMEOUT>0.01</CONTAINER-TIMEOUT>
    <CONTAINER-TRIGGER>FIRST-CONTAINED-TRIGGER</CONTAINER-TRIGGER>
    <HEADER-TYPE>SHORT-HEADER</HEADER-TYPE>
    <MINIMUM-RX-CONTAINER-QUEUE-SIZE>4</MINIMUM-RX-CONTAINER-QUEUE-SIZE>
    <MINIMUM-TX-CONTAINER-QUEUE-SIZE>8</MINIMUM-TX-CONTAINER-QUEUE-SIZE>
    <RX-ACCEPT-CONTAINED-I-PDU>ACCEPT-CONFIGURED</RX-ACCEPT-CONTAINED-I-PDU>
    <THRESHOLD-SIZE>100</THRESHOLD-SIZE>
    <UNUSED-BIT-PATTERN>255</UNUSED-BIT-PATTERN>
</CONTAINER-I-PDU>
"""
    % NS
)


class TestReadContainerIPdu:
    def test_read_full(self):
        element = _parse(FULL_XML)
        ipdu = ContainerIPdu(None, "CIP1")
        ARXMLParser().readContainerIPdu(element, ipdu)

        props_list = ipdu.getContainedIPduTriggeringProps()
        assert len(props_list) == 2
        assert isinstance(props_list[0], ContainedIPduProps)
        assert props_list[0].getCollectionSemantics().getValue() == "QUEUED"
        assert props_list[0].getHeaderIdLongHeader().getValue() == 305419896
        assert props_list[1].getCollectionSemantics().getValue() == "LAST-IS-BEST"

        refs = ipdu.getContainedPduTriggeringRefs()
        assert [ref.getValue() for ref in refs] == ["/Cluster/PT1", "/Cluster/PT2"]
        assert refs[0].getDest() == "PDU-TRIGGERING"

        assert ipdu.getContainerTimeout() is not None
        assert ipdu.getContainerTimeout().getValue() == 0.01
        assert ipdu.getContainerTrigger().getValue() == "FIRST-CONTAINED-TRIGGER"
        assert ipdu.getHeaderType().getValue() == "SHORT-HEADER"
        assert ipdu.getMinimumRxContainerQueueSize().getValue() == 4
        assert ipdu.getMinimumTxContainerQueueSize().getValue() == 8
        assert ipdu.getRxAcceptContainedIPdu().getValue() == "ACCEPT-CONFIGURED"
        assert ipdu.getThresholdSize().getValue() == 100
        assert ipdu.getUnusedBitPattern().getValue() == 255

    def test_read_empty(self):
        xml = '<CONTAINER-I-PDU xmlns="%s"><SHORT-NAME>CIP1</SHORT-NAME></CONTAINER-I-PDU>' % NS
        element = _parse(xml)
        ipdu = ContainerIPdu(None, "CIP1")
        ARXMLParser().readContainerIPdu(element, ipdu)

        assert ipdu.getContainedIPduTriggeringProps() == []
        assert ipdu.getContainedPduTriggeringRefs() == []
        assert ipdu.getContainerTimeout() is None
        assert ipdu.getContainerTrigger() is None
        assert ipdu.getHeaderType() is None
        assert ipdu.getMinimumRxContainerQueueSize() is None
        assert ipdu.getMinimumTxContainerQueueSize() is None
        assert ipdu.getRxAcceptContainedIPdu() is None
        assert ipdu.getThresholdSize() is None
        assert ipdu.getUnusedBitPattern() is None

    def test_read_via_ar_package_dispatch(self):
        xml = (
            """
        <AR-PACKAGE xmlns="%s">
            <ELEMENTS>
                <CONTAINER-I-PDU>
                    <SHORT-NAME>CIP1</SHORT-NAME>
                    <HEADER-TYPE>LONG-HEADER</HEADER-TYPE>
                </CONTAINER-I-PDU>
            </ELEMENTS>
        </AR-PACKAGE>
        """
            % NS
        )
        element = _parse(xml)
        parent = ARPackage(parent=None, short_name="Pkg")
        ARXMLParser().readARPackageElements(element, parent)

        ipdus = parent.getContainerIPdus()
        assert len(ipdus) == 1
        assert ipdus[0].getShortName() == "CIP1"
        assert ipdus[0].getHeaderType().getValue() == "LONG-HEADER"

"""Parser tests for ISignalIPdu (Table 6.19, p.342).

Own child set and order per the I-SIGNAL-I-PDU group of AUTOSAR_00052.xsd (l.66972),
sequenced after the PDU and I-PDU groups in the I-SIGNAL-I-PDU complexType
(l.67054). PDU-COUNTERS and PDU-REPLICATIONS carry atp.Status="removed" in the XSD
and are not modeled (Rule 0015). The tests exercise readISignalIPdu, which must
dispatch to readIPdu (Base = IPdu) exactly once for the inherited levels.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
    UnlimitedInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    ContainedIPduProps,
    IPduTiming,
    ISignalIPdu,
    ISignalToIPduMapping,
)
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"

FULL_XML = f"""<I-SIGNAL-I-PDU xmlns='{NS}' UUID='3f4a5b6c-7d8e-49a0-b1c2-3d4e5f6a7b8c'>
    <SHORT-NAME>ISignalIPdu1</SHORT-NAME>
    <HAS-DYNAMIC-LENGTH>true</HAS-DYNAMIC-LENGTH>
    <LENGTH>8</LENGTH>
    <CONTAINED-I-PDU-PROPS>
        <COLLECTION-SEMANTICS>QUEUED</COLLECTION-SEMANTICS>
        <OFFSET>2</OFFSET>
    </CONTAINED-I-PDU-PROPS>
    <I-PDU-TIMING-SPECIFICATIONS>
        <I-PDU-TIMING>
            <MINIMUM-DELAY>0.01</MINIMUM-DELAY>
        </I-PDU-TIMING>
    </I-PDU-TIMING-SPECIFICATIONS>
    <I-SIGNAL-TO-PDU-MAPPINGS>
        <I-SIGNAL-TO-I-PDU-MAPPING>
            <SHORT-NAME>mapping1</SHORT-NAME>
            <START-POSITION>0</START-POSITION>
        </I-SIGNAL-TO-I-PDU-MAPPING>
    </I-SIGNAL-TO-PDU-MAPPINGS>
    <UNUSED-BIT-PATTERN>255</UNUSED-BIT-PATTERN>
</I-SIGNAL-I-PDU>"""


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestReadISignalIPdu:
    def test_read_full(self):
        ipdu = ISignalIPdu(None, "ISignalIPdu1")
        ARXMLParser().readISignalIPdu(ET.fromstring(FULL_XML), ipdu)

        assert ipdu.getShortName() == "ISignalIPdu1"
        assert isinstance(ipdu.getHasDynamicLength(), Boolean)
        assert ipdu.getHasDynamicLength().getValue() is True
        assert isinstance(ipdu.getLength(), UnlimitedInteger)
        assert ipdu.getLength().getValue() == 8

        props = ipdu.getContainedIPduProps()
        assert isinstance(props, ContainedIPduProps)
        assert props.getCollectionSemantics().getValue() == "QUEUED"
        assert props.getOffset().getValue() == 2

        timing = ipdu.getIPduTimingSpecification()
        assert isinstance(timing, IPduTiming)
        assert timing.getMinimumDelay().getValue() == 0.01

        mappings = ipdu.getISignalToPduMappings()
        assert len(mappings) == 1
        mapping = mappings[0]
        assert isinstance(mapping, ISignalToIPduMapping)
        assert mapping.getShortName() == "mapping1"
        assert mapping.getStartPosition().getValue() == 0

        assert isinstance(ipdu.getUnusedBitPattern(), Integer)
        assert ipdu.getUnusedBitPattern().getValue() == 255

    def test_read_minimal(self):
        ipdu = ISignalIPdu(None, "ISignalIPdu1")
        element = ET.fromstring(f"<I-SIGNAL-I-PDU xmlns='{NS}'><SHORT-NAME>ISignalIPdu1</SHORT-NAME></I-SIGNAL-I-PDU>")
        ARXMLParser().readISignalIPdu(element, ipdu)

        assert ipdu.getShortName() == "ISignalIPdu1"
        assert ipdu.getHasDynamicLength() is None
        assert ipdu.getLength() is None
        assert ipdu.getContainedIPduProps() is None
        assert ipdu.getIPduTimingSpecification() is None
        assert ipdu.getISignalToPduMappings() == []
        assert ipdu.getUnusedBitPattern() is None

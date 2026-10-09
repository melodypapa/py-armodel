"""Parser tests for IPdu (Table 6.18, p.341).

Child set and order per the I-PDU group of AUTOSAR_00052.xsd (l.66381), sequenced
after the PDU group in every concrete IPdu complexType. IPdu is abstract: the tests
exercise the reusable readIPdu helper that concrete subclasses (DcmIPdu, NPdu,
SecuredIPdu, ...) call on their own wrapper element.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    UnlimitedInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    ContainedIPduProps,
    IPdu,
)
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


class ConcreteIPdu(IPdu):
    pass


FULL_XML = f"""<I-PDU xmlns='{NS}' UUID='1a2b3c4d-5e6f-47a8-9b0c-1d2e3f4a5b6d'>
    <SHORT-NAME>IPdu1</SHORT-NAME>
    <HAS-DYNAMIC-LENGTH>true</HAS-DYNAMIC-LENGTH>
    <LENGTH>8</LENGTH>
    <CONTAINED-I-PDU-PROPS>
        <COLLECTION-SEMANTICS>QUEUED</COLLECTION-SEMANTICS>
        <HEADER-ID-SHORT-HEADER>4</HEADER-ID-SHORT-HEADER>
        <OFFSET>2</OFFSET>
        <PRIORITY>5</PRIORITY>
    </CONTAINED-I-PDU-PROPS>
</I-PDU>"""


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestReadIPdu:
    def test_read_full(self):
        ipdu = ConcreteIPdu(None, "IPdu1")
        ARXMLParser().readIPdu(ET.fromstring(FULL_XML), ipdu)

        assert ipdu.getShortName() == "IPdu1"
        assert isinstance(ipdu.getHasDynamicLength(), Boolean)
        assert ipdu.getHasDynamicLength().getValue() is True
        assert isinstance(ipdu.getLength(), UnlimitedInteger)
        assert ipdu.getLength().getValue() == 8

        props = ipdu.getContainedIPduProps()
        assert isinstance(props, ContainedIPduProps)
        assert props.getCollectionSemantics().getValue() == "QUEUED"
        assert props.getHeaderIdShortHeader().getValue() == 4
        assert props.getOffset().getValue() == 2
        assert props.getPriority().getValue() == 5

    def test_read_minimal(self):
        ipdu = ConcreteIPdu(None, "IPdu1")
        element = ET.fromstring(f"<I-PDU xmlns='{NS}'><SHORT-NAME>IPdu1</SHORT-NAME></I-PDU>")
        ARXMLParser().readIPdu(element, ipdu)

        assert ipdu.getShortName() == "IPdu1"
        assert ipdu.getHasDynamicLength() is None
        assert ipdu.getLength() is None
        assert ipdu.getContainedIPduProps() is None

"""Parser tests for DataPrototypeInPortInterfaceRef (Table 7.19, p.788).

Table 7.19 (page-split) gives the class two iref attributes:
dataPrototypeInClientServerInterface and dataPrototypeInSenderReceiverInterface.
Wrapper element names per the XSD group DATA-PROTOTYPE-IN-PORT-INTERFACE-REF
(AUTOSAR_00052.xsd): DATA-PROTOTYPE-IN-CLIENT-SERVER-INTERFACE-IREF and
DATA-PROTOTYPE-IN-SENDER-RECEIVER-INTERFACE-IREF.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import (
    DataPrototypeInClientServerInterfaceInstanceRef,
    DataPrototypeInPortInterfaceRef,
    DataPrototypeInSenderReceiverInterfaceInstanceRef,
)
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    AUTOSAR.getInstance().new()
    document = AUTOSAR.getInstance()
    document.setARRelease("R23-11")
    return ARXMLParser()


def _snip(inner: str) -> ET.Element:
    return ET.fromstring(f"<ROOT xmlns='{NS}'>{inner}</ROOT>")


class TestDataPrototypeInPortInterfaceRef:
    def test_read_cs_iref(self, parser):
        xml = """
          <DATA-PROTOTYPE-IN-PORT-INTERFACE-REF>
            <TAG-ID>5</TAG-ID>
            <DATA-PROTOTYPE-IN-CLIENT-SERVER-INTERFACE-IREF>
              <ROOT-DATA-PROTOTYPE-IN-CS-REF DEST="ARGUMENT-DATA-PROTOTYPE">/Cs/Root</ROOT-DATA-PROTOTYPE-IN-CS-REF>
              <TARGET-DATA-PROTOTYPE-IN-CS-REF DEST="DATA-PROTOTYPE">/Cs/MyArg</TARGET-DATA-PROTOTYPE-IN-CS-REF>
            </DATA-PROTOTYPE-IN-CLIENT-SERVER-INTERFACE-IREF>
          </DATA-PROTOTYPE-IN-PORT-INTERFACE-REF>
        """
        root = _snip(xml)
        element = parser.find(root, "DATA-PROTOTYPE-IN-PORT-INTERFACE-REF")
        ref = DataPrototypeInPortInterfaceRef()
        parser.readDataPrototypeInPortInterfaceRef(element, ref)

        assert ref.getTagId() is not None
        assert ref.getTagId().getValue() == 5
        cs_ref = ref.getDataPrototypeInClientServerInterface()
        assert isinstance(cs_ref, DataPrototypeInClientServerInterfaceInstanceRef)
        assert cs_ref.getBaseRef() is None
        assert cs_ref.getRootDataPrototypeInCsRef() is not None
        assert cs_ref.getRootDataPrototypeInCsRef().getValue() == "/Cs/Root"
        assert cs_ref.getTargetDataPrototypeInCsRef() is not None
        assert cs_ref.getTargetDataPrototypeInCsRef().getValue() == "/Cs/MyArg"
        assert ref.getDataPrototypeInSenderReceiverInterface() is None

    def test_read_sr_iref(self, parser):
        xml = """
          <DATA-PROTOTYPE-IN-PORT-INTERFACE-REF>
            <TAG-ID>7</TAG-ID>
            <DATA-PROTOTYPE-IN-SENDER-RECEIVER-INTERFACE-IREF>
              <ROOT-DATA-PROTOTYPE-IN-SR-REF DEST="AUTOSAR-DATA-PROTOTYPE">/Sr/Root</ROOT-DATA-PROTOTYPE-IN-SR-REF>
              <TARGET-DATA-PROTOTYPE-IN-SR-REF DEST="DATA-PROTOTYPE">/Sr/MyVar</TARGET-DATA-PROTOTYPE-IN-SR-REF>
            </DATA-PROTOTYPE-IN-SENDER-RECEIVER-INTERFACE-IREF>
          </DATA-PROTOTYPE-IN-PORT-INTERFACE-REF>
        """
        root = _snip(xml)
        element = parser.find(root, "DATA-PROTOTYPE-IN-PORT-INTERFACE-REF")
        ref = DataPrototypeInPortInterfaceRef()
        parser.readDataPrototypeInPortInterfaceRef(element, ref)

        assert ref.getTagId() is not None
        assert ref.getTagId().getValue() == 7
        sr_ref = ref.getDataPrototypeInSenderReceiverInterface()
        assert isinstance(sr_ref, DataPrototypeInSenderReceiverInterfaceInstanceRef)
        assert sr_ref.getBaseRef() is None
        assert sr_ref.getRootDataPrototypeInSrRef() is not None
        assert sr_ref.getRootDataPrototypeInSrRef().getValue() == "/Sr/Root"
        assert sr_ref.getTargetDataPrototypeInSrRef() is not None
        assert sr_ref.getTargetDataPrototypeInSrRef().getValue() == "/Sr/MyVar"
        assert ref.getDataPrototypeInClientServerInterface() is None

    def test_read_tag_id_only(self, parser):
        root = _snip("<DATA-PROTOTYPE-IN-PORT-INTERFACE-REF><TAG-ID>7</TAG-ID></DATA-PROTOTYPE-IN-PORT-INTERFACE-REF>")
        element = parser.find(root, "DATA-PROTOTYPE-IN-PORT-INTERFACE-REF")
        ref = DataPrototypeInPortInterfaceRef()
        parser.readDataPrototypeInPortInterfaceRef(element, ref)

        assert ref.getTagId() is not None
        assert ref.getTagId().getValue() == 7
        assert ref.getDataPrototypeInClientServerInterface() is None
        assert ref.getDataPrototypeInSenderReceiverInterface() is None

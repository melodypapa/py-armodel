"""Parser tests for DataPrototypeInSenderReceiverInterfaceInstanceRef (Table 7.20, p.788).

Inner element names per the XSD group DATA-PROTOTYPE-IN-SENDER-RECEIVER-INTERFACE-INSTANCE-REF
(AUTOSAR_00052.xsd): ROOT-DATA-PROTOTYPE-IN-SR-REF, CONTEXT-DATA-PROTOTYPE-IN-SR-REF (0..*,
flat -- no wrapper element) and TARGET-DATA-PROTOTYPE-IN-SR-REF. The `base` association is
atpDerived (XSD: "Association <<atpDerived>>base skipped") -- no XML element.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import DataPrototypeInSenderReceiverInterfaceInstanceRef
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


class TestDataPrototypeInSenderReceiverInterfaceInstanceRef:
    def test_read_full_iref(self, parser):
        xml = """
          <DATA-PROTOTYPE-IN-SENDER-RECEIVER-INTERFACE-IREF>
            <ROOT-DATA-PROTOTYPE-IN-SR-REF DEST="AUTOSAR-DATA-PROTOTYPE">/Sr/Root</ROOT-DATA-PROTOTYPE-IN-SR-REF>
            <CONTEXT-DATA-PROTOTYPE-IN-SR-REF DEST="APPLICATION-RECORD-ELEMENT">/Sr/Root/RecElem</CONTEXT-DATA-PROTOTYPE-IN-SR-REF>
            <CONTEXT-DATA-PROTOTYPE-IN-SR-REF DEST="APPLICATION-ARRAY-ELEMENT">/Sr/Root/RecElem/ArrElem</CONTEXT-DATA-PROTOTYPE-IN-SR-REF>
            <TARGET-DATA-PROTOTYPE-IN-SR-REF DEST="DATA-PROTOTYPE">/Sr/MyVar</TARGET-DATA-PROTOTYPE-IN-SR-REF>
          </DATA-PROTOTYPE-IN-SENDER-RECEIVER-INTERFACE-IREF>
        """
        root = _snip(xml)
        element = parser.find(root, "DATA-PROTOTYPE-IN-SENDER-RECEIVER-INTERFACE-IREF")
        iref = DataPrototypeInSenderReceiverInterfaceInstanceRef()
        parser.readDataPrototypeInSenderReceiverInterfaceInstanceRef(element, iref)

        root_ref = iref.getRootDataPrototypeInSrRef()
        assert root_ref is not None
        assert root_ref.getValue() == "/Sr/Root"
        assert root_ref.getDest() == "AUTOSAR-DATA-PROTOTYPE"

        ctx_refs = iref.getContextDataPrototypeInSrRefs()
        assert len(ctx_refs) == 2
        assert ctx_refs[0].getValue() == "/Sr/Root/RecElem"
        assert ctx_refs[0].getDest() == "APPLICATION-RECORD-ELEMENT"
        assert ctx_refs[1].getValue() == "/Sr/Root/RecElem/ArrElem"
        assert ctx_refs[1].getDest() == "APPLICATION-ARRAY-ELEMENT"

        target_ref = iref.getTargetDataPrototypeInSrRef()
        assert target_ref is not None
        assert target_ref.getValue() == "/Sr/MyVar"
        assert target_ref.getDest() == "DATA-PROTOTYPE"

    def test_read_empty_iref(self, parser):
        root = _snip("<DATA-PROTOTYPE-IN-SENDER-RECEIVER-INTERFACE-IREF/>")
        element = parser.find(root, "DATA-PROTOTYPE-IN-SENDER-RECEIVER-INTERFACE-IREF")
        iref = DataPrototypeInSenderReceiverInterfaceInstanceRef()
        parser.readDataPrototypeInSenderReceiverInterfaceInstanceRef(element, iref)

        assert iref.getBaseRef() is None
        assert iref.getRootDataPrototypeInSrRef() is None
        assert iref.getContextDataPrototypeInSrRefs() == []
        assert iref.getTargetDataPrototypeInSrRef() is None

"""Parser tests for DataPrototypeInClientServerInterfaceInstanceRef (Table 7.21, p.788).

Inner element names per the XSD group DATA-PROTOTYPE-IN-CLIENT-SERVER-INTERFACE-INSTANCE-REF
(AUTOSAR_00052.xsd): ROOT-DATA-PROTOTYPE-IN-CS-REF, CONTEXT-DATA-PROTOTYPE-IN-CS-REF (0..*,
flat -- no wrapper element) and TARGET-DATA-PROTOTYPE-IN-CS-REF. The `base` association is
atpDerived (XSD: "Association <<atpDerived>>base skipped") -- no XML element.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import DataPrototypeInClientServerInterfaceInstanceRef
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


class TestDataPrototypeInClientServerInterfaceInstanceRef:
    def test_read_full_iref(self, parser):
        xml = """
          <DATA-PROTOTYPE-IN-CLIENT-SERVER-INTERFACE-IREF>
            <ROOT-DATA-PROTOTYPE-IN-CS-REF DEST="ARGUMENT-DATA-PROTOTYPE">/Cs/Root</ROOT-DATA-PROTOTYPE-IN-CS-REF>
            <CONTEXT-DATA-PROTOTYPE-IN-CS-REF DEST="APPLICATION-RECORD-ELEMENT">/Cs/Root/RecElem</CONTEXT-DATA-PROTOTYPE-IN-CS-REF>
            <CONTEXT-DATA-PROTOTYPE-IN-CS-REF DEST="APPLICATION-ARRAY-ELEMENT">/Cs/Root/RecElem/ArrElem</CONTEXT-DATA-PROTOTYPE-IN-CS-REF>
            <TARGET-DATA-PROTOTYPE-IN-CS-REF DEST="DATA-PROTOTYPE">/Cs/MyArg</TARGET-DATA-PROTOTYPE-IN-CS-REF>
          </DATA-PROTOTYPE-IN-CLIENT-SERVER-INTERFACE-IREF>
        """
        root = _snip(xml)
        element = parser.find(root, "DATA-PROTOTYPE-IN-CLIENT-SERVER-INTERFACE-IREF")
        iref = DataPrototypeInClientServerInterfaceInstanceRef()
        parser.readDataPrototypeInClientServerInterfaceInstanceRef(element, iref)

        root_ref = iref.getRootDataPrototypeInCsRef()
        assert root_ref is not None
        assert root_ref.getValue() == "/Cs/Root"
        assert root_ref.getDest() == "ARGUMENT-DATA-PROTOTYPE"

        ctx_refs = iref.getContextDataPrototypeInCsRefs()
        assert len(ctx_refs) == 2
        assert ctx_refs[0].getValue() == "/Cs/Root/RecElem"
        assert ctx_refs[0].getDest() == "APPLICATION-RECORD-ELEMENT"
        assert ctx_refs[1].getValue() == "/Cs/Root/RecElem/ArrElem"
        assert ctx_refs[1].getDest() == "APPLICATION-ARRAY-ELEMENT"

        target_ref = iref.getTargetDataPrototypeInCsRef()
        assert target_ref is not None
        assert target_ref.getValue() == "/Cs/MyArg"
        assert target_ref.getDest() == "DATA-PROTOTYPE"

    def test_read_empty_iref(self, parser):
        root = _snip("<DATA-PROTOTYPE-IN-CLIENT-SERVER-INTERFACE-IREF/>")
        element = parser.find(root, "DATA-PROTOTYPE-IN-CLIENT-SERVER-INTERFACE-IREF")
        iref = DataPrototypeInClientServerInterfaceInstanceRef()
        parser.readDataPrototypeInClientServerInterfaceInstanceRef(element, iref)

        assert iref.getBaseRef() is None
        assert iref.getRootDataPrototypeInCsRef() is None
        assert iref.getContextDataPrototypeInCsRefs() == []
        assert iref.getTargetDataPrototypeInCsRef() is None

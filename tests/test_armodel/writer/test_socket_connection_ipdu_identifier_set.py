"""Writer round-trip tests for SocketConnectionIpduIdentifierSet (R23-11 CP_TPS_SystemTemplate, Table 6.164, p.490).

Aggregated by ARPackage.element - the ARPackage ELEMENTS choice serializes the FibexElement
subclass. SoConIPduIdentifier (Table 6.163, synced) gets real child field-value coverage.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    RefType,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import (
    PduCollectionSemanticsEnum,
    PduCollectionTriggerEnum,
    SocketConnectionIpduIdentifierSet,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _fill_identifier(identifier, header_id):
    identifier.setHeaderId(PositiveInteger().setValue(str(header_id)))
    identifier.setPduCollectionPduTimeout(TimeValue().setValue("0.5"))
    identifier.setPduCollectionSemantics(PduCollectionSemanticsEnum().setValue(PduCollectionSemanticsEnum.QUEUED))
    identifier.setPduCollectionTrigger(PduCollectionTriggerEnum().setValue(PduCollectionTriggerEnum.ALWAYS))
    ref = RefType()
    ref.setDest("PDU-TRIGGERING")
    ref.setValue("/PduTriggerings/%s" % identifier.getShortName())
    identifier.setPduTriggeringRef(ref)
    return identifier


def _new_set():
    identifier_set = SocketConnectionIpduIdentifierSet(None, "IpduSet")
    identifier1 = identifier_set.createIPduIdentifier("ipdu_id1")
    _fill_identifier(identifier1, 4)
    identifier2 = identifier_set.createIPduIdentifier("ipdu_id2")
    _fill_identifier(identifier2, 8)
    return identifier_set


def _namespaced(element: ET.Element) -> ET.Element:
    inner = ET.tostring(element).decode("utf-8")
    return ET.fromstring(inner.replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))


class TestWriteSocketConnectionIpduIdentifierSet:
    def test_write_all_attrs(self):
        package = AUTOSAR.getInstance().createARPackage("Pkg")
        package.addReferrableElement(_new_set())
        parent = ET.Element("PARENT")
        ARXMLWriter().writeARPackageElements(parent, package)

        node = parent.find("ELEMENTS/SOCKET-CONNECTION-IPDU-IDENTIFIER-SET")
        assert node is not None
        assert node.find("SHORT-NAME").text == "IpduSet"
        identifiers = node.findall("I-PDU-IDENTIFIERS/SO-CON-I-PDU-IDENTIFIER")
        assert len(identifiers) == 2
        assert identifiers[0].find("SHORT-NAME").text == "ipdu_id1"
        assert identifiers[0].findtext("HEADER-ID") == "4"
        assert identifiers[0].findtext("PDU-COLLECTION-SEMANTICS") == "QUEUED"
        assert identifiers[0].findtext("PDU-COLLECTION-TRIGGER") == "ALWAYS"
        assert identifiers[0].findtext("PDU-TRIGGERING-REF") == "/PduTriggerings/ipdu_id1"
        assert identifiers[1].find("SHORT-NAME").text == "ipdu_id2"
        assert identifiers[1].findtext("HEADER-ID") == "8"

    def test_write_empty_omits_wrapper(self):
        package = AUTOSAR.getInstance().createARPackage("Pkg")
        package.addReferrableElement(SocketConnectionIpduIdentifierSet(None, "EmptySet"))
        parent = ET.Element("PARENT")
        ARXMLWriter().writeARPackageElements(parent, package)

        node = parent.find("ELEMENTS/SOCKET-CONNECTION-IPDU-IDENTIFIER-SET")
        assert node is not None
        assert node.find("I-PDU-IDENTIFIERS") is None

    def test_round_trip_preserves_child_field_values(self):
        writer = ARXMLWriter()
        parser = ARXMLParser()
        package = AUTOSAR.getInstance().createARPackage("Pkg")
        package.addReferrableElement(_new_set())
        parent = ET.Element("PARENT")
        writer.writeARPackageElements(parent, package)
        root = _namespaced(parent)

        reloaded_package = AUTOSAR.getInstance().createARPackage("Pkg2")
        parser.readARPackageElements(root, reloaded_package)

        identifier_set = reloaded_package.getReferrableElement("IpduSet", SocketConnectionIpduIdentifierSet)
        assert isinstance(identifier_set, SocketConnectionIpduIdentifierSet)
        identifiers = identifier_set.getIPduIdentifiers()
        assert len(identifiers) == 2
        assert identifiers[0].getShortName() == "ipdu_id1"
        assert identifiers[0].getHeaderId().getValue() == 4
        assert identifiers[0].getPduCollectionPduTimeout().getValue() == 0.5
        assert identifiers[0].getPduCollectionSemantics().getValue() == PduCollectionSemanticsEnum.QUEUED
        assert identifiers[0].getPduCollectionTrigger().getValue() == PduCollectionTriggerEnum.ALWAYS
        assert identifiers[0].getPduTriggeringRef().getValue() == "/PduTriggerings/ipdu_id1"
        assert identifiers[1].getShortName() == "ipdu_id2"
        assert identifiers[1].getHeaderId().getValue() == 8

"""Reader tests for SocketConnectionIpduIdentifierSet (R23-11 CP_TPS_SystemTemplate, Table 6.164, p.490).

XSD group SOCKET-CONNECTION-IPDU-IDENTIFIER-SET (AUTOSAR_00052.xsd l.108469): the
I-PDU-IDENTIFIERS wrapper aggregates SO-CON-I-PDU-IDENTIFIER children. Aggregated by
ARPackage.element - the ARPackage ELEMENTS choice instantiates the ARElement subclass.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import (
    SocketConnectionIpduIdentifierSet,
    SoConIPduIdentifier,
)
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    AUTOSAR.getInstance().new()
    return ARXMLParser()


def test_read_socket_connection_ipdu_identifier_set(parser):
    root = ET.fromstring(
        "<ROOT xmlns='{ns}'>"
        "<ELEMENTS>"
        "<SOCKET-CONNECTION-IPDU-IDENTIFIER-SET>"
        "<SHORT-NAME>IpduSet</SHORT-NAME>"
        "<I-PDU-IDENTIFIERS>"
        "<SO-CON-I-PDU-IDENTIFIER>"
        "<SHORT-NAME>ipdu_id1</SHORT-NAME>"
        "<HEADER-ID>4</HEADER-ID>"
        "<PDU-COLLECTION-SEMANTICS>QUEUED</PDU-COLLECTION-SEMANTICS>"
        "</SO-CON-I-PDU-IDENTIFIER>"
        "<SO-CON-I-PDU-IDENTIFIER>"
        "<SHORT-NAME>ipdu_id2</SHORT-NAME>"
        "<HEADER-ID>8</HEADER-ID>"
        "</SO-CON-I-PDU-IDENTIFIER>"
        "</I-PDU-IDENTIFIERS>"
        "</SOCKET-CONNECTION-IPDU-IDENTIFIER-SET>"
        "</ELEMENTS>"
        "</ROOT>".format(ns=NS)
    )
    package = AUTOSAR.getInstance().createARPackage("Pkg")
    parser.readARPackageElements(root, package)

    identifier_set = package.getReferrableElement("IpduSet", SocketConnectionIpduIdentifierSet)
    assert isinstance(identifier_set, SocketConnectionIpduIdentifierSet)
    identifiers = identifier_set.getIPduIdentifiers()
    assert len(identifiers) == 2
    assert all(isinstance(i, SoConIPduIdentifier) for i in identifiers)
    assert identifiers[0].getShortName() == "ipdu_id1"
    assert identifiers[0].getHeaderId().getValue() == 4
    assert identifiers[0].getPduCollectionSemantics().getValue() == "QUEUED"
    assert identifiers[1].getShortName() == "ipdu_id2"
    assert identifiers[1].getHeaderId().getValue() == 8


def test_read_empty_set(parser):
    root = ET.fromstring(
        "<ROOT xmlns='{ns}'>"
        "<ELEMENTS>"
        "<SOCKET-CONNECTION-IPDU-IDENTIFIER-SET>"
        "<SHORT-NAME>EmptySet</SHORT-NAME>"
        "</SOCKET-CONNECTION-IPDU-IDENTIFIER-SET>"
        "</ELEMENTS>"
        "</ROOT>".format(ns=NS)
    )
    package = AUTOSAR.getInstance().createARPackage("Pkg")
    parser.readARPackageElements(root, package)

    identifier_set = package.getReferrableElement("EmptySet", SocketConnectionIpduIdentifierSet)
    assert isinstance(identifier_set, SocketConnectionIpduIdentifierSet)
    assert identifier_set.getIPduIdentifiers() == []

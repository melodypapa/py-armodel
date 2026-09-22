"""Parser tests for IdsPlatformInstantiation (AUTOSAR_FO_TPS_SecurityExtractTemplate, Table B.13, p.63).

The abstract class owns the reusable readIdsPlatformInstantiation helper that the
concrete IdsmModuleInstantiation calls; the IDS-PLATFORM-INSTANTIATION group
(AUTOSAR_00052.xsd l.69551) holds NETWORK-INTERFACE-REFS then TIME-BASES.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.IntrusionDetectionSystem import (
    IdsmModuleInstantiation,
)
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _new_instance() -> IdsmModuleInstantiation:
    package = AUTOSAR.getInstance().createARPackage("IdsM")
    return IdsmModuleInstantiation(package, "IdsmInst")


def test_read_ids_platform_instantiation_full():
    element = ET.fromstring(
        "<IDS-PLATFORM-INSTANTIATION xmlns='%s'>"
        "<SHORT-NAME>IdsmInst</SHORT-NAME>"
        "<NETWORK-INTERFACE-REFS>"
        "<NETWORK-INTERFACE-REF DEST='PLATFORM-MODULE-ETHERNET-ENDPOINT-CONFIGURATION'>/Pkg/Cfg1</NETWORK-INTERFACE-REF>"
        "<NETWORK-INTERFACE-REF DEST='IDSM-MODULE-INSTANTIATION'>/Pkg/Cfg2</NETWORK-INTERFACE-REF>"
        "</NETWORK-INTERFACE-REFS>"
        "<TIME-BASES>"
        "<TIME-BASE-RESOURCE-REF-CONDITIONAL>"
        "<TIME-BASE-RESOURCE-REF DEST='TIME-BASE-RESOURCE'>/Pkg/TimeBase</TIME-BASE-RESOURCE-REF>"
        "</TIME-BASE-RESOURCE-REF-CONDITIONAL>"
        "</TIME-BASES>"
        "</IDS-PLATFORM-INSTANTIATION>" % NS
    )
    instance = _new_instance()
    ARXMLParser().readIdsPlatformInstantiation(element, instance)

    refs = instance.getNetworkInterfaceRefs()
    assert len(refs) == 2
    assert refs[0].getValue() == "/Pkg/Cfg1"
    assert refs[0].getDest() == "PLATFORM-MODULE-ETHERNET-ENDPOINT-CONFIGURATION"
    assert refs[1].getValue() == "/Pkg/Cfg2"
    assert refs[1].getDest() == "IDSM-MODULE-INSTANTIATION"
    assert instance.getTimeBaseRef().getValue() == "/Pkg/TimeBase"
    assert instance.getTimeBaseRef().getDest() == "TIME-BASE-RESOURCE"


def test_read_ids_platform_instantiation_empty():
    element = ET.fromstring("<IDS-PLATFORM-INSTANTIATION xmlns='%s'><SHORT-NAME>IdsmInst</SHORT-NAME></IDS-PLATFORM-INSTANTIATION>" % NS)
    instance = _new_instance()
    ARXMLParser().readIdsPlatformInstantiation(element, instance)

    assert instance.getNetworkInterfaceRefs() == []
    assert instance.getTimeBaseRef() is None

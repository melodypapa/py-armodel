"""Parser tests for IdsmModuleInstantiation (AUTOSAR_FO_TPS_SecurityExtractTemplate, Table B.14, p.63).

Table B.14 lists no Attribute rows; the readIdsmModuleInstantiation handler
forwards to the inherited IdsPlatformInstantiation coverage and the XSD
complexType (AUTOSAR_00052.xsd l.69915) carries the Identifiable + base-chain
groups only.
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


def test_read_idsm_module_instantiation_inherited_members():
    element = ET.fromstring(
        "<IDSM-MODULE-INSTANTIATION xmlns='%s'>"
        "<SHORT-NAME>IdsmInst</SHORT-NAME>"
        "<NETWORK-INTERFACE-REFS>"
        "<NETWORK-INTERFACE-REF DEST='PLATFORM-MODULE-ETHERNET-ENDPOINT-CONFIGURATION'>/Pkg/Cfg1</NETWORK-INTERFACE-REF>"
        "</NETWORK-INTERFACE-REFS>"
        "<TIME-BASES>"
        "<TIME-BASE-RESOURCE-REF-CONDITIONAL>"
        "<TIME-BASE-RESOURCE-REF DEST='TIME-BASE-RESOURCE'>/Pkg/TimeBase</TIME-BASE-RESOURCE-REF>"
        "</TIME-BASE-RESOURCE-REF-CONDITIONAL>"
        "</TIME-BASES>"
        "</IDSM-MODULE-INSTANTIATION>" % NS
    )
    instance = _new_instance()
    ARXMLParser().readIdsmModuleInstantiation(element, instance)

    assert instance.getShortName() == "IdsmInst"
    refs = instance.getNetworkInterfaceRefs()
    assert len(refs) == 1
    assert refs[0].getValue() == "/Pkg/Cfg1"
    assert instance.getTimeBaseRef().getValue() == "/Pkg/TimeBase"


def test_read_idsm_module_instantiation_empty():
    element = ET.fromstring("<IDSM-MODULE-INSTANTIATION xmlns='%s'><SHORT-NAME>IdsmInst</SHORT-NAME></IDSM-MODULE-INSTANTIATION>" % NS)
    instance = _new_instance()
    ARXMLParser().readIdsmModuleInstantiation(element, instance)

    assert instance.getNetworkInterfaceRefs() == []
    assert instance.getTimeBaseRef() is None

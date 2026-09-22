"""Writer round-trip tests for IdsPlatformInstantiation (AUTOSAR_FO_TPS_SecurityExtractTemplate, Table B.13, p.63).

The abstract class owns the reusable writeIdsPlatformInstantiation helper that
the concrete IdsmModuleInstantiation calls; element order per XSD group
IDS-PLATFORM-INSTANTIATION (AUTOSAR_00052.xsd l.69551): NETWORK-INTERFACE-REFS,
TIME-BASES (the atpSplitable TIME-BASES wrapper nests
TIME-BASE-RESOURCE-REF-CONDITIONAL / TIME-BASE-RESOURCE-REF).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.IntrusionDetectionSystem import (
    IdsmModuleInstantiation,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _ref(value: str, dest: str) -> RefType:
    ref = RefType()
    ref.setValue(value)
    ref.setDest(dest)
    return ref


def _new_instance() -> IdsmModuleInstantiation:
    package = AUTOSAR.getInstance().createARPackage("IdsM")
    instance = IdsmModuleInstantiation(package, "IdsmInst")
    instance.addNetworkInterfaceRef(_ref("/Pkg/Cfg1", "PLATFORM-MODULE-ETHERNET-ENDPOINT-CONFIGURATION"))
    instance.addNetworkInterfaceRef(_ref("/Pkg/Cfg2", "IDSM-MODULE-INSTANTIATION"))
    instance.setTimeBaseRef(_ref("/Pkg/TimeBase", "TIME-BASE-RESOURCE"))
    return instance


def test_write_ids_platform_instantiation_content_order():
    parent = ET.Element("IDSM-MODULE-INSTANTIATION")
    ARXMLWriter().writeIdsPlatformInstantiation(parent, _new_instance())

    assert parent.find("SHORT-NAME").text == "IdsmInst"
    children = [child.tag for child in parent]
    assert children == ["SHORT-NAME", "NETWORK-INTERFACE-REFS", "TIME-BASES"]
    refs = parent.findall("NETWORK-INTERFACE-REFS/NETWORK-INTERFACE-REF")
    assert len(refs) == 2
    assert refs[0].text == "/Pkg/Cfg1"
    assert refs[0].attrib["DEST"] == "PLATFORM-MODULE-ETHERNET-ENDPOINT-CONFIGURATION"
    assert refs[1].text == "/Pkg/Cfg2"
    assert refs[1].attrib["DEST"] == "IDSM-MODULE-INSTANTIATION"
    conditional = parent.find("TIME-BASES/TIME-BASE-RESOURCE-REF-CONDITIONAL")
    assert conditional is not None
    time_base_ref = conditional.find("TIME-BASE-RESOURCE-REF")
    assert time_base_ref.text == "/Pkg/TimeBase"
    assert time_base_ref.attrib["DEST"] == "TIME-BASE-RESOURCE"


def test_write_ids_platform_instantiation_empty_omits_optional_tags():
    package = AUTOSAR.getInstance().createARPackage("IdsM")
    instance = IdsmModuleInstantiation(package, "EmptyInst")
    parent = ET.Element("IDSM-MODULE-INSTANTIATION")
    ARXMLWriter().writeIdsPlatformInstantiation(parent, instance)

    assert [child.tag for child in parent] == ["SHORT-NAME"]


def test_round_trip_preserves_all_values():
    parent = ET.Element("IDSM-MODULE-INSTANTIATION")
    ARXMLWriter().writeIdsPlatformInstantiation(parent, _new_instance())
    inner = ET.tostring(parent).decode("utf-8")
    root = ET.fromstring(inner.replace("<IDSM-MODULE-INSTANTIATION>", "<IDSM-MODULE-INSTANTIATION xmlns='%s'>" % NS, 1))

    package = AUTOSAR.getInstance().createARPackage("IdsM")
    parsed = IdsmModuleInstantiation(package, "IdsmInst")
    ARXMLParser().readIdsPlatformInstantiation(root, parsed)

    refs = parsed.getNetworkInterfaceRefs()
    assert len(refs) == 2
    assert refs[0].getValue() == "/Pkg/Cfg1"
    assert refs[0].getDest() == "PLATFORM-MODULE-ETHERNET-ENDPOINT-CONFIGURATION"
    assert refs[1].getValue() == "/Pkg/Cfg2"
    assert refs[1].getDest() == "IDSM-MODULE-INSTANTIATION"
    assert parsed.getTimeBaseRef().getValue() == "/Pkg/TimeBase"
    assert parsed.getTimeBaseRef().getDest() == "TIME-BASE-RESOURCE"

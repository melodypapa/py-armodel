"""Writer round-trip tests for IdsmModuleInstantiation (AUTOSAR_FO_TPS_SecurityExtractTemplate, Table B.14, p.63).

Table B.14 lists no Attribute rows; the writeIdsmModuleInstantiation helper
emits the IDSM-MODULE-INSTANTIATION element with the inherited
IdsPlatformInstantiation content only (AUTOSAR_00052.xsd l.69915).
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
    instance.setTimeBaseRef(_ref("/Pkg/TimeBase", "TIME-BASE-RESOURCE"))
    return instance


def test_write_idsm_module_instantiation_xml():
    parent = ET.Element("ROOT")
    ARXMLWriter().writeIdsmModuleInstantiation(parent, _new_instance())

    node = parent.find("IDSM-MODULE-INSTANTIATION")
    assert node is not None
    assert node.find("SHORT-NAME").text == "IdsmInst"
    children = [child.tag for child in node]
    assert children == ["SHORT-NAME", "NETWORK-INTERFACE-REFS", "TIME-BASES"]
    ref = node.find("NETWORK-INTERFACE-REFS/NETWORK-INTERFACE-REF")
    assert ref.text == "/Pkg/Cfg1"
    assert ref.attrib["DEST"] == "PLATFORM-MODULE-ETHERNET-ENDPOINT-CONFIGURATION"


def test_round_trip_preserves_all_values():
    parent = ET.Element("ROOT")
    ARXMLWriter().writeIdsmModuleInstantiation(parent, _new_instance())
    inner = ET.tostring(parent).decode("utf-8")
    root = ET.fromstring(inner.replace("<ROOT>", "<ROOT xmlns='%s'>" % NS, 1))

    package = AUTOSAR.getInstance().createARPackage("IdsM")
    parsed = IdsmModuleInstantiation(package, "IdsmInst")
    ARXMLParser().readIdsmModuleInstantiation(root[0], parsed)

    assert parsed.getShortName() == "IdsmInst"
    refs = parsed.getNetworkInterfaceRefs()
    assert len(refs) == 1
    assert refs[0].getValue() == "/Pkg/Cfg1"
    assert refs[0].getDest() == "PLATFORM-MODULE-ETHERNET-ENDPOINT-CONFIGURATION"
    assert parsed.getTimeBaseRef().getValue() == "/Pkg/TimeBase"
    assert parsed.getTimeBaseRef().getDest() == "TIME-BASE-RESOURCE"

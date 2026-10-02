"""
Tests for writing EcucContainerDef content (Table 2.3, p.37, abstract — via
concrete subclass).

XSD group ECUC-CONTAINER-DEF (AUTOSAR_00052.xsd) element order:
DESTINATION-URI-REFS, MULTIPLICITY-CONFIG-CLASSES, ORIGIN,
POST-BUILD-VARIANT-MULTIPLICITY, REQUIRES-INDEX (POST-BUILD-CHANGEABLE is
atp.Status="removed" and not modeled).

Round-trip counterpart: tests/test_armodel/parser/test_ecuc_container_def.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucDestinationUriDefRefType, EcucMultiplicityConfigurationClass, EcucParamConfContainerDef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, String
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteEcucContainerDef:
    """Tests for writeEcucContainerDef — own element field values (Table 2.3)."""

    def _make_obj(self):
        return EcucParamConfContainerDef(AUTOSAR.getInstance().createARPackage("Pkg_W"), "Container1")

    def test_write_empty(self):
        """Test that a container without attributes emits no own-field elements."""
        element = ET.Element("ECUC-PARAM-CONF-CONTAINER-DEF")
        ARXMLWriter().writeEcucContainerDef(element, self._make_obj())

        assert element.find("SHORT-NAME").text == "Container1"
        assert element.find("DESTINATION-URI-REFS") is None
        assert element.find("MULTIPLICITY-CONFIG-CLASSES") is None
        assert element.find("ORIGIN") is None
        assert element.find("POST-BUILD-VARIANT-MULTIPLICITY") is None
        assert element.find("REQUIRES-INDEX") is None

    def test_write_fields_in_xsd_order(self):
        """Test that all attributes are emitted in XSD order with the spec values."""
        container = self._make_obj()
        uri_ref = EcucDestinationUriDefRefType()
        uri_ref.setDest("ECUC-DESTINATION-URI-DEF")
        uri_ref.setValue("/AUTOSAR/UriDefs/Uri1")
        container.addDestinationUriRef(uri_ref)
        container.addMultiplicityConfigClass(EcucMultiplicityConfigurationClass())
        container.setOrigin(String().setValue("AUTOSAR Ecuc Definition Collection"))
        container.setPostBuildVariantMultiplicity(Boolean().setValue(True))
        container.setRequiresIndex(Boolean().setValue(False))

        element = ET.Element("ECUC-PARAM-CONF-CONTAINER-DEF")
        ARXMLWriter().writeEcucContainerDef(element, container)

        tags = [c.tag for c in element]
        assert tags == ["SHORT-NAME", "DESTINATION-URI-REFS", "MULTIPLICITY-CONFIG-CLASSES", "ORIGIN", "POST-BUILD-VARIANT-MULTIPLICITY", "REQUIRES-INDEX"]
        uri_ref_element = element.find("DESTINATION-URI-REFS/DESTINATION-URI-REF")
        assert uri_ref_element.text == "/AUTOSAR/UriDefs/Uri1"
        assert uri_ref_element.attrib["DEST"] == "ECUC-DESTINATION-URI-DEF"
        assert len(element.findall("MULTIPLICITY-CONFIG-CLASSES/ECUC-MULTIPLICITY-CONFIGURATION-CLASS")) == 1
        assert element.find("ORIGIN").text == "AUTOSAR Ecuc Definition Collection"
        assert element.find("POST-BUILD-VARIANT-MULTIPLICITY").text == "true"
        assert element.find("REQUIRES-INDEX").text == "false"

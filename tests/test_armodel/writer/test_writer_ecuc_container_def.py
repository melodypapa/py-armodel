"""
Tests for writing ECUC-CONTAINER-DEF content —
EcucContainerDef, Table 2.3 (p.37, R23-11).

XSD group ECUC-CONTAINER-DEF (AUTOSAR_00052.xsd l.51599) element order:
DESTINATION-URI-REFS, MULTIPLICITY-CONFIG-CLASSES, ORIGIN,
POST-BUILD-VARIANT-MULTIPLICITY, REQUIRES-INDEX
(POST-BUILD-CHANGEABLE carries atp.Status="removed" and is not modeled).

Round-trip counterpart: tests/test_armodel/parser/test_ecuc_container_def.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import (
    EcucConfigurationClassEnum,
    EcucConfigurationVariantEnum,
    EcucContainerDef,
    EcucDestinationUriDefRefType,
    EcucMultiplicityConfigurationClass,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, String
from armodel.writer.arxml_writer import ARXMLWriter


class _Concrete(EcucContainerDef):
    pass


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteEcucContainerDef:
    """Tests for writeEcucContainerDef — own element field values (Table 2.3)."""

    def _make(self):
        return _Concrete(AUTOSAR.getInstance().createARPackage("Pkg_W"), "Holder")

    def test_write_empty(self):
        """Test that an EcucContainerDef without own attributes emits only the inherited content."""
        element = ET.Element("ECUC-PARAM-CONF-CONTAINER-DEF")
        ARXMLWriter().writeEcucContainerDef(element, self._make())

        assert element.find("SHORT-NAME").text == "Holder"
        assert element.find("DESTINATION-URI-REFS") is None
        assert element.find("MULTIPLICITY-CONFIG-CLASSES") is None
        assert element.find("ORIGIN") is None
        assert element.find("POST-BUILD-VARIANT-MULTIPLICITY") is None
        assert element.find("REQUIRES-INDEX") is None

    def test_write_fields_in_xsd_order(self):
        """Test that all attributes are emitted in XSD group order with the spec values."""
        holder = self._make()
        holder.addDestinationUriRef(EcucDestinationUriDefRefType().setValue("/EcucDestinationUriDefs/Uri1").setDest("ECUC-DESTINATION-URI-DEF"))
        cfg_class = EcucMultiplicityConfigurationClass()
        cfg_class.setConfigClass(EcucConfigurationClassEnum().setValue(EcucConfigurationClassEnum.POST_BUILD))
        cfg_class.setConfigVariant(EcucConfigurationVariantEnum().setValue(EcucConfigurationVariantEnum.VARIANT_POST_BUILD))
        holder.addMultiplicityConfigClass(cfg_class)
        origin = String()
        origin.setValue("VENDOR")
        holder.setOrigin(origin)
        pbvm = Boolean()
        pbvm.setValue(True)
        holder.setPostBuildVariantMultiplicity(pbvm)
        ri = Boolean()
        ri.setValue(False)
        holder.setRequiresIndex(ri)

        element = ET.Element("ECUC-PARAM-CONF-CONTAINER-DEF")
        ARXMLWriter().writeEcucContainerDef(element, holder)

        tags = [c.tag for c in element]
        assert tags[:5] == ["SHORT-NAME", "DESTINATION-URI-REFS", "MULTIPLICITY-CONFIG-CLASSES", "ORIGIN", "POST-BUILD-VARIANT-MULTIPLICITY"]
        assert tags[5] == "REQUIRES-INDEX"
        uri_ref = element.find("DESTINATION-URI-REFS/DESTINATION-URI-REF")
        assert uri_ref.text == "/EcucDestinationUriDefs/Uri1"
        assert uri_ref.attrib["DEST"] == "ECUC-DESTINATION-URI-DEF"
        assert element.find("MULTIPLICITY-CONFIG-CLASSES/ECUC-MULTIPLICITY-CONFIGURATION-CLASS") is not None
        assert element.find("ORIGIN").text == "VENDOR"
        assert element.find("POST-BUILD-VARIANT-MULTIPLICITY").text == "true"
        assert element.find("REQUIRES-INDEX").text == "false"

"""
Tests for writing the reference-def family (Tables 2.26/2.27/2.28/2.30/2.32,
R23-11).

Element orders (XSD groups): ECUC-ABSTRACT-REFERENCE-DEF → WITH-AUTO;
ECUC-ABSTRACT-INTERNAL-REFERENCE-DEF → REQUIRES-SYMBOLIC-NAME-VALUE;
ECUC-CHOICE-REFERENCE-DEF → DESTINATION-REFS; ECUC-INSTANCE-REFERENCE-DEF →
DESTINATION-CONTEXT, DESTINATION-TYPE.

Round-trip counterpart: tests/test_armodel/parser/test_ecuc_reference_def_family.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucChoiceReferenceDef, EcucInstanceReferenceDef, EcucReferenceDef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, RefType, String
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteEcucReferenceDefFamily:
    def test_write_abstract_reference_with_auto(self):
        """Test that WITH-AUTO is emitted with the spec value."""
        ref = EcucReferenceDef(AUTOSAR.getInstance().createARPackage("Pkg_W"), "Ref1")
        ref.setWithAuto(Boolean().setValue(True))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeEcucReferenceDef(parent, ref)

        element = parent.find("ECUC-REFERENCE-DEF")
        assert element.find("WITH-AUTO").text == "true"

    def test_write_choice_reference_destinations(self):
        """Test that DESTINATION-REFS is emitted with the spec values."""
        ref = EcucChoiceReferenceDef(AUTOSAR.getInstance().createARPackage("Pkg_W"), "Ref1")
        dest = RefType()
        dest.setDest("ECUC-PARAM-CONF-CONTAINER-DEF")
        dest.setValue("/AUTOSAR/Containers/C1")
        ref.addDestinationRef(dest)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeEcucChoiceReferenceDef(parent, ref)

        child = parent.find("ECUC-CHOICE-REFERENCE-DEF")
        dest_ref = child.find("DESTINATION-REFS/DESTINATION-REF")
        assert dest_ref is not None
        assert dest_ref.text == "/AUTOSAR/Containers/C1"
        assert dest_ref.attrib["DEST"] == "ECUC-PARAM-CONF-CONTAINER-DEF"

    def test_write_instance_reference_fields(self):
        """Test that DESTINATION-CONTEXT/DESTINATION-TYPE are emitted with the spec values."""
        ref = EcucInstanceReferenceDef(AUTOSAR.getInstance().createARPackage("Pkg_W"), "Ref1")
        ref.setDestinationContext(String().setValue("SwComponentType"))
        ref.setDestinationType(String().setValue("PortInterface"))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeEcucInstanceReferenceDef(parent, ref)

        child = parent.find("ECUC-INSTANCE-REFERENCE-DEF")
        assert child.find("DESTINATION-CONTEXT").text == "SwComponentType"
        assert child.find("DESTINATION-TYPE").text == "PortInterface"

"""Parser tests for the reference-def family (Tables 2.26/2.27/2.28/2.30/2.32).

Element orders (XSD groups): ECUC-ABSTRACT-REFERENCE-DEF → WITH-AUTO;
ECUC-ABSTRACT-INTERNAL-REFERENCE-DEF → REQUIRES-SYMBOLIC-NAME-VALUE;
ECUC-CHOICE-REFERENCE-DEF → DESTINATION-REFS; ECUC-INSTANCE-REFERENCE-DEF →
DESTINATION-CONTEXT, DESTINATION-TYPE.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucChoiceReferenceDef, EcucInstanceReferenceDef, EcucReferenceDef

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


class TestReadEcucReferenceDefFamily:
    def test_read_abstract_reference_with_auto(self, parser):
        ref = EcucReferenceDef(AUTOSAR.getInstance(), "Ref")
        element = ET.fromstring(f"<ECUC-REFERENCE-DEF xmlns='{NS}'><SHORT-NAME>Ref</SHORT-NAME><WITH-AUTO>true</WITH-AUTO></ECUC-REFERENCE-DEF>")
        parser.readEcucReferenceDef(element, ref)
        assert ref.getWithAuto().getValue() is True

    def test_read_choice_reference_destinations(self, parser):
        ref = EcucChoiceReferenceDef(AUTOSAR.getInstance(), "Ref")
        element = ET.fromstring(
            f"<ECUC-CHOICE-REFERENCE-DEF xmlns='{NS}'>"
            "<SHORT-NAME>Ref</SHORT-NAME>"
            "<DESTINATION-REFS>"
            '<DESTINATION-REF DEST="ECUC-PARAM-CONF-CONTAINER-DEF">/AUTOSAR/Containers/C1</DESTINATION-REF>'
            "</DESTINATION-REFS>"
            "</ECUC-CHOICE-REFERENCE-DEF>"
        )
        parser.readEcucChoiceReferenceDef(element, ref)
        refs = ref.getDestinationRefs()
        assert len(refs) == 1
        assert refs[0].getValue() == "/AUTOSAR/Containers/C1"
        assert refs[0].getDest() == "ECUC-PARAM-CONF-CONTAINER-DEF"

    def test_read_instance_reference_fields(self, parser):
        ref = EcucInstanceReferenceDef(AUTOSAR.getInstance(), "Ref")
        element = ET.fromstring(
            f"<ECUC-INSTANCE-REFERENCE-DEF xmlns='{NS}'>"
            "<SHORT-NAME>Ref</SHORT-NAME>"
            "<DESTINATION-CONTEXT>SwComponentType</DESTINATION-CONTEXT>"
            "<DESTINATION-TYPE>PortInterface</DESTINATION-TYPE>"
            "</ECUC-INSTANCE-REFERENCE-DEF>"
        )
        parser.readEcucInstanceReferenceDef(element, ref)
        assert ref.getDestinationContext().getValue() == "SwComponentType"
        assert ref.getDestinationType().getValue() == "PortInterface"

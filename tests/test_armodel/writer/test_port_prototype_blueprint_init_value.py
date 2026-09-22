"""Writer tests for PortPrototypeBlueprintInitValue (AUTOSAR_FO_TPS_StandardizationTemplate, Table 4.10, p.60).

The writer helper is exercised directly (the class has no ARPackage-level
dispatch; it nests inside PortPrototypeBlueprint's INIT-VALUES wrapper).
XML element order per XSD group PORT-PROTOTYPE-BLUEPRINT-INIT-VALUE
(AUTOSAR_00052.xsd l.92938): DATA-PROTOTYPE-REF, VALUE.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure import TextValueSpecification
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.BlueprintDedicated.PortPrototypeBlueprint import (
    PortPrototypeBlueprintInitValue,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral, RefType
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _new_init_value():
    init_value = PortPrototypeBlueprintInitValue()

    ref = RefType()
    ref.setDest("AUTOSAR-DATA-PROTOTYPE")
    ref.setValue("/Pkg/Blueprint/Dp")
    init_value.setDataPrototypeRef(ref)

    value = TextValueSpecification()
    value.setValue(ARLiteral().setValue("42"))
    init_value.setValue(value)
    return init_value


class TestWritePortPrototypeBlueprintInitValue:
    def test_write_all_fields(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writePortPrototypeBlueprintInitValue(parent, _new_init_value())
        node = parent.find("PORT-PROTOTYPE-BLUEPRINT-INIT-VALUE")
        assert node is not None
        data_ref = node.find("DATA-PROTOTYPE-REF")
        assert data_ref.text == "/Pkg/Blueprint/Dp"
        assert data_ref.attrib["DEST"] == "AUTOSAR-DATA-PROTOTYPE"
        value = node.find("VALUE/TEXT-VALUE-SPECIFICATION/VALUE")
        assert value.text == "42"
        children = [child.tag for child in node]
        assert children == ["DATA-PROTOTYPE-REF", "VALUE"]

    def test_write_empty_fields_omits_optional_tags(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writePortPrototypeBlueprintInitValue(parent, PortPrototypeBlueprintInitValue())
        node = parent.find("PORT-PROTOTYPE-BLUEPRINT-INIT-VALUE")
        assert node is not None
        assert len(list(node)) == 0

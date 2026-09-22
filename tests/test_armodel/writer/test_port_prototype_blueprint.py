"""Writer tests for PortPrototypeBlueprint (AUTOSAR_FO_TPS_StandardizationTemplate, Table 4.9, p.60).

XML element order per XSD group PORT-PROTOTYPE-BLUEPRINT (AUTOSAR_00052.xsd l.92841):
INIT-VALUES, INTERFACE-REF, PROVIDED-COM-SPECS, REQUIRED-COM-SPECS (after the
emitted IDENTIFIABLE base chain content).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure import TextValueSpecification
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.BlueprintDedicated.PortPrototypeBlueprint import (
    PortPrototypeBlueprint,
    PortPrototypeBlueprintInitValue,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral, RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import NonqueuedReceiverComSpec, NonqueuedSenderComSpec
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


class _MockParent(ARObject):
    def __init__(self):
        super().__init__()


def _new_blueprint():
    blueprint = PortPrototypeBlueprint(_MockParent(), "Blueprint1")

    init_value = PortPrototypeBlueprintInitValue()
    ref = RefType()
    ref.setDest("AUTOSAR-DATA-PROTOTYPE")
    ref.setValue("/Pkg/Blueprint/Dp")
    init_value.setDataPrototypeRef(ref)
    value = TextValueSpecification()
    value.setValue(ARLiteral().setValue("42"))
    init_value.setValue(value)
    blueprint.addInitValue(init_value)

    iface_ref = RefType()
    iface_ref.setDest("SENDER-RECEIVER-INTERFACE")
    iface_ref.setValue("/AUTOSAR/If")
    blueprint.setInterfaceRef(iface_ref)

    blueprint.addProvidedComSpec(NonqueuedSenderComSpec())
    blueprint.addRequiredComSpec(NonqueuedReceiverComSpec())
    return blueprint


class TestWritePortPrototypeBlueprint:
    def test_write_all_fields(self):
        parent = ET.Element("ROOT")
        ARXMLWriter().writePortPrototypeBlueprint(parent, _new_blueprint())
        node = parent.find("PORT-PROTOTYPE-BLUEPRINT")
        assert node is not None
        children = [child.tag for child in node]
        assert children == ["SHORT-NAME", "INIT-VALUES", "INTERFACE-REF", "PROVIDED-COM-SPECS", "REQUIRED-COM-SPECS"]
        init_values = node.findall("INIT-VALUES/PORT-PROTOTYPE-BLUEPRINT-INIT-VALUE")
        assert len(init_values) == 1
        data_ref = init_values[0].find("DATA-PROTOTYPE-REF")
        assert data_ref.text == "/Pkg/Blueprint/Dp"
        assert data_ref.attrib["DEST"] == "AUTOSAR-DATA-PROTOTYPE"
        assert init_values[0].find("VALUE/TEXT-VALUE-SPECIFICATION/VALUE").text == "42"
        iface_ref = node.find("INTERFACE-REF")
        assert iface_ref.text == "/AUTOSAR/If"
        assert iface_ref.attrib["DEST"] == "SENDER-RECEIVER-INTERFACE"
        assert len(node.findall("PROVIDED-COM-SPECS/NONQUEUED-SENDER-COM-SPEC")) == 1
        assert len(node.findall("REQUIRED-COM-SPECS/NONQUEUED-RECEIVER-COM-SPEC")) == 1

    def test_write_empty_fields_omits_optional_tags(self):
        parent = ET.Element("ROOT")
        ARXMLWriter().writePortPrototypeBlueprint(parent, PortPrototypeBlueprint(_MockParent(), "Empty1"))
        node = parent.find("PORT-PROTOTYPE-BLUEPRINT")
        assert node is not None
        assert [child.tag for child in node] == ["SHORT-NAME"]

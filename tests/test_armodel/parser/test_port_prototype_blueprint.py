"""Parser tests for PortPrototypeBlueprint (AUTOSAR_FO_TPS_StandardizationTemplate, Table 4.9, p.60).

XML element order per XSD group PORT-PROTOTYPE-BLUEPRINT (AUTOSAR_00052.xsd l.92841):
INIT-VALUES, INTERFACE-REF, PROVIDED-COM-SPECS, REQUIRED-COM-SPECS.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.BlueprintDedicated.PortPrototypeBlueprint import (
    PortPrototypeBlueprint,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import NonqueuedReceiverComSpec, NonqueuedSenderComSpec
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


class _MockParent(ARObject):
    def __init__(self):
        super().__init__()


def _blueprint_fragment():
    return (
        "<PORT-PROTOTYPE-BLUEPRINT xmlns='%s'>"
        "<SHORT-NAME>Blueprint1</SHORT-NAME>"
        "<INIT-VALUES>"
        "<PORT-PROTOTYPE-BLUEPRINT-INIT-VALUE>"
        "<DATA-PROTOTYPE-REF DEST='AUTOSAR-DATA-PROTOTYPE'>/Pkg/Blueprint/Dp</DATA-PROTOTYPE-REF>"
        "<VALUE><TEXT-VALUE-SPECIFICATION><VALUE>42</VALUE></TEXT-VALUE-SPECIFICATION></VALUE>"
        "</PORT-PROTOTYPE-BLUEPRINT-INIT-VALUE>"
        "</INIT-VALUES>"
        "<INTERFACE-REF DEST='SENDER-RECEIVER-INTERFACE'>/AUTOSAR/If</INTERFACE-REF>"
        "<PROVIDED-COM-SPECS><NONQUEUED-SENDER-COM-SPEC/></PROVIDED-COM-SPECS>"
        "<REQUIRED-COM-SPECS><NONQUEUED-RECEIVER-COM-SPEC/></REQUIRED-COM-SPECS>"
        "</PORT-PROTOTYPE-BLUEPRINT>" % NS
    )


def test_parse_port_prototype_blueprint():
    blueprint = PortPrototypeBlueprint(_MockParent(), "Blueprint1")
    root = ET.fromstring(_blueprint_fragment())
    ARXMLParser().readPortPrototypeBlueprint(root, blueprint)

    init_values = blueprint.getInitValues()
    assert len(init_values) == 1
    assert init_values[0].getDataPrototypeRef().getValue() == "/Pkg/Blueprint/Dp"
    assert init_values[0].getDataPrototypeRef().getDest() == "AUTOSAR-DATA-PROTOTYPE"
    assert init_values[0].getValue().getValue().getValue() == "42"
    assert blueprint.getInterfaceRef().getValue() == "/AUTOSAR/If"
    assert blueprint.getInterfaceRef().getDest() == "SENDER-RECEIVER-INTERFACE"
    assert len(blueprint.getProvidedComSpecs()) == 1
    assert isinstance(blueprint.getProvidedComSpecs()[0], NonqueuedSenderComSpec)
    assert len(blueprint.getRequiredComSpecs()) == 1
    assert isinstance(blueprint.getRequiredComSpecs()[0], NonqueuedReceiverComSpec)


def test_parse_port_prototype_blueprint_empty():
    blueprint = PortPrototypeBlueprint(_MockParent(), "Blueprint1")
    root = ET.fromstring("<PORT-PROTOTYPE-BLUEPRINT xmlns='%s'><SHORT-NAME>Blueprint1</SHORT-NAME></PORT-PROTOTYPE-BLUEPRINT>" % NS)
    ARXMLParser().readPortPrototypeBlueprint(root, blueprint)

    assert blueprint.getInitValues() == []
    assert blueprint.getInterfaceRef() is None
    assert blueprint.getProvidedComSpecs() == []
    assert blueprint.getRequiredComSpecs() == []


def test_round_trip_preserves_all_values():
    blueprint = PortPrototypeBlueprint(_MockParent(), "Blueprint1")
    root = ET.fromstring(_blueprint_fragment())
    ARXMLParser().readPortPrototypeBlueprint(root, blueprint)

    parent = ET.Element("ROOT")
    from armodel.writer.arxml_writer import ARXMLWriter

    ARXMLWriter().writePortPrototypeBlueprint(parent, blueprint)
    inner = ET.tostring(parent).decode("utf-8")
    reparsed_root = ET.fromstring(inner.replace("<ROOT>", "<ROOT xmlns='%s'>" % NS, 1))

    parsed = PortPrototypeBlueprint(_MockParent(), "Blueprint1")
    ARXMLParser().readPortPrototypeBlueprint(reparsed_root[0], parsed)

    init_values = parsed.getInitValues()
    assert len(init_values) == 1
    assert init_values[0].getDataPrototypeRef().getValue() == "/Pkg/Blueprint/Dp"
    assert init_values[0].getValue().getValue().getValue() == "42"
    assert parsed.getInterfaceRef().getValue() == "/AUTOSAR/If"
    assert parsed.getInterfaceRef().getDest() == "SENDER-RECEIVER-INTERFACE"
    assert isinstance(parsed.getProvidedComSpecs()[0], NonqueuedSenderComSpec)
    assert isinstance(parsed.getRequiredComSpecs()[0], NonqueuedReceiverComSpec)

"""Parser tests for PortPrototypeBlueprintInitValue (AUTOSAR_FO_TPS_StandardizationTemplate, Table 4.10, p.60).

The reader helper is exercised directly on a PORT-PROTOTYPE-BLUEPRINT-INIT-VALUE
fragment (the class has no ARPackage-level dispatch; it nests inside
PortPrototypeBlueprint's INIT-VALUES wrapper). XML element order per XSD group
PORT-PROTOTYPE-BLUEPRINT-INIT-VALUE (AUTOSAR_00052.xsd l.92938): DATA-PROTOTYPE-REF,
VALUE.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.BlueprintDedicated.PortPrototypeBlueprint import (
    PortPrototypeBlueprintInitValue,
)
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _init_value_fragment():
    return (
        "<PORT-PROTOTYPE-BLUEPRINT-INIT-VALUE xmlns='%s'>"
        "<DATA-PROTOTYPE-REF DEST='AUTOSAR-DATA-PROTOTYPE'>/Pkg/Blueprint/Dp</DATA-PROTOTYPE-REF>"
        "<VALUE><TEXT-VALUE-SPECIFICATION><SHORT-LABEL>iv</SHORT-LABEL><VALUE>42</VALUE></TEXT-VALUE-SPECIFICATION></VALUE>"
        "</PORT-PROTOTYPE-BLUEPRINT-INIT-VALUE>" % NS
    )


def test_parse_port_prototype_blueprint_init_value():
    init_value = PortPrototypeBlueprintInitValue()
    root = ET.fromstring(_init_value_fragment())
    ARXMLParser().readPortPrototypeBlueprintInitValue(root, init_value)

    assert init_value.getDataPrototypeRef().getValue() == "/Pkg/Blueprint/Dp"
    assert init_value.getDataPrototypeRef().getDest() == "AUTOSAR-DATA-PROTOTYPE"
    assert init_value.getValue().getShortLabel().getValue() == "iv"
    assert init_value.getValue().getValue().getValue() == "42"


def test_parse_port_prototype_blueprint_init_value_empty():
    init_value = PortPrototypeBlueprintInitValue()
    root = ET.fromstring("<PORT-PROTOTYPE-BLUEPRINT-INIT-VALUE xmlns='%s'/>" % NS)
    ARXMLParser().readPortPrototypeBlueprintInitValue(root, init_value)

    assert init_value.getDataPrototypeRef() is None
    assert init_value.getValue() is None


def test_round_trip_preserves_all_values():
    init_value = PortPrototypeBlueprintInitValue()
    root = ET.fromstring(_init_value_fragment())
    ARXMLParser().readPortPrototypeBlueprintInitValue(root, init_value)

    parent = ET.Element("ROOT")
    from armodel.writer.arxml_writer import ARXMLWriter

    ARXMLWriter().writePortPrototypeBlueprintInitValue(parent, init_value)
    inner = ET.tostring(parent).decode("utf-8")
    reparsed_root = ET.fromstring(inner.replace("<ROOT>", "<ROOT xmlns='%s'>" % NS, 1))

    parsed = PortPrototypeBlueprintInitValue()
    ARXMLParser().readPortPrototypeBlueprintInitValue(reparsed_root[0], parsed)

    assert parsed.getDataPrototypeRef().getValue() == "/Pkg/Blueprint/Dp"
    assert parsed.getDataPrototypeRef().getDest() == "AUTOSAR-DATA-PROTOTYPE"
    assert parsed.getValue().getShortLabel().getValue() == "iv"
    assert parsed.getValue().getValue().getValue() == "42"

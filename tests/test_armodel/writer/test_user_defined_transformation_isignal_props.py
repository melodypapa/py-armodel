"""Writer round-trip tests for UserDefinedTransformationISignalProps (Table 7.28, p.828).

Wrapper form per XSD: USER-DEFINED-TRANSFORMATION-I-SIGNAL-PROPS → -VARIANTS →
-CONDITIONAL → content. Conditional content order per XSD (base group
TRANSFORMATION-I-SIGNAL-PROPS-CONTENT: CS-ERROR-REACTION, then tail TRANSFORMER-REF;
the own group USER-DEFINED-TRANSFORMATION-I-SIGNAL-PROPS-CONTENT is an empty
sequence — the class contributes no own XML content).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import (
    CSTransformerErrorReactionEnum,
    UserDefinedTransformationISignalProps,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _new_props():
    props = UserDefinedTransformationISignalProps()
    props.setCsErrorReaction(CSTransformerErrorReactionEnum().setValue(CSTransformerErrorReactionEnum.AUTONOMOUS))

    transformer_ref = RefType()
    transformer_ref.setDest("TRANSFORMATION-TECHNOLOGY")
    transformer_ref.setValue("/Transformers/CustomSerializer")
    props.setTransformerRef(transformer_ref)
    return props


EXPECTED_CONDITIONAL_ORDER = [
    "CS-ERROR-REACTION",
    "TRANSFORMER-REF",
]


class TestWriteUserDefinedTransformationISignalProps:
    def test_write_wrapper_form_in_xsd_order(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeUserDefinedTransformationISignalProps(parent, _new_props())

        assert parent[0].tag == "USER-DEFINED-TRANSFORMATION-I-SIGNAL-PROPS"
        assert parent[0][0].tag == "USER-DEFINED-TRANSFORMATION-I-SIGNAL-PROPS-VARIANTS"
        conditional = parent[0][0][0]
        assert conditional.tag == "USER-DEFINED-TRANSFORMATION-I-SIGNAL-PROPS-CONDITIONAL"

        children = [child.tag for child in conditional]
        assert children == EXPECTED_CONDITIONAL_ORDER

        assert conditional.find("CS-ERROR-REACTION").text == "AUTONOMOUS"
        transformer_ref = conditional.find("TRANSFORMER-REF")
        assert transformer_ref.text == "/Transformers/CustomSerializer"
        assert transformer_ref.attrib["DEST"] == "TRANSFORMATION-TECHNOLOGY"

    def test_write_empty_omits_optional_tags(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeUserDefinedTransformationISignalProps(parent, UserDefinedTransformationISignalProps())

        assert parent[0].tag == "USER-DEFINED-TRANSFORMATION-I-SIGNAL-PROPS"
        conditional = parent[0][0][0]
        assert conditional.tag == "USER-DEFINED-TRANSFORMATION-I-SIGNAL-PROPS-CONDITIONAL"
        assert len(list(conditional)) == 0

    def test_round_trip_preserves_all_values(self):
        props = _new_props()
        parent = ET.Element("PARENT")
        ARXMLWriter().writeUserDefinedTransformationISignalProps(parent, props)
        root = ET.fromstring("<ROOT xmlns='%s'>%s</ROOT>" % (NS, ET.tostring(parent).decode("utf-8")))

        parsed = UserDefinedTransformationISignalProps()
        ARXMLParser().readUserDefinedTransformationISignalProps(root[0][0], parsed)

        assert isinstance(parsed, UserDefinedTransformationISignalProps)
        assert parsed.getCsErrorReaction().getValue() == "AUTONOMOUS"
        assert parsed.getTransformerRef().getValue() == "/Transformers/CustomSerializer"
        assert parsed.getTransformerRef().getDest() == "TRANSFORMATION-TECHNOLOGY"

    def test_dispatch_through_isignal_group(self):
        from armodel.models import ISignalGroup

        group = ISignalGroup(parent=AUTOSAR.getInstance(), short_name="grp")
        group.addTransformationISignalProps(_new_props())

        parent = ET.Element("PARENT")
        ARXMLWriter().writeISignalGroupTransformationISignalProps(parent, group)

        assert parent[0].tag == "TRANSFORMATION-I-SIGNAL-PROPSS"
        assert parent[0][0].tag == "USER-DEFINED-TRANSFORMATION-I-SIGNAL-PROPS"
        assert parent[0][0][0].tag == "USER-DEFINED-TRANSFORMATION-I-SIGNAL-PROPS-VARIANTS"
        assert parent[0][0][0][0].tag == "USER-DEFINED-TRANSFORMATION-I-SIGNAL-PROPS-CONDITIONAL"
        assert parent[0][0][0][0].find("TRANSFORMER-REF").text == "/Transformers/CustomSerializer"

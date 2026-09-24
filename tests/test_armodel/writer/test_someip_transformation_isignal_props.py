"""Writer round-trip tests for SomeipTransformationISignalProps (Table 7.11, p.778).

Wrapper form per XSD: SOMEIP-TRANSFORMATION-I-SIGNAL-PROPS → -VARIANTS →
-CONDITIONAL → content. Conditional content order per XSD (base group
TRANSFORMATION-I-SIGNAL-PROPS-CONTENT tail TRANSFORMER-REF, then own group
SOMEIP-TRANSFORMATION-I-SIGNAL-PROPS-CONTENT minus the removed-status elements).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    RefType,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import (
    CSTransformerErrorReactionEnum,
    SOMEIPMessageTypeEnum,
    SomeipTransformationISignalProps,
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
    props = SomeipTransformationISignalProps()
    props.setCsErrorReaction(CSTransformerErrorReactionEnum().setValue(CSTransformerErrorReactionEnum.AUTONOMOUS))

    transformer_ref = RefType()
    transformer_ref.setDest("TRANSFORMATION-TECHNOLOGY")
    transformer_ref.setValue("/Transformers/Serializer")
    props.setTransformerRef(transformer_ref)

    props.setImplementsLegacyStringSerialization(Boolean().setValue(True))
    props.setInterfaceVersion(PositiveInteger().setValue("4"))
    props.setIsDynamicLengthFieldSize(Boolean().setValue(False))
    props.setMessageType(SOMEIPMessageTypeEnum().setValue(SOMEIPMessageTypeEnum.REQUEST_NO_RETURN))
    props.setSizeOfArrayLengthFields(PositiveInteger().setValue("8"))
    props.setSizeOfStringLengthFields(PositiveInteger().setValue("12"))
    props.setSizeOfStructLengthFields(PositiveInteger().setValue("16"))
    props.setSizeOfUnionLengthFields(PositiveInteger().setValue("4"))

    first = RefType()
    first.setDest("TLV-DATA-ID-DEFINITION-SET")
    first.setValue("/TlvSets/Set1")
    second = RefType()
    second.setDest("TLV-DATA-ID-DEFINITION-SET")
    second.setValue("/TlvSets/Set2")
    props.addTlvDataIdDefinitionRef(first)
    props.addTlvDataIdDefinitionRef(second)
    return props


EXPECTED_CONDITIONAL_ORDER = [
    "CS-ERROR-REACTION",
    "TRANSFORMER-REF",
    "IMPLEMENTS-LEGACY-STRING-SERIALIZATION",
    "INTERFACE-VERSION",
    "IS-DYNAMIC-LENGTH-FIELD-SIZE",
    "MESSAGE-TYPE",
    "SIZE-OF-ARRAY-LENGTH-FIELDS",
    "SIZE-OF-STRING-LENGTH-FIELDS",
    "SIZE-OF-STRUCT-LENGTH-FIELDS",
    "SIZE-OF-UNION-LENGTH-FIELDS",
    "TLV-DATA-ID-DEFINITION-REFS",
]


class TestWriteSomeipTransformationISignalProps:
    def test_write_wrapper_form_in_xsd_order(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeSomeipTransformationISignalProps(parent, _new_props())

        assert parent[0].tag == "SOMEIP-TRANSFORMATION-I-SIGNAL-PROPS"
        assert parent[0][0].tag == "SOMEIP-TRANSFORMATION-I-SIGNAL-PROPS-VARIANTS"
        conditional = parent[0][0][0]
        assert conditional.tag == "SOMEIP-TRANSFORMATION-I-SIGNAL-PROPS-CONDITIONAL"

        children = [child.tag for child in conditional]
        assert children == EXPECTED_CONDITIONAL_ORDER

        assert conditional.find("CS-ERROR-REACTION").text == "AUTONOMOUS"
        transformer_ref = conditional.find("TRANSFORMER-REF")
        assert transformer_ref.text == "/Transformers/Serializer"
        assert transformer_ref.attrib["DEST"] == "TRANSFORMATION-TECHNOLOGY"
        assert conditional.find("IMPLEMENTS-LEGACY-STRING-SERIALIZATION").text == "true"
        assert conditional.find("INTERFACE-VERSION").text == "4"
        assert conditional.find("IS-DYNAMIC-LENGTH-FIELD-SIZE").text == "false"
        assert conditional.find("MESSAGE-TYPE").text == "REQUEST-NO-RETURN"
        assert conditional.find("SIZE-OF-ARRAY-LENGTH-FIELDS").text == "8"
        assert conditional.find("SIZE-OF-STRING-LENGTH-FIELDS").text == "12"
        assert conditional.find("SIZE-OF-STRUCT-LENGTH-FIELDS").text == "16"
        assert conditional.find("SIZE-OF-UNION-LENGTH-FIELDS").text == "4"

    def test_write_refs_wrapper(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeSomeipTransformationISignalProps(parent, _new_props())

        refs_element = parent.find("SOMEIP-TRANSFORMATION-I-SIGNAL-PROPS/SOMEIP-TRANSFORMATION-I-SIGNAL-PROPS-VARIANTS/SOMEIP-TRANSFORMATION-I-SIGNAL-PROPS-CONDITIONAL/TLV-DATA-ID-DEFINITION-REFS")
        refs = list(refs_element)
        assert len(refs) == 2
        assert refs[0].tag == "TLV-DATA-ID-DEFINITION-REF"
        assert refs[0].text == "/TlvSets/Set1"
        assert refs[0].attrib["DEST"] == "TLV-DATA-ID-DEFINITION-SET"
        assert refs[1].text == "/TlvSets/Set2"

    def test_write_empty_omits_optional_tags(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeSomeipTransformationISignalProps(parent, SomeipTransformationISignalProps())

        assert parent[0].tag == "SOMEIP-TRANSFORMATION-I-SIGNAL-PROPS"
        conditional = parent[0][0][0]
        assert conditional.tag == "SOMEIP-TRANSFORMATION-I-SIGNAL-PROPS-CONDITIONAL"
        assert len(list(conditional)) == 0

    def test_round_trip_preserves_all_values(self):
        props = _new_props()
        parent = ET.Element("PARENT")
        ARXMLWriter().writeSomeipTransformationISignalProps(parent, props)
        root = ET.fromstring("<ROOT xmlns='%s'>%s</ROOT>" % (NS, ET.tostring(parent).decode("utf-8")))

        parsed = SomeipTransformationISignalProps()
        ARXMLParser().readSomeipTransformationISignalProps(root[0][0], parsed)

        assert isinstance(parsed, SomeipTransformationISignalProps)
        assert parsed.getCsErrorReaction().getValue() == "AUTONOMOUS"
        assert parsed.getTransformerRef().getValue() == "/Transformers/Serializer"
        assert parsed.getTransformerRef().getDest() == "TRANSFORMATION-TECHNOLOGY"
        assert parsed.getImplementsLegacyStringSerialization().getValue() is True
        assert parsed.getInterfaceVersion().getValue() == 4
        assert parsed.getIsDynamicLengthFieldSize().getValue() is False
        assert parsed.getMessageType().getValue() == "REQUEST-NO-RETURN"
        assert parsed.getSizeOfArrayLengthFields().getValue() == 8
        assert parsed.getSizeOfStringLengthFields().getValue() == 12
        assert parsed.getSizeOfStructLengthFields().getValue() == 16
        assert parsed.getSizeOfUnionLengthFields().getValue() == 4
        refs = parsed.getTlvDataIdDefinitionRefs()
        assert len(refs) == 2
        assert refs[0].getValue() == "/TlvSets/Set1"
        assert refs[0].getDest() == "TLV-DATA-ID-DEFINITION-SET"
        assert refs[1].getValue() == "/TlvSets/Set2"
        assert refs[1].getDest() == "TLV-DATA-ID-DEFINITION-SET"

    def test_dispatch_through_isignal_group(self):
        from armodel.models import ISignalGroup

        group = ISignalGroup(parent=AUTOSAR.getInstance(), short_name="grp")
        group.addTransformationISignalProps(_new_props())

        parent = ET.Element("PARENT")
        ARXMLWriter().writeISignalGroupTransformationISignalProps(parent, group)

        assert parent[0].tag == "TRANSFORMATION-I-SIGNAL-PROPSS"
        assert parent[0][0].tag == "SOMEIP-TRANSFORMATION-I-SIGNAL-PROPS"
        assert parent[0][0][0].tag == "SOMEIP-TRANSFORMATION-I-SIGNAL-PROPS-VARIANTS"
        assert parent[0][0][0][0].tag == "SOMEIP-TRANSFORMATION-I-SIGNAL-PROPS-CONDITIONAL"
        assert parent[0][0][0][0].find("MESSAGE-TYPE").text == "REQUEST-NO-RETURN"

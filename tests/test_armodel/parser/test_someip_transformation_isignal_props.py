"""Parser tests for SomeipTransformationISignalProps (Table 7.11, p.778).

Concrete atpVariation subclass of TransformationISignalProps. Wire form per XSD:
SOMEIP-TRANSFORMATION-I-SIGNAL-PROPS → -VARIANTS → -CONDITIONAL → content groups.
Own content order per XSD group SOMEIP-TRANSFORMATION-I-SIGNAL-PROPS-CONTENT:
IMPLEMENTS-LEGACY-STRING-SERIALIZATION, INTERFACE-VERSION, IS-DYNAMIC-LENGTH-FIELD-SIZE,
MESSAGE-TYPE, SIZE-OF-ARRAY/STRING/STRUCT/UNION-LENGTH-FIELDS, TLV-DATA-ID-DEFINITION-REFS
(the removed-status IMPLEMENTS-SOMEIP-STRING-HANDLING / SESSION-HANDLING-SR /
TLV-DATA-IDS / TLV-DATA-ID-0-REFS elements are not modeled, Rule 0015).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
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


def _snip(inner: str) -> ET.Element:
    xml = "<ROOT xmlns='%s'>%s</ROOT>" % (NS, inner)
    return ET.fromstring(xml)


CONDITIONAL_XML = (
    "<SOMEIP-TRANSFORMATION-I-SIGNAL-PROPS-VARIANTS>"
    "<SOMEIP-TRANSFORMATION-I-SIGNAL-PROPS-CONDITIONAL>"
    "<CS-ERROR-REACTION>AUTONOMOUS</CS-ERROR-REACTION>"
    '<TRANSFORMER-REF DEST="TRANSFORMATION-TECHNOLOGY">/Transformers/Serializer</TRANSFORMER-REF>'
    "<IMPLEMENTS-LEGACY-STRING-SERIALIZATION>true</IMPLEMENTS-LEGACY-STRING-SERIALIZATION>"
    "<INTERFACE-VERSION>4</INTERFACE-VERSION>"
    "<IS-DYNAMIC-LENGTH-FIELD-SIZE>false</IS-DYNAMIC-LENGTH-FIELD-SIZE>"
    "<MESSAGE-TYPE>REQUEST-NO-RETURN</MESSAGE-TYPE>"
    "<SIZE-OF-ARRAY-LENGTH-FIELDS>8</SIZE-OF-ARRAY-LENGTH-FIELDS>"
    "<SIZE-OF-STRING-LENGTH-FIELDS>12</SIZE-OF-STRING-LENGTH-FIELDS>"
    "<SIZE-OF-STRUCT-LENGTH-FIELDS>16</SIZE-OF-STRUCT-LENGTH-FIELDS>"
    "<SIZE-OF-UNION-LENGTH-FIELDS>4</SIZE-OF-UNION-LENGTH-FIELDS>"
    "<TLV-DATA-ID-DEFINITION-REFS>"
    '<TLV-DATA-ID-DEFINITION-REF DEST="TLV-DATA-ID-DEFINITION-SET">/TlvSets/Set1</TLV-DATA-ID-DEFINITION-REF>'
    '<TLV-DATA-ID-DEFINITION-REF DEST="TLV-DATA-ID-DEFINITION-SET">/TlvSets/Set2</TLV-DATA-ID-DEFINITION-REF>'
    "</TLV-DATA-ID-DEFINITION-REFS>"
    "</SOMEIP-TRANSFORMATION-I-SIGNAL-PROPS-CONDITIONAL>"
    "</SOMEIP-TRANSFORMATION-I-SIGNAL-PROPS-VARIANTS>"
)


class TestReadSomeipTransformationISignalProps:
    def test_read_full(self):
        props = SomeipTransformationISignalProps()
        root = _snip(CONDITIONAL_XML)
        ARXMLParser().readSomeipTransformationISignalProps(root, props)

        assert isinstance(props, SomeipTransformationISignalProps)
        cs_error_reaction = props.getCsErrorReaction()
        assert isinstance(cs_error_reaction, CSTransformerErrorReactionEnum)
        assert cs_error_reaction.getValue() == "AUTONOMOUS"

        assert props.getTransformerRef().getValue() == "/Transformers/Serializer"
        assert props.getTransformerRef().getDest() == "TRANSFORMATION-TECHNOLOGY"

        assert props.getImplementsLegacyStringSerialization().getValue() is True
        assert props.getInterfaceVersion().getValue() == 4
        assert props.getIsDynamicLengthFieldSize().getValue() is False

        message_type = props.getMessageType()
        assert isinstance(message_type, SOMEIPMessageTypeEnum)
        assert message_type.getValue() == "REQUEST-NO-RETURN"

        assert props.getSizeOfArrayLengthFields().getValue() == 8
        assert props.getSizeOfStringLengthFields().getValue() == 12
        assert props.getSizeOfStructLengthFields().getValue() == 16
        assert props.getSizeOfUnionLengthFields().getValue() == 4

        refs = props.getTlvDataIdDefinitionRefs()
        assert len(refs) == 2
        assert refs[0].getValue() == "/TlvSets/Set1"
        assert refs[0].getDest() == "TLV-DATA-ID-DEFINITION-SET"
        assert refs[1].getValue() == "/TlvSets/Set2"
        assert refs[1].getDest() == "TLV-DATA-ID-DEFINITION-SET"

    def test_read_optional_absent(self):
        props = SomeipTransformationISignalProps()
        root = _snip("<SOMEIP-TRANSFORMATION-I-SIGNAL-PROPS-VARIANTS>" "<SOMEIP-TRANSFORMATION-I-SIGNAL-PROPS-CONDITIONAL />" "</SOMEIP-TRANSFORMATION-I-SIGNAL-PROPS-VARIANTS>")
        ARXMLParser().readSomeipTransformationISignalProps(root, props)

        assert props.getCsErrorReaction() is None
        assert props.getTransformerRef() is None
        assert props.getImplementsLegacyStringSerialization() is None
        assert props.getInterfaceVersion() is None
        assert props.getIsDynamicLengthFieldSize() is None
        assert props.getMessageType() is None
        assert props.getSizeOfArrayLengthFields() is None
        assert props.getSizeOfStringLengthFields() is None
        assert props.getSizeOfStructLengthFields() is None
        assert props.getSizeOfUnionLengthFields() is None
        assert props.getTlvDataIdDefinitionRefs() == []

    def test_dispatch_through_isignal(self):
        from armodel.models import ISignal

        signal = ISignal(parent=AUTOSAR.getInstance(), short_name="sig")
        root = _snip("<TRANSFORMATION-I-SIGNAL-PROPSS><SOMEIP-TRANSFORMATION-I-SIGNAL-PROPS>%s</SOMEIP-TRANSFORMATION-I-SIGNAL-PROPS></TRANSFORMATION-I-SIGNAL-PROPSS>" % CONDITIONAL_XML)
        ARXMLParser().readISignalTransformationISignalProps(root, signal)

        props_list = signal.getTransformationISignalProps()
        assert len(props_list) == 1
        props = props_list[0]
        assert isinstance(props, SomeipTransformationISignalProps)
        assert props.getMessageType().getValue() == "REQUEST-NO-RETURN"
        assert props.getInterfaceVersion().getValue() == 4


class TestSomeipTransformationISignalPropsRoundTrip:
    def test_parse_write_reparse(self):
        parsed_first = SomeipTransformationISignalProps()
        root = _snip(CONDITIONAL_XML)
        ARXMLParser().readSomeipTransformationISignalProps(root, parsed_first)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeSomeipTransformationISignalProps(parent, parsed_first)
        written = ET.tostring(parent).decode("utf-8")
        reparse_root = ET.fromstring("<ROOT xmlns='%s'>%s</ROOT>" % (NS, written))

        parsed_second = SomeipTransformationISignalProps()
        ARXMLParser().readSomeipTransformationISignalProps(reparse_root[0][0], parsed_second)

        assert parsed_second.getCsErrorReaction().getValue() == "AUTONOMOUS"
        assert parsed_second.getTransformerRef().getValue() == "/Transformers/Serializer"
        assert parsed_second.getImplementsLegacyStringSerialization().getValue() is True
        assert parsed_second.getInterfaceVersion().getValue() == 4
        assert parsed_second.getIsDynamicLengthFieldSize().getValue() is False
        assert parsed_second.getMessageType().getValue() == "REQUEST-NO-RETURN"
        assert parsed_second.getSizeOfArrayLengthFields().getValue() == 8
        assert parsed_second.getSizeOfStringLengthFields().getValue() == 12
        assert parsed_second.getSizeOfStructLengthFields().getValue() == 16
        assert parsed_second.getSizeOfUnionLengthFields().getValue() == 4
        refs = parsed_second.getTlvDataIdDefinitionRefs()
        assert len(refs) == 2
        assert refs[0].getValue() == "/TlvSets/Set1"
        assert refs[0].getDest() == "TLV-DATA-ID-DEFINITION-SET"
        assert refs[1].getValue() == "/TlvSets/Set2"

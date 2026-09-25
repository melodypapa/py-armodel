"""Parser tests for UserDefinedTransformationISignalProps (Table 7.28, p.828).

Concrete atpVariation subclass of TransformationISignalProps with ZERO own attribute
rows. Wire form per XSD: USER-DEFINED-TRANSFORMATION-I-SIGNAL-PROPS → -VARIANTS →
-CONDITIONAL → content groups. Own content order per XSD group
USER-DEFINED-TRANSFORMATION-I-SIGNAL-PROPS-CONTENT: empty sequence — the class adds
nothing beyond the base TRANSFORMATION-I-SIGNAL-PROPS content (CS-ERROR-REACTION,
DATA-PROTOTYPE-TRANSFORMATION-PROPSS, TRANSFORMER-REF).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
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


def _snip(inner: str) -> ET.Element:
    xml = "<ROOT xmlns='%s'>%s</ROOT>" % (NS, inner)
    return ET.fromstring(xml)


CONDITIONAL_XML = (
    "<USER-DEFINED-TRANSFORMATION-I-SIGNAL-PROPS-VARIANTS>"
    "<USER-DEFINED-TRANSFORMATION-I-SIGNAL-PROPS-CONDITIONAL>"
    "<CS-ERROR-REACTION>AUTONOMOUS</CS-ERROR-REACTION>"
    '<TRANSFORMER-REF DEST="TRANSFORMATION-TECHNOLOGY">/Transformers/CustomSerializer</TRANSFORMER-REF>'
    "</USER-DEFINED-TRANSFORMATION-I-SIGNAL-PROPS-CONDITIONAL>"
    "</USER-DEFINED-TRANSFORMATION-I-SIGNAL-PROPS-VARIANTS>"
)


class TestReadUserDefinedTransformationISignalProps:
    def test_read_base_content(self):
        props = UserDefinedTransformationISignalProps()
        root = _snip(CONDITIONAL_XML)
        ARXMLParser().readUserDefinedTransformationISignalProps(root, props)

        assert isinstance(props, UserDefinedTransformationISignalProps)
        cs_error_reaction = props.getCsErrorReaction()
        assert isinstance(cs_error_reaction, CSTransformerErrorReactionEnum)
        assert cs_error_reaction.getValue() == "AUTONOMOUS"

        assert props.getTransformerRef().getValue() == "/Transformers/CustomSerializer"
        assert props.getTransformerRef().getDest() == "TRANSFORMATION-TECHNOLOGY"

    def test_read_optional_absent(self):
        props = UserDefinedTransformationISignalProps()
        root = _snip("<USER-DEFINED-TRANSFORMATION-I-SIGNAL-PROPS-VARIANTS>" "<USER-DEFINED-TRANSFORMATION-I-SIGNAL-PROPS-CONDITIONAL />" "</USER-DEFINED-TRANSFORMATION-I-SIGNAL-PROPS-VARIANTS>")
        ARXMLParser().readUserDefinedTransformationISignalProps(root, props)

        assert props.getCsErrorReaction() is None
        assert props.getTransformerRef() is None

    def test_dispatch_through_isignal(self):
        from armodel.models import ISignal

        signal = ISignal(parent=AUTOSAR.getInstance(), short_name="sig")
        root = _snip("<TRANSFORMATION-I-SIGNAL-PROPSS><USER-DEFINED-TRANSFORMATION-I-SIGNAL-PROPS>%s</USER-DEFINED-TRANSFORMATION-I-SIGNAL-PROPS></TRANSFORMATION-I-SIGNAL-PROPSS>" % CONDITIONAL_XML)
        ARXMLParser().readISignalTransformationISignalProps(root, signal)

        props_list = signal.getTransformationISignalProps()
        assert len(props_list) == 1
        props = props_list[0]
        assert isinstance(props, UserDefinedTransformationISignalProps)
        assert props.getTransformerRef().getValue() == "/Transformers/CustomSerializer"
        assert props.getCsErrorReaction().getValue() == "AUTONOMOUS"

    def test_dispatch_through_isignal_group(self):
        from armodel.models import ISignalGroup

        group = ISignalGroup(parent=AUTOSAR.getInstance(), short_name="grp")
        root = _snip("<TRANSFORMATION-I-SIGNAL-PROPSS><USER-DEFINED-TRANSFORMATION-I-SIGNAL-PROPS>%s</USER-DEFINED-TRANSFORMATION-I-SIGNAL-PROPS></TRANSFORMATION-I-SIGNAL-PROPSS>" % CONDITIONAL_XML)
        ARXMLParser().readISignalGroupTransformationISignalProps(root, group)

        props_list = group.getTransformationISignalProps()
        assert len(props_list) == 1
        props = props_list[0]
        assert isinstance(props, UserDefinedTransformationISignalProps)
        assert props.getTransformerRef().getValue() == "/Transformers/CustomSerializer"


class TestUserDefinedTransformationISignalPropsRoundTrip:
    def test_parse_write_reparse(self):
        parsed_first = UserDefinedTransformationISignalProps()
        root = _snip(CONDITIONAL_XML)
        ARXMLParser().readUserDefinedTransformationISignalProps(root, parsed_first)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeUserDefinedTransformationISignalProps(parent, parsed_first)
        written = ET.tostring(parent).decode("utf-8")
        reparse_root = ET.fromstring("<ROOT xmlns='%s'>%s</ROOT>" % (NS, written))

        parsed_second = UserDefinedTransformationISignalProps()
        ARXMLParser().readUserDefinedTransformationISignalProps(reparse_root[0][0], parsed_second)

        assert isinstance(parsed_second, UserDefinedTransformationISignalProps)
        assert parsed_second.getCsErrorReaction().getValue() == "AUTONOMOUS"
        assert parsed_second.getTransformerRef().getValue() == "/Transformers/CustomSerializer"
        assert parsed_second.getTransformerRef().getDest() == "TRANSFORMATION-TECHNOLOGY"

"""Parser tests for TransformationISignalProps (Table 7.8, p.772).

Abstract class (Base = Describable) — exercised through its concrete subclass
EndToEndTransformationISignalProps. Content element order per XSD group
TRANSFORMATION-I-SIGNAL-PROPS-CONTENT: CS-ERROR-REACTION,
DATA-PROTOTYPE-TRANSFORMATION-PROPSS, TRANSFORMER-REF.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import (
    CSTransformerErrorReactionEnum,
    EndToEndTransformationISignalProps,
    TransformationISignalProps,
)
from armodel.parser.arxml_parser import ARXMLParser

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
    "<END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-VARIANTS>"
    "<END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-CONDITIONAL>"
    "<CS-ERROR-REACTION>AUTONOMOUS</CS-ERROR-REACTION>"
    "<DATA-PROTOTYPE-TRANSFORMATION-PROPSS>"
    "<DATA-PROTOTYPE-TRANSFORMATION-PROPS>"
    '<TRANSFORMATION-PROPS-REF DEST="SOMEIP-TRANSFORMATION-PROPS">/Transformers/SomeipProps</TRANSFORMATION-PROPS-REF>'
    "</DATA-PROTOTYPE-TRANSFORMATION-PROPS>"
    "</DATA-PROTOTYPE-TRANSFORMATION-PROPSS>"
    '<TRANSFORMER-REF DEST="TRANSFORMATION-TECHNOLOGY">/Transformers/Serializer</TRANSFORMER-REF>'
    "</END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-CONDITIONAL>"
    "</END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-VARIANTS>"
)


class TestReadTransformationISignalProps:
    def test_read_full(self):
        props = EndToEndTransformationISignalProps()
        root = _snip(CONDITIONAL_XML)
        ARXMLParser().readEndToEndTransformationISignalProps(root, props)

        assert isinstance(props, TransformationISignalProps)
        cs_error_reaction = props.getCsErrorReaction()
        assert isinstance(cs_error_reaction, CSTransformerErrorReactionEnum)
        assert cs_error_reaction.getValue() == "AUTONOMOUS"

        dp_props_list = props.getDataPrototypeTransformationProps()
        assert len(dp_props_list) == 1
        assert dp_props_list[0].getTransformationPropsRef().getValue() == "/Transformers/SomeipProps"
        assert dp_props_list[0].getTransformationPropsRef().getDest() == "SOMEIP-TRANSFORMATION-PROPS"

        assert props.getTransformerRef().getValue() == "/Transformers/Serializer"
        assert props.getTransformerRef().getDest() == "TRANSFORMATION-TECHNOLOGY"

    def test_read_empty(self):
        props = EndToEndTransformationISignalProps()
        root = _snip("<END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-VARIANTS>" "<END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-CONDITIONAL />" "</END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-VARIANTS>")
        ARXMLParser().readEndToEndTransformationISignalProps(root, props)

        assert props.getCsErrorReaction() is None
        assert props.getDataPrototypeTransformationProps() == []
        assert props.getTransformerRef() is None

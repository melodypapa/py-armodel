"""Parser tests for EndToEndTransformationISignalProps (Table 7.27, p.809).

Concrete subclass of TransformationISignalProps (Table 7.8) serialized through
the class-level atpVariation split wrapper END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-VARIANTS /
END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-CONDITIONAL (XSD group END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS,
AUTOSAR_00052.xsd l.54798). Content element order per XSD group
END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-CONTENT: DATA-IDS, DATA-LENGTH,
MAX-DATA-LENGTH, MIN-DATA-LENGTH, SOURCE-ID.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import EndToEndTransformationISignalProps
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
    '<TRANSFORMER-REF DEST="TRANSFORMATION-TECHNOLOGY">/Transformers/E2E</TRANSFORMER-REF>'
    "<DATA-IDS>"
    "<DATA-ID>1</DATA-ID>"
    "<DATA-ID>2</DATA-ID>"
    "</DATA-IDS>"
    "<DATA-LENGTH>64</DATA-LENGTH>"
    "<MAX-DATA-LENGTH>2032</MAX-DATA-LENGTH>"
    "<MIN-DATA-LENGTH>24</MIN-DATA-LENGTH>"
    "<SOURCE-ID>7</SOURCE-ID>"
    "</END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-CONDITIONAL>"
    "</END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-VARIANTS>"
)


class TestReadEndToEndTransformationISignalProps:
    def test_read_full(self):
        props = EndToEndTransformationISignalProps()
        root = _snip(CONDITIONAL_XML)
        ARXMLParser().readEndToEndTransformationISignalProps(root, props)

        transformer_ref = props.getTransformerRef()
        assert transformer_ref.getValue() == "/Transformers/E2E"
        assert transformer_ref.getDest() == "TRANSFORMATION-TECHNOLOGY"

        ids = props.getDataIds()
        assert [i.getValue() for i in ids] == [1, 2]

        assert props.getDataLength().getValue() == 64
        assert props.getMaxDataLength().getValue() == 2032
        assert props.getMinDataLength().getValue() == 24
        assert props.getSourceId().getValue() == 7

    def test_read_empty(self):
        props = EndToEndTransformationISignalProps()
        root = _snip("<END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-VARIANTS>" "<END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-CONDITIONAL />" "</END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-VARIANTS>")
        ARXMLParser().readEndToEndTransformationISignalProps(root, props)

        assert props.getTransformerRef() is None
        assert props.getDataIds() == []
        assert props.getDataLength() is None
        assert props.getMaxDataLength() is None
        assert props.getMinDataLength() is None
        assert props.getSourceId() is None

"""Writer round-trip tests for EndToEndTransformationISignalProps (Table 7.27, p.809).

Serialized through the class-level atpVariation split wrapper
END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-VARIANTS /
END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-CONDITIONAL; content element order per
XSD group END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-CONTENT: DATA-IDS,
DATA-LENGTH, MAX-DATA-LENGTH, MIN-DATA-LENGTH, SOURCE-ID (VARIATION-POINT,
sequenceOffset 10000, is not emitted — no Conditional model).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import EndToEndTransformationISignalProps
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    return ARXMLWriter()


def _parent():
    return ET.Element("PARENT")


def _ref(value, dest):
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


def _posint(value):
    p = PositiveInteger()
    p.setValue(str(value))
    return p


def _new_props():
    props = EndToEndTransformationISignalProps()
    props.setTransformerRef(_ref("/Transformers/E2E", "TRANSFORMATION-TECHNOLOGY"))
    props.addDataId(_posint(1))
    props.addDataId(_posint(2))
    props.setDataLength(_posint(64))
    props.setMaxDataLength(_posint(2032))
    props.setMinDataLength(_posint(24))
    props.setSourceId(_posint(7))
    return props


class TestWriteEndToEndTransformationISignalProps:
    def test_full(self, writer):
        props = _new_props()
        parent = _parent()
        writer.writeEndToEndTransformationISignalProps(parent, props)

        node = parent.find("END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS")
        assert node is not None
        cond = node.find("END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-VARIANTS/END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-CONDITIONAL")
        assert cond is not None

        transformer_ref = cond.find("TRANSFORMER-REF")
        assert transformer_ref.text == "/Transformers/E2E"
        assert transformer_ref.attrib["DEST"] == "TRANSFORMATION-TECHNOLOGY"

        ids_wrapper = cond.find("DATA-IDS")
        assert ids_wrapper is not None
        ids = ids_wrapper.findall("DATA-ID")
        assert [id.text for id in ids] == ["1", "2"]

        assert cond.find("DATA-LENGTH").text == "64"
        assert cond.find("MAX-DATA-LENGTH").text == "2032"
        assert cond.find("MIN-DATA-LENGTH").text == "24"
        assert cond.find("SOURCE-ID").text == "7"

    def test_xsd_content_element_order(self, writer):
        props = _new_props()
        parent = _parent()
        writer.writeEndToEndTransformationISignalProps(parent, props)

        cond = parent.find("END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS/END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-VARIANTS/END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-CONDITIONAL")
        children = [child.tag for child in cond]
        assert children == ["TRANSFORMER-REF", "DATA-IDS", "DATA-LENGTH", "MAX-DATA-LENGTH", "MIN-DATA-LENGTH", "SOURCE-ID"]

    def test_empty(self, writer):
        props = EndToEndTransformationISignalProps()
        parent = _parent()
        writer.writeEndToEndTransformationISignalProps(parent, props)

        cond = parent.find("END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS/END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-VARIANTS/END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-CONDITIONAL")
        assert cond is not None
        assert cond.find("DATA-IDS") is None
        assert cond.find("DATA-LENGTH") is None
        assert cond.find("MAX-DATA-LENGTH") is None
        assert cond.find("MIN-DATA-LENGTH") is None
        assert cond.find("SOURCE-ID") is None

    def test_none(self, writer):
        parent = _parent()
        writer.writeEndToEndTransformationISignalProps(parent, None)
        assert len(parent) == 0

    def test_round_trip(self, writer):
        props = _new_props()
        parent = _parent()
        writer.writeEndToEndTransformationISignalProps(parent, props)

        reparsed = ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))
        new_props = EndToEndTransformationISignalProps()
        ARXMLParser().readEndToEndTransformationISignalProps(reparsed[0], new_props)

        assert new_props.getTransformerRef().getValue() == "/Transformers/E2E"
        assert new_props.getTransformerRef().getDest() == "TRANSFORMATION-TECHNOLOGY"
        assert [i.getValue() for i in new_props.getDataIds()] == [1, 2]
        assert new_props.getDataLength().getValue() == 64
        assert new_props.getMaxDataLength().getValue() == 2032
        assert new_props.getMinDataLength().getValue() == 24
        assert new_props.getSourceId().getValue() == 7

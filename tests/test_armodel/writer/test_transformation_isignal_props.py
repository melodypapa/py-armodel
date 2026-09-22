"""Writer round-trip tests for TransformationISignalProps (Table 7.8, p.772).

Content element order per XSD group TRANSFORMATION-I-SIGNAL-PROPS-CONTENT:
CS-ERROR-REACTION, DATA-PROTOTYPE-TRANSFORMATION-PROPSS, TRANSFORMER-REF.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import (
    CSTransformerErrorReactionEnum,
    DataPrototypeTransformationProps,
    EndToEndTransformationISignalProps,
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
    props = EndToEndTransformationISignalProps()
    props.setCsErrorReaction(CSTransformerErrorReactionEnum().setValue(CSTransformerErrorReactionEnum.AUTONOMOUS))

    dp_props = DataPrototypeTransformationProps()
    ref = RefType()
    ref.setDest("SOMEIP-TRANSFORMATION-PROPS")
    ref.setValue("/Transformers/SomeipProps")
    dp_props.setTransformationPropsRef(ref)
    props.addDataPrototypeTransformationProps(dp_props)

    transformer_ref = RefType()
    transformer_ref.setDest("TRANSFORMATION-TECHNOLOGY")
    transformer_ref.setValue("/Transformers/Serializer")
    props.setTransformerRef(transformer_ref)
    return props


class TestWriteTransformationISignalProps:
    def test_write_content_in_xsd_order(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeTransformationISignalProps(parent, _new_props())
        children = [child.tag for child in parent]
        assert children == ["CS-ERROR-REACTION", "DATA-PROTOTYPE-TRANSFORMATION-PROPSS"]
        assert parent.find("CS-ERROR-REACTION").text == "AUTONOMOUS"
        dp_ref = parent.find("DATA-PROTOTYPE-TRANSFORMATION-PROPSS/DATA-PROTOTYPE-TRANSFORMATION-PROPS/TRANSFORMATION-PROPS-REF")
        assert dp_ref.text == "/Transformers/SomeipProps"
        assert dp_ref.attrib["DEST"] == "SOMEIP-TRANSFORMATION-PROPS"

    def test_write_empty_omits_optional_tags(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeTransformationISignalProps(parent, EndToEndTransformationISignalProps())
        assert len(list(parent)) == 0

    def test_round_trip_preserves_all_values(self):
        props = _new_props()
        parent = ET.Element("PARENT")
        ARXMLWriter().writeEndToEndTransformationISignalProps(parent, props)
        root = ET.fromstring("<ROOT xmlns='%s'>%s</ROOT>" % (NS, ET.tostring(parent).decode("utf-8")))
        parsed = EndToEndTransformationISignalProps()
        ARXMLParser().readEndToEndTransformationISignalProps(root[0][0], parsed)

        assert isinstance(parsed, EndToEndTransformationISignalProps)
        assert parsed.getCsErrorReaction().getValue() == "AUTONOMOUS"
        assert len(parsed.getDataPrototypeTransformationProps()) == 1
        assert parsed.getDataPrototypeTransformationProps()[0].getTransformationPropsRef().getValue() == "/Transformers/SomeipProps"
        assert parsed.getTransformerRef().getValue() == "/Transformers/Serializer"
        assert parsed.getTransformerRef().getDest() == "TRANSFORMATION-TECHNOLOGY"

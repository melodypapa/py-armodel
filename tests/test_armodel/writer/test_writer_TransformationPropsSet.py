"""Writer/reader round-trip tests for TransformationPropsSet (Table 7.14, p.782)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import TransformationPropsSet
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    String,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import (
    SOMEIPTransformationProps,
    UserDefinedTransformationProps,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    autosar = AUTOSAR.getInstance()
    autosar.new()
    autosar.setARRelease("R23-11")
    yield
    autosar.new()


@pytest.fixture
def writer():
    return ARXMLWriter()


@pytest.fixture
def parser():
    return ARXMLParser()


def _new_props_set():
    props_set = TransformationPropsSet(None, "tps")
    props_set.setUuid(String().setValue("5e6f7a8b-9c0d-4bcc-ddee-4a5b6c7d8e9f"))
    someip_props = props_set.createSOMEIPTransformationProps("someipProps")
    someip_props.setAlignment(PositiveInteger().setValue(8))
    someip_props.setSizeOfArrayLengthField(PositiveInteger().setValue(4))
    props_set.createUserDefinedTransformationProps("userProps")
    return props_set


class TestWriteTransformationPropsSet:
    def test_write_all_elements_in_xsd_order(self, writer):
        """
        The helper writes the SHORT-NAME first and the TRANSFORMATION-PROPSS wrapper
        (emitted only when non-empty) holding the concrete subtype elements in the
        XSD choice order.
        """
        parent = ET.Element("AR-PACKAGE")
        writer.writeTransformationPropsSet(parent, _new_props_set())

        element = parent[0]
        assert element.tag == "TRANSFORMATION-PROPS-SET"
        assert element.attrib["UUID"] == "5e6f7a8b-9c0d-4bcc-ddee-4a5b6c7d8e9f"
        assert [child.tag for child in element][0] == "SHORT-NAME"
        assert element.find("SHORT-NAME").text == "tps"
        wrapper = element.find("TRANSFORMATION-PROPSS")
        assert [child.tag for child in wrapper] == [
            "SOMEIP-TRANSFORMATION-PROPS",
            "USER-DEFINED-TRANSFORMATION-PROPS",
        ]
        assert wrapper[0].find("SHORT-NAME").text == "someipProps"
        assert wrapper[0].find("ALIGNMENT").text == "8"
        assert wrapper[0].find("SIZE-OF-ARRAY-LENGTH-FIELD").text == "4"
        assert wrapper[1].find("SHORT-NAME").text == "userProps"

    def test_write_empty_element(self, writer):
        """
        A set without transformation props emits no TRANSFORMATION-PROPSS wrapper.
        """
        parent = ET.Element("AR-PACKAGE")
        writer.writeTransformationPropsSet(parent, TransformationPropsSet(None, "tps"))

        element = parent[0]
        assert element.find("TRANSFORMATION-PROPSS") is None


class TestTransformationPropsSetRoundTrip:
    def test_round_trip_preserves_field_values(self, writer, parser):
        """
        Write -> serialize -> parse keeps every field value including the concrete
        subtype elements inside the TRANSFORMATION-PROPSS wrapper.
        """
        parent = ET.Element("AR-PACKAGE")
        writer.writeTransformationPropsSet(parent, _new_props_set())
        xml = ET.tostring(parent[0], encoding="unicode")

        parsed_element = ET.fromstring("<WRAP xmlns='%s'>%s</WRAP>" % (NS, xml))[0]
        props_set = parser.readTransformationPropsSet(parsed_element, TransformationPropsSet(None, "tps"))

        assert props_set.getShortName() == "tps"
        assert props_set.getUuid().getValue() == "5e6f7a8b-9c0d-4bcc-ddee-4a5b6c7d8e9f"
        props_list = props_set.getTransformationProps()
        assert len(props_list) == 2
        assert isinstance(props_list[0], SOMEIPTransformationProps)
        assert props_list[0].getShortName() == "someipProps"
        assert props_list[0].getAlignment().getValue() == 8
        assert props_list[0].getSizeOfArrayLengthField().getValue() == 4
        assert isinstance(props_list[1], UserDefinedTransformationProps)
        assert props_list[1].getShortName() == "userProps"

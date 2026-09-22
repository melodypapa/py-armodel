"""Writer round-trip tests for DataTransformationSet (Table 7.1, p.763).

XML element order per XSD group DATA-TRANSFORMATION-SET: DATA-TRANSFORMATIONS,
TRANSFORMATION-TECHNOLOGYS.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, RefType, String
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import DataTransformationSet
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class _MockParent(ARObject):
    def __init__(self):
        super().__init__()


def _new_set():
    data_set = DataTransformationSet(_MockParent(), "Transformers")

    dtf = data_set.createDataTransformation("Chain")
    enabled = Boolean()
    enabled.setValue(True)
    dtf.setExecuteDespiteDataUnavailability(enabled)
    ref = RefType()
    ref.setDest("TRANSFORMATION-TECHNOLOGY")
    ref.setValue("/Transformers/Serializer")
    dtf.addTransformerChainRef(ref)

    tech = data_set.createTransformationTechnology("Serializer")
    protocol = String()
    protocol.setValue("SOME/IP")
    tech.setProtocol(protocol)
    return data_set


class TestWriteDataTransformationSet:
    def test_write_wrappers_in_xsd_order(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDataTransformationSet(parent, _new_set())
        node = parent.find("DATA-TRANSFORMATION-SET")
        assert node is not None
        children = [child.tag for child in node]
        assert children == ["SHORT-NAME", "DATA-TRANSFORMATIONS", "TRANSFORMATION-TECHNOLOGYS"]
        dtf = node.find("DATA-TRANSFORMATIONS/DATA-TRANSFORMATION")
        assert dtf is not None
        assert dtf.find("SHORT-NAME").text == "Chain"
        assert dtf.find("EXECUTE-DESPITE-DATA-UNAVAILABILITY").text == "true"
        chain_ref = dtf.find("TRANSFORMER-CHAIN-REFS/TRANSFORMER-CHAIN-REF")
        assert chain_ref.text == "/Transformers/Serializer"
        assert chain_ref.attrib["DEST"] == "TRANSFORMATION-TECHNOLOGY"
        tech = node.find("TRANSFORMATION-TECHNOLOGYS/TRANSFORMATION-TECHNOLOGY")
        assert tech is not None
        assert tech.find("SHORT-NAME").text == "Serializer"
        assert tech.find("PROTOCOL").text == "SOME/IP"

    def test_write_empty_set_omits_wrapper_tags(self):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDataTransformationSet(parent, DataTransformationSet(_MockParent(), "Empty"))
        node = parent.find("DATA-TRANSFORMATION-SET")
        assert node is not None
        assert node.find("DATA-TRANSFORMATIONS") is None
        assert node.find("TRANSFORMATION-TECHNOLOGYS") is None

    def test_round_trip_preserves_all_values(self):
        data_set = _new_set()
        parent = ET.Element("PARENT")
        ARXMLWriter().writeDataTransformationSet(parent, data_set)
        root = ET.fromstring("<AUTOSAR xmlns='%s'>%s</AUTOSAR>" % (NS, ET.tostring(parent).decode("utf-8")))
        parsed = DataTransformationSet(_MockParent(), "Transformers")
        ARXMLParser().readDataTransformationSet(root[0][0], parsed)

        assert len(parsed.getDataTransformations()) == 1
        dtf = parsed.getDataTransformations()[0]
        assert dtf.getShortName() == "Chain"
        assert dtf.getExecuteDespiteDataUnavailability().getValue() is True
        assert len(dtf.getTransformerChainRefs()) == 1
        assert dtf.getTransformerChainRefs()[0].getValue() == "/Transformers/Serializer"
        assert dtf.getTransformerChainRefs()[0].getDest() == "TRANSFORMATION-TECHNOLOGY"

        assert len(parsed.getTransformationTechnologies()) == 1
        tech = parsed.getTransformationTechnologies()[0]
        assert tech.getShortName() == "Serializer"
        assert tech.getProtocol().getValue() == "SOME/IP"

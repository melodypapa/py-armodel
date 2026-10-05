"""Writer/parser round-trip tests for the Transformer classes
(CP_TPS_SoftwareComponentTemplate Tables 4.39, 4.40, 4.87).

XML element order per the XSD groups DATA-TRANSFORMATION and
TRANSFORMATION-TECHNOLOGY (AUTOSAR_00052.xsd): DATA-TRANSFORMATION-KIND,
EXECUTE-DESPITE-DATA-UNAVAILABILITY, TRANSFORMER-CHAIN-REFS; BUFFER-PROPERTIES,
HAS-INTERNAL-STATE, NEEDS-ORIGINAL-DATA, PROTOCOL, TRANSFORMATION-DESCRIPTIONS,
TRANSFORMER-CLASS, VERSION.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARPackage
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, RefType, String
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import (
    BufferProperties,
    DataTransformation,
    DataTransformationKindEnum,
    DataTransformationSet,
    EndToEndTransformationDescription,
    TransformationTechnology,
    TransformerClassEnum,
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


def _build_document():
    document = AUTOSAR.getInstance()
    package = document.createARPackage("Transformers")
    dtf_set = package.createDataTransformationSet("Set")
    return document, package, dtf_set


def _serialize_package(package: ARPackage) -> str:
    element = ET.Element("ROOT")
    ARXMLWriter().writeARPackageElements(element, package)
    return ET.tostring(element).decode("utf-8")


class TestDataTransformationRoundTrip:
    def test_round_trip_field_values(self, tmp_path):
        document, package, dtf_set = _build_document()
        dtf = dtf_set.createDataTransformation("Chain")
        dtf.setDataTransformationKind(DataTransformationKindEnum().setValue("ASYMMETRIC-TO-BYTE-ARRAY"))
        dtf.setExecuteDespiteDataUnavailability(Boolean().setValue(True))
        ref = RefType()
        ref.setDest("TRANSFORMATION-TECHNOLOGY")
        ref.setValue("/Transformers/Set/Serializer")
        dtf.addTransformerChainRef(ref)
        tech = dtf_set.createTransformationTechnology("Serializer")
        tech.setProtocol(String().setValue("SOME/IP"))

        file_name = str(tmp_path / "transformer.arxml")
        ARXMLWriter().save(file_name, document)

        reload = AUTOSAR.getInstance()
        reload.clear()
        reload.setARRelease("R23-11")
        ARXMLParser().load(file_name, reload)

        dtf_set2 = reload.find("/Transformers/Set")
        assert isinstance(dtf_set2, DataTransformationSet)

        dtf2 = dtf_set2.getDataTransformations()[0]
        assert isinstance(dtf2, DataTransformation)
        assert dtf2.getShortName() == "Chain"
        assert dtf2.getDataTransformationKind().getValue() == "ASYMMETRIC-TO-BYTE-ARRAY"
        assert dtf2.getExecuteDespiteDataUnavailability().getValue() is True
        assert len(dtf2.getTransformerChainRefs()) == 1
        assert dtf2.getTransformerChainRefs()[0].getValue() == "/Transformers/Set/Serializer"
        assert dtf2.getTransformerChainRefs()[0].getDest() == "TRANSFORMATION-TECHNOLOGY"

        tech2 = dtf_set2.getTransformationTechnologies()[0]
        assert isinstance(tech2, TransformationTechnology)
        assert tech2.getProtocol().getValue() == "SOME/IP"

    def test_empty_wrapper_not_emitted(self):
        document, package, dtf_set = _build_document()
        dtf_set.createDataTransformation("Chain")

        xml = _serialize_package(package)

        assert "TRANSFORMER-CHAIN-REFS" not in xml
        assert "VARIATION-POINT" not in xml


class TestTransformationTechnologyRoundTrip:
    def test_round_trip_field_values(self, tmp_path):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger

        document, package, dtf_set = _build_document()
        tech = dtf_set.createTransformationTechnology("Tech")
        buffer_props = tech.getBufferProperties()
        assert buffer_props is None
        tech.setBufferProperties(BufferProperties().setHeaderLength(PositiveInteger().setValue("24")).setInPlace(Boolean().setValue(True)))
        tech.setHasInternalState(Boolean().setValue(True))
        tech.setNeedsOriginalData(Boolean().setValue(False))
        tech.setProtocol(String().setValue("EndToEnd"))
        desc = EndToEndTransformationDescription()
        desc.setCrcOffset(PositiveInteger().setValue("8"))
        tech.setTransformationDescription(desc)
        tech.setTransformerClass(TransformerClassEnum().setValue("SAFETY"))
        tech.setVersion(String().setValue("2.0"))

        file_name = str(tmp_path / "technology.arxml")
        ARXMLWriter().save(file_name, document)

        reload = AUTOSAR.getInstance()
        reload.clear()
        reload.setARRelease("R23-11")
        ARXMLParser().load(file_name, reload)

        dtf_set2 = reload.find("/Transformers/Set")
        tech2 = dtf_set2.getTransformationTechnologies()[0]
        assert isinstance(tech2, TransformationTechnology)
        assert tech2.getShortName() == "Tech"
        assert tech2.getBufferProperties().getHeaderLength().getValue() == 24
        assert tech2.getBufferProperties().getInPlace().getValue() is True
        assert tech2.getHasInternalState().getValue() is True
        assert tech2.getNeedsOriginalData().getValue() is False
        assert tech2.getProtocol().getValue() == "EndToEnd"
        desc2 = tech2.getTransformationDescription()
        assert isinstance(desc2, EndToEndTransformationDescription)
        assert desc2.getCrcOffset().getValue() == 8
        assert tech2.getTransformerClass().getValue() == "SAFETY"
        assert tech2.getVersion().getValue() == "2.0"

    def test_element_order_and_empty_wrappers(self):
        document, package, dtf_set = _build_document()
        tech = dtf_set.createTransformationTechnology("Tech")
        tech.setHasInternalState(Boolean().setValue(True))

        xml = _serialize_package(package)

        assert "TRANSFORMATION-TECHNOLOGYS" in xml
        tech_element = xml[xml.index("<TRANSFORMATION-TECHNOLOGY>") : xml.index("</TRANSFORMATION-TECHNOLOGY>")]
        assert "BUFFER-PROPERTIES" not in tech_element
        assert "TRANSFORMATION-DESCRIPTIONS" not in tech_element
        assert "VARIATION-POINT" not in tech_element
        assert "HAS-INTERNAL-STATE" in tech_element
        assert "VERSION" not in tech_element

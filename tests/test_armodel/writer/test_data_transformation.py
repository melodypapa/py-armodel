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
    DataTransformation,
    DataTransformationKindEnum,
    DataTransformationSet,
    TransformationTechnology,
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
        dtf.setDataTransformationKind(DataTransformationKindEnum().setValue(DataTransformationKindEnum.ASYMMETRIC_TO_BYTE_ARRAY))
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
        assert dtf2.getDataTransformationKind().getValue() == "asymmetricToByteArray"
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

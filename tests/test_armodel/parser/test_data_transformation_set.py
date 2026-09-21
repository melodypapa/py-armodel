"""Parser tests for DataTransformationSet (Table 7.1, p.763).

Covers the ARPackage DATA-TRANSFORMATION-SET dispatch and the
readDataTransformationSet helper (DATA-TRANSFORMATIONS /
TRANSFORMATION-TECHNOLOGYS wrappers per XSD group order).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARPackage
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import DataTransformation, DataTransformationSet, TransformationTechnology
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class MockParent(ARObject):
    def __init__(self):
        super().__init__()

    @property
    def full_name(self) -> str:
        return ""


def _package_element(inner: str) -> ET.Element:
    xml = "<AR-PACKAGE xmlns='%s'>" "<SHORT-NAME>Transformers</SHORT-NAME>" "<ELEMENTS>%s</ELEMENTS>" "</AR-PACKAGE>" % (NS, inner)
    return ET.fromstring(xml)


def _read_package(inner: str) -> ARPackage:
    package_element = _package_element(inner)
    package = ARPackage(MockParent(), "Transformers")
    ARXMLParser().readARPackage(package_element, package)
    return package


class TestReadDataTransformationSet:
    def test_ar_package_dispatch(self):
        package = _read_package(
            "<DATA-TRANSFORMATION-SET><SHORT-NAME>TransformerSet</SHORT-NAME>"
            "<DATA-TRANSFORMATIONS><DATA-TRANSFORMATION><SHORT-NAME>Chain</SHORT-NAME>"
            "<EXECUTE-DESPITE-DATA-UNAVAILABILITY>true</EXECUTE-DESPITE-DATA-UNAVAILABILITY>"
            "</DATA-TRANSFORMATION></DATA-TRANSFORMATIONS>"
            "<TRANSFORMATION-TECHNOLOGYS><TRANSFORMATION-TECHNOLOGY><SHORT-NAME>Serializer</SHORT-NAME>"
            "<PROTOCOL>SOME/IP</PROTOCOL>"
            "</TRANSFORMATION-TECHNOLOGY></TRANSFORMATION-TECHNOLOGYS>"
            "</DATA-TRANSFORMATION-SET>"
        )

        elements = package.getElements()
        assert len(elements) == 1
        data_set = elements[0]
        assert isinstance(data_set, DataTransformationSet)
        assert data_set.getShortName() == "TransformerSet"
        assert isinstance(data_set.getDataTransformations()[0], DataTransformation)
        assert isinstance(data_set.getTransformationTechnologies()[0], TransformationTechnology)

    def test_read_field_values(self):
        package = _read_package(
            "<DATA-TRANSFORMATION-SET><SHORT-NAME>TransformerSet</SHORT-NAME>"
            "<DATA-TRANSFORMATIONS><DATA-TRANSFORMATION><SHORT-NAME>Chain</SHORT-NAME>"
            "<EXECUTE-DESPITE-DATA-UNAVAILABILITY>true</EXECUTE-DESPITE-DATA-UNAVAILABILITY>"
            '<TRANSFORMER-CHAIN-REFS><TRANSFORMER-CHAIN-REF DEST="TRANSFORMATION-TECHNOLOGY">/Transformers/Serializer</TRANSFORMER-CHAIN-REF></TRANSFORMER-CHAIN-REFS>'
            "</DATA-TRANSFORMATION></DATA-TRANSFORMATIONS>"
            "<TRANSFORMATION-TECHNOLOGYS><TRANSFORMATION-TECHNOLOGY><SHORT-NAME>Serializer</SHORT-NAME>"
            "<PROTOCOL>SOME/IP</PROTOCOL><VERSION>2.0</VERSION>"
            "</TRANSFORMATION-TECHNOLOGY></TRANSFORMATION-TECHNOLOGYS>"
            "</DATA-TRANSFORMATION-SET>"
        )

        data_set = package.getElements()[0]
        dtf = data_set.getDataTransformations()[0]
        assert dtf.getExecuteDespiteDataUnavailability().getValue() is True
        assert dtf.getTransformerChainRefs()[0].getValue() == "/Transformers/Serializer"
        assert dtf.getTransformerChainRefs()[0].getDest() == "TRANSFORMATION-TECHNOLOGY"
        tech = data_set.getTransformationTechnologies()[0]
        assert tech.getProtocol().getValue() == "SOME/IP"
        assert tech.getVersion().getValue() == "2.0"

    def test_read_empty_set(self):
        package = _read_package("<DATA-TRANSFORMATION-SET><SHORT-NAME>Empty</SHORT-NAME></DATA-TRANSFORMATION-SET>")

        data_set = package.getElements()[0]
        assert data_set.getDataTransformations() == []
        assert data_set.getTransformationTechnologies() == []

"""Writer/reader round-trip tests for E2EProfileCompatibilityProps (Table 4.93, p.202).

The expected XML uses the XSD-valid element spellings from
``autosar/R23-11/xsd/AUTOSAR_00052.xsd`` (group E-2-E-PROFILE-COMPATIBILITY-PROPS).
The class is aggregated by ARPackage.element, so the round-trip goes through the
ARPackage dispatch on both sides.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import E2EProfileCompatibilityProps
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    AUTOSAR.getInstance().new()
    document = AUTOSAR.getInstance()
    document.setARRelease("R23-11")
    return ARXMLWriter()


@pytest.fixture
def parser():
    AUTOSAR.getInstance().new()
    document = AUTOSAR.getInstance()
    document.setARRelease("R23-11")
    return ARXMLParser()


class TestE2EProfileCompatibilityPropsWriter:
    def test_write_transit_to_invalid_extended_true(self, writer):
        package = AUTOSAR.getInstance().createARPackage("E2EProfileCompatibilityPropsCollection")
        props = package.createE2EProfileCompatibilityProps("Props")
        props.setTransitToInvalidExtended(Boolean().setValue("true"))

        parent = ET.Element("PARENT")
        writer.writeE2EProfileCompatibilityProps(parent, props)

        assert len(parent) == 1
        child = parent[0]
        assert child.tag == "E-2-E-PROFILE-COMPATIBILITY-PROPS"
        assert child.find("TRANSIT-TO-INVALID-EXTENDED") is not None
        assert child.find("TRANSIT-TO-INVALID-EXTENDED").text == "true"

    def test_write_empty_omits_attribute(self, writer):
        package = AUTOSAR.getInstance().createARPackage("E2EProfileCompatibilityPropsCollection")
        props = package.createE2EProfileCompatibilityProps("Props")

        parent = ET.Element("PARENT")
        writer.writeE2EProfileCompatibilityProps(parent, props)

        assert len(parent) == 1
        assert parent[0].tag == "E-2-E-PROFILE-COMPATIBILITY-PROPS"
        assert parent[0].find("TRANSIT-TO-INVALID-EXTENDED") is None

    def test_write_none(self, writer):
        parent = ET.Element("PARENT")
        writer.writeE2EProfileCompatibilityProps(parent, None)

        assert len(parent) == 0

    def test_write_arpackage_dispatch(self, writer):
        """Test that the ARPackage element dispatcher routes E2EProfileCompatibilityProps to the dedicated writer."""
        package = AUTOSAR.getInstance().createARPackage("E2EProfileCompatibilityPropsCollection")
        props = package.createE2EProfileCompatibilityProps("Props")
        props.setTransitToInvalidExtended(Boolean().setValue("false"))

        parent = ET.Element("AR-PACKAGE")
        writer.writeARPackageElements(parent, package)

        child = parent.find("ELEMENTS/E-2-E-PROFILE-COMPATIBILITY-PROPS")
        assert child is not None
        assert child.find("TRANSIT-TO-INVALID-EXTENDED").text == "false"


class TestE2EProfileCompatibilityPropsRoundTrip:
    def _round_trip(self, writer, parser, tmp_path, value):
        document = AUTOSAR.getInstance()
        document.setARRelease("R23-11")
        package = document.createARPackage("E2EProfileCompatibilityPropsCollection")
        props = package.createE2EProfileCompatibilityProps("Props")
        if value is not None:
            props.setTransitToInvalidExtended(Boolean().setValue(value))

        out_file = str(tmp_path / "e2e_profile_compatibility_props.arxml")
        writer.save(out_file, document)

        recovered = AUTOSAR.getInstance()
        recovered.clear()
        recovered.setARRelease("R23-11")
        parser.load(out_file, recovered)
        return recovered

    @pytest.mark.parametrize("value", ["true", "false"])
    def test_round_trip_preserves_value(self, writer, parser, tmp_path, value):
        recovered = self._round_trip(writer, parser, tmp_path, value)

        reloaded_pkg = recovered.getARPackages()[0]
        props = reloaded_pkg.getReferrableElement("Props", E2EProfileCompatibilityProps)
        assert props is not None
        assert props.getShortName() == "Props"
        assert props.getTransitToInvalidExtended() is not None
        assert props.getTransitToInvalidExtended().getValue() is (value == "true")

    def test_round_trip_empty_wrapper(self, writer, parser, tmp_path):
        recovered = self._round_trip(writer, parser, tmp_path, None)

        reloaded_pkg = recovered.getARPackages()[0]
        props = reloaded_pkg.getReferrableElement("Props", E2EProfileCompatibilityProps)
        assert props is not None
        assert props.getTransitToInvalidExtended() is None

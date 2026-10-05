"""Writer/reader round-trip tests for SwAxisType (Table 5.52, p.356).

The expected XML uses the XSD-valid element spellings from
``autosar/R23-11/xsd/AUTOSAR_00052.xsd`` (group SW-AXIS-TYPE,
element order SW-GENERIC-AXIS-DESC (sequenceOffset 20) then the
SW-GENERIC-AXIS-PARAM-TYPES wrapper (sequenceOffset 30)).
The class is aggregated by ARPackage.element, so the round-trip goes
through the ARPackage dispatch on both sides.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.MSR.DataDictionary.Axis import SwAxisType
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultiLanguageParagraph
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


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


def _make_desc() -> DocumentationBlock:
    desc = DocumentationBlock()
    desc.addP(MultiLanguageParagraph())
    return desc


class TestSwAxisTypeWriter:
    def test_write_element_order(self, writer):
        """Test the XSD sequenceOffset order: SW-GENERIC-AXIS-DESC before SW-GENERIC-AXIS-PARAM-TYPES."""
        package = AUTOSAR.getInstance().createARPackage("SwAxisTypes")
        axis_type = package.createSwAxisType("Axis")
        axis_type.setSwGenericAxisDesc(_make_desc())
        axis_type.createSwGenericAxisParamType("ParamA")

        parent = ET.Element("PARENT")
        writer.writeSwAxisType(parent, axis_type)

        assert len(parent) == 1
        child = parent[0]
        assert child.tag == "SW-AXIS-TYPE"
        tags = [c.tag for c in child]
        assert tags.index("SW-GENERIC-AXIS-DESC") < tags.index("SW-GENERIC-AXIS-PARAM-TYPES")

    def test_write_empty_omits_wrappers(self, writer):
        package = AUTOSAR.getInstance().createARPackage("SwAxisTypes")
        axis_type = package.createSwAxisType("Axis")

        parent = ET.Element("PARENT")
        writer.writeSwAxisType(parent, axis_type)

        assert len(parent) == 1
        assert parent[0].tag == "SW-AXIS-TYPE"
        assert parent[0].find("SW-GENERIC-AXIS-DESC") is None
        assert parent[0].find("SW-GENERIC-AXIS-PARAM-TYPES") is None

    def test_write_none(self, writer):
        parent = ET.Element("PARENT")
        writer.writeSwAxisType(parent, None)

        assert len(parent) == 0

    def test_write_arpackage_dispatch(self, writer):
        """Test that the ARPackage element dispatcher routes SwAxisType to the dedicated writer."""
        package = AUTOSAR.getInstance().createARPackage("SwAxisTypes")
        package.createSwAxisType("Axis")

        parent = ET.Element("AR-PACKAGE")
        writer.writeARPackageElements(parent, package)

        child = parent.find("ELEMENTS/SW-AXIS-TYPE")
        assert child is not None


class TestSwAxisTypeRoundTrip:
    def _round_trip(self, writer, parser, tmp_path, with_desc, with_params):
        document = AUTOSAR.getInstance()
        document.setARRelease("R23-11")
        package = document.createARPackage("SwAxisTypes")
        axis_type = package.createSwAxisType("Axis")
        if with_desc:
            axis_type.setSwGenericAxisDesc(_make_desc())
        if with_params:
            axis_type.createSwGenericAxisParamType("ParamA")
            axis_type.createSwGenericAxisParamType("ParamB")

        out_file = str(tmp_path / "sw_axis_type.arxml")
        writer.save(out_file, document)

        recovered = AUTOSAR.getInstance()
        recovered.clear()
        recovered.setARRelease("R23-11")
        parser.load(out_file, recovered)
        return recovered

    @pytest.mark.parametrize("with_desc,with_params", [(True, True), (True, False), (False, True), (False, False)])
    def test_round_trip_preserves_fields(self, writer, parser, tmp_path, with_desc, with_params):
        recovered = self._round_trip(writer, parser, tmp_path, with_desc, with_params)

        reloaded_pkg = recovered.getARPackages()[0]
        axis_type = reloaded_pkg.getReferrableElement("Axis", SwAxisType)
        assert axis_type is not None
        assert axis_type.getShortName() == "Axis"
        if with_desc:
            assert axis_type.getSwGenericAxisDesc() is not None
            assert len(axis_type.getSwGenericAxisDesc().getPs()) == 1
        else:
            assert axis_type.getSwGenericAxisDesc() is None
        if with_params:
            assert [pt.getShortName() for pt in axis_type.getSwGenericAxisParamTypes()] == ["ParamA", "ParamB"]
        else:
            assert axis_type.getSwGenericAxisParamTypes() == []

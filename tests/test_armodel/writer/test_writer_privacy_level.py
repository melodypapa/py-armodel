"""Tests for the writePrivacyLevel handler (R23-11 PrivacyLevel, Table 3.4, p.18)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType
from armodel.models.M2.AUTOSARTemplates.LogAndTraceExtract import PrivacyLevel
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

XSD_CHILD_ORDER = [
    "COMPU-METHOD-REF",
    "PRIVACY-LEVEL",
]

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    return ARXMLWriter()


@pytest.fixture
def parser():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    return ARXMLParser()


def _parent():
    return ET.Element("PARENT")


def _compu_method_ref():
    ref = RefType()
    ref.setDest("COMPU-METHOD")
    ref.setValue("/LogAndTrace/CompuMethods/PrivacyLevels")
    return ref


def _privacy_value():
    value = PositiveInteger()
    value.setValue("1")
    return value


def _fill(privacy_level):
    privacy_level.setCompuMethodRef(_compu_method_ref())
    privacy_level.setPrivacyLevel(_privacy_value())
    return privacy_level


class TestWritePrivacyLevel:
    """Tests for writePrivacyLevel handler (R23-11 PrivacyLevel, Table 3.4, p.18)."""

    def test_children_in_xsd_order(self, writer):
        parent = _parent()
        writer.writePrivacyLevel(parent, _fill(PrivacyLevel()))
        child = parent.find("PRIVACY-LEVEL")
        assert child is not None
        child_tags = [element.tag for element in child]
        assert child_tags == XSD_CHILD_ORDER
        compu_method_ref = child.find("COMPU-METHOD-REF")
        assert compu_method_ref.text == "/LogAndTrace/CompuMethods/PrivacyLevels"
        assert compu_method_ref.get("DEST") == "COMPU-METHOD"
        assert child.find("PRIVACY-LEVEL").text == "1"

    def test_empty_children_omitted(self, writer):
        parent = _parent()
        writer.writePrivacyLevel(parent, PrivacyLevel())
        child = parent.find("PRIVACY-LEVEL")
        assert child is not None
        for tag in XSD_CHILD_ORDER:
            assert child.find(tag) is None

    def test_round_trip_write_then_read(self, writer, parser):
        parent = _parent()
        writer.writePrivacyLevel(parent, _fill(PrivacyLevel()))
        child = parent.find("PRIVACY-LEVEL")
        fragment = ET.tostring(child, encoding="unicode")

        reloaded = ET.fromstring(f"<ROOT xmlns='{NS}'>{fragment}</ROOT>")
        parsed = PrivacyLevel()
        parser.readPrivacyLevel(reloaded.find(f"{{{NS}}}PRIVACY-LEVEL"), parsed)
        assert parsed.getCompuMethodRef().getValue() == "/LogAndTrace/CompuMethods/PrivacyLevels"
        assert parsed.getCompuMethodRef().getDest() == "COMPU-METHOD"
        assert parsed.getPrivacyLevel().getValue() == 1

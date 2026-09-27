"""Writer tests for MemorySection and SectionNamePrefix (writeMemorySections / writeSectionNamePrefixes)."""

import xml.etree.cElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption import ResourceConsumption
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AlignmentType,
    CIdentifier,
    Identifier,
    PositiveInteger,
    RefType,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import VariationPoint
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


def _make_ref(dest, value):
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


def _make_positive_int(text):
    val = PositiveInteger()
    val.setValue(text)
    return val


def _make_vp(label):
    vp = VariationPoint()
    vp.setShortLabel(Identifier().setValue(label))
    return vp


def _consumption_with_full_section():
    consumption = ResourceConsumption(AUTOSAR.getInstance().createARPackage("Pkg"), "RC")
    section = consumption.createMemorySection("MemSec")
    section.setAlignment(AlignmentType().setValue("16"))
    section.addExecutableEntityRef(_make_ref("EXECUTABLE-ENTITY", "/Swc/Entity"))
    section.setMemClassSymbol(CIdentifier().setValue("MEMCLASS"))
    section.addOption(Identifier().setValue("INLINE"))
    section.addOption(Identifier().setValue("LOCAL_INLINE"))
    section.setPrefixRef(_make_ref("SECTION-NAME-PREFIX", "/Pkg/Prefix"))
    section.setSize(_make_positive_int("128"))
    section.setSwAddrMethodRef(_make_ref("SW-ADDR-METHOD", "/Pkg/AddrMethod"))
    section.setSymbol(Identifier().setValue("SecSym"))
    section.setVariationPoint(_make_vp("VP1"))
    return consumption


class TestWriteMemorySections:
    def test_write_field_values(self, writer):
        consumption = _consumption_with_full_section()
        parent = _parent()
        writer.writeMemorySections(parent, consumption)
        assert len(parent) == 1
        sections_tag = parent[0]
        assert sections_tag.tag == "MEMORY-SECTIONS"
        mem = sections_tag[0]
        assert mem.tag == "MEMORY-SECTION"
        assert mem.find("SHORT-NAME").text == "MemSec"
        assert mem.find("ALIGNMENT").text == "16"
        assert mem.find("MEM-CLASS-SYMBOL").text == "MEMCLASS"
        assert [o.text for o in mem.findall("OPTIONS/OPTION")] == ["INLINE", "LOCAL_INLINE"]
        assert mem.find("SIZE").text == "128"
        assert mem.find("SYMBOL").text == "SecSym"
        ref = mem.find("EXECUTABLE-ENTITY-REFS/EXECUTABLE-ENTITY-REF")
        assert ref.get("DEST") == "EXECUTABLE-ENTITY"
        assert ref.text == "/Swc/Entity"
        assert mem.find("PREFIX-REF").get("DEST") == "SECTION-NAME-PREFIX"
        assert mem.find("PREFIX-REF").text == "/Pkg/Prefix"
        assert mem.find("SW-ADDRMETHOD-REF").get("DEST") == "SW-ADDR-METHOD"
        assert mem.find("SW-ADDRMETHOD-REF").text == "/Pkg/AddrMethod"

    def test_write_xsd_element_order(self, writer):
        """Children follow the XSD sequenceOffset order of group MEMORY-SECTION (VARIATION-POINT last)."""
        consumption = _consumption_with_full_section()
        parent = _parent()
        writer.writeMemorySections(parent, consumption)
        mem = parent[0][0]
        tags = [c.tag for c in mem]
        assert tags == [
            "SHORT-NAME",
            "ALIGNMENT",
            "EXECUTABLE-ENTITY-REFS",
            "MEM-CLASS-SYMBOL",
            "OPTIONS",
            "PREFIX-REF",
            "SIZE",
            "SW-ADDRMETHOD-REF",
            "SYMBOL",
            "VARIATION-POINT",
        ]

    def test_write_variation_point(self, writer):
        consumption = _consumption_with_full_section()
        parent = _parent()
        writer.writeMemorySections(parent, consumption)
        mem = parent[0][0]
        vp = mem.find("VARIATION-POINT")
        assert vp is not None
        assert vp.find("SHORT-LABEL").text == "VP1"

    def test_write_empty_consumption(self, writer):
        consumption = ResourceConsumption(AUTOSAR.getInstance().createARPackage("Pkg"), "RC")
        parent = _parent()
        writer.writeMemorySections(parent, consumption)
        assert len(parent) == 0


def _consumption_with_full_prefix():
    consumption = ResourceConsumption(AUTOSAR.getInstance().createARPackage("Pkg"), "RC")
    prefix = consumption.createSectionNamePrefix("Prefix")
    prefix.setSymbol(Identifier().setValue("PfxSym"))
    prefix.setImplementedInRef(_make_ref("AUTOSAR-ENGINEERING-OBJECT", "/Pkg/Header"))
    prefix.setVariationPoint(_make_vp("VP2"))
    return consumption


class TestWriteSectionNamePrefixes:
    def test_write_prefix_fields(self, writer):
        consumption = _consumption_with_full_prefix()
        parent = _parent()
        writer.writeSectionNamePrefixes(parent, consumption.getSectionNamePrefixes())
        assert len(parent) == 1
        prefixes_tag = parent[0]
        assert prefixes_tag.tag == "SECTION-NAME-PREFIXS"
        prefix = prefixes_tag[0]
        assert prefix.tag == "SECTION-NAME-PREFIX"
        assert prefix.find("SHORT-NAME").text == "Prefix"
        assert prefix.find("IMPLEMENTED-IN-REF").get("DEST") == "AUTOSAR-ENGINEERING-OBJECT"
        assert prefix.find("IMPLEMENTED-IN-REF").text == "/Pkg/Header"

    def test_write_prefix_symbol(self, writer):
        """The inherited SYMBOL (IMPLEMENTATION-PROPS group) is written."""
        consumption = _consumption_with_full_prefix()
        parent = _parent()
        writer.writeSectionNamePrefixes(parent, consumption.getSectionNamePrefixes())
        prefix = parent[0][0]
        assert prefix.find("SYMBOL") is not None
        assert prefix.find("SYMBOL").text == "PfxSym"

    def test_write_prefix_variation_point(self, writer):
        consumption = _consumption_with_full_prefix()
        parent = _parent()
        writer.writeSectionNamePrefixes(parent, consumption.getSectionNamePrefixes())
        prefix = parent[0][0]
        vp = prefix.find("VARIATION-POINT")
        assert vp is not None
        assert vp.find("SHORT-LABEL").text == "VP2"

    def test_write_prefix_xsd_element_order(self, writer):
        """Children follow the XSD group order: REFERRABLE, IMPLEMENTATION-PROPS, SECTION-NAME-PREFIX (VARIATION-POINT last)."""
        consumption = _consumption_with_full_prefix()
        parent = _parent()
        writer.writeSectionNamePrefixes(parent, consumption.getSectionNamePrefixes())
        prefix = parent[0][0]
        assert [c.tag for c in prefix] == ["SHORT-NAME", "SYMBOL", "IMPLEMENTED-IN-REF", "VARIATION-POINT"]

    def test_write_empty_prefix_list(self, writer):
        parent = _parent()
        writer.writeSectionNamePrefixes(parent, [])
        assert len(parent) == 0

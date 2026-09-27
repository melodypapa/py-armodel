"""Parser tests for MemorySection and SectionNamePrefix (readMemorySections / readSectionNamePrefixes)."""

import xml.etree.ElementTree as ET

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
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"

MEMORY_SECTIONS_XML = (
    "<ROOT xmlns='{ns}'>"
    "<MEMORY-SECTIONS>"
    "<MEMORY-SECTION>"
    "<SHORT-NAME>MemSec</SHORT-NAME>"
    "<ALIGNMENT>16</ALIGNMENT>"
    "<EXECUTABLE-ENTITY-REFS>"
    "<EXECUTABLE-ENTITY-REF DEST='EXECUTABLE-ENTITY'>/Swc/Entity</EXECUTABLE-ENTITY-REF>"
    "</EXECUTABLE-ENTITY-REFS>"
    "<MEM-CLASS-SYMBOL>MEMCLASS</MEM-CLASS-SYMBOL>"
    "<OPTIONS><OPTION>INLINE</OPTION><OPTION>LOCAL_INLINE</OPTION></OPTIONS>"
    "<PREFIX-REF DEST='SECTION-NAME-PREFIX'>/Pkg/Prefix</PREFIX-REF>"
    "<SIZE>128</SIZE>"
    "<SW-ADDRMETHOD-REF DEST='SW-ADDR-METHOD'>/Pkg/AddrMethod</SW-ADDRMETHOD-REF>"
    "<SYMBOL>SecSym</SYMBOL>"
    "<VARIATION-POINT><SHORT-LABEL>VP1</SHORT-LABEL></VARIATION-POINT>"
    "</MEMORY-SECTION>"
    "</MEMORY-SECTIONS>"
    "</ROOT>"
).format(ns=NS)

@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    return ARXMLParser()


def _consumption():
    pkg = AUTOSAR.getInstance().createARPackage("Pkg")
    return ResourceConsumption(pkg, "RC")


class TestReadMemorySections:
    def test_read_typed_members(self, parser):
        """ALIGNMENT, MEM-CLASS-SYMBOL, OPTIONS items and SYMBOL read into their spec-typed instances."""
        consumption = _consumption()
        parser.readMemorySections(ET.fromstring(MEMORY_SECTIONS_XML), consumption)
        assert len(consumption.getMemorySections()) == 1
        section = consumption.getMemorySections()[0]
        assert isinstance(section.getAlignment(), AlignmentType)
        assert isinstance(section.getMemClassSymbol(), CIdentifier)
        assert isinstance(section.getSymbol(), Identifier)
        assert len(section.getOptions()) == 2
        for option in section.getOptions():
            assert isinstance(option, Identifier)
        assert isinstance(section.getSize(), PositiveInteger)

    def test_read_field_values(self, parser):
        consumption = _consumption()
        parser.readMemorySections(ET.fromstring(MEMORY_SECTIONS_XML), consumption)
        section = consumption.getMemorySections()[0]
        assert section.getShortName() == "MemSec"
        assert section.getAlignment().getValue() == "16"
        assert section.getMemClassSymbol().getValue() == "MEMCLASS"
        assert [o.getValue() for o in section.getOptions()] == ["INLINE", "LOCAL_INLINE"]
        assert section.getSize().getValue() == 128
        assert section.getSymbol().getValue() == "SecSym"
        refs = section.getExecutableEntityRefs()
        assert len(refs) == 1
        assert isinstance(refs[0], RefType)
        assert refs[0].getDest() == "EXECUTABLE-ENTITY"
        assert refs[0].value == "/Swc/Entity"
        assert section.getPrefixRef().getDest() == "SECTION-NAME-PREFIX"
        assert section.getPrefixRef().value == "/Pkg/Prefix"
        assert section.getSwAddrMethodRef().getDest() == "SW-ADDR-METHOD"
        assert section.getSwAddrMethodRef().value == "/Pkg/AddrMethod"

    def test_read_variation_point(self, parser):
        consumption = _consumption()
        parser.readMemorySections(ET.fromstring(MEMORY_SECTIONS_XML), consumption)
        section = consumption.getMemorySections()[0]
        assert section.getVariationPoint() is not None
        assert section.getVariationPoint().getShortLabel().getValue() == "VP1"

    def test_read_empty_section(self, parser):
        consumption = _consumption()
        element = ET.fromstring(f"<ROOT xmlns='{NS}'><MEMORY-SECTIONS><MEMORY-SECTION><SHORT-NAME>Empty</SHORT-NAME></MEMORY-SECTION></MEMORY-SECTIONS></ROOT>")
        parser.readMemorySections(element, consumption)
        section = consumption.getMemorySections()[0]
        assert section.getAlignment() is None
        assert section.getExecutableEntityRefs() == []
        assert section.getMemClassSymbol() is None
        assert section.getOptions() == []
        assert section.getPrefixRef() is None
        assert section.getSize() is None
        assert section.getSwAddrMethodRef() is None
        assert section.getSymbol() is None
        assert section.getVariationPoint() is None

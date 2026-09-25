"""
Tests for writing NV-BLOCK-NEEDS elements — NvBlockNeeds, Table 11.8 (p.680, R23-11).

NvBlockNeeds (Base = ServiceNeeds) carries 22 own attributes whose writer element order
must follow the XSD sequence (AUTOSAR_00052.xsd group NV-BLOCK-NEEDS): CALC-RAM-BLOCK-CRC
→ WRITING-PRIORITY. The NV-BLOCK-NEEDS element is emitted inline by writeNvBlockNeeds and
its round-trip goes through readNvBlockNeeds; the NvBlockDescriptor.nvBlockNeeds dispatch
is exercised through writeNvBlockDescriptor / readNvBlockDescriptor.

Round-trip counterpart: tests/test_armodel/parser/test_nv_block_needs.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import (
    NvBlockNeeds,
    NvBlockNeedsReliabilityEnum,
    NvBlockNeedsWritingPriorityEnum,
    RamBlockStatusControlEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, PositiveInteger, TimeValue
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import NvBlockDescriptor
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

XSD_ELEMENT_ORDER = [
    "SHORT-NAME",
    "CALC-RAM-BLOCK-CRC",
    "CHECK-STATIC-BLOCK-ID",
    "CYCLIC-WRITING-PERIOD",
    "N-DATA-SETS",
    "N-ROM-BLOCKS",
    "RAM-BLOCK-STATUS-CONTROL",
    "READONLY",
    "RELIABILITY",
    "RESISTANT-TO-CHANGED-SW",
    "RESTORE-AT-START",
    "SELECT-BLOCK-FOR-FIRST-INIT-ALL",
    "STORE-AT-SHUTDOWN",
    "STORE-CYCLIC",
    "STORE-EMERGENCY",
    "STORE-IMMEDIATE",
    "STORE-ON-CHANGE",
    "USE-AUTO-VALIDATION-AT-SHUT-DOWN",
    "USE-CRC-COMP-MECHANISM",
    "WRITE-ONLY-ONCE",
    "WRITE-VERIFICATION",
    "WRITING-FREQUENCY",
    "WRITING-PRIORITY",
]

ATTRIBUTE_TAGS = set(XSD_ELEMENT_ORDER[1:])


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    """Create ARXML writer instance."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    return ARXMLWriter()


def _bool(value: bool) -> Boolean:
    return Boolean().setValue(value)


def _filled_needs() -> NvBlockNeeds:
    needs = NvBlockNeeds(None, "nv")
    needs.setCalcRamBlockCrc(_bool(True))
    needs.setCheckStaticBlockId(_bool(False))
    needs.setCyclicWritingPeriod(TimeValue().setValue("0.005"))
    needs.setNDataSets(PositiveInteger().setValue("4"))
    needs.setNRomBlocks(PositiveInteger().setValue("3"))
    needs.setRamBlockStatusControl(RamBlockStatusControlEnum().setValue(RamBlockStatusControlEnum.API))
    needs.setReadonly(_bool(True))
    needs.setReliability(NvBlockNeedsReliabilityEnum().setValue(NvBlockNeedsReliabilityEnum.ERROR_CORRECTION))
    needs.setResistantToChangedSw(_bool(True))
    needs.setRestoreAtStart(_bool(False))
    needs.setSelectBlockForFirstInitAll(_bool(True))
    needs.setStoreAtShutdown(_bool(True))
    needs.setStoreCyclic(_bool(False))
    needs.setStoreEmergency(_bool(True))
    needs.setStoreImmediate(_bool(False))
    needs.setStoreOnChange(_bool(True))
    needs.setUseAutoValidationAtShutDown(_bool(True))
    needs.setUseCRCCompMechanism(_bool(False))
    needs.setWriteOnlyOnce(_bool(True))
    needs.setWriteVerification(_bool(False))
    needs.setWritingFrequency(PositiveInteger().setValue("10"))
    needs.setWritingPriority(NvBlockNeedsWritingPriorityEnum().setValue(NvBlockNeedsWritingPriorityEnum.HIGH))
    return needs


class TestWriteNvBlockNeeds:
    def _write(self, writer, needs: NvBlockNeeds) -> ET.Element:
        parent = ET.Element("ROOT")
        writer.writeNvBlockNeeds(parent, needs)
        return parent.find("NV-BLOCK-NEEDS")

    def test_write_all_attribute_values(self, writer):
        """Test that all 22 attribute elements are emitted with their field values."""
        elem = self._write(writer, _filled_needs())

        assert elem is not None
        assert elem.find("CALC-RAM-BLOCK-CRC").text == "true"
        assert elem.find("CHECK-STATIC-BLOCK-ID").text == "false"
        assert elem.find("CYCLIC-WRITING-PERIOD").text == "0.005"
        assert elem.find("N-DATA-SETS").text == "4"
        assert elem.find("N-ROM-BLOCKS").text == "3"
        assert elem.find("RAM-BLOCK-STATUS-CONTROL").text == "api"
        assert elem.find("READONLY").text == "true"
        assert elem.find("RELIABILITY").text == "errorCorrection"
        assert elem.find("RESISTANT-TO-CHANGED-SW").text == "true"
        assert elem.find("RESTORE-AT-START").text == "false"
        assert elem.find("SELECT-BLOCK-FOR-FIRST-INIT-ALL").text == "true"
        assert elem.find("STORE-AT-SHUTDOWN").text == "true"
        assert elem.find("STORE-CYCLIC").text == "false"
        assert elem.find("STORE-EMERGENCY").text == "true"
        assert elem.find("STORE-IMMEDIATE").text == "false"
        assert elem.find("STORE-ON-CHANGE").text == "true"
        assert elem.find("USE-AUTO-VALIDATION-AT-SHUT-DOWN").text == "true"
        assert elem.find("USE-CRC-COMP-MECHANISM").text == "false"
        assert elem.find("WRITE-ONLY-ONCE").text == "true"
        assert elem.find("WRITE-VERIFICATION").text == "false"
        assert elem.find("WRITING-FREQUENCY").text == "10"
        assert elem.find("WRITING-PRIORITY").text == "high"

    def test_xsd_element_order(self, writer):
        """Test that the emitted element order follows the XSD group sequence."""
        elem = self._write(writer, _filled_needs())

        children = [child.tag for child in elem]
        assert children == XSD_ELEMENT_ORDER

    def test_absent_elements_not_emitted(self, writer):
        """Test that a needs with no set field emits none of the attribute elements."""
        elem = self._write(writer, NvBlockNeeds(None, "nv"))

        assert elem is not None
        emitted = {child.tag for child in elem}
        assert emitted.isdisjoint(ATTRIBUTE_TAGS)


class TestNvBlockDescriptorDispatch:
    def test_write_nv_block_descriptor_nv_block_needs_field_values(self, writer):
        """Test the NvBlockDescriptor.nvBlockNeeds dispatch emits field values one level down."""
        descriptor = NvBlockDescriptor(None, "desc")
        descriptor.setNvBlockNeeds(_filled_needs())

        parent = ET.Element("ROOT")
        writer.writeNvBlockDescriptor(parent, descriptor)

        needs_element = parent.find("NV-BLOCK-DESCRIPTOR/NV-BLOCK-NEEDS")
        assert needs_element is not None
        assert needs_element.find("RAM-BLOCK-STATUS-CONTROL").text == "api"
        assert needs_element.find("STORE-ON-CHANGE").text == "true"


class TestWriteReadRoundTrip:
    def test_round_trip_field_values(self, writer):
        """Test that write and re-parse preserve every field value."""
        original = _filled_needs()

        parent = ET.Element("ROOT")
        writer.writeNvBlockNeeds(parent, original)
        xml = ET.tostring(parent.find("NV-BLOCK-NEEDS"), encoding="unicode")
        element = ET.fromstring(f"<ROOT xmlns='{NS}'>{xml}</ROOT>")

        parser = ARXMLParser()
        reloaded = NvBlockNeeds(None, "nv")
        parser.readNvBlockNeeds(element[0], reloaded)

        assert reloaded.getCalcRamBlockCrc().getValue() is True
        assert reloaded.getCheckStaticBlockId().getValue() is False
        assert reloaded.getCyclicWritingPeriod().getValue() == 0.005
        assert reloaded.getNDataSets().getValue() == 4
        assert reloaded.getNRomBlocks().getValue() == 3
        assert reloaded.getRamBlockStatusControl().getValue() == "api"
        assert reloaded.getReadonly().getValue() is True
        assert reloaded.getReliability().getValue() == "errorCorrection"
        assert reloaded.getResistantToChangedSw().getValue() is True
        assert reloaded.getRestoreAtStart().getValue() is False
        assert reloaded.getSelectBlockForFirstInitAll().getValue() is True
        assert reloaded.getStoreAtShutdown().getValue() is True
        assert reloaded.getStoreCyclic().getValue() is False
        assert reloaded.getStoreEmergency().getValue() is True
        assert reloaded.getStoreImmediate().getValue() is False
        assert reloaded.getStoreOnChange().getValue() is True
        assert reloaded.getUseAutoValidationAtShutDown().getValue() is True
        assert reloaded.getUseCRCCompMechanism().getValue() is False
        assert reloaded.getWriteOnlyOnce().getValue() is True
        assert reloaded.getWriteVerification().getValue() is False
        assert reloaded.getWritingFrequency().getValue() == 10
        assert reloaded.getWritingPriority().getValue() == "high"

    def test_round_trip_absent_elements(self, writer):
        """Test that a needs with no set fields round-trips to all-None."""
        parent = ET.Element("ROOT")
        writer.writeNvBlockNeeds(parent, NvBlockNeeds(None, "nv"))
        xml = ET.tostring(parent.find("NV-BLOCK-NEEDS"), encoding="unicode")
        element = ET.fromstring(f"<ROOT xmlns='{NS}'>{xml}</ROOT>")

        parser = ARXMLParser()
        reloaded = NvBlockNeeds(None, "nv")
        parser.readNvBlockNeeds(element[0], reloaded)

        assert reloaded.getCalcRamBlockCrc() is None
        assert reloaded.getCyclicWritingPeriod() is None
        assert reloaded.getRamBlockStatusControl() is None
        assert reloaded.getStoreOnChange() is None
        assert reloaded.getWritingPriority() is None

    def test_round_trip_through_nv_block_descriptor(self, writer):
        """Test the NvBlockDescriptor dispatch write → re-parse round-trip with field values."""
        descriptor = NvBlockDescriptor(None, "desc")
        descriptor.setNvBlockNeeds(_filled_needs())

        parent = ET.Element("ROOT")
        writer.writeNvBlockDescriptor(parent, descriptor)
        xml = ET.tostring(parent.find("NV-BLOCK-DESCRIPTOR"), encoding="unicode")
        element = ET.fromstring(f"<ROOT xmlns='{NS}'>{xml}</ROOT>")

        parser = ARXMLParser()
        reloaded_descriptor = NvBlockDescriptor(None, "desc")
        parser.readNvBlockDescriptor(element[0], reloaded_descriptor)

        needs = reloaded_descriptor.getNvBlockNeeds()
        assert needs is not None
        assert needs.getShortName() == "nv"
        assert needs.getRamBlockStatusControl().getValue() == "api"
        assert needs.getNDataSets().getValue() == 4
        assert needs.getStoreOnChange().getValue() is True
        assert needs.getWritingPriority().getValue() == "high"

"""
Tests for reading NV-BLOCK-NEEDS elements — NvBlockNeeds, Table 11.8 (p.680, R23-11).

NvBlockNeeds (Base = ServiceNeeds) carries 22 own attributes whose reader coverage must
match the XSD sequence (AUTOSAR_00052.xsd group NV-BLOCK-NEEDS). Dispatch consumers:
NvBlockDescriptor.nvBlockNeeds, BswServiceDependency.serviceNeeds and
SwcServiceDependency.serviceNeeds (the three "Aggregated by" rows of Table 11.8).

Round-trip counterpart: tests/test_armodel/writer/test_nv_block_needs.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior import BswServiceDependency
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import NvBlockNeeds
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.NvBlockComponent import NvBlockDescriptor
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ServiceMapping import SwcServiceDependency
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"

FULL_INNER = (
    "<SHORT-NAME>nv</SHORT-NAME>"
    "<CALC-RAM-BLOCK-CRC>true</CALC-RAM-BLOCK-CRC>"
    "<CHECK-STATIC-BLOCK-ID>false</CHECK-STATIC-BLOCK-ID>"
    "<CYCLIC-WRITING-PERIOD>0.005</CYCLIC-WRITING-PERIOD>"
    "<N-DATA-SETS>4</N-DATA-SETS>"
    "<N-ROM-BLOCKS>3</N-ROM-BLOCKS>"
    "<RAM-BLOCK-STATUS-CONTROL>api</RAM-BLOCK-STATUS-CONTROL>"
    "<READONLY>true</READONLY>"
    "<RELIABILITY>errorCorrection</RELIABILITY>"
    "<RESISTANT-TO-CHANGED-SW>true</RESISTANT-TO-CHANGED-SW>"
    "<RESTORE-AT-START>false</RESTORE-AT-START>"
    "<SELECT-BLOCK-FOR-FIRST-INIT-ALL>true</SELECT-BLOCK-FOR-FIRST-INIT-ALL>"
    "<STORE-AT-SHUTDOWN>true</STORE-AT-SHUTDOWN>"
    "<STORE-CYCLIC>false</STORE-CYCLIC>"
    "<STORE-EMERGENCY>true</STORE-EMERGENCY>"
    "<STORE-IMMEDIATE>false</STORE-IMMEDIATE>"
    "<STORE-ON-CHANGE>true</STORE-ON-CHANGE>"
    "<USE-AUTO-VALIDATION-AT-SHUT-DOWN>true</USE-AUTO-VALIDATION-AT-SHUT-DOWN>"
    "<USE-CRC-COMP-MECHANISM>false</USE-CRC-COMP-MECHANISM>"
    "<WRITE-ONLY-ONCE>true</WRITE-ONLY-ONCE>"
    "<WRITE-VERIFICATION>false</WRITE-VERIFICATION>"
    "<WRITING-FREQUENCY>10</WRITING-FREQUENCY>"
    "<WRITING-PRIORITY>high</WRITING-PRIORITY>"
)


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    """Create ARXML parser instance."""
    return ARXMLParser()


def _snip(inner: str, root_tag: str = "ROOT") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadNvBlockNeeds:
    def test_read_all_attribute_values(self, parser):
        """Test that readNvBlockNeeds populates every attribute with its field value."""
        needs = NvBlockNeeds(None, "nv")
        element = _snip(FULL_INNER, root_tag="NV-BLOCK-NEEDS")

        parser.readNvBlockNeeds(element, needs)

        assert needs.getCalcRamBlockCrc().getValue() is True
        assert needs.getCheckStaticBlockId().getValue() is False
        assert needs.getCyclicWritingPeriod().getValue() == 0.005
        assert isinstance(needs.getNDataSets(), PositiveInteger)
        assert needs.getNDataSets().getValue() == 4
        assert isinstance(needs.getNRomBlocks(), PositiveInteger)
        assert needs.getNRomBlocks().getValue() == 3
        assert needs.getRamBlockStatusControl().getValue() == "api"
        assert needs.getReadonly().getValue() is True
        assert needs.getReliability().getValue() == "errorCorrection"
        assert needs.getResistantToChangedSw().getValue() is True
        assert needs.getRestoreAtStart().getValue() is False
        assert needs.getSelectBlockForFirstInitAll().getValue() is True
        assert needs.getStoreAtShutdown().getValue() is True
        assert needs.getStoreCyclic().getValue() is False
        assert needs.getStoreEmergency().getValue() is True
        assert needs.getStoreImmediate().getValue() is False
        assert needs.getStoreOnChange().getValue() is True
        assert needs.getUseAutoValidationAtShutDown().getValue() is True
        assert needs.getUseCRCCompMechanism().getValue() is False
        assert needs.getWriteOnlyOnce().getValue() is True
        assert needs.getWriteVerification().getValue() is False
        assert needs.getWritingFrequency().getValue() == 10
        assert needs.getWritingPriority().getValue() == "high"

    def test_read_absent_elements(self, parser):
        """Test that absent attribute elements leave every field None."""
        needs = NvBlockNeeds(None, "nv")
        element = _snip("<SHORT-NAME>nv</SHORT-NAME>", root_tag="NV-BLOCK-NEEDS")

        parser.readNvBlockNeeds(element, needs)

        assert needs.getCalcRamBlockCrc() is None
        assert needs.getCheckStaticBlockId() is None
        assert needs.getCyclicWritingPeriod() is None
        assert needs.getNDataSets() is None
        assert needs.getNRomBlocks() is None
        assert needs.getRamBlockStatusControl() is None
        assert needs.getReadonly() is None
        assert needs.getReliability() is None
        assert needs.getResistantToChangedSw() is None
        assert needs.getRestoreAtStart() is None
        assert needs.getSelectBlockForFirstInitAll() is None
        assert needs.getStoreAtShutdown() is None
        assert needs.getStoreCyclic() is None
        assert needs.getStoreEmergency() is None
        assert needs.getStoreImmediate() is None
        assert needs.getStoreOnChange() is None
        assert needs.getUseAutoValidationAtShutDown() is None
        assert needs.getUseCRCCompMechanism() is None
        assert needs.getWriteOnlyOnce() is None
        assert needs.getWriteVerification() is None
        assert needs.getWritingFrequency() is None
        assert needs.getWritingPriority() is None


class TestNvBlockDescriptorDispatch:
    def test_read_nv_block_descriptor_nv_block_needs_field_values(self, parser):
        """Test the NvBlockDescriptor.nvBlockNeeds dispatch populates field values one level down."""
        descriptor = NvBlockDescriptor(None, "desc")
        element = _snip(
            "<SHORT-NAME>desc</SHORT-NAME>"
            "<NV-BLOCK-NEEDS>"
            "<SHORT-NAME>nv</SHORT-NAME>"
            "<RAM-BLOCK-STATUS-CONTROL>nvRamManager</RAM-BLOCK-STATUS-CONTROL>"
            "<RELIABILITY>errorDetection</RELIABILITY>"
            "<STORE-ON-CHANGE>true</STORE-ON-CHANGE>"
            "</NV-BLOCK-NEEDS>",
            root_tag="NV-BLOCK-DESCRIPTOR",
        )

        parser.readNvBlockDescriptor(element, descriptor)

        needs = descriptor.getNvBlockNeeds()
        assert needs is not None
        assert needs.getShortName() == "nv"
        assert needs.getRamBlockStatusControl().getValue() == "nvRamManager"
        assert needs.getReliability().getValue() == "errorDetection"
        assert needs.getStoreOnChange().getValue() is True


class TestSwcServiceDependencyDispatch:
    def test_read_swc_service_dependency_service_needs_field_values(self, parser):
        """Test the SwcServiceDependency.serviceNeeds dispatch populates field values one level down."""
        dependency = SwcServiceDependency(None, "dep")
        element = _snip(
            "<SERVICE-NEEDS>"
            "<NV-BLOCK-NEEDS>"
            "<SHORT-NAME>nv</SHORT-NAME>"
            "<CALC-RAM-BLOCK-CRC>true</CALC-RAM-BLOCK-CRC>"
            "<N-DATA-SETS>4</N-DATA-SETS>"
            "<WRITING-PRIORITY>medium</WRITING-PRIORITY>"
            "</NV-BLOCK-NEEDS>"
            "</SERVICE-NEEDS>"
        )

        parser.readSwcServiceDependencyServiceNeeds(element, dependency)

        needs_list = dependency.getServiceNeeds()
        assert len(needs_list) == 1
        needs = needs_list[0]
        assert needs.getShortName() == "nv"
        assert needs.getCalcRamBlockCrc().getValue() is True
        assert needs.getNDataSets().getValue() == 4
        assert needs.getWritingPriority().getValue() == "medium"


class TestBswServiceDependencyDispatch:
    def test_read_bsw_service_dependency_service_needs_field_values(self, parser):
        """Test the BswServiceDependency.serviceNeeds dispatch populates field values one level down."""
        dependency = BswServiceDependency()
        element = _snip(
            "<SERVICE-NEEDS>"
            "<NV-BLOCK-NEEDS>"
            "<SHORT-NAME>nv</SHORT-NAME>"
            "<RAM-BLOCK-STATUS-CONTROL>api</RAM-BLOCK-STATUS-CONTROL>"
            "<RESTORE-AT-START>true</RESTORE-AT-START>"
            "</NV-BLOCK-NEEDS>"
            "</SERVICE-NEEDS>"
        )

        parser.readBswServiceDependencyServiceNeeds(element, dependency)

        needs = dependency.getServiceNeeds()
        assert needs is not None
        assert needs.getShortName() == "nv"
        assert needs.getRamBlockStatusControl().getValue() == "api"
        assert needs.getRestoreAtStart().getValue() is True

"""
Tests for writing SWC-IMPLEMENTATION elements — Table 8.7 (p.623, R23-11).

SwcImplementation (Base = Implementation) carries its own elements BEHAVIOR-REF
(RefType, 0..1, DEST restricted to SwcInternalBehavior) and REQUIRED-RTE-VENDOR
(String, 0..1). The PER-INSTANCE-MEMORY-SIZES wrapper contains zero or more
PerInstanceMemorySize children.

Round-trip counterpart: tests/test_armodel/parser/test_swc_implementation.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DateTime, Identifier, PositiveInteger, RefType, String
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import VariationPoint
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcImplementation import PerInstanceMemorySize, SwcImplementation
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


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


def _build_memory_size(alignment, memory_ref, size, variation_label=None):
    value = PerInstanceMemorySize()
    value.setAlignment(PositiveInteger().setValue(str(alignment)))
    reference = RefType()
    reference.setValue(memory_ref)
    reference.setDest("PER-INSTANCE-MEMORY")
    value.setPerInstanceMemoryRef(reference)
    value.setSize(PositiveInteger().setValue(str(size)))
    if variation_label is not None:
        value.setVariationPoint(VariationPoint().setShortLabel(Identifier().setValue(variation_label)))
    return value


def _build_impl(with_optionals=True, with_memory_sizes=False):
    pkg = AUTOSAR.getInstance().createARPackage("Pkg")
    impl = pkg.createSwcImplementation("Impl1")
    if with_optionals:
        behavior_ref = RefType()
        behavior_ref.setValue("/Pkg/Behavior")
        behavior_ref.setDest("SWC-INTERNAL-BEHAVIOR")
        impl.setBehaviorRef(behavior_ref)
        impl.setRequiredRTEVendor(String().setValue("Vector"))
    if with_memory_sizes:
        first = _build_memory_size(16, "/Pkg/Memory1", 64, "MemorySizeVP")
        first.setChecksum(String().setValue("checksum-1"))
        first.setTimestamp(DateTime().setValue("2024-01-02T12:34:56Z"))
        impl.addPerInstanceMemorySize(first)
        impl.addPerInstanceMemorySize(_build_memory_size(8, "/Pkg/Memory2", 32))
    return impl


def _save_and_reload():
    with tempfile.NamedTemporaryFile(suffix=".arxml", delete=False) as tmp:
        tmp_path = tmp.name
    try:
        ARXMLWriter().save(tmp_path, AUTOSAR.getInstance())
        AUTOSAR.getInstance().new()
        AUTOSAR.getInstance().setARRelease("R23-11")
        ARXMLParser().load(tmp_path, AUTOSAR.getInstance())
    finally:
        if os.path.exists(tmp_path):
            os.unlink(tmp_path)


class TestWriteSwcImplementation:
    """
    Test writeSwcImplementation — BEHAVIOR-REF and REQUIRED-RTE-VENDOR field values (Table 8.7).
    """

    def test_write_behavior_ref_and_required_rte_vendor_field_values(self, writer):
        """
        Test that BEHAVIOR-REF (with DEST) and REQUIRED-RTE-VENDOR are emitted in XSD order.
        """
        impl = _build_impl()
        parent = ET.Element("ELEMENTS")

        writer.writeSwcImplementation(parent, impl)

        swc = parent.find("SWC-IMPLEMENTATION")
        assert swc is not None
        behavior_ref = swc.find("BEHAVIOR-REF")
        assert behavior_ref is not None
        assert behavior_ref.text == "/Pkg/Behavior"
        assert behavior_ref.get("DEST") == "SWC-INTERNAL-BEHAVIOR"
        vendor = swc.find("REQUIRED-RTE-VENDOR")
        assert vendor is not None
        assert vendor.text == "Vector"
        children = list(swc)
        assert children.index(behavior_ref) < children.index(vendor)

    def test_write_without_optionals_emits_no_optional_elements(self, writer):
        """
        Test that unset fields emit no BEHAVIOR-REF / REQUIRED-RTE-VENDOR / PER-INSTANCE-MEMORY-SIZES.
        """
        impl = _build_impl(with_optionals=False)
        parent = ET.Element("ELEMENTS")

        writer.writeSwcImplementation(parent, impl)

        swc = parent.find("SWC-IMPLEMENTATION")
        assert swc is not None
        assert swc.find("BEHAVIOR-REF") is None
        assert swc.find("REQUIRED-RTE-VENDOR") is None
        assert swc.find("PER-INSTANCE-MEMORY-SIZES") is None

    def test_full_document_round_trip_field_values(self):
        """
        Test save → reload asserts the SwcImplementation field values end-to-end.
        """
        _build_impl()
        _save_and_reload()

        pkg = AUTOSAR.getInstance().getARPackages()[0]
        impl = pkg.getReferrableElement("Impl1", SwcImplementation)
        assert impl is not None
        assert impl.getBehaviorRef() is not None
        assert impl.getBehaviorRef().getValue() == "/Pkg/Behavior"
        assert impl.getBehaviorRef().getDest() == "SWC-INTERNAL-BEHAVIOR"
        assert impl.getRequiredRTEVendor() is not None
        assert impl.getRequiredRTEVendor().getValue() == "Vector"

    def test_write_per_instance_memory_sizes_values_and_xsd_order(self, writer):
        impl = _build_impl(with_memory_sizes=True)
        parent = ET.Element("ELEMENTS")

        writer.writeSwcImplementation(parent, impl)

        swc = parent.find("SWC-IMPLEMENTATION")
        assert swc is not None
        wrapper = swc.find("PER-INSTANCE-MEMORY-SIZES")
        assert wrapper is not None
        sizes = wrapper.findall("PER-INSTANCE-MEMORY-SIZE")
        assert len(sizes) == 2
        first, second = sizes
        assert first.get("S") == "checksum-1"
        assert first.get("T") == "2024-01-02T12:34:56Z"
        assert [child.tag for child in first] == ["ALIGNMENT", "PER-INSTANCE-MEMORY-REF", "SIZE", "VARIATION-POINT"]
        assert first.findtext("ALIGNMENT") == "16"
        memory_ref = first.find("PER-INSTANCE-MEMORY-REF")
        assert memory_ref is not None
        assert memory_ref.text == "/Pkg/Memory1"
        assert memory_ref.get("DEST") == "PER-INSTANCE-MEMORY"
        assert first.findtext("SIZE") == "64"
        assert first.findtext("VARIATION-POINT/SHORT-LABEL") == "MemorySizeVP"
        assert second.findtext("ALIGNMENT") == "8"
        assert second.findtext("PER-INSTANCE-MEMORY-REF") == "/Pkg/Memory2"
        assert second.findtext("SIZE") == "32"
        assert [child.tag for child in swc] == ["SHORT-NAME", "BEHAVIOR-REF", "PER-INSTANCE-MEMORY-SIZES", "REQUIRED-RTE-VENDOR"]

    def test_full_document_round_trip_per_instance_memory_size_values(self):
        _build_impl(with_memory_sizes=True)
        _save_and_reload()

        pkg = AUTOSAR.getInstance().getARPackages()[0]
        impl = pkg.getReferrableElement("Impl1", SwcImplementation)
        assert impl is not None
        sizes = impl.getPerInstanceMemorySizes()
        assert len(sizes) == 2
        first, second = sizes
        assert first.getAlignment().getValue() == 16
        assert first.getPerInstanceMemoryRef().getValue() == "/Pkg/Memory1"
        assert first.getPerInstanceMemoryRef().getDest() == "PER-INSTANCE-MEMORY"
        assert first.getSize().getValue() == 64
        assert first.getChecksum().getValue() == "checksum-1"
        assert first.getTimestamp().getValue() == "2024-01-02T12:34:56Z"
        assert first.getVariationPoint().getShortLabel().getValue() == "MemorySizeVP"
        assert second.getAlignment().getValue() == 8
        assert second.getPerInstanceMemoryRef().getValue() == "/Pkg/Memory2"
        assert second.getSize().getValue() == 32
        assert second.getVariationPoint() is None

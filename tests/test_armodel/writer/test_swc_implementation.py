"""
Tests for writing SWC-IMPLEMENTATION elements — Table 8.7 (p.623, R23-11).

SwcImplementation (Base = Implementation) carries its own elements BEHAVIOR-REF
(RefType, 0..1, DEST restricted to SwcInternalBehavior) and REQUIRED-RTE-VENDOR
(String, 0..1). PER-INSTANCE-MEMORY-SIZES is deferred until the
PerInstanceMemorySize class is synced (Rule 0001.10 placeholder).

Round-trip counterpart: tests/test_armodel/parser/test_swc_implementation.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType, String
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcImplementation import SwcImplementation
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


def _build_impl(with_optionals=True):
    pkg = AUTOSAR.getInstance().createARPackage("Pkg")
    impl = pkg.createSwcImplementation("Impl1")
    if with_optionals:
        behavior_ref = RefType()
        behavior_ref.setValue("/Pkg/Behavior")
        behavior_ref.setDest("SWC-INTERNAL-BEHAVIOR")
        impl.setBehaviorRef(behavior_ref)
        impl.setRequiredRTEVendor(String().setValue("Vector"))
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
        impl = pkg.getElement("Impl1", SwcImplementation)
        assert impl is not None
        assert impl.getBehaviorRef() is not None
        assert impl.getBehaviorRef().getValue() == "/Pkg/Behavior"
        assert impl.getBehaviorRef().getDest() == "SWC-INTERNAL-BEHAVIOR"
        assert impl.getRequiredRTEVendor() is not None
        assert impl.getRequiredRTEVendor().getValue() == "Vector"

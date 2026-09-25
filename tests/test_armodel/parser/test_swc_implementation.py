"""
Tests for parsing SWC-IMPLEMENTATION elements — Table 8.7 (p.623, R23-11).

SwcImplementation (Base = Implementation) carries its own elements BEHAVIOR-REF
(RefType, 0..1, DEST restricted to SwcInternalBehavior) and REQUIRED-RTE-VENDOR
(String, 0..1). PER-INSTANCE-MEMORY-SIZES is deferred until the
PerInstanceMemorySize class is synced (Rule 0001.10 placeholder).

Round-trip counterpart: tests/test_armodel/writer/test_swc_implementation.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType, String
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcImplementation import SwcImplementation
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


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
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    return ARXMLParser()


def _impl():
    pkg = AUTOSAR.getInstance().createARPackage("Pkg")
    return SwcImplementation(pkg, "Impl1")


class TestReadSwcImplementation:
    """
    Test readSwcImplementation — BEHAVIOR-REF and REQUIRED-RTE-VENDOR field values (Table 8.7).
    """

    def test_read_behavior_ref_field_value(self, parser):
        """
        Test that the BEHAVIOR-REF value and DEST are populated into the behaviorRef field.
        """
        impl = _impl()
        element = ET.fromstring(
            f"""<SWC-IMPLEMENTATION xmlns='{NS}'>
                <SHORT-NAME>Impl1</SHORT-NAME>
                <BEHAVIOR-REF DEST="SWC-INTERNAL-BEHAVIOR">/Pkg/Behavior</BEHAVIOR-REF>
            </SWC-IMPLEMENTATION>"""
        )

        parser.readSwcImplementation(element, impl)

        assert impl.getBehaviorRef() is not None
        assert isinstance(impl.getBehaviorRef(), RefType)
        assert impl.getBehaviorRef().getValue() == "/Pkg/Behavior"
        assert impl.getBehaviorRef().getDest() == "SWC-INTERNAL-BEHAVIOR"

    def test_read_required_rte_vendor_field_value(self, parser):
        """
        Test that the REQUIRED-RTE-VENDOR value is populated into the requiredRTEVendor field.
        """
        impl = _impl()
        element = ET.fromstring(
            f"""<SWC-IMPLEMENTATION xmlns='{NS}'>
                <SHORT-NAME>Impl1</SHORT-NAME>
                <REQUIRED-RTE-VENDOR>Vector</REQUIRED-RTE-VENDOR>
            </SWC-IMPLEMENTATION>"""
        )

        parser.readSwcImplementation(element, impl)

        assert impl.getRequiredRTEVendor() is not None
        assert isinstance(impl.getRequiredRTEVendor(), String)
        assert impl.getRequiredRTEVendor().getValue() == "Vector"

    def test_read_without_optional_elements_leaves_fields_none(self, parser):
        """
        Test that an element without BEHAVIOR-REF / REQUIRED-RTE-VENDOR leaves both fields None.
        """
        impl = _impl()
        element = ET.fromstring(f"<SWC-IMPLEMENTATION xmlns='{NS}'><SHORT-NAME>Impl1</SHORT-NAME></SWC-IMPLEMENTATION>")

        parser.readSwcImplementation(element, impl)

        assert impl.getBehaviorRef() is None
        assert impl.getRequiredRTEVendor() is None

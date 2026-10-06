"""
Tests for writing DIAGNOSTIC-ECU-INSTANCE-PROPS elements —
DiagnosticEcuInstanceProps, Table 4.205 (p.207, R23-11).

The XSD group DIAGNOSTIC-ECU-INSTANCE-PROPS (AUTOSAR_00052.xsd l.35261)
fixes the element structure: the ECU-INSTANCE-REFS wrapper (choice of
unbounded ECU-INSTANCE-REF with DEST ECU-INSTANCE--SUBTYPES-ENUM) precedes
the optional OBD-SUPPORT element (DIAGNOSTIC-OBD-SUPPORT-ENUM); the wrapper
is emitted only when ecuInstanceRefs is non-empty, OBD-SUPPORT only when
obdSupport is present. obdSupport round-trips as the typed
DiagnosticObdSupportEnum (Table 4.206) literal — the enum value maps back
to its OBD-SUPPORT XSD token. The XSD elements
DTC-STATUS-AVAILABILITY-MASK and SEND-RESP-PEND-ON-TRANS-TO-BOOT carry
atp.Status="removed" and are not modeled (Rule 0015).
The dispatch entry is writeARPackageElement → writeDiagnosticEcuInstanceProps.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_ecu_instance_props.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticEcuInstanceProps
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DiagnosticObdSupportEnum, RefType
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset the AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestWriteDiagnosticEcuInstanceProps:
    """Tests for writeDiagnosticEcuInstanceProps — own element field values (Table 4.205)."""

    def _make_props(self, short_name: str = "EcuInstanceProps1") -> DiagnosticEcuInstanceProps:
        package = AUTOSAR.getInstance().createARPackage("DiagnosticEcuInstancePropss")
        return package.createDiagnosticEcuInstanceProps(short_name)

    def _make_ref(self, value: str) -> RefType:
        ref = RefType()
        ref.setDest("ECU-INSTANCE")
        ref.setValue(value)
        return ref

    def _populate(self, props: DiagnosticEcuInstanceProps) -> DiagnosticEcuInstanceProps:
        props.addEcuInstanceRef(self._make_ref("/AUTOSAR/EcuInstances/Ecu1"))
        props.addEcuInstanceRef(self._make_ref("/AUTOSAR/EcuInstances/Ecu2"))
        props.setObdSupport(DiagnosticObdSupportEnum().setValue(DiagnosticObdSupportEnum.PRIMARY_ECU))
        return props

    def test_write_ecu_instance_refs_wrapper(self):
        """Test that populated refs are emitted as the ECU-INSTANCE-REFS wrapper before OBD-SUPPORT with values and DEST attributes."""
        props = self._populate(self._make_props())

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticEcuInstanceProps(parent, props)

        child = parent.find("DIAGNOSTIC-ECU-INSTANCE-PROPS")
        assert child is not None
        refs_wrapper = child.find("ECU-INSTANCE-REFS")
        assert refs_wrapper is not None
        ref_elements = refs_wrapper.findall("ECU-INSTANCE-REF")
        assert len(ref_elements) == 2
        assert ref_elements[0].text == "/AUTOSAR/EcuInstances/Ecu1"
        assert ref_elements[0].attrib["DEST"] == "ECU-INSTANCE"
        assert ref_elements[1].text == "/AUTOSAR/EcuInstances/Ecu2"
        assert ref_elements[1].attrib["DEST"] == "ECU-INSTANCE"
        assert [c.tag for c in child if c.tag in ("ECU-INSTANCE-REFS", "OBD-SUPPORT")] == ["ECU-INSTANCE-REFS", "OBD-SUPPORT"]

    def test_write_empty_refs_emits_no_wrapper(self):
        """Test that an empty ecuInstanceRefs list emits no ECU-INSTANCE-REFS wrapper (empty wrapper case)."""
        props = self._make_props()
        props.setObdSupport(DiagnosticObdSupportEnum().setValue(DiagnosticObdSupportEnum.NO_OBD_SUPPORT))

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticEcuInstanceProps(parent, props)

        child = parent.find("DIAGNOSTIC-ECU-INSTANCE-PROPS")
        assert child is not None
        assert child.find("ECU-INSTANCE-REFS") is None
        assert child.find("OBD-SUPPORT").text == "NO-OBD-SUPPORT"

    def test_write_unset_own_fields_emit_no_own_elements(self):
        """Test that an unpopulated props emits no ECU-INSTANCE-REFS and no OBD-SUPPORT element."""
        self._make_props()

        parent = ET.Element("PARENT")
        props = AUTOSAR.getInstance().getARPackages()[0].getReferrableElement("EcuInstanceProps1", DiagnosticEcuInstanceProps)
        ARXMLWriter().writeDiagnosticEcuInstanceProps(parent, props)

        child = parent.find("DIAGNOSTIC-ECU-INSTANCE-PROPS")
        assert child is not None
        assert child.find("ECU-INSTANCE-REFS") is None
        assert child.find("OBD-SUPPORT") is None

    def test_arpackage_dispatch_writes_element(self):
        """Test that writeARPackageElement dispatches DiagnosticEcuInstanceProps to a DIAGNOSTIC-ECU-INSTANCE-PROPS element."""
        props = self._populate(self._make_props())

        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElement(parent, props)

        child = parent.find("DIAGNOSTIC-ECU-INSTANCE-PROPS")
        assert child is not None
        assert child.find("SHORT-NAME").text == "EcuInstanceProps1"
        assert child.find("ECU-INSTANCE-REFS") is not None
        assert child.find("OBD-SUPPORT").text == "PRIMARY-ECU"

    def test_round_trip_preserves_field_values(self):
        """Test the full set → save → reload → assert cycle over an ARPackage with field values."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("DiagnosticEcuInstancePropss")
        self._populate(package.createDiagnosticEcuInstanceProps("EcuInstanceProps1"))

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            props_2 = package_2.getReferrableElement("EcuInstanceProps1", DiagnosticEcuInstanceProps)
            assert props_2 is not None
            assert props_2.getShortName() == "EcuInstanceProps1"
            refs = props_2.getEcuInstanceRefs()
            assert len(refs) == 2
            assert refs[0].getValue() == "/AUTOSAR/EcuInstances/Ecu1"
            assert refs[0].getDest() == "ECU-INSTANCE"
            assert refs[1].getValue() == "/AUTOSAR/EcuInstances/Ecu2"
            assert props_2.getObdSupport() is not None
            assert isinstance(props_2.getObdSupport(), DiagnosticObdSupportEnum)
            assert props_2.getObdSupport().getValue() == DiagnosticObdSupportEnum.PRIMARY_ECU
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_round_trip_empty(self):
        """Test that a DiagnosticEcuInstanceProps without own fields round-trips with empty refs and obdSupport None."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("DiagnosticEcuInstancePropss")
        package.createDiagnosticEcuInstanceProps("EcuInstanceProps1")

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            props_2 = package_2.getReferrableElement("EcuInstanceProps1", DiagnosticEcuInstanceProps)
            assert props_2 is not None
            assert props_2.getEcuInstanceRefs() == []
            assert props_2.getObdSupport() is None
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

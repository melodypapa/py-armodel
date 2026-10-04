"""
Tests for reading the DIAGNOSTIC-ECU-INSTANCE-PROPS element —
DiagnosticEcuInstanceProps, Table 4.205 (p.207, R23-11).

DiagnosticEcuInstanceProps (Base most-derived ARElement) carries two own
Attribute rows: ecuInstance (kind ref, multiplicity *) round-trips as the
ECU-INSTANCE-REFS wrapper (choice of unbounded ECU-INSTANCE-REF, DEST
ECU-INSTANCE--SUBTYPES-ENUM — XSD group DIAGNOSTIC-ECU-INSTANCE-PROPS,
AUTOSAR_00052.xsd l.35261); obdSupport (kind attr, multiplicity 0..1, markdown
Type DiagnosticObdSupportEnum) round-trips as the typed
DiagnosticObdSupportEnum (Table 4.206) literal — the OBD-SUPPORT XSD token
maps to the enum value. The XSD elements
DTC-STATUS-AVAILABILITY-MASK and SEND-RESP-PEND-ON-TRANS-TO-BOOT carry
atp.Status="removed" and are not modeled (Rule 0015).

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_ecu_instance_props.py
"""

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DiagnosticObdSupportEnum
from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticEcuInstanceProps:
    """Tests for readDiagnosticEcuInstanceProps — own element field values (Table 4.205)."""

    def _read(self, parser, inner):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticEcuInstanceProps

        props = DiagnosticEcuInstanceProps(AUTOSAR.getInstance(), "EcuInstanceProps1")
        parser.readDiagnosticEcuInstanceProps(_snip(inner, root_tag="DIAGNOSTIC-ECU-INSTANCE-PROPS"), props)
        return props

    def test_read_ecu_instance_refs(self, parser):
        """Test that the ECU-INSTANCE-REFS wrapper is read into the ecuInstanceRefs list as RefType values."""
        props = self._read(
            parser,
            "<SHORT-NAME>EcuInstanceProps1</SHORT-NAME>"
            "<ECU-INSTANCE-REFS>"
            '<ECU-INSTANCE-REF DEST="ECU-INSTANCE">/AUTOSAR/EcuInstances/Ecu1</ECU-INSTANCE-REF>'
            '<ECU-INSTANCE-REF DEST="ECU-INSTANCE">/AUTOSAR/EcuInstances/Ecu2</ECU-INSTANCE-REF>'
            "</ECU-INSTANCE-REFS>",
        )
        assert props.getShortName() == "EcuInstanceProps1"
        refs = props.getEcuInstanceRefs()
        assert len(refs) == 2
        assert refs[0].getValue() == "/AUTOSAR/EcuInstances/Ecu1"
        assert refs[0].getDest() == "ECU-INSTANCE"
        assert refs[1].getValue() == "/AUTOSAR/EcuInstances/Ecu2"
        assert refs[1].getDest() == "ECU-INSTANCE"

    def test_read_empty_ecu_instance_refs_wrapper_leaves_empty_list(self, parser):
        """Test that an empty ECU-INSTANCE-REFS wrapper leaves ecuInstanceRefs empty (empty wrapper case)."""
        props = self._read(parser, "<SHORT-NAME>EcuInstanceProps1</SHORT-NAME><ECU-INSTANCE-REFS></ECU-INSTANCE-REFS>")
        assert props.getEcuInstanceRefs() == []

    def test_read_obd_support(self, parser):
        """Test that the OBD-SUPPORT token is read as the typed enum literal."""
        props = self._read(parser, "<SHORT-NAME>EcuInstanceProps1</SHORT-NAME><OBD-SUPPORT>PRIMARY-ECU</OBD-SUPPORT>")
        obd_support = props.getObdSupport()
        assert obd_support is not None
        assert isinstance(obd_support, DiagnosticObdSupportEnum)
        assert obd_support.getValue() == "primaryEcu"

    def test_read_without_own_fields_leaves_defaults(self, parser):
        """Test that an element without own fields leaves ecuInstanceRefs empty and obdSupport None."""
        props = self._read(parser, "<SHORT-NAME>EcuInstanceProps1</SHORT-NAME>")
        assert props.getEcuInstanceRefs() == []
        assert props.getObdSupport() is None

    def test_read_field_order_refs_then_obd_support(self, parser):
        """Test that both own fields are read when the wrapper precedes OBD-SUPPORT (XSD sequence order)."""
        props = self._read(
            parser,
            "<SHORT-NAME>EcuInstanceProps1</SHORT-NAME>"
            "<ECU-INSTANCE-REFS>"
            '<ECU-INSTANCE-REF DEST="ECU-INSTANCE">/AUTOSAR/EcuInstances/Ecu1</ECU-INSTANCE-REF>'
            "</ECU-INSTANCE-REFS>"
            "<OBD-SUPPORT>MASTER-ECU</OBD-SUPPORT>",
        )
        assert len(props.getEcuInstanceRefs()) == 1
        assert isinstance(props.getObdSupport(), DiagnosticObdSupportEnum)
        assert props.getObdSupport().getValue() == "masterEcu"

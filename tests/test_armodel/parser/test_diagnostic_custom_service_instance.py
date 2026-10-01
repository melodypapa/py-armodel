"""
Tests for reading the DIAGNOSTIC-CUSTOM-SERVICE-INSTANCE element —
DiagnosticCustomServiceInstance, Table 4.27 (p.70, R23-11).

DiagnosticCustomServiceInstance (Base chain reaches DiagnosticServiceInstance)
carries the inherited ACCESS-PERMISSION-REF (SERVICE-CLASS-REF is atpDerived,
skipped in the XSD group) and its own 0..1 CUSTOM-SERVICE-CLASS-REF — XSD group
DIAGNOSTIC-CUSTOM-SERVICE-INSTANCE, AUTOSAR_00052.xsd l.34019.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_custom_service_instance.py
"""

from unittest.mock import MagicMock

from tests.test_armodel.parser._helpers import _snip


class TestReadDiagnosticCustomServiceInstance:
    """Tests for readDiagnosticCustomServiceInstance — own element field values (Table 4.27)."""

    def _read(self, parser, inner):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticCustomServiceInstance

        instance = DiagnosticCustomServiceInstance(parent=MagicMock(), short_name="Csi")
        element = _snip(inner, root_tag="DIAGNOSTIC-CUSTOM-SERVICE-INSTANCE")
        parser.readDiagnosticCustomServiceInstance(element, instance)
        return instance

    def test_with_custom_service_class_ref(self, parser):
        """Test that CUSTOM-SERVICE-CLASS-REF is read with DEST and value."""
        inner = "<SHORT-NAME>Csi</SHORT-NAME>" '<CUSTOM-SERVICE-CLASS-REF DEST="DIAGNOSTIC-CUSTOM-SERVICE-CLASS">/AUTOSAR/DiagnosticCustomInstances/CustomServiceClass</CUSTOM-SERVICE-CLASS-REF>'
        instance = self._read(parser, inner)
        assert instance.getShortName() == "Csi"
        ref = instance.getCustomServiceClassRef()
        assert ref is not None
        assert ref.getDest() == "DIAGNOSTIC-CUSTOM-SERVICE-CLASS"
        assert ref.getValue() == "/AUTOSAR/DiagnosticCustomInstances/CustomServiceClass"

    def test_without_custom_service_class_ref(self, parser):
        """Test that an absent CUSTOM-SERVICE-CLASS-REF leaves customServiceClassRef None."""
        instance = self._read(parser, "<SHORT-NAME>Csi</SHORT-NAME>")
        assert instance.getCustomServiceClassRef() is None

    def test_with_inherited_access_permission_ref(self, parser):
        """Test that the inherited ACCESS-PERMISSION-REF is read through the base helper."""
        inner = (
            "<SHORT-NAME>Csi</SHORT-NAME>"
            '<ACCESS-PERMISSION-REF DEST="DIAGNOSTIC-ACCESS-PERMISSION">/AUTOSAR/Dcm/AccessPermission</ACCESS-PERMISSION-REF>'
            '<CUSTOM-SERVICE-CLASS-REF DEST="DIAGNOSTIC-CUSTOM-SERVICE-CLASS">/AUTOSAR/DiagnosticCustomInstances/CustomServiceClass</CUSTOM-SERVICE-CLASS-REF>'
        )
        instance = self._read(parser, inner)
        access_ref = instance.getAccessPermissionRef()
        assert access_ref is not None
        assert access_ref.getDest() == "DIAGNOSTIC-ACCESS-PERMISSION"
        assert access_ref.getValue() == "/AUTOSAR/Dcm/AccessPermission"
        assert instance.getCustomServiceClassRef() is not None

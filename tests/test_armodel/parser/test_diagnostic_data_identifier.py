"""
Tests for reading DIAGNOSTIC-DATA-IDENTIFIER elements — DiagnosticDataIdentifier, Table 4.2 (p.34, R23-11).

DiagnosticDataIdentifier (Base = DiagnosticAbstractDataIdentifier) carries the
DATA-ELEMENTS wrapper list (DIAGNOSTIC-PARAMETER items), DID-SIZE,
REPRESENTS-VIN and SUPPORT-INFO-BYTE (XSD group DIAGNOSTIC-DATA-IDENTIFIER,
AUTOSAR_00052.xsd l.34234). The reader populates the model via the
addDataElement/set* mutators; the dispatch entry is readARPackageElements →
readDiagnosticDataIdentifier.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_data_identifier.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import DiagnosticParameter
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticDataIdentifier

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str, root_tag: str = "DIAGNOSTIC-DATA-IDENTIFIER") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadDiagnosticDataIdentifier:
    """Tests for readDiagnosticDataIdentifier — own element field values (Table 4.2)."""

    def _read(self, parser, inner):
        did = DiagnosticDataIdentifier(parent=AUTOSAR.getInstance(), short_name="Di")
        parser.readDiagnosticDataIdentifier(_snip(inner), did)
        return did

    def test_read_sets_all_fields(self, parser):
        """Test that DATA-ELEMENTS, DID-SIZE, REPRESENTS-VIN and SUPPORT-INFO-BYTE are read with their field values."""
        did = self._read(
            parser,
            "<SHORT-NAME>Di</SHORT-NAME>"
            "<ID><POSITIVE-INTEGER-VALUE-VARIATION-POINT>4</POSITIVE-INTEGER-VALUE-VARIATION-POINT></ID>"
            "<DATA-ELEMENTS>"
            "<DIAGNOSTIC-PARAMETER><SHORT-NAME>De1</SHORT-NAME></DIAGNOSTIC-PARAMETER>"
            "<DIAGNOSTIC-PARAMETER><SHORT-NAME>De2</SHORT-NAME></DIAGNOSTIC-PARAMETER>"
            "</DATA-ELEMENTS>"
            "<DID-SIZE>8</DID-SIZE>"
            "<REPRESENTS-VIN>true</REPRESENTS-VIN>"
            "<SUPPORT-INFO-BYTE><POSITION>6</POSITION></SUPPORT-INFO-BYTE>",
        )
        assert did.getId() is not None
        assert did.getId().getValue() == 4
        assert len(did.getDataElements()) == 2
        assert isinstance(did.getDataElements()[0], DiagnosticParameter)
        assert did.getDidSize() is not None
        assert did.getDidSize().getValue() == 8
        assert did.getRepresentsVin() is not None
        assert did.getRepresentsVin().getValue() is True
        assert did.getSupportInfoByte() is not None

    def test_read_empty(self, parser):
        """Test that absent elements leave the fields at their defaults."""
        did = self._read(parser, "<SHORT-NAME>Di</SHORT-NAME>")
        assert did.getId() is None
        assert did.getDataElements() == []
        assert did.getDidSize() is None
        assert did.getRepresentsVin() is None
        assert did.getSupportInfoByte() is None

    def test_read_empty_data_elements_wrapper(self, parser):
        """Test that an empty DATA-ELEMENTS wrapper yields an empty dataElements list."""
        did = self._read(
            parser,
            "<SHORT-NAME>Di</SHORT-NAME>" "<DATA-ELEMENTS></DATA-ELEMENTS>" "<DID-SIZE>8</DID-SIZE>",
        )
        assert did.getDataElements() == []
        assert did.getDidSize().getValue() == 8


def test_arpackage_dispatch_reads_diagnostic_data_identifier(parser):
    """Test that readARPackageElements dispatches DIAGNOSTIC-DATA-IDENTIFIER with field values."""
    package = AUTOSAR.getInstance().createARPackage("Dids")
    ar_package = ET.fromstring(
        "<AR-PACKAGE xmlns='%s'>"
        "<SHORT-NAME>Dids</SHORT-NAME>"
        "<ELEMENTS>"
        "<DIAGNOSTIC-DATA-IDENTIFIER>"
        "<SHORT-NAME>Di</SHORT-NAME>"
        "<DID-SIZE>8</DID-SIZE>"
        "<REPRESENTS-VIN>true</REPRESENTS-VIN>"
        "</DIAGNOSTIC-DATA-IDENTIFIER>"
        "</ELEMENTS>"
        "</AR-PACKAGE>" % NS
    )
    parser.readARPackageElements(ar_package, package)

    did = package.getElement("Di", DiagnosticDataIdentifier)
    assert did is not None
    assert isinstance(did, DiagnosticDataIdentifier)
    assert did.getDidSize().getValue() == 8
    assert did.getRepresentsVin().getValue() is True

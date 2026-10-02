"""
Tests for reading DIAGNOSTIC-DYNAMIC-DATA-IDENTIFIER elements — DiagnosticDynamicDataIdentifier, Table 4.3 (p.34, R23-11).

DiagnosticDynamicDataIdentifier (Base = DiagnosticAbstractDataIdentifier) has no
own attributes (XSD group DIAGNOSTIC-DYNAMIC-DATA-IDENTIFIER, AUTOSAR_00052.xsd
l.35097, empty sequence). The reader delegates to
readDiagnosticAbstractDataIdentifier for the inherited id; the dispatch entry is
readARPackageElements → readDiagnosticDynamicDataIdentifier.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_dynamic_data_identifier.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticDynamicDataIdentifier

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str, root_tag: str = "DIAGNOSTIC-DYNAMIC-DATA-IDENTIFIER") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadDiagnosticDynamicDataIdentifier:
    """Tests for readDiagnosticDynamicDataIdentifier — inherited base field values (Table 4.3)."""

    def test_read_sets_inherited_id(self, parser):
        """Test that the inherited id is read through the base helper."""
        did = DiagnosticDynamicDataIdentifier(parent=AUTOSAR.getInstance(), short_name="Ddi")
        parser.readDiagnosticDynamicDataIdentifier(
            _snip("<SHORT-NAME>Ddi</SHORT-NAME>" "<ID><POSITIVE-INTEGER-VALUE-VARIATION-POINT>9</POSITIVE-INTEGER-VALUE-VARIATION-POINT></ID>"),
            did,
        )
        assert did.getShortName() == "Ddi"
        assert did.getId() is not None
        assert did.getId().getValue() == 9

    def test_read_empty(self, parser):
        """Test that an element without children leaves the inherited id None."""
        did = DiagnosticDynamicDataIdentifier(parent=AUTOSAR.getInstance(), short_name="Ddi")
        parser.readDiagnosticDynamicDataIdentifier(_snip("<SHORT-NAME>Ddi</SHORT-NAME>"), did)
        assert did.getId() is None


def test_arpackage_dispatch_reads_diagnostic_dynamic_data_identifier(parser):
    """Test that readARPackageElements dispatches DIAGNOSTIC-DYNAMIC-DATA-IDENTIFIER with field values."""
    package = AUTOSAR.getInstance().createARPackage("Dids")
    ar_package = ET.fromstring(
        "<AR-PACKAGE xmlns='%s'>"
        "<SHORT-NAME>Dids</SHORT-NAME>"
        "<ELEMENTS>"
        "<DIAGNOSTIC-DYNAMIC-DATA-IDENTIFIER>"
        "<SHORT-NAME>Ddi</SHORT-NAME>"
        "<ID><POSITIVE-INTEGER-VALUE-VARIATION-POINT>9</POSITIVE-INTEGER-VALUE-VARIATION-POINT></ID>"
        "</DIAGNOSTIC-DYNAMIC-DATA-IDENTIFIER>"
        "</ELEMENTS>"
        "</AR-PACKAGE>" % NS
    )
    parser.readARPackageElements(ar_package, package)

    did = package.getReferrableElement("Ddi", DiagnosticDynamicDataIdentifier)
    assert did is not None
    assert isinstance(did, DiagnosticDynamicDataIdentifier)
    assert did.getId() is not None
    assert did.getId().getValue() == 9

"""Parser tests for DiagnosticParameterIdentifier (Table 4.127, p.149).

XSD group DIAGNOSTIC-PARAMETER-IDENTIFIER (AUTOSAR_00052.xsd l.40783) element order:
DATA-ELEMENTS (wrapper, unbounded DIAGNOSTIC-PARAMETER items), ID, PID-SIZE,
SUPPORT-INFO-BYTE.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_parameter_identifier.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticParameterIdentifier

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str, root_tag: str = "DIAGNOSTIC-PARAMETER-IDENTIFIER") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadDiagnosticParameterIdentifier:
    def test_read_sets_all_fields(self, parser):
        parameter_identifier = DiagnosticParameterIdentifier(AUTOSAR.getInstance(), "Pid1")
        element = _snip(
            "<SHORT-NAME>Pid1</SHORT-NAME>"
            "<DATA-ELEMENTS><DIAGNOSTIC-PARAMETER><IDENT><SHORT-NAME>Param1</SHORT-NAME></IDENT></DIAGNOSTIC-PARAMETER></DATA-ELEMENTS>"
            "<ID>4</ID>"
            "<PID-SIZE>6</PID-SIZE>"
            "<SUPPORT-INFO-BYTE/>"
        )
        parser.readDiagnosticParameterIdentifier(element, parameter_identifier)
        assert parameter_identifier.getShortName() == "Pid1"
        data_elements = parameter_identifier.getDataElements()
        assert len(data_elements) == 1
        assert data_elements[0].getIdent() is not None
        assert data_elements[0].getIdent().getShortName() == "Param1"
        assert parameter_identifier.getId() is not None
        assert parameter_identifier.getId().getValue() == 4
        assert parameter_identifier.getPidSize() is not None
        assert parameter_identifier.getPidSize().getValue() == 6
        assert parameter_identifier.getSupportInfoByte() is not None

    def test_read_empty(self, parser):
        parameter_identifier = DiagnosticParameterIdentifier(AUTOSAR.getInstance(), "Pid1")
        element = _snip("<SHORT-NAME>Pid1</SHORT-NAME>")
        parser.readDiagnosticParameterIdentifier(element, parameter_identifier)
        assert parameter_identifier.getDataElements() == []
        assert parameter_identifier.getId() is None
        assert parameter_identifier.getPidSize() is None
        assert parameter_identifier.getSupportInfoByte() is None

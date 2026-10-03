"""Parser tests for DiagnosticInfoType (Table 4.146, p.160).

XSD group DIAGNOSTIC-INFO-TYPE (AUTOSAR_00052.xsd l.38300) element order:
DATA-ELEMENTS (wrapper, unbounded DIAGNOSTIC-PARAMETER items), ID.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_info_type.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticInfoType

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str, root_tag: str = "DIAGNOSTIC-INFO-TYPE") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadDiagnosticInfoType:
    def test_read_sets_all_fields(self, parser):
        info_type = DiagnosticInfoType(AUTOSAR.getInstance(), "InfoType1")
        element = _snip("<SHORT-NAME>InfoType1</SHORT-NAME>" "<DATA-ELEMENTS><DIAGNOSTIC-PARAMETER><IDENT><SHORT-NAME>Param1</SHORT-NAME></IDENT></DIAGNOSTIC-PARAMETER></DATA-ELEMENTS>" "<ID>6</ID>")
        parser.readDiagnosticInfoType(element, info_type)
        assert info_type.getShortName() == "InfoType1"
        data_elements = info_type.getDataElements()
        assert len(data_elements) == 1
        assert data_elements[0].getIdent() is not None
        assert data_elements[0].getIdent().getShortName() == "Param1"
        assert info_type.getId() is not None
        assert info_type.getId().getValue() == 6

    def test_read_empty(self, parser):
        info_type = DiagnosticInfoType(AUTOSAR.getInstance(), "InfoType1")
        element = _snip("<SHORT-NAME>InfoType1</SHORT-NAME>")
        parser.readDiagnosticInfoType(element, info_type)
        assert info_type.getDataElements() == []
        assert info_type.getId() is None

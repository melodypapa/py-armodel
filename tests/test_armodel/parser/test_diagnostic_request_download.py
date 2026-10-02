"""Parser tests for DiagnosticRequestDownload (Table 4.121, p.144).

XSD group DIAGNOSTIC-REQUEST-DOWNLOAD (AUTOSAR_00052.xsd l.41794) element order:
REQUEST-DOWNLOAD-CLASS-REF.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_request_download.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticRequestDownload

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str, root_tag: str = "DIAGNOSTIC-REQUEST-DOWNLOAD") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadDiagnosticRequestDownload:
    def test_read_sets_all_fields(self, parser):
        request_download = DiagnosticRequestDownload(AUTOSAR.getInstance(), "RequestDownload1")
        element = _snip(
            "<SHORT-NAME>RequestDownload1</SHORT-NAME>"
            "<REQUEST-DOWNLOAD-CLASS-REF DEST='DIAGNOSTIC-REQUEST-DOWNLOAD-CLASS'>/AUTOSAR/DiagnosticRequestDownloadClasses/Class1</REQUEST-DOWNLOAD-CLASS-REF>"
        )
        parser.readDiagnosticRequestDownload(element, request_download)
        assert request_download.getShortName() == "RequestDownload1"
        assert request_download.getRequestDownloadClassRef() is not None
        assert request_download.getRequestDownloadClassRef().getValue() == "/AUTOSAR/DiagnosticRequestDownloadClasses/Class1"
        assert request_download.getRequestDownloadClassRef().getDest() == "DIAGNOSTIC-REQUEST-DOWNLOAD-CLASS"

    def test_read_empty(self, parser):
        request_download = DiagnosticRequestDownload(AUTOSAR.getInstance(), "RequestDownload1")
        element = _snip("<SHORT-NAME>RequestDownload1</SHORT-NAME>")
        parser.readDiagnosticRequestDownload(element, request_download)
        assert request_download.getRequestDownloadClassRef() is None

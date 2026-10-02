"""Parser tests for DiagnosticRequestUpload (Table 4.123, p.145).

XSD group DIAGNOSTIC-REQUEST-UPLOAD (AUTOSAR_00052.xsd l.42454) element order:
REQUEST-UPLOAD-CLASS-REF.

Round-trip counterpart: tests/test_armodel/writer/test_writer_diagnostic_request_upload.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import DiagnosticRequestUpload

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str, root_tag: str = "DIAGNOSTIC-REQUEST-UPLOAD") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


class TestReadDiagnosticRequestUpload:
    def test_read_sets_all_fields(self, parser):
        request_upload = DiagnosticRequestUpload(AUTOSAR.getInstance(), "RequestUpload1")
        element = _snip(
            "<SHORT-NAME>RequestUpload1</SHORT-NAME>" "<REQUEST-UPLOAD-CLASS-REF DEST='DIAGNOSTIC-REQUEST-UPLOAD-CLASS'>/AUTOSAR/DiagnosticRequestUploadClasses/Class1</REQUEST-UPLOAD-CLASS-REF>"
        )
        parser.readDiagnosticRequestUpload(element, request_upload)
        assert request_upload.getShortName() == "RequestUpload1"
        assert request_upload.getRequestUploadClassRef() is not None
        assert request_upload.getRequestUploadClassRef().getValue() == "/AUTOSAR/DiagnosticRequestUploadClasses/Class1"
        assert request_upload.getRequestUploadClassRef().getDest() == "DIAGNOSTIC-REQUEST-UPLOAD-CLASS"

    def test_read_empty(self, parser):
        request_upload = DiagnosticRequestUpload(AUTOSAR.getInstance(), "RequestUpload1")
        element = _snip("<SHORT-NAME>RequestUpload1</SHORT-NAME>")
        parser.readDiagnosticRequestUpload(element, request_upload)
        assert request_upload.getRequestUploadClassRef() is None

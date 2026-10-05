import logging
import os

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.validation.validator import ARXMLValidator
from armodel.writer.arxml_writer import ARXMLWriter

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "validation", "data")
TINY_XSD = os.path.join(DATA_DIR, "tiny_autosar.xsd")

ARXMLValidator.register_schema_file("AUTOSAR_TINY.xsd", TINY_XSD)


@pytest.fixture(autouse=True)
def _fresh_document():
    AUTOSAR.getInstance().new()
    yield


def _document_with_tiny_schema_location():
    document = AUTOSAR.getInstance()
    document.schema_location = "http://autosar.org/schema/r4.0 AUTOSAR_TINY.xsd"
    return document


def test_valid_document_saves(tmp_path):
    path = os.path.join(str(tmp_path), "out.arxml")
    ARXMLWriter().save(path, _document_with_tiny_schema_location())
    assert os.path.exists(path)


def test_schema_invalid_document_raises_and_does_not_write(tmp_path, caplog):
    document = _document_with_tiny_schema_location()
    document.createARPackage("Pkg")
    path = os.path.join(str(tmp_path), "out.arxml")
    with pytest.raises(ValueError) as exc_info:
        ARXMLWriter().save(path, document)
    assert "failed schema validation" in str(exc_info.value)
    assert "line" in str(exc_info.value)
    assert not os.path.exists(path)


def test_warning_mode_logs_and_writes(tmp_path, caplog):
    document = _document_with_tiny_schema_location()
    document.createARPackage("Pkg")
    path = os.path.join(str(tmp_path), "out.arxml")
    caplog.set_level(logging.WARNING)
    ARXMLWriter(options={"warning": True}).save(path, document)
    assert os.path.exists(path)
    assert any("Schema error" in record.getMessage() for record in caplog.records)


def test_validate_false_skips_validation(tmp_path):
    document = _document_with_tiny_schema_location()
    document.createARPackage("Pkg")
    path = os.path.join(str(tmp_path), "out.arxml")
    ARXMLWriter(options={"validate": False}).save(path, document)
    assert os.path.exists(path)


def test_default_schema_location_skips_validation(tmp_path, caplog):
    document = AUTOSAR.getInstance()
    path = os.path.join(str(tmp_path), "out.arxml")
    caplog.set_level(logging.WARNING)
    ARXMLWriter().save(path, document)
    assert os.path.exists(path)
    assert any("No XSD schema found" in record.getMessage() for record in caplog.records)

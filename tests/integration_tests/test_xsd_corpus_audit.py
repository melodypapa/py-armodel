import glob
import os

import pytest

from armodel.validation.validator import ARXMLValidator

CORPUS = sorted(glob.glob(os.path.join(os.path.dirname(__file__), "test_files", "*.arxml")))
GATED = [f for f in CORPUS if ARXMLValidator.for_document(open(f, "rb").read()) is not None]


@pytest.mark.parametrize("filename", GATED, ids=[os.path.basename(f) for f in GATED])
def test_corpus_file_validates_against_bundled_schema(filename):
    with open(filename, "rb") as f:
        data = f.read()
    validator = ARXMLValidator.for_document(data)
    errors = validator.validate_bytes(data)
    assert errors == [], "%s failed validation:\n%s" % (
        os.path.basename(filename),
        "\n".join("  line %s: %s" % (error.line, error.message) for error in errors),
    )


def test_corpus_gate_mapping_present():
    assert GATED, "no corpus file is gated by a bundled schema — detection is broken"

"""Validates that every full-document AUTOSAR fragment constant used as test data
is schema-valid. Deliberately malformed fixtures opt out with a `# xsd-skip: <reason>`
marker on (or directly above) the assignment."""

import ast
import glob
import os
import re

import pytest

from armodel.validation.validator import SCHEMA_DIR, ARXMLValidator

TESTS_DIR = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", ".."))
DEFAULT_XSD = os.path.join(SCHEMA_DIR, "R4.4.0", "AUTOSAR_00046.xsd")
DOC_PATTERN = re.compile(r"^\s*(<\?xml[^>]*?>)?\s*<AUTOSAR[\s>]", re.S)
SKIP_MARKER = "xsd-skip"


def collect_fragments():
    found = []
    pattern = os.path.join(TESTS_DIR, "**", "test_*.py")
    for path in sorted(glob.glob(pattern, recursive=True)):
        with open(path, encoding="utf-8") as f:
            source = f.read()
        try:
            tree = ast.parse(source)
        except SyntaxError:
            continue
        lines = source.splitlines()
        for node in ast.walk(tree):
            if not isinstance(node, (ast.Assign, ast.AnnAssign)):
                continue
            value = node.value
            if not (isinstance(value, ast.Constant) and isinstance(value.value, str)):
                continue
            if not DOC_PATTERN.match(value.value):
                continue
            targets = node.targets if isinstance(node, ast.Assign) else [node.target]
            name = targets[0].id if targets and isinstance(targets[0], ast.Name) else "constant@%d" % node.lineno
            skipped = SKIP_MARKER in "\n".join(lines[max(0, node.lineno - 3) : node.lineno])
            found.append((path, name, value.value, skipped))
    return found


ALL_FRAGMENTS = collect_fragments()
CHECKED = [(path, name, xml) for path, name, xml, skipped in ALL_FRAGMENTS if not skipped]


@pytest.mark.parametrize(
    "path,name,xml",
    CHECKED,
    ids=["%s:%s" % (os.path.relpath(p, TESTS_DIR), n) for p, n, _ in CHECKED],
)
def test_test_data_fragment_validates(path, name, xml):
    data = xml.encode("utf-8")
    xsd_path = ARXMLValidator.detect_schema_path(data)
    if xsd_path is None:
        xsd_path = DEFAULT_XSD
    errors = ARXMLValidator(xsd_path).validate_bytes(data)
    assert errors == [], "%s:%s is schema-invalid (fix the test data or add a xsd-skip marker if deliberately malformed):\n%s" % (
        os.path.relpath(path, TESTS_DIR),
        name,
        "\n".join("  line %s: %s" % (error.line, error.message) for error in errors),
    )


def test_fragment_scan_found_targets():
    assert len(ALL_FRAGMENTS) >= 10, "fragment scanner found nothing — its AST patterns are broken"

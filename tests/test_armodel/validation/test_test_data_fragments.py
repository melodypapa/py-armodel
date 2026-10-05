"""Validates that full-document AUTOSAR fragment expressions used as test data are
schema-valid. Covered: plain string constants and constant `+` concatenations are
validated in full; f-string fragments are validated with every interpolation hole
substituted — module-level string constants are resolved to their real values (e.g.
the AUTOSAR namespace), anything else becomes the sentinel "PLACEHOLDER" — and any
schema error fails. Fragments whose namespace stays unresolvable after substitution
are counted but not validated. Anything else — e.g. fragments composed at runtime —
is not covered. Deliberately malformed fixtures opt out with a `# xsd-skip: <reason>`
marker on the assignment or within the statement."""

import ast
import glob
import os
import re
from typing import Dict, Optional

import pytest

from armodel.validation.validator import SCHEMA_DIR, ARXMLValidator

TESTS_DIR = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", ".."))
DEFAULT_XSD = os.path.join(SCHEMA_DIR, "R4.4.0", "AUTOSAR_00046.xsd")
DOC_PATTERN = re.compile(r"^\s*(<\?xml[^>]*?>)?\s*<AUTOSAR[\s>]", re.S)
SKIP_MARKER = re.compile(r"#\s*xsd-skip\b")
PLACEHOLDER = "PLACEHOLDER"
XMLNS_PATTERN = re.compile(r"xmlns(?::[\w.\-]+)?\s*=\s*[\"']([^\"']*)[\"']")


def _module_constants(tree) -> Dict[str, str]:
    constants = {}
    for node in tree.body:
        if not isinstance(node, (ast.Assign, ast.AnnAssign)):
            continue
        value = node.value
        if not (isinstance(value, ast.Constant) and isinstance(value.value, str)):
            continue
        targets = node.targets if isinstance(node, ast.Assign) else [node.target]
        for target in targets:
            if isinstance(target, ast.Name):
                constants[target.id] = value.value
    return constants


def _fold_concat(node) -> Optional[str]:
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
        left = _fold_concat(node.left)
        right = _fold_concat(node.right)
        if left is not None and right is not None:
            return left + right
    return None


def _substitute_joined_str(node, module_constants: Dict[str, str]) -> str:
    parts = []
    for child in node.values:
        if isinstance(child, ast.FormattedValue):
            expression = child.value
            if isinstance(expression, ast.Name) and expression.id in module_constants:
                parts.append(module_constants[expression.id])
            else:
                parts.append(PLACEHOLDER)
        elif isinstance(child, ast.Constant):
            parts.append(child.value if isinstance(child.value, str) else str(child.value))
    return "".join(parts)


def _has_unresolved_namespace(xml: str) -> bool:
    return any(PLACEHOLDER in value for value in XMLNS_PATTERN.findall(xml))


def collect_fragments():
    found = []
    pattern = os.path.join(TESTS_DIR, "**", "test_*.py")
    for path in sorted(glob.glob(pattern, recursive=True)):
        with open(path, encoding="utf-8", errors="replace") as f:
            source = f.read()
        try:
            tree = ast.parse(source)
        except SyntaxError:
            continue
        module_constants = _module_constants(tree)
        lines = source.splitlines()
        for node in ast.walk(tree):
            if not isinstance(node, (ast.Assign, ast.AnnAssign)):
                continue
            value = node.value
            if value is None:
                continue
            is_fstring = False
            if isinstance(value, ast.Constant) and isinstance(value.value, str):
                xml = value.value
            elif isinstance(value, ast.BinOp):
                xml = _fold_concat(value)
            elif isinstance(value, ast.JoinedStr):
                xml = _substitute_joined_str(value, module_constants)
                is_fstring = True
            else:
                continue
            if xml is None or not DOC_PATTERN.match(xml):
                continue
            targets = node.targets if isinstance(node, ast.Assign) else [node.target]
            name = targets[0].id if targets and isinstance(targets[0], ast.Name) else "constant@%d" % node.lineno
            unresolved = is_fstring and _has_unresolved_namespace(xml)
            if is_fstring:
                name += " (f-string, unresolved)" if unresolved else " (f-string)"
            validated = not any(SKIP_MARKER.search(line) for line in lines[max(0, node.lineno - 3) : node.end_lineno])
            if unresolved:
                validated = False
            found.append((path, name, xml, validated))
    return found


ALL_FRAGMENTS = collect_fragments()
CHECKED = [(path, name, xml) for path, name, xml, validated in ALL_FRAGMENTS if validated]


@pytest.mark.parametrize(
    "path,name,xml",
    CHECKED,
    ids=["%s:%s" % (os.path.relpath(p, TESTS_DIR), n) for p, n, _ in CHECKED],
)
def test_test_data_fragment_validates(path, name, xml):
    data = xml.encode("utf-8")
    xsd_path = ARXMLValidator.detect_schema_path(data)
    fallback = xsd_path is None
    if fallback:
        xsd_path = DEFAULT_XSD
    errors = ARXMLValidator(xsd_path).validate_bytes(data)
    assert errors == [], "%s:%s is schema-invalid (fix the test data or add a xsd-skip marker if deliberately malformed) [schema: %s%s]:\n%s" % (
        os.path.relpath(path, TESTS_DIR),
        name,
        os.path.basename(xsd_path),
        " fallback" if fallback else "",
        "\n".join("  line %s: %s" % (error.line, error.message) for error in errors),
    )


def test_fragment_scan_found_targets():
    assert len(ALL_FRAGMENTS) >= 40, "fragment scanner found nothing — its AST patterns are broken"

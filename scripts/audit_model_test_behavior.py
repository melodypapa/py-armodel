#!/usr/bin/env python3
"""Audit model classes against their model-unit tests.

This is intentionally conservative: it reports likely gaps for review rather
than treating naming conventions as proof that a behavior is covered.
"""

import argparse
import ast
import json
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

SRC_ROOT = Path("src/armodel/models")
TEST_ROOT = Path("tests/test_armodel/models")


def parse_file(path: Path) -> Optional[ast.Module]:
    try:
        return ast.parse(path.read_text(encoding="utf-8"))
    except (OSError, SyntaxError):
        return None


def source_classes(path: Path) -> List[ast.ClassDef]:
    tree = parse_file(path)
    if tree is None:
        return []
    return [node for node in tree.body if isinstance(node, ast.ClassDef)]


def test_records() -> List[Tuple[Path, ast.ClassDef, str]]:
    records = []
    for path in TEST_ROOT.rglob("test_*.py"):
        tree = parse_file(path)
        if tree is None:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef) and node.name.startswith("Test"):
                records.append((path, node, text))
    return records


def class_tests(class_name: str, records: List[Tuple[Path, ast.ClassDef, str]]) -> List[Tuple[Path, ast.ClassDef, str]]:
    return [record for record in records if class_name in record[2]]


def method_names(node: ast.ClassDef) -> Set[str]:
    return {child.name for child in node.body if isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef))}


def normalized_methods(node: ast.ClassDef) -> Set[str]:
    values = set()
    for name in method_names(node):
        values.add(name.removeprefix("test_").replace("_", "").lower())
    return values


def calls_and_assertions(node: ast.ClassDef) -> Tuple[Set[str], Set[str], Set[str]]:
    calls = set()
    assertions = set()
    constructors = set()
    for child in ast.walk(node):
        if isinstance(child, ast.Call):
            if isinstance(child.func, ast.Attribute):
                calls.add(child.func.attr)
            elif isinstance(child.func, ast.Name):
                calls.add(child.func.id)
                constructors.add(child.func.id)
        if isinstance(child, ast.Assert):
            assertions.add(ast.unparse(child.test) if hasattr(ast, "unparse") else "assert")
    return calls, assertions, constructors


def audit_class(source: ast.ClassDef, tests: List[Tuple[Path, ast.ClassDef, str]]) -> Dict[str, object]:
    test_methods = set()
    calls = set()
    assertions = set()
    constructors = set()
    for _, test_class, _ in tests:
        test_methods.update(normalized_methods(test_class))
        test_calls, test_assertions, test_constructors = calls_and_assertions(test_class)
        calls.update(test_calls)
        assertions.update(test_assertions)
        constructors.update(test_constructors)

    source_methods = method_names(source)
    issues = []
    for name in sorted(source_methods):
        normalized = name.replace("_", "").lower()
        if name == "__init__":
            covered = source.name in constructors or bool({"init", "initialization", "constructor"} & test_methods)
        else:
            covered = normalized in test_methods
        if not covered:
            issues.append({"code": "HEURISTIC_METHOD_TOKEN_GAP", "method": name})
        if name.startswith("set") and name != "setEnumValues" and name not in calls:
            issues.append({"code": "MISSING_SETTER_CALL", "method": name})

    is_enum = any(isinstance(base, ast.Name) and base.id == "AREnum" for base in source.bases)
    if is_enum:
        for required in ("getEnumValues", "validateEnumValue", "setValue", "getValue"):
            if required not in calls:
                issues.append({"code": "HEURISTIC_ENUM_API_GAP", "method": required})
        if not any("False" in assertion for assertion in assertions):
            issues.append({"code": "HEURISTIC_INVALID_ENUM_GAP"})

    return {
        "class": source.name,
        "tests": [str(path) for path, _, _ in tests],
        "issues": issues,
    }


def build_report() -> Dict[str, object]:
    records = test_records()
    classes = []
    for path in SRC_ROOT.rglob("*.py"):
        for source in source_classes(path):
            matching = class_tests(source.name, records)
            result = audit_class(source, matching)
            result["source"] = str(path)
            classes.append(result)
    return {"classes": classes}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--format", choices=("text", "json"), default="text")
    parser.add_argument("--strict", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    report = build_report()
    issue_count = sum(len(item["issues"]) for item in report["classes"])
    if args.format == "json":
        print(json.dumps(report, indent=2, sort_keys=True))
    else:
        print(f"Audited {len(report['classes'])} model classes; {issue_count} issues reported.")
        for item in report["classes"]:
            if item["issues"]:
                print(f"{item['source']}::{item['class']}")
                for issue in item["issues"]:
                    print(f"  - {issue}")
    return 1 if args.strict and issue_count else 0


if __name__ == "__main__":
    raise SystemExit(main())

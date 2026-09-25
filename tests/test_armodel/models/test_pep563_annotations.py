import ast
from pathlib import Path

MODELS_DIR = Path(__file__).resolve().parents[3] / "src" / "armodel" / "models"


def _top_level_string_annotations(path):
    tree = ast.parse(path.read_text(encoding="utf-8"))
    hits = []
    for node in ast.walk(tree):
        if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        args = node.args
        params = list(args.args) + list(args.posonlyargs) + list(args.kwonlyargs)
        if args.vararg:
            params.append(args.vararg)
        if args.kwarg:
            params.append(args.kwarg)
        annotations = [a.annotation for a in params if a.annotation]
        if node.returns:
            annotations.append(node.returns)
        for ann in annotations:
            if isinstance(ann, ast.Constant) and isinstance(ann.value, str):
                hits.append((node.name, ann.lineno))
    return hits


def test_no_top_level_quoted_annotations_in_pep563_modules():
    offenders = []
    for path in sorted(MODELS_DIR.rglob("*.py")):
        source = path.read_text(encoding="utf-8")
        if "from __future__ import annotations" not in source:
            continue
        for name, lineno in _top_level_string_annotations(path):
            offenders.append(f"{path.relative_to(MODELS_DIR)}:{lineno} ({name})")
    assert not offenders, (
        "Top-level quoted annotations are stored verbatim under PEP 563 and stay "
        "unresolved ForwardRefs on Python 3.8 typing.get_type_hints(); use bare names "
        '(quotes only nested, e.g. Optional["Foo"]):\n' + "\n".join(offenders)
    )

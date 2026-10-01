import ast
from pathlib import Path

MODELS_DIR = Path(__file__).resolve().parents[3] / "src" / "armodel" / "models"
FUTURE = "from __future__ import annotations"
SUBSCRIPT_CONTAINERS = {"Optional", "List", "Dict", "Set", "Tuple", "Union", "Type"}


def _annotation_nodes(tree):
    for node in ast.walk(tree):
        if isinstance(node, ast.AnnAssign) and node.annotation is not None:
            yield node.annotation
        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            a = node.args
            params = list(a.args) + list(a.posonlyargs) + list(a.kwonlyargs)
            if a.vararg:
                params.append(a.vararg)
            if a.kwarg:
                params.append(a.kwarg)
            for p in params:
                if p.annotation is not None:
                    yield p.annotation
            if node.returns is not None:
                yield node.returns


def _quoted_identifiers(annotation):
    for node in ast.walk(annotation):
        if isinstance(node, ast.Constant) and isinstance(node.value, str) and node.value.isidentifier():
            yield node


def test_no_quoted_annotations_in_pep563_models():
    offenders = []
    for path in sorted(MODELS_DIR.rglob("*.py")):
        source = path.read_text(encoding="utf-8")
        if FUTURE not in source:
            continue
        tree = ast.parse(source)
        for ann in _annotation_nodes(tree):
            for node in _quoted_identifiers(ann):
                offenders.append("%s:%d ('%s')" % (path.relative_to(MODELS_DIR), node.lineno, node.value))
    assert not offenders, "Bare-identifier string annotations must not be quoted in PEP 563 modules " "(stored verbatim, resolved identically unquoted):\n" + "\n".join(offenders)


def test_no_nested_quoted_refs_in_optional_or_list():
    offenders = []
    for path in sorted(MODELS_DIR.rglob("*.py")):
        tree = ast.parse(path.read_text(encoding="utf-8"))
        for ann in _annotation_nodes(tree):
            for node in ast.walk(ann):
                if isinstance(node, ast.Subscript) and getattr(node.value, "id", "") in SUBSCRIPT_CONTAINERS:
                    for inner in _quoted_identifiers(node.slice):
                        offenders.append("%s:%d ('%s')" % (path.relative_to(MODELS_DIR), inner.lineno, inner.value))
    assert not offenders, 'Nested quoted forward refs like Optional["Foo"] must be bare names ' "(PEP 563 makes quoting redundant; convert the file instead):\n" + "\n".join(offenders)


def test_all_init_and_clear_self_assignments_annotated():
    offenders = []
    for path in sorted(MODELS_DIR.rglob("*.py")):
        rel = path.relative_to(MODELS_DIR)
        tree = ast.parse(path.read_text(encoding="utf-8"))
        for node in ast.walk(tree):
            if not isinstance(node, ast.ClassDef):
                continue
            for item in node.body:
                if not isinstance(item, ast.FunctionDef) or item.name not in ("__init__", "clear"):
                    continue
                annotated = set()
                for st in ast.walk(item):
                    if isinstance(st, ast.AnnAssign) and isinstance(st.target, ast.Attribute) and isinstance(st.target.value, ast.Name) and st.target.value.id == "self":
                        annotated.add(st.target.attr)
                for st in ast.walk(item):
                    if isinstance(st, ast.Assign) and len(st.targets) == 1:
                        t = st.targets[0]
                        if isinstance(t, ast.Attribute) and isinstance(t.value, ast.Name) and t.value.id == "self" and t.attr not in annotated:
                            offenders.append("%s:%d (%s.%s -> self.%s)" % (rel, st.lineno, node.name, item.name, t.attr))
    assert not offenders, "Every self.<member> assignment in __init__/clear must carry an annotation " "(setter-only lazy members and mixin class-level defaults are exempt by design):\n" + "\n".join(
        offenders
    )

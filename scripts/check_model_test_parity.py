#!/usr/bin/env python3
"""
Check that unit-test files for model classes mirror the structure of the
source model files (file presence + class coverage).

The test suite is organized three ways, all handled here:

  * Per file      : ``src/.../Foo.py`` -> ``tests/.../test_Foo.py``
  * Per class     : ``src/.../Foo.py`` (class ``Bar``) -> ``tests/.../test_Bar.py``
  * Per sub-package: package dir ``Pkg/`` -> ``tests/.../Pkg/test_Pkg.py``

What this verifies (whole-repo):

  1. FILE PRESENCE - every model source file ``Foo.py`` (excluding
     ``__init__.py``) should have a ``test_Foo.py`` (or ``test_Foo_*.py``) in
     the *mirrored* test directory. Missing ones are UNCOVERED.

  2. ORPHANS - every test ``test_X.py`` must map to a real source entity: a
     source file ``X.py``, a top-level class ``X`` (also when declared in a
     package ``__init__.py``), or a sub-package directory ``X/``. Otherwise it
     is an ORPHAN (references something that no longer exists in source).

  3. CLASS COVERAGE (package-scoped, usage-verified) - for every model source
     file, each top-level class is checked for a ``test_<ClassName>.py`` *in
     the mirrored package directory* (not anywhere in the tree, so a class
     name shared across packages is not falsely counted). A test only counts
     if it actually *references* the class (import or usage), so a
     ``test_Foo.py`` does NOT automatically cover every class in ``Foo.py``.
     Files where no class is tested are real gaps; files where only some
     classes are tested are partial.

  4. MISPLACED TESTS (non-fatal warning) - a test must live in the directory
     that mirrors the source entity it tests (or inside its own package dir
     for a package test). Tests found elsewhere are reported but do not fail
     the check, since they still exercise code.

``__init__.py`` package markers are not model classes, so they are excluded
from the uncovered / class-coverage reports.

Usage (run from the repository root):
    python scripts/check_model_test_parity.py
"""
import ast
import re
from pathlib import Path

SRC_ROOT = Path("src/armodel/models")
TEST_ROOT = Path("tests/test_armodel/models")


def top_level_classes(src_file: Path):
    try:
        tree = ast.parse(src_file.read_text(encoding="utf-8"))
    except (OSError, SyntaxError):
        return []
    return [n.name for n in tree.body if isinstance(n, ast.ClassDef)]


def build_source_index():
    file_stem_to_rel = {}  # source file stem -> rel dir
    class_to_rel = {}  # class name -> set of rel dirs
    dir_rel_set = set()  # all source directory rel paths
    for d in SRC_ROOT.rglob("*"):
        if d.is_dir():
            dir_rel_set.add(d.relative_to(SRC_ROOT))
    for sf in SRC_ROOT.rglob("*.py"):
        if not sf.is_file():
            continue
        rel = sf.relative_to(SRC_ROOT).parent
        file_stem_to_rel[sf.stem] = rel
        for c in top_level_classes(sf):
            class_to_rel.setdefault(c, set()).add(rel)
    return file_stem_to_rel, class_to_rel, dir_rel_set


def build_test_index():
    records = []  # (tf, name, body, split, trel, text)
    for tf in TEST_ROOT.rglob("test_*.py"):
        if not tf.is_file():
            continue
        name = tf.name
        if name == "test___init__.py":
            body, split = "", ""
        else:
            body = name[5:-3]  # strip "test_" + ".py"
            split = body.split("_", 1)[0]
        trel = tf.parent.relative_to(TEST_ROOT)
        text = tf.read_text(encoding="utf-8", errors="ignore")
        records.append((tf, name, body, split, trel, text))
    return records


def has_file_test(tdir: Path, stem: str):
    if not tdir.is_dir():
        return False
    for f in tdir.iterdir():
        fn = f.name
        if fn == f"test_{stem}.py" or (fn.startswith(f"test_{stem}_") and fn.endswith(".py")):
            return True
    return False


def tests_under(rel, records, cache):
    if rel in cache:
        return cache[rel]
    res = [r for r in records if r[4] == rel or rel in r[4].parents]
    cache[rel] = res
    return res


def class_covered(class_name, file_stem, pkg_tests):
    """A class is covered if a test in the package references it by name,
    or a file-level test (named after the source file) references it."""
    pat = re.compile(r"\b" + re.escape(class_name) + r"\b")
    for _tf, _name, body, split, _trel, text in pkg_tests:
        targets = {body, split}
        if class_name in targets or file_stem in targets:
            if pat.search(text):
                return True
    return False


def main():
    if not SRC_ROOT.is_dir() or not TEST_ROOT.is_dir():
        print("ERROR: source or test root not found (run from repo root)")
        raise SystemExit(1)

    file_stem_to_rel, class_to_rel, dir_rel_set = build_source_index()
    records = build_test_index()
    cache = {}

    src_file_stems = set(file_stem_to_rel)
    src_class_names = set(class_to_rel)
    src_dir_names = {p.name for p in dir_rel_set}

    src_files = sorted(p for p in SRC_ROOT.rglob("*.py") if p.is_file() and p.name != "__init__.py")

    # ---- 1. FILE PRESENCE ------------------------------------------------
    uncovered = [s for s in src_files if not has_file_test(test_dir_for(s), s.stem)]

    # ---- 2. ORPHANS ------------------------------------------------------
    orphan = []
    for tf, name, body, split, _trel, _text in records:
        if name == "test___init__.py" or name.endswith("_init.py"):
            continue
        if body in src_file_stems or body in src_class_names or body in src_dir_names or split in src_file_stems or split in src_class_names or split in src_dir_names:
            continue
        orphan.append(tf)

    # ---- 3. CLASS COVERAGE (package-scoped, usage-verified) --------------
    class_none = []  # files where no class has any test at all
    class_partial = []  # files where some (not all) classes have a test
    for sf in src_files:
        classes = top_level_classes(sf)
        if not classes:
            continue
        rel = sf.relative_to(SRC_ROOT).parent
        pkg_tests = tests_under(rel, records, cache)
        tested = [c for c in classes if class_covered(c, sf.stem, pkg_tests)]
        if not tested:
            class_none.append((sf, classes))
        elif len(tested) < len(classes):
            class_partial.append((sf, classes, tested))

    # ---- 4. MISPLACED TESTS (non-fatal warning) --------------------------
    misplaced = []
    for tf, name, body, split, trel, _text in records:
        if name == "test___init__.py" or name.endswith("_init.py"):
            # package __init__ test: must sit in the mirrored package dir
            if tf.parent.relative_to(TEST_ROOT) == trel:
                continue
            misplaced.append(tf)
            continue
        expected = set()
        for n in (body, split):
            if n in file_stem_to_rel:
                expected.add(file_stem_to_rel[n])
            if n in class_to_rel:
                expected.update(class_to_rel[n])
            if n in dir_rel_set:
                expected.add(n)
        # package test located inside its own package dir
        if body and body == trel.name and trel in dir_rel_set:
            continue
        if trel in expected:
            continue
        misplaced.append(tf)

    # ---- REPORT ----------------------------------------------------------
    print("=" * 72)
    print("MODEL SOURCE <-> UNIT TEST PARITY" " (file presence + class coverage)")
    print("=" * 72)
    print(f"Source model files (excl. __init__.py): {len(src_files)}")
    print(f"Test files                                 : {len(records)}")
    print(f"COVERED (test_Foo.py in mirrored dir)     : " f"{len(src_files) - len(uncovered)}")
    print(f"UNCOVERED source files                    : {len(uncovered)}")
    print(f"ORPHAN tests (no matching source entity) : {len(orphan)}")
    print(f"CLASSES untested (no test for any class) : {len(class_none)}")
    print(f"CLASSES partially tested                 : {len(class_partial)}")
    print(f"MISPLACED tests (warning, non-fatal)     : {len(misplaced)}")
    print("-" * 72)

    if uncovered:
        print("1) SOURCE FILES WITHOUT A MIRRORED test_Foo.py:")
        for s in uncovered:
            print(f"  [ ] {s.relative_to(SRC_ROOT)}")
    else:
        print("1) Every model source file has a mirrored test_Foo.py.")

    if orphan:
        print("-" * 72)
        print("2) ORPHAN TESTS (reference a source file/class/dir that " "does not exist):")
        for t in orphan:
            print(f"  [?] {t.relative_to(TEST_ROOT)}")

    if class_none:
        print("-" * 72)
        print("3) MODEL CLASSES WITH NO TEST AT ALL (real gaps):")
        for sf, classes in class_none:
            print(f"  [NONE] {sf.relative_to(SRC_ROOT)}")
            print(f"         classes: {', '.join(classes)}")

    if class_partial:
        print("-" * 72)
        print("3) MODEL CLASSES WITH PARTIAL COVERAGE (untested classes):")
        for sf, classes, tested in class_partial:
            missing = [c for c in classes if c not in tested]
            print(f"  [PART] {sf.relative_to(SRC_ROOT)}")
            print(f"         untested: {', '.join(missing)}")

    if misplaced:
        print("-" * 72)
        print("4) MISPLACED TESTS (not in the mirrored source dir, " "non-fatal):")
        for t in misplaced:
            print(f"  [>] {t.relative_to(TEST_ROOT)}")

    print("=" * 72)
    if uncovered or orphan or class_none:
        raise SystemExit(1)
    print("OK: file-presence parity and class coverage verified.")


def test_dir_for(src_file: Path) -> Path:
    rel = src_file.relative_to(SRC_ROOT).parent
    return TEST_ROOT / rel


if __name__ == "__main__":
    main()

# Model Test Parity Checker

This document describes `scripts/check_model_test_parity.py`, a tool that
verifies the unit-test suite for the model classes mirrors the structure of
the source under `src/armodel/models/`.

## Purpose

The model tree is large and grows continuously. This checker gives a fast,
whole-repo signal that:

- every model source file has a mirrored unit test, and
- every test references a real source entity (no dangling tests), and
- every model class is actually exercised by a test.

It is intended as a CI gate and as a triage aid for finding untested model
classes.

## Conventions it understands

The test suite is organized three ways, and the checker handles all of them:

- **Per file:** `src/.../Foo.py` -> `tests/.../test_Foo.py`
  (also `test_Foo_*.py`, a disambiguator suffix).
- **Per class:** `src/.../Foo.py` defining class `Bar` ->
  `tests/.../test_Bar.py` (anywhere in the test tree).
- **Per sub-package:** a package directory `Pkg/` ->
  `tests/.../Pkg/test_Pkg.py` (or `test___init__.py`,
  `test_<Pkg>_init.py`).

A class declared inside a package `__init__.py` is treated as a real class
(e.g. `PortPrototype` lives in `SWComponentTemplate/Components/__init__.py`
and is matched by `test_PortPrototype.py`).

`__init__.py` package markers are not model classes, so they are excluded
from the "uncovered source file" report.

## Usage

Run from the repository root:

```bash
python scripts/check_model_test_parity.py
```

The script exits non-zero when any of the following are present, so it is
safe to use as a CI step:

- an uncovered source file,
- an orphan test,
- a source file whose classes have no test at all.

## Output

The report has four sections.

### 1. File-presence parity (UNCOVERED)

Each source `Foo.py` (excluding `__init__.py`) should have a `test_Foo.py`
in the *mirrored* test directory. Missing ones are listed as:

```
  [ ] M2/AUTOSARTemplates/.../Foo.py
```

Note: this is a structural check. A file may still be tested by
class-named tests located in a subdirectory; the class-aware view (section 3)
is the authoritative "is it tested?" answer.

### 2. Orphan tests (ORPHAN)

A test `test_X.py` must map to a real source file `X.py`, a top-level class
`X` (including those in `__init__.py`), or a sub-package directory `X/`.
If none match, the source entity was likely renamed or removed and the test
is dangling:

```
  [?] M2/AUTOSARTemplates/GenericStructure/test_ArRef.py
```

### 3. Class-aware coverage (real gaps)

For each source file, every top-level class is checked for a dedicated
`test_<ClassName>.py` anywhere in the test tree. A file-level `test_Foo.py`
counts as covering all classes in `Foo.py`. Files where no class is tested
at all are reported as real gaps:

```
  [NONE] M2/AUTOSARTemplates/.../Foo.py
         classes: ClassA, ClassB
```

Files where only some classes are tested are reported separately as
`[PART]` with the untested class names.

### 4. Summary

A header line prints the counts for each section, e.g.:

```
Source model files (excl. __init__.py): 150
Test files                                 : 154
COVERED (test_Foo.py in mirrored dir)     : 110
UNCOVERED source files                    : 40
ORPHAN tests (no matching source entity) : 1
CLASSES untested (no test for any class) : 39
CLASSES partially tested                 : 0
```

## Scope

The checker only inspects `src/armodel/models/` and its mirror
`tests/test_armodel/models/`. Other testable packages (`data_models`, `lib`)
are intentionally out of scope; extend `SRC_ROOT` / `TEST_ROOT` at the top of
the script if broader coverage is needed.

# Design: Primitive Pattern Validation (ARLiteral regex enforcement)

Date: 2026-10-13 · Status: approved (design gate) · Branch: `feature/g21-sdg-primitive-var`

## Problem

~30 `ARLiteral` subclasses under
`src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/PrimitiveTypes.py`
(e.g. `McdIdentifier`, `MetaClassName`, `CIdentifierWithIndex`, `Identifier`, `Ref`,
`Ip4AddressString`, `RevisionLabelString`) document an `xml.xsd.pattern` regex in their
docstrings, but nothing enforces it: invalid values are accepted silently by the model
API and by the parser (when XSD `validate` is disabled or unavailable).

## Goals

1. Enforce the spec regex for constrained primitive literal values — always on.
2. A dedicated exception type (`PrimitivePatternError`) raised on violation.
3. The existing `warning` option downgrades raise → `logger.warning` (both for parser
   loads and for programmatic API use), mirroring `_validateARXML` behavior.
4. Patterns are canonical, XSD-first (`<xsd:pattern>` facets of the type named by the
   class's `xml.xsd.customType` Tag); markdown `xml.xsd.pattern` is the fallback only
   when the XSD has no facet. Docstring text is never parsed at runtime.

## Non-goals

- Writer-side validation, XSD codegen, registry generation (Approach A/B rejected —
  per-class attribute chosen).
- Changing `AREnum` membership semantics or `Numerical` numeric parsing.
- New CLI surface.

## Design

### 1. Pattern placement (per-class attribute, Approach C)

Each constrained `ARLiteral` subclass declares:

```python
PATTERN: Optional[str] = r"[A-Z][a-zA-Z0-9_]*"   # META-CLASS-NAME
```

- `ARLiteral` base declares `PATTERN: Optional[str] = None`; unconstrained subclasses
  inherit it and are skipped by validation.
- Pattern values are taken from the R23-11 XSD (e.g. `autosar/R23-11/xsd/AUTOSAR_00052.xsd`
  restriction facets); markdown fallback where the XSD lacks the facet. The XSD anchor
  (type name, e.g. `META-CLASS-NAME`) is recorded next to the attribute as a short
  comment-free convention: the class docstring's existing `xml.xsd.customType` Tag
  remains the provenance record (no new state).
- One-time extraction pass populates the existing constrained classes; future synced
  classes add `PATTERN` during their sync (see Rollout).

### 2. Exception

New module `src/armodel/validation/exceptions.py`:

```python
class PrimitivePatternError(ValueError):
    def __init__(self, class_name, value, pattern, xsd_type=None): ...
```

- Fields: `class_name`, `value`, `pattern`, optional `xsd_type`.
- Message shape: `value "<v>" does not match pattern "<p>" (<XSD-TYPE>)` (xsd_type
  omitted when unknown).
- Plain `ValueError` subclass; intentionally unrelated to the `ValidationError`
  result record in `validator.py` (that is a data record, not an exception).

### 3. Validation hook (always on)

- `ARLiteral` gains an instance method `checkValue(self, value)` (public, reusable)
  that reads `type(self).PATTERN`; the existing `value` setter calls it first.
- Semantics: skip when `cls.PATTERN is None`, value is `None`, or value is not a
  non-empty `str` (numerics/bools keep their own parse paths). Otherwise
  `re.fullmatch(cls.PATTERN, value)` must succeed (patterns are XSD facet regexes —
  full-string semantics; Python `re` covers the used facet syntax).
- On failure: consult the warning state (below) — raise `PrimitivePatternError` or
  emit a warning via `logging.getLogger(__name__)` and keep the value.
- Compiled patterns are cached per class (module-level `lru_cache`/dict keyed by
  pattern string).

### 4. Warning plumbing (thread-local warn mode)

- `src/armodel/validation/` gains a thread-local warn-mode switch (default off =
  raise), plus public helpers `set_warning_mode(enabled: bool)` and a context manager
  `warning_mode(enabled)` for scoped use.
- Parser: `ARXMLParser.load()` wraps the parse in `warning_mode(True)` when
  `self.options["warning"] is True`; violations then log (with file context added by
  the parser's existing logger) instead of raising. All other option combinations
  behave as today (raise).
- Programmatic API: default raise; users opt into warnings with the same helpers.
  Thread-local keeps library use re-entrant and parallel-safe.

### 5. Scope & rollout

- Phase 1 (this feature): populate `PATTERN` for the existing constrained literal
  classes in `PrimitiveTypes.py` (extraction pass, XSD-verified), implement exception +
  hook + warning plumbing + tests.
- Phase 2 (follow-up, separate change): the `sync-autosar-class` workflow gains a
  "PATTERN present and matches the XSD facet" expectation (audit check), so newly
  synced classes stay covered.
- Out of scope: classes outside `PrimitiveTypes.py` with docstring patterns (audit in
  Phase 2 decides), writer-side checks.

### 6. Testing

- Unit (new `tests/test_armodel/validation/` + per-class cases):
  - parametrized valid/invalid value per constrained class (XSD examples where
    available);
  - `PrimitivePatternError` fields/message; `PATTERN=None` and non-str passthrough;
  - warn-mode: downgrade logged, value kept, thread-local isolation (parallel parse
    simulation);
  - compiled-pattern caching.
- Parser integration (small fixture ARXML with one bad `McdIdentifier`-style value):
  - `warning=True` → warning logged, model still loaded;
  - default → `PrimitivePatternError` raised;
  - round-trip of a valid document unchanged.

## Risks / notes

- Some legacy files may contain values violating the strict XSD pattern (real-world
  ARXML is messier than the schema); the warning mode is the escape hatch, and default
  raise matches the existing `validate` option philosophy (strict by default,
  `warning=True` to tolerate).
- XSD facet regexes are XML-Schema flavor; the used subset (character classes,
  quantifiers, alternation, anchors implied) is compatible with Python `re`.

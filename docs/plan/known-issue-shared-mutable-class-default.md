# Known Issue: Shared Mutable Class Default

- Status: **Not fixed (decision pending)** — code left as-is; this file only records the finding
- Found: 2026-10-08
- Triggered by: Group21 9b audit — `AbstractVariationRestriction` fix (commit `0147d5143`)
- Related rules: Rule 0022 (`0..*` → `List[T]`), Rule 0004 (None guards)

## 1. Summary

In `AbstractVariationRestriction` (see
[ModelRestrictionTypes.py](../../src/armodel/models/M2/AUTOSARTemplates/GenericStructure/GeneralTemplateClasses/ModelRestrictionTypes.py)),
the `validBindingTimes` field was declared as a **class-level mutable default** in order to fix the
`AttributeError` raised by `VariationRestrictionWithSeverity`:

```python
class AbstractVariationRestriction(ARObject, ABC):
    # List of valid binding times. Tags: xml.sequenceOffset=20
    validBindingTimes: List[FullBindingTimeEnum] = []
```

The `list` object is created once when the class body is evaluated and is unique per process. Any subclass
instance that does **not shadow it with an instance attribute of the same name** shares that same list.
This is the classic mutable-default pitfall, just at class-attribute scope instead of function-signature scope.

For contrast: `variation: Optional[Boolean] = None` is a scalar (immutable) and carries no such risk.

## 2. Blast Radius

| Class | Location | Initializes instance attr? | Risk |
|---|---|---|---|
| `SdgPrimitiveAttributeWithVariation` | `SpecialDataDef.py:221` / reassigned at `:235` | Yes (`self.validBindingTimes = []`) | None |
| `SdgAggregationWithVariation` | `SpecialDataDef.py:238` / reassigned at `:254` | Yes | None |
| `SdgForeignReferenceWithVariation` | `SpecialDataDef.py:384` / reassigned at `:398` | Yes | None |
| `VariationRestrictionWithSeverity` | `ModelRestrictionTypes.py:278` (class body is `pass`) | **No** | **Shares the class-level list** |

So the risk currently lands **only** on `VariationRestrictionWithSeverity`; the other three subclasses
reassign the field in `__init__`, which creates an instance attribute that shadows the class attribute.

## 3. Concrete Consequences

### 3.1 Cross-instance leakage

```python
a = VariationRestrictionWithSeverity(...)
b = VariationRestrictionWithSeverity(...)
a.addValidBindingTime(FullBindingTimeEnum.CODE_GENERATION_TIME)
b.getValidBindingTimes()   # also sees CODE_GENERATION_TIME — should not
```

### 3.2 Getter returns an alias (more insidious)

`getValidBindingTimes()` simply does `return self.validBindingTimes`
(`ModelRestrictionTypes.py:246`). For a sharing instance, the caller receives **the class attribute itself**,
so a single `lst.append(...)` permanently pollutes the whole class: every instance created afterwards is born
with that value. On the writer side, `writeAbstractVariationRestriction` (`arxml_writer.py:15414`) iterates
the list and serializes it into the XML.

### 3.3 Process-lifetime residue and test-order dependence

The pollution does not disappear when the object is destroyed; its lifetime equals the interpreter's lifetime.
It shows up as: a test passes when run alone, but fails when the full suite runs because another test case
introduced dirty data earlier (flaky / order-dependent) — the hardest class of bug to locate.
If the parser ever parses in threads, it also becomes a data race.

## 4. Why "subclasses reassign it" Is Not a Safety Net

Shadowing depends on **every** subclass remembering to write `self.validBindingTimes = []`. That is a
convention, not an enforced guarantee:

- a new subclass that forgets to do so silently joins the shared list;
- the repo has a known combined-inheritance issue — `Referrable.__init__` calls `ARObject.__init__`
  directly (bypassing `super()`) — so "just add an `__init__` to the abstract base class" is not a reliable
  path. This is precisely why class-level defaults were used in the first place.

Conclusion: this is a time-bomb-shaped fragile design that merely happens to have no trigger path today.

## 5. Candidate Fixes (none applied)

### Option A: Drop the shared default; initialize per instance in each subclass (recommended)

- Remove the class-level default of `AbstractVariationRestriction.validBindingTimes`;
- Give `VariationRestrictionWithSeverity` its own `__init__` that sets `self.validBindingTimes = []`;
- The abstract base's three accessors still raise `AttributeError` on an uninitialized instance, so **every**
  concrete subclass is then required to initialize the field.

Pros: no sharing, no aliasing. Cons: adding a subclass still requires remembering the init (convention risk
remains, but at least nothing is silently shared).

### Option B: Lazy initialization

- In the accessors, create an instance-level empty list on first use when the attribute is absent
  (e.g. `if not hasattr(self, "validBindingTimes")`), or fall back via `getattr`.

Pros: safe for any subclass. Cons: departs from the repo's existing accessor style — a new paradigm that
would need review sign-off.

### Option C: Keep the status quo (current choice)

Keep the shared default and record it only as a known defect. Precondition: `VariationRestrictionWithSeverity`
is not used as a mutable object anywhere in the current codebase (it is referenced only by the stub
inheritance-relationship tests).

## 6. Repro / Verification Hint

If a fix is confirmed later, this minimal repro verifies whether the pollution is gone:

```python
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ModelRestrictionTypes import (
    VariationRestrictionWithSeverity,
)

a = VariationRestrictionWithSeverity()
b = VariationRestrictionWithSeverity()
a.addValidBindingTime("CODE-GENERATION-TIME")
assert b.getValidBindingTimes() == [], "shared mutable class default leaked"
```

## 7. TODO

- [ ] Decide between Option A / B / C
- [ ] If A/B: modify `ModelRestrictionTypes.py` (and possibly `SpecialDataDef.py`)
- [ ] If A/B: re-run `audit_class.py AbstractVariationRestriction` + full `pytest`

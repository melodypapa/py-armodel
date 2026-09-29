# ClientServerOperationMapping forward-reference cleanup

## Goal

Remove the quoted `DataPrototypeMapping` references from `ClientServerOperationMapping` while preserving runtime importability and the resolved public type hints.

## Current state

In `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/PortInterface/__init__.py`, `ClientServerOperationMapping` is defined before `DataPrototypeMapping`. The consumer currently uses quoted forward references in the `argumentMappings` field annotation, `addArgumentMapping` parameter, and `getArgumentMappings` return annotation. `DataPrototypeMapping` itself depends on `TextTableMapping` and `SubElementMapping`, both defined between these classes. The module does not enable postponed annotation evaluation.

## Design

Move the contiguous `TextTableMapping`, `SubElementMapping`, and `DataPrototypeMapping` class definitions so they appear before `ClientServerOperationMapping`. Preserve each class body and relative order unchanged. Then replace the three quoted `DataPrototypeMapping` references with bare class references. Keep the quoted `ClientServerOperationMapping` self-return annotations unchanged; they are independent forward references within that class and are outside this change.

## Alternatives considered

- Keep the quoted forward references: smallest and valid, but does not meet the requested cleanup.
- Add `from __future__ import annotations`: affects annotation representation across the entire module and conflicts with existing repository checks unless other top-level quoted annotations are normalized too.
- Move the three dependency classes as a block: keeps runtime annotation evaluation and limits type changes to the requested references, at the cost of relocating a substantial block of class definitions. This is the selected approach.

## Tests and validation

Add a test that checks the three `ClientServerOperationMapping` annotations are actual resolved `DataPrototypeMapping` types, including the `argumentMappings` field annotation in the source AST. Run the focused PortInterface model tests and paired parser/writer mapping-set tests, followed by lint and Black checks. Confirm imports and `typing.get_type_hints` continue to resolve correctly.

## Scope and non-goals

No model behavior, serialization, parser/writer logic, docstrings, AUTOSAR spec checklist, or class implementations are to change. The paused `ClientServerApplicationErrorMapping` confirmation is a separate task and remains untouched by this refactor.

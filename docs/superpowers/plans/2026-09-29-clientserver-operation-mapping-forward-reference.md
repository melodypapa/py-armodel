# ClientServerOperationMapping Forward-Reference Cleanup Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Remove quotes from `ClientServerOperationMapping`'s three `DataPrototypeMapping` annotations without changing runtime imports or resolved type hints.

**Architecture:** Move `MappingDirectionEnum` before `TextTableMapping`, then place the unchanged `TextTableMapping`, `SubElementMapping`, and `DataPrototypeMapping` block before `ClientServerOperationMapping`. The final declaration order is `MappingDirectionEnum`, `TextTableMapping`, `SubElementMapping`, `DataPrototypeMapping`, `ClientServerOperationMapping`. Then use bare `DataPrototypeMapping` references in the member field, adder parameter, and getter return annotation; leave self-return annotations unchanged.

**Tech Stack:** Python 3.8-compatible annotations, pytest, Black, flake8, Ruff.

## Global Constraints

- Python 3.8 compatibility: use `typing.List` / `typing.Optional`; do not add PEP 604 syntax.
- Do not add comments or change model behavior, reader/writer logic, docstrings, or spec checklist content.
- Keep runtime annotation resolution available without adding `from __future__ import annotations` to the module.
- Preserve the four moved class bodies byte-for-byte; make only the three requested annotation edits in `ClientServerOperationMapping`.

---

### Task 1: Add a regression test for bare member-type annotations

**Files:**
- Modify: `tests/test_armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/PortInterface/test_PortInterface.py`
- Production source under test: `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/PortInterface/__init__.py`

**Interfaces:**
- Uses existing imports `inspect`, `List`, `Optional`, `ClientServerOperationMapping`, and `DataPrototypeMapping`.
- Adds no public production interface.

- [x] **Step 1: Write the failing test**

Add this method to `TestClientServerOperationMapping`:

```python
    def test_argument_mapping_annotations_are_bare(self):
        assert ClientServerOperationMapping.addArgumentMapping.__annotations__["value"] == Optional[DataPrototypeMapping]
        assert ClientServerOperationMapping.getArgumentMappings.__annotations__["return"] == List[DataPrototypeMapping]
        init_source = inspect.getsource(ClientServerOperationMapping.__init__)
        assert "self.argumentMappings: List[DataPrototypeMapping] = []" in init_source
```

- [x] **Step 2: Run the test to verify it fails for the quoted forward references**

Run: `uv run pytest tests/test_armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/PortInterface/test_PortInterface.py::TestClientServerOperationMapping::test_argument_mapping_annotations_are_bare -q`

Expected: FAIL because the raw method annotations contain `ForwardRef('DataPrototypeMapping')` and the initializer source currently contains `List["DataPrototypeMapping"]`.

### Task 2: Move the dependency classes and remove the three quotes

**Files:**
- Modify: `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/PortInterface/__init__.py`

**Interfaces:**
- The consumer annotations resolve directly to the existing `DataPrototypeMapping` class object.
- `MappingDirectionEnum`, `TextTableMapping`, `SubElementMapping`, and `DataPrototypeMapping` retain their current definitions and move into dependency order before `ClientServerOperationMapping`.

- [ ] **Step 1: Move `MappingDirectionEnum` before `TextTableMapping`**

Move the complete `MappingDirectionEnum` class definition, including its checklist, before `TextTableMapping`. Preserve its body and checklist unchanged. This is required because `TextTableMapping` annotates `mappingDirection` with that enum.

- [ ] **Step 2: Move the mapping-class block before `ClientServerOperationMapping`**

Move the complete contiguous definitions `TextTableMapping`, `SubElementMapping`, and `DataPrototypeMapping`, in that order, to immediately before `ClientServerOperationMapping`. Preserve their method bodies, annotations, docstrings, and checklist comments unchanged. The final order must be `MappingDirectionEnum`, `TextTableMapping`, `SubElementMapping`, `DataPrototypeMapping`, `ClientServerOperationMapping`.

- [ ] **Step 3: Replace the consumer's three quoted type references**

Replace the three existing annotation lines with these exact lines:

```python
        self.argumentMappings: List[DataPrototypeMapping] = []
    def addArgumentMapping(self, value: Optional[DataPrototypeMapping]) -> "ClientServerOperationMapping":
    def getArgumentMappings(self) -> List[DataPrototypeMapping]:
```

Keep the existing method implementations and docstrings exactly as they are. Do not change the quoted `"ClientServerOperationMapping"` self-return annotations.

### Task 3: Verify the regression and affected behavior

**Files:**
- Test: `tests/test_armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/PortInterface/test_PortInterface.py`
- Test: `tests/test_armodel/parser/test_ar_package_port_interface_mapping_set.py`
- Test: `tests/test_armodel/writer/test_ar_package_port_interface_mapping_set.py`

**Interfaces:**
- Confirms `typing.get_type_hints` still resolves the consumer methods to `Optional[DataPrototypeMapping]` and `List[DataPrototypeMapping]`.
- Confirms parser/writer round-trips continue to work with the relocated class definitions.

- [ ] **Step 1: Run all focused PortInterface model, parser, and writer tests**

Run: `uv run pytest tests/test_armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/PortInterface/test_PortInterface.py tests/test_armodel/parser/test_ar_package_port_interface_mapping_set.py tests/test_armodel/writer/test_ar_package_port_interface_mapping_set.py -q`

Expected: all focused tests pass, including `test_argument_mapping_annotations_are_bare`.

- [ ] **Step 2: Run lint and formatting checks**

Run: `npm run lint && npm run black-check`

Expected: flake8 and Ruff pass; Black reports the touched files unchanged.

- [ ] **Step 3: Commit the completed refactor**

```bash
git add src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/PortInterface/__init__.py tests/test_armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/PortInterface/test_PortInterface.py docs/superpowers/plans/2026-09-29-clientserver-operation-mapping-forward-reference.md
git commit -m "refactor: remove DataPrototypeMapping forward-reference quotes"
```

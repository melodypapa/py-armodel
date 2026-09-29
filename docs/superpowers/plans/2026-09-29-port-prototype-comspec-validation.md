# Port Prototype ComSpec Validation Improvement Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make both port-prototype ComSpec validators check constrained reference `DEST` values only when those optional references are present.

**Architecture:** Keep `_validateProvidedComSpec` and `_validateRequiredComSpec` and their current ComSpec subclass allowlists. Follow `ClientComSpec`'s accessor pattern by retrieving a reference once, validating its `DEST` if non-`None`, accepting absence, and keeping explicit subtype-specific branches and unsupported-type errors.

**Tech Stack:** Python 3.8-compatible annotations, pytest, Black, flake8, Ruff.

## Global Constraints

- An absent constrained ComSpec reference is accepted; a present reference with the wrong `DEST` raises `ValueError`.
- Keep the PPort and RPort subtype allowlists unchanged.
- Do not change ComSpec models, parser/writer behavior, reference multiplicities, or add a shared helper.
- Keep existing error text for wrong `DEST` and unsupported ComSpec types stable.
- Run tests in the repo's uv-managed environment with `uv run pytest`.

---

### Task 1: Test reference validation only when references exist

**Files:**
- Modify: `tests/test_armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Components/test_Components.py`
- Production under test: `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Components/__init__.py`

**Interfaces:**
- Uses imported `PPortPrototype`, `RPortPrototype`, `NonqueuedSenderComSpec`, `ClientComSpec`, `NonqueuedReceiverComSpec`, `ParameterRequireComSpec`, and `RefType`.
- Calls public `addProvidedComSpec` / `addRequiredComSpec`, which invoke the respective validators before appending.

- [x] **Step 1: Add the behavior test first**

Add this test method to `Test_M2_AUTOSARTemplates_SWComponentTemplate_Components`:

```python
    def test_comspec_refs_are_optional_but_dest_is_checked_when_present(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        provided_port = PPortPrototype(ar_root, "Provided")
        required_port = RPortPrototype(ar_root, "Required")

        sender_without_ref = NonqueuedSenderComSpec()
        provided_port.addProvidedComSpec(sender_without_ref)
        assert provided_port.getProvidedComSpecs() == [sender_without_ref]

        sender_ref = RefType().setValue("/Test/Variable")
        sender_ref.dest = "VARIABLE-DATA-PROTOTYPE"
        sender_with_ref = NonqueuedSenderComSpec().setDataElementRef(sender_ref)
        provided_port.addProvidedComSpec(sender_with_ref)
        assert provided_port.getProvidedComSpecs() == [sender_without_ref, sender_with_ref]

        client_without_ref = ClientComSpec()
        receiver_without_ref = NonqueuedReceiverComSpec()
        parameter_without_ref = ParameterRequireComSpec()
        for com_spec in (client_without_ref, receiver_without_ref, parameter_without_ref):
            required_port.addRequiredComSpec(com_spec)

        client_ref = RefType().setValue("/Test/Operation")
        client_ref.dest = "CLIENT-SERVER-OPERATION"
        client_with_ref = ClientComSpec().setOperationRef(client_ref)
        receiver_ref = RefType().setValue("/Test/Variable")
        receiver_ref.dest = "VARIABLE-DATA-PROTOTYPE"
        receiver_with_ref = NonqueuedReceiverComSpec().setDataElementRef(receiver_ref)
        parameter_ref = RefType().setValue("/Test/Parameter")
        parameter_ref.dest = "PARAMETER-DATA-PROTOTYPE"
        parameter_with_ref = ParameterRequireComSpec().setParameterRef(parameter_ref)
        for com_spec in (client_with_ref, receiver_with_ref, parameter_with_ref):
            required_port.addRequiredComSpec(com_spec)

        assert required_port.getRequiredComSpecs() == [client_without_ref, receiver_without_ref, parameter_without_ref, client_with_ref, receiver_with_ref, parameter_with_ref]
```

- [x] **Step 2: Run the new test and verify the expected failure**

Run: `uv run pytest tests/test_armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Components/test_Components.py::Test_M2_AUTOSARTemplates_SWComponentTemplate_Components::test_comspec_refs_are_optional_but_dest_is_checked_when_present -q`

Expected before implementation: FAIL because `_validateProvidedComSpec` raises `ValueError` for `sender_without_ref`.

- [x] **Step 3: Remove the obsolete missing-reference error expectation and exercise rejection through add methods**

In `test_Validate_PPortComSpec_Errors`, remove the block that constructs `com_spec_no_ref` and expects `ValueError("operation of NonqueuedSenderComSpec is invalid")`. In the wrong-destination PPort block, replace the direct `_validateProvidedComSpec` call with `provided_port.addProvidedComSpec(com_spec_invalid_dest)` and assert after the `pytest.raises` block that `com_spec_invalid_dest not in provided_port.getProvidedComSpecs()`.

In `test_Validate_RPortComSpec_Errors`, replace the direct validator call in each wrong-destination `pytest.raises` block with the corresponding `required_port.addRequiredComSpec(client_spec)`, `required_port.addRequiredComSpec(receiver_spec)`, or `required_port.addRequiredComSpec(param_spec)`. Preserve each existing error-message assertion and immediately after each `pytest.raises` context add the corresponding exact assertion: `assert client_spec not in required_port.getRequiredComSpecs()`, `assert receiver_spec not in required_port.getRequiredComSpecs()`, and `assert param_spec not in required_port.getRequiredComSpecs()`. Keep the unsupported-type check calling `_validateRequiredComSpec` directly so the unsupported-type path remains explicitly covered.

### Task 2: Update both validators to use optional getter-based `DEST` checks

**Files:**
- Modify: `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Components/__init__.py`

**Interfaces:**
- `_validateProvidedComSpec(self, com_spec: PPortComSpec)` retains accepted types `NonqueuedSenderComSpec`, `ServerComSpec`, `QueuedSenderComSpec`, `ModeSwitchSenderComSpec`, `NvProvideComSpec`, and `ParameterProvideComSpec`.
- `_validateRequiredComSpec(self, com_spec: RPortComSpec)` retains accepted types `ClientComSpec`, `NonqueuedReceiverComSpec`, `QueuedReceiverComSpec`, `ModeSwitchReceiverComSpec`, `ParameterRequireComSpec`, and `NvRequireComSpec`.

- [x] **Step 1: Change the NonqueuedSenderComSpec validation branch**

Replace the mandatory-ref/direct-field checks with:

```python
        if isinstance(com_spec, NonqueuedSenderComSpec):
            data_element_ref = com_spec.getDataElementRef()
            if data_element_ref is not None and data_element_ref.getDest() != "VARIABLE-DATA-PROTOTYPE":
                raise ValueError("Invalid operation dest of NonqueuedSenderComSpec")
```

Leave all remaining `elif` branches and the unsupported-type `else` unchanged.

- [x] **Step 2: Read each required-side reference once and check its destination only when present**

Replace the three repeated getter checks in `_validateRequiredComSpec` with these branch bodies, keeping the existing error strings:

```python
        if isinstance(com_spec, ClientComSpec):
            operation_ref = com_spec.getOperationRef()
            if operation_ref is not None and operation_ref.getDest() != "CLIENT-SERVER-OPERATION":
                raise ValueError("Invalid operation dest of ClientComSpec.")
        elif isinstance(com_spec, NonqueuedReceiverComSpec):
            data_element_ref = com_spec.getDataElementRef()
            if data_element_ref is not None and data_element_ref.getDest() != "VARIABLE-DATA-PROTOTYPE":
                raise ValueError("Invalid date element dest of NonqueuedReceiverComSpec.")
```

For `ParameterRequireComSpec`, use the corresponding accessor and preserve the message:

```python
        elif isinstance(com_spec, ParameterRequireComSpec):
            parameter_ref = com_spec.getParameterRef()
            if parameter_ref is not None and parameter_ref.getDest() != "PARAMETER-DATA-PROTOTYPE":
                raise ValueError("Invalid parameter dest of ParameterRequireComSpec.")
```

Leave `QueuedReceiverComSpec`, `ModeSwitchReceiverComSpec`, `NvRequireComSpec`, and the unsupported-type branch unchanged.

- [x] **Step 3: Run the new test and existing focused error tests**

Run: `uv run pytest tests/test_armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Components/test_Components.py -k 'comspec_refs_are_optional_but_dest_is_checked_when_present or Validate_PPortComSpec_Errors or Validate_RPortComSpec_Errors' -q`

Expected: PASS; absent references are accepted, valid destinations append successfully, existing invalid-destination messages remain, and unsupported types remain rejected.

### Task 3: Verify the component model suite and quality gates

**Files:**
- Source: `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Components/__init__.py`
- Tests: `tests/test_armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Components/test_Components.py`

- [x] **Step 1: Run the complete Components model test file**

Run: `uv run pytest tests/test_armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Components/test_Components.py -q`

Expected: all tests pass.

- [x] **Step 2: Run lint, formatting, and whitespace checks**

Run: `npm run lint && npm run black-check && git diff --check`

Expected: flake8 and Ruff pass; Black reports no formatting changes; `git diff --check` reports no whitespace errors.

- [x] **Step 3: Commit the implementation** — `31fb21c1`

```bash
git add src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Components/__init__.py tests/test_armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Components/test_Components.py
git commit -m "fix: validate optional port ComSpec reference destinations"
```

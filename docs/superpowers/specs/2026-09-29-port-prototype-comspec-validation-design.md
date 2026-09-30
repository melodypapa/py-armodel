# Port Prototype ComSpec Validation Design

## Goal

Improve `_validateProvidedComSpec` and `_validateRequiredComSpec` so ComSpec references are checked for the expected AUTOSAR `DEST` when present, without treating an absent optional reference as an error.

## Current behavior

The validators live on `AbstractProvidedPortPrototype` and `AbstractRequiredPortPrototype` in `src/armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Components/__init__.py`.

- `_validateProvidedComSpec` accepts the established PPort ComSpec subclasses. For `NonqueuedSenderComSpec`, it currently rejects a missing `dataElementRef` and checks `DEST` via the field directly.
- `_validateRequiredComSpec` accepts the established RPort ComSpec subclasses. For `ClientComSpec`, `NonqueuedReceiverComSpec`, and `ParameterRequireComSpec`, it retrieves the corresponding reference and checks `DEST` only when that optional reference is present.
- Both validators reject unsupported ComSpec types.

The desired pattern follows `ClientComSpec` reference access: use the public getter and validate the returned reference's `DEST` only when non-`None`.

## Design

Keep both validators and their existing ComSpec subtype allowlists. For every subtype branch with a reference whose destination is constrained, retrieve it through its getter and compare its `DEST` only if the reference is present:

- `NonqueuedSenderComSpec.getDataElementRef()` → `VARIABLE-DATA-PROTOTYPE`.
- `ClientComSpec.getOperationRef()` → `CLIENT-SERVER-OPERATION`.
- `NonqueuedReceiverComSpec.getDataElementRef()` → `VARIABLE-DATA-PROTOTYPE`.
- `ParameterRequireComSpec.getParameterRef()` → `PARAMETER-DATA-PROTOTYPE`.

An absent reference is accepted by these validators; this change does not add required-reference checks. Present references with a wrong `DEST` continue to raise `ValueError`. Existing supported-type handling and unsupported-type rejection remain intact. No shared helper is introduced; the explicit branches are short and preserve the class-specific error context.

## Test design

Update and extend the existing validator tests in `tests/test_armodel/models/M2/AUTOSARTemplates/SWComponentTemplate/Components/test_Components.py` to cover:

- PPort `NonqueuedSenderComSpec` with absent reference (accepted), expected `DEST` (accepted), and wrong `DEST` (rejected).
- RPort `ClientComSpec`, `NonqueuedReceiverComSpec`, and `ParameterRequireComSpec` with absent references (accepted), expected `DEST` (accepted), and wrong `DEST` (rejected).
- Existing unsupported PPort and RPort ComSpec rejections.
- Public `addProvidedComSpec` / `addRequiredComSpec` continue appending accepted specs and do not append specs rejected by validation.

Keep error wording stable for existing wrong-`DEST` and unsupported-type errors unless a test demonstrates it is necessary to adjust wording. Remove or revise the existing test that currently treats a missing PPort data-element reference as an error.

## Scope and non-goals

Do not change the AUTOSAR ComSpec classes, parser/writer behavior, the existing subtype allowlists, or any reference multiplicities in the model. Do not add a generic validation framework or shared helper. The change is limited to the two port-prototype validators and their tests.

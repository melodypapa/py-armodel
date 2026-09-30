# ComSpec DEST Validation Design

## Goal

Validate the constrained reference destination (`DEST`) for every concrete ComSpec type accepted by `AbstractProvidedPortPrototype` and `AbstractRequiredPortPrototype`. A ComSpec with a mismatching destination, or a subtype unsupported on that port side, must emit a warning and must not be appended. Validation must not raise an exception.

## Scope

The implementation is limited to reference `DEST` validation and subtype support in the PPort and RPort ComSpec validators. It will not validate other attributes, reference paths/target existence, reference presence, parser behavior, writer behavior, or ComSpec model classes. A missing optional reference has no `DEST` to compare and is accepted. Passing `None` to an add method remains a no-op.

## Supported subtype/reference matrix

The current model hierarchy contains six concrete supported subtypes on each port side. Reference target types below follow AUTOSAR CP R23-11 Software Component Template tables for the ComSpec classes and inherited `SenderComSpec`/`ReceiverComSpec` reference declarations.

| Port side | ComSpec subtype | Reference accessor | Expected `DEST` |
|---|---|---|---|
| PPort | `NonqueuedSenderComSpec` | `getDataElementRef()` | `VARIABLE-DATA-PROTOTYPE` |
| PPort | `QueuedSenderComSpec` | `getDataElementRef()` | `VARIABLE-DATA-PROTOTYPE` |
| PPort | `ServerComSpec` | `getOperationRef()` | `CLIENT-SERVER-OPERATION` |
| PPort | `ModeSwitchSenderComSpec` | `getModeGroupRef()` | `MODE-DECLARATION-GROUP-PROTOTYPE` |
| PPort | `NvProvideComSpec` | `getVariableRef()` | `VARIABLE-DATA-PROTOTYPE` |
| PPort | `ParameterProvideComSpec` | `getParameterRef()` | `PARAMETER-DATA-PROTOTYPE` |
| RPort | `ClientComSpec` | `getOperationRef()` | `CLIENT-SERVER-OPERATION` |
| RPort | `NonqueuedReceiverComSpec` | `getDataElementRef()` | `VARIABLE-DATA-PROTOTYPE` |
| RPort | `QueuedReceiverComSpec` | `getDataElementRef()` | `VARIABLE-DATA-PROTOTYPE` |
| RPort | `ModeSwitchReceiverComSpec` | `getModeGroupRef()` | `MODE-DECLARATION-GROUP-PROTOTYPE` |
| RPort | `NvRequireComSpec` | `getVariableRef()` | `VARIABLE-DATA-PROTOTYPE` |
| RPort | `ParameterRequireComSpec` | `getParameterRef()` | `PARAMETER-DATA-PROTOTYPE` |

The AUTOSAR source references are the R23-11 Software Component Template tables: `SenderComSpec` (4.67), `ReceiverComSpec` (4.60), `ClientComSpec` (4.77), `ServerComSpec` (4.78), `ModeSwitchSenderComSpec` (4.79), `ModeSwitchReceiverComSpec` (4.81), `ParameterProvideComSpec` (4.82), `ParameterRequireComSpec` (4.83), `NvRequireComSpec` (4.84), and `NvProvideComSpec` (4.85). The queued and nonqueued sender/receiver classes inherit their respective data-element references.

## Behavior and architecture

Keep the subtype handling explicit in `_validateProvidedComSpec` and `_validateRequiredComSpec`; do not introduce a shared helper or move validation into model classes. For each recognized subtype, retrieve its reference once. If it is absent, validation succeeds. If present with the expected destination, validation succeeds. If present with a mismatching destination, log a warning and return an invalid result. Unsupported subtypes also log a warning and return an invalid result rather than raising.

The public `addProvidedComSpec` and `addRequiredComSpec` methods append only when the respective validator reports success. Thus warning cases leave the stored list unchanged, and valid or reference-absent supported ComSpecs are appended.

## Testing

Tests will cover each concrete subtype on its correct port side, including valid destinations, mismatching destinations, and absent references. Mismatches must be observable as warnings and must not append the ComSpec or raise. Unsupported subtypes must warn and be skipped. Existing `None` no-op behavior and validation of both port sides remain covered.

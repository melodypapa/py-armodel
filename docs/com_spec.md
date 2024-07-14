Allowed combinations of a specific Type of PortInterface, a specific Type of PortPrototype, and a specific Type of ComSpec

| Type of PortPrototype | Type of ComSpec           | Role of Element | Type of PortInterface   | Role of Type-Ref          |
| --------------------- | ------------------------- | --------------- | ----------------------- | ------------------------- |
| PPortPrototype        | NonqueuedSenderComSpec    | dataElement     | SenderReceiverInterface | providedInterface         |
| PPortPrototype        | QueuedSenderComSpec       | dataElement     | SenderReceiverInterface | providedInterface         |
| RPortPrototype        | NonqueuedReceiverComSpec  | dataElement     | SenderReceiverInterface | requiredInterface         |
| RPortPrototype        | QueuedReceiverComSpec     | dataElement     | SenderReceiverInterface | requiredInterface         |
| PRPortPrototype       | NonqueuedSenderComSpec    | dataElement     | SenderReceiverInterface | providedRequiredInterface |
| PRPortPrototype       | NonqueuedReceiverComSpec  | dataElement     | SenderReceiverInterface | providedRequiredInterface |
| PRPortPrototype       | QueuedReceiverComSpec     | dataElement     | SenderReceiverInterface | providedRequiredInterface |
| PRPortPrototype       | QueuedSenderComSpec       | dataElement     | SenderReceiverInterface | providedRequiredInterface |
| PPortPrototype        | NvProvideComSpec          | nvData          | NvDataInterface         | providedInterface         |
| RPortPrototype        | NvRequireComSpec          | nvData          | NvDataInterface         | requiredInterface         |
| PRPortPrototype       | NvProvideComSpec          | nvData          | NvDataInterface         | providedRequiredInterface |
| PRPortPrototype       | NvRequireComSpec          | nvData          | NvDataInterface         | providedRequiredInterface |
| PPortPrototype        | ModeSwitchSenderComSpec   | modeGroup       | ModeSwitchInterface     | providedInterface         |
| RPortPrototype        | ModeSwitchReceiverComSpec | modeGroup       | ModeSwitchInterface     | requiredInterface         |
| PRPortPrototype       | ModeSwitchSenderComSpec   | modeGroup       | ModeSwitchInterface     | providedRequiredInterface |
| PRPortPrototype       | ModeSwitchReceiverComSpec | modeGroup       | ModeSwitchInterface     | providedRequiredInterface |
| PPortPrototype        | ParameterProvideComSpec   | parameter       | ParameterInterface      | providedInterface         |
| RPortPrototype        | ParameterRequireComSpec   | parameter       | ParameterInterface      | requiredInterface         |
| PPortPrototype        | ServerComSpec             | operation       | ClientServerInterface   | providedInterface         |
| RPortPrototype        | ClientComSpec             | operation       | ClientServerInterface   | requiredInterface         |
| PRPortPrototype       | ServerComSpec             | operation       | ClientServerInterface   | providedRequiredInterface |
| PRPortPrototype       | ClientComSpec             | operation       | ClientServerInterface   | providedRequiredInterface |
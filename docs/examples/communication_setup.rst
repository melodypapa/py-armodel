Communication Setup Examples
=============================

This section provides examples for setting up communication in AUTOSAR models.

Example 1: Create Sender-Receiver Interface
-------------------------------------------

.. code-block:: python

   from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
   from armodel.models.M2.AUTOSARTemplates.CommonStructure.GenericStructure.PortInterface import SenderReceiverInterface, DataPrototype
   from armodel.models.M2.AUTOSARTemplates.CommonStructure.GenericStructure.DataTypeImplementation import ImplementationDataType
   from armodel.models.M2.AUTOSARTemplates.CommonStructure.GenericStructure.ARObj import ARRef
   from armodel.writer.arxml_writer import ARXMLWriter

   # Initialize AUTOSAR
   autosar = AUTOSAR.getInstance()
   autosar.new()
   autosar.setARRelease('R24-11')

   # Create package
   package = autosar.createARPackage('MyPackage')

   # Create data type
   data_type = ImplementationDataType()
   data_type.short_name = 'MyDataType'
   data_type.category = 'TYPE_REFERENCE'
   package.addImplementationDataType(data_type)

   # Create sender-receiver interface
   interface = SenderReceiverInterface()
   interface.short_name = 'MySenderReceiverInterface'

   # Create data element
   data_element = DataPrototype()
   data_element.short_name = 'MyDataElement'
   data_element.type_ref = ARRef(data_type)

   # Add data element to interface
   interface.data_elements.append(data_element)

   # Add to package
   package.addSenderReceiverInterface(interface)

   # Write to file
   writer = ARXMLWriter()
   writer.write_to_file(autosar, 'sender_receiver_interface.arxml')

   print("Created sender-receiver interface")

Example 2: Create Client-Server Interface
------------------------------------------

.. code-block:: python

   from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
   from armodel.models.M2.AUTOSARTemplates.CommonStructure.GenericStructure.PortInterface import ClientServerInterface, Operation, Argument
   from armodel.models.M2.AUTOSARTemplates.CommonStructure.GenericStructure.DataTypeImplementation import ImplementationDataType
   from armodel.models.M2.AUTOSARTemplates.CommonStructure.GenericStructure.ARObj import ARRef
   from armodel.writer.arxml_writer import ARXMLWriter

   # Initialize AUTOSAR
   autosar = AUTOSAR.getInstance()
   autosar.new()
   autosar.setARRelease('R24-11')

   # Create package
   package = autosar.createARPackage('MyPackage')

   # Create data types
   input_type = ImplementationDataType()
   input_type.short_name = 'InputType'
   input_type.category = 'TYPE_REFERENCE'
   package.addImplementationDataType(input_type)

   output_type = ImplementationDataType()
   output_type.short_name = 'OutputType'
   output_type.category = 'TYPE_REFERENCE'
   package.addImplementationDataType(output_type)

   # Create client-server interface
   interface = ClientServerInterface()
   interface.short_name = 'MyClientServerInterface'
   interface.is_service = True

   # Create operation
   operation = Operation()
   operation.short_name = 'MyOperation'

   # Create input argument
   input_arg = Argument()
   input_arg.short_name = 'InputArg'
   input_arg.type_ref = ARRef(input_type)
   input_arg.direction = 'IN'

   # Create output argument
   output_arg = Argument()
   output_arg.short_name = 'OutputArg'
   output_arg.type_ref = ARRef(output_type)
   output_arg.direction = 'OUT'

   # Add arguments to operation
   operation.arguments.append(input_arg)
   operation.arguments.append(output_arg)

   # Add operation to interface
   interface.operations.append(operation)

   # Add to package
   package.addClientServerInterface(interface)

   # Write to file
   writer = ARXMLWriter()
   writer.write_to_file(autosar, 'client_server_interface.arxml')

   print("Created client-server interface")

Example 3: Create System Signal
--------------------------------

.. code-block:: python

   from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
   from armodel.models.M2.AUTOSARTemplates.CommonStructure.SystemTemplate.System import SystemSignal
   from armodel.writer.arxml_writer import ARXMLWriter

   # Initialize AUTOSAR
   autosar = AUTOSAR.getInstance()
   autosar.new()
   autosar.setARRelease('R24-11')

   # Create package
   package = autosar.createARPackage('MyPackage')

   # Create system signal
   signal = SystemSignal()
   signal.short_name = 'MySystemSignal'

   # Add to package
   package.addSystemSignal(signal)

   # Write to file
   writer = ARXMLWriter()
   writer.write_to_file(autosar, 'system_signal.arxml')

   print("Created system signal")

Example 4: Create Assembly Connector
-------------------------------------

.. code-block:: python

   from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
   from armodel.models.M2.AUTOSARTemplates.CommonStructure.SWComponentTemplate.ApplicationSwComponentType import ApplicationSwComponentType
   from armodel.models.M2.AUTOSARTemplates.CommonStructure.SWComponentTemplate.CompositionSwComponentType import CompositionSwComponentType
   from armodel.models.M2.AUTOSARTemplates.CommonStructure.SWComponentTemplate.SwConnector import AssemblySwConnector, SwComponentPrototype
   from armodel.models.M2.AUTOSARTemplates.CommonStructure.SWComponentTemplate.PortPrototype import PPortPrototype, RPortPrototype, PPortInCompositionInstanceRef, RPortInCompositionInstanceRef
   from armodel.models.M2.AUTOSARTemplates.CommonStructure.GenericStructure.PortInterface import SenderReceiverInterface
   from armodel.models.M2.AUTOSARTemplates.CommonStructure.GenericStructure.ARObj import ARRef
   from armodel.writer.arxml_writer import ARXMLWriter

   # Initialize AUTOSAR
   autosar = AUTOSAR.getInstance()
   autosar.new()
   autosar.setARRelease('R24-11')

   # Create package
   package = autosar.createARPackage('MyPackage')

   # Create interface
   interface = SenderReceiverInterface()
   interface.short_name = 'MyInterface'
   package.addSenderReceiverInterface(interface)

   # Create two components
   comp1 = ApplicationSwComponentType()
   comp1.short_name = 'Provider'
   comp1.category = 'APPLICATION'

   comp2 = ApplicationSwComponentType()
   comp2.short_name = 'Consumer'
   comp2.category = 'APPLICATION'

   # Add ports
   port1 = PPortPrototype()
   port1.short_name = 'DataOut'
   port1.provided_interface_ref = ARRef(interface)
   comp1.addProvidedPort(port1)

   port2 = RPortPrototype()
   port2.short_name = 'DataIn'
   port2.required_interface_ref = ARRef(interface)
   comp2.addRequiredPort(port2)

   # Add components to package
   package.addApplicationSwComponentType(comp1)
   package.addApplicationSwComponentType(comp2)

   # Create composition
   composition = CompositionSwComponentType()
   composition.short_name = 'MyComposition'

   # Add prototypes
   proto1 = SwComponentPrototype()
   proto1.short_name = 'ProviderProto'
   proto1.type_ref = ARRef(comp1)

   proto2 = SwComponentPrototype()
   proto2.short_name = 'ConsumerProto'
   proto2.type_ref = ARRef(comp2)

   composition.sw_component_prototypes.append(proto1)
   composition.sw_component_prototypes.append(proto2)

   # Create connector
   connector = AssemblySwConnector()
   connector.short_name = 'MyConnector'

   # Set provider reference
   provider_ref = PPortInCompositionInstanceRef()
   provider_ref.context_component_ref = ARRef(proto1)
   provider_ref.port_ref = ARRef(port1)

   # Set requester reference
   requester_ref = RPortInCompositionInstanceRef()
   requester_ref.context_component_ref = ARRef(proto2)
   requester_ref.port_ref = ARRef(port2)

   connector.provider_ref = provider_ref
   connector.requester_ref = requester_ref

   # Add connector to composition
   composition.connectors.append(connector)

   # Add composition to package
   package.addCompositionSwComponentType(composition)

   # Write to file
   writer = ARXMLWriter()
   writer.write_to_file(autosar, 'assembly_connector.arxml')

   print("Created assembly connector")

Example 5: List All Interfaces
-------------------------------

.. code-block:: python

   from armodel.parser.arxml_parser import ARXMLParser

   # Parse ARXML
   parser = ARXMLParser()
   model = parser.parse_from_file('example.arxml')

   # List sender-receiver interfaces
   print("Sender-Receiver Interfaces:")
   for interface in model.getSenderReceiverInterfaces():
       print(f"  - {interface.short_name}")
       print(f"    Data elements: {len(interface.data_elements)}")

   # List client-server interfaces
   print("\nClient-Server Interfaces:")
   for interface in model.getClientServerInterfaces():
       print(f"  - {interface.short_name}")
       print(f"    Operations: {len(interface.operations)}")

   # List mode-switch interfaces
   print("\nMode-Switch Interfaces:")
   for interface in model.getModeSwitchInterfaces():
       print(f"  - {interface.short_name}")

Example 6: List All System Signals
-----------------------------------

.. code-block:: python

   from armodel.parser.arxml_parser import ARXMLParser

   # Parse ARXML
   parser = ARXMLParser()
   model = parser.parse_from_file('example.arxml')

   # List system signals
   print("System Signals:")
   for signal in model.getSystemSignals():
       print(f"  - {signal.short_name}")

   # List system signal groups
   print("\nSystem Signal Groups:")
   for group in model.getSystemSignalGroups():
       print(f"  - {group.short_name}")
       print(f"    Signals: {len(group.system_signal_refs)}")

Example 7: List All Connectors
-------------------------------

.. code-block:: python

   from armodel.parser.arxml_parser import ARXMLParser

   # Parse ARXML
   parser = ARXMLParser()
   model = parser.parse_from_file('example.arxml')

   # List assembly connectors
   print("Assembly Connectors:")
   connectors = model.getAssemblySwConnectors()
   for connector in connectors:
       print(f"  - {connector.short_name}")
       print(f"    Provider: {connector.provider_ref.dest}")
       print(f"    Requester: {connector.requester_ref.dest}")

   # List delegation connectors
   print("\nDelegation Connectors:")
   for connector in model.getDelegationSwConnectors():
       print(f"  - {connector.short_name}")

Example 8: Create Communication Specification
---------------------------------------------

.. code-block:: python

   from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
   from armodel.models.M2.AUTOSARTemplates.CommonStructure.SWComponentTemplate.ApplicationSwComponentType import ApplicationSwComponentType
   from armodel.models.M2.AUTOSARTemplates.CommonStructure.SWComponentTemplate.PortPrototype import PPortPrototype, RPortPrototype
   from armodel.models.M2.AUTOSARTemplates.CommonStructure.GenericStructure.PortInterface import SenderReceiverInterface, ServerComSpec
   from armodel.models.M2.AUTOSARTemplates.CommonStructure.GenericStructure.ARObj import ARRef
   from armodel.writer.arxml_writer import ARXMLWriter

   # Initialize AUTOSAR
   autosar = AUTOSAR.getInstance()
   autosar.new()
   autosar.setARRelease('R24-11')

   # Create package
   package = autosar.createARPackage('MyPackage')

   # Create interface
   interface = SenderReceiverInterface()
   interface.short_name = 'MyInterface'
   package.addSenderReceiverInterface(interface)

   # Create component
   component = ApplicationSwComponentType()
   component.short_name = 'MyComponent'
   component.category = 'APPLICATION'

   # Add port with communication specification
   port = PPortPrototype()
   port.short_name = 'MyPort'
   port.provided_interface_ref = ARRef(interface)

   # Create server communication specification
   com_spec = ServerComSpec()
   com_spec.short_name = 'MyComSpec'

   # Add com spec to port
   port.server_com_spec = com_spec

   # Add port to component
   component.addProvidedPort(port)

   # Add to package
   package.addApplicationSwComponentType(component)

   # Write to file
   writer = ARXMLWriter()
   writer.write_to_file(autosar, 'communication_spec.arxml')

   print("Created communication specification")

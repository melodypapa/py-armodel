Working with Components
=======================

This section provides examples for working with AUTOSAR software components.

Example 1: Create Application Component
---------------------------------------

.. code-block:: python

   from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
   from armodel.models.M2.AUTOSARTemplates.CommonStructure.SWComponentTemplate.ApplicationSwComponentType import ApplicationSwComponentType
   from armodel.writer.arxml_writer import ARXMLWriter

   # Initialize AUTOSAR
   autosar = AUTOSAR.getInstance()
   autosar.new()
   autosar.setARRelease('R24-11')

   # Create package
   package = autosar.createARPackage('MyPackage')

   # Create application component
   component = ApplicationSwComponentType()
   component.short_name = 'MyApplicationComponent'
   component.category = 'APPLICATION'

   # Add to package
   package.addApplicationSwComponentType(component)

   # Write to file
   writer = ARXMLWriter()
   writer.write_to_file(autosar, 'application_component.arxml')

   print("Created application component")

Example 2: Create Composition Component
----------------------------------------

.. code-block:: python

   from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
   from armodel.models.M2.AUTOSARTemplates.CommonStructure.SWComponentTemplate.CompositionSwComponentType import CompositionSwComponentType
   from armodel.models.M2.AUTOSARTemplates.CommonStructure.SWComponentTemplate.SwConnector import AssemblySwConnector
   from armodel.models.M2.AUTOSARTemplates.CommonStructure.SWComponentTemplate.PortPrototype import PPortPrototype, RPortPrototype
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

   # Create two atomic components
   comp1 = ApplicationSwComponentType()
   comp1.short_name = 'Component1'
   comp1.category = 'APPLICATION'

   comp2 = ApplicationSwComponentType()
   comp2.short_name = 'Component2'
   comp2.category = 'APPLICATION'

   # Add ports to components
   port1 = PPortPrototype()
   port1.short_name = 'Port1'
   port1.provided_interface_ref = ARRef(interface)
   comp1.addProvidedPort(port1)

   port2 = RPortPrototype()
   port2.short_name = 'Port2'
   port2.required_interface_ref = ARRef(interface)
   comp2.addRequiredPort(port2)

   # Add components to package
   package.addApplicationSwComponentType(comp1)
   package.addApplicationSwComponentType(comp2)

   # Create composition
   composition = CompositionSwComponentType()
   composition.short_name = 'MyComposition'

   # Add components to composition
   from armodel.models.M2.AUTOSARTemplates.CommonStructure.SWComponentTemplate.SwConnector import SwComponentPrototype

   prototype1 = SwComponentPrototype()
   prototype1.short_name = 'Prototype1'
   prototype1.type_ref = ARRef(comp1)

   prototype2 = SwComponentPrototype()
   prototype2.short_name = 'Prototype2'
   prototype2.type_ref = ARRef(comp2)

   composition.sw_component_prototypes.append(prototype1)
   composition.sw_component_prototypes.append(prototype2)

   # Add to package
   package.addCompositionSwComponentType(composition)

   # Write to file
   writer = ARXMLWriter()
   writer.write_to_file(autosar, 'composition_component.arxml')

   print("Created composition component")

Example 3: Create Service Component
------------------------------------

.. code-block:: python

   from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
   from armodel.models.M2.AUTOSARTemplates.CommonStructure.SWComponentTemplate.ServiceSwComponentType import ServiceSwComponentType
   from armodel.writer.arxml_writer import ARXMLWriter

   # Initialize AUTOSAR
   autosar = AUTOSAR.getInstance()
   autosar.new()
   autosar.setARRelease('R24-11')

   # Create package
   package = autosar.createARPackage('MyPackage')

   # Create service component
   service = ServiceSwComponentType()
   service.short_name = 'MyService'
   service.category = 'SERVICE'

   # Add to package
   package.addServiceSwComponentType(service)

   # Write to file
   writer = ARXMLWriter()
   writer.write_to_file(autosar, 'service_component.arxml')

   print("Created service component")

Example 4: Add Behavior to Component
-------------------------------------

.. code-block:: python

   from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
   from armodel.models.M2.AUTOSARTemplates.CommonStructure.SWComponentTemplate.ApplicationSwComponentType import ApplicationSwComponentType
   from armodel.models.M2.AUTOSARTemplates.CommonStructure.SWComponentTemplate.Behavior import SwcInternalBehavior, RunnableEntity, InitEvent
   from armodel.models.M2.AUTOSARTemplates.CommonStructure.GenericStructure.ARObj import ARRef
   from armodel.writer.arxml_writer import ARXMLWriter

   # Initialize AUTOSAR
   autosar = AUTOSAR.getInstance()
   autosar.new()
   autosar.setARRelease('R24-11')

   # Create package
   package = autosar.createARPackage('MyPackage')

   # Create component
   component = ApplicationSwComponentType()
   component.short_name = 'MyComponent'
   component.category = 'APPLICATION'

   # Add to package
   package.addApplicationSwComponentType(component)

   # Create internal behavior
   behavior = SwcInternalBehavior()
   behavior.short_name = 'MyBehavior'
   behavior.component_ref = ARRef(component)

   # Create runnable entity
   runnable = RunnableEntity()
   runnable.short_name = 'MyRunnable'

   # Add runnable to behavior
   behavior.runnables.append(runnable)

   # Create init event
   init_event = InitEvent()
   init_event.short_name = 'MyInitEvent'
   init_event.start_on_event_ref = ARRef(runnable)

   # Add event to behavior
   behavior.events.append(init_event)

   # Add behavior to package
   package.addSwcInternalBehavior(behavior)

   # Write to file
   writer = ARXMLWriter()
   writer.write_to_file(autosar, 'component_with_behavior.arxml')

   print("Created component with behavior")

Example 5: Connect Components
------------------------------

.. code-block:: python

   from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
   from armodel.models.M2.AUTOSARTemplates.CommonStructure.SWComponentTemplate.ApplicationSwComponentType import ApplicationSwComponentType
   from armodel.models.M2.AUTOSARTemplates.CommonStructure.SWComponentTemplate.CompositionSwComponentType import CompositionSwComponentType
   from armodel.models.M2.AUTOSARTemplates.CommonStructure.SWComponentTemplate.SwConnector import AssemblySwConnector, SwComponentPrototype
   from armodel.models.M2.AUTOSARTemplates.CommonStructure.SWComponentTemplate.PortPrototype import PPortPrototype, RPortPrototype
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
   comp1.short_name = 'ProviderComponent'
   comp1.category = 'APPLICATION'

   comp2 = ApplicationSwComponentType()
   comp2.short_name = 'ConsumerComponent'
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
   proto1.short_name = 'Provider'
   proto1.type_ref = ARRef(comp1)

   proto2 = SwComponentPrototype()
   proto2.short_name = 'Consumer'
   proto2.type_ref = ARRef(comp2)

   composition.sw_component_prototypes.append(proto1)
   composition.sw_component_prototypes.append(proto2)

   # Create connector
   connector = AssemblySwConnector()
   connector.short_name = 'DataConnection'

   from armodel.models.M2.AUTOSARTemplates.CommonStructure.SWComponentTemplate.PortPrototype import PPortInCompositionInstanceRef, RPortInCompositionInstanceRef

   provider_ref = PPortInCompositionInstanceRef()
   provider_ref.context_component_ref = ARRef(proto1)
   provider_ref.port_ref = ARRef(port1)

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
   writer.write_to_file(autosar, 'connected_components.arxml')

   print("Created connected components")

Example 6: List All Components
-------------------------------

.. code-block:: python

   from armodel.parser.arxml_parser import ARXMLParser

   # Parse ARXML
   parser = ARXMLParser()
   model = parser.parse_from_file('example.arxml')

   # List all atomic components
   print("Atomic Software Components:")
   for swc in model.getAtomicSwComponentTypes():
       print(f"  - {swc.short_name}")
       print(f"    Category: {swc.category}")
       print(f"    Provided ports: {len(swc.provided_ports)}")
       print(f"    Required ports: {len(swc.required_ports)}")

   # List all composition components
   print("\nComposition Software Components:")
   for comp in model.getCompositionSwComponentTypes():
       print(f"  - {comp.short_name}")
       print(f"    Prototypes: {len(comp.sw_component_prototypes)}")
       print(f"    Connectors: {len(comp.connectors)}")

   # List all service components
   print("\nService Software Components:")
   for service in model.getServiceSwComponentTypes():
       print(f"  - {service.short_name}")

Example 7: Find Component by Name
----------------------------------

.. code-block:: python

   from armodel.parser.arxml_parser import ARXMLParser

   # Parse ARXML
   parser = ARXMLParser()
   model = parser.parse_from_file('example.arxml')

   # Find component by name
   component = model.findAtomicSwComponentType('MyComponent')

   if component:
       print(f"Found component: {component.short_name}")
       print(f"Category: {component.category}")

       # Access ports
       print("\nProvided ports:")
       for port in component.provided_ports:
           print(f"  - {port.short_name}")

       print("\nRequired ports:")
       for port in component.required_ports:
           print(f"  - {port.short_name}")

       # Access behavior
       behavior = model.getBehavior(component)
       if behavior:
           print(f"\nBehavior: {behavior.short_name}")
           print(f"Runnables: {len(behavior.runnables)}")
           print(f"Events: {len(behavior.events)}")
   else:
       print("Component not found")

Example 8: Clone Component
---------------------------

.. code-block:: python

   from armodel.parser.arxml_parser import ARXMLParser
   from armodel.writer.arxml_writer import ARXMLWriter
   import copy

   # Parse ARXML
   parser = ARXMLParser()
   model = parser.parse_from_file('example.arxml')

   # Find component to clone
   original = model.findAtomicSwComponentType('OriginalComponent')

   if original:
       # Clone the component
       clone = copy.deepcopy(original)
       clone.short_name = 'ClonedComponent'

       # Add to package
       package = model.findARPackage('MyPackage')
       if package:
           package.addApplicationSwComponentType(clone)

       # Write to file
       writer = ARXMLWriter()
       writer.write_to_file(model, 'with_clone.arxml')

       print("Component cloned successfully")
   else:
       print("Original component not found")

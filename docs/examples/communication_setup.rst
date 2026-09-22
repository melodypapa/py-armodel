Communication Setup Examples
=============================

This section provides examples for setting up communication in AUTOSAR models.

Example 1: Create Sender-Receiver Interface
-------------------------------------------

.. code-block:: python

   from armodel import AUTOSAR
   from armodel.writer import ARXMLWriter
   from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import TRefType

   # Initialize AUTOSAR
   document = AUTOSAR.getInstance()
   document.clear()
   document.setARRelease('R23-11')

   # Create package
   package = document.createARPackage('MyPackage')

   # Create data type
   data_type = package.createImplementationDataType('MyDataType')
   data_type.setCategory('TYPE_REFERENCE')

   # Create sender-receiver interface
   interface = package.createSenderReceiverInterface('MySenderReceiverInterface')

   # Create data element with a type reference
   data_element = interface.createDataElement('MyDataElement')
   type_ref = TRefType()
   type_ref.setDest('IMPLEMENTATION-DATA-TYPE')
   type_ref.setValue('/MyPackage/MyDataType')
   data_element.setTypeTRef(type_ref)

   # Write to file
   writer = ARXMLWriter()
   writer.save('sender_receiver_interface.arxml', document)

   print("Created sender-receiver interface")

Example 2: Create Client-Server Interface
------------------------------------------

.. code-block:: python

   from armodel import AUTOSAR
   from armodel.writer import ARXMLWriter
   from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean

   # Initialize AUTOSAR
   document = AUTOSAR.getInstance()
   document.clear()
   document.setARRelease('R23-11')

   # Create package
   package = document.createARPackage('MyPackage')

   # Create client-server interface
   interface = package.createClientServerInterface('MyClientServerInterface')

   # Mark the interface as service interface
   is_service = Boolean()
   is_service.value = True
   interface.setIsService(is_service)

   # Create operation
   operation = interface.createOperation('MyOperation')

   # Write to file
   writer = ARXMLWriter()
   writer.save('client_server_interface.arxml', document)

   print("Created client-server interface")

Example 3: Create System Signal
--------------------------------

.. code-block:: python

   from armodel import AUTOSAR
   from armodel.writer import ARXMLWriter

   # Initialize AUTOSAR
   document = AUTOSAR.getInstance()
   document.clear()
   document.setARRelease('R23-11')

   # Create package
   package = document.createARPackage('MyPackage')

   # Create system signal
   package.createSystemSignal('MySystemSignal')

   # Create a system signal group
   group = package.createSystemSignalGroup('MySystemSignalGroup')

   # Write to file
   writer = ARXMLWriter()
   writer.save('system_signal.arxml', document)

   print("Created system signal")

Example 4: Create Assembly Connector
-------------------------------------

.. code-block:: python

   from armodel import AUTOSAR
   from armodel.writer import ARXMLWriter
   from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
   from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.InstanceRefs import (
       PPortInCompositionInstanceRef,
       RPortInCompositionInstanceRef,
   )

   # Initialize AUTOSAR
   document = AUTOSAR.getInstance()
   document.clear()
   document.setARRelease('R23-11')

   # Create package, interface and two components with ports
   package = document.createARPackage('MyPackage')
   interface = package.createSenderReceiverInterface('MyInterface')

   comp1 = package.createApplicationSwComponentType('Provider')
   port1 = comp1.createPPortPrototype('DataOut')
   comp2 = package.createApplicationSwComponentType('Consumer')
   port2 = comp2.createRPortPrototype('DataIn')

   # Create composition with two component prototypes
   composition = package.createCompositionSwComponentType('MyComposition')
   proto1 = composition.createSwComponentPrototype('ProviderProto')
   proto2 = composition.createSwComponentPrototype('ConsumerProto')

   # Create connector and wire provider and requester
   connector = composition.createAssemblySwConnector('MyConnector')

   provider_ref = PPortInCompositionInstanceRef()
   context_ref = RefType()
   context_ref.setDest('SW-COMPONENT-PROTOTYPE')
   context_ref.setValue('/MyPackage/MyComposition/ProviderProto')
   provider_ref.setContextComponentRef(context_ref)
   target_ref = RefType()
   target_ref.setDest('P-PORT-PROTOTYPE')
   target_ref.setValue('/MyPackage/Provider/DataOut')
   provider_ref.setTargetPPortRef(target_ref)
   connector.setProviderIRef(provider_ref)

   requester_ref = RPortInCompositionInstanceRef()
   context_ref = RefType()
   context_ref.setDest('SW-COMPONENT-PROTOTYPE')
   context_ref.setValue('/MyPackage/MyComposition/ConsumerProto')
   requester_ref.setContextComponentRef(context_ref)
   target_ref = RefType()
   target_ref.setDest('R-PORT-PROTOTYPE')
   target_ref.setValue('/MyPackage/Consumer/DataIn')
   requester_ref.setTargetRPortRef(target_ref)
   connector.setRequesterIRef(requester_ref)

   # Write to file
   writer = ARXMLWriter()
   writer.save('assembly_connector.arxml', document)

   print("Created assembly connector")

Example 5: List All Interfaces
-------------------------------

.. code-block:: python

   from armodel import AUTOSAR
   from armodel.parser import ARXMLParser

   document = AUTOSAR.getInstance()
   document.clear()
   document.setARRelease('R23-11')

   # Parse ARXML
   parser = ARXMLParser()
   parser.load('example.arxml', document)

   # List sender-receiver interfaces
   print("Sender-Receiver Interfaces:")
   for package in document.getARPackages():
       for interface in package.getSenderReceiverInterfaces():
           print(f"  - {interface.short_name}")
           print(f"    Data elements: {len(interface.getDataElements())}")

   # List client-server interfaces
   print("\nClient-Server Interfaces:")
   for package in document.getARPackages():
       for interface in package.getClientServerInterfaces():
           print(f"  - {interface.short_name}")

   # List mode-switch interfaces
   print("\nMode-Switch Interfaces:")
   for package in document.getARPackages():
       for interface in package.getModeSwitchInterfaces():
           print(f"  - {interface.short_name}")

Example 6: List All System Signals
-----------------------------------

.. code-block:: python

   from armodel import AUTOSAR
   from armodel.parser import ARXMLParser

   document = AUTOSAR.getInstance()
   document.clear()
   document.setARRelease('R23-11')

   # Parse ARXML
   parser = ARXMLParser()
   parser.load('example.arxml', document)

   # List system signals
   print("System Signals:")
   for package in document.getARPackages():
       for signal in package.getSystemSignals():
           print(f"  - {signal.short_name}")

   # List system signal groups
   print("\nSystem Signal Groups:")
   for package in document.getARPackages():
       for group in package.getSystemSignalGroups():
           print(f"  - {group.short_name}")

Example 7: List All Connectors
-------------------------------

.. code-block:: python

   from armodel import AUTOSAR
   from armodel.parser import ARXMLParser

   document = AUTOSAR.getInstance()
   document.clear()
   document.setARRelease('R23-11')

   # Parse ARXML
   parser = ARXMLParser()
   parser.load('example.arxml', document)

   # List assembly connectors of all compositions
   for package in document.getARPackages():
       for composition in package.getCompositionSwComponentTypes():
           for connector in composition.getAssemblySwConnectors():
               print(f"Assembly Connector: {connector.short_name}")
           for connector in composition.getDelegationSwConnectors():
               print(f"Delegation Connector: {connector.short_name}")

Example 8: Reference an Interface from a Port
----------------------------------------------

.. code-block:: python

   from armodel import AUTOSAR
   from armodel.writer import ARXMLWriter
   from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import TRefType

   # Initialize AUTOSAR
   document = AUTOSAR.getInstance()
   document.clear()
   document.setARRelease('R23-11')

   # Create package and interface
   package = document.createARPackage('MyPackage')
   interface = package.createSenderReceiverInterface('MyInterface')

   # Create component with a provided port
   component = package.createApplicationSwComponentType('MyComponent')

   port = component.createPPortPrototype('MyPort')
   interface_ref = TRefType()
   interface_ref.setDest('SENDER-RECEIVER-INTERFACE')
   interface_ref.setValue('/MyPackage/MyInterface')
   port.setProvidedInterfaceTRef(interface_ref)

   # Write to file
   writer = ARXMLWriter()
   writer.save('communication_spec.arxml', document)

   print("Created communication specification")

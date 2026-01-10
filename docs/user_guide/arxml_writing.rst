ARXML Writing Guide
===================

This guide provides detailed information about writing ARXML files with py-armodel.

Writer Overview
---------------

py-armodel provides a comprehensive ARXML writer that can generate AUTOSAR XML files according to the AUTOSAR standard.

.. code-block:: python

   from armodel.writer.arxml_writer import ARXMLWriter

Basic Writing
-------------

Writing a Model to File
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from armodel.writer.arxml_writer import ARXMLWriter

   # Create writer instance
   writer = ARXMLWriter()

   # Write model to file
   writer.write_to_file(autosar_model, 'output.arxml')

   print("ARXML file written successfully")

Creating a New Model
--------------------

Initialize AUTOSAR Model
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR

   # Get the AUTOSAR singleton instance
   autosar = AUTOSAR.getInstance()

   # Clear any existing data
   autosar.new()

   # Set the AUTOSAR schema version
   autosar.setARRelease('R24-11')

   print(f"Created AUTOSAR model with schema version: {autosar.schema_version}")

Creating AR Packages
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Create top-level package
   main_package = autosar.createARPackage('MyPackage')

   # Create nested package
   sub_package = main_package.createARPackage('SubPackage')

   print(f"Created packages: {main_package.short_name}, {sub_package.short_name}")

Creating Software Components
----------------------------

Application Software Component
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from armodel.models.M2.AUTOSARTemplates.CommonStructure.SWComponentTemplate.ApplicationSwComponentType import ApplicationSwComponentType

   # Create application software component
   component = ApplicationSwComponentType()
   component.short_name = 'MyApplicationComponent'

   # Set category
   component.category = 'APPLICATION'

   # Add to package
   main_package.addApplicationSwComponentType(component)

   print(f"Created component: {component.short_name}")

Composition Software Component
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from armodel.models.M2.AUTOSARTemplates.CommonStructure.SWComponentTemplate.CompositionSwComponentType import CompositionSwComponentType

   # Create composition software component
   composition = CompositionSwComponentType()
   composition.short_name = 'MyComposition'

   # Add to package
   main_package.addCompositionSwComponentType(composition)

   print(f"Created composition: {composition.short_name}")

Service Software Component
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from armodel.models.M2.AUTOSARTemplates.CommonStructure.SWComponentTemplate.ServiceSwComponentType import ServiceSwComponentType

   # Create service software component
   service = ServiceSwComponentType()
   service.short_name = 'MyService'

   # Add to package
   main_package.addServiceSwComponentType(service)

   print(f"Created service: {service.short_name}")

Creating Ports
--------------

Provided Ports
~~~~~~~~~~~~~~

.. code-block:: python

   from armodel.models.M2.AUTOSARTemplates.CommonStructure.SWComponentTemplate.PortPrototype import PPortPrototype

   # Create provided port
   provided_port = PPortPrototype()
   provided_port.short_name = 'MyProvidedPort'

   # Set interface reference (assuming interface exists)
   from armodel.models.M2.AUTOSARTemplates.CommonStructure.GenericStructure.PortInterface import SenderReceiverInterface

   interface = SenderReceiverInterface()
   interface.short_name = 'MyInterface'
   main_package.addSenderReceiverInterface(interface)

   from armodel.models.M2.AUTOSARTemplates.CommonStructure.GenericStructure.ARObj import ARRef
   provided_port.provided_interface_ref = ARRef(interface)

   # Add to component
   component.addProvidedPort(provided_port)

   print(f"Created provided port: {provided_port.short_name}")

Required Ports
~~~~~~~~~~~~~~

.. code-block:: python

   from armodel.models.M2.AUTOSARTemplates.CommonStructure.SWComponentTemplate.PortPrototype import RPortPrototype

   # Create required port
   required_port = RPortPrototype()
   required_port.short_name = 'MyRequiredPort'

   # Set interface reference
   required_port.required_interface_ref = ARRef(interface)

   # Add to component
   component.addRequiredPort(required_port)

   print(f"Created required port: {required_port.short_name}")

Creating Data Types
-------------------

Implementation Data Type
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from armodel.models.M2.AUTOSARTemplates.CommonStructure.GenericStructure.DataTypeImplementation import ImplementationDataType

   # Create implementation data type
   data_type = ImplementationDataType()
   data_type.short_name = 'MyDataType'
   data_type.category = 'TYPE_REFERENCE'

   # Add to package
   main_package.addImplementationDataType(data_type)

   print(f"Created data type: {data_type.short_name}")

Application Data Type
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from armodel.models.M2.AUTOSARTemplates.CommonStructure.GenericStructure.DataTypeApplication import ApplicationDataType

   # Create application data type
   app_data_type = ApplicationDataType()
   app_data_type.short_name = 'MyAppDataType'

   # Add to package
   main_package.addApplicationDataType(app_data_type)

   print(f"Created application data type: {app_data_type.short_name}")

Creating Port Interfaces
-------------------------

Sender-Receiver Interface
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from armodel.models.M2.AUTOSARTemplates.CommonStructure.GenericStructure.PortInterface import SenderReceiverInterface
   from armodel.models.M2.AUTOSARTemplates.CommonStructure.GenericStructure.PortInterface import DataPrototype

   # Create sender-receiver interface
   sr_interface = SenderReceiverInterface()
   sr_interface.short_name = 'MySenderReceiverInterface'

   # Create data element
   data_element = DataPrototype()
   data_element.short_name = 'MyDataElement'

   # Set type reference
   data_element.type_ref = ARRef(data_type)

   # Add data element to interface
   sr_interface.data_elements.append(data_element)

   # Add to package
   main_package.addSenderReceiverInterface(sr_interface)

   print(f"Created sender-receiver interface: {sr_interface.short_name}")

Client-Server Interface
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from armodel.models.M2.AUTOSARTemplates.CommonStructure.GenericStructure.PortInterface import ClientServerInterface
   from armodel.models.M2.AUTOSARTemplates.CommonStructure.GenericStructure.PortInterface import Operation

   # Create client-server interface
   cs_interface = ClientServerInterface()
   cs_interface.short_name = 'MyClientServerInterface'

   # Create operation
   operation = Operation()
   operation.short_name = 'MyOperation'

   # Add operation to interface
   cs_interface.operations.append(operation)

   # Add to package
   main_package.addClientServerInterface(cs_interface)

   print(f"Created client-server interface: {cs_interface.short_name}")

Creating Behavior
-----------------

Internal Behavior
~~~~~~~~~~~~~~~~~

.. code-block:: python

   from armodel.models.M2.AUTOSARTemplates.CommonStructure.SWComponentTemplate.Behavior import SwcInternalBehavior

   # Create internal behavior
   behavior = SwcInternalBehavior()
   behavior.short_name = 'MyBehavior'

   # Set component reference
   behavior.component_ref = ARRef(component)

   # Add to package
   main_package.addSwcInternalBehavior(behavior)

   print(f"Created internal behavior: {behavior.short_name}")

Runnable Entity
~~~~~~~~~~~~~~~

.. code-block:: python

   from armodel.models.M2.AUTOSARTemplates.CommonStructure.SWComponentTemplate.Behavior import RunnableEntity

   # Create runnable entity
   runnable = RunnableEntity()
   runnable.short_name = 'MyRunnable'

   # Add to behavior
   behavior.runnables.append(runnable)

   print(f"Created runnable entity: {runnable.short_name}")

Events
~~~~~~

.. code-block:: python

   from armodel.models.M2.AUTOSARTemplates.CommonStructure.SWComponentTemplate.Behavior import InitEvent

   # Create init event
   init_event = InitEvent()
   init_event.short_name = 'MyInitEvent'

   # Set runnable reference
   init_event.start_on_event_ref = ARRef(runnable)

   # Add to behavior
   behavior.events.append(init_event)

   print(f"Created init event: {init_event.short_name}")

Creating Connectors
-------------------

Assembly Connector
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from armodel.models.M2.AUTOSARTemplates.CommonStructure.SWComponentTemplate.SwConnector import AssemblySwConnector

   # Create assembly connector
   connector = AssemblySwConnector()
   connector.short_name = 'MyConnector'

   # Set provider and requester references
   from armodel.models.M2.AUTOSARTemplates.CommonStructure.SWComponentTemplate.PortPrototype import PPortInCompositionInstanceRef, RPortInCompositionInstanceRef

   provider_ref = PPortInCompositionInstanceRef()
   provider_ref.port_ref = ARRef(provided_port)

   requester_ref = RPortInCompositionInstanceRef()
   requester_ref.port_ref = ARRef(required_port)

   connector.provider_ref = provider_ref
   connector.requester_ref = requester_ref

   # Add to composition
   composition.connectors.append(connector)

   print(f"Created assembly connector: {connector.short_name}")

System Elements
---------------

System Signal
~~~~~~~~~~~~~

.. code-block:: python

   from armodel.models.M2.AUTOSARTemplates.CommonStructure.SystemTemplate.System import SystemSignal

   # Create system signal
   signal = SystemSignal()
   signal.short_name = 'MySystemSignal'

   # Add to package
   main_package.addSystemSignal(signal)

   print(f"Created system signal: {signal.short_name}")

ECU Instance
~~~~~~~~~~~~

.. code-block:: python

   from armodel.models.M2.AUTOSARTemplates.CommonStructure.SystemTemplate.System import ECUInstance

   # Create ECU instance
   ecu = ECUInstance()
   ecu.short_name = 'MyECU'

   # Add to package
   main_package.addECUInstance(ecu)

   print(f"Created ECU instance: {ecu.short_name}")

Advanced Writing
----------------

Setting Attributes
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Set various attributes on elements
   component.category = 'APPLICATION'
   data_type.category = 'TYPE_REFERENCE'
   sr_interface.is_service = False
   cs_interface.is_service = True

Adding Documentation
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Add description to elements
   from armodel.models.M2.MSR.Documentation import Documentation

   doc = Documentation()
   doc.short_name = 'MyDocumentation'
   doc.content = 'This is a description of the element'

   component.documentation = doc

Adding Annotations
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from armodel.models.M2.MSR.Annotation import Annotation

   # Create annotation
   annotation = Annotation()
   annotation.short_name = 'MyAnnotation'
   annotation.content = 'Additional information'

   # Add to element
   if not hasattr(component, 'annotations'):
       component.annotations = []
   component.annotations.append(annotation)

Writer Options
--------------

Formatting Options
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   writer = ARXMLWriter()

   # Write with formatting
   writer.write_to_file(autosar_model, 'output.arxml', pretty_print=True)

Validation
~~~~~~~~~~

The writer validates the model before writing:

.. code-block:: python

   try:
       writer.write_to_file(autosar_model, 'output.arxml')
       print("File written successfully")
   except Exception as e:
       print(f"Validation error: {e}")

Best Practices
--------------

1. **Set schema version**: Always call ``setARRelease()`` before writing
2. **Use proper references**: Ensure all references point to valid elements
3. **Add descriptions**: Include documentation for better readability
4. **Validate before writing**: Check the model structure
5. **Use consistent naming**: Follow AUTOSAR naming conventions

Example: Complete Creation Workflow
------------------------------------

.. code-block:: python

   from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
   from armodel.models.M2.AUTOSARTemplates.CommonStructure.SWComponentTemplate.ApplicationSwComponentType import ApplicationSwComponentType
   from armodel.models.M2.AUTOSARTemplates.CommonStructure.SWComponentTemplate.PortPrototype import PPortPrototype, RPortPrototype
   from armodel.models.M2.AUTOSARTemplates.CommonStructure.GenericStructure.PortInterface import SenderReceiverInterface, DataPrototype
   from armodel.models.M2.AUTOSARTemplates.CommonStructure.GenericStructure.DataTypeImplementation import ImplementationDataType
   from armodel.models.M2.AUTOSARTemplates.CommonStructure.GenericStructure.ARObj import ARRef
   from armodel.writer.arxml_writer import ARXMLWriter

   def create_sample_model():
       """Create a sample AUTOSAR model."""
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

       # Create interface
       interface = SenderReceiverInterface()
       interface.short_name = 'MyInterface'

       data_element = DataPrototype()
       data_element.short_name = 'MyDataElement'
       data_element.type_ref = ARRef(data_type)

       interface.data_elements.append(data_element)
       package.addSenderReceiverInterface(interface)

       # Create component
       component = ApplicationSwComponentType()
       component.short_name = 'MyComponent'
       component.category = 'APPLICATION'

       # Add ports
       provided_port = PPortPrototype()
       provided_port.short_name = 'MyProvidedPort'
       provided_port.provided_interface_ref = ARRef(interface)
       component.addProvidedPort(provided_port)

       required_port = RPortPrototype()
       required_port.short_name = 'MyRequiredPort'
       required_port.required_interface_ref = ARRef(interface)
       component.addRequiredPort(required_port)

       package.addApplicationSwComponentType(component)

       return autosar

   # Create and write model
   model = create_sample_model()
   writer = ARXMLWriter()
   writer.write_to_file(model, 'sample.arxml')

   print("Sample ARXML file created successfully")

Next Steps
----------

* Learn about :doc:`arxml_parsing` to read ARXML files
* Explore the :doc:`../api/writer` API reference
* Check :doc:`../examples` for more writing examples
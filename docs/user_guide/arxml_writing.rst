ARXML Writing Guide
===================

This guide provides detailed information about writing ARXML files with py-armodel.

Writer Overview
---------------

py-armodel provides a comprehensive ARXML writer that generates AUTOSAR XML files according to the AUTOSAR standard.

.. code-block:: python

   from armodel.writer import ARXMLWriter

Basic Writing
-------------

Writing a Model to File
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from armodel import AUTOSAR
   from armodel.writer import ARXMLWriter

   document = AUTOSAR.getInstance()

   # Save the document to a file
   writer = ARXMLWriter()
   writer.save('output.arxml', document)

   print("ARXML file written successfully")

Creating a New Model
--------------------

Initialize AUTOSAR Model
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from armodel import AUTOSAR

   # Get the AUTOSAR singleton instance
   document = AUTOSAR.getInstance()

   # Clear any existing data
   document.clear()

   # Set the AUTOSAR schema version (REQUIRED before writing)
   document.setARRelease('R23-11')

Creating AR Packages
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Create top-level package
   main_package = document.createARPackage('MyPackage')

   # Create nested package
   sub_package = main_package.createARPackage('SubPackage')

   print(f"Created packages: {main_package.short_name}, {sub_package.short_name}")

Creating Software Components
----------------------------

Application Software Component
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Create application software component
   component = main_package.createApplicationSwComponentType('MyApplicationComponent')

   # Set category
   component.setCategory('APPLICATION')

   print(f"Created component: {component.short_name}")

Composition Software Component
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Create composition software component
   composition = main_package.createCompositionSwComponentType('MyComposition')

   print(f"Created composition: {composition.short_name}")

Service Software Component
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Create service software component
   service = main_package.createServiceSwComponentType('MyService')

   service.setCategory('SERVICE')

   print(f"Created service: {service.short_name}")

Creating Ports
--------------

Provided Ports
~~~~~~~~~~~~~~

.. code-block:: python

   from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import TRefType

   # Create a provided port on the component
   provided_port = component.createPPortPrototype('MyProvidedPort')

   # Reference the interface the port provides
   interface_ref = TRefType()
   interface_ref.setDest('SENDER-RECEIVER-INTERFACE')
   interface_ref.setValue('/MyPackage/MyInterface')
   provided_port.setProvidedInterfaceTRef(interface_ref)

Required Ports
~~~~~~~~~~~~~~

.. code-block:: python

   # Create a required port on the component
   required_port = component.createRPortPrototype('MyRequiredPort')
   required_port.setRequiredInterfaceTRef(interface_ref)

Creating Data Types
-------------------

Implementation Data Type
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Create implementation data type
   data_type = main_package.createImplementationDataType('MyDataType')
   data_type.setCategory('TYPE_REFERENCE')

Application Data Type
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Create an application primitive data type
   app_data_type = main_package.createApplicationPrimitiveDataType('MyAppDataType')

Creating Port Interfaces
-------------------------

Sender-Receiver Interface
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import TRefType

   # Create sender-receiver interface
   sr_interface = main_package.createSenderReceiverInterface('MyInterface')

   # Create data element with a type reference
   data_element = sr_interface.createDataElement('MyDataElement')
   type_ref = TRefType()
   type_ref.setDest('IMPLEMENTATION-DATA-TYPE')
   type_ref.setValue('/MyPackage/MyDataType')
   data_element.setTypeTRef(type_ref)

Client-Server Interface
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Create client-server interface
   cs_interface = main_package.createClientServerInterface('MyClientServerInterface')

   # Create operation
   operation = cs_interface.createOperation('MyOperation')

Creating Behavior
-----------------

Internal Behavior
~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Create the internal behavior of a component
   behavior = component.createSwcInternalBehavior('MyBehavior')

Runnable Entity
~~~~~~~~~~~~~~~

.. code-block:: python

   # Create runnable entity
   runnable = behavior.createRunnableEntity('MyRunnable')

Events
~~~~~~

.. code-block:: python

   from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import TRefType

   # Create init event
   init_event = behavior.createInitEvent('MyInitEvent')

   # Reference the runnable to start on
   start_ref = TRefType()
   start_ref.setDest('RUNNABLE-ENTITY')
   start_ref.setValue('/MyPackage/MyBehavior/MyRunnable')
   init_event.setStartOnEventRef(start_ref)

Creating Connectors
-------------------

Composition components provide factory methods for their connectors and
component prototypes:

.. code-block:: python

   # Create a component prototype inside the composition
   prototype = composition.createSwComponentPrototype('Provider')

   # Create an assembly connector
   connector = composition.createAssemblySwConnector('MyConnector')

System Elements
---------------

System Signal
~~~~~~~~~~~~~

.. code-block:: python

   # Create system signal
   signal = main_package.createSystemSignal('MySystemSignal')

   print(f"Created system signal: {signal.short_name}")

ECU Instance
~~~~~~~~~~~~

.. code-block:: python

   # Create ECU instance
   ecu = main_package.createEcuInstance('MyECU')

   print(f"Created ECU instance: {ecu.short_name}")

Adding Documentation
~~~~~~~~~~~~~~~~~~~~

Elements derived from ``Identifiable`` accept an introduction block:

.. code-block:: python

   from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock

   # Add an introduction documentation block to an element
   doc = DocumentationBlock()
   doc.addP('This is a description of the element')
   component.setIntroduction(doc)

Best Practices
--------------

1. **Set schema version**: Always call ``setARRelease()`` before writing
2. **Use factory methods**: Create elements with ``createXXX()`` methods so parent
   links are maintained automatically
3. **Use proper references**: Set ``TRefType``/``RefType`` destination and value
4. **Use consistent naming**: Follow AUTOSAR naming conventions

Example: Complete Creation Workflow
------------------------------------

.. code-block:: python

   from armodel import AUTOSAR
   from armodel.writer import ARXMLWriter
   from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import TRefType

   def create_sample_model():
       """Create a sample AUTOSAR model."""
       # Initialize AUTOSAR
       document = AUTOSAR.getInstance()
       document.clear()
       document.setARRelease('R23-11')

       # Create package
       package = document.createARPackage('MyPackage')

       # Create data type
       data_type = package.createImplementationDataType('MyDataType')
       data_type.setCategory('TYPE_REFERENCE')

       # Create interface with a data element
       interface = package.createSenderReceiverInterface('MyInterface')
       data_element = interface.createDataElement('MyDataElement')
       type_ref = TRefType()
       type_ref.setDest('IMPLEMENTATION-DATA-TYPE')
       type_ref.setValue('/MyPackage/MyDataType')
       data_element.setTypeTRef(type_ref)

       # Create component
       component = package.createApplicationSwComponentType('MyComponent')
       component.setCategory('APPLICATION')

       # Add a provided port
       provided_port = component.createPPortPrototype('MyProvidedPort')
       interface_ref = TRefType()
       interface_ref.setDest('SENDER-RECEIVER-INTERFACE')
       interface_ref.setValue('/MyPackage/MyInterface')
       provided_port.setProvidedInterfaceTRef(interface_ref)

       return document

   # Create and write model
   document = create_sample_model()
   writer = ARXMLWriter()
   writer.save('sample.arxml', document)

   print("Sample ARXML file created successfully")

Next Steps
----------

* Learn about :doc:`arxml_parsing` to read ARXML files
* Explore the :doc:`../api/writer` API reference
* Check :doc:`../examples/basic_usage` for more writing examples

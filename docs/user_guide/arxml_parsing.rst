ARXML Parsing Guide
===================

This guide provides detailed information about parsing ARXML files with py-armodel.

Parser Overview
---------------

py-armodel provides a comprehensive ARXML parser that can read AUTOSAR XML files according to the AUTOSAR standard.

.. code-block:: python

   from armodel.parser import ARXMLParser

Basic Parsing
-------------

Parsing a Single File
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from armodel import AUTOSAR
   from armodel.parser import ARXMLParser

   # Get the AUTOSAR document singleton
   document = AUTOSAR.getInstance()
   document.clear()
   document.setARRelease('R23-11')  # REQUIRED before parsing

   # Create parser instance
   parser = ARXMLParser()

   # Parse a single ARXML file into the document
   parser.load('example.arxml', document)

   # Access the model
   print(f"Loaded model with {len(document.getARPackages())} packages")

Parsing Multiple Files
~~~~~~~~~~~~~~~~~~~~~~

Multiple files can be loaded into the same document, for example when a
model is split over several ARXML files:

.. code-block:: python

   files = ['file1.arxml', 'file2.arxml', 'file3.arxml']

   for file_path in files:
       parser.load(file_path, document)
       print(f"Parsed {file_path}")

Parser Options
--------------

Warning Mode
~~~~~~~~~~~~

The parser can be configured to suppress exceptions and issue warnings instead:

.. code-block:: python

   parser = ARXMLParser(options={"warning": True})

   parser.load('example.arxml', document)

Logging
~~~~~~~

Enable logging to see detailed parsing information:

.. code-block:: python

   import logging

   # Configure logging
   logging.basicConfig(
       level=logging.INFO,
       format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
   )

   # Parse with logging enabled
   parser = ARXMLParser()
   parser.load('example.arxml', document)

Accessing Parsed Elements
--------------------------

The parsed model is an ``AUTOSAR`` object that provides various methods to access elements.
Top-level elements live in AR packages; use the package getters to iterate over them.

AR Packages
~~~~~~~~~~~

.. code-block:: python

   # Get all AR packages
   packages = document.getARPackages()

   for package in packages:
       print(f"Package: {package.short_name}")

   # Find an element by its full path (including the package path)
   package = document.getElement('MyPackage')          # top-level package
   sub_package = document.getElement('MyPackage/SubPackage')  # nested package

Software Components
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   for package in document.getARPackages():
       # Get all atomic software component types
       atomic_swcs = package.getAtomicSwComponentTypes()

       # Get all composition software component types
       composition_swcs = package.getCompositionSwComponentTypes()

       # Get all software component types (atomic and composition)
       all_swcs = package.getSwComponentTypes()

   # Find a specific component by its full path
   component = document.findAtomicSwComponentType('/MyPackage/MyComponent')

   if component:
       print(f"Component: {component.short_name}")
       print(f"Category: {component.getCategory()}")

Data Types
~~~~~~~~~~

.. code-block:: python

   for package in document.getARPackages():
       # Get all implementation data types
       impl_data_types = package.getImplementationDataTypes()

   # Find a specific data type by its full path
   data_type = document.findImplementationDataType('/MyPackage/MyDataType')

   if data_type:
       print(f"Data Type: {data_type.short_name}")
       print(f"Category: {data_type.getCategory()}")

Port Interfaces
~~~~~~~~~~~~~~~

.. code-block:: python

   for package in document.getARPackages():
       # Get all sender-receiver interfaces
       sr_interfaces = package.getSenderReceiverInterfaces()

       # Get all client-server interfaces
       cs_interfaces = package.getClientServerInterfaces()

       # Get all mode-switch interfaces
       mode_interfaces = package.getModeSwitchInterfaces()

   for interface in sr_interfaces:
       print(f"Interface: {interface.short_name}")
       print(f"Data elements: {[de.short_name for de in interface.getDataElements()]}")

System Elements
~~~~~~~~~~~~~~~

.. code-block:: python

   for package in document.getARPackages():
       # Get all system signals
       for signal in package.getSystemSignals():
           print(f"Signal: {signal.short_name}")

       # Get all system signal groups
       signal_groups = package.getSystemSignalGroups()

   # Find a specific signal by its full path
   signal = document.findSystemSignal('/MyPackage/MySignal')

   if signal:
       print(f"Signal: {signal.short_name}")

ECU Instances
~~~~~~~~~~~~~

.. code-block:: python

   for package in document.getARPackages():
       # Get all ECU instances
       for ecu in package.getEcuInstances():
           print(f"ECU: {ecu.short_name}")

Ports and Connectors
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   component = document.findAtomicSwComponentType('/MyPackage/MyComponent')

   if component:
       # Get provided ports
       for port in component.getPPortPrototypes():
           print(f"Provided port: {port.short_name}")
           print(f"Interface: {port.getProvidedInterfaceTRef().getValue()}")

       # Get required ports
       for port in component.getRPortPrototypes():
           print(f"Required port: {port.short_name}")
           print(f"Interface: {port.getRequiredInterfaceTRef().getValue()}")

   # Get assembly connectors of a composition
   composition = document.find('/MyPackage/MyComposition')
   for connector in composition.getAssemblySwConnectors():
       print(f"Connector: {connector.short_name}")

Behaviors and Implementations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   component = document.findAtomicSwComponentType('/MyPackage/MyComponent')

   if component:
       behavior = component.getInternalBehavior()

       if behavior:
           print(f"Behavior: {behavior.short_name}")

           # Get runnable entities
           for runnable in behavior.getRunnableEntities():
               print(f"  Runnable: {runnable.short_name}")

Advanced Parsing
----------------

Validation
~~~~~~~~~~

The parser validates the ARXML structure according to AUTOSAR standards:

.. code-block:: python

   parser = ARXMLParser()

   try:
       parser.load('example.arxml', document)
       print("File parsed successfully")
   except Exception as e:
       print(f"Parsing error: {e}")

Error Handling
~~~~~~~~~~~~~~

.. code-block:: python

   parser = ARXMLParser()

   try:
       parser.load('example.arxml', document)
   except FileNotFoundError:
       print("ARXML file not found")
   except Exception as e:
       print(f"Parsing error: {e}")
       print(f"Error type: {type(e).__name__}")

Working with References
------------------------

Understanding AR References
~~~~~~~~~~~~~~~~~~~~~~~~~~~

AUTOSAR uses references to link elements together. References are
modeled with ``RefType`` objects that carry a destination type
(``dest``) and a path (``value``):

.. code-block:: python

   for package in document.getARPackages():
       for interface in package.getSenderReceiverInterfaces():
           for data_element in interface.getDataElements():
               type_ref = data_element.getTypeTRef()
               if type_ref is not None:
                   print(f"Data element: {data_element.short_name}")
                   print(f"  Dest:  {type_ref.getDest()}")
                   print(f"  Value: {type_ref.getValue()}")

                   # Resolve the reference to the referenced element
                   data_type = document.find(type_ref)
                   if data_type:
                       print(f"  -> Type: {data_type.short_name}")

Parsing ECUC Values
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   for package in document.getARPackages():
       # Get ECUC value collections
       for collection in package.getEcucValueCollections():
           print(f"ECUC Collection: {collection.short_name}")

       # Get module configurations
       for module_config in package.getEcucModuleConfigurationValues():
           print(f"  Module: {module_config.short_name}")

           # Containers of a module configuration
           for container in module_config.getContainers():
               print(f"    Container: {container.short_name}")

Parsing BSW Modules
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   for package in document.getARPackages():
       # Get BSW module descriptions
       for module in package.getBswModuleDescriptions():
           print(f"BSW Module: {module.short_name}")

Best Practices
--------------

1. **Set the AUTOSAR release**: Always call ``setARRelease()`` before parsing
2. **Use warning mode**: Pass ``options={"warning": True}`` to tolerate recoverable issues
3. **Check for None**: ``find()`` and ``getElement()`` return ``None`` if not found
4. **Use full paths**: The ``find`` methods expect the full element path (e.g. ``/Pkg/Name``)
5. **Iterate packages**: Most elements are accessed through their AR package

Example: Complete Parsing Workflow
----------------------------------

.. code-block:: python

   from armodel import AUTOSAR
   from armodel.parser import ARXMLParser

   def parse_and_analyze(arxml_file):
       """Parse and analyze an ARXML file."""
       document = AUTOSAR.getInstance()
       document.clear()
       document.setARRelease('R23-11')

       parser = ARXMLParser(options={"warning": True})

       try:
           # Parse the file
           parser.load(arxml_file, document)

           # Print summary
           print("\n=== ARXML Analysis ===")
           print(f"Packages: {len(document.getARPackages())}")

           atomic_swcs = []
           signals = []
           ecus = []
           for package in document.getARPackages():
               atomic_swcs.extend(package.getAtomicSwComponentTypes())
               signals.extend(package.getSystemSignals())
               ecus.extend(package.getEcuInstances())

           print(f"Atomic SWCs: {len(atomic_swcs)}")
           print(f"System Signals: {len(signals)}")
           print(f"ECU Instances: {len(ecus)}")

           # Analyze components
           print("\n=== Software Components ===")
           for swc in atomic_swcs:
               print(f"{swc.short_name}: {len(swc.getPPortPrototypes())} provided ports, "
                     f"{len(swc.getRPortPrototypes())} required ports")

           return document

       except Exception as e:
           print(f"Error parsing file: {e}")
           return None

   # Usage
   document = parse_and_analyze('example.arxml')

Next Steps
----------

* Learn about :doc:`arxml_writing` to generate ARXML files
* Explore the :doc:`../api/parser` API reference
* Check :doc:`../examples/basic_usage` for more parsing examples

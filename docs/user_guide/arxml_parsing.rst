ARXML Parsing Guide
===================

This guide provides detailed information about parsing ARXML files with py-armodel.

Parser Overview
---------------

py-armodel provides a comprehensive ARXML parser that can read and validate AUTOSAR XML files according to the AUTOSAR standard.

.. code-block:: python

   from armodel.parser.arxml_parser import ARXMLParser

Basic Parsing
-------------

Parsing a Single File
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from armodel.parser.arxml_parser import ARXMLParser

   # Create parser instance
   parser = ARXMLParser()

   # Parse a single ARXML file
   autosar_model = parser.parse_from_file('example.arxml')

   # Access the model
   print(f"Loaded model with {len(autosar_model.getARPackages())} packages")

Parsing Multiple Files
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Parse multiple files
   files = ['file1.arxml', 'file2.arxml', 'file3.arxml']

   for file_path in files:
       model = parser.parse_from_file(file_path)
       print(f"Parsed {file_path}")

Parser Options
--------------

Warning Mode
~~~~~~~~~~~~

The parser can be configured to suppress exceptions and issue warnings instead:

.. code-block:: python

   parser = ARXMLParser(options={"warning": True})

   with warnings.catch_warnings(record=True) as w:
       warnings.simplefilter("always")
       model = parser.parse_from_file('example.arxml')
       for warning in w:
           print(f"Warning: {warning.message}")

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
   model = parser.parse_from_file('example.arxml')

Accessing Parsed Elements
--------------------------

The parsed model is an ``AUTOSAR`` object that provides various methods to access elements.

AR Packages
~~~~~~~~~~~

.. code-block:: python

   # Get all AR packages
   packages = autosar_model.getARPackages()

   for package in packages:
       print(f"Package: {package.short_name}")

   # Find a specific package
   package = autosar_model.findARPackage('MyPackage')

Software Components
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Get all atomic software component types
   atomic_swcs = autosar_model.getAtomicSwComponentTypes()

   # Get all composition software component types
   composition_swcs = autosar_model.getCompositionSwComponentTypes()

   # Get all service software component types
   service_swcs = autosar_model.getServiceSwComponentTypes()

   # Find a specific component
   component = autosar_model.findAtomicSwComponentType('MyComponent')

   if component:
       print(f"Component: {component.short_name}")
       print(f"Category: {component.category}")

Data Types
~~~~~~~~~~

.. code-block:: python

   # Get all application data types
   app_data_types = autosar_model.getApplicationDataTypes()

   # Get all implementation data types
   impl_data_types = autosar_model.getImplementationDataTypes()

   # Find a specific data type
   data_type = autosar_model.findImplementationDataType('MyDataType')

   if data_type:
       print(f"Data Type: {data_type.short_name}")
       print(f"Category: {data_type.category}")

Port Interfaces
~~~~~~~~~~~~~~~

.. code-block:: python

   # Get all sender-receiver interfaces
   sr_interfaces = autosar_model.getSenderReceiverInterfaces()

   # Get all client-server interfaces
   cs_interfaces = autosar_model.getClientServerInterfaces()

   # Get all mode-switch interfaces
   mode_interfaces = autosar_model.getModeSwitchInterfaces()

   # Find a specific interface
   interface = autosar_model.findSenderReceiverInterface('MyInterface')

   if interface:
       print(f"Interface: {interface.short_name}")
       print(f"Data elements: {[de.short_name for de in interface.data_elements]}")

System Elements
~~~~~~~~~~~~~~~

.. code-block:: python

   # Get all system signals
   signals = autosar_model.getSystemSignals()

   for signal in signals:
       print(f"Signal: {signal.short_name}")

   # Get all system signal groups
   signal_groups = autosar_model.getSystemSignalGroups()

   # Find a specific signal
   signal = autosar_model.findSystemSignal('MySignal')

   if signal:
       print(f"Signal: {signal.short_name}")
       print(f"Type: {signal.type_ref.dest}")

ECU and Mappings
~~~~~~~~~~~~~~~~

.. code-block:: python

   # Get all ECU instances
   ecus = autosar_model.getECUInstances()

   for ecu in ecus:
       print(f"ECU: {ecu.short_name}")

   # Get software-to-ECU mappings
   mappings = autosar_model.getSwToEcuMappings()

   for mapping in mappings:
       print(f"Mapping: {mapping.short_name}")

Ports and Connectors
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Access component ports
   component = autosar_model.findAtomicSwComponentType('MyComponent')

   if component:
       # Get provided ports
       for port in component.provided_ports:
           print(f"Provided port: {port.short_name}")
           print(f"Interface: {port.provided_interface_ref.dest}")

       # Get required ports
       for port in component.required_ports:
           print(f"Required port: {port.short_name}")
           print(f"Interface: {port.required_interface_ref.dest}")

   # Get assembly connectors
   connectors = autosar_model.getAssemblySwConnectors()

   for connector in connectors:
       print(f"Connector: {connector.short_name}")
       print(f"Provider: {connector.provider_ref.dest}")
       print(f"Requester: {connector.requester_ref.dest}")

Behaviors and Implementations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Get behavior for a component
   component = autosar_model.findAtomicSwComponentType('MyComponent')

   if component:
       behavior = autosar_model.getBehavior(component)

       if behavior:
           print(f"Behavior: {behavior.short_name}")

           # Get runnable entities
           for runnable in behavior.runnables:
               print(f"  Runnable: {runnable.short_name}")

           # Get events
           for event in behavior.events:
               print(f"  Event: {event.short_name} ({event.__class__.__name__})")

   # Get implementation for a component
   implementation = autosar_model.getImplementation(component)

   if implementation:
       print(f"Implementation: {implementation.short_name}")

Advanced Parsing
----------------

Handling Large Files
~~~~~~~~~~~~~~~~~~~~

For large ARXML files, consider using memory-efficient parsing:

.. code-block:: python

   # Process large files with careful memory management
   parser = ARXMLParser()

   try:
       model = parser.parse_from_file('large_file.arxml')
       # Process the model
   except MemoryError:
       print("File too large - consider splitting or processing in chunks")

Validation
~~~~~~~~~~

The parser validates the ARXML structure according to AUTOSAR standards:

.. code-block:: python

   parser = ARXMLParser()

   try:
       model = parser.parse_from_file('example.arxml')
       print("File parsed and validated successfully")
   except Exception as e:
       print(f"Validation error: {e}")

Error Handling
~~~~~~~~~~~~~~

.. code-block:: python

   from armodel.parser.arxml_parser import ARXMLParser
   import logging

   logging.basicConfig(level=logging.ERROR)

   parser = ARXMLParser()

   try:
       model = parser.parse_from_file('example.arxml')
   except FileNotFoundError:
       print("ARXML file not found")
   except Exception as e:
       print(f"Parsing error: {e}")
       print(f"Error type: {type(e).__name__}")

Working with References
------------------------

Understanding AR References
~~~~~~~~~~~~~~~~~~~~~~~~~~~

AUTOSAR uses references to link elements together:

.. code-block:: python

   # Access a reference
   interface = autosar_model.findSenderReceiverInterface('MyInterface')

   if interface and interface.data_elements:
       data_element = interface.data_elements[0]

       # Access the data type reference
       if hasattr(data_element, 'type_ref'):
           print(f"Data element: {data_element.short_name}")
           print(f"Type reference: {data_element.type_ref.dest}")

           # Resolve the reference
           data_type = data_element.type_ref.resolve(autosar_model)
           if data_type:
               print(f"Resolved type: {data_type.short_name}")

Navigating References
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   component = autosar_model.findAtomicSwComponentType('MyComponent')

   if component:
       for port in component.provided_ports:
           # Navigate to interface
           interface_ref = port.provided_interface_ref
           interface = interface_ref.resolve(autosar_model)

           if interface:
               print(f"Port: {port.short_name} -> Interface: {interface.short_name}")

Special Parsing Scenarios
--------------------------

Parsing with Different AUTOSAR Versions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   parser = ARXMLParser()
   model = parser.parse_from_file('example.arxml')

   # Check the AUTOSAR version
   print(f"Schema version: {model.schema_version}")

Parsing ECUC Values
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Get ECUC value collections
   ecuc_collections = autosar_model.getEcucValueCollections()

   for collection in ecuc_collections:
       print(f"ECUC Collection: {collection.short_name}")

       # Get module configurations
       for module_config in collection.module_configs:
           print(f"  Module: {module_config.short_name}")

Parsing BSW Modules
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Get BSW module descriptions
   bsw_modules = autosar_model.getBswModuleDescriptions()

   for module in bsw_modules:
       print(f"BSW Module: {module.short_name}")

       # Get behaviors
       if hasattr(module, 'behaviors'):
           for behavior in module.behaviors:
               print(f"  Behavior: {behavior.short_name}")

Best Practices
--------------

1. **Always validate**: Check if elements exist before accessing them
2. **Use try-except**: Handle parsing errors gracefully
3. **Enable logging**: Use logging for debugging parsing issues
4. **Check references**: Validate that references can be resolved
5. **Memory management**: Be careful with large files

Example: Complete Parsing Workflow
----------------------------------

.. code-block:: python

   from armodel.parser.arxml_parser import ARXMLParser
   import logging

   # Configure logging
   logging.basicConfig(level=logging.INFO)

   def parse_and_analyze(arxml_file):
       """Parse and analyze an ARXML file."""
       parser = ARXMLParser()

       try:
           # Parse the file
           model = parser.parse_from_file(arxml_file)

           # Print summary
           print(f"\n=== ARXML Analysis ===")
           print(f"Packages: {len(model.getARPackages())}")
           print(f"Atomic SWCs: {len(model.getAtomicSwComponentTypes())}")
           print(f"Composition SWCs: {len(model.getCompositionSwComponentTypes())}")
           print(f"System Signals: {len(model.getSystemSignals())}")
           print(f"ECU Instances: {len(model.getECUInstances())}")

           # Analyze components
           print(f"\n=== Software Components ===")
           for swc in model.getAtomicSwComponentTypes():
               print(f"{swc.short_name}: {len(swc.provided_ports)} provided ports, "
                     f"{len(swc.required_ports)} required ports")

           return model

       except Exception as e:
           print(f"Error parsing file: {e}")
           return None

   # Usage
   model = parse_and_analyze('example.arxml')

Next Steps
----------

* Learn about :doc:`arxml_writing` to generate ARXML files
* Explore the :doc:`../api/parser` API reference
* Check :doc:`../examples` for more parsing examples
Quick Start Guide
=================

This guide will help you get started with py-armodel quickly by walking through common tasks.

Parsing an ARXML File
---------------------

The most common operation is parsing an existing ARXML file:

.. code-block:: python

   from armodel.parser.arxml_parser import ARXMLParser

   # Create a parser instance
   parser = ARXMLParser()

   # Parse an ARXML file
   autosar_model = parser.parse_from_file('example.arxml')

   # The autosar_model is now an AUTOSAR object containing all elements
   print(f"Loaded ARXML with {len(autosar_model.getARPackages())} packages")

Accessing AUTOSAR Elements
---------------------------

Once you have parsed an ARXML file, you can access various AUTOSAR elements:

Getting Software Components
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Get all atomic software component types
   atomic_swcs = autosar_model.getAtomicSwComponentTypes()
   for swc in atomic_swcs:
       print(f"Component: {swc.short_name}")

   # Get all composition software component types
   composition_swcs = autosar_model.getCompositionSwComponentTypes()
   for comp in composition_swcs:
       print(f"Composition: {comp.short_name}")

Finding Specific Elements
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Find a specific component by short name
   component = autosar_model.findAtomicSwComponentType('MyComponent')

   if component:
       print(f"Found component: {component.short_name}")

       # Access ports
       for port in component.provided_ports:
           print(f"  Provided port: {port.short_name}")

       for port in component.required_ports:
           print(f"  Required port: {port.short_name}")

   # Find a data type
   data_type = autosar_model.findImplementationDataType('MyDataType')

   # Find a system signal
   signal = autosar_model.findSystemSignal('MySignal')

Getting System Signals
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Get all system signals
   signals = autosar_model.getSystemSignals()
   for signal in signals:
       print(f"Signal: {signal.short_name}")

   # Get all system signal groups
   signal_groups = autosar_model.getSystemSignalGroups()
   for group in signal_groups:
       print(f"Signal Group: {group.short_name}")

Creating a New AUTOSAR Model
-----------------------------

You can create a new AUTOSAR model from scratch:

.. code-block:: python

   from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR

   # Get the AUTOSAR singleton instance
   autosar = AUTOSAR.getInstance()

   # Clear any existing data
   autosar.new()

   # Set the AUTOSAR schema version
   autosar.setARRelease('R24-11')

   # Create an AR package
   package = autosar.createARPackage('MyPackage')

   print(f"Created AUTOSAR model with package: {package.short_name}")

Creating Software Components
----------------------------

.. code-block:: python

   from armodel.models.M2.AUTOSARTemplates.CommonStructure.SWComponentTemplate.ApplicationSwComponentType import ApplicationSwComponentType

   # Create a new application software component
   component = ApplicationSwComponentType()
   component.short_name = 'MyComponent'

   # Add the component to a package
   package.addApplicationSwComponentType(component)

   print(f"Created component: {component.short_name}")

Writing an ARXML File
---------------------

After creating or modifying a model, you can write it to an ARXML file:

.. code-block:: python

   from armodel.writer.arxml_writer import ARXMLWriter

   # Create a writer instance
   writer = ARXMLWriter()

   # Write the model to a file
   writer.write_to_file(autosar, 'output.arxml')

   print("ARXML file written successfully")

Working with Ports
------------------

Adding Ports to a Component
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from armodel.models.M2.AUTOSARTemplates.CommonStructure.SWComponentTemplate.PortPrototype import PPortPrototype, RPortPrototype

   # Add a provided port
   provided_port = PPortPrototype()
   provided_port.short_name = 'MyProvidedPort'
   component.addProvidedPort(provided_port)

   # Add a required port
   required_port = RPortPrototype()
   required_port.short_name = 'MyRequiredPort'
   component.addRequiredPort(required_port)

Working with Data Types
------------------------

Creating a Data Type
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from armodel.models.M2.AUTOSARTemplates.CommonStructure.GenericStructure.DataTypeImplementation import ImplementationDataType

   # Create an implementation data type
   data_type = ImplementationDataType()
   data_type.short_name = 'MyDataType'

   # Add to package
   package.addImplementationDataType(data_type)

Working with Connectors
------------------------

Exporting Connectors to Excel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can use the CLI tool to export connectors:

.. code-block:: bash

   connector2xlsx input.arxml connectors.xlsx

Updating Connectors from Excel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Update connectors based on Excel modifications:

.. code-block:: bash

   connector-update input.arxml connectors.xlsx output.arxml

Using CLI Tools
---------------

Dump ARXML Content
~~~~~~~~~~~~~~~~~~

View all content of an ARXML file:

.. code-block:: bash

   arxml-dump --arxml example.arxml

List Software Components
~~~~~~~~~~~~~~~~~~~~~~~~~

List all software components in a directory:

.. code-block:: bash

   armodel-component /path/to/arxml/files

List with long names and filter:

.. code-block:: bash

   armodel-component --format long --filter CompositionSwComponent /path/to/arxml/files

List System Signals
~~~~~~~~~~~~~~~~~~~

List all system signals:

.. code-block:: bash

   armodel-system-signal /path/to/arxml/files

Check for Duplicate UUIDs
~~~~~~~~~~~~~~~~~~~~~~~~~~

Validate UUID uniqueness:

.. code-block:: bash

   armodel-uuid-checker /path/to/arxml/files

Format ARXML Files
~~~~~~~~~~~~~~~~~~

Format an ARXML file:

.. code-block:: bash

   arxml-format input.arxml output.arxml

Common Patterns
---------------

Iterating Through All Elements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Get all AR packages
   for package in autosar_model.getARPackages():
       print(f"Package: {package.short_name}")

       # Get all elements in the package
       for element in package.elements:
           print(f"  Element: {element.short_name} ({element.__class__.__name__})")

Error Handling
~~~~~~~~~~~~~~

.. code-block:: python

   from armodel.parser.arxml_parser import ARXMLParser
   import logging

   # Enable logging
   logging.basicConfig(level=logging.INFO)

   try:
       parser = ARXMLParser()
       autosar_model = parser.parse_from_file('example.arxml')
   except Exception as e:
       print(f"Error parsing ARXML: {e}")

Working with UUIDs
------------------

py-armodel includes UUID management:

.. code-block:: python

   from armodel.models.utils.uuid_mgr import UUIDManager

   # Get the UUID manager
   uuid_mgr = UUIDManager()

   # Check for duplicate UUIDs
   duplicates = uuid_mgr.check_duplicates()

   if duplicates:
       print(f"Found {len(duplicates)} duplicate UUIDs")
       for uuid, elements in duplicates.items():
           print(f"  UUID {uuid} used by: {[e.short_name for e in elements]}")

Next Steps
----------

* Read the :doc:`arxml_parsing` guide for detailed parsing information
* Read the :doc:`arxml_writing` guide for detailed writing information
* Check the :doc:`../api/parser` and :doc:`../api/writer` API references
* Explore the :doc:`../examples` directory for more examples
Quick Start Guide
=================

This guide will help you get started with py-armodel quickly by walking through common tasks.

The AUTOSAR Singleton
---------------------

py-armodel keeps the whole AUTOSAR model in a singleton ``AUTOSAR`` object.
Every parse or write operation works on this document:

.. code-block:: python

   from armodel import AUTOSAR

   document = AUTOSAR.getInstance()
   document.clear()                # start with an empty model (or call document.new())
   document.setARRelease('R23-11') # REQUIRED before parsing or writing

Parsing an ARXML File
---------------------

The most common operation is parsing an existing ARXML file:

.. code-block:: python

   from armodel import AUTOSAR
   from armodel.parser import ARXMLParser

   document = AUTOSAR.getInstance()
   document.clear()
   document.setARRelease('R23-11')

   parser = ARXMLParser()

   # Load an ARXML file into the document
   parser.load('example.arxml', document)

   # The document now contains all elements
   print(f"Loaded ARXML with {len(document.getARPackages())} packages")

Accessing AUTOSAR Elements
---------------------------

Once you have parsed an ARXML file, you can access various AUTOSAR elements.
Most elements live inside AR packages.

Getting Software Components
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Get all atomic software component types of a package
   for package in document.getARPackages():
       for swc in package.getAtomicSwComponentTypes():
           print(f"Component: {swc.short_name}")

   # Get all composition software component types of a package
   for package in document.getARPackages():
       for comp in package.getCompositionSwComponentTypes():
           print(f"Composition: {comp.short_name}")

Finding Specific Elements
~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``find`` methods take the **full path** of the element
(package path separated by ``/``):

.. code-block:: python

   # Find a specific component by its full path
   component = document.findAtomicSwComponentType('/MyPackage/MyComponent')

   if component:
       print(f"Found component: {component.short_name}")

       # Access ports
       for port in component.getPorts():
           print(f"  Port: {port.short_name}")

   # Find a data type
   data_type = document.findImplementationDataType('/MyPackage/MyDataType')

   # Find a system signal
   signal = document.findSystemSignal('/MyPackage/MySignal')

Getting System Signals
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   for package in document.getARPackages():
       # Get all system signals of the package
       for signal in package.getSystemSignals():
           print(f"Signal: {signal.short_name}")

       # Get all system signal groups
       for group in package.getSystemSignalGroups():
           print(f"Signal Group: {group.short_name}")

Creating a New AUTOSAR Model
-----------------------------

You can create a new AUTOSAR model from scratch:

.. code-block:: python

   from armodel import AUTOSAR

   # Get the AUTOSAR singleton instance
   document = AUTOSAR.getInstance()

   # Clear any existing data
   document.clear()

   # Set the AUTOSAR schema version
   document.setARRelease('R23-11')

   # Create an AR package
   package = document.createARPackage('MyPackage')

   print(f"Created AUTOSAR model with package: {package.short_name}")

Creating Software Components
----------------------------

.. code-block:: python

   # Create a new application software component inside the package
   component = package.createApplicationSwComponentType('MyComponent')

   print(f"Created component: {component.short_name}")

Writing an ARXML File
---------------------

After creating or modifying a model, you can write it to an ARXML file:

.. code-block:: python

   from armodel import AUTOSAR
   from armodel.writer import ARXMLWriter

   document = AUTOSAR.getInstance()

   # Save the document to a file
   writer = ARXMLWriter()
   writer.save('output.arxml', document)

   print("ARXML file written successfully")

Working with Ports
------------------

Adding Ports to a Component
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import TRefType

   # Create a provided port on the component
   provided_port = component.createPPortPrototype('MyProvidedPort')

   # Reference the interface the port provides
   interface_ref = TRefType()
   interface_ref.setDest('SENDER-RECEIVER-INTERFACE')
   interface_ref.setValue('/MyPackage/MyInterface')
   provided_port.setProvidedInterfaceTRef(interface_ref)

   # Create a required port
   required_port = component.createRPortPrototype('MyRequiredPort')
   required_port.setRequiredInterfaceTRef(interface_ref)

Working with Data Types
------------------------

Creating a Data Type
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Create an implementation data type
   data_type = package.createImplementationDataType('MyDataType')
   data_type.setCategory('TYPE_REFERENCE')

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

List all software components in ARXML files:

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

   armodel-uuid-checker input.arxml output.arxml

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
   for package in document.getARPackages():
       print(f"Package: {package.short_name}")

       # Get all elements in the package
       for element in package.getElements():
           print(f"  Element: {element.short_name} ({element.__class__.__name__})")

Error Handling
~~~~~~~~~~~~~~

.. code-block:: python

   from armodel import AUTOSAR
   from armodel.parser import ARXMLParser

   # Warnings instead of exceptions for recoverable issues
   parser = ARXMLParser(options={"warning": True})

   document = AUTOSAR.getInstance()
   document.clear()
   document.setARRelease('R23-11')

   try:
       parser.load('example.arxml', document)
   except FileNotFoundError:
       print("ARXML file not found")
   except Exception as e:
       print(f"Error parsing ARXML: {e}")

Working with UUIDs
------------------

py-armodel includes duplicate UUID checking:

.. code-block:: python

   from armodel import AUTOSAR

   document = AUTOSAR.getInstance()

   # Get all duplicate UUIDs after loading a document
   duplicates = document.getDuplicateUUIDs()

   if duplicates:
       print(f"Found {len(duplicates)} duplicate UUIDs")
       for uuid in duplicates:
           print(f"  UUID {uuid}")
   else:
       print("No duplicate UUIDs found")

Next Steps
----------

* Read the :doc:`arxml_parsing` guide for detailed parsing information
* Read the :doc:`arxml_writing` guide for detailed writing information
* Check the :doc:`../api/parser` and :doc:`../api/writer` API references
* Explore the :doc:`../examples/basic_usage` examples for more use cases

Basic Usage Examples
====================

This section provides basic examples for using py-armodel.

Example 1: Parse and Inspect ARXML
-----------------------------------

.. code-block:: python

   from armodel import AUTOSAR
   from armodel.parser import ARXMLParser

   # Prepare the document
   document = AUTOSAR.getInstance()
   document.clear()
   document.setARRelease('R23-11')

   # Parse ARXML file
   parser = ARXMLParser()
   parser.load('example.arxml', document)

   # Collect elements from all packages
   atomic_swcs = []
   composition_swcs = []
   for package in document.getARPackages():
       atomic_swcs.extend(package.getAtomicSwComponentTypes())
       composition_swcs.extend(package.getCompositionSwComponentTypes())

   # Print basic information
   print(f"Number of packages: {len(document.getARPackages())}")
   print(f"Number of atomic SWCs: {len(atomic_swcs)}")
   print(f"Number of composition SWCs: {len(composition_swcs)}")

   # List all packages
   print("\nPackages:")
   for package in document.getARPackages():
       print(f"  - {package.short_name}")

   # List all components
   print("\nComponents:")
   for swc in atomic_swcs:
       print(f"  - {swc.short_name} ({swc.getCategory()})")

Example 2: Create Simple Component
-----------------------------------

.. code-block:: python

   from armodel import AUTOSAR
   from armodel.writer import ARXMLWriter

   # Initialize AUTOSAR
   document = AUTOSAR.getInstance()
   document.clear()
   document.setARRelease('R23-11')

   # Create package
   package = document.createARPackage('MyPackage')

   # Create component
   component = package.createApplicationSwComponentType('MyComponent')
   component.setCategory('APPLICATION')

   # Write to file
   writer = ARXMLWriter()
   writer.save('simple_component.arxml', document)

   print("Created simple_component.arxml")

Example 3: Add Ports to Component
----------------------------------

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

   # Add provided port
   provided_port = component.createPPortPrototype('MyProvidedPort')
   interface_ref = TRefType()
   interface_ref.setDest('SENDER-RECEIVER-INTERFACE')
   interface_ref.setValue('/MyPackage/MyInterface')
   provided_port.setProvidedInterfaceTRef(interface_ref)

   # Add required port
   required_port = component.createRPortPrototype('MyRequiredPort')
   required_port.setRequiredInterfaceTRef(interface_ref)

   # Write to file
   writer = ARXMLWriter()
   writer.save('component_with_ports.arxml', document)

   print("Created component_with_ports.arxml")

Example 4: Find and Access Elements
------------------------------------

.. code-block:: python

   from armodel import AUTOSAR
   from armodel.parser import ARXMLParser

   document = AUTOSAR.getInstance()
   document.clear()
   document.setARRelease('R23-11')

   # Parse ARXML
   parser = ARXMLParser()
   parser.load('example.arxml', document)

   # Find specific component by full path
   component = document.findAtomicSwComponentType('/MyPackage/MyComponent')

   if component:
       print(f"Found component: {component.short_name}")

       # Access ports
       print("\nProvided ports:")
       for port in component.getPPortPrototypes():
           print(f"  - {port.short_name}")

       print("\nRequired ports:")
       for port in component.getRPortPrototypes():
           print(f"  - {port.short_name}")

   # Find specific data type
   data_type = document.findImplementationDataType('/MyPackage/MyDataType')

   if data_type:
       print(f"\nFound data type: {data_type.short_name}")
       print(f"Category: {data_type.getCategory()}")

   # Find specific system signal
   signal = document.findSystemSignal('/MyPackage/MySignal')

   if signal:
       print(f"\nFound system signal: {signal.short_name}")

Example 5: Iterate Through All Elements
----------------------------------------

.. code-block:: python

   from armodel import AUTOSAR
   from armodel.parser import ARXMLParser

   document = AUTOSAR.getInstance()
   document.clear()
   document.setARRelease('R23-11')

   # Parse ARXML
   parser = ARXMLParser()
   parser.load('example.arxml', document)

   # Iterate through packages
   for package in document.getARPackages():
       print(f"\nPackage: {package.short_name}")

       # Iterate through elements in package
       for element in package.getElements():
           print(f"  Element: {element.short_name} ({element.__class__.__name__})")

   # Iterate through all components
   print("\n\nAll Atomic SWCs:")
   for package in document.getARPackages():
       for swc in package.getAtomicSwComponentTypes():
           print(f"  - {swc.short_name}")

   # Iterate through all interfaces
   print("\nAll Sender-Receiver Interfaces:")
   for package in document.getARPackages():
       for interface in package.getSenderReceiverInterfaces():
           print(f"  - {interface.short_name}")

Example 6: Read and Write ARXML
--------------------------------

.. code-block:: python

   from armodel import AUTOSAR
   from armodel.parser import ARXMLParser
   from armodel.writer import ARXMLWriter

   document = AUTOSAR.getInstance()
   document.clear()
   document.setARRelease('R23-11')

   # Read ARXML
   parser = ARXMLParser()
   parser.load('input.arxml', document)

   # Modify model (optional)
   # ... modifications ...

   # Write ARXML
   writer = ARXMLWriter()
   writer.save('output.arxml', document)

   print("Read from input.arxml and wrote to output.arxml")

Example 7: Error Handling
--------------------------

.. code-block:: python

   from armodel import AUTOSAR
   from armodel.parser import ARXMLParser

   def parse_with_error_handling(file_path):
       """Parse ARXML with error handling."""
       document = AUTOSAR.getInstance()
       document.clear()
       document.setARRelease('R23-11')

       parser = ARXMLParser()

       try:
           parser.load(file_path, document)
           print(f"Successfully parsed {file_path}")
           return document

       except FileNotFoundError:
           print(f"Error: File not found: {file_path}")
           return None

       except Exception as e:
           print(f"Error parsing file: {e}")
           print(f"Error type: {type(e).__name__}")
           return None

   # Usage
   document = parse_with_error_handling('example.arxml')

   if document:
       print("Model loaded successfully")
   else:
       print("Failed to load model")

Example 8: Working with UUIDs
------------------------------

.. code-block:: python

   from armodel import AUTOSAR
   from armodel.parser import ARXMLParser

   document = AUTOSAR.getInstance()
   document.clear()
   document.setARRelease('R23-11')

   # Parse ARXML
   parser = ARXMLParser()
   parser.load('example.arxml', document)

   # Check for duplicate UUIDs
   duplicates = document.getDuplicateUUIDs()

   if duplicates:
       print(f"Found {len(duplicates)} duplicate UUIDs:")
       for uuid in duplicates:
           print(f"\nUUID: {uuid}")
           for element in document.getARObjectByUUID(uuid):
               print(f"  - {element.short_name} ({element.__class__.__name__})")
   else:
       print("No duplicate UUIDs found")

Example 9: Format ARXML File
-----------------------------

Reading a file and writing it back with py-armodel normalizes the XML layout:

.. code-block:: python

   from armodel import AUTOSAR
   from armodel.parser import ARXMLParser
   from armodel.writer import ARXMLWriter

   document = AUTOSAR.getInstance()
   document.clear()
   document.setARRelease('R23-11')

   # Read ARXML
   parser = ARXMLParser()
   parser.load('input.arxml', document)

   # Write it back (the ``arxml-format`` CLI tool does the same)
   writer = ARXMLWriter()
   writer.save('formatted.arxml', document)

   print("Formatted ARXML written to formatted.arxml")

Example 10: Multiple File Processing
-------------------------------------

.. code-block:: python

   from armodel import AUTOSAR
   from armodel.parser import ARXMLParser

   # List of ARXML files
   files = ['file1.arxml', 'file2.arxml', 'file3.arxml']

   document = AUTOSAR.getInstance()
   document.clear()
   document.setARRelease('R23-11')

   parser = ARXMLParser()

   # Process each file
   for file_path in files:
       try:
           parser.load(file_path, document)

           # Print summary
           atomic_swcs = []
           signals = []
           for package in document.getARPackages():
               atomic_swcs.extend(package.getAtomicSwComponentTypes())
               signals.extend(package.getSystemSignals())

           print(f"\n{file_path}:")
           print(f"  Packages: {len(document.getARPackages())}")
           print(f"  Components: {len(atomic_swcs)}")
           print(f"  Signals: {len(signals)}")

       except Exception as e:
           print(f"Error processing {file_path}: {e}")

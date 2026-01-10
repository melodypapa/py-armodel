Basic Usage Examples
====================

This section provides basic examples for using py-armodel.

Example 1: Parse and Inspect ARXML
-----------------------------------

.. code-block:: python

   from armodel.parser.arxml_parser import ARXMLParser

   # Create parser
   parser = ARXMLParser()

   # Parse ARXML file
   model = parser.parse_from_file('example.arxml')

   # Print basic information
   print(f"Number of packages: {len(model.getARPackages())}")
   print(f"Number of atomic SWCs: {len(model.getAtomicSwComponentTypes())}")
   print(f"Number of composition SWCs: {len(model.getCompositionSwComponentTypes())}")

   # List all packages
   print("\nPackages:")
   for package in model.getARPackages():
       print(f"  - {package.short_name}")

   # List all components
   print("\nComponents:")
   for swc in model.getAtomicSwComponentTypes():
       print(f"  - {swc.short_name} ({swc.category})")

Example 2: Create Simple Component
-----------------------------------

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

   # Create component
   component = ApplicationSwComponentType()
   component.short_name = 'MyComponent'
   component.category = 'APPLICATION'

   # Add to package
   package.addApplicationSwComponentType(component)

   # Write to file
   writer = ARXMLWriter()
   writer.write_to_file(autosar, 'simple_component.arxml')

   print("Created simple_component.arxml")

Example 3: Add Ports to Component
----------------------------------

.. code-block:: python

   from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
   from armodel.models.M2.AUTOSARTemplates.CommonStructure.SWComponentTemplate.ApplicationSwComponentType import ApplicationSwComponentType
   from armodel.models.M2.AUTOSARTemplates.CommonStructure.SWComponentTemplate.PortPrototype import PPortPrototype, RPortPrototype
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

   # Add provided port
   provided_port = PPortPrototype()
   provided_port.short_name = 'MyProvidedPort'
   provided_port.provided_interface_ref = ARRef(interface)
   component.addProvidedPort(provided_port)

   # Add required port
   required_port = RPortPrototype()
   required_port.short_name = 'MyRequiredPort'
   required_port.required_interface_ref = ARRef(interface)
   component.addRequiredPort(required_port)

   # Add to package
   package.addApplicationSwComponentType(component)

   # Write to file
   writer = ARXMLWriter()
   writer.write_to_file(autosar, 'component_with_ports.arxml')

   print("Created component_with_ports.arxml")

Example 4: Find and Access Elements
------------------------------------

.. code-block:: python

   from armodel.parser.arxml_parser import ARXMLParser

   # Parse ARXML
   parser = ARXMLParser()
   model = parser.parse_from_file('example.arxml')

   # Find specific component
   component = model.findAtomicSwComponentType('MyComponent')

   if component:
       print(f"Found component: {component.short_name}")

       # Access ports
       print("\nProvided ports:")
       for port in component.provided_ports:
           print(f"  - {port.short_name}")

       print("\nRequired ports:")
       for port in component.required_ports:
           print(f"  - {port.short_name}")

   # Find specific data type
   data_type = model.findImplementationDataType('MyDataType')

   if data_type:
       print(f"\nFound data type: {data_type.short_name}")
       print(f"Category: {data_type.category}")

   # Find specific system signal
   signal = model.findSystemSignal('MySignal')

   if signal:
       print(f"\nFound system signal: {signal.short_name}")

Example 5: Iterate Through All Elements
----------------------------------------

.. code-block:: python

   from armodel.parser.arxml_parser import ARXMLParser

   # Parse ARXML
   parser = ARXMLParser()
   model = parser.parse_from_file('example.arxml')

   # Iterate through packages
   for package in model.getARPackages():
       print(f"\nPackage: {package.short_name}")

       # Iterate through elements in package
       if hasattr(package, 'elements'):
           for element in package.elements:
               print(f"  Element: {element.short_name} ({element.__class__.__name__})")

   # Iterate through all components
   print("\n\nAll Atomic SWCs:")
   for swc in model.getAtomicSwComponentTypes():
       print(f"  - {swc.short_name}")

   # Iterate through all interfaces
   print("\nAll Sender-Receiver Interfaces:")
   for interface in model.getSenderReceiverInterfaces():
       print(f"  - {interface.short_name}")

Example 6: Read and Write ARXML
--------------------------------

.. code-block:: python

   from armodel.parser.arxml_parser import ARXMLParser
   from armodel.writer.arxml_writer import ARXMLWriter

   # Read ARXML
   parser = ARXMLParser()
   model = parser.parse_from_file('input.arxml')

   # Modify model (optional)
   # ... modifications ...

   # Write ARXML
   writer = ARXMLWriter()
   writer.write_to_file(model, 'output.arxml')

   print("Read from input.arxml and wrote to output.arxml")

Example 7: Error Handling
--------------------------

.. code-block:: python

   from armodel.parser.arxml_parser import ARXMLParser
   import logging

   # Configure logging
   logging.basicConfig(level=logging.INFO)

   def parse_with_error_handling(file_path):
       """Parse ARXML with error handling."""
       parser = ARXMLParser()

       try:
           model = parser.parse_from_file(file_path)
           print(f"Successfully parsed {file_path}")
           return model

       except FileNotFoundError:
           print(f"Error: File not found: {file_path}")
           return None

       except Exception as e:
           print(f"Error parsing file: {e}")
           print(f"Error type: {type(e).__name__}")
           return None

   # Usage
   model = parse_with_error_handling('example.arxml')

   if model:
       print("Model loaded successfully")
   else:
       print("Failed to load model")

Example 8: Working with UUIDs
------------------------------

.. code-block:: python

   from armodel.parser.arxml_parser import ARXMLParser
   from armodel.models.utils.uuid_mgr import UUIDManager

   # Parse ARXML
   parser = ARXMLParser()
   model = parser.parse_from_file('example.arxml')

   # Get UUID manager
   uuid_mgr = UUIDManager()

   # Check for duplicate UUIDs
   duplicates = uuid_mgr.check_duplicates()

   if duplicates:
       print(f"Found {len(duplicates)} duplicate UUIDs:")
       for uuid, elements in duplicates.items():
           print(f"\nUUID: {uuid}")
           for element in elements:
               print(f"  - {element.short_name} ({element.__class__.__name__})")
   else:
       print("No duplicate UUIDs found")

Example 9: Format ARXML File
-----------------------------

.. code-block:: python

   from armodel.parser.arxml_parser import ARXMLParser
   from armodel.writer.arxml_writer import ARXMLWriter

   # Read ARXML
   parser = ARXMLParser()
   model = parser.parse_from_file('input.arxml')

   # Write with formatting
   writer = ARXMLWriter()
   writer.write_to_file(model, 'formatted.arxml', pretty_print=True)

   print("Formatted ARXML written to formatted.arxml")

Example 10: Multiple File Processing
-------------------------------------

.. code-block:: python

   from armodel.parser.arxml_parser import ARXMLParser

   # List of ARXML files
   files = ['file1.arxml', 'file2.arxml', 'file3.arxml']

   parser = ARXMLParser()

   # Process each file
   for file_path in files:
       try:
           model = parser.parse_from_file(file_path)

           # Print summary
           print(f"\n{file_path}:")
           print(f"  Packages: {len(model.getARPackages())}")
           print(f"  Components: {len(model.getAtomicSwComponentTypes())}")
           print(f"  Signals: {len(model.getSystemSignals())}")

       except Exception as e:
           print(f"Error processing {file_path}: {e}")
Diagnostics Examples
=====================

This section provides examples for working with AUTOSAR diagnostics.

Example 1: Create Diagnostic Connection
----------------------------------------

.. code-block:: python

   from armodel import AUTOSAR
   from armodel.writer import ARXMLWriter

   # Initialize AUTOSAR
   document = AUTOSAR.getInstance()
   document.clear()
   document.setARRelease('R23-11')

   # Create package
   package = document.createARPackage('MyPackage')

   # Create diagnostic connection
   diag_connection = package.createDiagnosticConnection('MyDiagConnection')

   # Write to file
   writer = ARXMLWriter()
   writer.save('diagnostic_connection.arxml', document)

   print("Created diagnostic connection")

Example 2: Create Diagnostic Service Table
-------------------------------------------

.. code-block:: python

   from armodel import AUTOSAR
   from armodel.writer import ARXMLWriter

   # Initialize AUTOSAR
   document = AUTOSAR.getInstance()
   document.clear()
   document.setARRelease('R23-11')

   # Create package
   package = document.createARPackage('MyPackage')

   # Create diagnostic service table
   service_table = package.createDiagnosticServiceTable('MyServiceTable')

   # Write to file
   writer = ARXMLWriter()
   writer.save('diagnostic_service_table.arxml', document)

   print("Created diagnostic service table")

Example 3: List Diagnostic Elements
------------------------------------

Diagnostic elements are regular AR package elements. Filter the package
elements by their class to list them:

.. code-block:: python

   from armodel import AUTOSAR
   from armodel.parser import ARXMLParser
   from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection import DiagnosticConnection
   from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticContribution import DiagnosticServiceTable

   document = AUTOSAR.getInstance()
   document.clear()
   document.setARRelease('R23-11')

   # Parse ARXML
   parser = ARXMLParser()
   parser.load('example.arxml', document)

   # List diagnostic connections
   print("Diagnostic Connections:")
   for package in document.getARPackages():
       for element in package.getElements():
           if isinstance(element, DiagnosticConnection):
               print(f"  - {element.short_name} (in {package.short_name})")

   # List diagnostic service tables
   print("\nDiagnostic Service Tables:")
   for package in document.getARPackages():
       for element in package.getElements():
           if isinstance(element, DiagnosticServiceTable):
               print(f"  - {element.short_name}")

Example 4: Find Diagnostic Elements
------------------------------------

Elements are found by their full path:

.. code-block:: python

   from armodel import AUTOSAR
   from armodel.parser import ARXMLParser

   document = AUTOSAR.getInstance()
   document.clear()
   document.setARRelease('R23-11')

   # Parse ARXML
   parser = ARXMLParser()
   parser.load('example.arxml', document)

   # Find a diagnostic connection by its full path
   diag_connection = document.find('/MyPackage/MyDiagConnection')

   if diag_connection:
       print(f"Found: {diag_connection.short_name} "
             f"({diag_connection.__class__.__name__})")

Example 5: Complete Diagnostic Setup
-------------------------------------

.. code-block:: python

   from armodel import AUTOSAR
   from armodel.writer import ARXMLWriter

   # Initialize AUTOSAR
   document = AUTOSAR.getInstance()
   document.clear()
   document.setARRelease('R23-11')

   # Create package
   package = document.createARPackage('MyPackage')

   # Create diagnostic connection
   package.createDiagnosticConnection('MyDiagConnection')

   # Create diagnostic service table
   package.createDiagnosticServiceTable('MyServiceTable')

   # Write to file
   writer = ARXMLWriter()
   writer.save('complete_diagnostics.arxml', document)

   print("Created complete diagnostic setup")

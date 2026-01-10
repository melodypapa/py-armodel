Diagnostics Examples
=====================

This section provides examples for working with AUTOSAR diagnostics.

Example 1: Create Diagnostic Connection
----------------------------------------

.. code-block:: python

   from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
   from armodel.models.M2.AUTOSARTemplates.CommonStructure.SWComponentTemplate.ApplicationSwComponentType import ApplicationSwComponentType
   from armodel.models.M2.AUTOSARTemplates.CommonStructure.GenericStructure.DiagnosticExtract import DiagnosticConnection
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

   # Create diagnostic connection
   diag_connection = DiagnosticConnection()
   diag_connection.short_name = 'MyDiagConnection'

   # Add to component
   if not hasattr(component, 'diagnostic_connections'):
       component.diagnostic_connections = []
   component.diagnostic_connections.append(diag_connection)

   # Add to package
   package.addApplicationSwComponentType(component)

   # Write to file
   writer = ARXMLWriter()
   writer.write_to_file(autosar, 'diagnostic_connection.arxml')

   print("Created diagnostic connection")

Example 2: Create Diagnostic Service Table
-------------------------------------------

.. code-block:: python

   from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
   from armodel.models.M2.AUTOSARTemplates.CommonStructure.GenericStructure.DiagnosticExtract import DiagnosticServiceTable
   from armodel.writer.arxml_writer import ARXMLWriter

   # Initialize AUTOSAR
   autosar = AUTOSAR.getInstance()
   autosar.new()
   autosar.setARRelease('R24-11')

   # Create package
   package = autosar.createARPackage('MyPackage')

   # Create diagnostic service table
   service_table = DiagnosticServiceTable()
   service_table.short_name = 'MyServiceTable'

   # Add to package
   package.addDiagnosticServiceTable(service_table)

   # Write to file
   writer = ARXMLWriter()
   writer.write_to_file(autosar, 'diagnostic_service_table.arxml')

   print("Created diagnostic service table")

Example 3: Create Diagnostic Event Needs
-----------------------------------------

.. code-block:: python

   from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
   from armodel.models.M2.AUTOSARTemplates.CommonStructure.GenericStructure.DiagnosticExtract import DiagnosticEventNeeds
   from armodel.writer.arxml_writer import ARXMLWriter

   # Initialize AUTOSAR
   autosar = AUTOSAR.getInstance()
   autosar.new()
   autosar.setARRelease('R24-11')

   # Create package
   package = autosar.createARPackage('MyPackage')

   # Create diagnostic event needs
   event_needs = DiagnosticEventNeeds()
   event_needs.short_name = 'MyEventNeeds'

   # Add to package
   package.addDiagnosticEventNeeds(event_needs)

   # Write to file
   writer = ARXMLWriter()
   writer.write_to_file(autosar, 'diagnostic_event_needs.arxml')

   print("Created diagnostic event needs")

Example 4: Create Diagnostic Communication Manager Needs
--------------------------------------------------------

.. code-block:: python

   from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
   from armodel.models.M2.AUTOSARTemplates.CommonStructure.GenericStructure.DiagnosticExtract import DiagnosticCommunicationManagerNeeds
   from armodel.writer.arxml_writer import ARXMLWriter

   # Initialize AUTOSAR
   autosar = AUTOSAR.getInstance()
   autosar.new()
   autosar.setARRelease('R24-11')

   # Create package
   package = autosar.createARPackage('MyPackage')

   # Create diagnostic communication manager needs
   dcm_needs = DiagnosticCommunicationManagerNeeds()
   dcm_needs.short_name = 'MyDCMNeeds'

   # Add to package
   package.addDiagnosticCommunicationManagerNeeds(dcm_needs)

   # Write to file
   writer = ARXMLWriter()
   writer.write_to_file(autosar, 'dcm_needs.arxml')

   print("Created diagnostic communication manager needs")

Example 5: Create Diagnostic Routine Needs
-------------------------------------------

.. code-block:: python

   from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
   from armodel.models.M2.AUTOSARTemplates.CommonStructure.GenericStructure.DiagnosticExtract import DiagnosticRoutineNeeds
   from armodel.writer.arxml_writer import ARXMLWriter

   # Initialize AUTOSAR
   autosar = AUTOSAR.getInstance()
   autosar.new()
   autosar.setARRelease('R24-11')

   # Create package
   package = autosar.createARPackage('MyPackage')

   # Create diagnostic routine needs
   routine_needs = DiagnosticRoutineNeeds()
   routine_needs.short_name = 'MyRoutineNeeds'

   # Add to package
   package.addDiagnosticRoutineNeeds(routine_needs)

   # Write to file
   writer = ARXMLWriter()
   writer.write_to_file(autosar, 'diagnostic_routine_needs.arxml')

   print("Created diagnostic routine needs")

Example 6: List All Diagnostic Elements
----------------------------------------

.. code-block:: python

   from armodel.parser.arxml_parser import ARXMLParser

   # Parse ARXML
   parser = ARXMLParser()
   model = parser.parse_from_file('example.arxml')

   # List diagnostic connections
   print("Diagnostic Connections:")
   for component in model.getAtomicSwComponentTypes():
       if hasattr(component, 'diagnostic_connections'):
           for conn in component.diagnostic_connections:
               print(f"  - {conn.short_name} (in {component.short_name})")

   # List diagnostic service tables
   print("\nDiagnostic Service Tables:")
   for table in model.getDiagnosticServiceTables():
       print(f"  - {table.short_name}")

   # List diagnostic event needs
   print("\nDiagnostic Event Needs:")
   for needs in model.getDiagnosticEventNeeds():
       print(f"  - {needs.short_name}")

   # List diagnostic routine needs
   print("\nDiagnostic Routine Needs:")
   for needs in model.getDiagnosticRoutineNeeds():
       print(f"  - {needs.short_name}")

Example 7: Find Diagnostic Elements
------------------------------------

.. code-block:: python

   from armodel.parser.arxml_parser import ARXMLParser

   # Parse ARXML
   parser = ARXMLParser()
   model = parser.parse_from_file('example.arxml')

   # Find specific diagnostic service table
   service_table = model.findDiagnosticServiceTable('MyServiceTable')

   if service_table:
       print(f"Found service table: {service_table.short_name}")

   # Find specific diagnostic event needs
   event_needs = model.findDiagnosticEventNeeds('MyEventNeeds')

   if event_needs:
       print(f"Found event needs: {event_needs.short_name}")

   # Find component with diagnostic connections
   component = model.findAtomicSwComponentType('MyComponent')

   if component and hasattr(component, 'diagnostic_connections'):
       print(f"\nDiagnostic connections in {component.short_name}:")
       for conn in component.diagnostic_connections:
           print(f"  - {conn.short_name}")

Example 8: Complete Diagnostic Setup
-------------------------------------

.. code-block:: python

   from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
   from armodel.models.M2.AUTOSARTemplates.CommonStructure.SWComponentTemplate.ApplicationSwComponentType import ApplicationSwComponentType
   from armodel.models.M2.AUTOSARTemplates.CommonStructure.GenericStructure.DiagnosticExtract import (
       DiagnosticConnection,
       DiagnosticServiceTable,
       DiagnosticEventNeeds,
       DiagnosticCommunicationManagerNeeds,
       DiagnosticRoutineNeeds
   )
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

   # Create diagnostic connection
   diag_connection = DiagnosticConnection()
   diag_connection.short_name = 'MyDiagConnection'

   # Add diagnostic connection to component
   if not hasattr(component, 'diagnostic_connections'):
       component.diagnostic_connections = []
   component.diagnostic_connections.append(diag_connection)

   # Add component to package
   package.addApplicationSwComponentType(component)

   # Create diagnostic service table
   service_table = DiagnosticServiceTable()
   service_table.short_name = 'MyServiceTable'
   package.addDiagnosticServiceTable(service_table)

   # Create diagnostic event needs
   event_needs = DiagnosticEventNeeds()
   event_needs.short_name = 'MyEventNeeds'
   package.addDiagnosticEventNeeds(event_needs)

   # Create diagnostic communication manager needs
   dcm_needs = DiagnosticCommunicationManagerNeeds()
   dcm_needs.short_name = 'MyDCMNeeds'
   package.addDiagnosticCommunicationManagerNeeds(dcm_needs)

   # Create diagnostic routine needs
   routine_needs = DiagnosticRoutineNeeds()
   routine_needs.short_name = 'MyRoutineNeeds'
   package.addDiagnosticRoutineNeeds(routine_needs)

   # Write to file
   writer = ARXMLWriter()
   writer.write_to_file(autosar, 'complete_diagnostics.arxml')

   print("Created complete diagnostic setup")
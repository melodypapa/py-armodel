Working with Components
=======================

This section provides examples for working with AUTOSAR software components.

Example 1: Create Application Component
---------------------------------------

.. code-block:: python

   from armodel import AUTOSAR
   from armodel.writer import ARXMLWriter

   # Initialize AUTOSAR
   document = AUTOSAR.getInstance()
   document.clear()
   document.setARRelease('R23-11')

   # Create package
   package = document.createARPackage('MyPackage')

   # Create application component
   component = package.createApplicationSwComponentType('MyApplicationComponent')
   component.setCategory('APPLICATION')

   # Write to file
   writer = ARXMLWriter()
   writer.save('application_component.arxml', document)

   print("Created application component")

Example 2: Create Composition Component
----------------------------------------

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

   # Create interface
   interface = package.createSenderReceiverInterface('MyInterface')

   # Create two atomic components
   comp1 = package.createApplicationSwComponentType('Component1')
   comp1.setCategory('APPLICATION')

   comp2 = package.createApplicationSwComponentType('Component2')
   comp2.setCategory('APPLICATION')

   # Add ports to components
   port1 = comp1.createPPortPrototype('Port1')
   interface_ref = TRefType()
   interface_ref.setDest('SENDER-RECEIVER-INTERFACE')
   interface_ref.setValue('/MyPackage/MyInterface')
   port1.setProvidedInterfaceTRef(interface_ref)

   port2 = comp2.createRPortPrototype('Port2')
   port2.setRequiredInterfaceTRef(interface_ref)

   # Create composition
   composition = package.createCompositionSwComponentType('MyComposition')

   # Add component prototypes to the composition
   prototype1 = composition.createSwComponentPrototype('Prototype1')
   prototype2 = composition.createSwComponentPrototype('Prototype2')

   # Write to file
   writer = ARXMLWriter()
   writer.save('composition_component.arxml', document)

   print("Created composition component")

Example 3: Create Service Component
------------------------------------

.. code-block:: python

   from armodel import AUTOSAR
   from armodel.writer import ARXMLWriter

   # Initialize AUTOSAR
   document = AUTOSAR.getInstance()
   document.clear()
   document.setARRelease('R23-11')

   # Create package
   package = document.createARPackage('MyPackage')

   # Create service component
   service = package.createServiceSwComponentType('MyService')
   service.setCategory('SERVICE')

   # Write to file
   writer = ARXMLWriter()
   writer.save('service_component.arxml', document)

   print("Created service component")

Example 4: Add Behavior to Component
-------------------------------------

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

   # Create component
   component = package.createApplicationSwComponentType('MyComponent')
   component.setCategory('APPLICATION')

   # Create internal behavior
   behavior = component.createSwcInternalBehavior('MyBehavior')

   # Create runnable entity
   behavior.createRunnableEntity('MyRunnable')

   # Create init event which starts the runnable
   init_event = behavior.createInitEvent('MyInitEvent')
   start_ref = TRefType()
   start_ref.setDest('RUNNABLE-ENTITY')
   start_ref.setValue('/MyPackage/MyBehavior/MyRunnable')
   init_event.setStartOnEventRef(start_ref)

   # Write to file
   writer = ARXMLWriter()
   writer.save('component_with_behavior.arxml', document)

   print("Created component with behavior")

Example 5: List All Components
-------------------------------

.. code-block:: python

   from armodel import AUTOSAR
   from armodel.parser import ARXMLParser

   document = AUTOSAR.getInstance()
   document.clear()
   document.setARRelease('R23-11')

   # Parse ARXML
   parser = ARXMLParser()
   parser.load('example.arxml', document)

   # List all atomic components
   print("Atomic Software Components:")
   for package in document.getARPackages():
       for swc in package.getAtomicSwComponentTypes():
           print(f"  - {swc.short_name}")
           print(f"    Category: {swc.getCategory()}")
           print(f"    Provided ports: {len(swc.getPPortPrototypes())}")
           print(f"    Required ports: {len(swc.getRPortPrototypes())}")

   # List all composition components
   print("\nComposition Software Components:")
   for package in document.getARPackages():
       for comp in package.getCompositionSwComponentTypes():
           print(f"  - {comp.short_name}")
           print(f"    Prototypes: {len(comp.getComponents())}")
           print(f"    Connectors: {len(comp.getAssemblySwConnectors())}")

Example 6: Find Component by Name
----------------------------------

.. code-block:: python

   from armodel import AUTOSAR
   from armodel.parser import ARXMLParser

   document = AUTOSAR.getInstance()
   document.clear()
   document.setARRelease('R23-11')

   # Parse ARXML
   parser = ARXMLParser()
   parser.load('example.arxml', document)

   # Find component by full path
   component = document.findAtomicSwComponentType('/MyPackage/MyComponent')

   if component:
       print(f"Found component: {component.short_name}")
       print(f"Category: {component.getCategory()}")

       # Access ports
       print("\nProvided ports:")
       for port in component.getPPortPrototypes():
           print(f"  - {port.short_name}")

       # Access behavior
       behavior = component.getInternalBehavior()
       if behavior:
           print(f"\nBehavior: {behavior.short_name}")
           print(f"Runnables: {len(behavior.getRunnableEntities())}")
           print(f"Init events: {len(behavior.getInitEvents())}")
   else:
       print("Component not found")

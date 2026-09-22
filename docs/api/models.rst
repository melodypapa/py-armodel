Models API Reference
====================

This section documents the AUTOSAR model classes.

AUTOSAR Root Classes
--------------------

.. autoclass:: armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure.AUTOSAR
   :no-index:
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure.AbstractAUTOSAR
   :no-index:
   :members:
   :undoc-members:
   :show-inheritance:

AR Package
----------

.. autoclass:: armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ARPackage
   :no-index:
   :members:
   :undoc-members:
   :show-inheritance:

Software Components
-------------------

Application Software Component
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.ApplicationSwComponentType
   :no-index:
   :members:
   :undoc-members:
   :show-inheritance:

Composition Software Component
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.CompositionSwComponentType
   :no-index:
   :members:
   :undoc-members:
   :show-inheritance:

Port Prototypes
---------------

Provided Port
~~~~~~~~~~~~~

.. autoclass:: armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.PPortPrototype
   :no-index:
   :members:
   :undoc-members:
   :show-inheritance:

Required Port
~~~~~~~~~~~~~

.. autoclass:: armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.RPortPrototype
   :no-index:
   :members:
   :undoc-members:
   :show-inheritance:

Port Interfaces
---------------

Sender-Receiver Interface
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.SenderReceiverInterface
   :no-index:
   :members:
   :undoc-members:
   :show-inheritance:

Client-Server Interface
~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.ClientServerInterface
   :no-index:
   :members:
   :undoc-members:
   :show-inheritance:

Mode-Switch Interface
~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.ModeSwitchInterface
   :no-index:
   :members:
   :undoc-members:
   :show-inheritance:

Data Types
----------

Implementation Data Type
~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: armodel.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes.ImplementationDataType
   :no-index:
   :members:
   :undoc-members:
   :show-inheritance:

Data Prototypes
---------------

.. autoclass:: armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.VariableDataPrototype
   :no-index:
   :members:
   :undoc-members:
   :show-inheritance:

Behavior
--------

Internal Behavior
~~~~~~~~~~~~~~~~~

.. autoclass:: armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.SwcInternalBehavior
   :no-index:
   :members:
   :undoc-members:
   :show-inheritance:

Runnable Entity
~~~~~~~~~~~~~~~

.. autoclass:: armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RunnableEntity
   :no-index:
   :members:
   :undoc-members:
   :show-inheritance:

Events
------

Init Event
~~~~~~~~~~

.. autoclass:: armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents.InitEvent
   :no-index:
   :members:
   :undoc-members:
   :show-inheritance:

Connectors
----------

Assembly Connector
~~~~~~~~~~~~~~~~~~

.. autoclass:: armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.AssemblySwConnector
   :no-index:
   :members:
   :undoc-members:
   :show-inheritance:

Delegation Connector
~~~~~~~~~~~~~~~~~~~~

.. autoclass:: armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.DelegationSwConnector
   :no-index:
   :members:
   :undoc-members:
   :show-inheritance:

System Elements
---------------

System Signal
~~~~~~~~~~~~~

.. autoclass:: armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.SystemSignal
   :no-index:
   :members:
   :undoc-members:
   :show-inheritance:

ECU Instance
~~~~~~~~~~~~

.. autoclass:: armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.EcuInstance
   :no-index:
   :members:
   :undoc-members:
   :show-inheritance:

BSW Modules
-----------

BSW Module Description
~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswOverview.BswModuleDescription
   :no-index:
   :members:
   :undoc-members:
   :show-inheritance:

ECUC Configuration
------------------

ECUC Value Collection
~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: armodel.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate.EcucValueCollection
   :no-index:
   :members:
   :undoc-members:
   :show-inheritance:

ECUC Module Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: armodel.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate.EcucModuleConfigurationValues
   :no-index:
   :members:
   :undoc-members:
   :show-inheritance:

References
----------

Reference Type
~~~~~~~~~~~~~~

.. autoclass:: armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.RefType
   :no-index:
   :members:
   :undoc-members:
   :show-inheritance:

Typed Reference
~~~~~~~~~~~~~~~

.. autoclass:: armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.TRefType
   :no-index:
   :members:
   :undoc-members:
   :show-inheritance:

UUID Management
---------------

UUID Manager
~~~~~~~~~~~~

.. autoclass:: armodel.models.utils.uuid_mgr.UUIDMgr
   :no-index:
   :members:
   :undoc-members:
   :show-inheritance:

Usage Examples
--------------

Creating Components
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from armodel import AUTOSAR

   # Get AUTOSAR instance
   document = AUTOSAR.getInstance()
   document.clear()
   document.setARRelease('R23-11')

   # Create package and component
   package = document.createARPackage('MyPackage')
   component = package.createApplicationSwComponentType('MyComponent')
   component.setCategory('APPLICATION')

Finding Elements
~~~~~~~~~~~~~~~~

.. code-block:: python

   # Find component by full path
   component = document.findAtomicSwComponentType('/MyPackage/MyComponent')

   # Find data type by full path
   data_type = document.findImplementationDataType('/MyPackage/MyDataType')

   # Find system signal by full path
   signal = document.findSystemSignal('/MyPackage/MySignal')

Working with References
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import TRefType

   # Create a typed reference to an interface
   ref = TRefType()
   ref.setDest('SENDER-RECEIVER-INTERFACE')
   ref.setValue('/MyPackage/MyInterface')

   # Resolve a reference to the referenced element
   resolved = document.find(ref)

   if resolved:
       print(f"Resolved to: {resolved.short_name}")

Models API Reference
====================

This section documents the AUTOSAR model classes.

AUTOSAR Root Classes
--------------------

.. autoclass:: armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure.AUTOSAR
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure.AbstractAUTOSAR
   :members:
   :undoc-members:
   :show-inheritance:

AR Package
----------

.. autoclass:: armodel.models.M2.AUTOSARTemplates.CommonStructure.GenericStructure.ARObj.ARPackage
   :members:
   :undoc-members:
   :show-inheritance:

Software Components
-------------------

Application Software Component
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: armodel.models.M2.AUTOSARTemplates.CommonStructure.SWComponentTemplate.ApplicationSwComponentType
   :members:
   :undoc-members:
   :show-inheritance:

Composition Software Component
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: armodel.models.M2.AUTOSARTemplates.CommonStructure.SWComponentTemplate.CompositionSwComponentType
   :members:
   :undoc-members:
   :show-inheritance:

Service Software Component
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: armodel.models.M2.AUTOSARTemplates.CommonStructure.SWComponentTemplate.ServiceSwComponentType
   :members:
   :undoc-members:
   :show-inheritance:

Port Prototypes
---------------

Provided Port
~~~~~~~~~~~~~

.. autoclass:: armodel.models.M2.AUTOSARTemplates.CommonStructure.SWComponentTemplate.PortPrototype.PPortPrototype
   :members:
   :undoc-members:
   :show-inheritance:

Required Port
~~~~~~~~~~~~~

.. autoclass:: armodel.models.M2.AUTOSARTemplates.CommonStructure.SWComponentTemplate.PortPrototype.RPortPrototype
   :members:
   :undoc-members:
   :show-inheritance:

Port Interfaces
---------------

Sender-Receiver Interface
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: armodel.models.M2.AUTOSARTemplates.CommonStructure.GenericStructure.PortInterface.SenderReceiverInterface
   :members:
   :undoc-members:
   :show-inheritance:

Client-Server Interface
~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: armodel.models.M2.AUTOSARTemplates.CommonStructure.GenericStructure.PortInterface.ClientServerInterface
   :members:
   :undoc-members:
   :show-inheritance:

Mode-Switch Interface
~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: armodel.models.M2.AUTOSARTemplates.CommonStructure.GenericStructure.PortInterface.ModeSwitchInterface
   :members:
   :undoc-members:
   :show-inheritance:

Data Types
----------

Application Data Type
~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: armodel.models.M2.AUTOSARTemplates.CommonStructure.GenericStructure.DataTypeApplication.ApplicationDataType
   :members:
   :undoc-members:
   :show-inheritance:

Implementation Data Type
~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: armodel.models.M2.AUTOSARTemplates.CommonStructure.GenericStructure.DataTypeImplementation.ImplementationDataType
   :members:
   :undoc-members:
   :show-inheritance:

Data Prototypes
---------------

.. autoclass:: armodel.models.M2.AUTOSARTemplates.CommonStructure.GenericStructure.PortInterface.DataPrototype
   :members:
   :undoc-members:
   :show-inheritance:

Behavior
--------

Internal Behavior
~~~~~~~~~~~~~~~~~

.. autoclass:: armodel.models.M2.AUTOSARTemplates.CommonStructure.SWComponentTemplate.Behavior.SwcInternalBehavior
   :members:
   :undoc-members:
   :show-inheritance:

Runnable Entity
~~~~~~~~~~~~~~~

.. autoclass:: armodel.models.M2.AUTOSARTemplates.CommonStructure.SWComponentTemplate.Behavior.RunnableEntity
   :members:
   :undoc-members:
   :show-inheritance:

Events
------

Init Event
~~~~~~~~~~

.. autoclass:: armodel.models.M2.AUTOSARTemplates.CommonStructure.SWComponentTemplate.Behavior.InitEvent
   :members:
   :undoc-members:
   :show-inheritance:

Data Receive Event
~~~~~~~~~~~~~~~~~~

.. autoclass:: armodel.models.M2.AUTOSARTemplates.CommonStructure.SWComponentTemplate.Behavior.DataReceiveEvent
   :members:
   :undoc-members:
   :show-inheritance:

Mode Switch Event
~~~~~~~~~~~~~~~~~

.. autoclass:: armodel.models.M2.AUTOSARTemplates.CommonStructure.SWComponentTemplate.Behavior.SwcModeSwitchEvent
   :members:
   :undoc-members:
   :show-inheritance:

Connectors
----------

Assembly Connector
~~~~~~~~~~~~~~~~~~

.. autoclass:: armodel.models.M2.AUTOSARTemplates.CommonStructure.SWComponentTemplate.SwConnector.AssemblySwConnector
   :members:
   :undoc-members:
   :show-inheritance:

Delegation Connector
~~~~~~~~~~~~~~~~~~~~

.. autoclass:: armodel.models.M2.AUTOSARTemplates.CommonStructure.SWComponentTemplate.SwConnector.DelegationSwConnector
   :members:
   :undoc-members:
   :show-inheritance:

System Elements
---------------

System Signal
~~~~~~~~~~~~~

.. autoclass:: armodel.models.M2.AUTOSARTemplates.CommonStructure.SystemTemplate.System.SystemSignal
   :members:
   :undoc-members:
   :show-inheritance:

ECU Instance
~~~~~~~~~~~~

.. autoclass:: armodel.models.M2.AUTOSARTemplates.CommonStructure.SystemTemplate.System.ECUInstance
   :members:
   :undoc-members:
   :show-inheritance:

BSW Modules
-----------

BSW Module Description
~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswModuleDescription
   :members:
   :undoc-members:
   :show-inheritance:

BSW Behavior
~~~~~~~~~~~~

.. autoclass:: armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior
   :members:
   :undoc-members:
   :show-inheritance:

ECUC Configuration
------------------

ECUC Value Collection
~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: armodel.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate.EcucValueCollection
   :members:
   :undoc-members:
   :show-inheritance:

ECUC Module Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autoclass:: armodel.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate.EcucModuleConfigurationValues
   :members:
   :undoc-members:
   :show-inheritance:

References
----------

AR Reference
~~~~~~~~~~~

.. autoclass:: armodel.models.M2.AUTOSARTemplates.CommonStructure.GenericStructure.ARObj.ARRef
   :members:
   :undoc-members:
   :show-inheritance:

UUID Management
---------------

UUID Manager
~~~~~~~~~~~~

.. autoclass:: armodel.models.utils.uuid_mgr.UUIDManager
   :members:
   :undoc-members:
   :show-inheritance:

Usage Examples
--------------

Creating Components
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
   from armodel.models.M2.AUTOSARTemplates.CommonStructure.SWComponentTemplate.ApplicationSwComponentType import ApplicationSwComponentType

   # Get AUTOSAR instance
   autosar = AUTOSAR.getInstance()
   autosar.new()

   # Create component
   component = ApplicationSwComponentType()
   component.short_name = 'MyComponent'
   component.category = 'APPLICATION'

   # Add to package
   package = autosar.createARPackage('MyPackage')
   package.addApplicationSwComponentType(component)

Finding Elements
~~~~~~~~~~~~~~~

.. code-block:: python

   # Find component
   component = autosar.findAtomicSwComponentType('MyComponent')

   # Find data type
   data_type = autosar.findImplementationDataType('MyDataType')

   # Find system signal
   signal = autosar.findSystemSignal('MySignal')

Working with References
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from armodel.models.M2.AUTOSARTemplates.CommonStructure.GenericStructure.ARObj import ARRef

   # Create reference
   ref = ARRef(target_element)

   # Resolve reference
   resolved = ref.resolve(autosar_model)

   if resolved:
       print(f"Resolved to: {resolved.short_name}")
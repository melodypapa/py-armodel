.. py-armodel documentation master file

Welcome to py-armodel's Documentation
======================================

py-armodel is a Python library for parsing and generating AUTOSAR ARXML files. It provides comprehensive support for AUTOSAR models including software components, data types, communication patterns, and system configurations.

**Current Version**: 1.9.0  
**Python Requirements**: >= 3.5  
**License**: MIT

.. image:: https://badge.fury.io/py/armodel.svg
   :target: https://badge.fury.io/py/armodel
   :alt: PyPI version

.. image:: https://img.shields.io/badge/docs-latest-brightgreen.svg
   :target: https://py-armodel.readthedocs.io/en/latest/
   :alt: Documentation Status

.. image:: https://coveralls.io/repos/github/melodypapa/py-armodel/badge.svg?branch=main
   :target: https://coveralls.io/github/melodypapa/py-armodel?branch=main
   :alt: Coverage Status

.. contents:: Table of Contents
   :depth: 2
   :local:
   :backlinks: none

Overview
--------

py-armodel provides a complete ARXML (AUTOSAR XML) file parser and writer, supporting various AUTOSAR elements defined in the AUTOSAR standard. It implements data structures, interfaces, components, and communication patterns specified in AUTOSAR.

Key Features
------------

* **ARXML Parsing**: Parse AUTOSAR XML files with full validation
* **ARXML Generation**: Write AUTOSAR models to XML files
* **CLI Tools**: Multiple command-line tools for processing ARXML files
* **Data Models**: Complete AUTOSAR data model implementation
* **Connector Management**: Import/export software connectors to/from Excel
* **System Modeling**: Support for system signals, mappings, and ECU instances
* **Diagnostics**: Support for diagnostic connections, service tables, and event requirements
* **Communication Protocols**: Support for CAN, LIN, FlexRay, and Ethernet
* **BSW Support**: Complete Basic Software module description support

Quick Start
-----------

Installation
~~~~~~~~~~~~

Install py-armodel using pip:

.. code-block:: bash

   pip install armodel

Basic Usage
~~~~~~~~~~~

Parse an ARXML file:

.. code-block:: python

   from armodel.parser.arxml_parser import ARXMLParser

   parser = ARXMLParser()
   autosar_model = parser.parse_from_file('example.arxml')

Access AUTOSAR elements:

.. code-block:: python

   # Get all atomic software component types
   swcs = autosar_model.getAtomicSwComponentTypes()

   # Find a specific component
   component = autosar_model.findAtomicSwComponentType('MyComponent')

   # Get system signals
   signals = autosar_model.getSystemSignals()

Write an ARXML file:

.. code-block:: python

   from armodel.writer.arxml_writer import ARXMLWriter

   writer = ARXMLWriter()
   writer.write_to_file(autosar_model, 'output.arxml')

Documentation Structure
-----------------------

.. toctree::
   :maxdepth: 2
   :caption: User Guide:

   user_guide/installation
   user_guide/quickstart
   user_guide/arxml_parsing
   user_guide/arxml_writing
   user_guide/cli_tools

.. toctree::
   :maxdepth: 2
   :caption: API Reference:

   api/parser
   api/writer
   api/models
   api/cli

.. toctree::
   :maxdepth: 2
   :caption: Examples:

   examples/basic_usage
   examples/working_with_components
   examples/communication_setup
   examples/diagnostics

.. toctree::
   :maxdepth: 2
   :caption: Additional Information:

   changelog
   contributing
   license

Project Structure
-----------------

.. code-block:: text

   src/armodel/
   ├── cli/                    # Command-line tools
   ├── data_models/            # Data model definitions
   ├── lib/                    # Library functions
   ├── models/                 # AUTOSAR model definitions
   │   └── M2/                 # M2 model layer (MSR and AUTOSARTemplates)
   ├── parser/                 # Parser implementations
   ├── report/                 # Report generation
   ├── transformer/            # Transformers
   └── writer/                 # Writer implementations

Supported AUTOSAR Elements
---------------------------

**Component Types**

* ApplicationSwComponentType
* CompositionSwComponentType
* SensorActuatorSwComponentType
* ServiceSwComponentType

**Port Interfaces**

* SenderReceiverInterface
* ClientServerInterface
* ModeSwitchInterface
* ParameterInterface
* NvDataInterface

**Data Types**

* ApplicationDataType
* ImplementationDataType
* ApplicationRecordElement
* ApplicationArrayElement
* CompuMethod
* DataConstr
* Unit

**Communication**

* AssemblySwConnector
* DelegationSwConnector
* ServerComSpec
* ModeSwitchReceiverComSpec
* NvProvideComSpec
* NvRequireComSpec

**Protocols**

* CAN (CAN-FRAME, CAN-COMMUNICATION-CONNECTOR)
* LIN (LIN-CLUSTER, LIN-UNCONDITIONAL-FRAME)
* FlexRay (FLEXRAY-CLUSTER, FLEXRAY-COMMUNICATION-CONNECTOR)
* Ethernet (ETHERNET-COMMUNICATION-CONNECTOR, SO-AD-CONFIG)

**Behavior**

* RunnableEntity
* InternalBehavior
* SwcImplementation
* BswImplementation

**Events**

* InitEvent
* DataReceiveEvent
* SwcModeSwitchEvent
* BswBackgroundEvent
* BswDataReceivedEvent

**Diagnostics**

* DiagnosticConnection
* DiagnosticServiceTable
* DiagnosticEventNeeds

**System**

* SystemSignal
* SystemSignalGroup
* ECU-INSTANCE
* SWC-TO-ECU-MAPPING

**BSW Modules**

* BswModuleDescription
* BswBehavior
* BswSchedulableEntity
* BswCalledEntity

**ECUC Configuration**

* EcucValueCollection
* EcucModuleConfigurationValues
* EcucContainerValue
* EcucParameterValue

Command-Line Tools
------------------

py-armodel provides several CLI tools for common operations:

* ``arxml-dump`` - Dump all ARXML data to screen
* ``arxml-format`` - Format ARXML files
* ``armodel-component`` - List all software component types
* ``connector2xlsx`` - Export connectors to Excel
* ``connector-update`` - Update connectors from Excel
* ``armodel-system-signal`` - List all system signals
* ``armodel-memory-section`` - Manage memory sections
* ``armodel-file-list`` - List file information
* ``armodel-uuid-checker`` - Check for duplicate UUIDs
* ``format-xml`` - Format XML files

See :doc:`user_guide/cli_tools` for detailed usage information.

Contributing
------------

Contributions are welcome! Please see :doc:`contributing` for guidelines on how to contribute to py-armodel.

License
-------

py-armodel is licensed under the MIT License. See :doc:`license` for details.

Links
-----

* `GitHub Repository <https://github.com/melodypapa/py-armodel>`_
* `PyPI Package <https://pypi.org/project/armodel/>`_
* `AUTOSAR Official Website <https://www.autosar.org/>`

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
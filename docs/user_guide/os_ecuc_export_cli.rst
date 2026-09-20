``os-ecuc-export`` CLI
======================

``os-ecuc-export`` reads an AUTOSAR OS ECUC configuration and exports the
semantic OS configuration as YAML or an Excel workbook.

Command
-------

Run the command from the repository root or provide absolute paths:

.. code-block:: text

   os-ecuc-export [-h] [-v] [-w] INPUT [INPUT ...] OUTPUT

Arguments:

* ``INPUT``: one or more ECUC ARXML input paths. The command parses the first
  input path.
* ``OUTPUT``: output path. Its extension selects the output format.

Options:

* ``-h, --help``: show command help.
* ``-v, --verbose``: print debug information to the console.
* ``-w, --warning``: log unresolved standard references as warnings instead
  of failing conversion.

There is no ``--format`` option. The output filename is authoritative.

Output Formats
--------------

.. list-table::
   :header-rows: 1

   * - Extension
     - Format
   * - ``.yaml``
     - YAML
   * - ``.yml``
     - YAML
   * - ``.xlsx``
     - Excel workbook

Other extensions, including ``.json``, are rejected with a ``ValueError``.

Example: ``Os_ECUC.arxml``
--------------------------

The integration fixture is:

.. code-block:: text

   tests/integration_tests/test_files/Os_ECUC.arxml

Export YAML:

.. code-block:: bash

   os-ecuc-export tests/integration_tests/test_files/Os_ECUC.arxml build/os_config.yaml

Export Excel:

.. code-block:: bash

   os-ecuc-export tests/integration_tests/test_files/Os_ECUC.arxml build/os_config.xlsx

The fixture contains one semantic application and four semantic tasks:

.. code-block:: text

   Application: OsApplication_QM
   Tasks:
     - Init_Task
     - Rte_Event_Task
     - Rte_Time_Task
     - SchMDiagStateTask_20ms

The YAML export has these top-level sections:

.. code-block:: yaml

   OsApplication:
   - name: OsApplication_QM
     ...
   OsTask:
   - name: Init_Task
     ...

Exported Application Fields
---------------------------

Each ``OsApplication`` entry contains:

.. code-block:: text

   name
   OsTrusted
   OsTrustedApplicationDelayTimingViolationCall
   OsTrustedApplicationWithProtection
   OsAppAlarmRef
   OsAppCounterRef
   OsAppEcucPartitionRef
   OsAppIsrRef
   OsAppScheduleTableRef
   OsAppTaskRef
   OsMemoryMappingCodeLocationRef
   OsRestartTask
   OsAppStartupHook
   OsAppErrorHook
   OsAppShutdownHook
   OsTrustedFunctionName
   ApplicationState

For ``Os_ECUC.arxml``, ``OsAppTaskRef`` contains task names such as
``Init_Task`` and ``Rte_Event_Task``. References that are not converted into
semantic application or task objects remain ECUC paths.

Exported Task Fields
--------------------

Each ``OsTask`` entry contains:

.. code-block:: text

   name
   OsTaskActivation
   OsTaskPeriod
   OsTaskPriority
   OsTaskSchedule
   OsStacksize
   OsMemoryMappingCodeLocationRef
   OsTaskAccessingApplication
   OsTaskEventRef
   OsTaskResourceRef
   OsTaskAppModeRef
   OsTaskAllInterruptLockBudget
   OsTaskExecutionBudget
   OsTaskOsInterruptLockBudget
   OsTaskTimeFrame
   OsTaskResourceLockBudget
   OsTaskResourceLockResourceRef

Examples from the fixture include:

.. code-block:: yaml

   - name: Init_Task
     OsTaskActivation: 1
     OsTaskPriority: 127
     OsTaskSchedule: NON
     OsStacksize: 1024
     OsTaskAccessingApplication:
     - OsApplication_QM
     OsTaskAppModeRef:
     - /Os/Os/OSDEFAULTAPPMODE

Fields whose values are ``None`` or empty lists are omitted from YAML.
Repeated values are exported as lists. In Excel, repeated values are written
as comma-separated text in the corresponding cell, and the complete column
set is retained.

Warning Mode
------------

Strict mode is the default. An unresolved standard reference raises an OS
ECUC conversion error. Use ``-w`` to continue and preserve the unresolved
path:

.. code-block:: bash

   os-ecuc-export -w input/Os_ECUC.arxml build/os_config.yaml

The command also writes ``os_ecuc_export.log`` beside the output file.

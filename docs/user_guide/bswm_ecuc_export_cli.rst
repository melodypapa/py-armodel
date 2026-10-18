``bswm-ecuc-export`` CLI
========================

``bswm-ecuc-export`` reads the BswM configuration of an AUTOSAR ECUC ARXML file
and exports it as an Excel workbook or YAML. The export covers the BswM
configuration values (``BswMAction``, ``BswMActionList``, rules, conditions,
ports and general settings) of the ``BswM`` module.

Command
-------

.. code-block:: text

   bswm-ecuc-export [-h] [-v] [-w] INPUT OUTPUT

Arguments:

* ``INPUT``: the ECUC configuration ARXML file to read.
* ``OUTPUT``: the output file. Its extension selects the output format.

Options:

* ``-h, --help``: show command help.
* ``-v, --verbose``: print debug information to the console.
* ``-w, --warning``: report unresolved references as warnings and keep the
  unresolved path, instead of failing the export.

``OUTPUT`` must not be the same file as ``INPUT``.

Output Formats
--------------

.. list-table::
   :header-rows: 1

   * - Extension
     - Format
   * - ``.xlsx``
     - Excel workbook, one worksheet per section
   * - ``.yaml``, ``.yml``
     - YAML, one top-level key per section

Other extensions, including ``.json``, are rejected with an error.

Examples
--------

The repository ships a BswM ECUC fixture with a decision chain, rules,
conditions and ports. It also contains deliberate constraint violations, so
``BswMChecks`` has five rows for it:

.. code-block:: bash

   bswm-ecuc-export tests/test_armodel/parser/data/bswm_ecuc_arbitration.arxml build/bswm.xlsx
   bswm-ecuc-export tests/test_armodel/parser/data/bswm_ecuc_arbitration.arxml build/bswm.yaml

A fixture with a dangling reference needs warning mode, because the default
mode stops at the first unresolved reference:

.. code-block:: bash

   bswm-ecuc-export -w tests/test_armodel/parser/data/bswm_ecuc_minimal.arxml build/bswm.xlsx

The command writes ``bswm_ecuc_export.log`` beside the output file. The log is
replaced on each run.

Workbook Sheets
---------------

The sheets follow the SWS decision chain. ``BswMAction`` and ``BswMActionList``
come first, followed by the rules and the logic that feeds them.

.. list-table::
   :header-rows: 1

   * - Sheet
     - One row per
   * - ``BswMAction``
     - configured action
   * - ``BswMActionList``
     - action list item (an action list without items has one row)
   * - ``BswMRule``
     - arbitration rule
   * - ``BswMLogicalExpression``
     - logical expression
   * - ``BswMModeCondition``
     - mode condition
   * - ``BswMModeRequestPort``
     - mode request port
   * - ``BswMEventRequestPort``
     - event request port
   * - ``BswMSwitchPort``
     - mode switch port
   * - ``BswMRteModeRequestPort``
     - RTE mode request port
   * - ``BswMDataTypeMappingSets``
     - referenced DataTypeMappingSet (one row per reference)
   * - ``BswMGeneral``
     - the general settings (one row)
   * - ``BswMChecks``
     - configuration constraint violation (see below)

Sheets with no configured entries are still written, with their header row.

Columns
-------

Columns that are not described below are the SWS parameters and references of
the element, as named in the SWS. Multi-valued cells list one value per line
in Excel and as a list in YAML. Empty cells and empty lists are omitted from
YAML.

BswMConfig
  The ``BswMConfig`` instance that owns the row. A configuration with several
  partitions has one ``BswMConfig`` per partition, and each row is labelled
  with its partition.

Used-by columns
  ``UsedBy...`` columns list the entries that reference the row. For example,
  ``BswMAction.UsedByActionLists`` lists the action lists that run the action.
  An empty ``UsedBy...`` cell means the entry is not referenced, which can
  reveal configuration that is not used.

  References are matched by the full path of the element. Two partitions can
  both contain an action named ``AC_Start``, and each one lists only its own
  users.

Action columns
  ``BswMAction`` has one column for each SWS parameter or reference of the
  action type that is set (for example ``BswMUserCalloutFunction`` for a user
  callout). Action type is in ``BswMActionType``. An action has at most one
  action type.

Reference cells
  Action parameters and the source of mode and event request ports keep the
  full path of a referenced element, for example ``BswMRteSwitchPortRef``.
  References in rules, logical expressions, mode conditions and action list
  items show the short name.

Checks Sheet
------------

``BswMChecks`` lists the configuration constraints of SWS BSW Mode Manager
chapter 10 that the configuration violates. Each row has ``Rule``,
``Element`` and ``Message`` columns.

.. list-table::
   :header-rows: 1

   * - Rule
     - Check
   * - ``SWS_BswM_00242``
     - ``BSWM_NAND`` has exactly two arguments
   * - ``SWS_BswM_00243``
     - ``BSWM_NOT`` has exactly one argument
   * - ``SWS_BswM_00256``
     - the condition type matches the port kind: equality for mode request
       ports, set/cleared for event request ports
   * - ``SWS_BswM_00203``
     - an initial value does not set both ``BswMBswModeInitValue`` and
       ``BswMCompuScaleModeValue``
   * - ``SWS_BswM_CONSTR_00001``
     - no two items of an action list share a ``BswMActionListItemIndex``
   * - ``SWS_BswM_00240``
     - ``BswMReportFailRuntimeErrorId`` is within 128..255
   * - ``SWS_BswM_CONSTR_00003``, ``00004``, ``00005``
     - a group is not both enabled and disabled in the same deadline
       monitoring or group switch action
   * - ``SWS_BswM_00037``
     - action list nesting is at most 7 levels and is not cyclic

A clean configuration has no rows in ``BswMChecks``. The export still
succeeds: ``BswMChecks`` reports violations, but does not stop the export.

Warning Mode
------------

Strict mode is the default. An unresolved BswM reference, such as an action
list item that points to a missing action, stops the export. Use ``-w`` to
continue. The unresolved path is kept in the output and a warning is logged.

Limitations
-----------

* The draft action ``BswMIdsMBlockStateChangeRequest`` is not exported. Its
  parameters are not defined in the SWS chapter 10.
* References to other modules (ComM channels, EcuM modes, mode declarations,
  PDU groups) are written as paths. They are not resolved against those
  modules.
* Only configured values are exported. The parameter definitions (ranges,
  defaults, multiplicities) are not part of the output.

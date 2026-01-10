CLI Tools Reference
===================

py-armodel provides several command-line tools for common AUTOSAR operations.

Overview
--------

All CLI tools can be installed automatically when you install py-armodel:

.. code-block:: bash

   pip install armodel

The tools are then available in your system path.

Available Tools
---------------

arxml-dump
~~~~~~~~~~

Dump all ARXML data to screen for inspection.

**Usage:**

.. code-block:: bash

   arxml-dump --arxml <file1.arxml> --arxml <file2.arxml>

**Options:**

* ``--arxml`` - Specify ARXML file(s) to dump (can be used multiple times)
* ``-h, --help`` - Show help message

**Example:**

.. code-block:: bash

   arxml-dump --arxml SoftwareComponents.arxml

arxml-format
~~~~~~~~~~~~

Format ARXML files for better readability.

**Usage:**

.. code-block:: bash

   arxml-format <input.arxml> <output.arxml>

**Example:**

.. code-block:: bash

   arxml-format input.arxml formatted_output.arxml

armodel-component
~~~~~~~~~~~~~~~~~

List all software component types in ARXML files.

**Usage:**

.. code-block:: bash

   armodel-component [OPTIONS] <arxml_folder>

**Options:**

* ``-v, --verbose`` - Print debug information
* ``-f FORMAT, --format FORMAT`` - Specify output format
  * ``short`` - Only print short names (default)
  * ``long`` - Print with ARPackage names
* ``--filter FILTER`` - Filter components
  * ``CompositionSwComponent`` - Print only composition components
* ``-h, --help`` - Show help message

**Examples:**

List all components with short names:

.. code-block:: bash

   armodel-component /path/to/arxml/files

List composition components with long names:

.. code-block:: bash

   armodel-component --format long --filter CompositionSwComponent /path/to/arxml/files

connector2xlsx
~~~~~~~~~~~~~~

Export software connectors to an Excel file.

**Usage:**

.. code-block:: bash

   connector2xlsx <input.arxml> <output.xlsx>

**Supported Connectors:**

* AssemblySwConnector
* DelegationSwConnector

**Example:**

.. code-block:: bash

   connector2xlsx SoftwareComponents.arxml connectors.xlsx

connector-update
~~~~~~~~~~~~~~~

Update software connectors from an Excel file.

**Usage:**

.. code-block:: bash

   connector-update <input.arxml> <excel_file.xlsx> <output.arxml>

**Example:**

.. code-block:: bash

   connector-update SoftwareComponents.arxml connectors.xlsx Updated.arxml

armodel-system-signal
~~~~~~~~~~~~~~~~~~~~~

List all system signals in ARXML files.

**Usage:**

.. code-block:: bash

   armodel-system-signal <arxml_folder>

**Example:**

.. code-block:: bash

   armodel-system-signal /path/to/arxml/files

armodel-memory-section
~~~~~~~~~~~~~~~~~~~~~~

Manage memory sections in ARXML files.

**Usage:**

.. code-block:: bash

   armodel-memory-section <arxml_folder>

**Example:**

.. code-block:: bash

   armodel-memory-section /path/to/arxml/files

armodel-file-list
~~~~~~~~~~~~~~~~~

List file information for ARXML files.

**Usage:**

.. code-block:: bash

   armodel-file-list <arxml_folder>

**Example:**

.. code-block:: bash

   armodel-file-list /path/to/arxml/files

armodel-uuid-checker
~~~~~~~~~~~~~~~~~~~~

Check for duplicate UUIDs in ARXML files.

**Usage:**

.. code-block:: bash

   armodel-uuid-checker <arxml_folder>

**Output:**

The tool will report any duplicate UUIDs found in the ARXML files.

**Example:**

.. code-block:: bash

   armodel-uuid-checker /path/to/arxml/files

format-xml
~~~~~~~~~~

Format XML files for better readability.

**Usage:**

.. code-block:: bash

   format-xml <input.xml> <output.xml>

**Example:**

.. code-block:: bash

   format-xml input.xml formatted_output.xml

Common Patterns
---------------

Batch Processing
~~~~~~~~~~~~~~~~

Process multiple ARXML files:

.. code-block:: bash

   # List components in multiple files
   armodel-component file1.arxml file2.arxml file3.arxml

   # Check UUIDs in multiple directories
   armodel-uuid-checker dir1 dir2 dir3

Piping Output
~~~~~~~~~~~~~

Pipe output to other tools:

.. code-block:: bash

   # List components and filter
   armodel-component /path/to/files | grep "MyComponent"

   # Save system signals to file
   armodel-system-signal /path/to/files > signals.txt

Combining Tools
~~~~~~~~~~~~~~~

Use multiple tools together:

.. code-block:: bash

   # 1. Export connectors to Excel
   connector2xyzl SoftwareComponents.arxml connectors.xlsx

   # 2. Edit the Excel file
   # (use your spreadsheet editor)

   # 3. Update connectors from Excel
   connector-update SoftwareComponents.arxml connectors.xlsx Updated.arxml

   # 4. Format the updated file
   arxml-format Updated.arxml Final.arxml

Advanced Usage
--------------

Verbose Mode
~~~~~~~~~~~~

Enable verbose output for debugging:

.. code-block:: bash

   armodel-component -v /path/to/files

Filtering Results
~~~~~~~~~~~~~~~~~

Filter component types:

.. code-block:: bash

   # Only composition components
   armodel-component --filter CompositionSwComponent /path/to/files

   # All components with long names
   armodel-component --format long /path/to/files

Working with Directories
~~~~~~~~~~~~~~~~~~~~~~~~

Process all ARXML files in a directory:

.. code-block:: bash

   armodel-component /path/to/arxml/directory

The tool will recursively find and process all ``.arxml`` files.

Error Handling
--------------

File Not Found
~~~~~~~~~~~~~~

.. code-block:: bash

   armodel-dump --arxml nonexistent.arxml
   # Error: File not found: nonexistent.arxml

Invalid ARXML
~~~~~~~~~~~~~

.. code-block:: bash

   armodel-component invalid.arxml
   # Error: Failed to parse ARXML file

Duplicate UUIDs
~~~~~~~~~~~~~~~

.. code-block:: bash

   armodel-uuid-checker /path/to/files
   # Warning: Found 3 duplicate UUIDs
   # UUID xxx used by: Component1, Component2

Tips and Tricks
---------------

1. **Use pipe inspection**: Pipe output to ``less`` for large outputs
2. **Save to file**: Redirect output to a file for later analysis
3. **Check UUIDs first**: Always run ``armodel-uuid-checker`` before processing
4. **Format files**: Use ``arxml-format`` to improve readability
5. **Batch processing**: Process multiple files at once for efficiency

Performance
-----------

For large projects with many ARXML files:

* Use specific paths instead of recursive searches when possible
* Filter results to reduce output size
* Consider processing files in batches
* Use verbose mode only when debugging

Integration with Other Tools
----------------------------

Version Control
~~~~~~~~~~~~~~~

Track changes in ARXML files:

.. code-block:: bash

   # List components before changes
   armodel-component /path/to/files > components_before.txt

   # Make changes...

   # List components after changes
   armodel-component /path/to/files > components_after.txt

   # Compare
   diff components_before.txt components_after.txt

CI/CD Pipelines
~~~~~~~~~~~~~~~

Integrate with continuous integration:

.. code-block:: bash

   # In CI pipeline
   armodel-uuid-checker /path/to/files
   if [ $? -ne 0 ]; then
       echo "Duplicate UUIDs found!"
       exit 1
   fi

Documentation
~~~~~~~~~~~~~

Generate documentation from ARXML:

.. code-block:: bash

   # Extract component information
   armodel-component --format long /path/to/files > documentation.txt

   # Extract system signals
   armodel-system-signal /path/to/files > signals.txt

Troubleshooting
---------------

Tool Not Found
~~~~~~~~~~~~~~

If a tool is not found:

.. code-block:: bash

   # Reinstall py-armodel
   pip install --upgrade --force-reinstall armodel

   # Check installation
   pip show armodel

Permission Errors
~~~~~~~~~~~~~~~~~

If you encounter permission errors:

.. code-block:: bash

   # Use user installation
   pip install --user armodel

   # Or use virtual environment
   python -m venv venv
   source venv/bin/activate
   pip install armodel

Memory Issues
~~~~~~~~~~~~~

For very large ARXML files:

.. code-block:: bash

   # Process files individually
   for file in *.arxml; do
       armodel-dump --arxml "$file" > "$file.dump"
   done

Getting Help
------------

All tools support the ``--help`` flag:

.. code-block:: bash

   arxml-dump --help
   armodel-component --help
   connector2xlsx --help

Next Steps
----------

* Read the :doc:`quickstart` guide for basic usage
* Explore :doc:`arxml_parsing` and :doc:`arxml_writing` for programmatic access
* Check :doc:`../examples` for more examples
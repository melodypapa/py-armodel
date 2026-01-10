CLI API Reference
=================

This section documents the command-line interface (CLI) tools.

CLI Modules
-----------

arxml-dump CLI
~~~~~~~~~~~~~~

.. automodule:: armodel.cli.arxml_dump_cli
   :members:
   :undoc-members:
   :show-inheritance:

arxml-format CLI
~~~~~~~~~~~~~~~~

.. automodule:: armodel.cli.arxml_format_cli
   :members:
   :undoc-members:
   :show-inheritance:

connector2xlsx CLI
~~~~~~~~~~~~~~~~~~

.. automodule:: armodel.cli.connector2xlsx_cli
   :members:
   :undoc-members:
   :show-inheritance:

connector-update CLI
~~~~~~~~~~~~~~~~~~~~

.. automodule:: armodel.cli.connector_update_cli
   :members:
   :undoc-members:
   :show-inheritance:

swc-list CLI
~~~~~~~~~~~~

.. automodule:: armodel.cli.swc_list_cli
   :members:
   :undoc-members:
   :show-inheritance:

system-signal CLI
~~~~~~~~~~~~~~~~~

.. automodule:: armodel.cli.system_signal_cli
   :members:
   :undoc-members:
   :show-inheritance:

memory-section CLI
~~~~~~~~~~~~~~~~~~

.. automodule:: armodel.cli.memory_section_cli
   :members:
   :undoc-members:
   :show-inheritance:

file-list CLI
~~~~~~~~~~~~~

.. automodule:: armodel.cli.file_list_cli
   :members:
   :undoc-members:
   :show-inheritance:

uuid-checker CLI
~~~~~~~~~~~~~~~~

.. automodule:: armodel.cli.uuid_checker_cli
   :members:
   :undoc-members:
   :show-inheritance:

format-xml CLI
~~~~~~~~~~~~~~

.. automodule:: armodel.cli.format_xml_cli
   :members:
   :undoc-members:
   :show-inheritance:

Library Functions
-----------------

CLI Arguments Parser
~~~~~~~~~~~~~~~~~~~~

.. automodule:: armodel.lib.cli_args_parser
   :members:
   :undoc-members:
   :show-inheritance:

Software Component Library
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. automodule:: armodel.lib.sw_component
   :members:
   :undoc-members:
   :show-inheritance:

System Signal Library
~~~~~~~~~~~~~~~~~~~~~~

.. automodule:: armodel.lib.system_signal
   :members:
   :undoc-members:
   :show-inheritance:

Usage Examples
--------------

Using CLI in Python
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from armodel.cli.arxml_dump_cli import cli_main
   import sys

   # Simulate command-line arguments
   sys.argv = ['arxml-dump', '--arxml', 'example.arxml']

   # Run CLI
   cli_main()

Creating Custom CLI Tools
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from armodel.parser.arxml_parser import ARXMLParser
   from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
   import argparse

   def custom_cli():
       parser = argparse.ArgumentParser(description='Custom ARXML tool')
       parser.add_argument('input', help='Input ARXML file')
       parser.add_argument('--output', help='Output file')

       args = parser.parse_args()

       # Parse ARXML
       arxml_parser = ARXMLParser()
       model = arxml_parser.parse_from_file(args.input)

       # Process model
       # ... custom processing ...

       # Write output
       if args.output:
           from armodel.writer.arxml_writer import ARXMLWriter
           writer = ARXMLWriter()
           writer.write_to_file(model, args.output)

   if __name__ == '__main__':
       custom_cli()
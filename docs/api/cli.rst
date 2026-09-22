CLI API Reference
=================

This section documents the command-line interface (CLI) tools.

CLI Modules
-----------

arxml-dump CLI
~~~~~~~~~~~~~~

.. automodule:: armodel.cli.arxml_dump_cli
   :no-index:
   :members:
   :undoc-members:

arxml-format CLI
~~~~~~~~~~~~~~~~

.. automodule:: armodel.cli.arxml_format_cli
   :no-index:
   :members:
   :undoc-members:

connector2xlsx CLI
~~~~~~~~~~~~~~~~~~

.. automodule:: armodel.cli.connector2xlsx_cli
   :no-index:
   :members:
   :undoc-members:

connector-update CLI
~~~~~~~~~~~~~~~~~~~~

.. automodule:: armodel.cli.connector_update_cli
   :no-index:
   :members:
   :undoc-members:

swc-list CLI (armodel-component)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. automodule:: armodel.cli.swc_list_cli
   :no-index:
   :members:
   :undoc-members:

system-signal CLI
~~~~~~~~~~~~~~~~~

.. automodule:: armodel.cli.system_signal_cli
   :no-index:
   :members:
   :undoc-members:

memory-section CLI
~~~~~~~~~~~~~~~~~~

.. automodule:: armodel.cli.memory_section_cli
   :no-index:
   :members:
   :undoc-members:

file-list CLI
~~~~~~~~~~~~~

.. automodule:: armodel.cli.file_list_cli
   :no-index:
   :members:
   :undoc-members:

uuid-checker CLI
~~~~~~~~~~~~~~~~

.. automodule:: armodel.cli.uuid_checker_cli
   :no-index:
   :members:
   :undoc-members:

os-ecuc-export CLI
~~~~~~~~~~~~~~~~~~

.. automodule:: armodel.cli.os_config_export_cli
   :no-index:
   :members:
   :undoc-members:

format-xml CLI
~~~~~~~~~~~~~~

.. automodule:: armodel.cli.format_xml_cli
   :no-index:
   :members:
   :undoc-members:

Library Functions
-----------------

CLI Arguments Parser
~~~~~~~~~~~~~~~~~~~~

.. automodule:: armodel.lib.cli_args_parser
   :no-index:
   :members:
   :undoc-members:

Software Component Library
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. automodule:: armodel.lib.sw_component
   :no-index:
   :members:
   :undoc-members:

System Signal Library
~~~~~~~~~~~~~~~~~~~~~~

.. automodule:: armodel.lib.system_signal
   :no-index:
   :members:
   :undoc-members:

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

   from armodel import AUTOSAR
   from armodel.parser import ARXMLParser
   from armodel.writer import ARXMLWriter
   import argparse

   def custom_cli():
       ap = argparse.ArgumentParser(description='Custom ARXML tool')
       ap.add_argument('INPUT', help='Input ARXML file')
       ap.add_argument('OUTPUT', help='Output file')

       args = ap.parse_args()

       # Parse ARXML
       document = AUTOSAR.getInstance()
       document.clear()
       document.setARRelease('R23-11')

       arxml_parser = ARXMLParser()
       arxml_parser.load(args.INPUT, document)

       # Process model
       # ... custom processing ...

       # Write output
       writer = ARXMLWriter()
       writer.save(args.OUTPUT, document)

   if __name__ == '__main__':
       custom_cli()

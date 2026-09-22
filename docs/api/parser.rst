Parser API Reference
====================

This section documents the parser API for reading ARXML files.

Main Parser Class
-----------------

.. autoclass:: armodel.parser.arxml_parser.ARXMLParser
   :no-index:
   :members:
   :undoc-members:
   :show-inheritance:

Abstract Parser
---------------

.. autoclass:: armodel.parser.abstract_arxml_parser.AbstractARXMLParser
   :no-index:
   :members:
   :undoc-members:
   :show-inheritance:

Excel Parser
------------

.. autoclass:: armodel.parser.excel_parser.AbstractExcelParser
   :no-index:
   :members:
   :undoc-members:

Connector Excel Parser
----------------------

.. autoclass:: armodel.parser.connector_xlsx_parser.ConnectorXlsReader
   :no-index:
   :members:
   :undoc-members:
   :show-inheritance:

ECUC Parser
-----------

.. autoclass:: armodel.parser.ecuc_parser.EcucParser
   :no-index:
   :members:
   :undoc-members:

OS ECUC Parser
--------------

.. autoclass:: armodel.parser.os_ecuc_parser.OsEcucParser
   :no-index:
   :members:
   :undoc-members:
   :show-inheritance:

File List Parser
----------------

.. autoclass:: armodel.parser.file_parser.FileListParser
   :no-index:
   :members:
   :undoc-members:
   :show-inheritance:

Usage Examples
--------------

Basic Parsing
~~~~~~~~~~~~~

.. code-block:: python

   from armodel import AUTOSAR
   from armodel.parser import ARXMLParser

   # Get the AUTOSAR document singleton
   document = AUTOSAR.getInstance()
   document.clear()
   document.setARRelease('R23-11')  # REQUIRED before parsing

   # Create parser and load a file into the document
   parser = ARXMLParser()
   parser.load('example.arxml', document)

   # Access the document
   packages = document.getARPackages()

Parsing with Options
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Create parser with warning mode (recoverable issues are reported
   # as warnings instead of raising exceptions)
   parser = ARXMLParser(options={"warning": True})

   parser.load('example.arxml', document)

Parsing Multiple Files
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   parser = ARXMLParser()

   files = ['file1.arxml', 'file2.arxml', 'file3.arxml']

   for file_path in files:
       parser.load(file_path, document)

Error Handling
~~~~~~~~~~~~~~

.. code-block:: python

   from armodel import AUTOSAR
   from armodel.parser import ARXMLParser

   parser = ARXMLParser()
   document = AUTOSAR.getInstance()
   document.clear()
   document.setARRelease('R23-11')

   try:
       parser.load('example.arxml', document)
   except FileNotFoundError:
       print("File not found")
   except Exception as e:
       print(f"Parsing error: {e}")

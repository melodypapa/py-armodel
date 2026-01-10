Parser API Reference
====================

This section documents the parser API for reading ARXML files.

Main Parser Class
-----------------

.. autoclass:: armodel.parser.arxml_parser.ARXMLParser
   :members:
   :undoc-members:
   :show-inheritance:

Abstract Parser
---------------

.. autoclass:: armodel.parser.abstract_arxml_parser.AbstractARXMLParser
   :members:
   :undoc-members:
   :show-inheritance:

Excel Parser
------------

.. autoclass:: armodel.parser.excel_parser.ExcelParser
   :members:
   :undoc-members:
   :show-inheritance:

Connector Excel Parser
----------------------

.. autoclass:: armodel.parser.connector_xlsx_parser.ConnectorXlsxParser
   :members:
   :undoc-members:
   :show-inheritance:

File Parser
-----------

.. autoclass:: armodel.parser.file_parser.FileParser
   :members:
   :undoc-members:
   :show-inheritance:

Parser Exceptions
-----------------

Exception Classes
~~~~~~~~~~~~~~~~~

The parser may raise the following exceptions:

.. autoexception:: armodel.parser.arxml_parser.ARXMLParserError
   :members:
   :show-inheritance:

.. autoexception:: armodel.parser.arxml_parser.ValidationError
   :members:
   :show-inheritance:

Usage Examples
--------------

Basic Parsing
~~~~~~~~~~~~~

.. code-block:: python

   from armodel.parser.arxml_parser import ARXMLParser

   # Create parser
   parser = ARXMLParser()

   # Parse file
   model = parser.parse_from_file('example.arxml')

   # Access model
   packages = model.getARPackages()

Parsing with Options
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Create parser with warning mode
   parser = ARXMLParser(options={"warning": True})

   # Parse with warnings
   model = parser.parse_from_file('example.arxml')

Parsing Multiple Files
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   parser = ARXMLParser()

   files = ['file1.arxml', 'file2.arxml', 'file3.arxml']

   models = []
   for file_path in files:
       model = parser.parse_from_file(file_path)
       models.append(model)

Error Handling
~~~~~~~~~~~~~~

.. code-block:: python

   from armodel.parser.arxml_parser import ARXMLParser, ARXMLParserError

   parser = ARXMLParser()

   try:
       model = parser.parse_from_file('example.arxml')
   except ARXMLParserError as e:
       print(f"Parser error: {e}")
   except FileNotFoundError:
       print("File not found")
   except Exception as e:
       print(f"Unexpected error: {e}")
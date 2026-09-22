Writer API Reference
====================

This section documents the writer API for generating ARXML files.

Main Writer Class
-----------------

.. autoclass:: armodel.writer.arxml_writer.ARXMLWriter
   :no-index:
   :members:
   :undoc-members:
   :show-inheritance:

Abstract Writer
---------------

.. autoclass:: armodel.writer.abstract_arxml_writer.AbstractARXMLWriter
   :no-index:
   :members:
   :undoc-members:
   :show-inheritance:

Usage Examples
--------------

Basic Writing
~~~~~~~~~~~~~

.. code-block:: python

   from armodel import AUTOSAR
   from armodel.writer import ARXMLWriter

   document = AUTOSAR.getInstance()

   # Save the document to a file
   writer = ARXMLWriter()
   writer.save('output.arxml', document)

Error Handling
~~~~~~~~~~~~~~

.. code-block:: python

   from armodel import AUTOSAR
   from armodel.writer import ARXMLWriter

   writer = ARXMLWriter()

   try:
       writer.save('output.arxml', document)
   except Exception as e:
       print(f"Writer error: {e}")

Batch Writing
~~~~~~~~~~~~~

Multiple ARXML files can be written from one document by saving the
document after each processing step:

.. code-block:: python

   from armodel import AUTOSAR
   from armodel.parser import ARXMLParser
   from armodel.writer import ARXMLWriter

   document = AUTOSAR.getInstance()
   document.clear()
   document.setARRelease('R23-11')

   parser = ARXMLParser()
   writer = ARXMLWriter()

   for input_file in ['file1.arxml', 'file2.arxml', 'file3.arxml']:
       document.clear()
       parser.load(input_file, document)

       output_file = input_file.replace('.arxml', '_converted.arxml')
       writer.save(output_file, document)
       print(f"Wrote {output_file}")

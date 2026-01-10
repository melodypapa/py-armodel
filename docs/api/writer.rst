Writer API Reference
====================

This section documents the writer API for generating ARXML files.

Main Writer Class
-----------------

.. autoclass:: armodel.writer.arxml_writer.ARXMLWriter
   :members:
   :undoc-members:
   :show-inheritance:

Abstract Writer
---------------

.. autoclass:: armodel.writer.abstract_arxml_writer.AbstractARXMLWriter
   :members:
   :undoc-members:
   :show-inheritance:

Writer Exceptions
-----------------

Exception Classes
~~~~~~~~~~~~~~~~~

The writer may raise the following exceptions:

.. autoexception:: armodel.writer.arxml_writer.ARXMLWriterError
   :members:
   :show-inheritance:

.. autoexception:: armodel.writer.arxml_writer.ValidationError
   :members:
   :show-inheritance:

Usage Examples
--------------

Basic Writing
~~~~~~~~~~~~~

.. code-block:: python

   from armodel.writer.arxml_writer import ARXMLWriter

   # Create writer
   writer = ARXMLWriter()

   # Write model to file
   writer.write_to_file(autosar_model, 'output.arxml')

Writing with Formatting
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   writer = ARXMLWriter()

   # Write with pretty printing
   writer.write_to_file(
       autosar_model,
       'output.arxml',
       pretty_print=True
   )

Writing to String
~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Write to string instead of file
   xml_string = writer.write_to_string(autosar_model)

   print(xml_string)

Error Handling
~~~~~~~~~~~~~~

.. code-block:: python

   from armodel.writer.arxml_writer import ARXMLWriter, ARXMLWriterError

   writer = ARXMLWriter()

   try:
       writer.write_to_file(autosar_model, 'output.arxml')
   except ARXMLWriterError as e:
       print(f"Writer error: {e}")
   except Exception as e:
       print(f"Unexpected error: {e}")

Advanced Usage
--------------

Custom Formatting
~~~~~~~~~~~~~~~~~

.. code-block:: python

   writer = ARXMLWriter()

   # Write with custom indentation
   writer.write_to_file(
       autosar_model,
       'output.arxml',
       indent='  ',
       encoding='utf-8'
   )

Writing Specific Elements
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Write only specific packages
   from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR

   autosar = AUTOSAR.getInstance()
   package = autosar.findARPackage('MyPackage')

   if package:
       writer.write_element_to_file(package, 'package.arxml')

Batch Writing
~~~~~~~~~~~~~

.. code-block:: python

   # Write multiple models
   models = [model1, model2, model3]
   writer = ARXMLWriter()

   for i, model in enumerate(models):
       output_file = f'output_{i}.arxml'
       writer.write_to_file(model, output_file)
       print(f"Wrote {output_file}")
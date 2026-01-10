Installation
============

Requirements
------------

* Python >= 3.5
* pip (Python package installer)

Installing from PyPI
--------------------

The easiest way to install py-armodel is using pip:

.. code-block:: bash

   pip install armodel

This will install py-armodel and all its dependencies:

* **colorama** - Cross-platform colored terminal output
* **openpyxl** - Excel file processing
* **lxml** - XML processing library

Installing from Source
----------------------

If you prefer to install from source, clone the repository and install:

.. code-block:: bash

   git clone https://github.com/melodypapa/py-armodel.git
   cd py-armodel
   pip install .

Development Installation
-------------------------

For development, install the package in editable mode with test dependencies:

.. code-block:: bash

   git clone https://github.com/melodypapa/py-armodel.git
   cd py-armodel
   pip install -e ".[pytest]"

This allows you to modify the code without reinstalling.

Verifying Installation
----------------------

To verify that py-armodel is installed correctly, run:

.. code-block:: bash

   python -c "import armodel; print(armodel.__version__)"

You should see the version number printed.

You can also check the installed CLI tools:

.. code-block:: bash

   arxml-dump --help

Installing Dependencies
------------------------

If you need to install dependencies manually:

.. code-block:: bash

   pip install colorama openpyxl lxml

Upgrading
---------

To upgrade to the latest version:

.. code-block:: bash

   pip install --upgrade armodel

Uninstalling
------------

To uninstall py-armodel:

.. code-block:: bash

   pip uninstall armodel

Troubleshooting
---------------

Permission Errors
~~~~~~~~~~~~~~~~~

If you encounter permission errors during installation, try:

.. code-block:: bash

   pip install --user armodel

Or use a virtual environment:

.. code-block:: bash

   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install armodel

XML Library Issues
~~~~~~~~~~~~~~~~~~~

py-armodel uses lxml for XML processing. If you encounter issues installing lxml:

On Ubuntu/Debian:

.. code-block:: bash

   sudo apt-get install python3-dev libxml2-dev libxslt1-dev
   pip install armodel

On macOS:

.. code-block:: bash

   brew install libxml2 libxslt
   pip install armodel

On Windows, lxml binary wheels are available and should install without issues.
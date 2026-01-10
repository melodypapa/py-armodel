Contributing to py-armodel
===========================

Thank you for your interest in contributing to py-armodel! This document provides guidelines for contributing to the project.

Getting Started
---------------

Prerequisites
~~~~~~~~~~~~~

* Python >= 3.5
* Git
* Familiarity with AUTOSAR standard

Setting Up Development Environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Fork the repository on GitHub
2. Clone your fork:

.. code-block:: bash

   git clone https://github.com/your-username/py-armodel.git
   cd py-armodel

3. Create a virtual environment:

.. code-block:: bash

   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

4. Install in development mode:

.. code-block:: bash

   pip install -e ".[pytest]"

5. Install development dependencies:

.. code-block:: bash

   pip install -r tests/requirements.txt

6. Run tests to verify setup:

.. code-block:: bash

   pytest

Code Style
----------

py-armodel follows PEP 8 style guidelines. We use Flake8 for code linting.

.. code-block:: bash

   # Run Flake8
   flake8 src/armodel

   # Auto-fix some issues
   autopep8 --in-place --aggressive src/armodel/**/*.py

Testing
-------

Running Tests
~~~~~~~~~~~~~

Run all tests:

.. code-block:: bash

   pytest

Run tests with coverage:

.. code-block:: bash

   pytest --cov=armodel --cov-report term-missing

Run specific test file:

.. code-block:: bash

   pytest tests/test_armodel/parser/test_arxml_parser.py

Run specific test:

.. code-block:: bash

   pytest tests/test_armodel/parser/test_arxml_parser.py::test_parse

Writing Tests
~~~~~~~~~~~~~

Tests should be placed in the ``tests/`` directory following the project structure.

Example test:

.. code-block:: python

   import pytest
   from armodel.parser.arxml_parser import ARXMLParser

   def test_parse_simple_arxml():
       parser = ARXMLParser()
       model = parser.parse_from_file('test_files/simple.arxml')

       assert model is not None
       assert len(model.getARPackages()) > 0

Documentation
-------------

Building Documentation
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   cd docs
   make html

The documentation will be built in ``docs/_build/html/``.

Writing Documentation
~~~~~~~~~~~~~~~~~~~~~

Documentation is written in reStructuredText format. See the existing documentation for examples.

When adding new features or modifying existing ones, update the relevant documentation:

* API changes: Update API reference in ``docs/api/``
* New features: Add examples in ``docs/examples/``
* User-facing changes: Update user guide in ``docs/user_guide/``

Submitting Changes
------------------

Creating a Pull Request
~~~~~~~~~~~~~~~~~~~~~~~

1. Create a new branch for your changes:

.. code-block:: bash

   git checkout -b feature/my-feature

2. Make your changes and commit them:

.. code-block:: bash

   git add .
   git commit -m "Add my feature"

3. Push to your fork:

.. code-block:: bash

   git push origin feature/my-feature

4. Create a pull request on GitHub

Pull Request Guidelines
~~~~~~~~~~~~~~~~~~~~~~~

* Provide a clear description of the changes
* Reference related issues (e.g., "Fixes #123")
* Include tests for new features
* Update documentation as needed
* Ensure all tests pass
* Ensure code follows style guidelines

Commit Message Format
~~~~~~~~~~~~~~~~~~~~~

Use clear, descriptive commit messages:

.. code-block:: text

   Add support for new AUTOSAR element

   - Add MyNewElement class
   - Update parser to read MyNewElement
   - Update writer to write MyNewElement
   - Add tests for MyNewElement

   Fixes #123

Development Workflow
--------------------

Feature Development
~~~~~~~~~~~~~~~~~~~

1. Create an issue describing the feature
2. Discuss the implementation approach
3. Create a branch for the feature
4. Implement the feature
5. Add tests
6. Update documentation
7. Submit a pull request

Bug Fixes
~~~~~~~~~

1. Create an issue describing the bug
2. Reproduce the bug
3. Create a branch for the fix
4. Fix the bug
5. Add regression tests
6. Submit a pull request

Code Review Process
-------------------

All pull requests go through code review. Be prepared to:

* Answer questions about your changes
* Make requested modifications
* Update tests or documentation as needed
* Address any issues raised during review

Project Structure
-----------------

Understanding the codebase:

* ``src/armodel/parser/`` - ARXML parsing logic
* ``src/armodel/writer/`` - ARXML writing logic
* ``src/armodel/models/`` - AUTOSAR model classes
* ``src/armodel/cli/`` - Command-line tools
* ``tests/`` - Test files
* ``docs/`` - Documentation

AUTOSAR Standard Compliance
----------------------------

py-armodel aims to comply with the AUTOSAR standard. When adding new features:

1. Reference the relevant AUTOSAR specification
2. Follow the naming conventions
3. Implement all required attributes
4. Handle optional attributes appropriately
5. Validate against the AUTOSAR schema

Common Tasks
------------

Adding a New AUTOSAR Element
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Create the model class in ``src/armodel/models/``
2. Add parsing logic in ``src/armodel/parser/``
3. Add writing logic in ``src/armodel/writer/``
4. Add tests in ``tests/``
5. Update documentation

Adding a CLI Tool
~~~~~~~~~~~~~~~~~

1. Create the CLI module in ``src/armodel/cli/``
2. Add entry point in ``setup.py``
3. Add tests
4. Update documentation

Adding Tests
~~~~~~~~~~~~

1. Create test file in ``tests/``
2. Write test functions
3. Add test ARXML files if needed
4. Ensure tests pass

Getting Help
------------

If you need help:

* Check existing issues on GitHub
* Read the documentation
* Ask questions in issues or discussions
* Review existing pull requests for examples

Community Guidelines
--------------------

* Be respectful and constructive
* Welcome new contributors
* Focus on what is best for the community
* Show empathy towards other community members

License
-------

By contributing to py-armodel, you agree that your contributions will be licensed under the MIT License.

Thank You
----------

Thank you for contributing to py-armodel! Your contributions help make the project better for everyone.
.. _JOBTMPL/UnitTesting:

UnitTesting
###########

This template runs multiple jobs from a matrix as a cross of Python versions and systems. The summary report in junit
XML format is optionally uploaded as an artifact.

Configuration options to ``pytest`` should be given via section ``[tool.pytest.ini_options]`` in a ``pyproject.toml``
file.

**Behavior:**

1. Checkout repository
2. Setup Python and install dependencies
3. Run unit tests using ``pytest``.
4. Upload junit test summary as an artifact

**Dependencies:**

* :gh:`actions/checkout`
* :gh:`msys2/setup-msys2`
* :gh:`actions/setup-python`
* :gh:`actions/upload-artifact`

Instantiation
*************

Simple Example
==============

.. code-block:: yaml

   jobs:
     Params:
       # ...

     UnitTesting:
       uses: pyTooling/Actions/.github/workflows/UnitTesting.yml@r4
       needs:
         - Params
       with:
         jobs: ${{ needs.Params.outputs.python_jobs }}
         artifact: ${{ fromJson(needs.Params.outputs.artifact_names).unittesting }}


Complex Example
===============

.. code-block:: yaml

   TBD

Parameters
**********

jobs
====

+----------------+----------+----------+--------------+
| Parameter Name | Required | Type     | Default      |
+================+==========+==========+==============+
| jobs           | yes      | string   | — — — —      |
+----------------+----------+----------+--------------+

JSON list with environment fields, telling the system and Python versions to run tests with.


requirements
============

+----------------+----------+----------+---------------------------------+
| Parameter Name | Required | Type     | Default                         |
+================+==========+==========+=================================+
| requirements   | optional | string   | ``-r tests/requirements.txt``   |
+----------------+----------+----------+---------------------------------+

Python dependencies to be installed through pip.


pacboy
======

+----------------+----------+----------+-----------+
| Parameter Name | Required | Type     | Default   |
+================+==========+==========+===========+
| pacboy         | optional | string   | ``""``    |
+----------------+----------+----------+-----------+

Additional MSYS2 dependencies to be installed through pacboy (pacman).

Internally, a workflow step reads the requirements file for Python and compares requested packages with a list of
packages that should be installed through pacman/pacboy compared to installation via pip. These are mainly core packages
or packages with embedded C code.

.. code-block:: yaml

   pacboy: >-
     python-lxml:p


mingw_requirements
==================

+--------------------+----------+----------+----------+
| Parameter Name     | Required | Type     | Default  |
+====================+==========+==========+==========+
| mingw_requirements | optional | string   | ``""``   |
+--------------------+----------+----------+----------+

Override Python dependencies to be installed through pip on MSYS2 (MINGW64) only.


tests_directory
===============

+-----------------+----------+----------+-----------+
| Parameter Name  | Required | Type     | Default   |
+=================+==========+==========+===========+
| tests_directory | optional | string   | ``tests`` |
+-----------------+----------+----------+-----------+

Path to the directory containing tests (test working directory).


unittest_directory
==================

+--------------------+----------+----------+----------+
| Parameter Name     | Required | Type     | Default  |
+====================+==========+==========+==========+
| unittest_directory | optional | string   | ``unit`` |
+--------------------+----------+----------+----------+

Path to the directory containing unit tests (relative to tests_directory).


artifact
========

+----------------+----------+----------+----------+
| Parameter Name | Required | Type     | Default  |
+================+==========+==========+==========+
| artifact       | optional | string   | ``""``   |
+----------------+----------+----------+----------+

Generate unit test report with junitxml and upload results as an artifact.


Secrets
*******

This job template needs no secrets.


Results
*******

This job template has no output parameters.

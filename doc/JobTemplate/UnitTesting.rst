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

* actions/checkout@v2
* actions/setup-python@v2
* actions/upload-artifact@v2

Instantiation
*************

Simple Example
==============

.. code-block:: yaml

   jobs:
     Params:
       # ...

     UnitTesting:
       uses: pyTooling/Actions/.github/workflows/UnitTesting.yml@r0
       needs:
         - Params
       with:
         jobs: ${{ needs.Params.outputs.python_jobs }}
         artifact: ${{ fromJson(needs.Params.outputs.params).artifacts.Unittesting }}


Complex Example
===============

.. code-block:: yaml

   TBD

Parameters
**********

jobs
====

JSON list with environment fields, telling the system and Python versions to run tests with.

+----------+----------+--------------+
| Required | Type     | Default      |
+==========+==========+==============+
| yes      | string   | — — — —      |
+----------+----------+--------------+

requirements
============

Python dependencies to be installed through pip.

+----------+----------+----------+
| Required | Type     | Default  |
+==========+==========+==========+
| optional | string   | ``-r tests/requirements.txt``   |
+----------+----------+----------+


pacboy
======

MSYS2 dependencies to be installed through pacboy (pacman).

+----------+----------+-----------------------------------------------------------------+
| Required | Type     | Default                                                         |
+==========+==========+=================================================================+
| optional | string   | ``python-pip:p python-wheel:p python-coverage:p python-lxml:p`` |
+----------+----------+-----------------------------------------------------------------+

.. code-block:: yaml

   pacboy: >-
     python-pip:p
     python-wheel:p
     python-coverage:p
     python-lxml:p


mingw_requirements
==================

Override Python dependencies to be installed through pip on MSYS2 (MINGW64) only.

+----------+----------+----------+
| Required | Type     | Default  |
+==========+==========+==========+
| optional | string   | ``""``   |
+----------+----------+----------+


tests_directory
===============

Path to the directory containing tests (test working directory).

+----------+----------+-----------+
| Required | Type     | Default   |
+==========+==========+===========+
| optional | string   | ``tests`` |
+----------+----------+-----------+


unittest_directory
==================

Path to the directory containing unit tests (relative to tests_directory).

+----------+----------+----------+
| Required | Type     | Default  |
+==========+==========+==========+
| optional | string   | ``unit`` |
+----------+----------+----------+


artifact
========

Generate unit test report with junitxml and upload results as an artifact.

+----------+----------+----------+
| Required | Type     | Default  |
+==========+==========+==========+
| optional | string   | ``""``   |
+----------+----------+----------+


Secrets
*******

This job template needs no secrets.

Results
*******

This job template has no output parameters.

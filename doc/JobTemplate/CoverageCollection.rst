.. _JOBTMPL/CodeCoverage:

CoverageCollection
##################

This jobs runs the specified unit tests with activated code coverage collection (incl. branch coverage).

It uses pytest, pytest-cov and coverage.py in a single job run, thus it uses one fixed Python version (usually latest).
It generates HTML and Cobertura reports (XML), then it uploads the HTML report as an artifact and the jUnit test results
(XML) to `Codecov <https://about.codecov.io/>`__ and `Codacy <https://www.codacy.com/>`__.

Configuration options to ``pytest`` and ``coverage.py`` should be given via sections ``[tool.pytest.ini_options]`` and
``[tool.coverage.*]`` in a ``pyproject.toml`` file.

**Behavior:**

1. Checkout repository
2. Setup Python and install dependencies
3. Extract configuration from ``pyproject.toml`` or ``.coveragerc``.
4. Run unit tests and collect code coverage
5. Convert coverage data to a Cobertura XML file
6. Convert coverage data to a HTML report
7. Upload HTML report as an artifact
8. Publish Cobertura file to CodeCov
9. Publish Cobertura file to Codacy

**Preconditions:**

* A CodeCov account was created.
* A Codacy account was created.

**Requirements:**

Setup a secret (e.g. ``codacy_token``) in GitHub to handover the Codacy project token to the job.

**Dependencies:**

* actions/checkout@v2
* actions/setup-python@v2
* actions/upload-artifact@v2
* codecov/codecov-action@v1
* codacy/codacy-coverage-reporter-action@master


Instantiation
*************

Simple Example
==============

.. code-block:: yaml

   jobs:
     Coverage:
       uses: pyTooling/Actions/.github/workflows/CoverageCollection.yml@r0
       with:
         artifact: Coverage
       secrets:
         codacy_token: ${{ secrets.CODACY_PROJECT_TOKEN }}

Complex Example
===============

.. code-block:: yaml

   jobs:
     Coverage:
       uses: pyTooling/Actions/.github/workflows/CoverageCollection.yml@r0
       needs:
         - Params
       with:
         python_version: ${{ fromJson(needs.Params.outputs.params).python_version }}
         artifact: ${{ fromJson(needs.Params.outputs.params).artifacts.Coverage }}
       secrets:
         codacy_token: ${{ secrets.CODACY_PROJECT_TOKEN }}

Parameters
**********

python_version
==============

Python version used for running unit tests.

+----------+----------+----------+
| Required | Type     | Default  |
+==========+==========+==========+
| optional | string   | 3.11     |
+----------+----------+----------+


requirements
============

Python dependencies to be installed through pip.

+----------+----------+-------------------------------+
| Required | Type     | Default                       |
+==========+==========+===============================+
| optional | string   | ``-r tests/requirements.txt`` |
+----------+----------+-------------------------------+


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

Path to the directory containing unit tests (relative to test_directory).

+----------+----------+-----------+
| Required | Type     | Default   |
+==========+==========+===========+
| optional | string   | ``unit``  |
+----------+----------+-----------+


coverage_config
===============

Path to the ``.coveragerc`` file. Use ``pyproject.toml`` by default.

+----------+----------+--------------------+
| Required | Type     | Default            |
+==========+==========+====================+
| optional | string   | ``pyproject.toml`` |
+----------+----------+--------------------+


artifact
========

Name of the coverage artifact.

+----------+----------+--------------+
| Required | Type     | Default      |
+==========+==========+==============+
| yes      | string   | — — — —      |
+----------+----------+--------------+

Secrets
*******

codacy_token
============

Token to push result to codacy.

+----------+----------+--------------+
| Required | Type     | Default      |
+==========+==========+==============+
| yes      | string   | — — — —      |
+----------+----------+--------------+


Results
*******

This job template has no output parameters.

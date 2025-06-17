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

* :gh:`actions/checkout`
* :gh:`actions/setup-python`
* :gh:`actions/upload-artifact`
* :gh:`codecov/codecov-action`
* :gh:`codacy/codacy-coverage-reporter-action`


Instantiation
*************

Simple Example
==============

.. code-block:: yaml

   jobs:
     Coverage:
       uses: pyTooling/Actions/.github/workflows/CoverageCollection.yml@r4
       with:
         artifact: Coverage
       secrets: inherit

Complex Example
===============

.. code-block:: yaml

   jobs:
     Coverage:
       uses: pyTooling/Actions/.github/workflows/CoverageCollection.yml@r4
       needs:
         - Params
       with:
         python_version: ${{ needs.Params.outputs.python_version }}
         artifact: ${{ fromJson(needs.Params.outputs.artifact_names).codecoverage_html }}
       secrets: inherit

Parameters
**********

python_version
==============

+----------------+----------+----------+----------+
| Parameter Name | Required | Type     | Default  |
+================+==========+==========+==========+
| python_version | optional | string   | 3.11     |
+----------------+----------+----------+----------+

Python version used for running unit tests.


requirements
============

+----------------+----------+----------+-------------------------------+
| Parameter Name | Required | Type     | Default                       |
+================+==========+==========+===============================+
| requirements   | optional | string   | ``-r tests/requirements.txt`` |
+----------------+----------+----------+-------------------------------+

Python dependencies to be installed through pip.


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

+--------------------+----------+----------+-----------+
| Parameter Name     | Required | Type     | Default   |
+====================+==========+==========+===========+
| unittest_directory | optional | string   | ``unit``  |
+--------------------+----------+----------+-----------+

Path to the directory containing unit tests (relative to tests_directory).


coverage_config
===============

+-----------------+----------+----------+--------------------+
| Parameter Name  | Required | Type     | Default            |
+=================+==========+==========+====================+
| coverage_config | optional | string   | ``pyproject.toml`` |
+-----------------+----------+----------+--------------------+

Path to the ``.coveragerc`` file. Use ``pyproject.toml`` by default.


artifact
========

+----------------+----------+----------+--------------+
| Parameter Name | Required | Type     | Default      |
+================+==========+==========+==============+
| artifact       | yes      | string   | — — — —      |
+----------------+----------+----------+--------------+

Name of the coverage artifact.


Secrets
*******

codacy_token
============

+----------------+----------+----------+--------------+
| Secret Name    | Required | Type     | Default      |
+================+==========+==========+==============+
| codacy_token   | yes      | string   | — — — —      |
+----------------+----------+----------+--------------+

Token to push result to codacy.


Results
*******

This job template has no output parameters.

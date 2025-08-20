.. _JOBTMPL/Parameters:

Parameters
##########

The ``Parameters`` job template is a workaround for the limitations of GitHub Actions to handle global variables in
GitHub Actions workflows (see `actions/runner#480 <https://github.com/actions/runner/issues/480>`__.

It generates output parameters with artifact names and a job matrix to be used in later running jobs.

**Behavior:**

.. todo:: Parameters:Behavior Needs documentation.

**Dependencies:**

*None*

Instantiation
*************

Simple Example
==============

The following instantiation example creates a job `Params` derived from job template `Parameters` version `r0`. It only
requires a `name` parameter to create the artifact names.

.. code-block:: yaml

   name: Pipeline

   on:
     push:
     workflow_dispatch:

   jobs:
     Params:
       uses: pyTooling/Actions/.github/workflows/Parameters.yml@r5
       with:
         name: pyTooling

Complex Example
===============

The following instantiation example creates 3 jobs from the same template, but with differing input parameters. The
first job `UnitTestingParams` might be used to create a job matrix of unit tests. It creates the cross of default
systems (Windows, Ubuntu, macOS, MinGW64, UCRT64) and the given list of Python versions including some mypy versions. In
addition a list of excludes (marked as :deletion:`deletions`) and includes (marked as :addition:`additions`) is handed
over resulting in the following combinations:

+------------+-------------+-------------+--------------+--------------+-------------------------+------------+-------------+------------------------------+-------------------------------+
| Version    | 3.8 🔴      | 3.9 🟠      | 3.10 🟡      | 3.11 🟢      | 3.12 🟢                 | 3.13.a1 🟣 | pypy-3.8 🔴 | pypy-3.9 🟠                  | pypy-3.10 🟡                  |
+============+=============+=============+==============+==============+=========================+============+=============+==============================+===============================+
| Windows 🧊 | windows:3.8 | windows:3.9 | windows:3.10 | windows:3.11 |                         |            |             | :deletion:`windows:pypy-3.9` | :deletion:`windows:pypy-3.10` |
+------------+-------------+-------------+--------------+--------------+-------------------------+------------+-------------+------------------------------+-------------------------------+
| Ubuntu 🐧  | ubuntu:3.8  | ubuntu:3.9  | ubuntu:3.10  | ubuntu:3.11  | :addition:`ubuntu:3.12` |            |             | ubuntu:pypy-3.9              | ubuntu:pypy-3.10              |
+------------+-------------+-------------+--------------+--------------+-------------------------+------------+-------------+------------------------------+-------------------------------+
| macOS 🍎   | macos:3.8   | macos:3.9   | macos:3.10   | macos:3.11   | :addition:`macos:3.12`  |            |             | macos:pypy-3.9               | macos:pypy-3.10               |
+------------+-------------+-------------+--------------+--------------+-------------------------+------------+-------------+------------------------------+-------------------------------+
| MSYS 🟪    |             |             |              |              |                         |            |             |                              |                               |
+------------+-------------+-------------+--------------+--------------+-------------------------+------------+-------------+------------------------------+-------------------------------+
| MinGW32 ⬛ |             |             |              |              |                         |            |             |                              |                               |
+------------+-------------+-------------+--------------+--------------+-------------------------+------------+-------------+------------------------------+-------------------------------+
| MinGW64 🟦 |             |             |              | mingw64:3.11 |                         |            |             |                              |                               |
+------------+-------------+-------------+--------------+--------------+-------------------------+------------+-------------+------------------------------+-------------------------------+
| Clang32 🟫 |             |             |              |              |                         |            |             |                              |                               |
+------------+-------------+-------------+--------------+--------------+-------------------------+------------+-------------+------------------------------+-------------------------------+
| Clang64 🟧 |             |             |              |              |                         |            |             |                              |                               |
+------------+-------------+-------------+--------------+--------------+-------------------------+------------+-------------+------------------------------+-------------------------------+
| UCRT64 🟨  |             |             |              |              |                         |            |             |                              |                               |
+------------+-------------+-------------+--------------+--------------+-------------------------+------------+-------------+------------------------------+-------------------------------+


.. code-block:: yaml

   name: Pipeline

   on:
     push:
     workflow_dispatch:

   jobs:
     UnitTestingParams:
       uses: pyTooling/Actions/.github/workflows/Parameters.yml@r5
       with:
         name: pyTooling
         python_version_list: "3.8 3.9 3.10 3.11 pypy-3.9 pypy-3.10"
         include_list: "ubuntu:3.12 macos:3.12"
         exclude_list: "windows:pypy-3.9 windows:pypy-3.10"

     PerformanceTestingParams:
       uses: pyTooling/Actions/.github/workflows/Parameters.yml@r5
       with:
         name: pyTooling
         python_version_list: "3.11 3.12"
         system_list: "ubuntu windows macos"

     PlatformTestingParams:
       uses: pyTooling/Actions/.github/workflows/Parameters.yml@dev
       with:
         name: pyTooling
         python_version_list: "3.12"
         system_list: "ubuntu windows macos mingw32 mingw64 clang64 ucrt64"

Parameters
**********

name
====

+----------------+----------+----------+--------------+
| Parameter Name | Required | Type     | Default      |
+================+==========+==========+==============+
| name           | yes      | string   | — — — —      |
+----------------+----------+----------+--------------+

The name of the library or package.

It's used to create artifact names.


python_version
==============

+----------------+----------+----------+----------+
| Parameter Name | Required | Type     | Default  |
+================+==========+==========+==========+
| python_version | optional | string   | ``3.12`` |
+----------------+----------+----------+----------+

Python version to be used for all jobs requiring a single Python version.


python_version_list
===================

+----------------------+----------+----------+----------------------------+
| Parameter Name       | Required | Type     | Default                    |
+======================+==========+==========+============================+
| python_version_list  | optional | string   | ``3.8 3.9 3.10 3.11 3.12`` |
+----------------------+----------+----------+----------------------------+

Space separated list of CPython versions and/or mypy version to run tests with.

.. include:: ../PythonVersionList.rst


system_list
===========

+----------------+----------+----------+-----------------------------------------+
| Parameter Name | Required | Type     | Default                                 |
+================+==========+==========+=========================================+
| system_list    | optional | string   | ``ubuntu windows macos mingw64 ucrt64`` |
+----------------+----------+----------+-----------------------------------------+

Space separated list of systems to run tests on.

.. include:: ../SystemList.rst


include_list
============

+----------------+----------+----------+----------+
| Parameter Name | Required | Type     | Default  |
+================+==========+==========+==========+
| include_list   | optional | string   | ``""``   |
+----------------+----------+----------+----------+

Space separated list of ``system:python`` items to be included into the list of test.

**Example:**

.. code-block:: yaml

   include_list: "ubuntu:3.11 macos:3.11"


exclude_list
============

+----------------+----------+----------+----------+
| Parameter Name | Required | Type     | Default  |
+================+==========+==========+==========+
| exclude_list   | optional | string   | ``""``   |
+----------------+----------+----------+----------+

Space separated list of ``system:python`` items to be excluded from the list of test.

**Example:**

.. code-block:: yaml

   exclude_list: "windows:pypy-3.8 windows:pypy-3.9"


disable_list
============

+----------------+----------+----------+----------+
| Parameter Name | Required | Type     | Default  |
+================+==========+==========+==========+
| disable_list   | optional | string   | ``""``   |
+----------------+----------+----------+----------+

Space separated list of ``system:python`` items to be temporarily disabled from the list of test.

Each disabled item creates a warning in the workflow log:

.. image:: /_static/GH_Workflow_DisabledJobsWarnings.png
   :scale: 80 %


**Example:**

.. code-block:: yaml

   disable_list: "windows:3.10 windows:3.11"


Secrets
*******

This job template needs no secrets.

Results
*******

python_version
==============

A single string parameter representing the default Python version that should be used across multiple jobs in the same
pipeline.

Such a parameter is needed as a workaround, because GitHub Actions doesn't support proper handling of global pipeline
variables. Thus, this job is used to compute an output parameter that can be reused in other jobs.

**Usage Example:**

.. code-block:: yaml

   jobs:
     Params:
       uses: pyTooling/Actions/.github/workflows/Parameters.yml@r5
       with:
         name: pyTooling

     CodeCoverage:
       uses: pyTooling/Actions/.github/workflows/CoverageCollection.yml@r5
       needs:
         - Params
       with:
         python_version: ${{ needs.Params.outputs.python_version }}

python_jobs
===========

A list of dictionaries containing a job description.

A job description contains the following key-value pairs:

* ``sysicon`` - icon to display
* ``system`` -  name of the system
* ``runs-on`` - virtual machine image and base operating system
* ``runtime`` - name of the runtime environment if not running natively on the VM image
* ``shell`` -   name of the shell
* ``pyicon`` -  icon for CPython or pypy
* ``python`` -  Python version
* ``envname`` - full name of the selected environment

**Usage Example:**

.. code-block:: yaml

   jobs:
     Params:
       uses: pyTooling/Actions/.github/workflows/Parameters.yml@r5
       with:
         name: pyTooling

     UnitTesting:
       uses: pyTooling/Actions/.github/workflows/UnitTesting.yml@dev
       needs:
         - Params
       with:
         jobs: ${{ needs.Params.outputs.python_jobs }}

This list can be unpacked with ``fromJson(...)`` in a job ``strategy:matrix:include``:

.. code-block:: yaml

   UnitTesting:
     name: ${{ matrix.sysicon }} ${{ matrix.pyicon }} Unit Tests using Python ${{ matrix.python }}
     runs-on: ${{ matrix.runs-on }}

     strategy:
       matrix:
         include: ${{ fromJson(inputs.jobs) }}

     defaults:
       run:
         shell: ${{ matrix.shell }}

     steps:
       - name: 🐍 Setup Python ${{ matrix.python }}
         if: matrix.system != 'msys2'
         uses: actions/setup-python@v4
         with:
           python-version: ${{ matrix.python }}


artifact_names
==============

A dictionary of artifact names sharing a common prefix.

The supported artifacts are:

* ``unittesting_xml`` - UnitTesting XML summary report
* ``unittesting_html`` - UnitTesting HTML summary report
* ``codecoverage_sqlite`` - Code Coverage internal database (SQLite)
* ``codecoverage_json`` - Code Coverage JSON report
* ``codecoverage_xml`` - Code Coverage XML report
* ``codecoverage_html`` - Code Coverage HTML report
* ``statictyping_html`` - Static Type Checking HTML report
* ``package_all`` - Packaged Python project (multiple formats)
* ``documentation_pdf`` - Documentation in PDF format
* ``documentation_html`` - Documentation in HTML format

**Usage Example:**

.. code-block:: yaml

   jobs:
     Params:
       uses: pyTooling/Actions/.github/workflows/Parameters.yml@r5
       with:
         name: pyTooling

     Coverage:
       uses: pyTooling/Actions/.github/workflows/CoverageCollection.yml@dev
       needs:
         - Params
       with:
         artifact: ${{ fromJson(needs.Params.outputs.artifact_names).codecoverage_html }}


Params
======

.. attention:: ``Params`` is deprecated.

* ``params['unittesting']`` |rarr| ``artifact_names['unittesting_xml']``
* ``params['coverage']`` |rarr| ``artifact_names['codecoverage_xml']``
* ``params['typing']`` |rarr| ``artifact_names['statictyping_html']``
* ``params['package']`` |rarr| ``artifact_names['package_all']``
* ``params['doc']`` |rarr| ``artifact_names['documentation_html']``

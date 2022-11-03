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
       uses: pyTooling/Actions/.github/workflows/Parameters.yml@r0
       with:
         name: pyTooling

Complex Example
===============

The following instantiation example creates 3 jobs from the same template, but with differing input parameters. The
first job `UnitTestingParams` might be used to create a job matrix of unit tests. It creates the cross of default
systems (Windows, Ubuntu, MacOS, MinGW64) and the given list of Python versions including some mypy versions. In
addition a list of excludes (marked as :deletion:`deletions`) and includes (marked as :addition:`additions`) is handed
over resulting in the following combinations:

+------------+-------------+-------------+-------------+--------------+-------------------------+------------+-------------+------------------------------+------------------------------+
| Version    | 3.7 🔴      | 3.8 🟠      | 3.9 🟡      | 3.10 🟢      | 3.11 🟢                 | 3.12.a1 🟣 | pypy-3.7 🔴 | pypy-3.8 🟠                  | pypy-3.9 🟡                  |
+============+=============+=============+=============+==============+=========================+============+=============+==============================+==============================+
| Windows 🧊 | windows:3.7 | windows:3.8 | windows:3.9 | windows:3.10 |                         |            |             | :deletion:`windows:pypy-3.8` | :deletion:`windows:pypy-3.9` |
+------------+-------------+-------------+-------------+--------------+-------------------------+------------+-------------+------------------------------+------------------------------+
| Ubuntu 🐧  | ubuntu:3.7  | ubuntu:3.8  | ubuntu:3.9  | ubuntu:3.10  | :addition:`ubuntu:3.11` |            |             | ubuntu:pypy-3.8              | ubuntu:pypy-3.9              |
+------------+-------------+-------------+-------------+--------------+-------------------------+------------+-------------+------------------------------+------------------------------+
| MacOS 🍎   | macos:3.7   | macos:3.8   | macos:3.9   | macos:3.10   | :addition:`macos:3.11`  |            |             | macos:pypy-3.8               | macos:pypy-3.9               |
+------------+-------------+-------------+-------------+--------------+-------------------------+------------+-------------+------------------------------+------------------------------+
| MSYS 🟪    |             |             |             |              |                         |            |             |                              |                              |
+------------+-------------+-------------+-------------+--------------+-------------------------+------------+-------------+------------------------------+------------------------------+
| MinGW32 ⬛ |             |             |             |              |                         |            |             |                              |                              |
+------------+-------------+-------------+-------------+--------------+-------------------------+------------+-------------+------------------------------+------------------------------+
| MinGW64 🟦 |             |             |             | mingw64:3.10 |                         |            |             |                              |                              |
+------------+-------------+-------------+-------------+--------------+-------------------------+------------+-------------+------------------------------+------------------------------+
| Clang32 🟫 |             |             |             |              |                         |            |             |                              |                              |
+------------+-------------+-------------+-------------+--------------+-------------------------+------------+-------------+------------------------------+------------------------------+
| Clang64 🟧 |             |             |             |              |                         |            |             |                              |                              |
+------------+-------------+-------------+-------------+--------------+-------------------------+------------+-------------+------------------------------+------------------------------+
| UCRT64 🟨  |             |             |             |              |                         |            |             |                              |                              |
+------------+-------------+-------------+-------------+--------------+-------------------------+------------+-------------+------------------------------+------------------------------+


.. code-block:: yaml

   name: Pipeline

   on:
     push:
     workflow_dispatch:

   jobs:
     UnitTestingParams:
       uses: pyTooling/Actions/.github/workflows/Parameters.yml@r0
       with:
         name: pyTooling
         python_version_list: "3.7 3.8 3.9 3.10 pypy-3.8 pypy-3.9"
         include_list: "ubuntu:3.11 macos:3.11"
         exclude_list: "windows:pypy-3.8 windows:pypy-3.9"

     PerformanceTestingParams:
       uses: pyTooling/Actions/.github/workflows/Parameters.yml@r0
       with:
         name: pyTooling
         python_version_list: "3.10 3.11"
         system_list: "ubuntu windows macos"

     PlatformTestingParams:
       uses: pyTooling/Actions/.github/workflows/Parameters.yml@dev
       with:
         name: pyTooling
         python_version_list: "3.10"
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
| python_version | optional | string   | ``3.11`` |
+----------------+----------+----------+----------+

Python version to be used for all jobs requiring a single Python version.


python_version_list
===================

+----------------------+----------+----------+---------------------------+
| Parameter Name       | Required | Type     | Default                   |
+======================+==========+==========+===========================+
| python_version_list  | optional | string   | ``3.7 3.8 3.9 3.10 3.11`` |
+----------------------+----------+----------+---------------------------+

Space separated list of CPython versions and/or mypy version to run tests with.

**Possible values:**

* ``3.6``, ``3.7``, ``3.8``, ``3.9``, ``3.10`` , ``3.11``, ``3.12``
* ``pypy-3.7``, ``pypy-3.8``, ``pypy-3.9``

+------+-----------+------------------+-----------------------------------------+
| Icon | Version   | Maintained until | Comments                                |
+======+===========+==================+=========================================+
| ⚫   | 3.6       | 2021.12.23       | :red:`outdated`                         |
+------+-----------+------------------+-----------------------------------------+
| 🔴   | 3.7       | 2023.06.27       |                                         |
+------+-----------+------------------+-----------------------------------------+
| 🟠   | 3.8       | 2024.10          |                                         |
+------+-----------+------------------+-----------------------------------------+
| 🟡   | 3.9       | 2025.10          |                                         |
+------+-----------+------------------+-----------------------------------------+
| 🟢   | 3.10      | 2026.10          |                                         |
+------+-----------+------------------+-----------------------------------------+
| 🟢   | 3.11      | 2027.10          | :green:`latest`                         |
+------+-----------+------------------+-----------------------------------------+
| 🟣   | 3.12      | 2028.10          | Python 3.12 alpha (or RC) will be used. |
+------+-----------+------------------+-----------------------------------------+
| ⟲🔴  | pypy-3.7  | ????.??          |                                         |
+------+-----------+------------------+-----------------------------------------+
| ⟲🟠  | pypy-3.8  | ????.??          |                                         |
+------+-----------+------------------+-----------------------------------------+
| ⟲🟡  | pypy-3.9  | ????.??          |                                         |
+------+-----------+------------------+-----------------------------------------+


system_list
===========

+----------------+----------+----------+----------------------------------+
| Parameter Name | Required | Type     | Default                          |
+================+==========+==========+==================================+
| system_list    | optional | string   | ``ubuntu windows mingw64 macos`` |
+----------------+----------+----------+----------------------------------+

Space separated list of systems to run tests on.

**Possible values:**

* Native systems: ``ubuntu``, ``windows``, ``macos``
* MSYS2: ``msys``, ``mingw32``, ``mingw64``, ``clang32``, ``clang64``, ``ucrt64``

+------+-----------+------------------------------+-----------------------------------------------------------------+
| Icon | System    | Used version                 | Comments                                                        |
+======+===========+==============================+=================================================================+
| 🧊   | Windows   | Windows Server 2022 (latest) |                                                                 |
+------+-----------+------------------------------+-----------------------------------------------------------------+
| 🐧   | Ubuntu    | Ubuntu 20.04 (LTS) (latest)  | While this marked latest, Ubuntu 22.02 LTS is already provided. |
+------+-----------+------------------------------+-----------------------------------------------------------------+
| 🍎   | MacOS     | macOS Big Sur 11 (latest)    | While this marked latest, macOS Monterey 12 is already provided.|
+------+-----------+------------------------------+-----------------------------------------------------------------+
| 🟪   | MSYS      |                              |                                                                 |
+------+-----------+------------------------------+-----------------------------------------------------------------+
| ⬛   | MinGW32   |                              |                                                                 |
+------+-----------+------------------------------+-----------------------------------------------------------------+
| 🟦   | MinGW64   |                              |                                                                 |
+------+-----------+------------------------------+-----------------------------------------------------------------+
| 🟫   | Clang32   |                              |                                                                 |
+------+-----------+------------------------------+-----------------------------------------------------------------+
| 🟧   | Clang64   |                              |                                                                 |
+------+-----------+------------------------------+-----------------------------------------------------------------+
| 🟨   | UCRT64    |                              |                                                                 |
+------+-----------+------------------------------+-----------------------------------------------------------------+


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
variables. Thus, this job is used to compute an output parameter that can be reused in many other jobs.

**Usage Example:**

.. code-block:: yaml

   jobs:
     Params:
       uses: pyTooling/Actions/.github/workflows/Parameters.yml@r0
       with:
         name: pyTooling

     CodeCoverage:
       uses: pyTooling/Actions/.github/workflows/CoverageCollection.yml@r0
       needs:
         - Params
       with:
         python_version: ${{ needs.Params.outputs.python_version }}

python_jobs
===========

.. todo:: Parameters:python_jobs Needs documentation.

artifact_names
==============

.. todo:: Parameters:artifact_names Needs documentation.

Params
======

.. attention:: ``Params`` is deprecated.

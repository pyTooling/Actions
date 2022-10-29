Parameters
##########

The `Parameters` job template is a workaround for the limitations of GitHub Actions to handle global variables in
GitHub Actions workflows (see [actions/runner#480](https://github.com/actions/runner/issues/480)).

It generates output parameters with artifact names and a job matrix to be used in later running jobs.

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
addition a list of excludes (marked as :deletetion:`deletion`) and includes (marked as :additions:`additions`) is handed
over resulting in the following combinations:

+---------+-------------+-------------+-------------+--------------+-------------------------+---------+----------+------------------------------+------------------------------+
| Version | 3.7         | 3.8         | 3.9         | 3.10         | 3.11                    | 3.12.a1 | mypy-3.7 | mypy-3.8                     | mypy-3.9                     |
+=========+=============+=============+=============+==============+=========================+=========+==========+==============================+==============================+
| Windows | windows:3.7 | windows:3.8 | windows:3.9 | windows:3.10 |                         |         |          | :deletion:`windows:mypy-3.8` | :deletion:`windows:mypy-3.9` |
+---------+-------------+-------------+-------------+--------------+-------------------------+---------+----------+------------------------------+------------------------------+
| Ubuntu  | ubuntu:3.7  | ubuntu:3.8  | ubuntu:3.9  | ubuntu:3.10  | :addition:`ubuntu:3.11` |         |          | ubuntu:mypy-3.8              | ubuntu:mypy-3.9              |
+---------+-------------+-------------+-------------+--------------+-------------------------+---------+----------+------------------------------+------------------------------+
| MacOS   | macos:3.7   | macos:3.8   | macos:3.9   | macos:3.10   | :addition:`macos:3.11`  |         |          | macos:mypy-3.8               | macos:mypy-3.9               |
+---------+-------------+-------------+-------------+--------------+-------------------------+---------+----------+------------------------------+------------------------------+
| MSYS    |             |             |             |              |                         |         |          |                              |                              |
+---------+-------------+-------------+-------------+--------------+-------------------------+---------+----------+------------------------------+------------------------------+
| MinGW32 |             |             |             |              |                         |         |          |                              |                              |
+---------+-------------+-------------+-------------+--------------+-------------------------+---------+----------+------------------------------+------------------------------+
| MinGW64 |             |             |             | mingw64:3.10 |                         |         |          |                              |                              |
+---------+-------------+-------------+-------------+--------------+-------------------------+---------+----------+------------------------------+------------------------------+
| Clang32 |             |             |             |              |                         |         |          |                              |                              |
+---------+-------------+-------------+-------------+--------------+-------------------------+---------+----------+------------------------------+------------------------------+
| Clang64 |             |             |             |              |                         |         |          |                              |                              |
+---------+-------------+-------------+-------------+--------------+-------------------------+---------+----------+------------------------------+------------------------------+
| UCRT64  |             |             |             |              |                         |         |          |                              |                              |
+---------+-------------+-------------+-------------+--------------+-------------------------+---------+----------+------------------------------+------------------------------+



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

Template Parameters
*******************

Name
======
The name of the library or package.

 It's used to create artifact names.


python_version_list
===================

TBD


system_list
===========

TBD


include_list
============

TBD

exclude_list
============

TBD

Template Results
****************

Params
======


Jobs
====




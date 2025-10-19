.. _JOBTMPL/Parameters:
.. index::
   single: GitHub Action Reusable Workflow; Parameters Template

Parameters
##########

The ``Parameters`` job template is a workaround for the limitations of GitHub Actions to handle global variables in
GitHub Actions workflows (see `actions/runner#480 <https://github.com/actions/runner/issues/480>`__).

It generates output parameters containing a list of artifact names and a job matrix to be used in later-running jobs.

.. topic:: Features

   * Generate artifact names for various artifacts.
   * Generate a matrix of job combinations as a JSON string made from:

     * systems (Ubuntu, macOS, Windows)
     * architecture (x64-64, aarch64)
     * Python versions (3.9, 3.10, ..., 3.13),
     * Python implementation (CPython, PyPy), and
     * environments (Native, MinGW64, UCRT64, ...).

   * Provide a (default) Python version for other jobs.

.. topic:: Behavior

   1. Delay job execution by :ref:`JOBTMPL/Parameters/Input/pipeline-delay` seconds.
   2. Compute job matrix using an embedded Python script.
   3. Assemble artifact names using a common prefix derived from Python namespace and package name.

.. topic:: Job Execution

   .. image:: ../../_static/pyTooling-Actions-Parameters.png
      :width: 1000px

.. topic:: Dependencies

   * Python from base-system.


.. _JOBTMPL/Parameters/Instantiation:

Instantiation
*************

Simple Example
==============

.. grid:: 2

   .. grid-item::
      :columns: 5

      The following instantiation example creates a ``Params`` job derived from job template ``Parameters`` version
      ``@r6``. It only requires a :ref:`JOBTMPL/Parameters/Input/package_name` parameter to create the artifact names.

   .. grid-item::
      :columns: 7

      .. code-block:: yaml

         jobs:
           Params:
             uses: pyTooling/Actions/.github/workflows/Parameters.yml@r6
             with:
               package_name: myPackage

           UnitTesting:
             uses: pyTooling/Actions/.github/workflows/UnitTesting.yml@r6
             needs:
               - Params
             with:
               jobs: ${{ needs.Params.outputs.python_jobs }}

Complex Example
===============

.. grid:: 2

   .. grid-item::
      :columns: 5

      The following instantiation example creates 3 jobs from the same template, but with differing input parameters.

      The first ``UnitTestingParams`` job might be used to create a job matrix of unit tests. It creates the cross of
      default systems (Windows, Ubuntu, macOS, macOS-ARM, MinGW64, UCRT64) and the given list of Python versions
      including some mypy versions. In addition a list of excludes (marked as :deletion:`deletions`) and includes
      (marked as :addition:`additions`) is handed over resulting in the following combinations.

      The second ``PerformanceTestingParams`` job might be used to create a job matrix for performance tests. Here a
      pipeline might be limited to the latest two Python versions on a selected list of platforms.

      The third ``PlatformTestingParams`` job might be used to create a job matrix for platform compatibility tests.
      Here a pipeline might be limited to the latest Python version, but all available platforms.

   .. grid-item::
      :columns: 7

      .. code-block:: yaml

         jobs:
           UnitTestingParams:
             uses: pyTooling/Actions/.github/workflows/Parameters.yml@r6
             with:
               package_namespace:   myFramework
               package_name:        Extension
               python_version_list: '3.9 3.10 3.11 3.12 pypy-3.10 pypy-3.11'
               system_list:         'ubuntu windows macos macos-arm mingw64 ucrt64'
               include_list:        'ubuntu:3.13 macos:3.13 macos-arm:3.13'
               exclude_list:        'windows:pypy-3.10 windows:pypy-3.11'

           PerformanceTestingParams:
             uses: pyTooling/Actions/.github/workflows/Parameters.yml@r6
             with:
               package_namespace:   myFramework
               package_name:        Extension
               python_version_list: '3.12 3.13'
               system_list:         'ubuntu windows macos macos-arm'

           PlatformTestingParams:
             uses: pyTooling/Actions/.github/workflows/Parameters.yml@r6
             with:
               package_namespace:   myFramework
               package_name:        Extension
               python_version_list: '3.13'
               system_list:         'ubuntu windows macos macos-arm mingw32 mingw64 clang64 ucrt64'

+--------------------------------+----------------+-----------------+-----------------+-----------------+----------------------------+------------+-------------+-------------------------------+-------------------------------+
| Version                        | 3.9 🔴         | 3.10 🟠         | 3.11 🟡         |    3.12 🟢      | 3.13 🟢                    | 3.14.b1 🟣 | pypy-3.9 🔴 | pypy-3.10 🟠                  | pypy-3.11 🟡                  |
+================================+================+=================+=================+=================+============================+============+=============+===============================+===============================+
| Ubuntu 🐧                      | ubuntu:3.9     | ubuntu:3.10     | ubuntu:3.11     | ubuntu:3.12     | :addition:`ubuntu:3.13`    |            |             | ubuntu:pypy-3.10              | ubuntu:pypy-3.11              |
+--------------------------------+----------------+-----------------+-----------------+-----------------+----------------------------+------------+-------------+-------------------------------+-------------------------------+
| macOS (x86-64) 🍎              | macos:3.9      | macos:3.10      | macos:3.11      | macos:3.12      | :addition:`macos:3.13`     |            |             | macos:pypy-3.10               | macos:pypy-3.11               |
+--------------------------------+----------------+-----------------+-----------------+-----------------+----------------------------+------------+-------------+-------------------------------+-------------------------------+
| macOS (aarch64) 🍏             | macos-arm:3.9  | macos-arm:3.10  | macos-arm:3.11  | macos-arm:3.12  | :addition:`macos-arm:3.13` |            |             | macos:pypy-3.10               | macos:pypy-3.11               |
+--------------------------------+----------------+-----------------+-----------------+-----------------+----------------------------+------------+-------------+-------------------------------+-------------------------------+
| Windows Server 🪟              | windows:3.9    | windows:3.10    | windows:3.11    | windows:3.12    |                            |            |             | :deletion:`windows:pypy-3.10` | :deletion:`windows:pypy-3.11` |
+--------------------------------+----------------+-----------------+-----------------+-----------------+----------------------------+------------+-------------+-------------------------------+-------------------------------+
| Windows Server 🪟 + MSYS 🟪    |                |                 |                 |                 |                            |            |             |                               |                               |
+--------------------------------+----------------+-----------------+-----------------+-----------------+----------------------------+------------+-------------+-------------------------------+-------------------------------+
| Windows Server 🪟 + MinGW32 ⬛ |                |                 |                 |                 |                            |            |             |                               |                               |
+--------------------------------+----------------+-----------------+-----------------+-----------------+----------------------------+------------+-------------+-------------------------------+-------------------------------+
| Windows Server 🪟 + MinGW64 🟦 |                |                 |                 | mingw64:3.12    |                            |            |             |                               |                               |
+--------------------------------+----------------+-----------------+-----------------+-----------------+----------------------------+------------+-------------+-------------------------------+-------------------------------+
| Windows Server 🪟 + Clang32 🟫 |                |                 |                 |                 |                            |            |             |                               |                               |
+--------------------------------+----------------+-----------------+-----------------+-----------------+----------------------------+------------+-------------+-------------------------------+-------------------------------+
| Windows Server 🪟 + Clang64 🟧 |                |                 |                 |                 |                            |            |             |                               |                               |
+--------------------------------+----------------+-----------------+-----------------+-----------------+----------------------------+------------+-------------+-------------------------------+-------------------------------+
| Windows Server 🪟 + UCRT64 🟨  |                |                 |                 | ucrt64:3.12     |                            |            |             |                               |                               |
+--------------------------------+----------------+-----------------+-----------------+-----------------+----------------------------+------------+-------------+-------------------------------+-------------------------------+


.. _JOBTMPL/Parameters/Parameters:

Parameter Summary
*****************

.. rubric:: Goto :ref:`input parameters <JOBTMPL/Parameters/Inputs>`

+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| Parameter Name                                                      | Required | Type     | Default                                                           |
+=====================================================================+==========+==========+===================================================================+
| :ref:`JOBTMPL/Parameters/Input/ubuntu_image_version`                | no       | string   | ``'24.04'``                                                       |
+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/Parameters/Input/name`                                | no       | string   | ``''``                                                            |
+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/Parameters/Input/package_namespace`                   | no       | string   | ``''``                                                            |
+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/Parameters/Input/package_name`                        | no       | string   | ``''``                                                            |
+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/Parameters/Input/python_version`                      | no       | string   | ``'3.14'``                                                        |
+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/Parameters/Input/python_version_list`                 | no       | string   | ``'3.10 3.11 3.12 3.13 3.14'``                                    |
+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/Parameters/Input/system_list`                         | no       | string   | ``'ubuntu windows macos macos-arm mingw64 ucrt64'``               |
+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/Parameters/Input/include_list`                        | no       | string   | ``''``                                                            |
+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/Parameters/Input/exclude_list`                        | no       | string   | ``'windows-arm:3.9 windows-arm:3.10'``                            |
+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/Parameters/Input/disable_list`                        | no       | string   | ``'windows-arm:pypy-3.10 windows-arm:pypy-3.11'``                 |
+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/Parameters/Input/ubuntu_image`                        | no       | string   | ``'ubuntu-24.04'``                                                |
+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/Parameters/Input/ubuntu_arm_image`                    | no       | string   | ``'ubuntu-24.04-arm'``                                            |
+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/Parameters/Input/windows_image`                       | no       | string   | ``'windows-2025'``                                                |
+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/Parameters/Input/windows_arm_image`                   | no       | string   | ``'windows-11-arm'``                                              |
+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/Parameters/Input/macos_intel_image`                   | no       | string   | ``'macos-13'``                                                    |
+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/Parameters/Input/macos_arm_image`                     | no       | string   | ``'macos-15'``                                                    |
+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/Parameters/Input/pipeline-delay`                      | no       | number   | ``0``                                                             |
+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+

.. rubric:: Goto :ref:`secrets <JOBTMPL/Parameters/Secrets>`

This job template needs no secrets.

.. rubric:: Goto :ref:`output parameters <JOBTMPL/Parameters/Outputs>`

+---------------------------------------------------------------------+----------------+-------------------------------------------------------------------+
| Result Name                                                         | Type           | Description                                                       |
+=====================================================================+================+===================================================================+
| :ref:`JOBTMPL/Parameters/Output/python_version`                     | string         |                                                                   |
+---------------------------------------------------------------------+----------------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/Parameters/Output/package_fullname`                   | string         |                                                                   |
+---------------------------------------------------------------------+----------------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/Parameters/Output/package_directory`                  | string         |                                                                   |
+---------------------------------------------------------------------+----------------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/Parameters/Output/artifact_basename`                  | string         |                                                                   |
+---------------------------------------------------------------------+----------------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/Parameters/Output/artifact_names`                     | string (JSON)  |                                                                   |
+---------------------------------------------------------------------+----------------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/Parameters/Output/python_jobs`                        | string (JSON)  |                                                                   |
+---------------------------------------------------------------------+----------------+-------------------------------------------------------------------+


.. _JOBTMPL/Parameters/Inputs:

Input Parameters
****************

.. _JOBTMPL/Parameters/Input/ubuntu_image_version:

.. include:: ../_ubuntu_image_version.rst


.. _JOBTMPL/Parameters/Input/name:

name
====

:Type:            string
:Required:        no
:Default Value:   ``''``
:Possible Values: Any valid artifact name.
:Description:     Prefix used to generate artifact names. Usually, the name of the Python package. |br|
                  In case this parameter is an empty string, the artifact prefix is derived from :ref:`JOBTMPL/Parameters/Input/package_name`
                  if the package is a simple Python package, **or** from :ref:`JOBTMPL/Parameters/Input/package_namespace`
                  and :ref:`JOBTMPL/Parameters/Input/package_name`, if the package is a Python namespace package.


.. _JOBTMPL/Parameters/Input/package_namespace:

package_namespace
=================

:Type:            string
:Required:        no
:Default Value:   ``''``
:Possible Values: Any valid Python namespace.
:Description:     In case the package is a Python namespace package, the name of the library's or package's namespace
                  needs to be specified using this parameter. |br|
                  In case of a simple Python package, this parameter must be specified as an empty string (``''``),
                  which is the default. |br|
                  This parameter is used to derive :ref:`JOBTMPL/Parameters/Input/name`, if it's an empty string.
:Example:
                  .. grid:: 2

                     .. grid-item::
                        :columns: 5

                        .. rubric:: Example Instantiation

                        .. code-block:: yaml

                           name: Pipeline

                           jobs:
                             ConfigParams:
                               uses: pyTooling/Actions/.github/workflows/Parameters.yml@r6
                               with:
                                 package_namespace: myFramework
                                 package_name:      Extension

                     .. grid-item::
                        :columns: 4

                        .. rubric:: Example Directory Structure

                        .. code-block::

                           📂ProjectRoot/
                             📂myFramework/
                               📂Extension/
                                 📦SubPackage/
                                   🐍__init__.py
                                   🐍SubModuleA.py
                                 🐍__init__.py
                                 🐍ModuleB.py


.. _JOBTMPL/Parameters/Input/package_name:

package_name
============

:Type:            string
:Required:        no
:Default Value:   ``''``
:Possible Values: Any valid Python package name.
:Description:     In case of a simple Python package, this package's name is specified using this parameter. |br|
                  In case the package is a Python namespace package, the parameter
                  :ref:`JOBTMPL/Parameters/Input/package_namespace` must be specified, too. |br|
                  This parameter is used to derive :ref:`JOBTMPL/Parameters/Input/name`, if it's an empty string.
:Example:
                  .. grid:: 2

                     .. grid-item::
                        :columns: 5

                        .. rubric:: Example Instantiation

                        .. code-block:: yaml

                           name: Pipeline

                           jobs:
                             ConfigParams:
                               uses: pyTooling/Actions/.github/workflows/Parameters.yml@r6
                               with:
                                 package_name: myPackage

                     .. grid-item::
                        :columns: 4

                        .. rubric:: Example Directory Structure

                        .. code-block::

                           📂ProjectRoot/
                             📂myFramework/
                               📦SubPackage/
                                 🐍__init__.py
                                 🐍SubModuleA.py
                               🐍__init__.py
                               🐍ModuleB.py


.. _JOBTMPL/Parameters/Input/python_version:

python_version
==============

:Type:            string
:Required:        no
:Default Value:   ``'3.14'``
:Possible Values: Any valid Python version conforming to the pattern ``<major>.<minor>`` or ``pypy-<major>.<minor>``. |br|
                  See `actions/python-versions - available Python versions <https://github.com/actions/python-versions>`__
                  and `actions/setup-python - configurable Python versions <https://github.com/actions/setup-python>`__.
:Description:     Python version used as default for other jobs requiring a single Python version. |br|
                  In case :ref:`JOBTMPL/Parameters/Input/python_version_list` is an empty string, this version is used
                  to populate the version list.


.. _JOBTMPL/Parameters/Input/python_version_list:

python_version_list
===================

:Type:            string
:Required:        no
:Default Value:   ``'3.10 3.11 3.12 3.13 3.14'``
:Possible Values: A space separated list of valid Python versions conforming to the pattern ``<major>.<minor>`` or
                  ``pypy-<major>.<minor>``. |br|
                  See `actions/python-versions - available Python versions <https://github.com/actions/python-versions>`__
                  and `actions/setup-python - configurable Python versions <https://github.com/actions/setup-python>`__.
:Description:     The list of space-separated Python versions used for Python variation testing.

                  .. include:: ../PythonVersionList.rst


.. _JOBTMPL/Parameters/Input/system_list:

system_list
===========

:Type:            string
:Required:        no
:Default Value:   ``'ubuntu windows macos macos-arm mingw64 ucrt64'``
:Possible Values: A space separated list of system names.
:Description:     The list of space-separated systems used for application testing.

                  .. include:: ../SystemList.rst


.. _JOBTMPL/Parameters/Input/include_list:

include_list
============

:Type:            string
:Required:        no
:Default Value:   ``''``
:Possible Values: A space separated list of ``<system>:<python_version>`` tuples.
:Description:     List of space-separated ``<system>:<python_version>`` tuples to be included into the list of test
                  variants.
:Example:
                  .. code-block:: yaml

                     jobs:
                       ConfigParams:
                         uses: pyTooling/Actions/.github/workflows/Parameters.yml@r6
                         with:
                           package_name: myPackage
                           include_list: "ubuntu:3.11 macos:3.11"


.. _JOBTMPL/Parameters/Input/exclude_list:

exclude_list
============

:Type:            string
:Required:        no
:Default Value:   ``'windows-arm:3.9 windows-arm:3.10'``
:Possible Values: A space separated list of ``<system>:<python_version>`` tuples.
:Description:     List of space-separated ``<system>:<python_version>`` tuples to be excluded from the list of test
                  variants.
:Example:
                  .. code-block:: yaml

                     jobs:
                       ConfigParams:
                         uses: pyTooling/Actions/.github/workflows/Parameters.yml@r6
                         with:
                           package_name: myPackage
                           exclude_list: "windows:pypy-3.8 windows:pypy-3.9"


.. _JOBTMPL/Parameters/Input/disable_list:

disable_list
============

:Type:            string
:Required:        no
:Default Value:   ``'windows-arm:pypy-3.10 windows-arm:pypy-3.11'``
:Possible Values: A space separated list of ``<system>:<python_version>`` tuples.
:Description:     List of space-separated ``<system>:<python_version>`` tuples to be temporarily disabled from the list
                  of test variants. |br|
                  Each disabled item creates a warning in the workflow log.
:Warning Example:
                  .. code-block:: yaml

                     jobs:
                       ConfigParams:
                         uses: pyTooling/Actions/.github/workflows/Parameters.yml@r6
                         with:
                           package_name: myPackage
                           disable_list: "windows:3.10 windows:3.11"

                  .. image:: ../../_static/GH_Workflow_DisabledJobsWarnings.png
                     :width: 400px


.. _JOBTMPL/Parameters/Input/ubuntu_image:

ubuntu_image
============

:Type:            string
:Required:        no
:Default Value:   ``'ubuntu-24.04'``
:Possible Values: See `actions/runner-images - Available Images <https://github.com/actions/runner-images?tab=readme-ov-file#available-images>`__
                  for available Ubuntu image versions.
:Description:     Name of the Ubuntu x86-64 image and version used to run a Ubuntu jobs when selected via :ref:`JOBTMPL/Parameters/Input/system_list`.


.. _JOBTMPL/Parameters/Input/ubuntu_arm_image:

ubuntu_arm_image
================

:Type:            string
:Required:        no
:Default Value:   ``'ubuntu-24.04-arm'``
:Possible Values: See `actions/partner-runner-images - Available Images <https://github.com/actions/partner-runner-images?tab=readme-ov-file#available-images>`__
                  for available Ubuntu ARM image versions.
:Description:     Name of the Ubuntu aarch64 image and version used to run a Ubuntu ARM jobs when selected via :ref:`JOBTMPL/Parameters/Input/system_list`.


.. _JOBTMPL/Parameters/Input/windows_image:

windows_image
=============

:Type:            string
:Required:        no
:Default Value:   ``'windows-2025'``
:Possible Values: See `actions/runner-images - Available Images <https://github.com/actions/runner-images?tab=readme-ov-file#available-images>`__
:Description:     Name of the Windows Server x86-64 image and version used to run a Windows jobs when selected via :ref:`JOBTMPL/Parameters/Input/system_list`.


.. _JOBTMPL/Parameters/Input/windows_arm_image:

windows_arm_image
=================

:Type:            string
:Required:        no
:Default Value:   ``'windows-11-arm'``
:Possible Values: See `actions/partner-runner-images - Available Images <https://github.com/actions/partner-runner-images?tab=readme-ov-file#available-images>`__
:Description:     Name of the Windows aarch64 image and version used to run a Windows ARM jobs when selected via :ref:`JOBTMPL/Parameters/Input/system_list`.


.. _JOBTMPL/Parameters/Input/macos_intel_image:

macos_intel_image
=================

:Type:            string
:Required:        no
:Default Value:   ``'macos-13'``
:Possible Values: See `actions/runner-images - Available Images <https://github.com/actions/runner-images?tab=readme-ov-file#available-images>`__
:Description:     Name of the macOS x86-64 image and version used to run a macOS Intel jobs when selected via :ref:`JOBTMPL/Parameters/Input/system_list`.


.. _JOBTMPL/Parameters/Input/macos_arm_image:

macos_arm_image
===============

:Type:            string
:Required:        no
:Default Value:   ``'macos-15'``
:Possible Values: See `actions/runner-images - Available Images <https://github.com/actions/runner-images?tab=readme-ov-file#available-images>`__
:Description:     Name of the macOS aarch64 image and version used to run a macOS ARM jobs when selected via :ref:`JOBTMPL/Parameters/Input/system_list`.


.. _JOBTMPL/Parameters/Input/pipeline-delay:

pipeline-delay
==============

:Type:            number
:Required:        no
:Default Value:   ``0``
:Possible Values: Any integer number.
:Description:     Slow down this job, to delay the startup of the GitHub Action pipline.


.. _JOBTMPL/Parameters/Secrets:

Secrets
*******

This job template needs no secrets.


.. _JOBTMPL/Parameters/Outputs:

Outputs
*******

.. _JOBTMPL/Parameters/Output/python_version:

python_version
==============

:Type:            string
:Default Value:   ``'3.14'``
:Possible Values: Any valid Python version conforming to the pattern ``<major>.<minor>`` or ``pypy-<major>.<minor>``.
:Description:     Returns

                  A single string parameter representing the default Python version that should be used across multiple jobs in the same
                  pipeline.

                  Such a parameter is needed as a workaround, because GitHub Actions doesn't support proper handling of global pipeline
                  variables. Thus, this job is used to compute an output parameter that can be reused in other jobs.
:Example:
                  .. code-block:: yaml

                     jobs:
                       Params:
                         uses: pyTooling/Actions/.github/workflows/Parameters.yml@r6
                         with:
                           name: pyTooling

                       CodeCoverage:
                         uses: pyTooling/Actions/.github/workflows/CoverageCollection.yml@r6
                         needs:
                           - Params
                         with:
                           python_version: ${{ needs.Params.outputs.python_version }}


.. _JOBTMPL/Parameters/Output/package_fullname:

package_fullname
================

:Type:            string
:Description:     Returns the full package name composed from :ref:`JOBTMPL/Parameters/Input/package_namespace`
                  and :ref:`JOBTMPL/Parameters/Input/package_name`.
:Example:         ``myFramework.Extension``


.. _JOBTMPL/Parameters/Output/package_directory:

package_directory
=================

:Type:            string
:Description:     Returns the full package path composed from :ref:`JOBTMPL/Parameters/Input/package_namespace`
                  and :ref:`JOBTMPL/Parameters/Input/package_name`.
:Example:         ``myFramework/Extension``


.. _JOBTMPL/Parameters/Output/artifact_basename:

artifact_basename
=================

:Type:            string
:Description:     Returns the basename (prefix) of all :ref:`artifact names <JOBTMPL/Parameters/Output/artifact_names>` |br|.
                  The basename is either :ref:`JOBTMPL/Parameters/Input/name` if set, otherwise its
                  :ref:`JOBTMPL/Parameters/Output/package_fullname`.
:Example:         ``myFramework.Extension``


.. _JOBTMPL/Parameters/Output/artifact_names:

artifact_names
==============

:Type:            string (JSON)
:Description:     Returns a JSON dictionary of artifact names sharing a common prefix (see :ref:`JOBTMPL/Parameters/Input/name`). |br|
                  As artifacts are handed from jo to job, a consistent naming scheme is advised to avoid duplications
                  and naming artifacts by hand. This technique solves again the problem of global variables in GitHub
                  Action YAMl files and the need for assigning the same value (here artifact name) to multiple jobs
                  templates.

                  The supported artifacts are:

                  :unittesting_xml:        UnitTesting XML summary report
                  :unittesting_html:       UnitTesting HTML summary report
                  :perftesting_xml:        PerformanceTesting XML summary report
                  :benchtesting_xml:       Benchmarking XML summary report
                  :apptesting_xml:         ApplicationTesting XML summary report
                  :codecoverage_sqlite:    Code Coverage internal database (SQLite)
                  :codecoverage_xml:       Code Coverage Cobertura XML report
                  :codecoverage_json:      Code Coverage Coverage.py JSON report
                  :codecoverage_html:      Code Coverage HTML report
                  :statictyping_cobertura: Static Type Checking Cobertura XML report
                  :statictyping_junit:     Static Type Checking JUnit XML report
                  :statictyping_html:      Static Type Checking HTML report
                  :package_all:            Packaged Python project (multiple formats)
                  :documentation_html:     Documentation in HTML format
                  :documentation_latex:    Documentation in LaTeX format
                  :documentation_pdf:      Documentation in PDF format
:Example:
                  .. code-block:: yaml

                     jobs:
                       Params:
                         uses: pyTooling/Actions/.github/workflows/Parameters.yml@r6
                         with:
                           name: pyTooling

                       Coverage:
                         uses: pyTooling/Actions/.github/workflows/UnitTesting.yml@r6
                         needs:
                           - Params
                         with:
                           unittest_xml_artifact: ${{ fromJson(needs.Params.outputs.artifact_names).unittesting_xml }}


.. _JOBTMPL/Parameters/Output/python_jobs:

python_jobs
===========

:Type:            string (JSON)
:Description:     Returns a JSON array of job descriptions, wherein each job description is a dictionary providing the
                  following key-value pairs:

                  :sysicon: icon to display
                  :system:  name of the system
                  :runs-on: virtual machine image and base operating system
                  :runtime: name of the runtime environment if not running natively on the VM image
                  :shell:   name of the shell
                  :pyicon:  icon for CPython or pypy
                  :python:  Python version
                  :envname: full name of the selected environment
:Example:
                  .. code-block:: yaml

                     jobs:
                       Params:
                         uses: pyTooling/Actions/.github/workflows/Parameters.yml@r6
                         with:
                           name: pyDummy

                       UnitTesting:
                         uses: pyTooling/Actions/.github/workflows/UnitTesting.yml@r6
                         needs:
                           - Params
                         with:
                           jobs: ${{ needs.Params.outputs.python_jobs }}
:Usage:           The generated JSON array can be unpacked using the ``fromJson(...)`` function in a job's matrix
                  ``strategy:matrix:include`` like this:

                  .. code-block:: yaml

                     name: Unit Testing (Matrix)

                     on:
                       workflow_call:
                         inputs:
                           jobs:
                             required: true
                             type: string

                     jobs:
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
:Debugging:       The job prints debugging information like system |times| Python version |times| environment
                  combinations as well as the generated JSON array in the job's log.

                  .. code-block:: json

                     [
                       {"sysicon": "🐧",  "system": "ubuntu",   "runs-on": "ubuntu-24.04",  "runtime": "native",  "shell": "bash",      "pyicon": "🔴", "python": "3.9",  "envname": "Linux (x86-64)"                 },
                       {"sysicon": "🐧",  "system": "ubuntu",   "runs-on": "ubuntu-24.04",  "runtime": "native",  "shell": "bash",      "pyicon": "🟠", "python": "3.10", "envname": "Linux (x86-64)"                 },
                       {"sysicon": "🐧",  "system": "ubuntu",   "runs-on": "ubuntu-24.04",  "runtime": "native",  "shell": "bash",      "pyicon": "🟡", "python": "3.11", "envname": "Linux (x86-64)"                 },
                       {"sysicon": "🐧",  "system": "ubuntu",   "runs-on": "ubuntu-24.04",  "runtime": "native",  "shell": "bash",      "pyicon": "🟢", "python": "3.12", "envname": "Linux (x86-64)"                 },
                       {"sysicon": "🐧",  "system": "ubuntu",   "runs-on": "ubuntu-24.04",  "runtime": "native",  "shell": "bash",      "pyicon": "🟢", "python": "3.13", "envname": "Linux (x86-64)"                 },
                       {"sysicon": "🪟",  "system": "windows",   "runs-on": "windows-2025", "runtime": "native",  "shell": "pwsh",      "pyicon": "🔴", "python": "3.9",  "envname": "Windows (x86-64)"               },
                       {"sysicon": "🪟",  "system": "windows",   "runs-on": "windows-2025", "runtime": "native",  "shell": "pwsh",      "pyicon": "🟠", "python": "3.10", "envname": "Windows (x86-64)"               },
                       {"sysicon": "🪟",  "system": "windows",   "runs-on": "windows-2025", "runtime": "native",  "shell": "pwsh",      "pyicon": "🟡", "python": "3.11", "envname": "Windows (x86-64)"               },
                       {"sysicon": "🪟",  "system": "windows",   "runs-on": "windows-2025", "runtime": "native",  "shell": "pwsh",      "pyicon": "🟢", "python": "3.12", "envname": "Windows (x86-64)"               },
                       {"sysicon": "🪟",  "system": "windows",   "runs-on": "windows-2025", "runtime": "native",  "shell": "pwsh",      "pyicon": "🟢", "python": "3.13", "envname": "Windows (x86-64)"               },
                       {"sysicon": "🍎",  "system": "macos",     "runs-on": "macos-13",     "runtime": "native",  "shell": "bash",      "pyicon": "🔴", "python": "3.9",  "envname": "macOS (x86-64)"                  },
                       {"sysicon": "🍎",  "system": "macos",     "runs-on": "macos-13",     "runtime": "native",  "shell": "bash",      "pyicon": "🟠", "python": "3.10", "envname": "macOS (x86-64)"                  },
                       {"sysicon": "🍎",  "system": "macos",     "runs-on": "macos-13",     "runtime": "native",  "shell": "bash",      "pyicon": "🟡", "python": "3.11", "envname": "macOS (x86-64)"                  },
                       {"sysicon": "🍎",  "system": "macos",     "runs-on": "macos-13",     "runtime": "native",  "shell": "bash",      "pyicon": "🟢", "python": "3.12", "envname": "macOS (x86-64)"                  },
                       {"sysicon": "🍎",  "system": "macos",     "runs-on": "macos-13",     "runtime": "native",  "shell": "bash",      "pyicon": "🟢", "python": "3.13", "envname": "macOS (x86-64)"                  },
                       {"sysicon": "🍏",  "system": "macos-arm", "runs-on": "macos-15",     "runtime": "native",  "shell": "bash",      "pyicon": "🔴", "python": "3.9",  "envname": "macOS (aarch64)"                 },
                       {"sysicon": "🍏",  "system": "macos-arm", "runs-on": "macos-15",     "runtime": "native",  "shell": "bash",      "pyicon": "🟠", "python": "3.10", "envname": "macOS (aarch64)"                 },
                       {"sysicon": "🍏",  "system": "macos-arm", "runs-on": "macos-15",     "runtime": "native",  "shell": "bash",      "pyicon": "🟡", "python": "3.11", "envname": "macOS (aarch64)"                 },
                       {"sysicon": "🍏",  "system": "macos-arm", "runs-on": "macos-15",     "runtime": "native",  "shell": "bash",      "pyicon": "🟢", "python": "3.12", "envname": "macOS (aarch64)"                 },
                       {"sysicon": "🍏",  "system": "macos-arm", "runs-on": "macos-15",     "runtime": "native",  "shell": "bash",      "pyicon": "🟢", "python": "3.13", "envname": "macOS (aarch64)"                 },
                       {"sysicon": "🪟🟦", "system": "msys2",    "runs-on": "windows-2025", "runtime": "MINGW64", "shell": "msys2 {0}", "pyicon": "🟢", "python": "3.12", "envname": "Windows+MSYS2 (x86-64) - MinGW64"},
                       {"sysicon": "🪟🟨", "system": "msys2",    "runs-on": "windows-2025", "runtime": "UCRT64",  "shell": "msys2 {0}", "pyicon": "🟢", "python": "3.12", "envname": "Windows+MSYS2 (x86-64) - UCRT64" }
                     ]


.. _JOBTMPL/Parameters/Optimizations:

Optimizations
*************

This template offers no optimizations (reduced job runtime).

Nontheless, the generated output :ref:`JOBTMPL/Parameters/Output/python_jobs` is influenced by many input parameters
generating :math:`N^2` many Python job combinations, which in turn will influence the overall pipeline runtime and how many
jobs (parallel VMs) are needed to execute the matrix.

.. hint::

   Some VM images (macOS, Windows) have parallelism limitations and run slower then Ubuntu-based jobs. Additionally,
   environments like MSYS2 require an additional setup time increasing a jobs runtime significantly.

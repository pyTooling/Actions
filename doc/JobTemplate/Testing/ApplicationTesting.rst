.. _JOBTMPL/ApplicationTesting:
.. index::
   single: pytest; ApplicationTesting Template
   single: GitHub Action Reusable Workflow; ApplicationTesting Template

ApplicationTesting
##################

The ``ApplicationTesting`` job template runs tests against the **packaged and installed** Python package, on a matrix
of Python versions and systems. It is the counterpart of :ref:`JOBTMPL/UnitTesting`, which runs tests against the
sources in the repository.

The distinction matters, because the two find different defects. Unit testing imports the package from the checked out
working directory, so it passes even when a module is missing from the wheel, an entry point is misspelled or a
:file:`py.typed` marker was never packaged. Application testing downloads the wheel artifact produced by
:ref:`JOBTMPL/Package`, installs it with :term:`pip` and runs the tests from :file:`tests/app` against that
installation.

Configuration options for :term:`pytest` should be given via section ``[tool.pytest.ini_options]`` in a
:file:`pyproject.toml` file.

.. topic:: Features

   * Run application tests from a job matrix crossing Python versions and systems.
   * Install the package under test from the wheel artifact instead of from the sources.
   * Install system dependencies via *apt*, *homebrew* or *pacboy* and Python dependencies via *pip*.
   * Run user defined scripts per system before the tests are started.
   * Optionally upload the test report summary in JUnit XML format as an artifact.

.. topic:: Behavior

   1. Checkout repository.
   2. Install system dependencies (:ref:`JOBTMPL/ApplicationTesting/Input/apt`,
      :ref:`JOBTMPL/ApplicationTesting/Input/brew`, :ref:`JOBTMPL/ApplicationTesting/Input/pacboy`).
   3. Prepare the Python environment as described by the matrix entry
      (:ref:`JOBTMPL/ApplicationTesting/Input/jobs`) and install the Python dependencies using :term:`pip`
      (:ref:`JOBTMPL/ApplicationTesting/Input/requirements`,
      :ref:`JOBTMPL/ApplicationTesting/Input/mingw_requirements`).
   4. Run the instructions given by the ``*_before_script`` parameter of the current system, e.g.
      :ref:`JOBTMPL/ApplicationTesting/Input/ubuntu_before_script`.
   5. Download the wheel artifact (:ref:`JOBTMPL/ApplicationTesting/Input/wheel`).
   6. Install the wheel using :term:`pip`.
   7. Run the application tests using :term:`pytest` (:ref:`JOBTMPL/ApplicationTesting/Input/apptest_directory`,
      :ref:`JOBTMPL/ApplicationTesting/Input/tests_directory`,
      :ref:`JOBTMPL/ApplicationTesting/Input/root_directory`).
   8. Upload the test report summary as an artifact (:ref:`JOBTMPL/ApplicationTesting/Input/apptest_xml_artifact`,
      :ref:`JOBTMPL/ApplicationTesting/Input/apptest_report_xml`).

   .. note::

      Steps 5 and 6 are what separates this template from :ref:`JOBTMPL/UnitTesting`. Because the package is installed
      from the wheel, the job must run after :ref:`JOBTMPL/Package`.

.. topic:: Dependencies

   * :gh:`actions/checkout`
   * :gh:`msys2/setup-msys2`
   * :gh:`actions/setup-python`
   * :gh:`pyTooling/download-artifact`

     * :gh:`actions/download-artifact`

   * :gh:`pyTooling/upload-artifact`

     * :gh:`actions/upload-artifact`

   * apt: Packages specified via :ref:`JOBTMPL/ApplicationTesting/Input/apt` parameter.
   * homebrew: Packages specified via :ref:`JOBTMPL/ApplicationTesting/Input/brew` parameter.
   * MSYS2: Packages specified via :ref:`JOBTMPL/ApplicationTesting/Input/pacboy` parameter.
   * pip

     * Python packages specified via :ref:`JOBTMPL/ApplicationTesting/Input/requirements` or
       :ref:`JOBTMPL/ApplicationTesting/Input/mingw_requirements` parameter.


.. _JOBTMPL/ApplicationTesting/Instantiation:

Instantiation
*************

The following instantiation example creates an ``AppTesting`` job derived from job template ``ApplicationTesting``
version ``@r7``. The job matrix comes from :ref:`JOBTMPL/Parameters` and the wheel from :ref:`JOBTMPL/Package`, so both
jobs must be listed as dependencies.

.. code-block:: yaml

   jobs:
     Params:
       uses: pyTooling/Actions/.github/workflows/Parameters.yml@r7
       with:
         package_name: myPackage

     Package:
       uses: pyTooling/Actions/.github/workflows/Package.yml@r7
       needs:
         - Params
       with:
         artifact: ${{ fromJson(needs.Params.outputs.artifact_names).package_all }}

     AppTesting:
       uses: pyTooling/Actions/.github/workflows/ApplicationTesting.yml@r7
       needs:
         - Params
         - Package
       with:
         jobs:                 ${{ needs.Params.outputs.python_jobs }}
         wheel:                ${{ fromJson(needs.Params.outputs.artifact_names).package_all }}
         apptest_xml_artifact: ${{ fromJson(needs.Params.outputs.artifact_names).apptesting_xml }}


.. seealso::

   :ref:`JOBTMPL/UnitTesting`
     Runs the same kind of tests against the sources instead of against the installed package.
   :ref:`JOBTMPL/Package`
     Produces the wheel artifact this template installs.
   :ref:`JOBTMPL/PublishTestResults`
     Merges the produced JUnit XML reports and publishes them.


.. _JOBTMPL/ApplicationTesting/Parameters:

Parameter Summary
*****************

.. rubric:: Goto :ref:`input parameters <JOBTMPL/ApplicationTesting/Inputs>`

+-------------------------------------------------------------------+----------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| Parameter Name                                                    | Required | Type          | Default                                                                                                                      |
+===================================================================+==========+===============+==============================================================================================================================+
| :ref:`JOBTMPL/ApplicationTesting/Input/jobs`                      | yes      | string        | — — — —                                                                                                                      |
+-------------------------------------------------------------------+----------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`JOBTMPL/ApplicationTesting/Input/wheel`                     | no       | string        | ``''``                                                                                                                       |
+-------------------------------------------------------------------+----------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`JOBTMPL/ApplicationTesting/Input/apt`                       | no       | string        | ``''``                                                                                                                       |
+-------------------------------------------------------------------+----------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`JOBTMPL/ApplicationTesting/Input/brew`                      | no       | string        | ``''``                                                                                                                       |
+-------------------------------------------------------------------+----------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`JOBTMPL/ApplicationTesting/Input/pacboy`                    | no       | string        | ``''``                                                                                                                       |
+-------------------------------------------------------------------+----------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`JOBTMPL/ApplicationTesting/Input/requirements`              | no       | string        | ``'-r ./requirements.txt'``                                                                                                  |
+-------------------------------------------------------------------+----------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`JOBTMPL/ApplicationTesting/Input/mingw_requirements`        | no       | string        | ``''``                                                                                                                       |
+-------------------------------------------------------------------+----------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`JOBTMPL/ApplicationTesting/Input/macos_before_script`       | no       | string        | ``''``                                                                                                                       |
+-------------------------------------------------------------------+----------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`JOBTMPL/ApplicationTesting/Input/macos_arm_before_script`   | no       | string        | ``''``                                                                                                                       |
+-------------------------------------------------------------------+----------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`JOBTMPL/ApplicationTesting/Input/ubuntu_before_script`      | no       | string        | ``''``                                                                                                                       |
+-------------------------------------------------------------------+----------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`JOBTMPL/ApplicationTesting/Input/windows_before_script`     | no       | string        | ``''``                                                                                                                       |
+-------------------------------------------------------------------+----------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`JOBTMPL/ApplicationTesting/Input/windows_arm_before_script` | no       | string        | ``''``                                                                                                                       |
+-------------------------------------------------------------------+----------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`JOBTMPL/ApplicationTesting/Input/mingw64_before_script`     | no       | string        | ``''``                                                                                                                       |
+-------------------------------------------------------------------+----------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`JOBTMPL/ApplicationTesting/Input/ucrt64_before_script`      | no       | string        | ``''``                                                                                                                       |
+-------------------------------------------------------------------+----------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`JOBTMPL/ApplicationTesting/Input/root_directory`            | no       | string        | ``''``                                                                                                                       |
+-------------------------------------------------------------------+----------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`JOBTMPL/ApplicationTesting/Input/tests_directory`           | no       | string        | ``'tests'``                                                                                                                  |
+-------------------------------------------------------------------+----------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`JOBTMPL/ApplicationTesting/Input/apptest_directory`         | no       | string        | ``'app'``                                                                                                                    |
+-------------------------------------------------------------------+----------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`JOBTMPL/ApplicationTesting/Input/apptest_report_xml`        | no       | string (JSON) | :jsoncode:`{"directory": "report/app", "filename": "TestReportSummary.xml", "fullpath": "report/app/TestReportSummary.xml"}` |
+-------------------------------------------------------------------+----------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`JOBTMPL/ApplicationTesting/Input/apptest_xml_artifact`      | no       | string        | ``''``                                                                                                                       |
+-------------------------------------------------------------------+----------+---------------+------------------------------------------------------------------------------------------------------------------------------+
| :ref:`JOBTMPL/ApplicationTesting/Input/unittest_html_artifact`    | no       | string        | ``''``                                                                                                                       |
+-------------------------------------------------------------------+----------+---------------+------------------------------------------------------------------------------------------------------------------------------+

.. rubric:: Goto :ref:`secrets <JOBTMPL/ApplicationTesting/Secrets>`

This job template needs no secrets.

.. rubric:: Goto :ref:`output parameters <JOBTMPL/ApplicationTesting/Outputs>`

This job template has no output parameters.


.. _JOBTMPL/ApplicationTesting/Inputs:

Input Parameters
****************

.. _JOBTMPL/ApplicationTesting/Input/jobs:

jobs
====

:Type:            string
:Required:        yes
:Default Value:   — — — —
:Possible Values: A JSON string with an array of dictionaries with the following key-value pairs:

                  :sysicon: icon to display
                  :system:  name of the system
                  :runs-on: virtual machine image and base operating system
                  :runtime: name of the runtime environment if not running natively on the VM image
                  :shell:   name of the shell
                  :pyicon:  icon for CPython or pypy
                  :python:  Python version
                  :envname: full name of the selected environment
:Description:     A JSON encoded job matrix to run multiple Python job variations. |br|
                  Usually taken from :ref:`JOBTMPL/Parameters/Output/python_jobs`.

.. _JOBTMPL/ApplicationTesting/Input/wheel:

wheel
=====

:Type:            string
:Required:        no
:Default Value:   ``''``
:Possible Values: Any valid artifact name.
:Description:     Name of the artifact containing the wheel package to install and test. |br|
                  Produced by :ref:`JOBTMPL/Package`. If empty, no package is downloaded and the tests run against
                  whatever is installed in the environment.

.. _JOBTMPL/ApplicationTesting/Input/apt:

apt
===

:Type:            string
:Required:        no
:Default Value:   ``''``
:Possible Values: Any valid list of parameters for ``apt install``. |br|
                  Packages are specified as a space separated list like ``'graphviz curl gzip'``.
:Description:     Additional Ubuntu system dependencies to be installed through *apt*.

.. _JOBTMPL/ApplicationTesting/Input/brew:

brew
====

:Type:            string
:Required:        no
:Default Value:   ``''``
:Possible Values: Any valid list of parameters for ``brew install``. |br|
                  Packages are specified as a space separated list.
:Description:     Additional macOS system dependencies to be installed through *homebrew*.

.. _JOBTMPL/ApplicationTesting/Input/pacboy:

pacboy
======

:Type:            string
:Required:        no
:Default Value:   ``''``
:Possible Values: Any valid list of parameters for ``pacboy sync``. |br|
                  Packages are specified as a space separated list like ``'python-pip:p graphviz:p'``.
:Description:     Additional MSYS2 dependencies to be installed through *pacboy* (*pacman*).

.. _JOBTMPL/ApplicationTesting/Input/requirements:

requirements
============

:Type:            string
:Required:        no
:Default Value:   ``'-r ./requirements.txt'``
:Possible Values: Any valid list of parameters for ``pip install``. |br|
                  Either a requirements file can be referenced using ``'-r path/to/requirements.txt'``, or a list of
                  packages can be specified using a space separated list.
:Description:     Python dependencies needed to *run* the application tests, installed through *pip*. |br|
                  The package under test is not installed from here - it comes from
                  :ref:`JOBTMPL/ApplicationTesting/Input/wheel`.

.. _JOBTMPL/ApplicationTesting/Input/mingw_requirements:

mingw_requirements
==================

:Type:            string
:Required:        no
:Default Value:   ``''``
:Possible Values: Any valid list of parameters for ``pip install``.
:Description:     Overrides :ref:`JOBTMPL/ApplicationTesting/Input/requirements` on MSYS2 (MinGW64, UCRT64) only. |br|
                  MSYS2 provides some Python packages through *pacboy*, so the pip requirements often differ there.

.. _JOBTMPL/ApplicationTesting/Input/macos_before_script:

macos_before_script
===================

:Type:            string
:Required:        no
:Default Value:   ``''``
:Possible Values: Any valid Bash script.
:Description:     Scripts to execute on macOS (Intel) before *pytest* is started.

.. _JOBTMPL/ApplicationTesting/Input/macos_arm_before_script:

macos_arm_before_script
=======================

:Type:            string
:Required:        no
:Default Value:   ``''``
:Possible Values: Any valid Bash script.
:Description:     Scripts to execute on macOS (Apple silicon) before *pytest* is started.

.. _JOBTMPL/ApplicationTesting/Input/ubuntu_before_script:

ubuntu_before_script
====================

:Type:            string
:Required:        no
:Default Value:   ``''``
:Possible Values: Any valid Bash script.
:Description:     Scripts to execute on Ubuntu (x86-64 and aarch64) before *pytest* is started.

.. _JOBTMPL/ApplicationTesting/Input/windows_before_script:

windows_before_script
=====================

:Type:            string
:Required:        no
:Default Value:   ``''``
:Possible Values: Any valid PowerShell script.
:Description:     Scripts to execute on Windows (x86-64) before *pytest* is started.

.. _JOBTMPL/ApplicationTesting/Input/windows_arm_before_script:

windows_arm_before_script
=========================

:Type:            string
:Required:        no
:Default Value:   ``''``
:Possible Values: Any valid PowerShell script.
:Description:     Scripts to execute on Windows (aarch64) before *pytest* is started.

.. _JOBTMPL/ApplicationTesting/Input/mingw64_before_script:

mingw64_before_script
=====================

:Type:            string
:Required:        no
:Default Value:   ``''``
:Possible Values: Any valid Bash script.
:Description:     Scripts to execute on Windows within MSYS2 MinGW64 before *pytest* is started.

.. _JOBTMPL/ApplicationTesting/Input/ucrt64_before_script:

ucrt64_before_script
====================

:Type:            string
:Required:        no
:Default Value:   ``''``
:Possible Values: Any valid Bash script.
:Description:     Scripts to execute on Windows within MSYS2 UCRT64 before *pytest* is started.

.. _JOBTMPL/ApplicationTesting/Input/root_directory:

root_directory
==============

:Type:            string
:Required:        no
:Default Value:   ``''``
:Possible Values: Any path relative to the repository root. An empty string means the repository root.
:Description:     Working directory from which *pytest* is started.

.. _JOBTMPL/ApplicationTesting/Input/tests_directory:

tests_directory
===============

:Type:            string
:Required:        no
:Default Value:   ``'tests'``
:Possible Values: Any path relative to :ref:`JOBTMPL/ApplicationTesting/Input/root_directory`.
:Description:     Directory containing all tests.

.. _JOBTMPL/ApplicationTesting/Input/apptest_directory:

apptest_directory
=================

:Type:            string
:Required:        no
:Default Value:   ``'app'``
:Possible Values: Any path relative to :ref:`JOBTMPL/ApplicationTesting/Input/tests_directory`.
:Description:     Directory containing the application tests. |br|
                  With the defaults, the tests are collected from :file:`tests/app`.

.. _JOBTMPL/ApplicationTesting/Input/apptest_report_xml:

apptest_report_xml
==================

:Type:            string (JSON)
:Required:        no
:Default Value:   :jsoncode:`{"directory": "report/app", "filename": "TestReportSummary.xml", "fullpath": "report/app/TestReportSummary.xml"}`
:Possible Values: Any valid JSON string containing a JSON object with fields:

                  :directory: Directory or sub-directory where the report will be saved.
                  :filename:  File name of the report.
                  :fullpath:  Directory and file name of the report.
:Description:     Path of the application test summary report in JUnit XML format, as a JSON object. |br|
                  This path is configured in :file:`pyproject.toml` and can be extracted by
                  :ref:`JOBTMPL/ExtractConfiguration`.

.. _JOBTMPL/ApplicationTesting/Input/apptest_xml_artifact:

apptest_xml_artifact
====================

:Type:            string
:Required:        no
:Default Value:   ``''``
:Possible Values: Any valid artifact name. An empty string disables the upload.
:Description:     Name of the artifact receiving the application test report in JUnit XML format. |br|
                  If empty, *pytest* is run without ``--junitxml`` and no report is uploaded.

.. _JOBTMPL/ApplicationTesting/Input/unittest_html_artifact:

unittest_html_artifact
======================

:Type:            string
:Required:        no
:Default Value:   ``''``
:Possible Values: Any valid artifact name. An empty string disables the upload.
:Description:     Name of the artifact receiving the application test report in HTML format.

                  .. note::

                     The parameter is named ``unittest_html_artifact`` although it carries the *application* test
                     report. The name is kept for backwards compatibility with existing pipeline instantiations.


.. _JOBTMPL/ApplicationTesting/Secrets:

Secrets
*******

This job template needs no secrets.


.. _JOBTMPL/ApplicationTesting/Outputs:

Outputs
*******

This job template has no output parameters.

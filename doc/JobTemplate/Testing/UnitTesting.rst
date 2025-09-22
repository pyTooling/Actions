.. _JOBTMPL/UnitTesting:
.. index::
   single: pytest; UnitTesting Template
   single: Coverage.py; UnitTesting Template
   single: GitHub Action Reusable Workflow; UnitTesting Template

UnitTesting
###########

This template runs multiple jobs from a matrix as a cross of Python versions and systems. The summary report in junit
XML format is optionally uploaded as an artifact.

Configuration options to ``pytest`` should be given via section ``[tool.pytest.ini_options]`` in a ``pyproject.toml``
file.

.. topic:: Features

   * Execute unit tests using `pytest <https://docs.pytest.org/en/stable/>`__.

     * Provide unit test results as JUnit XML file (pyTest XML dialect).

   * Collect code coverage using `Coverage.py <https://coverage.readthedocs.io/>`__.

     * Provide code coverage results as pytest SQLite database.
     * Provide code coverage results as Cobertura XML file.
     * Provide code coverage results as pytest JSON file.
     * Provide code coverage results as HTML report.

.. topic:: Behavior

   1. Checkout repository.
   2. Setup environment and install dependencies (``apt``, ``homebrew``, ``pacman``, ...).
   3. Setup Python and install dependencies (``pip``).
   4. Run instructions from ``*_before_script`` parameter.
   5. Run unit tests using *pytest* and if enabled in combination with *Coverage.py*.
   6. Convert gathered results to other formats.
   7. Upload results (test reports, code coverage reports, ...) as an artifacts.

.. topic:: Job Execution

   .. image:: ../../_static/pyTooling-Actions-UnitTesting.png
      :width: 600px

.. topic:: Dependencies

   * :gh:`actions/checkout`
   * :gh:`msys2/setup-msys2`
   * :gh:`actions/setup-python`
   * :gh:`pyTooling/download-artifact`

     * :gh:`actions/download-artifact`

   * :gh:`pyTooling/upload-artifact`

     * :gh:`actions/upload-artifact`

   * apt: Packages specified via :ref:`JOBTMPL/UnitTesting/Input/apt` parameter.
   * homebrew: Packages specified via :ref:`JOBTMPL/UnitTesting/Input/brew` parameter.
   * MSYS2: Packages specified via :ref:`JOBTMPL/UnitTesting/Input/pacboy` parameter.
   * pip

     * :pypi:`wheel`
     * :pypi:`tomli`
     * Python packages specified via :ref:`JOBTMPL/UnitTesting/Input/requirements` or
       :ref:`JOBTMPL/UnitTesting/Input/mingw_requirements` parameter.


.. _JOBTMPL/UnitTesting/Instantiation:

Instantiation
*************

The following instantiation example creates a ``UnitTesting`` job derived from job template ``UnitTesting`` version
`@r5`. For providing the job matrix as a JSON string, the :ref:`JOBTMPL/Parameters` job template is used. Additionally,
the job needs configuration settings, which are stored in :file:`pyproject.toml`. Instead of duplicating these settings,
the :ref:`JOBTMPL/ExtractConfiguration` job template is used to extract these settings.

.. code-block:: yaml

   jobs:
     ConfigParams:
       uses: pyTooling/Actions/.github/workflows/ExtractConfiguration.yml@r5

     UnitTestingParams:
       uses: pyTooling/Actions/.github/workflows/Parameters.yml@r5
       with:
         package_name: myPackage

     UnitTesting:
       uses: pyTooling/Actions/.github/workflows/UnitTesting.yml@r5
       needs:
         - ConfigParams
         - UnitTestingParams
       with:
         jobs:                     ${{ needs.UnitTestingParams.outputs.python_jobs }}
         requirements:             '-r tests/unit/requirements.txt'
         unittest_report_xml:      ${{ needs.ConfigParams.outputs.unittest_report_xml }}
         unittest_xml_artifact:    ${{ fromJson(needs.UnitTestingParams.outputs.artifact_names).unittesting_xml }}
         coverage_sqlite_artifact: ${{ fromJson(needs.UnitTestingParams.outputs.artifact_names).codecoverage_sqlite }}


.. seealso::

   :ref:`JOBTMPL/Parameters`
     ``Parameters`` is usually used to pre-compute the job matrix as a JSON string with all system |times| environment
     |times| Python version combinations.
   :ref:`JOBTMPL/PublishTestResults`
     ``PublishTestResults`` can be used to merge all JUnit test reports into one file.
   :ref:`JOBTMPL/PublishCoverageResults`
     ``PublishCoverageResults`` can be used to merge all code coverage reports into one file.


.. _JOBTMPL/UnitTesting/Parameters:

Parameter Summary
*****************

.. # |unittest_report_xml| code-block:: json

                         { "directory": "report/unit",
                            "filename":  "TestReportSummary.xml",
                            "fullpath":  "report/unit/TestReportSummary.xml"
                         }


.. rubric:: Goto :ref:`input parameters <JOBTMPL/UnitTesting/Inputs>`

+-------------------------------------------------------------------------+----------+----------+-----------------------------------------------------------------------------------------------------------------------------------+
| Parameter Name                                                          | Required | Type     | Default                                                                                                                           |
+=========================================================================+==========+==========+===================================================================================================================================+
| :ref:`JOBTMPL/UnitTesting/Input/jobs`                                   | yes      | string   | — — — —                                                                                                                           |
+-------------------------------------------------------------------------+----------+----------+-----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`JOBTMPL/UnitTesting/Input/apt`                                    | no       | string   | ``''``                                                                                                                            |
+-------------------------------------------------------------------------+----------+----------+-----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`JOBTMPL/UnitTesting/Input/brew`                                   | no       | string   | ``''``                                                                                                                            |
+-------------------------------------------------------------------------+----------+----------+-----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`JOBTMPL/UnitTesting/Input/pacboy`                                 | no       | string   | ``''``                                                                                                                            |
+-------------------------------------------------------------------------+----------+----------+-----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`JOBTMPL/UnitTesting/Input/requirements`                           | no       | string   | ``'-r tests/requirements.txt'``                                                                                                   |
+-------------------------------------------------------------------------+----------+----------+-----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`JOBTMPL/UnitTesting/Input/mingw_requirements`                     | no       | string   | ``''``                                                                                                                            |
+-------------------------------------------------------------------------+----------+----------+-----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`JOBTMPL/UnitTesting/Input/macos_before_script`                    | no       | string   | ``''``                                                                                                                            |
+-------------------------------------------------------------------------+----------+----------+-----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`JOBTMPL/UnitTesting/Input/macos_arm_before_script`                | no       | string   | ``''``                                                                                                                            |
+-------------------------------------------------------------------------+----------+----------+-----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`JOBTMPL/UnitTesting/Input/ubuntu_before_script`                   | no       | string   | ``''``                                                                                                                            |
+-------------------------------------------------------------------------+----------+----------+-----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`JOBTMPL/UnitTesting/Input/mingw64_before_script`                  | no       | string   | ``''``                                                                                                                            |
+-------------------------------------------------------------------------+----------+----------+-----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`JOBTMPL/UnitTesting/Input/ucrt64_before_script`                   | no       | string   | ``''``                                                                                                                            |
+-------------------------------------------------------------------------+----------+----------+-----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`JOBTMPL/UnitTesting/Input/root_directory`                         | no       | string   | ``''``                                                                                                                            |
+-------------------------------------------------------------------------+----------+----------+-----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`JOBTMPL/UnitTesting/Input/tests_directory`                        | no       | string   | ``'tests'``                                                                                                                       |
+-------------------------------------------------------------------------+----------+----------+-----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`JOBTMPL/UnitTesting/Input/unittest_directory`                     | no       | string   | ``'unit'``                                                                                                                        |
+-------------------------------------------------------------------------+----------+----------+-----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`JOBTMPL/UnitTesting/Input/unittest_report_xml`                    | no       | string   | :jsoncode:`{"directory": "report/unit", "filename":  "TestReportSummary.xml", "fullpath":  "report/unit/TestReportSummary.xml"}`  |
+-------------------------------------------------------------------------+----------+----------+-----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`JOBTMPL/UnitTesting/Input/coverage_config`                        | no       | string   | ``'pyproject.toml'``                                                                                                              |
+-------------------------------------------------------------------------+----------+----------+-----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`JOBTMPL/UnitTesting/Input/coverage_report_xml`                    | no       | string   | :jsoncode:`{"directory": "report/coverage", "filename":  "coverage.xml", "fullpath":  "report/coverage/coverage.xml"}`            |
+-------------------------------------------------------------------------+----------+----------+-----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`JOBTMPL/UnitTesting/Input/coverage_report_json`                   | no       | string   | :jsoncode:`{"directory": "report/coverage", "filename":  "coverage.json", "fullpath":  "report/coverage/coverage.json"}`          |
+-------------------------------------------------------------------------+----------+----------+-----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`JOBTMPL/UnitTesting/Input/coverage_report_html`                   | no       | string   | :jsoncode:`{"directory": "report/coverage"}`                                                                                      |
+-------------------------------------------------------------------------+----------+----------+-----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`JOBTMPL/UnitTesting/Input/unittest_xml_artifact`                  | no       | string   | ``''``                                                                                                                            |
+-------------------------------------------------------------------------+----------+----------+-----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`JOBTMPL/UnitTesting/Input/unittest_html_artifact`                 | no       | string   | ``''``                                                                                                                            |
+-------------------------------------------------------------------------+----------+----------+-----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`JOBTMPL/UnitTesting/Input/coverage_sqlite_artifact`               | no       | string   | ``''``                                                                                                                            |
+-------------------------------------------------------------------------+----------+----------+-----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`JOBTMPL/UnitTesting/Input/coverage_xml_artifact`                  | no       | string   | ``''``                                                                                                                            |
+-------------------------------------------------------------------------+----------+----------+-----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`JOBTMPL/UnitTesting/Input/coverage_json_artifact`                 | no       | string   | ``''``                                                                                                                            |
+-------------------------------------------------------------------------+----------+----------+-----------------------------------------------------------------------------------------------------------------------------------+
| :ref:`JOBTMPL/UnitTesting/Input/coverage_html_artifact`                 | no       | string   | ``''``                                                                                                                            |
+-------------------------------------------------------------------------+----------+----------+-----------------------------------------------------------------------------------------------------------------------------------+

.. rubric:: Goto :ref:`secrets <JOBTMPL/UnitTesting/Secrets>`

This job template needs no secrets.

.. rubric:: Goto :ref:`output parameters <JOBTMPL/UnitTesting/Outputs>`

This job template has no output parameters.


.. _JOBTMPL/UnitTesting/Inputs:

Input Parameters
****************

.. _JOBTMPL/UnitTesting/Input/jobs:

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
:Description:     A JSON encoded job matrix to run multiple Python job variations.


.. _JOBTMPL/UnitTesting/Input/apt:

apt
===

:Type:            string
:Required:        no
:Default Value:   ``''``
:Possible Values: Any valid list of parameters for ``apt install``. |br|
                  Packages are specified as a space separated list like ``'graphviz curl gzip'``.
:Description:     Additional Ubuntu system dependencies to be installed through *apt*.
:Example:
                  .. code-block:: yaml

                     UnitTests:
                       ...
                       with:
                         apt: >-
                           graphviz
                           curl
                           gzip

.. _JOBTMPL/UnitTesting/Input/brew:

brew
====

:Type:            string
:Required:        no
:Default Value:   ``''``
:Possible Values: Any valid list of parameters for ``brew install``. |br|
                  Packages are specified as a space separated list.
:Description:     Additional macOS system dependencies to be installed through *brew*.


.. _JOBTMPL/UnitTesting/Input/pacboy:

pacboy
======

:Type:            string
:Required:        no
:Default Value:   ``''``
:Possible Values: Any valid list of parameters for ``pacboy``. |br|
                  Packages are specified as a space separated list like ``'python-lxml:p python-numpy:p'``.
:Description:     Additional MSYS2 system dependencies to be installed through *pacboy* (*pacman*). |br|
                  Usually, Python packages start with ``python-``. The suffix ``:p`` ensures pacboy figures out the
                  correct package repository prefix for MinGW64, UCRT64, ...

                  .. note::

                     Internally, a dedicated workflow step reads the :ref:`JOBTMPL/UnitTesting/Input/requirements` file
                     for Python and compares requested packages with a list of packages that should be installed through
                     *pacman*/*pacboy* compared to installation via *pip*. These are mainly core packages or packages
                     with embedded C code. |br|
                     The list of identified packages is handed over to *pacboy* for preinstallation. Otherwise *pip*
                     will later raise an error. |br|
                     The packages listed by this parameter will be installed in addition to the identified packages.

                  .. attention::

                     Ensure your Python requirements match the available version from MSYS2 packages list, otherwise
                     if your :file:`requirements.txt` requests a newer version then provided by MSYS2, such a dependency
                     will fail.
:Example:
                  .. code-block:: yaml

                     UnitTests:
                       ...
                       with:
                         pacboy: >-
                           python-lxml:p
:Packages:        The following list of Python packages is identified to be installed via *pacboy*:

                  * :ucrt64:`python-coverage` |rarr| :pypi:`coverage`
                  * :ucrt64:`igraph` |rarr| :pypi:`igraph`
                  * :ucrt64:`python-lxml` |rarr| :pypi:`lxml`
                  * :ucrt64:`python-markupsafe` |rarr| :pypi:`markupsafe`
                  * :ucrt64:`python-numpy` |rarr| :pypi:`numpy`
                  * :ucrt64:`python-pip` |rarr| :pypi:`pip`
                  * :ucrt64:`python-pyaml` |rarr| :pypi:`pyaml`
                  * :ucrt64:`python-ruamel-yaml` |rarr| :pypi:`ruamel-yaml`
                  * :ucrt64:`python-wheel` |rarr| :pypi:`wheel`
                  * :ucrt64:`python-tomli` |rarr| :pypi:`tomli`
                  * :ucrt64:`python-types-pyyaml` |rarr| :pypi:`types.pyyaml`


.. _JOBTMPL/UnitTesting/Input/requirements:

requirements
============

:Type:            string
:Required:        no
:Default Value:   ``'-r tests/requirements.txt'``
:Possible Values: Any valid list of parameters for ``pip install``. |br|
                  Either a requirements file can be referenced using ``'-r path/to/requirements.txt'``, or a list of
                  packages can be specified using a space separated list like ``'coverage pytest'``.
:Description:     Python dependencies to be installed through *pip*.


.. _JOBTMPL/UnitTesting/Input/mingw_requirements:

mingw_requirements
==================

:Type:            string
:Required:        no
:Default Value:   ``''``
:Possible Values: Any valid list of parameters for ``pip install``. |br|
                  Either a requirements file can be referenced using ``'-r path/to/requirements.txt'``, or a list of
                  packages can be specified using a space separated list like ``'coverage pytest'``.
:Description:     Override Python dependencies to be installed through *pip* in MSYS2 (MinGW64/UCRT64) only.


.. _JOBTMPL/UnitTesting/Input/macos_before_script:

macos_before_script
===================

:Type:            string
:Required:        no
:Default Value:   ``''``
:Possible Values: Any valid *Bash* instructions as single-line or multi-line string suitable for macOS (Intel platform).
:Description:     These optional *Bash* instructions for macOS are executed after setting up the environment and
                  installing the platform specific dependencies and before running the unit test.


.. _JOBTMPL/UnitTesting/Input/macos_arm_before_script:

macos_arm_before_script
=======================

:Type:            string
:Required:        no
:Default Value:   ``''``
:Possible Values: Any valid *Bash* instructions as single-line or multi-line string suitable for macOS (ARM platform).
:Description:     These optional *Bash* instructions for macOS are executed after setting up the environment and
                  installing the platform specific dependencies and before running the unit test.


.. _JOBTMPL/UnitTesting/Input/ubuntu_before_script:

ubuntu_before_script
====================

:Type:            string
:Required:        no
:Default Value:   ``''``
:Possible Values: Any valid *Bash* instructions as single-line or multi-line string suitable for Ubuntu.
:Description:     These optional *Bash* instructions for Ubuntu are executed after setting up the environment and
                  installing the platform specific dependencies and before running the unit test.


.. _JOBTMPL/UnitTesting/Input/mingw64_before_script:

mingw64_before_script
=====================

:Type:            string
:Required:        no
:Default Value:   ``''``
:Possible Values: Any valid *Bash* instructions as single-line or multi-line string suitable for MinGW64 on Windows.
:Description:     These optional *Bash* instructions for MinGW64 on Windows are executed after setting up the
                  environment and installing the platform specific dependencies and before running the unit test.


.. _JOBTMPL/UnitTesting/Input/ucrt64_before_script:

ucrt64_before_script
====================

:Type:            string
:Required:        no
:Default Value:   ``''``
:Possible Values: Any valid *Bash* instructions as single-line or multi-line string suitable for UCRT64 on Windows.
:Description:     These optional *Bash* instructions for UCRT64 on Windows are executed after setting up the
                  environment and installing the platform specific dependencies and before running the unit test.

.. hint::

   The next parameters allow running different test kinds (unit tests, performance tests, platform tests, ...) with the
   same job template, but isolated in sub-directories, thus pytest only discovers a subset of tests. The following code
   blocks showcase how the job template uses these parameters and how it relates to a proposed directory structure.

   .. grid:: 3

      .. grid-item::
         :columns: 5

         .. card:: Relation between :ref:`JOBTMPL/UnitTesting/Input/root_directory`, :ref:`JOBTMPL/UnitTesting/Input/tests_directory` and :ref:`JOBTMPL/UnitTesting/Input/unittest_directory`

            .. code-block:: bash

               cd <RepositoryRoot>
               cd ${root_directory}

               python -m \
                 pytest -raP \
                   --color=yes ..... \
                   "${tests_directory}/${unittest_directory}"

      .. grid-item::
         :columns: 3

         .. card:: Directory Structure

            .. code-block::

               <RepositoryRoot>/
                 doc/
                 myPackage/
                   __init__.py
                 tests/
                   unit/
                     myTests.py

      .. grid-item::
         :columns: 3

         .. card:: Example for Default Values

            .. code-block:: bash

               cd <RepositoryRoot>
               cd .

               python -m \
                 pytest -raP \
                   --color=yes ..... \
                   "tests/unit"


.. _JOBTMPL/UnitTesting/Input/root_directory:

root_directory
==============

:Type:            string
:Required:        no
:Default Value:   ``''``
:Possible Values: Any valid directory or sub-directory.
:Description:     Working directory for running tests. |br|
                  Usually, this is the repository's root directory. Tests are called relatively from here. See
                  :ref:`JOBTMPL/UnitTesting/Input/tests_directory` and :ref:`JOBTMPL/UnitTesting/Input/unittest_directory`.


.. _JOBTMPL/UnitTesting/Input/tests_directory:

tests_directory
===============

:Type:            string
:Required:        no
:Default Value:   ``'tests'``
:Possible Values: Any valid directory or sub-directory.
:Description:     Path to the directory containing tests (relative from :ref:`JOBTMPL/UnitTesting/Input/root_directory`).


.. _JOBTMPL/UnitTesting/Input/unittest_directory:

unittest_directory
==================

:Type:            string
:Required:        no
:Default Value:   ``'unit'``
:Possible Values: Any valid directory or sub-directory.
:Description:     Path to the directory containing unit tests (relative from :ref:`JOBTMPL/UnitTesting/Input/tests_directory`).


.. _JOBTMPL/UnitTesting/Input/unittest_report_xml:

unittest_report_xml
===================

:Type:            string (JSON)
:Required:        no
:Default Value:
                  .. code-block:: json

                     { "directory": "reports/unit",
                       "filename":  "UnittestReportSummary.xml",
                       "fullpath":  "reports/unit/UnittestReportSummary.xml"
                     }
:Possible Values: Any valid JSON string containing a JSON object with fields:

                  :directory: Directory or sub-directory where the unittest summary report in XML format will be saved.
                  :filename:  Filename of the generated JUnit XML report. |br|
                              Any valid filename accepted by ``pytest ... --junitxml=${unittest_report_xml}``.
                  :fullpath:  The concatenation of both previous fields using the ``/`` separator.
:Description:     Directory, filename and fullpath as JSON object where the unittest summary report in XML format will
                  be saved. |br|
                  This path is configured in :file:`pyproject.toml` and can be extracted by
                  :ref:`JOBTMPL/ExtractConfiguration`.
:Example:
                  .. code-block:: yaml

                     ConfigParams:
                       uses: pyTooling/Actions/.github/workflows/ExtractConfiguration.yml@r5

                     UnitTesting:
                       uses: pyTooling/Actions/.github/workflows/UnitTesting.yml@r5
                       needs:
                         - ConfigParams
                       with:
                         ...
                         unittest_report_xml: ${{ needs.ConfigParams.outputs.unittest_report_xml }}


.. _JOBTMPL/UnitTesting/Input/coverage_config:

coverage_config
===============

:Type:            string
:Required:        no
:Default Value:   ``'pyproject.toml'``
:Possible Values: TBD


.. _JOBTMPL/UnitTesting/Input/coverage_report_xml:

coverage_report_xml
===================

:Type:            string (JSON)
:Required:        no
:Default Value:
                  .. code-block:: json

                     { "directory": "reports/coverage",
                       "filename":  "coverage.xml",
                       "fullpath":  "reports/coverage/coverage.xml"
                     }
:Possible Values: Any valid JSON string containing a JSON object with fields:

                  :directory: Directory or sub-directory where the code coverage report in Cobertura XML format will be
                              saved.
                  :filename:  Filename of the generated Cobertura XML report. |br|
                              Any valid XML filename.
                  :fullpath:  The concatenation of both previous fields using the ``/`` separator.
:Description:     Directory, filename and fullpath as JSON object where the code coverage report in Cobertura XML format
                  will be saved. |br|
                  This path is configured in :file:`pyproject.toml` and can be extracted by
                  :ref:`JOBTMPL/ExtractConfiguration`.
:Example:
                  .. code-block:: yaml

                     ConfigParams:
                       uses: pyTooling/Actions/.github/workflows/ExtractConfiguration.yml@r5

                     UnitTesting:
                       uses: pyTooling/Actions/.github/workflows/UnitTesting.yml@r5
                       needs:
                         - ConfigParams
                       with:
                         ...
                         coverage_report_xml: ${{ needs.ConfigParams.outputs.coverage_report_xml }}


.. _JOBTMPL/UnitTesting/Input/coverage_report_json:

coverage_report_json
====================

:Type:            string (JSON)
:Required:        no
:Default Value:
                  .. code-block:: json

                     { "directory": "reports/coverage",
                       "filename":  "coverage.json",
                       "fullpath":  "reports/coverage/coverage.json"
                     }
:Possible Values: Any valid JSON string containing a JSON object with fields:

                  :directory: Directory or sub-directory where the code coverage report in Coverage.py's JSON format
                              will be saved.
                  :filename:  Filename of the generated Coverage.py JSON report. |br|
                              Any valid JSON filename.
                  :fullpath:  The concatenation of both previous fields using the ``/`` separator.
:Description:     Directory, filename and fullpath as JSON object where the code coverage report in Coverage.py's JSON
                  format will be saved. |br|
                  This path is configured in :file:`pyproject.toml` and can be extracted by
                  :ref:`JOBTMPL/ExtractConfiguration`.
:Example:
                  .. code-block:: yaml

                     ConfigParams:
                       uses: pyTooling/Actions/.github/workflows/ExtractConfiguration.yml@r5

                     UnitTesting:
                       uses: pyTooling/Actions/.github/workflows/UnitTesting.yml@r5
                       needs:
                         - ConfigParams
                       with:
                         ...
                         coverage_report_json: ${{ needs.ConfigParams.outputs.coverage_report_json }}


.. _JOBTMPL/UnitTesting/Input/coverage_report_html:

coverage_report_html
====================

:Type:            string (JSON)
:Required:        no
:Default Value:
                  .. code-block:: json

                     { "directory": "reports/coverage/html"
                     }
:Possible Values: Any valid JSON string containing a JSON object with fields:

                  :directory: Directory or sub-directory where the code coverage report in HTML format will be saved.
:Description:     Directory as JSON object where the code coverage report in HTML format will be saved. |br|
                  This path is configured in :file:`pyproject.toml` and can be extracted by
                  :ref:`JOBTMPL/ExtractConfiguration`.
:Example:
                  .. code-block:: yaml

                     ConfigParams:
                       uses: pyTooling/Actions/.github/workflows/ExtractConfiguration.yml@r5

                     UnitTesting:
                       uses: pyTooling/Actions/.github/workflows/UnitTesting.yml@r5
                       needs:
                         - ConfigParams
                       with:
                         ...
                         coverage_report_html: ${{ needs.ConfigParams.outputs.coverage_report_html }}


.. _JOBTMPL/UnitTesting/Input/unittest_xml_artifact:

unittest_xml_artifact
=====================

:Type:            string
:Required:        no
:Possible Values: Any valid artifact name.
:Description:     Name of the artifact containing the unittest report summary in XML format.


.. _JOBTMPL/UnitTesting/Input/unittest_html_artifact:

unittest_html_artifact
======================

:Type:            string
:Required:        no
:Possible Values: Any valid artifact name.
:Description:     Name of the artifact containing the unittest report in HTML format.


.. _JOBTMPL/UnitTesting/Input/coverage_sqlite_artifact:

coverage_sqlite_artifact
========================

:Type:            string
:Required:        no
:Possible Values: Any valid artifact name.
:Description:     Name of the artifact containing the code coverage report as SQLite database.


.. _JOBTMPL/UnitTesting/Input/coverage_xml_artifact:

coverage_xml_artifact
=====================

:Type:            string
:Required:        no
:Possible Values: Any valid artifact name.
:Description:     Name of the artifact containing the code coverage report in XML format.


.. _JOBTMPL/UnitTesting/Input/coverage_json_artifact:

coverage_json_artifact
======================

:Type:            string
:Required:        no
:Possible Values: Any valid artifact name.
:Description:     Name of the artifact containing the code coverage report in JSON format.


.. _JOBTMPL/UnitTesting/Input/coverage_html_artifact:

coverage_html_artifact
======================

:Type:            string
:Required:        no
:Possible Values: Any valid artifact name.
:Description:     Name of the artifact containing the code coverage report in HTML format.


.. _JOBTMPL/UnitTesting/Secrets:

Secrets
*******

This job template needs no secrets.


.. _JOBTMPL/UnitTesting/Outputs:

Outputs
*******

This job template has no output parameters.


.. _JOBTMPL/UnitTesting/Optimizations:

Optimizations
*************

The following optimizations can be used to reduce the template's runtime.

Disable unit test XML generation
  If parameter :ref:`JOBTMPL/UnitTesting/Input/unittest_xml_artifact` is empty, no unit test summary report will be
  generated and no JUnit XML artifact will be uploaded.
Disabled code coverage collection
  If parameter :ref:`JOBTMPL/UnitTesting/Input/coverage_config` is empty, no code coverage will be collected.
Disable code coverage SQLite database artifact upload
  If parameter :ref:`JOBTMPL/UnitTesting/Input/coverage_sqlite_artifact` is empty, the collected code coverage database
  (SQLlite format) wont be uploaded as an artifact.
Disable code coverage report conversion to the Cobertura XML format.
  If parameter :ref:`JOBTMPL/UnitTesting/Input/coverage_xml_artifact` is empty, no Cobertura XML file will be generated
  from code coverage report. As no Cobertura XML file exists, no code coverage XML artifact will be uploaded.
Disable code coverage report conversion to the *Coverage.py* JSON format.
  If parameter :ref:`JOBTMPL/UnitTesting/Input/coverage_json_artifact` is empty, no *Coverage.py* JSON file will be
  generated from code coverage report. As no JSON file exists, no code coverage JSON artifact will be uploaded.
Disable code coverage report conversion to an HTML website.
  If parameter :ref:`JOBTMPL/UnitTesting/Input/coverage_html_artifact` is empty, no coverage report HTML report will be
  generated from code coverage report. As no HTML report exists, no code coverage HTML artifact will be uploaded.

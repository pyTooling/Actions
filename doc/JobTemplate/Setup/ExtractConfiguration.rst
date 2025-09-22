.. _JOBTMPL/ExtractConfiguration:
.. index::
   single: GitHub Action Reusable Workflow; ExtractConfiguration Template

ExtractConfiguration
####################

The ``ExtractConfiguration`` job template extracts Python project settings from :file:`pyproject.toml` and shares the
values via output parameters with other jobs. Thus, only a single centralized implementation is needed to avoid code
duplications within jobs.


.. topic:: Features

   * Extract the unittest report file in pytest's JUnit XML format as directory name, filename and full path from
     :file:`pyproject.toml`.
   * Extract the merged unittest XML report file as directory name, filename and full path from :file:`pyproject.toml`.
   * Extract code coverage report in HTML format as directory from :file:`pyproject.toml`.
   * Extract code coverage report file in Cobertura XML format as directory name, filename and full path from
     :file:`pyproject.toml`.
   * Extract code coverage report file in Coverage.py's JSON format as directory name, filename and full path from
     :file:`pyproject.toml`.
   * Extract static typing report file in Cobertura XML format as directory name, filename and full path from
     :file:`pyproject.toml`.
   * Extract static typing report file in JUnit XML format as directory name, filename and full path from
     :file:`pyproject.toml`.
   * Extract static typing report in HTML format as directory name from :file:`pyproject.toml`.

.. topic:: Behavior

   1. Checkout repository.
   2. Install Python dependencies.
   3. Compute the full package name and the package source directory.
   4. Read :file:`pyproject.toml` and extract settings for:

      * :term:`Coverage.py`
      * :term:`mypy`
      * :term:`pyEDAA.Reports`
      * :term:`pytest`

.. topic:: Job Execution

   .. image:: ../../_static/pyTooling-Actions-ExtractConfiguration.png
      :width: 600px

.. topic:: Dependencies

   * :gh:`actions/checkout`
   * :gh:`actions/setup-python`

     * :pypi:`wheel`
     * :pypi:`tomli`


.. _JOBTMPL/ExtractConfiguration/Instantiation:

Instantiation
*************

The following instantiation example creates a ``ConfigParams`` job derived from job template ``ExtractConfiguration``
version ``@r5``. It requires no special parameters to extract unit test (pytest) and code coverage (Coverage.py)
settings.

.. code-block:: yaml

   jobs:
     ConfigParams:
       uses: pyTooling/Actions/.github/workflows/ExtractConfiguration.yml@r5

     UnitTesting:
       uses: pyTooling/Actions/.github/workflows/UnitTesting.yml@r5
       needs:
         - ConfigParams
       with:
         unittest_report_xml:  ${{ needs.ConfigParams.outputs.unittest_report_xml }}
         coverage_report_xml:  ${{ needs.ConfigParams.outputs.coverage_report_xml }}
         coverage_report_json: ${{ needs.ConfigParams.outputs.coverage_report_json }}
         coverage_report_html: ${{ needs.ConfigParams.outputs.coverage_report_html }}


.. seealso::

   :ref:`JOBTMPL/UnitTesting`
     ``UnitTesting`` is usually
   :ref:`JOBTMPL/StaticTypeCheck`
     xxx
   :ref:`JOBTMPL/CheckDocumentation`
     xxx
   :ref:`JOBTMPL/InstallPackage`
     xxx
   :ref:`JOBTMPL/PublishCoverageResults`
     xxx
   :ref:`JOBTMPL/PublishTestResults`
     xxx
   :ref:`JOBTMPL/SphinxDocumentation`
     xxx

.. _JOBTMPL/ExtractConfiguration/Parameters:

Parameter Summary
*****************

.. rubric:: Goto :ref:`input parameters <JOBTMPL/ExtractConfiguration/Inputs>`

+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| Parameter Name                                                      | Required | Type     | Default                                                           |
+=====================================================================+==========+==========+===================================================================+
| :ref:`JOBTMPL/ExtractConfiguration/Input/ubuntu_image_version`      | no       | string   | ``'24.04'``                                                       |
+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/ExtractConfiguration/Input/python_version`            | no       | string   | ``'3.13'``                                                        |
+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/ExtractConfiguration/Input/coverage_config`           | no       | string   | ``'pyproject.toml'``                                              |
+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+

.. rubric:: Goto :ref:`secrets <JOBTMPL/ExtractConfiguration/Secrets>`

This job template needs no secrets.

.. rubric:: Goto :ref:`output parameters <JOBTMPL/ExtractConfiguration/Outputs>`

+---------------------------------------------------------------------------------+----------------+-------------------------------------------------------------------+
| Result Name                                                                     | Type           | Description                                                       |
+=================================================================================+================+===================================================================+
| :ref:`JOBTMPL/ExtractConfiguration/Output/unittest_report_xml`                  | string (JSON)  |                                                                   |
+---------------------------------------------------------------------------------+----------------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/ExtractConfiguration/Output/unittest_merged_report_xml`           | string (JSON)  |                                                                   |
+---------------------------------------------------------------------------------+----------------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/ExtractConfiguration/Output/coverage_report_html`                 | string (JSON)  |                                                                   |
+---------------------------------------------------------------------------------+----------------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/ExtractConfiguration/Output/coverage_report_xml`                  | string (JSON)  |                                                                   |
+---------------------------------------------------------------------------------+----------------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/ExtractConfiguration/Output/coverage_report_json`                 | string (JSON)  |                                                                   |
+---------------------------------------------------------------------------------+----------------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/ExtractConfiguration/Output/typing_report_cobertura`              | string (JSON)  |                                                                   |
+---------------------------------------------------------------------------------+----------------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/ExtractConfiguration/Output/typing_report_junit`                  | string (JSON)  |                                                                   |
+---------------------------------------------------------------------------------+----------------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/ExtractConfiguration/Output/typing_report_html`                   | string (JSON)  |                                                                   |
+---------------------------------------------------------------------------------+----------------+-------------------------------------------------------------------+


.. _JOBTMPL/ExtractConfiguration/Inputs:

Input Parameters
****************

.. _JOBTMPL/ExtractConfiguration/Input/ubuntu_image_version:

.. include:: ../_ubuntu_image_version.rst


.. _JOBTMPL/ExtractConfiguration/Input/python_version:

.. include:: ../_python_version.rst


.. _JOBTMPL/ExtractConfiguration/Input/coverage_config:

coverage_config
===============

:Type:            string
:Required:        no
:Default Value:   ``'pyproject.toml'``
:Possible Values: Any valid path to a :file:`pyproject.toml` file. |br|
                  Alternatively, path to a :file:`.coveragerc` file (deprecated).
:Description:     Path to a Python project configuration file for extraction of project settings.
:Example:
                  .. grid:: 2

                     .. grid-item::
                        :columns: 5

                        .. rubric:: Extracted values from :file:`pyproject.toml`

                        .. code-block:: toml

                           [tool.coverage.xml]
                           output = "report/coverage/coverage.xml"

                           [tool.coverage.json]
                           output = "report/coverage/coverage.json"

                           [tool.coverage.html]
                           directory = "report/coverage/html"
                           title="Code Coverage of myPackage"

                           [tool.mypy]
                           html_report = "report/typing/html"
                           junit_xml = "report/typing/StaticTypingSummary.xml"
                           cobertura_xml_report = "report/typing"

                           [tool.pyedaa-reports]
                           junit_xml = "report/unit/unittest.xml"

                           [tool.pytest]
                           junit_xml = "report/unit/UnittestReportSummary.xml"


.. _JOBTMPL/ExtractConfiguration/Secrets:

Secrets
*******

This job template needs no secrets.


.. _JOBTMPL/ExtractConfiguration/Outputs:

Outputs
*******

.. _JOBTMPL/ExtractConfiguration/Output/unittest_report_xml:

unittest_report_xml
===================

:Type:            string (JSON)
:Description:     Returns a string in JSON format containing the directory, the filename and the fullpath to the unit
                  test's report XML file created by :term:`pytest` in JUnit XML format.

                  The JSON object contains these fields:

                  :directory: Contains the directory where the unittest XML report file will be created. |br|
                              Example: :file:`reports/unit`
                  :filename:  Contains the filename of the unittest XML report file. |br|
                              Example: :file:`UnittestReportSummary.xml`
                  :fullpath:  Contains the path where the unittest XML report file will be created. |br|
                              This is the concatenation of both previous JSON fields. |br|
                              Example: :file:`reports/unit/UnittestReportSummary.xml`
:pyproject.toml:  Matching :file:`pyproject.toml` configuration for tool :term:`pytest`.

                  .. code-block:: toml

                     [tool.pytest]
                     junit_xml = "report/unit/UnittestReportSummary.xml"
:Example:
                  .. code-block:: json

                     { "directory": "reports/unit",
                       "filename":  "UnittestReportSummary.xml",
                       "fullpath":  "reports/unit/UnittestReportSummary.xml"
                     }
:Usage:
                  .. tab-set::

                     .. tab-item:: Forwarding complete JSON object
                        :sync: ForwardParam

                        .. code-block:: yaml

                           ConfigParams:
                             uses: pyTooling/Actions/.github/workflows/ExtractConfiguration.yml@r5

                           OtherJob:
                             uses: some/path/to/a/template@r5
                             needs:
                               - ConfigParams
                             with:
                               report: ${{ needs.ConfigParams.outputs.unittest_report_xml }}

                     .. tab-item:: Assembling new JSON object
                        :sync: AssembleParam

                        .. code-block:: yaml

                           ConfigParams:
                             uses: pyTooling/Actions/.github/workflows/ExtractConfiguration.yml@r5

                           OtherJob:
                             uses: some/path/to/a/template@r5
                             needs:
                               - ConfigParams
                             with:
                               report: >-
                                 { "dir":  "${{ fromJson(needs.ConfigParams.outputs.unittest_report_xml).directory }}",
                                   "file": "${{ fromJson(needs.ConfigParams.outputs.unittest_report_xml).filename }}"
                                 }

                     .. tab-item:: Using single field from JSON object
                        :sync: SingleFieldFromParam

                        .. code-block:: yaml

                           ConfigParams:
                             uses: pyTooling/Actions/.github/workflows/ExtractConfiguration.yml@r5

                           OtherJob:
                             uses: some/path/to/a/template@r5
                             needs:
                               - ConfigParams
                             with:
                               fullpath: ${{ fromJson(needs.ConfigParams.outputs.unittest_report_xml).fullpath }}


.. _JOBTMPL/ExtractConfiguration/Output/unittest_merged_report_xml:

unittest_merged_report_xml
==========================

:Type:            string (JSON)
:Description:     Returns a string in JSON format containing the directory, the filename and the fullpath to the merged
                  unittest report file in JUnit XML format created by :term:`pyEDAA.Reports`.

                  The JSON object contains these fields:

                  :directory: Contains the directory where the merged unittest XML report file will be created. |br|
                              Example: :file:`reports/unit`
                  :filename:  Contains the filename of the merged unittest XML report file. |br|
                              Example: :file:`unittest.xml`
                  :fullpath:  Contains the path where the merged unittest XML report file will be created. |br|
                              This is the concatenation of both previous JSON fields. |br|
                              Example: :file:`reports/unit/unittest.xml`
:pyproject.toml:  Matching :file:`pyproject.toml` configuration for tool :term:`pyEDAA.Reports`.

                  .. code-block:: toml

                     [tool.pyedaa-reports]
                     junit_xml = "report/unit/unittest.xml"
:Example:
                  .. code-block:: json

                     { "directory": "reports/unit",
                       "filename":  "unittest.xml",
                       "fullpath":  "reports/unit/unittest.xml"
                     }
:Usage:
                  .. tab-set::

                     .. tab-item:: Forwarding complete JSON object
                        :sync: ForwardParam

                        .. code-block:: yaml

                           ConfigParams:
                             uses: pyTooling/Actions/.github/workflows/ExtractConfiguration.yml@r5

                           OtherJob:
                             uses: some/path/to/a/template@r5
                             needs:
                               - ConfigParams
                             with:
                               report: ${{ needs.ConfigParams.outputs.unittest_merged_report_xml }}

                     .. tab-item:: Assembling new JSON object
                        :sync: AssembleParam

                        .. code-block:: yaml

                           ConfigParams:
                             uses: pyTooling/Actions/.github/workflows/ExtractConfiguration.yml@r5

                           OtherJob:
                             uses: some/path/to/a/template@r5
                             needs:
                               - ConfigParams
                             with:
                               report: >-
                                 { "dir":  "${{ fromJson(needs.ConfigParams.outputs.unittest_merged_report_xml).directory }}",
                                   "file": "${{ fromJson(needs.ConfigParams.outputs.unittest_merged_report_xml).filename }}"
                                 }

                     .. tab-item:: Using single field from JSON object
                        :sync: SingleFieldFromParam

                        .. code-block:: yaml

                           ConfigParams:
                             uses: pyTooling/Actions/.github/workflows/ExtractConfiguration.yml@r5

                           OtherJob:
                             uses: some/path/to/a/template@r5
                             needs:
                               - ConfigParams
                             with:
                               fullpath: ${{ fromJson(needs.ConfigParams.outputs.unittest_merged_report_xml).fullpath }}


.. _JOBTMPL/ExtractConfiguration/Output/coverage_report_html:

coverage_report_html
====================

:Type:            string (JSON)
:Description:     Returns a string in JSON format containing the directory and the full path, where the code coverage
                  HTML report will be generated by :term:`Coverage.py`.

                  The JSON object contains these fields:

                  :directory: Contains the directory where the code coverage report in HTML format will be created. |br|
                              Example: :file:`report/coverage/html`
                  :fullpath:  Contains the path where the code coverage report in HTML format will be created. |br|
                              This is the same as the previous JSON field. |br|
                              Example: :file:`report/coverage/html`
:pyproject.toml:  Matching :file:`pyproject.toml` configuration for tool :term:`Coverage.py`.

                  .. code-block:: toml

                     [tool.coverage.html]
                     directory = "report/coverage/html"
                     title="Code Coverage of pyDummy"
:Example:
                  .. code-block:: json

                     { "directory": "report/coverage/html",
                       "fullpath":  "report/coverage/html"
                     }
:Usage:
                  .. tab-set::

                     .. tab-item:: Forwarding complete JSON object
                        :sync: ForwardParam

                        .. code-block:: yaml

                           ConfigParams:
                             uses: pyTooling/Actions/.github/workflows/ExtractConfiguration.yml@r5

                           OtherJob:
                             uses: some/path/to/a/template@r5
                             needs:
                               - ConfigParams
                             with:
                               report: ${{ needs.ConfigParams.outputs.coverage_report_html }}

                     .. tab-item:: Assembling new JSON object
                        :sync: AssembleParam

                        .. code-block:: yaml

                           ConfigParams:
                             uses: pyTooling/Actions/.github/workflows/ExtractConfiguration.yml@r5

                           OtherJob:
                             uses: some/path/to/a/template@r5
                             needs:
                               - ConfigParams
                             with:
                               report: >-
                                 { "dir":  "${{ fromJson(needs.ConfigParams.outputs.coverage_report_html).directory }}",
                                   "file": "${{ fromJson(needs.ConfigParams.outputs.coverage_report_html).filename }}"
                                 }

                     .. tab-item:: Using single field from JSON object
                        :sync: SingleFieldFromParam

                        .. code-block:: yaml

                           ConfigParams:
                             uses: pyTooling/Actions/.github/workflows/ExtractConfiguration.yml@r5

                           OtherJob:
                             uses: some/path/to/a/template@r5
                             needs:
                               - ConfigParams
                             with:
                               fullpath: ${{ fromJson(needs.ConfigParams.outputs.coverage_report_html).fullpath }}


.. _JOBTMPL/ExtractConfiguration/Output/coverage_report_xml:

coverage_report_xml
===================

:Type:            string (JSON)
:Description:     Returns a string in JSON format containing the directory, the filename and the fullpath to the code
                  coverage XML report file in Cobertura XML format created by :term:`Coverage.py`.

                  The JSON object contains these fields:

                  :directory: Contains the directory where the code coverage XML report file will be created. |br|
                              Example: :file:`reports/unit`
                  :filename:  Contains the filename of the code coverage XML report file. |br|
                              Example: :file:`unittest.xml`
                  :fullpath:  Contains the path where the code coverage XML report file will be created. |br|
                              This is the concatenation of both previous JSON fields. |br|
                              Example: :file:`reports/unit/unittest.xml`
:pyproject.toml:  Matching :file:`pyproject.toml` configuration for tool :term:`Coverage.py`.

                  .. code-block:: toml

                     [tool.coverage.xml]
                     output = "report/coverage/coverage.xml"
:Example:
                  .. code-block:: json

                     { "directory": "reports/coverage",
                       "filename":  "coverage.xml",
                       "fullpath":  "reports/coverage/coverage.xml"
                     }
:Usage:
                  .. tab-set::

                     .. tab-item:: Forwarding complete JSON object
                        :sync: ForwardParam

                        .. code-block:: yaml

                           ConfigParams:
                             uses: pyTooling/Actions/.github/workflows/ExtractConfiguration.yml@r5

                           OtherJob:
                             uses: some/path/to/a/template@r5
                             needs:
                               - ConfigParams
                             with:
                               report: ${{ needs.ConfigParams.outputs.coverage_report_xml }}

                     .. tab-item:: Assembling new JSON object
                        :sync: AssembleParam

                        .. code-block:: yaml

                           ConfigParams:
                             uses: pyTooling/Actions/.github/workflows/ExtractConfiguration.yml@r5

                           OtherJob:
                             uses: some/path/to/a/template@r5
                             needs:
                               - ConfigParams
                             with:
                               report: >-
                                 { "dir":  "${{ fromJson(needs.ConfigParams.outputs.coverage_report_xml).directory }}",
                                   "file": "${{ fromJson(needs.ConfigParams.outputs.coverage_report_xml).filename }}"
                                 }

                     .. tab-item:: Using single field from JSON object
                        :sync: SingleFieldFromParam

                        .. code-block:: yaml

                           ConfigParams:
                             uses: pyTooling/Actions/.github/workflows/ExtractConfiguration.yml@r5

                           OtherJob:
                             uses: some/path/to/a/template@r5
                             needs:
                               - ConfigParams
                             with:
                               fullpath: ${{ fromJson(needs.ConfigParams.outputs.coverage_report_xml).fullpath }}


.. _JOBTMPL/ExtractConfiguration/Output/coverage_report_json:

coverage_report_json
====================

:Type:            string (JSON)
:Description:     Returns a string in JSON format containing the directory, the filename and the fullpath to the code
                  coverage JSON report file created by :term:`Coverage.py`.

                  The JSON object contains these fields:

                  :directory: Contains the directory where the code coverage JSON report file will be created. |br|
                              Example: :file:`reports/unit`
                  :filename:  Contains the filename of the code coverage JSON report file. |br|
                              Example: :file:`unittest.json`
                  :fullpath:  Contains the path where the code coverage JSON report file will be created. |br|
                              This is the concatenation of both previous JSON fields. |br|
                              Example: :file:`reports/unit/unittest.json`
:pyproject.toml:  Matching :file:`pyproject.toml` configuration for tool :term:`Coverage.py`.

                  .. code-block:: toml

                     [tool.coverage.json]
                     output = "report/coverage/coverage.json"
:Example:
                  .. code-block:: json

                     { "directory": "reports/coverage",
                       "filename":  "coverage.json",
                       "fullpath":  "reports/coverage/coverage.json"
                     }
:Usage:
                  .. tab-set::

                     .. tab-item:: Forwarding complete JSON object
                        :sync: ForwardParam

                        .. code-block:: yaml

                           ConfigParams:
                             uses: pyTooling/Actions/.github/workflows/ExtractConfiguration.yml@r5

                           OtherJob:
                             uses: some/path/to/a/template@r5
                             needs:
                               - ConfigParams
                             with:
                               report: ${{ needs.ConfigParams.outputs.coverage_report_json }}

                     .. tab-item:: Assembling new JSON object
                        :sync: AssembleParam

                        .. code-block:: yaml

                           ConfigParams:
                             uses: pyTooling/Actions/.github/workflows/ExtractConfiguration.yml@r5

                           OtherJob:
                             uses: some/path/to/a/template@r5
                             needs:
                               - ConfigParams
                             with:
                               report: >-
                                 { "dir":  "${{ fromJson(needs.ConfigParams.outputs.coverage_report_json).directory }}",
                                   "file": "${{ fromJson(needs.ConfigParams.outputs.coverage_report_json).filename }}"
                                 }

                     .. tab-item:: Using single field from JSON object
                        :sync: SingleFieldFromParam

                        .. code-block:: yaml

                           ConfigParams:
                             uses: pyTooling/Actions/.github/workflows/ExtractConfiguration.yml@r5

                           OtherJob:
                             uses: some/path/to/a/template@r5
                             needs:
                               - ConfigParams
                             with:
                               fullpath: ${{ fromJson(needs.ConfigParams.outputs.coverage_report_json).fullpath }}


.. _JOBTMPL/ExtractConfiguration/Output/typing_report_cobertura:

typing_report_cobertura
=======================

:Type:            string (JSON)
:Description:     Returns a string in JSON format containing the directory, the filename and the fullpath to the static
                  type checking report file in Cobertura format created by :term:`mypy`.

                  The JSON object contains these fields:

                  :directory: Contains the directory where the type checking XML report file will be created. |br|
                              Example: :file:`reports/typing`
                  :filename:  Contains the filename of the type checking XML report file. |br|
                              Example: :file:`cobertura.xml`
                  :fullpath:  Contains the path where the type checking XML report file will be created. |br|
                              This is the concatenation of both previous JSON fields. |br|
                              Example: :file:`reports/typing/cobertura.xml`
:pyproject.toml:  Matching :file:`pyproject.toml` configuration for tool :term:`mypy`.

                  .. code-block:: toml

                     [tool.mypy]
                     cobertura_xml_report = "report/typing"
:Example:
                  .. code-block:: json

                     { "directory": "reports/typing",
                       "filename":  "cobertura.xml",
                       "fullpath":  "reports/typing/cobertura.xml"
                     }
:Usage:
                  .. tab-set::

                     .. tab-item:: Forwarding complete JSON object
                        :sync: ForwardParam

                        .. code-block:: yaml

                           ConfigParams:
                             uses: pyTooling/Actions/.github/workflows/ExtractConfiguration.yml@r5

                           OtherJob:
                             uses: some/path/to/a/template@r5
                             needs:
                               - ConfigParams
                             with:
                               report: ${{ needs.ConfigParams.outputs.typing_report_cobertura }}

                     .. tab-item:: Assembling new JSON object
                        :sync: AssembleParam

                        .. code-block:: yaml

                           ConfigParams:
                             uses: pyTooling/Actions/.github/workflows/ExtractConfiguration.yml@r5

                           OtherJob:
                             uses: some/path/to/a/template@r5
                             needs:
                               - ConfigParams
                             with:
                               report: >-
                                 { "dir":  "${{ fromJson(needs.ConfigParams.outputs.typing_report_cobertura).directory }}",
                                   "file": "${{ fromJson(needs.ConfigParams.outputs.typing_report_cobertura).filename }}"
                                 }

                     .. tab-item:: Using single field from JSON object
                        :sync: SingleFieldFromParam

                        .. code-block:: yaml

                           ConfigParams:
                             uses: pyTooling/Actions/.github/workflows/ExtractConfiguration.yml@r5

                           OtherJob:
                             uses: some/path/to/a/template@r5
                             needs:
                               - ConfigParams
                             with:
                               fullpath: ${{ fromJson(needs.ConfigParams.outputs.typing_report_cobertura).fullpath }}


.. _JOBTMPL/ExtractConfiguration/Output/typing_report_junit:

typing_report_junit
===================

:Type:            string (JSON)
:Description:     Returns a string in JSON format containing the directory, the filename and the fullpath to the static
                  type checking report file in JUnit XML format created by :term:`mypy`.

                  The JSON object contains these fields:

                  :directory: Contains the directory where the static typing JUnit XML report file will be created. |br|
                              Example: :file:`reports/typing`
                  :filename:  Contains the filename of the static typing JUnit XML report file. |br|
                              Example: :file:`StaticTypingSummary.xml`
                  :fullpath:  Contains the path where the cstatic typing JUnit XML report file will be created. |br|
                              This is the concatenation of both previous JSON fields. |br|
                              Example: :file:`reports/typing/StaticTypingSummary.xml`
:pyproject.toml:  Matching :file:`pyproject.toml` configuration for tool :term:`mypy`.

                  .. code-block:: toml

                     [tool.mypy]
                     junit_xml = "report/typing/StaticTypingSummary.xml"
:Example:
                  .. code-block:: json

                     { "directory": "reports/typing",
                       "filename":  "StaticTypingSummary.xml",
                       "fullpath":  "reports/typing/StaticTypingSummary.xml"
                     }
:Usage:
                  .. tab-set::

                     .. tab-item:: Forwarding complete JSON object
                        :sync: ForwardParam

                        .. code-block:: yaml

                           ConfigParams:
                             uses: pyTooling/Actions/.github/workflows/ExtractConfiguration.yml@r5

                           OtherJob:
                             uses: some/path/to/a/template@r5
                             needs:
                               - ConfigParams
                             with:
                               report: ${{ needs.ConfigParams.outputs.typing_report_junit }}

                     .. tab-item:: Assembling new JSON object
                        :sync: AssembleParam

                        .. code-block:: yaml

                           ConfigParams:
                             uses: pyTooling/Actions/.github/workflows/ExtractConfiguration.yml@r5

                           OtherJob:
                             uses: some/path/to/a/template@r5
                             needs:
                               - ConfigParams
                             with:
                               report: >-
                                 { "dir":  "${{ fromJson(needs.ConfigParams.outputs.typing_report_junit).directory }}",
                                   "file": "${{ fromJson(needs.ConfigParams.outputs.typing_report_junit).filename }}"
                                 }

                     .. tab-item:: Using single field from JSON object
                        :sync: SingleFieldFromParam

                        .. code-block:: yaml

                           ConfigParams:
                             uses: pyTooling/Actions/.github/workflows/ExtractConfiguration.yml@r5

                           OtherJob:
                             uses: some/path/to/a/template@r5
                             needs:
                               - ConfigParams
                             with:
                               fullpath: ${{ fromJson(needs.ConfigParams.outputs.typing_report_junit).fullpath }}


.. _JOBTMPL/ExtractConfiguration/Output/typing_report_html:

typing_report_html
==================

:Type:            string (JSON)
:Description:     Returns a string in JSON format containing the directory, the filename and the fullpath to the static
                  type checking report in HTML format created by :term:`mypy`.

                  The JSON object contains these fields:

                  :directory: Contains the directory where the static typing HTML report will be created. |br|
                              Example: :file:`reports/typing/html`
                  :fullpath:  Contains the path where the static typing HTML report will be created. |br|
                              This is the same as the previous JSON field. |br|
                              Example: :file:`reports/typing/html`
:pyproject.toml:  Matching :file:`pyproject.toml` configuration for tool :term:`mypy`.

                  .. code-block:: toml

                     [tool.mypy]
                     html_report = "report/typing/html"
:Example:
                  .. code-block:: json

                     { "directory": "reports/typing/html",
                       "fullpath":  "reports/typing/html"
                     }
:Usage:
                  .. tab-set::

                     .. tab-item:: Forwarding complete JSON object
                        :sync: ForwardParam

                        .. code-block:: yaml

                           ConfigParams:
                             uses: pyTooling/Actions/.github/workflows/ExtractConfiguration.yml@r5

                           OtherJob:
                             uses: some/path/to/a/template@r5
                             needs:
                               - ConfigParams
                             with:
                               report: ${{ needs.ConfigParams.outputs.typing_report_html }}

                     .. tab-item:: Assembling new JSON object
                        :sync: AssembleParam

                        .. code-block:: yaml

                           ConfigParams:
                             uses: pyTooling/Actions/.github/workflows/ExtractConfiguration.yml@r5

                           OtherJob:
                             uses: some/path/to/a/template@r5
                             needs:
                               - ConfigParams
                             with:
                               report: >-
                                 { "dir":  "${{ fromJson(needs.ConfigParams.outputs.typing_report_html).directory }}",
                                   "file": "${{ fromJson(needs.ConfigParams.outputs.typing_report_html).filename }}"
                                 }

                     .. tab-item:: Using single field from JSON object
                        :sync: SingleFieldFromParam

                        .. code-block:: yaml

                           ConfigParams:
                             uses: pyTooling/Actions/.github/workflows/ExtractConfiguration.yml@r5

                           OtherJob:
                             uses: some/path/to/a/template@r5
                             needs:
                               - ConfigParams
                             with:
                               fullpath: ${{ fromJson(needs.ConfigParams.outputs.typing_report_html).fullpath }}


.. _JOBTMPL/ExtractConfiguration/Optimizations:

Optimizations
*************

This template offers no optimizations (reduced job runtime).

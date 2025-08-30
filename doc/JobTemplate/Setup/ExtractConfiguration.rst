.. _JOBTMPL/ExtractConfiguration:

ExtractConfiguration
####################

The ``ExtractConfiguration`` job template is a .....



.. topic:: Features

   * Concatenate :ref:`JOBTMPL/ExtractConfiguration/Input/package_namespace` and :ref:`JOBTMPL/ExtractConfiguration/Input/package_name`
     to :ref:`JOBTMPL/ExtractConfiguration/Output/package_fullname` (with dot) and :ref:`JOBTMPL/ExtractConfiguration/Output/package_directory`
     (with slash).
   * Provide commands to prepare the source code directory structure suitable for mypy.
   * Extract the unittest XML report file (pytest JUnit XML) as directory name, filename and full path from :file:`pyproject.toml`.
   * Extract the merged unittest XML report file as directory name, filename and full path from :file:`pyproject.toml`.
   * Extract code coverage report HTML directory from :file:`pyproject.toml`.
   * Extract code coverage XML report file as directory name, filename and full path from :file:`pyproject.toml`.
   * Extract code coverage JSON report file as directory name, filename and full path from :file:`pyproject.toml`.

.. topic:: Behavior:

   .. todo:: ExtractConfiguration:Behavior needs documentation.

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

The following instantiation example creates a job ``ConfigParams`` derived from job template ``ExtractConfiguration``
version ``@r5``. It only requires a :ref:`JOBTMPL/ExtractConfiguration/Input/package_name` parameter to extract unit
test (pytest) and code coverage (Coverage.py) settings.

.. code-block:: yaml

   name: Pipeline

   on:
     push:
     workflow_dispatch:

   jobs:
     ConfigParams:
       uses: pyTooling/Actions/.github/workflows/ExtractConfiguration.yml@r5
       with:
         package_name: myPackage

     UnitTesting:
       uses: pyTooling/Actions/.github/workflows/UnitTesting.yml@r5
       needs:
         - ConfigParams
       with:
         unittest_report_xml_directory:  ${{ needs.ConfigParams.outputs.unittest_report_xml_directory }}
         unittest_report_xml_filename:   ${{ needs.ConfigParams.outputs.unittest_report_xml_filename }}
         coverage_report_xml_directory:  ${{ needs.ConfigParams.outputs.coverage_report_xml_directory }}
         coverage_report_xml_filename:   ${{ needs.ConfigParams.outputs.coverage_report_xml_filename }}
         coverage_report_json_directory: ${{ needs.ConfigParams.outputs.coverage_report_json_directory }}
         coverage_report_json_filename:  ${{ needs.ConfigParams.outputs.coverage_report_json_filename }}
         coverage_report_html_directory: ${{ needs.ConfigParams.outputs.coverage_report_html_directory }}


.. seealso::

   :ref:`JOBTMPL/UnitTesting`
     ``UnitTesting`` is usualy
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
| :ref:`JOBTMPL/ExtractConfiguration/Input/package_namespace`         | no       | string   | ``''``                                                            |
+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/ExtractConfiguration/Input/package_name`              | yes      | string   | — — — —                                                           |
+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/ExtractConfiguration/Input/coverage_config`           | no       | string   | ``'pyproject.toml'``                                              |
+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+

.. rubric:: Goto :ref:`secrets <JOBTMPL/ExtractConfiguration/Secrets>`

This job template needs no secrets.

.. rubric:: Goto :ref:`output parameters <JOBTMPL/ExtractConfiguration/Outputs>`

+---------------------------------------------------------------------------------+----------+-------------------------------------------------------------------+
| Result Name                                                                     | Type     | Description                                                       |
+=================================================================================+==========+===================================================================+
| :ref:`JOBTMPL/ExtractConfiguration/Output/package_fullname`                     | string   |                                                                   |
+---------------------------------------------------------------------------------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/ExtractConfiguration/Output/package_directory`                    | string   |                                                                   |
+---------------------------------------------------------------------------------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/ExtractConfiguration/Output/mypy_prepare_command`                 | string   |                                                                   |
+---------------------------------------------------------------------------------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/ExtractConfiguration/Output/unittest_report_xml_directory`        | string   |                                                                   |
+---------------------------------------------------------------------------------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/ExtractConfiguration/Output/unittest_report_xml_filename`         | string   |                                                                   |
+---------------------------------------------------------------------------------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/ExtractConfiguration/Output/unittest_report_xml`                  | string   |                                                                   |
+---------------------------------------------------------------------------------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/ExtractConfiguration/Output/unittest_merged_report_xml_directory` | string   |                                                                   |
+---------------------------------------------------------------------------------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/ExtractConfiguration/Output/unittest_merged_report_xml_filename`  | string   |                                                                   |
+---------------------------------------------------------------------------------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/ExtractConfiguration/Output/unittest_merged_report_xml`           | string   |                                                                   |
+---------------------------------------------------------------------------------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/ExtractConfiguration/Output/coverage_report_html_directory`       | string   |                                                                   |
+---------------------------------------------------------------------------------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/ExtractConfiguration/Output/coverage_report_xml_directory`        | string   |                                                                   |
+---------------------------------------------------------------------------------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/ExtractConfiguration/Output/coverage_report_xml_filename`         | string   |                                                                   |
+---------------------------------------------------------------------------------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/ExtractConfiguration/Output/coverage_report_xml`                  | string   |                                                                   |
+---------------------------------------------------------------------------------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/ExtractConfiguration/Output/coverage_report_json_directory`       | string   |                                                                   |
+---------------------------------------------------------------------------------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/ExtractConfiguration/Output/coverage_report_json_filename`        | string   |                                                                   |
+---------------------------------------------------------------------------------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/ExtractConfiguration/Output/coverage_report_json`                 | string   |                                                                   |
+---------------------------------------------------------------------------------+----------+-------------------------------------------------------------------+


.. _JOBTMPL/ExtractConfiguration/Inputs:

Input Parameters
****************

.. _JOBTMPL/ExtractConfiguration/Input/ubuntu_image_version:

ubuntu_image_version
====================

:Type:            string
:Required:        no
:Default Value:   ``'24.04'``
:Possible Values: See `actions/runner-images - Available Images <https://github.com/actions/runner-images?tab=readme-ov-file#available-images>`__
                  for available Ubuntu image versions.
:Description:     Version of the Ubuntu image used to run this job.

                  .. note::

                     Unfortunately, GitHub Actions has only a `limited set of functions <https://docs.github.com/en/actions/reference/workflows-and-actions/expressions#functions>`__,
                     thus, the usual Ubuntu image name like ``'ubuntu-24.04'`` can't be split into image name and image
                     version.


.. _JOBTMPL/ExtractConfiguration/Input/python_version:

python_version
==============

:Type:            string
:Required:        no
:Default Value:   ``'3.13'``
:Possible Values: Any valid Python version conforming to the pattern ``<major>.<minor>`` or ``pypy-<major>.<minor>``. |br|
                  See `actions/python-versions - available Python versions <https://github.com/actions/python-versions>`__
                  and `actions/setup-python - configurable Python versions <https://github.com/actions/setup-python>`__.
:Description:     Python version used to run Python code in this job.


.. _JOBTMPL/ExtractConfiguration/Input/package_namespace:

package_namespace
=================

:Type:            string
:Required:        no
:Default Value:   ``''``
:Possible Values: Any valid Python namespace.
:Description:     In case the package is a Python namespace package, the name of the library's or package's namespace
                  needs to be specified using this parameter. |br|
                  In case of a simple Python package, this parameter must be specified as an empty string (``''``),
                  which is the default.
:Example:
                  .. grid:: 2

                     .. grid-item::
                        :columns: 5

                        .. rubric:: Example Instantiation

                        .. code-block:: yaml

                           name: Pipeline

                           jobs:
                             ConfigParams:
                               uses: pyTooling/Actions/.github/workflows/ExtractConfiguration.yml@r5
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


.. _JOBTMPL/ExtractConfiguration/Input/package_name:

package_name
============

:Type:            string
:Required:        no
:Default Value:   ``''``
:Possible Values: Any valid Python package name.
:Description:     In case of a simple Python package, this package's name is specified using this parameter. |br|
                  In case the package is a Python namespace package, the parameter
                  :ref:`JOBTMPL/ExtractConfiguration/Input/package_namespace` must be specified, too.
:Example:
                  .. grid:: 2

                     .. grid-item::
                        :columns: 5

                        .. rubric:: Example Instantiation

                        .. code-block:: yaml

                           name: Pipeline

                           jobs:
                             ConfigParams:
                               uses: pyTooling/Actions/.github/workflows/ExtractConfiguration.yml@r5
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

                           [tool.pytest]
                           junit_xml = "report/unit/UnittestReportSummary.xml"

                           [tool.pyedaa-reports]
                           junit_xml = "report/unit/unittest.xml"

                           [tool.coverage.xml]
                           output = "report/coverage/coverage.xml"

                           [tool.coverage.json]
                           output = "report/coverage/coverage.json"

                           [tool.coverage.html]
                           directory = "report/coverage/html"
                           title="Code Coverage of pyDummy"


.. _JOBTMPL/ExtractConfiguration/Secrets:

Secrets
*******

This job template needs no secrets.


.. _JOBTMPL/ExtractConfiguration/Outputs:

Outputs
*******

.. _JOBTMPL/ExtractConfiguration/Output/package_fullname:

package_fullname
================

:Type:            string
:Description:     Returns the full package name composed from :ref:`JOBTMPL/ExtractConfiguration/Input/package_namespace`
                  and :ref:`JOBTMPL/ExtractConfiguration/Input/package_name`.
:Example:         ``myFramework.Extension``


.. _JOBTMPL/ExtractConfiguration/Output/package_directory:

package_directory
=================

:Type:            string
:Description:     Returns the full package path composed from :ref:`JOBTMPL/ExtractConfiguration/Input/package_namespace`
                  and :ref:`JOBTMPL/ExtractConfiguration/Input/package_name`.
:Example:         ``myFramework/Extension``


.. _JOBTMPL/ExtractConfiguration/Output/mypy_prepare_command:

mypy_prepare_command
====================

:Type:            string
:Description:     Returns a preparation command for `mypy <https://mypy-lang.org/>`__. |br|
                  In case the Python package is a namespace package, an :file:`__init__.py` must be created, otherwise
                  mypy has problems analyzing the namespace package.
:Example:         ``touch myFramework/__init__.py``

.. _JOBTMPL/ExtractConfiguration/Output/unittest_report_xml_directory:

unittest_report_xml_directory
=============================

:Type:            string
:Description:     Returns the directory where the unittest XML report file (`pytest <https://docs.pytest.org/>`__ JUnit XML)
                  will be created. |br|
                  This is the directory portion of :ref:`JOBTMPL/ExtractConfiguration/Output/unittest_report_xml`.
:Example:         :file:`reports/unit`
:pyproject.toml:
                  .. code-block:: toml

                     [tool.pytest]
                     junit_xml = "report/unit/UnittestReportSummary.xml"


.. _JOBTMPL/ExtractConfiguration/Output/unittest_report_xml_filename:

unittest_report_xml_filename
============================

:Type:            string
:Description:     Returns the filename of the unittest XML report file (`pytest <https://docs.pytest.org/>`__ JUnit XML). |br|
                  This is the filename portion of :ref:`JOBTMPL/ExtractConfiguration/Output/unittest_report_xml`.
:Example:         :file:`UnittestReportSummary.xml`
:pyproject.toml:
                  .. code-block:: toml

                     [tool.pytest]
                     junit_xml = "report/unit/UnittestReportSummary.xml"


.. _JOBTMPL/ExtractConfiguration/Output/unittest_report_xml:

unittest_report_xml
===================

:Type:            string
:Description:     Returns the path where the unittest XML report file (`pytest <https://docs.pytest.org/>`__ JUnit XML)
                  will be created. |br|
                  This is the concatenation of :ref:`directory portion <JOBTMPL/ExtractConfiguration/Output/unittest_report_xml_directory>`
                  and :ref:`filename portion <JOBTMPL/ExtractConfiguration/Output/unittest_report_xml_filename>`.
:Example:         :file:`reports/unit/UnittestReportSummary.xml`
:pyproject.toml:
                  .. code-block:: toml

                     [tool.pytest]
                     junit_xml = "report/unit/UnittestReportSummary.xml"


.. _JOBTMPL/ExtractConfiguration/Output/unittest_merged_report_xml_directory:

unittest_merged_report_xml_directory
====================================

:Type:            string
:Description:     Returns the directory where the merged unittest XML report file
                  (`pyedaa-reports <https://edaa-org.github.io/pyEDAA.Reports/>`__ JUnit XML) will be created. |br|
                  This is the directory portion of :ref:`JOBTMPL/ExtractConfiguration/Output/unittest_merged_report_xml`.
:Example:         :file:`reports/unit`
:pyproject.toml:
                  .. code-block:: toml

                     [tool.pyedaa-reports]
                     junit_xml = "report/unit/unittest.xml"


.. _JOBTMPL/ExtractConfiguration/Output/unittest_merged_report_xml_filename:

unittest_merged_report_xml_filename
===================================

:Type:            string
:Description:     Returns the filename of the merged unittest XML report
                  (`pyedaa-reports <https://edaa-org.github.io/pyEDAA.Reports/>`__ JUnit XML). |br|
                  This is the filename portion of :ref:`JOBTMPL/ExtractConfiguration/Output/unittest_merged_report_xml`.
:Example:         :file:`unittest.xml`
:pyproject.toml:
                  .. code-block:: toml

                     [tool.pyedaa-reports]
                     junit_xml = "report/unit/unittest.xml"


.. _JOBTMPL/ExtractConfiguration/Output/unittest_merged_report_xml:

unittest_merged_report_xml
==========================

:Type:            string
:Description:     Returns the path where the merged unittest XML report file (`pyedaa-reports <https://edaa-org.github.io/pyEDAA.Reports/>`__ JUnit XML)
                  will be created. |br|
                  This is the concatenation of :ref:`directory portion <JOBTMPL/ExtractConfiguration/Output/unittest_merged_report_xml_directory>`
                  and :ref:`filename portion <JOBTMPL/ExtractConfiguration/Output/unittest_merged_report_xml_filename>`.
:Example:         :file:`report/unit/unittest.xml`
:pyproject.toml:
                  .. code-block:: toml

                     [tool.pyedaa-reports]
                     junit_xml = "report/unit/unittest.xml"


.. _JOBTMPL/ExtractConfiguration/Output/coverage_report_html_directory:

coverage_report_html_directory
==============================

:Type:            string
:Description:     Returns the directory where the code coverage HTML report (`Coverage.py <https://coverage.readthedocs.io/>`__)
                  will be generated.
:Example:         :file:`report/coverage/html`
:pyproject.toml:
                  .. code-block:: toml

                     [tool.coverage.html]
                     directory = "report/coverage/html"
                     title="Code Coverage of pyDummy"


.. _JOBTMPL/ExtractConfiguration/Output/coverage_report_xml_directory:

coverage_report_xml_directory
=============================

:Type:            string
:Description:     Returns the directory where the code coverage XML report file (`Coverage.py <https://coverage.readthedocs.io/>`__)
                  will be created. |br|
                  This is the directory portion of :ref:`JOBTMPL/ExtractConfiguration/Output/coverage_report_xml`.
:Example:         :file:`reports/coverage`
:pyproject.toml:
                  .. code-block:: toml

                     [tool.coverage.xml]
                     output = "report/coverage/coverage.xml"


.. _JOBTMPL/ExtractConfiguration/Output/coverage_report_xml_filename:

coverage_report_xml_filename
============================

:Type:            string
:Description:     Returns the filename of the code coverage XML report file (`Coverage.py <https://coverage.readthedocs.io/>`__). |br|
                  This is the filename portion of :ref:`JOBTMPL/ExtractConfiguration/Output/coverage_report_xml`.
:Example:         :file:`coverage.xml`
:pyproject.toml:
                  .. code-block:: toml

                     [tool.coverage.xml]
                     output = "report/coverage/coverage.xml"


.. _JOBTMPL/ExtractConfiguration/Output/coverage_report_xml:

coverage_report_xml
===================

:Type:            string
:Description:     Returns the path where the code coverage XML report file (`Coverage.py <https://coverage.readthedocs.io/>`__)
                  will be created. |br|
                  This is the concatenation of :ref:`directory portion <JOBTMPL/ExtractConfiguration/Output/coverage_report_xml_directory>`
                  and :ref:`filename portion <JOBTMPL/ExtractConfiguration/Output/coverage_report_xml_filename>`.
:Example:         :file:`report/coverage/coverage.xml`
:pyproject.toml:
                  .. code-block:: toml

                     [tool.coverage.xml]
                     output = "report/coverage/coverage.xml"


.. _JOBTMPL/ExtractConfiguration/Output/coverage_report_json_directory:

coverage_report_json_directory
==============================

:Type:            string
:Description:     Returns the directory where the code coverage JSON report file (`Coverage.py <https://coverage.readthedocs.io/>`__)
                  will be created. |br|
                  This is the directory portion of :ref:`JOBTMPL/ExtractConfiguration/Output/coverage_report_json`.
:Example:         :file:`reports/coverage`
:pyproject.toml:
                  .. code-block:: toml

                     [tool.coverage.json]
                     output = "report/coverage/coverage.json"


.. _JOBTMPL/ExtractConfiguration/Output/coverage_report_json_filename:

coverage_report_json_filename
=============================

:Type:            string
:Description:     Returns the filename of the code coverage JSON report file (`Coverage.py <https://coverage.readthedocs.io/>`__). |br|
                  This is the filename portion of :ref:`JOBTMPL/ExtractConfiguration/Output/coverage_report_json`.
:Example:         :file:`coverage.json`
:pyproject.toml:
                  .. code-block:: toml

                     [tool.coverage.json]
                     output = "report/coverage/coverage.json"


.. _JOBTMPL/ExtractConfiguration/Output/coverage_report_json:

coverage_report_json
====================

:Type:            string
:Description:     Returns the path where the code coverage JSON report file (`Coverage.py <https://coverage.readthedocs.io/>`__)
                  will be created. |br|
                  This is the concatenation of :ref:`directory portion <JOBTMPL/ExtractConfiguration/Output/coverage_report_json_directory>`
                  and :ref:`filename portion <JOBTMPL/ExtractConfiguration/Output/coverage_report_json_filename>`.
:Example:         :file:`report/coverage/coverage.json`
:pyproject.toml:
                  .. code-block:: toml

                     [tool.coverage.json]
                     output = "report/coverage/coverage.json"


.. _JOBTMPL/LatexDocumentation/Optimizations:

Optimizations
*************

This template offers no optimizations (reduced job runtime).

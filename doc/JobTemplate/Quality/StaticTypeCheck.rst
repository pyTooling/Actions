.. _JOBTMPL/StaticTypeCheck:
.. index::
   single: mypy; StaticTypeCheck Template
   single: GitHub Action Reusable Workflow; StaticTypeCheck Template

StaticTypeCheck
###############

This job template runs a static type check using :term:`mypy` and collects the results. These results can be converted
to a HTML report and uploaded as an artifact.

.. topic:: Features

   * Run static type check using :term:`mypy`.

.. topic:: Behavior

   1. Checkout repository
   2. Setup Python and install dependencies
   3. Run type checking.
   4. Upload type checking report as an artifact

.. topic:: Job Execution

   .. image:: ../../_static/pyTooling-Actions-StaticTypeCheck.png
      :width: 400px

.. topic:: Dependencies

   * :gh:`actions/checkout`
   * :gh:`actions/setup-python`
   * pip

     * Python packages specified via :ref:`JOBTMPL/StaticTypeCheck/Input/requirements`.

   * :gh:`pyTooling/upload-artifact`

     * :gh:`actions/upload-artifact`


.. _JOBTMPL/StaticTypeCheck/Instantiation:

Instantiation
*************

Simple Example
==============

This example runs mypy for the Python package ``myPackage`` according to the configuration stored in
:file:`pyproject.toml`. It prints a report into the job's log. In addition is generates a report in HTML format into the
directory ``report/typing``.

.. grid:: 2

   .. grid-item::
      :columns: 6

      .. code-block:: yaml

         jobs:
           StaticTypeCheck:
             uses: pyTooling/Actions/.github/workflows/StaticTypeCheck.yml@r6
             with:
               cobertura_artifact: 'TypeChecking-Cobertura'
               junit_artifact:     'TypeChecking-JUnit'
               html_artifact:      'TypeChecking-HTML'

   .. grid-item::
      :columns: 6

      .. code-block:: toml

         [tool.mypy]
         packages = ["myPackage"]
         strict = true
         pretty = true

         html_report = "report/typing/html"
         junit_xml = "report/typing/StaticTypingSummary.xml"
         cobertura_xml_report = "report/typing"


Complex Example
===============

To ease the handling of mypy parameters stored in :file:`pyproject.toml`, the :ref:`JOBTMPL/ExtractConfiguration` is
used to extract the set configuration parameters for later usage. Similarly, :ref:`JOBTMPL/Parameters` is used to
precompute the artifact's name.

.. code-block:: yaml

   jobs:
     ConfigParams:
       uses: pyTooling/Actions/.github/workflows/ExtractConfiguration.yml@r6
       with:
         package_name: myPackage

     Params:
       uses: pyTooling/Actions/.github/workflows/Parameters.yml@r6
       with:
         package_name: myPackage

     StaticTypeCheck:
       uses: pyTooling/Actions/.github/workflows/StaticTypeCheck.yml@r6
       needs:
         - ConfigParams
         - Params
       with:
         python_version: ${{ needs.Params.outputs.python_version }}
         junit_report:   ${{ needs.ConfigParams.outputs.typing_report_junit }}
         junit_artifact: ${{ fromJson(needs.Params.outputs.artifact_names).statictyping_junit }}


.. _JOBTMPL/StaticTypeCheck/Parameters:

Parameter Summary
*****************

.. rubric:: Goto :ref:`input parameters <JOBTMPL/StaticTypeCheck/Inputs>`

+---------------------------------------------------------------------+----------+----------------+------------------------------------------------------------------------------------------------------------------------------------------+
| Parameter Name                                                      | Required | Type           | Default                                                                                                                                  |
+=====================================================================+==========+================+==========================================================================================================================================+
| :ref:`JOBTMPL/StaticTypeCheck/Input/ubuntu_image_version`           | no       | string         | ``'24.04'``                                                                                                                              |
+---------------------------------------------------------------------+----------+----------------+------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`JOBTMPL/StaticTypeCheck/Input/python_version`                 | no       | string         | ``'3.13'``                                                                                                                               |
+---------------------------------------------------------------------+----------+----------------+------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`JOBTMPL/StaticTypeCheck/Input/requirements`                   | no       | string         | ``'-r tests/requirements.txt'``                                                                                                          |
+---------------------------------------------------------------------+----------+----------------+------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`JOBTMPL/StaticTypeCheck/Input/mypy_options`                   | no       | string         | ``''``                                                                                                                                   |
+---------------------------------------------------------------------+----------+----------------+------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`JOBTMPL/StaticTypeCheck/Input/cobertura_report`               | no       | string (JSON)  | :jsoncode:`{"fullpath": "report/typing/cobertura.xml", "directory": "report/typing", "filename": "cobertura.xml"}`                       |
+---------------------------------------------------------------------+----------+----------------+------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`JOBTMPL/StaticTypeCheck/Input/junit_report`                   | no       | string (JSON)  | :jsoncode:`{"fullpath": "report/typing/StaticTypingSummary.xml", "directory": "report/typing", "filename": "StaticTypingSummary.xml"}`   |
+---------------------------------------------------------------------+----------+----------------+------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`JOBTMPL/StaticTypeCheck/Input/html_report`                    | no       | string (JSON)  | :jsoncode:`{"directory": "report/typing/html"}`                                                                                          |
+---------------------------------------------------------------------+----------+----------------+------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`JOBTMPL/StaticTypeCheck/Input/cobertura_artifact`             | no       | string         | ``''``                                                                                                                                   |
+---------------------------------------------------------------------+----------+----------------+------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`JOBTMPL/StaticTypeCheck/Input/junit_artifact`                 | no       | string         | ``''``                                                                                                                                   |
+---------------------------------------------------------------------+----------+----------------+------------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`JOBTMPL/StaticTypeCheck/Input/html_artifact`                  | no       | string         | ``''``                                                                                                                                   |
+---------------------------------------------------------------------+----------+----------------+------------------------------------------------------------------------------------------------------------------------------------------+

.. rubric:: Goto :ref:`secrets <JOBTMPL/StaticTypeCheck/Secrets>`

This job template needs no secrets.

.. rubric:: Goto :ref:`output parameters <JOBTMPL/StaticTypeCheck/Outputs>`

This job template has no output parameters.


.. _JOBTMPL/StaticTypeCheck/Inputs:

Input Parameters
****************

.. _JOBTMPL/StaticTypeCheck/Input/ubuntu_image_version:

.. include:: ../_ubuntu_image_version.rst


.. _JOBTMPL/StaticTypeCheck/Input/python_version:

.. include:: ../_python_version.rst


.. _JOBTMPL/StaticTypeCheck/Input/requirements:

requirements
============

:Type:            string
:Required:        no
:Default Value:   ``'-r tests/requirements.txt'``
:Possible Values: Any valid list of parameters for ``pip install``. |br|
                  Either a requirements file can be referenced using ``'-r path/to/requirements.txt'``, or a list of
                  packages can be specified using a space separated list like ``'mypy lxml'``.
:Description:     Python dependencies to be installed through *pip*.


.. _JOBTMPL/StaticTypeCheck/Input/mypy_options:

mypy_options
============

:Type:            string
:Required:        no
:Default Value:   ``''``
:Possible Values: Any valid command line options for :term:`mypy`.
:Description:     Additional options handed over to mypy as ``mypy ${mypy_options}``.


.. _JOBTMPL/StaticTypeCheck/Input/cobertura_report:

cobertura_report
================

:Type:            string (JSON)
:Required:        no
:Default Value:
                  .. code-block:: json

                     { "directory": "reports/typing",
                       "filename":  "cobertura.xml",
                       "fullpath":  "reports/typing/cobertura.xml"
                     }
:Possible Values: Any valid JSON string containing a JSON object with fields:

                  :directory: Directory or sub-directory where the type checking report in Cobertura XML format will be
                              saved.
                  :filename:  Filename of the generated type checking report in Cobertura XML format. |br|
                              Currently, this filename is hardcoded within :term:`mypy` as :file:`cobertura.xml`.
                  :fullpath:  The concatenation of both previous fields using the ``/`` separator.
:Description:     Directory, filename and fullpath as JSON object where the type checking report in Cobertura XML format
                  will be saved. |br|
                  This path is configured in :file:`pyproject.toml` and can be extracted by
                  :ref:`JOBTMPL/ExtractConfiguration`.
:Example:
                  .. code-block:: yaml

                     ConfigParams:
                       uses: pyTooling/Actions/.github/workflows/ExtractConfiguration.yml@r6

                     UnitTesting:
                       uses: pyTooling/Actions/.github/workflows/StaticTypeCheck.yml@r6
                       needs:
                         - ConfigParams
                       with:
                         ...
                         cobertura_report: ${{ needs.ConfigParams.outputs.statictyping_cobertura }}


.. _JOBTMPL/StaticTypeCheck/Input/junit_report:

junit_report
============

:Type:            string (JSON)
:Required:        no
:Default Value:
                  .. code-block:: json

                     { "directory": "reports/typing",
                       "filename":  "StaticTypingSummary.xml",
                       "fullpath":  "reports/typing/StaticTypingSummary.xml"
                     }
:Possible Values: Any valid JSON string containing a JSON object with fields:

                  :directory: Directory or sub-directory where the type checking report in JUnit XML format will be
                              saved.
                  :filename:  Filename of the generated type checking report in JUnit XML format. |br|
                              Any valid file name for mypy's JUnit XML report.
                  :fullpath:  The concatenation of both previous fields using the ``/`` separator.
:Description:     Directory, filename and fullpath as JSON object where the type checking report in JUnit XML format
                  will be saved. |br|
                  This path is configured in :file:`pyproject.toml` and can be extracted by
                  :ref:`JOBTMPL/ExtractConfiguration`.
:Example:
                  .. code-block:: yaml

                     ConfigParams:
                       uses: pyTooling/Actions/.github/workflows/ExtractConfiguration.yml@r6

                     UnitTesting:
                       uses: pyTooling/Actions/.github/workflows/StaticTypeCheck.yml@r6
                       needs:
                         - ConfigParams
                       with:
                         ...
                         junit_report: ${{ needs.ConfigParams.outputs.statictyping_junit }}


.. _JOBTMPL/StaticTypeCheck/Input/html_report:

html_report
===========

:Type:            string (JSON)
:Required:        no
:Default Value:
                  .. code-block:: json

                     { "directory": "reports/typing/html"
                     }
:Possible Values: Any valid JSON string containing a JSON object with fields:

                  :directory: Directory or sub-directory where the type checking report in HTML format will be saved.
:Description:     Directory as JSON object where the type checking report in HTML format will be saved. |br|
                  This path is configured in :file:`pyproject.toml` and can be extracted by
                  :ref:`JOBTMPL/ExtractConfiguration`.
:Example:
                  .. code-block:: yaml

                     ConfigParams:
                       uses: pyTooling/Actions/.github/workflows/ExtractConfiguration.yml@r6

                     UnitTesting:
                       uses: pyTooling/Actions/.github/workflows/StaticTypeCheck.yml@r6
                       needs:
                         - ConfigParams
                       with:
                         ...
                         html_report: ${{ needs.ConfigParams.outputs.statictyping_html }}


.. _JOBTMPL/StaticTypeCheck/Input/cobertura_artifact:

cobertura_artifact
==================

:Type:            string
:Required:        no
:Default Value:   ``''``
:Possible Values: Any valid artifact name.
:Description:     Name of the artifact containing the Cobertura XML report.


.. _JOBTMPL/StaticTypeCheck/Input/junit_artifact:

junit_artifact
==============

:Type:            string
:Required:        no
:Default Value:   ``''``
:Possible Values: Any valid artifact name.
:Description:     Name of the artifact containing the JUnit XML report.


.. _JOBTMPL/StaticTypeCheck/Input/html_artifact:

html_artifact
=============

:Type:            string
:Required:        no
:Default Value:   ``''``
:Possible Values: Any valid artifact name.
:Description:     Name of the artifact containing the HTML report.


.. _JOBTMPL/StaticTypeCheck/Secrets:

Secrets
*******

This job template needs no secrets.


.. _JOBTMPL/StaticTypeCheck/Outputs:

Outputs
*******

This job template has no output parameters.


.. _JOBTMPL/StaticTypeCheck/Optimizations:

Optimizations
*************

This template offers no optimizations (reduced job runtime).

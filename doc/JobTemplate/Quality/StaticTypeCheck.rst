.. _JOBTMPL/StaticTypeCheck:

StaticTypeCheck
###############

This job template runs a static type check using `mypy <https://mypy-lang.org/>`__ and collects the results. These
results can be converted to a HTML report and uploaded as an artifact.

.. topic:: Features

   * Run static type check using mypy.

.. topic:: Behavior

   1. Checkout repository
   2. Setup Python and install dependencies
   3. Run type checking command(s).
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
             uses: pyTooling/Actions/.github/workflows/StaticTypeCheck.yml@r5
             with:
               html_report: 'htmlmpyp'
               artifact:    'TypeChecking'

   .. grid-item::
      :columns: 6

      .. code-block:: toml

         [tool.mypy]
         packages = ["myPackage"]
         strict = true
         pretty = true

         html_report = "htmlmpyp"


Complex Example
===============

To ease the handling of mypy parameters stored in :file:`pyproject.toml`, the :ref:`JOBTMPL/ExtractConfiguration` is
used to extract the set configuration parameters for later usage. Similarly, :ref:`JOBTMPL/Parameters` is used to
precompute the artifact's name.

.. code-block:: yaml

   jobs:
     ConfigParams:
       uses: pyTooling/Actions/.github/workflows/ExtractConfiguration.yml@r5
       with:
         package_name: myPackage

     Params:
       uses: pyTooling/Actions/.github/workflows/Parameters.yml@r5
       with:
         package_name: myPackage

     StaticTypeCheck:
       uses: pyTooling/Actions/.github/workflows/StaticTypeCheck.yml@r5
       needs:
         - ConfigParams
         - Params
       with:
         python_version: ${{ needs.Params.outputs.python_version }}
         report:         ${{ needs.ConfigParams.outputs.typing_report_html_directory }}
         artifact:       ${{ fromJson(needs.Params.outputs.artifact_names).statictyping_html }}


.. _JOBTMPL/StaticTypeCheck/Parameters:

Parameter Summary
*****************

.. rubric:: Goto :ref:`input parameters <JOBTMPL/StaticTypeCheck/Inputs>`

+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| Parameter Name                                                      | Required | Type     | Default                                                           |
+=====================================================================+==========+==========+===================================================================+
| :ref:`JOBTMPL/StaticTypeCheck/Input/ubuntu_image_version`           | no       | string   | ``'24.04'``                                                       |
+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/StaticTypeCheck/Input/python_version`                 | no       | string   | ``'3.13'``                                                        |
+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/StaticTypeCheck/Input/requirements`                   | no       | string   | ``'-r tests/requirements.txt'``                                   |
+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/StaticTypeCheck/Input/html_report`                    | no       | string   | ``'report/typing'``                                               |
+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/StaticTypeCheck/Input/junit_report`                   | no       | string   | ``'StaticTypingSummary.xml'``                                     |
+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/StaticTypeCheck/Input/html_artifact`                  | no       | string   | ``''``                                                            |
+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/StaticTypeCheck/Input/junit_artifact`                 | no       | string   | ``''``                                                            |
+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+

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


.. _JOBTMPL/StaticTypeCheck/Input/html_report:

html_report
===========

:Type:            string
:Required:        no
:Default Value:   ``'report/typing'``
:Possible Values: Any valid directory or subdirectory path.
:Description:     The directory containing the generated HTML report.


.. _JOBTMPL/StaticTypeCheck/Input/junit_report:

junit_report
============

:Type:            string
:Required:        no
:Default Value:   ``'StaticTypingSummary.xml'``
:Possible Values: Any valid file name for mypy's JUnit XML report.
:Description:     File name for the JUnit XML file.


.. _JOBTMPL/StaticTypeCheck/Input/html_artifact:

html_artifact
=============

:Type:            string
:Required:        no
:Default Value:   ``''``
:Possible Values: Any valid artifact name.
:Description:     Name of the artifact containing the HTML report.


.. _JOBTMPL/StaticTypeCheck/Input/junit_artifact:

junit_artifact
==============

:Type:            string
:Required:        no
:Default Value:   ``''``
:Possible Values: Any valid artifact name.
:Description:     Name of the artifact containing the JUnit XML report.


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

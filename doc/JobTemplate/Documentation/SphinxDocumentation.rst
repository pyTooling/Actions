.. _JOBTMPL/SphinxDocumentation:

SphinxDocumentation
###################

The ``SphinxDocumentation`` job template compiles the ReStructured Text documentation using Sphinx to an HTML website
and a LaTeX documentation. This LaTeX document can be translated using e.g. MikTeX to a PDF file.

.. topic:: Features

   * Build documentation using Sphinx as HTML and upload as artifact. |br|
     (see :ref:`JOBTMPL/SphinxDocumentation/Input/html_artifact`).
   * Build documentation using Sphinx as LaTeX and upload as artifact. |br|
     (see :ref:`JOBTMPL/SphinxDocumentation/Input/latex_artifact`).

     * Workaround `sphinx-doc/sphinx#13189 <https://github.com/sphinx-doc/sphinx/issues/13189>`__
     * Workaround `sphinx-doc/sphinx#13190 <https://github.com/sphinx-doc/sphinx/issues/13190>`__

   * Optionally: download code coverage artifact (JSON format) given by :ref:`JOBTMPL/SphinxDocumentation/Input/coverage_json_artifact`.
   * Optionally: download unit test report artifact (XML format) given by :ref:`JOBTMPL/SphinxDocumentation/Input/unittest_xml_artifact`.

.. topic:: Behavior

   1. Checkout repository.
   2. Install system dependencies.
   3. Setup Python environment and install Python dependencies.
   4. Download optional artifacts for integration of further reports into the documentation.
   5. Build the HTML documentation using Sphinx.
   6. Build the LaTeX documentation using Sphinx.

      1. Apply LaTeX workaround I.
      2. Apply LaTeX workaround II.

   7. Upload the HTML and LaTeX artifacts.

.. topic:: Job Execution

   .. image:: ../../_static/pyTooling-Actions-SphinxDocumentation.png
      :width: 600px

.. topic:: Dependencies

   * :gh:`actions/checkout`
   * :gh:`actions/setup-python`
   * :gh:`pyTooling/download-artifact`

     * :gh:`actions/download-artifact`

   * :gh:`pyTooling/upload-artifact`

     * :gh:`actions/upload-artifact`

   * apt

     * `graphviz <https://graphviz.org/>`__

   * pip

     * :pypi:`wheel`
     * Python packages specified via :ref:`JOBTMPL/SphinxDocumentation/Input/requirements` parameter.


.. _JOBTMPL/SphinxDocumentation/Instantiation:

Instantiation
*************

.. code-block:: yaml

   name: Pipeline

   on:
     push:
     workflow_dispatch:

   jobs:
     UnitTestingParams:
       uses: pyTooling/Actions/.github/workflows/Parameters.yml@r5
       with:
         package_name: myPackage

     Documentation:
       uses: pyTooling/Actions/.github/workflows/SphinxDocumentation.yml@r5
       needs:
         - UnitTestingParams
       with:
         python_version: ${{ needs.UnitTestingParams.outputs.python_version }}
         html_artifact:  ${{ fromJson(needs.UnitTestingParams.outputs.artifact_names).documentation_html }}
         latex_artifact: ${{ fromJson(needs.UnitTestingParams.outputs.artifact_names).documentation_latex }}


.. _JOBTMPL/SphinxDocumentation/Parameters:

Parameter Summary
*****************

.. rubric:: Goto :ref:`input parameters <JOBTMPL/SphinxDocumentation/Inputs>`

+-------------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| Parameter Name                                                          | Required | Type     | Default                                                           |
+=========================================================================+==========+==========+===================================================================+
| :ref:`JOBTMPL/SphinxDocumentation/Input/ubuntu_image_version`           | no       | string   | ``'24.04'``                                                       |
+-------------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/SphinxDocumentation/Input/python_version`                 | no       | string   | ``'3.13'``                                                        |
+-------------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/SphinxDocumentation/Input/requirements`                   | no       | string   | ``'-r doc/requirements.txt'``                                     |
+-------------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/SphinxDocumentation/Input/doc_directory`                  | no       | string   | ``'doc'``                                                         |
+-------------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/SphinxDocumentation/Input/coverage_report_json_directory` | no       | string   | ``''``                                                            |
+-------------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/SphinxDocumentation/Input/coverage_json_artifact`         | no       | string   | ``''``                                                            |
+-------------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/SphinxDocumentation/Input/unittest_xml_artifact`          | no       | string   | ``''``                                                            |
+-------------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/SphinxDocumentation/Input/unittest_xml_directory`         | no       | string   | ``'report/unit'``                                                 |
+-------------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/SphinxDocumentation/Input/html_artifact`                  | no       | string   | ``''``                                                            |
+-------------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/SphinxDocumentation/Input/latex_artifact`                 | no       | string   | ``''``                                                            |
+-------------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+

.. rubric:: Goto :ref:`secrets <JOBTMPL/SphinxDocumentation/Secrets>`

This job template needs no secrets.

.. rubric:: Goto :ref:`output parameters <JOBTMPL/SphinxDocumentation/Outputs>`

This job template has no output parameters.


.. _JOBTMPL/SphinxDocumentation/Inputs:

Input Parameters
****************

.. _JOBTMPL/SphinxDocumentation/Input/ubuntu_image_version:

.. include:: ../_ubuntu_image_version.rst


.. _JOBTMPL/SphinxDocumentation/Input/python_version:

.. include:: ../_python_version.rst


.. _JOBTMPL/SphinxDocumentation/Input/requirements:

requirements
============

:Type:            string
:Required:        no
:Default Value:   ``'-r doc/requirements.txt'``
:Possible Values: Any valid list of parameters for ``pip install``. |br|
                  Either a requirements file can be referenced using ``'-r path/to/requirements.txt'``, or a list of
                  packages can be specified using a space separated list like ``'Sphinx sphinx_rtd_theme sphinxcontrib-mermaid'``.
:Description:     Python dependencies to be installed through *pip*.


.. _JOBTMPL/SphinxDocumentation/Input/doc_directory:

doc_directory
=============

:Type:            string
:Required:        no
:Default Value:   ``'doc'``
:Possible Values: Any valid directory or sub-directory.
:Description:     Directory where the Sphinx documentation is located.

                  .. attention::

                     When this parameter gets changed, :ref:`JOBTMPL/SphinxDocumentation/Input/requirements` needs to be
                     adjusted as well.


.. _JOBTMPL/SphinxDocumentation/Input/coverage_report_json_directory:

coverage_report_json_directory
==============================

:Type:            string
:Required:        no
:Default Value:   ``''``
:Possible Values: Any valid directory or sub-directory.
:Description:     tbd


.. _JOBTMPL/SphinxDocumentation/Input/coverage_json_artifact:

coverage_json_artifact
======================

:Type:            string
:Required:        no
:Default Value:   ``''``
:Possible Values: Any valid artifact name.
:Description:     Name of the artifact containing the code coverage report in JSON format.


.. _JOBTMPL/SphinxDocumentation/Input/unittest_xml_artifact:

unittest_xml_artifact
=====================

:Type:            string
:Required:        no
:Default Value:   ``''``
:Possible Values: Any valid artifact name.
:Description:     Name of the artifact containing the unittest XML report summary in XML format.


.. _JOBTMPL/SphinxDocumentation/Input/unittest_xml_directory:

unittest_xml_directory
======================

:Type:            string
:Required:        no
:Default Value:   ``'report/unit'``
:Possible Values: Any valid directory or sub-directory.
:Description:     Directory where unittest XML artifact will be extracted.


.. _JOBTMPL/SphinxDocumentation/Input/html_artifact:

html_artifact
=============

:Type:            string
:Required:        no
:Default Value:   ``''``
:Possible Values: Any valid artifact name.
:Description:     Name of the artifact containing the generated HTML website.
:Optimization:
                  .. hint::

                     If this parameter is empty, no HTML website will be generated and no artifact will be uploaded.


.. _JOBTMPL/SphinxDocumentation/Input/latex_artifact:

latex_artifact
==============

:Type:            string
:Required:        no
:Default Value:   ``''``
:Possible Values: Any valid artifact name.
:Description:     Name of the artifact containing the generated LaTeX document and resource files (e.g., images).
:Optimization:
                  .. hint::

                     If this parameter is empty, no LaTeX document will be generated and no artifact will be uploaded.


.. _JOBTMPL/SphinxDocumentation/Secrets:

Secrets
*******

This job template needs no secrets.


.. _JOBTMPL/SphinxDocumentation/Outputs:

Outputs
*******

This job template has no output parameters.


.. _JOBTMPL/SphinxDocumentation/Optimizations:

Optimizations
*************

The following optimizations can be used to reduce the template's runtime.

Disable HTML website generation and HTML artifact
  If parameter :ref:`JOBTMPL/SphinxDocumentation/Input/html_artifact` is empty, no HTML website will be generated and
  uploaded.
Disable LaTeX document generation and LaTeX artifact
  If parameter :ref:`JOBTMPL/SphinxDocumentation/Input/latex_artifact` is empty, no LaTeX document will be generated and
  uploaded.

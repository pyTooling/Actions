.. _JOBTMPL/LaTeXDocumentation:

LaTeXDocumentation
##################

The ``LaTeXDocumentation`` job template downloads an artifact containing a LaTeX document and translates to a PDF file
using MikTeX.

The translation process uses ``latexmk`` for handling multiple passes. The default LaTeX processor is ``xelatex``, but
can be switched by a parameter.

.. topic:: Features

   * Translate a LaTeX document to PDF.

.. topic:: Behavior

   1. Download the LaTeX artifact.
   2. Build the PDF using ``latexmk``.
   3. Upload the generated PDF as an artifact.

.. topic:: Dependencies

   * :gh:`pyTooling/download-artifact`

     * :gh:`actions/download-artifact`

   * :gh:`pyTooling/upload-artifact`

     * :gh:`actions/upload-artifact`

   * :gh:`addnab/docker-run-action`

     * :dockerhub:`pytooling/miktex <pytooling/miktex:sphinx>`


.. _JOBTMPL/LaTeXDocumentation/Instantiation:

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

     PDFDocumentation:
       uses: pyTooling/Actions/.github/workflows/LaTeXDocumentation.yml@r5
       needs:
         - UnitTestingParams
         - Documentation
       with:
         document: pyEDAA.ProjectModel
         latex_artifact: ${{ fromJson(needs.UnitTestingParams.outputs.artifact_names).documentation_latex }}
         pdf_artifact:   ${{ fromJson(needs.UnitTestingParams.outputs.artifact_names).documentation_pdf }}


.. _JOBTMPL/LaTeXDocumentation/Parameters:

Parameter Summary
*****************

.. rubric:: Goto :ref:`input parameters <JOBTMPL/LaTeXDocumentation/Inputs>`

+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| Parameter Name                                                      | Required | Type     | Default                                                           |
+=====================================================================+==========+==========+===================================================================+
| :ref:`JOBTMPL/LaTeXDocumentation/Input/ubuntu_image_version`        | no       | string   | ``'24.04'``                                                       |
+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/LaTeXDocumentation/Input/latex_artifact`              | yes      | string   | — — — —                                                           |
+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/LaTeXDocumentation/Input/document`                    | yes      | string   | — — — —                                                           |
+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/LaTeXDocumentation/Input/processor`                   | no       | string   | ``'xelatex'``                                                     |
+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+
| :ref:`JOBTMPL/LaTeXDocumentation/Input/pdf_artifact`                | no       | string   | ``''``                                                            |
+---------------------------------------------------------------------+----------+----------+-------------------------------------------------------------------+

.. rubric:: Goto :ref:`secrets <JOBTMPL/LaTeXDocumentation/Secrets>`

This job template needs no secrets.

.. rubric:: Goto :ref:`output parameters <JOBTMPL/LaTeXDocumentation/Outputs>`

This job template has no output parameters.


.. _JOBTMPL/LaTeXDocumentation/Inputs:

Input Parameters
****************

.. _JOBTMPL/LaTeXDocumentation/Input/ubuntu_image_version:

.. include:: ../_ubuntu_image_version.rst


.. _JOBTMPL/LaTeXDocumentation/Input/latex_artifact:

latex_artifact
==============

:Type:            string
:Required:        yes
:Default Value:   — — — —
:Possible Values: Any valid artifact name.
:Description:     Name of the artifact containing the LaTeX document to translate.


.. _JOBTMPL/LaTeXDocumentation/Input/document:

document
========

:Type:            string
:Required:        yes
:Default Value:   — — — —
:Possible Values: Any valid document name.
:Description:     Name of the LaTeX document


.. _JOBTMPL/LaTeXDocumentation/Input/processor:

processor
=========

:Type:            string
:Required:        no
:Default Value:   ``'xelatex'``
:Possible Values: Any supported LaTeX processor supported by MikTeX and ``latexmk``.
:Description:     Name of the used LaTeX processor.


.. _JOBTMPL/LaTeXDocumentation/Input/pdf_artifact:

pdf_artifact
============

:Type:            string
:Required:        no
:Default Value:   ``''``
:Possible Values: Any valid artifact name.
:Description:     Name of the artifact containing the generated PDF document.
:Optimization:
                  .. hint::

                     If this parameter is empty, no PDF file will be generated and no artifact will be uploaded.

.. _JOBTMPL/LaTeXDocumentation/Secrets:

Secrets
*******

This job template needs no secrets.


.. _JOBTMPL/LaTeXDocumentation/Outputs:

Outputs
*******

This job template has no output parameters.


.. _JOBTMPL/LaTeXDocumentation/Optimizations:

Optimizations
*************

The following optimizations can be used to reduce the template's runtime.

Disable PDF generation and PDF artifact
  If parameter :ref:`JOBTMPL/LaTeXDocumentation/Input/pdf_artifact` is empty, no PDF will be generated and uploaded.

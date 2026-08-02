.. _JOBTMPL/LaTeXDocumentation:
.. index::
   single: MikTeX; LaTeXDocumentation Template
   single: GitHub Action Reusable Workflow; LaTeXDocumentation Template

LaTeXDocumentation
##################

The ``LaTeXDocumentation`` job template downloads an artifact containing a LaTeX document and translates to a PDF file
using MikTeX.

The translation process uses ``latexmk`` for handling multiple passes. The default LaTeX processor is ``lualatex``, but
can be switched by a parameter.

.. topic:: Features

   * Translate a LaTeX document to PDF.

.. topic:: Behavior

   1. Download the LaTeX artifact.
   2. Optionally update the MiKTeX packages in the container - see
      :ref:`JOBTMPL/LaTeXDocumentation/Input/update`.
   3. Build the PDF using ``latexmk`` inside the MiKTeX container.
   4. Upload the generated PDF as an artifact.

   Steps 3 and 4 are skipped if :ref:`JOBTMPL/LaTeXDocumentation/Input/pdf_artifact` is empty.

.. topic:: Dependencies

   * :gh:`pyTooling/download-artifact`

     * :gh:`actions/download-artifact`

   * :gh:`pyTooling/upload-artifact`

     * :gh:`actions/upload-artifact`

   * The job runs inside the MiKTeX container given by
     :ref:`JOBTMPL/LaTeXDocumentation/Input/miktex_image`, which provides ``latexmk``.

.. _JOBTMPL/LaTeXDocumentation/Instantiation:

Instantiation
*************

.. code-block:: yaml

   jobs:
     UnitTestingParams:
       uses: pyTooling/Actions/.github/workflows/Parameters.yml@r7
       with:
         package_name: myPackage

     Documentation:
       uses: pyTooling/Actions/.github/workflows/SphinxDocumentation.yml@r7
       needs:
         - UnitTestingParams
       with:
         python_version: ${{ needs.UnitTestingParams.outputs.python_version }}
         html_artifact:  ${{ fromJson(needs.UnitTestingParams.outputs.artifact_names).documentation_html }}
         latex_artifact: ${{ fromJson(needs.UnitTestingParams.outputs.artifact_names).documentation_latex }}

     PDFDocumentation:
       uses: pyTooling/Actions/.github/workflows/LaTeXDocumentation.yml@r7
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

+--------------------------------------------------------------+----------+--------+-------------------------------+
| Parameter Name                                               | Required | Type   | Default                       |
+==============================================================+==========+========+===============================+
| :ref:`JOBTMPL/LaTeXDocumentation/Input/ubuntu_image_version` | no       | string | ``'26.04'``                   |
+--------------------------------------------------------------+----------+--------+-------------------------------+
| :ref:`JOBTMPL/LaTeXDocumentation/Input/latex_artifact`       | yes      | string | — — — —                       |
+--------------------------------------------------------------+----------+--------+-------------------------------+
| :ref:`JOBTMPL/LaTeXDocumentation/Input/document`             | yes      | string | — — — —                       |
+--------------------------------------------------------------+----------+--------+-------------------------------+
| :ref:`JOBTMPL/LaTeXDocumentation/Input/processor`            | no       | string | ``'lualatex'``                |
+--------------------------------------------------------------+----------+--------+-------------------------------+
| :ref:`JOBTMPL/LaTeXDocumentation/Input/pdf_artifact`         | no       | string | ``''``                        |
+--------------------------------------------------------------+----------+--------+-------------------------------+
| :ref:`JOBTMPL/LaTeXDocumentation/Input/miktex_image`         | no       | string | ``'pytooling/miktex:sphinx'`` |
+--------------------------------------------------------------+----------+--------+-------------------------------+
| :ref:`JOBTMPL/LaTeXDocumentation/Input/update`               | no       | string | ``'false'``                   |
+--------------------------------------------------------------+----------+--------+-------------------------------+
| :ref:`JOBTMPL/LaTeXDocumentation/Input/halt-on-error`        | no       | string | ``'true'``                    |
+--------------------------------------------------------------+----------+--------+-------------------------------+
| :ref:`JOBTMPL/LaTeXDocumentation/Input/can-fail`             | no       | string | ``'false'``                   |
+--------------------------------------------------------------+----------+--------+-------------------------------+

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
:Default Value:   ``'lualatex'``
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

.. _JOBTMPL/LaTeXDocumentation/Input/miktex_image:

miktex_image
============

:Type:            string
:Required:        no
:Default Value:   ``'pytooling/miktex:sphinx'``
:Possible Values: Any Docker image providing a MiKTeX installation with ``latexmk``.
:Description:     Docker image used to translate the LaTeX sources to PDF. |br|
                  The default image ships the LaTeX packages Sphinx emits.

.. _JOBTMPL/LaTeXDocumentation/Input/update:

update
======

:Type:            string
:Required:        no
:Default Value:   ``'false'``
:Possible Values: ``'true'`` - update the MiKTeX packages inside the container before building.
                  ``'false'`` - use the packages shipped with the image.
:Description:     Update MiKTeX packages before the document is built. |br|
                  Updating costs runtime on every run, so this is meant as an escape hatch when the image lags behind
                  a LaTeX package Sphinx needs.

.. _JOBTMPL/LaTeXDocumentation/Input/halt-on-error:

halt-on-error
=============

:Type:            string
:Required:        no
:Default Value:   ``'true'``
:Possible Values: ``'true'`` - stop at the first LaTeX error.
                  ``'false'`` - continue as far as possible.
:Description:     Pass ``-halt-on-error`` to ``latexmk``. |br|
                  With ``'false'`` LaTeX keeps going, and a PDF may still be produced from a document with unresolved
                  references.

.. _JOBTMPL/LaTeXDocumentation/Input/can-fail:

can-fail
========

:Type:            string
:Required:        no
:Default Value:   ``'false'``
:Possible Values: ``'true'`` - a failed translation does not fail the pipeline.
                  ``'false'`` - a failed translation fails the job.
:Description:     Sets ``continue-on-error`` on the job. |br|
                  PDF generation is the most fragile documentation step, so a pipeline that only needs HTML can
                  tolerate its failure.

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
